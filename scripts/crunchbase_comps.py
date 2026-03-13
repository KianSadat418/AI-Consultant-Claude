#!/usr/bin/env python3
"""
crunchbase_comps.py -- Pulls funding round data, valuations, and investor
information for comparable companies using Crunchbase Basic API.
Falls back to web search for funding data if no API key.

Usage:
  python crunchbase_comps.py "hearing aid startup"
  python crunchbase_comps.py "digital health seed round"
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


CRUNCHBASE_API_URL = "https://api.crunchbase.com/api/v4"


def search_crunchbase(query, limit=10):
    """Search Crunchbase for companies matching the query."""
    api_key = os.environ.get("CRUNCHBASE_API_KEY")
    if not api_key:
        return None

    headers = {"X-cb-user-key": api_key}

    # Search for organizations
    search_url = f"{CRUNCHBASE_API_URL}/autocompletes"
    params = {
        "query": query,
        "collection_ids": "organizations",
        "limit": limit,
    }

    try:
        resp = requests.get(search_url, headers=headers, params=params, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        return data.get("entities", [])
    except Exception as e:
        print(f"[founder] Crunchbase search error: {e}")
        return None


def get_company_funding(company_id):
    """Get funding details for a specific company."""
    api_key = os.environ.get("CRUNCHBASE_API_KEY")
    if not api_key:
        return None

    headers = {"X-cb-user-key": api_key}

    url = f"{CRUNCHBASE_API_URL}/entities/organizations/{company_id}"
    params = {
        "field_ids": [
            "short_description",
            "funding_total",
            "last_funding_type",
            "last_funding_at",
            "num_funding_rounds",
            "founded_on",
            "num_employees_enum",
            "categories",
            "location_identifiers",
            "investor_identifiers",
        ],
        "card_ids": ["funding_rounds"],
    }

    try:
        resp = requests.get(url, headers=headers, params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"[founder] Crunchbase company detail error: {e}")
        return None


def format_comparables(companies_data):
    """Format company data into a clean comparable analysis."""
    comps = []
    for company in companies_data:
        props = company.get("properties", {})
        comp = {
            "name": props.get("identifier", {}).get("value", "Unknown"),
            "description": props.get("short_description", ""),
            "funding_total": props.get("funding_total", {}).get("value_usd", 0),
            "last_round_type": props.get("last_funding_type", "Unknown"),
            "last_round_date": props.get("last_funding_at", "Unknown"),
            "num_rounds": props.get("num_funding_rounds", 0),
            "founded": props.get("founded_on", "Unknown"),
            "employees": props.get("num_employees_enum", "Unknown"),
        }

        # Extract funding rounds if available
        cards = company.get("cards", {})
        rounds = cards.get("funding_rounds", [])
        comp["rounds"] = []
        for r in rounds[:5]:
            rprops = r.get("properties", {})
            comp["rounds"].append({
                "type": rprops.get("funding_type", "Unknown"),
                "amount": rprops.get("money_raised", {}).get("value_usd", 0),
                "date": rprops.get("announced_on", "Unknown"),
                "investors": [
                    inv.get("value", "")
                    for inv in rprops.get("investor_identifiers", [])
                ],
            })

        comps.append(comp)

    return comps


def generate_web_search_queries(query):
    """Generate web search queries as fallback when no API key."""
    base_terms = query.strip()
    queries = [
        f"{base_terms} funding round 2024 2025",
        f"{base_terms} startup raised seed series",
        f"{base_terms} venture capital investment",
        f"{base_terms} startup valuation",
        f"{base_terms} crunchbase funding",
    ]
    return queries


def main():
    if len(sys.argv) < 2:
        print("Usage: python crunchbase_comps.py <company name or industry keyword>")
        print('Example: python crunchbase_comps.py "digital health"')
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    print(f"[founder] Searching for comparable companies: {query}")

    api_key = os.environ.get("CRUNCHBASE_API_KEY")

    if api_key:
        # Use Crunchbase API
        results = search_crunchbase(query)
        if results:
            print(f"[founder] Found {len(results)} companies via Crunchbase API")

            all_data = []
            for entity in results[:10]:
                entity_id = entity.get("identifier", {}).get("permalink", "")
                if entity_id:
                    detail = get_company_funding(entity_id)
                    if detail:
                        all_data.append(detail)

            comps = format_comparables(all_data)

            print("\n" + "=" * 60)
            print("COMPARABLE COMPANIES")
            print("=" * 60)
            print(json.dumps(comps, indent=2))
        else:
            print("[founder] No results found via Crunchbase API")
    else:
        print("[founder] CRUNCHBASE_API_KEY not set.")
        print("[founder] Generating web search queries for funding data...")
        queries = generate_web_search_queries(query)

        print("\n" + "=" * 60)
        print("WEB SEARCH QUERIES (run these to find comparable funding data)")
        print("=" * 60)
        for i, q in enumerate(queries, 1):
            print(f"  {i}. {q}")

        print("\n" + "-" * 60)
        print("MANUAL RESEARCH TEMPLATE")
        print("-" * 60)
        print(f"""
Search for companies similar to: {query}

For each comparable company, find:
- Company name and URL
- Total funding raised
- Last round: type, amount, date
- Key investors
- Valuation (if disclosed)
- Stage and employee count

Good sources:
- Crunchbase.com (free tier has limited data)
- PitchBook (if you have access)
- TechCrunch funding news
- Industry-specific databases
""")

    return True


if __name__ == "__main__":
    main()
