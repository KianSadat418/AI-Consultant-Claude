---
name: founder
description: >
  Company-agnostic founder toolkit delivering McKinsey-level strategic analysis.
  Routes all /founder subcommands including market sizing, competitive analysis,
  GTM strategy, financial modeling, fundraising, pitch decks, legal structure,
  and full parallel company audits. Triggers on any /founder command. Always use
  this skill when the user types /founder followed by any subcommand, or asks
  for startup strategy, market analysis, competitive intelligence, fundraising
  help, pitch deck guidance, or any founder-related strategic question.
---

# /founder -- Founder Toolkit Orchestrator

You are the orchestrator for the `/founder` skill package. When a user types `/founder <subcommand>`, route to the correct sub-skill. If no subcommand is given, display the command menu.

## Step 1: Load Company Context

Before routing ANY subcommand, check for `CONTEXT.md` in the current working directory.

```
if CONTEXT.md exists:
  Load it. Parse company name, stage, industry, traction, team, competitors, risks.
  Confirm: "Loaded context for [Company Name] ([Stage], [Industry])."

if CONTEXT.md does NOT exist:
  Tell the user:
  "No CONTEXT.md found. You can:
   1. Describe your company inline and I'll use that as context
   2. Run: cp ~/.claude/templates/founder/CONTEXT-template.md ./CONTEXT.md
      Then fill it out and re-run your command."
  If user provides inline context, proceed with that.
```

## Step 2: Route to Sub-Skill

Match the subcommand and read the corresponding SKILL.md:

| Command | Skill Path | Description |
|---------|-----------|-------------|
| `/founder tam` | `skills/founder-tam/SKILL.md` | TAM/SAM/SOM market sizing |
| `/founder trends` | `skills/founder-trends/SKILL.md` | Industry trend analysis |
| `/founder compete` | `skills/founder-compete/SKILL.md` | Competitive landscape |
| `/founder persona` | `skills/founder-persona/SKILL.md` | Customer personas & segmentation |
| `/founder swot` | `skills/founder-swot/SKILL.md` | SWOT + Porter's Five Forces |
| `/founder gtm` | `skills/founder-gtm/SKILL.md` | Go-to-market strategy |
| `/founder pricing` | `skills/founder-pricing/SKILL.md` | Pricing strategy |
| `/founder risk` | `skills/founder-risk/SKILL.md` | Risk assessment & scenario planning |
| `/founder journey` | `skills/founder-journey/SKILL.md` | Customer journey mapping |
| `/founder uniteco` | `skills/founder-uniteco/SKILL.md` | Unit economics |
| `/founder model` | `skills/founder-model/SKILL.md` | Financial modeling & projections |
| `/founder raise` | `skills/founder-raise/SKILL.md` | Fundraising strategy |
| `/founder pitch` | `skills/founder-pitch/SKILL.md` | Pitch deck builder |
| `/founder legal` | `skills/founder-legal/SKILL.md` | Legal structure & entity setup |
| `/founder equity` | `skills/founder-equity/SKILL.md` | Cap table & equity structuring |
| `/founder expand` | `skills/founder-expand/SKILL.md` | Market entry & expansion |
| `/founder analyze` | `skills/founder-analyze/SKILL.md` | Full parallel company audit (flagship) |
| `/founder synthesis` | `skills/founder-synthesis/SKILL.md` | McKinsey-style executive strategy summary |

## Step 3: If No Subcommand Given

Display:

```
FOUNDER TOOLKIT -- Strategic Analysis Suite
============================================

MARKET PILLAR
  /founder tam        Total Addressable Market sizing
  /founder trends     Industry trend analysis
  /founder compete    Competitive landscape
  /founder persona    Customer personas & segmentation

STRATEGY PILLAR
  /founder swot       SWOT + Porter's Five Forces
  /founder gtm        Go-to-market strategy
  /founder pricing    Pricing strategy
  /founder risk       Risk assessment & scenario planning
  /founder journey    Customer journey mapping

FINANCE PILLAR
  /founder uniteco    Unit economics
  /founder model      Financial modeling & projections
  /founder raise      Fundraising strategy
  /founder pitch      Pitch deck builder

LEGAL & OPS PILLAR
  /founder legal      Legal structure & entity setup
  /founder equity     Cap table & equity structuring
  /founder expand     Market entry & expansion

FLAGSHIP
  /founder analyze    Full parallel company audit
  /founder synthesis  Executive strategy summary

Tip: Drop a CONTEXT.md in your working directory for personalized analysis.
```

## Critical Rules

1. **Data first, always.** Every sub-skill must gather real data via web search BEFORE producing analysis. No skill should generate output from training data alone.
2. **CONTEXT.md is king.** Every analysis must be tailored to the specific company context. Generic output is unacceptable.
3. **Investor-ready quality.** Every output file must be formatted and written at a level suitable for sharing with investors, board members, or senior advisors.
4. **Save outputs.** Every skill saves its output as a markdown file in the current working directory. File names are ALL CAPS with hyphens (e.g., `MARKET-SIZING.md`).
5. **Graceful degradation.** If API keys for Tier 2/3 tools are not available, fall back to Claude's built-in web search. Never fail silently.
