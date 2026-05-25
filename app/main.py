from fastapi import FastAPI, Query
from typing import Optional
from fastapi.responses import HTMLResponse
from .ai import suggest_tool
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
                    background: linear-gradient(135deg, #0f172a, #1e293b);
                    color: white;
                    text-align: center;
                    margin: 0;
                    padding: 60px;
                }

                .box {
                    background: rgba(30, 41, 59, 0.9);
                    padding: 30px;
                    border-radius: 16px;
                    display: inline-block;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                }

                a {
                    color: #38bdf8;
                    text-decoration: none;
                    font-weight: bold;
                }

                a:hover {
                    text-decoration: underline;
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