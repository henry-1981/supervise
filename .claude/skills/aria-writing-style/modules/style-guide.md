# Comprehensive Writing Style Guide

## Voice and Tone

### Active Voice (Preferred)

Active voice clarifies responsibility and improves readability.

**Use:**
- "The manufacturer shall validate the device."
- "The risk management process identifies hazards."
- "Clinical data supports the intended use claim."

**Avoid:**
- "The device shall be validated by the manufacturer."
- "Hazards are identified by the risk management process."
- "The intended use claim is supported by clinical data."

### Passive Voice (Acceptable Cases)

Passive voice is acceptable when the actor is unknown or irrelevant.

**Acceptable:**
- "The standard was published in 2023."
- "Regulatory requirements must be met."
- "The device was recalled due to safety concerns."

## Clarity and Precision

### Ambiguous Pronouns (Avoid)

Replace pronouns with specific nouns.

**Poor:**
"The device and the accessory must be compatible. It should be verified during design validation."

**Better:**
"The device and the accessory must be compatible. Compatibility should be verified during design validation."

### One Idea Per Sentence

Complex sentences reduce comprehension.

**Poor:**
"The device shall perform self-test at startup, and if the self-test fails, the device shall display an error message and prevent normal operation until the issue is resolved."

**Better:**
"The device shall perform self-test at startup. If the self-test fails, the device shall display an error message. The device shall prevent normal operation until the issue is resolved."

## Regulatory Language

### Requirement Levels

**Shall**: Mandatory requirement
- "The manufacturer shall establish a quality management system."

**Should**: Recommendation (strong preference)
- "The manufacturer should consider post-market surveillance data."

**May**: Permissible option
- "The manufacturer may use historical clinical data."

### Citation Format

Always cite regulations with complete references.

**Format:**
`[Standard] [Section], [Version/Year]`

**Examples:**
- ISO 13485:2016, Section 7.3
- 21 CFR 820.30(a)
- EU MDR Annex I, Section 1

## Professional Tone

### Objective Language

Avoid subjective or promotional language.

**Poor:**
- "Our innovative device provides excellent results."
- "The superior design ensures maximum safety."

**Better:**
- "Clinical data demonstrates a 95% success rate (n=200)."
- "Risk mitigation measures reduce residual risk to acceptable levels per ISO 14971."

### Evidence-Based Statements

Support claims with data or citations.

**Poor:**
"The device is safe for home use."

**Better:**
"Human factors validation (n=15 representative users) demonstrated safe home use per IEC 62366-1."

## Formatting Guidelines

### Headings

Use hierarchical heading structure.

```
# Level 1: Document Title
## Level 2: Major Sections
### Level 3: Subsections
#### Level 4: Detailed Points
```

### Lists

Use lists for clarity and scannability.

**Unordered lists:** Related items without sequence
- Risk mitigation measures
- Applicable standards
- Verification methods

**Ordered lists:** Sequential steps or priorities
1. Identify hazards
2. Estimate risks
3. Evaluate risks
4. Implement risk controls

### Tables

Use tables for structured data.

| Hazard | Severity | Probability | Risk Level | Mitigation |
|--------|----------|-------------|------------|------------|
| Electric shock | Catastrophic | Remote | Medium | Double insulation |

## Common Mistakes

### Inconsistent Terminology

**Poor:** Using "product", "medical device", and "equipment" interchangeably.

**Better:** Use "medical device" consistently throughout the document.

### Missing Citations

**Poor:** "The device complies with applicable standards."

**Better:** "The device complies with ISO 13485:2016 and IEC 60601-1:2012+AMD1:2020."

### Vague Quantifiers

**Poor:** "Most users", "significant improvement", "low risk"

**Better:** "85% of users (n=100)", "25% reduction in procedure time", "Risk Index 4 per ISO 14971 matrix"

## Document-Specific Guidelines

### Regulatory Reports

- Executive summary (1-2 pages)
- Clear section headings
- Citations in every claim
- Appendices for supporting data

### Technical Specifications

- Numbered requirements
- Testable acceptance criteria
- Traceability to higher-level requirements
- Version control information

### Review Reports

- Standardized review checklist
- Objective findings (not opinions)
- Clear accept/reject/conditional decisions
- Action items with owners and deadlines

## Review Checklist

Before finalizing any regulatory document:

- [ ] Active voice used consistently
- [ ] No ambiguous pronouns
- [ ] One idea per sentence
- [ ] Correct requirement levels (shall/should/may)
- [ ] Complete citations with versions
- [ ] Objective, evidence-based language
- [ ] Consistent terminology per terminology.md
- [ ] Proper heading hierarchy
- [ ] Lists and tables formatted correctly
- [ ] Document version and date included
