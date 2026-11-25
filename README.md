# Student Deadline Guardian

I built Student Deadline Guardian as a small planning app for keeping academic and other important deadlines in one place. It uses due dates and priority labels to show what is coming up and provides a short list of upcoming items.

The backend is written with FastAPI. Deadline records are stored in a CSV file, and a browser interface is served from `/ui`.

## Features in the code

- List deadlines with calculated days remaining: `GET /deadlines`.
- View a summary of total deadlines, high-priority items, and items within seven days: `GET /summary`.
- Add a deadline: `POST /deadlines`.
- Generate a short upcoming-deadline digest: `GET /digest`.
- Open the browser interface at `/ui`.
- Explore the API through FastAPI docs at `/docs`.

## Technology

- Python
- FastAPI and Pydantic
- pandas
- CSV file storage
- HTML, CSS, and JavaScript interface

## Run locally

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn app.main:app --reload --port 8100
```

Open:

- Interface: http://127.0.0.1:8100/ui
- API documentation: http://127.0.0.1:8100/docs

## API quick checks

Get the deadline summary:

```powershell
Invoke-RestMethod -Method GET -Uri "http://127.0.0.1:8100/summary"
```

Get the upcoming digest:

```powershell
Invoke-RestMethod -Method GET -Uri "http://127.0.0.1:8100/digest"
```

## Data storage and limitations

The current implementation reads and writes `data/deadlines.csv`. This is simple for a local prototype, but it is not a multi-user database and does not provide concurrent-write protection.

The application code is present, but automated tests and deployment have not been verified.

## Possible next steps

- Move deadline storage to SQLite or PostgreSQL.
- Add edit and delete operations.
- Add validation for priority and category values.
- Add automated tests for date calculations and API routes.
- Add reminders or calendar integration.

## Author

**Afzal Hussain** · [@Afzu01](https://github.com/Afzu01)
