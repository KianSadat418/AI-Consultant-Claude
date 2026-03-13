#!/bin/bash
#
# uninstall.sh -- Remove the /founder Claude Code skill package
#

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
NC='\033[0m'

echo ""
echo -e "${BOLD}Uninstalling /founder skill package...${NC}"
echo ""

CLAUDE_DIR="$HOME/.claude"
REMOVED=0

# Remove skills
SKILLS=(
    "founder"
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

echo -e "${BOLD}Removing skills...${NC}"
for skill in "${SKILLS[@]}"; do
    SKILL_DIR="$CLAUDE_DIR/commands/$skill"
    if [ -d "$SKILL_DIR" ]; then
        rm -rf "$SKILL_DIR"
        echo -e "  ${GREEN}✓${NC} Removed $skill"
        REMOVED=$((REMOVED + 1))
    fi
done

# Remove agents
echo -e "\n${BOLD}Removing agents...${NC}"
AGENT_FILES=(
    "founder-market-agent.md"
    "founder-competitive-agent.md"
    "founder-strategy-agent.md"
    "founder-finance-agent.md"
    "founder-legal-agent.md"
)

for agent in "${AGENT_FILES[@]}"; do
    AGENT_PATH="$CLAUDE_DIR/agents/$agent"
    if [ -f "$AGENT_PATH" ]; then
        rm -f "$AGENT_PATH"
        echo -e "  ${GREEN}✓${NC} Removed $agent"
        REMOVED=$((REMOVED + 1))
    fi
done

# Remove scripts
echo -e "\n${BOLD}Removing scripts...${NC}"
if [ -d "$CLAUDE_DIR/scripts/founder" ]; then
    rm -rf "$CLAUDE_DIR/scripts/founder"
    echo -e "  ${GREEN}✓${NC} Removed scripts/founder/"
    REMOVED=$((REMOVED + 1))
fi

# Remove templates
echo -e "\n${BOLD}Removing templates...${NC}"
if [ -d "$CLAUDE_DIR/templates/founder" ]; then
    rm -rf "$CLAUDE_DIR/templates/founder"
    echo -e "  ${GREEN}✓${NC} Removed templates/founder/"
    REMOVED=$((REMOVED + 1))
fi

echo ""
if [ $REMOVED -gt 0 ]; then
    echo -e "${GREEN}${BOLD}Uninstall complete.${NC} Removed $REMOVED components."
else
    echo -e "${YELLOW}Nothing to remove. The /founder package was not installed.${NC}"
fi

echo ""
echo "Note: Python packages (anthropic, firecrawl-py, etc.) were NOT removed."
echo "To remove them: pip uninstall anthropic firecrawl-py requests beautifulsoup4"
echo ""
echo "Any analysis files (MARKET-SIZING.md, COMPANY-ANALYSIS.md, etc.) in your"
echo "working directories were NOT removed."
echo ""
