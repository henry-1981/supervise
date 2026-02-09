# VALID Framework - External References

## Overview

This document provides external references for regulatory quality standards, guidelines, and best practices that inform the VALID framework.

---

## Regulatory Standards

### FDA (United States)

**21 CFR Part 820 - Quality System Regulation**
- **820.40 - Document Controls**
  - Requirement for documented procedures to control documents
  - Ensures accuracy and prevents use of obsolete documents
  - VALID Impact: Verified and Inspectable dimensions
  - URL: https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfcfr/CFRSearch.cfm?fr=820.40

**21 CFR Part 820.30 - Design Controls**
- **820.30(j) - Design History File**
  - Requirements for DHF contents and organization
  - Traceability of design activities
  - VALID Impact: Linked and Inspectable dimensions
  - URL: https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfcfr/CFRSearch.cfm?fr=820.30

**FDA Guidance: Design Control Guidance for Medical Device Manufacturers (1997)**
- Interpretation of 21 CFR 820.30
- Best practices for design control implementation
- VALID Impact: All dimensions
- URL: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/design-control-guidance-medical-device-manufacturers

**FDA Guidance: eCTD Technical Conformance Guide v4.0**
- Electronic submission format requirements
- File structure and validation rules
- VALID Impact: Deliverable dimension
- URL: https://www.fda.gov/drugs/electronic-regulatory-submission-and-review/ectd-technical-conformance-guide

### ISO Standards

**ISO 13485:2016 - Medical Devices Quality Management Systems**
- **Section 4.2.4 - Control of Records**
  - Records must be legible, readily identifiable, and retrievable
  - Retention times and protection requirements
  - VALID Impact: Accurate and Inspectable dimensions
  - Standard: ISO 13485:2016

**ISO 13485:2016 - Section 7.3.4 - Design and Development Review**
- Design review requirements
- Documentation of review results, decisions, and actions
  - VALID Impact: Inspectable dimension
  - Standard: ISO 13485:2016

**ISO 14971:2019 - Application of Risk Management to Medical Devices**
- Risk management file requirements
- Traceability between risks and risk controls
- Risk-benefit analysis documentation
- VALID Impact: Linked and Inspectable dimensions
- Standard: ISO 14971:2019

**IEC 62304:2006+AMD1:2015 - Medical Device Software - Software Lifecycle Processes**
- **Section 5.1.1 - Requirements Traceability**
  - Traceability between requirements and system test cases
  - Verification and validation documentation
  - VALID Impact: Linked dimension
  - Standard: IEC 62304:2006+AMD1:2015

### EU Regulations

**EU MDR 2017/745 - Medical Device Regulation**
- **Article 61 - Clinical Evaluation**
  - Clinical evaluation requirements
  - Documentation and reporting standards
  - VALID Impact: Verified and Accurate dimensions
  - Regulation: (EU) 2017/745

**Annex XIV - Clinical Evaluation and Post-Market Clinical Follow-up**
- Clinical evaluation report (CER) requirements
- Traceability to essential requirements
  - VALID Impact: Linked dimension
  - Regulation: (EU) 2017/745 Annex XIV

**MEDDEV 2.7/1 Rev 4 - Clinical Evaluation (June 2016)**
- CER template and guidance
- Evidence requirements and evaluation methodology
- VALID Impact: Deliverable dimension
- Guidance: MEDDEV 2.7/1 Rev 4

---

## Quality Management References

### GHTF/IMDRF Guidance

**IMDRF/SaMD WG/N10 FINAL:2013 - Software as a Medical Device**
- Software documentation requirements
- Quality management for SaMD
- VALID Impact: All dimensions for software devices

**IMDRF/SaMD WG/N41 FINAL:2015 - Clinical Evaluation**
- Clinical evaluation pathway for SaMD
- Evidence requirements
- VALID Impact: Verified and Linked dimensions

### Industry Standards

**AAMI TIR45:2012 - Guidance on the Use of AGILE Practices in the Development of Medical Device Software**
- Agile development with design control compliance
- Traceability in iterative development
- VALID Impact: Linked dimension adaptation for Agile

**IEEE 829-2008 - Standard for Software and System Test Documentation**
- Test documentation structure
- Traceability matrix best practices
- VALID Impact: Linked dimension test documentation

---

## Context7 MCP Library References

### Regulatory Libraries

**FDA Regulations:**
- Library ID: `fda-cfr-title21`
- Content: 21 CFR Parts 800-1299 (Medical Devices)
- Use: Verify FDA citations in Verified dimension
- TTL: 30 days (regulations update quarterly)

**ISO Standards:**
- Library ID: `iso-13485-2016`
- Content: ISO 13485:2016 full text
- Use: Verify ISO 13485 citations
- TTL: 365 days (standard stable)

**ISO 14971:**
- Library ID: `iso-14971-2019`
- Content: ISO 14971:2019 full text
- Use: Verify risk management citations
- TTL: 365 days

**IEC 62304:**
- Library ID: `iec-62304-2006-amd1-2015`
- Content: IEC 62304:2006+AMD1:2015 full text
- Use: Verify software lifecycle citations
- TTL: 365 days

**EU MDR:**
- Library ID: `eu-mdr-2017-745`
- Content: Regulation (EU) 2017/745 full text
- Use: Verify EU MDR citations
- TTL: 90 days (updates via corrigenda)

### Usage Pattern

```markdown
# Example: Verify FDA Citation

1. Extract citation from document: "21 CFR 820.30(g)"
2. Use Context7 MCP:
   - resolve-library-id("FDA 21 CFR 820")
   - get-library-docs(library_id, section="820.30(g)")
3. Compare document text with retrieved regulation text
4. Score as accurate if exact match, inaccurate if mismatch
```

---

## ARIA Integration

### Notion Databases

**Audit Log Database:**
- Purpose: Track document changes and decisions
- VALID Use: Inspectable dimension audit trail
- Fields: Timestamp, Agent, Action, Document, Changes, Rationale

**Document Registry:**
- Purpose: Track document versions and status
- VALID Use: Inspectable dimension version control
- Fields: Document ID, Version, Status, Author, Approval Status

**Quality Reports Database:**
- Purpose: Store VALID validation results
- VALID Use: Quality trending and improvement tracking
- Fields: Document ID, VALID Score, Dimension Scores, Grade, Pass/Fail

### Sequential Thinking MCP

**Use Cases:**
- Complex regulatory pathway analysis (multi-market submissions)
- Trade-off analysis (risk-benefit evaluation)
- Root cause analysis (quality gate failures)

**VALID Integration:**
- Activated with `--ultrathink` flag for complex decisions
- Used in Verified dimension for regulatory interpretation
- Applied in Inspectable dimension for decision rationale

---

## Quality Benchmarks

### Industry Averages (Regulatory Submissions)

**First Draft Quality:**
- Industry Average: 65-70 (Grade D/C)
- ARIA Target: 75+ (Grade C)
- Source: Internal QMS audit data (2023-2024)

**Final Submission Quality:**
- Industry Average: 85-90 (Grade B/A)
- ARIA Target: 90+ (Grade A)
- Source: Regulatory submission outcomes analysis

### Dimension-Specific Benchmarks

| Dimension | Industry Average | ARIA Target | Critical Threshold |
|-----------|-----------------|-------------|-------------------|
| Verified | 75-85 | 90+ | 70 |
| Accurate | 80-90 | 92+ | 70 |
| Linked | 70-80 | 88+ | 70 |
| Inspectable | 75-85 | 90+ | 70 |
| Deliverable | 85-95 | 95+ | 70 |

**Data Source:** Medical device QMS audit findings (ISO 13485 certified companies, n=50)

---

## Best Practice Resources

### Regulatory Writing

**Regulatory Focus - Quality Documentation Best Practices**
- URL: https://www.raps.org/
- Content: Templates, style guides, submission strategies
- VALID Impact: Accurate and Deliverable dimensions

**FDA Webinars and Training**
- URL: https://www.fda.gov/training-and-continuing-education
- Content: Design controls, software validation, clinical evaluation
- VALID Impact: All dimensions

### Traceability Tools

**Requirements Management Tools:**
- Jama Connect, IBM DOORS, Polarion
- Purpose: Bidirectional traceability automation
- VALID Impact: Linked dimension automation

**Quality Management Systems:**
- MasterControl, Greenlight Guru, ETQ Reliance
- Purpose: Document control and audit trail
- VALID Impact: Inspectable dimension automation

### Template Libraries

**Regulatory Documentation Templates:**
- 510(k) submission templates
- CE Technical File templates
- DHF/DMR templates
- VALID Impact: Deliverable dimension compliance

**Sources:**
- FDA.gov (public examples)
- Notified Body guidance (TÜV SÜD, BSI, MDC)
- Industry associations (AdvaMed, MedTech Europe)

---

## Training and Certification

### Regulatory Affairs Certification

**RAC (Regulatory Affairs Certification)**
- Organization: RAPS (Regulatory Affairs Professionals Society)
- Relevant Topics: Quality systems, documentation, submissions
- VALID Impact: Overall framework understanding

**CQA (Certified Quality Auditor)**
- Organization: ASQ (American Society for Quality)
- Relevant Topics: Audit techniques, documentation review
- VALID Impact: Inspectable dimension expertise

### Online Courses

**Design Controls and 21 CFR 820.30**
- Provider: FDA (free), OrielSTAT, Medical Device Academy
- Topics: DHF, traceability, design validation
- VALID Impact: Linked and Inspectable dimensions

**Clinical Evaluation Report Writing (EU MDR)**
- Provider: UL, TÜV SÜD, Emergo
- Topics: CER structure, MEDDEV 2.7/1 compliance
- VALID Impact: Verified, Accurate, Deliverable dimensions

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-02-09 | Initial reference document | ARIA Team |

---

## Related ARIA Skills

- **aria-writing-style** - Technical writing standards for regulatory documents
- **aria-templates** - Document template library for regulatory submissions
- **aria-research** - Research methodology for regulatory intelligence
- **aria-integration-context7** - Context7 MCP optimization for regulation lookup
- **aria-integration-notion** - Notion database integration for audit trail

---

## Feedback and Updates

This reference document is maintained by the ARIA team. For updates or corrections:

1. Submit feedback via `/aria feedback` command
2. Request specific regulation additions via team lead
3. Report broken links or outdated references

**Last Reviewed:** 2026-02-09
**Next Review:** 2026-05-09 (Quarterly)
