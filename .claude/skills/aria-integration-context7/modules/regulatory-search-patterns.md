# Regulatory Search Patterns

Complete Context7 query templates for FDA 21 CFR 820, ISO 13485, EU MDR 2017/745, and citation formats.

## FDA 21 CFR 820 QSR Search Patterns

### Library Resolution

**Base Query Formats**:
- "fda 21 cfr 820" - Standard Quality System Regulation
- "fda qsr" - Abbreviated Quality System Regulation
- "21 cfr part 820" - Official CFR citation format

**Context7 Library ID**: `fda-21-cfr-part-820`

### Search Topics by Subpart

**Subpart 820.20 - Quality Management System**:
- "quality system requirements"
- "management responsibility"
- "quality policy"
- "quality manual"
- "organizational structure"

**Subpart 820.30 - Design Controls**:
- "design controls"
- "design input"
- "design output"
- "design review"
- "design verification"
- "design validation"
- "design transfer"
- "design history file"

**Subpart 820.40 - Document Controls**:
- "document control"
- "document approval"
- "document distribution"
- "document changes"
- "design documents"

**Subpart 820.50 - Purchasing Controls**:
- "purchasing controls"
- "supplier evaluation"
- "supplier qualification"
- "purchased data"

**Subpart 820.60 - Identification**:
- "identification"
- "product identification"
- "labeling control"

**Subpart 820.70 - Production and Process Controls**:
- "production controls"
- "process validation"
- "manufacturing processes"
- "equipment"
- "acceptance criteria"

**Subpart 820.75 - Process Validation**:
- "process validation"
- "validation protocols"
- "validation reports"

**Subpart 820.80 - Acceptance Activities**:
- "acceptance activities"
- "incoming inspection"
- "acceptance testing"
- "acceptance records"

**Subpart 820.90 - Tagging**:
- "tagging"
- "control of nonconforming product"
- "quarantine"

**Subpart 820.100 - Traceability**:
- "traceability"
- "distribution records"
- "lot tracking"

**Subpart 820.110 - Installation**:
- "installation"
- "inspection and installation"

**Subpart 820.120 - Servicing**:
- "servicing"
- "service reports"
- "service procedures"

**Subpart 820.130 - Labeling Control**:
- "labeling control"
- "labeling inspection"
- "label integrity"

**Subpart 820.140 - Purchasing Control**:
- "purchasing data"
- "purchasing documents"

**Subpart 820.150 - Statistical Techniques**:
- "statistical techniques"
- "sampling plans"
- "process capability"

**Subpart 820.160 - Complaint Files**:
- "complaint files"
- "complaint handling"

**Subpart 820.170 - Servicing Reports**:
- "servicing reports"
- "service feedback"

**Subpart 820.180 - Analysis of Data**:
- "analysis of data"
- "trend analysis"
- "quality data"

**Subpart 820.190 - Techniques**:
- "statistical techniques"
- "quality planning"
- "quality audit"

**Subpart 820.200 - Servicing Reports**:
- "servicing reports"
- "service procedures"

### Query Template Examples

```javascript
// Example 1: Design Controls Overview
mcp__context7__resolve-library-id({
  query: "fda 21 cfr 820 design controls"
});

// Example 2: Specific Design Control Subsection
mcp__context7__get-library-docs({
  libraryId: "fda-21-cfr-part-820",
  query: "820.30 design validation requirements"
});

// Example 3: Cross-Subpart Search
mcp__context7__get-library-docs({
  libraryId: "fda-21-cfr-part-820",
  query: "document control design history file"
});
```

## ISO 13485 QMS Search Patterns

### Library Resolution

**Base Query Formats**:
- "iso 13485" - Standard query
- "iso 13485:2016" - Version-specific query
- "iso 13485 quality management system" - Descriptive query

**Context7 Library ID**: `iso-13485`

### Search Topics by Clause

**Clause 4 - Quality Management System**:
- "quality management system"
- "quality management system requirements"
- "quality policy"
- "quality objectives"
- "quality manual"
- "document control"
- "control of documents"
- "control of quality records"

**Clause 5 - Management Responsibility**:
- "management responsibility"
- "top management commitment"
- "quality policy"
- "quality planning"
- "responsibility authority"
- "management representative"
- "internal communication"
- "management review"

**Clause 6 - Resource Management**:
- "resource management"
- "human resources"
- "competence awareness"
- "training"
- "infrastructure"
- "work environment"

**Clause 7 - Product Realization**:
- "product realization"
- "planning of product realization"
- "customer-related processes"
- "design and development"
- "design development planning"
- "design development inputs"
- "design development outputs"
- "design development review"
- "design development verification"
- "design development validation"
- "design development transfer"
- "purchasing"
- "purchasing process"
- "purchasing information"
- "verification of purchased product"
- "production and service provision"
- "control of production and service provision"
- "validation of processes for production"
- "identification and traceability"
- "customer property"
- "preservation of product"
- "control of monitoring and measuring devices"

**Clause 8 - Measurement, Analysis and Improvement**:
- "measurement analysis improvement"
- "monitoring and measurement"
- "internal audit"
- "monitoring of customer satisfaction"
- "monitoring of processes"
- "monitoring of product"
- "control of nonconforming product"
- "analysis of data"
- "improvement"
- "continual improvement"
- "corrective action"
- "preventive action"

### Query Template Examples

```javascript
// Example 1: QMS Overview
mcp__context7__resolve-library-id({
  query: "iso 13485 quality management system"
});

// Example 2: Design and Development
mcp__context7__get-library-docs({
  libraryId: "iso-13485",
  query: "design and development validation clause 7.3.8"
});

// Example 3: Internal Audit
mcp__context7__get-library-docs({
  libraryId: "iso-13485",
  query: "internal audit requirements clause 8.2.2"
});
```

## EU MDR 2017/745 Search Patterns

### Library Resolution

**Base Query Formats**:
- "eu mdr 2017/745" - Official citation
- "eu mdr" - Abbreviated
- "medical device regulation" - Descriptive
- "mdr 2017/745" - Alternative format

**Context7 Library ID**: `eu-mdr-2017-745`

### Search Topics by Chapter

**Chapter I - General Provisions**:
- "general provisions"
- "scope"
- "definition"
- "medical device definition"
- "accessory definition"
- "manufacturer definition"

**Chapter II - Placing on the Market and Putting into Service**:
- "placing on the market"
- "putting into service"
- "requirements"
- "conformity assessment"
- "economic operators"
- "manufacturer obligations"
- "authorized representative"
- "importer obligations"
- "distributor obligations"

**Chapter III - Technical Documentation**:
- "technical documentation"
- "general safety and performance requirements"
- "benefit-risk ratio"
- "clinical evaluation"
- "post-market surveillance"
- "risk management"
- "usability engineering"

**Chapter IV - Classification**:
- "classification rules"
- "device classification"
- "classification criteria"
- "duration of use"
- "invasive devices"
- "active devices"

**Chapter V - Conformity Assessment**:
- "conformity assessment"
- "assessment procedures"
- "notified bodies"
- "declaration of conformity"
- "CE marking"

**Chapter VI - Notified Bodies**:
- "notified bodies"
- "notification"
- "designation"
- "responsibilities"
- "coordination"

**Chapter VII - Clinical Evaluation**:
- "clinical evaluation"
- "clinical investigation"
- "performance evaluation"
- "clinical data"
- "clinical evidence"

**Chapter VIII - Post-Market Surveillance**:
- "post-market surveillance"
- "vigilance"
- "field safety corrective actions"
- "trend reporting"
- "periodic safety update report"

**Chapter IX - Market Surveillance**:
- "market surveillance"
- "competent authorities"
- "shared IT system"
- "EUDAMED"
- "unique device identification"

**Chapter X - Transparency**:
- "transparency"
- "summary of safety and performance"
- "implant card"
- "register of information"

### Annex Search Patterns

**Annex I - General Safety and Performance Requirements**:
- "annex i general safety performance requirements"
- "essential requirements"
- "risk management"
- "clinical evaluation"
- "technical documentation"

**Annex IX - Conformity Assessment**:
- "annex ix conformity assessment"
- "assessment procedures"
- "quality management system"
- "technical documentation assessment"

**Annex XI - Clinical Evaluation**:
- "annex xi clinical evaluation"
- "clinical investigation"
- "performance evaluation"
- "clinical study"

**Annex XIV - Clinical Evaluation**:
- "annex xiv clinical evaluation"
- "clinical evaluation report"
- "clinical evaluation plan"

**Annex XV - Clinical Investigation**:
- "annex xv clinical investigation"
- "clinical investigation plan"
- "clinical investigation report"

### Query Template Examples

```javascript
// Example 1: MDR Overview
mcp__context7__resolve-library-id({
  query: "eu mdr 2017/745 medical device regulation"
});

// Example 2: Technical Documentation
mcp__context7__get-library-docs({
  libraryId: "eu-mdr-2017-745",
  query: "technical documentation annex i chapter ii"
});

// Example 3: Clinical Evaluation
mcp__context7__get-library-docs({
  libraryId: "eu-mdr-2017-745",
  query: "clinical evaluation requirements chapter vii annex xiv"
});
```

## Citation Format Standards

### FDA Citations

**Standard Format**: 21 CFR §820.XX
**Example**: 21 CFR §820.30 Design Controls

**In-Text Citation**: (21 CFR 820.30)
**Reference List**: Title 21 CFR Part 820 - Quality System Regulation

### ISO Citations

**Standard Format**: ISO 13485:2016, Clause X.X
**Example**: ISO 13485:2016, Clause 7.3.8 Design and development validation

**In-Text Citation**: (ISO 13485:2016, 7.3.8)
**Reference List**: ISO 13485:2016 - Medical devices — Quality management systems

### EU MDR Citations

**Standard Format**: Regulation (EU) 2017/745, Article XX
**Example**: Regulation (EU) 2017/745, Article 10 - Manufacturer obligations

**In-Text Citation**: (MDR 2017/745, Art. 10)
**Reference List**: Regulation (EU) 2017/745 on medical devices

**Annex Citation**: Regulation (EU) 2017/745, Annex IX

## Combined Search Patterns

### Cross-Regulation Comparison

**Design Controls**:
```javascript
// FDA Design Controls
mcp__context7__get-library-docs({
  libraryId: "fda-21-cfr-part-820",
  query: "design controls 820.30"
});

// ISO Design and Development
mcp__context7__get-library-docs({
  libraryId: "iso-13485",
  query: "design and development clause 7.3"
});

// EU MDR Technical Documentation
mcp__context7__get-library-docs({
  libraryId: "eu-mdr-2017-745",
  query: "technical documentation annex i"
});
```

**Risk Management**:
```javascript
// FDA Risk Analysis
mcp__context7__get-library-docs({
  libraryId: "fda-21-cfr-part-820",
  query: "risk analysis 820.30"
});

// ISO Risk Management (reference to ISO 14971)
mcp__context7__get-library-docs({
  libraryId: "iso-13485",
  query: "risk management clause 7.1"
});

// EU MDR Risk Management
mcp__context7__get-library-docs({
  libraryId: "eu-mdr-2017-745",
  query: "risk management annex i chapter i"
});
```

## Optimization Tips

1. **Use Specific Citations**: Include section numbers in queries for more precise results
2. **Batch Related Queries**: Group queries by regulation and topic to reduce API calls
3. **Cache Common Queries**: Store results for frequently accessed sections
4. **Version Specificity**: Include year in ISO queries (e.g., ISO 13485:2016)
5. **Annex/Chapter Precision**: For EU MDR, specify annex or chapter for faster results

---

Last Updated: 2026-02-09
Maintained by: ARIA Development Team
