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

---

## 🚀 Live & Local Endpoints

### 🌐 Production (Deployed on Render)

- Base URL: https://smarttools-platform.onrender.com
- Health Check: https://smarttools-platform.onrender.com/health
- API Docs (Swagger): https://smarttools-platform.onrender.com/docs
- OpenAPI Schema: https://smarttools-platform.onrender.com/openapi.json
- Tools API: https://smarttools-platform.onrender.com/tools

---

### 💻 Local Development Server

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