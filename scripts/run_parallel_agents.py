#!/usr/bin/env python3
"""
run_parallel_agents.py -- Core script for the flagship /founder analyze command.
Spawns 5 parallel Claude API calls (one per analysis pillar) and synthesizes
results into a comprehensive company analysis.

Requires: ANTHROPIC_API_KEY environment variable.
Uses claude-sonnet-4-6 for parallel agents (speed + cost).
Uses claude-opus-4-6 for final synthesis (quality).

Usage:
  python run_parallel_agents.py
  python run_parallel_agents.py --context ./CONTEXT.md
  python run_parallel_agents.py --no-synthesis  # Skip final synthesis step
"""

import os
import sys
import json
import asyncio
import time
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

try:
    import anthropic
except ImportError:
    print("[founder] ERROR: anthropic SDK not installed. Run: pip install anthropic")
    sys.exit(1)


# Configuration
AGENT_MODEL = "claude-sonnet-4-6"
SYNTHESIS_MODEL = "claude-opus-4-6"
MAX_TOKENS_AGENT = 4096
MAX_TOKENS_SYNTHESIS = 8192

AGENTS_DIR = os.path.expanduser("~/.claude/agents")
AGENT_FILES = {
    "market": "founder-market-agent.md",
    "competitive": "founder-competitive-agent.md",
    "strategy": "founder-strategy-agent.md",
    "finance": "founder-finance-agent.md",
    "legal": "founder-legal-agent.md",
}


def load_context(context_path=None):
    """Load CONTEXT.md from specified path or current directory."""
    if context_path:
        path = context_path
    else:
        candidates = ["CONTEXT.md", "context.md", "Context.md"]
        path = None
        for name in candidates:
            full_path = os.path.join(os.getcwd(), name)
            if os.path.exists(full_path):
                path = full_path
                break

    if not path or not os.path.exists(path):
        print("[founder] ERROR: No CONTEXT.md found.")
        print("[founder] Create one with: cp ~/.claude/templates/founder/CONTEXT-template.md ./CONTEXT.md")
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"[founder] Loaded context from: {path} ({len(content)} chars)")
    return content


def load_agent_prompt(agent_name):
    """Load an agent's system prompt from the agents directory."""
    filepath = os.path.join(AGENTS_DIR, AGENT_FILES[agent_name])
    if not os.path.exists(filepath):
        print(f"[founder] WARNING: Agent file not found: {filepath}")
        return None

    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


async def run_agent(client, agent_name, system_prompt, context):
    """Run a single agent and return its output."""
    start = time.time()
    print(f"[founder] Starting {agent_name} agent...")

    user_message = f"""Analyze the following company and produce your assessment.

COMPANY CONTEXT:
{context}

Produce your complete analysis now. Output valid JSON only."""

    try:
        response = await asyncio.to_thread(
            client.messages.create,
            model=AGENT_MODEL,
            max_tokens=MAX_TOKENS_AGENT,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )

        output = ""
        for block in response.content:
            if block.type == "text":
                output += block.text

        elapsed = time.time() - start
        print(f"[founder] {agent_name} agent complete ({elapsed:.1f}s, {len(output)} chars)")
        return {"agent": agent_name, "output": output, "elapsed": elapsed, "success": True}

    except Exception as e:
        elapsed = time.time() - start
        print(f"[founder] {agent_name} agent FAILED ({elapsed:.1f}s): {e}")
        return {"agent": agent_name, "output": "", "elapsed": elapsed, "success": False, "error": str(e)}


async def run_synthesis(client, agent_outputs, context):
    """Run the final synthesis using Opus."""
    print(f"\n[founder] Running final synthesis with {SYNTHESIS_MODEL}...")
    start = time.time()

    # Build synthesis prompt
    pillar_summaries = []
    for result in agent_outputs:
        if result["success"]:
            pillar_summaries.append(
                f"## {result['agent'].upper()} ANALYSIS\n{result['output']}"
            )
        else:
            pillar_summaries.append(
                f"## {result['agent'].upper()} ANALYSIS\n[Analysis failed: {result.get('error', 'unknown error')}]"
            )

    all_analyses = "\n\n---\n\n".join(pillar_summaries)

    system_prompt = """You are a McKinsey senior partner synthesizing a team's analysis into a comprehensive strategy document. You have 5 pillar analyses (market, competitive, strategy, finance, legal) and the company context.

Your job:
1. Synthesize all findings into a cohesive narrative
2. Identify the most important insights across all pillars
3. Resolve any contradictions between pillar analyses
4. Produce a board-ready executive strategy document
5. Provide clear, actionable recommendations with priorities

Write in a confident, direct, evidence-based tone. Be honest about risks.
The output should feel like it took a team of analysts a week to produce.

Format as clean markdown. Do not output JSON for this step."""

    user_message = f"""COMPANY CONTEXT:
{context}

PILLAR ANALYSES:
{all_analyses}

Synthesize these analyses into a comprehensive Company Analysis document.
Include: Executive Summary, Market Analysis, Competitive Landscape, Strategic Assessment, Financial Assessment, Legal & Risk Assessment, Strategic Recommendations (3 paths), Top 10 Priority Initiatives, and a "1 Hour Brief"."""

    try:
        response = await asyncio.to_thread(
            client.messages.create,
            model=SYNTHESIS_MODEL,
            max_tokens=MAX_TOKENS_SYNTHESIS,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )

        output = ""
        for block in response.content:
            if block.type == "text":
                output += block.text

        elapsed = time.time() - start
        print(f"[founder] Synthesis complete ({elapsed:.1f}s, {len(output)} chars)")
        return output

    except Exception as e:
        elapsed = time.time() - start
        print(f"[founder] Synthesis FAILED ({elapsed:.1f}s): {e}")
        return None


async def main_async(context_path=None, skip_synthesis=False):
    """Main async execution flow."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("[founder] ERROR: ANTHROPIC_API_KEY environment variable not set.")
        print("[founder] Set it with: export ANTHROPIC_API_KEY=your-key-here")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    context = load_context(context_path)

    # Load all agent prompts
    agents = {}
    for name in AGENT_FILES:
        prompt = load_agent_prompt(name)
        if prompt:
            agents[name] = prompt
        else:
            print(f"[founder] Skipping {name} agent (prompt not found)")

    if not agents:
        print("[founder] ERROR: No agent prompts found. Check installation.")
        sys.exit(1)

    print(f"\n[founder] Launching {len(agents)} parallel agents...")
    print(f"[founder] Agent model: {AGENT_MODEL}")
    print(f"[founder] Synthesis model: {SYNTHESIS_MODEL}")
    print()

    total_start = time.time()

    # Run all agents in parallel
    tasks = [
        run_agent(client, name, prompt, context)
        for name, prompt in agents.items()
    ]
    results = await asyncio.gather(*tasks)

    # Save individual agent outputs
    for result in results:
        if result["success"]:
            filename = f"_agent-{result['agent']}-output.json"
            filepath = os.path.join(os.getcwd(), filename)
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)
            print(f"[founder] Saved: {filename}")

    # Report status
    successful = sum(1 for r in results if r["success"])
    failed = sum(1 for r in results if not r["success"])
    print(f"\n[founder] Agent results: {successful} successful, {failed} failed")

    # Run synthesis
    if not skip_synthesis and successful > 0:
        synthesis = await run_synthesis(client, results, context)

        if synthesis:
            output_path = os.path.join(os.getcwd(), "COMPANY-ANALYSIS.md")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(synthesis)
            print(f"\n[founder] Analysis saved: {output_path}")
        else:
            print("[founder] Synthesis failed. Individual agent outputs are saved.")
    elif skip_synthesis:
        print("[founder] Synthesis skipped (--no-synthesis flag).")
    else:
        print("[founder] No successful agent outputs to synthesize.")

    total_elapsed = time.time() - total_start
    print(f"\n[founder] Total execution time: {total_elapsed:.1f}s")

    # Cost estimate
    # Rough estimate: ~1000 input tokens + ~4000 output tokens per agent
    # Sonnet: $3/M input, $15/M output
    # Opus synthesis: $15/M input, $75/M output
    agent_cost = successful * (0.003 * 1 + 0.015 * 4)  # ~$0.063 per agent
    synth_cost = 0.015 * 20 + 0.075 * 8  # ~$0.90 for synthesis
    total_est = agent_cost + synth_cost
    print(f"[founder] Estimated API cost: ~${total_est:.2f}")


def main():
    context_path = None
    skip_synthesis = False

    for i, arg in enumerate(sys.argv[1:], 1):
        if arg == "--context" and i < len(sys.argv) - 1:
            context_path = sys.argv[i + 1]
        elif arg == "--no-synthesis":
            skip_synthesis = True

    asyncio.run(main_async(context_path, skip_synthesis))


if __name__ == "__main__":
    main()
