-- Annual LAD supply and stock-tightness panel.
-- Purpose: construct predetermined and time-varying local supply/vacancy proxies.
SELECT
  COALESCE(s.year, h.year) AS year,
  COALESCE(s.lad_code, h.lad_code) AS lad_code,
  COALESCE(s.lad_name, h.lad_name) AS lad_name,
  s.reference_period_label,
  s.reference_period_start_date,
  s.reference_period_end_date,
  s.net_additional_dwellings,
  s.housing_completions,
  s.demolitions,
  h.dwelling_stock_total,
  h.vacant_dwellings,
  h.long_term_vacant_dwellings,
  h.vacancy_rate,
  h.long_term_vacancy_rate,
  SAFE_DIVIDE(s.net_additional_dwellings, h.dwelling_stock_total) AS net_additions_rate,
  SAFE_DIVIDE(s.housing_completions, h.dwelling_stock_total) AS completions_rate,
  SAFE_DIVIDE(s.demolitions, h.dwelling_stock_total) AS demolitions_rate
FROM `re-trends.re_trends.fact_lad_supply_year` s
FULL OUTER JOIN `re-trends.re_trends.fact_lad_housing_stock_year` h
  ON s.lad_code = h.lad_code
  AND s.year = h.year
WHERE COALESCE(s.year, h.year) >= 2001
ORDER BY year, lad_code;
