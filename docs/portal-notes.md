# Portal notes (A1 recon)

Source: `python scripts/recon_portals.py` run on 2026-10-31 plus screenshots. Re-check before sleeping and before the demo: portals change. Raw output in `docs/recon-out/` (local only, not committed).

Legend: [auto] seen by the script, [manual] still to confirm by hand.

## Summary table

| Flow | Login needed | OTP | CAPTCHA | Iframes / popups | Loads from our network | Automatable |
|---|---|---|---|---|---|---|
| myScheme home | No (Sign In button exists, optional) [auto] | No [auto] | None seen [auto] | 1 iframe (likely the chatbot widget) [auto] | Yes, HTTP 200, ~4s [auto] | Yes |
| myScheme search + filters | No [auto] | No [auto] | None seen [auto] | 1 iframe [auto] | Yes, HTTP 200, ~3s [auto] | Yes |
| myScheme scheme detail | [manual] | [manual] | [manual] | [manual] | [manual] | [manual] |
| SSP Odisha home | No for public pages; Login button top-right [auto] | Word "OTP" appears in page source, so it is used somewhere (login or status) [auto] | None seen on home [auto] | 0 iframes [auto] | Yes, HTTP 200, redirects to /home, ~4s [auto] | Yes |
| SSP: Check Eligibility | [manual] | [manual] | [manual] | [manual] | [manual] | [manual] |
| SSP: Know Your Status | [manual] | [manual] | [manual] | [manual] | [manual] | [manual] |

## myScheme

- Search URL: `https://www.myscheme.gov.in/search` (returns scheme cards with title, ministry, summary, tags).
- Left filter panel: many checkboxes (minority, differently abled, DBT scheme, below poverty line, student, etc., with counts) and dropdown selects (disability percentage, occupation, ...). About 51 visible inputs.
- Header: Sign In button, language switch, theme toggle. A floating chatbot button bottom-right (probably the iframe). The agent should ignore it.
- Selector notes: [manual] check scheme detail page sections (Details, Benefits, Eligibility, Documents Required) and whether the cards have stable links.

## SSP Odisha

- `https://scholarship.odisha.gov.in/` redirects to `/home`. Same tab for everything the script clicked, no new tabs.
- Header menu: About, Schemes, How to Apply, FAQs, Contact Us, search icon, Login.
- Hero button text is **"Check Scholarship Eligibility"** (not "Check Eligibility"). The script's click on "Check Eligibility" and "Know Your Status" did not leave the home page, so the screenshots show no real flow yet.
- [manual] Find where "Know Your Status" lives (menu, footer, or after Login) and what it asks for (application number, mobile, OTP?).
- [manual] Click "Check Scholarship Eligibility" by hand and record the fields and any OTP or CAPTCHA.

## Decision (provisional)

- Primary flow: myScheme search and scheme page reading (public, no login, loads fine).
- Backup / second flow: SSP public pages (Check Scholarship Eligibility, Know Your Status) with OTP handoff, pending the manual walkthrough.
- Who has a genuine SSP account (for delegated login): [ask the team]
