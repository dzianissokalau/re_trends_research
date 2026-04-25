-- Quarterly mortgage shock series.
-- Purpose: compare effective new-business rates, quoted fixed rates, and quoted-effective spreads.
WITH effective AS (
  SELECT
    DATE_TRUNC(month, QUARTER) AS quarter,
    AVG(IF(series_code = 'Z6JM', effective_rate_percent, NULL)) AS effective_new_business_z6jm,
    AVG(IF(series_code = 'BJ95', effective_rate_percent, NULL)) AS effective_new_business_bj95
  FROM `re-trends.re_trends.mortgage_rates_monthly_effective`
  WHERE series_code IN ('Z6JM', 'BJ95')
    AND business_flow_type = 'new_business'
    AND month >= DATE '2004-01-01'
  GROUP BY quarter
),
quoted AS (
  SELECT
    DATE_TRUNC(month, QUARTER) AS quarter,
    AVG(IF(series_code = 'BV34', quoted_rate_percent, NULL)) AS quoted_2y_75_ltv_bv34,
    AVG(IF(series_code = 'BV42', quoted_rate_percent, NULL)) AS quoted_5y_75_ltv_bv42
  FROM `re-trends.re_trends.mortgage_rates_monthly_quoted`
  WHERE series_code IN ('BV34', 'BV42')
    AND occupancy_type = 'owner_occupied'
    AND month >= DATE '2004-01-01'
  GROUP BY quarter
),
combined AS (
  SELECT
    COALESCE(e.quarter, q.quarter) AS quarter,
    COALESCE(e.effective_new_business_z6jm, e.effective_new_business_bj95) AS effective_new_business_headline,
    e.effective_new_business_z6jm,
    e.effective_new_business_bj95,
    q.quoted_2y_75_ltv_bv34,
    q.quoted_5y_75_ltv_bv42,
    q.quoted_2y_75_ltv_bv34 - COALESCE(e.effective_new_business_z6jm, e.effective_new_business_bj95) AS quoted_effective_spread_2y
  FROM effective e
  FULL OUTER JOIN quoted q
    USING (quarter)
)
SELECT
  *,
  effective_new_business_headline - LAG(effective_new_business_headline) OVER (ORDER BY quarter) AS delta_effective_new_business_headline,
  quoted_2y_75_ltv_bv34 - LAG(quoted_2y_75_ltv_bv34) OVER (ORDER BY quarter) AS delta_quoted_2y_75_ltv,
  quoted_5y_75_ltv_bv42 - LAG(quoted_5y_75_ltv_bv42) OVER (ORDER BY quarter) AS delta_quoted_5y_75_ltv,
  quoted_effective_spread_2y - LAG(quoted_effective_spread_2y) OVER (ORDER BY quarter) AS delta_quoted_effective_spread_2y
FROM combined
WHERE quarter >= DATE '2015-01-01'
ORDER BY quarter;
