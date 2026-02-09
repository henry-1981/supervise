---
name: aria-templates
description: >
  Document template library for ARIA business documents. Provides standardized
  templates for regulatory submissions, technical reports, and business
  correspondence. Used by manager-docs and expert-writer for consistent
  document formatting and structure across all ARIA outputs.
license: Apache-2.0
compatibility: Designed for Claude Code
user-invocable: true
metadata:
  version: "1.0.0"
  category: "domain"
  status: "active"
  updated: "2025-02-09"
  modularized: "true"
  tags: "aria, templates, documents, formatting"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords: ["template", "document", "format", "structure"]
  agents: ["manager-docs", "expert-writer"]
  phases: ["brief", "execute", "deliver"]
  languages: ["en", "ko"]
---

# ARIA Document Templates

## Overview

This skill provides a comprehensive library of document templates for regulatory and technical documentation within the ARIA ecosystem.

## Template Categories

### 1. Regulatory Documents

#### Regulatory Submission Template
```markdown
# [Regulatory Type] Submission

**Document ID**: [DOC-YYYY-NNN]
**Version**: 1.0
**Date**: [YYYY-MM-DD]
**Author**: [Author Name]
**Status**: Draft | Review | Approved | Submitted

## Document Control

### Revision History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Name] | Initial release |

### Approval Record
| Role | Name | Signature | Date |
|------|------|-----------|------|
| Author | | | |
| Reviewer | | | |
| Approver | | | |

### Distribution
| Recipient | Type | Date |
|-----------|------|------|
| [Name] | [Type] | [Date] |

## Executive Summary

[2-3 paragraph overview of submission]

## Table of Contents
[Auto-generated]

## 1. Introduction

### 1.1 Purpose
[Statement of submission purpose]

### 1.2 Scope
[Boundaries of submission]

### 1.3 References
[Cited regulations and standards]

## 2. [Content Section]

[Regulatory-specific content]

## 3. Conclusion

[Summary and recommendations]

## Appendices

### Appendix A: Supporting Data
### Appendix B: Calculations
### Appendix C: Correspondence
```

### 2. Technical Reports

#### Technical Report Template
```markdown
# [Report Title]

**Document ID**: [DOC-YYYY-NNN]
**Version**: [X.Y.Z]
**Date**: [YYYY-MM-DD]
**Prepared by**: [Organization/Individual]
**Prepared for**: [Client/Stakeholder]

## Executive Summary

[Summary of key findings and recommendations]

## 1. Background

[Context and motivation for report]

## 2. Objectives

[Clear statement of report objectives]

## 3. Methodology

### 3.1 Approach
[Methods used]

### 3.2 Data Sources
[Origin of information]

### 3.3 Assumptions
[Key assumptions and limitations]

## 4. Findings

### 4.1 [Finding Category]
[Detailed findings]

### 4.2 [Finding Category]
[Detailed findings]

## 5. Analysis

[Interpretation of findings]

## 6. Recommendations

### 6.1 Priority Recommendations
[Immediate actions]

### 6.2 Future Considerations
[Long-term suggestions]

## 7. Conclusion

[Summary of report]

## References

[Cited sources]

## Appendices

[A. Data Tables]
[B. Technical Details]
[C. Glossary]
```

### 3. Quality Documents

#### Validation Report Template
```markdown
# [System/Process] Validation Report

**Document ID**: [VAL-YYYY-NNN]
**Version**: [X.Y.Z]
**Date**: [YYYY-MM-DD]

## Validation Summary

| Item | Status |
|------|--------|
| Validation Protocol | [Approved/Complete] |
| Installation Qualification | [Pass/Fail] |
| Operational Qualification | [Pass/Fail] |
| Performance Qualification | [Pass/Fail] |

## 1. Validation Overview

### 1.1 System Description
[System being validated]

### 1.2 Validation Approach
[Strategy and methodology]

## 2. Validation Protocol

### 2.1 Objectives
[Validation objectives]

### 2.2 Acceptance Criteria
[Defined criteria]

### 2.3 Test Cases
[Test scenarios]

## 3. Results

### 3.1 Installation Qualification
[IQ results]

### 3.2 Operational Qualification
[OQ results]

### 3.3 Performance Qualification
[PQ results]

## 4. Deviations

[Any deviations from protocol]

## 5. Conclusion

[Validation outcome]

## 6. Approvals

[Sign-off section]
```

### 4. Business Correspondence

#### Email Template
```markdown
Subject: [Clear, specific subject line]

Dear [Recipient Name],

[Opening: State purpose of email]

[Body: Main content in organized paragraphs]

[Closing: Next steps or call to action]

Best regards,
[Your Name]
[Title]
[Contact Information]

---
[Additional information if needed]
```

#### Memo Template
```markdown
# MEMORANDUM

**To**: [Recipient(s)]
**From**: [Sender]
**Date**: [YYYY-MM-DD]
**Subject**: [Clear subject]

## Purpose
[Statement of memo purpose]

## Background
[Context information]

## Details
[Main content]

## Action Required
[Any actions needed]

[Distribution list if applicable]
```

## Template Usage Guide

### Selecting the Right Template

#### By Document Type
- **Regulatory Submission**: Use Regulatory Submission Template
- **Technical Analysis**: Use Technical Report Template
- **Quality Validation**: Use Validation Report Template
- **Internal Communication**: Use Memo Template

#### By Purpose
- **Formal submission**: Regulatory templates
- **Information sharing**: Technical report templates
- **Decision making**: Business analysis templates
- **Documentation**: Quality record templates

### Customization Guidelines

#### Required Customizations
- Replace all bracketed placeholders
- Add organization-specific headers
- Include applicable standards
- Adjust for specific requirements

#### Optional Customizations
- Add organization branding
- Include supplementary sections
- Modify formatting to match style guide
- Add approval workflow sections

### Template Maintenance

#### Version Control
- Track template versions
- Document template changes
- Maintain change history
- Archive obsolete templates

#### Quality Assurance
- Regular template reviews
- User feedback collection
- Compliance verification
- Continuous improvement

## Template Components

### Standard Sections

#### Header Block
Always includes:
- Document title
- Document ID
- Version number
- Date
- Author/Preparer
- Status

#### Document Control
Always includes:
- Revision history table
- Approval record
- Distribution list
- Reference documents

#### Body Sections
Varies by document type but includes:
- Introduction/Purpose
- Main content
- Conclusions/Recommendations

#### Appendices
As needed:
- Detailed data
- Supporting calculations
- Reference materials
- Glossary

### Standard Tables

#### Revision History
| Version | Date | Author | Changes | Approval |
|---------|------|--------|---------|----------|
| 1.0 | [Date] | [Name] | [Description] | [Name] |

#### Approval Record
| Role | Name | Signature | Date |
|------|------|-----------|------|
| [Role] | [Name] | | [Date] |

#### Distribution List
| Recipient | Type | Date | Method |
|-----------|------|------|---------|
| [Name] | [Type] | [Date] | [Method] |

## Template Best Practices

### Do's
1. Use consistent formatting
2. Follow template structure
3. Complete all required fields
4. Maintain version control
5. Review before use
6. Customize appropriately

### Don'ts
1. Skip required sections
2. Mix document types
3. Use outdated templates
4. Ignore placeholder text
5. Modify without approval
6. Inconsistent formatting

## Creating Custom Templates

### Template Development Process

#### Step 1: Define Requirements
- Document purpose
- Target audience
- Required content
- Applicable standards

#### Step 2: Design Structure
- Section organization
- Heading hierarchy
- Table layouts
- Formatting standards

#### Step 3: Create Template
- Set up placeholders
- Add instructions
- Include examples
- Test with sample content

#### Step 4: Validate Template
- Review for completeness
- Test with real documents
- Gather user feedback
- Refine as needed

### Template Standards

#### Naming Convention
- Format: [type]-[subtype]-v[X.Y.Z]
- Example: regulatory-submission-v1.0.0
- Use lowercase with hyphens

#### Version Numbering
- Major version: Structural changes
- Minor version: Content additions
- Patch version: Corrections

#### File Organization
```
templates/
├── regulatory/
│   ├── submission-template.md
│   └── response-template.md
├── technical/
│   ├── report-template.md
│   └── analysis-template.md
├── quality/
│   ├── validation-template.md
│   └── deviation-template.md
└── business/
    ├── memo-template.md
    └── email-template.md
```

## Template Resources

### Quick Reference

#### Common Sections
- **Header**: ID, Version, Date, Author, Status
- **Control**: Revision History, Approvals, Distribution
- **Content**: Varies by document type
- **Appendices**: Supporting materials

#### Standard Placeholders
- [Document ID]: Unique identifier
- [Version]: X.Y.Z format
- [Date]: YYYY-MM-DD format
- [Author]: Name and title
- [Status]: Draft/Review/Approved

### Additional Resources

- **Style Guide**: See aria-writing-style
- **Quality Standards**: See aria-quality-valid
- **Research Methods**: See aria-research
- **Analysis Guidelines**: See aria-analysis
