---
name: founder-raise
description: >
  Fundraising strategy playbook covering round sizing, use of funds, investor
  targeting, SAFE vs priced round analysis, dilution modeling, outreach sequencing,
  and data room checklist. Use when the user types /founder raise or asks about
  fundraising, raising capital, investor strategy, SAFE notes, term sheets,
  pitch to investors, or funding rounds.
---

# /founder raise -- Fundraising Strategy

## Purpose
Deliver a complete fundraising playbook: round sizing with rationale, use of funds breakdown, investor targeting framework, outreach sequencing, SAFE vs. priced round analysis, dilution modeling, data room checklist, and timeline to close. Output should be immediately actionable.

## Trigger
User types: `/founder raise [optional: round stage or amount]`

## Data Retrieval (run before any analysis)

1. **Load CONTEXT.md** if present. Extract: stage, traction, team, current funding, target raise, geography.

2. **Load existing analyses**: `FINANCIAL-MODEL.md`, `MARKET-SIZING.md`, `UNIT-ECONOMICS.md` if present.

3. **Run web searches** (minimum 6 queries):
   - `"[industry] [stage] funding rounds 2025"`
   - `"[industry] seed round size median 2025"`
   - `"SAFE vs priced round [stage] startup"`
   - `"[industry] active investors seed"` (or relevant stage)
   - `"[industry] startup fundraising timeline"`
   - `"post-money SAFE terms standard 2025"`

4. **If CRUNCHBASE_API_KEY is set**:
   ```bash
   python ~/.claude/scripts/founder/crunchbase_comps.py "[industry]"
   ```

5. **Fallback**: Build strategy from web search + CONTEXT.md.

## Analysis Framework

### Round Sizing
- How much to raise (based on 18-24 months runway + milestones)
- Use of funds breakdown (%, dollar amounts, timeline)
- Buffer for unexpected costs (15-20% contingency)
- Milestone-based justification: "This capital gets us to [milestone], which unlocks [next round]"

### SAFE vs. Priced Round Analysis
- When SAFE makes sense (pre-seed, seed, speed matters)
- When priced round makes sense (larger raises, strategic investors, later stage)
- Post-money SAFE mechanics and implications
- Valuation cap guidance (benchmarked to comparable rounds)
- Key terms to negotiate

### Investor Targeting Framework
- **Tier 1 (best fit)**: Investors who actively invest in the stage + industry + geography. Criteria: recent portfolio overlap, fund size match, stated thesis alignment, warm intro available.
- **Tier 2 (good fit)**: Investors who sometimes invest in the space. Broader thesis, may need more education on the market.
- **Tier 3 (worth a shot)**: Investors who are adjacent. Long shots but could be strategic.
- For each tier: how many to target, expected conversion rate, sourcing strategy.

### Outreach Sequencing
- Warm intro strategy (how to find and leverage warm connections)
- Cold outreach templates (for when no warm intro exists)
- Sequencing: who to pitch first, why, and how to create urgency
- Follow-up cadence
- Managing multiple conversations simultaneously

### Dilution Modeling
- Pre-money valuation range (benchmarked)
- Post-money valuation
- Founder ownership after this round
- Option pool requirements
- Modeling through Series A (projected dilution path)

### Data Room Checklist
Everything investors will ask for, organized and ready.

## Output Format

Save as `FUNDRAISING-STRATEGY.md`:

```markdown
# Fundraising Strategy: [Company Name]
_Generated [date] | Target: [Stage] Round_

## Executive Summary
[4-5 sentences: Recommended raise amount, instrument type, target valuation
range, timeline to close, and the key milestone this capital unlocks.]

## Round Structure

### Recommended Raise
- **Amount**: $[X]
- **Instrument**: [SAFE / Priced Round] -- [reasoning]
- **Valuation cap / Pre-money**: $[X] -- $[X] range
- **Target close**: [X] weeks from start of fundraise

### Use of Funds
| Category | Amount | % | Timeline | Milestone |
|---------|--------|---|---------|-----------|
| Engineering/Product | $[X] | [X]% | [months] | [what it builds] |
| Sales/Marketing | $[X] | [X]% | [months] | [what it achieves] |
| Operations | $[X] | [X]% | [months] | [what it enables] |
| Contingency | $[X] | [X]% | -- | Buffer |
| **Total** | **$[X]** | **100%** | | |

### Milestone Roadmap
This capital takes us from [current state] to [target state]:
| Milestone | Timeline | Metric | Unlocks |
|-----------|---------|--------|---------|
| [milestone] | Month [X] | [metric target] | [what it enables] |

## SAFE vs. Priced Round Analysis

| Factor | SAFE | Priced Round |
|--------|------|-------------|
| Speed to close | [assessment] | [assessment] |
| Legal costs | $[X]-$[X] | $[X]-$[X] |
| Investor preference | [data] | [data] |
| Complexity | [assessment] | [assessment] |
| Valuation setting | Cap only | Full valuation |
| Board seats | None | Possible |
| **Recommendation** | | |

### Key Terms Guide
[Plain-English explanation of: valuation cap, discount, MFN, pro-rata rights,
information rights, board seats, anti-dilution provisions.]

## Comparable Funding Rounds

| Company | Industry | Stage | Amount | Valuation | Date | Investors |
|---------|---------|-------|--------|-----------|------|-----------|
| [comp] | [industry] | [stage] | $[X]M | $[X]M | [date] | [investors] |
[...5-10 comparable rounds]

### Insights from Comparables
[What the data tells us about appropriate valuation, round size, and investor interest]

## Investor Targeting

### Tier 1 -- Best Fit ([X] targets)
| Investor | Type | Recent Relevant Deal | Thesis Fit | Intro Path |
|----------|------|---------------------|-----------|-----------|
| [name] | [fund type] | [deal] | [fit score] | [warm/cold] |

### Tier 2 -- Good Fit ([X] targets)
[Same structure]

### Tier 3 -- Worth a Shot ([X] targets)
[Same structure]

### Ideal Investor Profile
[What makes a perfect investor for this round: check size, expertise, network,
follow-on capacity, brand value]

## Outreach Strategy

### Sequencing Plan
1. **Weeks 1-2**: [Who to reach first and why]
2. **Weeks 3-4**: [Broader outreach]
3. **Weeks 5-6**: [Follow-ups and second meetings]
4. **Weeks 7-8**: [Term sheet negotiation]

### Warm Intro Playbook
[How to identify mutual connections, template for the ask, timing]

### Cold Outreach Template
**Subject**: [Template]
**Body**: [3-sentence template: hook, credibility, ask]

### Follow-Up Cadence
[When and how to follow up at each stage]

## Dilution Modeling

### This Round
| Metric | Low | Mid | High |
|--------|-----|-----|------|
| Pre-money valuation | $[X]M | $[X]M | $[X]M |
| Raise amount | $[X] | $[X] | $[X] |
| Post-money | $[X]M | $[X]M | $[X]M |
| Dilution this round | [X]% | [X]% | [X]% |
| Founder ownership after | [X]% | [X]% | [X]% |

### Through Series A (Projected)
| Round | Raise | Valuation | Dilution | Cumulative Founder % |
|-------|-------|-----------|---------|---------------------|
| Current round | $[X] | $[X]M | [X]% | [X]% |
| Option pool | -- | -- | [X]% | [X]% |
| Series A (proj.) | $[X]M | $[X]M | [X]% | [X]% |

## Data Room Checklist

### Must-Have (Before First Meeting)
- [ ] Pitch deck (12-15 slides)
- [ ] Executive summary (1-page)
- [ ] Financial model (3-year projection)
- [ ] Cap table (current)
- [ ] Team bios and LinkedIn profiles

### Should-Have (Before Term Sheet)
- [ ] Product demo or walkthrough
- [ ] Customer testimonials or LOIs
- [ ] Market sizing analysis
- [ ] Competitive landscape
- [ ] Incorporation documents

### Nice-to-Have (Due Diligence)
- [ ] IP documentation
- [ ] Key contracts and agreements
- [ ] Technical architecture overview
- [ ] Customer pipeline
- [ ] Reference list (customers, advisors)

## Timeline to Close
| Phase | Duration | Activities |
|-------|---------|-----------|
| Preparation | [X] weeks | [activities] |
| Outreach | [X] weeks | [activities] |
| Meetings | [X] weeks | [activities] |
| Due diligence | [X] weeks | [activities] |
| Close | [X] weeks | [activities] |
| **Total** | **[X] weeks** | |

## Common Investor Questions (with Recommended Answers)
1. **"Why now?"** -- [Framework for answering]
2. **"What's your unfair advantage?"** -- [Framework]
3. **"How do you think about competition?"** -- [Framework]
4. **"What's your biggest risk?"** -- [Framework]
5. **"What happens if you can't raise?"** -- [Framework]
```

## Output File
Save as: `FUNDRAISING-STRATEGY.md` in the current working directory.
