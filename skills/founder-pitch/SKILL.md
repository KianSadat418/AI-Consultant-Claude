---
name: founder-pitch
description: >
  Pitch deck narrative builder with slide-by-slide brief, talking points,
  investor Q&A prep, and executive summary for cold emails. Uses narrative arc
  methodology from top seed investors. Use when the user types /founder pitch
  or asks about pitch deck, investor presentation, pitch narrative, or fundraising
  deck.
---

# /founder pitch -- Pitch Deck Builder

## Purpose
Create a complete pitch deck narrative brief: slide-by-slide content with talking points, key metrics placement, storytelling arc, investor Q&A preparation, and a 3-sentence executive summary for cold emails. Uses the narrative arc methodology favored by top seed-stage investors.

## Trigger
User types: `/founder pitch [optional: target investor or round context]`

## Data Retrieval (run before any analysis)

1. **Load CONTEXT.md** if present. Extract all available company data.

2. **Load ALL existing analysis files** in the working directory (any founder skill outputs). The pitch deck should synthesize everything available.

3. **Run web searches** (minimum 4 queries):
   - `"[industry] pitch deck examples successful"`
   - `"[stage] startup pitch deck best practices 2025"`
   - If target investor named: `"[investor name] portfolio thesis"`
   - `"[industry] investor questions common"`

4. **Fallback**: Build pitch narrative from CONTEXT.md + web search.

## Analysis Framework

### Narrative Arc
The pitch follows a hero's journey structure:
1. **The World Has a Problem** (Slides 1-2): Establish stakes
2. **We Have the Solution** (Slides 3-4): Show the answer
3. **The Market is Massive** (Slide 5): Prove it's worth doing
4. **We're Already Winning** (Slides 6-7): Show momentum
5. **Here's How We Win Big** (Slides 8-9): Strategy and competitive edge
6. **The Team That Makes It Happen** (Slide 10): Why this team
7. **The Ask** (Slides 11-12): What you need and what you'll do with it

### Slide-by-Slide Brief (12 Slides)

**Slide 1: Title / Hook**
- Company name, one-line description, logo placeholder
- A compelling one-liner that makes someone lean in

**Slide 2: Problem**
- The problem in the customer's words
- Scale of the problem (how many people, how much money wasted)
- Why now (why hasn't this been solved before?)
- Emotional hook: make the investor feel the pain

**Slide 3: Solution**
- What the product does in 1 sentence
- 3 key capabilities
- Screenshot or product visual placeholder
- "Before vs. After" transformation

**Slide 4: Product / Demo**
- Product walkthrough highlights
- Key UX moments
- Technical differentiator if relevant
- Customer quote if available

**Slide 5: Market Size**
- TAM / SAM / SOM (pull from MARKET-SIZING.md if available)
- Growth rate
- "Why this market, why now" in 1 sentence

**Slide 6: Business Model**
- Revenue model (how you make money)
- Pricing tiers (pull from PRICING-STRATEGY.md if available)
- Unit economics snapshot (CAC, LTV, margins)

**Slide 7: Traction**
- The most impressive metrics: revenue, users, growth rate, retention
- Key milestones achieved
- Social proof: logos, testimonials, press
- Momentum graph (up and to the right)

**Slide 8: Competition**
- Positioning map or 2x2 matrix
- Why you win (not "they suck" but "our approach is fundamentally different")
- Moats and defensibility

**Slide 9: Go-To-Market**
- How you acquire customers
- Top channels and early results
- Expansion strategy

**Slide 10: Team**
- Founder(s) with relevant background
- Key hires and advisory board
- "Why this team wins" narrative
- Team gaps you're hiring for (shows self-awareness)

**Slide 11: Financials**
- 3-year revenue projection (pull from FINANCIAL-MODEL.md if available)
- Key assumptions (2-3 most important)
- Path to profitability or next fundraise milestone

**Slide 12: The Ask**
- Amount raising
- Use of funds (3-4 buckets)
- Key milestones this capital unlocks
- Call to action

### Appendix Slides (3-5 extra)
- Detailed financials
- Product roadmap
- Customer case study
- Technical architecture
- Regulatory/compliance details

## Output Format

Save as `PITCH-DECK-BRIEF.md`:

```markdown
# Pitch Deck Brief: [Company Name]
_Generated [date] | [Stage] Round | Target: $[X]_

## 3-Sentence Executive Summary (For Cold Emails)
[Sentence 1: What the company does and for whom]
[Sentence 2: Key traction or validation metric]
[Sentence 3: What you're raising and the milestone it unlocks]

## Narrative Arc
[2-3 paragraphs telling the company story as a narrative, not bullet points.
This is the "script" for presenting the deck verbally.]

## Slide-by-Slide Brief

### Slide 1: [Company Name]
**Headline**: [Compelling one-liner]
**Content**:
- [What to put on this slide]
**Talking points**:
- [What to say when presenting this slide]
**Key metric to highlight**: [if applicable]

### Slide 2: The Problem
**Headline**: [Problem statement in customer's words]
**Content**:
- [Problem description]
- [Scale: X people affected, $Y wasted annually]
- [Why now: market timing justification]
**Talking points**:
- [Opening story or anecdote]
- [Data point that makes the room lean in]
**Emotional hook**: [The moment that makes this real]

### Slide 3: The Solution
**Headline**: [Solution in 1 sentence]
**Content**:
- [3 key capabilities]
- [Before/after transformation]
**Talking points**:
- [Demo walkthrough script]
- [Customer quote or reaction]
**Key metric**: [If applicable]

[Continue for all 12 slides + appendix slides with same detail level]

## Key Metrics to Highlight Throughout
| Metric | Value | Where to Use | Why It Matters |
|--------|-------|-------------|---------------|
| [metric] | [value] | Slide [X] | [investor significance] |

## Investor Q&A Preparation

### Likely Questions & Recommended Answers

**Q: Why should we invest now vs. waiting?**
A: [Framework: urgency + FOMO + milestone ahead]

**Q: What's your biggest risk?**
A: [Framework: honest + mitigation + turn into strength]

**Q: How do you compete with [big company]?**
A: [Framework: different game + focus + speed advantage]

**Q: What if a competitor raises $50M?**
A: [Framework: market is big enough + execution matters + moats]

**Q: What's your burn rate and runway?**
A: [Direct answer + path to next milestone]

**Q: Why this team?**
A: [Unfair advantages + complementary skills + relevant experience]

**Q: What happens if you can't raise your next round?**
A: [Path to profitability or revenue sustainability plan]

**Q: What are your top 3 priorities for the next 12 months?**
A: [Clear, measurable priorities]

**Q: Who are your target acquirers?**
A: [Strategic buyers + why + but building for independence]

**Q: What's the one metric you obsess over?**
A: [North star metric + why it matters + current trajectory]

## Design Direction Notes
[Guidance for a designer: color palette suggestions, mood, visual style,
layout principles. Reference best-in-class decks from the industry.]

## Deck Flow Check
[Verify the narrative flows logically. Each slide should answer a question
that the previous slide raised. No slide should feel disconnected.]
```

## Output File
Save as: `PITCH-DECK-BRIEF.md` in the current working directory.
