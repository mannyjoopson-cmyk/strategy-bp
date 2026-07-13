# Strategy BP

Strategy BP is an open-source strategic research plugin for Codex. Before product definition, it turns an ambiguous direction into a decision question, falsifiable hypotheses, traceable evidence, and explicit action thresholds.

[中文说明](README.zh-CN.md)

## What It Does

- Screens emerging opportunities before committing to full research
- Evaluates market, user, competitor, commercial, and capability questions
- Separates facts, inferences, hypotheses, and recommendations
- Applies A-D evidence levels and independent-source checks
- Exposes conflicting evidence, limitations, counterexamples, and risks
- Produces validation metrics, scale conditions, and stop conditions

## Research Modes

- Opportunity scan: decide whether a direction deserves formal research.
- Standard research: the default mode for a complete direction decision.
- Deep diligence: for high-risk or high-investment decisions; paid data, outreach, private access, and personal-data processing require explicit approval.

## Install

After the GitHub repository is published, add it as a Codex marketplace and install the only plugin it contains:

```bash
codex plugin marketplace add mannyjoopson-cmyk/strategy-bp
codex plugin add strategy-bp@strategy-bp
```

For a local checkout, the first command can use the repository directory instead.

For skill-only use, copy `plugins/strategy-bp/skills/strategy-bp/` to `$CODEX_HOME/skills/strategy-bp/`, then start a new Codex task.

## Use

```text
Use strategy-bp in standard research mode to evaluate [product direction].
Clarify the decision, scope, and critical hypotheses first.
Apply A-D evidence levels and independent-source checks to critical conclusions.
Provide analysis and recommendations, but do not make the decision for me.
```

## Safety And Data

This plugin includes no hooks, MCP servers, credentials, analytics, automatic outreach, or data-purchasing capability. It must not contact people, enter private communities, or process personal data without explicit user approval.

## Repository Structure

- `.agents/plugins/marketplace.json`: single-plugin marketplace metadata
- `plugins/strategy-bp/skills/strategy-bp/`: installable skill and modular references
- `plugins/strategy-bp/templates/Strategy-Brief.md`: strategy research deliverable
- `plugins/strategy-bp/examples/`: routing examples for all three modes
- `plugins/strategy-bp/docs/ROLE-CONTRACT.md`: responsibilities and boundaries

## License

MIT. See `LICENSE`.
