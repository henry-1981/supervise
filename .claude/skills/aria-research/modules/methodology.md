# Research Methodology

Systematic approach for regulatory intelligence gathering and information retrieval.

## Research Framework

### Five-Phase Research Process

#### Phase 1: Planning and Scoping

**Objectives:**
- Define specific research question or information need
- Identify applicable regulatory domains
- Determine search scope and boundaries
- Select appropriate research sources

**Key Activities:**
- Clarify research objectives with stakeholder
- Map to regulatory domains (FDA, EU, MFDS, etc.)
- Identify applicable standards (ISO, IEC, etc.)
- Determine acceptable source types (primary, secondary, tertiary)
- Establish timeline and resource constraints

**Deliverables:**
- Research plan document
- Scope definition statement
- Source prioritization list
- Search strategy outline

#### Phase 2: Information Gathering

**Objectives:**
- Systematically collect regulatory information
- Retrieve current effective versions
- Identify applicable guidance and interpretations
- Find relevant precedents and examples

**Key Activities:**
- Use Context7 MCP for standards lookup
- Search regulatory databases (FDA.gov, EU EUDAMED)
- Review guidance documents and regulatory interpretations
- Identify predicate devices or precedent submissions
- Collect industry best practices

**Deliverables:**
- Source document collection
- Regulatory requirement extracts
- Guidance document summaries
- Precedent analysis notes

#### Phase 3: Quality Assessment

**Objectives:**
- Evaluate source authority and reliability
- Verify currency and applicability
- Check for updates or superseded versions
- Assess regulatory interpretation validity

**Key Activities:**
- Apply quality assessment criteria (see quality-assessment.md)
- Verify source authenticity and official status
- Check effective dates and amendment status
- Evaluate applicability to specific device type
- Assess interpretation validity and consensus

**Deliverables:**
- Source quality ratings
- Currency verification notes
- Applicability determination
- Interpretation validation summary

#### Phase 4: Synthesis and Analysis

**Objectives:**
- Organize findings by regulatory domain
- Extract key requirements and constraints
- Identify gaps or ambiguities
- Document assumptions and limitations

**Key Activities:**
- Group findings by regulation/standard
- Extract specific requirements with citations
- Identify regulatory gaps or unclear areas
- Document interpretation assumptions
- Note conflicting guidance or requirements

**Deliverables:**
- Organized findings by domain
- Requirement extraction table
- Gap analysis summary
- Assumption documentation

#### Phase 5: Documentation and Citation

**Objectives:**
- Apply consistent citation format
- Link sources to specific claims
- Maintain traceability to originals
- Enable verification by reviewers

**Key Activities:**
- Format citations per citation.md standards
- Link each claim to source citation
- Create traceability matrix
- Document version and effective dates
- Provide verification guidance

**Deliverables:**
- Fully cited research report
- Traceability matrix
- Source verification instructions
- Research limitations statement

---

## Research Types and Approaches

### Regulatory Research

**Purpose:** Identify and interpret regulatory requirements for specific device types and markets.

**Typical Sources:**
- FDA 21 CFR (Code of Federal Regulations)
- EU MDR 2017/745 (Medical Device Regulation)
- MFDS regulations (Korean Ministry of Food and Drug Safety)
- National regulations for target markets

**Research Approach:**
1. Identify device classification
2. Determine applicable regulatory chapters/articles
3. Use Context7 MCP for current effective version
4. Extract specific requirements
5. Review regulatory guidance for interpretation
6. Document regulatory pathway determination

### Standards Research

**Purpose:** Identify applicable standards and interpret requirements for device development and compliance.

**Typical Sources:**
- ISO 13485 (Quality Management Systems)
- IEC 62304 (Software Lifecycle)
- ISO 14971 (Risk Management)
- IEC 60601 series (Electrical Safety)
- IEC 62366 (Usability Engineering)

**Research Approach:**
1. Determine device type and characteristics
2. Identify normative vs informative standards
3. Use Context7 MCP for current published versions
4. Check harmonization status (for EU)
5. Extract specific clauses and requirements
6. Document implementation guidance

### Clinical Research

**Purpose:** Gather clinical evidence for safety and effectiveness evaluation.

**Typical Sources:**
- PubMed/MEDLINE literature database
- Cochrane systematic reviews
- Clinical trial registries (ClinicalTrials.gov)
- Device-specific clinical literature

**Research Approach:**
1. Define clinical question (PICO format)
2. Develop search strategy with keywords
3. Search literature databases
4. Apply inclusion/exclusion criteria
5. Assess study quality and bias
6. Synthesize clinical evidence

### Precedent Research

**Purpose:** Find and analyze predicate devices or previous regulatory submissions.

**Typical Sources:**
- FDA 510(k) database
- FDA PMA database
- EU EUDAMED (European Database on Medical Devices)
- Company submission archives

**Research Approach:**
1. Define device characteristics and intended use
2. Search regulatory databases by classification
3. Identify potential predicate devices
4. Retrieve 510(k) summaries or SSED
5. Compare technological characteristics
6. Assess substantial equivalence rationale

### Guidance Research

**Purpose:** Find and interpret regulatory guidance documents and agency positions.

**Typical Sources:**
- FDA guidance documents
- EU MDCG guidance (Medical Device Coordination Group)
- Notified Body guidance and position papers
- Regulatory authority presentations and webinars

**Research Approach:**
1. Identify relevant topic area
2. Search agency guidance databases
3. Check for draft vs final status
4. Review comments and Q&A
5. Assess current applicability
6. Document regulatory position

---

## Search Strategy Development

### Keyword Development

**Regulatory Keywords:**
- Device classification terms (Class I, II, III)
- Regulatory pathway terms (510(k), PMA, De Novo)
- Intended use terms (diagnostic, therapeutic, monitoring)
- Product code (FDA product classification)

**Standards Keywords:**
- Standard number (ISO 13485, IEC 62304)
- Domain terms (quality management, software lifecycle, risk)
- Requirement terms (verification, validation, traceability)
- Process terms (design control, CAPA, complaint handling)

**Clinical Keywords:**
- Device type terms (stent, pump, monitor)
- Clinical terms (safety, effectiveness, adverse events)
- Population terms (pediatric, geriatric, specific conditions)
- Outcome terms (mortality, morbidity, quality of life)

### Boolean Search Techniques

**AND Operator:** Narrow results by requiring all terms
- Example: "medical device" AND "software" AND "IEC 62304"

**OR Operator:** Broaden results by including alternative terms
- Example: "510(k)" OR "premarket notification"

**NOT Operator:** Exclude irrelevant results
- Example: "medical device" NOT "in vitro diagnostic"

**Phrase Search:** Use quotes for exact phrase matching
- Example: "substantial equivalence"

**Wildcard:** Use * for term variants
- Example: "regulat*" matches regulation, regulatory, regulate

---

## Context7 MCP Integration Patterns

### Standard Library Lookup

```
Step 1: Resolve library identifier
mcp__context7__resolve-library-id: "ISO 13485"
→ Returns: library_id for ISO 13485

Step 2: Retrieve documentation
mcp__context7__get-library-docs: library_id, section_filter
→ Returns: Current documentation content

Step 3: Extract requirements
Parse returned content for specific requirements
Identify section numbers and requirement text

Step 4: Format citation
"ISO 13485:2016, Section X.Y: [requirement text]"
```

### Multi-Library Research

When research spans multiple regulations/standards:

```
1. Identify all applicable libraries
   - FDA-21CFR for US market
   - EU-MDR for European market
   - ISO-13485 for QMS requirements

2. Resolve each library identifier
   - Run mcp__context7__resolve-library-id for each

3. Retrieve specific sections
   - Filter by relevant sections/articles
   - Avoid retrieving entire documents

4. Cross-reference requirements
   - Identify overlaps and differences
   - Document multi-market compliance strategy
```

### Version Currency Verification

Always verify using Context7 to ensure current version:

```
1. Resolve library (returns current version info)
2. Compare with project documentation
3. Flag if project uses older version
4. Recommend update if significant changes
```

---

## Research Documentation Templates

### Research Plan Template

```markdown
# Research Plan: [Topic]

## Research Question
[Specific question or information need]

## Scope
- Regulatory Domains: [FDA, EU, MFDS, etc.]
- Standards: [ISO, IEC, etc.]
- Markets: [US, EU, Korea, etc.]
- Device Type: [Classification and intended use]

## Search Strategy
- Primary Sources: [List]
- Secondary Sources: [List]
- Keywords: [List]
- Exclusions: [What to exclude]

## Timeline
- Start Date: [Date]
- Completion Date: [Date]
- Review Date: [Date]

## Deliverables
- [Deliverable 1]
- [Deliverable 2]
```

### Research Findings Template

```markdown
# Research Findings: [Topic]

## Executive Summary
[Key findings in 2-3 sentences]

## Regulatory Requirements

### [Regulation 1: FDA 21 CFR Part XXX]
- Section XXX: [Requirement]
  - Citation: [Full citation]
  - Interpretation: [Brief interpretation]
  - Applicability: [Applicable/Not Applicable with rationale]

### [Standard 1: ISO XXXXX]
- Clause X.Y: [Requirement]
  - Citation: [Full citation]
  - Normative/Informative: [Status]
  - Harmonization: [EU harmonized: Yes/No]

## Gaps and Ambiguities
- [Gap or ambiguity 1]
- [Gap or ambiguity 2]

## Assumptions
- [Assumption 1]
- [Assumption 2]

## Recommendations
- [Recommendation 1]
- [Recommendation 2]

## References
[Complete citation list]
```

---

## Quality Control Checklist

### Before Completing Research

- [ ] All sources cited with complete information
- [ ] Current versions verified via Context7
- [ ] Quality assessment completed for all sources
- [ ] Gaps and ambiguities documented
- [ ] Assumptions clearly stated
- [ ] Findings organized by regulatory domain
- [ ] Traceability to original sources maintained
- [ ] Peer review completed (if required)

### Research Validation

- [ ] Sources are authoritative (Tier 1 or 2)
- [ ] Current effective versions used
- [ ] Applicable to specific device type
- [ ] Regulatory pathway correctly identified
- [ ] Requirements complete and accurate
- [ ] Citations verifiable by reviewers
- [ ] Limitations clearly documented
- [ ] Recommendations actionable

---

Version: 1.0.0
Last Updated: 2026-02-09
