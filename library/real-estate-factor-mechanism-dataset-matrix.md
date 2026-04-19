# Real Estate Factor, Mechanism, Dataset, And Starter Paper Matrix

## Scope
- This is a practical companion to `real-estate-price-dynamics-research-library.md`.
- For a ranked set of research ideas that turns these factor paths into concrete quantitative projects, see `../ideas/real-estate-price-mechanism-ranked-ideas.md`.
- It is UK-first and England-focused where possible, because that is the most natural fit for your current research direction and data stack.
- It is designed for explanatory variables. For target variables such as sale prices, price indices, rents, listings, and stock, keep using your main real-estate datasets separately.
- Dataset links were checked on April 11, 2026.
- This version also adds several high-trust factors that recur across core housing theory and top empirical work, beyond the original set of nine.

## Matrix

| Factor | Likely mechanism into real-estate prices | Best datasets to start with | Best starter papers |
| --- | --- | --- | --- |
| Income | Higher permanent income raises housing demand, borrowing capacity, bid-rents, and willingness to pay for amenities. | [ONS small area income estimates](https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/datasets/smallareaincomeestimatesformiddlelayersuperoutputareasenglandandwales)<br>[HMRC Survey of Personal Incomes](https://www.gov.uk/government/collections/personal-incomes-statistics)<br>[Nomis ASHE resident and workplace earnings](https://www.nomisweb.co.uk/articles/1320.aspx) | Hendershott and Abraham (1992)<br>Roback (1982)<br>Geng (2018) |
| Wealth distribution | More unequal wealth and credit access can shift demand toward specific market segments, especially prime areas or the low end under easier credit. | [ONS Wealth and Assets Survey](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/incomeandwealth/datasets/wealthandassetssurvey)<br>[HMRC personal wealth statistics](https://www.gov.uk/government/statistics/personal-wealth-statistics-by-gender-and-region-2020-to-2022)<br>[HM Land Registry Price Paid Data](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads) | Määttänen and Terviö (2014)<br>Landvoigt, Piazzesi, and Schneider (2015) |
| Crime | Crime raises local disamenity and risk, reduces neighborhood desirability, and can weaken both prices and liquidity. | [Police.uk open crime data](https://data.police.uk/)<br>[Home Office police-recorded crime open data tables](https://www.gov.uk/government/statistics/police-recorded-crime-open-data-tables)<br>[ONS crime and justice data](https://www.ons.gov.uk/peoplepopulationandcommunity/crimeandjustice) | Gibbons (2004)<br>Linden and Rockoff (2008) |
| Schools | Better school quality is capitalized into nearby house prices through parental demand, sorting, and catchment scarcity. | [Compare school performance](https://www.compare-school-performance.service.gov.uk/)<br>[Get Information About Schools](https://get-information-schools.service.gov.uk/)<br>[Department for Education statistics and data](https://www.gov.uk/government/organisations/department-for-education/about/statistics) | Black (1999)<br>Nguyen-Hoang and Yinger (2011) |
| Property characteristics and housing quality | Floor area, age, type, tenure, condition, and energy efficiency are capitalized directly through hedonic pricing and indirectly through operating costs, mortgageability, and segment sorting. | [Energy Performance of Buildings data](https://epc.opendatacommunities.org/)<br>[HM Land Registry Price Paid Data](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads)<br>[English Housing Survey: local authority housing stock condition modelling, 2023](https://www.gov.uk/government/statistics/english-housing-survey-local-authority-housing-stock-condition-modelling-2023) | Rosen (1974)<br>Sirmans, Macpherson, and Zietz (2005)<br>Glaeser, Gyourko, and Saks (2005) |
| Property supply | Supply elasticity, planning constraints, land scarcity, and new-build flows shape both level effects and boom-bust amplitude. | [ONS house building statistics](https://www.gov.uk/government/collections/house-building-statistics)<br>[DLUHC dwelling stock estimates](https://www.gov.uk/government/collections/dwelling-stock-including-vacants)<br>[Energy Performance of Buildings data](https://epc.opendatacommunities.org/) | Saiz (2010)<br>Hilber and Vermeulen (2016)<br>Glaeser, Gyourko, and Saks (2005) |
| Demographics and household formation | Age structure, cohort size, household formation, and one-person-household growth shift underlying housing demand over time and across places. | [ONS population estimates for England and Wales](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/bulletins/populationestimatesforenglandandwales/latest)<br>[ONS household projections for England](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationprojections/datasets/householdprojectionsforengland)<br>[ONS population projections for local authorities by single year of age and sex](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationprojections/datasets/localauthoritiesinenglandz1) | Mankiw and Weil (1989)<br>Green and Hendershott (1996)<br>Geng (2018) |
| Population growth and migration | Inflows raise local demand, alter buyer composition, and change pressure on both rents and sale prices; outflows can relieve pressure. | [ONS internal migration in England and Wales](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/internalmigrationinenglandandwales/detailedinternalmigrationestimates20222021and2023localauthorities)<br>[ONS subnational population projections for England](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationprojections/bulletins/subnationalpopulationprojectionsforengland/2022based)<br>[ONS household projections for England](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationprojections/datasets/householdprojectionsforengland) | Roback (1982)<br>Hsieh and Moretti (2019)<br>Olney and Thompson (2024) |
| Accessibility and transport | Better access to jobs, stations, and services lowers generalized travel costs and raises willingness to pay for location. | [DfT journey time statistics](https://www.gov.uk/government/collections/journey-time-statistics)<br>[DfT journey time data tables](https://www.gov.uk/government/statistical-data-sets/journey-time-statistics-data-tables-jts)<br>[ONS method used to travel to work](https://www.ons.gov.uk/datasets/TS061) | Roback (1982)<br>Gibbons and Machin (2005) |
| Environmental quality and climate risk | Pollution, flooding, and long-run climate risk alter desirability, insurance costs, financing, and sometimes market liquidity before they fully hit prices. | [Environment Agency Flood Map for Planning - Flood Zones](https://environment.data.gov.uk/dataset/04532375-a198-476e-985e-0579a0a11b47)<br>[DEFRA UK-AIR data archive](https://uk-air.defra.gov.uk/data/)<br>[Land use change statistics](https://www.gov.uk/government/collections/land-use-change-statistics) | Chay and Greenstone (2005)<br>Beltran, Maddison, and Elliott (2019)<br>Bernstein, Gustafson, and Lewis (2019) |
| Unemployment | Higher unemployment weakens effective demand, tightens credit access, reduces transactions, and can amplify downturns through labor-market stress. | [Nomis model-based unemployment](https://www.nomisweb.co.uk/datasets/umb)<br>[Nomis claimant count](https://www.nomisweb.co.uk/)<br>[ONS labour market statistics](https://www.ons.gov.uk/employmentandlabourmarket) | Gan and Zhang (2006)<br>Liu, Miao, and Zha (2016) |
| Mortgage rates | Lower mortgage rates reduce user cost and monthly payment burdens, increase leverage capacity, and can raise price-to-income and price-to-rent ratios. | [Bank of England interest and exchange rates data](https://www.bankofengland.co.uk/boeapps/database/Bank-Rate.asp)<br>[Bank of England effective interest rates](https://www.bankofengland.co.uk/statistics/details/further-details-about-effective-interest-rates)<br>[Bank of England money and credit statistics](https://www.bankofengland.co.uk/statistics/money-and-credit) | Poterba (1984)<br>Himmelberg, Mayer, and Sinai (2005)<br>Ahearne et al. (2005) |
| Credit availability and lending standards | Looser underwriting, higher loan-to-value or loan-to-income multiples, and broader credit supply can raise prices even when headline rates move little. | [FCA mortgage lending statistics](https://www.fca.org.uk/data/mortgage-lending-statistics)<br>[Bank of England Credit Conditions Survey 2026 Q1](https://www.bankofengland.co.uk/credit-conditions-survey/2026/2026-q1)<br>[Bank of England money and credit statistics](https://www.bankofengland.co.uk/statistics/money-and-credit) | Mian and Sufi (2009)<br>Favara and Imbs (2015)<br>Adelino, Schoar, and Severino (2012) |
| Inflation | Inflation changes real borrowing costs, tax interactions, expected returns, construction costs, and affordability pressure. | [ONS CPIH and CPI](https://www.ons.gov.uk/economy/inflationandpriceindices)<br>[ONS producer price inflation and construction cost indicators](https://www.ons.gov.uk/economy/inflationandpriceindices) | Poterba (1980)<br>Hendershott and Abraham (1992)<br>Ahearne et al. (2005) |
| Taxes and transaction costs | Property taxes, stamp duties, and housing-tax subsidies affect user cost, mobility, and the capitalization of local fiscal conditions into prices. | [Council Tax levels set by local authorities in England 2026 to 2027](https://www.gov.uk/government/statistics/council-tax-levels-set-by-local-authorities-in-england-2026-to-2027/council-tax-levels-set-by-local-authorities-in-england-2026-to-2027)<br>[Annual Stamp Tax Statistics](https://www.gov.uk/government/statistics/uk-stamp-tax-statistics)<br>[Council Tax statistics collection](https://www.gov.uk/government/collections/council-tax-statistics) | Poterba (1980)<br>Poterba (1984)<br>Hendershott and Slemrod (1982) |
| Construction costs and replacement cost | Higher building costs can raise replacement values, slow supply response, and change the persistence and overshooting of price cycles. | [ONS construction output price indices](https://www.ons.gov.uk/businessindustryandtrade/constructionindustry/datasets/interimconstructionoutputpriceindices)<br>[ONS construction output price indices QMI](https://www.ons.gov.uk/businessindustryandtrade/constructionindustry/methodologies/constructionoutputpriceindicesopisqmi)<br>[Land use change statistics](https://www.gov.uk/government/collections/land-use-change-statistics) | Hendershott and Abraham (1992)<br>Capozza, Hendershott, Mack, and Mayer (2002)<br>Potter and Syverson (2025) |
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

### Property characteristics and housing quality
- Best first pick: EPC data if you need broad public coverage of property type, floor area, age band, and energy efficiency.
- Add Price Paid Data when you need transaction-level type, tenure, and new-build flags for hedonic or repeat-sale style work.
- Use the English Housing Survey condition modelling when the question is dwelling quality at local-authority scale rather than individual property attributes.

### Property supply
- Best first pick: DLUHC dwelling stock estimates for stock level and tenure composition.
- Add house building statistics when you want flow measures such as starts, completions, or net additions.
- Add EPC counts when you want a practical high-frequency proxy for market activity, stock quality, or upgrade intensity.

### Demographics and household formation
- Best first pick: ONS household projections when the question is medium-run demand pressure.
- Use population estimates and projections when age structure or cohort size is central to the mechanism.
- Keep in mind that demographic pressure matters more where supply is inelastic.

### Population growth and migration
- Best first pick: ONS internal migration data for local inflow and outflow patterns.
- Use subnational population projections when you want a planning-style medium-term demand view.
- Treat migration as both a cause and a response: high prices can also deter in-migration.

### Accessibility and transport
- Best first pick: DfT journey time statistics when you need a practical area-level accessibility measure.
- Use ONS travel-to-work data when the mechanism is commuting structure rather than pure station proximity.
- Accessibility often interacts with wages and agglomeration, not just with commuting convenience.

### Environmental quality and climate risk
- Best first pick: Environment Agency flood zones for physical risk screening.
- Use UK-AIR when pollution or air quality is the relevant environmental channel.
- Watch for non-price responses first: lower turnover, weaker liquidity, or insurance frictions can show up before large sale-price discounts.

### Unemployment
- Best first pick: Nomis model-based unemployment for cleaner local unemployment rates.
- Use claimant count when you want timelier monthly stress indicators.
- If the analysis is about household distress, pair unemployment with arrears, approvals, or transaction volumes where available.

### Mortgage rates
- Best first pick: Bank of England effective mortgage rates when you want realized borrowing costs.
- Use quoted household mortgage rates when you care about the offer-side channel facing new borrowers.
- Pair mortgage rates with approvals and loan-to-income data when you want the financing channel rather than only the valuation channel.

### Credit availability and lending standards
- Best first pick: FCA mortgage lending statistics when you want LTV, income-multiple, and commitment detail.
- Use the Bank of England Credit Conditions Survey when the mechanism is tightening or loosening credit supply.
- This factor is especially important in boom-bust work because it is not the same thing as mortgage rates.

### Inflation
- Best first pick: CPIH if you want the ONS headline inflation series that includes owner-occupier housing costs.
- Add construction-cost or producer-price indicators when the channel is replacement cost or development feasibility.
- Keep real and nominal versions of housing outcomes separate because inflation can distort naive price-growth comparisons.

### Taxes and transaction costs
- Best first pick: Council Tax levels for recurring local tax burden and Annual Stamp Tax Statistics for transaction-tax intensity.
- Use this factor when the research question is about user cost, lock-in, or capitalization of fiscal differences.
- Stamp duties often affect transactions first and prices second, especially over short windows.

### Construction costs and replacement cost
- Best first pick: ONS construction output price indices for a public-sector measure of construction inflation.
- Use this factor more cautiously in highly supply-constrained places, where land scarcity and regulation can dominate build-cost effects.
- Replacement-cost logic is strongest in markets where new supply can realistically respond.

### Important events
- Best first pick: Electoral Commission data for elections and referendums with clean dates.
- Use ACLED when you want conflict or geopolitical event timing.
- Use the UK economic policy uncertainty index when the main channel is uncertainty rather than a discrete local event.

## Recommended Starter Bundles

### If the question is "Why did local prices move differently across areas?"
- Income: ONS small area income estimates
- Crime: Police.uk
- Schools: Compare school performance plus GIAS
- Property characteristics: EPC plus Price Paid Data
- Supply: dwelling stock estimates plus house building statistics
- Accessibility: DfT journey time statistics
- Starter papers: Rosen (1974), Black (1999), Gibbons (2004), Gibbons and Machin (2005), Saiz (2010), Hilber and Vermeulen (2016)

### If the question is "Why did affordability worsen?"
- Income: ONS small area income estimates or ASHE
- Mortgage rates: Bank of England effective mortgage rates
- Credit availability: FCA mortgage lending statistics
- Inflation: CPIH
- Supply: dwelling stock estimates
- Taxes: Council Tax levels and Stamp Tax statistics
- Starter papers: Poterba (1980), Poterba (1984), Himmelberg, Mayer, and Sinai (2005), Geng (2018), Hendershott and Abraham (1992)

### If the question is "Why are structurally expensive places staying expensive?"
- Migration: ONS internal migration data
- Accessibility: DfT journey time statistics
- Supply: planning applications plus dwelling stock
- Environment: flood risk where relevant
- Starter papers: Roback (1982), Saiz (2010), Hilber and Vermeulen (2016), Gyourko, Mayer, and Sinai (2013), Hsieh and Moretti (2019)

### If the question is "How do shocks and crises affect housing markets?"
- Important events: Electoral Commission or ACLED plus UK EPU
- Unemployment: Nomis model-based unemployment
- Mortgage rates: Bank of England effective rates and approvals
- Credit availability: Credit Conditions Survey
- Inflation: ONS CPI energy components
- Environment: Environment Agency flood zones when the shock is physical rather than policy-driven
- Starter papers: Choi (2023), Balcilar et al. (2021), Mian and Sufi (2009), Favara and Imbs (2015), Liu, Miao, and Zha (2016)

## Notes And Caveats
- Wealth distribution is the hardest item on your list to measure locally in the UK. Expect to mix national or regional wealth data with local proxy variables.
- Important events work best when you define the channel up front: uncertainty, financing, migration, physical damage, or energy-cost shock.
- Online listing datasets can be compositionally biased. If you use portal or classifieds data, benchmark their coverage against transactions, stock, or survey sources before treating them as representative of the whole market.
- Property-level composition effects matter. Average prices can move because the quality mix of homes sold changed, not only because constant-quality prices changed.
- Schools and crime are often highly localized. Align them spatially as tightly as possible to the property.
- Supply works best with both stock and flow measures. Stock alone misses new-building dynamics; flow alone misses inherited scarcity.
- Demographic and migration variables are often slow-moving, so they are usually more useful for explaining level differences than month-to-month price moves.
- Credit standards and taxes frequently affect transactions and liquidity before they show up strongly in average sale prices.
- Environmental risk often interacts with insurance and planning rules, so simple distance or exposure variables can miss important institutional channels.
- Expectations and speculative demand matter in the bubble literature, but clean UK-first public datasets are weaker here than for income, supply, credit, or local amenities; if you later go deeper on bubbles, build price-to-rent, momentum, and turnover proxies explicitly.
