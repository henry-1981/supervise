---
id: SPEC-ARIA-009
version: 1.0.0
status: Draft
created: 2026-02-10
updated: 2026-02-10
author: MoAI Team
priority: Medium
domain: configuration-cleanup
related-specs: SPEC-ARIA-008
tags: cleanup, mcp, config, aria-removal
---

# SPEC-ARIA-009: MCP 서버 및 Config 파일 ARIA 잔여물 정리

## HISTORY

| 버전 | 날짜 | 변경사항 | 작성자 |
|------|------|----------|--------|
| 1.0.0 | 2026-02-10 | 초기 SPEC 작성 - SPEC-ARIA-008 후속 정리 | MoAI Team |

---

## Environment

### 현재 상황

SPEC-ARIA-008에서 moai-dev worktree의 ARIA 파일(에이전트, 스킬, 커맨드, 훅 등)은 제거되었으나, MCP 서버 설정과 config 파일에 ARIA 개발 잔여물이 여전히 존재한다.

**잔여물 위치 및 현황:**

1. **`.mcp.json`** - ARIA 전용 MCP 서버 2개 존재:
   - `google-workspace`: ARIA Phase 4용 Google Workspace 통합 (사용하지 않음)
   - `notion`: ARIA regulatory management용 Notion 통합 (사용하지 않음)
   - `context7` description: "Up-to-date regulatory documentation lookup" (ARIA 전용 표현)
   - `sequential-thinking` description: "Complex regulatory pathway analysis" (ARIA 전용 표현)

2. **`.claude/settings.local.json`** - 비활성화 필요한 MCP 서버 참조:
   - `enabledMcpjsonServers`에 `google-workspace`, `notion` 포함

3. **`.claude-plugin/`** - ARIA 플러그인 전체 디렉토리:
   - `plugin.json`: ARIA 플러그인 정의 (name: "aria")
   - `capabilities.yaml`: ARIA 기능 정의 (notion, google_workspace 참조 포함)

4. **`.moai/config/sections/output.yaml`** - ARIA regulatory 전용 출력 설정:
   - 문서 헤더: "ARIA Regulatory Intelligence Assistant"
   - regulatory_submission 섹션 (FDA eCopy 등)
   - regulatory 테마 및 템플릿 참조

5. **`.moai/config/sections/analytics.yaml`** - ARIA analytics 설정:
   - 문서 헤더: "ARIA Advanced Analytics Features Configuration"
   - regulatory_monitoring 섹션
   - notion/google_workspace MCP 설정
   - knowledge_base aria 경로 참조

6. **`.moai/config/multilingual-triggers.yaml`** - Notion MCP 트리거:
   - `mcp-notion` 섹션 (Notion 트리거 키워드)

### 목표 상태

moai-dev worktree에서 ARIA와 무관한 순수 MoAI-ADK 환경을 완성한다:
- MCP 서버: context7 + sequential-thinking + pencil만 유지 (범용 description)
- config 파일: MoAI-ADK 범용 설정으로 업데이트
- ARIA 플러그인 디렉토리 제거

---

## Assumptions

- [A1] moai-dev worktree에서만 작업한다 (main 브랜치 영향 없음)
- [A2] context7과 sequential-thinking MCP 서버는 유지하되 description만 범용화한다
- [A3] .claude-plugin/ 디렉토리의 ARIA 플러그인은 moai-dev에서 불필요하다
- [A4] output.yaml과 analytics.yaml은 MoAI-ADK 범용 설정으로 대체한다
- [A5] notion, google-workspace MCP 서버는 moai-dev에서 완전히 제거한다

---

## Requirements

### EARS-001 (Ubiquitous)
시스템은 항상 .mcp.json에서 ARIA 전용 MCP 서버(notion, google-workspace)를 포함하지 않아야 한다.

### EARS-002 (Ubiquitous)
시스템은 항상 .claude/settings.local.json의 enabledMcpjsonServers에서 ARIA 전용 서버 참조를 포함하지 않아야 한다.

### EARS-003 (Ubiquitous)
시스템은 항상 MCP 서버 description을 MoAI-ADK 범용 표현으로 유지해야 한다.

### EARS-004 (Event-Driven)
WHEN ARIA 플러그인 디렉토리(.claude-plugin/)가 존재할 때, 시스템은 해당 디렉토리를 제거해야 한다.

### EARS-005 (Event-Driven)
WHEN config 파일에 ARIA 전용 설정이 존재할 때, 시스템은 MoAI-ADK 범용 설정으로 대체해야 한다.

### EARS-006 (Ubiquitous)
시스템은 항상 multilingual-triggers.yaml에서 ARIA 전용 MCP 트리거(mcp-notion)를 포함하지 않아야 한다.

---

## Specifications

### 변경 대상 파일 목록

| 파일 | 작업 | 상세 |
|------|------|------|
| `.mcp.json` | 수정 | notion, google-workspace 서버 제거; context7, sequential-thinking description 범용화 |
| `.claude/settings.local.json` | 수정 | enabledMcpjsonServers에서 notion, google-workspace 제거 |
| `.claude-plugin/plugin.json` | 삭제 | ARIA 플러그인 정의 전체 |
| `.claude-plugin/capabilities.yaml` | 삭제 | ARIA 기능 정의 전체 |
| `.moai/config/sections/output.yaml` | 수정 | ARIA regulatory 참조 제거, MoAI-ADK 범용화 |
| `.moai/config/sections/analytics.yaml` | 수정 | ARIA analytics 참조 제거, MoAI-ADK 범용화 |
| `.moai/config/multilingual-triggers.yaml` | 수정 | mcp-notion 섹션 제거 |

### 변경 상세

**1. `.mcp.json` 변경:**
- 제거: `google-workspace` 서버 블록 전체
- 제거: `notion` 서버 블록 전체
- 수정: `context7.description` -> "Library documentation lookup via Context7"
- 수정: `sequential-thinking.description` -> "Complex problem analysis with sequential reasoning"

**2. `.claude/settings.local.json` 변경:**
- `enabledMcpjsonServers`에서 `google-workspace`, `notion` 항목 제거
- 결과: `["context7", "sequential-thinking"]`

**3. `.claude-plugin/` 디렉토리 삭제:**
- `plugin.json`, `capabilities.yaml` 포함 전체 디렉토리 삭제

**4. `.moai/config/sections/output.yaml` 변경:**
- 헤더 주석: "ARIA Regulatory Intelligence Assistant" -> "MoAI-ADK Output Configuration"
- `regulatory_submission` 섹션 제거
- `regulatory-standard` CSS 테마 참조를 범용 표현으로 변경
- `regulatory-template.dotx` 워드 템플릿 참조를 범용 표현으로 변경

**5. `.moai/config/sections/analytics.yaml` 변경:**
- 헤더 주석: "ARIA Advanced Analytics Features" -> "MoAI-ADK Analytics Configuration"
- `regulatory_monitoring` 섹션 제거
- `knowledge_base.path`: aria 경로 참조 제거
- `notion` 관련 설정 블록 제거
- `google_workspace` 관련 설정 블록 제거
- `notion_query` 타이밍 설정 제거

**6. `.moai/config/multilingual-triggers.yaml` 변경:**
- `mcp-notion` 섹션 전체 제거

### 구현 우선순위

| 순서 | 작업 | 위험도 | 근거 |
|------|------|--------|------|
| 1 | .mcp.json MCP 서버 정리 | 낮음 | 핵심 잔여물, 즉시 효과 |
| 2 | .claude/settings.local.json 업데이트 | 낮음 | MCP 서버 참조 동기화 |
| 3 | .claude-plugin/ 디렉토리 삭제 | 낮음 | ARIA 플러그인 제거 |
| 4 | config 파일 범용화 (output, analytics, triggers) | 낮음 | 설정 정리 |

---

## Traceability

| 요구사항 | 파일 | 검증 방법 |
|----------|------|----------|
| EARS-001 | .mcp.json | notion, google-workspace 키 부재 확인 |
| EARS-002 | .claude/settings.local.json | enabledMcpjsonServers에 notion, google-workspace 부재 확인 |
| EARS-003 | .mcp.json | description에 "regulatory" 문자열 부재 확인 |
| EARS-004 | .claude-plugin/ | 디렉토리 부재 확인 |
| EARS-005 | .moai/config/sections/*.yaml | "aria", "ARIA", "regulatory" 문자열 부재 확인 |
| EARS-006 | multilingual-triggers.yaml | mcp-notion 섹션 부재 확인 |

---

## TAG References

- **SPEC-ARIA-009** 현재 문서
- **PLAN-ARIA-009** 구현 계획 (plan.md)
- **ACCEPT-ARIA-009** 인수 조건 (acceptance.md)
- **SPEC-ARIA-008** 선행 SPEC (환경 분리 및 ARIA 파일 제거)
