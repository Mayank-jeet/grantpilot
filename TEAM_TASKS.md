# GrantPilot: TEAM TASKS (read this first)

Repo: https://github.com/Mayank-jeet/grantpilot

GrantPilot is an AI agent that finds scholarships for a student and fills the application on real government portals. It pauses for OTP/CAPTCHA, never bypasses them, and saves the receipt.

Build cutoff: **tomorrow 12 PM**. After that, only bug fixes and demo prep (demo rehearsal, video, deck).

---

## STEP 0: Do this now (10 minutes, everyone)

1. Accept the GitHub collaborator invite (check email / GitHub notifications).
2. Clone the repo in VS Code: `Ctrl+Shift+P` -> **Git: Clone** -> `https://github.com/Mayank-jeet/grantpilot.git` -> Open.
3. Set your name once:
   ```
   git config user.name "Your Name"
   git config user.email "your-github-email"
   ```
4. Write "done" in the group chat.

---

## WHO DOES WHAT

| Person | Role | You own these folders |
|---|---|---|
| **A** | Agent engineer | `backend/app/agent/`, `backend/app/portals/` |
| **B** | AI / data engineer | `backend/app/intake/`, `backend/app/discovery/`, `backend/app/db/` |
| **C** | Frontend + demo | `frontend/`, `backend/app/api/`, `docs/` |

Stay inside your own folders. If you must edit a shared file (`main.py`, `requirements.txt`, `package.json`, `.env.example`), tell the chat first and commit it quickly.

---

## FIRST TASKS (next 1-2 hours)

### Person A: Agent
- [ ] Open myScheme (myscheme.gov.in) and the public pages of the Odisha State Scholarship Portal (scholarship.odisha.gov.in) by hand. Write down: is login needed, is there OTP/CAPTCHA, are there iframes or popups, does it load from our network.
- [ ] Set up Playwright (Python) and a script that opens myScheme, searches for a scheme and reads the page.
- [ ] Start the loop: observe the page -> ask the LLM for ONE action -> run it -> check the result.

### Person B: AI / data
- [ ] Create a Supabase project. Tables: `profiles`, `documents`, `runs`, `steps`, `receipts`, `sources`.
- [ ] Share the Supabase URL and key privately in chat (never in the repo).
- [ ] Test sending a document photo to the vision model and getting structured fields back (name, DOB, income, category).

### Person C: Frontend
- [ ] Create the React app in `frontend/` (Vite + TypeScript + Tailwind).
- [ ] Create the FastAPI skeleton in `backend/app/main.py` with one WebSocket that streams a test message.
- [ ] Show that message live in the React UI.

---

## PLAN FOR THE NEXT 24 HOURS

| Hours | Goal |
|---|---|
| 0-2 | Check portals, set up repo, keys, Supabase. Pick final flow. |
| 2-4 | Skeleton: backend, UI, DB, a live browser screenshot in the UI. |
| 4-7 | Agent loop completes a real myScheme search end to end. |
| 7-10 | Error recovery, retries, OTP/CAPTCHA/login handoff to the user. |
| 10-12 | Document upload, extraction and validation. |
| 12-14 | Scheme discovery with citations. Checkpoint and push. |
| 14-21 | **SLEEP.** Do not skip it. |
| 21-22 | Fix the top bugs, run the full flow 3 times. |
| 22-23 | Edge cases (portal down, wrong input, missing document), receipt capture. |
| 23-24 | Deploy, finish README with architecture diagram, push. |
| After | Demo rehearsal, 2-3 min video, 5-7 slide deck, submission. |

If we fall behind, cut in this order: extra portals -> UI polish -> extra validators -> vector search. **Never cut:** browser loop, error recovery, OTP/CAPTCHA handoff, receipt capture, deployment.

---

## HOW TO USE GIT (every task)

```
git checkout main
git pull
git checkout -b agent/short-task-name      (prefix: agent/ or data/ or ui/)

... work ...

git add .
git commit -m "agent: what you did"
git pull origin main
git push -u origin agent/short-task-name
```

Then open a Pull Request on GitHub and merge it into `main`. Message the chat when you merge.

- Commit small and often. Merge to `main` at least every 2-3 hours.
- Always `git pull` before you start and before you push.
- Never use `git push -f`.
- If you get a merge conflict: open the file, keep the right code, delete the `<<<<<<<`, `=======`, `>>>>>>>` lines, then `git add <file>` and `git commit`. Ask for help if unsure.

---

## RULES (breaking these can disqualify us)

1. **No dummy data.** No hardcoded JSON, fake receipts or placeholder numbers. Data must come from live portals/APIs, official datasets, or real user input saved in the database.
2. **Never commit secrets or personal data:** `.env`, API keys, Aadhaar, real documents, `node_modules`, `venv`. Share keys privately in chat. If a key is pushed by mistake, rotate it immediately.
3. **Never bypass CAPTCHA or OTP.** The agent stops and asks the user.
4. **Do not submit false applications.** Use genuine details only. Stop at the preview/review page unless the account holder really wants to submit.
5. **The demo must be live.** No pre-recorded videos or mockups shown as the working app.
6. **All core logic must be written during the hackathon.** Commit your own code regularly so the history shows it.
7. **Everyone must be able to explain the whole project** (architecture, data flow, agent loop, RAG) in judging.
8. **Keep `main` working.** Do not merge anything that breaks the app. If `main` breaks, tell the chat immediately.

---

## COMMUNICATION

- Post in the chat when you: finish a task, merge to `main`, need to edit a shared file, or are blocked for more than 20 minutes.
- Ask for help early. A 5 minute question saves an hour.
