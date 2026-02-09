# Template References and Resources

External resources for regulatory document templates and formatting standards.

## Official Regulatory Templates

### FDA Templates

**510(k) Template**
- Source: FDA Center for Devices and Radiological Health (CDRH)
- URL: https://www.fda.gov/medical-devices/premarket-notification-510k/510k-template
- Content: Official FDA template for Traditional and Abbreviated 510(k) submissions
- Last Updated: Check FDA website for current version

**PMA Template**
- Source: FDA CDRH
- URL: https://www.fda.gov/medical-devices/premarket-approval-pma/pma-checklist
- Content: PMA application checklist and guidance
- Last Updated: Check FDA website for current version

**De Novo Template**
- Source: FDA CDRH
- URL: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request
- Content: De Novo classification request template
- Last Updated: Check FDA website for current version

### EU MDR Templates

**Technical Documentation Template**
- Source: European Commission, Medical Device Coordination Group (MDCG)
- URL: https://health.ec.europa.eu/medical-devices-topics-interest/guidance-mdcg-endorsed-documents-and-other-guidance_en
- Content: Templates for Annex II and Annex III technical documentation
- Key Document: MDCG 2019-9 (Summary of Safety and Clinical Performance)

**Clinical Evaluation Report Template**
- Source: MEDDEV 2.7/1 rev 4
- URL: https://ec.europa.eu/docsroom/documents/17522
- Content: CER structure and methodology
- Sections: Device description, literature review, clinical data analysis

**Declaration of Conformity Template**
- Source: EU MDR 2017/745, Annex IV
- URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32017R0745
- Content: EU Declaration of Conformity format requirements

## ISO Standards Templates

**ISO 13485 QMS Documentation Templates**

- **Quality Manual Template**: ISO 13485:2016, Section 4.2.2
- **Procedure Templates**: ISO 13485:2016, Section 4.2.3
- **Record Templates**: ISO 13485:2016, Section 4.2.4

**ISO 14971 Risk Management Templates**

- **Risk Management Plan Template**: ISO 14971:2019, Annex C
- **Risk Analysis Template (FMEA)**: ISO 14971:2019, Annex D
- **Risk Management Report Template**: ISO 14971:2019, Annex E

**IEC 62304 Software Documentation Templates**

- **Software Development Plan**: IEC 62304:2006+AMD1:2015, Section 5.1
- **Software Requirements Specification**: IEC 62304, Section 5.2
- **Software Design Specification**: IEC 62304, Section 5.3

## Industry Best Practice Templates

### RAPS (Regulatory Affairs Professionals Society)

**Website**: https://www.raps.org/

**Available Templates**:
- Regulatory submission checklists
- Gap analysis templates
- Regulatory strategy templates
- Post-market surveillance templates

**Access**: RAPS membership required for most resources

### MDIC (Medical Device Innovation Consortium)

**Website**: https://mdic.org/

**Available Templates**:
- Clinical evaluation templates
- Human factors templates
- Real-world evidence templates

**Access**: Publicly available resources

### Notified Body Guidance

**BSI Group**
- URL: https://www.bsigroup.com/en-GB/medical-devices/
- Content: Technical file guidance, templates, checklists

**TÜV SÜD**
- URL: https://www.tuvsud.com/en/services/product-certification/medical-devices-and-ivd
- Content: MDR/IVDR documentation guidance

## Template Formatting Standards

### Document Structure Standards

**IEEE 29148:2018** - Systems and Software Engineering — Life Cycle Processes — Requirements Engineering
- URL: https://standards.ieee.org/standard/29148-2018.html
- Content: Requirements document structure
- Applicable to: Technical specifications, requirements documents

**ISO/IEC/IEEE 26511:2018** - Systems and software engineering — Requirements for managers of information for users of systems, software, and services
- URL: https://www.iso.org/standard/67905.html
- Content: User documentation structure
- Applicable to: Instructions for use, user manuals

### Citation and Reference Standards

**AMA Manual of Style, 11th Edition**
- Publisher: American Medical Association
- Content: Citation format for medical literature
- Applicable to: Clinical evaluation reports, literature reviews

**The Bluebook: A Uniform System of Citation**
- Publisher: Harvard Law Review
- Content: Legal citation format
- Applicable to: Regulatory citations, legal references

## Template Automation Tools

### Document Generation Tools

**MedTech Confluence** (Commercial)
- Description: Regulatory document template library
- Features: Version control, collaboration, automated formatting

**Greenlight Guru** (Commercial)
- Description: QMS with built-in templates
- Features: eQMS integration, automated workflows

**PleaseReview** (Commercial)
- Description: Document review and approval automation
- Features: Approval workflows, version control, audit trail

### Open Source Tools

**Pandoc**
- URL: https://pandoc.org/
- Description: Universal document converter
- Use Case: Convert templates between formats (Markdown, DOCX, PDF)

**LaTeX Templates**
- URL: https://www.overleaf.com/latex/templates
- Description: Scientific document templates
- Use Case: Technical specifications, test reports

## ARIA Template Extensions

### Template Metadata Standards

ARIA templates extend base templates with:

**Frontmatter Schema**:
```yaml
---
template_id: unique-identifier
template_version: semver
template_type: base|custom|submission
regulatory_framework: FDA|EU|ISO|Generic
document_type: report|specification|review|submission
---
```

**Variable Substitution**:
```markdown
{{device_name}} - Auto-filled from device profile
{{project_code}} - Auto-filled from project metadata
{{date_iso}} - Auto-generated ISO date
```

**VALID Integration**:
- Verified: Regulatory citations auto-checked via Context7
- Accurate: Data fields validated against source
- Linked: Traceability auto-generated
- Inspectable: Revision history auto-tracked
- Deliverable: Export format compliance checked

### Template Repository

**ARIA Template Library Location**:
- Base Templates: `.claude/skills/aria-templates/templates/`
- Custom Templates: `.aria/custom-templates/`
- Organization Templates: `.aria/org-templates/` (if configured)

**Template Versioning**:
- Semantic versioning (MAJOR.MINOR.PATCH)
- Backward compatibility maintained for MINOR versions
- Breaking changes require MAJOR version increment

**Template Updates**:
- Base templates updated with regulatory changes
- Update notifications via ARIA
- Migration guides provided for breaking changes

## Collaborative Template Development

### Template Contribution Guidelines

For organizations building custom template libraries:

1. **Start with Base Template**: Extend existing ARIA templates
2. **Document Customizations**: Clear comments explaining changes
3. **Validate Against VALID**: Ensure quality framework compliance
4. **Version Control**: Use Git for template version management
5. **Peer Review**: Templates reviewed by RA/QA experts before deployment

### Template Governance

**Template Approval Process**:
1. Template created/modified
2. Quality review (VALID framework check)
3. Regulatory review (citation verification)
4. Pilot testing (generate sample document)
5. Approval and deployment

**Template Maintenance**:
- Quarterly review of base templates
- Annual audit of custom templates
- Immediate updates for regulation changes

## Additional Resources

### Training Resources

**FDA Training Materials**
- URL: https://www.fda.gov/training-and-continuing-education
- Content: Medical device regulation training, including documentation requirements

**ISO Training**
- URL: https://www.iso.org/training.html
- Content: ISO standards training and certification

**RAPS Learning Portal**
- URL: https://www.raps.org/learning
- Content: Regulatory affairs professional development

### Professional Communities

**LinkedIn Groups**:
- Medical Device Regulatory Affairs Professionals
- ISO 13485 Community
- FDA Regulatory Professionals

**Forums**:
- RAPS Regulatory Focus Community
- MedTech Quality Professionals
- ISO TC 210 (medical device standards committee)

### Books and Publications

**"Medical Device Regulatory Practices"** by Basavaraj K. Nanjwade
- Publisher: Academic Press
- Content: Comprehensive regulatory guidance including documentation

**"Design Controls for the Medical Device Industry"** by Marie Freebody
- Publisher: CRC Press
- Content: Design control documentation and templates

**"The FDA and Worldwide Medical Device Regulatory and Clinical Requirements"** by Brian R. MacLeod
- Publisher: Regulatory Control Systems
- Content: Multi-market regulatory submission guidance

---

## Template Quality Assurance

All ARIA templates undergo:

1. **Regulatory Validation**: Citations verified against source regulations
2. **Expert Review**: Reviewed by RA/QA professionals
3. **Field Testing**: Tested in real submissions
4. **User Feedback**: Continuously improved based on user feedback
5. **VALID Compliance**: Quality framework validation before release

For template issues or suggestions, use `/aria feedback` command.
