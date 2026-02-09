# Template Usage Guide

How to effectively use ARIA regulatory document templates.

## Getting Started

### Step 1: Select Template

Choose the appropriate template based on your task:

```
Task: Create 510(k) submission for Class II device
→ Template: templates/510k-submission.md

Task: Document design verification results
→ Template: templates/design-verification.md

Task: Prepare clinical evaluation for EU submission
→ Template: templates/clinical-evaluation.md
```

### Step 2: Generate Document

Use ARIA template command to generate from template:

```
/aria template generate 510k-submission --device "Blood Glucose Monitor XYZ-100"
```

This creates a new document with:
- Auto-generated document ID
- Pre-filled device information
- Guidance text in place
- Version control initialized

### Step 3: Fill Content

Replace placeholders and guidance text:

**Placeholders** (in brackets):
```markdown
Device Name: [DEVICE-NAME]
→ Device Name: Blood Glucose Monitor XYZ-100

Manufacturer: [MANUFACTURER]
→ Manufacturer: MedTech Innovations, Inc.
```

**Guidance Text** (italicized):
```markdown
*Describe the intended use in one clear sentence.*
→ The device is intended for quantitative measurement of glucose in capillary whole blood for diabetes management in the home setting.
```

### Step 4: Validate

Run VALID framework validation:

```
/aria template validate DOC-510K-2026-001
```

Checks:
- All placeholders filled
- Regulatory citations present
- Traceability complete
- Format compliance

### Step 5: Submit for Review

Sync to Notion Document Registry:

```
/aria deliver sync DOC-510K-2026-001
```

Creates:
- Notion page in Document Registry
- Approval workflow
- Version history tracking

## Template Workflows

### Workflow 1: Submission Document

**Scenario**: Preparing FDA 510(k) submission

**Steps**:
1. Generate from `510k-submission.md` template
2. Fill device description and intended use
3. Complete substantial equivalence section
4. Add performance testing summary
5. Attach labeling documents
6. Validate with VALID framework
7. Submit for regulatory review approval

**Typical Duration**: 2-4 weeks

**Key Checkpoints**:
- Predicate device selection (requires approval)
- Substantial equivalence rationale (requires approval)
- Performance data completeness (requires validation)
- Labeling accuracy (requires review)

### Workflow 2: Design Control Document

**Scenario**: Design verification report

**Steps**:
1. Generate from `design-verification.md` template
2. Link design input requirements (traceability)
3. Reference test protocols
4. Fill test results tables
5. Document pass/fail decisions
6. Address any deviations
7. Validate with VALID framework
8. Submit for design review approval

**Typical Duration**: 1-2 weeks

**Key Checkpoints**:
- All design inputs have corresponding verification tests
- Acceptance criteria are objective and measurable
- Test results meet acceptance criteria
- Deviations have documented corrective actions

### Workflow 3: Risk Management Document

**Scenario**: Risk management report for ISO 14971 compliance

**Steps**:
1. Generate from `risk-management-report.md` template
2. Reference Risk Management Plan
3. Summarize FMEA/FTA results
4. Complete risk evaluation against criteria
5. Document risk controls
6. Perform risk-benefit analysis
7. Validate with VALID framework
8. Submit for risk management review

**Typical Duration**: 2-3 weeks

**Key Checkpoints**:
- All identified hazards assessed
- Risk controls implemented for Medium/High risks
- Residual risks evaluated and acceptable
- Overall residual risk acceptable per plan

## Advanced Features

### Variable Substitution

Templates support auto-substitution from device profile:

**Device Profile** (stored in Notion):
```yaml
device_name: Blood Glucose Monitor XYZ-100
device_model: XYZ-100
manufacturer: MedTech Innovations, Inc.
device_class: Class II
regulatory_pathway: 510(k)
intended_use: Quantitative glucose measurement in capillary blood
```

**Template Usage**:
```markdown
Device: {{device_name}}
Model: {{device_model}}
Manufacturer: {{manufacturer}}
```

**Auto-Generated Output**:
```markdown
Device: Blood Glucose Monitor XYZ-100
Model: XYZ-100
Manufacturer: MedTech Innovations, Inc.
```

### Conditional Sections

Templates include conditional sections based on device characteristics:

```markdown
{{#if device_class == "Class III"}}
## Premarket Approval (PMA) Requirements

*This section is required for Class III devices only.*

{{/if}}
```

### Traceability Linking

Templates auto-link to related documents:

```markdown
Design Inputs:
- REQ-001 → [User Requirements Specification v2.0](notion://...)
- REQ-002 → [Technical Specification v1.5](notion://...)

Verification Tests:
- TP-001 → [Test Protocol TP-001 v1.0](notion://...)
- TR-001 → [Test Report TR-001 v1.0](notion://...)
```

### Regulatory Citation Verification

Templates integrate with Context7 MCP for citation verification:

```markdown
Per ISO 13485:2016, Section 7.3.6...
[Context7 Auto-Check: ✓ Current version, ✓ Section exists]

Per 21 CFR 820.30(f)...
[Context7 Auto-Check: ✓ Current regulation, ✓ Cited correctly]
```

## Template Customization

### Creating Custom Templates

Users can create organization-specific templates:

1. Copy base template from `templates/`
2. Add custom sections
3. Modify guidance text
4. Save to `.aria/custom-templates/`
5. Register in template catalog

**Example Custom Template**:

```markdown
---
template_id: custom-design-review
template_version: 1.0.0
base_template: review-report
organization: MedTech Innovations
---

# Design Review Report - MedTech Innovations Format

## Company-Specific Sections

### Executive Summary
*One-page summary for senior management.*

### Regulatory Impact Assessment
*Analysis of regulatory implications.*

### Commercial Viability
*Market analysis and competitive positioning.*

[... standard review sections follow ...]
```

### Template Inheritance

Custom templates can inherit from base templates:

```yaml
---
template_id: expedited-510k
base_template: 510k-submission
modifications:
  - remove_section: "Traditional 510(k) Sections"
  - add_section: "Expedited Review Justification"
  - add_section: "FDA Guidance Compliance Matrix"
---
```

### Section Reuse

Templates support section reuse across documents:

```markdown
{{include templates/sections/approval-block.md}}
{{include templates/sections/revision-history.md}}
{{include templates/sections/regulatory-references.md}}
```

## Best Practices

### 1. Start with Template Selection

Always start with the most specific template available:

**Good**: Use `510k-submission.md` for FDA 510(k)
**Poor**: Use generic `regulatory-report.md` and customize heavily

### 2. Fill Sequentially

Complete sections in order:

1. Document information (metadata)
2. Regulatory references
3. Device description
4. Technical content
5. Conclusions
6. Approval signatures

### 3. Preserve Traceability

Maintain document links as you fill:

```markdown
Bad: "Requirements are verified by testing."
Good: "Requirements [REQ-001] through [REQ-050] are verified by test protocols [TP-001] through [TP-010] with results documented in [TR-001] through [TR-010]."
```

### 4. Validate Early and Often

Run VALID checks after each major section:

```
/aria template validate DOC-510K-2026-001 --section "Device Description"
/aria template validate DOC-510K-2026-001 --section "Substantial Equivalence"
/aria template validate DOC-510K-2026-001 --full
```

### 5. Use Version Control

Commit after each significant update:

```
Document v1.0 → Initial draft from template
Document v1.1 → Device description completed
Document v1.2 → Substantial equivalence analysis completed
Document v2.0 → Reviewer feedback incorporated
Document v3.0 → Approved final version
```

## Common Mistakes

### Mistake 1: Incomplete Placeholder Replacement

**Problem**: Leaving `[PLACEHOLDER]` text in final document

**Detection**: VALID framework flags unreplaced placeholders

**Solution**: Search for `[` before final validation

### Mistake 2: Inconsistent Terminology

**Problem**: Using multiple terms for the same concept

**Detection**: VALID framework checks terminology consistency

**Solution**: Reference aria-writing-style terminology list

### Mistake 3: Missing Citations

**Problem**: Regulatory claims without source references

**Detection**: VALID framework requires citations for all claims

**Solution**: Use Context7 to verify and format citations correctly

### Mistake 4: Broken Traceability

**Problem**: Referenced documents don't exist or versions mismatch

**Detection**: VALID framework validates all links

**Solution**: Verify links before finalizing document

### Mistake 5: Non-Standard Format

**Problem**: Deviating from template structure without justification

**Detection**: Template diff check shows unexpected changes

**Solution**: Use template inheritance for intentional modifications

## Troubleshooting

### Issue: Template Not Found

**Symptom**: `/aria template generate` fails with "template not found"

**Causes**:
- Typo in template name
- Template not in catalog
- Custom template not registered

**Solution**:
```
/aria template list  # Show available templates
/aria template search "510k"  # Search by keyword
```

### Issue: Validation Failures

**Symptom**: VALID framework reports multiple errors

**Common Causes and Fixes**:
- Unreplaced placeholders → Search and replace all `[...]`
- Missing citations → Add regulatory references
- Broken links → Update document IDs
- Inconsistent terminology → Use aria-writing-style glossary

### Issue: Auto-Substitution Not Working

**Symptom**: Variables like `{{device_name}}` not replaced

**Causes**:
- Device profile not created in Notion
- Variable name typo
- Template syntax error

**Solution**:
```
/aria device profile show  # Verify device data
/aria template debug DOC-ID  # Show substitution log
```

## Templates + ARIA Workflows

### Integration with Brief Phase

During task briefing, ARIA suggests appropriate templates:

```
User: "I need to prepare a 510(k) submission"

ARIA Brief Phase:
- Analyzes task type → Submission document
- Suggests template → 510k-submission.md
- Identifies required data → Device profile, predicate device, test data
- Creates action plan → Template-based workflow
```

### Integration with Execute Phase

During execution, ARIA assists with template completion:

```
ARIA Execute Phase:
- Loads template
- Guides section-by-section completion
- Validates content against VALID framework
- Verifies citations via Context7
- Maintains traceability links
```

### Integration with Deliver Phase

During delivery, ARIA prepares final output:

```
ARIA Deliver Phase:
- Final VALID validation
- Format conversion (MD → PDF/DOCX)
- Sync to Notion Document Registry
- Generate submission package
- Create audit trail
```

## Template Maintenance

### Version Control

Templates are versioned independently:

```
templates/510k-submission.md v1.0.0 → Initial release
templates/510k-submission.md v1.1.0 → Add expedited review section
templates/510k-submission.md v2.0.0 → FDA guidance update (breaking change)
```

### Update Notifications

ARIA notifies when templates have updates:

```
Warning: Template '510k-submission.md' has a newer version (v2.0.0).
Current document uses v1.0.0.
Recommendation: Review changes before upgrading.
```

### Template Quality

All templates undergo VALID validation:

- Verified: Citations checked against source regulations
- Accurate: Guidance text reviewed by RA/QA experts
- Linked: Traceability examples validated
- Inspectable: Template change history maintained
- Deliverable: Output format tested with regulatory bodies
