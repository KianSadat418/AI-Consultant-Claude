---
name: founder-swot
description: >
  SWOT analysis combined with Porter's Five Forces using Harvard Business School
  strategy methodology. Includes cross-analysis (SO/WT strategies) and industry
  attractiveness scoring. Use when the user types /founder swot or asks about
  SWOT analysis, Porter's Five Forces, strategic assessment, or industry
  attractiveness evaluation.
---

# /founder swot -- SWOT + Porter's Five Forces

## Purpose
Deliver an HBS-caliber strategic assessment combining a rigorous SWOT analysis (7 items per quadrant, cross-analysis matrix) with Porter's Five Forces (each force rated 1-10 with evidence). Produces a comprehensive view of internal capabilities and external dynamics.

## Trigger
User types: `/founder swot [optional: company name or focus area]`

## Data Retrieval (run before any analysis)

1. **Load CONTEXT.md** if present. Extract: company strengths, weaknesses, team, product, stage, industry, competitors, risks.

2. **Run web searches** (minimum 6 queries):
   - `"[industry] competitive dynamics"`
   - `"[industry] barriers to entry"`
   - `"[industry] supplier landscape concentration"`
   - `"[industry] customer bargaining power"`
   - `"[industry] substitute products alternatives"`
   - `"[industry] regulatory environment"`
   - `"[industry] threats opportunities 2025"`

3. **Fallback**: Build analysis from CONTEXT.md data + web search results.

## Analysis Framework

### SWOT Analysis

**Strengths (minimum 7 items)**:
Internal advantages. Consider: team expertise, technology/IP, first-mover advantage, partnerships, cost structure, culture, customer relationships, data assets, speed/agility, brand. Each strength must be specific (not "good team" but "founding team has 15 years combined experience in [specific domain] with exits at [companies]").

**Weaknesses (minimum 7 items)**:
Internal limitations. Consider: resource constraints, technical debt, team gaps, lack of brand recognition, dependency risks, unit economics challenges, geographic limitations, product gaps. Be brutally honest.

**Opportunities (minimum 7 items)**:
External positive dynamics. Consider: market growth, regulatory tailwinds, technology shifts, competitor weaknesses, unserved segments, partnership possibilities, M&A targets, geographic expansion. Each must be tied to a specific trend or data point from web research.

**Threats (minimum 7 items)**:
External negative dynamics. Consider: competitive intensity, regulatory risk, technology disruption, economic headwinds, talent market, customer concentration risk, platform dependency, market saturation. Each must be evidence-based.

### Cross-Analysis Matrix
This is the strategic insight layer. For each combination:
- **SO Strategies** (Strengths x Opportunities): How can strengths exploit opportunities?
- **WO Strategies** (Weaknesses x Opportunities): How can opportunities help overcome weaknesses?
- **ST Strategies** (Strengths x Threats): How can strengths counter threats?
- **WT Strategies** (Weaknesses x Threats): What are the critical vulnerabilities (weakness + threat)?

### Porter's Five Forces

Rate each force 1-10 with specific evidence:

**1. Competitive Rivalry**:
- Number and size of competitors
- Industry growth rate (growing markets = less rivalry)
- Product differentiation level
- Switching costs
- Exit barriers
- Rating: [1-10] with justification

**2. Threat of New Entrants**:
- Capital requirements to enter
- Economies of scale advantage of incumbents
- Brand loyalty and switching costs
- Access to distribution channels
- Regulatory/legal barriers
- Technology/IP barriers
- Rating: [1-10] with justification

**3. Bargaining Power of Suppliers**:
- Supplier concentration
- Switching costs for inputs
- Availability of substitutes for inputs
- Importance of volume to suppliers
- Threat of forward integration by suppliers
- Rating: [1-10] with justification

**4. Bargaining Power of Buyers**:
- Buyer concentration vs. company concentration
- Purchase volume significance
- Product differentiation
- Switching costs for buyers
- Buyer price sensitivity
- Threat of backward integration
- Rating: [1-10] with justification

**5. Threat of Substitutes**:
- Availability of close substitutes
- Price-performance of substitutes
- Switching costs to substitutes
- Buyer propensity to switch
- Rating: [1-10] with justification

**Industry Attractiveness Score**: Average of 5 forces (inverted -- higher = more attractive):
- 8-10: Highly attractive (low competitive pressure)
- 5-7: Moderately attractive (manageable dynamics)
- 1-4: Challenging (strong forces working against new entrants)

## Output Format

Save as `SWOT-ANALYSIS.md`:

```markdown
# Strategic Assessment: [Company Name]
_Generated [date] | SWOT + Porter's Five Forces_

## Executive Summary
[4-5 sentences: Key strategic position, biggest opportunity, biggest threat,
and the single most important strategic priority.]

## SWOT Matrix

### Strengths
1. [Specific strength with supporting detail]
2. [Specific strength with supporting detail]
3. [Specific strength with supporting detail]
4. [Specific strength with supporting detail]
5. [Specific strength with supporting detail]
6. [Specific strength with supporting detail]
7. [Specific strength with supporting detail]

### Weaknesses
1. [Specific weakness with honest assessment]
2. [Specific weakness with honest assessment]
3. [Specific weakness with honest assessment]
4. [Specific weakness with honest assessment]
5. [Specific weakness with honest assessment]
6. [Specific weakness with honest assessment]
7. [Specific weakness with honest assessment]

### Opportunities
1. [Opportunity + data point/trend supporting it]
2. [Opportunity + data point/trend supporting it]
3. [Opportunity + data point/trend supporting it]
4. [Opportunity + data point/trend supporting it]
5. [Opportunity + data point/trend supporting it]
6. [Opportunity + data point/trend supporting it]
7. [Opportunity + data point/trend supporting it]

### Threats
1. [Threat + evidence/data]
2. [Threat + evidence/data]
3. [Threat + evidence/data]
4. [Threat + evidence/data]
5. [Threat + evidence/data]
6. [Threat + evidence/data]
7. [Threat + evidence/data]

## Cross-Analysis Strategies

### SO Strategies (Leverage)
| Strength | Opportunity | Strategy |
|----------|-----------|---------|
| [S#] | [O#] | [Actionable strategy] |

### WO Strategies (Develop)
| Weakness | Opportunity | Strategy |
|----------|-----------|---------|
| [W#] | [O#] | [How to use opportunity to fix weakness] |

### ST Strategies (Defend)
| Strength | Threat | Strategy |
|----------|-------|---------|
| [S#] | [T#] | [How to use strength to counter threat] |

### WT Strategies (Critical Vulnerabilities)
| Weakness | Threat | Risk | Mitigation |
|----------|-------|------|-----------|
| [W#] | [T#] | [What could go wrong] | [How to mitigate] |

## Porter's Five Forces

### 1. Competitive Rivalry: [X]/10
[2-3 paragraph analysis with specific competitor data]

### 2. Threat of New Entrants: [X]/10
[2-3 paragraph analysis with barrier assessment]

### 3. Bargaining Power of Suppliers: [X]/10
[2-3 paragraph analysis with supplier landscape data]

### 4. Bargaining Power of Buyers: [X]/10
[2-3 paragraph analysis with buyer dynamics]

### 5. Threat of Substitutes: [X]/10
[2-3 paragraph analysis with substitute landscape]

### Industry Attractiveness Score: [X]/10
[Overall assessment of whether this is a good industry to enter/compete in]

## Five Forces Summary

| Force | Rating | Key Driver | Implication |
|-------|--------|-----------|-------------|
| Rivalry | [X]/10 | [main driver] | [what it means] |
| New Entrants | [X]/10 | [main driver] | [what it means] |
| Supplier Power | [X]/10 | [main driver] | [what it means] |
| Buyer Power | [X]/10 | [main driver] | [what it means] |
| Substitutes | [X]/10 | [main driver] | [what it means] |
| **Attractiveness** | **[X]/10** | | |

## Strategic Implications
[3-4 paragraphs: What the combined SWOT + Five Forces analysis means
for the company's strategy. Specific recommendations for the next 12 months.
Identify the #1 strategic priority.]
```

## Output File
Save as: `SWOT-ANALYSIS.md` in the current working directory.
