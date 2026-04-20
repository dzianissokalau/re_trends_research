# Mortgage-Rate Pass-Through Under Supply Constraints (UK)

> Disclaimer: This document was generated with AI and has received only limited human review. It may contain errors or omissions and should be independently verified before use.

## Purpose

This document is a build sheet for an AI research agent that will execute the actual study.

The target question is:

> Do national mortgage-rate shocks capitalise more strongly into local UK house prices where supply and stock adjustment are weakest?

The plan below is intentionally operational. It tells the next agent:

- what the core estimand is
- which datasets in this repo are primary versus optional
- how to align different time and geography grains
- which empirical designs are credible with current data
- what to do if identification or data quality weakens

## One-Sentence Thesis

The working thesis is that the same national mortgage-rate move should produce a larger local price response in places where housing supply is hard to expand and vacant stock is scarce, because quantities cannot adjust easily and financing changes are capitalised more into prices.

## Core Hypotheses

### `H1` Baseline heterogeneity

For a given national mortgage-rate shock, real house prices respond more in supply-constrained local markets than in less constrained markets.

### `H2` Quantity-versus-price adjustment

Where supply is more elastic, the same mortgage shock should show up relatively more in transaction volumes and relatively less in prices.

### `H3` Stock tightness channel

Low vacancy and low long-term vacancy strengthen pass-through because the local stock buffer is small even if annual supply flows are not unusually low.

### `H4` Credit-friction channel

If the quoted-effective mortgage spread matters more than the mortgage-rate level, the mechanism is better described as tightening/friction/selection rather than pure user-cost pass-through.

### `H5` Recent-UK contract-structure nuance

Pass-through should be slower and more episode-dependent in the UK after the rise of fixed-rate lending, especially after 2016, so timing matters as much as average effect size.

## Recommended Study Design

Use a tiered design rather than trying to force one specification to do everything.

1. `LAD-quarter` panel as the primary design.
2. `MSOA-quarter` panel as a higher-resolution robustness layer using `LAD` constraint proxies.
3. National event-study and descriptive episode charts to interpret timing.
4. Optional higher-resolution transaction-side extensions after the baseline design is stable.
5. Optional repeat-sale-leaning extension only after property identity work is good enough.

Why `LAD` first:

- the strongest supply and stock datasets in the repo are `LAD` level
- claimant-rate controls are already `local_authority` monthly
- `MSOA` work is possible, but the key constraint proxies must be inherited from `LAD`, which weakens interpretation

## Literature Overview

The research should be framed as the intersection of four literatures: user cost, mortgage/credit transmission, supply elasticity, and UK-specific mortgage-market transmission.

### `1` User cost and housing asset pricing

- `Poterba (1984)`, *Tax Subsidies to Owner-Occupied Housing: An Asset-Market Approach*.
  Main use here: the conceptual anchor that financing conditions and inflation affect the user cost of owner-occupation and can capitalise into house values.
  Source: [NBER working paper page with published-version reference](https://www.nber.org/papers/w0553)

- `Mishkin (2007)`, *Housing and the Monetary Transmission Mechanism*.
  Main use here: housing is a key transmission channel, but the effect depends on prices, collateral, expectations, and supply response rather than a single direct rate-price mapping.
  Source: [NBER](https://www.nber.org/papers/w13518)

### `2` Mortgage credit and house prices

- `Adelino, Schoar, and Severino`, *Credit Supply and House Prices: Evidence from Mortgage Market Segmentation*.
  Main use here: easier credit raises house prices, with stronger effects in lower-supply-elasticity places; also a warning that elasticities may be smaller than some aggregate studies imply.
  Source: [NBER working paper](https://www.nber.org/papers/w17832)

- `Ahlfeldt, Szumilo, and Tripathy (2024)`, *Housing-consumption channel of mortgage demand*.
  Main use here: in UK data, house prices and mortgage demand reinforce each other; this matters for interpreting amplification rather than a one-way rate-to-price effect.
  Source: [Bank of England](https://www.bankofengland.co.uk/working-paper/2024/housing-consumption-channel-of-mortgage-demand)

- `Miller and Wanengkirtyo (2020)`, *Liquidity and monetary transmission: a quasi-experimental approach*.
  Main use here: mortgage-rate pass-through can vary with bank balance-sheet conditions, so effective-rate movements are not a perfect pure-policy shock.
  Source: [Bank of England](https://www.bankofengland.co.uk/working-paper/2020/liquidity-and-monetary-transmission-a-quasi-experimental-approach)

### `3` Supply elasticity and local heterogeneity

- `Saiz (2010)`, *The Geographic Determinants of Housing Supply*.
  Main use here: housing supply elasticity varies systematically with physical and regulatory constraints; this motivates heterogeneous local pass-through rather than a spatially uniform effect.
  Source: [Oxford Academic](https://doi.org/10.1162/qjec.2010.125.3.1253)

- `Hilber and Vermeulen (2016)`, *The Impact of Supply Constraints on House Prices in England*.
  Main use here: for England specifically, house prices respond more strongly to demand shocks where supply constraints are tighter.
  Source: [Oxford Academic](https://doi.org/10.1111/ecoj.12213)

- `Albuquerque, Iseringhausen, and Opitz (2024)`, *The Housing Supply Channel of Monetary Policy*.
  Main use here: regional responses to monetary shocks are larger in supply-inelastic places, including stronger house-price and consumption responses.
  Source: [IMF](https://www.imf.org/en/publications/wp/issues/2024/02/02/the-housing-supply-channel-of-monetary-policy-544046)

### `4` UK-specific monetary transmission and mortgage contract structure

- `Albuquerque, Lazarowicz, and Lenney (2025)`, *Monetary transmission through the housing sector*.
  Main use here: in UK data, higher rates push house prices down strongly but gradually; rents adjust differently; mortgagors bear a large share of the housing transmission channel.
  Source: [Bank of England](https://www.bankofengland.co.uk/working-paper/2025/monetary-transmission-through-the-housing-sector)

- `Rajan, Rodriguez-Tous, and Salgado-Moreno (2025)`, *Monetary policy and mortgage fixation lengths*.
  Main use here: UK mortgage fixation structure matters for pass-through timing and can shift with policy conditions; this is directly relevant for distributed-lag design.
  Source: [Bank of England](https://www.bankofengland.co.uk/working-paper/2025/monetary-policy-and-mortgage-fixation-lengths)

- `Foulis, Hazell, Mian, and Tracey (2026)`, *How do interest rates affect consumption? Household debt and the role of asset prices*.
  Main use here: UK evidence that asset prices and borrowing, not just lower debt service, are central to transmission; strengthens the case for focusing on local house-price heterogeneity.
  Source: [Bank of England](https://www.bankofengland.co.uk/working-paper/2026/how-do-interest-rates-affect-consumption-household-debt-and-the-role-of-asset-prices)

- `Ahearne et al. (2005)`, *House Prices and Monetary Policy: A Cross-Country Study*.
  Main use here: a broad macro backdrop linking house-price booms to easier monetary conditions, without implying central banks directly target house prices.
  Source: [Federal Reserve Board](https://www.federalreserve.gov/pubs/ifdp/2005/841/default.htm)

### What the literature implies for this project

The literature supports the study question, but it also sets guardrails:

- do not model mortgage-rate changes as if they are automatically exogenous
- do not ignore local supply heterogeneity
- do not ignore UK mortgage fixation structure and slow repricing
- do not treat price response as the only margin; transaction quantities matter too

## Available Data In This Repo

The plan below is restricted first to data already documented in `/Users/dzianissokalau/Documents/projects/re_trends/data_resources_research/`.

### Primary datasets

| Dataset | Role in study | Geography | Time | Key strengths | Main caveats |
| --- | --- | --- | --- | --- | --- |
| `source_land_registry_price_paid` | Main sale-price outcome | transaction -> postcode -> `LAD` / `MSOA` | historical from 1995 | completed transactions, broad history | registration lag, no canonical property id |
| `dim_postcode_geography` | Geography bridge | postcode -> `MSOA`, `LAD` | latest NSPL snapshot | canonical postcode join spine | latest snapshot only, not full geography history |
| `fact_lad_supply_year` | Supply-flow constraint proxy | `LAD` | `2001-02` to `2024-25` | official realized supply flows | annual, England only, financial-year timing |
| `fact_lad_housing_stock_year` | Stock/vacancy tightness proxy | `LAD` | stock `2001-2024`, vacancy `2004-2025` | total stock and vacancy rates | annual, England only, stock/vacancy dates differ |
| `mortgage_rates_monthly_effective` | Borrower-cost series | national | `1999-01` to `2026-02` verified snapshot | actual rates paid, new business vs stock split | methodology breaks in `2004`, `2011`, `2016`, `2018-06` |
| `mortgage_rates_monthly_quoted` | Product-rate series and robustness | national | `1995-01` to `2026-03` verified snapshot | stable product labels by fixation/LTV | quoted not paid, methodology breaks around `2011` and `2019` |
| `inflation_monthly_core` | Real-price deflator | national | long history, latest verified `2026-02` | clean CPIH/CPI/RPI index series | use index series only, not annual rates |

### Strong secondary datasets

| Dataset | Use | Why secondary |
| --- | --- | --- |
| `fact_area_labour_month` | local monthly demand/labour stress control at local-authority level | strong control series, but not the core mechanism |
| `fact_area_income_year` | affordability and demand-side heterogeneity | sparse release years and geography-vintage changes |
| `fact_area_demographics_year` | structural control or heterogeneity splits | LSOA and geography-vintage complications |
| `fact_area_deprivation` | long-run structural heterogeneity | release-based, not annual |
| `inflation_monthly_housing_components` | optional interpretation via rent/OOH inflation | not needed for baseline identification |

### Data not currently present in the repo, but useful if later added

- exogenous MPC or OIS surprise series
- direct local mortgage originations/LTV composition
- planning refusal/approval data
- physical land-scarcity or topographic constraint measures
- harmonised historical postcode geography snapshots

These are not required for the baseline differential-pass-through study, but they matter if the goal becomes a stronger causal claim.

## Data-Construction Blueprint

Build the data in layers and do not jump straight to the regression.

### Layer `A`: Transaction-to-area panel

Start from `source_land_registry_price_paid`.

For each transaction:

1. Normalize postcode.
2. Join to `dim_postcode_geography` on `postcode_compact`.
3. Assign both `lad_code` and `middle_area_code` (`MSOA`).
4. Keep England-only rows for the main sample because the supply datasets are England-only.

Before trusting the joined panel, audit postcode join success by transaction year. `dim_postcode_geography` is the latest NSPL snapshot rather than a full postcode history table, so some older postcodes may fail to join because they disappeared from later releases. If join coverage drops materially in earlier years, either:

- restrict the main sample to the period with stable join coverage, or
- reconstruct a historical postcode bridge before making long-run claims

Create quarterly area panels:

- `LAD-quarter` primary
- `MSOA-quarter` secondary

For each area-quarter compute:

- transaction count
- median sold price
- mean log sold price
- property-type shares
- estate-type shares
- new-build share

Preferred outcome variants:

1. raw nominal median price
2. raw real median price using `CPIH all-items index` `L522`
3. composition-adjusted price measure from a simple hedonic regression using:
   - `property_type`
   - `estate_type`
   - `new_build`

If quarterly `MSOA` counts are thin, collapse to semiannual or annual for `MSOA` only. Do not sacrifice the `LAD` baseline to preserve `MSOA`.

### Layer `B`: Mortgage shock series

Construct multiple national mortgage series because no single series is ideal.

#### Preferred shock families

1. `Effective new business headline`
   - pre-2016 legacy headline: `BJ95`
   - post-2016 current headline: `Z6JM`
   - interpretation: actual rates paid on newly originated mortgages

2. `Quoted fixed-rate products`
   - `BV34`: 2-year 75% LTV fixed, owner-occupied
   - `BV42`: 5-year 75% LTV fixed, owner-occupied
   - interpretation: clean product pricing with long history

3. `Quoted-effective spread`
   - chosen quoted rate minus matched effective new-business rate
   - interpretation: tightening/friction/selection proxy rather than pure user cost

#### Recommended shock definitions

Build all of the following:

- monthly level
- monthly change
- quarterly average
- quarterly change
- cumulative change over 4 quarters

#### Sample recommendation

Use two windows:

1. `Primary clean window`: `2016Q1` onward.
   Reason: current effective-rate family starts in `2016-01`, giving cleaner product definitions for the modern UK fixed-rate era.

2. `Longer historical window`: earliest feasible quarter after `2001Q2`.
   Reason: aligns with annual supply data availability.
   Guardrail: include methodology-period dummies and treat pre/post break comparisons cautiously.

Do not interpret level shifts across the effective-rate methodology breakpoints (`2004`, `2011`, `2016`, `2018-06`) as pure market movements.

### Layer `C`: Supply and stock tightness proxies

Build annual `LAD` measures first, then assign them to quarters.

From `fact_lad_supply_year`:

- `net_additional_dwellings / lag dwelling_stock_total`
- `housing_completions / lag dwelling_stock_total`
- optionally `demolitions / lag stock`

From `fact_lad_housing_stock_year`:

- `vacancy_rate`
- `long_term_vacancy_rate`
- `dwelling_stock_total`

#### Timing alignment rules

These must be explicit:

- `fact_lad_supply_year` is a financial-year dataset.
  Example: `2001-02` covers `2001-04-01` to `2002-03-31`.
- `fact_lad_housing_stock_year.year` is a calendar year with stock reference date `YYYY-03-31`.
- vacancy snapshots are not always `31 March`; preserve the exact source timing where possible.

#### Preferred constraint constructions

Build both static and time-varying versions.

Static, predetermined measures:

- pre-period mean supply rate
- pre-period mean completion rate
- pre-period mean vacancy rate
- pre-period mean long-term vacancy rate

Time-varying measures:

- annual supply rate carried to matching quarters
- annual vacancy rate carried forward until next release

Preferred baseline:

- use predetermined pre-period measures for the main interaction design
- use time-varying measures as robustness

Reason: this reduces simultaneity between current prices and current supply outcomes.

### Layer `D`: Local controls

Keep controls simple in the baseline.

Recommended control blocks:

- area fixed effects
- quarter fixed effects
- local-authority claimant rate or claimant-rate change from `fact_area_labour_month`
- optional area-specific linear trends

Use `fact_area_income_year` only for periodic heterogeneity splits or coarse demand controls, not as a high-frequency panel regressor.

## Primary Empirical Strategy

### `1` Descriptive stage

Before any causal language, produce:

- national chart of mortgage series since 1999
- national chart of real house-price growth
- maps of supply rate and vacancy rate by `LAD`
- binned scatter of cumulative real price growth versus supply/vacancy proxies
- episode charts for `2008-09`, `2020-21`, and `2022-24`

The descriptive stage should answer:

- do tight and slack markets already look different in unconditional data?
- do price and transaction-volume responses diverge around major rate moves?
- do the different mortgage series tell the same story?

### `2` Baseline differential-pass-through model

Use a local-projection-style interacted panel.

For horizon `h`:

`y_{i,t+h} - y_{i,t-1} = alpha_{i,h} + tau_{t,h} + beta_h (Shock_t x Constraint_i) + gamma_h Controls_{i,t-1} + e_{i,t+h}`

Where:

- `y` is log real house price
- `Shock_t` is the national mortgage-rate change
- `Constraint_i` is a standardized predetermined supply-tightness proxy
- `alpha_{i,h}` are area fixed effects
- `tau_{t,h}` are time fixed effects

Interpretation:

- `beta_h < 0` for a mortgage-rate increase means tighter markets suffer larger price declines
- `beta_h > 0` for a mortgage-rate cut means tighter markets enjoy larger price increases

Because `Shock_t` is national, the time fixed effect absorbs the average national price response. The identified object is the *differential local response* by constraint intensity.

Inference rule:

- cluster at least by `LAD` in `LAD` models
- in `MSOA` models with inherited `LAD` constraints, cluster at least by `LAD`
- if feasible, compare with two-way clustering by area and quarter or with a time-series-robust alternative to make sure inference is not driven by the national shock structure

### `3` Panel alternatives

Estimate all of these:

1. distributed-lag FE panel
2. local projections
3. quartile interaction model
4. event-study around major tightening/easing episodes

Use the local-projection form as the headline figure because timing likely matters in the UK.

### `4` Quantity adjustment outcomes

Repeat the interacted design with:

- transaction counts
- log transaction counts
- new-build share in transactions

Interpretation rule:

- strong price response with weak quantity response suggests capitalisation
- weak price response with strong quantity response suggests quantity adjustment

### `5` Heterogeneity extensions

Estimate splits by:

- London versus rest of England
- top versus bottom supply-constraint quartile
- low versus high vacancy quartile
- property type where transaction counts allow:
  - detached
  - semi-detached
  - terraced
  - flat/maisonette

Do not start with too many splits. First establish whether the baseline interaction exists.

## Recommended Robustness Sequence

Run robustness in this order:

1. `Real versus nominal prices`
   Use `L522` CPIH index as default deflator.
   Use `D7BT` CPI index as robustness.

2. `Alternative mortgage series`
   Compare quoted fixed rates, effective new-business rates, and quoted-effective spreads.

3. `Alternative constraint measures`
   Compare supply rate, completions rate, vacancy rate, long-term vacancy rate.

4. `Alternative geography`
   `LAD` headline, `MSOA` robustness with `LAD` constraints inherited.

5. `Alternative sample windows`
   - full post-2001 sample
   - post-2010
   - post-2016 clean modern-mortgage sample
   - `2020-2025` episode-specific sample

6. `Alternative weighting`
   - unweighted
   - weighted by transaction count

7. `Composition handling`
   - raw median
   - hedonic-adjusted
   - property-type-specific panels

8. `Control sensitivity`
   - no local controls
   - claimant-rate controls
   - area trends

## Falsification And Sanity Checks

The next agent should explicitly run these checks:

1. Future-shock placebo:
   future mortgage shocks should not predict current price changes after controls.

2. Pre-trend test in event studies:
   tight and slack markets should not diverge mechanically before the shock episode unless already on different trends.

3. Non-housing placebo outcome if available:
   the interaction should not explain unrelated series mechanically.

4. Shock-definition concordance:
   if quoted and effective shocks tell opposite stories, stop and diagnose before interpreting coefficients.

5. Geography stability:
   ensure `LAD` code changes are harmonized and England-only restriction is enforced.

## Decision Tree

This is the most important section for a future AI agent.

### Step `1`: Can a stable area-quarter panel be built?

- If `LAD-quarter` transaction counts are adequate:
  proceed with `LAD` as the headline design.
- If many `LAD-quarter` cells are sparse:
  move to semiannual or annual frequency for the headline design.
- If `MSOA-quarter` is sparse:
  keep it only as a robustness layer or drop it.

### Step `2`: Are mortgage shock measures coherent?

- If quoted fixed rates and effective new-business rates are highly correlated and give the same sign:
  proceed with one headline series and one robustness series.
- If they diverge materially:
  separate the analysis into:
  - user-cost level channel
  - tightening/friction channel via quoted-effective spread
- If level shifts appear around documented methodology breaks:
  shorten the sample or use break dummies and avoid pooled interpretation across regimes.

### Step `3`: Are supply proxies coherent?

- If low supply rate and low vacancy identify similar places:
  build a simple standardized tightness index as a secondary summary measure.
- If supply-flow and vacancy proxies disagree:
  treat them as separate mechanisms:
  - construction-flow constraint
  - stock-buffer constraint
- If results only appear for one proxy:
  interpret the mechanism narrowly and do not generalize to all supply constraints.

### Step `4`: Does the baseline interaction appear in prices?

- If tighter areas show larger price responses with stable sign across specifications:
  this supports the main hypothesis.
- If the interaction is weak in prices but strong in transaction volumes:
  conclude that adjustment is happening mainly on the quantity margin.
- If no interaction appears in either prices or quantities:
  conclude that current constraint proxies are too noisy or mortgage shocks are too common/national to create measurable spatial heterogeneity in this design.
- If the sign reverses:
  test whether lock-in, local recession exposure, or composition changes dominate.

### Step `5`: Is the result episode-specific?

- If the effect is concentrated in `2022-24`:
  frame the result as a fixed-rate-reset / recent-tightening era finding, not a stable long-run elasticity.
- If the effect is present in both pre- and post-2016 windows:
  treat it as a more general feature of UK housing transmission.
- If only the clean post-2016 sample behaves well:
  prefer that shorter sample for headline claims.

### Step `6`: Does the spread matter more than the rate level?

- If quoted-effective spread interactions dominate:
  emphasize credit frictions, lender selection, or pass-through impairment.
- If mortgage-rate level interactions dominate:
  emphasize user-cost capitalisation under supply constraints.
- If both matter:
  present a two-channel interpretation instead of forcing a single mechanism.

### Step `7`: How strong is the claim?

- If the study uses only observed mortgage rates:
  describe the result as differential pass-through or differential association, not a fully identified causal effect of monetary policy.
- If an external exogenous shock series is added later and results survive:
  upgrade the claim toward causal heterogeneous monetary transmission.

## Minimum Deliverables For The Actual Research Run

The next agent should produce at least:

1. a data appendix describing sample construction and timing alignment
2. one main table for baseline interacted-panel estimates
3. one local-projection figure by supply-tightness quartile
4. one map of constraint proxies
5. one event-study figure for a major tightening episode
6. one robustness table comparing mortgage shock definitions
7. one interpretation section that distinguishes:
   - user-cost channel
   - stock-buffer channel
   - credit-friction channel

## Guardrails And Common Failure Modes

- Do not call this a UK-wide study unless the sample restriction is clearly England-only for the main analysis.
- Do not use annual inflation-rate series to deflate prices. Use index series.
- Do not mix nominal PPD outcomes with real interpretation.
- Do not treat `MSOA` results as independently identified if the key constraints are only `LAD` level.
- Do not treat quoted rates and effective rates as interchangeable.
- Do not ignore documented methodology breaks in the BoE mortgage series.
- Do not over-control with noisy annual variables and erase the signal.
- Do not claim repeat-sale evidence without first solving property identity.

## Practical Build Order

The fastest credible path is:

1. Build `LAD-quarter` real price and transaction panels from PPD plus postcode geography.
2. Build mortgage shock panel with quoted and effective variants.
3. Build predetermined `LAD` supply and vacancy proxies.
4. Run descriptive charts and baseline local projections.
5. Add claimant-rate controls and robustness.
6. Add `MSOA` and other transaction-side extensions only if the baseline is promising.

## Bottom Line

This project is worth doing with current repo data.

The cleanest claim available from current in-repo data is:

> national mortgage-rate movements are associated with different local house-price responses depending on local supply and stock tightness

The cleanest headline design is:

- England only
- `LAD-quarter`
- post-2016 primary window, post-2001 robustness window
- real sale prices from PPD
- national mortgage shocks from effective new-business and quoted fixed-rate series
- local supply tightness from annual supply-flow and vacancy proxies

If that design works, the project has a strong path to a publishable empirical note and a strong platform for later upgrades with external policy-shock data.
