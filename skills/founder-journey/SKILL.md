---
name: founder-journey
description: >
  Customer journey mapping across the full lifecycle from awareness through
  loyalty and churn. Includes touchpoints, pain points, emotional curve,
  friction analysis, and optimization opportunities. Use when the user types
  /founder journey or asks about customer journey, user experience mapping,
  onboarding flow, retention strategy, or churn analysis.
---

# /founder journey -- Customer Journey Mapping

## Purpose
Map the complete customer lifecycle from first awareness through loyalty (and churn), identifying touchpoints, emotional states, pain points, and optimization opportunities at every stage. Output should be actionable for product, marketing, and customer success teams.

## Trigger
User types: `/founder journey [optional: specific stage to focus on]`

## Data Retrieval (run before any analysis)

1. **Load CONTEXT.md** if present. Extract: product, target customer, onboarding process, known pain points, current metrics.

2. **Load existing analyses**: `CUSTOMER-PERSONAS.md`, `COMPETITIVE-LANDSCAPE.md` if present.

3. **Run web searches** (minimum 5 queries):
   - `"[industry] customer journey map"`
   - `"[competitor] onboarding experience review"`
   - `"[industry] churn reasons"`
   - `"[product type] activation benchmarks"`
   - `"[industry] customer retention strategy"`

4. **Fallback**: Build journey from web search + CONTEXT.md + competitor analysis.

## Analysis Framework

Map 7 lifecycle stages. For each stage:
- Customer actions (what they do)
- Customer thoughts (what they're thinking)
- Customer emotions (what they feel -- map the emotional curve)
- Touchpoints (where interaction happens)
- Pain points (specific friction moments)
- Delight opportunities (moments to exceed expectations)
- Key metrics (what to measure)
- Recommended tools (software/platforms for this stage)
- Optimization opportunities (ranked by impact)

### Stage 1: Awareness
How does the customer first learn about the product/company?

### Stage 2: Consideration
How do they evaluate the product against alternatives?

### Stage 3: Decision
What drives the purchase/signup decision? What almost stops them?

### Stage 4: Onboarding
First 7 days. Time-to-value. Setup friction. Aha moment identification.

### Stage 5: Engagement
Active usage phase. Feature adoption. Usage patterns. Habit formation.

### Stage 6: Loyalty
What turns users into advocates? Referral behavior. Expansion revenue.

### Stage 7: Churn Risk / Recovery
Warning signs. At-risk triggers. Win-back strategies. Exit interview insights.

## Output Format

Save as `CUSTOMER-JOURNEY.md`:

```markdown
# Customer Journey Map: [Company Name]
_Generated [date] | 7 lifecycle stages mapped_

## Executive Summary
[3-4 sentences: The most critical friction point, the biggest delight
opportunity, and the #1 recommended optimization.]

## Journey Overview

| Stage | Duration | Key Metric | Benchmark | Critical Moment |
|-------|----------|-----------|-----------|-----------------|
| Awareness | [time] | [metric] | [bench] | [moment] |
| Consideration | [time] | [metric] | [bench] | [moment] |
| Decision | [time] | [metric] | [bench] | [moment] |
| Onboarding | [time] | [metric] | [bench] | [moment] |
| Engagement | [time] | [metric] | [bench] | [moment] |
| Loyalty | [time] | [metric] | [bench] | [moment] |
| Churn Risk | [time] | [metric] | [bench] | [moment] |

## Emotional Curve (Narrative)
[Narrative description of the emotional highs and lows across the journey.
Where does excitement peak? Where does frustration spike? Where is the
"aha moment"? Where do customers feel abandoned?]

## Stage 1: Awareness

### Customer Actions
- [What they do at this stage]

### Customer Thoughts
- "[What they're thinking]"

### Emotional State
[Positive/Neutral/Negative + description]

### Touchpoints
| Touchpoint | Channel | Importance | Current Quality |
|-----------|---------|-----------|----------------|
| [touchpoint] | [channel] | [H/M/L] | [1-10] |

### Pain Points
1. [Specific friction with impact]
2. [Specific friction with impact]

### Delight Opportunities
1. [Opportunity + expected impact]

### Key Metrics
- [Metric]: [benchmark]

### Recommended Tools
- [Tool]: [purpose]

### Optimization Priority
[Top optimization for this stage + expected impact]

[Repeat full structure for all 7 stages]

## Key Friction Points (Prioritized)

| # | Stage | Friction | Impact | Effort to Fix | Priority |
|---|-------|---------|--------|--------------|----------|
| 1 | [stage] | [friction] | [H/M/L] | [H/M/L] | [1-X] |
[...all major friction points]

## Optimization Roadmap

### Quick Wins (This Week)
1. [Optimization + stage + expected impact]
2. [Optimization + stage + expected impact]
3. [Optimization + stage + expected impact]

### Near-term (30 Days)
1. [Optimization + investment required]
2. [Optimization + investment required]

### Medium-term (90 Days)
1. [Optimization + investment required]
2. [Optimization + investment required]

## Metrics Dashboard
| Stage | Primary Metric | Secondary Metric | Target | Current |
|-------|---------------|-----------------|--------|---------|
| [stage] | [metric] | [metric] | [target] | [current or TBD] |
```

## Output File
Save as: `CUSTOMER-JOURNEY.md` in the current working directory.
