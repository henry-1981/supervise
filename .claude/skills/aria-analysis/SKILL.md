---
name: aria-analysis
description: >
  Data analysis methodology skill for regulatory data interpretation and statistical analysis.
  Defines systematic data analysis approaches, statistical techniques for regulatory submissions,
  and result interpretation guidelines. Use with Sequential Thinking MCP for complex analysis
  and expert-analyst agent for comprehensive data analysis tasks.
license: Apache-2.0
compatibility: Designed for Claude Code
allowed-tools: Read Grep Glob Bash mcp__sequential-thinking__sequentialthinking
user-invocable: false
metadata:
  version: "1.0.0"
  category: "workflow"
  status: "active"
  updated: "2026-02-09"
  modularized: "true"
  tags: "analysis, data-analysis, statistics, regulatory, interpretation"
  author: "ARIA Team"
  context: "regulatory"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords:
    [
      "analysis",
      "data analysis",
      "statistical analysis",
      "statistics",
      "clinical data",
      "performance data",
      "post-market data",
      "trend analysis",
      "root cause analysis",
      "interpretation",
      "significance",
    ]
  agents: ["expert-analyst", "expert-clinical", "expert-capa"]
  phases: ["execute", "deliver"]
---

# ARIA Data Analysis Methodology

## Quick Reference (30 seconds)

Data analysis methodology for regulatory data interpretation and statistical analysis.

Core Capabilities:

- Systematic Analysis Approach: Structured methodology for regulatory data analysis
- Statistical Techniques: Methods appropriate for regulatory submissions
- Result Interpretation Guidelines: Standards for presenting analysis results
- Sequential Thinking Integration: Complex multi-step analysis using MCP
- Clinical Data Analysis: Safety and effectiveness evaluation

When to Use:

- Clinical data analysis (safety, effectiveness, performance)
- Post-market surveillance data (adverse events, complaints)
- Manufacturing data (process capability, control charts)
- Risk analysis data (probability, severity, detectability)
- CAPA effectiveness data (trend analysis, root cause)
- Performance testing results (verification, validation)

Analysis Types:

- Descriptive Statistics: Summarize and describe data characteristics
- Inferential Statistics: Draw conclusions from sample data
- Hypothesis Testing: Evaluate clinical claims and assertions
- Survival Analysis: Time-to-event data (device longevity, failure)
- Trend Analysis: Post-market surveillance and quality trends
- Risk-Benefit Analysis: Evaluate device safety and effectiveness trade-offs

---

## Implementation Guide (5 minutes)

### Analysis Methodology Framework

All analysis activities follow a systematic approach defined in modules/methodology.md.

#### Analysis Phases

**Phase 1: Data Understanding**
- Define analysis objectives and questions
- Identify data sources and types
- Assess data quality and completeness
- Determine appropriate analysis techniques

**Phase 2: Data Preparation**
- Clean and validate data
- Handle missing values
- Identify and address outliers
- Transform data as needed for analysis

**Phase 3: Analysis Execution**
- Apply appropriate statistical techniques
- Use Sequential Thinking MCP for complex multi-step analysis
- Document assumptions and limitations
- Generate analysis results and visualizations

**Phase 4: Result Interpretation**
- Interpret statistical significance vs clinical significance
- Consider regulatory context and requirements
- Identify key findings and patterns
- Document implications for regulatory submission

**Phase 5: Reporting**
- Present results clearly and accurately
- Include appropriate tables, figures, and statistical summaries
- Link findings to regulatory requirements
- Provide evidence-based conclusions

### Statistical Techniques for Regulatory Data

Detailed statistical methods are in modules/statistics.md.

#### Descriptive Statistics

Used to summarize and describe data characteristics:

- Measures of Central Tendency: Mean, median, mode
- Measures of Dispersion: Standard deviation, range, IQR
- Frequency Distributions: Histograms, frequency tables
- Percentiles and Quartiles: Distribution characteristics

#### Inferential Statistics

Used to draw conclusions about populations from samples:

- Confidence Intervals: Estimate population parameters
- Hypothesis Testing: t-tests, ANOVA, chi-square
- Sample Size Determination: Power analysis for clinical studies
- Non-parametric Tests: When normality assumptions not met

#### Clinical Data Analysis

Specific techniques for clinical evaluation:

- Safety Analysis: Adverse event rates, serious adverse events
- Effectiveness Analysis: Primary and secondary endpoints
- Survival Analysis: Kaplan-Meier, Cox proportional hazards
- Equivalence/Non-inferiority Testing: For substantial equivalence claims

### Result Interpretation Guidelines

Interpretation standards are defined in modules/interpretation.md.

#### Statistical Significance vs Clinical Significance

**Statistical Significance:**
- P-value < 0.05 (typical threshold)
- Rejects null hypothesis
- May not indicate practical importance

**Clinical Significance:**
- Meaningful clinical difference
- Relevant to patient outcomes
- Clinically important effect size
- May exist even if not statistically significant (underpowered study)

**Regulatory Perspective:**
- Both statistical and clinical significance matter
- Effect size and confidence intervals important
- Clinical relevance determines regulatory acceptance
- Safety signals require investigation regardless of p-value

---

## Sequential Thinking MCP Integration

### Complex Analysis Workflow

Use Sequential Thinking MCP for multi-step regulatory analysis:

1. Problem Decomposition
2. Systematic analysis planning
3. Step-by-step execution
4. Integration of findings

Example workflow:

```
mcp__sequential-thinking__sequentialthinking: {
  problem: "Analyze clinical data for 510(k) substantial equivalence",
  steps: [
    "Define primary and secondary endpoints",
    "Assess data quality and completeness",
    "Perform descriptive statistics",
    "Conduct hypothesis tests",
    "Evaluate clinical significance",
    "Compare with predicate device data",
    "Synthesize evidence for substantial equivalence"
  ]
}
```

### Multi-Market Data Analysis

When analyzing data across multiple markets:

```
mcp__sequential-thinking__sequentialthinking: {
  problem: "Interpret multi-market post-market surveillance data",
  steps: [
    "Stratify data by market (US, EU, Korea)",
    "Calculate adverse event rates per market",
    "Identify market-specific trends",
    "Assess reporting biases by market",
    "Synthesize global safety profile",
    "Determine regulatory reporting requirements"
  ]
}
```

---

## Analysis Checklists

### Clinical Data Analysis Checklist

- [ ] Define primary and secondary endpoints
- [ ] Assess data quality (completeness, accuracy)
- [ ] Determine appropriate statistical methods
- [ ] Calculate sample size adequacy
- [ ] Perform descriptive statistics
- [ ] Conduct hypothesis tests (if applicable)
- [ ] Evaluate clinical significance of findings
- [ ] Compare with predicate device (for 510(k))
- [ ] Document assumptions and limitations
- [ ] Present results clearly with tables/figures

### Post-Market Surveillance Analysis Checklist

- [ ] Define surveillance period and data sources
- [ ] Calculate adverse event rates
- [ ] Identify serious adverse events
- [ ] Perform trend analysis over time
- [ ] Compare with pre-market clinical data
- [ ] Assess reporting biases
- [ ] Determine if safety signal exists
- [ ] Document follow-up actions required
- [ ] Prepare regulatory reporting (if needed)

### CAPA Effectiveness Analysis Checklist

- [ ] Define effectiveness criteria
- [ ] Collect pre-CAPA and post-CAPA data
- [ ] Perform trend analysis
- [ ] Calculate recurrence rates
- [ ] Assess root cause resolution
- [ ] Determine statistical significance of improvement
- [ ] Document verification of effectiveness
- [ ] Identify residual risks

---

## Module References

- modules/methodology.md: Detailed data analysis methodology framework
- modules/statistics.md: Statistical techniques for regulatory data
- modules/interpretation.md: Result interpretation and reporting guidelines
- examples.md: Analysis examples for common regulatory scenarios

---

Version: 1.0.0 (Phase 2.3)
Last Updated: 2026-02-09
Language: English
Target Agents: expert-analyst, expert-clinical, expert-capa
