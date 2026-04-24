# AI-First Research Idea Evaluation Template

> Disclaimer: This document was generated with AI and has received only limited human review. It may contain errors or omissions and should be independently verified before use.

## Purpose

- This file converts the old CSV scorecard into a Markdown-first template that is easier to review, discuss, and edit in research planning sessions.
- Use it together with [ai-first-research-idea-evaluation-framework.md](./ai-first-research-idea-evaluation-framework.md).
- Keep one filled section per idea when evaluating new research candidates.

## Worked Example

### Core Idea Fields

| Field | Value |
| --- | --- |
| `idea_id` | `EXAMPLE-001` |
| `title` | `Mortgage-rate pass-through under supply constraints` |
| `theme` | `Finance, housing, and macro` |
| `decision_user` | `Market analyst` |
| `decision_improved` | `Interpret local house-price sensitivity to national rate shocks` |
| `outcome_variable` | `Real local house-price growth` |
| `main_mechanism` | `National mortgage shocks capitalise more strongly where supply and vacancy buffers are tight` |
| `primary_geography` | `LAD|MSOA` |
| `primary_time_grain` | `Quarterly` |
| `internal_tables` | `source_land_registry_price_paid`, `dim_postcode_geography`, `fact_lad_supply_year`, `fact_lad_housing_stock_year`, `mortgage_rates_monthly_effective`, `mortgage_rates_monthly_quoted`, `inflation_monthly_core` |
| `open_source_sources_needed` | None required for baseline |
| `candidate_design` | `Distributed-lag interaction panel` |
| `main_failure_risk` | `Historical postcode join stability and annual-to-quarterly constraint alignment` |

### Scoring

| Block | Field | Score |
| --- | --- | --- |
| Impact | `impact_decision_leverage` | `13` |
| Impact | `impact_economic_exposure` | `9` |
| Impact | `impact_timing_actionability` | `8` |
| Impact | `impact_edge` | `8` |
| Impact | `impact_total_45` | `38` |
| Feasibility | `feasibility_internal_data_readiness` | `11` |
| Feasibility | `feasibility_open_source_augmentability` | `7` |
| Feasibility | `feasibility_alignment` | `4` |
| Feasibility | `feasibility_design_credibility` | `4` |
| Feasibility | `feasibility_execution_cost_inverse` | `3` |
| Feasibility | `feasibility_total_35` | `29` |
| Strategic fit | `strategic_reusable_asset_creation` | `8` |
| Strategic fit | `strategic_forecast_monitoring_value` | `6` |
| Strategic fit | `strategic_communication_clarity` | `5` |
| Strategic fit | `strategic_total_20` | `19` |
| Overall | `total_score_100` | `86` |

### Decision

| Field | Value |
| --- | --- |
| `stage_1_pass` | `yes` |
| `priority_bucket` | `build_now` |
| `next_step` | `Write full research plan and define baseline panel` |

## Blank Template

### Core Idea Fields

| Field | Value |
| --- | --- |
| `idea_id` | `TEMPLATE-001` |
| `title` |  |
| `theme` |  |
| `decision_user` |  |
| `decision_improved` |  |
| `outcome_variable` |  |
| `main_mechanism` |  |
| `primary_geography` |  |
| `primary_time_grain` |  |
| `internal_tables` |  |
| `open_source_sources_needed` |  |
| `candidate_design` |  |
| `main_failure_risk` |  |

### Scoring

| Block | Field | Score |
| --- | --- | --- |
| Impact | `impact_decision_leverage` | `0` |
| Impact | `impact_economic_exposure` | `0` |
| Impact | `impact_timing_actionability` | `0` |
| Impact | `impact_edge` | `0` |
| Impact | `impact_total_45` | `0` |
| Feasibility | `feasibility_internal_data_readiness` | `0` |
| Feasibility | `feasibility_open_source_augmentability` | `0` |
| Feasibility | `feasibility_alignment` | `0` |
| Feasibility | `feasibility_design_credibility` | `0` |
| Feasibility | `feasibility_execution_cost_inverse` | `0` |
| Feasibility | `feasibility_total_35` | `0` |
| Strategic fit | `strategic_reusable_asset_creation` | `0` |
| Strategic fit | `strategic_forecast_monitoring_value` | `0` |
| Strategic fit | `strategic_communication_clarity` | `0` |
| Strategic fit | `strategic_total_20` | `0` |
| Overall | `total_score_100` | `0` |

### Decision

| Field | Value |
| --- | --- |
| `stage_1_pass` | `no` |
| `priority_bucket` |  |
| `next_step` |  |
