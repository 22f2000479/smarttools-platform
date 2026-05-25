# SmartTools Platform

SmartTools Platform is a FastAPI backend project built to explore AI tools and how APIs can be structured.

It demonstrates both:
- Vibe coding (simple implementation)
- Spec Driven Development (structured architecture)

---

## Architecture (SDD)

app/
- main.py → API layer
- reports.py → business logic
- data.py → dataset
- models.py → schema definitions

---

## Features

- List AI tools
- Filter by category and pricing
- Sorting and pagination
- Clean API design
- Layered architecture (SDD approach)

---

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic

---

## API Endpoints---

### Health Check
GET /health

### Tools API
GET /tools

Supports:
- category filtering
- pricing filtering
- sorting
- pagination

---

## Run Locally

```bash
pip install fastapi uvicorn httpx pytest
python -m uvicorn app.main:app --reload