---
name: founder-persona
description: >
  Customer persona creation and market segmentation using Jobs-to-be-Done and
  demographic/psychographic methodology. Builds 4 detailed buyer personas with
  segment sizing and prioritization. Use when the user types /founder persona
  or asks about customer personas, buyer profiles, target audience, customer
  segmentation, or ideal customer profile (ICP).
---

# /founder persona -- Customer Personas & Segmentation

## Purpose
Build 4 research-backed customer personas combining Jobs-to-be-Done methodology with traditional demographic/psychographic profiling. Each persona must be specific enough for a product manager to design features for, a marketer to write copy for, and a salesperson to qualify leads against.

## Trigger
User types: `/founder persona [optional: target customer description]`

## Data Retrieval (run before any analysis)

1. **Load CONTEXT.md** if present. Extract: target market, customer description, industry, product, traction data, geography.

2. **Run web searches** (minimum 6 queries):
   - `"[target customer job title] pain points challenges"`
   - `"[industry] buyer persona research"`
   - `"[industry] customer segments"`
   - `"[competitor] customer reviews G2 Capterra TrustPilot"` (mine for pain points)
   - `"[industry] subreddit community forum pain points"`
   - `"[target customer] buying behavior B2B"` or `"[target demographic] consumer behavior"`
   - `"[industry] willingness to pay survey"`

3. **If FIRECRAWL_API_KEY is set**, scrape:
   - Competitor review pages
   - Industry community forums
   - Job descriptions for target buyer roles

4. **Fallback**: Build personas from web search data, competitor review mining, and industry research.

## Analysis Framework

### Phase 1: Segment Identification
Before building individual personas, identify the market segments:
- Analyze the total addressable customer base
- Identify 4-6 distinct segments based on: use case, company size (B2B), demographics (B2C), buying behavior, or pain point severity
- Size each segment (% of total market, estimated customer count, estimated revenue potential)
- Create a prioritization matrix: Segment Size x Willingness to Pay x Ease of Acquisition

### Phase 2: Jobs-to-be-Done Analysis
For each segment, identify:
- **Functional jobs**: What task are they trying to accomplish?
- **Emotional jobs**: How do they want to feel?
- **Social jobs**: How do they want to be perceived?
- **Related jobs**: What do they do immediately before and after?
- **Job importance**: How critical is this job to their role/life? (1-10)
- **Job satisfaction with current solutions**: How well are they served today? (1-10)
- **Opportunity score**: Importance + (Importance - Satisfaction). High scores = biggest opportunities.

### Phase 3: Full Persona Construction
Build 4 detailed personas (1 per top segment). Each persona must include:

**Demographics**:
- Name (fictional but realistic), age range, gender distribution
- Job title (B2B) or life stage (B2C)
- Company size and industry (B2B) or household details (B2C)
- Income/budget range
- Geography/location type
- Education level
- Technology proficiency

**Psychographics**:
- Values and beliefs relevant to the purchase decision
- Risk tolerance (early adopter vs. cautious buyer)
- Information sources (how they research solutions)
- Decision-making style (data-driven, peer-influenced, authority-driven)
- Brand affinities (what brands do they trust and why?)

**Pain Points (Top 5 Daily Frustrations)**:
Each frustration must be specific and tied to the problem the product solves. Not generic complaints, but the exact moments of friction in their day/workflow.

**Goals**:
- Primary goal (what success looks like in their role/life)
- Secondary goals
- How they measure success

**Buying Behavior**:
- Where they discover new solutions
- Who else is involved in the decision (B2B: decision-making unit; B2C: household influencers)
- Average evaluation period (how long from awareness to purchase)
- Budget authority and approval process
- Preferred purchasing channel
- Price sensitivity (what would they pay? what would feel too expensive?)

**Media Consumption**:
- Publications, podcasts, newsletters they follow
- Social platforms they use
- Communities they participate in
- Events/conferences they attend

**Top 3 Objections**:
The specific reasons this persona would hesitate to buy. For each:
- The objection in their words
- The underlying concern
- How to address it

**Trigger Events**:
Specific events that would cause this persona to actively seek a solution:
- New job/role change
- Budget cycle timing
- Competitive pressure
- Regulatory deadline
- Pain threshold reached

**Willingness to Pay**:
- Estimated WTP range
- Value anchors (what are they comparing to?)
- Price sensitivity triggers

### Phase 4: Segment Prioritization
Create a prioritization matrix scoring each persona/segment on:
- Market size (1-10)
- Willingness to pay (1-10)
- Ease of acquisition (1-10)
- Strategic fit (1-10)
- Lifetime value potential (1-10)
- Weighted total score
Recommend which persona to target first and why.

## Output Format

Save as `CUSTOMER-PERSONAS.md`:

```markdown
# Customer Personas: [Company Name]
_Generated [date] | 4 personas across [X] market segments_

## Executive Summary
[3-4 sentences: Who the ideal customers are, which segment to prioritize,
and the key insight that should shape product and marketing strategy.]

## Market Segmentation Overview

| Segment | Size (% of market) | Est. Customers | WTP | Priority |
|---------|-------------------|---------------|-----|----------|
| [Segment 1] | [X]% | [X] | $[X]/yr | [1-4] |
| [Segment 2] | [X]% | [X] | $[X]/yr | [1-4] |
| [Segment 3] | [X]% | [X] | $[X]/yr | [1-4] |
| [Segment 4] | [X]% | [X] | $[X]/yr | [1-4] |

## Persona 1: [Name] -- "[Tagline capturing their core need]"
_Segment: [Segment Name] | Priority: [1-4]_

### Demographics
[Full demographic profile]

### Psychographics
[Values, decision style, brand affinities]

### Jobs-to-be-Done
- **Functional**: [job]
- **Emotional**: [job]
- **Social**: [job]
- **Opportunity Score**: [X]/20

### Top 5 Daily Frustrations
1. [Specific, vivid frustration]
2. [Specific, vivid frustration]
3. [Specific, vivid frustration]
4. [Specific, vivid frustration]
5. [Specific, vivid frustration]

### Goals
- **Primary**: [goal]
- **Secondary**: [goals]
- **Success metric**: [how they know they've succeeded]

### Buying Behavior
- **Discovery channels**: [where they find solutions]
- **Decision-making unit**: [who else is involved]
- **Evaluation period**: [timeframe]
- **Budget**: $[X] range
- **Preferred channel**: [how they buy]

### Media & Community
- **Reads**: [publications]
- **Listens to**: [podcasts]
- **Active on**: [platforms/communities]
- **Attends**: [events]

### Top 3 Objections
1. **"[Objection in their words]"** -- [underlying concern] -- [response strategy]
2. **"[Objection in their words]"** -- [underlying concern] -- [response strategy]
3. **"[Objection in their words]"** -- [underlying concern] -- [response strategy]

### Trigger Events
- [Event 1]: [why it triggers search behavior]
- [Event 2]: [why it triggers search behavior]
- [Event 3]: [why it triggers search behavior]

### Willingness to Pay
- **Range**: $[X] -- $[X] per [period]
- **Value anchor**: [what they compare to]
- **Price ceiling**: $[X] (above this, they seek alternatives)

[Repeat full profile for Personas 2, 3, 4]

## Prioritization Matrix

| Criteria (Weight) | [Persona 1] | [Persona 2] | [Persona 3] | [Persona 4] |
|-------------------|-------------|-------------|-------------|-------------|
| Market Size (25%) | [X]/10 | [X]/10 | [X]/10 | [X]/10 |
| WTP (25%) | [X]/10 | [X]/10 | [X]/10 | [X]/10 |
| Ease of Acquisition (20%) | [X]/10 | [X]/10 | [X]/10 | [X]/10 |
| Strategic Fit (15%) | [X]/10 | [X]/10 | [X]/10 | [X]/10 |
| LTV Potential (15%) | [X]/10 | [X]/10 | [X]/10 | [X]/10 |
| **Weighted Total** | **[X]** | **[X]** | **[X]** | **[X]** |

## Recommended Targeting Strategy
[2-3 paragraphs: Which persona to go after first, why, and how.
Include messaging angle, channel strategy, and key proof points for each.]
```

## Output File
Save as: `CUSTOMER-PERSONAS.md` in the current working directory.
