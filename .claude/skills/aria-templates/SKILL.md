---
name: aria-templates
description: >
  Document template library for medical device regulatory documentation.
  Provides ready-to-use templates for common regulatory documents
  with usage guides and customization support.
license: Apache-2.0
compatibility: Designed for Claude Code with ARIA
user-invocable: false
metadata:
  version: "1.0.0"
  category: "domain"
  status: "active"
  updated: "2026-02-09"
  modularized: "true"
  tags: "aria, regulatory, templates, documentation"
  author: "MoAI-ADK Team"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 300
  level2_tokens: 3000

# MoAI Extension: Triggers
triggers:
  keywords: ["template", "document", "report", "submission"]
  agents: ["expert-writer", "manager-docs"]
  phases: ["execute", "deliver"]
---

# ARIA Document Templates

Regulatory document templates for medical device RA/QA workflows.

## Template Catalog

### Core Regulatory Templates

**Submission Documents**
- `regulatory-report.md` - General regulatory report structure
- `510k-submission.md` - FDA 510(k) premarket notification
- `ce-technical-file.md` - EU MDR technical documentation
- `clinical-evaluation.md` - Clinical evaluation report per MEDDEV 2.7/1

**Quality Management**
- `design-verification.md` - Design verification report
- `design-validation.md` - Design validation report
- `risk-management-report.md` - Risk management summary per ISO 14971
- `capa-report.md` - Corrective and preventive action report

**Technical Documentation**
- `technical-spec.md` - Technical specification document
- `user-requirements.md` - User requirements specification
- `software-requirements.md` - Software requirements per IEC 62304
- `interface-control.md` - Interface control document

**Review and Audit**
- `review-report.md` - Design review/document review report
- `audit-report.md` - Internal/external audit report
- `test-protocol.md` - Test protocol template
- `test-report.md` - Test report template

### Quick Template Selection

| Document Type | Template | Use When |
|--------------|----------|----------|
| FDA 510(k) submission | `510k-submission.md` | Preparing premarket notification |
| EU MDR technical file | `ce-technical-file.md` | Preparing CE marking documentation |
| Clinical data | `clinical-evaluation.md` | Demonstrating safety and performance |
| Design verification | `design-verification.md` | Verifying design outputs meet inputs |
| Design validation | `design-validation.md` | Validating device meets user needs |
| Risk management | `risk-management-report.md` | Summarizing risk analysis and controls |
| CAPA | `capa-report.md` | Documenting corrective/preventive actions |
| Technical specs | `technical-spec.md` | Defining device requirements |
| Reviews | `review-report.md` | Documenting design/document reviews |
| Audits | `audit-report.md` | Recording audit findings and responses |

## Template Structure

All templates follow consistent structure:

```markdown
# [Document Title]

**Document Information**
- Document ID: [AUTO-GENERATED]
- Version: [SEMVER]
- Date: [ISO DATE]
- Status: Draft/Review/Approved

**Regulatory References**
- [Applicable regulations and standards]

**Approval**
- Author: [NAME]
- Reviewer: [NAME]
- Approver: [NAME]

---

## [Content Sections]
[Template-specific sections with guidance]

---

**Revision History**
| Version | Date | Author | Changes |
|---------|------|--------|---------|
```

## Using Templates

### Basic Usage

1. Select appropriate template from catalog
2. Generate document from template
3. Fill in bracketed placeholders `[PLACEHOLDER]`
4. Replace guidance text (italicized) with actual content
5. Review against VALID quality framework
6. Submit for approval

### Template Variables

Common variables across all templates:

- `[DOCUMENT-ID]` - Auto-generated unique identifier
- `[VERSION]` - Semantic version (1.0.0)
- `[DATE]` - ISO 8601 format (2026-02-09)
- `[DEVICE-NAME]` - Device commercial name
- `[DEVICE-MODEL]` - Device model number
- `[MANUFACTURER]` - Legal manufacturer name
- `[AUTHOR]` - Document author name
- `[REVIEWER]` - Document reviewer name
- `[APPROVER]` - Document approver name

### Customization Support

For template customization guide, see `modules/custom.md`.

For detailed template library, see `modules/library.md`.

For template usage patterns, see `modules/usage-guide.md`.

## Integration Points

### Notion MCP Integration

Templates automatically integrate with Notion databases:

- Document Registry tracks all generated documents
- Template metadata synced to Notion
- Version control via Notion page history
- Approval workflows via Notion database

### Context7 MCP Integration

Templates include regulatory citations that can be verified via Context7:

- Automatic regulation lookup
- Standard version verification
- Hyperlinked citations in output

## Quality Standards

All templates enforce VALID framework:

- **Verified**: Citations match source regulations
- **Accurate**: Data fields require validation
- **Linked**: Traceability matrices included
- **Inspectable**: Revision history mandatory
- **Deliverable**: Export formats supported

## Usage

This skill is automatically loaded when:
- Creating regulatory documents
- Standardizing document formats
- Generating submission packages

Agents that use this skill:
- expert-writer: Document creation
- manager-docs: Template management
