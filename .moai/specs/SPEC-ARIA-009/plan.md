---
id: PLAN-ARIA-009
spec: SPEC-ARIA-009
version: 1.0.0
status: Draft
created: 2026-02-10
---

# PLAN-ARIA-009: MCP 서버 및 Config 파일 ARIA 잔여물 정리

## Implementation Plan

### Phase 1: MCP 서버 정리 (핵심)

**Task 1.1: .mcp.json 수정**
- notion 서버 블록 제거
- google-workspace 서버 블록 제거
- context7 description 범용화: "Library documentation lookup via Context7"
- sequential-thinking description 범용화: "Complex problem analysis with sequential reasoning"

**Task 1.2: .claude/settings.local.json 수정**
- enabledMcpjsonServers에서 "google-workspace", "notion" 제거

### Phase 2: ARIA 플러그인 제거

**Task 2.1: .claude-plugin/ 디렉토리 삭제**
- plugin.json 삭제
- capabilities.yaml 삭제
- 디렉토리 자체 삭제

### Phase 3: Config 파일 범용화

**Task 3.1: output.yaml 수정**
- 헤더 주석 범용화
- regulatory_submission 섹션 제거
- regulatory 테마/템플릿 참조 범용화

**Task 3.2: analytics.yaml 수정**
- 헤더 주석 범용화
- regulatory_monitoring 섹션 제거
- notion/google_workspace MCP 설정 제거
- knowledge_base aria 경로 참조 제거

**Task 3.3: multilingual-triggers.yaml 수정**
- mcp-notion 섹션 제거

### Phase 4: 검증

**Task 4.1: 잔여물 검색**
- grep으로 "aria|ARIA|notion|google.workspace|regulatory" 패턴 검색
- 변경된 파일에서 잔여 참조 없음 확인

## Risk Assessment

| 위험 | 영향 | 완화 전략 |
|------|------|----------|
| config 파일 구조 파손 | 중간 | YAML 유효성 검사 후 커밋 |
| MCP 서버 연결 실패 | 낮음 | context7, sequential-thinking만 유지 확인 |
| 설정 누락 | 낮음 | 변경 전후 diff 비교 |

## Dependencies

- SPEC-ARIA-008 완료 (선행 조건 충족됨)
- moai-dev worktree에서 작업 (main 브랜치 미영향)
