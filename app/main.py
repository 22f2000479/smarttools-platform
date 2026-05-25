from fastapi import FastAPI
from typing import Optional
from .ai import suggest_tool
from fastapi import Query
from fastapi.responses import HTMLResponse
from .reports import get_tools
from .models import Category, Pricing

app = FastAPI(
    title="SmartTools API",
    description="API for discovering AI tools",
    version="1.0.0"
)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>SmartTools API</title>
            <style>
                body {
                    font-family: Arial;
                    background: #0f172a;
                    color: white;
                    text-align: center;
                    padding-top: 100px;
                }
                .box {
                    background: #1e293b;
                    padding: 30px;
                    border-radius: 12px;
                    display: inline-block;
                }
                a {
                    color: #38bdf8;
                    text-decoration: none;
                }
            </style>
        </head>
        <body>
            <div class="box">
                <h1>🚀 SmartTools API</h1>
                <p>FastAPI backend for AI tool discovery</p>
                <p><a href="/docs">Open Swagger Docs</a></p>
                <p><a href="/health">Check Health</a></p>
            </div>
        </body>
    </html>
    """

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

@app.get("/ai/suggest")
def ai_suggest(query: str = Query(...)):
    return {
        "query": query,
        "suggested_tool": suggest_tool(query)
    }

@app.get("/health")
def health():
    return {"status": "ok"}


