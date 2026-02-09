# Custom Template Creation

Guide for creating organization-specific and project-specific templates.

## Why Create Custom Templates?

### Organization-Specific Requirements

Different organizations have unique needs:

- **Internal format standards**: Company-specific document structure
- **Additional review steps**: Extra approval checkpoints
- **Branding requirements**: Logo, header/footer, style
- **Proprietary processes**: Custom CAPA workflow, risk matrix

### Project-Specific Templates

Individual projects may require:

- **Device-specific sections**: Specialized testing for unique device types
- **Market-specific requirements**: Region-specific regulatory sections
- **Collaborative formats**: Multi-company submission packages
- **Expedited pathways**: Streamlined templates for fast-track submissions

## Custom Template Structure

### Basic Custom Template

```markdown
---
# Standard Template Metadata
template_id: custom-mycompany-design-review
template_version: 1.0.0
template_type: custom
base_template: review-report  # Optional: inherit from base template

# Customization Metadata
organization: MyCompany Medical Devices
author: Jane Doe, Director of Regulatory Affairs
created: 2026-02-09
regulatory_framework: FDA  # FDA, EU, ISO, or Custom

# ARIA Integration
aria_workflow: execute  # When this template is used
aria_agents: [expert-writer, expert-reviewer]  # Which agents can use it

# VALID Framework Customization
valid_custom_checks:
  - check_id: company_logo
    description: Verify company logo present on first page
  - check_id: approval_matrix
    description: Verify all required signatures per SOP-DR-001
---

# [DOCUMENT TITLE]

**Document Information**
- Document ID: [AUTO-GENERATED]
- Version: [SEMVER]
- Date: [ISO DATE]
- Template: {{template_id}} v{{template_version}}

**MyCompany Specific Information**
- Project Code: [PROJECT-CODE]
- Division: [DIVISION]
- Regulatory Strategy: [STRATEGY]

**Approval Matrix** (per SOP-DR-001)
- Design Engineer: [NAME] ________ Date: ________
- Quality Engineer: [NAME] ________ Date: ________
- Regulatory Affairs: [NAME] ________ Date: ________
- Medical Director: [NAME] ________ Date: ________  (Class III only)
- VP R&D: [NAME] ________ Date: ________

---

## Content Sections

[Custom sections follow...]

---

**MyCompany Footer**
Confidential and Proprietary
© 2026 MyCompany Medical Devices, Inc.
All rights reserved.
```

## Template Inheritance

### Inheriting from Base Templates

Custom templates can extend base templates:

```yaml
---
template_id: expedited-510k-mycompany
base_template: 510k-submission
template_version: 1.0.0

# Modifications to base template
modifications:
  # Add sections
  add_sections:
    - section_id: expedited-justification
      title: "Expedited Review Justification"
      position: after_device_description
      required: true

    - section_id: fda-guidance-compliance
      title: "FDA Guidance Compliance Matrix"
      position: before_conclusions
      required: true

  # Remove sections
  remove_sections:
    - traditional-510k-checklist

  # Modify sections
  modify_sections:
    - section_id: substantial-equivalence
      add_subsection: "Real-World Evidence"
      guidance: "Include post-market data from predicate device"
---
```

### Override Behavior

When inheriting, custom content overrides base:

**Base Template Section**:
```markdown
## Device Description

*Describe the device, its components, and operating principle.*
```

**Custom Template Override**:
```markdown
## Device Description

*Describe the device following MyCompany Device Description Standard (DDS-001).*

### Required Subsections (per DDS-001):
1. Device Overview
2. Components and Materials
3. Operating Principle
4. Unique Features
5. Accessories and Consumables
```

## Custom Sections

### Section Templates

Create reusable section templates:

**File**: `.aria/custom-templates/sections/mycompany-approval.md`

```markdown
## Approval Signatures

This document has been reviewed and approved by:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Author | [AUTHOR-NAME] | | [DATE] |
| Technical Reviewer | [REVIEWER-NAME] | | [DATE] |
| Quality Reviewer | [QA-REVIEWER-NAME] | | [DATE] |
| Regulatory Reviewer | [RA-REVIEWER-NAME] | | [DATE] |
| Approver | [APPROVER-NAME] | | [DATE] |

**Approval Status**: {{approval_status}}
**Electronic Signature**: {{esignature_enabled}}
```

**Usage in Custom Template**:
```markdown
{{include .aria/custom-templates/sections/mycompany-approval.md}}
```

### Dynamic Content

Templates support dynamic content generation:

```markdown
## Risk Analysis Summary

{{#if device_class == "Class III"}}
### Class III Risk Requirements

Per FDA guidance, Class III devices require comprehensive risk analysis:

- FMEA for all hazards
- FTA for catastrophic hazards
- Risk-benefit analysis
- Clinical data supporting safety claims

{{else if device_class == "Class II"}}
### Class II Risk Requirements

Per FDA guidance, Class II devices require:

- FMEA for significant hazards
- Risk controls for Medium/High risks
- Verification of risk control effectiveness

{{/if}}

**Risk Management Plan**: [RMP-{{project_code}}-{{version}}]
```

## Custom Variables

### Defining Custom Variables

Custom templates can define organization-specific variables:

```yaml
---
template_id: custom-design-validation
custom_variables:
  # Company information
  company_name: MyCompany Medical Devices, Inc.
  company_address: 123 Medical Park, Boston, MA
  company_qms_cert: ISO 13485:2016 Cert #12345

  # Project variables
  project_code: PROJ-2026-001
  project_manager: Jane Smith
  regulatory_lead: John Doe

  # Process variables
  design_review_sop: SOP-DR-001
  design_validation_sop: SOP-DV-002
  approval_matrix_sop: SOP-AP-003
---
```

### Variable Types

**Static Variables**: Fixed values
```yaml
company_name: MyCompany Medical Devices
regulatory_framework: FDA
```

**Computed Variables**: Derived from other variables
```yaml
document_id: "{{template_id}}-{{project_code}}-{{date_iso}}"
full_title: "{{document_type}} - {{device_name}} {{device_model}}"
```

**Lookup Variables**: Retrieved from Notion database
```yaml
device_name: "{{notion.device_registry.name}}"
project_status: "{{notion.project_tracker.status}}"
risk_level: "{{notion.risk_register.overall_risk}}"
```

## Custom Validation Rules

### VALID Framework Extensions

Add organization-specific validation rules:

```yaml
---
template_id: custom-510k
valid_custom_checks:
  - check_id: mycompany_logo_present
    dimension: Deliverable
    description: "Verify MyCompany logo on title page"
    severity: error
    validation_method: image_detection

  - check_id: project_code_format
    dimension: Trackable
    description: "Verify project code follows PROJ-YYYY-NNN format"
    severity: error
    validation_method: regex
    pattern: "^PROJ-\\d{4}-\\d{3}$"

  - check_id: approval_matrix_complete
    dimension: Inspectable
    description: "Verify all required approvals per SOP-AP-003"
    severity: error
    validation_method: signature_check
    required_roles: [Author, Technical_Reviewer, QA_Reviewer, RA_Reviewer, Approver]

  - check_id: confidentiality_footer
    dimension: Deliverable
    description: "Verify confidentiality footer on all pages"
    severity: warning
    validation_method: footer_check
---
```

### Custom Validation Scripts

Provide custom validation logic:

```python
# .aria/custom-templates/validators/project_code_validator.py

def validate_project_code(document):
    """Validate project code format and existence."""

    project_code = document.get_variable('project_code')

    # Check format: PROJ-YYYY-NNN
    if not re.match(r'^PROJ-\d{4}-\d{3}$', project_code):
        return {
            'valid': False,
            'error': f'Invalid project code format: {project_code}',
            'expected': 'PROJ-YYYY-NNN (e.g., PROJ-2026-001)'
        }

    # Check existence in Notion Project Tracker
    notion_result = notion_api.query_database(
        database_id=PROJECT_TRACKER_DB,
        filter={'Project Code': {'equals': project_code}}
    )

    if not notion_result:
        return {
            'valid': False,
            'error': f'Project code not found in Project Tracker: {project_code}',
            'suggestion': 'Create project in Notion first'
        }

    return {'valid': True}
```

## Template Packaging

### Template Package Structure

Organize custom templates in packages:

```
.aria/custom-templates/
├── mycompany-package/
│   ├── package.yaml          # Package metadata
│   ├── templates/
│   │   ├── design-review.md
│   │   ├── design-validation.md
│   │   └── 510k-submission.md
│   ├── sections/
│   │   ├── approval-matrix.md
│   │   ├── company-header.md
│   │   └── confidentiality-footer.md
│   ├── validators/
│   │   ├── project_code.py
│   │   └── approval_matrix.py
│   └── assets/
│       ├── logo.png
│       └── letterhead.pdf
```

### Package Metadata

**File**: `package.yaml`

```yaml
---
package_id: mycompany-regulatory-templates
package_version: 1.0.0
package_name: MyCompany Regulatory Templates
package_description: |
  Custom regulatory templates for MyCompany Medical Devices
  following internal SOPs and FDA/EU MDR requirements.

author:
  name: Jane Doe
  email: jane.doe@mycompany.com
  organization: MyCompany Medical Devices

compatibility:
  aria_version: ">=1.0.0"
  base_templates: ["regulatory-report", "510k-submission", "review-report"]

templates:
  - template_id: mycompany-design-review
    file: templates/design-review.md
    description: Design review report per SOP-DR-001

  - template_id: mycompany-design-validation
    file: templates/design-validation.md
    description: Design validation report per SOP-DV-002

  - template_id: mycompany-510k
    file: templates/510k-submission.md
    description: FDA 510(k) submission with MyCompany branding

sections:
  - section_id: mycompany-approval
    file: sections/approval-matrix.md
  - section_id: mycompany-header
    file: sections/company-header.md

validators:
  - validator_id: project_code
    file: validators/project_code.py
  - validator_id: approval_matrix
    file: validators/approval_matrix.py

assets:
  - asset_id: company_logo
    file: assets/logo.png
    usage: title_page
  - asset_id: letterhead
    file: assets/letterhead.pdf
    usage: document_background
---
```

### Package Installation

Install custom template package:

```
/aria template install .aria/custom-templates/mycompany-package/
```

ARIA performs:
1. Validate package structure
2. Check compatibility
3. Install templates to catalog
4. Register validators
5. Import assets
6. Update template index

## Best Practices

### 1. Start with Base Templates

Always extend base templates rather than creating from scratch:

**Good**: Inherit from `510k-submission.md` and add company sections
**Poor**: Create entirely new 510(k) template

**Rationale**: Base templates are maintained and updated with regulatory changes

### 2. Document Customizations

Add clear comments explaining customizations:

```markdown
<!-- MyCompany Custom Section: Added per SOP-DR-001 v2.3 -->
## Executive Summary for Management

*One-page summary for executive review committee.*

<!-- End Custom Section -->
```

### 3. Version Custom Templates

Use semantic versioning for custom templates:

```yaml
template_version: 1.0.0  # Initial release
template_version: 1.1.0  # Add new section (backward compatible)
template_version: 2.0.0  # Change structure (breaking change)
```

### 4. Test Before Deployment

Test custom templates before organization-wide deployment:

```
/aria template test mycompany-design-review --validate
/aria template test mycompany-design-review --generate-sample
/aria template test mycompany-design-review --valid-check
```

### 5. Maintain Synchronization

Keep custom templates synchronized with base template updates:

```
Base Template Update: 510k-submission.md v1.0.0 → v2.0.0
Action Required: Review custom template mycompany-510k for compatibility
Update custom template to incorporate regulatory changes
```

## Troubleshooting

### Issue: Template Inheritance Not Working

**Symptom**: Custom template doesn't inherit from base template

**Causes**:
- Incorrect `base_template` reference
- Base template not found
- Circular inheritance

**Solution**:
```yaml
# Verify base template exists
/aria template list --show-base

# Fix reference
base_template: 510k-submission  # Correct
base_template: templates/510k-submission.md  # Wrong (don't include path)
```

### Issue: Custom Variables Not Substituted

**Symptom**: `{{custom_variable}}` not replaced in output

**Causes**:
- Variable not defined in template metadata
- Variable name typo
- Syntax error in variable reference

**Solution**:
```yaml
# Define all variables in frontmatter
custom_variables:
  project_code: PROJ-2026-001

# Use correct syntax
{{project_code}}  # Correct
{{project-code}}  # Wrong (use underscore)
${project_code}  # Wrong (wrong syntax)
```

### Issue: Custom Validation Failing

**Symptom**: Document fails custom validation checks

**Debug Steps**:
```
/aria template validate DOC-ID --debug
/aria template validate DOC-ID --show-custom-checks
/aria template validate DOC-ID --skip-custom  # Test without custom checks
```

## Example: Complete Custom Template

See `templates/examples/custom-template-example.md` for a complete working example of a custom template with:

- Template inheritance
- Custom sections
- Dynamic content
- Custom variables
- Custom validation rules
- Package structure
