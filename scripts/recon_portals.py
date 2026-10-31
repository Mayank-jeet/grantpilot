import asyncio,json,re,sys,time
from pathlib import Path
from playwright.async_api import async_playwright

OUT=Path(__file__).resolve().parent.parent/"docs"/"recon-out"
TARGETS=[
 ("myscheme-home","https://www.myscheme.gov.in/",[]),
 ("myscheme-search","https://www.myscheme.gov.in/search",[]),
 ("ssp-home","https://scholarship.odisha.gov.in/",["Check Eligibility","Know Your Status"]),
]
HINTS={"captcha":r"captcha","otp":r"\botp\b","login":r"log\s?in|sign\s?in","aadhaar":r"aadhaar|aadhar"}

async def probe(page,label,t0):
 await page.wait_for_timeout(2500)
 html=await page.content()
 low=html.lower()
 shot=OUT/f"{label}.png"
 await page.screenshot(path=str(shot),full_page=False)
 return {
  "label":label,"url":page.url,"title":await page.title(),
  "load_s":round(time.time()-t0,1),
  "iframes":len(page.frames)-1,
  "inputs":await page.locator("input:visible").count(),
  "password_inputs":await page.locator("input[type=password]:visible").count(),
  "buttons":await page.locator("button:visible,a:visible").count(),
  "hints":{k:bool(re.search(v,low)) for k,v in HINTS.items()},
  "screenshot":shot.name,
 }

async def run(headless):
 OUT.mkdir(parents=True,exist_ok=True)
 report=[]
 async with async_playwright() as p:
  browser=await p.chromium.launch(headless=headless)
  for name,url,clicks in TARGETS:
   ctx=await browser.new_context(viewport={"width":1280,"height":800})
   popups=[]
   ctx.on("page",lambda pg:popups.append(pg))
   page=await ctx.new_page()
   t0=time.time()
   try:
    resp=await page.goto(url,timeout=45000,wait_until="domcontentloaded")
    r=await probe(page,name,t0)
    r["http_status"]=resp.status if resp else None
    report.append(r)
    for text in clicks:
     t1=time.time()
     try:
      await page.goto(url,timeout=45000,wait_until="domcontentloaded")
      before=len(popups)
      await page.get_by_text(text,exact=False).first.click(timeout=8000)
      await page.wait_for_timeout(1500)
      newtab=len(popups)>before
      tgt=popups[-1] if newtab else page
      r2=await probe(tgt,f"{name}-{text.replace(' ','-').lower()}",t1)
      r2["clicked"]=text
      r2["opened_new_tab"]=newtab
      report.append(r2)
     except Exception as e:
      report.append({"label":f"{name}:{text}","error":str(e)[:200]})
   except Exception as e:
    report.append({"label":name,"url":url,"error":str(e)[:200]})
   await ctx.close()
  await browser.close()
 (OUT/"report.json").write_text(json.dumps(report,indent=1),encoding="utf-8")
 for r in report:
  print(json.dumps(r,ensure_ascii=False))
 print("\nSaved to",OUT)

if __name__=="__main__":
 asyncio.run(run(headless="--headless" in sys.argv))
