# ARIA Codebase Structure

## Directory Organization

ARIA follows Claude Code Plugin architecture with MoAI-ADK patterns. The codebase is organized into functional directories for agents, skills, commands, and configuration.

## Root Structure

Root Directory Contents

- .claude-plugin/: Plugin manifest and capability declarations
- .claude/: Claude Code configuration and resource definitions
- agents/: Custom ARIA-specific agent definitions
- skills/: Custom ARIA-specific skill definitions
- commands/: Custom slash commands
- README.md: Project documentation and user guide
- CHANGELOG.md: Version history and release notes
- LICENSE: MIT License

## Plugin Configuration

.claude-plugin/ Directory

- plugin.json: Plugin manifest with name, version, author metadata
- capabilities.yaml: Declared capabilities for agent orchestration system

Plugin Metadata

Name: cowork-supervisor
Version: 1.0.0
Author: Henry (HB)
License: MIT

## Agent Architecture

Agents Directory Structure

Two-tier agent organization: MoAI framework agents and ARIA domain agents

.claude/agents/moai/ (Framework Agents)

- manager-ddd.md: Domain-driven development workflow specialist
- manager-docs.md: Documentation generation and validation
- manager-git.md: Git operations and branching strategy
- manager-project.md: Project configuration and structure
- manager-quality.md: Quality gates and TRUST 5 validation
- manager-spec.md: SPEC document creation with EARS format
- manager-strategy.md: System design and architecture decisions
- manager-tdd.md: Test-driven development workflow

- builder-agent.md: New agent definition creation
- builder-plugin.md: Plugin creation and packaging
- builder-skill.md: New skill creation

- expert-backend.md: API and server development
- expert-chrome-extension.md: Chrome extension development
- expert-debug.md: Debugging and troubleshooting
- expert-devops.md: CI/CD and infrastructure
- expert-frontend.md: UI and client development
- expert-performance.md: Performance optimization
- expert-refactoring.md: Code refactoring
- expert-security.md: Security analysis
- expert-testing.md: Test creation and strategy

- team-analyst.md: Requirements analysis (team mode)
- team-architect.md: Technical design (team mode)
- team-backend-dev.md: Server implementation (team mode)
- team-designer.md: UI/UX design (team mode)
- team-frontend-dev.md: Client implementation (team mode)
- team-quality.md: Quality validation (team mode)
- team-researcher.md: Codebase exploration (team mode)
- team-tester.md: Test creation (team mode)

.claude/agents/aria/ (Domain Expert Agents)

- expert-regulatory.md: FDA/MDR regulatory strategy specialist
- expert-standards.md: ISO/IEC standards compliance specialist
- expert-risk.md: ISO 14971 risk management specialist
- expert-design-control.md: Design control and DHF management specialist
- expert-capa.md: CAPA process lifecycle specialist
- expert-clinical.md: Clinical evaluation specialist
- expert-submission.md: Regulatory submission preparation specialist
- expert-audit.md: Audit preparation and support specialist

Agents Directory (Custom)

- aggregator.md: Result synthesis from multiple agents
- capability-discoverer.md: Plugin capability detection
- intent-clarifier.md: User intent understanding
- orchestra.md: Multi-agent coordination
- supervisor.md: Main orchestrator
- supervisor-planner.md: Execution planning

## Skill System

Skills Directory Structure

Progressive disclosure architecture with Level 1 metadata, Level 2 body, Level 3 modules

.claude/skills/moai/ (Framework Skills)

- SKILL.md: MoAI foundation skill
- moai-workflow-team/SKILL.md: Team coordination workflows
- moai-design-tools/SKILL.md: Design tool integration
- moai-docs-generation/SKILL.md: Documentation generation
- moai-domain-backend/SKILL.md: Backend domain patterns
- moai-domain-database/SKILL.md: Database patterns
- moai-domain-frontend/SKILL.md: Frontend domain patterns
- moai-domain-uiux/SKILL.md: UI/UX patterns
- moai-formats-data/SKILL.md: Data format optimization
- moai-foundation-claude/SKILL.md: Claude Code authoring
- moai-foundation-context/SKILL.md: Context management
- moai-foundation-core/SKILL.md: Core principles
- moai-foundation-quality/SKILL.md: Quality frameworks
- moai-library-mermaid/SKILL.md: Mermaid diagrams
- moai-library-nextra/SKILL.md: Nextra documentation
- moai-workflow-docs/SKILL.md: Documentation workflows
- moai-workflow-jit-docs/SKILL.md: Just-in-time documentation
- moai-workflow-templates/SKILL.md: Template management

.claude/skills/aria/ (Domain Skills)

- aria-domain-raqa/SKILL.md: RA/QA domain knowledge
  - modules/regulatory-workflow.md: Regulatory processes
  - modules/clinical-evaluation.md: Clinical assessment
  - modules/audit-preparation.md: Audit protocols

- aria-knowledge-fda/SKILL.md: FDA regulations
  - modules/21-cfr-820.md: QSR requirements
  - modules/510k-process.md: 510(k) submission
  - modules/pma-process.md: PMA submission

- aria-knowledge-eumdr/SKILL.md: EU MDR regulations
  - modules/classification.md: Device classification
  - modules/clinical-evaluation.md: CER requirements
  - modules/technical-documentation.md: Technical file structure
  - modules/post-market-surveillance.md: PMS requirements
  -modules/vigilance.md: Vigilance reporting

- aria-knowledge-standards/SKILL.md: ISO/IEC standards
  - modules/iso-13485.md: QMS standard
  - modules/iso-14971.md: Risk management
  - modules/iec-62304.md: Software lifecycle
  - modules/iec-62366.md: Usability engineering
  - modules/iso-14971.md: Risk management

- aria-knowledge-mfds/SKILL.md: MFDS regulations

- aria-risk-management/SKILL.md: Risk management
  - modules/fMEA-analysis.md: Failure analysis
  - modules/risk-benefit.md: Risk-benefit analysis
  - modules/alarp-principle.md: ALARP application

- aria-design-control/SKILL.md: Design control
  - modules/design-inputs.md: Input requirements
  - modules/design-outputs.md: Output verification
  - modules/design-validation.md: Validation protocols
  - modules/design-transfer.md: Transfer process

- aria-capa-process/SKILL.md: CAPA management
  - modules/root-cause-analysis.md: RCA methods
  - modules/capa-verification.md: Verification protocols

- aria-submission-templates/SKILL.md: Submission templates

Skills Directory (Custom)

- cowork-supervisor/SKILL.md: Supervisor orchestration skill

## Command System

Commands Directory

- supervise.md: Main supervision slash command

## Configuration Files

.claude/ Configuration

- settings.json: Claude Code settings
- rules/moai/: MoAI-ADK rules and patterns
  - core/: Core rules (constitution, hooks, MCP, settings)
  - development/: Development rules (agents, skills, coding standards)
  - workflow/: Workflow rules (file reading, SPEC, modes)
  - languages/: Language-specific rules (16 languages)

.moai/ Configuration

- config/: MoAI configuration sections
  - quality.yaml: Quality gates and development mode
  - workflow.yaml: Workflow execution settings
  - language.yaml: Language preferences
  - user.yaml: User information
- specs/SPEC-ARIA-003/: Specification documents
  - spec.md: Main specification
  - plan.md: Implementation plan
  - acceptance.md: Acceptance criteria
  - integration-test-report.md: Test results
  - mcp-integration-research-report.md: MCP research
  - notion-db-schema.md: Database schemas

## Output Styles

.claude/output-styles/moai/

- moai.md: MoAI output style
- r2d2.md: R2D2 personality style
- yoda.md: Yoda personality style

## Template System

.claude/templates/

- aria-agent-template.md: Agent creation template

## File Naming Conventions

Agents: {category}-{agent-name}.md
Skills: {category}-{skill-name}/SKILL.md
Modules: {module-name}.md
Commands: {command-name}.md

## Import Dependencies

Agent Imports: Skills listed in agent frontmatter skills field
Skill Imports: Referenced via @skill-name or absolute path
Module Imports: Referenced via modules/{module-name} or @skill-name/modules/{module-name}
