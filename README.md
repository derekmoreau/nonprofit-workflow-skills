# Nonprofit Workflow Skills

Nonprofit Workflow Skills helps nonprofit teams turn program plans, funder requirements, budgets, and results into useful working documents. Five reusable skills guide common tasks, with instructions to ground claims in source material, flag missing information, and prepare outputs for staff review.

The project includes evaluation rubrics and results comparing model outputs with and without the skills across 20 development cases. The evaluation examines nonprofit relevance, evidence integrity, and usability.

Use the skills independently or follow a typical program lifecycle:

- **Logic Model:** connect activities, outputs and intended outcomes.
- **Grant Proposal:** draft applications against funder requirements.
- **Program Results:** explain results with clear calculations and evidence.
- **Grant Report:** prepare reports from program and financial records.
- **Review Before Sending:** check drafts against sources and destination requirements; use this throughout the workflow.

## Quick start

Clone the repository and load the plugin in Claude Code:

```sh
git clone https://github.com/derekmoreau/nonprofit-workflow-skills.git
cd nonprofit-workflow-skills
claude --plugin-dir ./plugin
```

See [installation guidance](plugin/README.md) for Codex and platform testing notes.

Models can make mistakes. Check facts, calculations, permissions and sensitive information before sharing your work.

## Results

Average improvement over the same model without skills, in percentage points, across four known development cases per workflow. All generation models used Medium effort. Results vary by task; review generated work before use.

| Workflow | Sonnet 5 | Opus 5 | GPT-5.6 Sol |
|---|---:|---:|---:|
| Logic Model | -6.9 | +8.0 | +8.7 |
| Grant Proposal | +11.7 | +22.7 | +19.6 |
| Program Results | -0.6 | +5.9 | +4.4 |
| Grant Report | +23.9 | +1.7 | +18.1 |
| Review Before Sending | +14.7 | +9.5 | +8.7 |
| **Overall mean** | **+8.6** | **+9.6** | **+11.9** |

## How we tested

Each case used the same prompt and source package with and without skills. We checked outputs against shared and workflow-specific rubrics using deterministic checks and an LLM judge, then averaged the paired score improvements. See [evals](evals/README.md) for the method, scoring notes and case results.

## Layout

- [plugin/](plugin/) — the five skills and shared references.
- [evals/](evals/) — evaluation rubrics, methods and results.
