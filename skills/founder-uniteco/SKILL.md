---
name: founder-uniteco
description: >
  Unit economics analysis with CAC, LTV, payback period, gross margin, and
  contribution margin calculations benchmarked against industry standards.
  Includes sensitivity analysis and improvement levers. Use when the user types
  /founder uniteco or asks about unit economics, CAC, LTV, payback period,
  customer acquisition cost, lifetime value, or margins.
---

# /founder uniteco -- Unit Economics

## Purpose
Deliver VP Finance-caliber unit economics analysis with CAC by channel, LTV calculations, LTV:CAC ratio, payback period, margin analysis, industry benchmarks, sensitivity modeling, and improvement lever prioritization. Every number must show its assumptions.

## Trigger
User types: `/founder uniteco [optional: specific metric to focus on]`

## Data Retrieval (run before any analysis)

1. **Load CONTEXT.md** if present. Extract: pricing, cost structure, churn data, growth metrics, business model.

2. **Load existing analyses**: `PRICING-STRATEGY.md`, `CUSTOMER-PERSONAS.md`, `GTM-PLAYBOOK.md` if present.

3. **Run web searches** (minimum 5 queries):
   - `"[industry] CAC benchmarks 2025"`
   - `"[industry] LTV benchmarks"`
   - `"[business model type] gross margin benchmarks"`
   - `"SaaS unit economics benchmarks"` (or relevant model)
   - `"[industry] churn rate benchmarks"`

4. **Fallback**: Build from CONTEXT.md data + industry benchmarks from web search.

## Analysis Framework

### CAC Analysis (by channel)
For each acquisition channel:
- Estimated CAC = (channel spend + allocated overhead) / customers acquired
- Blended CAC across all channels
- Organic vs. paid CAC
- CAC trend direction (increasing/stable/decreasing and why)
- Benchmark comparison

### LTV Calculation
- **Method 1**: LTV = ARPU x Gross Margin % x (1 / Churn Rate)
- **Method 2**: LTV = ARPU x Gross Margin % x Average Customer Lifespan
- State all assumptions clearly
- Show monthly cohort-based calculation if data is available
- Include expansion revenue impact on LTV

### Key Ratios
- **LTV:CAC ratio**: Target >3:1 for venture-scale businesses
- **Payback period**: Months to recover CAC. Target <18 months.
- **Gross margin**: Revenue - COGS / Revenue
- **Contribution margin**: After variable costs per customer
- **Net revenue retention**: Including expansion, contraction, and churn

### Sensitivity Analysis
Model impact of changes to key variables:
- What if CAC increases 50%? 100%?
- What if churn increases 20%? 50%?
- What if ARPU increases 20%? Decreases 20%?
- What if gross margin drops 10 points?
Show the resulting LTV:CAC ratio for each scenario.

### Improvement Levers (ranked by impact)
For each lever:
- What it improves (CAC, LTV, margin, payback)
- Expected magnitude of improvement
- Implementation difficulty (Easy/Medium/Hard)
- Timeline to impact
- Priority score

## Output Format

Save as `UNIT-ECONOMICS.md`:

```markdown
# Unit Economics: [Company Name]
_Generated [date] | [Business Model Type]_

## Executive Summary
[3-4 sentences: Current unit economics health, how it compares to benchmarks,
the biggest risk, and the highest-impact improvement lever.]

## Key Metrics Overview

| Metric | Current/Estimated | Industry Benchmark | Status |
|--------|------------------|-------------------|--------|
| CAC (blended) | $[X] | $[X] | [Good/Watch/Concern] |
| LTV | $[X] | $[X] | [Good/Watch/Concern] |
| LTV:CAC | [X]:1 | >3:1 | [Good/Watch/Concern] |
| Payback period | [X] months | <18 months | [Good/Watch/Concern] |
| Gross margin | [X]% | [X]% | [Good/Watch/Concern] |
| Monthly churn | [X]% | [X]% | [Good/Watch/Concern] |
| Net revenue retention | [X]% | >100% | [Good/Watch/Concern] |

## CAC Analysis

### By Channel
| Channel | Spend | Customers | CAC | % of Total | Trend |
|---------|-------|-----------|-----|-----------|-------|
| [channel] | $[X] | [X] | $[X] | [X]% | [direction] |
| **Blended** | **$[X]** | **[X]** | **$[X]** | **100%** | |

### CAC Composition
- Marketing spend: $[X] ([X]%)
- Sales cost: $[X] ([X]%)
- Onboarding cost: $[X] ([X]%)
- Overhead allocation: $[X] ([X]%)

## LTV Analysis

### Calculation
| Component | Value | Source |
|-----------|-------|--------|
| ARPU (monthly) | $[X] | [source] |
| Gross margin | [X]% | [source] |
| Monthly churn rate | [X]% | [source/estimate] |
| Average lifespan | [X] months | 1/churn |
| **LTV** | **$[X]** | ARPU x Margin x Lifespan |

### LTV with Expansion Revenue
[If upsell/cross-sell potential exists, calculate enhanced LTV]

## Margin Analysis

### Per-Customer P&L
| Line Item | Monthly | Annual | % of Revenue |
|-----------|---------|--------|-------------|
| Revenue | $[X] | $[X] | 100% |
| COGS | $[X] | $[X] | [X]% |
| **Gross Profit** | **$[X]** | **$[X]** | **[X]%** |
| Variable opex | $[X] | $[X] | [X]% |
| **Contribution Margin** | **$[X]** | **$[X]** | **[X]%** |

## Sensitivity Analysis

### What If CAC Changes?
| CAC Scenario | CAC | LTV:CAC | Payback | Verdict |
|-------------|-----|---------|---------|---------|
| Current | $[X] | [X]:1 | [X] mo | [status] |
| +50% | $[X] | [X]:1 | [X] mo | [status] |
| +100% | $[X] | [X]:1 | [X] mo | [status] |
| -25% | $[X] | [X]:1 | [X] mo | [status] |

### What If Churn Changes?
| Churn Scenario | Churn | LTV | LTV:CAC | Verdict |
|---------------|-------|-----|---------|---------|
| Current | [X]% | $[X] | [X]:1 | [status] |
| +20% | [X]% | $[X] | [X]:1 | [status] |
| +50% | [X]% | $[X] | [X]:1 | [status] |
| -20% | [X]% | $[X] | [X]:1 | [status] |

### What If ARPU Changes?
[Same structure]

## Improvement Levers (Ranked by Impact)

| # | Lever | Improves | Expected Impact | Difficulty | Timeline | Priority |
|---|-------|---------|----------------|-----------|----------|----------|
| 1 | [lever] | [metric] | [X]% improvement | [E/M/H] | [time] | Critical |
| 2 | [lever] | [metric] | [X]% improvement | [E/M/H] | [time] | High |
[...8-10 levers]

### Lever Deep Dives
[2-3 sentences per top lever: what to do specifically, expected ROI, implementation notes]

## Benchmark Comparison

| Metric | [Company] | Top Quartile | Median | Bottom Quartile |
|--------|-----------|-------------|--------|----------------|
| CAC | $[X] | $[X] | $[X] | $[X] |
| LTV | $[X] | $[X] | $[X] | $[X] |
| LTV:CAC | [X]:1 | [X]:1 | [X]:1 | [X]:1 |
| Payback | [X] mo | [X] mo | [X] mo | [X] mo |
| Gross Margin | [X]% | [X]% | [X]% | [X]% |

## Key Assumptions & Risks
[List every assumption with its sensitivity]

## 90-Day Unit Economics Improvement Plan
1. [Priority action + expected metric improvement]
2. [Priority action + expected metric improvement]
3. [Priority action + expected metric improvement]
```

## Output File
Save as: `UNIT-ECONOMICS.md` in the current working directory.
