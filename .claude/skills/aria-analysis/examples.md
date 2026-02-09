# Analysis Examples for Common Regulatory Scenarios

Practical examples of data analysis for medical device regulatory submissions.

## Example 1: 510(k) Performance Comparison

### Scenario

Compare performance of new blood pressure monitor with predicate device.

### Data

- New device: n=100, mean systolic BP = 120.5 mmHg, SD = 15.2 mmHg
- Predicate device: n=100, mean systolic BP = 119.8 mmHg, SD = 14.8 mmHg
- Equivalence margin: ±5 mmHg

### Analysis

**Step 1: Descriptive Statistics**

| Device | n | Mean (mmHg) | SD (mmHg) | 95% CI |
|--------|---|-------------|-----------|---------|
| New | 100 | 120.5 | 15.2 | (117.5, 123.5) |
| Predicate | 100 | 119.8 | 14.8 | (116.8, 122.8) |

**Step 2: Equivalence Testing (TOST)**

- Difference: 0.7 mmHg
- 95% CI for difference: (-2.6, 4.0)
- Equivalence margin: ±5 mmHg
- Result: 95% CI entirely within ±5 mmHg margin

**Step 3: Interpretation**

Statistical Conclusion: New device is statistically equivalent to predicate device (p < 0.05 for both one-sided tests).

Clinical Conclusion: Performance difference of 0.7 mmHg is clinically insignificant for blood pressure measurement.

Regulatory Conclusion: Performance data supports substantial equivalence to predicate device.

---

## Example 2: Adverse Event Rate Analysis

### Scenario

Post-market surveillance data for implantable cardiac device over 12 months.

### Data

- Devices implanted: 500
- Total patient-years: 450 (accounting for loss to follow-up)
- Serious adverse events (SAE): 18
- Device-related SAE: 9

### Analysis

**Step 1: Calculate Event Rates**

Overall SAE rate = 18 / 450 = 0.04 events per patient-year = 4.0%

Device-related SAE rate = 9 / 450 = 0.02 events per patient-year = 2.0%

**Step 2: Confidence Intervals**

Using Poisson distribution for rare events:

Device-related SAE rate: 2.0% (95% CI: 0.9%, 3.8%)

**Step 3: Comparison with Pre-Market Data**

- Pre-market clinical study: 2.5% device-related SAE rate
- Post-market: 2.0% (95% CI: 0.9%, 3.8%)
- Interpretation: Post-market rate consistent with pre-market data (CIs overlap)

**Step 4: Trend Analysis**

| Quarter | SAE Count | Device-Years | Rate (%) |
|---------|-----------|--------------|----------|
| Q1 | 3 | 112.5 | 2.7 |
| Q2 | 2 | 112.5 | 1.8 |
| Q3 | 2 | 112.5 | 1.8 |
| Q4 | 2 | 112.5 | 1.8 |

No increasing trend observed (stable rates across quarters).

**Step 5: Interpretation**

Statistical Conclusion: Post-market SAE rate (2.0%) is consistent with pre-market rate (2.5%), no statistically significant increase.

Safety Conclusion: No safety signal detected. Device continues to demonstrate acceptable safety profile.

Regulatory Action: No immediate regulatory reporting required. Continue routine surveillance.

---

## Example 3: Clinical Study Sample Size Determination

### Scenario

Design clinical study to demonstrate new diagnostic device sensitivity is non-inferior to predicate.

### Assumptions

- Predicate device sensitivity: 85%
- Expected new device sensitivity: 88% (optimistic estimate)
- Non-inferiority margin: -5% (new device sensitivity should be no more than 5% lower than predicate)
- Significance level (α): 0.05 (one-sided)
- Power (1-β): 0.90

### Sample Size Calculation

Using formula for non-inferiority test of proportions:

n = (Zα + Zβ)² × [p1(1-p1) + p2(1-p2)] / (p1 - p2 - δ)²

Where:
- p1 = 0.88 (new device expected sensitivity)
- p2 = 0.85 (predicate sensitivity)
- δ = -0.05 (non-inferiority margin)
- Zα = 1.645 (one-sided α = 0.05)
- Zβ = 1.282 (power = 0.90)

Calculation:

n = (1.645 + 1.282)² × [0.88(0.12) + 0.85(0.15)] / (0.88 - 0.85 - (-0.05))²
n = (2.927)² × [0.1056 + 0.1275] / (0.08)²
n = 8.57 × 0.2331 / 0.0064
n ≈ 312

**Accounting for Dropout (10%):**

n_total = 312 / 0.90 ≈ 347

**Interpretation:**

Required sample size: 347 patients per group (or 347 total if paired comparison).

Justification: Sample size provides 90% power to demonstrate non-inferiority with 5% margin.

---

## Example 4: CAPA Effectiveness Analysis

### Scenario

Evaluate effectiveness of corrective action to reduce device labeling defects.

### Data

**Pre-CAPA (6 months):**
- Total production: 10,000 units
- Labeling defects: 150
- Defect rate: 1.5%

**Post-CAPA (6 months):**
- Total production: 12,000 units
- Labeling defects: 60
- Defect rate: 0.5%

### Analysis

**Step 1: Calculate Defect Rates**

Pre-CAPA rate: 150 / 10,000 = 1.5%

Post-CAPA rate: 60 / 12,000 = 0.5%

**Step 2: Statistical Comparison**

Chi-square test for proportions:
- χ²(1) = 85.7, p < 0.001

Risk Ratio: 0.5% / 1.5% = 0.33 (67% reduction)

95% CI for Risk Ratio: (0.25, 0.44)

**Step 3: Control Chart**

Monitor monthly defect rates post-CAPA:

| Month | Defects | Production | Rate (%) |
|-------|---------|------------|----------|
| 1 | 12 | 2,000 | 0.6 |
| 2 | 8 | 2,000 | 0.4 |
| 3 | 11 | 2,000 | 0.55 |
| 4 | 9 | 2,000 | 0.45 |
| 5 | 10 | 2,000 | 0.5 |
| 6 | 10 | 2,000 | 0.5 |

Process stable, no upward trend.

**Step 4: Interpretation**

Statistical Conclusion: Statistically significant reduction in labeling defect rate (p < 0.001).

Practical Conclusion: CAPA reduced defect rate by 67%, from 1.5% to 0.5%.

Effectiveness Conclusion: CAPA is effective. Defect rate remains stable at reduced level for 6 months post-implementation.

Regulatory Action: Document CAPA effectiveness verification. Close CAPA.

---

## Example 5: Survival Analysis for Device Longevity

### Scenario

Analyze implantable device longevity using Kaplan-Meier survival analysis.

### Data

- 200 devices implanted
- Follow-up: 0-60 months
- Device failures: 25
- Censored (patient lost to follow-up or study end): 175

### Analysis

**Step 1: Kaplan-Meier Survival Curve**

| Time (months) | At Risk | Failures | Censored | Survival (%) | 95% CI |
|---------------|---------|----------|----------|--------------|--------|
| 12 | 200 | 2 | 10 | 99.0 | (97.5, 100) |
| 24 | 188 | 5 | 15 | 96.4 | (93.8, 99.0) |
| 36 | 168 | 8 | 20 | 91.8 | (88.2, 95.4) |
| 48 | 140 | 6 | 25 | 88.0 | (83.8, 92.2) |
| 60 | 109 | 4 | 105 | 84.8 | (79.9, 89.7) |

**Step 2: Median Survival Time**

Median survival not reached (>50% devices still functional at 60 months).

**Step 3: Survival at Key Timepoints**

- 12 months: 99.0% (95% CI: 97.5%, 100%)
- 24 months: 96.4% (95% CI: 93.8%, 99.0%)
- 36 months: 91.8% (95% CI: 88.2%, 95.4%)
- 60 months: 84.8% (95% CI: 79.9%, 89.7%)

**Step 4: Interpretation**

Clinical Conclusion: Device demonstrates excellent long-term survival, with 84.8% still functioning at 5 years.

Regulatory Conclusion: Device longevity meets or exceeds typical expectations for this device class.

Labeling Recommendation: Include survival data in Instructions for Use, informing patients of expected device longevity.

---

Version: 1.0.0
Last Updated: 2026-02-09
