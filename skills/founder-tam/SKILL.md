---
name: founder-tam
description: >
  Total Addressable Market (TAM/SAM/SOM) analysis with dual top-down and
  bottom-up methodology. Use when the user types /founder tam or asks about
  market sizing, TAM, SAM, SOM, addressable market, or market opportunity.
---

# /founder tam -- Total Addressable Market Analysis

## Purpose
Deliver investor-grade TAM/SAM/SOM market sizing using dual methodology (top-down + bottom-up), real analyst data, and clear assumption documentation. Output should match the quality of a Gartner or McKinsey market sizing brief.

## Trigger
User types: `/founder tam [optional: industry or company name]`

## Data Retrieval (run before any analysis)

**This is non-negotiable. Do NOT begin analysis until data is gathered.**

1. **Load CONTEXT.md** if present in the working directory. Extract: industry, target market, geography, product type, pricing signals, current traction.

2. **Run web searches** (minimum 5 queries, adapt to industry):
   - `"[industry] market size 2025 2026"`
   - `"[industry] TAM total addressable market"`
   - `"[industry] market forecast CAGR growth rate"`
   - `"[specific segment] market size report"`
   - `"[industry] Gartner IDC McKinsey market size"`
   - `"[industry] [geography] market opportunity"`

3. **If PERPLEXITY_API_KEY is set**, run:
   ```bash
   python ~/.claude/scripts/founder/market_research.py "[industry] total addressable market size analyst reports 2024 2025 forecast"
   ```

4. **Fallback**: If no API keys are available, rely entirely on web search results. Triangulate from at least 3 different sources. Note the source and date for every data point.

## Analysis Framework

### Phase 1: Top-Down Sizing
Start from the broadest industry figure and narrow down:

1. **Global TAM**: Total worldwide spending in the broadest relevant category.
   - Source this from analyst reports (Gartner, IDC, Statista, Grand View Research, CB Insights).
   - Cite the source, year, and exact figure.

2. **Segmented TAM**: Narrow to the specific product category or vertical.
   - What percentage of the global TAM is the relevant segment?
   - Apply segment filters: geography, customer type (B2B/B2C/B2G), use case.

3. **SAM (Serviceable Addressable Market)**: The portion the company can realistically reach.
   - Filter by: geography served, customer segments targeted, distribution capability, pricing tier.
   - SAM = TAM × (% reachable given current or near-term go-to-market).

4. **SOM (Serviceable Obtainable Market)**: What the company can capture in 3-5 years.
   - Factor in: competitive intensity, sales capacity, brand awareness, product maturity.
   - SOM = SAM × realistic market share capture (justify the percentage with comparables).

### Phase 2: Bottom-Up Sizing
Build from unit economics upward:

1. **Count addressable customers**: How many potential buyers exist?
   - For B2B: number of companies in target segment × relevant decision-makers per company.
   - For B2C: target demographic population × adoption rate estimate.

2. **Price per unit/customer**: Average revenue per customer per year.
   - Use pricing from CONTEXT.md or competitor pricing data.

3. **Bottom-up TAM** = Addressable customers × Price per customer.
4. **Bottom-up SAM** = Reachable customers × Price per customer.
5. **Bottom-up SOM** = Customers acquirable in 3-5 years × Price per customer.

### Phase 3: Reconciliation
- Compare top-down and bottom-up estimates side by side.
- If they diverge by >50%, explain the gap. Common reasons: different definitions of the addressable segment, price assumptions, geographic scope differences.
- State your confidence level (high/medium/low) with reasoning.

### Phase 4: Growth Projection
- 5-year CAGR projection with assumptions stated.
- Growth drivers (technology adoption, regulatory tailwinds, demographic shifts).
- Growth inhibitors (market saturation, regulatory risk, substitution threats).
- Compare growth rate to adjacent markets.

## Output Format

Save as `MARKET-SIZING.md` in the current working directory.

```markdown
# Market Sizing: [Company Name]
_Generated [date] | Data sources: [list key sources]_

## Executive Summary
[3-4 sentences: total market opportunity, growth trajectory, and the company's
realistic addressable portion. Lead with the most compelling number.]

## Top-Down Analysis

### Global TAM
- **Total market**: $[X]B ([year])
- **Source**: [Analyst firm, report name, date]
- **Definition**: [What this number includes/excludes]

### Segmented TAM
- **Relevant segment**: $[X]B
- **Segment definition**: [How we narrowed from global]
- **Segment share of total**: [X]%

### SAM (Serviceable Addressable Market)
- **SAM**: $[X]B
- **Filters applied**: [Geography, customer type, distribution reach]
- **Reasoning**: [Why this is the reachable portion]

### SOM (Serviceable Obtainable Market)
- **SOM (3-year)**: $[X]M
- **SOM (5-year)**: $[X]M
- **Assumed market share**: [X]%
- **Basis for share assumption**: [Comparable company penetration rates]

## Bottom-Up Analysis

### Customer Count
- **Total addressable customers**: [X]
- **Methodology**: [How counted]
- **Data source**: [Census data, industry reports, etc.]

### Revenue per Customer
- **Average annual revenue**: $[X]
- **Basis**: [Pricing model, competitor benchmarks]

### Bottom-Up Estimates
| Metric | Estimate | Methodology |
|--------|----------|-------------|
| TAM | $[X] | [customer count] × [price] |
| SAM | $[X] | [reachable customers] × [price] |
| SOM | $[X] | [acquirable customers] × [price] |

## Reconciliation

| Metric | Top-Down | Bottom-Up | Delta | Explanation |
|--------|----------|-----------|-------|-------------|
| TAM | $[X] | $[X] | [X]% | [reason for difference] |
| SAM | $[X] | $[X] | [X]% | [reason for difference] |
| SOM | $[X] | $[X] | [X]% | [reason for difference] |

**Confidence Level**: [High/Medium/Low] -- [reasoning]

## 5-Year Growth Projection

| Year | Market Size | Growth Rate | Key Driver |
|------|------------|-------------|------------|
| [Y1] | $[X] | [X]% | [driver] |
| [Y2] | $[X] | [X]% | [driver] |
| [Y3] | $[X] | [X]% | [driver] |
| [Y4] | $[X] | [X]% | [driver] |
| [Y5] | $[X] | [X]% | [driver] |

**CAGR**: [X]%

### Growth Drivers
1. [Driver with supporting data]
2. [Driver with supporting data]
3. [Driver with supporting data]

### Growth Inhibitors
1. [Inhibitor with risk level]
2. [Inhibitor with risk level]

## Analyst Report Comparison

| Source | TAM Estimate | Year | Notes |
|--------|-------------|------|-------|
| [Firm 1] | $[X] | [year] | [scope/methodology] |
| [Firm 2] | $[X] | [year] | [scope/methodology] |
| [Firm 3] | $[X] | [year] | [scope/methodology] |

## Key Assumptions
1. [Assumption + sensitivity: "If X changes by Y%, TAM shifts by Z%"]
2. [Assumption + sensitivity]
3. [Assumption + sensitivity]

## Implications for [Company Name]
[2-3 paragraphs: What this market sizing means for the company's strategy,
positioning, and fundraising narrative. Tie back to CONTEXT.md specifics.]
```

## Output File
Save as: `MARKET-SIZING.md` in the current working directory.
