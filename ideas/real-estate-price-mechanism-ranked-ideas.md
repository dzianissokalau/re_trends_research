# Real Estate Price Mechanism Ranked Research Ideas

## Purpose
- This file turns the current literature library and factor-to-dataset matrix into a ranked set of research ideas focused on UK residential sale prices.
- It is designed to answer a practical question: which quantitative studies are both interesting and realistically supportable with the current `re_trends` data stack and its companion dataset specs?
- The primary price target throughout is achieved sale price from `source_land_registry_price_paid`.
- The emphasis is on causal or quasi-causal research designs, strong descriptive decompositions, and theory-validation exercises rather than generic feature lists.

## Companion Files
- Conceptual literature spine: [real-estate-price-dynamics-research-library.md](../library/real-estate-price-dynamics-research-library.md)
- Factor-to-mechanism-to-data bridge: [real-estate-factor-mechanism-dataset-matrix.md](../library/real-estate-factor-mechanism-dataset-matrix.md)
- Structured rank table for filtering and sorting: [real-estate-price-mechanism-ranked-ideas.csv](./real-estate-price-mechanism-ranked-ideas.csv)

## Scope And Defaults
- The ideas are UK-first and England-heavy because that matches the strongest overlap between the literature and the currently available data specs.
- The strongest current designs are area-panel and macro-interaction studies built from transactions plus geography, supply, stock, crime, deprivation, demographics, labour, mortgage, and inflation tables.
- School and EPC studies are included because the relevant datasets exist, but most of them are more join-intensive and should be treated as second-wave work after the area-panel backbone is stable.
- Two ideas are explicitly marked as `Extension` because they depend on yet-to-be-built or broadened amenity or environmental layers.

## Ranking Method
- Scores are on a `1-5` scale for `Novelty`, `Impact`, `Complexity`, and `Available data`.
- Higher `Complexity` means harder execution.
- Composite score formula: `Novelty + Impact + Available data + (6 - Complexity)`.
- `Plan ID` preserves the numbering from the approved plan.
- `Composite rank` re-sorts the full ideas set using the stated rule: higher composite score first, then higher impact, then higher novelty, then higher available data.
- If ideas remain tied after those rules, this implementation breaks ties by lower complexity and then by original `Plan ID` to keep the ordering deterministic.

## Core Research Interfaces
- Primary outcomes: log sale price, constant-quality price growth, repeat-sale or pseudo-repeat-sale appreciation, local median prices, real price growth, price-to-income ratios, price dispersion, and transaction/liquidity proxies.
- Spatial backbone: `dim_postcode_geography` for postcode to `LSOA`, `MSOA`, and `LAD`.
- Time defaults: transaction date for prices, calendar month for macro and crime, academic year for school data, financial year for supply, release year for deprivation.
- Default methods: hedonic panels, repeat-sales or pseudo-repeat-sales, event studies, DiD, distributed-lag panels, nonlinear threshold models, and local projections.

## Cross-Cutting Data Rules
- Keep `2011` and `2021` `LSOA` or `MSOA` vintages separate unless an explicit crosswalk is added.
- Treat deprivation as within-release relative ranking, not as a cross-nation cardinal score.
- Prefer achieved sale prices over listing proxies for all main outcomes in this ideas set.
- Build nominal and real versions of every core price series.
- Treat `AQMA` as an environmental-presence proxy, not as full pollution exposure.
- Treat school proximity as a quality-access proxy, not as a true catchment assignment.

## Master Table

| Plan ID | Composite rank | Theme | Study | Scores `(N/I/C/D)` | Composite | Data readiness |
| --- | --- | --- | --- | --- | --- | --- |
| `#1` | `1` | Finance, affordability, and macro | Mortgage-rate pass-through under supply constraints | `4/5/3/5` | `17` | `ready_now` |
| `#2` | `2` | Supply, stock, and spatial divergence | Net supply component heterogeneity and price response | `4/5/3/5` | `17` | `ready_now` |
| `#3` | `3` | Finance, affordability, and macro | Price-to-income misalignment and mean reversion | `4/5/3/5` | `17` | `ready_now` |
| `#4` | `4` | Supply, stock, and spatial divergence | Vacancy buffer versus price resilience | `4/4/2/5` | `17` | `ready_now` |
| `#5` | `5` | Finance, affordability, and macro | Quoted-effective mortgage spread as tightening proxy | `4/4/2/5` | `17` | `ready_now` |
| `#6` | `6` | Crime, deprivation, and environment | Crime composition capitalization versus total crime | `4/4/2/5` | `17` | `ready_now` |
| `#11` | `7` | Supply, stock, and spatial divergence | Demand shocks amplified in constrained or superstar areas | `4/5/4/5` | `16` | `ready_now` |
| `#7` | `8` | Finance, affordability, and macro | Inflation decomposition and real-price regime shifts | `4/5/3/4` | `16` | `ready_now` |
| `#8` | `9` | Demography, labour, methods, and extensions | Age composition and price gradients | `3/4/2/5` | `16` | `ready_now` |
| `#9` | `10` | Demography, labour, methods, and extensions | Local labour shocks and housing cyclicality | `3/4/2/5` | `16` | `ready_now` |
| `#10` | `11` | Crime, deprivation, and environment | Nonlinear deprivation gradient and threshold effects | `3/4/2/5` | `16` | `ready_now` |
| `#21` | `12` | Finance, affordability, and macro | Deflator choice sensitivity for real-price conclusions | `3/4/2/5` | `16` | `ready_now` |
| `#14` | `13` | Property quality and EPC | Energy-shock salience and EPC premium shift after 2022 | `5/5/4/3` | `15` | `join_intensive` |
| `#13` | `14` | Schools and human capital | Ofsted upgrade/downgrade event study | `4/5/4/4` | `15` | `join_intensive` |
| `#12` | `15` | Demography, labour, methods, and extensions | Hedonic versus repeat-sales divergence under composition change | `4/4/3/4` | `15` | `ready_now` |
| `#15` | `16` | Supply, stock, and spatial divergence | Population growth versus stock growth mismatch | `4/4/3/4` | `15` | `ready_now` |
| `#16` | `17` | Crime, deprivation, and environment | Persistent crime shocks and discount persistence | `4/4/3/4` | `15` | `ready_now` |
| `#17` | `18` | Supply, stock, and spatial divergence | Boom-bust amplitude in constrained places | `4/4/3/4` | `15` | `ready_now` |
| `#18` | `19` | Schools and human capital | Nearest primary versus secondary quality capitalization | `3/5/4/4` | `14` | `join_intensive` |
| `#19` | `20` | Schools and human capital | School-quality premium under affordability stress | `4/4/4/4` | `14` | `join_intensive` |
| `#20` | `21` | Crime, deprivation, and environment | AQMA declaration and price/liquidity effects | `4/4/3/3` | `14` | `ready_now` |
| `#24` | `22` | Schools and human capital | Nearby-school density and choice premium | `4/4/3/3` | `14` | `join_intensive` |
| `#22` | `23` | Crime, deprivation, and environment | Environmental injustice capitalization: AQMA x deprivation | `5/4/4/3` | `13` | `ready_now` |
| `#25` | `24` | Property quality and EPC | EPC upgrade capitalization using repeated certificates | `5/4/5/3` | `13` | `join_intensive` |
| `#23` | `25` | Property quality and EPC | EPC rating premium net of structural attributes | `4/4/4/3` | `13` | `join_intensive` |
| `#27` | `26` | Property quality and EPC | Floor-area versus efficiency trade-off in price formation | `4/3/4/3` | `12` | `join_intensive` |
| `#28` | `27` | Property quality and EPC | New-build, tenure, and property-type interactions with energy quality | `4/3/4/3` | `12` | `join_intensive` |
| `#30` | `28` | Demography, labour, methods, and extensions | Flood and climate-risk capitalization beyond AQMA | `5/5/5/2` | `11` | `extension` |
| `#29` | `29` | Demography, labour, methods, and extensions | Amenity access and broadband premium | `5/4/4/2` | `11` | `extension` |
| `#26` | `30` | Schools and human capital | Inspection volatility and price dispersion/liquidity | `4/3/4/4` | `11` | `join_intensive` |

## Recommended Starter Set
- First-wave build order: `#1`, `#2`, `#3`, `#4`, `#5`, and `#6`.
- Those six studies share the best combination of strong theory anchors, implemented data, manageable joins, and direct policy or market relevance.
- The next best second-wave studies are `#11`, `#7`, `#8`, `#9`, `#10`, and `#21`.
- School and EPC work should follow once the property-to-school and property-to-EPC joins are validated on a stable sample.

## Theme 1. Finance, Affordability, And Macro

### `#1` Mortgage-rate pass-through under supply constraints
- Research question: Do national mortgage-rate shocks capitalise more strongly into local prices where supply and stock adjustment are weakest?
- Why it is interesting: This connects user-cost theory to local supply heterogeneity instead of treating mortgage shocks as spatially uniform.
- Potential impact: High. It can explain why the same national financing shock creates sharply different local outcomes and helps frame affordability debates in constrained markets.
- Available knowledge base: Strong. Main anchors are `Poterba (1984)`, `Saiz (2010)`, `Hilber and Vermeulen (2016)`, and `Ahearne et al. (2005)`.
- Available data: `source_land_registry_price_paid`, `dim_postcode_geography`, `fact_lad_supply_year`, `fact_lad_housing_stock_year`, `mortgage_rates_monthly_effective`, `mortgage_rates_monthly_quoted`, and `inflation_monthly_core`.
- High-level quantitative plan: Build quarterly `LAD` and `MSOA` sale-price panels, estimate mortgage-shock pass-through, interact shocks with supply and vacancy measures, then compare pooled, fixed-effects, and repeat-sale-leaning variants.
- Important caveats: Supply is observed mostly at `LAD` level, so `MSOA` work will need carefully assigned higher-level constraint proxies.

### `#3` Price-to-income misalignment and mean reversion
- Research question: Do extreme local price-to-income gaps predict slower future real appreciation or deeper subsequent drawdowns?
- Why it is interesting: It operationalizes the valuation literature in a UK-first area panel without requiring rents.
- Potential impact: High. It can identify local overheating and help separate structural expensiveness from short-run stretch.
- Available knowledge base: Strong. Main anchors are `Himmelberg, Mayer, and Sinai (2005)`, `Gallin (2008)`, and `Geng (2018)`.
- Available data: `source_land_registry_price_paid`, `dim_postcode_geography`, `fact_area_income_year`, and `inflation_monthly_core`.
- High-level quantitative plan: Construct annual and rolling local price-to-income ratios, form forward real-return windows, estimate nonlinear threshold regressions, and test whether high-ratio areas mean-revert more strongly.
- Important caveats: `fact_area_income_year` changes geography vintage, so all long-run panels must stay within comparable `MSOA` regimes or use an explicit bridge.

### `#5` Quoted-effective mortgage spread as tightening proxy
- Research question: Can the spread between quoted and effective mortgage rates proxy lender frictions or borrower selection when direct credit microdata are absent?
- Why it is interesting: It creates a tractable credit-tightening series from currently implemented data rather than waiting for richer lending microdata.
- Potential impact: High. It gives the ideas set a financing-frictions measure that can be used across many downstream studies.
- Available knowledge base: Strong. Main anchors are `Mian and Sufi (2009)`, `Mian and Sufi (2011)`, and the broader credit-channel literature.
- Available data: `mortgage_rates_monthly_quoted`, `mortgage_rates_monthly_effective`, `source_land_registry_price_paid`, `fact_area_income_year`, `fact_area_deprivation`, `fact_lad_supply_year`, and `fact_lad_housing_stock_year`.
- High-level quantitative plan: Build a national monthly spread series, aggregate prices to compatible time frequency, then interact the spread with local affordability, deprivation, and supply proxies in panel models.
- Important caveats: The spread is an indirect tightening proxy, so interpretation should stay at the level of financing friction or market selection, not literal underwriting standards.

### `#7` Inflation decomposition and real-price regime shifts
- Research question: When are nominal house-price booms mostly inflation pass-through, and when are they real revaluations?
- Why it is interesting: It turns inflation into a decomposition tool rather than a background control.
- Potential impact: High. It clarifies market narratives and makes long-run price comparisons far more defensible.
- Available knowledge base: Strong. Main anchors are `Poterba (1980)`, `Poterba (1984)`, and `Hendershott and Abraham (1992)`.
- Available data: `source_land_registry_price_paid`, `inflation_monthly_core`, and `inflation_monthly_housing_components`.
- High-level quantitative plan: Construct nominal and multiple real price indices, compare real growth under headline and housing-specific deflators, then classify regimes where nominal growth mostly reflects general inflation, housing-cost inflation, or real repricing.
- Important caveats: The housing-components table mixes monthly observations and annual weights, so any monthly decomposition must filter strictly by `period_type` and `value_type`.

### `#21` Deflator choice sensitivity for real-price conclusions
- Research question: How much do conclusions about peaks, drawdowns, and long-run appreciation change when different inflation deflators are used?
- Why it is interesting: It stress-tests one of the most common hidden assumptions in housing analysis.
- Potential impact: Medium to high. It improves analytical hygiene across the whole research program and can materially change historical interpretation.
- Available knowledge base: Strong. Main anchors are `Hill (2011)` and the housing valuation literature that distinguishes nominal from real comparisons.
- Available data: `source_land_registry_price_paid`, `inflation_monthly_core`, and `inflation_monthly_housing_components`.
- High-level quantitative plan: Rebuild the same price series under `CPIH`, `CPI`, `RPI`, and housing-component deflators, then compare ranking stability, turning points, drawdown depth, and persistence across versions.
- Important caveats: This is a measurement-sensitivity study, so it should be framed as a robustness layer rather than a standalone causal design.

## Theme 2. Supply, Stock, And Spatial Divergence

### `#2` Net supply component heterogeneity and price response
- Research question: Which realized supply components matter most for slowing local price growth: completions, conversions, change of use, or demolitions?
- Why it is interesting: It goes beyond one headline net-supply variable and tests whether different supply channels have different price effects.
- Potential impact: High. It is directly relevant to planning and housing-supply policy.
- Available knowledge base: Strong. Main anchors are `DiPasquale and Wheaton (1992)`, `Saiz (2010)`, and `Glaeser, Gyourko, and Saks (2005)`.
- Available data: `source_land_registry_price_paid`, `dim_postcode_geography`, and `fact_lad_supply_year`.
- High-level quantitative plan: Aggregate transactions to annual `LAD` panels, estimate distributed-lag models with supply components instead of a single headline series, and compare the marginal response to each component family.
- Important caveats: Supply is measured at financial-year `LAD` grain, so time alignment and interpretation must stay explicit.

### `#4` Vacancy buffer versus price resilience
- Research question: Do higher vacancy and long-term vacancy rates buffer local housing markets against shocks, or do they mostly signal structurally weak demand?
- Why it is interesting: It treats vacancy as both a slack measure and a structural-fragility signal.
- Potential impact: High. It helps distinguish healthy market flexibility from decline-related slack.
- Available knowledge base: Strong. Main anchors are `Wheaton (1990)` and the durable-housing literature.
- Available data: `source_land_registry_price_paid`, `dim_postcode_geography`, and `fact_lad_housing_stock_year`.
- High-level quantitative plan: Define downturn and rebound episodes, interact them with vacancy regimes, and estimate whether high-vacancy areas fall less, recover more slowly, or both.
- Important caveats: Pre- and post-2013 vacancy definitions are not perfectly comparable, so regime breaks must be made explicit.

### `#11` Demand shocks amplified in constrained or superstar areas
- Research question: Do income growth and financing shocks create larger price gains in supply-constrained or persistently high-demand places?
- Why it is interesting: It unifies superstar-city and supply-inelasticity arguments in one empirically testable area panel.
- Potential impact: High. It explains why expensive places often stay expensive while becoming more shock-sensitive.
- Available knowledge base: Strong. Main anchors are `Gyourko, Mayer, and Sinai (2013)`, `Hilber and Vermeulen (2016)`, and `Hsieh and Moretti (2019)`.
- Available data: `source_land_registry_price_paid`, `fact_area_income_year`, `fact_lad_supply_year`, `fact_lad_housing_stock_year`, `mortgage_rates_monthly_effective`, and `dim_postcode_geography`.
- High-level quantitative plan: Estimate price responses to income growth and mortgage shocks with interactions for supply tightness, vacancy scarcity, and persistent local premium status.
- Important caveats: “Superstar” status should be defined transparently from observable persistence, not from a hand-picked place list.

### `#15` Population growth versus stock growth mismatch
- Research question: Are the sharpest local price pressures observed where demographic demand proxies outrun stock and net additions?
- Why it is interesting: It turns long-run demand pressure into an explicit stock-adjustment mismatch metric.
- Potential impact: Medium to high. It can clarify whether local affordability problems are more demand-led or stock-led.
- Available knowledge base: Strong. Main anchors are `Mankiw and Weil (1989)` and `Geng (2018)`.
- Available data: `source_land_registry_price_paid`, `fact_area_demographics_year`, `fact_lad_housing_stock_year`, `fact_lad_supply_year`, and `dim_postcode_geography`.
- High-level quantitative plan: Build annual demand-growth and stock-growth measures, form mismatch indicators, and estimate nonlinear price responses and persistence by mismatch regime.
- Important caveats: The demographic table is strongest for age and population continuity, not for full annual household structure.

### `#17` Boom-bust amplitude in constrained places
- Research question: Do supply-constrained places experience both larger booms and more asymmetric or slower corrections?
- Why it is interesting: It extends supply-inelasticity work from level effects to full cycle shape.
- Potential impact: Medium to high. It helps explain volatility, not just expensiveness.
- Available knowledge base: Strong. Main anchors are `Glaeser, Gyourko, and Saiz (2008)` and `Hilber and Vermeulen (2016)`.
- Available data: `source_land_registry_price_paid`, `fact_lad_supply_year`, `fact_lad_housing_stock_year`, `mortgage_rates_monthly_effective`, and `dim_postcode_geography`.
- High-level quantitative plan: Identify local boom and correction phases from price cycles, then regress amplitude, duration, and recovery speed on supply and stock proxies.
- Important caveats: Cycle dating should be sensitivity-tested because turning points can shift with deflator choice and aggregation frequency.

## Theme 3. Crime, Deprivation, And Environment

### `#6` Crime composition capitalization versus total crime
- Research question: Do different crime categories carry different price discounts once total crime is decomposed?
- Why it is interesting: It tests whether the market prices visible disorder, violence, theft risk, and antisocial behaviour differently rather than folding them into one average crime coefficient.
- Potential impact: High. It improves neighborhood-safety modeling and helps identify which safety dimensions are most economically salient.
- Available knowledge base: Strong. Main anchors are `Gibbons (2004)` and `Linden and Rockoff (2008)`.
- Available data: `source_land_registry_price_paid`, `dim_postcode_geography`, and `fact_area_crime_month`.
- High-level quantitative plan: Build `LSOA`-month crime exposures by category, estimate category-specific hedonic and panel effects, and compare pooled versus property-type-specific elasticities.
- Important caveats: Crime-category definitions and recording practices can shift over time, so long-run category panels need stability checks.

### `#10` Nonlinear deprivation gradient and threshold effects
- Research question: Are deprivation discounts smooth, or do prices fall sharply beyond specific deprivation thresholds?
- Why it is interesting: It tests for neighborhood tipping points rather than assuming a linear place-quality slope.
- Potential impact: High. It can improve targeting for regeneration and local affordability analysis.
- Available knowledge base: Strong. Main anchors are `Roback (1982)` and the broader place-quality capitalization literature.
- Available data: `source_land_registry_price_paid`, `dim_postcode_geography`, and `fact_area_deprivation`.
- High-level quantitative plan: Merge transactions to within-release deprivation percentiles, estimate spline and threshold models, and compare percentile-based versus rank-based specifications.
- Important caveats: Cross-nation or cross-release score comparisons remain unsafe, so this should stay within comparable release contexts.

### `#16` Persistent crime shocks and discount persistence
- Research question: Do large local crime increases produce temporary fear discounts or longer-run neighborhood scarring?
- Why it is interesting: It turns the long crime panel into a persistence study rather than a static cross-section.
- Potential impact: Medium to high. It helps distinguish transitory disamenities from durable local deterioration.
- Available knowledge base: Strong. Main anchors are the crime-capitalization literature plus local-shock event-study methods.
- Available data: `source_land_registry_price_paid`, `fact_area_crime_month`, and `dim_postcode_geography`.
- High-level quantitative plan: Detect large local crime shocks, estimate event-time price responses, and measure the half-life of discounts and post-shock recovery.
- Important caveats: Shock identification should separate broad national crime waves from genuinely local shifts.

### `#20` AQMA declaration and price/liquidity effects
- Research question: Does `AQMA` declaration or sustained `AQMA` exposure slow appreciation or reduce local transaction intensity?
- Why it is interesting: It exploits the implemented environmental layer without waiting for a full pollution raster build.
- Potential impact: Medium. It can deliver a credible first environmental capitalization study from the current stack.
- Available knowledge base: Strong enough. Main anchors are `Chay and Greenstone (2005)` and later environmental-risk capitalization work.
- Available data: `source_land_registry_price_paid`, `fact_area_environment`, and `dim_postcode_geography`.
- High-level quantitative plan: Build authority-year event panels around declaration timing, estimate price and transaction-count effects, and check pre-trends and alternative event windows.
- Important caveats: The current environment table is `AQMA`-first and not a full historical pollution exposure model.

### `#22` Environmental injustice capitalization: AQMA x deprivation
- Research question: Are environmental disamenities priced differently in already-deprived places?
- Why it is interesting: It links environmental burden, place inequality, and housing-market valuation in one design.
- Potential impact: Medium. It can identify whether environmental harms are ignored, amplified, or discounted differently across local social contexts.
- Available knowledge base: Strong enough. Main anchors are `Currie et al. (2015)` and the environmental capitalization branch in the literature library.
- Available data: `source_land_registry_price_paid`, `fact_area_environment`, `fact_area_deprivation`, and `dim_postcode_geography`.
- High-level quantitative plan: Estimate price effects of `AQMA` presence with deprivation interactions, then compare effect size by deprivation percentile or decile.
- Important caveats: Because `AQMA` is a coarse proxy, findings should be framed as environmental-presence heterogeneity, not as exact pollution-dose effects.

## Theme 4. Schools And Human Capital

### `#13` Ofsted upgrade/downgrade event study
- Research question: Do nearby prices respond to school inspection rating upgrades and downgrades?
- Why it is interesting: It gives the ideas set a direct school-quality event study rather than relying only on static school-performance correlations.
- Potential impact: High. It can produce some of the clearest local amenity evidence in the full ideas set.
- Available knowledge base: Strong. Main anchors are `Black (1999)` and the school-capitalization literature summarized in the library.
- Available data: `dim_school`, `fact_school_ofsted_inspection`, `source_land_registry_price_paid`, and `dim_postcode_geography`.
- High-level quantitative plan: Build school-event panels, map nearby sales using school coordinates and property postcode centroids, estimate event-time effects, and test multiple radii and placebo dates.
- Important caveats: The current property side is postcode-centroid based, so very tight radius interpretations need caution.

### `#18` Nearest primary versus secondary quality capitalization
- Research question: Are primary and secondary school quality premia different, and do they vary by property type or urban context?
- Why it is interesting: It decomposes the school premium into distinct life-stage channels instead of averaging everything together.
- Potential impact: Medium to high. It can sharpen school-context modeling and family-segment interpretation.
- Available knowledge base: Strong. Main anchors are `Black (1999)` and later review work on school-quality capitalization.
- Available data: `mart_property_school_context`, `dim_school`, `fact_school_performance_year`, `fact_school_ofsted_inspection`, and `source_land_registry_price_paid`.
- High-level quantitative plan: Use nearest-school and nearby-school context features, then estimate differential capitalization by school phase, dwelling type, and urbanity.
- Important caveats: The current school mart is a current-context snapshot rather than a point-in-time historical catchment reconstruction.

### `#19` School-quality premium under affordability stress
- Research question: Does school-quality capitalization strengthen or weaken when mortgage conditions tighten?
- Why it is interesting: It tests whether constrained households become more selective about quality-location trade-offs.
- Potential impact: Medium. It links local amenity demand to macro affordability regimes.
- Available knowledge base: Strong. Main anchors are `Black (1999)` plus user-cost and financing-channel theory.
- Available data: `mart_property_school_context`, `fact_school_performance_year`, `fact_school_ofsted_inspection`, `source_land_registry_price_paid`, and `mortgage_rates_monthly_effective`.
- High-level quantitative plan: Interact school-quality measures with high-rate or low-affordability periods and test whether premiums become steeper, flatter, or more segmented.
- Important caveats: Timing alignment matters because school outcomes are by academic year while mortgage and sale data are monthly.

### `#24` Nearby-school density and choice premium
- Research question: Do places with many nearby good schools command a premium above what is explained by the nearest school alone?
- Why it is interesting: It captures choice-set value, not just nearest-provider value.
- Potential impact: Medium. It broadens the school mechanism from single-school access to neighborhood option density.
- Available knowledge base: Good. It extends standard school capitalization logic in a direction that the current school mart supports well.
- Available data: `mart_property_school_context`, `dim_school`, `fact_school_performance_year`, and `source_land_registry_price_paid`.
- High-level quantitative plan: Use nearby-school counts, quality shares, and mean nearby performance scores, then compare model lift relative to nearest-school-only specifications.
- Important caveats: Urban-rural comparisons need care because school density is structurally different across settlement types.

### `#26` Inspection volatility and price dispersion/liquidity
- Research question: Does repeated inspection volatility around local schools widen sale-price dispersion or reduce nearby transaction intensity?
- Why it is interesting: It reframes school quality as an uncertainty channel rather than just a level premium.
- Potential impact: Lower than the other school studies but still useful as a niche uncertainty mechanism test.
- Available knowledge base: Moderate. It is more novel than classical school-premium work but has a thinner direct prior.
- Available data: `dim_school`, `fact_school_ofsted_inspection`, `source_land_registry_price_paid`, and `dim_postcode_geography`.
- High-level quantitative plan: Build local school-quality uncertainty measures from inspection volatility, then relate them to sale-price dispersion and local transaction counts.
- Important caveats: Dispersion and liquidity outcomes are noisier than price levels, so this should come after the core school event studies.

## Theme 5. Property Quality And EPC

### `#14` Energy-shock salience and EPC premium shift after 2022
- Research question: Did the market premium for efficient homes steepen after the utilities shock made running costs more salient?
- Why it is interesting: It uses a concrete macro shock to test time-varying capitalization of energy efficiency.
- Potential impact: High. It is policy-relevant for retrofit, affordability, and consumer response to energy costs.
- Available knowledge base: Strong enough. It sits cleanly inside hedonic pricing and housing-cost salience logic.
- Available data: `fact_property_epc_certificate`, `dim_property_epc_latest`, `source_land_registry_price_paid`, and `dim_postcode_geography`.
- High-level quantitative plan: Join sale records to latest or near-sale EPC state, estimate EPC premia before and after 2022, and interact the shift with property type, age band, and region.
- Important caveats: Transaction-to-EPC matching needs a transparent quality threshold and should be validated on a high-confidence matched subset first.

### `#23` EPC rating premium net of structural attributes
- Research question: Does energy efficiency still price once floor area, age band, built form, tenure, and other structural characteristics are controlled?
- Why it is interesting: It is the cleanest EPC benchmark study and provides the baseline for all later retrofit work.
- Potential impact: Medium. It creates a defensible estimate of the stand-alone efficiency premium.
- Available knowledge base: Strong enough. Main anchor is `Rosen (1974)` plus hedonic housing-quality work.
- Available data: `dim_property_epc_latest`, `source_land_registry_price_paid`, and `fact_property_epc_certificate`.
- High-level quantitative plan: Estimate matched and hedonic sale-price models on the highest-confidence EPC-linked sample, then compare results with and without structural controls.
- Important caveats: EPC-linked samples can be compositionally selective, so matched-sample representativeness must be checked.

### `#25` EPC upgrade capitalization using repeated certificates
- Research question: Are retrofit-like energy improvements capitalized into later sale prices?
- Why it is interesting: It moves from static quality premia to dynamic upgrade effects.
- Potential impact: Medium. It is especially useful for retrofit economics and renovation policy.
- Available knowledge base: Moderate to strong. It combines repeat-observation logic with hedonic quality-change reasoning.
- Available data: `fact_property_epc_certificate`, `dim_property_epc_latest`, and `source_land_registry_price_paid`.
- High-level quantitative plan: Detect material EPC improvements for the same inferred property, treat them as upgrade events, and compare subsequent sale outcomes against matched non-upgraded controls.
- Important caveats: This is one of the hardest studies in the ideas set because it needs repeated certificates, robust timing logic, and careful property identity handling.

### `#27` Floor-area versus efficiency trade-off in price formation
- Research question: When space and running-cost efficiency trade off, which dimension dominates buyer valuation?
- Why it is interesting: It tests a direct trade-off at the heart of modern affordability and liveability choices.
- Potential impact: Medium. It can clarify whether buyers pay more for larger homes even when they are costlier to run.
- Available knowledge base: Moderate. It follows naturally from hedonic theory but is more exploratory than the top EPC items.
- Available data: `dim_property_epc_latest`, `fact_property_epc_certificate`, and `source_land_registry_price_paid`.
- High-level quantitative plan: Estimate interactions between floor area and efficiency metrics, then compare the trade-off across regions, property types, and post-2022 periods.
- Important caveats: Floor area and structural quality are tightly correlated, so the identifying variation will be limited without careful controls.

### `#28` New-build, tenure, and property-type interactions with energy quality
- Research question: Is the energy-efficiency premium concentrated in specific segments such as flats, leasehold homes, or older stock?
- Why it is interesting: It tests whether the EPC premium is really a segment effect hidden by pooled estimates.
- Potential impact: Medium. It is useful for market segmentation and targeted retrofit or development analysis.
- Available knowledge base: Moderate. It extends standard hedonic logic into segmentation rather than opening a new theory branch.
- Available data: `dim_property_epc_latest`, `fact_property_epc_certificate`, and `source_land_registry_price_paid`.
- High-level quantitative plan: Estimate segmented hedonic models and pooled interaction models for new-build status, tenure, property type, and age band.
- Important caveats: Sub-sample power can drop quickly, especially once matching filters are tightened.

## Theme 6. Demography, Labour, Methods, And Extensions

### `#8` Age composition and price gradients
- Research question: Which age mixes explain local price levels and which explain price growth?
- Why it is interesting: It separates structural life-cycle demand from short-run market momentum.
- Potential impact: High enough to matter across many place-based questions, especially affordability and family-market segmentation.
- Available knowledge base: Strong. Main anchors are `Mankiw and Weil (1989)` and `Geng (2018)`.
- Available data: `fact_area_demographics_year`, `source_land_registry_price_paid`, and `dim_postcode_geography`.
- High-level quantitative plan: Build within-vintage age-share panels, estimate effects on local price levels and growth, and test nonlinearities for family-heavy versus older areas.
- Important caveats: Only age and population measures are continuous across annual years; the richer demographic families are census-year only.

### `#9` Local labour shocks and housing cyclicality
- Research question: Do claimant-count spikes predict sharper drawdowns, weaker rebounds, or wider local price dispersion?
- Why it is interesting: It adds a monthly local stress channel that is timelier than most annual datasets.
- Potential impact: High enough to make it one of the best near-term cyclical studies in the ideas set.
- Available knowledge base: Strong. Main anchors are `Gan and Zhang (2006)` and `Liu, Miao, and Zha (2016)`.
- Available data: `fact_area_labour_month`, `source_land_registry_price_paid`, `dim_postcode_geography`, and optionally mortgage tables.
- High-level quantitative plan: Use local projections around claimant shocks, interact with affordability or supply exposure, and compare effects on price growth, drawdowns, and dispersion.
- Important caveats: Labour data are at `LAD` level in the current implementation, so finer-grain interpretation must be proxy-based.

### `#12` Hedonic versus repeat-sales divergence under composition change
- Research question: When do hedonic and repeat-sales price indices disagree, and how much of the gap is due to changing sales mix?
- Why it is interesting: It makes measurement itself a research object, not just a preprocessing step.
- Potential impact: Medium to high. It improves every later price study by clarifying which constant-quality method is most trustworthy in each setting.
- Available knowledge base: Strong. Main anchors are `Bailey, Muth, and Nourse (1963)`, `Case and Shiller (1987)`, and `Hill (2011)`.
- Available data: `source_land_registry_price_paid`, with geography enrichment from `dim_postcode_geography`.
- High-level quantitative plan: Build parallel hedonic and repeat-sale or pseudo-repeat-sale indices, then decompose divergence into mix shifts, sparse-repeat bias, and geography aggregation effects.
- Important caveats: Pure repeat-sales work is constrained by address normalization quality, so the first pass may need a conservative pseudo-repeat design.

### `#29` `Extension` Amenity access and broadband premium
- Research question: Once a property-level amenity mart exists, how much do stations, parks, shops, and broadband proxies price into nearby sales?
- Why it is interesting: It opens a broad liveability and accessibility branch that the current literature supports strongly.
- Potential impact: Medium. It could become one of the richest future hedonic extensions once the amenity layer is built.
- Available knowledge base: Strong. Main anchors are `Roback (1982)` and `Gibbons and Machin (2005)`.
- Available data: Planned `mart_property_amenity_context` plus `source_land_registry_price_paid`.
- High-level quantitative plan: Use nearest-distance and amenity-density features in hedonic and segmented models, then compare urban and rural capitalization patterns.
- Important caveats: This remains an extension because the amenity mart is still a design-stage spec rather than a loaded table.

### `#30` `Extension` Flood and climate-risk capitalization beyond AQMA
- Research question: Once the environmental layer expands beyond `AQMA`, do physical climate risks affect prices, liquidity, or only specific submarkets?
- Why it is interesting: It is the highest-upside frontier study in the whole ideas set.
- Potential impact: Very high. It connects housing valuation, insurance, local resilience, and climate adaptation.
- Available knowledge base: Strong. Main anchors are `Beltran, Maddison, and Elliott (2019)`, `Bernstein, Gustafson, and Lewis (2019)`, `Keys and Mulder (2020)`, and `Baldauf, Garlappi, and Yannelis (2020)`.
- Available data: Current `fact_area_environment` is not yet sufficient; this study needs a broadened environmental layer with flood and climate-risk measures.
- High-level quantitative plan: Build property or area-level risk exposure measures, estimate price and liquidity capitalization, and test whether markets react only after repeated events or salience shocks.
- Important caveats: This is intentionally parked as an extension because the current environment implementation is AQMA-only.

## Validation Checklist
- Boundary safety: do not silently compare `2011` and `2021` small-area vintages without a bridge.
- Deprivation safety: use percentiles or within-release ranks, not raw cross-nation scores.
- Measurement safety: compare nominal and real outcomes, and compare hedonic and repeat-sale variants where possible.
- Event-study safety: require pre-trend checks, placebo dates, and alternate treatment radii.
- Sample safety: quantify how match filters change the EPC or school-linked sample relative to the full transaction universe.
- Robustness safety: vary time aggregation, winsorization, fixed-effects structure, and urban-rural splits.

## How To Use These Ideas
- Start with the top six `ready_now` studies to establish shared price panels, deflators, and geography joins.
- Reuse those common panels for the rest of the area-level research rather than rebuilding one-off datasets study by study.
- Treat school and EPC work as dedicated second-wave packages because they depend on higher-friction joins and stronger sample-validation needs.
- Treat the two `Extension` items as design targets for future data-build work, not as immediate execution tasks.
