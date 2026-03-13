---
name: founder-analyze
description: >
  Full parallel company audit orchestrating all analysis pillars simultaneously.
  Spawns 5 parallel sub-agents (market, competitive, strategy, finance, legal)
  and synthesizes results into a comprehensive company analysis. This is the
  flagship command. Use when the user types /founder analyze or asks for a full
  company analysis, comprehensive audit, or complete startup assessment.
---

# /founder analyze -- Full Parallel Company Audit (Flagship)

## Purpose
This is the flagship command. It orchestrates a complete company analysis across all five pillars (market, competitive, strategy, finance, legal) and synthesizes them into a single comprehensive document. The output should feel like a strategy firm delivered it after a week of work.

## Trigger
User types: `/founder analyze [optional: company name or URL]`

## Execution Flow

### Step 1: Load Context
```
if CONTEXT.md exists:
  Load it. Parse all fields.
  Confirm: "Running full analysis for [Company Name]..."
else:
  STOP. Tell the user:
  "The /founder analyze command requires a CONTEXT.md file.
   Run: cp ~/.claude/templates/founder/CONTEXT-template.md ./CONTEXT.md
   Fill it out, then re-run /founder analyze."
```

### Step 2: Data Retrieval Blitz
Run comprehensive web searches across ALL pillars simultaneously:

**Market searches**:
- `"[industry] market size 2025 2026 TAM"`
- `"[industry] trends forecast"`
- `"[industry] growth rate CAGR"`

**Competitive searches**:
- `"[competitor 1] funding revenue customers"`
- `"[competitor 2] pricing features"`
- `"[industry] startups funded 2024 2025"`
- `"[industry] competitive landscape"`

**Strategy searches**:
- `"[industry] go to market strategy"`
- `"[industry] customer acquisition channels CAC"`
- `"[industry] pricing benchmarks"`

**Finance searches**:
- `"[industry] unit economics benchmarks"`
- `"[stage] startup financial benchmarks"`
- `"[industry] revenue multiples"`

**Legal searches**:
- `"[industry] regulatory requirements"`
- `"startup [state] formation legal"`

### Step 3: Parallel Agent Execution

**If ANTHROPIC_API_KEY is set** (preferred path):
```bash
python ~/.claude/scripts/founder/run_parallel_agents.py
```
This spawns 5 concurrent Claude API calls using the agent definitions in `~/.claude/agents/`:
- `founder-market-agent.md` -> Market + TAM analysis
- `founder-competitive-agent.md` -> Competitive intelligence
- `founder-strategy-agent.md` -> Strategy + GTM
- `founder-finance-agent.md` -> Finance + unit economics
- `founder-legal-agent.md` -> Legal + risk

Each agent receives:
- Its pillar-specific system prompt
- The full CONTEXT.md
- Relevant web search results

Sub-agents use `claude-sonnet-4-6` for speed and cost efficiency.

**If ANTHROPIC_API_KEY is NOT set** (fallback path):
Run each pillar analysis sequentially using Claude Code's built-in capabilities:
1. Market analysis (TAM + trends + personas)
2. Competitive analysis (landscape + positioning)
3. Strategy analysis (SWOT + GTM + pricing)
4. Financial analysis (unit economics + model)
5. Legal analysis (structure + equity + risk)

### Step 4: Collect and Validate Outputs
- Ensure all 5 pillar outputs are complete
- Check for data consistency across pillars
- Flag any contradictions (e.g., market size in market analysis vs. financial model)

### Step 5: Final Synthesis
**If API key available**: Make a final synthesis call using `claude-opus-4-6`:
- Input: All 5 pillar outputs + CONTEXT.md
- System prompt: McKinsey senior partner synthesizing a team's work
- Output: Executive strategy document

**If API key not available**: Perform synthesis directly in Claude Code.

### Step 6: Generate Output
Save comprehensive analysis as `COMPANY-ANALYSIS.md`.

## Output Format

Save as `COMPANY-ANALYSIS.md`:

```markdown
# Company Analysis: [Company Name]
_Generated [date] | Full 5-Pillar Strategic Assessment_
_Analysis methodology: [Parallel agents / Sequential analysis]_

---

## Executive Strategy Summary
[5 paragraphs written in McKinsey senior partner voice:
1. Company overview and strategic position
2. Market opportunity assessment
3. Competitive dynamics and positioning
4. Financial health and trajectory
5. Top strategic priority and recommended path forward]

---

## I. MARKET ANALYSIS

### Total Addressable Market
[TAM/SAM/SOM with dual methodology, cited sources, growth projection]

### Industry Trends
[Top 5 macro trends, top 5 micro trends, technology disruption timeline]

### Customer Landscape
[Primary personas, segment sizing, Jobs-to-be-Done analysis]

### Market Verdict
[Is this a good market to be in? Why? What timing considerations exist?]

---

## II. COMPETITIVE LANDSCAPE

### Competitor Map
[Direct competitors table with funding, features, pricing, threat level]

### Positioning Analysis
[Where the company sits vs. competitors, positioning map]

### Competitive Moats
[Assessment of defensibility for the company and top competitors]

### White Space Opportunities
[Unserved segments, missing features, pricing gaps]

### Competitive Verdict
[Can this company win? What's the path to competitive advantage?]

---

## III. STRATEGIC ASSESSMENT

### SWOT Summary
[Key strengths, weaknesses, opportunities, threats with cross-analysis]

### Go-to-Market Strategy
[Recommended channels, messaging framework, launch sequence]

### Pricing Recommendation
[Tier structure, competitive pricing position, revenue model]

### Customer Journey
[Critical touchpoints, friction points, optimization priorities]

### Strategy Verdict
[What strategy should the company pursue and why?]

---

## IV. FINANCIAL ASSESSMENT

### Unit Economics
[CAC, LTV, LTV:CAC, payback period, margins -- all benchmarked]

### Financial Projections (3-Year Summary)
| Metric | Year 1 | Year 2 | Year 3 |
|--------|--------|--------|--------|
| Revenue | $[X] | $[X] | $[X] |
| Customers | [X] | [X] | [X] |
| Burn rate | $[X]/mo | $[X]/mo | $[X]/mo |
| Gross margin | [X]% | [X]% | [X]% |

### Fundraising Assessment
[Round recommendation, valuation range, investor targeting guidance]

### Financial Verdict
[Are the economics viable? What needs to improve?]

---

## V. LEGAL & RISK ASSESSMENT

### Entity & Structure
[Recommended entity, key formation steps]

### Regulatory Landscape
[Industry-specific compliance requirements]

### Risk Matrix (Top 10)
[Ranked risks with scores, mitigation strategies]

### Equity Framework
[Recommended equity structure, vesting, option pool]

### Legal Verdict
[What legal/regulatory actions are most urgent?]

---

## SYNTHESIS: STRATEGIC RECOMMENDATIONS

### The Big Picture
[2-3 paragraphs: Overall assessment of the company's position and potential.
Be honest about both strengths and challenges.]

### Three Strategic Paths

#### Path A: Conservative
- **Approach**: [description]
- **Investment required**: $[X]
- **Timeline**: [X] months
- **Expected outcome**: [metric]
- **Key risk**: [risk]

#### Path B: Balanced (Recommended)
- **Approach**: [description]
- **Investment required**: $[X]
- **Timeline**: [X] months
- **Expected outcome**: [metric]
- **Key risk**: [risk]

#### Path C: Aggressive
- **Approach**: [description]
- **Investment required**: $[X]
- **Timeline**: [X] months
- **Expected outcome**: [metric]
- **Key risk**: [risk]

### Top 10 Priority Initiatives (Next 90 Days)
| # | Initiative | Pillar | Impact | Effort | Owner |
|---|-----------|--------|--------|--------|-------|
| 1 | [initiative] | [pillar] | [H/M/L] | [H/M/L] | [role] |
[...10 initiatives]

### Decision Framework
[Guidance for the next 10 strategic decisions the founder will face.
How to weigh tradeoffs, what principles to follow.]

### "If I Only Had 1 Hour" Brief
[The entire analysis compressed into a 1-page executive brief.
If a busy investor had 60 seconds, what would they need to know?]

---

_Analysis complete. Individual pillar reports can be generated with deeper
detail using the specific /founder commands (tam, compete, gtm, etc.)._
```

## Output File
Save as: `COMPANY-ANALYSIS.md` in the current working directory.

## Cost Estimate
- With parallel agents (API): ~$0.10-$0.40 per run
- Without API (sequential): Uses Claude Code credits only
