# GrantPilot

**An AI agent that finds scholarships for a student and fills in the application on real government portals. It pauses for OTP/CAPTCHA and saves the receipt.**

Hackathon track: Autonomous Public Service & Bureaucracy Execution Agent.

---

## What it does

1. **Reads the student's documents** (marksheet, income and caste certificates) with a vision model and validates them (name mismatch, missing fields, expiry).
2. **Finds matching scholarships** from live official sources (myScheme.gov.in, Odisha State Scholarship Portal) with source citations.
3. **Drives the real portal** with a browser agent (Playwright + LLM): fills forms, handles popups and errors, retries and re-plans.
4. **Hands off to the human** for login, OTP and CAPTCHA. It never bypasses them.
5. **Saves the receipt** (screenshot, PDF, reference number or status) to the database.

## Tech stack

| Layer | Choice |
|---|---|
| Backend | Python, FastAPI, WebSockets |
| Browser agent | Playwright + DOM/accessibility-tree extraction |
| LLM | Claude API (tool use, vision) |
| Discovery / RAG | Live myScheme pages, embeddings, citations |
| Database | Supabase (Postgres + storage) |
| Frontend | React (Vite + TypeScript), Tailwind CSS |

## Project structure

```
grantpilot/
|-- backend/    # FastAPI app: api, agent, portals, intake, discovery, receipts, db
|-- frontend/   # React + Vite + TypeScript
|-- docs/       # architecture, demo script, fallback plan, compliance
`-- scripts/    # smoke test, portal checker
```

## Team and ownership

Stay in your own folders to avoid merge conflicts.

| Person | Owns |
|---|---|
| A: Agent | `backend/app/agent/`, `backend/app/portals/` |
| B: AI / Data | `backend/app/intake/`, `backend/app/discovery/`, `backend/app/db/` |
| C: Frontend | `frontend/`, `backend/app/api/`, `docs/` |

Tell the team in chat before editing shared files: `main.py`, `requirements.txt`, `package.json`, `.env.example`.

## Git workflow

```bash
git checkout main && git pull          # start from the latest main
git checkout -b agent/short-task-name  # prefixes: agent/ data/ ui/
git add . && git commit -m "agent: add observe-plan-act loop"
git pull origin main                   # before pushing
git push -u origin agent/short-task-name
```

Open a Pull Request into `main` and tell the team when you merge. Merge to `main` at least every 2-3 hours. Never use `git push -f`.

## Rules

- **No dummy data.** No hardcoded JSON or fake numbers. Everything comes from live portals/APIs or real user input stored in the database.
- **Never commit** `.env`, API keys, `node_modules`, `venv`, or real personal documents (Aadhaar etc.).
- **Consent first.** The student logs in and clears OTP/CAPTCHA themselves. No passwords or OTPs are stored.
- **Stop before a false submission.** Use genuine details only; stop at the preview/review page unless the account holder really wants to submit.
- Every team member must be able to explain the whole codebase during judging.

## Setup

Setup instructions will be added here as the backend and frontend are built.

## Roadmap

- DigiLocker / API Setu integration for verified documents (needs partner registration)
- More states and portals
- Application status tracking and deadline reminders
