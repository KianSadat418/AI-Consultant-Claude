# /founder -- Strategic Analysis Toolkit for Claude Code

**18 Skills** | **5 Parallel Agents** | **6 Scripts** | **MIT License**

A company-agnostic founder toolkit that delivers McKinsey-level strategic analysis directly inside Claude Code. Combines real-time data retrieval, parallel sub-agents, and structured synthesis to produce investor-ready deliverables in minutes instead of weeks.

Drop a `CONTEXT.md` file with your company details, run `/founder analyze`, and get a comprehensive strategic assessment across market sizing, competitive intelligence, GTM strategy, financial modeling, and legal structure. Swap the context file, re-run any command, get a fresh analysis for a different company.

---

## Quick Start

### Install

```bash
curl -fsSL https://raw.githubusercontent.com/YOUR_USERNAME/founder-claude/main/install.sh | bash
```

### Setup

```bash
# Copy the context template to your working directory
cp ~/.claude/templates/founder/CONTEXT-template.md ./CONTEXT.md

# Edit with your company details
# (the more detail you provide, the better the analysis)
```

### Run

```bash
# In Claude Code, type any command:
/founder              # See all available commands
/founder tam          # Market sizing analysis
/founder compete      # Competitive landscape
/founder analyze      # Full company audit (flagship)
```

---

## Commands

| Command | Description | Output File |
|---------|-------------|-------------|
| `/founder` | Show all commands | -- |
| `/founder tam` | TAM/SAM/SOM market sizing (dual methodology) | `MARKET-SIZING.md` |
| `/founder trends` | Industry trend analysis (PESTLE + micro signals) | `INDUSTRY-TRENDS.md` |
| `/founder compete` | Competitive landscape (10+ competitors mapped) | `COMPETITIVE-LANDSCAPE.md` |
| `/founder persona` | Customer personas & segmentation (4 JTBD personas) | `CUSTOMER-PERSONAS.md` |
| `/founder swot` | SWOT + Porter's Five Forces | `SWOT-ANALYSIS.md` |
| `/founder gtm` | Go-to-market strategy playbook | `GTM-PLAYBOOK.md` |
| `/founder pricing` | Pricing strategy (3-tier recommendation) | `PRICING-STRATEGY.md` |
| `/founder risk` | Risk assessment & scenario planning (15 risks) | `RISK-ASSESSMENT.md` |
| `/founder journey` | Customer journey mapping (7 lifecycle stages) | `CUSTOMER-JOURNEY.md` |
| `/founder uniteco` | Unit economics (CAC/LTV/margins benchmarked) | `UNIT-ECONOMICS.md` |
| `/founder model` | Financial modeling (3-year, monthly Y1 detail) | `FINANCIAL-MODEL.md` |
| `/founder raise` | Fundraising strategy (round sizing + investor targeting) | `FUNDRAISING-STRATEGY.md` |
| `/founder pitch` | Pitch deck builder (12-slide narrative + Q&A prep) | `PITCH-DECK-BRIEF.md` |
| `/founder legal` | Legal structure & entity setup | `LEGAL-STRUCTURE.md` |
| `/founder equity` | Cap table & equity structuring | `EQUITY-STRUCTURE.md` |
| `/founder expand` | Market entry & expansion planning | `MARKET-ENTRY.md` |
| `/founder analyze` | **Full parallel company audit (flagship)** | `COMPANY-ANALYSIS.md` |
| `/founder synthesis` | McKinsey-style executive strategy summary | `STRATEGY-SYNTHESIS.md` |

---

## Architecture

The toolkit follows a 3-phase pipeline for every analysis:

### Phase 1: Data Retrieval
Every skill gathers real data before producing analysis. No skill generates output from training data alone.

- **Tier 1 (always)**: Claude Code built-in web search for current data points, market figures, competitor info, and recent news.
- **Tier 2 (when API keys available)**: Firecrawl for competitor website scraping, Perplexity API for deep market research, Crunchbase API for funding comparables.
- **Tier 3 (flagship only)**: Anthropic API parallel sub-agents for simultaneous multi-pillar analysis.

### Phase 2: Analysis
Each skill applies a specific named consulting framework (Porter's Five Forces, JTBD, MECE, BCG matrix, etc.) to the gathered data. The prompt engineering inside each SKILL.md is the core intellectual property of the package.

### Phase 3: Synthesis
For the flagship `/founder analyze` command, 5 parallel sub-agents (market, competitive, strategy, finance, legal) run simultaneously. Their outputs are collected and fed into a final synthesis call using `claude-opus-4-6` for the executive strategy document.

```
CONTEXT.md
    |
    v
[Data Retrieval] -- Web Search + APIs
    |
    v
[Parallel Agents] -- 5 Claude API calls (Sonnet, concurrent)
    |         |         |         |         |
    v         v         v         v         v
  Market  Compete  Strategy  Finance   Legal
    |         |         |         |         |
    +----+----+----+----+----+----+
         |
         v
  [Synthesis] -- Claude Opus final pass
         |
         v
  COMPANY-ANALYSIS.md
```

---

## CONTEXT.md Setup

The `CONTEXT.md` file is what makes this toolkit reusable across companies. It contains your company's essential information that every skill reads before running analysis.

```bash
cp ~/.claude/templates/founder/CONTEXT-template.md ./CONTEXT.md
```

**Required fields:**
- Company name, one-line description
- Stage (idea / pre-seed / seed / Series A+)
- Industry

**Recommended fields:**
- Website URL
- Target market and customer description
- Current traction (revenue, users, growth)
- Founding team summary
- Fundraising status and goals
- Known competitors
- Key risks and strategic questions

The more context you provide, the more tailored and accurate the analysis.

---

## API Keys

All API keys are optional. The toolkit works with zero configuration using Claude Code's built-in web search. API keys unlock enhanced data retrieval.

| Key | Required? | What It Unlocks | Cost |
|-----|-----------|----------------|------|
| `ANTHROPIC_API_KEY` | Optional | Parallel sub-agents for `/founder analyze` | ~$0.10-0.40/run |
| `FIRECRAWL_API_KEY` | Optional | Competitor website scraping (pricing, features) | Free tier available |
| `PERPLEXITY_API_KEY` | Optional | Deep market research with cited sources | Free tier available |
| `CRUNCHBASE_API_KEY` | Optional | Funding round comparables and investor data | Free tier available |

Set keys in your environment:
```bash
export ANTHROPIC_API_KEY=your-key-here
export FIRECRAWL_API_KEY=your-key-here
export PERPLEXITY_API_KEY=your-key-here
export CRUNCHBASE_API_KEY=your-key-here
```

---

## Cost Estimates

| Command | Without API | With Anthropic API |
|---------|------------|-------------------|
| Individual skills (`/founder tam`, etc.) | Free (uses Claude Code) | N/A |
| `/founder analyze` (sequential) | Free (uses Claude Code) | N/A |
| `/founder analyze` (parallel agents) | N/A | ~$0.10-0.40 per run |

The parallel agent path spawns 5 Sonnet calls + 1 Opus synthesis call per run.

---

## Project Structure

```
founder-claude/
├── founder/
│   └── SKILL.md                        # Orchestrator (routes all /founder subcommands)
├── skills/
│   ├── founder-tam/SKILL.md            # TAM/SAM/SOM market sizing
│   ├── founder-trends/SKILL.md         # Industry trend analysis
│   ├── founder-compete/SKILL.md        # Competitive landscape
│   ├── founder-persona/SKILL.md        # Customer personas & segmentation
│   ├── founder-swot/SKILL.md           # SWOT + Porter's Five Forces
│   ├── founder-gtm/SKILL.md           # Go-to-market strategy
│   ├── founder-pricing/SKILL.md        # Pricing strategy
│   ├── founder-risk/SKILL.md           # Risk assessment & scenario planning
│   ├── founder-journey/SKILL.md        # Customer journey mapping
│   ├── founder-uniteco/SKILL.md        # Unit economics
│   ├── founder-model/SKILL.md          # Financial modeling & projections
│   ├── founder-raise/SKILL.md          # Fundraising strategy
│   ├── founder-pitch/SKILL.md          # Pitch deck builder
│   ├── founder-legal/SKILL.md          # Legal structure & entity setup
│   ├── founder-equity/SKILL.md         # Cap table & equity structuring
│   ├── founder-expand/SKILL.md         # Market entry & expansion
│   ├── founder-analyze/SKILL.md        # Flagship: full parallel audit
│   └── founder-synthesis/SKILL.md      # McKinsey-style exec strategy summary
├── agents/
│   ├── founder-market-agent.md         # Market + TAM sub-agent
│   ├── founder-competitive-agent.md    # Competitive intelligence sub-agent
│   ├── founder-strategy-agent.md       # Strategy + GTM sub-agent
│   ├── founder-finance-agent.md        # Finance + unit economics sub-agent
│   └── founder-legal-agent.md          # Legal + risk sub-agent
├── scripts/
│   ├── fetch_context.py                # Loads and validates CONTEXT.md
│   ├── scrape_competitor.py            # Firecrawl-based competitor scraper
│   ├── market_research.py              # Perplexity API market research
│   ├── crunchbase_comps.py             # Crunchbase funding comparables
│   ├── web_search.py                   # General web search utility
│   └── run_parallel_agents.py          # Spawns parallel Claude API sub-agents
├── templates/
│   ├── CONTEXT-template.md             # Template for user's company context
│   ├── market-sizing.md                # Output template for TAM analysis
│   ├── competitive-landscape.md        # Output template for competitive analysis
│   ├── gtm-playbook.md                # Output template for GTM strategy
│   ├── financial-model.md              # Output template for financial projections
│   ├── pitch-deck-brief.md             # Output template for pitch narrative
│   └── company-analysis.md             # Output template for full flagship analysis
├── install.sh
├── uninstall.sh
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## Requirements

| Requirement | Version | Required? |
|------------|---------|-----------|
| Claude Code | Latest | Yes |
| Python | 3.8+ | Optional (for API scripts) |
| Git | Any | Yes (for installation) |
| anthropic (Python) | >=0.25.0 | Optional (for parallel agents) |
| firecrawl-py | >=0.0.16 | Optional (for competitor scraping) |
| requests | >=2.31.0 | Optional (for API scripts) |
| beautifulsoup4 | >=4.12.0 | Optional (fallback scraping) |

---

## Uninstall

```bash
curl -fsSL https://raw.githubusercontent.com/YOUR_USERNAME/founder-claude/main/uninstall.sh | bash
```

Or if you cloned the repo:
```bash
bash uninstall.sh
```

This removes all skills, agents, scripts, and templates from `~/.claude/`. It does not remove Python packages or any analysis files generated in your working directories.

---

## License

MIT License. See [LICENSE](LICENSE) for details.
