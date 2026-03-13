---
name: founder-compete
description: >
  Competitive landscape analysis using Bain competitive intelligence methodology.
  Maps direct and indirect competitors, pricing, positioning, moats, and white
  space opportunities. Use when the user types /founder compete or asks about
  competitors, competitive analysis, market positioning, or competitive landscape.
---

# /founder compete -- Competitive Landscape Analysis

## Purpose
Deliver a Bain-caliber competitive intelligence report mapping direct and indirect competitors with feature comparison, pricing audit, positioning analysis, moat assessment, and white space identification. Output must be specific enough to inform product and GTM decisions.

## Trigger
User types: `/founder compete [optional: specific competitor name or URL]`

## Data Retrieval (run before any analysis)

1. **Load CONTEXT.md** if present. Extract: industry, known competitors, product description, pricing, differentiators.

2. **Run web searches** (minimum 8 queries):
   - `"[industry] competitors landscape"`
   - `"[known competitor 1] pricing features"`
   - `"[known competitor 2] pricing features"`
   - `"[industry] startups funded 2024 2025"`
   - `"[product type] comparison review"`
   - `"[industry] G2 Capterra reviews"` (if B2B SaaS)
   - `"[known competitor] revenue customers funding"`
   - `"alternatives to [known competitor]"`

3. **If FIRECRAWL_API_KEY is set**, scrape competitor websites:
   ```bash
   python ~/.claude/scripts/founder/scrape_competitor.py "[competitor URL]"
   ```
   Scrape: pricing pages, about/team pages, careers pages (hiring = investment signal), product feature pages.

4. **If CRUNCHBASE_API_KEY is set**, pull funding data:
   ```bash
   python ~/.claude/scripts/founder/crunchbase_comps.py "[industry keyword]"
   ```

5. **Fallback**: Build competitor profiles entirely from web search. Search for each competitor individually: "[competitor] funding", "[competitor] pricing", "[competitor] reviews".

## Analysis Framework

### Phase 1: Competitor Identification
Build three tiers:

**Direct Competitors (minimum 10)**:
Companies solving the same problem for the same customer. For each:
- Company name, URL, HQ location
- Founded year, funding raised, last round
- Employee count (estimate from LinkedIn/careers page)
- Target customer segment
- Core product offering
- Pricing model and price points
- Key differentiator (what they claim)
- Estimated market share or traction signals

**Indirect Competitors (minimum 5)**:
Companies solving adjacent problems or serving the same customer with different solutions. Include: spreadsheets/manual processes, in-house solutions, different technology approaches.

**Emerging Threats (minimum 3)**:
Early-stage startups, big tech initiatives, or open-source projects that could disrupt the space. Search for recent Y Combinator batches, Product Hunt launches, and GitHub trending repos in the space.

### Phase 2: Feature Comparison Matrix
Build a detailed feature comparison table:
- List 15-20 features/capabilities relevant to the product category
- Rate each competitor: Full / Partial / None / Unknown
- Highlight feature gaps (features no one has built yet)
- Highlight feature parity (table stakes features everyone has)
- Identify unique features per competitor

### Phase 3: Pricing Analysis
For each competitor with discoverable pricing:
- Pricing model (per seat, usage-based, flat rate, freemium, etc.)
- Price tiers and what each includes
- Free trial/freemium availability
- Enterprise pricing signals
- Price-to-value positioning (premium / mid-market / budget)

### Phase 4: Positioning Map
Create a textual positioning map using two axes:
- **X-axis**: Choose the most differentiating dimension (e.g., price, simplicity, breadth of features, target company size)
- **Y-axis**: Choose the second most differentiating dimension
- Place each competitor on the map with coordinates
- Identify clusters and white space

### Phase 5: Competitive Moats Analysis
For each top 5 competitor, assess moats using the Buffett/Morningstar framework:
- **Network effects**: Does the product get better with more users?
- **Switching costs**: How hard is it to leave?
- **Cost advantages**: Do they have scale or structural cost advantages?
- **Intangible assets**: Brand, patents, regulatory licenses, data moats?
- **Efficient scale**: Is the market too small for another player?
Rate each moat: Strong / Moderate / Weak / None.

### Phase 6: White Space Identification
Based on all the above analysis:
- What customer segments are underserved?
- What features are missing from all competitors?
- What pricing models are unexplored?
- What geographic markets lack strong competitors?
- What adjacent problems are unsolved?

### Phase 7: Threat Assessment
For each direct competitor, rate:
- **Threat level**: Low / Medium / High / Critical
- **Basis for rating**: funding, traction, product quality, team strength
- **Likely next move**: What will they do in the next 12 months?
- **Defensive strategy**: How should the company respond?

## Output Format

Save as `COMPETITIVE-LANDSCAPE.md`:

```markdown
# Competitive Landscape: [Company Name]
_Generated [date] | [X] competitors analyzed_

## Executive Summary
[4-5 sentences: competitive intensity, main threats, biggest opportunity,
and recommended positioning. Be direct about where the company stands.]

## Direct Competitors

| # | Company | Founded | Funding | Employees | Target Customer | Threat |
|---|---------|---------|---------|-----------|----------------|--------|
| 1 | [name] | [year] | $[X]M | ~[X] | [segment] | [H/M/L] |
[...10 rows minimum]

### Detailed Profiles

#### 1. [Competitor Name]
- **URL**: [url]
- **Funding**: $[X]M ([last round type], [date])
- **Investors**: [notable investors]
- **Product**: [2-3 sentence description]
- **Pricing**: [model + price points]
- **Strengths**: [bullet list]
- **Weaknesses**: [bullet list]
- **Recent moves**: [launches, hires, partnerships from last 6 months]
- **Threat assessment**: [Low/Medium/High] -- [1 sentence justification]

[Repeat for top 5-7 competitors with full profiles; brief entries for the rest]

## Indirect Competitors & Alternatives
| Company/Solution | Approach | Overlap | Threat Level |
|-----------------|----------|---------|-------------|
| [name] | [how they solve it differently] | [where they overlap] | [H/M/L] |

## Emerging Threats
| Company/Project | Stage | Why to Watch | Timeline |
|----------------|-------|-------------|----------|
| [name] | [stage] | [signal] | [when they become a threat] |

## Feature Comparison Matrix

| Feature | [Company] | [Comp 1] | [Comp 2] | [Comp 3] | [Comp 4] | [Comp 5] |
|---------|-----------|----------|----------|----------|----------|----------|
| [feature 1] | [status] | [status] | [status] | [status] | [status] | [status] |
[...15-20 features]

**Legend**: Full = fully built | Partial = limited | None = not available | ? = unknown

### Feature Gaps (No One Has Built)
- [Gap 1]: [Why it matters]
- [Gap 2]: [Why it matters]

### Table Stakes (Everyone Has)
- [Feature list that is now expected by customers]

## Pricing Landscape

| Company | Model | Entry Price | Mid-Tier | Enterprise | Free Tier |
|---------|-------|-----------|----------|-----------|-----------|
| [comp] | [model] | $[X]/mo | $[X]/mo | Custom | [Y/N] |

### Pricing Insights
[2-3 paragraphs on pricing patterns, opportunities, and risks]

## Positioning Map

**Axes**: [X-axis label] vs. [Y-axis label]

```
[Y-axis label] HIGH
    |
    |   [Comp A]        [Comp B]
    |
    |        [YOUR COMPANY]
    |
    |   [Comp C]    [Comp D]
    |
    +-------------------------------- [X-axis label] HIGH
```

### Positioning Insights
[Where the company sits, where it should move, and why]

## Competitive Moats Assessment

| Competitor | Network Effects | Switching Costs | Cost Advantage | Intangibles | Overall |
|-----------|----------------|----------------|---------------|------------|---------|
| [comp] | [S/M/W/N] | [S/M/W/N] | [S/M/W/N] | [S/M/W/N] | [S/M/W] |

## White Space Opportunities
1. **[Opportunity]**: [Description + evidence + estimated size]
2. **[Opportunity]**: [Description + evidence + estimated size]
3. **[Opportunity]**: [Description + evidence + estimated size]

## Strategic Recommendations
[3-4 paragraphs: How to position against the competitive landscape.
Include specific product, pricing, and messaging recommendations.
Identify the top 3 competitive risks and mitigation strategies.]
```

## Output File
Save as: `COMPETITIVE-LANDSCAPE.md` in the current working directory.
