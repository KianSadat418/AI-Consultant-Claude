#!/usr/bin/env python3
"""
fetch_context.py -- Loads and validates CONTEXT.md from the current directory.
Returns parsed context as a dictionary. If no CONTEXT.md found, prints the
template and exits with instructions.
"""

import os
import sys
import re
import json
from dotenv import load_dotenv
load_dotenv()


REQUIRED_FIELDS = [
    "company name",
    "description",
    "stage",
    "industry",
]

OPTIONAL_FIELDS = [
    "website",
    "target market",
    "traction",
    "team",
    "fundraising",
    "geography",
    "target customer",
    "competitors",
    "risks",
]

TEMPLATE_PATH = os.path.expanduser("~/.claude/templates/founder/CONTEXT-template.md")


def find_context_file():
    """Look for CONTEXT.md in the current working directory."""
    candidates = ["CONTEXT.md", "context.md", "Context.md"]
    for name in candidates:
        path = os.path.join(os.getcwd(), name)
        if os.path.exists(path):
            return path
    return None


def parse_context(filepath):
    """Parse CONTEXT.md into a dictionary of sections."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    context = {"_raw": content, "_filepath": filepath}

    # Extract key-value pairs from markdown headers and content
    sections = re.split(r"^##\s+", content, flags=re.MULTILINE)

    for section in sections:
        if not section.strip():
            continue
        lines = section.strip().split("\n")
        header = lines[0].strip().lower().rstrip(":")
        body = "\n".join(lines[1:]).strip()

        # Also check for inline key: value patterns
        if body:
            context[header] = body

    # Try to extract key fields from various formats
    # Support both "## Company Name" and "**Company Name**: value" patterns
    inline_patterns = re.findall(
        r"\*\*([^*]+)\*\*\s*:\s*(.+)", content, re.IGNORECASE
    )
    for key, value in inline_patterns:
        normalized_key = key.strip().lower()
        if normalized_key not in context:
            context[normalized_key] = value.strip()

    # Also support "- **Key**: Value" patterns
    list_patterns = re.findall(
        r"-\s*\*\*([^*]+)\*\*\s*:\s*(.+)", content, re.IGNORECASE
    )
    for key, value in list_patterns:
        normalized_key = key.strip().lower()
        if normalized_key not in context:
            context[normalized_key] = value.strip()

    return context


def validate_context(context):
    """Check that minimum required fields are present."""
    missing = []
    found_keys = [k.lower() for k in context.keys()]

    for field in REQUIRED_FIELDS:
        field_found = False
        for key in found_keys:
            if field in key:
                field_found = True
                break
        if not field_found:
            missing.append(field)

    return missing


def print_template():
    """Print the CONTEXT.md template for the user."""
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("""# Company Context

## Company Name
[Your company name]

## One-Line Description
[What your company does in one sentence]

## Website
[URL or "not yet launched"]

## Stage
[idea / pre-seed / seed / Series A+]

## Industry
[Primary industry / sector]

## Target Market
[Who you sell to: B2B / B2C / B2B2C, geography, segment]

## Traction
[Current revenue, users, pilots, LOIs, or other validation]

## Team
[Founding team: names, roles, relevant experience]

## Fundraising
[Current status: bootstrapped / raising / closed round. Target amount if raising.]

## Geography
[Where you operate and target customers]

## Target Customer
[Describe your ideal customer in 2-3 sentences]

## Known Competitors
[List 3-10 competitors you're aware of, with URLs if possible]

## Key Risks & Questions
[What keeps you up at night? What do you most want analyzed?]
""")


def main():
    filepath = find_context_file()

    if filepath is None:
        print("=" * 60)
        print("  No CONTEXT.md found in the current directory.")
        print("=" * 60)
        print()
        print("To use the /founder toolkit, create a CONTEXT.md file")
        print("in your working directory with your company details.")
        print()
        print("Quick start:")
        print(f"  cp {TEMPLATE_PATH} ./CONTEXT.md")
        print("  # Then edit CONTEXT.md with your company info")
        print()
        print("Or here's the template to fill out:")
        print("-" * 60)
        print_template()
        sys.exit(1)

    print(f"[founder] Loading context from: {filepath}")
    context = parse_context(filepath)

    missing = validate_context(context)
    if missing:
        print(f"[founder] WARNING: Missing recommended fields: {', '.join(missing)}")
        print("[founder] The analysis will proceed but may be less accurate.")
    else:
        print("[founder] Context validated. All required fields present.")

    # Print summary
    for key, value in context.items():
        if key.startswith("_"):
            continue
        preview = value[:80] + "..." if len(value) > 80 else value
        preview = preview.replace("\n", " ")
        print(f"  {key}: {preview}")

    # Output as JSON for piping to other scripts
    if "--json" in sys.argv:
        output = {k: v for k, v in context.items() if not k.startswith("_")}
        print(json.dumps(output, indent=2))

    return context


if __name__ == "__main__":
    main()
