---
name: aria-research
description: >
  Research methodology for ARIA business documents. Provides source citation
  standards, information quality assessment criteria, and research protocols
  for regulatory and technical documentation. Used by expert-researcher for
  evidence gathering, literature review, and source verification.
license: Apache-2.0
compatibility: Designed for Claude Code
user-invocable: true
metadata:
  version: "1.0.0"
  category: "domain"
  status: "active"
  updated: "2025-02-09"
  modularized: "true"
  tags: "aria, research, methodology, citation"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords: ["research", "literature", "sources", "citation", "evidence"]
  agents: ["expert-researcher"]
  phases: ["brief", "execute"]
  languages: ["en", "ko"]
---

# ARIA Research Methodology

## Overview

This skill provides standardized research methodologies for regulatory and technical documentation within the ARIA ecosystem.

## Research Process

### Step 1: Research Planning

#### Define Research Questions
- Specific and measurable
- Relevant to objectives
- Answerable with available resources
- Aligned with regulatory requirements

#### Identify Key Concepts
- Core terminology
- Related concepts
- Synonyms and variations
- Technical terms

#### Scope Boundaries
- Inclusion criteria
- Exclusion criteria
- Time periods covered
- Geographic scope

### Step 2: Source Identification

#### Primary Sources
- Original regulations and laws
- Regulatory guidance documents
- Technical standards
- Clinical trial data

#### Secondary Sources
- Peer-reviewed journals
- Government publications
- Industry white papers
- Professional association documents

#### Tertiary Sources
- Textbooks and handbooks
- Review articles
- Meta-analyses
- Systematic reviews

### Step 3: Source Evaluation

#### Quality Assessment Criteria

| Criterion | High Quality | Medium Quality | Low Quality |
|-----------|-------------|---------------|-------------|
| **Authority** | Regulatory body, peer-reviewed | Industry publication | Unverified source |
| **Currency** | Within 3 years | 3-5 years | Over 5 years |
| **Accuracy** | Verified, cited | Generally accepted | Uncited claims |
| **Objectivity** | Balanced perspective | Mild bias | Clear bias |
| **Coverage** | Comprehensive | Adequate | Limited |

#### Source Verification Checklist
- [ ] Author credentials verified
- [ ] Publisher reputation confirmed
- [ ] Publication date checked
- [ ] References cited properly
- [ ] Claims supported by evidence
- [ ] Bias assessed
- [ ] Conflicts of interest disclosed

## Citation Standards

### Regulatory Documents

#### Format Template
```markdown
[Agency]. [Document Title]. [Publication Date]. [URL or Accession Number].

Example:
FDA. Guidance for Industry: Q8(R2) Pharmaceutical Development. 2009.
https://www.fda.gov/regulatory-information/search-fda-guidance-documents
```

#### Key Elements
- Agency name (full, no abbreviations)
- Document title (italicized or quoted)
- Publication or revision date
- Document number or identifier
- URL for online sources

### Journal Articles

#### Format Template
```markdown
[Author(s)]. "[Article Title]." [Journal Name], vol. [volume], no. [issue],
[Year], pp. [page range]. DOI.

Example:
Smith, J., and Brown, A. "Quality Risk Management in Biotechnology."
Journal of Pharmaceutical Sciences, vol. 105, no. 3, 2016, pp. 785-792.
doi:10.1016/j.xphs.2016.01.015
```

#### Key Elements
- Author names (Last, First)
- Article title (in quotes)
- Journal name (italicized)
- Volume and issue numbers
- Publication year
- Page range
- Digital Object Identifier (DOI)

### Technical Standards

#### Format Template
```markdown
[Organization]. [Standard Number]: [Standard Title]. [Year].

Example:
International Organization for Standardization. ISO 13485: Medical devices -
Quality management systems. 2016.
```

### Online Sources

#### Format Template
```markdown
[Author/Organization]. "[Page Title]." [Website Name], [Publication Date],
[URL]. [Access Date].

Example:
World Health Organization. "Good Manufacturing Practices for Pharmaceutical
Products." WHO, 2024, https://www.who.int/publications. Accessed 2025-02-09.
```

## Information Quality Assessment

### Evidence Hierarchy

| Level | Source Type | Reliability |
|-------|-------------|-------------|
| 1 | Meta-analyses, systematic reviews | Highest |
| 2 | Randomized controlled trials | Very high |
| 3 | Cohort studies | High |
| 4 | Case-control studies | Moderate |
| 5 | Case reports, expert opinion | Low |

### Quality Metrics

#### CRAAP Test
- **Currency**: Publication date, revision history
- **Relevance**: Direct applicability to research question
- **Authority**: Author credentials, publisher reputation
- **Accuracy**: Verifiable facts, proper citations
- **Purpose**: Educational, commercial, propaganda

#### Red Flags
- Anonymous sources
- No publication date
- No references cited
- Clear bias or agenda
- Poor writing quality
- Outdated information

## Research Documentation

### Research Log Template

```markdown
# Research Log

## Search Strategy
- **Keywords**: [List search terms]
- **Databases**: [Sources searched]
- **Date Range**: [Coverage period]
- **Inclusion Criteria**: [What was included]
- **Exclusion Criteria**: [What was excluded]

## Sources Found

| # | Source | Type | Quality | Notes |
|---|--------|------|---------|-------|
| 1 | [Citation] | [Type] | [H/M/L] | [Notes] |

## Key Findings
[Summary of relevant information]

## Gaps Identified
[Missing information or conflicting data]

## Next Steps
[Additional research needed]
```

### Literature Review Template

```markdown
# Literature Review

## Introduction
[Topic and research question]

## Methodology
[Search strategy and sources]

## Results

### Theme 1: [Theme name]
[Synthesize findings]

### Theme 2: [Theme name]
[Synthesize findings]

## Discussion
[Interpret findings, identify trends]

## Conclusion
[Summary and implications]

## References
[Complete citation list]
```

## Research Best Practices

### Do's
1. Start with authoritative sources
2. Verify information across multiple sources
3. Document all sources immediately
4. Assess source quality before using
5. Keep organized research notes
6. Update research regularly

### Don'ts
1. Rely on single sources
2. Use outdated regulations
3. Accept claims without verification
4. Skip citation documentation
5. Ignore source bias
6. Assume all online sources are valid

## Special Considerations

### Regulatory Research
- Always use current versions
- Check for recent updates
- Verify jurisdiction applicability
- Note draft vs final status
- Track amendment history

### Technical Research
- Prefer peer-reviewed sources
- Check author expertise
- Verify funding sources
- Assess conflict of interest
- Confirm reproducibility

### International Sources
- Note language of original
- Use official translations
- Check cultural context
- Verify legal applicability
- Consider local variations

## Plagiarism Prevention

### Proper Attribution
- Direct quotes: Use quotation marks
- Paraphrasing: Still requires citation
- Ideas: Credit original source
- Common knowledge: No citation needed

### Common Knowledge Guidelines
- Found in multiple sources
- Widely accepted as fact
- Not disputed by experts
- Not requiring specialized knowledge

### Fair Use Guidelines
- Purpose: Educational or commentary
- Nature: Factual rather than creative
- Amount: Small portion of work
- Effect: Does not replace original
