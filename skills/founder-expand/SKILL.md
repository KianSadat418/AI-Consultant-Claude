---
name: founder-expand
description: >
  Market entry and expansion strategy with market attractiveness scoring, entry
  mode analysis, localization requirements, and 12-month entry roadmap. Use when
  the user types /founder expand or asks about market expansion, international
  entry, new market strategy, geographic expansion, or market entry planning.
---

# /founder expand -- Market Entry & Expansion

## Purpose
Deliver a global expansion strategy with market attractiveness scoring, entry mode analysis (direct/partnership/acquisition/licensing/digital-first), localization requirements, and a 12-month entry roadmap with investment estimates and success KPIs.

## Trigger
User types: `/founder expand [optional: target market or region]`

## Data Retrieval (run before any analysis)

1. **Load CONTEXT.md** if present. Extract: current markets, product, target expansion markets, industry.

2. **Load existing analyses**: `MARKET-SIZING.md`, `COMPETITIVE-LANDSCAPE.md`, `RISK-ASSESSMENT.md` if present.

3. **Run web searches** (minimum 6 queries):
   - `"[target market] market size [industry]"`
   - `"[target market] regulatory environment [industry]"`
   - `"[target market] consumer behavior [industry]"`
   - `"[industry] companies successfully entered [target market]"`
   - `"[target market] business registration requirements"`
   - `"[target market] competitive landscape [industry]"`

4. **Fallback**: Build from web search + CONTEXT.md.

## Analysis Framework

### Market Attractiveness Scoring
Score each target market on 5 dimensions (1-10 each, weighted):
- **Market size** (25%): Current TAM and growth rate in the target market
- **Growth rate** (20%): Projected CAGR and momentum
- **Competition** (20%): How crowded, how strong incumbents are
- **Regulation** (20%): Ease of doing business, regulatory burden
- **Accessibility** (15%): Language, culture, distribution, payment infrastructure

### Entry Mode Analysis
For each viable entry mode:
- **Direct entry**: Set up own operations. Pros, cons, cost, timeline.
- **Partnership**: Local distribution/channel partner. Pros, cons, cost, timeline.
- **Acquisition**: Buy a local player. Pros, cons, cost, timeline.
- **Licensing**: License to local operator. Pros, cons, cost, timeline.
- **Digital-first**: Launch digitally, minimal local presence. Pros, cons, cost, timeline.

### Localization Requirements
- Language and content localization
- Currency and payment methods
- Legal/compliance localization
- Cultural adaptation (product, marketing, support)
- Local hiring needs
- Tax and financial reporting

### 12-Month Entry Roadmap
Month-by-month plan from decision to established presence.

## Output Format

Save as `MARKET-ENTRY.md`:

```markdown
# Market Entry Strategy: [Company Name] -> [Target Market]
_Generated [date]_

## Executive Summary
[4-5 sentences: Target market opportunity, recommended entry mode,
investment required, expected timeline to meaningful traction.]

## Market Attractiveness Scorecard

| Dimension | Weight | Score (1-10) | Weighted Score | Evidence |
|-----------|--------|-------------|---------------|----------|
| Market size | 25% | [X] | [X] | [data] |
| Growth rate | 20% | [X] | [X] | [data] |
| Competition | 20% | [X] | [X] | [data] |
| Regulation | 20% | [X] | [X] | [data] |
| Accessibility | 15% | [X] | [X] | [data] |
| **Total** | **100%** | | **[X]/10** | |

### Market Verdict
[Interpret the score: what it means for entry timing and strategy]

## Entry Mode Recommendation

### Recommended: [Mode]
**Why**: [Clear reasoning]

### Entry Mode Comparison
| Factor | Direct | Partnership | Acquisition | Licensing | Digital-First |
|--------|--------|-----------|------------|----------|--------------|
| Setup cost | $[X] | $[X] | $[X] | $[X] | $[X] |
| Time to market | [X] mo | [X] mo | [X] mo | [X] mo | [X] mo |
| Control level | [H/M/L] | [H/M/L] | [H/M/L] | [H/M/L] | [H/M/L] |
| Revenue potential | [H/M/L] | [H/M/L] | [H/M/L] | [H/M/L] | [H/M/L] |
| Risk level | [H/M/L] | [H/M/L] | [H/M/L] | [H/M/L] | [H/M/L] |
| **Recommendation** | | | | | |

## Localization Checklist
- [ ] [Item with estimated cost and timeline]
[...complete checklist]

## 12-Month Entry Roadmap

| Month | Phase | Key Activities | Investment | Milestone |
|-------|-------|---------------|-----------|-----------|
| 1 | Research | [activities] | $[X] | [milestone] |
| 2-3 | Setup | [activities] | $[X] | [milestone] |
| 4-6 | Soft launch | [activities] | $[X] | [milestone] |
| 7-9 | Growth | [activities] | $[X] | [milestone] |
| 10-12 | Scale | [activities] | $[X] | [milestone] |

## Investment Summary
| Category | Amount | Timeline |
|---------|--------|---------|
| [category] | $[X] | [when] |
| **Total** | **$[X]** | |

## Success KPIs
| KPI | Month 6 Target | Month 12 Target |
|-----|---------------|----------------|
| [metric] | [target] | [target] |

## Risks & Mitigation
| Risk | Probability | Impact | Mitigation |
|------|-----------|--------|-----------|
| [risk] | [H/M/L] | [H/M/L] | [strategy] |
```

## Output File
Save as: `MARKET-ENTRY.md` in the current working directory.
