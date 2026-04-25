# re_trends_research

> Disclaimer: This document was generated with AI and has received only limited human review. It may contain errors or omissions and should be independently verified before use.

This repository is a Markdown-first, AI-first research workspace for UK real-estate and economic analysis built around the `re_trends` data stack. It combines reusable research frameworks, a curated literature and dataset library, ranked project ideas, and worked research studies with SQL extracts, analysis code, and published outputs.

## What This Repo Contains

- `ai-first-research-frameworks/`: reusable frameworks for turning broad topics into decision-grade research plans and for ranking candidate ideas before execution.
- `library/`: supporting literature and factor-to-dataset reference material for housing-price research.
- `ideas/`: ranked research ideas derived from the literature and current data spine, including both Markdown and tabular versions.
- `researches/`: executed or in-progress studies, each with its own plan, draft, SQL extracts, analysis code, and outputs.

## Best Entry Points

- Start with [AI-First Research Plan Framework](./ai-first-research-frameworks/ai-first-research-plan-framework.md) for the planning standard.
- Use [AI-First Research Idea Evaluation Framework](./ai-first-research-frameworks/ai-first-research-idea-evaluation-framework.md) and the [template](./ai-first-research-frameworks/ai-first-research-idea-evaluation-template.md) to triage new studies.
- Read [Real Estate Price Dynamics Research Library](./library/real-estate-price-dynamics-research-library.md) for the conceptual literature spine.
- Read [Real Estate Factor, Mechanism, Dataset, And Starter Paper Matrix](./library/real-estate-factor-mechanism-dataset-matrix.md) for the bridge from theory to UK-first datasets.
- Read [Real Estate Price Mechanism Ranked Research Ideas](./ideas/real-estate-price-mechanism-ranked-ideas.md) for the prioritized project pipeline.

## Current Worked Study

The main completed example in the repo is [Mortgage-Rate Pass-Through Under Supply Constraints In England](./researches/mortgage-rate-pass-through-under-supply-constraints-uk/).

That study folder includes:

- [research-plan.md](./researches/mortgage-rate-pass-through-under-supply-constraints-uk/research-plan.md): the full AI-first research plan.
- [idea-evaluation.md](./researches/mortgage-rate-pass-through-under-supply-constraints-uk/idea-evaluation.md): the pre-build scoring and justification.
- [research-draft.md](./researches/mortgage-rate-pass-through-under-supply-constraints-uk/research-draft.md): the writeup of the first-pass empirical results.
- [queries/](./researches/mortgage-rate-pass-through-under-supply-constraints-uk/queries/): the SQL extract pipeline for the analysis inputs.
- [analysis/analyze.py](./researches/mortgage-rate-pass-through-under-supply-constraints-uk/analysis/analyze.py): a Python stdlib-only analysis script that reads the extracted CSVs and regenerates summary tables, charts, and Markdown outputs.
- [outputs/analysis-results-summary.md](./researches/mortgage-rate-pass-through-under-supply-constraints-uk/outputs/analysis-results-summary.md): the compact result summary.
- [outputs/](./researches/mortgage-rate-pass-through-under-supply-constraints-uk/outputs/): committed CSV extracts, model summaries, and SVG figures for the study.

## Repository Workflow

The intended workflow is:

1. Start from a decision question, not just a topic.
2. Use the framework files to score and shape a candidate idea.
3. Ground the idea in the literature and dataset library.
4. Promote the idea into a dedicated folder under `researches/`.
5. Store the research plan, idea evaluation, SQL extracts, analysis code, and generated outputs together.
6. Write review drafts that can later be hardened into publication-grade or operational work.

## Reproducing The Current Study Outputs

The current mortgage-rate study is structured so the analysis can be rerun from committed CSV extracts.

1. Refresh or replace the CSV files in [`researches/mortgage-rate-pass-through-under-supply-constraints-uk/outputs/`](./researches/mortgage-rate-pass-through-under-supply-constraints-uk/outputs/) by running the SQL files in [`queries/`](./researches/mortgage-rate-pass-through-under-supply-constraints-uk/queries/) against the underlying warehouse.
2. Run:

```bash
python3 researches/mortgage-rate-pass-through-under-supply-constraints-uk/analysis/analyze.py
```

3. The script rewrites the Markdown, CSV, and SVG artifacts in the study's `outputs/` directory.

The current analysis script has no third-party Python dependencies; it uses only the standard library.

## Notes

- This repository is documentation-heavy and intentionally keeps research context close to the generated outputs.
- Some study outputs are committed directly to make review easier without needing warehouse access.
- `.gitignore` currently excludes generated `outputs/*.csv` only for the mortgage-rate study path pattern that is explicitly listed there; review ignore rules if you add new study folders or new output types.
- Most documents in this repo are AI-assisted research artifacts and should be treated as draft analytical material unless independently validated.

## Git Guardrails

This repo treats `.gitignore` as a safety boundary.

- Ignored files must not be force-added.
- Pushes to `main` or `master` require explicit approval.
- History rewrites require explicit approval.

Versioned hooks live in `.githooks/`. Enable them in a local clone with:

```bash
git config core.hooksPath .githooks
```

For agent-specific safety rules, see [AGENTS.md](./AGENTS.md).
