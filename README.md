# Nonprofit Workflow Skills

Nonprofit Workflow Skills helps nonprofit teams turn program plans, funder requirements, budgets, and results into useful working documents. Five reusable skills guide common tasks. They instruct models to use source evidence, flag missing information, and prepare outputs for staff review.

The project includes the skills, evaluation rubrics, and results. V2 expands evaluation from 20 to 50 development cases and adds focused improvements to the existing workflows.

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

See [installation guidance](plugin/README.md) for Codex and platform testing notes. V2 retains the original five workflows and staff approval. Native Claude validation of the updated instructions remains pending.

Models can make mistakes. Check facts, calculations, permissions and sensitive information before sharing your work.

## What changed in V2

- **30 additional evaluation cases:** 50 development cases in total, ten per workflow. The recorded case set contains 20 original cases and 30 extensions.
- **Clearer grading guidance:** accept evidence that applies across related findings, distinguish missing evidence from demonstrated errors, and select review statuses consistently.
- **Targeted skill fixes:** distinguish matching funds from total financing, preserve exact eligibility intervals and counting units, and connect findings to the supplied program goal.
- **Stronger evidence checks:** inspect the complete source packet, report missing responses, and check consent and disclosure across the whole output.

The five workflows and file-based approach remain unchanged. No setup interview, connector, or automatic submission step is required. See the [evaluation guide](evals/README.md) for methods, results, and remaining limits.

## Evaluation results

The October comparison found **26/50 whole-task passes (52%)**, compared with **20/50 (40%)** for its V1 reference: **+12 percentage points**. Ten cases improved, four regressed, and 36 tied. No cases were excluded.

The test compared the September 7 V1 review package with a V2 development snapshot. Those tested files differ from the exact public V1 and the prepared V2 update. The result measures progress during development; it is not a direct before-and-after score for the two public versions. The prepared V2 update has not had a complete model evaluation. The [evaluation guide](evals/README.md) identifies the tested versions and explains the limits.

| Measure | V1 reference | Evaluated V2 snapshot |
|---|---:|---:|
| Whole-task passes | 20/50 (40%) | 26/50 (52%) |
| Mean applicable-criterion score | 95.69% | 96.26% |
| Outputs with a critical failure flag | 13/50 | 8/50 |

Both versions used the same 50 cases and GPT-6.1 Sol at High effort. All cases were used during development. The grader was nonblind and has known errors. These results show observed progress on these cases; they do not establish general reliability or improved Claude performance.

Known evaluation failures include omitted grant-eligibility intervals and internal approval procedures in recipient copy. Staff must check original requirements and recipient text before use. Later targeted checks and their limits are documented in the evaluation guide.

The [original three-model results](evals/README.md#september-2026-original-evaluation) remain available without score changes. They compare skills with no skills and use a different metric. See [evaluation methods and results](evals/README.md) for both studies, regressions, and grading limits.

## How we tested

Each paired comparison used the same task and source package. The October comparison used frozen grading rules and reported whole-task outcomes alongside criterion scores. The [evaluation guide](evals/README.md) explains what changed and what remains uncertain.

Run the offline checks with:

```sh
python3 evals/verify.py
```

These checks verify the original results arithmetic, rubric inventory, and local links. They do not check the October comparison or run models.

## Layout

- [plugin/](plugin/) — the five skills and shared references.
- [evals/](evals/) — evaluation rubrics, methods and results.
