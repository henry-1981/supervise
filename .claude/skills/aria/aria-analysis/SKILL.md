---
name: aria-analysis
description: >
  Data analysis methodology for ARIA business documents. Provides statistical
  techniques, result interpretation guidelines, and data visualization standards
  for regulatory and technical documentation. Used by expert-analyst for
  quantitative analysis, trend identification, and evidence generation.
license: Apache-2.0
compatibility: Designed for Claude Code
user-invocable: true
metadata:
  version: "1.0.0"
  category: "domain"
  status: "active"
  updated: "2025-02-09"
  modularized: "true"
  tags: "aria, analysis, data, statistics"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords: ["analysis", "statistics", "data", "quantitative", "trends"]
  agents: ["expert-analyst"]
  phases: ["brief", "execute"]
  languages: ["en", "ko"]
---

# ARIA Data Analysis Guide

## Overview

This skill provides standardized methodologies for data analysis in regulatory and technical documentation within the ARIA ecosystem.

## Analysis Framework

### Step 1: Data Preparation

#### Data Collection
- Define data requirements
- Identify data sources
- Establish collection protocols
- Document provenance

#### Data Cleaning
- Remove duplicates
- Handle missing values
- Correct outliers
- Standardize formats

#### Data Validation
- Verify data integrity
- Check for consistency
- Validate against source
- Document assumptions

### Step 2: Analysis Selection

#### Descriptive Statistics
- **Purpose**: Summarize data characteristics
- **Measures**: Mean, median, mode, standard deviation
- **Use Case**: Baseline understanding

#### Inferential Statistics
- **Purpose**: Draw conclusions from samples
- **Methods**: Hypothesis testing, confidence intervals
- **Use Case**: Generalizing findings

#### Trend Analysis
- **Purpose**: Identify patterns over time
- **Methods**: Time series, regression
- **Use Case**: Performance monitoring

#### Comparative Analysis
- **Purpose**: Compare groups or conditions
- **Methods**: T-tests, ANOVA
- **Use Case**: Impact assessment

### Step 3: Analysis Execution

#### Statistical Software
- Use validated tools
- Document parameters
- Maintain audit trail
- Preserve raw data

#### Quality Assurance
- Peer review analysis
- Verify assumptions
- Check robustness
- Document limitations

## Statistical Techniques

### Common Tests

| Test | Purpose | Data Type | Sample Size |
|------|---------|-----------|-------------|
| T-test (independent) | Compare two groups | Continuous | n >= 30 |
| T-test (paired) | Compare related measures | Continuous | n >= 30 |
| ANOVA | Compare multiple groups | Continuous | n >= 30 per group |
| Chi-square | Test independence | Categorical | n >= 5 per cell |
| Correlation | Measure relationship | Continuous | n >= 30 |
| Regression | Predict outcomes | Mixed | n >= 10 per predictor |

### Effect Sizes

#### Interpretation Guidelines
- **Small**: d = 0.2, r = 0.1
- **Medium**: d = 0.5, r = 0.3
- **Large**: d = 0.8, r = 0.5

#### Calculation Methods
- Cohen's d for mean differences
- Pearson's r for correlations
- Odds ratios for categorical data

### Confidence Intervals

#### Standard Levels
- **90% CI**: Moderate certainty
- **95% CI**: High certainty (standard)
- **99% CI**: Very high certainty

#### Interpretation
- Range containing true population parameter
- Narrower intervals = more precise estimates
- Non-overlapping CIs indicate significant differences

## Result Interpretation

### Statistical Significance

#### P-value Interpretation
- **p < 0.001**: Very strong evidence
- **p < 0.01**: Strong evidence
- **p < 0.05**: Moderate evidence (standard threshold)
- **p >= 0.05**: Insufficient evidence

#### Common Pitfalls
- P-hacking: Multiple testing without correction
- P-value misunderstanding: Does not measure effect size
- Statistical vs practical significance

### Practical Significance

#### Consider Context
- Effect size magnitude
- Real-world impact
- Cost-benefit analysis
- Stakeholder requirements

#### Decision Framework
1. Is the result statistically significant?
2. Is the effect size meaningful?
3. Are the results reproducible?
4. Do they inform decision-making?

## Data Visualization

### Chart Selection

| Purpose | Chart Type | When to Use |
|---------|-----------|-------------|
| Distribution | Histogram | Show data spread |
| Comparison | Bar chart | Compare categories |
| Trend | Line chart | Show changes over time |
| Relationship | Scatter plot | Show correlation |
| Composition | Pie chart | Show proportions (max 5 categories) |
| Distribution | Box plot | Show outliers and spread |

### Visualization Standards

#### Formatting Guidelines
- Clear titles and labels
- Consistent color schemes
- Appropriate scales
- Legend included when needed
- Data source cited

#### Accessibility
- Colorblind-friendly palettes
- High contrast ratios
- Text annotations for key points
- Alternative text descriptions

### Reporting Results

#### Structure
```markdown
## Analysis Results

### Methods
[Brief description of analysis approach]

### Findings
[Present results clearly]

### Statistical Summary
| Metric | Value | 95% CI | p-value |
|--------|-------|--------|---------|
| [Metric] | [Value] | [CI] | [p] |

### Interpretation
[What results mean in context]

### Visualization
[Include relevant charts]
```

## Quality Assurance

### Analysis Checklist

#### Before Analysis
- [ ] Data properly cleaned
- [ ] Assumptions verified
- [ ] Appropriate test selected
- [ ] Sample size adequate
- [ ] Documentation complete

#### After Analysis
- [ ] Results validated
- [ ] Calculations verified
- [ ] Interpretation reviewed
- [ ] Limitations documented
- [ ] Conclusions justified

### Common Errors to Avoid

1. **Data dredging**: Testing many hypotheses without correction
2. **Confusing correlation with causation**: Relationship != causation
3. **Ignoring assumptions**: Violating test prerequisites
4. **Overfitting**: Models too complex for data
5. **Cherry-picking**: Selectively reporting results

## Documentation Requirements

### Analysis Report Template

```markdown
# Data Analysis Report

## 1. Methods

### 1.1 Data Sources
[Describe data provenance]

### 1.2 Preparation
[Document cleaning and validation steps]

### 1.3 Statistical Tests
[Justify test selection]

## 2. Results

### 2.1 Descriptive Statistics
[Summary statistics table]

### 2.2 Inferential Statistics
[Test results with p-values and CIs]

### 2.3 Visualizations
[Charts and figures]

## 3. Interpretation

### 3.1 Key Findings
[Main conclusions]

### 3.2 Limitations
[Study constraints]

### 3.3 Recommendations
[Actionable insights]

## 4. Appendix

### 4.1 Raw Data
[Link to data source]

### 4.2 Analysis Code
[Link to analysis scripts]

### 4.3 Supplementary Results
[Additional analyses]
```

## Best Practices

1. **Plan before analyzing**: Define hypotheses upfront
2. **Document everything**: Maintain complete audit trail
3. **Validate assumptions**: Check test prerequisites
4. **Report transparently**: Include all relevant results
5. **Interpret cautiously**: Acknowledge limitations
