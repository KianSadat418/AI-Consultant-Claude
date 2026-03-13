#!/usr/bin/env python3
"""
web_search.py -- General web search utility wrapper.
Used by other scripts as a fallback when API keys are not available.
Provides structured search result formatting.

Usage:
  python web_search.py "hearing aid market size 2025"
  python web_search.py "hearing aid market size 2025" --num 5
"""

import os
import sys
import json
from dotenv import load_dotenv
load_dotenv()

try:
    import requests
except ImportError:
    print("[founder] ERROR: requests not installed. Run: pip install requests")
    sys.exit(1)


def search_google(query, num_results=5):
    """Search using Google Custom Search API if keys are available."""
    api_key = os.environ.get("GOOGLE_API_KEY")
    cse_id = os.environ.get("GOOGLE_CSE_ID")

    if not api_key or not cse_id:
        return None

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": cse_id,
        "q": query,
        "num": min(num_results, 10),
    }

    try:
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        data = resp.json()

        results = []
        for item in data.get("items", []):
            results.append({
                "title": item.get("title", ""),
                "url": item.get("link", ""),
                "snippet": item.get("snippet", ""),
            })
        return results
    except Exception as e:
        print(f"[founder] Google Search API error: {e}")
        return None


def search_serper(query, num_results=5):
    """Search using Serper API if key is available."""
    api_key = os.environ.get("SERPER_API_KEY")
    if not api_key:
        return None

    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json",
    }
    payload = {
        "q": query,
        "num": num_results,
    }

    try:
        resp = requests.post(
            "https://google.serper.dev/search",
            headers=headers,
            json=payload,
            timeout=15,
        )
        resp.raise_for_status()
        data = resp.json()

        results = []
        for item in data.get("organic", []):
            results.append({
                "title": item.get("title", ""),
                "url": item.get("link", ""),
                "snippet": item.get("snippet", ""),
            })
        return results
    except Exception as e:
        print(f"[founder] Serper API error: {e}")
        return None


def generate_search_instructions(query, num_results=5):
    """When no search API is available, generate instructions for Claude."""
    return {
        "status": "no_api_available",
        "instruction": (
            f"No web search API key is configured. "
            f"Use Claude Code's built-in web search to find: {query}"
        ),
        "suggested_queries": [
            query,
            f"{query} report",
            f"{query} statistics data",
        ],
        "note": (
            "Claude Code has built-in web search capability. "
            "The skill should instruct Claude to search directly."
        ),
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python web_search.py <query> [--num N]")
        print('Example: python web_search.py "hearing aid market size 2025"')
        sys.exit(1)

    # Parse arguments
    num_results = 5
    query_parts = []
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "--num" and i + 1 < len(sys.argv):
            num_results = int(sys.argv[i + 1])
            i += 2
        else:
            query_parts.append(sys.argv[i])
            i += 1

    query = " ".join(query_parts)
    print(f"[founder] Searching: {query} (max {num_results} results)")

    # Try available search APIs in order
    results = search_serper(query, num_results)
    if results:
        source = "Serper"
    else:
        results = search_google(query, num_results)
        if results:
            source = "Google Custom Search"
        else:
            results = None
            source = None

    if results:
        print(f"[founder] Found {len(results)} results via {source}")
        print("\n" + "=" * 60)
        print("SEARCH RESULTS")
        print("=" * 60)
        for i, r in enumerate(results, 1):
            print(f"\n  [{i}] {r['title']}")
            print(f"      {r['url']}")
            print(f"      {r['snippet']}")
        print("\n" + json.dumps(results, indent=2))
    else:
        print("[founder] No web search API available.")
        fallback = generate_search_instructions(query, num_results)
        print("\n" + "=" * 60)
        print("FALLBACK INSTRUCTIONS")
        print("=" * 60)
        print(json.dumps(fallback, indent=2))


if __name__ == "__main__":
    main()
