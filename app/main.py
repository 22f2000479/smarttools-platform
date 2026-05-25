from fastapi import FastAPI
from typing import Optional
from .ai import suggest_tool
from fastapi import Query

from .reports import get_tools
from .models import Category, Pricing

app = FastAPI(
    title="SmartTools API",
    description="API for discovering AI tools",
    version="1.0.0"
)

@app.get("/ai/suggest")
def ai_suggest(query: str = Query(...)):
    return {
        "query": query,
        "suggested_tool": suggest_tool(query)
    }

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tools")
def tools(
    category: Optional[Category] = None,
    pricing: Optional[Pricing] = None,
    sort: str = "rating",
    descending: bool = True,
    offset: int = 0,
    limit: int = 20
):
    return get_tools(
        category=category,
        pricing=pricing,
        sort=sort,
        descending=descending,
        offset=offset,
        limit=limit
    )