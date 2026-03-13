---
name: founder-model
description: >
  3-year financial projection with monthly Year 1 detail and quarterly Years 2-3.
  Covers revenue modeling, cost structure, break-even analysis, cash flow,
  and scenario planning. Use when the user types /founder model or asks about
  financial projections, revenue model, financial forecast, burn rate, cash flow,
  or break-even analysis.
---

# /founder model -- Financial Modeling & Projections

## Purpose
Build a 3-year financial model with monthly granularity for Year 1 and quarterly for Years 2-3. Includes revenue model, cost structure, break-even analysis, cash flow forecast, burn rate tracking, and 3-scenario planning. Every assumption must be stated and justified.

## Trigger
User types: `/founder model [optional: specific financial question]`

## Data Retrieval (run before any analysis)

1. **Load CONTEXT.md** if present. Extract: revenue, pricing, team size, cost structure, traction, fundraising.

2. **Load existing analyses**: `UNIT-ECONOMICS.md`, `PRICING-STRATEGY.md`, `MARKET-SIZING.md` if present.

3. **Run web searches** (minimum 5 queries):
   - `"[industry] startup growth rates by stage"`
   - `"[industry] revenue multiples 2025"`
   - `"[stage] startup burn rate benchmarks"`
   - `"[business model] SaaS financial model benchmarks"` (or relevant model)
   - `"[industry] comparable company financials"`

4. **Fallback**: Build projections from CONTEXT.md + benchmarks + unit economics.

## Analysis Framework

### Revenue Model
- Define revenue streams (subscriptions, transactions, services, etc.)
- Monthly revenue = Customers x ARPU (show customer growth assumptions)
- Customer growth model: acquisition rate, churn rate, expansion revenue
- Revenue recognition timing
- Seasonal adjustments if applicable

### Cost Structure
**Fixed Costs (Monthly)**:
- Salaries and benefits (by role and hire timing)
- Office/workspace
- Software and tools
- Insurance and legal
- Other overhead

**Variable Costs (Per Customer/Unit)**:
- Hosting/infrastructure
- Customer support
- Payment processing
- Third-party APIs
- COGS components

### Key Metrics to Track Monthly
- MRR/ARR
- Customer count (new, churned, net)
- Burn rate (gross and net)
- Runway (months remaining)
- Gross margin
- CAC (if spend data available)
- Revenue per employee

### Break-Even Analysis
- Monthly break-even point (revenue = costs)
- Customer count needed for break-even
- Timeline to break-even for each scenario
- Cash needed to reach break-even

### Cash Flow Forecast
- Starting cash position
- Monthly cash inflows (revenue + funding)
- Monthly cash outflows (costs + capex)
- Ending cash position
- Runway remaining

### 3 Scenarios
- **Best case**: Aggressive growth assumptions. What needs to go right?
- **Base case**: Moderate, realistic assumptions. Most likely outcome.
- **Worst case**: Slow growth, higher costs, longer sales cycles.

## Output Format

Save as `FINANCIAL-MODEL.md`:

```markdown
# Financial Model: [Company Name]
_Generated [date] | 3-Year Projection_

## Executive Summary
[4-5 sentences: Revenue trajectory, break-even timeline, cash needs,
and the key assumption that most impacts the model.]

## Key Assumptions

| Assumption | Base Case | Best Case | Worst Case | Source |
|-----------|-----------|-----------|------------|--------|
| Monthly customer growth | [X]% | [X]% | [X]% | [source] |
| Monthly churn | [X]% | [X]% | [X]% | [source] |
| ARPU | $[X] | $[X] | $[X] | [source] |
| Gross margin | [X]% | [X]% | [X]% | [source] |
| First hire month | Month [X] | Month [X] | Month [X] | Plan |
| Monthly burn rate (start) | $[X]K | $[X]K | $[X]K | Plan |

## Year 1 -- Monthly Projections (Base Case)

| Month | Customers | New | Churned | MRR | Costs | Net Burn | Runway |
|-------|----------|-----|---------|-----|-------|---------|--------|
| 1 | [X] | [X] | [X] | $[X] | $[X] | $[X] | [X] mo |
| 2 | [X] | [X] | [X] | $[X] | $[X] | $[X] | [X] mo |
| 3 | [X] | [X] | [X] | $[X] | $[X] | $[X] | [X] mo |
| 4 | [X] | [X] | [X] | $[X] | $[X] | $[X] | [X] mo |
| 5 | [X] | [X] | [X] | $[X] | $[X] | $[X] | [X] mo |
| 6 | [X] | [X] | [X] | $[X] | $[X] | $[X] | [X] mo |
| 7 | [X] | [X] | [X] | $[X] | $[X] | $[X] | [X] mo |
| 8 | [X] | [X] | [X] | $[X] | $[X] | $[X] | [X] mo |
| 9 | [X] | [X] | [X] | $[X] | $[X] | $[X] | [X] mo |
| 10 | [X] | [X] | [X] | $[X] | $[X] | $[X] | [X] mo |
| 11 | [X] | [X] | [X] | $[X] | $[X] | $[X] | [X] mo |
| 12 | [X] | [X] | [X] | $[X] | $[X] | $[X] | [X] mo |

## Years 2-3 -- Quarterly Projections (Base Case)

| Quarter | Customers | MRR | ARR Run Rate | Costs | Gross Margin | Net Burn |
|---------|----------|-----|-------------|-------|-------------|---------|
| Y2 Q1 | [X] | $[X]K | $[X]K | $[X]K | [X]% | $[X]K |
| Y2 Q2 | [X] | $[X]K | $[X]K | $[X]K | [X]% | $[X]K |
| Y2 Q3 | [X] | $[X]K | $[X]K | $[X]K | [X]% | $[X]K |
| Y2 Q4 | [X] | $[X]K | $[X]K | $[X]K | [X]% | $[X]K |
| Y3 Q1 | [X] | $[X]K | $[X]K | $[X]K | [X]% | $[X]K |
| Y3 Q2 | [X] | $[X]K | $[X]K | $[X]K | [X]% | $[X]K |
| Y3 Q3 | [X] | $[X]K | $[X]K | $[X]K | [X]% | $[X]K |
| Y3 Q4 | [X] | $[X]K | $[X]K | $[X]K | [X]% | $[X]K |

## Cost Structure

### Fixed Costs (Monthly at Steady State)
| Category | Amount | Notes |
|---------|--------|-------|
| Salaries & benefits | $[X] | [headcount plan reference] |
| Office/workspace | $[X] | [type] |
| Software & tools | $[X] | [key tools] |
| Insurance & legal | $[X] | |
| Other overhead | $[X] | |
| **Total Fixed** | **$[X]** | |

### Variable Costs (Per Customer/Month)
| Category | Amount | % of Revenue |
|---------|--------|-------------|
| Hosting/infrastructure | $[X] | [X]% |
| Support | $[X] | [X]% |
| Payment processing | $[X] | [X]% |
| Other COGS | $[X] | [X]% |
| **Total Variable** | **$[X]** | **[X]%** |

### Headcount Plan
| Role | Hire Month | Monthly Cost | Cumulative |
|------|-----------|-------------|-----------|
| [role] | Month [X] | $[X] | [X] employees |

## Break-Even Analysis
- **Break-even MRR**: $[X]
- **Break-even customers**: [X]
- **Timeline to break-even**: Month [X] (base case)
- **Cash needed to reach break-even**: $[X]

## Cash Flow Forecast

| Period | Starting Cash | Revenue | Costs | Funding | Ending Cash | Runway |
|--------|-------------|---------|-------|---------|------------|--------|
[Monthly for Year 1, quarterly for Years 2-3]

## Scenario Comparison

| Metric | Best | Base | Worst |
|--------|------|------|-------|
| Y1 ending ARR | $[X] | $[X] | $[X] |
| Y2 ending ARR | $[X] | $[X] | $[X] |
| Y3 ending ARR | $[X] | $[X] | $[X] |
| Break-even month | [X] | [X] | [X] |
| Total cash needed | $[X] | $[X] | $[X] |
| Y3 gross margin | [X]% | [X]% | [X]% |
| Y3 headcount | [X] | [X] | [X] |

## Benchmark Comparison
| Metric | [Company] | Top Quartile | Median |
|--------|-----------|-------------|--------|
| Y1 growth rate | [X]% | [X]% | [X]% |
| Gross margin | [X]% | [X]% | [X]% |
| Burn multiple | [X]x | [X]x | [X]x |
| Revenue/employee | $[X]K | $[X]K | $[X]K |

## Red Flags
[Conditions that should trigger concern and strategic response]

## Key Risks to the Model
[Which assumptions, if wrong, would most impact the projections]
```

## Output File
Save as: `FINANCIAL-MODEL.md` in the current working directory.
