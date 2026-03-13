---
name: founder-risk
description: >
  Risk assessment and scenario planning using Deloitte risk management methodology.
  Covers 15 risks across 5 categories with probability/impact scoring, scenario
  modeling, and mitigation strategies. Use when the user types /founder risk or
  asks about risk assessment, risk analysis, scenario planning, or contingency
  planning.
---

# /founder risk -- Risk Assessment & Scenario Planning

## Purpose
Deliver a Deloitte-caliber risk assessment covering 15 risks across 5 categories, each with probability/impact scoring, early warning indicators, mitigation strategies, and contingency plans. Includes 4 scenario models (best/base/worst/black swan) with revenue impact projections.

## Trigger
User types: `/founder risk [optional: specific risk area to focus on]`

## Data Retrieval (run before any analysis)

1. **Load CONTEXT.md** if present. Extract: industry, stage, team, product, known risks, geography, regulatory environment.

2. **Load existing analyses**: Any founder skill outputs in the working directory.

3. **Run web searches** (minimum 6 queries):
   - `"[industry] startup risks failures"`
   - `"[industry] companies that failed why"`
   - `"[industry] regulatory risk 2025 2026"`
   - `"[industry] macro risk economic"`
   - `"startup [stage] common risks"`
   - `"[industry] [geography] market risk"`

4. **Fallback**: Build risk assessment from web search + CONTEXT.md data.

## Analysis Framework

### 15 Risks Across 5 Categories (minimum 3 per category)

**Market Risks (3+)**:
- Market timing (too early/too late)
- Market size overestimation
- Customer adoption slower than expected
- Demand shifts or substitution
- Geographic/cultural market mismatch

**Operational Risks (3+)**:
- Key person dependency
- Technical debt / scalability
- Supply chain / vendor dependency
- Talent acquisition and retention
- Execution speed vs. competition

**Financial Risks (3+)**:
- Runway and cash flow
- Unit economics not achieving targets
- Fundraising environment deterioration
- Currency/inflation exposure
- Revenue concentration

**Regulatory Risks (3+)**:
- Industry-specific regulation changes
- Data privacy / compliance (GDPR, HIPAA, etc.)
- Licensing requirements
- Tax/trade policy changes
- Litigation exposure

**Reputational Risks (3+)**:
- Brand damage scenarios
- Customer data breach
- Founder/team controversy
- Product failure in production
- Negative press/social media crisis

### For Each Risk, Document:
- **Description**: What the risk is, specifically
- **Probability**: 1-5 (1=unlikely, 5=near certain)
- **Impact**: 1-5 (1=minor inconvenience, 5=existential threat)
- **Risk Score**: Probability x Impact (1-25)
- **Early warning indicators**: What signals should trigger concern?
- **Mitigation strategy**: Proactive steps to reduce probability or impact
- **Contingency plan**: What to do if the risk materializes
- **Owner**: Who on the team should monitor this?

### Scenario Planning (4 scenarios)

**Best Case**: Everything goes right
- Revenue trajectory, customer growth, market conditions
- What would need to be true for this to happen?
- Probability estimate

**Base Case**: Realistic expectations
- Moderate growth, normal challenges
- Revenue trajectory
- Most likely outcomes

**Worst Case**: Multiple risks materialize
- Revenue impact, cash runway implications
- What triggers the worst case?
- Recovery strategy

**Black Swan**: Low-probability, high-impact event
- Pandemic, market crash, major competitor pivot, regulatory shock
- How to survive it
- Minimum viable operations plan

## Output Format

Save as `RISK-ASSESSMENT.md`:

```markdown
# Risk Assessment: [Company Name]
_Generated [date] | 15 risks analyzed across 5 categories_

## Executive Risk Summary
[4-5 sentences: Overall risk profile, the top 3 risks by score, and the
single most important mitigation priority for the next 90 days.]

## Risk Matrix (Sorted by Score)

| # | Risk | Category | Probability | Impact | Score | Priority |
|---|------|---------|------------|--------|-------|----------|
| 1 | [risk] | [cat] | [1-5] | [1-5] | [1-25] | Critical |
| 2 | [risk] | [cat] | [1-5] | [1-5] | [1-25] | Critical |
[...15 risks sorted by score descending]

## Detailed Risk Analysis

### Market Risks

#### 1. [Risk Name] -- Score: [X]/25
- **Description**: [2-3 sentences]
- **Probability**: [X]/5 -- [justification]
- **Impact**: [X]/5 -- [justification]
- **Early warnings**: [Observable signals that this risk is materializing]
- **Mitigation**: [Proactive steps]
- **Contingency**: [Reactive plan if it happens]
- **Owner**: [Role responsible]

[Repeat for all risks in all 5 categories]

## Scenario Analysis

### Best Case (Probability: [X]%)
**Conditions**: [What must be true]
| Metric | Month 6 | Month 12 | Month 24 |
|--------|---------|----------|----------|
| Revenue | $[X] | $[X] | $[X] |
| Customers | [X] | [X] | [X] |
| Team size | [X] | [X] | [X] |
| Runway | [X] mo | [X] mo | [X] mo |

### Base Case (Probability: [X]%)
[Same structure]

### Worst Case (Probability: [X]%)
**Trigger events**: [What would cause this]
[Same structure]
**Recovery strategy**: [How to pivot/survive]

### Black Swan (Probability: <[X]%)
**Event**: [Description]
**Impact**: [How it affects the business]
**Survival plan**: [Minimum viable operations]
**Recovery timeline**: [How long to bounce back]

## Risk Mitigation Priorities

### Immediate (Next 30 Days)
1. [Action item + risk it addresses + owner]
2. [Action item + risk it addresses + owner]
3. [Action item + risk it addresses + owner]

### Near-term (30-90 Days)
1. [Action item]
2. [Action item]
3. [Action item]

### Ongoing Monitoring
| Risk | Metric to Watch | Threshold | Frequency |
|------|----------------|-----------|-----------|
| [risk] | [metric] | [when to worry] | [how often] |

## Risk-Adjusted Decision Framework
[Guidance on how to weigh risks in upcoming decisions:
hiring, spending, product scope, market entry, fundraising timing.]
```

## Output File
Save as: `RISK-ASSESSMENT.md` in the current working directory.
