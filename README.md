# SmartTools Platform

SmartTools Platform is a FastAPI backend project built to explore AI tools and how APIs can be structured.

This project demonstrates basic backend concepts like filtering, API design, and routing.

---

## Features

- List AI tools
- Filter by category
- Filter by pricing
- Basic API structure
- Swagger UI support

---

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic

---

## API Endpoints

### Health
GET /health

### Tools
GET /tools

Supports filtering using query params.

---

## Run

pip install fastapi uvicorn

python -m uvicorn app.main:app --reload

---

## Branches

- main
- sdd_submission
- vibe_coded_submission