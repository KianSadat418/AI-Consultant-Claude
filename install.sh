#!/bin/bash
#
# install.sh -- Install the /founder Claude Code skill package
#
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/YOUR_USERNAME/founder-claude/main/install.sh | bash
#
# Or clone and run locally:
#   git clone https://github.com/YOUR_USERNAME/founder-claude.git
#   cd founder-claude && bash install.sh
#

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

echo ""
echo -e "${CYAN}${BOLD}"
echo "  ╔══════════════════════════════════════════════════╗"
echo "  ║                                                  ║"
echo "  ║   /founder -- Founder Toolkit for Claude Code    ║"
echo "  ║                                                  ║"
echo "  ║   18 Skills | 5 Agents | 6 Scripts               ║"
echo "  ║   McKinsey-level strategic analysis              ║"
echo "  ║                                                  ║"
echo "  ╚══════════════════════════════════════════════════╝"
echo -e "${NC}"

# Check dependencies
echo -e "${BOLD}Checking dependencies...${NC}"

# Python check
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2)
    echo -e "  ${GREEN}✓${NC} Python $PYTHON_VERSION"
elif command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version 2>&1 | cut -d' ' -f2)
    echo -e "  ${GREEN}✓${NC} Python $PYTHON_VERSION"
else
    echo -e "  ${YELLOW}!${NC} Python not found (optional, needed for API-powered features)"
fi

# Git check
if command -v git &> /dev/null; then
    echo -e "  ${GREEN}✓${NC} Git $(git --version | cut -d' ' -f3)"
else
    echo -e "  ${RED}✗${NC} Git not found. Please install git first."
    exit 1
fi

# Determine source directory
if [ -f "./founder/SKILL.md" ]; then
    # Running from cloned repo
    SOURCE_DIR="."
    echo -e "  ${GREEN}✓${NC} Running from cloned repository"
else
    # Clone to temp directory
    TEMP_DIR=$(mktemp -d)
    echo -e "\n${BOLD}Cloning repository...${NC}"
    git clone --quiet https://github.com/YOUR_USERNAME/founder-claude.git "$TEMP_DIR"
    SOURCE_DIR="$TEMP_DIR"
    echo -e "  ${GREEN}✓${NC} Repository cloned"
fi

# Create target directories
CLAUDE_DIR="$HOME/.claude"
COMMANDS_DIR="$CLAUDE_DIR/commands"
AGENTS_DIR="$CLAUDE_DIR/agents"
SCRIPTS_DIR="$CLAUDE_DIR/scripts/founder"
TEMPLATES_DIR="$CLAUDE_DIR/templates/founder"

mkdir -p "$COMMANDS_DIR"
mkdir -p "$AGENTS_DIR"
mkdir -p "$SCRIPTS_DIR"
mkdir -p "$TEMPLATES_DIR"

# Install orchestrator skill
echo -e "\n${BOLD}Installing skills...${NC}"
mkdir -p "$COMMANDS_DIR/founder"
cp "$SOURCE_DIR/founder/SKILL.md" "$COMMANDS_DIR/founder/SKILL.md"
echo -e "  ${GREEN}✓${NC} /founder (orchestrator)"

# Install sub-skills
SKILLS=(
    "founder-tam"
    "founder-trends"
    "founder-compete"
    "founder-persona"
    "founder-swot"
    "founder-gtm"
    "founder-pricing"
    "founder-risk"
    "founder-journey"
    "founder-uniteco"
    "founder-model"
    "founder-raise"
    "founder-pitch"
    "founder-legal"
    "founder-equity"
    "founder-expand"
    "founder-analyze"
    "founder-synthesis"
)

for skill in "${SKILLS[@]}"; do
    if [ -f "$SOURCE_DIR/skills/$skill/SKILL.md" ]; then
        mkdir -p "$COMMANDS_DIR/$skill"
        cp "$SOURCE_DIR/skills/$skill/SKILL.md" "$COMMANDS_DIR/$skill/SKILL.md"
        echo -e "  ${GREEN}✓${NC} $skill"
    else
        echo -e "  ${YELLOW}!${NC} $skill (not found, skipping)"
    fi
done

# Install agents
echo -e "\n${BOLD}Installing agents...${NC}"
AGENT_FILES=(
    "founder-market-agent.md"
    "founder-competitive-agent.md"
    "founder-strategy-agent.md"
    "founder-finance-agent.md"
    "founder-legal-agent.md"
)

for agent in "${AGENT_FILES[@]}"; do
    if [ -f "$SOURCE_DIR/agents/$agent" ]; then
        cp "$SOURCE_DIR/agents/$agent" "$AGENTS_DIR/$agent"
        echo -e "  ${GREEN}✓${NC} $agent"
    else
        echo -e "  ${YELLOW}!${NC} $agent (not found, skipping)"
    fi
done

# Install scripts
echo -e "\n${BOLD}Installing scripts...${NC}"
SCRIPT_FILES=(
    "fetch_context.py"
    "scrape_competitor.py"
    "market_research.py"
    "crunchbase_comps.py"
    "web_search.py"
    "run_parallel_agents.py"
)

for script in "${SCRIPT_FILES[@]}"; do
    if [ -f "$SOURCE_DIR/scripts/$script" ]; then
        cp "$SOURCE_DIR/scripts/$script" "$SCRIPTS_DIR/$script"
        chmod +x "$SCRIPTS_DIR/$script"
        echo -e "  ${GREEN}✓${NC} $script"
    else
        echo -e "  ${YELLOW}!${NC} $script (not found, skipping)"
    fi
done

# Install templates
echo -e "\n${BOLD}Installing templates...${NC}"
if [ -d "$SOURCE_DIR/templates" ]; then
    cp "$SOURCE_DIR/templates/"*.md "$TEMPLATES_DIR/" 2>/dev/null || true
    TEMPLATE_COUNT=$(ls -1 "$TEMPLATES_DIR/"*.md 2>/dev/null | wc -l)
    echo -e "  ${GREEN}✓${NC} $TEMPLATE_COUNT templates installed"
fi

# Install Python dependencies (optional)
if command -v pip3 &> /dev/null || command -v pip &> /dev/null; then
    if [ -f "$SOURCE_DIR/requirements.txt" ]; then
        echo -e "\n${BOLD}Installing Python dependencies...${NC}"
        PIP_CMD=$(command -v pip3 || command -v pip)
        $PIP_CMD install -r "$SOURCE_DIR/requirements.txt" --quiet 2>/dev/null && \
            echo -e "  ${GREEN}✓${NC} Python packages installed" || \
            echo -e "  ${YELLOW}!${NC} Some packages failed to install (optional)"
    fi
fi

# Cleanup temp directory
if [ -n "$TEMP_DIR" ] && [ -d "$TEMP_DIR" ]; then
    rm -rf "$TEMP_DIR"
fi

# Success summary
echo ""
echo -e "${GREEN}${BOLD}"
echo "  ══════════════════════════════════════════════════"
echo "  Installation complete!"
echo "  ══════════════════════════════════════════════════"
echo -e "${NC}"
echo -e "  ${BOLD}Installed:${NC}"
echo "    18 skills (commands)"
echo "     5 parallel analysis agents"
echo "     6 Python scripts"
echo "     7 output templates"
echo ""
echo -e "  ${BOLD}Quick Start:${NC}"
echo "    1. Create your company context file:"
echo -e "       ${CYAN}cp ~/.claude/templates/founder/CONTEXT-template.md ./CONTEXT.md${NC}"
echo "       (then edit CONTEXT.md with your company details)"
echo ""
echo "    2. Run any command in Claude Code:"
echo -e "       ${CYAN}/founder${NC}              -- See all commands"
echo -e "       ${CYAN}/founder tam${NC}           -- Market sizing"
echo -e "       ${CYAN}/founder compete${NC}       -- Competitive landscape"
echo -e "       ${CYAN}/founder analyze${NC}       -- Full company audit (flagship)"
echo ""
echo -e "  ${BOLD}Optional API Keys (for enhanced data):${NC}"
echo "    export ANTHROPIC_API_KEY=...    (parallel agents)"
echo "    export FIRECRAWL_API_KEY=...    (competitor scraping)"
echo "    export PERPLEXITY_API_KEY=...   (deep market research)"
echo "    export CRUNCHBASE_API_KEY=...   (funding comparables)"
echo ""
