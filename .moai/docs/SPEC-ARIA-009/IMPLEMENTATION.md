# SPEC-ARIA-009: 구현 진행 상황

**SPEC ID**: SPEC-ARIA-009
**Title**: MCP 서버 및 Config 파일 ARIA 잔여물 정리
**Status**: In Progress
**Created**: 2026-02-10
**Updated**: 2026-02-10

---

## 개요

SPEC-ARIA-008에서 ARIA 에이전트, 스킬, 커맨드, 훅 등의 파일이 제거되었으나, MCP 서버 설정과 Config 파일에 ARIA 개발 잔여물이 남아있습니다. 본 SPEC은 이러한 잔여물을 정리하여 순수한 MoAI-ADK 환경을 완성하는 것을 목표합니다.

---

## 구현 대상 파일 목록

| 파일 | 작업 유형 | 상세 | 상태 |
|------|---------|------|------|
| `.mcp.json` | 수정 | notion, google-workspace 제거; context7, sequential-thinking description 범용화 | 대기 |
| `.claude/settings.local.json` | 수정 | enabledMcpjsonServers에서 notion, google-workspace 제거 | 대기 |
| `.claude-plugin/plugin.json` | 삭제 | ARIA 플러그인 정의 전체 제거 | 대기 |
| `.claude-plugin/capabilities.yaml` | 삭제 | ARIA 기능 정의 전체 제거 | 대기 |
| `.moai/config/sections/output.yaml` | 수정 | ARIA regulatory 참조 제거, MoAI-ADK 범용화 | 대기 |
| `.moai/config/sections/analytics.yaml` | 수정 | ARIA analytics 참조 제거, MoAI-ADK 범용화 | 대기 |
| `.moai/config/multilingual-triggers.yaml` | 수정 | mcp-notion 섹션 제거 | 대기 |

---

## 구현 상세

### 1. MCP 서버 정리 (`.mcp.json`)

**변경 사항:**
- `notion` 서버 블록 전체 제거
- `google-workspace` 서버 블록 전체 제거
- `context7` description 수정: "Library documentation lookup via Context7"
- `sequential-thinking` description 수정: "Complex problem analysis with sequential reasoning"

**검증:**
- JSON 유효성 확인
- 제거된 서버에 대한 참조가 없는지 확인

---

### 2. Settings 파일 정리 (`.claude/settings.local.json`)

**변경 사항:**
- `enabledMcpjsonServers` 배열에서 `notion` 제거
- `enabledMcpjsonServers` 배열에서 `google-workspace` 제거
- 결과: `["context7", "sequential-thinking"]` 유지

**검증:**
- JSON 유효성 확인
- 필수 MCP 서버 포함 확인

---

### 3. ARIA 플러그인 디렉토리 제거 (`.claude-plugin/`)

**변경 사항:**
- `.claude-plugin/` 디렉토리 전체 삭제
  - `plugin.json` 제거
  - `capabilities.yaml` 제거
  - 기타 ARIA 플러그인 관련 파일 제거

**검증:**
- 디렉토리 존재 여부 확인
- 삭제 후 참조 부재 확인

---

### 4. Config 파일 범용화

#### 4.1 `.moai/config/sections/output.yaml`

**변경 사항:**
- 파일 헤더 주석: "ARIA Regulatory Intelligence Assistant" → "MoAI-ADK Output Configuration"
- `regulatory_submission` 섹션 제거
- `regulatory-standard` CSS 테마 참조 범용화
- `regulatory-template.dotx` 워드 템플릿 참조 범용화

**검증:**
- YAML 유효성 확인
- "ARIA", "regulatory" 문자열 부재 확인 (표준 용어 제외)

---

#### 4.2 `.moai/config/sections/analytics.yaml`

**변경 사항:**
- 파일 헤더 주석: "ARIA Advanced Analytics Features" → "MoAI-ADK Analytics Configuration"
- `regulatory_monitoring` 섹션 제거
- `knowledge_base.path` aria 경로 참조 제거
- Notion 관련 설정 블록 제거
- Google Workspace 관련 설정 블록 제거
- `notion_query` 타이밍 설정 제거

**검증:**
- YAML 유효성 확인
- "ARIA", "notion", "google_workspace" 문자열 부재 확인

---

#### 4.3 `.moai/config/multilingual-triggers.yaml`

**변경 사항:**
- `mcp-notion` 섹션 전체 제거

**검증:**
- YAML 유효성 확인
- "mcp-notion" 참조 부재 확인

---

## 구현 우선순위

| 순서 | 작업 | 위험도 | 근거 | 예상 소요시간 |
|------|------|--------|------|--------------|
| 1 | .mcp.json MCP 서버 정리 | 낮음 | 핵심 잔여물, 즉시 효과 | 5분 |
| 2 | .claude/settings.local.json 업데이트 | 낮음 | MCP 서버 참조 동기화 | 3분 |
| 3 | .claude-plugin/ 디렉토리 삭제 | 낮음 | ARIA 플러그인 제거 | 2분 |
| 4 | Config 파일 범용화 (output, analytics, triggers) | 낮음 | 설정 정리 | 10분 |

**예상 총 소요시간**: 약 20분

---

## 테스트 계획

### 단위 테스트

1. **MCP 서버 검증**
   ```bash
   # JSON 유효성 확인
   python -m json.tool .mcp.json > /dev/null && echo "Valid JSON"

   # 제거된 서버 부재 확인
   grep -c "notion" .mcp.json  # 결과: 0
   grep -c "google-workspace" .mcp.json  # 결과: 0
   ```

2. **Settings 파일 검증**
   ```bash
   # JSON 유효성 확인
   python -m json.tool .claude/settings.local.json > /dev/null

   # 필수 MCP 서버 확인
   grep "context7\|sequential-thinking" .claude/settings.local.json
   ```

3. **Config 파일 검증**
   ```bash
   # YAML 유효성 확인
   python -c "import yaml; yaml.safe_load(open('.moai/config/sections/output.yaml'))"
   python -c "import yaml; yaml.safe_load(open('.moai/config/sections/analytics.yaml'))"
   python -c "import yaml; yaml.safe_load(open('.moai/config/multilingual-triggers.yaml'))"

   # ARIA 참조 부재 확인
   grep -i "aria\|regulatory\|notion\|google.workspace" .moai/config/sections/*.yaml
   ```

---

## 위험 분석 및 완화 전략

| 위험 | 영향 | 확률 | 완화 전략 |
|------|------|------|----------|
| 필수 설정 오류 | MoAI-ADK 기능 손상 | 낮음 | YAML/JSON 유효성 검증 |
| 불완전한 제거 | ARIA 참조 남음 | 낮음 | Grep 검색으로 완전성 확인 |
| 버전 컨트롤 충돌 | 머지 어려움 | 낮음 | 깔끔한 커밋, 명확한 메시지 |

---

## 의존성

- **선행 SPEC**: SPEC-ARIA-008 (ARIA 파일 제거 완료)
- **선행 작업**: moai-dev worktree 준비 완료
- **도구 요구사항**: Python (YAML/JSON 검증)

---

## 완료 기준

1. 모든 변경 대상 파일이 수정/삭제됨
2. YAML/JSON 유효성 검증 통과
3. ARIA 관련 문자열이 모두 제거됨 (표준 속성 제외)
4. 깃 커밋이 생성되고 PR이 작성됨
5. EARS 요구사항 검증 체크리스트 완료

---

## 예상 결과

구현 완료 후 다음 상태를 기대합니다:

- `.mcp.json`: context7 + sequential-thinking만 유지, 범용 description
- `.claude/settings.local.json`: context7 + sequential-thinking만 활성화
- `.claude-plugin/`: 디렉토리 삭제 완료
- `.moai/config/sections/*.yaml`: ARIA 참조 완전 제거
- 프로젝트: 순수한 MoAI-ADK 환경 완성

---

## 참고

- **SPEC 문서**: `.moai/specs/SPEC-ARIA-009/spec.md`
- **인수 조건**: `.moai/specs/SPEC-ARIA-009/acceptance.md`
- **구현 계획**: `.moai/specs/SPEC-ARIA-009/plan.md`
