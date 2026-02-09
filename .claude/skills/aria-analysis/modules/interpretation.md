# Result Interpretation Guidelines

Standards for interpreting and reporting regulatory data analysis results.

## Statistical vs Clinical Significance

### Statistical Significance

**Definition:** The probability that observed results occurred by chance alone is low (typically p < 0.05).

**Interpretation:**
- p < 0.05: Statistically significant result
- p < 0.01: Highly statistically significant
- p < 0.001: Very highly statistically significant

**Limitations:**
- Large sample size can make trivial differences statistically significant
- Does not indicate practical or clinical importance
- Does not measure effect magnitude

### Clinical Significance

**Definition:** The magnitude of effect is large enough to be clinically meaningful or relevant to patient outcomes.

**Assessment Criteria:**
- Effect size (Cohen's d, odds ratio, risk ratio)
- Clinical importance to patient health or outcomes
- Practical relevance for device performance
- Cost-benefit considerations

**Examples:**

Statistically significant but not clinically significant:
- Device accuracy differs by 0.1% (p = 0.01) but acceptable tolerance is ±5%

Clinically significant but not statistically significant:
- 20% reduction in adverse events (p = 0.08) due to underpowered study

Both statistically and clinically significant:
- 50% reduction in device-related infections (p < 0.001)

---

## Effect Size Interpretation

### Cohen's d (Standardized Mean Difference)

| Effect Size | Cohen's d | Interpretation |
|-------------|-----------|----------------|
| Small | 0.2 | Subtle difference |
| Medium | 0.5 | Moderate difference |
| Large | 0.8 | Substantial difference |
| Very Large | > 1.2 | Highly substantial difference |

### Odds Ratio (OR) and Risk Ratio (RR)

| Value | Interpretation |
|-------|----------------|
| OR or RR = 1.0 | No association |
| OR or RR > 1.0 | Increased odds/risk |
| OR or RR < 1.0 | Decreased odds/risk |
| OR or RR > 2.0 or < 0.5 | Strong association |

**Example:**
- OR = 2.5 for adverse events: 2.5 times higher odds of adverse event compared to control

---

## Regulatory Interpretation Context

### FDA 510(k) Substantial Equivalence

**Statistical Evidence:**
- Performance data comparable to predicate device
- Non-inferiority or equivalence testing
- Confidence intervals overlap or demonstrate equivalence

**Clinical Evidence:**
- Similar safety profile
- Similar effectiveness outcomes
- Technological characteristics differences do not affect safety/effectiveness

**Interpretation:**
- Statistical equivalence supports but does not guarantee regulatory acceptance
- Clinical relevance of differences must be justified
- Totality of evidence considered

### EU MDR Clinical Evaluation

**Clinical Data Requirements:**
- Sufficient clinical evidence of safety and performance
- State of the art consideration
- Benefit-risk ratio favorable

**Interpretation:**
- Clinical significance of outcomes emphasized
- Comparison with alternative treatments
- Long-term safety and performance data valued

---

## Safety Signal Interpretation

### Adverse Event Rate Interpretation

**Baseline Comparison:**
- Compare observed rate with pre-market clinical data
- Compare with predicate device (if applicable)
- Compare with literature or device class norms

**Statistical Process Control:**
- Upper control limit (UCL) = Mean + 3×SD
- Signal: Rate exceeds UCL
- Trend: 7+ consecutive points above/below mean

**Clinical Significance:**
- Severity of adverse events
- Frequency and recurrence
- Preventability and mitigation options

**Regulatory Action Thresholds:**
- Serious adverse events: Always investigate
- Rate increase > 50%: Likely requires investigation
- New unexpected events: Evaluate and report

---

## Result Presentation Standards

### Tables

**Table 1: Baseline Characteristics**

| Characteristic | Treatment (n=XX) | Control (n=XX) | p-value |
|----------------|------------------|----------------|---------|
| Age, mean ± SD | XX.X ± X.X | XX.X ± X.X | X.XX |
| Sex, n (%) | | | |
| Male | XX (XX%) | XX (XX%) | X.XX |
| Female | XX (XX%) | XX (XX%) | |

**Table 2: Primary Endpoint Analysis**

| Endpoint | Treatment | Control | Difference (95% CI) | p-value |
|----------|-----------|---------|---------------------|---------|
| Success Rate, n (%) | XX (XX%) | XX (XX%) | XX% (XX%, XX%) | X.XX |

### Figures

**Figure Requirements:**
- Clear axis labels with units
- Legends for multiple data series
- Error bars (SD, SE, or CI) for means
- Statistical significance indicators (*, **, ***)
- High resolution for regulatory submission

**Common Figure Types:**
- Bar charts: Compare means across groups
- Box plots: Show distributions and outliers
- Kaplan-Meier curves: Survival or time-to-event
- Control charts: Trend analysis over time

---

## Reporting Checklist

### Required Elements

- [ ] Analysis objective clearly stated
- [ ] Data sources and sample size reported
- [ ] Statistical methods described
- [ ] Assumptions stated and verified
- [ ] Descriptive statistics presented
- [ ] Hypothesis test results (if applicable)
- [ ] Effect sizes reported
- [ ] Confidence intervals provided
- [ ] Statistical significance assessed
- [ ] Clinical significance evaluated
- [ ] Limitations clearly stated
- [ ] Regulatory implications discussed

### Interpretation Statement Template

```markdown
## Interpretation

### Statistical Findings
[Summarize statistical test results, p-values, confidence intervals]

### Clinical Significance
[Assess magnitude of effect, clinical relevance, patient impact]

### Regulatory Context
[Link findings to regulatory requirements, predicate comparison, acceptance criteria]

### Limitations
[State study limitations, assumptions, potential biases]

### Conclusions
[Provide evidence-based conclusions supported by analysis]
```

---

## Common Interpretation Pitfalls

**Overinterpreting Non-Significant Results:**
- Wrong: "No difference exists between groups"
- Correct: "No statistically significant difference was detected (p = 0.12)"
- Consider: Study may be underpowered to detect true difference

**Ignoring Clinical Significance:**
- Wrong: Relying solely on p-value
- Correct: Evaluate effect size and clinical meaningfulness
- Example: p = 0.001 does not guarantee clinically important difference

**Confusing Association with Causation:**
- Wrong: "X causes Y" based on observational study
- Correct: "X is associated with Y" or "X is correlated with Y"
- RCT: Stronger evidence for causation

**Multiple Comparisons Without Adjustment:**
- Problem: Increased false positive rate
- Solution: Bonferroni correction or FDR control
- Label exploratory analyses appropriately

**Cherry-Picking Favorable Results:**
- Problem: Selective reporting inflates evidence
- Solution: Report all pre-specified analyses
- Label post-hoc analyses as exploratory

---

## Sensitivity Analysis

### Purpose

Assess robustness of results to assumptions and analytical choices.

### Common Sensitivity Analyses

**Missing Data:**
- Complete case analysis (exclude missing)
- Best-case scenario (impute favorable outcomes)
- Worst-case scenario (impute unfavorable outcomes)
- Multiple imputation

**Outlier Handling:**
- Include all data
- Exclude outliers
- Winsorize (cap extreme values)

**Subgroup Analysis:**
- Analyze by age group, sex, disease severity
- Pre-specify subgroups to avoid data dredging
- Use interaction tests for subgroup differences

**Analysis Method:**
- Parametric vs non-parametric tests
- Different adjustment for covariates
- Alternative statistical models

### Reporting Sensitivity Analysis

```markdown
## Sensitivity Analysis

### Missing Data
Primary analysis used complete case analysis (n=XX).
Sensitivity analysis using multiple imputation (n=XX) yielded consistent results:
- Primary analysis: Effect = XX (95% CI: XX, XX), p = X.XX
- Multiple imputation: Effect = XX (95% CI: XX, XX), p = X.XX

### Conclusion
Results are robust to handling of missing data.
```

---

Version: 1.0.0
Last Updated: 2026-02-09
