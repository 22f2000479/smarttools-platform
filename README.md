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

## API Endpoints

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
```

## Live & Local Endpoints

### Production (Deployed on Render)

- Base URL: https://smarttools-platform.onrender.com
- Health Check: https://smarttools-platform.onrender.com/health
- API Docs (Swagger): https://smarttools-platform.onrender.com/docs
- OpenAPI Schema: https://smarttools-platform.onrender.com/openapi.json
- Tools API: https://smarttools-platform.onrender.com/tools

---

### Local Development Server

- Base URL: http://127.0.0.1:8000
- Health Check: http://127.0.0.1:8000/health
- API Docs (Swagger): http://127.0.0.1:8000/docs
- OpenAPI Schema: http://127.0.0.1:8000/openapi.json
- Tools API: http://127.0.0.1:8000/tools

---

## ⚠️ Known Issues (Render Deployment)

- The application is deployed on Render Free Tier, which may cause **cold start delays**
- On first request after inactivity, the API may take a few seconds to respond or show temporary errors
- Sometimes endpoints may show `404 Not Found` on first load, but work correctly after refreshing
- This happens due to server spin-down in free hosting environments

### 🔄 Recommendation

- If an endpoint fails initially, refresh the request 1–2 times
- Wait a few seconds after inactivity before testing APIs