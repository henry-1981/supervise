# ARIA Agent Template for aria-backend-dev

## YAML Frontmatter Pattern Analysis

Based on ARIA agent patterns, here is the standard pattern:

```yaml
---
name: expert-regulatory
description: |
  RA/QA Regulatory 전문가 에이전트. FDA 510(k)/PMA 경로 분석,
  복수국 시장 요구사항 매트릭스, 규정 변경 영향도 분석 제공.
  MUST INVOKE when ANY of these keywords appear in user request:
  EN: regulatory, FDA, 510(k), PMA, MDR, CE marking, submission, market approval
  KO: 규제, 인허가, 식약처, MFDS, 허가, 제출, 시장 진입
tools: Read, Write, Edit, Grep, Glob, Bash, WebFetch, WebSearch, mcp__context7__resolve-library-id, mcp__context7__get-library-docs, mcp__sequential-thinking__sequentialthinking
model: opus
permissionMode: default
memory: project
skills:
  - aria-domain-raqa
  - aria-knowledge-fda
  - aria-knowledge-eumdr
mcpServers:
  - context7
  - sequential-thinking
hooks:
  PreToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: "\"$CLAUDE_PROJECT_DIR/aria hooks\" aria-validation"
          timeout: 5
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: "\"$CLAUDE_PROJECT_DIR/aria hooks\" aria-verification"
          timeout: 15
---
```

## Required Fields

| Field | Value Format | Description |
|-------|-------------|-------------|
| name | kebab-case | Expert identifier (e.g., expert-regulatory) |
| description | YAML folded scalar (\>) | Multiline description with keywords |
| tools | Space-delimited string | Available tools for this agent |
| model | opus/sonnet/inherit | Claude model assignment |
| permissionMode | default/acceptEdits/plan | Permission behavior |
| memory | user/project/local | Persistent memory scope |
| skills | YAML array | Skills to preload |
| mcpServers | YAML array | MCP server configurations |

## Model Assignment Guide (SPEC-ARIA-003)

| Agent | Model | Complexity | Rationale |
|-------|-------|------------|-----------|
| expert-regulatory | opus | High | Multi-market strategy, complex pathway analysis |
| expert-standards | opus | High | Conflict resolution, hierarchy interpretation |
| expert-risk | opus | High | Risk-benefit analysis, complex mitigation |
| expert-clinical | opus | High | Clinical evaluation, equivalence analysis |
| expert-design-control | sonnet | Medium | Process management, documentation |
| expert-capa | sonnet | Medium | Lifecycle management, root cause |
| expert-submission | sonnet | Medium | Template-based, structured |
| expert-audit | sonnet | Medium | Checklist-based, preparation |

## Tool Permissions by Category

### Foundation Tools (Always Required)
- Read, Write, Edit - File operations
- Grep, Glob - Search and discovery
- Bash - Shell command execution

### MCP Tools (ARIA-Specific)
- mcp__context7__resolve-library-id - Regulation lookup
- mcp__context7__get-library-docs - Standard documentation
- mcp__sequential-thinking__sequentialthinking - Complex analysis

### Optional Tools
- WebFetch - Manual documentation access
- WebSearch - Research fallback
- AskUserQuestion - User interaction (MoAI only)

## Progressive Disclosure Pattern for Skills

Based on `.claude/skills/ (generic)SKILL.md`:

### Level 1: Metadata (~100 tokens)
```yaml
---
name: aria-domain-raqa
description: >
  RA/QA 도메인 전문 지식 스킬. 규제 프레임워크, 표준 해석,
  위험관리 원칙 제공.
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
  tags: "raqa, regulatory, quality, medical-device"
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000
triggers:
  keywords: ["regulatory", "standard", "risk", "capa", "audit"]
  agents: ["expert-regulatory", "expert-standards", "expert-risk"]
  phases: ["plan", "run"]
---
```

### Level 2: Body (~5000 tokens)
- RA/QA domain overview
- Common regulatory frameworks
- Risk management principles
- Quick reference guides

### Level 3: Bundled (on-demand)
- modules/regulatory-overview.md
- modules/standards-overview.md
- modules/risk-overview.md
- examples/regulatory-strategy-example.md

## Agent File Structure Template

```markdown
---
[YAML frontmatter as above]
---

# [Agent Display Name]

## Primary Mission

[Single-sentence mission statement]

Version: 1.0.0
Last Updated: 2026-02-09

## Orchestration Metadata

can_resume: false
typical_chain_position: middle
depends_on: ["manager-spec"]
spawns_subagents: false
token_budget: high
context_retention: high
output_format: [Output format description]

---

## Agent Persona

Job: [Professional job title]
Area of Expertise: [Specialization area]
Goal: [Primary objective]

## Core Capabilities

[Domain-specific capabilities list]

## Scope Boundaries

IN SCOPE:
- [Tasks within scope]

OUT OF SCOPE:
- [Tasks outside scope - delegate to other agents]

## VALID Framework Compliance

### Verified (규정 원문 인용)
- 모든 규제 주장에 [Standard] Section [Number] 형식 인용
- Context7 MCP로 규정 원문 대조 검증

### Accurate (데이터 출처 검증)
- 모든 데이터에 출처 인용 (Federal Register, Official Journal, MFDS)
- 날짜/버전 정확성 확인

### Linked (추적성 확보)
- Requirements ↔ Documents ↔ Evidence 양방향 링크
- Notion DB Relations 설정

### Inspectable (감사 추적 완전성)
- 모든 결정에 근거 문서화
- 타임스탬프 기록

### Deliverable (제출 형식 준수)
- eCopy format, PDF/A format 준수
- RTA criteria 충족

## MCP Integration

### Context7 MCP Usage
```yaml
# 규정 검색 시
1. mcp__context7__resolve-library-id(query="FDA 21 CFR 820")
2. mcp__context7__get-library-docs(topics=["design-control", "risk-management"])
```

### Sequential Thinking MCP Usage
```yaml
# 복잡한 규제 전략 분석 시
1. Assumption Audit: What are we assuming about market requirements?
2. First Principles: What is the core regulatory objective?
3. Alternative Generation: 510(k) vs PMA vs De Novo vs Exempt
4. Trade-off Analysis: Timeline vs Cost vs Success probability
5. Bias Check: Anchoring to familiar pathway?
```

## Workflow Steps

### Step 1: Analyze Request
[Request analysis process]

### Step 2: Load Context
[Context loading process]

### Step 3: Execute Domain Logic
[Domain-specific execution]

### Step 4: Validate Output
[VALID framework validation]

### Step 5: Generate Response
[Response generation in user's conversation_language]

## Success Criteria

[Specific success criteria for this agent]

## Language Handling

[HARD] Receive and respond to prompts in user's conversation_language

Output Language Requirements:
- [HARD] Domain analysis: User's conversation_language
- [HARD] Code examples: Always in English
- [HARD] Regulatory citations: Original language (English)
- [HARD] Commit messages: Always in English

---

Last Updated: 2026-02-09
Version: 1.0.0
Agent Tier: Domain (ARIA Sub-agents)
Context7 Integration: Enabled
```

## Quality Checklist for aria-backend-dev

### Pre-Generation Checklist
- [ ] YAML frontmatter all required fields present
- [ ] name follows kebab-case convention
- [ ] description uses YAML folded scalar (>)
- [ ] model assignment matches SPEC requirements
- [ ] skills array includes correct domain skills
- [ ] mcpServers includes context7 (required for VALID Verified)
- [ ] permissionMode set to default (unless special case)
- [ ] memory set to project (for cross-session learning)

### Post-Generation Checklist
- [ ] File saved in .claude/agents/aria/ directory
- [ ] Filename matches YAML name field (expert-regulatory.md)
- [ ] Markdown formatting consistent throughout
- [ ] All sections from template present
- [ ] VALID framework section complete
- [ ] MCP integration section specific to agent domain
- [ ] Language handling section includes conversation_language rule
- [ ] Version: 1.0.0 and Last Updated: 2026-02-09 present

### Skill-Specific Checklist
- [ ] Progressive Disclosure structure present
- [ ] Level 1 tokens ~100 (metadata only)
- [ ] Level 2 tokens ~5000 (body content)
- [ ] triggers keywords relevant to domain
- [ ] triggers agents include relevant ARIA agents
- [ ] modules/ directory structure planned
- [ ] examples/ directory planned (if applicable)

## Common Patterns to Avoid

### Don't Do This
```yaml
# Wrong: description as plain string
description: "Backend architecture and database specialist"
```

### Do This Instead
```yaml
# Correct: description as YAML folded scalar
description: |
  Backend architecture and database specialist. Use PROACTIVELY for
  API design, authentication, database modeling, and server implementation.
```

### Don't Do This
```yaml
# Wrong: skills as plain string
skills: "aria-domain-raqa aria-knowledge-fda"
```

### Do This Instead
```yaml
# Correct: skills as YAML array
skills:
  - aria-domain-raqa
  - aria-knowledge-fda
  - aria-knowledge-eumdr
```

## Next Steps for aria-backend-dev

1. Create `.claude/agents/aria/expert-regulatory.md` using template
2. Create `.claude/agents/aria/expert-standards.md` using template
3. Create `.claude/agents/aria/expert-risk.md` using template
4. Create `.claude/skills/aria-domain-raqa/SKILL.md` using Progressive Disclosure pattern
5. Create `.claude/skills/aria-knowledge-fda/SKILL.md` using Progressive Disclosure pattern
6. Create `.claude/skills/aria-knowledge-eumdr/SKILL.md` using Progressive Disclosure pattern
7. Create `.claude/skills/aria-knowledge-standards/SKILL.md` using Progressive Disclosure pattern
8. Create `.claude/skills/aria-risk-management/SKILL.md` using Progressive Disclosure pattern
9. Generate module content for each skill
10. Validate all files against quality checklist

---

Template Version: 1.0.0
Created: 2026-02-09
Author: aria-quality (based on MoAI-ADK patterns)
