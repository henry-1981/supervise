# ARIA Technical Stack

## Core Technology

ARIA is built on Claude Code Plugin architecture with MoAI-ADK (AI Development Kit) patterns. The system leverages modern AI agent orchestration, progressive disclosure knowledge delivery, and Model Context Protocol (MCP) integration.

## Foundation Framework

Claude Code Plugin System

Claude Code provides extensible plugin architecture with agent definition, skill system, command interface, and MCP integration.

Plugin Architecture: Standalone plugin in ~/.claude/plugins/local/cowork-supervisor
Manifest: .claude-plugin/plugin.json with name, version, author metadata
Capabilities: .claude-plugin/capabilities.yaml for orchestration system

MoAI-ADK Patterns

Agent Authoring: YAML frontmatter with name, description, tools, skills, model, permissionMode
Skill Authoring: Progressive disclosure with Level 1 metadata, Level 2 body, Level 3 modules
Agent Delegation: Task() tool for specialized agent invocation with context passing
Token Optimization: 200K budget management with strategic /clear execution

## Agent System

Agent Definition Format

Location: .claude/agents/{category}/{agent-name}.md
Format: YAML frontmatter with markdown system prompt

Key Frontmatter Fields

name: Unique identifier in kebab-case
description: When to invoke with MUST INVOKE trigger keywords
tools: Tool allowlist (Read, Write, Edit, Grep, Glob, Bash, Task, etc.)
model: Model selection (opus, sonnet, haiku, inherit)
permissionMode: Permission behavior (default, acceptEdits, plan, bypassPermissions)
skills: Preloaded skill list for domain expertise
mcpServers: MCP server configuration
memory: Persistent memory scope (user, project, local)

Agent Categories

Manager Agents: Workflow coordination (manager-spec, manager-ddd, manager-docs, manager-quality)
Expert Agents: Domain implementation (expert-regulatory, expert-risk, expert-design-control)
Builder Agents: Component creation (builder-agent, builder-skill, builder-plugin)
Team Agents: Parallel execution (team-researcher, team-analyst, team-architect)

Model Assignment Strategy

Opus: High-complexity regulatory analysis (expert-regulatory, expert-standards, expert-risk, expert-clinical)
Sonnet: Process and submission workflows (expert-design-control, expert-capa, expert-submission, expert-audit)
Haiku: Fast exploration and research (team-researcher)

## Skill System

Progressive Disclosure Architecture

Three-level token optimization system

Level 1 (Metadata): Approximately 100 tokens per skill, always loaded for skills in agent frontmatter
Level 2 (Body): Approximately 5000 tokens, loaded when trigger conditions match
Level 3 (Bundled): On-demand access to modules, examples, reference documentation

Skill Definition Format

Location: .claude/skills/{category}/{skill-name}/SKILL.md
Format: YAML frontmatter with markdown content

Required Frontmatter Fields

name: Skill identifier in kebab-case (pattern: moai-{category}-{name} or aria-{category}-{name})
description: Purpose description using YAML folded scalar (>), max 1024 characters
license: SPDX license identifier (default: Apache-2.0)
compatibility: Target platform (default: Designed for Claude Code)
allowed-tools: Space-delimited tool names

Optional Frontmatter Fields

user-invocable: Slash command menu visibility (default: true)
metadata: Key-value pairs for version, category, status, updated, modularized, tags
progressive_disclosure: Token optimization configuration with enabled, level1_tokens, level2_tokens
triggers: Loading conditions with keywords, agents, phases, languages

Skill Categories

Foundation Skills: Core principles and patterns (moai-foundation-core, moai-foundation-claude)
Workflow Skills: Development workflows (moai-workflow-spec, moai-workflow-docs)
Domain Skills: Specialized expertise (aria-domain-raqa, aria-risk-management)
Language Skills: Programming language patterns (moai-lang-python, moai-lang-typescript)
Library Skills: Third-party library integration (moai-library-mermaid, moai-library-nextra)

Module System

Location: .claude/skills/{skill-name}/modules/{module-name}.md
Purpose: Extended content unlimited size, self-contained topics
Access: On-demand loading via cross-references from SKILL.md

ARIA Domain Skills: 9 skills with 22 total modules

- aria-domain-raqa: 3 modules (regulatory workflow, clinical evaluation, audit preparation)
- aria-knowledge-fda: 3 modules (21 CFR 820, 510(k) process, PMA process)
- aria-knowledge-eumdr: 5 modules (classification, clinical evaluation, technical documentation, post-market surveillance, vigilance)
- aria-knowledge-standards: 5 modules (ISO 13485, ISO 14971, IEC 62304, IEC 62366, IEC 60601)
- aria-knowledge-mfds: 1 module (MFDS regulations)
- aria-risk-management: 3 modules (FMEA analysis, risk-benefit, ALARP principle)
- aria-design-control: 4 modules (design inputs, design outputs, design validation, design transfer)
- aria-capa-process: 1 module (root cause analysis, CAPA verification)
- aria-submission-templates: 1 module (submission templates)

## MCP Integration

Model Context Protocol (MCP)

MCP enables external tool integration through standardized server protocol. ARIA integrates multiple MCP servers for enhanced capabilities.

MCP Configuration

Location: .mcp.json
Format: JSON with mcpServers object

Configured Servers

context7: Library documentation lookup
- Command: npx -y @context7/mcp
- Purpose: Up-to-date library documentation access
- Tools: mcp__context7__resolve-library-id, mcp__context7__get-library-docs

sequential-thinking: Complex problem analysis
- Purpose: Multi-step reasoning and architecture decisions
- Activation: --ultrathink flag for enhanced analysis
- Tool: mcp__sequential-thinking__sequentialthinking

notion: Database integration (planned)
- Purpose: CAPA Tracker, Risk Register, Document Registry
- API: Notion API for database operations
- Integration: Direct database read/write access

MCP Tool Loading

Deferred Loading: MCP tools must be loaded before use via ToolSearch or direct invocation
Usage Pattern: Use ToolSearch to find and load tools, then call loaded tools directly
Agent Configuration: MCP servers specified in agent frontmatter mcpServers field

## Command System

Slash Commands

Location: .claude/commands/{command-name}.md
Format: YAML frontmatter with markdown documentation

Command Definition

name: Command invocation name (e.g., supervise)
description: What the command does
parameters: Expected parameters (,,)
examples: Usage examples

ARIA Commands

supervise: Main supervision command for multi-agent orchestration
- Usage: /supervise "task description"
- Flow: Intent clarification, capability discovery, planning, orchestration, aggregation

## Quality Framework

VALID Framework

Five-pillar quality assurance system for regulatory content

Verified: All regulatory claims cite standard, section, version
- Implementation: Automatic citation validation
- Enforcement: Pre-delivery verification checklist

Accurate: Information validated against authoritative sources
- Implementation: Context7 for latest regulatory updates
- Enforcement: Source attribution requirements

Linked: Traceability maintained across artifacts
- Implementation: Notion DB integration for requirement-risk-test-document links
- Enforcement: Automatic traceability matrix generation

Inspectable: Complete audit trail for decisions
- Implementation: Decision logging with reasoning chain
- Enforcement: Audit readiness checklist

Deliverable: Final outputs meet submission criteria
- Implementation: Submission readiness validation
- Enforcement: Quality gate before delivery

TRUST 5 Framework

MoAI quality gates for code and documentation

Tested: 85%+ coverage with characterization tests
Readable: Clear naming and English comments
Unified: Consistent formatting with ruff/black
Secured: OWASP compliance and input validation
Trackable: Conventional commits with issue references

## Data Management

Notion Database Integration

Three core databases for regulatory workflow

CAPA Tracker
- Purpose: CAPA lifecycle management from issue identification to effectiveness validation
- Schema: Issue ID, description, root cause, CAPA plan, verification, effectiveness, closure
- Integration: expert-capa agent with aria-capa-process skill

Risk Register
- Purpose: ISO 14971 risk management with FMEA analysis
- Schema: Risk ID, hazard, harm, cause, controls, risk score, acceptability, review date
- Integration: expert-risk agent with aria-risk-management skill

Document Registry
- Purpose: DHF/DMR/DHR traceability matrix
- Schema: Document ID, type, version, status, linked requirements, approval date
- Integration: expert-design-control agent with aria-design-control skill

## Performance Optimization

Token Budget Management

200K token context window with strategic allocation

SPEC Phase: 30K tokens for requirement analysis
Run Phase: 180K tokens for implementation with selective file loading
Sync Phase: 40K tokens for documentation with result caching

Aggressive /clear Strategy: Execute after SPEC creation, when context exceeds 150K tokens, before major phase transitions

Progressive File Loading: Tier 1 always loaded, Tier 2 implementation-relevant, Tier 3 on-demand reference

Caching Strategy: Session-level cache for frequently accessed docs, project-specific documentation in memory, stale content eviction

## Development Workflow

MoAI SPEC-First DDD

Three-phase development workflow

Plan Phase: /moai plan creates EARS specification document
Run Phase: /moai run implements with DDD methodology (ANALYZE-PRESERVE-IMPROVE)
Sync Phase: /moai sync generates documentation and prepares deployment

Wave Parallelism Model

Concurrent wave execution for parallel development

Wave 3.1: Regulatory experts (expert-regulatory, expert-standards, expert-risk)
Wave 3.2: Process experts (expert-design-control, expert-capa)
Wave 3.3: Submission and audit (expert-submission, expert-clinical, expert-audit)

## Security and Compliance

Access Control

Permission Modes: default, acceptEdits, delegate, plan, bypassPermissions
Tool Permissions: Least privilege with allowlist approach
Sandboxing: OS-level isolation for file system and network

Regulatory Compliance

21 CFR Part 11: Electronic records and signatures
ISO 27001: Information security management
GDPR: Data protection and privacy

## Deployment

Installation Methods

Standalone Installation: Clone to ~/.claude/plugins/local/cowork-supervisor
Marketplace Installation: Via team-attention-plugins marketplace

Configuration: Register in installed_plugins.json, enable in settings.json
Version Control: Git-based version tracking with CHANGELOG.md

## Technology Stack Summary

Foundation: Claude Code Plugin + MoAI-ADK
Agent System: 8 domain experts + 9 domain skills
Knowledge System: Progressive disclosure with 22 modules
Integration: MCP (Context7, Notion, Sequential Thinking)
Data: Notion DB (CAPA, Risk, Document)
Quality: VALID + TRUST 5 frameworks
Optimization: Token budget management + caching
Deployment: Standalone plugin with marketplace distribution
