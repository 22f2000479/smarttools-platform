# SmartTools Platform (Vibe Coding Branch)

This is a single-file FastAPI implementation focusing on speed and simplicity.

---

## Features

- Single file backend
- Fast API development
- Tool listing
- Basic filtering

---

## Tech Stack

- Python
- FastAPI
- Uvicorn

---

## API

- GET /health
- GET /tools

Supports:
- category
- pricing
- limit

---

## Run

pip install fastapi uvicorn

python -m uvicorn app.main:app --reload