---
name: founder-legal
description: >
  Legal structure and entity setup guide covering entity type selection,
  formation checklist, IP assignment, founder agreements, and industry-specific
  regulatory compliance. Use when the user types /founder legal or asks about
  LLC vs C-Corp, entity formation, legal structure, IP protection, founder
  agreements, or regulatory compliance.
---

# /founder legal -- Legal Structure & Entity Setup

## Purpose
Provide a comprehensive legal structure guide covering entity type selection, formation steps, IP protection, founder agreements, and industry-specific regulatory requirements. Always includes disclaimer that this is informational only, not legal advice.

## Trigger
User types: `/founder legal [optional: specific legal question]`

## Data Retrieval (run before any analysis)

1. **Load CONTEXT.md** if present. Extract: industry, geography, team structure, IP situation, stage, regulatory concerns.

2. **Run web searches** (minimum 5 queries):
   - `"[state] LLC formation requirements 2025"`
   - `"C-Corp vs LLC startup [industry]"`
   - `"[industry] regulatory requirements startup"`
   - `"startup founder agreement template"`
   - `"[industry] IP protection patent trademark"`

3. **Fallback**: Build from web search + CONTEXT.md.

## Analysis Framework

### Entity Type Decision Tree
Walk through the decision:
- Raising VC? -> C-Corp (Delaware) in most cases
- Bootstrapping? -> LLC may be more tax-efficient
- Industry-specific requirements (e.g., healthcare, finance)?
- Multiple founders? Implications for each entity type
- IP-heavy? Patent vs. trade secret strategy
- International expansion plans? Entity structure implications

### Formation Checklist
Step-by-step process for the recommended entity type:
- State selection and reasoning
- Filing requirements and costs
- EIN application
- Operating agreement / bylaws
- Initial resolutions
- Bank account setup
- Registered agent selection

### IP Protection
- IP assignment agreement (founders assign all relevant IP to the company)
- Patent filing assessment (worth it? timing? provisional vs. full?)
- Trademark strategy (name, logo, tagline)
- Trade secret protection practices
- Open-source compliance (if using OSS)

### Founder Agreements
- Equity split framework
- Vesting schedule (standard 4-year, 1-year cliff)
- IP assignment clauses
- Non-compete / non-solicit considerations
- Role and responsibility definitions
- Decision-making framework
- Exit and separation terms

### Regulatory Compliance
Industry-specific requirements. Especially important for:
- MedTech: FDA pathways, HIPAA compliance, clinical trial requirements
- FinTech: State money transmitter licenses, banking regulations
- EdTech: FERPA, COPPA compliance
- HealthTech: HIPAA, state telehealth regulations
- AI/Data: Privacy regulations (GDPR, CCPA), AI governance

## Output Format

Save as `LEGAL-STRUCTURE.md`:

```markdown
# Legal Structure Guide: [Company Name]
_Generated [date]_

> **DISCLAIMER**: This document is for informational purposes only and does not
> constitute legal advice. Consult a qualified attorney before making legal
> decisions. Laws vary by jurisdiction and change frequently.

## Executive Summary
[3-4 sentences: Recommended entity type, key formation steps, most important
legal priority, and the most critical regulatory consideration.]

## Entity Recommendation

### Recommended: [Entity Type]
**Why**: [Clear reasoning based on company specifics]

### Decision Analysis
| Factor | LLC | C-Corp (DE) | C-Corp ([Home State]) |
|--------|-----|------------|----------------------|
| VC fundraising | [fit] | [fit] | [fit] |
| Tax treatment | [details] | [details] | [details] |
| Equity incentives | [details] | [details] | [details] |
| Complexity | [level] | [level] | [level] |
| Cost to form | $[X] | $[X] | $[X] |
| Industry fit | [fit] | [fit] | [fit] |

### State Selection
**Recommended**: [State] -- [reasoning]

## Formation Checklist

### Phase 1: Entity Setup (Week 1-2)
- [ ] Choose and reserve company name
- [ ] File [Articles of Incorporation / Articles of Organization] in [State]
- [ ] Obtain EIN from IRS
- [ ] Draft and sign [Bylaws / Operating Agreement]
- [ ] File for foreign qualification in [operating state] if different
- [ ] Appoint registered agent in [State]
- [ ] Adopt initial board resolutions

### Phase 2: Foundational Agreements (Week 2-4)
- [ ] Execute Founder Agreement / Stockholders Agreement
- [ ] Sign IP Assignment Agreements (all founders)
- [ ] Set up vesting schedule (4 years, 1-year cliff recommended)
- [ ] Issue founder shares / membership interests
- [ ] File 83(b) elections (within 30 days of share issuance -- CRITICAL)

### Phase 3: Operational Setup (Week 3-6)
- [ ] Open business bank account
- [ ] Set up accounting system
- [ ] Obtain business insurance (general liability at minimum)
- [ ] Register for state and local taxes
- [ ] File any required industry-specific licenses

### Estimated Costs
| Item | DIY Cost | With Attorney |
|------|---------|--------------|
| State filing fees | $[X] | $[X] |
| Registered agent (annual) | $[X] | $[X] |
| Legal fees for formation | $0 | $[X]-$[X] |
| IP filings | $[X] | $[X] |
| **Total setup** | **$[X]** | **$[X]** |

## IP Protection Plan

### IP Assignment
[What needs to be assigned, by whom, when, and template guidance]

### Patent Strategy
[Assessment: Is patent protection worth pursuing? Provisional vs. full?
Timeline and cost estimates. Alternative: trade secret protection.]

### Trademark Strategy
[Name search guidance, classes to file in, timeline, cost]

### Trade Secret Protection
[NDAs, employee agreements, access controls, documentation practices]

## Founder Agreement Key Terms

### Equity & Vesting
[Recommended structure with reasoning]

### Roles & Decision-Making
[How to structure decision rights and responsibilities]

### Separation Terms
[What happens if a founder leaves -- good leaver / bad leaver provisions]

## Industry-Specific Regulatory Requirements

### [Primary Regulation/Compliance Area]
- **Requirement**: [What's required]
- **Timeline**: [When it needs to be addressed]
- **Cost**: $[X] estimate
- **Risk of non-compliance**: [Consequences]
- **Action items**: [What to do]

[Repeat for each relevant regulation]

## "Talk to a Lawyer About These Specific Things"
[Prioritized list of topics where professional legal counsel is strongly
recommended. Be specific about WHAT to discuss so the founder gets maximum
value from limited attorney time.]

1. [Topic]: [Why it's important and what to ask]
2. [Topic]: [Why it's important and what to ask]
3. [Topic]: [Why it's important and what to ask]
4. [Topic]: [Why it's important and what to ask]
5. [Topic]: [Why it's important and what to ask]

## Recommended Legal Resources
[Relevant templates, accelerator legal programs like YCLA or Orrick's
startup toolkit, affordable legal service providers for early-stage startups]
```

## Output File
Save as: `LEGAL-STRUCTURE.md` in the current working directory.
