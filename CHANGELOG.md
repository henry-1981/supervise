# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-02-09

### Added
- **ARIA (AI Regulatory Intelligence Assistant)** - Complete Phase 1 implementation
- Plugin structure with `.claude-plugin/plugin.json` and `capabilities.yaml`
- Orchestrator agent for central coordination and intent classification
- `/aria` command with natural language interface for RA/QA professionals
- ARIA core skill with Brief-Execute-Deliver workflow modules
- VALID quality framework skeleton (Verified, Accurate, Linked, Inspectable, Deliverable)
- `aria.yaml` configuration file with language, workflow, and quality settings
- MCP server integration (Context7, Sequential Thinking)

### Features
- **Brief-Execute-Deliver Workflow**: Three-phase regulatory task execution with 60%-30%-10% token allocation
- **Intent Classification**: Automatic categorization into document drafting, analysis, review, or search
- **User Interaction**: Korean language support with plain language error messages
- **Approval Checkpoints**: User approval required before Execute phase
- **Error Handling**: Plain language error messages with next-step guidance
- **Regulatory Citation**: Source citation for all regulatory claims
- **Quality Gates**: VALID framework for regulatory compliance

### Technical
- Plugin manifest v2.0.0 with Claude Code minVersion 1.0.0
- Orchestrator agent with Opus model, 300-second timeout
- Skill-based architecture with progressive disclosure
- MCP integration for regulatory research and complex analysis
- Configuration management with aria.yaml

### Documentation
- Complete SPEC-ARIA-001 with EARS format requirements
- CLAUDE.md with ARIA execution directives
- Comprehensive README.md (updated for ARIA)
- CHANGELOG.md entry for Phase 1 completion

## [1.0.0] - 2026-02-05

### Added
- Initial release of Cowork Supervisor plugin
- Intent Clarifier agent for understanding user requests
- Capability Discoverer agent for plugin detection
- Supervisor Planner agent for execution planning
- Orchestra agent for multi-plugin coordination
- Aggregator agent for result synthesis
- `/supervise` command for easy invocation
- Comprehensive README with installation and usage docs

### Features
- Multi-plugin orchestration with parallel/sequential execution
- Automatic plugin capability discovery
- User approval checkpoints for execution plans
- Error handling with fallback strategies
- Cross-domain result aggregation with conflict resolution
- Source attribution in final responses
