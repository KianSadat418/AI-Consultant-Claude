---
name: founder-trends
description: >
  Industry trend analysis with Goldman Sachs Research-style output covering macro
  and micro trends, technology disruption, regulatory watch, and investment signals.
  Use when the user types /founder trends or asks about industry trends, market
  movements, disruption signals, or emerging opportunities in any sector.
---

# /founder trends -- Industry Trend Analysis

## Purpose
Deliver a Goldman Sachs Research-caliber industry trend report covering macro forces, micro signals, technology disruption timelines, regulatory developments, and investment activity. Every trend is rated by impact and mapped to a specific timeline with actionable implications for the company.

## Trigger
User types: `/founder trends [optional: industry or focus area]`

## Data Retrieval (run before any analysis)

1. **Load CONTEXT.md** if present. Extract: industry, sub-sector, geography, stage, known competitors.

2. **Run web searches** (minimum 8 queries):
   - `"[industry] trends 2025 2026"`
   - `"[industry] emerging technology disruption"`
   - `"[industry] venture capital investment 2025"`
   - `"[industry] regulatory changes 2025 2026"`
   - `"[industry] market forecast analyst report"`
   - `"[industry] job postings hiring trends"` (signal for where companies invest)
   - `"[industry] M&A acquisition activity"`
   - `"[industry] startup funding news recent"`

3. **If PERPLEXITY_API_KEY is set**, run:
   ```bash
   python ~/.claude/scripts/founder/market_research.py "[industry] major trends disruptions regulatory changes 2024 2025 analyst research"
   ```

4. **Fallback**: Triangulate from web search results. Prioritize sources from the last 6 months. Every trend must have at least one cited data point or source.

## Analysis Framework

### Phase 1: PESTLE Macro Scan (5 Macro Trends)
Identify 5 major macro trends using the PESTLE framework:
- **P**olitical: Government policy shifts, trade agreements, geopolitical tensions affecting the industry.
- **E**conomic: Interest rates, consumer spending, B2B budget cycles, currency effects.
- **S**ocial: Demographic shifts, behavioral changes, cultural attitudes, workforce dynamics.
- **T**echnological: Platform shifts, AI/ML adoption, infrastructure changes, new development paradigms.
- **L**egal: Regulatory changes, compliance requirements, IP landscape shifts, litigation trends.
- **E**nvironmental: Sustainability mandates, ESG investor requirements, climate adaptation.

For each macro trend: state the trend, cite supporting evidence, rate impact (1-10), assign timeline (already happening / 6-12 months / 1-3 years / 3-5 years).

### Phase 2: Micro Signal Detection (7 Micro Trends)
Identify 7 specific, observable micro trends from the last 12 months:
- New product launches or pivots by competitors
- Hiring pattern shifts (what roles are companies hiring for?)
- Pricing model changes in the industry
- Partnership/integration announcements
- Customer behavior shifts (adoption curves, churn patterns)
- Investor thesis shifts (what are VCs writing about?)
- Community/developer ecosystem growth signals

Each micro trend must reference a specific company, event, or data point from the last 12 months.

### Phase 3: Technology Disruption Timeline
Map technology disruptions on a timeline:
- **Now (adopted by early majority)**: Technologies already reshaping the industry.
- **Near-term (1-2 years)**: Technologies in early adopter phase that will become mainstream.
- **Medium-term (2-4 years)**: Technologies in R&D/pilot phase with high disruption potential.
- **Long-term (4-7 years)**: Speculative but plausible technology shifts (cite research).

### Phase 4: Regulatory Watch List
List upcoming regulatory changes or proposals that could impact the industry:
- Regulation name/proposal
- Jurisdiction
- Expected timeline
- Impact assessment (positive/negative/neutral for the company)
- Probability of passage

### Phase 5: Investment Signal Mapping
Map recent investment activity:
- Major funding rounds in the space (last 12 months)
- Acqui-hires and M&A signals
- Corporate venture arms entering the space
- Geographic shifts in investment (e.g., growing activity in specific regions)

### Phase 6: "So What" Analysis
For each trend (macro and micro), write a specific implication paragraph:
- What does this trend mean for THIS company specifically?
- Is it an opportunity or a threat?
- What should the founder do about it in the next 90 days?

## Output Format

Save as `INDUSTRY-TRENDS.md`:

```markdown
# Industry Trend Analysis: [Industry]
_Generated [date] | Analysis period: Last 12 months + 5-year forward look_
_Company context: [Company Name] ([Stage])_

## Executive Summary
[4-5 sentences capturing the most important trend dynamics and what they mean
for the company. Lead with the single most impactful finding.]

## Macro Trends (PESTLE Analysis)

### 1. [Trend Name] -- [PESTLE Category]
- **Impact Rating**: [X]/10
- **Timeline**: [timeframe]
- **Evidence**: [Specific data point, source, date]
- **Description**: [2-3 sentences]
- **Implication for [Company]**: [What to do about it]

[Repeat for all 5 macro trends]

## Micro Trends (Last 12 Months)

### 1. [Trend Name]
- **Impact Rating**: [X]/10
- **Timeline**: [Short/Mid/Long-term]
- **Signal**: [Specific company, event, or data point with date]
- **Description**: [2-3 sentences]
- **Implication for [Company]**: [What to do about it]

[Repeat for all 7 micro trends]

## Technology Disruption Timeline

| Technology | Phase | Expected Mainstream | Disruption Level | Key Players |
|-----------|-------|-------------------|-----------------|-------------|
| [tech] | Now | Adopted | [High/Med/Low] | [companies] |
| [tech] | Near-term (1-2yr) | [year] | [High/Med/Low] | [companies] |
| [tech] | Medium-term (2-4yr) | [year] | [High/Med/Low] | [research labs] |
| [tech] | Long-term (4-7yr) | [year] | [High/Med/Low] | [speculative] |

## Regulatory Watch List

| Regulation | Jurisdiction | Timeline | Impact | Probability | Action Required |
|-----------|-------------|----------|--------|------------|-----------------|
| [name] | [country/state] | [date] | [+/-/neutral] | [High/Med/Low] | [brief action] |

## Investment Signals

### Recent Funding Activity
| Company | Round | Amount | Date | Relevance |
|---------|-------|--------|------|-----------|
| [company] | [stage] | $[X]M | [date] | [why it matters] |

### M&A Activity
[Notable acquisitions and what they signal about the market]

### Investor Thesis Shifts
[What top VCs and analysts are writing about this space]

## Trend Impact Matrix

| Trend | Impact (1-10) | Urgency | Opportunity/Threat | Recommended Action |
|-------|--------------|---------|-------------------|-------------------|
| [trend] | [X] | [Now/Soon/Watch] | [O/T/Both] | [1-line action] |

## Strategic Implications for [Company Name]
[3-4 paragraphs synthesizing what all these trends mean for the company.
Prioritize the top 3 trends the founder should act on immediately.
Include specific 90-day recommendations.]

## Sources
[Numbered list of all sources cited in the analysis]
```

## Output File
Save as: `INDUSTRY-TRENDS.md` in the current working directory.
