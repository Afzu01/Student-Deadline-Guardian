from datetime import date, datetime
from pathlib import Path

import pandas as pd
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "deadlines.csv"
UI_FILE = Path(__file__).resolve().parent.parent / "ui" / "index.html"

app = FastAPI(title="Student Deadline Guardian", version="1.0.0")


class DeadlineCreate(BaseModel):
    title: str = Field(..., min_length=3)
    course: str
    category: str
    due_date: date
    priority: str
    notes: str = ""


def load_df() -> pd.DataFrame:
    df = pd.read_csv(DATA_FILE)
    df["due_date"] = pd.to_datetime(df["due_date"]).dt.date
    return df


def save_df(df: pd.DataFrame) -> None:
    out = df.copy()
    out["due_date"] = out["due_date"].astype(str)
    out.to_csv(DATA_FILE, index=False)


@app.get("/")
def root() -> dict:
    return {"message": "Student Deadline Guardian", "docs": "/docs", "ui": "/ui"}


@app.get("/ui")
def ui() -> FileResponse:
    return FileResponse(UI_FILE)


@app.get("/deadlines")
def get_deadlines() -> list[dict]:
    df = load_df().sort_values("due_date")
    today = date.today()
    items = []
    for _, row in df.iterrows():
        days_left = (row["due_date"] - today).days
        items.append(
            {
                "id": int(row["id"]),
                "title": row["title"],
                "course": row["course"],
                "category": row["category"],
                "due_date": row["due_date"].isoformat(),
                "priority": row["priority"],
                "notes": row["notes"],
                "days_left": int(days_left),
            }
        )
    return items


@app.get("/summary")
def summary() -> dict:
    df = load_df()
    total = len(df)
    high = int((df["priority"] == "high").sum())
    within_week = int((pd.to_datetime(df["due_date"]).dt.date <= (date.today().fromordinal(date.today().toordinal() + 7))).sum())
    return {"total": total, "high_priority": high, "within_7_days": within_week}


@app.post("/deadlines")
def add_deadline(payload: DeadlineCreate) -> dict:
    df = load_df()
    next_id = int(df["id"].max()) + 1 if not df.empty else 1
    row = {
        "id": next_id,
        "title": payload.title,
        "course": payload.course,
        "category": payload.category,
        "due_date": payload.due_date,
        "priority": payload.priority,
        "notes": payload.notes,
    }
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    save_df(df)
    return {"status": "added", "id": next_id}


@app.get("/digest")
def digest() -> dict:
    df = load_df().sort_values("due_date")
    upcoming = df.head(5)
    lines = [
        f"{r['title']} ({r['course']}) - due {r['due_date'].isoformat()} - {r['priority']}"
        for _, r in upcoming.iterrows()
    ]
    return {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "message": "Top upcoming deadlines",
        "items": lines,
    }
