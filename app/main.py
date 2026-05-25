from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI(title="SmartTools Vibe API")

TOOLS = [
    {"id": 1, "name": "ChatGPT", "category": "chatbot", "pricing": "freemium", "rating": 4.8},
    {"id": 2, "name": "Midjourney", "category": "design", "pricing": "paid", "rating": 4.7},
    {"id": 3, "name": "Copilot", "category": "coding", "pricing": "paid", "rating": 4.6},
    {"id": 4, "name": "Perplexity", "category": "search", "pricing": "freemium", "rating": 4.5},
]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tools")
def get_tools(
    category: Optional[str] = None,
    pricing: Optional[str] = None,
    limit: int = 10
):
    results = TOOLS

    if category:
        results = [t for t in results if t["category"] == category]

    if pricing:
        results = [t for t in results if t["pricing"] == pricing]

    return results[:limit]