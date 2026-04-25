# So What Iteration Plan

## Purpose

The next iteration should make the research draft more useful to a reviewer or decision-maker by answering: "What should we do differently because of this research?"

The answer should stay cautious: the current evidence is review-ready screening evidence, not publication-grade causal evidence. The practical output should be a local mortgage-rate stress-monitoring prototype with separate price-pass-through and transaction-stress channels.

## Current Position

- `H1` remains low-confidence directional evidence: supply-flow tightness is a candidate price-pass-through feature, but it is sensitive to London and mortgage-rate timing.
- `H2` remains inconclusive: supply-flow tightness does not show a clean transaction-volume decline channel.
- `H3` remains mixed: vacancy tightness is inconclusive for prices but stronger as a transaction-stress marker.
- `H4` remains inconclusive: the quoted-effective spread is not a useful price channel in the current design.
- `H5` remains low-confidence: the recent fixed-rate episode weakens when completion windows are shifted.
- The public conclusion should be: build and validate a stress-monitoring prototype, not a standalone local price-risk score.

## Execution Checklist

1. Review `research-draft.md` and confirm the Executive Summary, So What section, Interpretation, Decision Implications, Limitations, and Next Steps all tell the same story.
2. Keep the `So What` section near the top of the draft, immediately after `Executive Summary`, with one short paragraph, one practical table, and one recommended next artifact.
3. Maintain the `Decision Implications` table with explicit statuses: `Use now`, `Use cautiously`, `Watch`, and `Do not use yet`.
4. Keep the `Candidate Stress Monitor` subsection focused on two channels:
   - Price-pass-through screening: supply-flow tightness, mortgage-rate timing variants, London/non-London splits, and price-measurement robustness.
   - Transaction-stress screening: vacancy tightness, transaction-volume responses, latest-quarter completeness flags, and timing variants.
5. Keep the first three `Next Steps` decision-artifact focused:
   - Refresh completed-sale data after more registrations arrive.
   - Build the stress-monitoring prototype.
   - Validate the prototype out of sample against simple baselines.
6. Keep limitations visible wherever practical implications are discussed: London sensitivity, completed-sale timing lag, observed rather than exogenous mortgage-rate shocks, current NSPL geography, and lack of hedonic or repeat-sales adjustment.

## Prototype Specification For The Next Iteration

The next artifact should be a research-facing monitor, not an operational decision rule.

Minimum inputs:

- LAD identifier and name.
- Latest stable completed-sale quarter.
- Supply-flow tightness proxy.
- Vacancy or long-vacancy tightness proxy.
- Mortgage-rate timing variant used.
- London/non-London flag.
- Data freshness warning.

Minimum outputs:

- Price-pass-through candidate signal.
- Transaction-stress candidate signal.
- Confidence label.
- Short caveat string explaining the main reason confidence is not higher.
- Validation status against simple baselines.

Default confidence rule:

- `High`: do not assign in the current evidence base.
- `Medium`: use only if direction and significance survive timing, geography, composition, labour, sparsity, and constraint-definition checks.
- `Medium-low`: use for vacancy-led transaction stress if the signal remains stable in the next validation pass.
- `Low`: use for supply-flow price pass-through unless London and timing sensitivity are resolved.
- `Inconclusive`: use when direction is unstable or mostly null.

## Constraints

- Do not add new warehouse pulls unless a data-dependent claim cannot be checked from existing local artifacts.
- Do not add disallowed market-platform source classes or terminology.
- Do not add public operational spend-control language.
- Do not commit local tabular extract outputs unless the repository policy changes.
- Preserve the AI disclaimer and evidence-status framing.
- Preserve source references to official data sources already used in the draft.

## Validation Checklist

- Confirm `research-draft.md` contains `## So What`.
- Confirm the draft does not reference local extract filenames directly.
- Confirm all figure references point to committed SVG files under `outputs/`.
- Search the research folder for disallowed source terminology and remove any matches.
- Search the public draft for operational spend-control terms and remove any matches.
- Confirm `git diff` only includes the intended Markdown files unless the analysis was intentionally rerun.

## Suggested Final Answer After Iteration

If asked "so what?", answer:

> This does not yet prove a causal supply-constraint price channel. The useful takeaway is narrower: supply-flow tightness is worth monitoring as a candidate price-pass-through feature, while vacancy tightness is the stronger transaction-stress marker. The next step is to build a two-channel local mortgage-rate stress monitor, keep confidence warnings visible, and validate it before using it for decisions.
