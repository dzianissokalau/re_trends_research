-- Postcode join coverage by transaction year.
-- Purpose: quantify whether current NSPL postcode geography is adequate for historical sales.
WITH ppd AS (
  SELECT
    EXTRACT(YEAR FROM date) AS transaction_year,
    UPPER(REGEXP_REPLACE(COALESCE(postcode, ''), r'\s+', '')) AS postcode_compact
  FROM `re-trends.re_trends.land_registry_price_paid_transactions`
  WHERE date >= DATE '2001-01-01'
),
joined AS (
  SELECT
    p.transaction_year,
    p.postcode_compact,
    g.postcode_compact AS matched_postcode_compact,
    g.lad_code,
    g.country_code
  FROM ppd p
  LEFT JOIN `re-trends.re_trends.dim_postcode_geography` g
    ON p.postcode_compact = g.postcode_compact
)
SELECT
  transaction_year,
  COUNT(*) AS transaction_count,
  COUNTIF(postcode_compact != '') AS transaction_with_postcode_count,
  COUNTIF(matched_postcode_compact IS NOT NULL) AS postcode_matched_count,
  COUNTIF(lad_code LIKE 'E%') AS england_lad_matched_count,
  SAFE_DIVIDE(COUNTIF(matched_postcode_compact IS NOT NULL), COUNT(*)) AS postcode_match_rate,
  SAFE_DIVIDE(COUNTIF(lad_code LIKE 'E%'), COUNT(*)) AS england_lad_match_rate
FROM joined
GROUP BY transaction_year
ORDER BY transaction_year;
