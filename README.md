# SmartTools Platform (SDD Branch)

This branch follows a structured, layered architecture using Spec Driven Development.

---

## Architecture

app/
├── main.py
├── reports.py
├── data.py
├── models.py

Each file has a clear responsibility.

---

## Features

- Layered architecture
- Filtering system
- Sorting and pagination
- Clean separation of concerns

---

## Tech Stack

- Python
- FastAPI
- Pydantic

---

## API

- GET /health
- GET /tools

Supports:
- category filtering
- pricing filtering
- sorting
- pagination

---

## Run

pip install fastapi uvicorn

python -m uvicorn app.main:app --reload