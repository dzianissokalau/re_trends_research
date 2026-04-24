# Idea Evaluation: Mortgage-Rate Pass-Through Under Supply Constraints (UK)

> Evaluation date: 2026-04-24

## Inputs
- Research idea: [research_plan.md](./research_plan.md)
- Evaluation framework: [economic-research-idea-evaluation-framework.md](../../ideas/economic-research-idea-evaluation-framework.md)

## Overall Verdict
- Classification: `Build now`
- Total score: `81/100`

This idea scores highly because it is decision-relevant, executable with the current internal data spine, and likely to create reusable assets for later forecasting, monitoring, and housing-market mechanism work.

## Stage 1 Hard Gates
- `Decision gate`: Pass
  The study can improve local house-price forecasting, mortgage-sensitivity monitoring, scenario analysis, and interpretation of constrained versus slack housing markets.
- `Outcome gate`: Pass
  The core outcomes are already measurable from current tables, especially achieved sale prices and transaction counts from `source_land_registry_price_paid`.
- `Mechanism gate`: Pass
  The mechanism is clear: national mortgage-rate shocks should be capitalised more strongly into prices where supply and stock adjustment are weakest.
- `Data gate`: Pass
  The baseline study is feasible from current internal tables, with optional public-data extensions available later.
- `Design gate`: Pass
  The proposed `LAD-quarter` interacted panel and local-projection design are credible and can survive basic skepticism.

## Stage 2 Weighted Scorecard

| Block | Max | Score |
| --- | ---: | ---: |
| Impact | `45` | `35` |
| Feasibility | `35` | `27` |
| Strategic fit | `20` | `19` |
| Total | `100` | `81` |

## Detailed Scoring

### Block A. Impact (`35/45`)
- `A1` Decision leverage: `12/15`
  If true, the result would change how local price sensitivity is interpreted in stress tests, scenario analysis, and market allocation.
- `A2` Economic exposure: `8/10`
  Mortgage transmission and housing prices affect a large England-wide market with clear policy, lending, and investment relevance.
- `A3` Timing and actionability: `8/10`
  The study is useful on an active decision horizon because mortgage conditions move regularly and local pass-through matters in near-term monitoring.
- `A4` Edge versus obvious consensus: `7/10`
  The broad mechanism is not novel by itself, but the UK-specific implementation with the current `re_trends` stack still offers differentiated insight.

### Block B. Feasibility (`27/35`)
- `B1` Internal data readiness: `10/12`
  Most of the required spine already exists: prices, geography, supply, stock, vacancy, mortgage rates, inflation, and labour controls.
- `B2` Open-source augmentability: `6/8`
  Missing upgrades such as exogenous monetary-policy shocks or stronger planning-constraint measures have realistic public-data paths.
- `B3` Geography and time alignment: `4/5`
  Alignment is good for the headline `LAD-quarter` design, though weaker for `MSOA` robustness and older postcode-history joins.
- `B4` Design credibility: `4/5`
  The differential-pass-through design is strong, but without an exogenous policy-shock series the study should stop short of the strongest causal language.
- `B5` Execution cost and fragility: `3/5`
  The study is feasible now, but it still requires careful panel construction, methodology-break handling, and sample auditing.

### Block C. Strategic Fit (`19/20`)
- `C1` Reusable asset creation: `8/8`
  The study would create reusable `LAD-quarter` price panels, mortgage-shock series, and supply/vacancy interaction features.
- `C2` Forecast and monitoring value: `5/6`
  The output would be directly useful for scenario analysis, forecasting features, and recurring local market monitoring.
- `C3` Communication clarity: `6/6`
  The core message is easy to explain: rate shocks should matter more where supply and vacancy buffers are tighter.

## Why This Idea Scores Well
- It answers a real economic decision question rather than a literature-only question.
- It relies heavily on the current internal data spine rather than on speculative future builds.
- It has a plausible primary design and a well-defined robustness sequence.
- It creates reusable infrastructure rather than a one-off paper output.

## Main Weaknesses
- The mortgage shock is not yet fully exogenous.
- `dim_postcode_geography` is a latest-snapshot bridge, which may weaken older historical joins.
- Key supply-tightness measures are `LAD` level and annual, which limits the strength of fine-grained spatial claims.

## Best Upgrades
- Add an external exogenous policy-shock series such as MPC or OIS surprises.
- Add a historical postcode-geography bridge or narrow the main sample to the stable join period.
- Add stronger structural constraint measures such as planning or land-scarcity proxies.
- Add direct local mortgage origination or borrower-composition data if a clean source becomes available.

## Bottom Line
This is exactly the kind of idea the framework is designed to prioritize: high decision relevance, strong current feasibility, and strong platform-building value. The cleanest current claim is differential mortgage-rate pass-through under local supply and stock tightness, with a clear path to stronger causal identification later.
