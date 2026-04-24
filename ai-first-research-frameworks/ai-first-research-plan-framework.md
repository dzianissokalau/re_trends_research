# AI-First Economic Research Plan Framework

This framework is designed for AI-driven economics quantitative research and forecasting. It is not a framework for producing commentary about research. Its purpose is to create research plans that can lead to useful forecasts, decision tools, risk signals, causal estimates, policy insight, and investment or operational decisions.

The framework should be used by an AI research agent before execution begins. The agent should use it to transform a broad economic topic into a decision-grade research plan with clear novelty, credible data use, validation standards, and actionability.

## Core Standard

Every research plan must satisfy three standards:

1. **Novelty**: The project should produce insight that is not already obvious from existing literature, public dashboards, or basic descriptive statistics.
2. **Clarity**: The research question, data, method, validation path, and output must be understandable before modeling begins.
3. **Actionability**: The output should be capable of changing an economic decision, forecast, allocation, policy, monitoring process, or risk assessment.

The AI should reject or redesign any plan that is interesting but unlikely to influence decisions.

## 1. Start From A Decision, Not A Topic

A weak starting point is:

> Study housing affordability trends.

A strong starting point is:

> Estimate which UK local authorities are most likely to experience affordability stress over the next 12 months, and identify the variables that could change investment, lending, or policy decisions.

For every proposed research idea, the AI must define:

- **Decision maker**: investor, policymaker, lender, developer, local authority, household, regulator, central bank analyst, or business operator.
- **Decision type**: allocate capital, price risk, target intervention, forecast demand, detect stress, evaluate policy, monitor leading indicators, or plan capacity.
- **Decision horizon**: nowcast, 3 months, 12 months, 3 years, or structural long term.
- **Decision output**: ranking, probability, scenario, threshold alert, elasticity estimate, causal estimate, forecast distribution, or monitoring score.
- **Cost of being wrong**: false positives, false negatives, delayed action, misallocation, missed turning points, or reputational risk.

The AI should reject any idea that cannot name a plausible decision that could change.

## 2. Literature And Prior Research Map

The AI should use literature to identify the frontier, not to pad a report.

For each topic, the AI should extract:

- Main economic mechanisms already established.
- Known empirical findings.
- Known failures, weak assumptions, or disputed results.
- Data sources used in prior work.
- Methods used in prior work.
- Forecast horizons attempted.
- Geographies and populations studied.
- Practical limitations of prior research.
- Areas where prior work is stale, low frequency, non-local, descriptive, or not linked to decisions.

The AI should summarize the literature frontier with these questions:

```text
What is already known?
What is still uncertain?
What do existing studies fail to predict, explain, or operationalize?
Where could our warehouse data create an advantage?
What would be genuinely new?
```

Novelty should be judged against actual prior work, not against the AI's intuition.

## 3. Data Asset Inventory

The framework treats data as a strategic advantage. Before proposing methods, the AI should inspect or request metadata about available warehouse data and relevant public sources.

For every relevant dataset, record:

- Table or source name.
- Geographic coverage.
- Time coverage.
- Update frequency.
- Granularity.
- Unit of observation.
- Join keys.
- Missingness.
- Known quality issues.
- Historical revisions.
- Publication lag.
- Licensing or usage constraints.
- Whether the data was available at prediction time.

Each research plan should classify data into:

- **Core outcome data**: the variable to explain, forecast, rank, or estimate.
- **Leading indicators**: variables available before the outcome.
- **Structural covariates**: slow-moving local, sectoral, household, or firm characteristics.
- **Shock variables**: rates, inflation, policy changes, energy costs, migration, employment, credit, taxation, or supply shocks.
- **Validation data**: independent sources for checking results.
- **External enrichment data**: public datasets worth acquiring.

For forecasting work, the AI must explicitly distinguish between data available at prediction time and data only known later.

## 4. Novelty Engine

The AI should search for several forms of novelty. A project does not need to be novel in every dimension, but it should be meaningfully novel in at least two.

Potential sources of novelty:

- **New decision framing**: turning a broad issue into an actionable risk signal or decision tool.
- **New data linkage**: joining datasets that are rarely combined.
- **Higher frequency**: producing monthly, weekly, or real-time indicators where prior work is annual or quarterly.
- **Local granularity**: local authority, postcode sector, neighborhood, school catchment, travel-to-work area, or market segment.
- **Forward-looking design**: predicting future stress, demand, or turning points rather than describing the past.
- **Heterogeneity**: identifying which places, households, firms, sectors, or cohorts behave differently.
- **Mechanism testing**: separating income, credit, supply, rates, expectations, and policy channels.
- **Early warning indicators**: detecting changes before headline data confirms them.
- **Scenario usefulness**: estimating outcomes under plausible macro, policy, or market shocks.
- **Operational deployment**: creating repeatable monitoring rather than a one-off report.

Each idea should receive a novelty score:

```text
Novelty from question: 0-5
Novelty from data: 0-5
Novelty from method: 0-5
Novelty from granularity or frequency: 0-5
Novelty from decision usefulness: 0-5
```

The AI should explain the specific novelty claim in one paragraph.

## 5. Research Question Design

The AI should convert broad topics into precise research questions.

Each question must specify:

- Outcome variable.
- Population, sector, or geography.
- Time period.
- Forecast horizon or causal estimand.
- Comparison group or benchmark.
- Economic mechanism.
- Decision relevance.
- Expected deliverable.

Forecasting question format:

```text
Can we forecast [outcome] for [unit] over [horizon] using [leading indicators], and identify [actionable segment, risk, or driver] better than [baseline]?
```

Causal question format:

```text
What is the effect of [shock, policy, or exposure] on [outcome] for [population or geography], through [mechanism], relative to [counterfactual], over [time horizon]?
```

Monitoring question format:

```text
Can we build a repeatable indicator that detects [risk or opportunity] for [unit] earlier than [existing source or official release], with acceptable false-positive and false-negative rates?
```

## 6. Hypothesis And Mechanism Map

Before modeling, the AI should create an economic mechanism map.

For each project, define:

- Expected causal channels.
- Confounders.
- Lag structure.
- Feedback loops.
- Measurement error risks.
- Expected signs of relationships.
- Alternative explanations.
- Variables needed to distinguish mechanisms.

Example:

```text
Interest rates -> mortgage affordability -> transaction volumes -> house price pressure
Wage growth -> household income -> affordability resilience
Rental inflation -> deposit constraints -> first-time buyer demand
Planning constraints -> housing supply elasticity -> local price sensitivity
```

The AI should represent the mechanism as a structured table or DAG before selecting models.

## 7. Method Selection

The method should follow the research task. The AI must separate forecasting, causal inference, descriptive measurement, and scenario analysis.

### Forecasting

Include:

- Naive baseline.
- Seasonal or historical average baseline.
- Classical benchmark such as ARIMA, VAR, panel regression, or dynamic factor model.
- ML benchmark such as regularized regression, random forest, or gradient boosting.
- Hierarchical or Bayesian model where geography, sparsity, or uncertainty justify it.
- Ensemble forecast where multiple models contribute distinct signal.
- Probabilistic forecast, not only point forecast.

The complex model only earns its place if it beats simple baselines out of sample or produces materially better decision insight.

### Causal Inference

Consider:

- Difference-in-differences.
- Event study.
- Synthetic control.
- Instrumental variables.
- Regression discontinuity.
- Panel fixed effects.
- Matching or weighting.
- Sensitivity analysis for unobserved confounding.

The AI must state the identifying assumption and how it will be challenged.

### Scenario And Stress Testing

Consider:

- Elasticity estimation.
- Counterfactual simulation.
- Microsimulation.
- Regional or sectoral stress testing.
- Macro-to-local transmission models.
- Forecast distributions under alternative assumptions.

Scenario work must state which assumptions are empirical estimates and which are imposed.

## 8. Validation And Quality Gates

Every research plan should include pre-defined tests before execution begins.

### Forecast Validation

Use:

- Rolling-origin backtests.
- Out-of-sample evaluation windows.
- Leakage checks.
- Comparison to naive, seasonal, and expert baselines.
- Accuracy by geography, regime, subgroup, and time horizon.
- Calibration of uncertainty intervals.
- Turning-point detection performance.
- Stability across data revisions.
- Degradation tests under missing or delayed inputs.

### Causal Validation

Use:

- Pre-trend tests.
- Placebo tests.
- Robustness to controls.
- Alternative specifications.
- Sensitivity to geography and time definitions.
- Spillover checks.
- Falsification outcomes.
- External validity discussion.

### General Research Quality

Require:

- Data lineage.
- Reproducible queries and code.
- Versioned datasets.
- Missing-data treatment.
- Clear assumptions.
- Human review of surprising results.
- Red-team critique before publication or deployment.

## 9. Actionability Layer

The AI must translate results into a decision artifact.

Possible final artifacts:

- Risk ranking.
- Forecast dashboard.
- Early warning indicator.
- Scenario table.
- Investment screen.
- Policy targeting map.
- Lending risk signal.
- Market turning-point monitor.
- Local area opportunity score.
- Confidence bands and uncertainty labels.
- Scheduled monitoring pipeline.

Every research plan should include a "so what" table:

```text
Finding | Confidence | Decision implication | Who should act | Timing | Risk
```

The research is not complete until the AI can explain what a decision maker might do differently.

## 10. Prioritization Score

Before execution, each candidate project should be scored out of 100:

```text
Decision impact: 20
Novelty: 15
Data advantage: 15
Feasibility: 15
Forecast or identification credibility: 15
Actionability: 10
Timeliness: 5
Reusability as monitoring system: 5
```

Reject or redesign projects with:

- No clear decision user.
- Mostly descriptive output.
- No credible data advantage.
- Weak validation path.
- Interesting topic but unclear action.
- High complexity with low practical value.
- No clear output beyond a written report.

## 11. Required Research Plan Template

The AI should produce every research plan using this structure:

```text
1. Title
2. Decision Use Case
3. Main Research Question
4. Why This Matters Now
5. Literature Frontier
6. Novelty Claim
7. Available Warehouse Data
8. Public Data To Acquire
9. Economic Mechanism
10. Hypotheses
11. Methodology
12. Forecast, Causal, Monitoring, Or Scenario Design
13. Validation Strategy
14. Expected Outputs
15. Actionability
16. Risks And Limitations
17. Quality Gates
18. Execution Plan
19. Success Criteria
20. Kill Criteria
```

## 12. Success Criteria

A research project should be considered successful only if it meets most of these criteria:

- It answers a decision-relevant question.
- It uses data that is appropriate for the decision horizon.
- It has a clear novelty claim.
- It beats a credible baseline or provides a defensible causal estimate.
- It exposes uncertainty rather than hiding it.
- It identifies heterogeneity, thresholds, or leading indicators that matter.
- It can be repeated, monitored, or updated.
- It produces an output that a decision maker can use.

## 13. Kill Criteria

The AI should stop or redesign a project if:

- The model cannot beat a naive or seasonal baseline.
- The data linkage is too noisy.
- A key variable is unavailable at decision time.
- Results are unstable across backtests.
- The causal design relies on implausible assumptions.
- The output is mainly descriptive and does not support a decision.
- The expected artifact is only a narrative report with no operational use.
- No clear user action emerges.

Kill criteria should be defined before execution to avoid over-investing in weak ideas.

## 14. AI Operating Principles

The AI research agent should follow these rules:

1. Start from decisions, not topics.
2. Prefer measurable questions over broad narratives.
3. Separate forecasting, causal inference, descriptive measurement, and scenario analysis.
4. Always benchmark against simple models.
5. Treat data availability timing as sacred.
6. Make uncertainty visible.
7. Search for non-obvious heterogeneity.
8. Use literature to locate the frontier, not to decorate the report.
9. Prioritize repeatable systems over one-off reports.
10. Convert findings into decision artifacts.
11. State assumptions before modeling.
12. Challenge results that look too clean.
13. Consider the cost of false positives and false negatives.
14. Prefer research that can influence a real economic decision.

## 15. AI Execution Workflow

The AI should run the planning process in this order:

```text
1. Clarify the decision and user.
2. Map existing literature and prior research.
3. Inventory warehouse and public data.
4. Identify possible novelty.
5. Formulate precise research questions.
6. Build the mechanism map.
7. Select method candidates and baselines.
8. Define validation tests.
9. Define the decision artifact.
10. Score the project.
11. Define success and kill criteria.
12. Produce the final research plan.
```

The final plan should be concise enough to execute but detailed enough that another AI or analyst could reproduce the reasoning.

## Mission Statement

Produce economically grounded, empirically credible, novel, and decision-useful research plans that exploit our data advantage and can survive out-of-sample validation, methodological scrutiny, and real-world use.
