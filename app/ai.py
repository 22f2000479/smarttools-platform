def suggest_tool(query: str):
    """
    Simple rule-based AI tool recommender
    based on user intent keywords.
    """

    query = query.lower()

    if "code" in query or "coding" in query:
        return "GitHub Copilot"

    elif "image" in query or "design" in query:
        return "Midjourney"

    elif "video" in query:
        return "Runway"

    elif "chat" in query or "assistant" in query:
        return "ChatGPT"

    elif "search" in query or "research" in query:
        return "Perplexity"

    else:
        return "ChatGPT"