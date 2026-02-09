# ARIA Skills Directory

ARIA (AI Regulatory Intelligence Assistant) skill definitions following the Agent Skills open standard (agentskills.io).

## Skill Organization

### Workflow Skills (6)

Core workflow skills that define ARIA's BRIEF-EXECUTE-DELIVER pipeline.

| Skill | Level 1 Tokens | Level 2 Tokens | Purpose |
|-------|---------------|----------------|---------|
| aria-workflows | ~100 | ~5000 | BRIEF-EXECUTE-DELIVER orchestration |
| aria-templates | ~100 | ~5000 | Document templates (brief, submission, CAPA) |
| aria-quality-valid | ~100 | ~5000 | VALID framework quality gates |
| aria-analysis | ~100 | ~5000 | Feasibility study and requirement analysis |
| aria-research | ~100 | ~5000 | Web research methodologies |
| aria-writing-style | ~100 | ~5000 | RA/QA technical writing standards |
| aria-analytics | ~100 | ~5000 | Data analysis and reporting |

### Knowledge Skills (9) - Phase 3

Specialized domain knowledge skills using Progressive Disclosure system for efficient token management.

| Skill | Level 1 Tokens | Level 2 Tokens | Focus |
|-------|---------------|----------------|-------|
| aria-domain-raqa | ~100 | ~5000 | RA/QA domain overview, regulatory hierarchy |
| aria-knowledge-fda | ~100 | ~5000 | FDA 21 CFR 820, 510(k), PMA, De Novo |
| aria-knowledge-eumdr | ~100 | ~5000 | EU MDR 2017/745, CE marking, Technical Files |
| aria-knowledge-standards | ~100 | ~5000 | ISO 13485, IEC 62304, ISO 14971 |
| aria-knowledge-mfds | ~100 | ~5000 | Korea MFDS, Medical Device Act |
| aria-risk-management | ~100 | ~5000 | ISO 14971 risk analysis, FMEA, FTA |
| aria-design-control | ~100 | ~5000 | FDA 21 CFR 820.30, DHF/DMR/DHR |
| aria-capa-process | ~100 | ~5000 | ISO 13485 CAPA, root cause analysis |
| aria-submission-templates | ~100 | ~5000 | eCopy, PMA, CE Technical File templates |

## Progressive Disclosure System

ARIA implements a 3-level Progressive Disclosure system for token efficiency:

### Level 1: Metadata (~100 tokens)
Always loaded for skills in agent frontmatter. Contains:
- Skill name and description
- Version and category
- Trigger keywords
- Agent associations

```yaml
---
name: aria-knowledge-fda
description: >
  FDA regulations knowledge base for medical devices.
  Covers 21 CFR 820 QSR, 510(k), PMA, De Novo pathways.
metadata:
  version: "1.0.0"
  category: "domain"
  tags: "fda, regulatory, 510(k), pma"
---
```

### Level 2: Body (~5000 tokens)
Loaded when trigger conditions match. Contains:
- Full regulatory content
- Code examples and procedures
- Reference summaries
- Trigger keywords activation

### Level 3: Bundled (variable)
On-demand access. Contains:
- reference.md: Detailed reference documents
- modules/: Specialized content modules
- examples/: Use case examples

## Skill Structure

### Directory Layout
```
.claude/skills/aria/
├── SKILL.md                           # Main ARIA workflows skill
├── aria-workflows/                    # (Bundled in SKILL.md)
├── aria-templates/
│   ├── SKILL.md                       # Level 1+2 content
│   └── modules/
│       ├── INDEX.md                   # Module catalog
│       ├── brief-templates.md         # Brief phase templates
│       └── quick-reference.md         # Template quick reference
├── aria-quality-valid/
│   ├── SKILL.md
│   └── modules/
│       └── quick-reference.md         # VALID checklist
├── aria-analysis/
│   ├── SKILL.md
│   └── modules/
│       ├── INDEX.md
│       ├── feasibility-study.md       # Feasibility analysis
│       ├── requirement-analysis.md    # Requirements matrix
│       └── quick-reference.md
├── aria-research/
│   ├── SKILL.md
│   └── modules/
│       ├── INDEX.md
│       ├── web-research.md            # Web research patterns
│       └── quick-reference.md
├── aria-writing-style/
│   ├── SKILL.md
│   └── modules/
│       └── quick-reference.md         # RA/QA writing guidelines
└── aria-analytics/
    └── SKILL.md
```

### Knowledge Skills Structure (Phase 3)
```
.claude/skills/aria/
├── aria-domain-raqa/
│   ├── SKILL.md                       # Level 1+2: Domain overview
│   ├── reference.md                   # Level 3: Regulatory hierarchy
│   └── modules/
│       ├── terminology.md             # RA/QA glossary
│       ├── regulatory-hierarchy.md    # Regulation > Standard > Guidance
│       └── market-classification.md   # Global classification comparison
├── aria-knowledge-fda/
│   ├── SKILL.md                       # Level 1+2: FDA regulations
│   ├── reference.md                   # Level 3: 21 CFR 820 full text
│   └── modules/
│       ├── 21-cfr-820.md              # QSR requirements
│       ├── 510k-pathway.md            # Substantial equivalence
│       ├── pma-pathway.md             # PMA process
│       ├── de-novo-pathway.md         # De Novo classification
│       └── predicate-devices.md       # Predicate search strategies
├── aria-knowledge-eumdr/
│   ├── SKILL.md                       # Level 1+2: EU MDR
│   ├── reference.md                   # Level 3: MDR 2017/745 full text
│   └── modules/
│       ├── mdr-annex-i.md             # GSPR requirements
│       ├── classification-rules.md    # MDR Rule 1-22
│       ├── technical-file.md          # Technical File structure
│       ├── clinical-evaluation.md     # Clinical evidence requirements
│       └── eudamed.md                 # EUDAMED database
├── aria-knowledge-standards/
│   ├── SKILL.md                       # Level 1+2: ISO/IEC standards
│   ├── reference.md                   # Level 3: Standard summaries
│   └── modules/
│       ├── iso-13485.md               # QMS requirements
│       ├── iso-14971.md               # Risk management
│       ├── iec-62304.md               # Software lifecycle
│       ├── iso-14971.md               # Risk management
│       └── harmonized-standards.md    # EU/US harmonized standards
├── aria-knowledge-mfds/
│   ├── SKILL.md                       # Level 1+2: Korea MFDS
│   ├── reference.md                   # Level 3: Medical Device Act
│   └── modules/
│       ├── classification.md          # Class I-IV criteria
│       ├── approval-pathways.md       # Approval routes
│       └── postmarket.md              # PMS requirements
├── aria-risk-management/
│   ├── SKILL.md                       # Level 1+2: ISO 14971 process
│   ├── reference.md                   # Level 3: ISO 14971 full text
│   └── modules/
│       ├── risk-identification.md     # Hazard/harm analysis
│       ├── risk-estimation.md         # Severity × probability
│       ├── risk-evaluation.md         # ALARP principles
│       ├── risk-control.md            # Control measures hierarchy
│       ├── fmea.md                    # FMEA methodology
│       ├── fta.md                     # Fault Tree Analysis
│       └── risk-benefit.md            # Benefit-risk analysis
├── aria-design-control/
│   ├── SKILL.md                       # Level 1+2: 21 CFR 820.30
│   ├── reference.md                   # Level 3: Design control full text
│   └── modules/
│       ├── design-planning.md         # Design plan
│       ├── design-inputs.md           # User needs → design inputs
│       ├── design-outputs.md          # Design outputs
│       ├── design-review.md           # Design review phases
│       ├── design-verification.md     # V&V requirements
│       ├── design-validation.md       # Clinical validation
│       ├── design-transfer.md         # Design to production
│       └── design-changes.md          # Design change control
├── aria-capa-process/
│   ├── SKILL.md                       # Level 1+2: ISO 13485 CAPA
│   ├── reference.md                   # Level 3: CAPA procedures
│   └── modules/
│       ├── capa-initiation.md         # CAPA trigger criteria
│       ├── investigation.md           # Root cause analysis
│       ├── corrective-actions.md      # Correction vs CA
│       ├── preventive-actions.md      # PA strategies
│       ├── effectiveness-check.md     # Verification of effectiveness
│       └── capa-closure.md            # Closure requirements
└── aria-submission-templates/
    ├── SKILL.md                       # Level 1+2: Package templates
    ├── reference.md                   # Level 3: Template library
    └── modules/
        ├── 510k-template.md           # eCopy structure
        ├── pma-template.md            # Original PMA format
        ├── ce-technical-file.md       # Technical File structure
        ├── summary-template.md        # 510(k) Summary
        ├── indications-for-use.md     # IFU drafting
        └── declaration-of-conformity.md # EU DoC
```

## Skill Frontmatter Schema

All ARIA skills follow the Agent Skills standard with MoAI extensions:

```yaml
---
name: aria-knowledge-fda
description: >
  FDA regulations knowledge base for medical devices.
  Covers 21 CFR 820 QSR, 510(k), PMA, De Novo pathways.
license: Apache-2.0
compatibility: Designed for Claude Code
allowed-tools: Read Grep Glob Bash mcp__context7__resolve-library-id mcp__context7__get-library-docs
user-invocable: false
metadata:
  version: "1.0.0"
  category: "domain"
  status: "active"
  updated: "2026-02-09"
  modularized: "true"
  tags: "fda, regulatory, 510(k), pma, de-novo, 21-cfr-820"
  context7-libraries: fda-21-cfr-820, fda-510k, fda-pma
  agent: "expert-regulatory"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords:
    - FDA
    - 21 CFR 820
    - 510(k)
    - PMA
    - De Novo
    - predicate device
    - substantial equivalence
  agents:
    - expert-regulatory
    - expert-clinical
    - expert-submission
  phases:
    - plan
    - run
---
```

## Trigger Configuration

Skills auto-load based on trigger conditions:

### Keyword Triggers
```yaml
triggers:
  keywords:
    - regulatory
    - FDA
    - 510(k)
    - MDR
    - risk management
    - CAPA
```

### Agent Triggers
```yaml
triggers:
  agents:
    - expert-regulatory  # Loads when this agent starts
    - expert-standards
```

### Phase Triggers
```yaml
triggers:
  phases:
    - plan   # Loads during planning phase
    - run    # Loads during implementation
```

## Skill Loading Examples

### Agent Skill Loading
When `expert-regulatory` agent starts:
```yaml
skills: aria-domain-raqa, aria-knowledge-fda, aria-knowledge-eumdr
```
All three skills load Level 1 (metadata) immediately.

### Trigger-Based Loading
When user request contains "risk analysis":
1. Agent checks for keyword trigger
2. `aria-risk-management` skill loads Level 2 (full content)
3. If modules needed, Level 3 (bundled) loads on-demand

## Tool Permissions by Skill Category

### Foundation Skills (aria-domain-raqa)
- Allowed: Read, Grep, Glob, Context7 MCP
- Never: Bash, Task, Write, Edit

### Knowledge Skills (aria-knowledge-*)
- Allowed: Read, Grep, Glob, Context7 MCP
- Never: Bash, Task, Write, Edit

### Workflow Skills (aria-*)
- Allowed: Read, Write, Edit, Grep, Glob, Bash
- Never: AskUserQuestion, Task (except managers)

## Agent-Skill Mapping

### expert-regulatory
- aria-domain-raqa (always)
- aria-knowledge-fda (FDA work)
- aria-knowledge-eumdr (EU work)

### expert-standards
- aria-domain-raqa (always)
- aria-knowledge-standards (always)

### expert-risk
- aria-domain-raqa (always)
- aria-risk-management (always)

### expert-design-control
- aria-domain-raqa (always)
- aria-design-control (always)

### expert-capa
- aria-domain-raqa (always)
- aria-capa-process (always)

### expert-clinical
- aria-domain-raqa (always)
- aria-knowledge-fda (FDA clinical)
- aria-knowledge-eumdr (EU clinical)

### expert-submission
- aria-domain-raqa (always)
- aria-submission-templates (always)

### expert-audit
- aria-domain-raqa (always)
- aria-knowledge-standards (QMS audits)

## Usage Examples

### Via Agent Frontmatter
```yaml
# .claude/agents/aria/expert-regulatory.md
skills: aria-domain-raqa, aria-knowledge-fda, aria-knowledge-eumdr
```

### Via Runtime Loading
```python
# Not recommended - use agent frontmatter instead
Skill("aria-knowledge-fda")
```

## Token Budget Management

### Scenario: 510(k) Submission Preparation

**Initial Load (Level 1 only):**
- aria-domain-raqa: 100 tokens
- aria-knowledge-fda: 100 tokens
- aria-submission-templates: 100 tokens
- **Total: 300 tokens**

**After Keyword Trigger "510(k)" (Level 2 loads):**
- aria-knowledge-fda: +5000 tokens (510(k) pathway content)
- aria-submission-templates: +5000 templates
- **Total: 10,300 tokens**

**Module Access (Level 3, on-demand):**
- predicate-devices.md: ~2000 tokens (only when needed)
- **Total: 12,300 tokens**

### Savings Comparison
- **Without Progressive Disclosure:** All skills = ~45,000 tokens
- **With Progressive Disclosure:** 300 → 10,300 → 12,300 tokens
- **Savings:** 73% reduction in initial load

## Version History

- **Phase 3** (2026-02-09): 9 knowledge skills with Progressive Disclosure
- **Phase 2** (2026-02-08): Analytics skill added
- **Phase 1** (2026-02-07): Initial workflow skills

## See Also

- [../agents/aria/README.md](../../agents/aria/README.md) - ARIA Agents Catalog
- [../../../CLAUDE.md](../../../CLAUDE.md) - ARIA Execution Directive
- [https://agentskills.io](https://agentskills.io) - Agent Skills Open Standard
