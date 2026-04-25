-- Main LAD-quarter completed-sale panel, post-2015.
-- Purpose: build real price and transaction outcomes for staged hypothesis tests.
WITH ppd AS (
  SELECT
    DATE_TRUNC(date, QUARTER) AS quarter,
    sold_price,
    property_type,
    estate_type,
    new_build,
    transaction_category,
    UPPER(REGEXP_REPLACE(COALESCE(postcode, ''), r'\s+', '')) AS postcode_compact
  FROM `re-trends.re_trends.land_registry_price_paid_transactions`
  WHERE date >= DATE '2015-01-01'
    AND sold_price BETWEEN 10000 AND 5000000
    AND transaction_category = 'standard'
),
joined AS (
  SELECT
    p.*,
    g.lad_code,
    g.lad_name,
    g.region_code
  FROM ppd p
  JOIN `re-trends.re_trends.dim_postcode_geography` g
    ON p.postcode_compact = g.postcode_compact
  WHERE g.lad_code LIKE 'E%'
),
panel AS (
  SELECT
    quarter,
    lad_code,
    ANY_VALUE(lad_name) AS lad_name,
    ANY_VALUE(region_code) AS region_code,
    COUNT(*) AS transaction_count,
    APPROX_QUANTILES(sold_price, 100)[OFFSET(50)] AS median_sold_price,
    AVG(LOG(sold_price)) AS mean_log_sold_price,
    SAFE_DIVIDE(COUNTIF(property_type = 'detached'), COUNT(*)) AS detached_share,
    SAFE_DIVIDE(COUNTIF(property_type = 'semi-detached'), COUNT(*)) AS semi_detached_share,
    SAFE_DIVIDE(COUNTIF(property_type = 'terraced'), COUNT(*)) AS terraced_share,
    SAFE_DIVIDE(COUNTIF(property_type = 'flat/maisonette'), COUNT(*)) AS flat_maisonette_share,
    SAFE_DIVIDE(COUNTIF(estate_type = 'freehold'), COUNT(*)) AS freehold_share,
    SAFE_DIVIDE(COUNTIF(new_build), COUNT(*)) AS new_build_share
  FROM joined
  GROUP BY quarter, lad_code
),
inflation AS (
  SELECT
    DATE_TRUNC(month, QUARTER) AS quarter,
    AVG(IF(series_code = 'L522', value, NULL)) AS cpih_index,
    AVG(IF(series_code = 'D7BT', value, NULL)) AS cpi_index
  FROM `re-trends.re_trends.inflation_monthly_core`
  WHERE series_code IN ('L522', 'D7BT')
    AND value_type = 'index'
    AND month >= DATE '2015-01-01'
  GROUP BY quarter
)
SELECT
  p.*,
  i.cpih_index,
  i.cpi_index,
  LOG(SAFE_DIVIDE(p.median_sold_price, i.cpih_index)) AS log_real_median_price_cpih,
  LOG(SAFE_DIVIDE(p.median_sold_price, i.cpi_index)) AS log_real_median_price_cpi
FROM panel p
LEFT JOIN inflation i
  USING (quarter)
ORDER BY p.quarter, p.lad_code;
