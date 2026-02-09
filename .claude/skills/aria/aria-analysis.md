---
name: aria-analysis
description: >
  Data analysis methodology for regulatory intelligence, including statistical techniques
  for regulatory data analysis, result interpretation guidelines, trend identification
  methods, and visualization recommendations for RA/QA professionals.
license: Apache-2.0
compatibility: Designed for Claude Code
allowed-tools: Read Grep Glob Bash mcp__claude_ai_Notion__notion-search mcp__claude_ai_Notion__notion-fetch mcp__sequential-thinking__sequentialthinking
user-invocable: true
metadata:
  version: "1.0.0"
  category: "domain"
  status: "active"
  updated: "2026-02-09"
  modularized: "false"
  tags: "analysis, statistics, trends, visualization, regulatory-data, data-interpretation"
  author: "ARIA Team"
  context: "Medical Device RA/QA data analysis and interpretation"
  agent: "expert-analyst"
  argument-hint: "Specify data source, analysis type, and output format"
  aliases: "data-analysis, statistical-analysis, trend-analysis"

# ARIA Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# ARIA Extension: Triggers
triggers:
  keywords: ["analyze", "statistics", "trend", "data", "interpretation", "visualization", "metrics", "correlation", "regression", "pattern"]
  agents: ["expert-analyst", "expert-regulatory", "expert-standards"]
  phases: ["execute"]
  languages: ["en"]
---

# ARIA Data Analysis Skill

## Purpose

Provides structured methodology for analyzing regulatory intelligence data, interpreting statistical results, identifying trends, and creating visualizations that support regulatory decision-making for medical devices.

## Core Principles

1. **Regulatory Context First**: All analysis must be grounded in regulatory requirements
2. **Data Integrity**: Maintain traceability from raw data to conclusions
3. **Statistical Validity**: Apply appropriate statistical methods for regulatory data
4. **Clear Communication**: Present findings in terms accessible to RA/QA professionals
5. **Evidence-Based**: Conclusions must be supported by quantitative analysis

## Analysis Methodology

### Phase 1: Data Preparation

**Data Collection Verification:**
- Confirm data source reliability (official regulatory databases, internal QMS, clinical data)
- Verify data completeness and currency
- Document any data limitations or exclusions

**Data Cleaning:**
- Identify and handle missing values
- Remove duplicates while maintaining audit trail
- Standardize formats (dates, device classifications, regulatory codes)
- Validate against source documents

**Data Structure Assessment:**
- Determine data type (time-series, categorical, numerical, mixed)
- Identify key variables and their relationships
- Assess sample size and statistical power

### Phase 2: Statistical Analysis

**Descriptive Statistics:**
- Central tendency measures (mean, median, mode)
- Dispersion measures (range, variance, standard deviation)
- Distribution analysis (normality tests, skewness, kurtosis)
- Frequency tables for categorical data

**Inferential Statistics:**
- Hypothesis testing appropriate to regulatory questions
- Confidence intervals for key metrics
- Correlation analysis for regulatory variables
- Regression analysis for trend prediction

**Regulatory-Specific Techniques:**
- Complaint trend analysis (Pareto charts, time series)
- Non-conformance pattern recognition
- CAPA effectiveness statistical evaluation
- Post-market surveillance signal detection
- Clinical outcome data analysis

### Phase 3: Result Interpretation

**Statistical Significance vs. Practical Significance:**
- Distinguish statistically significant results from regulatory impact
- Consider clinical relevance of statistical findings
- Assess effect sizes in regulatory context

**Regulatory Implication Assessment:**
- Map statistical findings to regulatory requirements
- Identify potential compliance risks or opportunities
- Consider regulatory precedent and historical context

**Uncertainty Communication:**
- Quantify and communicate confidence levels
- Document assumptions and limitations
- Identify areas requiring additional data

### Phase 4: Trend Identification

**Trend Detection Methods:**
- Time series analysis for regulatory changes over time
- Moving averages for complaint and adverse event trends
- Seasonality analysis for inspection findings
- Control charts for process monitoring

**Pattern Recognition:**
- Cluster analysis for similar regulatory issues
- Association rule mining for co-occurring non-conformities
- Root cause correlation patterns
- Geographical or facility-based patterns

**Predictive Analysis:**
- Trend extrapolation for resource planning
- Risk-based forecasting for compliance priorities
- Early warning indicators for regulatory issues

### Phase 5: Visualization

**Visualization Principles:**
- Choose chart types appropriate to data and audience
- Maintain regulatory context in all visualizations
- Use clear labeling and standardized formats
- Include statistical confidence indicators

**Recommended Chart Types:**

| Purpose | Chart Type | Regulatory Use Case |
|---------|-----------|-------------------|
| Trend over time | Line chart, Control chart | Complaint trends, submission timelines |
| Distribution | Histogram, Box plot | Review cycle times, response times |
| Comparison | Bar chart, Grouped bar | Multiple facilities, product lines |
| Composition | Stacked bar, Pie | Non-conformance categories |
| Correlation | Scatter plot, Heatmap | CAPA effectiveness vs. time |
| Frequency | Pareto chart | Complaint types, audit findings |

**Visualization Standards:**
- Include title, data source, date range
- Label axes with units and regulatory context
- Use consistent color schemes for similar data types
- Provide legend for all coded elements
- Indicate statistical significance where applicable

## Statistical Techniques Reference

### Descriptive Statistics

**Central Tendency:**
- Mean: Average value, sensitive to outliers
- Median: Middle value, robust to outliers
- Mode: Most frequent value, for categorical data

**Dispersion:**
- Range: Max - Min, simple spread measure
- Variance: Average squared deviation from mean
- Standard Deviation: Square root of variance, same units as data
- Interquartile Range (IQR): Q3 - Q1, robust spread measure

**Distribution:**
- Normal distribution: Bell curve, many statistical tests assume this
- Skewness: Asymmetry of distribution
- Kurtosis: Tailedness of distribution

### Inferential Statistics

**Hypothesis Testing:**
- Null hypothesis (H0): No effect or difference
- Alternative hypothesis (H1): Effect or difference exists
- P-value: Probability of observing results if H0 is true
- Significance level (alpha): Typically 0.05 for regulatory analysis

**Common Tests:**
- T-test: Compare two group means
- ANOVA: Compare three or more group means
- Chi-square: Test categorical variable independence
- Correlation: Measure linear relationship strength (-1 to +1)

**Confidence Intervals:**
- Range of values likely to contain true population parameter
- 95% CI: If repeated, 95% of intervals would contain true value
- Narrower intervals indicate more precise estimates

### Regression Analysis

**Linear Regression:**
- Simple linear: One predictor, one outcome
- Multiple linear: Multiple predictors, one outcome
- Output: Equation, R-squared (variance explained), coefficients

**Logistic Regression:**
- Outcome is binary (compliant/non-compliant)
- Output: Odds ratios, probability predictions

**Time Series:**
- Trend analysis over time
- Seasonality detection
- Forecasting future values

## Regulatory Data Types

### Complaint Data
- Analysis: Trend analysis, Pareto charts, correlation with product changes
- Key metrics: Complaint rate, time to resolution, repeat complaints
- Visualization: Line charts, Pareto charts, heat maps by product

### Non-Conformance Data
- Analysis: Pattern recognition, root cause correlation
- Key metrics: NC rate, type distribution, closure time
- Visualization: Bar charts, trend lines, control charts

### CAPA Data
- Analysis: Effectiveness assessment, time-to-completion
- Key metrics: CAPA opening rate, effectiveness verification, recurrence
- Visualization: Before/after comparisons, trend charts

### Audit Data
- Analysis: Finding patterns, scoring trends
- Key metrics: Finding count by category, severity distribution
- Visualization: Stacked bar charts, radar charts for audit areas

### Clinical Data
- Analysis: Outcome comparison, adverse event rates
- Key metrics: Success rates, complication rates, survival curves
- Visualization: Kaplan-Meier curves, forest plots for meta-analysis

### Submission Data
- Analysis: Cycle time analysis, approval rate trends
- Key metrics: Days to approval, query rate, approval rate
- Visualization: Box plots for cycle times, trend lines for rates

## Quality Assurance for Analysis

### Validation Checklist
- [ ] Data sources documented and verified
- [ ] Statistical methods appropriate for data type
- [ ] Assumptions stated and tested
- [ ] Results reproducible from documented methodology
- [ ] Limitations and uncertainties communicated
- [ ] Conclusions supported by quantitative evidence
- [ ] Visualizations accurately represent data
- [ ] Regulatory implications clearly stated

### Common Pitfalls to Avoid
- Over-interpreting small sample sizes
- Confusing statistical significance with practical importance
- Ignoring data limitations or biases
- Using inappropriate statistical tests
- Failing to document methodology
- Cherry-picking data to support conclusions
- Violating statistical assumptions without justification

## Integration with ARIA Workflow

### Brief Phase
- Identify analysis requirements from regulatory question
- Determine data availability and quality
- Select appropriate analytical methods

### Execute Phase
- Perform statistical analysis following methodology
- Create visualizations for key findings
- Interpret results in regulatory context

### Deliver Phase
- Present findings with clear regulatory implications
- Provide recommendations based on quantitative evidence
- Document methodology for audit trail

## Template References

When analysis is complete, integrate with:
- `aria-docs`: Create analysis reports
- `aria-templates`: Use standard analysis report formats
- `aria-knowledge`: Store validated analytical methods

## Notion Integration

Store analysis results in:
- Analysis database for reproducible research
- CAPA tracker for effectiveness analysis
- Risk register for quantitative risk assessments
- Knowledge base for validated analytical methods
