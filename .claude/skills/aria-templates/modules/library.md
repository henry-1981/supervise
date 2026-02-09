# Template Library

Comprehensive list of available regulatory document templates.

## Submission Templates

### FDA 510(k) Premarket Notification

**File**: `templates/510k-submission.md`

**Purpose**: FDA premarket notification for Class I/II devices

**Key Sections**:
- Cover letter with device classification
- Indications for use statement
- 510(k) summary or statement
- Truthful and accuracy statement
- Class III summary and certification
- Financial disclosure
- Substantial equivalence discussion
- Device description
- Performance testing summary
- Labeling

**Regulatory Reference**: 21 CFR 807, Subpart E

**Typical Use**: Medical devices requiring substantial equivalence demonstration

### CE Technical File

**File**: `templates/ce-technical-file.md`

**Purpose**: EU MDR technical documentation for CE marking

**Key Sections**:
- Device description and specifications
- Information on manufacturing process
- Design and verification documentation
- Risk management information
- Clinical evaluation per MEDDEV 2.7/1
- Post-market surveillance plan
- Declaration of conformity
- Notified Body certificates (if applicable)

**Regulatory Reference**: EU MDR 2017/745, Annex II/III

**Typical Use**: Class I/IIa/IIb/III devices for European market

### Clinical Evaluation Report

**File**: `templates/clinical-evaluation.md`

**Purpose**: Clinical data assessment per EU MDR requirements

**Key Sections**:
- Device description and intended use
- Literature search strategy and results
- Appraisal of clinical data
- Analysis of clinical data
- Benefit-risk determination
- Post-market clinical follow-up plan
- Conclusions

**Regulatory Reference**: EU MDR Annex XIV, MEDDEV 2.7/1 rev 4

**Typical Use**: All EU MDR submissions requiring clinical evidence

## Quality Management Templates

### Design Verification Report

**File**: `templates/design-verification.md`

**Purpose**: Document verification that design outputs meet design inputs

**Key Sections**:
- Design input requirements (traceability matrix)
- Verification test protocols
- Test execution records
- Pass/fail criteria
- Verification results summary
- Deviations and corrective actions
- Conclusions and approval

**Regulatory Reference**: 21 CFR 820.30(f), ISO 13485:2016 Section 7.3.6

**Typical Use**: All design control activities

### Design Validation Report

**File**: `templates/design-validation.md`

**Purpose**: Document validation that device meets user needs and intended use

**Key Sections**:
- Intended use and user profile
- Validation test protocols (clinical/simulated use)
- Acceptance criteria
- Validation results
- Human factors validation
- Clinical validation (if applicable)
- Conclusions and approval

**Regulatory Reference**: 21 CFR 820.30(g), ISO 13485:2016 Section 7.3.7

**Typical Use**: Final stage of design control process

### Risk Management Report

**File**: `templates/risk-management-report.md`

**Purpose**: Summary of risk management activities per ISO 14971

**Key Sections**:
- Risk management plan reference
- Risk analysis summary (FMEA/FTA)
- Risk evaluation against acceptability criteria
- Risk control measures
- Residual risk evaluation
- Risk-benefit analysis
- Overall residual risk acceptability
- Risk management review

**Regulatory Reference**: ISO 14971:2019

**Typical Use**: Required for all medical device submissions

### CAPA Report

**File**: `templates/capa-report.md`

**Purpose**: Document corrective and preventive action lifecycle

**Key Sections**:
- Problem description
- Root cause analysis
- Corrective action plan
- Preventive action plan
- Implementation verification
- Effectiveness check
- Closure and approval

**Regulatory Reference**: 21 CFR 820.100, ISO 13485:2016 Section 8.5

**Typical Use**: Quality system nonconformities and improvement opportunities

## Technical Documentation Templates

### Technical Specification

**File**: `templates/technical-spec.md`

**Purpose**: Define device technical requirements

**Key Sections**:
- Device overview and intended use
- Functional requirements (numbered)
- Performance requirements
- Interface requirements
- Design constraints
- Regulatory requirements
- Acceptance criteria
- Traceability matrix

**Regulatory Reference**: IEC 62304 Section 5.2 (software), IEEE 29148 (systems)

**Typical Use**: All design projects

### User Requirements Specification

**File**: `templates/user-requirements.md`

**Purpose**: Define user needs and intended use requirements

**Key Sections**:
- User profile and environment
- User needs analysis
- Intended use statement
- Use scenarios
- User requirements (numbered)
- Acceptance criteria
- Regulatory considerations

**Regulatory Reference**: IEC 62366-1:2015, 21 CFR 820.30(c)

**Typical Use**: Start of design control process

### Software Requirements Specification

**File**: `templates/software-requirements.md`

**Purpose**: Define software system and functional requirements

**Key Sections**:
- System requirements
- Software requirements
- Interface requirements
- Safety requirements per software safety class
- Security requirements
- Requirements traceability matrix

**Regulatory Reference**: IEC 62304:2006+AMD1:2015

**Typical Use**: Medical device software (SaMD, SiMD, firmware)

### Interface Control Document

**File**: `templates/interface-control.md`

**Purpose**: Define interfaces between system components

**Key Sections**:
- Interface identification
- Interface description
- Data format and protocols
- Timing requirements
- Error handling
- Interface verification requirements

**Regulatory Reference**: IEC 62304 Section 5.3

**Typical Use**: Multi-component systems, software integrations

## Review and Audit Templates

### Review Report

**File**: `templates/review-report.md`

**Purpose**: Document design reviews or document reviews

**Key Sections**:
- Review objectives and scope
- Review checklist
- Participants and roles
- Findings (conformances/non-conformances)
- Recommendations
- Action items with owners
- Conclusion (accept/reject/conditional)
- Approval signatures

**Regulatory Reference**: 21 CFR 820.30(e), ISO 13485:2016 Section 7.3.4

**Typical Use**: Design reviews, document reviews, change reviews

### Audit Report

**File**: `templates/audit-report.md`

**Purpose**: Document internal or external audit findings

**Key Sections**:
- Audit scope and objectives
- Audit plan and methodology
- Audit team
- Observations (major/minor findings, OFIs)
- Auditee responses
- Corrective action plans
- Follow-up and closure
- Audit conclusion

**Regulatory Reference**: 21 CFR 820.22, ISO 13485:2016 Section 8.2.2

**Typical Use**: QMS internal audits, supplier audits, regulatory inspections

### Test Protocol

**File**: `templates/test-protocol.md`

**Purpose**: Define test methodology and acceptance criteria

**Key Sections**:
- Test objectives
- Test items and requirements
- Test setup and equipment
- Test procedures (step-by-step)
- Acceptance criteria
- Pass/fail determination
- Data recording template
- Approval signatures

**Regulatory Reference**: 21 CFR 820.30(e), IEC 62304 Section 5.5

**Typical Use**: Verification testing, validation testing, performance testing

### Test Report

**File**: `templates/test-report.md`

**Purpose**: Document test execution and results

**Key Sections**:
- Test protocol reference
- Test setup and configuration
- Test results (data tables, graphs)
- Pass/fail determination
- Deviations from protocol
- Conclusions
- Attachments (raw data, screenshots)
- Approval signatures

**Regulatory Reference**: 21 CFR 820.30(e), IEC 62304 Section 5.6

**Typical Use**: All verification and validation testing

## Template Metadata

Each template includes:

**Header Block**:
- Document ID (auto-generated)
- Version and revision history
- Regulatory references
- Approval workflow

**Guidance Sections**:
- Italicized instructions
- Placeholder examples `[IN BRACKETS]`
- Regulatory citation format

**VALID Framework Markers**:
- Verification checkpoints
- Accuracy validation requirements
- Traceability links
- Inspectable audit trail
- Deliverable format compliance

## Customization Metadata

Templates support customization via frontmatter:

```yaml
---
template_id: regulatory-report
template_version: 1.0.0
regulatory_framework: FDA  # FDA, EU, ISO, Custom
device_class: Class II
document_type: submission
output_format: markdown  # markdown, pdf, docx
---
```

## Template Selection Guide

| Task | Recommended Template | Alternative |
|------|---------------------|-------------|
| US market clearance | `510k-submission.md` | `technical-spec.md` (for pre-submission) |
| EU market access | `ce-technical-file.md` | `clinical-evaluation.md` (standalone) |
| Design verification | `design-verification.md` | `test-report.md` (individual tests) |
| Design validation | `design-validation.md` | `clinical-evaluation.md` (if clinical) |
| Risk management | `risk-management-report.md` | N/A (required format) |
| CAPA tracking | `capa-report.md` | N/A (QMS requirement) |
| Software development | `software-requirements.md` | `technical-spec.md` (system-level) |
| Design review | `review-report.md` | N/A (standard process) |
| QMS audit | `audit-report.md` | N/A (standard process) |
| Testing | `test-protocol.md` + `test-report.md` | N/A (paired templates) |

## Integration with ARIA Workflows

Templates integrate with ARIA commands:

**Brief Phase**:
- Template selection based on task analysis
- Template customization for specific device/market

**Execute Phase**:
- Template instantiation with device data
- Section-by-section completion
- Regulatory citation verification via Context7

**Deliver Phase**:
- Template validation via VALID framework
- Export to Notion Document Registry
- Format conversion (PDF/DOCX) for submission
