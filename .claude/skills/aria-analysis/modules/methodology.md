# Data Analysis Methodology

Systematic approach for regulatory data analysis and interpretation.

## Five-Phase Analysis Framework

### Phase 1: Data Understanding

**Objectives:**
- Define analysis objectives and questions
- Identify data sources and data types
- Assess data quality and completeness
- Determine appropriate analytical techniques

**Key Activities:**
- Clarify regulatory purpose (510(k), PMA, post-market surveillance)
- Identify data sources (clinical trials, manufacturing, post-market)
- Assess data availability and quality
- Determine sample size adequacy
- Select statistical methods appropriate for data type

**Deliverables:**
- Analysis plan document
- Data inventory and quality assessment
- Statistical methods justification

### Phase 2: Data Preparation

**Objectives:**
- Clean and validate data
- Handle missing values appropriately
- Identify and address outliers
- Transform data as needed

**Key Activities:**
- Verify data accuracy and completeness
- Handle missing data (imputation, exclusion, sensitivity analysis)
- Identify outliers and determine handling approach
- Transform variables if needed (log transform, categorization)
- Create analysis-ready dataset

**Deliverables:**
- Clean validated dataset
- Data preparation documentation
- Missing data handling report
- Outlier assessment report

### Phase 3: Analysis Execution

**Objectives:**
- Apply appropriate statistical techniques
- Generate analysis results
- Document assumptions and limitations

**Key Activities:**
- Perform descriptive statistics
- Conduct hypothesis tests (if applicable)
- Calculate confidence intervals
- Generate visualizations (tables, figures, charts)
- Use Sequential Thinking MCP for complex multi-step analysis
- Document all analysis steps and code

**Deliverables:**
- Statistical analysis results
- Tables and figures
- Analysis code and documentation
- Assumptions and limitations statement

### Phase 4: Result Interpretation

**Objectives:**
- Interpret statistical significance
- Assess clinical significance
- Consider regulatory context

**Key Activities:**
- Evaluate statistical significance (p-values, confidence intervals)
- Assess clinical significance (effect size, clinical relevance)
- Compare with predicate device (for 510(k))
- Identify safety signals or concerns
- Determine regulatory implications
- Document interpretation rationale

**Deliverables:**
- Interpretation summary
- Clinical significance assessment
- Regulatory implications statement
- Safety assessment (if applicable)

### Phase 5: Reporting

**Objectives:**
- Present results clearly and accurately
- Link findings to regulatory requirements
- Provide evidence-based conclusions

**Key Activities:**
- Create analysis report with results
- Generate tables and figures following regulatory standards
- Link analysis to regulatory requirements
- Provide clear conclusions and recommendations
- Include sensitivity analyses if applicable

**Deliverables:**
- Analysis report
- Tables and figures
- Executive summary
- Regulatory submission-ready documentation

---

## Analysis Types and Approaches

### Clinical Data Analysis

**Purpose:** Evaluate safety and effectiveness of medical devices.

**Typical Data:**
- Primary endpoint data (effectiveness)
- Adverse event data (safety)
- Device performance data
- Patient demographics
- Follow-up duration

**Analysis Approach:**
1. Define endpoints (primary, secondary)
2. Assess data quality and missing data
3. Perform descriptive statistics by treatment group
4. Conduct hypothesis tests for primary endpoint
5. Analyze safety data (adverse event rates)
6. Perform subgroup analyses (if pre-specified)
7. Interpret clinical and statistical significance

### Post-Market Surveillance Data Analysis

**Purpose:** Monitor device safety and performance after market release.

**Typical Data:**
- Adverse event reports
- Complaint data
- Device malfunction reports
- Return rate data
- Post-market clinical follow-up data

**Analysis Approach:**
1. Define surveillance period and data sources
2. Calculate event rates (per patient-year, per device-year)
3. Perform trend analysis over time
4. Compare with pre-market clinical data
5. Identify safety signals
6. Assess need for corrective action or regulatory reporting

### Manufacturing and Quality Data Analysis

**Purpose:** Assess process capability and product quality.

**Typical Data:**
- In-process measurements
- Final product testing results
- Process parameters
- Defect rates
- Control chart data

**Analysis Approach:**
1. Calculate process capability indices (Cp, Cpk)
2. Generate control charts (X-bar, R, p-charts)
3. Identify out-of-control conditions
4. Perform trend analysis
5. Assess process stability and capability
6. Determine if process meets specifications

### Risk Analysis Data

**Purpose:** Quantify and evaluate device risks.

**Typical Data:**
- Hazard identification
- Probability estimates
- Severity ratings
- Detectability ratings
- Risk scores (P × S, RPN)

**Analysis Approach:**
1. Categorize risks by hazard type
2. Calculate risk scores or risk priority numbers
3. Identify high-priority risks
4. Evaluate risk acceptability
5. Assess residual risk after mitigation
6. Perform risk-benefit analysis

---

## Sequential Thinking Integration

### When to Use Sequential Thinking MCP

Use Sequential Thinking for:

- Multi-step regulatory analysis requiring logical progression
- Complex decision trees (regulatory pathway selection)
- Trade-off analysis (risk vs benefit)
- Multi-market data synthesis
- Root cause analysis with multiple contributing factors

### Sequential Thinking Pattern

```
Problem Definition:
Define the regulatory question or analysis objective

Step Decomposition:
Break down analysis into logical sequential steps

Step Execution:
Execute each step systematically, building on previous steps

Result Integration:
Synthesize findings across all steps

Conclusion:
Provide evidence-based regulatory conclusion
```

---

## Quality Control Checklist

### Before Finalizing Analysis

- [ ] Analysis plan documented and approved
- [ ] Data quality verified (accuracy, completeness)
- [ ] Missing data handled appropriately
- [ ] Outliers identified and addressed
- [ ] Appropriate statistical methods applied
- [ ] Assumptions documented and verified
- [ ] Results verified (independent check if critical)
- [ ] Statistical significance assessed
- [ ] Clinical significance evaluated
- [ ] Regulatory context considered
- [ ] Limitations clearly stated
- [ ] Results presented clearly (tables, figures)
- [ ] Conclusions supported by evidence

---

Version: 1.0.0
Last Updated: 2026-02-09
