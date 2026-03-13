#!/usr/bin/env python3
"""
market_research.py -- Deep market research using Perplexity API.
Falls back to constructing a structured research prompt for Claude if no API key.

Usage:
  python market_research.py "hearing aid market size 2025 TAM analyst report"
"""

import os
import sys
import json

try:
    import requests
except ImportError:
    print("[founder] ERROR: requests not installed. Run: pip install requests")
    sys.exit(1)


PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions"


def research_with_perplexity(query):
    """Use Perplexity API for deep research with citations."""
    api_key = os.environ.get("PERPLEXITY_API_KEY")
    if not api_key:
        return None

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "llama-3.1-sonar-large-128k-online",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a market research analyst. Provide detailed, "
                    "data-driven answers with specific numbers, sources, and dates. "
                    "Focus on: market size figures, growth rates, key players, "
                    "recent developments, and analyst report citations. "
                    "Always cite your sources."
                ),
            },
            {
                "role": "user",
                "content": query,
            },
        ],
        "temperature": 0.1,
        "max_tokens": 2000,
    }

    try:
        resp = requests.post(
            PERPLEXITY_API_URL,
            headers=headers,
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()

        content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        citations = data.get("citations", [])

        result = {
            "content": content,
            "citations": citations,
            "model": data.get("model", "unknown"),
        }
        return result

    except Exception as e:
        print(f"[founder] Perplexity API error: {e}")
        return None


def generate_research_prompt(query):
    """Generate a structured research prompt for Claude when no API key is available."""
    prompt = f"""MARKET RESEARCH TASK
====================

Research the following topic using web search. Gather real data, not estimates
from training data.

QUERY: {query}

INSTRUCTIONS:
1. Search for recent (last 12 months) analyst reports, market studies, and
   industry publications related to this query.
2. Find specific dollar figures for market size with their sources.
3. Identify growth rates (CAGR) with source citations.
4. List key players and their market share if available.
5. Note any recent developments (funding, M&A, product launches) that
   signal market direction.
6. Cite every data point with its source and date.

OUTPUT FORMAT:
- Market Size: $X (Source, Year)
- Growth Rate: X% CAGR (Source, Period)
- Key Players: [list with market share if available]
- Recent Developments: [list with dates]
- Analyst Reports Referenced: [list]
- Data Confidence: [High/Medium/Low with reasoning]

Search for this information now using web search before responding."""

    return prompt


def main():
    if len(sys.argv) < 2:
        print("Usage: python market_research.py <research query>")
        print('Example: python market_research.py "hearing aid market size 2025"')
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    print(f"[founder] Researching: {query}")

    # Try Perplexity API first
    result = research_with_perplexity(query)

    if result:
        print(f"[founder] Research complete via Perplexity API")
        print("\n" + "=" * 60)
        print("RESEARCH RESULTS")
        print("=" * 60)
        print(result["content"])

        if result["citations"]:
            print("\n" + "-" * 60)
            print("CITATIONS")
            print("-" * 60)
            for i, cite in enumerate(result["citations"], 1):
                print(f"  [{i}] {cite}")
    else:
        print("[founder] Perplexity API not available.")
        print("[founder] Generating structured research prompt for Claude...")
        prompt = generate_research_prompt(query)
        print("\n" + "=" * 60)
        print("RESEARCH PROMPT (use with Claude web search)")
        print("=" * 60)
        print(prompt)

    return result


if __name__ == "__main__":
    main()
