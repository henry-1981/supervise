# Statistical Techniques for Regulatory Data

Statistical methods appropriate for medical device regulatory submissions.

## Descriptive Statistics

### Measures of Central Tendency

**Mean (Arithmetic Average):**
- Use: Continuous normally distributed data
- Formula: Sum of values divided by count
- Example: Average device performance measurement
- Limitation: Sensitive to outliers

**Median (50th Percentile):**
- Use: Skewed data or ordinal data
- Interpretation: Middle value when data sorted
- Example: Median time to adverse event
- Advantage: Robust to outliers

**Mode:**
- Use: Categorical data or discrete data
- Interpretation: Most frequently occurring value
- Example: Most common adverse event type

### Measures of Dispersion

**Standard Deviation (SD):**
- Use: Continuous data variability
- Interpretation: Average distance from mean
- Reporting: Mean ± SD
- Example: Device measurement variability

**Range:**
- Use: Data spread (minimum to maximum)
- Limitation: Sensitive to outliers

**Interquartile Range (IQR):**
- Use: Robust measure of spread
- Calculation: Q3 - Q1 (75th percentile - 25th percentile)
- Use with: Median for skewed data

**Coefficient of Variation (CV):**
- Use: Compare variability across different scales
- Formula: (SD / Mean) × 100%
- Example: Process capability assessment

---

## Inferential Statistics

### Confidence Intervals

**Purpose:** Estimate population parameters with uncertainty quantification.

**95% Confidence Interval for Mean:**
- Interpretation: 95% confident true mean lies within interval
- Formula: Mean ± (1.96 × SE) for large samples
- Reporting: "Mean = 25.3 (95% CI: 23.1, 27.5)"

**Confidence Interval Interpretation:**
- Narrow CI: Precise estimate
- Wide CI: Uncertain estimate, larger sample needed
- Does not overlap with comparison: Significant difference

### Hypothesis Testing

**Null Hypothesis (H0):** No difference or no effect
**Alternative Hypothesis (H1):** Difference or effect exists

**P-value Interpretation:**
- p < 0.05: Reject null hypothesis (typical threshold)
- p ≥ 0.05: Fail to reject null hypothesis
- p < 0.01: Strong evidence against null hypothesis

**Type I and Type II Errors:**
- Type I Error (α): False positive, rejecting true null hypothesis
- Type II Error (β): False negative, failing to reject false null hypothesis
- Power (1 - β): Probability of detecting true effect

---

## Common Statistical Tests

### Comparing Two Groups

**Independent Samples t-Test:**
- Use: Compare means of two independent groups
- Assumptions: Normality, equal variances
- Example: Compare device performance vs predicate device
- Reporting: t(df) = value, p = value

**Paired Samples t-Test:**
- Use: Compare means of paired observations
- Example: Before vs after measurements on same patients
- Reporting: t(df) = value, p = value

**Mann-Whitney U Test (Wilcoxon Rank Sum Test):**
- Use: Non-parametric alternative to independent t-test
- When: Data not normally distributed or ordinal
- Example: Compare adverse event severity scores

**Chi-Square Test:**
- Use: Compare proportions or categorical data
- Example: Compare adverse event rates between groups
- Reporting: χ²(df) = value, p = value

### Comparing Multiple Groups

**One-Way ANOVA:**
- Use: Compare means across 3+ independent groups
- Assumptions: Normality, equal variances
- Post-hoc: Tukey HSD or Bonferroni for pairwise comparisons

**Kruskal-Wallis Test:**
- Use: Non-parametric alternative to one-way ANOVA
- When: Data not normally distributed

---

## Clinical Data-Specific Techniques

### Survival Analysis

**Kaplan-Meier Survival Curves:**
- Use: Time-to-event data (device failure, adverse events)
- Output: Survival probability over time
- Censoring: Handles patients lost to follow-up
- Reporting: Median survival time with 95% CI

**Cox Proportional Hazards Model:**
- Use: Assess effect of covariates on survival
- Output: Hazard ratio (HR) with 95% CI
- Interpretation: HR > 1 indicates increased risk
- Example: Effect of patient age on device failure

### Equivalence and Non-Inferiority Testing

**Equivalence Testing:**
- Purpose: Demonstrate new device is equivalent to predicate
- Method: Two one-sided tests (TOST)
- Margin: Pre-specified equivalence margin
- Conclusion: Reject null hypothesis if CI within margin

**Non-Inferiority Testing:**
- Purpose: Demonstrate new device is not worse than predicate
- Margin: Maximum acceptable difference
- Conclusion: Lower bound of CI > -margin

---

## Sample Size Determination

### Power Analysis

**Key Parameters:**
- Effect size (Cohen's d, difference in means)
- Significance level (α, typically 0.05)
- Power (1 - β, typically 0.80 or 0.90)
- Sample size (n)

**Sample Size Formula (Two-Sample t-Test):**

n = 2 × (Zα/2 + Zβ)² × (σ² / δ²)

Where:
- Zα/2: Critical value for significance level
- Zβ: Critical value for power
- σ: Standard deviation
- δ: Effect size (meaningful difference)

**Regulatory Considerations:**
- Justify effect size based on clinical significance
- Document assumptions (SD, effect size, dropout rate)
- Include sensitivity analysis for assumptions

---

## Post-Market Surveillance Statistics

### Adverse Event Rate Calculation

**Event Rate per Patient-Year:**

Rate = (Number of events) / (Total patient-years of exposure)

**95% Confidence Interval for Rate:**

Use Poisson distribution for rare events or exact binomial for proportions.

**Trend Analysis:**

- Control charts: Detect shifts or trends over time
- Statistical process control: Identify out-of-control signals
- Moving averages: Smooth fluctuations, reveal trends

---

## Risk-Benefit Analysis Statistics

### Risk-Benefit Ratio

**Calculation:**

Risk-Benefit Ratio = (Probability of Harm × Severity) / (Probability of Benefit × Magnitude)

**Interpretation:**
- Ratio < 1: Benefits outweigh risks
- Ratio > 1: Risks outweigh benefits
- Ratio ~ 1: Requires detailed evaluation

**Number Needed to Treat (NNT):**

NNT = 1 / (Event rate in control - Event rate in treatment)

Interpretation: Number of patients to treat for one additional good outcome.

**Number Needed to Harm (NNH):**

NNH = 1 / (Adverse event rate in treatment - Adverse event rate in control)

Interpretation: Number of patients treated for one additional harm.

---

## Statistical Assumptions and Diagnostics

### Normality Testing

**Shapiro-Wilk Test:**
- Null hypothesis: Data is normally distributed
- p < 0.05: Reject normality assumption

**Q-Q Plot (Quantile-Quantile Plot):**
- Visual assessment of normality
- Points on line: Approximately normal
- Deviations from line: Non-normal

### Homogeneity of Variance

**Levene's Test:**
- Null hypothesis: Variances are equal
- p < 0.05: Reject equal variance assumption
- Use if planning t-test or ANOVA

---

## Reporting Statistical Results

### Standard Reporting Format

**Descriptive Statistics:**
- Continuous: Mean ± SD or Median (IQR)
- Categorical: n (%)

**Hypothesis Tests:**
- Test statistic, degrees of freedom, p-value
- Example: "t(48) = 2.34, p = 0.023"

**Effect Sizes:**
- Always report effect size with hypothesis tests
- Cohen's d for t-tests
- Odds ratio or risk ratio for categorical data

**Confidence Intervals:**
- Always report 95% CI with estimates
- Example: "Mean difference = 3.2 (95% CI: 1.1, 5.3)"

---

## Common Statistical Pitfalls

**Multiple Comparisons:**
- Problem: Increased Type I error with multiple tests
- Solution: Bonferroni correction or false discovery rate control

**Post-hoc Analyses:**
- Problem: Data-driven hypothesis testing inflates Type I error
- Solution: Pre-specify analyses, label post-hoc as exploratory

**Interpreting Non-Significance:**
- Wrong: "No difference exists"
- Correct: "No statistically significant difference detected"
- Consider: Power, effect size, clinical significance

**P-value Misinterpretation:**
- Wrong: "Probability that null hypothesis is true"
- Correct: "Probability of observing data (or more extreme) if null hypothesis is true"

---

Version: 1.0.0
Last Updated: 2026-02-09
