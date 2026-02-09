# Agent-Skills Multi-System Project

This project contains two independent systems for different purposes:

## System Overview

| System | Purpose | Target Users | Command | Status |
|--------|---------|--------------|---------|--------|
| **MoAI-ADK** | Software Development Automation | Developers | `/moai` | Stable (v2.2.2) |
| **ARIA** | Medical Device Regulatory Affairs | RA/QA Professionals | `/aria` | In Development (v1.0.0) |

---

## MoAI-ADK (Development Automation)

### Purpose
Autonomous software development workflow orchestration using Plan-Run-Sync pipeline.

### Command Interface
```bash
/moai [subcommand] [args]
```

### Subcommands
- `plan` - Create SPEC documents using EARS format
- `run` - Implement SPEC using DDD methodology
- `sync` - Generate documentation and create PRs
- `project` - Project documentation generation
- `feedback` - Create GitHub issues
- `fix` - Auto-fix errors (single pass)
- `loop` - Iterative auto-fix until completion

### Configuration
- **Location**: `.moai/config/`
- **Main File**: `config.yaml`
- **Section Files**:
  - `sections/quality.yaml` - TRUST 5 quality gates
  - `sections/language.yaml` - Language settings
  - `sections/user.yaml` - User information
  - `sections/workflow.yaml` - Workflow configuration

### Skills
- **Location**: `.claude/skills/moai*/`
- **Categories**:
  - `moai-foundation-*` - Core framework skills
  - `moai-workflow-*` - Workflow orchestration
  - `moai-domain-*` - Domain expertise (backend, frontend, database)
  - `moai-lang-*` - Language-specific skills
  - `moai-platform-*` - Platform integration (Auth0, Vercel, etc.)
  - `moai-tool-*` - Tool integration (AST-grep, SVG)
  - `moai-library-*` - Library expertise (shadcn, Nextra)

### Agents
- **Location**: `.claude/agents/moai/`
- **Manager Agents** (7): spec, ddd, docs, quality, project, strategy, git
- **Expert Agents** (8): backend, frontend, security, devops, performance, debug, testing, refactoring
- **Builder Agents** (4): agent, command, skill, plugin

---

## ARIA (Regulatory Affairs Assistant)

### Purpose
Medical Device Regulatory Affairs and Quality Assurance workflow automation for RA/QA professionals.

### Command Interface
```bash
/aria [subcommand] [args]
```

### Subcommands
- `brief` - Task understanding and scoping
- `execute` - Task implementation
- `deliver` - Final output generation
- `search` - Regulatory information search
- `status` - Task progress display
- `init` - Notion database initialization
- `template` - Template management
- `knowledge` - Knowledge base query
- `audit` - Audit trail lookup

### Configuration
- **Location**: `.moai/config/aria.yaml`
- **Sections**:
  - Language: Korean (ko) for user-facing responses
  - Workflow: Brief-Execute-Deliver pipeline
  - Quality: VALID framework (Verified, Accurate, Linked, Inspectable, Deliverable)

### Skills
- **Location**: `.claude/skills/aria*/`
- **Categories**:
  - `aria-core` - Core orchestration
  - `aria-domain-raqa` - RA/QA domain knowledge
  - `aria-knowledge-*` - Regulatory knowledge (FDA, EU MDR, MFDS, Standards)
  - `aria-risk-management` - ISO 14971 risk analysis
  - `aria-design-control` - Design control process
  - `aria-capa-process` - CAPA lifecycle
  - `aria-integration-*` - MCP server integrations (Context7, Notion, Google)
  - `aria-submission-templates` - Submission templates

### Agents
- **Location**: `.claude/agents/aria/`
- **Core Agents** (4): orchestrator, manager-docs, manager-quality, manager-project
- **Business Agents** (4): expert-writer, expert-analyst, expert-reviewer, expert-researcher
- **Domain Agents** (8): expert-regulatory, expert-standards, expert-risk, expert-design-control, expert-capa, expert-clinical, expert-submission, expert-audit

### Templates
- **Location**: `.claude/templates/aria/`
- **Categories**: audit, clinical, eu-mdr, fda, risk, capa

---

## System Separation Guidelines

### When to Use Each System

| Use Case | System | Command |
|----------|--------|---------|
| Software development tasks | MoAI-ADK | `/moai` |
| Code refactoring | MoAI-ADK | `/moai run SPEC-REFACTOR-XXX` |
| Bug fixing | MoAI-ADK | `/moai fix` or `/moai loop` |
| Regulatory documentation | ARIA | `/aria brief "prepare 510(k)"` |
| Risk analysis | ARIA | `/aria execute TASK-001` |
| Audit preparation | ARIA | `/aria brief "ISO 13485 audit"` |

### Configuration Independence

Each system maintains independent configuration:

```bash
# MoAI-ADK configuration
cat .moai/config/config.yaml

# ARIA configuration
cat .moai/config/aria.yaml
```

### Agent Independence

ARIA agents do NOT reference MoAI infrastructure:

```bash
# ARIA agents use only aria-* skills
# ARIA agents have no MoAI hook dependencies
# ARIA configuration is self-contained in .moai/config/aria.yaml
```

### Skill Loading

Both systems load skills from the same `.claude/skills/` directory but use naming conventions to avoid conflicts:

- MoAI skills: `moai-*` prefix
- ARIA skills: `aria-*` prefix

---

## Known Issues and Resolution Path

### Current Issue: System Co-location
Both systems share the same project directory (`/Users/hb/Project/Agent-Skills`), which was initialized as a MoAI-ADK project.

### Logical Separation Status
- [x] Command namespaces are distinct (`/moai` vs `/aria`)
- [x] Agent directories are separated (`moai/` vs `aria/`)
- [x] Skill naming follows conventions (`moai-*` vs `aria-*`)
- [x] Configuration files consolidated (`.moai/config/aria.yaml`)
- [x] Project metadata updated (`Agent-Skills`)
- [x] ARIA agents independent of MoAI hooks
- [x] ARIA agents independent of MoAI skills
- [ ] System-specific README files

### Completed Improvements

1. **Configuration Consolidation**: Moved `config/aria.yaml` to `.moai/config/aria.yaml`
2. **Project Metadata**: Updated project name to "Agent-Skills"
3. **Hook Independence**: Removed MoAI hook references from 9 ARIA agents
4. **Skill Independence**: Removed `moai-foundation-core` dependency from ARIA orchestrator
5. **Agent Placement**: Moved `aria-analytics-specialist` from `moai/` to `aria/` directory

### Remaining Improvements

1. **Documentation**: Add system-specific README files

---

## Version Information

- **MoAI-ADK**: v2.2.2
- **ARIA**: v1.0.0 (Phase 1: Core Scaffold)
- **Project**: Agent-Skills

---

## Support and Feedback

- **MoAI-ADK Issues**: `/moai feedback`
- **ARIA Issues**: `/aria feedback` (planned)
- **Documentation**: See respective system documentation

---

Last Updated: 2026-02-09
Document: ROOT_SYSTEMS.md
