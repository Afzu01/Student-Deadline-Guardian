# Student Deadline Guardian

A practical student productivity app that helps track deadlines, urgency, and weekly planning.

## Portfolio pitch

An operations-style planning tool for students that turns scattered due dates into clear, prioritized weekly action.

## Why this helps real users

- Prevents missed deadlines with urgency visibility
- Keeps high-priority work visible
- Generates digest-style checklist for weekly planning

## Features

- Deadline dashboard with days-left logic
- Priority summary cards
- Add-new deadline form
- Weekly digest endpoint
- 3D-style modern interface at `/ui`

## Architecture

- FastAPI backend with CSV-backed deadline data
- Priority scoring from due date + impact fields
- Frontend dashboard for quick planning and updates

## Run

```powershell
cd D:\Code\python\student-deadline-guardian
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8100
```

- UI: http://127.0.0.1:8100/ui
- Docs: http://127.0.0.1:8100/docs

## API quick test

```powershell
Invoke-RestMethod -Method GET -Uri "http://127.0.0.1:8100/deadlines/summary"
```

## Recruiter demo points

1. Open `/ui` and show summary cards
2. Add a new deadline and show instant dashboard update
3. Show digest output and explain weekly planning impact

## Dataset

- 20 realistic academic + admin + career deadlines in `data/deadlines.csv`

## Screenshots / Demo GIF

- Add your UI screenshot here after first run
- Optional: add a 10-15 second GIF of adding a deadline and refreshing summary
