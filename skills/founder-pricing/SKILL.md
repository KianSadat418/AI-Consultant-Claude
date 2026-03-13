---
name: founder-pricing
description: >
  Pricing strategy analysis using Fortune 500 pricing consultant methodology.
  Covers competitor pricing audit, value-based pricing, cost-plus analysis,
  elasticity estimation, and 3-tier pricing recommendation. Use when the user
  types /founder pricing or asks about pricing strategy, pricing model, pricing
  tiers, monetization, or willingness to pay.
---

# /founder pricing -- Pricing Strategy

## Purpose
Deliver a Fortune 500 pricing consultant-level recommendation covering competitor pricing audit, value-based pricing model, cost-plus floor, price elasticity estimation, and a concrete 3-tier pricing recommendation with revenue projections.

## Trigger
User types: `/founder pricing [optional: product or pricing question]`

## Data Retrieval (run before any analysis)

1. **Load CONTEXT.md** if present. Extract: product, current pricing (if any), cost structure, target customer, competitors.

2. **Load existing analyses**: `COMPETITIVE-LANDSCAPE.md`, `CUSTOMER-PERSONAS.md`, `UNIT-ECONOMICS.md` if present.

3. **Run web searches** (minimum 6 queries):
   - `"[competitor 1] pricing page"`
   - `"[competitor 2] pricing"`
   - `"[industry] pricing benchmarks"`
   - `"[product type] willingness to pay"`
   - `"[industry] SaaS pricing strategy"` (or relevant model)
   - `"[industry] pricing case study"`

4. **If FIRECRAWL_API_KEY is set**, scrape competitor pricing pages directly.

5. **Fallback**: Build pricing analysis from web search data.

## Analysis Framework

### Phase 1: Competitor Pricing Audit
For every discoverable competitor:
- Pricing model (per seat, usage, flat, freemium, enterprise)
- Tier structure and price points
- Feature allocation per tier
- Free trial/freemium details
- Discount patterns (annual vs. monthly, volume)
- Price positioning (premium/mid/budget)

### Phase 2: Value-Based Pricing
Price from customer value, not cost:
- What problem does the product solve?
- What is the cost of NOT solving it? (Time, money, risk)
- What is the next-best alternative and its cost?
- Value delivered = (benefit of solution) - (cost of next-best alternative)
- Value-based price = fraction of value delivered (typically 10-30% for B2B)

### Phase 3: Cost-Plus Floor
- Variable cost per customer/unit
- Fixed cost allocation per customer
- Minimum price for positive contribution margin
- Break-even pricing

### Phase 4: Price Elasticity Estimation
- How sensitive is demand to price changes?
- Evidence from competitor tier adoption patterns
- Price anchoring effects
- Psychological pricing considerations ($9.99 vs $10, $99 vs $100)

### Phase 5: 3-Tier Recommendation
Design three pricing tiers:
- **Starter/Basic**: Entry point. Low barrier, proves value.
- **Professional/Growth**: Main revenue driver. Best value perception.
- **Enterprise/Scale**: Premium. High-touch, custom.

For each tier: name, price, features included, target persona, expected adoption %, revenue contribution %.

### Phase 6: Revenue Projections
3 scenarios using the recommended pricing:
- **Aggressive**: High adoption, fast scaling, optimistic conversion
- **Moderate**: Balanced assumptions
- **Conservative**: Slow adoption, high churn, price sensitivity

### Phase 7: Monetization Strategy
Beyond core pricing:
- Upsell opportunities
- Cross-sell potential
- Usage-based revenue streams
- Add-on/marketplace potential
- Annual vs. monthly pricing premium

## Output Format

Save as `PRICING-STRATEGY.md`:

```markdown
# Pricing Strategy: [Company Name]
_Generated [date]_

## Executive Summary
[4-5 sentences: Recommended pricing model, target price point, expected
revenue impact, and the key insight driving the recommendation.]

## Competitor Pricing Audit

| Competitor | Model | Starter | Pro | Enterprise | Free Tier |
|-----------|-------|---------|-----|-----------|-----------|
| [comp] | [model] | $[X]/mo | $[X]/mo | Custom | [Y/N] |
[...all competitors with discoverable pricing]

### Pricing Patterns
[Key observations about how the market prices]

### Price Gaps
[Where no one is pricing, underserved price points]

## Value-Based Analysis

### Value Delivered
- **Problem cost**: $[X] per [period] (what the customer loses without a solution)
- **Next-best alternative**: [solution] at $[X]
- **Value gap**: $[X] (value your product delivers above alternatives)
- **Value-based price range**: $[X] -- $[X] (10-30% of value delivered)

### Value by Persona
| Persona | Problem Cost | Alt Cost | Value Gap | Max WTP |
|---------|------------|---------|-----------|---------|
| [persona] | $[X] | $[X] | $[X] | $[X] |

## Cost Floor Analysis
- **Variable cost per customer**: $[X]/mo
- **Allocated fixed cost per customer**: $[X]/mo
- **Minimum viable price**: $[X]/mo (break-even)
- **Target margin**: [X]%
- **Cost-plus price**: $[X]/mo

## Recommended Pricing

### Tier Structure

| | Starter | Professional | Enterprise |
|--|---------|-------------|-----------|
| **Price** | $[X]/mo | $[X]/mo | Custom |
| **Annual price** | $[X]/yr (save [X]%) | $[X]/yr | Custom |
| **Target persona** | [persona] | [persona] | [persona] |
| **Key features** | [list] | [list] | [list] |
| **Limits** | [limits] | [limits] | Unlimited |
| **Expected adoption** | [X]% | [X]% | [X]% |

### Feature Allocation Rationale
[Why each feature is in its tier. The logic behind what makes users upgrade.]

### Pricing Psychology
[Anchoring, decoy effects, charm pricing decisions]

## Revenue Projections

| Scenario | Year 1 MRR | Year 1 ARR | Year 2 ARR | Year 3 ARR |
|----------|-----------|-----------|-----------|-----------|
| Aggressive | $[X]K | $[X]K | $[X]M | $[X]M |
| Moderate | $[X]K | $[X]K | $[X]K | $[X]M |
| Conservative | $[X]K | $[X]K | $[X]K | $[X]K |

### Key Assumptions
[What drives each scenario]

## Monetization Roadmap

### Immediate (Launch)
[Core pricing model]

### Near-term (6-12 months)
[Upsell, annual plans, add-ons]

### Medium-term (12-24 months)
[Usage-based components, marketplace, API pricing]

### Discount Strategy
[When to discount, how much, under what conditions]

## Pricing Risks
| Risk | Impact | Mitigation |
|------|--------|-----------|
| [risk] | [impact] | [strategy] |

## Implementation Checklist
1. [Step to implement recommended pricing]
2. [Step]
3. [Step]
```

## Output File
Save as: `PRICING-STRATEGY.md` in the current working directory.
