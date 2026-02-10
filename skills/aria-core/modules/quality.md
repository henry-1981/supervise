# VALID Quality Framework Module

## Overview

The VALID framework ensures regulatory document quality across five dimensions, adapted from TRUST 5 for regulatory compliance contexts.

---

## VALID Dimensions

### V - Verified

**Definition**: Content matches source regulation text and regulatory interpretations align with current guidance.

**Verification Process:**

1. **Citation Accuracy Check**
   - All cited regulation/standard clauses match actual source text
   - Standard names are correct (e.g., "ISO 13485:2016" not "ISO 13485")
   - Section numbers are accurate (e.g., "21 CFR 820.30(i)" not "820.30")
   - Version dates are current (e.g., "EU MDR 2017/745" not "MDR")

2. **Regulatory Interpretation Validation**
   - Interpretations align with current guidance documents
   - Claims are supported by authoritative sources
   - No speculative or unsupported regulatory statements

3. **Technical Claim Verification**
   - Technical claims are supported by evidence data
   - Test results link to actual test reports
   - Clinical claims have supporting clinical data

**Scoring Criteria:**
- **5 (Exceeds)**: All citations verified, interpretations current, claims fully supported
- **4 (Meets)**: All citations verified, interpretations current, minor claim gaps
- **3 (Mostly)**: Most citations verified, some interpretations need clarification
- **2 (Partial)**: Many citation issues, interpretations need review
- **1 (Fails)**: Citations missing or incorrect, interpretations unsupported

**Validation Methods:**
- Cross-reference with regulation originals via Context7 MCP
- Validate guidance currency through official sources
- Link technical claims to test data documentation

---

### A - Accurate

**Definition**: Data, figures, and references are correct and current.

**Accuracy Checks:**

1. **Data Validation**
   - All numbers and data match their sources
   - Calculations are correct and documented
   - Units of measure are consistent and correct
   - Statistical methods are appropriate and documented

2. **Document Currency**
   - Referenced documents are the latest version
   - Standards include current amendment versions
   - Guidance documents are current (not superseded)
   - Dates and version numbers are verified

3. **Reference Completeness**
   - All required references are included
   - Reference lists are complete and accurate
   - Cross-references are valid and consistent
   - Document identifiers are correct

**Scoring Criteria:**
- **5 (Exceeds)**: All data accurate, documents current, references complete
- **4 (Meets)**: Data accurate, documents current, minor reference gaps
- **3 (Mostly)**: Most data accurate, some documents need updating
- **2 (Partial)**: Many data discrepancies, outdated references
- **1 (Fails)**: Data incorrect, references missing or outdated

**Validation Methods:**
- Source validation against original documents
- Date checks for currency (within 365 days for guidance)
- Reference cross-linking validation

---

### L - Linked

**Definition**: Traceability between requirements, documents, and evidence.

**Linkage Requirements:**

1. **Requirement-to-Evidence Traceability**
   - Every requirement is linked to supporting evidence
   - Traceability matrix is complete
   - Requirements trace back to regulatory citations
   - Evidence links are valid and accessible

2. **Document Interdependencies**
   - Changes are reflected in all affected documents
   - Cross-references between documents are accurate
   - Document hierarchy is properly maintained
   - Version relationships are tracked

3. **Approval Chain Linkage**
   - Review and approval records exist
   - Approval history is traceable
   - Change decisions are linked to rationale
   - Sign-off requirements are met

**Scoring Criteria:**
- **5 (Exceeds)**: Complete traceability, all changes reflected, approvals tracked
- **4 (Meets)**: Traceability complete, minor cross-reference gaps
- **3 (Mostly)**: Most requirements linked, some cross-reference issues
- **2 (Partial)**: Many traceability gaps, inconsistent cross-references
- **1 (Fails)**: Traceability missing, cross-references broken

**Validation Methods:**
- Traceability matrix verification
- Cross-reference scanning and validation
- Document dependency graph analysis

---

### I - Inspectable

**Definition**: Audit trail maintained, decision rationale documented.

**Inspectability Requirements:**

1. **Decision Rationale**
   - Every regulatory decision has documented rationale
   - Alternative approaches considered and documented
   - Risk assessments support decisions
   - Subject matter expert input is recorded

2. **Change History**
   - All changes are tracked with version history
   - Change reasons are documented
   - Approval history for each change is maintained
   - Rollback capability exists for critical changes

3. **Audit Readiness**
   - Documents are organized for audit review
   - Supporting evidence is accessible
   - Decision-making process is transparent
   - Compliance justifications are clear

**Scoring Criteria:**
- **5 (Exceeds)**: Complete audit trail, full rationale, transparent process
- **4 (Meets)**: Audit trail complete, rationale documented, minor gaps
- **3 (Mostly)**: Most decisions documented, some rationale gaps
- **2 (Partial)**: Audit trail incomplete, rationale missing for key decisions
- **1 (Fails)**: No audit trail, decisions undocumented

**Validation Methods:**
- Audit trail completeness check
- Decision documentation review
- Change history verification

---

### D - Deliverable

**Definition**: Output meets submission format requirements.

**Deliverability Requirements:**

1. **Template Compliance**
   - Output follows required template structure
   - All required sections are present
   - Section ordering matches template
   - Template formatting is applied correctly

2. **Submission Authority Requirements**
   - Format meets submission authority guidelines (FDA, EU MDR, MFDS)
   - File format requirements are met (PDF, eSTAR, CER format)
   - Document size limits are respected
   - Required metadata is included

3. **Completeness**
   - All attachments are included
   - Reference documents are attached or linked
   - Required declarations and signatures are present
   - Supporting documentation is complete

**Scoring Criteria:**
- **5 (Exceeds)**: Template perfect, submission ready, all attachments included
- **4 (Meets)**: Template compliant, submission format correct, minor attachment gaps
- **3 (Mostly)**: Template mostly followed, some format issues
- **2 (Partial)**: Template not followed, significant format issues
- **1 (Fails)**: Template ignored, format incorrect, incomplete

**Validation Methods:**
- Template conformance check
- Submission authority format validation
- Completeness checklist verification

---

## Quality Gate Implementation

### Automated Checks

**Validated by manager-quality agent:**

```yaml
quality:
  framework: "VALID"
  auto_check: true
  levels:
    - L1:  # Format check (automated)
      - template_compliance: true
      - section_completeness: true
      - citation_format: true

    - L2:  # Reference check (semi-automated)
      - citation_accuracy: true
      - reference_currency: true
      - link_validity: true

    - L3:  # Content check (semi-automated)
      - regulatory_interpretation: true
      - claim_support: true
      - traceability: true
```

### Manual Review Points

**Require expert-reviewer validation:**

- Regulatory pathway decisions
- Predicate device selection rationale
- Risk acceptability determinations
- Clinical evaluation conclusions
- Substantial equivalence arguments

### VALID Score Calculation

**Overall Score**: Average of 5 dimensions (target: 4.0+)

```
VALID Score = (V + A + L + I + D) / 5

Where each dimension scores 1-5:
- 5: Exceeds requirements
- 4: Meets all requirements
- 3: Meets most requirements
- 2: Meets some requirements
- 1: Fails to meet requirements
```

**Passing Criteria:**
- Minimum overall score: 4.0
- No dimension below 3.0
- Critical dimensions (V, D) must be ≥ 4.0

---

## Error Handling for Quality Issues

### VALID Gate Failure

**When VALID gate fails:**

1. **Identify Issue**
   - Specify which dimension(s) failed
   - Document specific deficiencies
   - Provide examples of non-compliance

2. **Provide Remediation Guidance**
   - Explain what needs to be fixed
   - Suggest specific corrections
   - Reference applicable requirements

3. **Return to Execute Phase**
   - Document must return to Execute phase for refinement
   - Specific issues must be addressed
   - Re-validation required after fixes

**Error Message Pattern:**
```
## VALID Quality Gate Failed

**Overall Score**: 3.4/5.0 (Target: 4.0+)

**Failed Dimensions**:
- **V - Verified**: 3/5 - Citation format issues detected
- **L - Linked**: 3/5 - Traceability matrix incomplete

**Specific Issues**:
1. ISO 13485 citation missing version date
2. Requirement 5.2 not linked to evidence document

**Remediation Required**:
- Update all citations to include version dates
- Complete traceability matrix for all requirements
- Re-submit for VALID validation

Status: Returned to Execute phase for refinement
```

---

## Configuration

VALID framework behavior is configured in `aria.yaml`:

```yaml
quality:
  framework: "VALID"
  auto_check: true
  levels:
    - L1  # Format check (automated)
    - L2  # Reference check (semi-automated)
    - L3  # Content check (semi-automated)

  thresholds:
    min_overall_score: 4.0
    min_dimension_score: 3.0
    critical_dimensions:
      - Verified: 4.0
      - Deliverable: 4.0

  enforcement:
    gate_on_deliver: true
    return_on_fail: true
    max_iterations: 3
```

---

## Quality Reporting

### VALID Quality Report Structure

```
# VALID Quality Report

**Document**: [Document Name]
**Version**: [Version Number]
**Date**: [Assessment Date]

## Overall Score: 4.2/5.0 ✅

## Dimension Scores

### V - Verified: 4.5/5.0
- ✅ All citations match source text
- ✅ Regulatory interpretations current
- ⚠️  2 technical claims need additional support

### A - Accurate: 4.0/5.0
- ✅ All data verified
- ✅ References current
- ✅ No calculation errors

### L - Linked: 4.0/5.0
- ✅ Traceability matrix complete
- ✅ All requirements linked to evidence
- ✅ Cross-references accurate

### I - Inspectable: 4.0/5.0
- ✅ Decision rationale documented
- ✅ Change history tracked
- ✅ Audit ready

### D - Deliverable: 4.5/5.0
- ✅ Template compliance verified
- ✅ Submission format correct
- ✅ All attachments included

## Recommendations

### Required Fixes
- [ ] Add supporting evidence for claims in section 5.2
- [ ] Update citation format for ISO 13485

### Optional Improvements
- [ ] Consider adding more detail to decision rationale
- [ ] Strengthen evidence for clinical claim in section 7.3

## Conclusion

**Status**: READY FOR DELIVERY
**Next Steps**: Proceed to DELIVER phase for final formatting and distribution
```

---

## Integration with Workflow

### VALID Gate Checkpoints

**Brief Phase:**
- No VALID gates (planning phase)

**Execute Phase:**
- After Draft: L1 (Format) + L2 (Reference) checks
- After Review: Full L3 (Content) validation

**Deliver Phase:**
- Complete VALID gate pass required
- All dimensions must meet thresholds

### Continuous Quality Monitoring

**During Document Creation:**
- Real-time citation format checking
- Automated cross-reference validation
- Template compliance monitoring

**After Document Completion:**
- Full VALID quality gate
- Manual expert review for critical sections
- Final approval before delivery

---

## Best Practices

### For Document Authors

1. **Cite as You Write**
   - Include proper citations from the start
   - Use standard citation format consistently
   - Link claims to evidence immediately

2. **Maintain Traceability**
   - Update traceability matrix as you document requirements
   - Link all requirements to evidence documents
   - Keep cross-references current

3. **Document Decisions**
   - Record rationale for regulatory decisions
   - Note alternative approaches considered
   - Reference supporting guidance documents

### For Quality Reviewers

1. **Use VALID Checklist**
   - Systematically evaluate each dimension
   - Document specific issues found
   - Provide actionable remediation guidance

2. **Verify Critical Content**
   - Focus on regulatory pathway decisions
   - Validate predicate device selections
   - Review risk acceptability determinations

3. **Maintain Audit Trail**
   - Track all review findings
   - Document approval decisions
   - Maintain version history

---

## Compliance Mapping

### VALID to TRUST 5 Comparison

| VALID Dimension | TRUST 5 Dimension | Adaptation |
|----------------|------------------|------------|
| V - Verified | T - Tested | Regulatory verification vs code testing |
| A - Accurate | R - Readable | Data accuracy vs code readability |
| L - Linked | U - Understandable | Traceability vs code understanding |
| I - Inspectable | S - Secured | Audit trail vs security (different focus) |
| D - Deliverable | T - Trackable | Format compliance vs git tracking |

---

**Version**: 1.0.0
**Last Updated**: 2026-02-09
**Module**: VALID Quality Framework
