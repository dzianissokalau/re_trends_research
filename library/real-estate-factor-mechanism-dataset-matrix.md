# Real Estate Factor, Mechanism, Dataset, And Starter Paper Matrix

## Scope
- This is a practical companion to `real-estate-price-dynamics-research-library.md`.
- It is UK-first and England-focused where possible, because that is the most natural fit for your current research direction and data stack.
- It is designed for explanatory variables. For target variables such as sale prices, price indices, rents, listings, and stock, keep using your main real-estate datasets separately.
- Dataset links were checked on April 11, 2026.

## Matrix

| Factor | Likely mechanism into real-estate prices | Best datasets to start with | Best starter papers |
| --- | --- | --- | --- |
| Income | Higher permanent income raises housing demand, borrowing capacity, bid-rents, and willingness to pay for amenities. | [ONS small area income estimates](https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/datasets/smallareaincomeestimatesformiddlelayersuperoutputareasenglandandwales)<br>[HMRC Survey of Personal Incomes](https://www.gov.uk/government/collections/personal-incomes-statistics)<br>[Nomis ASHE resident and workplace earnings](https://www.nomisweb.co.uk/articles/1320.aspx) | Hendershott and Abraham (1992)<br>Roback (1982)<br>Geng (2018) |
| Wealth distribution | More unequal wealth and credit access can shift demand toward specific market segments, especially prime areas or the low end under easier credit. | [ONS Wealth and Assets Survey](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/incomeandwealth/datasets/wealthandassetssurvey)<br>[HMRC personal wealth statistics](https://www.gov.uk/government/statistics/personal-wealth-statistics-by-gender-and-region-2020-to-2022)<br>[HM Land Registry Price Paid Data](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads) | Määttänen and Terviö (2014)<br>Landvoigt, Piazzesi, and Schneider (2015) |
| Crime | Crime raises local disamenity and risk, reduces neighborhood desirability, and can weaken both prices and liquidity. | [Police.uk open crime data](https://data.police.uk/)<br>[Home Office police-recorded crime open data tables](https://www.gov.uk/government/statistics/police-recorded-crime-open-data-tables)<br>[ONS crime and justice data](https://www.ons.gov.uk/peoplepopulationandcommunity/crimeandjustice) | Gibbons (2004)<br>Linden and Rockoff (2008) |
| Schools | Better school quality is capitalized into nearby house prices through parental demand, sorting, and catchment scarcity. | [Compare school performance](https://www.compare-school-performance.service.gov.uk/)<br>[Get Information About Schools](https://get-information-schools.service.gov.uk/)<br>[Department for Education statistics and data](https://www.gov.uk/government/organisations/department-for-education/about/statistics) | Black (1999)<br>Nguyen-Hoang and Yinger (2011) |
| Property supply | Supply elasticity, planning constraints, land scarcity, and new-build flows shape both level effects and boom-bust amplitude. | [ONS house building statistics](https://www.gov.uk/government/collections/house-building-statistics)<br>[DLUHC dwelling stock estimates](https://www.gov.uk/government/collections/dwelling-stock-including-vacants)<br>[Energy Performance of Buildings data](https://epc.opendatacommunities.org/) | Saiz (2010)<br>Hilber and Vermeulen (2016)<br>Glaeser, Gyourko, and Saks (2005) |
| Unemployment | Higher unemployment weakens effective demand, tightens credit access, reduces transactions, and can amplify downturns through labor-market stress. | [Nomis model-based unemployment](https://www.nomisweb.co.uk/datasets/umb)<br>[Nomis claimant count](https://www.nomisweb.co.uk/)<br>[ONS labour market statistics](https://www.ons.gov.uk/employmentandlabourmarket) | Gan and Zhang (2006)<br>Liu, Miao, and Zha (2016) |
| Mortgage rates | Lower mortgage rates reduce user cost and monthly payment burdens, increase leverage capacity, and can raise price-to-income and price-to-rent ratios. | [Bank of England interest and exchange rates data](https://www.bankofengland.co.uk/boeapps/database/Bank-Rate.asp)<br>[Bank of England effective interest rates](https://www.bankofengland.co.uk/statistics/details/further-details-about-effective-interest-rates)<br>[Bank of England money and credit statistics](https://www.bankofengland.co.uk/statistics/money-and-credit) | Poterba (1984)<br>Himmelberg, Mayer, and Sinai (2005)<br>Ahearne et al. (2005) |
| Inflation | Inflation changes real borrowing costs, tax interactions, expected returns, construction costs, and affordability pressure. | [ONS CPIH and CPI](https://www.ons.gov.uk/economy/inflationandpriceindices)<br>[ONS producer price inflation and construction cost indicators](https://www.ons.gov.uk/economy/inflationandpriceindices) | Poterba (1980)<br>Hendershott and Abraham (1992)<br>Ahearne et al. (2005) |
| Important events | Elections, wars, crises, and policy shocks move prices through uncertainty, sentiment, financing conditions, migration, and energy-cost channels. | [Electoral Commission elections and referendums](https://www.electoralcommission.org.uk/elections-and-referendums)<br>[ACLED conflict event data](https://acleddata.com/data-export-tool/)<br>[FRED UK economic policy uncertainty index](https://fred.stlouisfed.org/series/GBRINDEPUQISMEI)<br>[ONS CPI energy components](https://www.ons.gov.uk/economy/inflationandpriceindices) | Choi (2023)<br>Balcilar et al. (2021) |

## How I Would Use This In Practice

### Income
- Best first pick: ONS small area income estimates if you want area-level household resources.
- Use HMRC personal incomes when you want tax-based income tails or richer top-end coverage.
- Use ASHE when the mechanism is wages or labor-market earning power rather than disposable household income.

### Wealth distribution
- Best first pick: ONS Wealth and Assets Survey for national and regional wealth structure.
- Main caveat: official UK wealth data are much weaker at fine geography than income data.
- Practical workaround: combine Wealth and Assets Survey or HMRC wealth statistics with local proxies from Price Paid Data to capture distributional exposure by area.

### Crime
- Best first pick: Police.uk for micro geography and monthly frequency.
- Use Home Office tables if you need more stable long panels or force-level comparability.
- Merge carefully: offense definitions and recording practices can change over time.

### Schools
- Best first pick: Compare school performance for outcomes and accountability metrics.
- Use GIAS for identifiers, openings, closures, type changes, and school characteristics.
- For catchment-style work, preserve school-year timing so that performance measures line up with listing or sale dates.

### Property supply
- Best first pick: DLUHC dwelling stock estimates for stock level and tenure composition.
- Add house building statistics when you want flow measures such as starts, completions, or net additions.
- Add EPC counts when you want a practical high-frequency proxy for market activity, stock quality, or upgrade intensity.

### Unemployment
- Best first pick: Nomis model-based unemployment for cleaner local unemployment rates.
- Use claimant count when you want timelier monthly stress indicators.
- If the analysis is about household distress, pair unemployment with arrears, approvals, or transaction volumes where available.

### Mortgage rates
- Best first pick: Bank of England effective mortgage rates when you want realized borrowing costs.
- Use quoted household mortgage rates when you care about the offer-side channel facing new borrowers.
- Pair mortgage rates with approvals and loan-to-income data when you want the financing channel rather than only the valuation channel.

### Inflation
- Best first pick: CPIH if you want the ONS headline inflation series that includes owner-occupier housing costs.
- Add construction-cost or producer-price indicators when the channel is replacement cost or development feasibility.
- Keep real and nominal versions of housing outcomes separate because inflation can distort naive price-growth comparisons.

### Important events
- Best first pick: Electoral Commission data for elections and referendums with clean dates.
- Use ACLED when you want conflict or geopolitical event timing.
- Use the UK economic policy uncertainty index when the main channel is uncertainty rather than a discrete local event.

## Recommended Starter Bundles

### If the question is "Why did local prices move differently across areas?"
- Income: ONS small area income estimates
- Crime: Police.uk
- Schools: Compare school performance plus GIAS
- Supply: dwelling stock estimates plus house building statistics
- Starter papers: Rosen (1974), Black (1999), Gibbons (2004), Saiz (2010), Hilber and Vermeulen (2016)

### If the question is "Why did affordability worsen?"
- Income: ONS small area income estimates or ASHE
- Mortgage rates: Bank of England effective mortgage rates
- Inflation: CPIH
- Supply: dwelling stock estimates
- Starter papers: Poterba (1984), Himmelberg, Mayer, and Sinai (2005), Geng (2018), Hendershott and Abraham (1992)

### If the question is "How do shocks and crises affect housing markets?"
- Important events: Electoral Commission or ACLED plus UK EPU
- Unemployment: Nomis model-based unemployment
- Mortgage rates: Bank of England effective rates and approvals
- Inflation: ONS CPI energy components
- Starter papers: Choi (2023), Balcilar et al. (2021), Mian and Sufi (2009), Liu, Miao, and Zha (2016)

## Notes And Caveats
- Wealth distribution is the hardest item on your list to measure locally in the UK. Expect to mix national or regional wealth data with local proxy variables.
- Important events work best when you define the channel up front: uncertainty, financing, migration, physical damage, or energy-cost shock.
- Schools and crime are often highly localized. Align them spatially as tightly as possible to the property.
- Supply works best with both stock and flow measures. Stock alone misses new-building dynamics; flow alone misses inherited scarcity.
