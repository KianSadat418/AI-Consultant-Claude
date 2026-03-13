---
name: founder-gtm
description: >
  Go-to-market strategy playbook with CSO-level planning covering acquisition
  channels, messaging frameworks, content strategy, partnership opportunities,
  and KPI frameworks. Use when the user types /founder gtm or asks about
  go-to-market strategy, customer acquisition, launch plan, growth strategy,
  or marketing channels.
---

# /founder gtm -- Go-To-Market Strategy

## Purpose
Deliver a CSO-level GTM playbook with phased launch plan, channel rankings by expected ROI, messaging framework, content strategy by funnel stage, partnership opportunities, and a complete KPI framework with benchmarks. Actionable enough to execute on Monday morning.

## Trigger
User types: `/founder gtm [optional: specific market or launch context]`

## Data Retrieval (run before any analysis)

1. **Load CONTEXT.md** if present. Extract: product, target customer, stage, traction, competitors, geography, pricing, team.

2. **Load existing analyses** if present in working directory:
   - `CUSTOMER-PERSONAS.md` (for targeting)
   - `COMPETITIVE-LANDSCAPE.md` (for differentiation)
   - `MARKET-SIZING.md` (for market context)

3. **Run web searches** (minimum 6 queries):
   - `"[industry] customer acquisition channels"`
   - `"[competitor] marketing strategy"`
   - `"[industry] CAC benchmarks 2025"`
   - `"[product type] go to market case study"`
   - `"[industry] content marketing strategy B2B"` (or B2C)
   - `"[industry] partnership growth strategy"`

4. **Fallback**: Build GTM from web search + CONTEXT.md + any existing analyses.

## Analysis Framework

### Phase 1: Pre-Launch (0-30 Days Before Launch)
- **Audience definition**: Who exactly are the first 100 customers? (Use persona data if available)
- **Positioning statement**: For [target customer] who [need], [product] is a [category] that [key benefit]. Unlike [competitor], we [key differentiator].
- **Pre-launch list building**: Strategies for building a waitlist/early access list
- **Beta program design**: How to structure early feedback loops
- **PR and awareness**: Press, community seeding, founder-led content

### Phase 2: Launch (Day 0-90)
- **Launch sequence**: Week-by-week plan for the first 90 days
- **Channel activation**: Which channels to light up first and why
- **Launch amplifiers**: Product Hunt, Hacker News, Twitter/X, LinkedIn, press, community partnerships
- **Founder-led sales**: Playbook for the first 50 deals
- **Quick wins**: Low-cost, high-impact activities for week 1

### Phase 3: Post-Launch (90+ Days)
- **Channel scaling**: How to double down on what works
- **Paid acquisition strategy**: When to start, where to spend, budget allocation
- **Content engine**: Sustainable content strategy
- **Referral and viral loops**: How to build network effects into growth
- **Sales process maturation**: From founder-led to first sales hire

### Channel Ranking (7 channels, ranked by expected ROI)
For each channel, provide:
- **Channel name and type** (paid, organic, outbound, community, partnership, etc.)
- **Expected CAC range**: Based on industry benchmarks
- **Time to results**: How long before meaningful traction
- **Scalability**: Can this grow to $1M+ ARR or is it capped?
- **Resource requirement**: People, tools, budget needed
- **Confidence level**: High/Medium/Low based on evidence
- **Recommended budget allocation**: % of total marketing budget
- **Quick win version**: Minimum viable test of this channel

### Messaging Framework
- **Core value proposition**: 1 sentence
- **3 supporting messages**: Each with a proof point or data point
- **Message by persona**: Tailored value prop per persona
- **Message by funnel stage**:
  - Awareness: What gets attention
  - Consideration: What builds trust
  - Decision: What drives conversion
- **Objection handling scripts**: Top 5 objections with responses

### Content Strategy by Funnel Stage
- **Top of funnel**: Thought leadership, SEO articles, social content. Topics + formats + frequency.
- **Middle of funnel**: Case studies, comparison guides, webinars. Topics + formats + frequency.
- **Bottom of funnel**: Demos, ROI calculators, pilot proposals. Format + delivery.
- **Post-purchase**: Onboarding sequences, success stories, community. Format + cadence.

### Partnership Opportunities
- **Distribution partnerships**: Companies with access to your target customers
- **Integration partnerships**: Products that complement yours
- **Co-marketing partnerships**: Non-competitive companies targeting same audience
- **Channel partnerships**: Resellers, consultants, agencies
For each: company name (or type), mutual value, effort level, expected impact.

## Output Format

Save as `GTM-PLAYBOOK.md`:

```markdown
# Go-To-Market Playbook: [Company Name]
_Generated [date] | Stage: [Company Stage]_

## Executive Summary
[4-5 sentences: The GTM strategy in brief. Lead with the #1 channel bet
and the expected timeline to first meaningful traction.]

## Positioning
**For** [target customer] **who** [need/pain],
**[Product]** is a [category] that [key benefit].
**Unlike** [competitor/alternative], we [key differentiator].

## Pre-Launch Plan (T-30 to T-0)

### First 100 Customers
[Who they are, where they are, how to reach them]

### Waitlist / Early Access Strategy
[Specific tactics with expected results]

### Beta Program Design
[Structure, feedback loops, success criteria]

### Pre-Launch Content & PR
[What to publish, where, timeline]

## Launch Plan (Day 0-90)

### Week-by-Week Execution Plan
| Week | Focus | Key Activities | Target Metrics |
|------|-------|---------------|---------------|
| 1 | [focus] | [activities] | [metrics] |
| 2-4 | [focus] | [activities] | [metrics] |
| 5-8 | [focus] | [activities] | [metrics] |
| 9-12 | [focus] | [activities] | [metrics] |

### Quick Wins (Week 1)
1. [High-impact, low-effort activity]
2. [High-impact, low-effort activity]
3. [High-impact, low-effort activity]
4. [High-impact, low-effort activity]
5. [High-impact, low-effort activity]

## Channel Rankings

| Rank | Channel | Type | Est. CAC | Time to Results | Scale Potential | Budget % |
|------|---------|------|----------|----------------|----------------|----------|
| 1 | [channel] | [type] | $[X] | [time] | [potential] | [X]% |
| 2 | [channel] | [type] | $[X] | [time] | [potential] | [X]% |
[...7 channels]

### Channel Deep Dives

#### 1. [Top Channel]
- **Why #1**: [Evidence-based reasoning]
- **Quick win test**: [Minimum viable experiment, $[X] budget, [X] week timeline]
- **Scale plan**: [How to go from test to full deployment]
- **Tools needed**: [Specific tools/platforms]
- **Benchmark CAC**: $[X] (industry: $[X])

[Repeat for top 3-4 channels]

## Messaging Framework

### Core Value Proposition
[1 clear sentence]

### Supporting Messages
1. [Message + proof point]
2. [Message + proof point]
3. [Message + proof point]

### Message by Persona
| Persona | Hook | Value Prop | Proof Point |
|---------|------|-----------|-------------|
| [Persona 1] | [hook] | [value] | [proof] |
| [Persona 2] | [hook] | [value] | [proof] |

### Objection Handling
| Objection | Response | Proof Point |
|-----------|---------|-------------|
| "[objection]" | [response] | [evidence] |

## Content Strategy

### Content Calendar (First 90 Days)
| Week | TOFU | MOFU | BOFU |
|------|------|------|------|
| 1-4 | [content] | [content] | [content] |
| 5-8 | [content] | [content] | [content] |
| 9-12 | [content] | [content] | [content] |

### Recommended Content Formats
[Prioritized list with rationale]

## Partnership Opportunities

| Partner Type | Target Company/Type | Mutual Value | Effort | Impact |
|-------------|-------------------|-------------|--------|--------|
| [type] | [target] | [value exchange] | [H/M/L] | [H/M/L] |

## KPI Framework

| Metric | Benchmark | Month 1 Target | Month 3 Target | Month 6 Target |
|--------|-----------|---------------|---------------|---------------|
| Website visitors | [industry avg] | [target] | [target] | [target] |
| Sign-ups/leads | [benchmark] | [target] | [target] | [target] |
| Activation rate | [benchmark] | [target] | [target] | [target] |
| CAC | $[industry avg] | $[target] | $[target] | $[target] |
| MRR | [stage benchmark] | $[target] | $[target] | $[target] |
[...10 metrics total]

## Top 5 Launch Risks & Contingencies
| Risk | Probability | Impact | Contingency |
|------|------------|--------|------------|
| [risk] | [H/M/L] | [H/M/L] | [backup plan] |

## Budget Allocation
[Monthly marketing budget recommendation with allocation by channel and activity]

## 90-Day Success Criteria
[What "good" looks like at 30, 60, and 90 days. Specific, measurable targets.]
```

## Output File
Save as: `GTM-PLAYBOOK.md` in the current working directory.
