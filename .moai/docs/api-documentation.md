# ARIA API Documentation

## Agent-Skill Interaction API

ARIA implements a sophisticated agent-skill interaction system where expert agents leverage domain skills through progressive disclosure architecture. This document describes the API contracts and interaction patterns.

## Agent Definition API

### Agent Frontmatter Schema

Location: `.claude/agents/{category}/{agent-name}.md`

```yaml
---
name: expert-regulatory
description: |
  RA (Regulatory Affairs) 전문가. 의료기기 규제 전략, 시장 진입 경로 분석, 규제 변경사항 모니터링, 복수국 시장 요구사항 분석에 사용하세요.
  MUST INVOKE when ANY of these keywords appear in user request:
  EN: regulatory, FDA, 510(k), PMA, De Novo, CE Marking, MDR, MFDS, market approval, submission pathway
  KO: 규제, FDA, 510(k), PMA, CE 마킹, MDR, MFDS, 시장 승인, 제출 경로
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
    - CE Marking
  agents:
    - manager-spec
    - manager-docs
  phases:
    - plan
    - run
---
```

### Agent Frontmatter Fields

**name** (required): Unique agent identifier in kebab-case

- Pattern: {category}-{role}
- Examples: expert-regulatory, expert-risk, expert-design-control
- Max length: 64 characters

**description** (required): When to invoke this agent

- Format: YAML folded scalar (>)
- Max length: 1024 characters
- Language: English (internal), Korean (user-facing)
- MUST include: "MUST INVOKE when ANY of these keywords appear"
- MUST list: EN (English) and KO (Korean) trigger keywords

**tools** (optional): Tool allowlist for this agent

- Format: Comma-separated string
- Default: Inherits all tools from parent
- Common tools: Read, Write, Edit, Grep, Glob, Bash, Task, TaskCreate, TaskUpdate
- Mutual exclusion: Cannot use with disallowedTools

**model** (optional): Model selection

- Values: opus, sonnet, haiku, inherit
- Default: inherit
- ARIA pattern: Opus for high-complexity analysis, Sonnet for process workflows

**permissionMode** (optional): Permission behavior

- Values: default, acceptEdits, delegate, plan, bypassPermissions
- Default: default
- ARIA pattern: default for most agents, plan for read-only agents

**memory** (optional): Persistent memory scope

- Values: user, project, local
- Default: None
- ARIA pattern: project for domain agents to share learnings

**skills** (optional): Preloaded domain skills

- Format: Comma-separated skill names
- Purpose: Domain expertise injection at startup
- ARIA pattern: 2-3 skills per expert agent

**mcpServers** (optional): MCP server configuration

- Format: Inline server definition or reference
- Purpose: External tool integration
- ARIA pattern: Context7 for regulatory updates, Notion for databases

**triggers** (optional): Loading conditions

- **keywords**: List of trigger terms
- **agents**: List of agents that load this agent
- **phases**: List of workflow phases (plan, run, sync)
- **languages**: Programming language list

## Skill Definition API

### Skill Frontmatter Schema

Location: `.claude/skills/{category}/{skill-name}/SKILL.md`

```yaml
---
name: aria-risk-management
description: >
  ISO 14971 위험관리 전문 지식. FMEA 분석, 위험-이익 평가, ALARP 원칙 적용,
  위험 수용성 판단, 위험관리 보고서 작성을 지원합니다.
license: Apache-2.0
compatibility: Designed for Claude Code
allowed-tools: Read Grep Glob Bash mcp__context7__resolve-library-id mcp__context7__get-library-docs
user-invocable: false
metadata:
  version: "3.0.0"
  category: "domain"
  status: "active"
  updated: "2026-02-09"
  modularized: "true"
  tags: "risk, fmea, iso-14971, alarp, medical-device"
  author: "ARIA Core Team"
  context7-libraries: "iso-14971, iso-13485"
  related-skills: "aria-design-control, aria-domain-raqa"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords:
    - risk
    - FMEA
    - hazard
    - ALARP
    - ISO 14971
    - risk assessment
    - risk analysis
    - 위험
    - 위험관리
    - FMEA 분석
  agents:
    - expert-risk
    - expert-design-control
    - expert-audit
  phases:
    - plan
    - run
  languages:
    - python
    - typescript
---
```

### Skill Frontmatter Fields

**name** (required): Skill identifier

- Pattern: {prefix}-{category}-{name}
- Prefixes: moai (framework), aria (domain)
- Examples: aria-risk-management, moai-foundation-core
- Max length: 64 characters

**description** (required): Purpose description

- Format: YAML folded scalar (>)
- Max length: 1024 characters
- Language: Korean (user-facing documentation)

**license** (optional): SPDX license identifier

- Default: Apache-2.0
- ARIA pattern: Apache-2.0 for all domain skills

**compatibility** (optional): Target platform

- Default: "Designed for Claude Code"
- Max length: 500 characters

**allowed-tools** (optional): Tool permissions

- Format: Space-delimited string
- Purpose: Security restriction
- ARIA pattern: Read, Grep, Glob, Bash, Context7 MCP

**user-invocable** (optional): Slash command visibility

- Values: true, false
- Default: true
- ARIA pattern: false for domain skills (agent-loaded only)

**metadata** (optional): Custom properties

- **version**: Semantic version as string (e.g., "3.0.0")
- **category**: foundation, workflow, domain, language, platform, library
- **status**: active, experimental, deprecated
- **updated**: ISO date string (e.g., "2026-02-09")
- **modularized**: "true" or "false"
- **tags**: Comma-separated tag list
- **author**: Skill author name
- **context7-libraries**: Comma-separated library identifiers
- **related-skills**: Comma-separated skill names

**progressive_disclosure** (optional): Token optimization

- **enabled**: Boolean
- **level1_tokens**: Approximate tokens for metadata level
- **level2_tokens**: Approximate tokens for body level

**triggers** (optional): Loading conditions

- **keywords**: List of 5-10 trigger terms
- **agents**: List of agent names
- **phases**: List of workflow phases
- **languages**: List of programming languages

## Agent-Skill Interaction Patterns

### Pattern 1: Direct Skill Loading

Agent specifies skills in frontmatter, skills load at agent startup.

```yaml
# Agent: expert-risk
skills: aria-risk-management, aria-knowledge-standards
```

**Loading Sequence**:
1. Agent invoked via Task() tool
2. Parse agent frontmatter skills field
3. Load Level 1 (metadata) for each skill
4. Check trigger conditions
5. Load Level 2 (body) if triggers match
6. Load Level 3 (modules) on-demand

**Token Cost**:
- Level 1: 100 tokens per skill (always loaded)
- Level 2: 5000 tokens per skill (trigger-based)
- Level 3: Variable (on-demand)

### Pattern 2: Trigger-Based Loading

Skills load based on trigger keyword detection.

```yaml
# Skill: aria-risk-management
triggers:
  keywords:
    - risk
    - FMEA
    - hazard
    - ISO 14971
  agents:
    - expert-risk
    - expert-design-control
```

**Trigger Conditions**:
- User request contains trigger keyword
- Agent listed in agents array is invoked
- Phase matches phases array value
- Language (if applicable) matches

### Pattern 3: MCP Tool Integration

Agent integrates MCP tools via mcpServers configuration.

```yaml
# Agent: expert-regulatory
mcpServers:
  context7:
    command: npx
    args: ["-y", "@context7/mcp"]
```

**MCP Tool Loading**:
1. Agent starts with MCP server configuration
2. Use ToolSearch to find and load MCP tools
3. Call loaded tools directly in agent execution
4. Access external data sources (Context7, Notion)

**Context7 Integration**:
```python
# Usage pattern in agent execution
mcp__context7__resolve-library_id(
    query="ISO 14971 risk management",
    libraryName="iso-14971"
)
# Returns library ID
mcp__context7__get-library-docs(
    libraryId="/iso/14971/2019",
    paths=["introduction", "terminology"]
)
# Returns documentation sections
```

### Pattern 4: Multi-Skill Coordination

Agent coordinates multiple skills for complex workflows.

```yaml
# Agent: expert-design-control
skills: aria-design-control, aria-risk-management, aria-knowledge-standards
```

**Coordination Pattern**:
1. Load all skills (Level 1 metadata)
2. Evaluate triggers for each skill
3. Load relevant skills (Level 2 body)
4. Cross-reference skill modules
5. Synthesize outputs from multiple skills

**Example Workflow**:
```
User: "Design verification protocol for surgical instrument"
→ expert-design-control agent invoked
→ aria-design-control skill loaded (design-validation.md module)
→ aria-risk-management skill loaded (FMEA analysis for verification)
→ aria-knowledge-standards skill loaded (ISO 13485 verification requirements)
→ Synthesize protocol with risk-based verification points
```

## Module Access API

### Module Reference Syntax

Skills reference modules using cross-reference syntax.

```markdown
See @aria-risk-management/modules/fMEA-analysis.md for FMEA templates
```

**Module Loading**:
1. Detect @ syntax in skill body
2. Load referenced module on-demand
3. Include module content in context
4. Enable deep-dive access without token overhead

### Module Structure

Location: `.claude/skills/{skill-name}/modules/{module-name}.md`

```markdown
# FMEA Analysis

## Overview
Failure Modes and Effects Analysis framework...

## Process
1. Identify failure modes
2. Assess severity (1-10)
3. Assess occurrence (1-10)
4. Assess detection (1-10)
5. Calculate RPN (Severity × Occurrence × Detection)
6. Prioritize high RPN items

## Template
[Provide FMEA template structure]

## Examples
[Provide example FMEA analysis]
```

**Module Content**:
- Unlimited size (no token limits)
- Self-contained topics
- Cross-referenced from SKILL.md
- Loaded on-demand based on user needs

## Agent Communication API

### Task() Tool Invocation

Agents invoke other agents via Task() tool.

```python
Task(
    subagent_type="expert-risk",
    prompt="Perform FMEA analysis for surgical instrument",
    context={
        "device_type": "surgical",
        "intended_use": "cutting tissue",
        "user_requirements": ["precision", "safety"]
    }
)
```

**Task Parameters**:
- **subagent_type**: Target agent name (required)
- **prompt**: Task description (required)
- **context**: Data dictionary (optional)

**Agent Handoff**:
1. Create handoff package with session context
2. Invoke Task() with target agent
3. Pass context and task requirements
4. Receive structured response from agent
5. Synthesize into final output

### Multi-Agent Orchestration

Orchestra agent coordinates multiple agents in parallel.

```python
# Sequential execution (dependencies exist)
Task(expert-risk, "Perform FMEA analysis")
→ Task(expert-design-control, "Create design controls based on risks")

# Parallel execution (independent tasks)
Parallel(
    Task(expert-regulatory, "Analyze FDA pathway"),
    Task(expert-standards, "Check ISO 13485 requirements"),
    Task(expert-clinical, "Assess clinical evidence needs")
)
→ Aggregate results into comprehensive strategy
```

## Quality Validation API

### VALID Framework Enforcement

Agents validate outputs against VALID criteria.

```python
# Validation checklist before delivery
validated = {
    "verified": check_citations(standard="ISO 14971", section="4.2", version="2019"),
    "accurate": validate_source(authoritative=True),
    "linked": verify_traceability(requirements, risks, tests),
    "inspectable": audit_trail_complete(),
    "deliverable": submission_ready_check()
}

if all(validated.values()):
    deliver_output()
else:
    request_revision()
```

### TRUST 5 Framework Enforcement

Manager-quality agent validates code quality.

```python
# Quality gate checklist
trust5 = {
    "tested": coverage_check(minimum=85),
    "readable": naming_conventions_check(),
    "unified": format_check(formatter="black"),
    "secured": owasp_check(),
    "trackable": commit_message_check(pattern="conventional")
}

if all(trust5.values()):
    approve_merge()
else:
    request_fixes()
```

## Configuration API

### MoAI Configuration Files

**.moai/config/sections/quality.yaml**:
```yaml
constitution:
  development_mode: "ddd"
  test_coverage_target: 85
  lsp_quality_gates:
    enabled: true
    run:
      max_errors: 0
      max_type_errors: 0
```

**.moai/config/sections/workflow.yaml**:
```yaml
workflow:
  auto_clear: true
  plan_tokens: 30000
  run_tokens: 180000
  sync_tokens: 40000
```

**.moai/config/sections/language.yaml**:
```yaml
language:
  conversation_language: "ko"
  documentation: "ko"
  code_comments: "ko"
```

## Notion Integration API

### Database Schema Definitions

Location: `.moai/specs/SPEC-ARIA-003/notion-db-schema.md`

**CAPA Tracker Schema**:
```json
{
  "database_id": "capa_tracker",
  "properties": {
    "Issue ID": {"type": "title"},
    "Description": {"type": "text"},
    "Root Cause": {"type": "text"},
    "CAPA Plan": {"type": "text"},
    "Verification": {"type": "text"},
    "Effectiveness": {"type": "select"},
    "Status": {"type": "select"},
    "Due Date": {"type": "date"}
  }
}
```

**Notion API Usage**:
```python
# Create CAPA entry
notion.pages.create(
    parent={"database_id": "capa_tracker"},
    properties={
        "Issue ID": {"title": [{"text": {"content": "CAPA-001"}}]},
        "Description": {"text": [{"content": "Non-conforming product detected"}]},
        "Status": {"select": {"name": "Open"}}
    }
)

# Query Risk Register
notion.databases.query(
    database_id="risk_register",
    filter={
        "property": "Risk Score",
        "number": {"greater_than": 50}
    }
)
```

## Error Handling API

### Agent Error Recovery

```python
try:
    result = Task(expert-risk, "Perform FMEA analysis")
except AgentError as e:
    # Fallback strategy
    if e.error_type == "skill_not_loaded":
        load_skill("aria-risk-management")
        retry_task()
    elif e.error_type == "mcp_unavailable":
        use_cached_regulatory_content()
    elif e.error_type == "token_limit":
        execute_clear_and_resume()
```

### Skill Loading Errors

```python
# Skill validation checklist
skill_valid = {
    "metadata_present": check_frontmatter_fields(),
    "level1_accessible": verify_level1_loading(),
    "triggers_configured": check_trigger_keywords(),
    "modules_exist": verify_module_files()
}

if not all(skill_valid.values()):
    report_skill_loading_error(skill_name)
```

## Performance Optimization API

### Token Budget Management

```python
# Token monitoring
token_budget = {
    "total": 200000,
    "used": calculate_used_tokens(),
    "available": 200000 - calculate_used_tokens()
}

if token_budget["available"] < 30000:
    # Aggressive clearing
    execute_clear()
    reload_level1_skills()
    resume_from_checkpoint()
```

### Progressive Disclosure Optimization

```python
# Skill loading optimization
if urgent_request:
    # Load only Level 1 (metadata)
    load_skill_metadata("aria-risk-management")
elif detailed_analysis_required:
    # Load Level 2 (body)
    load_skill_body("aria-risk-management")
if specific_module_needed:
    # Load Level 3 (modules)
    load_skill_module("aria-risk-management/modules/fMEA-analysis.md")
```

## Summary

ARIA API provides comprehensive interfaces for:

- Agent definition with YAML frontmatter schema
- Skill definition with progressive disclosure
- Agent-skill interaction patterns
- MCP integration (Context7, Notion)
- Multi-agent orchestration
- Quality framework enforcement (VALID, TRUST 5)
- Notion database integration
- Error handling and recovery
- Performance optimization

For detailed implementation examples, see:
- Agent definitions: `.claude/agents/aria/`
- Skill definitions: `.claude/skills/aria-/`
- Integration tests: `.moai/specs/SPEC-ARIA-003/integration-test-report.md`
