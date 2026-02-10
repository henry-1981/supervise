# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.1] - 2026-02-09

### Phase 1 Implementation Complete

#### Added
- **Core Orchestrator Agent**: Complete agent definition with Brief-Execute-Deliver workflow
- **/aria Command**: Full command implementation with natural language routing
- **aria-core Skill**: Core orchestration patterns and VALID quality framework
- **Plugin Manifest**: plugin.json and capabilities.yaml with complete capability declaration
- **Configuration System**: aria.yaml with language, workflow, quality, and integration settings
- **CLAUDE.md**: Complete execution directives for ARIA framework

#### Documentation
- Updated README.md with Phase 1 completion status
- Comprehensive agent routing logic documentation
- VALID quality framework implementation guide
- MCP integration architecture documentation
- Brief-Execute-Deliver workflow specification

#### Quality Verification
- All YAML configuration files validated
- Plugin structure compliant with Claude Code Plugin Specification v1.0
- File structure follows ARIA Phase 1 specifications (SPEC-ARIA-001)

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
