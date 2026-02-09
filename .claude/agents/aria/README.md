# ARIA Agents Directory

ARIA (AI Regulatory Intelligence Assistant) agent definitions for Medical Device RA/QA workflows.

## Agent Organization

### Core Agents (4)

| Agent | Model | Purpose | Skills |
|-------|-------|---------|--------|
| orchestrator | Sonnet | Central routing and delegation | aria-workflows |
| manager-docs | Sonnet | Document lifecycle management | aria-workflows, aria-templates |
| manager-quality | Sonnet | VALID framework quality gates | aria-quality-valid, aria-analysis |
| manager-project | Sonnet | Project timeline and milestone tracking | aria-analytics |

### Business Agents (4)

| Agent | Model | Purpose | Skills |
|-------|-------|---------|--------|
| expert-writer | Sonnet | Technical document drafting | aria-writing-style, aria-templates |
| expert-analyst | Sonnet | Data analysis and interpretation | aria-analytics, aria-analysis |
| expert-reviewer | Sonnet | Document review and compliance verification | aria-quality-valid, aria-analysis |
| expert-researcher | Haiku | Regulatory information research | aria-research, aria-domain-raqa |

### RA/QA Domain Agents (8) - Phase 3

| Agent | Model | Focus Area | Key Skills |
|-------|-------|------------|------------|
| **expert-regulatory** | Opus | Regulatory strategy (FDA, EU MDR, MFDS) | aria-domain-raqa, aria-knowledge-fda, aria-knowledge-eumdr |
| **expert-standards** | Opus | Standards interpretation (ISO 13485, IEC 62304, ISO 14971) | aria-domain-raqa, aria-knowledge-standards |
| **expert-risk** | Opus | Risk management (ISO 14971, FMEA, FTA) | aria-domain-raqa, aria-risk-management |
| **expert-design-control** | Sonnet | Design control process (DHF/DMR/DHR, 21 CFR 820.30) | aria-domain-raqa, aria-design-control |
| **expert-capa** | Sonnet | CAPA lifecycle management (ISO 13485) | aria-domain-raqa, aria-capa-process |
| **expert-clinical** | Opus | Clinical evaluation and post-market surveillance | aria-domain-raqa, aria-knowledge-fda, aria-knowledge-eumdr |
| **expert-submission** | Sonnet | Submission package preparation (510(k), PMA, CE) | aria-domain-raqa, aria-submission-templates |
| **expert-audit** | Sonnet | Audit management and response (ISO 13485, QMS) | aria-domain-raqa, aria-knowledge-standards |

### Specialized Team Agents (6)

| Agent | Model | Purpose | Skills |
|-------|-------|---------|--------|
| team-fda-researcher | Haiku | FDA regulation research | aria-knowledge-fda, aria-research |
| team-predicate-analyst | Sonnet | Predicate device analysis for 510(k) | aria-knowledge-fda, aria-analysis |
| team-submission-writer | Sonnet | Submission package drafting | aria-submission-templates, aria-writing-style |
| team-capa-expert | Sonnet | CAPA investigation and resolution | aria-capa-process, aria-analysis |
| team-capa-analyst | Sonnet | CAPA trend analysis | aria-capa-process, aria-analytics |
| team-audit-researcher | Haiku | Audit finding research | aria-knowledge-standards, aria-research |

### Legacy ARIA Agents (8)

These are the original ARIA domain agents from Phase 1-2, now superseded by the expert agents above:

- aria-orchestrator, aria-regulatory, aria-risk, aria-clinical, aria-submission, aria-labeling, aria-postmarket, aria-document, aria-quality, aria-analytics-specialist

## Model Assignments

### Opus Models (High-Complexity Analysis)
Used for agents requiring deep regulatory analysis and interpretation:
- expert-regulatory
- expert-standards
- expert-risk
- expert-clinical

### Sonnet Models (Implementation & Coordination)
Used for agents focusing on document creation and workflow coordination:
- orchestrator
- manager-docs, manager-quality, manager-project
- expert-writer, expert-analyst, expert-reviewer
- expert-design-control, expert-capa, expert-submission, expert-audit
- All team agents

### Haiku Models (Research & Quick Tasks)
Used for agents focused on information retrieval and preliminary research:
- expert-researcher
- team-fda-researcher
- team-audit-researcher

## Agent Invocation

### Via ARIA Orchestrator
```bash
# Natural language routing
/aria "Prepare a 510(k) submission for a new Class II medical device"

# Direct phase invocation
/aria brief "Analyze regulatory requirements for dental imaging device"
/aria execute "Create submission package"
/aria deliver "Finalize and export documents"
```

### Via Task Tool
```python
# Direct agent delegation
Task("expert-regulatory", "Analyze FDA pathway for dental imaging device")
Task("expert-risk", "Perform ISO 14971 risk analysis")
Task("expert-submission", "Prepare 510(k) submission package")
```

## Agent Collaboration Patterns

### Regulatory Submission Workflow
1. orchestrator → Routes request based on keywords
2. expert-regulatory → Determines submission pathway (510(k), PMA, De Novo)
3. team-predicate-analyst → Researches predicate devices
4. expert-submission → Drafts submission package using templates
5. expert-reviewer → Verifies compliance with VALID framework
6. manager-docs → Finalizes document formatting

### CAPA Investigation Workflow
1. orchestrator → Identifies CAPA request
2. team-capa-analyst → Analyzes trend data
3. expert-capa → Conducts root cause analysis
4. team-capa-expert → Develops corrective actions
5. manager-quality → Validates effectiveness checks
6. manager-docs → Documents CAPA in Notion

### Audit Response Workflow
1. orchestrator → Receives audit observation
2. team-audit-researcher → Researches applicable standards
3. expert-standards → Interprets regulatory requirements
4. expert-audit → Drafts response with evidence
5. expert-reviewer → Verifies response completeness
6. manager-docs → Submits response to auditor

## Skill Loading

All agents preload relevant skills at startup (defined in agent frontmatter `skills` field):

### Foundation Skills (All Agents)
- aria-domain-raqa: Domain terminology and regulatory hierarchy

### Knowledge Skills (Domain-Specific)
- aria-knowledge-fda: FDA regulations (expert-regulatory, expert-clinical, expert-submission)
- aria-knowledge-eumdr: EU MDR (expert-regulatory, expert-clinical, expert-submission)
- aria-knowledge-standards: ISO/IEC standards (expert-standards, expert-audit)
- aria-risk-management: ISO 14971 (expert-risk)
- aria-design-control: 21 CFR 820.30 (expert-design-control)
- aria-capa-process: ISO 13485 CAPA (expert-capa)
- aria-submission-templates: Package templates (expert-submission)

### Workflow Skills (Process-Specific)
- aria-workflows: BRIEF-EXECUTE-DELIVER pipeline
- aria-templates: Document templates
- aria-quality-valid: VALID framework gates
- aria-analysis: Feasibility and requirement analysis
- aria-research: Web research methodologies
- aria-writing-style: RA/QA writing standards
- aria-analytics: Data analysis and reporting

## MCP Integration

### Context7 MCP
Loaded by all domain expert agents for up-to-date regulatory and standards documentation lookup:
```yaml
mcpServers:
  context7:
    command: npx
    args: ["-y", "@context7/mcp"]
```

### Notion MCP
Used by manager agents for knowledge base synchronization:
- Document registry
- CAPA tracker
- Risk register
- Project milestones

## Agent Configuration

Each agent is defined in its own `.md` file with YAML frontmatter:

```yaml
---
name: expert-regulatory
description: |
  RA (Regulatory Affairs) expert for medical device regulatory strategy,
  market pathway analysis, and multi-market requirements.
tools: Read, Write, Edit, Grep, Glob, Bash, TaskCreate, TaskUpdate, TaskList, TaskGet
model: opus
permissionMode: default
memory: project
skills: aria-domain-raqa, aria-knowledge-fda, aria-knowledge-eumdr
mcpServers:
  context7:
    command: npx
    args: ["-y", "@context7/mcp"]
triggers:
  keywords:
    - regulatory
    - FDA
    - 510(k)
    - MDR
    - market approval
  agents:
    - manager-spec
    - manager-docs
  phases:
    - plan
    - run
---
```

## Version History

- **Phase 3** (2026-02-09): 8 RA/QA domain expert agents with knowledge skills
- **Phase 2** (2026-02-08): Team agents for specialized workflows
- **Phase 1** (2026-02-07): Initial ARIA orchestrator and domain agents

## See Also

- [../skills/aria/README.md](../skills/aria/README.md) - ARIA Skills Catalog
- [../../CLAUDE.md](../../CLAUDE.md) - ARIA Execution Directive
- [https://agentskills.io](https://agentskills.io) - Agent Skills Open Standard
