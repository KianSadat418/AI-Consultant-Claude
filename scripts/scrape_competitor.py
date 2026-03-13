#!/usr/bin/env python3
"""
scrape_competitor.py -- Scrapes competitor websites for competitive intelligence.
Uses Firecrawl API if FIRECRAWL_API_KEY is set, falls back to requests + BeautifulSoup.
Returns clean markdown of key page content.

Usage:
  python scrape_competitor.py "https://competitor.com"
  python scrape_competitor.py "https://competitor.com/pricing"
"""

import os
import sys
import json
import re
from dotenv import load_dotenv
load_dotenv()

try:
    import requests
except ImportError:
    print("[founder] ERROR: requests not installed. Run: pip install requests")
    sys.exit(1)


def scrape_with_firecrawl(url):
    """Scrape using Firecrawl API for clean markdown output."""
    api_key = os.environ.get("FIRECRAWL_API_KEY")
    if not api_key:
        return None

    try:
        from firecrawl import FirecrawlApp
        app = FirecrawlApp(api_key=api_key)
        result = app.scrape_url(url, params={"formats": ["markdown"]})
        if result and "markdown" in result:
            return result["markdown"]
        return None
    except ImportError:
        # Try direct API call
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        payload = {"url": url, "formats": ["markdown"]}
        try:
            resp = requests.post(
                "https://api.firecrawl.dev/v1/scrape",
                headers=headers,
                json=payload,
                timeout=30,
            )
            if resp.status_code == 200:
                data = resp.json()
                return data.get("data", {}).get("markdown", None)
        except Exception as e:
            print(f"[founder] Firecrawl API error: {e}")
        return None
    except Exception as e:
        print(f"[founder] Firecrawl error: {e}")
        return None


def scrape_with_bs4(url):
    """Fallback scraper using requests + BeautifulSoup."""
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        print("[founder] WARNING: beautifulsoup4 not installed. Run: pip install beautifulsoup4")
        return None

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }

    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
    except Exception as e:
        print(f"[founder] HTTP error fetching {url}: {e}")
        return None

    soup = BeautifulSoup(resp.text, "html.parser")

    # Remove script, style, nav, footer elements
    for tag in soup(["script", "style", "nav", "footer", "header", "iframe", "noscript"]):
        tag.decompose()

    # Extract key sections
    result_parts = []

    # Title
    title = soup.find("title")
    if title:
        result_parts.append(f"# {title.get_text().strip()}\n")

    # Meta description
    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc and meta_desc.get("content"):
        result_parts.append(f"**Description**: {meta_desc['content']}\n")

    # Main content: headings and paragraphs
    for tag in soup.find_all(["h1", "h2", "h3", "h4", "p", "li"]):
        text = tag.get_text().strip()
        if not text or len(text) < 10:
            continue

        if tag.name == "h1":
            result_parts.append(f"\n# {text}")
        elif tag.name == "h2":
            result_parts.append(f"\n## {text}")
        elif tag.name == "h3":
            result_parts.append(f"\n### {text}")
        elif tag.name == "h4":
            result_parts.append(f"\n#### {text}")
        elif tag.name == "li":
            result_parts.append(f"- {text}")
        else:
            result_parts.append(text)

    return "\n".join(result_parts)


def extract_intelligence(markdown_content):
    """Extract key competitive intelligence signals from scraped content."""
    signals = {
        "value_proposition": "",
        "pricing_signals": [],
        "key_features": [],
        "target_customer_signals": [],
        "team_signals": [],
        "traction_signals": [],
    }

    if not markdown_content:
        return signals

    content_lower = markdown_content.lower()

    # Pricing signals
    pricing_patterns = [
        r"\$\d+[\d,]*(?:\.\d{2})?(?:\s*/\s*(?:mo|month|year|yr|user|seat))?",
        r"(?:free|starter|basic|pro|premium|enterprise|business)\s*(?:plan|tier)?",
        r"(?:pricing|plans?|packages?)\s*(?:start|from|at)\s*\$?\d+",
    ]
    for pattern in pricing_patterns:
        matches = re.findall(pattern, content_lower)
        signals["pricing_signals"].extend(matches[:5])

    # Feature signals (lines starting with checkmarks, bullets about features)
    feature_patterns = re.findall(
        r"(?:^|\n)\s*[-*✓✔]\s*(.{10,80})",
        markdown_content,
    )
    signals["key_features"] = feature_patterns[:15]

    # Customer signals
    customer_patterns = [
        r"(?:trusted by|used by|loved by|built for|designed for)\s+(.{10,80})",
        r"(\d+[,+]?\s*(?:customers?|users?|companies|teams?|businesses))",
    ]
    for pattern in customer_patterns:
        matches = re.findall(pattern, content_lower)
        signals["target_customer_signals"].extend(matches[:5])

    # Traction signals
    traction_patterns = [
        r"(\d+[,.]?\d*[+]?\s*(?:customers?|users?|downloads?|companies))",
        r"(\$\d+[BMK]?\+?\s*(?:in\s+)?(?:revenue|ARR|funding|raised))",
    ]
    for pattern in traction_patterns:
        matches = re.findall(pattern, markdown_content, re.IGNORECASE)
        signals["traction_signals"].extend(matches[:5])

    return signals


def main():
    if len(sys.argv) < 2:
        print("Usage: python scrape_competitor.py <URL>")
        print("Example: python scrape_competitor.py https://competitor.com")
        sys.exit(1)

    url = sys.argv[1]
    print(f"[founder] Scraping: {url}")

    # Try Firecrawl first
    content = scrape_with_firecrawl(url)
    if content:
        print(f"[founder] Successfully scraped via Firecrawl ({len(content)} chars)")
    else:
        print("[founder] Firecrawl not available, falling back to basic scraper")
        content = scrape_with_bs4(url)
        if content:
            print(f"[founder] Successfully scraped via BeautifulSoup ({len(content)} chars)")
        else:
            print(f"[founder] ERROR: Could not scrape {url}")
            sys.exit(1)

    # Extract intelligence signals
    signals = extract_intelligence(content)

    # Output
    print("\n" + "=" * 60)
    print("SCRAPED CONTENT")
    print("=" * 60)
    # Truncate to reasonable length
    if len(content) > 5000:
        print(content[:5000])
        print(f"\n... [truncated, {len(content)} total chars]")
    else:
        print(content)

    print("\n" + "=" * 60)
    print("INTELLIGENCE SIGNALS")
    print("=" * 60)
    print(json.dumps(signals, indent=2))

    return content, signals


if __name__ == "__main__":
    main()
