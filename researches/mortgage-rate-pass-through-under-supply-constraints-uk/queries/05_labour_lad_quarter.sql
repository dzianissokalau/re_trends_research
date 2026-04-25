-- Quarterly LAD labour-market stress control.
-- Purpose: add claimant-rate controls to price and transaction models.
SELECT
  DATE_TRUNC(month, QUARTER) AS quarter,
  area_code AS lad_code,
  ANY_VALUE(area_name) AS lad_name,
  AVG(claimant_rate) AS claimant_rate,
  AVG(claimant_count) AS claimant_count
FROM `re-trends.re_trends.fact_area_labour_month`
WHERE month >= DATE '2015-01-01'
  AND area_code LIKE 'E%'
  AND is_headline_total
GROUP BY quarter, lad_code
ORDER BY quarter, lad_code;
