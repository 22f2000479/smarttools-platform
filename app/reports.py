from .data import DATA

def get_tools(
    category=None,
    pricing=None,
    sort="rating",
    descending=True,
    offset=0,
    limit=20
):
    results = DATA

    if category:
        results = [t for t in results if t.category == category]

    if pricing:
        results = [t for t in results if t.pricing == pricing]

    results.sort(
        key=lambda t: getattr(t, sort),
        reverse=descending
    )

    return [t.model_dump() for t in results[offset: offset + limit]]