# ARIA Skills Reference

Complete guide to ARIA (AI Regulatory Intelligence Assistant) skills for business workflow automation.

## Overview

ARIA skills implement the VALID framework and business workflow methodologies for regulatory intelligence and technical documentation. These skills support the Brief-Execute-Deliver workflow used by ARIA agents.

**Core Skills:**
- **aria-quality-valid**: VALID framework quality validation
- **aria-writing-style**: Technical writing standards
- **aria-templates**: Document template library
- **aria-research**: Regulatory research methodology
- **aria-analysis**: Data analysis for regulatory intelligence

---

## aria-quality-valid

### Purpose

VALID framework quality validation system for regulatory and technical documents. Ensures documents meet Verified, Accurate, Linked, Inspectable, and Deliverable quality standards.

### When to Use

- Validating regulatory documents for compliance
- Quality gate validation before document delivery
- Document review and improvement recommendations
- Preparing documents for regulatory submission

### VALID Dimensions

**V - Verified**

Content matches original regulatory text.

- Cross-reference with original regulations
- Verify interpretation accuracy
- Check for misinterpretation or misquotation

**A - Accurate**

Data, figures, and references are correct and current.

- Validate numerical data and statistics
- Verify reference currency and relevance
- Check calculation accuracy

**L - Linked**

Traceability between requirements, documents, and evidence.

- Maintain traceability matrix
- Link requirements to evidence
- Ensure audit trail completeness

**I - Inspectable**

Audit trail maintained with documented decision rationale.

- Document decision-making process
- Maintain change history
- Provide audit evidence

**D - Deliverable**

Output meets submission format requirements.

- Template compliance check
- Format validation
- Delivery requirement verification

### Usage Examples

Basic quality validation:

```
Use the aria-quality-valid skill to validate this regulatory document
for VALID framework compliance. Check all five dimensions and provide
improvement recommendations.
```

Comprehensive quality report:

```
Apply aria-quality-valid framework to generate a comprehensive quality
report for this technical specification. Include dimension scores,
specific findings, and actionable improvement recommendations.
```

Pre-submission validation:

```
Validate this document against aria-quality-valid standards before
regulatory submission. Ensure all five dimensions meet threshold
criteria and document any deficiencies.
```

### Related Agents

- **manager-quality**: Primary consumer for quality gate validation
- **expert-reviewer**: Uses for document review assessment
- **manager-docs**: Integrates into document workflow

### Quality Scoring

Each dimension scored 0-100 with weighted overall score:

- Verified: 25%
- Accurate: 25%
- Linked: 20%
- Inspectable: 15%
- Deliverable: 15%

Passing threshold: 80% overall, minimum 70% per dimension.

### Improvement Recommendations

The skill provides actionable recommendations:

1. Specific issues identified by dimension
2. Priority ranking (Critical, High, Medium, Low)
3. Remediation steps with examples
4. Re-validation checklist

---

## aria-writing-style

### Purpose

Technical writing style guide for regulatory and technical documentation. Ensures clarity, consistency, and compliance with industry standards.

### When to Use

- Creating regulatory documentation
- Writing technical specifications
- Standardizing document language
- Maintaining terminology consistency

### Style Guidelines

**Clarity Principles**

- Use simple, direct language
- Avoid jargon unless defined
- One concept per sentence
- Active voice preferred

**Structure Standards**

- Logical document organization
- Clear heading hierarchy
- Consistent section numbering
- Parallel structure in lists

**Terminology Management**

- Define terms on first use
- Use established glossary
- Maintain term consistency
- Document acronyms and abbreviations

**Sentence Structure**

- Average 15-20 words per sentence
- Limit one subordinate clause
- Place modifiers correctly
- Use parallel construction

### Usage Examples

Style checking:

```
Review this document using aria-writing-style guidelines. Check for
clarity, consistency, and terminology usage. Provide specific
improvements for non-compliant sections.
```

Terminology standardization:

```
Apply aria-writing-style terminology management to ensure consistent
term usage throughout this document. Identify undefined terms and
inconsistent usage.
```

Rewrite for clarity:

```
Rewrite this section following aria-writing-style clarity principles.
Simplify complex sentences, remove jargon, and improve readability
while maintaining technical accuracy.
```

### Related Agents

- **expert-writer**: Primary consumer for document creation
- **expert-reviewer**: Uses for style validation
- **manager-docs**: Integrates into document templates

### Document Types

Supports multiple document types:

- Regulatory submissions
- Technical specifications
- Standard operating procedures
- User manuals
- Compliance reports
- Validation protocols

### Language Support

- English (primary)
- Korean (한국어)
- Bilingual documentation

---

## aria-templates

### Purpose

Document template library for regulatory and technical documentation. Provides standardized templates with pre-defined structure, formatting, and content placeholders.

### When to Use

- Creating new regulatory documents
- Standardizing document formats
- Accelerating document creation
- Ensuring compliance with submission requirements

### Template Categories

**Regulatory Documents**

- Regulatory submission templates
- Compliance reports
- Validation protocols
- Risk assessment documents
- CAPA (Corrective and Preventive Action) reports

**Technical Documents**

- Technical specifications
- Design documents
- Test protocols
- User manuals
- Installation guides

**Project Management**

- Project plans
- Status reports
- Meeting minutes
- Requirements documents
- Change requests

### Template Features

**Structure**

- Pre-defined document outline
- Section headers with numbering
- Placeholder text for content
- Formatting and styles applied

**Placeholders**

- Variable substitution support
- Conditional sections
- Reusable components
- Version control markers

**Customization**

- User-defined templates
- Template inheritance
- Section override capability
- Custom field support

### Usage Examples

Create document from template:

```
Use aria-templates to create a regulatory submission document from
the FDA 510(k) template. Fill in required placeholders and maintain
template structure.
```

List available templates:

```
Show all available templates in aria-templates library. Categorize
by document type and include template descriptions and use cases.
```

Customize template:

```
Create a custom template based on the technical specification
template. Add company-specific sections and customize placeholder
fields for our standard format.
```

### Related Agents

- **manager-docs**: Primary consumer for document generation
- **expert-writer**: Uses for document creation
- **manager-project**: Uses for project documentation

### Template Parameters

Common template parameters:

- `{{project_name}}`: Project identifier
- `{{document_id}}`: Document tracking ID
- `{{version}}`: Document version number
- `{{date}}`: Creation/modification date
- `{{author}}`: Document author
- `{{approver}}`: Approval authority
- `{{custom_fields}}`: User-defined fields

### Template Versioning

Templates include version control:

- Template version tracking
- Change history logging
- Compatibility notes
- Migration guides

---

## aria-research

### Purpose

Regulatory research methodology for systematic information gathering, source verification, and citation management. Ensures research quality and traceability.

### When to Use

- Investigating regulatory requirements
- Researching standards and guidance
- Gathering competitive intelligence
- Preparing regulatory submissions

### Research Methodology

**Information Sources**

- Official regulatory body websites (FDA, EMA, PMDA, etc.)
- International standards organizations (ISO, IEC, IEEE)
- Industry guidance documents
- Scientific literature and journals
- Legal databases and precedents

**Source Evaluation**

- Authority assessment
- Currency verification
- Relevance scoring
- Reliability rating

**Citation Standards**

- Complete reference information
- Permanent links (DOI, URL)
- Access date documentation
- Version specification

### Research Process

1. **Define Research Scope**

   - Identify research questions
   - Determine information needs
   - Set search boundaries

2. **Source Discovery**

   - Systematic search strategy
   - Multiple source consultation
   - Expert consultation when needed

3. **Information Extraction**

   - Relevant content identification
   - Key point extraction
   - Context preservation

4. **Verification**

   - Source validation
   - Cross-reference checking
   - Expert review

5. **Documentation**

   - Proper citation formatting
   - Source archiving
   - Audit trail maintenance

### Usage Examples

Research regulatory requirement:

```
Use aria-research methodology to investigate FDA software validation
requirements for medical devices. Identify relevant guidances,
extract key requirements, and provide proper citations.
```

Multi-jurisdictional research:

```
Research medical device registration requirements across US, EU,
and Japan using aria-research standards. Compare requirements and
identify commonalities and differences with proper source citation.
```

Source verification:

```

Verify the accuracy of this regulatory claim using aria-research
source evaluation criteria. Confirm currency, authority, and
reliability of cited sources.
```

### Related Agents

- **expert-researcher**: Primary consumer for research tasks
- **expert-analyst**: Uses research for analysis
- **manager-quality**: Validates research quality

### Quality Criteria

Research quality assessed on:

- Source authority (official bodies preferred)
- Information currency (within 12 months preferred)
- Citation completeness (all required elements present)
- Traceability (audit trail maintained)
- Relevance (directly addresses research question)

### Integration

Integrates with MCP servers:

- **Context7**: Official document lookup
- **Notion**: Research repository
- **Sequential Thinking**: Complex research planning

---

## aria-analysis

### Purpose

Data analysis methodology for regulatory intelligence, including statistical analysis, trend identification, and predictive modeling for regulatory decision-making.

### When to Use

- Analyzing regulatory data and trends
- Evaluating submission success rates
- Identifying regulatory patterns
- Preparing analytical reports

### Analysis Techniques

**Descriptive Statistics**

- Frequency distributions
- Central tendency measures
- Variability indicators
- Correlation analysis

**Trend Analysis**

- Time series analysis
- Pattern identification
- Seasonality detection
- Outlier identification

**Comparative Analysis**

- Cross-jurisdictional comparison
- Competitor benchmarking
- Historical comparison
- Best practice identification

**Predictive Modeling**

- Regression analysis
- Classification models
- Clustering techniques
- Scenario modeling

### Visualization

**Chart Types**

- Line charts (trends over time)
- Bar charts (comparisons)
- Pie charts (distributions)
- Scatter plots (correlations)
- Heat maps (patterns)

**Visualization Principles**

- Clear labeling and titles
- Appropriate scale selection
- Color accessibility (WCAG 2.1)
- Simplified presentation

### Usage Examples

Regulatory trend analysis:

```
Apply aria-analysis methodology to identify trends in FDA 510(k)
submission data over the past 5 years. Include statistical summary,
trend visualization, and predictive insights.
```

Competitor analysis:

```

Analyze competitor regulatory submission success rates using
aria-analysis techniques. Compare submission types, timing, and
outcomes with statistical significance testing.
```

Risk assessment:

```

Perform quantitative risk analysis for regulatory compliance using
aria-analysis statistical methods. Calculate probability distributions
and confidence intervals for key risk factors.
```

### Related Agents

- **expert-analyst**: Primary consumer for analysis tasks
- **expert-researcher**: Provides research data
- **manager-quality**: Validates analytical quality

### Statistical Standards

Follows industry standards:

- FDA Statistical Guidance for Medical Devices
- ICH E9 Statistical Principles
- ISO 3534 Statistics vocabulary
- ASA ethical guidelines

### Reporting

Analysis reports include:

- Executive summary
- Methodology description
- Data sources and limitations
- Statistical findings
- Visualizations
- Conclusions and recommendations
- Appendices with detailed calculations

---

## Skill Integration

### Workflow Integration

Skills integrate into Brief-Execute-Deliver workflow:

**Brief Phase:**
- aria-research: Requirement investigation
- aria-analysis: Baseline data analysis

**Execute Phase:**
- aria-writing-style: Content creation
- aria-templates: Document generation
- aria-quality-valid: Ongoing validation

**Deliver Phase:**
- aria-quality-valid: Final quality gate
- aria-templates: Format compliance

### Progressive Disclosure

Each skill uses 3-level progressive disclosure:

**Level 1** (Metadata, ~100 tokens):
- Name, description, version
- Trigger keywords and agents
- Quick reference summary

**Level 2** (Implementation, ~5000 tokens):
- Detailed usage instructions
- Methodology and standards
- Integration patterns

**Level 3** (Advanced, unlimited):
- Complete reference documentation
- Working examples
- External resources

### MCP Integration

Skills integrate with MCP servers:

- **Context7**: Official document lookup
- **Sequential Thinking**: Complex analysis
- **Notion**: Knowledge management

---

## Quick Reference

| Skill | Purpose | Primary Agent | Key Feature |
|-------|---------|---------------|-------------|
| aria-quality-valid | VALID framework validation | manager-quality | 5-dimension quality scoring |
| aria-writing-style | Technical writing standards | expert-writer | Clarity and consistency |
| aria-templates | Document template library | manager-docs | Standardized formats |
| aria-research | Regulatory research methodology | expert-researcher | Source verification |
| aria-analysis | Data analysis and statistics | expert-analyst | Trend identification |

---

## Best Practices

### Skill Selection

Choose the right skill for the task:

1. **Quality validation**: aria-quality-valid
2. **Document creation**: aria-writing-style + aria-templates
3. **Information gathering**: aria-research
4. **Data interpretation**: aria-analysis
5. **Complex tasks**: Combine multiple skills

### Usage Patterns

Effective skill usage patterns:

- Start with research (aria-research)
- Apply writing standards (aria-writing-style)
- Use templates (aria-templates)
- Validate continuously (aria-quality-valid)
- Analyze results (aria-analysis)

### Quality Assurance

Ensure quality with:

- Skill combination for comprehensive coverage
- Validation at each workflow stage
- Documentation of skill usage
- Traceability of recommendations

---

## Version Information

**Current Version:** 1.0.0
**Last Updated:** 2025-02-09
**Status:** Active Development

---

## Support

For issues or questions:

- ARIA Project Repository
- SPEC-ARIA-002 Documentation
- MoAI-ADK Foundation Skills
