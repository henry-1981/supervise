# SPEC-ARIA-001: ARIA Phase 1 - Core Framework Implementation

## TAG BLOCK

```yaml
SPEC_ID: SPEC-ARIA-001
TITLE: ARIA Phase 1 - Core Framework Implementation
VERSION: 1.0.0
STATUS: Planned
PRIORITY: High
DOMAIN: aria-core
PHASE: 1
CREATED: 2026-02-09
AUTHOR: ARIA Architect
ASSIGNED: orchestrator
RELATED_SPECS:
```

---

## Environment

### System Context

**Project**: ARIA (AI Regulatory Intelligence Assistant)
**Type**: Claude Code Plugin
**Target Domain**: Medical Device RA/QA (Regulatory Affairs / Quality Assurance)
**Target Users**: Non-developer business professionals (RA/QA practitioners, QA engineers, design engineers)

### Technical Environment

**Platform**: Claude Code Plugin System
**Host Environment**: Claude Code Desktop/CLI
**Plugin Standard**: Claude Code Plugin Specification v1.0
**Language Support**: Korean (primary user-facing), English (internal agent communication)

### Integration Context

**MoAI-ADK Relationship**: ARIA borrows architectural principles from MoAI-ADK but specializes for regulatory workflows
**Plugin Ecosystem**: Part of Cowork plugin ecosystem with independent functionality
**MCP Dependencies**: Context7 MCP, Sequential Thinking MCP (Phase 1), Notion MCP (Phase 4)

---

## Assumptions

### Technical Assumptions

- [A1] Claude Code Plugin API supports agent definitions, commands, skills, and hooks
- [A2] MCP (Model Context Protocol) servers can be configured via `.mcp.json`
- [A3] Plugin directory structure follows `.claude-plugin/` convention with `plugin.json` manifest
- [A4] Agent definitions use YAML frontmatter in `.claude/agents/` markdown files
- [A5] Command definitions use YAML frontmatter in `.claude/commands/` markdown files
- [A6] Skills use progressive disclosure with SKILL.md and modules/ structure

### Domain Assumptions

- [A7] RA/QA practitioners are comfortable with natural language interfaces but not coding
- [A8] Regulatory workflows follow Read-Think-Write-Verify pattern universally
- [A9] VALID quality framework (Verified, Accurate, Linked, Inspectable, Deliverable) is appropriate for regulatory compliance
- [A10] Brief phase requires heavy token allocation (60%) for database-driven regulatory analysis

### User Assumptions

- [A11] Users prefer Korean language for all interactions (conversation_language: ko)
- [A12] Users require plain language error messages with clear next-step guidance
- [A13] Users expect approval checkpoints before major regulatory decisions

### Integration Assumptions

- [A14] Context7 MCP provides up-to-date regulatory documentation lookup
- [A15] Sequential Thinking MCP supports complex regulatory pathway analysis

---

## Requirements (EARS Format)

### Ubiquitous Requirements (Always Active)

**[UR-001] 시스템은 항상 한국어로 사용자 응답을 제공해야 한다.**

- **Rationale**: Target users are Korean RA/QA practitioners
- **Verification**: All user-facing output uses Korean; internal agent communication uses English
- **Acceptance**: No English responses exposed to end users

**[UR-002] 시스템은 항상 평이한 언어로 오류 메시지를 제공해야 한다.**

- **Rationale**: Non-developer users cannot interpret technical error messages
- **Verification**: Error messages use plain Korean with next-step guidance
- **Acceptance**: No technical jargon (e.g., "token limit exceeded") without explanation

**[UR-003] 시스템은 항상 규제 인용을 출처와 함께 제공해야 한다.**

- **Rationale**: Regulatory accuracy requires source verification
- **Verification**: All regulatory claims cite standard, section, and version
- **Acceptance**: No unsupported regulatory assertions

### Event-Driven Requirements (When-Then)

**[ER-001] WHEN 사용자가 `/aria` 명령어를 입력하면, 시스템은 사용자 의도를 분류해야 한다.**

- **Intent Categories**: 문서 작성(document drafting), 분석(analysis), 검토(review), 검색(search)
- **Method**: Keyword matching + Sequential Thinking MCP for complex queries
- **Output**: Classified intent with confidence score
- **Verification**: Test with natural language queries across all categories

**[ER-002] WHEN 사용자 의도가 분류되면, 시스템은 AskUserQuestion으로 범위를 정의해야 한다.**

- **Maximum Options**: 4 options per question
- **Language**: Korean (conversation_language: ko)
- **Purpose**: Scope clarification, regulatory pathway selection, market identification
- **Verification**: User interaction test with multi-choice questions

**[ER-003] WHEN 명확한 범위가 정의되면, 시스템은 Brief-Execute-Deliver 워크플로우를 시작해야 한다.**

- **Brief Phase**: Regulatory strategy analysis with user approval checkpoint
- **Execute Phase**: Document preparation with domain experts
- **Deliver Phase**: Quality-validated output
- **Token Allocation**: 60%-30%-10% (Brief-Execute-Deliver)
- **Verification**: End-to-end workflow test with simple document request

**[ER-004] WHEN 오류가 발생하면, 시스템은 평이한 언어로 복구 옵션을 제안해야 한다.**

- **Error Types**: Connection issues, missing information, regulatory ambiguity
- **Response Format**: Problem explanation + next-step guidance
- **Maximum Retries**: 3 automatic retries before user intervention
- **Verification**: Error scenario simulation tests

### State-Driven Requirements (If-Then)

**[SR-001] IF Phase 1 구현이 진행 중이면, 시스템은 플러그인 스캐폴드만 제공해야 한다.**

- **Scope**: Plugin structure, basic orchestration, /aria command
- **Exclusions**: RA/QA domain agents (Phase 3), MCP integrations (Phase 4)
- **Verification**: Feature completeness check against Phase 1 scope

**[SR-002] IF 사용자가 승인 체크포인트에 도달하면, 시스템은 전략 개요를 제시하고 승인을 요청해야 한다.**

- **Checkpoint**: Brief phase completion before Execute phase
- **Content**: Regulatory strategy, proposed approach, resource estimates
- **User Action**: Approve, modify, or request clarification
- **Verification**: Approval checkpoint test with realistic scenario

### Unwanted Requirements (Shall Not)

**[WR-001] 시스템은 사용자에게 기술적인 용어로 오류를 보고하면 안 된다.**

- **Prohibited**: Raw exception messages, stack traces, technical jargon
- **Required**: Plain language explanation with context
- **Example**: "서버 연결이 원활하지 않습니다. 30초 후 다시 시도합니다." instead of "ECONNREFUSED"

**[WR-002] 시스템은 출처 없이 규제 정보를 제시하면 안 된다.**

- **Prohibited**: Unsupported regulatory claims, uncited standards
- **Required**: Standard name, section number, version/date
- **Example**: "FDA 21 CFR Part 820.30(i)" instead of "FDA design controls"

**[WR-003] 시스템은 단일 질문에서 4개 이상의 옵션을 제시하면 안 된다.**

- **Prohibited**: AskUserQuestion with more than 4 options
- **Required**: Split complex decisions into multiple questions
- **Verification**: Question design review across all user interactions

### Optional Requirements (Nice to Have)

**[OR-001] 가능하면, 시스템은 진행 상황을 시각적으로 표시해야 한다.**

- **Features**: Progress indicators, phase completion markers, agent activity
- **Benefit**: Improved user experience during long-running operations
- **Priority**: Medium (can be deferred to Phase 2)

**[OR-002] 가능하면, 시스템은 자주 묻는 질문(FAQ)을 제공해야 한다.**

- **Content**: Common regulatory questions, command usage, troubleshooting
- **Format**: Accessible via `/aria help` command
- **Priority**: Low (documentation can be manual initially)

---

## Specifications

### S1: Plugin Structure

**[S1.1] Plugin Manifest**

파일 위치: `.claude-plugin/plugin.json`

```json
{
  "name": "aria-core",
  "description": "AI Regulatory Intelligence Assistant for Medical Device RA/QA professionals",
  "version": "2.0.0",
  "author": {
    "name": "ARIA Team",
    "email": "aria@example.com"
  },
  "claudeCode": {
    "minVersion": "1.0.0"
  },
  "capabilities": {
    "commands": ["aria"],
    "agents": ["orchestrator"],
    "skills": ["aria-core"],
    "mcpServers": ["context7", "sequential-thinking"]
  }
}
```

**[S1.2] Directory Structure**

```
supervise/
├── .claude-plugin/
│   ├── plugin.json                 # Plugin manifest (S1.1)
│   └── capabilities.yaml           # Capability declaration
├── .claude/
│   ├── agents/
│   │   └── aria/
│   │       └── orchestrator.md     # Main orchestrator agent (S2)
│   ├── commands/
│   │   └── aria.md                 # /aria command (S3)
│   └── skills/
│       └── aria-core/
│           ├── SKILL.md            # Core orchestration skill
│           └── modules/
│               ├── workflow.md     # Brief-Execute-Deliver workflow
│               └── quality.md      # VALID framework (stub for Phase 1)
├── aria.yaml                       # ARIA configuration (S4)
├── CLAUDE.md                       # ARIA execution directives
└── README.md                       # User documentation
```

### S2: Orchestrator Agent

**[S2.1] Agent Definition**

파일 위치: `.claude/agents/aria/orchestrator.md`

```yaml
---
name: orchestrator
description: >
  ARIA의 중앙 오케스트레이터. 사용자 요청을 분석하고
  적절한 전문 에이전트에 위임한다. Brief-Execute-Deliver
  워크플로우를 조율하며 모든 사용자 상호작용의 단일 진입점이다.
model: opus
permissionMode: default
tools: Task, AskUserQuestion, Read, Grep, Glob, Bash
skills:
  - aria-core
  - moai-foundation-core
mcpServers:
  - context7
  - sequential-thinking
memory: project
---

# Orchestrator Agent

## Core Responsibilities

1. **Intent Analysis**: Classify user requests into document drafting, analysis, review, or search
2. **Workflow Routing**: Route to appropriate Brief-Execute-Deliver phase
3. **Agent Delegation**: Delegate tasks to specialized agents
4. **User Interaction**: Use AskUserQuestion for scope clarification (max 4 options)
5. **Error Handling**: Provide plain language error messages with next-step guidance

## Intent Classification

When user provides input, analyze intent using keyword matching and Sequential Thinking MCP:

- **Document Drafting**: 작성, 생성, prepare, draft, write
- **Analysis**: 분석, analyze, assess, evaluate
- **Review**: 검토, review, audit, check
- **Search**: 검색, search, find, lookup

## User Interaction Protocol

All user-facing responses MUST be in Korean (conversation_language: ko).
All internal agent communication uses English.

## Error Handling

Error messages MUST:
- Use plain Korean language
- Avoid technical jargon
- Provide clear next-step guidance
- Include recovery options

Example: "서버 연결이 원활하지 않습니다. 30초 후 다시 시도합니다. 문제가 지속되면 네트워크 연결을 확인해 주세요."
```

**[S2.2] Intent Classification Logic**

```
IF keywords contain ["작성", "생성", "prepare", "draft", "write"]
  THEN intent = "document drafting"

ELSE IF keywords contain ["분석", "analyze", "assess", "evaluate"]
  THEN intent = "analysis"

ELSE IF keywords contain ["검토", "review", "audit", "check"]
  THEN intent = "review"

ELSE IF keywords contain ["검색", "search", "find", "lookup"]
  THEN intent = "search"

ELSE
  THEN use Sequential Thinking MCP for complex analysis
```

### S3: /aria Command

**[S3.1] Command Definition**

파일 위치: `.claude/commands/aria.md`

```yaml
---
name: aria
description: >
  ARIA(AI Regulatory Intelligence Assistant) 메인 명령어.
  의료기기 RA/QA 전문가를 위한 규제 업무 지원.
parameters:
  - name: query
    description: 규제 업무 요청 (자연어)
    required: false
    default: ""
examples:
  - "/aria '510(k) 제출 준비 도와주세요'"
  - "/aria 'ISO 13485 내부 심사 준비'"
  - "/aria help"
---

# /aria Command

## Usage

```
/aria [query]
```

## Parameters

- **query** (optional): 자연어 규제 업무 요청

## Examples

1. 510(k) submission preparation:
   ```
   /aria "510(k) 제출 준비 도와주세요"
   ```

2. ISO 13485 internal audit:
   ```
   /aria "ISO 13485 내부 심사 준비"
   ```

3. Help command:
   ```
   /aria help
   ```

## Behavior

When query is provided:
1. Analyze intent using orchestrator agent
2. Ask clarifying questions if needed (max 4 options)
3. Present Brief phase strategy for approval
4. Execute with domain experts
5. Deliver quality-validated output

When query is omitted:
1. Display ARIA introduction
2. Show common use cases
3. Provide help command reference
```

**[S3.2] Command Behavior Flow**

```
USER INPUT: /aria "510(k) 제출 준비"

┌─────────────────────────────────────────┐
│ 1. Intent Analysis                     │
│    - Classify: document drafting       │
│    - Domain: FDA 510(k)                │
│    - Scope: submission preparation     │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│ 2. Scope Definition (AskUserQuestion)   │
│    - Device classification?             │
│      [Class I] [Class II] [Class III]   │
│    - Predicate device known?            │
│      [Yes, specify] [No, search]        │
│    - Target market?                     │
│      [US only] [US + EU] [Global]       │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│ 3. Brief Phase (60% token budget)       │
│    - Regulatory pathway analysis        │
│    - Predicate device search            │
│    - Submission requirements            │
│    - Present strategy for approval      │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│ 4. User Approval Checkpoint             │
│    - Review regulatory strategy         │
│    - [Approve] [Modify] [Clarify]       │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│ 5. Execute Phase (30% token budget)     │
│    - Delegate to domain agents          │
│    - Document preparation               │
│    - Quality validation                 │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│ 6. Deliver Phase (10% token budget)     │
│    - VALID quality gates                │
│    - Format and package                 │
│    - Distribution (Phase 4: Notion)     │
└─────────────────────────────────────────┘
```

### S4: Configuration File

**[S4.1] aria.yaml Structure**

파일 위치: `aria.yaml` (project root)

```yaml
# ARIA Configuration File
# Version: 1.0.0

# Language Settings
language:
  # User-facing response language (ISO 639-1)
  conversation_language: ko
  conversation_language_name: Korean (한국어)

  # Internal agent communication language
  agent_prompt_language: en

  # Regulatory document language
  documentation_language: ko

# Workflow Settings
workflow:
  # Brief-Execute-Deliver workflow
  phases:
    brief:
      # Token budget percentage
      token_budget: 60
      # User approval required before Execute
      require_approval: true
      # Maximum questions per scope definition
      max_questions: 5

    execute:
      token_budget: 30
      # Maximum parallel agents
      max_parallel_agents: 3

    deliver:
      token_budget: 10
      # Quality gates enforcement
      enforce_valid: true

# Quality Framework
quality:
  # VALID Framework (Verified, Accurate, Linked, Inspectable, Deliverable)
  valid:
    verified:
      # Verify against original regulations
      enabled: true
      # Require source citations
      require_citations: true
      # Citation format: standard, section, version
      citation_format: "{standard} {section} ({version})"

    accurate:
      # Data validation
      enabled: true
      # Reference check date range
      reference_check_days: 365

    linked:
      # Traceability matrix
      enabled: true
      # Requirement-document-evidence linking
      traceability: true

    inspectable:
      # Audit trail
      enabled: true
      # Decision rationale documentation
      decision_rationale: true

    deliverable:
      # Format validation
      enabled: true
      # Submission format templates
      templates: true

# Agent Settings (Phase 1: Core agents only)
agents:
  orchestrator:
    model: opus
    timeout_seconds: 300

  # Business agents (Phase 2)
  manager_docs:
    model: sonnet
    timeout_seconds: 180

  manager_quality:
    model: sonnet
    timeout_seconds: 120

  manager_project:
    model: sonnet
    timeout_seconds: 60

# Integration Settings
integrations:
  # MCP Servers (Phase 1)
  mcp:
    context7:
      enabled: true
      timeout_seconds: 30

    sequential_thinking:
      enabled: true
      timeout_seconds: 60

    notion:
      enabled: false  # Phase 4
      timeout_seconds: 30

# Error Handling
error_handling:
  # Maximum retries for transient errors
  max_retries: 3

  # Retry delay (seconds)
  retry_delay: 30

  # Plain language error messages
  plain_language: true

  # Next-step guidance
  next_step_guidance: true

# Development Settings
development:
  # Debug mode
  debug: false

  # Log level: error, warn, info, debug
  log_level: info

  # Feature flags
  features:
    progress_indicators: false  # Phase 2
    faq: false  # Phase 2
    agent_memory: false  # Phase 5
```

**[S4.2] Configuration Loading**

Configuration loading priority:
1. `aria.yaml` (project root)
2. `.claude/settings.json` (Claude Code settings)
3. Default values

### S5: Workflow Skeleton

**[S5.1] Brief Phase Skeleton**

Brief phase goal: Regulatory strategy analysis with user approval checkpoint

```
BRIEF PHASE (60% token budget)
├── Intent Analysis
│   ├── Keyword matching
│   └── Sequential Thinking MCP (complex queries)
├── Scope Definition
│   ├── AskUserQuestion (max 4 options)
│   └── Maximum 5 questions
├── Regulatory Mapping
│   ├── Applicable regulations/standards
│   ├── Classification and pathway
│   └── Requirements identification
├── Strategy Development
│   ├── Approach options
│   ├── Resource estimates
│   └── Risk assessment
└── Approval Checkpoint
    ├── Present strategy overview
    ├── User decision: [Approve] [Modify] [Clarify]
    └── Gatekeeper function: Brief → Execute transition
```

**[S5.2] Execute Phase Skeleton**

Execute phase goal: Document preparation with domain experts (Phase 1: orchestrator only)

```
EXECUTE PHASE (30% token budget)
├── Task Decomposition
│   ├── Document structure
│   ├── Section requirements
│   └── Evidence collection
├── Agent Dispatch (Phase 1: orchestrator handles all)
│   ├── Core: manager-docs, manager-quality, manager-project
│   ├── Business: (Phase 2)
│   └── Domain: (Phase 3)
├── Document Preparation
│   ├── Template-based drafting
│   ├── Content generation
│   └── Validation checks
└── Quality Gates
    ├── VALID framework (stub for Phase 1)
    ├── Compliance verification
    └── Review cycle
```

**[S5.3] Deliver Phase Skeleton**

Deliver phase goal: Quality-validated output (Phase 1: local file output)

```
DELIVER PHASE (10% token budget)
├── Quality Review
│   ├── VALID framework verification
│   ├── Completeness check
│   └── Format validation
├── Format Conversion
│   ├── Markdown (default)
│   ├── PDF (Phase 2)
│   └── Word (Phase 2)
├── Packaging
│   ├── Document assembly
│   ├── Metadata attachment
│   └── Version labeling
└── Distribution (Phase 1: local files)
    ├── Local file system
    ├── Console output
    └── Notion MCP (Phase 4)
```

### S6: Error Handling

**[S6.1] Error Classification**

```
ERROR TYPES:

1. Connection Errors
   - Symptom: MCP server unreachable
   - Message: "서버 연결이 원활하지 않습니다. 30초 후 다시 시도합니다."
   - Recovery: Automatic retry (max 3)

2. Missing Information
   - Symptom: Insufficient context for task
   - Message: "추가 정보가 필요합니다. [질문] [옵션1] [옵션2] [옵션3] [옵션4]"
   - Recovery: AskUserQuestion for clarification

3. Regulatory Ambiguity
   - Symptom: Conflicting or unclear regulatory requirements
   - Message: "규제 요구사항이 명확하지 않습니다. 전문가 검토가 권장됩니다."
   - Recovery: Present options, request user decision

4. Token Limit
   - Symptom: Context window approaching limit
   - Message: "작업이 복잡하여 단계별로 진행하겠습니다. 계속하시겠습니까?"
   - Recovery: AskUserQuestion for continuation

5. Agent Failure
   - Symptom: Sub-agent task failure
   - Message: "작업에 실패했습니다. 다른 방법을 시도하시겠습니까?"
   - Recovery: Fallback strategy or user decision
```

**[S6.2] Error Message Template**

```markdown
## 문제 발생

[평이한 언어로 문제 설명]

### 원인

[기술적 원인을 평이한 언어로 변환]

### 다음 단계

1. [복구 옵션 1]
2. [복구 옵션 2]
3. [복구 옵션 3]

도움이 필요하시면 `/aria help`를 입력하세요.
```

### S7: MCP Integration

**[S7.1] .mcp.json Configuration**

파일 위치: `.mcp.json` (project root)

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@context7/mcp"],
      "description": "Up-to-date regulatory documentation lookup"
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"],
      "description": "Complex regulatory pathway analysis"
    }
  }
}
```

**[S7.2] Context7 MCP Usage (Phase 1)**

Context7 MCP provides up-to-date regulatory documentation lookup.

Usage in Brief phase:
- Search for latest FDA guidance documents
- Retrieve current ISO standard versions
- Verify regulation citations

Example usage pattern:
```
1. User query: "510(k) submission requirements"
2. Orchestrator identifies need for current FDA guidance
3. Context7 MCP search: "FDA 510(k) guidance 2024"
4. Retrieve and validate citation information
5. Include in Brief phase strategy
```

**[S7.3] Sequential Thinking MCP Usage (Phase 1)**

Sequential Thinking MCP supports complex regulatory pathway analysis.

Usage in Brief phase:
- Regulatory pathway decision support
- Substantial equivalence logic development
- Multi-market strategy analysis

Example usage pattern:
```
1. User query: "Class II device US + EU market entry strategy"
2. Orchestrator initiates Sequential Thinking MCP
3. Step-by-step analysis:
   - FDA classification and pathway
   - EU MDR classification and route
   - Common requirements and differences
   - Optimal market entry sequence
4. Present synthesized strategy for user approval
```

---

## Traceability

### Requirement-to-Specification Mapping

| Requirement | Specification | Verification |
|-------------|---------------|--------------|
| UR-001 (Korean responses) | S2.1, S3.1, S5.x | Language check in all user output |
| UR-002 (Plain language errors) | S6.1, S6.2 | Error message review |
| UR-003 (Regulatory citations) | S5.1, S7.2 | Citation format validation |
| ER-001 (Intent classification) | S2.2, S3.2 | Intent classification test |
| ER-002 (Scope definition) | S3.2, S5.1 | AskUserQuestion test |
| ER-003 (Workflow initiation) | S5.1-S5.3 | End-to-end workflow test |
| ER-004 (Error handling) | S6.1, S6.2 | Error scenario simulation |
| SR-001 (Phase 1 scope) | S1.1, S1.2 | Feature completeness check |
| SR-002 (Approval checkpoint) | S5.1, S5.2 | Approval checkpoint test |
| WR-001 (No technical errors) | S6.2 | Error message review |
| WR-002 (No unsupported claims) | S5.1, S7.2 | Citation validation |
| WR-003 (Max 4 options) | S2.1, S3.2 | Question design review |

### VALID Quality Framework Traceability

**V**erified:
- All regulatory claims cite source (UR-003, WR-002)
- Context7 MCP provides current documentation (S7.2)

**A**ccurate:
- Configuration validation (S4.2)
- Error recovery mechanisms (S6.1)

**L**inked:
- Requirement-to-specification traceability matrix (above)
- Brief-Execute-Deliver phase linkage (S5.x)

**I**nspectable:
- Decision rationale documentation (S4.1: decision_rationale)
- Audit trail capability (S4.1: inspectable.enabled)

**D**eliverable:
- Plugin structure follows Claude Code standard (S1.1, S1.2)
- Output format validation (S5.3)

---

## Dependencies

### External Dependencies

- **Claude Code**: Plugin API v1.0+
- **Context7 MCP**: Regulatory documentation lookup
- **Sequential Thinking MCP**: Complex analysis support

### Internal Dependencies

- **MoAI-ADK Principles**: Architectural patterns (not runtime dependency)
- **Cowork Plugin Ecosystem**: Integration compatibility (not runtime dependency)

### Phase Dependencies

- **Phase 1**: Standalone plugin skeleton
- **Phase 2**: Business agents, VALID framework full implementation
- **Phase 3**: RA/QA domain agents, regulatory knowledge bases
- **Phase 4**: Notion MCP, Google Workspace MCP
- **Phase 5**: Agent memory, advanced analytics

---

## Constraints

### Technical Constraints

- [C1] Plugin structure must comply with Claude Code Plugin Specification v1.0
- [C2] Agent definitions must use YAML frontmatter format
- [C3] Command definitions must support parameter syntax
- [C4] MCP integration must use .mcp.json configuration
- [C5] All user-facing output must be Korean (conversation_language: ko)

### Domain Constraints

- [C6] Regulatory claims must cite sources (standard, section, version)
- [C7] Error messages must use plain language without technical jargon
- [C8] User questions must present maximum 4 options

### Resource Constraints

- [C9] Total token budget: 200K per session (Brief 120K (60%) + Execute 60K (30%) + Deliver 20K (10%))
- [C10] Orchestrator agent timeout: 300 seconds
- [C11] Maximum automatic retries: 3

---

## Risks and Mitigation

### Technical Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Claude Code Plugin API changes | Medium | High | Follow official plugin documentation, version pinning |
| MCP server unavailability | Low | Medium | Retry logic, graceful degradation, cached responses |
| Token budget exceeded | Medium | Medium | Progressive disclosure, aggressive /clear strategy |

### Domain Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Regulatory information outdated | Low | High | Context7 MCP for current docs, date validation |
| User misinterpretation | Medium | Medium | Clear language, approval checkpoints, examples |
| Complex queries beyond Phase 1 | High | Low | Sequential Thinking MCP, graceful fallback |

### User Experience Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Language confusion (Ko/En) | Low | Medium | Strict separation: user=Ko, agent=En |
| Too many questions | Medium | Low | Max 5 questions in Brief, max 4 options |
| Unclear error messages | Low | High | Plain language policy, next-step guidance |

---

## Success Criteria

### Functional Requirements

- [FR1] Plugin structure is recognized by Claude Code
- [FR2] `/aria help` command displays usage information
- [FR3] Orchestrator classifies user intent (document drafting, analysis, review, search)
- [FR4] Basic user interaction with AskUserQuestion (max 4 options)
- [FR5] Error messages in plain Korean with next-step guidance
- [FR6] `.mcp.json` configured with Context7 and Sequential Thinking MCP

### Quality Requirements

- [QR1] All user-facing output is Korean
- [QR2] All error messages use plain language
- [QR3] Regulatory claims cite sources (when applicable)
- [QR4] Questions present maximum 4 options

### Integration Requirements

- [IR1] Context7 MCP can be accessed for regulatory research
- [IR2] Sequential Thinking MCP can be used for complex analysis
- [IR3] Plugin loads without errors in Claude Code

### Documentation Requirements

- [DR1] README.md describes ARIA capabilities
- [DR2] CLAUDE.md contains execution directives
- [DR3] CHANGELOG.md records Phase 1 changes

---

## References

### Internal References

- [ARCHITECTURE-REDESIGN.md](../docs/specs/ARCHITECTURE-REDESIGN.md): Complete system architecture
- [CONTEXT.md](../docs/CONTEXT.md): Project background and design decisions
- [CLAUDE.md](../CLAUDE.md): ARIA execution directives

### External References

- [Claude Code Plugin Documentation](https://claude.ai/claude-code/docs)
- [MoAI-ADK](https://github.com/henry-1981/Agent-RA): Architectural principles reference
- [Context7 MCP](https://context7.io): Regulatory documentation lookup
- [Sequential Thinking MCP](https://modelcontextprotocol.io): Complex analysis support

### Regulatory References

- FDA 21 CFR Part 820: Quality System Regulation
- EU MDR 2017/745: Medical Device Regulation
- ISO 13485: Medical device quality management systems
- ISO 14971: Medical device risk management
