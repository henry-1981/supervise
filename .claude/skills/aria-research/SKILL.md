---
name: aria-research
description: >
  Research methodology skill for regulatory intelligence gathering and information quality assessment.
  Defines systematic research approaches for regulatory documentation, source citation standards,
  and information quality evaluation criteria. Use with Context7 MCP for regulatory standards
  lookup and expert-researcher agent for comprehensive regulatory research tasks.
license: Apache-2.0
compatibility: Designed for Claude Code
allowed-tools: Read Grep Glob Bash mcp__context7__resolve-library-id mcp__context7__get-library-docs
user-invocable: false
metadata:
  version: "1.0.0"
  category: "workflow"
  status: "active"
  updated: "2026-02-09"
  modularized: "true"
  tags: "research, regulatory, citation, quality-assessment"
  author: "ARIA Team"
  context: "regulatory"
  context7-libraries: "FDA-21CFR, EU-MDR, ISO-13485, IEC-62304, ISO-14971"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords:
    [
      "research",
      "regulatory research",
      "citation",
      "source",
      "information quality",
      "literature review",
      "regulatory guidance",
      "standards research",
      "precedent",
      "predicate device",
    ]
  agents: ["expert-researcher", "expert-analyst", "expert-clinical"]
  phases: ["brief", "execute"]
---

# ARIA Research Methodology

## Quick Reference (30 seconds)

Research methodology skill for regulatory intelligence gathering and information quality assessment.

Core Capabilities:

- Systematic Research Approach: Structured methodology for regulatory information gathering
- Source Citation Standards: Consistent citation format for regulatory documentation
- Information Quality Assessment: Criteria for evaluating source reliability and currency
- Context7 Integration: Seamless lookup of regulatory standards and guidance
- Precedent Research: Methods for finding and analyzing predicate devices

When to Use:

- Regulatory requirement research (FDA, EU MDR, MFDS)
- Standards interpretation (ISO 13485, IEC 62304, ISO 14971)
- Predicate device identification for 510(k) submissions
- Regulatory guidance document retrieval
- Literature review for clinical evaluation
- Regulatory pathway determination
- Multi-market regulatory research

Research Types:

- Regulatory Research: FDA 21 CFR, EU MDR 2017/745, MFDS regulations
- Standards Research: ISO, IEC, ASTM, AAMI standards
- Clinical Research: Literature review, clinical evidence
- Precedent Research: Predicate devices, previous submissions
- Guidance Research: FDA guidance documents, MEDDEV, regulatory interpretations

---

## Implementation Guide (5 minutes)

### Research Methodology Framework

All research activities follow a systematic approach defined in modules/methodology.md.

#### Research Phases

**Phase 1: Planning**
- Define research question and objectives
- Identify applicable regulatory domains (FDA, EU, MFDS)
- Determine search scope and boundaries
- Select appropriate research sources

**Phase 2: Information Gathering**
- Use Context7 MCP for regulatory standards lookup
- Search regulatory databases (FDA, EU EUDAMED)
- Review guidance documents and interpretations
- Identify relevant precedents and predicates

**Phase 3: Quality Assessment**
- Evaluate source authority and reliability
- Verify currency and applicability
- Check for updates or superseded versions
- Assess regulatory interpretation validity

**Phase 4: Synthesis**
- Organize findings by regulatory domain
- Extract key requirements and constraints
- Identify gaps or ambiguities
- Document assumptions and limitations

**Phase 5: Citation**
- Apply consistent citation format
- Link sources to specific claims
- Maintain traceability to originals
- Enable verification by reviewers

### Source Citation Standards

Detailed citation format specifications are in modules/citation.md.

#### Regulatory Citation Format

All regulatory claims MUST include:

- **Regulation Name**: Full official name
- **Section/Article**: Specific section identifier
- **Version/Date**: Effective date or revision
- **Requirement Text**: Direct quote or paraphrase with citation

Examples:

```
FDA Citation:
21 CFR Part 820.30 (Design Controls): "Each manufacturer shall establish and maintain procedures to control the design of the device..."

EU MDR Citation:
Regulation (EU) 2017/745, Article 10(9): "Devices shall be designed and manufactured in such a way as to remove or reduce as far as possible..."

ISO Citation:
ISO 13485:2016, Section 7.3.2 (Design and development inputs): "Inputs relating to product requirements shall be determined and records maintained."
```

#### Standards Citation Format

Standards citations include:

- **Standard Number**: ISO, IEC, ASTM identifier
- **Publication Year**: Version year
- **Section/Clause**: Specific clause number
- **Title**: Section or requirement title
- **Requirement**: Specific requirement text

Example:

```
ISO 14971:2019, Section 5.3 (Risk analysis): "For each identified hazardous situation, the manufacturer shall estimate the associated risk(s) using available information or data."
```

### Information Quality Assessment

Quality assessment criteria are defined in modules/quality-assessment.md.

#### Assessment Dimensions

**Authority**
- Official regulatory source (FDA, EU, MFDS)
- Recognized standards body (ISO, IEC)
- Peer-reviewed publication
- Industry guidance (AAMI, GHTF)

**Currency**
- Current effective version
- Not superseded or withdrawn
- Recent regulatory interpretation
- Applicable to current market requirements

**Applicability**
- Relevant to product classification
- Applicable to target markets
- Appropriate for regulatory pathway
- Consistent with device characteristics

**Traceability**
- Verifiable original source
- Complete citation information
- Accessible for verification
- Linked to regulatory requirement

#### Quality Tiers

**Tier 1 (Primary Sources)**
- Official regulations (FDA 21 CFR, EU MDR)
- Published standards (ISO, IEC)
- Direct regulatory guidance
- Official regulatory database entries

**Tier 2 (Secondary Sources)**
- Recognized industry guidance (AAMI, GHTF)
- Professional association recommendations
- Regulatory authority presentations
- Notified body guidance

**Tier 3 (Tertiary Sources)**
- Industry white papers
- Consultant interpretations
- Conference presentations
- Trade publication articles

Use highest tier sources for regulatory submissions. Cite lower tiers only when higher tiers are unavailable, and flag as interpretive.

---

## Context7 MCP Integration

### Library Lookup Pattern

Use Context7 MCP for up-to-date regulatory standards:

1. Resolve library identifier
2. Retrieve current documentation
3. Extract relevant requirements
4. Cite with version information

Example workflow:

```
1. mcp__context7__resolve-library-id: "ISO 13485"
2. mcp__context7__get-library-docs: library_id, section filter
3. Extract requirement text
4. Format citation: "ISO 13485:2016, Section X.Y: [requirement]"
```

### Supported Regulatory Libraries

- FDA-21CFR: FDA Code of Federal Regulations
- EU-MDR: EU Medical Device Regulation 2017/745
- ISO-13485: Quality Management Systems
- IEC-62304: Medical Device Software Lifecycle
- ISO-14971: Risk Management
- IEC-60601: Medical Electrical Equipment Safety
- IEC-62366: Usability Engineering

---

## Research Checklists

### Regulatory Research Checklist

- [ ] Define specific regulatory question
- [ ] Identify applicable regulations (FDA, EU, MFDS)
- [ ] Search current effective versions via Context7
- [ ] Verify not superseded or amended
- [ ] Extract specific requirement text
- [ ] Cite with regulation, section, date
- [ ] Document any regulatory ambiguities
- [ ] Note interpretation assumptions

### Standards Research Checklist

- [ ] Identify applicable standards by device type
- [ ] Determine standard applicability (normative, informative)
- [ ] Retrieve current published version
- [ ] Check for amendments or corrigenda
- [ ] Extract specific clauses and requirements
- [ ] Cite with standard number, year, section
- [ ] Document harmonization status (if applicable)
- [ ] Note implementation guidance

### Predicate Device Research Checklist

- [ ] Define device classification and intended use
- [ ] Search FDA 510(k) database
- [ ] Identify potential predicate devices
- [ ] Retrieve 510(k) summaries
- [ [ Review technological characteristics
- [ ] Assess substantial equivalence
- [ ] Document similarities and differences
- [ ] Cite with 510(k) number and approval date

---

## Module References

- modules/methodology.md: Detailed research methodology framework
- modules/citation.md: Comprehensive citation format standards
- modules/quality-assessment.md: Information quality evaluation criteria
- reference.md: Research resources and databases

---

Version: 1.0.0 (Phase 2.3)
Last Updated: 2026-02-09
Language: English
Target Agents: expert-researcher, expert-analyst, expert-clinical
