---
name: founder-equity
description: >
  Cap table modeling and equity structuring covering co-founder splits, vesting
  schedules, option pool sizing, and dilution modeling through multiple rounds.
  Use when the user types /founder equity or asks about equity splits, cap table,
  vesting, option pool, dilution, co-founder equity, or stock options.
---

# /founder equity -- Cap Table & Equity Structuring

## Purpose
Deliver comprehensive equity planning: co-founder split frameworks, vesting schedule design, option pool sizing, cap table modeling through Series A, and dilution projections. Every recommendation backed by industry benchmarks.

## Trigger
User types: `/founder equity [optional: specific equity question]`

## Data Retrieval (run before any analysis)

1. **Load CONTEXT.md** if present. Extract: team structure, co-founder roles, stage, fundraising plans, existing equity arrangements.

2. **Load existing analyses**: `FUNDRAISING-STRATEGY.md`, `LEGAL-STRUCTURE.md` if present.

3. **Run web searches** (minimum 5 queries):
   - `"[stage] equity split benchmarks founders"`
   - `"startup vesting schedule best practices 2025"`
   - `"[stage] option pool size standard"`
   - `"startup equity dilution by round benchmarks"`
   - `"[investor type] standard equity terms"`

4. **Fallback**: Build from web search + CONTEXT.md.

## Analysis Framework

### Co-Founder Equity Split
- Equal vs. contribution-based split analysis
- Factors: idea origination, full-time commitment timing, cash investment, domain expertise, CEO role, prior exits
- Slicing Pie dynamic equity framework overview
- Recommendation with clear reasoning
- Common mistakes to avoid

### Vesting Schedule Design
- Standard 4-year / 1-year cliff and why it exists
- Acceleration triggers (single vs. double trigger)
- Founder-specific vesting considerations
- Advisor vesting (typically 2-year, monthly)
- Employee vesting variations
- 83(b) election importance and timing

### Option Pool Sizing
- Pre-seed through Series A benchmarks (typically 10-20%)
- Pre-money vs. post-money option pool creation
- Investor expectations by stage
- Hiring plan alignment (how many options needed for planned hires)
- Refresh grants and annual pool expansion

### Cap Table Modeling
- Current state cap table
- Post-seed/pre-seed modeling
- Post-Series A projection
- Common vs. preferred stock implications
- Convertible note / SAFE conversion mechanics

### Dilution Modeling
- Round-by-round dilution projections
- How option pool refreshes affect founder ownership
- Anti-dilution protection mechanics
- Maintaining control (voting rights, board composition)

## Output Format

Save as `EQUITY-STRUCTURE.md`:

```markdown
# Equity Structure: [Company Name]
_Generated [date]_

> **DISCLAIMER**: This document is for informational purposes only and does not
> constitute legal or financial advice. Consult qualified legal and financial
> advisors before making equity decisions.

## Executive Summary
[3-4 sentences: Recommended equity structure, key decisions to make now,
and the most important thing to get right at this stage.]

## Co-Founder Equity Split

### Recommended Split
| Founder | Role | Equity % | Rationale |
|---------|------|---------|-----------|
| [Founder 1] | [role] | [X]% | [why] |
| [Founder 2] | [role] | [X]% | [why] |
| Option pool | -- | [X]% | [for hires] |

### Split Analysis Framework
| Factor | Weight | [F1] Score | [F2] Score |
|--------|--------|-----------|-----------|
| Idea origination | [X]% | [1-10] | [1-10] |
| Full-time commitment | [X]% | [1-10] | [1-10] |
| Domain expertise | [X]% | [1-10] | [1-10] |
| Cash contribution | [X]% | [1-10] | [1-10] |
| Network/relationships | [X]% | [1-10] | [1-10] |
| CEO/leadership | [X]% | [1-10] | [1-10] |

### Common Mistakes
[What founders get wrong about equity splits and how to avoid it]

## Vesting Schedule

### Recommended Structure
- **Schedule**: 4-year vesting, 1-year cliff
- **Cliff**: 25% vests at 12 months, then monthly thereafter
- **Acceleration**: [Single/Double trigger recommendation]
- **83(b) election**: MUST file within 30 days of grant

### Vesting Timeline
| Month | Vested % | Unvested % | Notes |
|-------|---------|-----------|-------|
| 0 | 0% | 100% | Grant date |
| 12 | 25% | 75% | Cliff vests |
| 24 | 50% | 50% | |
| 36 | 75% | 25% | |
| 48 | 100% | 0% | Fully vested |

### Advisor Equity
| Advisor Type | Equity Range | Vesting | Notes |
|-------------|-------------|---------|-------|
| Strategic advisor (heavy) | 0.5%-1.0% | 2yr monthly | Weekly engagement |
| Advisory board | 0.25%-0.5% | 2yr monthly | Monthly engagement |
| Light advisor | 0.1%-0.25% | 2yr monthly | Quarterly engagement |

## Option Pool

### Recommended Pool Size: [X]%
- **Current stage benchmark**: [X]% ([source])
- **Hiring plan needs**: [X] hires x [X]% average = [X]%
- **Buffer for unplanned hires**: [X]%
- **Investor expectation**: [X]% pre-money option pool

### Option Grant Ranges by Role
| Role | Equity Range | Typical Grant |
|------|-------------|--------------|
| VP/C-level (early) | 1-3% | [X]% |
| Director/Lead | 0.25-1% | [X]% |
| Senior engineer | 0.1-0.5% | [X]% |
| Junior hire | 0.01-0.1% | [X]% |

## Cap Table

### Current State
| Shareholder | Shares | % Ownership | Type |
|-----------|--------|------------|------|
| [Founder 1] | [X] | [X]% | Common |
| [Founder 2] | [X] | [X]% | Common |
| Option pool (unallocated) | [X] | [X]% | Reserved |
| **Total** | **[X]** | **100%** | |

### Post-Seed (Projected)
| Shareholder | Shares | % Ownership | Type |
|-----------|--------|------------|------|
| [Founder 1] | [X] | [X]% | Common |
| [Founder 2] | [X] | [X]% | Common |
| Seed investors | [X] | [X]% | [SAFE/Preferred] |
| Option pool | [X] | [X]% | Reserved |
| **Total** | **[X]** | **100%** | |

### Post-Series A (Projected)
[Same structure with Series A investors added]

## Dilution Projections

| Round | Raise | Valuation | Round Dilution | Founder 1 % | Founder 2 % |
|-------|-------|-----------|---------------|-------------|-------------|
| Formation | -- | -- | -- | [X]% | [X]% |
| Option pool | -- | -- | [X]% | [X]% | [X]% |
| Pre-seed/Seed | $[X] | $[X]M | [X]% | [X]% | [X]% |
| Pool refresh | -- | -- | [X]% | [X]% | [X]% |
| Series A | $[X]M | $[X]M | [X]% | [X]% | [X]% |

### Key Insight
[What the dilution path means for the founders. Benchmark against
successful outcomes -- "At Series A, founders of successful companies
typically retain [X]% combined."]

## Red Flags to Avoid
1. [Common equity mistake + why it's dangerous + how to prevent]
2. [Common equity mistake + why it's dangerous + how to prevent]
3. [Common equity mistake + why it's dangerous + how to prevent]
4. [Common equity mistake + why it's dangerous + how to prevent]
5. [Common equity mistake + why it's dangerous + how to prevent]

## Next Steps
[Prioritized action items for equity structure, in order of urgency]
```

## Output File
Save as: `EQUITY-STRUCTURE.md` in the current working directory.
