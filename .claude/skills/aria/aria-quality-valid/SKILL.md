---
name: aria-quality-valid
description: >
  VALID framework quality assurance for ARIA business documents.
  Implements 5-dimensional quality validation: Verified (content matches
  original regulations), Accurate (data/numbers/refs are correct and current),
  Linked (requirements-documents-evidence traceability), Inspectable
  (audit trails with documented rationale), Deliverable (output meets
  submission format requirements). Used by manager-quality for quality
  gate validation and improvement recommendations.
license: Apache-2.0
compatibility: Designed for Claude Code
user-invocable: true
metadata:
  version: "1.0.0"
  category: "foundation"
  status: "active"
  updated: "2026-02-09"
  modularized: "true"
  tags: "aria, quality, validation, framework"

# ARIA Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# ARIA Extension: Triggers
triggers:
  keywords: ["quality", "validation", "review", "inspection", "compliance"]
  agents: ["manager-quality", "expert-reviewer"]
  phases: ["brief", "execute", "deliver"]
  languages: ["en", "ko"]
---

# VALID Quality Framework

## Overview

The VALID framework is a 5-dimensional quality assurance system designed for regulatory and technical documentation in the ARIA ecosystem.

## Five Dimensions

### 1. Verified (V)
**Definition**: Content matches original regulatory text

**Validation Criteria**:
- Cross-reference with original regulations
- Verify interpretation accuracy
- Confirm no unauthorized modifications
- Validate regulatory version used

**Checks**:
- [ ] Regulatory text cross-referenced
- [ ] Interpretation validated against source
- [ ] No additions beyond scope
- [ ] No omissions of critical requirements
- [ ] Regulatory version cited correctly

**Quality Score**: 20 points max
- Full cross-reference: 20 points
- Partial cross-reference: 10 points
- No cross-reference: 0 points

### 2. Accurate (A)
**Definition**: Data, numbers, and references are correct and current

**Validation Criteria**:
- Source verification for all claims
- Date validation for temporal references
- Numerical accuracy for quantitative data
- Reference currency (latest version)

**Checks**:
- [ ] All claims have verifiable sources
- [ ] Dates are current and accurate
- [ ] Numbers verified from source data
- [ ] References are latest available versions
- [ ] No contradictory information

**Quality Score**: 20 points max
- All verified: 20 points
- Minor inaccuracies: 10 points
- Major inaccuracies: 0 points

### 3. Linked (L)
**Definition**: Traceability between requirements, documents, and evidence

**Validation Criteria**:
- Requirements-to-document mapping
- Document-to-evidence linking
- Traceability matrix completeness
- Bidirectional traceability

**Checks**:
- [ ] Requirements mapped to document sections
- [ ] Document sections reference evidence
- [ ] Traceability matrix maintained
- [ ] Orphan requirements identified
- [ ] Orphan evidence identified

**Quality Score**: 20 points max
- Complete traceability: 20 points
- Minor gaps: 10 points
- Major gaps: 0 points

### 4. Inspectable (I)
**Definition**: Audit trails maintained with documented rationale

**Validation Criteria**:
- Decision rationale documented
- Change history tracked
- Approval workflow recorded
- Audit trail completeness

**Checks**:
- [ ] All decisions have documented rationale
- [ ] Change history complete
- [ ] Approval workflow documented
- [ ] Audit trail unbroken
- [ ] Reviewer comments preserved

**Quality Score**: 20 points max
- Full audit trail: 20 points
- Partial audit trail: 10 points
- No audit trail: 0 points

### 5. Deliverable (D)
**Definition**: Output meets submission format requirements

**Validation Criteria**:
- Template compliance
- Format specification adherence
- Submission requirement checklist
- Final quality gate pass

**Checks**:
- [ ] Correct template used
- [ ] Format specifications met
- [ ] Submission checklist complete
- [ ] Quality gate passed
- [ ] Distribution requirements satisfied

**Quality Score**: 20 points max
- Fully compliant: 20 points
- Minor deviations: 10 points
- Major deviations: 0 points

## Quality Scoring

### Total Score Calculation
```
Total Score = V + A + L + I + D (max 100 points)
```

### Quality Levels
- **Excellent**: 90-100 points - Ready for submission
- **Good**: 70-89 points - Minor improvements needed
- **Acceptable**: 50-69 points - Significant improvements needed
- **Poor**: 0-49 points - Major revisions required

## Quality Gate Process

### Phase 1: Initial Validation
- Run all 5 dimension checks
- Generate initial quality report
- Identify critical gaps

### Phase 2: Improvement Cycle
- Address identified issues
- Re-run failed checks
- Track improvement progress

### Phase 3: Final Validation
- Complete quality gate check
- Generate final quality report
- Approve for submission

## Quality Report Template

```markdown
# VALID Quality Report

**Document**: [Document Name]
**Date**: [Validation Date]
**Reviewer**: [Reviewer Name]
**Score**: [X/100]

## Dimension Scores

| Dimension | Score | Status | Notes |
|-----------|-------|--------|-------|
| Verified | [X/20] | [Pass/Fail] | [Notes] |
| Accurate | [X/20] | [Pass/Fail] | [Notes] |
| Linked | [X/20] | [Pass/Fail] | [Notes] |
| Inspectable | [X/20] | [Pass/Fail] | [Notes] |
| Deliverable | [X/20] | [Pass/Fail] | [Notes] |

## Issues Found

### Critical Issues
[List issues blocking submission]

### Major Issues
[List issues requiring significant work]

### Minor Issues
[List issues for improvement]

## Recommendations
[Specific improvement recommendations]

## Next Steps
[Action items for quality improvement]
```

## Integration with ARIA Workflow

### Brief Phase
- Establish quality baseline
- Define quality criteria
- Set quality targets

### Execute Phase
- Continuous quality monitoring
- Incremental validation
- Early issue detection

### Deliver Phase
- Final quality gate
- Submission approval
- Quality metrics reporting

## Best Practices

1. **Validate Early**: Start quality checks at draft stage
2. **Iterate Often**: Run validation after each significant change
3. **Document Decisions**: Maintain comprehensive audit trail
4. **Use Templates**: Ensure consistent deliverable format
5. **Track Metrics**: Monitor quality trends over time
