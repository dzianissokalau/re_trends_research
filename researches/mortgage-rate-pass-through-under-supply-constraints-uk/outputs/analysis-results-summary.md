# Analysis Results Summary

> Disclaimer: This document was generated with AI and has received only limited human review. It may contain errors or omissions and should be independently verified before use.

- Main LAD-quarter panel rows: `13,319`.
- LADs in panel: `296`.
- Quarters in panel: `2015Q1` to `2026Q1`.
- Sparse cells with fewer than 20 transactions: `45`.
- LADs with static 2013-2015 supply and vacancy constraints: `326`.

## Hypothesis Summary

- `H1` `low`: effective beta=-0.007102, p=0.0246; quoted beta=-0.001593, p=0.0966
- `H2` `inconclusive`: transaction beta=0.001319, p=0.9039
- `H3` `inconclusive`: stock-tightness beta=0.003484, p=0.1644
- `H4` `inconclusive`: spread beta=0.000230, p=0.8561
- `H5` `low`: supply_tightness Q1 price=-7.49%, tx=8.23%; supply_tightness Q4 price=-3.45%, tx=3.94%

## Data Issue Mitigations

- `Completed-sale timing and late registration`: Latest-quarter completeness audit, exclusion of outcomes ending in 2025Q4/2026Q1, lagged and cumulative mortgage-rate timings, and shifted episode windows. Residual risk: Completion date can still lag price negotiation and mortgage arrangement; exact decision date is unobserved.
- `Approximate median price and changing transaction composition`: Mean-log price robustness and property-mix controls using property type, tenure, and new-build shares. Residual risk: No repeat-sales or hedonic adjustment; unobserved quality mix can remain.
- `Current postcode geography applied to historical sales`: Postcode match-rate audit by transaction year and explicit NSPL-snapshot caveat. Residual risk: Point-in-time geography reconstruction is not available in the current extract.
- `Annual supply/vacancy timing and definitions`: Predetermined 2013-2015 averages plus alternative 2015-only and completions-based constraint checks. Residual risk: Supply and vacancy are annual, realized, and may be endogenous to local demand conditions.
- `Local labour-market confounding`: Claimant metric level and 4Q change controls from the existing labour extract; the current extract falls back to claimant count where claimant rate is unavailable. Residual risk: Claimant count is not population-normalized and is not a complete local-demand control.
- `Sparse LAD-quarter cells`: Baseline excludes cells below 20 transactions; robustness requires at least 50 transactions at both start and horizon. Residual risk: Small or volatile local markets can still have noisy median prices.
- `Observed mortgage rates are not exogenous shocks`: Multiple mortgage-rate definitions and timing conventions; conclusions framed as screening associations. Residual risk: No MPC/OIS surprise instrument is included.

## Completed-Sale Timing Checks

| Quarter | LAD cells | Transactions | Median transactions per LAD | Sparse cells | Change vs prior year |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2023Q4 | 296 | 173076 | 486.0 | 1 | -23.65% |
| 2024Q1 | 296 | 146661 | 417.0 | 1 | -9.21% |
| 2024Q2 | 296 | 167670 | 472.0 | 1 | 10.09% |
| 2024Q3 | 296 | 198206 | 560.5 | 1 | 8.39% |
| 2024Q4 | 296 | 207363 | 579.0 | 1 | 19.81% |
| 2025Q1 | 296 | 230099 | 662.0 | 1 | 56.89% |
| 2025Q2 | 296 | 122956 | 336.5 | 1 | -26.67% |
| 2025Q3 | 296 | 161477 | 452.5 | 1 | -18.53% |
| 2025Q4 | 296 | 137562 | 376.0 | 1 | -33.66% |
| 2026Q1 | 295 | 45757 | 126.0 | 1 | -80.11% |

## Lagged Mortgage-Rate Results

| Timing | Outcome | Shock | Constraint | Beta | SE | p-value | N |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| current_q | price_h4 | delta_effective_new_business_headline | supply_tightness | -0.007102 | 0.003159 | 0.0246 | 10433 |
| current_q | price_h4 | delta_effective_new_business_headline | stock_tightness | 0.003484 | 0.002506 | 0.1644 | 10433 |
| current_q | price_h4 | delta_quoted_2y_75_ltv | supply_tightness | -0.001593 | 0.000959 | 0.0966 | 10433 |
| current_q | price_h4 | delta_quoted_2y_75_ltv | stock_tightness | 0.001923 | 0.001219 | 0.1146 | 10433 |
| current_q | transactions_h4 | delta_effective_new_business_headline | supply_tightness | 0.001319 | 0.010930 | 0.9039 | 10433 |
| current_q | transactions_h4 | delta_effective_new_business_headline | stock_tightness | -0.022902 | 0.004422 | 0.0000 | 10433 |
| current_q | transactions_h4 | delta_quoted_2y_75_ltv | supply_tightness | 0.007957 | 0.002813 | 0.0047 | 10433 |
| current_q | transactions_h4 | delta_quoted_2y_75_ltv | stock_tightness | -0.008030 | 0.002139 | 0.0002 | 10433 |
| lag_1q | price_h4 | delta_effective_new_business_headline | supply_tightness | 0.001118 | 0.002203 | 0.6119 | 10433 |
| lag_1q | price_h4 | delta_effective_new_business_headline | stock_tightness | -0.011501 | 0.002592 | 0.0000 | 10433 |
| lag_1q | price_h4 | delta_quoted_2y_75_ltv | supply_tightness | -0.004200 | 0.002010 | 0.0367 | 10433 |
| lag_1q | price_h4 | delta_quoted_2y_75_ltv | stock_tightness | 0.001036 | 0.001120 | 0.3549 | 10433 |
| lag_1q | transactions_h4 | delta_effective_new_business_headline | supply_tightness | -0.009709 | 0.006106 | 0.1118 | 10433 |
| lag_1q | transactions_h4 | delta_effective_new_business_headline | stock_tightness | 0.012849 | 0.004195 | 0.0022 | 10433 |
| lag_1q | transactions_h4 | delta_quoted_2y_75_ltv | supply_tightness | -0.002303 | 0.005743 | 0.6885 | 10433 |
| lag_1q | transactions_h4 | delta_quoted_2y_75_ltv | stock_tightness | -0.007532 | 0.001976 | 0.0001 | 10433 |
| lag_2q | price_h4 | delta_effective_new_business_headline | supply_tightness | 0.007422 | 0.006003 | 0.2163 | 10433 |
| lag_2q | price_h4 | delta_effective_new_business_headline | stock_tightness | -0.005350 | 0.002548 | 0.0357 | 10433 |
| lag_2q | price_h4 | delta_quoted_2y_75_ltv | supply_tightness | 0.000157 | 0.000829 | 0.8500 | 10433 |
| lag_2q | price_h4 | delta_quoted_2y_75_ltv | stock_tightness | -0.004760 | 0.001139 | 0.0000 | 10433 |
| lag_2q | transactions_h4 | delta_effective_new_business_headline | supply_tightness | -0.000871 | 0.004692 | 0.8528 | 10433 |
| lag_2q | transactions_h4 | delta_effective_new_business_headline | stock_tightness | 0.003902 | 0.004203 | 0.3532 | 10433 |
| lag_2q | transactions_h4 | delta_quoted_2y_75_ltv | supply_tightness | -0.004157 | 0.002809 | 0.1390 | 10433 |
| lag_2q | transactions_h4 | delta_quoted_2y_75_ltv | stock_tightness | 0.003275 | 0.001866 | 0.0793 | 10433 |
| lag_3q | price_h4 | delta_effective_new_business_headline | supply_tightness | 0.009385 | 0.004360 | 0.0314 | 10433 |
| lag_3q | price_h4 | delta_effective_new_business_headline | stock_tightness | -0.009436 | 0.002644 | 0.0004 | 10433 |
| lag_3q | price_h4 | delta_quoted_2y_75_ltv | supply_tightness | 0.001353 | 0.002572 | 0.5989 | 10433 |
| lag_3q | price_h4 | delta_quoted_2y_75_ltv | stock_tightness | 0.001478 | 0.000999 | 0.1392 | 10433 |
| lag_3q | transactions_h4 | delta_effective_new_business_headline | supply_tightness | -0.009864 | 0.008485 | 0.2451 | 10433 |
| lag_3q | transactions_h4 | delta_effective_new_business_headline | stock_tightness | 0.033886 | 0.004975 | 0.0000 | 10433 |
| lag_3q | transactions_h4 | delta_quoted_2y_75_ltv | supply_tightness | 0.002084 | 0.001864 | 0.2634 | 10433 |
| lag_3q | transactions_h4 | delta_quoted_2y_75_ltv | stock_tightness | -0.005531 | 0.001921 | 0.0040 | 10433 |
| cumulative_2q | price_h4 | delta_effective_new_business_headline | supply_tightness | -0.001768 | 0.001270 | 0.1638 | 10433 |
| cumulative_2q | price_h4 | delta_effective_new_business_headline | stock_tightness | -0.002358 | 0.001340 | 0.0785 | 10433 |
| cumulative_2q | price_h4 | delta_quoted_2y_75_ltv | supply_tightness | -0.002658 | 0.000988 | 0.0072 | 10433 |
| cumulative_2q | price_h4 | delta_quoted_2y_75_ltv | stock_tightness | 0.001359 | 0.000865 | 0.1160 | 10433 |
| cumulative_2q | transactions_h4 | delta_effective_new_business_headline | supply_tightness | -0.002448 | 0.004549 | 0.5905 | 10433 |
| cumulative_2q | transactions_h4 | delta_effective_new_business_headline | stock_tightness | -0.002950 | 0.002214 | 0.1826 | 10433 |
| cumulative_2q | transactions_h4 | delta_quoted_2y_75_ltv | supply_tightness | 0.002601 | 0.002371 | 0.2727 | 10433 |
| cumulative_2q | transactions_h4 | delta_quoted_2y_75_ltv | stock_tightness | -0.007146 | 0.001449 | 0.0000 | 10433 |
| cumulative_4q | price_h4 | delta_effective_new_business_headline | supply_tightness | 0.000964 | 0.001043 | 0.3554 | 10433 |
| cumulative_4q | price_h4 | delta_effective_new_business_headline | stock_tightness | -0.002095 | 0.000778 | 0.0071 | 10433 |
| cumulative_4q | price_h4 | delta_quoted_2y_75_ltv | supply_tightness | -0.000895 | 0.000588 | 0.1282 | 10433 |
| cumulative_4q | price_h4 | delta_quoted_2y_75_ltv | stock_tightness | -0.000063 | 0.000569 | 0.9121 | 10433 |
| cumulative_4q | transactions_h4 | delta_effective_new_business_headline | supply_tightness | -0.001760 | 0.001471 | 0.2316 | 10433 |
| cumulative_4q | transactions_h4 | delta_effective_new_business_headline | stock_tightness | 0.002511 | 0.001244 | 0.0436 | 10433 |
| cumulative_4q | transactions_h4 | delta_quoted_2y_75_ltv | supply_tightness | 0.000747 | 0.001685 | 0.6576 | 10433 |
| cumulative_4q | transactions_h4 | delta_quoted_2y_75_ltv | stock_tightness | -0.003674 | 0.000991 | 0.0002 | 10433 |

## Robustness Results

| Robustness | Outcome | Shock | Constraint | Beta | SE | p-value | N |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| cpi_deflator | price_h4 | delta_effective_new_business_headline | supply_tightness | -0.007102 | 0.003159 | 0.0246 | 10433 |
| cpi_deflator | price_h4 | delta_effective_new_business_headline | stock_tightness | 0.003484 | 0.002506 | 0.1644 | 10433 |
| cpi_deflator | price_h4 | delta_quoted_2y_75_ltv | supply_tightness | -0.001593 | 0.000959 | 0.0966 | 10433 |
| cpi_deflator | price_h4 | delta_quoted_2y_75_ltv | stock_tightness | 0.001923 | 0.001219 | 0.1146 | 10433 |
| mean_log_price_measure | price_h4 | delta_effective_new_business_headline | supply_tightness | -0.005430 | 0.002505 | 0.0302 | 10433 |
| mean_log_price_measure | price_h4 | delta_effective_new_business_headline | stock_tightness | 0.005280 | 0.002380 | 0.0266 | 10433 |
| mean_log_price_measure | price_h4 | delta_quoted_2y_75_ltv | supply_tightness | -0.000412 | 0.000774 | 0.5948 | 10433 |
| mean_log_price_measure | price_h4 | delta_quoted_2y_75_ltv | stock_tightness | 0.001559 | 0.001043 | 0.1351 | 10433 |
| composition_controls | price_h4 | delta_effective_new_business_headline | supply_tightness | -0.005292 | 0.002259 | 0.0191 | 10433 |
| composition_controls | price_h4 | delta_effective_new_business_headline | stock_tightness | 0.002961 | 0.002164 | 0.1713 | 10433 |
| composition_controls | price_h4 | delta_quoted_2y_75_ltv | supply_tightness | -0.002168 | 0.000828 | 0.0089 | 10433 |
| composition_controls | price_h4 | delta_quoted_2y_75_ltv | stock_tightness | 0.001652 | 0.001070 | 0.1226 | 10433 |
| labour_controls | price_h4 | delta_effective_new_business_headline | supply_tightness | -0.007143 | 0.003190 | 0.0252 | 10152 |
| labour_controls | price_h4 | delta_effective_new_business_headline | stock_tightness | 0.004273 | 0.002522 | 0.0902 | 10152 |
| labour_controls | price_h4 | delta_quoted_2y_75_ltv | supply_tightness | -0.001591 | 0.000958 | 0.0969 | 10152 |
| labour_controls | price_h4 | delta_quoted_2y_75_ltv | stock_tightness | 0.001857 | 0.001218 | 0.1273 | 10152 |
| labour_controls | transactions_h4 | delta_effective_new_business_headline | supply_tightness | 0.002036 | 0.011154 | 0.8552 | 10152 |
| labour_controls | transactions_h4 | delta_effective_new_business_headline | stock_tightness | -0.024281 | 0.004451 | 0.0000 | 10152 |
| labour_controls | transactions_h4 | delta_quoted_2y_75_ltv | supply_tightness | 0.007908 | 0.002806 | 0.0048 | 10152 |
| labour_controls | transactions_h4 | delta_quoted_2y_75_ltv | stock_tightness | -0.008016 | 0.002141 | 0.0002 | 10152 |
| exclude_london | price_h4 | delta_effective_new_business_headline | supply_tightness | -0.000485 | 0.003181 | 0.8788 | 9213 |
| exclude_london | price_h4 | delta_effective_new_business_headline | stock_tightness | -0.002041 | 0.002504 | 0.4149 | 9213 |
| exclude_london | price_h4 | delta_quoted_2y_75_ltv | supply_tightness | -0.001628 | 0.000968 | 0.0926 | 9213 |
| exclude_london | price_h4 | delta_quoted_2y_75_ltv | stock_tightness | 0.000902 | 0.001222 | 0.4603 | 9213 |
| exclude_london | transactions_h4 | delta_effective_new_business_headline | supply_tightness | 0.015733 | 0.005913 | 0.0078 | 9213 |
| exclude_london | transactions_h4 | delta_effective_new_business_headline | stock_tightness | -0.022487 | 0.004761 | 0.0000 | 9213 |
| exclude_london | transactions_h4 | delta_quoted_2y_75_ltv | supply_tightness | 0.005211 | 0.002912 | 0.0735 | 9213 |
| exclude_london | transactions_h4 | delta_quoted_2y_75_ltv | stock_tightness | -0.006369 | 0.002320 | 0.0061 | 9213 |
| drop_latest_two_completion_quarters | price_h4 | delta_effective_new_business_headline | supply_tightness | -0.007199 | 0.003465 | 0.0377 | 9870 |
| drop_latest_two_completion_quarters | price_h4 | delta_effective_new_business_headline | stock_tightness | 0.004390 | 0.002600 | 0.0914 | 9870 |
| drop_latest_two_completion_quarters | price_h4 | delta_quoted_2y_75_ltv | supply_tightness | -0.001537 | 0.000896 | 0.0862 | 9870 |
| drop_latest_two_completion_quarters | price_h4 | delta_quoted_2y_75_ltv | stock_tightness | 0.001859 | 0.001227 | 0.1296 | 9870 |
| drop_latest_two_completion_quarters | transactions_h4 | delta_effective_new_business_headline | supply_tightness | 0.005182 | 0.011268 | 0.6456 | 9870 |
| drop_latest_two_completion_quarters | transactions_h4 | delta_effective_new_business_headline | stock_tightness | -0.027970 | 0.004247 | 0.0000 | 9870 |
| drop_latest_two_completion_quarters | transactions_h4 | delta_quoted_2y_75_ltv | supply_tightness | 0.008774 | 0.002911 | 0.0026 | 9870 |
| drop_latest_two_completion_quarters | transactions_h4 | delta_quoted_2y_75_ltv | stock_tightness | -0.008765 | 0.002151 | 0.0000 | 9870 |
| min_50_transactions | price_h4 | delta_effective_new_business_headline | supply_tightness | -0.007030 | 0.003884 | 0.0703 | 10401 |
| min_50_transactions | price_h4 | delta_effective_new_business_headline | stock_tightness | 0.003327 | 0.002500 | 0.1833 | 10401 |
| min_50_transactions | price_h4 | delta_quoted_2y_75_ltv | supply_tightness | -0.002845 | 0.001242 | 0.0220 | 10401 |
| min_50_transactions | price_h4 | delta_quoted_2y_75_ltv | stock_tightness | 0.002008 | 0.001223 | 0.1006 | 10401 |
| min_50_transactions | transactions_h4 | delta_effective_new_business_headline | supply_tightness | 0.010238 | 0.006577 | 0.1196 | 10401 |
| min_50_transactions | transactions_h4 | delta_effective_new_business_headline | stock_tightness | -0.023789 | 0.004273 | 0.0000 | 10401 |
| min_50_transactions | transactions_h4 | delta_quoted_2y_75_ltv | supply_tightness | 0.004361 | 0.003220 | 0.1756 | 10401 |
| min_50_transactions | transactions_h4 | delta_quoted_2y_75_ltv | stock_tightness | -0.007526 | 0.002118 | 0.0004 | 10401 |
| constraint_avg_completions_2013_2015 | price_h4 | delta_effective_new_business_headline | completions_tightness | -0.006192 | 0.002744 | 0.0240 | 10433 |
| constraint_avg_completions_2013_2015 | price_h4 | delta_quoted_2y_75_ltv | completions_tightness | -0.000704 | 0.000814 | 0.3871 | 10433 |
| constraint_avg_completions_2013_2015 | transactions_h4 | delta_effective_new_business_headline | completions_tightness | 0.000019 | 0.008879 | 0.9983 | 10433 |
| constraint_avg_completions_2013_2015 | transactions_h4 | delta_quoted_2y_75_ltv | completions_tightness | 0.005634 | 0.002644 | 0.0331 | 10433 |
| constraint_net_additions_2015 | price_h4 | delta_effective_new_business_headline | supply_tightness_2015 | -0.005039 | 0.003197 | 0.1149 | 10433 |
| constraint_net_additions_2015 | price_h4 | delta_quoted_2y_75_ltv | supply_tightness_2015 | -0.001886 | 0.001112 | 0.0899 | 10433 |
| constraint_net_additions_2015 | transactions_h4 | delta_effective_new_business_headline | supply_tightness_2015 | -0.000777 | 0.009321 | 0.9336 | 10433 |
| constraint_net_additions_2015 | transactions_h4 | delta_quoted_2y_75_ltv | supply_tightness_2015 | 0.005847 | 0.002956 | 0.0480 | 10433 |
| constraint_vacancy_2015 | price_h4 | delta_effective_new_business_headline | stock_tightness_2015 | 0.002705 | 0.002720 | 0.3199 | 10433 |
| constraint_vacancy_2015 | price_h4 | delta_quoted_2y_75_ltv | stock_tightness_2015 | 0.001749 | 0.001260 | 0.1650 | 10433 |
| constraint_vacancy_2015 | transactions_h4 | delta_effective_new_business_headline | stock_tightness_2015 | -0.023374 | 0.004550 | 0.0000 | 10433 |
| constraint_vacancy_2015 | transactions_h4 | delta_quoted_2y_75_ltv | stock_tightness_2015 | -0.008340 | 0.002203 | 0.0002 | 10433 |
| constraint_long_vacancy_2015 | price_h4 | delta_effective_new_business_headline | long_vacancy_tightness_2015 | -0.000376 | 0.002630 | 0.8862 | 10433 |
| constraint_long_vacancy_2015 | price_h4 | delta_quoted_2y_75_ltv | long_vacancy_tightness_2015 | 0.000970 | 0.001234 | 0.4321 | 10433 |
| constraint_long_vacancy_2015 | transactions_h4 | delta_effective_new_business_headline | long_vacancy_tightness_2015 | -0.026155 | 0.004483 | 0.0000 | 10433 |
| constraint_long_vacancy_2015 | transactions_h4 | delta_quoted_2y_75_ltv | long_vacancy_tightness_2015 | -0.008763 | 0.002153 | 0.0000 | 10433 |

## Primary Model Results

| Outcome | Shock | Constraint | Beta | SE | p-value | N |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| price_h4 | delta_effective_new_business_headline | supply_tightness | -0.007102 | 0.003159 | 0.0246 | 10433 |
| price_h4 | delta_effective_new_business_headline | stock_tightness | 0.003484 | 0.002506 | 0.1644 | 10433 |
| price_h4 | delta_quoted_2y_75_ltv | supply_tightness | -0.001593 | 0.000959 | 0.0966 | 10433 |
| price_h4 | delta_quoted_2y_75_ltv | stock_tightness | 0.001923 | 0.001219 | 0.1146 | 10433 |
| price_h4 | delta_quoted_effective_spread_2y | supply_tightness | 0.000230 | 0.001268 | 0.8561 | 10433 |
| price_h4 | delta_quoted_effective_spread_2y | stock_tightness | 0.001221 | 0.001297 | 0.3465 | 10433 |
