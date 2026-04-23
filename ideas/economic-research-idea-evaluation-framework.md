# Economics Research Idea Evaluation Framework

> Disclaimer: This document was generated with AI and has received only limited human review. It may contain errors or omissions and should be independently verified before use.

## Purpose

- This framework is for ranking AI-assisted quantitative research and forecasting ideas by real economic usefulness, not by academic novelty alone.
- The goal is to prioritize studies that can influence decisions such as pricing, investment, lending, development, risk management, policy, or allocation.
- It is designed to work with the current `re_trends` data spine first, while explicitly accounting for variables that can be added from open public sources.
- It should be used before a full research plan is written, so weak ideas are filtered out early and strong ideas are made operational quickly.

## What Good Ideas Look Like

A strong idea in this system should satisfy all of the following:

- It answers a decision-relevant question, not a literature-only question.
- It has a clear measurable outcome and a clear economic mechanism.
- It can be executed with credible identification or forecast logic.
- It uses existing internal data where possible and only asks for new extraction when the upside is large enough.
- It creates reusable assets such as panels, joins, shocks, or forecasting features that improve future work.

## What Should Be Rejected Early

Reject or heavily penalize ideas with one or more of these features:

- The output is mainly “research about research” rather than a direct economic insight.
- The intended user or decision is unclear.
- The outcome is interesting but not economically actionable.
- The main variable is unavailable internally and hard to obtain cleanly from open sources.
- The design is descriptive in a way that is likely to confuse correlation with mechanism.
- The geography, timing, or unit of observation do not line up cleanly enough to support the claim.

## Evaluation Process

Use a two-stage process rather than a single score.

### Stage 1. Hard Gates

An idea should proceed to scoring only if it passes these five gates:

1. `Decision gate`
   The idea must name the decision it could improve, for example house-price forecasting, local risk monitoring, supply planning, mortgage sensitivity, or affordability analysis.
2. `Outcome gate`
   The target variable must be measurable from existing tables or a realistic build path.
3. `Mechanism gate`
   The causal or predictive channel must be explainable in one sentence.
4. `Data gate`
   At least one viable path must exist:
   - internal tables already support it, or
   - the missing variable can be extracted from open sources with acceptable effort and reliability.
5. `Design gate`
   There must be a plausible empirical design, forecast framework, or monitoring design that could survive basic skepticism.

If any gate clearly fails, do not score the idea highly just because it sounds interesting.

### Stage 2. Weighted Scorecard

Score only ideas that pass Stage 1.

| Block | Weight | What it measures |
| --- | --- | --- |
| Impact | `45` | Whether the idea could materially improve an economic decision |
| Feasibility | `35` | Whether we can execute it credibly with available or realistically obtainable data |
| Strategic fit | `20` | Whether the work strengthens the broader research platform rather than being a one-off |

Total score: `100`.

## Block A. Impact (`45`)

Impact should dominate the framework. A technically easy idea should not outrank a materially important one unless the important one is close to impossible.

### `A1` Decision leverage (`0-15`)

How much could the result change a real decision if it is true?

- `0-3`: Mostly descriptive or intellectually interesting
- `4-7`: Useful context for a decision, but not central
- `8-11`: Likely to change thresholds, prioritization, or forecast interpretation
- `12-15`: Directly changes pricing, allocation, risk limits, investment, lending, development, or policy choices

### `A2` Economic exposure (`0-10`)

How large is the economic surface area affected?

- `0-2`: Narrow niche or low-value segment
- `3-5`: Meaningful local or segment relevance
- `6-8`: Broad market or policy relevance
- `9-10`: Large national or multi-region consequence

### `A3` Timing and actionability (`0-10`)

Can the research matter on a useful decision horizon?

- `0-2`: Mostly historical reflection
- `3-5`: Helpful for periodic strategy reviews
- `6-8`: Useful for active monitoring, scenario analysis, or near-term decisions
- `9-10`: Useful in live or frequent operational decisions

### `A4` Edge versus obvious consensus (`0-10`)

Does the idea have a realistic chance to produce differentiated insight given our data and methods?

- `0-2`: Already obvious or commoditized
- `3-5`: Some incremental value
- `6-8`: Clear chance of non-trivial new insight
- `9-10`: Strong differentiated edge from our data stack, geography, or modeling setup

## Block B. Feasibility (`35`)

Feasibility is about credible execution, not just whether a dataset exists.

### `B1` Internal data readiness (`0-12`)

How much of the required data already exists in our tables?

- `0-2`: Core outcome or key driver missing
- `3-5`: Outcome exists, but major explanatory layers are absent
- `6-8`: Most of the needed spine exists with known caveats
- `9-10`: Strong internal fit with modest joins or cleaning
- `11-12`: Research can start immediately from mature internal tables

Use current internal assets as the default advantage set:

- `source_land_registry_price_paid`
- `dim_postcode_geography`
- `fact_lad_supply_year`
- `fact_lad_housing_stock_year`
- `mortgage_rates_monthly_effective`
- `mortgage_rates_monthly_quoted`
- `inflation_monthly_core`
- `fact_area_income_year`
- `fact_area_labour_month`
- `fact_area_demographics_year`
- `fact_area_deprivation`
- `fact_area_crime_month`
- `fact_area_environment`
- `dim_school`
- `fact_school_performance_year`
- `fact_school_ofsted_inspection`
- `mart_property_school_context`
- `fact_property_epc_certificate`
- `dim_property_epc_latest`

### `B2` Open-source augmentability (`0-8`)

If internal data is incomplete, how realistic is the external build path?

- `0-1`: No clear open-source source or legal path
- `2-3`: Possible, but fragile, inconsistent, or burdensome
- `4-5`: Obtainable from reputable public sources with some transformation work
- `6-7`: Clean open-data path with stable documentation and good coverage
- `8`: Strong public source already identified and easy to operationalize

Typical high-value open-source extensions already identified in the library include:

- ONS income, population, projections, migration, inflation, and labour datasets
- Nomis local labour market series
- Bank of England mortgage and credit series
- Police.uk and Home Office crime data
- DfE school performance and school register data
- DLUHC house building and dwelling stock releases
- Environment Agency flood data and DEFRA air-quality data
- DfT journey-time and accessibility datasets

### `B3` Geography and time alignment (`0-5`)

Do the outcome, drivers, and controls line up at usable spatial and temporal grains?

- `0-1`: Serious mismatch likely to invalidate the design
- `2`: Workable only with aggressive aggregation or weak assumptions
- `3`: Reasonable alignment with caveats
- `4`: Good alignment with manageable crosswalk issues
- `5`: Clean alignment across main sources

### `B4` Design credibility (`0-5`)

Can we estimate or forecast this in a way that is believable?

- `0-1`: No credible design yet
- `2`: Only weak descriptive correlations likely
- `3`: Plausible baseline design exists
- `4`: Strong design with multiple validation paths
- `5`: Strong design plus clear falsification, robustness, or backtesting plan

### `B5` Execution cost and fragility (`0-5`)

This is an inverse complexity score: higher is better.

- `0-1`: High engineering load, fragile joins, or heavy manual intervention
- `2`: Material build effort or maintenance burden
- `3`: Moderate effort
- `4`: Light implementation burden
- `5`: Fast to build and easy to maintain

## Block C. Strategic Fit (`20`)

This block prevents short-term but disposable work from crowding out platform-building research.

### `C1` Reusable asset creation (`0-8`)

Will this idea create durable data products, features, or panels for later studies?

- `0-2`: One-off output
- `3-5`: Some reusable components
- `6-8`: Creates a reusable backbone for multiple projects

### `C2` Forecast and monitoring value (`0-6`)

Does the output improve forecasting, nowcasting, scenario analysis, or risk monitoring beyond a single paper?

- `0-1`: Little forecasting relevance
- `2-3`: Some model-feature relevance
- `4-5`: Strong forecasting or monitoring value
- `6`: Likely to become a recurring model or monitoring component

### `C3` Communication clarity (`0-6`)

Can the result be explained clearly to decision-makers?

- `0-1`: Hard to communicate or too abstract
- `2-3`: Requires substantial translation
- `4-5`: Clear story with understandable implications
- `6`: Very clear mechanism, output, and decision consequence

## Recommended Thresholds

After scoring, classify ideas into one of four buckets.

| Bucket | Rule of thumb | Meaning |
| --- | --- | --- |
| `Build now` | `80+` total and at least `30` on impact and `24` on feasibility | High-value and executable immediately |
| `Build after one data asset` | `70-79` total or impact is high but feasibility is held back by one missing layer | Worth doing once a specific table or extraction is built |
| `Incubate` | `60-69` total | Keep in pipeline, but not yet priority |
| `Reject / archive` | Below `60` or failed Stage 1 gates | Do not spend active research time now |

Use judgment over the numeric cutoffs when one block is extremely strong or weak. For example, a project with exceptional impact but one missing open-data extraction may still deserve early infrastructure work.

## How To Score Data More Rigorously

When evaluating data, do not stop at “dataset exists.”

Score the idea on the following practical questions:

1. Is the main outcome already in a trusted internal table?
2. Are the main explanatory variables already modeled internally?
3. If not, are public sources stable, well-documented, and legally usable?
4. Can the external data be aligned to our geography and time conventions?
5. Do we need historical crosswalks, property matching, or entity resolution?
6. Are there release breaks, methodology breaks, or coverage gaps that would distort the claim?
7. Does the build create a reusable asset, or only serve this one idea?

An idea should lose points quickly if the answer to questions `4-6` is weak.

## Default Research Prioritization Logic

When two ideas have similar total scores, prefer the one that:

1. has higher `Decision leverage`
2. uses the current internal spine more directly
3. produces a reusable panel or feature layer
4. supports both explanation and forecasting
5. is easier to communicate to non-academic decision-makers

Do not let “novelty” break ties unless the first four considerations are already close.

## Suggested Intake Template

Every new idea should be written in this structure before scoring:

1. `Idea title`
2. `Decision user`
3. `Decision improved`
4. `Outcome variable`
5. `Main mechanism`
6. `Primary geography and time grain`
7. `Minimum internal tables needed`
8. `Open-source tables needed`
9. `Candidate design`
10. `Main failure risk`
11. `Why this could matter economically`

If the author cannot fill this in cleanly, the idea is not ready for prioritization.

## Worked Interpretation Of The Current Stack

With the current `re_trends` research base, the highest-scoring ideas should usually have these characteristics:

- They use `source_land_registry_price_paid` as the primary outcome backbone.
- They align well with `dim_postcode_geography`.
- They exploit existing area panels such as supply, stock, labour, income, crime, deprivation, environment, mortgage, inflation, school, or EPC data.
- They answer a question that could influence pricing, lending, development, local risk, or affordability views.
- They can be expressed as a panel model, event study, local projection, or forecast system with a credible validation strategy.

Ideas should usually be downgraded when they depend mainly on:

- a not-yet-built property-amenity layer
- unstable historical postcode mapping
- vague “AI will find patterns” logic without a decision channel
- a high-dimensional forecast target with no clear benchmark or backtest design

## Portfolio Rule

The research portfolio should stay balanced across three lanes:

- `Decision-critical now`
  These are high-impact, high-feasibility studies that can support active economic views and forecasts.
- `Asset-building next`
  These are ideas whose main value is to create a reusable table, crosswalk, or feature layer that unlocks multiple future studies.
- `Longer-horizon options`
  These may be important, but should wait until the data spine is stronger or the economic need becomes more immediate.

In practice, most active effort should stay in the first lane, with a smaller deliberate share in the second lane. The third lane should remain visible but not consume much execution time.

## Minimal Operating Rule

An idea should not enter active production research unless:

- it passes all Stage 1 gates
- it scores at least `30/45` on impact
- it has a believable path to at least `24/35` on feasibility
- it names the internal tables and external sources required
- it states what decision would change if the result is true

That rule is intentionally strict. It is meant to keep the pipeline focused on work that can matter economically and be executed to a high standard.
