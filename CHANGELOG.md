# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.2.0] - 2026-02-09

### Phase 2: Universal Business Agents Implementation

This release completes the ARIA Phase 2, implementing universal business workflow agents and comprehensive skills for the Brief-Execute-Deliver workflow.

### Added

#### Core and Business Layer Agents (7 agents)
- **Core Agents (3)**: orchestrator, manager-docs, manager-quality
- **Business Expert Agents (4)**: expert-writer, expert-analyst, expert-reviewer, expert-researcher

#### Command Skills (5 skills)
- **aria-brief**: Brief Phase skill for task understanding and scope definition
- **aria-execute**: Execute Phase skill for workflow execution and agent orchestration
- **aria-deliver**: Deliver Phase skill for final quality validation and output delivery
- **aria-template**: Template management skill for regulatory document templates
- **aria-knowledge**: Knowledge base management skill with Notion MCP integration

#### Integrated Skills (21+ skills)
- **Core Skills**: aria-core, aria-quality-valid, aria-writing-style, aria-templates
- **Workflow Skills**: aria-brief, aria-execute, aria-deliver, aria-research, aria-analysis
- **Knowledge Skills**: aria-knowledge-fda, aria-knowledge-eumdr, aria-knowledge-mfds, aria-knowledge-standards
- **Domain Skills**: aria-capa-process, aria-design-control, aria-risk-management, aria-submission-templates, aria-domain-raqa
- **Integration Skills**: aria-integration-notion, aria-integration-context7, aria-integration-google

#### Template Library
- 50+ medical device regulatory document templates
- Categories: Core Regulatory, Quality Management, Technical Documentation, Review and Audit
- Templates include: 510(k) submission, CE technical file, clinical evaluation, design verification/validation, risk management report, CAPA report, and more
- All templates follow consistent structure with regulatory references and VALID quality framework

#### Knowledge Base Structure
- Notion MCP database schemas (6 databases)
- Regulatory document registry with version control
- CAPA tracker database
- Risk register management
- Submission tracking dashboard
- Audit log with decision history

### Workflow Features
- **Brief-Execute-Deliver Workflow**: Complete three-phase implementation
- **Progressive Disclosure**: Optimized token management (Level 1: ~100 tokens, Level 2: ~5000 tokens)
- **VALID Quality Framework**: 5-dimension validation (Verified, Accurate, Linked, Inspectable, Deliverable)
- **MCP Integration**: Notion, Context7, Sequential Thinking, Google Workspace (Phase 4)
- **Template-based Document Generation**: Automated regulatory document creation with quality gates
- **Knowledge Base**: Centralized regulatory knowledge with citation verification

### Technical Implementation
- Progressive disclosure system with 3-level token optimization
- MCP server integration (Context7 for regulatory research, Notion for knowledge base)
- Agent skill preloading for domain expertise
- Error handling with plain language messages and recovery guidance
- Regulatory citation verification with source tracking

### Documentation
- All agent definitions with YAML frontmatter and skill preloading
- All command skills with usage examples and MCP integration
- All skills with progressive disclosure metadata
- Template catalog with usage guidelines
- Knowledge base schema documentation

### Quality Gates
- **VALID Framework**: All 5 dimensions implemented
- **Template Compliance**: All templates follow ARIA writing style guide
- **Progressive Disclosure**: Token budgets verified (~100 tokens metadata, ~5000 tokens body)
- **MCP Integration**: Context7 and Notion server connections tested

## [2.1.0] - 2026-02-09

### Phase 1: Core Framework Implementation

This release completes the ARIA Phase 1 core framework, implementing the complete Brief-Execute-Deliver workflow for Medical Device RA/QA professionals.

### Added

#### Agent System (28 agents)
- **Manager Agents (7)**: orchestrator, manager-docs, manager-quality, manager-project, aria-clinical, aria-labeling, aria-postmarket
- **Business Expert Agents (8)**: expert-writer, expert-analyst, expert-reviewer, expert-researcher, expert-audit, expert-capa, expert-clinical, expert-design-control, expert-regulatory, expert-risk, expert-standards, expert-submission
- **Team Agents (6)**: team-audit-researcher, team-capa-analyst, team-capa-expert, team-fda-researcher, team-predicate-analyst, team-submission-writer

#### Command System (9 commands)
- **Main command**: `/aria` - Unified natural language interface
- **Subcommands**: `/aria brief`, `/aria execute`, `/aria deliver`, `/aria search`, `/aria status`, `/aria template`, `/aria knowledge`, `/aria audit`, `/aria init`

#### Skills (3 domains with 40+ files)
- **aria-core**: Brief-Execute-Deliver workflow, VALID quality framework
- **aria-capa-process**: CAPA lifecycle management
- **aria-design-control**: DHF/DMR/DHR design control documentation

#### Configuration
- `.claude-plugin/capabilities.yaml` - Plugin capability declaration
- `config/aria.yaml` - ARIA-specific configuration

### Workflow Features
- **Brief-Execute-Deliver Pipeline**: Three-phase systematic task execution
- **VALID Quality Framework**: Verified, Accurate, Linked, Inspectable, Deliverable validation
- **Agent Delegation**: Specialized agents for regulatory domain expertise
- **Regulatory Citation**: All claims cite source regulations (standard, section, version)
- **User Approval Checkpoints**: Critical decision validation before finalization

### Documentation
- CLAUDE.md: ARIA execution directives
- README.md: Updated with Phase 1 completion notes
- Agent definitions with YAML frontmatter
- Command definitions with examples
- Skill definitions with progressive disclosure

### Technical Implementation
- Progressive disclosure system for efficient token management
- MCP server integration (Context7, Sequential Thinking)
- Memory system for cross-session learning
- Error handling with plain language messages

## [2.0.0] - 2026-02-09

### Major Changes
- **Project Rebranding**: Cowork Supervisor → ARIA (AI Regulatory Intelligence Assistant)
- **Domain Specialization**: Generic multi-plugin orchestrator → Medical Device RA/QA specialist
- **Architecture Redesign**: 5-stage pipeline → Brief-Execute-Deliver workflow

### Added
- Read-Think-Write-Verify universal workflow pattern documentation
- MoAI-ADK benchmarking analysis with principle borrowing strategy
- Cowork plugin ecosystem relationship definition (independence/compatibility)
- Brief-centered token budget allocation (60%-30%-10% vs MoAI's 15%-75%-10%)
- Gatekeeper approval checkpoint between Brief and Execute phases
- Wave Parallelism model for database-centric regulatory analysis
- Dynamic Team Composition model replacing fixed file ownership
- MFDS regulatory classification correction (Class I/II/III/IV)
- Statutory law distinction (Medical Device Act / In Vitro Diagnostic Device Act / Digital Therapeutics Act)
- VALID quality framework (Verified, Accurate, Linked, Inspectable, Deliverable)
- 3-tier agent architecture (Core 4 + Business 4 + Domain 8 = 16 agents)
- Comprehensive architecture design documentation (ARCHITECTURE-REDESIGN.md)
- Project context documentation (CONTEXT.md)

### Changed
- Plan-Run-Sync → Brief-Execute-Deliver workflow terminology
- TRUST 5 → VALID quality framework adaptation for regulatory compliance
- Token budget: 60% Brief (regulatory analysis) vs MoAI's 15% Plan
- Target users: Developers → RA/QA practitioners (non-developers)
- Output: Code/test/artifacts → Regulatory documents/reports/submissions
- Version control: Git → Notion DB with traceability matrix

### Documentation
- Added comprehensive CONTEXT.md (599 lines) covering project background, MoAI-ADK benchmarking, design decisions, domain selection rationale, implementation strategy
- Added ARCHITECTURE-REDESIGN.md (2,168 lines) with complete system architecture, agent catalog, workflow design, MCP integration, RA/QA domain design, plugin ecosystem, implementation roadmap

### Removed
- Original 5-stage pipeline (Intent Clarification → Capability Discovery → Planning → Orchestration → Aggregation)
- Generic plugin orchestration focus
- Cowork Supervisor branding

## [1.0.0] - 2026-02-05

### Added
- Initial release of Cowork Supervisor plugin
- Intent Clarifier agent for understanding user requests
- Capability Discoverer agent for plugin detection
- Supervisor Planner agent for execution planning
- Orchestra agent for multi-plugin coordination
- Aggregator agent for result synthesis
- `/supervise` command for easy invocation

### Features
- Multi-plugin orchestration with parallel/sequential execution
- Automatic plugin capability discovery
- User approval checkpoints for execution plans
- Error handling with fallback strategies
- Cross-domain result aggregation with conflict resolution
- Source attribution in final responses
