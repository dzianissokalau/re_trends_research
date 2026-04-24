# Mortgage-Rate Pass-Through Under Supply Constraints In England

> Disclaimer: This document was generated with AI and has received only limited human review. It may contain errors or omissions and should be independently verified before use.

## 1. Title

Mortgage-Rate Pass-Through Under Supply Constraints In England

Working short title:

`Mortgage-rate pass-through under supply constraints`

This is an AI-first quantitative research plan for estimating whether national mortgage-rate shocks transmit differently to local house prices and transaction activity depending on local housing supply and stock tightness.

## 2. Decision Use Case

This project should not be treated as a general housing-market commentary exercise. It is intended to create a decision-grade local transmission tool.

| Field | Plan |
| --- | --- |
| Decision makers | Local authorities, housing policy teams, lenders, property-risk analysts, central-bank or macroprudential analysts, and housing-market researchers |
| Decision type | Price-risk monitoring, stress targeting, policy evaluation, market turning-point monitoring, and local affordability risk assessment |
| Decision horizon | 4 to 12 quarters after a mortgage-rate shock, with a shorter 1 to 4 quarter monitoring view |
| Decision output | Local elasticity estimates, local stress ranking, scenario table, and repeatable monitoring score |
| Main action | Identify which local authorities are most exposed to national mortgage-rate changes because local supply and stock buffers are weak |
| Cost of false positives | Overstating stress in constrained but resilient areas, misdirecting policy attention, or pricing local risk too pessimistically |
| Cost of false negatives | Missing areas where a national rate shock is likely to capitalise strongly into prices, affordability pressure, or transaction contraction |

Decision question:

> Given a national mortgage-rate move, which English local authorities should be expected to experience the largest differential house-price and transaction-volume response because local supply and stock adjustment are weakest?

## 3. Main Research Question

Primary causal-style question:

> What is the differential effect of national mortgage-rate shocks on real completed-sale prices across English local authorities, through local housing supply and stock-tightness constraints, over 1 to 12 quarters?

Primary monitoring question:

> Can we build a repeatable local authority score that identifies places where national mortgage-rate moves are most likely to transmit into local price pressure and transaction weakness?

Population and geography:

- main sample: England only
- main unit: `LAD-quarter`
- secondary unit: `MSOA-quarter`, using `LAD` constraint proxies only as a robustness layer

Outcome variables:

- log real completed-sale price
- real median completed-sale price
- transaction count
- log transaction count
- new-build share in transactions

Comparison group:

- high-supply-tightness local authorities versus low-supply-tightness local authorities
- high-stock-tightness local authorities versus low-stock-tightness local authorities

Core estimand:

- differential local response to a national mortgage-rate shock by standardized supply or stock-tightness exposure

## 4. Why This Matters Now

Mortgage transmission in the UK has become harder to interpret because national rates changed sharply after 2021 while mortgage fixation, refinancing lags, affordability constraints, and local supply bottlenecks varied across places.

The project matters now because:

- national mortgage-rate shocks are large enough to create observable local divergence
- local affordability debates need a way to separate national financing pressure from local supply exposure
- fixed-rate mortgage prevalence makes timing and lag structure more important than simple same-quarter correlations
- realized supply and vacancy data are now available in the warehouse at enough historical depth for local authority analysis
- a repeatable local monitoring score could help identify areas where future rate scenarios are likely to matter most

## 5. Literature Frontier

The literature should be used to locate the frontier, not to pad the report. The core frontier is the intersection of user cost, mortgage-credit transmission, housing supply elasticity, and UK mortgage-contract structure.

### What is already known

- `Poterba (1984)`, *Tax Subsidies to Owner-Occupied Housing: An Asset-Market Approach*.
  Financing conditions and inflation affect the user cost of owner-occupation and can capitalise into house values.
  Source: [NBER working paper page with published-version reference](https://www.nber.org/papers/w0553)

- `Mishkin (2007)`, *Housing and the Monetary Transmission Mechanism*.
  Housing is a key monetary-transmission channel, but the pathway runs through prices, collateral, expectations, and supply response.
  Source: [NBER](https://www.nber.org/papers/w13518)

- `Saiz (2010)`, *The Geographic Determinants of Housing Supply*.
  Housing supply elasticity varies systematically with physical and regulatory constraints, supporting heterogeneous local pass-through.
  Source: [Oxford Academic](https://doi.org/10.1162/qjec.2010.125.3.1253)

- `Hilber and Vermeulen (2016)`, *The Impact of Supply Constraints on House Prices in England*.
  English house prices respond more strongly to demand shocks where local supply constraints are tighter.
  Source: [Oxford Academic](https://doi.org/10.1111/ecoj.12213)

- `Ahearne et al. (2005)`, *House Prices and Monetary Policy: A Cross-Country Study*.
  Easier monetary conditions are associated with house-price booms across countries, but the mechanism should not be reduced to a direct policy-rate-to-price mapping.
  Source: [Federal Reserve Board](https://www.federalreserve.gov/pubs/ifdp/2005/841/default.htm)

### What is still uncertain

- how much UK mortgage-rate pass-through varies locally once common national shocks are absorbed by time effects
- whether realized supply flow, vacancy, or long-term vacancy is the more useful local constraint signal
- whether the 2022 to 2024 tightening episode is a special fixed-rate-reset episode or an example of a stable long-run transmission pattern
- whether differential price responses dominate transaction-volume responses in constrained areas
- whether quoted-effective spreads capture a different mechanism from mortgage-rate levels

### What prior work fails to operationalize

Prior work often shows that supply matters for house prices or that mortgage transmission matters nationally, but it is less often converted into a repeatable local monitoring artifact. This project should operationalize the mechanism as local authority elasticities, risk scores, and scenario tables that can be updated with warehouse data.

### Where the warehouse data creates an advantage

The current warehouse makes the study feasible because it combines:

- transaction-level completed-sale prices
- a canonical postcode-to-area bridge
- annual local authority supply and stock facts
- national effective and quoted mortgage-rate series
- inflation deflators
- local monthly labour-market controls

### What would be genuinely new

The novelty is not the idea that rates affect house prices. The novelty is a repeatable English local authority framework that estimates and monitors heterogeneous mortgage-rate transmission using realized local supply and stock-tightness proxies already available in the warehouse.

## 6. Novelty Claim

Novelty score:

| Dimension | Score | Rationale |
| --- | ---: | --- |
| Question | 4/5 | Turns a broad mortgage-rate question into local differential pass-through under supply constraints |
| Data | 4/5 | Combines transaction prices, mortgage-rate families, supply flows, stock, vacancies, and labour controls |
| Method | 3/5 | Uses standard local projections and panel methods, but applies them to a local transmission-monitoring artifact |
| Granularity or frequency | 4/5 | Builds `LAD-quarter` and optional `MSOA-quarter` panels instead of relying on national or annual summaries |
| Decision usefulness | 4/5 | Produces local elasticities, rankings, and scenario outputs that can support policy or risk monitoring |

Specific novelty claim:

> This project converts the mortgage-rate and supply-constraint literature into a repeatable local authority pass-through monitor, estimating where national financing shocks are likely to capitalise most strongly into English local house prices and transaction activity because local supply and stock buffers are weak.

Prioritization score:

| Criterion | Max | Score | Reason |
| --- | ---: | ---: | --- |
| Decision impact | 20 | 16 | Helps policy and risk teams identify locally exposed housing markets |
| Novelty | 15 | 12 | Novel local monitoring artifact, standard econometric toolkit |
| Data advantage | 15 | 13 | Strong warehouse linkage across transactions, rates, supply, stock, and controls |
| Feasibility | 15 | 12 | Feasible at `LAD`; `MSOA` depends on sparsity and inherited proxies |
| Forecast or identification credibility | 15 | 10 | Good differential design, but observed rates are not exogenous policy surprises |
| Actionability | 10 | 8 | Can produce rankings, scenarios, and monitoring score |
| Timeliness | 5 | 5 | Recent rate cycle makes the question live |
| Reusability as monitoring system | 5 | 4 | Repeatable with scheduled warehouse updates, but transaction lag limits nowcasting |
| Total | 100 | 80 | Proceed if data gates pass; strengthen later with external shock data |

## 7. Available Warehouse Data

Use only the datasets below unless a later section explicitly asks to acquire external data. Do not add other property portals or private source families to this plan.

### Core outcome data

| Table or source | Role | Geography | Time coverage | Grain | Join keys | Quality issues |
| --- | --- | --- | --- | --- | --- | --- |
| `source_land_registry_price_paid` | completed-sale price and transaction outcomes | transaction postcode joined to `LAD` / `MSOA` | historical from 1995 | one row per transaction | normalized postcode -> `dim_postcode_geography.postcode_compact` | registration lag, no canonical physical-property id, no coordinates |

### Geography spine

| Table or source | Role | Geography | Time coverage | Grain | Join keys | Quality issues |
| --- | --- | --- | --- | --- | --- | --- |
| `dim_postcode_geography` | postcode-to-area bridge | postcode to `OA`, `LSOA`, `MSOA`, `LAD`, region | latest NSPL snapshot | one row per normalized full postcode | `postcode_compact` | latest snapshot only, not a full point-in-time postcode geography history |

### Shock variables

| Table or source | Role | Geography | Time coverage | Grain | Join keys | Quality issues |
| --- | --- | --- | --- | --- | --- | --- |
| `mortgage_rates_monthly_effective` | actual mortgage rates paid | national | verified `1999-01` to `2026-02` | month + series code | month | methodology breaks in `2004`, `2011`, `2016`, and `2018-06`; distinguish new business from outstanding stock |
| `mortgage_rates_monthly_quoted` | product-rate robustness and spread construction | national | verified `1995-01` to `2026-03` | month + series code | month | quoted, not paid; methodology periods around `2011` and `2019` |
| `inflation_monthly_core` | real-price deflator | national | long history, verified latest month `2026-02` | month + ONS series code | month | use index series only, not annual-rate series |

### Structural covariates

| Table or source | Role | Geography | Time coverage | Grain | Join keys | Quality issues |
| --- | --- | --- | --- | --- | --- | --- |
| `fact_lad_supply_year` | realized supply-flow constraint proxy | England `LAD` | `2001-02` to `2024-25` | `LAD` + financial year | `lad_code`, financial-year label | annual, England only, financial-year timing, component fields mostly from `2012-13` onward |
| `fact_lad_housing_stock_year` | stock and vacancy tightness proxy | England `LAD` | stock `2001-2024`; vacancy `2004-2025` | `LAD` + calendar year | `lad_code`, year | annual, England only, stock and vacancy reference dates differ |
| `fact_area_income_year` | affordability and demand heterogeneity | England and Wales `MSOA` | `2012`, `2014`, `2016`, `2018`, `2020`, `2023` | `MSOA` + year + measure | `area_code`, year | sparse years, geography-vintage changes |
| `fact_area_demographics_year` | structural local controls or subgroup checks | England and Wales `LSOA` | supported years `2001-2024` depending on source family | `LSOA` + requested year | `area_code`, requested year | geography-vintage changes, many annual-estimate fields limited to age/population |
| `fact_area_deprivation` | slow-moving structural deprivation | UK small areas | release-based `2001-2025` | area + release year | `area_code`, release year | not an annual panel, cross-nation score comparability limits |

### Leading indicators and controls

| Table or source | Role | Geography | Time coverage | Grain | Join keys | Quality issues |
| --- | --- | --- | --- | --- | --- | --- |
| `fact_area_labour_month` | local labour-market stress control | UK local authorities | verified `1986-01` to `2026-02` | local authority + month | area code, month | local-authority boundary consistency should be checked |
| `inflation_monthly_housing_components` | optional macro-housing interpretation | national | verified to `2026-02` | period + series code | period start date | mixes monthly observations and yearly weights; not needed for baseline identification |

### Prediction-time availability

For monitoring or scenario use, the agent must distinguish what would have been available at the time:

- mortgage-rate data are monthly and generally available quickly after release
- transaction data are delayed because completed sales and registration lag the market
- supply and stock data are annual and published with lag
- local labour data are monthly but may be revised
- income, demographics, and deprivation are sparse or release-based and should be treated as structural rather than high-frequency signals

### Data readiness notes

| Dataset family | Update frequency | Publication lag | Missingness focus | Revision risk | Available at decision time? |
| --- | --- | --- | --- | --- | --- |
| completed sales | incremental source updates | material registration lag | postcode join failures, sparse area-quarter cells | corrections can arrive in later monthly updates | partly, but lagged |
| postcode geography | incremental NSPL refresh | depends on NSPL release | terminated or removed historical postcodes | latest snapshot can change joins | yes for current joins, weak for historical point-in-time joins |
| mortgage rates | monthly | short official release lag | series-specific start dates | methodology breaks and source revisions | yes |
| supply flow | annual financial year | annual release lag | pre-`2012-13` component nulls | official revisions possible | yes, but lagged and structural |
| stock and vacancy | annual | annual release lag | vacancy-only and stock-only years | official revisions possible | yes, but lagged and structural |
| labour controls | monthly | short official release lag | early-period rate nulls or boundary issues | monthly revisions expected | yes |
| inflation | monthly | short official release lag | series coverage differs | revisions possible | yes |

## 8. Public Data To Acquire

The baseline research can run with current warehouse data. External data should be added only if the goal is to strengthen causal identification or build a deployable decision monitor.

Priority external acquisitions:

| Candidate data | Why acquire | Required for baseline? | Decision if unavailable |
| --- | --- | --- | --- |
| MPC surprise or OIS surprise series | improves exogenous-shock interpretation | no | keep claims as differential association/pass-through, not causal monetary-policy effects |
| Planning applications, approvals, and refusal rates | distinguishes regulatory constraint from realized supply flow | no | treat supply-flow proxies as realized adjustment, not pure regulation |
| physical land-scarcity measures | separates physical scarcity from policy scarcity | no | avoid comparing directly to Saiz-style physical-elasticity claims |
| historical postcode geography snapshots or crosswalks | improves old-transaction geography joins | no, but important for long sample | restrict long-run sample if join coverage is poor |
| local mortgage origination or LTV composition | tests credit exposure heterogeneity | no | use mortgage-rate series as national shocks only |

## 9. Economic Mechanism

Mechanism map:

| Channel | Expected path | Expected sign after rate increase | Data needed | Confounders or risks |
| --- | --- | --- | --- | --- |
| User-cost capitalisation | mortgage rates -> user cost -> willingness to pay -> completed-sale prices | negative price response, larger in constrained areas | mortgage-rate shocks, real prices, supply constraints | national expectations, income shocks, composition change |
| Quantity adjustment | mortgage rates -> affordability -> buyer demand -> transaction counts | negative transaction response, possibly larger where demand is rate-sensitive | transaction counts, mortgage shocks, controls | registration lag, seasonal effects |
| Supply-flow constraint | low supply additions -> limited quantity adjustment -> stronger price capitalisation | stronger price response per rate shock | `fact_lad_supply_year`, stock denominator | supply responds to past prices, annual timing |
| Stock-buffer constraint | low vacancy -> limited available stock buffer -> stronger price capitalisation | stronger price response per rate shock | vacancy and long-term vacancy rates | vacancy definition changes and annual reference timing |
| Credit-friction channel | quoted-effective spread -> lender/borrower selection pressure -> local price and volume response | ambiguous; likely negative for prices and volumes | quoted and effective rates | spread may reflect composition, not pure credit supply |
| Fixed-rate lag | mortgage fixation -> delayed pass-through -> distributed response over quarters | delayed and persistent response | fixation-specific mortgage series | changing borrower composition and refinancing timing |

Alternative explanations to test:

- local labour-market weakness drives both prices and transactions
- constrained areas are more income-rich and more resilient, dampening price falls
- compositional shifts in property types mimic price responses
- national shocks coincide with macro episodes that affect high-price areas differently
- local supply proxies are endogenous to prior price growth

## 10. Hypotheses

`H1` Baseline heterogeneity:

For a given national mortgage-rate increase, real completed-sale prices fall more, or rise less, in supply-constrained local authorities than in less constrained local authorities.

`H2` Quantity-versus-price adjustment:

Where supply is more elastic, mortgage-rate shocks should show up relatively more in transaction volumes and relatively less in prices.

`H3` Stock tightness:

Low vacancy and low long-term vacancy should strengthen price pass-through because the local stock buffer is smaller.

`H4` Credit-friction channel:

If quoted-effective mortgage spreads explain more local heterogeneity than rate levels, interpret the result as credit friction or borrower selection rather than pure user-cost capitalisation.

`H5` Contract-structure timing:

Pass-through should be slower and more episode-dependent in the modern UK fixed-rate era, especially after 2016.

## 11. Methodology

### Data construction

Build the data in layers.

`Layer A`: transaction-to-area panel

1. Normalize transaction postcodes from `source_land_registry_price_paid`.
2. Join to `dim_postcode_geography` on `postcode_compact`.
3. Assign `lad_code` and `middle_area_code`.
4. Keep England-only rows for the main sample.
5. Audit postcode join success by transaction year before modeling.

Important geography guardrail:

`dim_postcode_geography` is the latest NSPL snapshot, not a full point-in-time geography table. If old transaction join coverage is weak, either restrict the long-run sample or acquire a historical postcode bridge before making long-run claims.

Create quarterly panels:

- primary: `LAD-quarter`
- secondary: `MSOA-quarter`, only as robustness with inherited `LAD` constraint proxies

For each area-quarter compute:

- transaction count
- median sold price
- mean log sold price
- property-type shares
- estate-type shares
- new-build share

Outcome variants:

- nominal median price
- real median price using CPIH all-items index `L522`
- composition-adjusted price measure from hedonic controls for `property_type`, `estate_type`, and `new_build`

`Layer B`: mortgage shock series

Construct multiple national mortgage-rate shocks:

- effective new-business headline:
  - legacy headline `BJ95`
  - current headline `Z6JM`
- quoted fixed-rate products:
  - `BV34`, 2-year 75% LTV fixed owner-occupied
  - `BV42`, 5-year 75% LTV fixed owner-occupied
- quoted-effective spread:
  - chosen quoted rate minus matched effective new-business rate

Build shock measures:

- monthly level
- monthly change
- quarterly average
- quarterly change
- cumulative four-quarter change

Sample windows:

- primary clean window: `2016Q1` onward
- longer robustness window: earliest feasible quarter after `2001Q2`
- episode window: `2020Q1` to latest available quarter, with emphasis on `2022-2024`

Guardrail:

Do not interpret level shifts across documented mortgage-rate methodology breaks (`2004`, `2011`, `2016`, `2018-06`) as pure market movements.

`Layer C`: supply and stock tightness

From `fact_lad_supply_year`:

- `net_additional_dwellings / lag dwelling_stock_total`
- `housing_completions / lag dwelling_stock_total`
- optional `demolitions / lag dwelling_stock_total`

From `fact_lad_housing_stock_year`:

- `vacancy_rate`
- `long_term_vacancy_rate`
- `dwelling_stock_total`

Construct both:

- predetermined static measures based on pre-period averages
- time-varying measures carried to quarters as robustness

Preferred baseline:

- use predetermined pre-period constraint measures in the main interaction design to reduce simultaneity

`Layer D`: controls

Baseline controls:

- area fixed effects
- quarter fixed effects
- local-authority claimant rate or claimant-rate change

Robustness controls:

- area-specific linear trends
- selected affordability or demographic structural controls

Avoid over-controlling with sparse annual variables in the baseline.

### Baseline model

Use an interacted local-projection panel:

```text
y_{i,t+h} - y_{i,t-1}
  = alpha_{i,h}
  + tau_{t,h}
  + beta_h (Shock_t x Constraint_i)
  + gamma_h Controls_{i,t-1}
  + e_{i,t+h}
```

Where:

- `y` is log real completed-sale price or log transaction count
- `Shock_t` is a national mortgage-rate shock
- `Constraint_i` is a standardized predetermined supply or stock-tightness proxy
- `alpha_i` are area fixed effects
- `tau_t` are time fixed effects

Interpretation:

- for a mortgage-rate increase, `beta_h < 0` means tighter places have larger relative price declines
- for a mortgage-rate cut, `beta_h > 0` means tighter places have larger relative price increases
- because the shock is national, time fixed effects absorb the average national response; identification comes from differential local response by constraint exposure

Inference:

- cluster at least by `LAD` in `LAD` models
- cluster by `LAD` in `MSOA` models with inherited `LAD` constraints
- compare with two-way clustering by area and quarter if feasible

### Alternative models

Run these as checks:

- distributed-lag fixed-effects panel
- quartile interaction model
- event study for major tightening and easing episodes
- binned local projections by constraint quartile

## 12. Forecast, Causal, Monitoring, Or Scenario Design

This project has three design layers. Keep them separate in the execution and reporting.

### Causal-style estimation

Goal:

- estimate differential pass-through by local supply and stock tightness

Identification claim:

- with observed mortgage rates only, the claim is differential pass-through or differential association, not a fully causal monetary-policy effect
- if an exogenous surprise series is later acquired and results survive, the claim can be upgraded toward causal heterogeneous monetary transmission

Identifying assumption:

- conditional on area fixed effects, time fixed effects, and controls, high-constraint and low-constraint areas would not have had systematically different price responses to national mortgage-rate moves except through the constraint-related transmission channel

Challenge this assumption using pre-trends, placebo shocks, controls, and alternative samples.

### Monitoring design

Goal:

- create a repeatable `LAD` mortgage pass-through exposure score

Candidate score:

```text
pass_through_exposure_score_i
  = standardized predicted price response to a 100 bp mortgage-rate increase
```

Components:

- estimated `beta_h` from local projections
- local standardized supply-flow constraint
- local standardized vacancy or long-term-vacancy tightness
- uncertainty band or confidence category

Output horizon:

- 4 quarters
- 8 quarters
- 12 quarters

### Scenario design

Scenario outputs should translate coefficients into practical tables:

- impact of +100 bp mortgage-rate shock
- impact of -100 bp mortgage-rate shock
- impact under high-spread tightening scenario
- predicted effect by local authority constraint quartile

Scenario assumptions must separate:

- empirical estimates from the model
- imposed mortgage-rate paths
- constraints treated as fixed

## 13. Validation Strategy

### Data validation gates

Before modeling:

1. Confirm no forbidden external property source families are used.
2. Confirm England-only restriction for the main sample.
3. Compute postcode join rate by transaction year.
4. Compute area-quarter transaction counts and flag sparse cells.
5. Confirm deflator uses index series such as `L522`, not annual-rate series.
6. Confirm mortgage-rate methodology-period fields are preserved or explicitly handled.
7. Confirm supply and stock timing alignment is documented.

### Causal validation

Run:

- pre-trend tests in event studies
- future-shock placebo tests
- alternative mortgage-shock definitions
- alternative constraint definitions
- geography sensitivity: `LAD` versus `MSOA` robustness
- sample sensitivity: post-2016, post-2010, and post-2001 windows
- composition sensitivity: raw median, hedonic-adjusted, and property-type-specific panels
- spillover discussion for adjacent local authorities if maps show spatial clustering

### Monitoring validation

If producing a monitoring score:

- backtest score stability across historical episodes
- check whether high-score areas have larger subsequent differential responses than low-score areas
- measure false-positive and false-negative rates using episode windows
- compare the score to simple baselines:
  - high prior price growth
  - high price level
  - London indicator
  - low vacancy only
  - low supply rate only

### General research quality

Require:

- reproducible SQL or notebook code
- versioned source snapshots
- clear missing-data treatment
- documented transformations
- human review of surprising or too-clean results
- red-team critique before publication or operational use

## 14. Expected Outputs

Minimum research outputs:

1. data appendix describing sample construction, geography joins, and timing alignment
2. main estimates table for interacted local-projection models
3. local-projection figure by supply or stock-tightness quartile
4. map of supply and vacancy tightness by local authority
5. event-study figure for at least one major tightening episode
6. robustness table comparing mortgage-rate shock definitions
7. scenario table for +100 bp and -100 bp mortgage-rate changes
8. local authority pass-through exposure ranking with uncertainty labels
9. interpretation section separating user-cost, stock-buffer, and credit-friction channels

Preferred final artifacts:

- Markdown research report
- CSV of `LAD` exposure scores
- chart pack or notebook outputs
- reproducible query scripts

## 15. Actionability

The research is not complete until it can say what a decision maker might do differently.

So-what table:

| Finding | Confidence | Decision implication | Who should act | Timing | Risk |
| --- | --- | --- | --- | --- | --- |
| High-constraint areas show larger negative price response to rate increases | high if robust across shock definitions and samples | prioritize affordability and market-stress monitoring in these areas | local authorities, lenders, policy analysts | 4 to 12 quarters | may overstate causal interpretation without exogenous shock |
| Vacancy tightness predicts pass-through better than supply flow | medium if robust only in some windows | monitor stock-buffer metrics, not just construction flow | housing policy teams and risk analysts | annual refresh | vacancy definitions and timing may weaken inference |
| Spread measures dominate rate-level measures | medium | frame risk as credit-friction or borrower-selection pressure | lenders and macroprudential analysts | monthly to quarterly | spread may reflect composition rather than credit supply |
| Price effects are weak but transaction effects are strong | medium | use the tool as liquidity or turnover stress monitor rather than price monitor | local authorities and market analysts | 1 to 4 quarters | transaction registration lag can blur timing |
| No stable heterogeneity appears | high if all robustness fails | do not deploy local pass-through monitor from current proxies | research owner | immediate | avoids operationalizing a weak signal |

## 16. Risks And Limitations

Key risks:

- mortgage-rate changes are national and not automatically exogenous
- current postcode geography is not a full historical point-in-time geography bridge
- realized supply may respond to past price growth, making current supply-flow measures endogenous
- vacancy rates and stock estimates are annual and have timing differences
- transaction composition can shift during rate episodes
- registration lag can blur quarterly timing
- `MSOA` estimates inherit `LAD` supply proxies, weakening interpretation
- external validity may differ between `2008-09`, pandemic-era, and `2022-24` episodes

Interpretation limits:

- without exogenous monetary surprise data, describe estimates as differential pass-through rather than definitive causal monetary-policy effects
- do not call the main sample UK-wide because the supply and stock facts are England-only
- do not claim repeat-sale evidence unless property identity is solved and audited
- do not use sparse structural covariates as if they were high-frequency controls

## 17. Quality Gates

The next AI agent must pass these gates before producing final claims.

Data gates:

- postcode join rate is documented by year
- sparse area-quarter cells are handled using a pre-specified rule
- mortgage shock series are plotted and checked for methodology breaks
- deflator choice is documented and uses an index series
- supply and stock variables are lagged or predetermined in the baseline

Model gates:

- main result is compared to at least one simple baseline
- pre-trend and future-shock placebo checks are run
- result is robust to at least two mortgage-rate definitions or clearly explained when not
- inference uses appropriate clustering
- sensitivity to London and high-price areas is tested

Decision gates:

- final output includes local authority ranking or scenario table
- uncertainty labels are visible
- recommended use is tied to a specific decision maker
- kill criteria are applied before publication

## 18. Execution Plan

### Phase 0: Setup and audit

1. Confirm available BigQuery table names and latest loaded dates.
2. Confirm no forbidden external property source families are used.
3. Create a reproducible workspace folder for queries, outputs, and logs.

Exit condition:

- table availability and sample boundaries are documented.

### Phase 1: Build analysis panels

1. Build `LAD-quarter` completed-sale panel.
2. Audit postcode join success by transaction year.
3. Build real price outcomes using `L522`.
4. Build transaction-count outcomes.
5. Build `MSOA-quarter` panel only after `LAD` quality is acceptable.

Exit condition:

- panel row counts, missingness, and sparse-cell rates are documented.

### Phase 2: Build shock and constraint features

1. Build effective-rate shock measures.
2. Build quoted fixed-rate shock measures.
3. Build quoted-effective spread measures.
4. Build predetermined supply-flow and stock-tightness proxies.
5. Build local labour controls.

Exit condition:

- shock series and constraint variables pass visual and summary-stat checks.

### Phase 3: Descriptive analysis

1. Plot national mortgage series and real house-price series.
2. Map supply and vacancy tightness.
3. Compare high- and low-constraint areas around major episodes.

Exit condition:

- descriptive patterns are coherent enough to proceed or the plan is redesigned.

### Phase 4: Estimation and validation

1. Estimate baseline local projections.
2. Run distributed-lag and quartile-interaction alternatives.
3. Run validation and falsification checks.
4. Build robustness table.

Exit condition:

- results are either robust enough for scenario output or killed using the criteria below.

### Phase 5: Decision artifact

1. Build exposure score.
2. Build local authority ranking with uncertainty labels.
3. Build scenario table.
4. Write final report and data appendix.

Exit condition:

- a decision maker can identify where action or monitoring would change.

## 19. Success Criteria

The project succeeds if most of these are true:

- the main research question is answered with a clear decision use case
- the `LAD-quarter` panel has acceptable coverage and timing documentation
- the baseline result is directionally stable across core specifications
- at least one supply or stock-tightness proxy produces interpretable heterogeneous pass-through
- price and transaction-volume results are jointly interpreted
- uncertainty is visible in charts, rankings, or scenario tables
- output includes an actionable local authority ranking or scenario artifact
- the plan can be rerun after new mortgage-rate, transaction, supply, and stock updates

Minimum publishable result:

> A defensible estimate of how much more, or less, a high-constraint English local authority responds to a national mortgage-rate shock relative to a low-constraint authority, with validation checks and uncertainty labels.

## 20. Kill Criteria

Stop or redesign the project if any of these occur:

- postcode join quality is too weak to support the selected sample window
- `LAD-quarter` transaction counts are too sparse even after aggregation
- mortgage-rate shock definitions disagree so strongly that no coherent shock measure can be defended
- supply and stock proxies are too noisy or too endogenous to interpret
- pre-trends or future-shock placebos strongly reject the design
- results are driven entirely by London or a handful of high-price local authorities
- the model adds no decision value beyond simple baselines such as London indicator, prior price growth, or low vacancy alone
- no stable local authority ranking or scenario output can be produced
- the only possible output is a descriptive narrative with no decision artifact

## Decision Tree For The AI Research Agent

### Step 1: Can a stable `LAD-quarter` panel be built?

- If transaction counts are adequate, proceed with `LAD` as the headline design.
- If many cells are sparse, move to semiannual or annual frequency.
- If coverage depends heavily on current postcode geography, shorten the sample or acquire historical postcode geography.

### Step 2: Are mortgage shock measures coherent?

- If quoted and effective shocks agree, use one headline series and one robustness series.
- If they diverge, split the interpretation into user-cost and credit-friction channels.
- If methodology breaks dominate the series, shorten the sample or use break-aware specifications.

### Step 3: Are supply proxies coherent?

- If supply-flow and vacancy proxies identify similar places, build a standardized tightness index as a secondary measure.
- If they disagree, treat them as separate mechanisms.
- If only one proxy works, interpret the mechanism narrowly.

### Step 4: Does the baseline interaction appear?

- If price effects are robust, proceed to scenario and ranking outputs.
- If price effects are weak but transaction effects are robust, recast the artifact as a transaction-stress monitor.
- If neither price nor transaction effects are robust, kill or redesign.

### Step 5: How strong is the claim?

- If using only observed mortgage rates, use differential pass-through language.
- If exogenous surprise data are added and results survive, consider stronger causal language.

## Practical Build Order

The fastest credible path is:

1. Build `LAD-quarter` real price and transaction panels from completed-sale data plus postcode geography.
2. Build mortgage shock panel with quoted and effective variants.
3. Build predetermined `LAD` supply and vacancy proxies.
4. Run descriptive charts and baseline local projections.
5. Add claimant-rate controls and robustness.
6. Add `MSOA` and other transaction-side extensions only if the baseline is promising.

## Bottom Line

This project should proceed only if it produces more than an interesting historical report. The decision-grade target is a local authority pass-through monitor that estimates where national mortgage-rate movements are most likely to transmit into local house-price and transaction stress because local supply and stock buffers are weak.

The cleanest headline design is:

- England only
- `LAD-quarter`
- post-2016 primary window, post-2001 robustness window
- real completed-sale prices
- national mortgage shocks from effective new-business and quoted fixed-rate series
- local supply tightness from annual supply-flow and vacancy proxies

If the validation gates hold, the project can support a repeatable local stress-ranking and scenario tool. If they fail, the project should stop before becoming a polished but non-actionable narrative.
