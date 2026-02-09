---
id: ACCEPT-ARIA-009
spec: SPEC-ARIA-009
version: 1.0.0
status: Draft
created: 2026-02-10
---

# ACCEPT-ARIA-009: 인수 조건

## Acceptance Criteria

### AC-001: MCP 서버 정리
- [ ] .mcp.json에 "notion" 서버 블록이 없다
- [ ] .mcp.json에 "google-workspace" 서버 블록이 없다
- [ ] .mcp.json의 context7 description에 "regulatory" 단어가 없다
- [ ] .mcp.json의 sequential-thinking description에 "regulatory" 단어가 없다
- [ ] .mcp.json이 유효한 JSON이다

### AC-002: settings.local.json 정리
- [ ] enabledMcpjsonServers에 "notion"이 없다
- [ ] enabledMcpjsonServers에 "google-workspace"가 없다
- [ ] enabledMcpjsonServers에 "context7"과 "sequential-thinking"이 존재한다

### AC-003: ARIA 플러그인 제거
- [ ] .claude-plugin/ 디렉토리가 존재하지 않는다

### AC-004: Config 파일 범용화
- [ ] output.yaml에 "ARIA" 문자열이 없다
- [ ] output.yaml에 "regulatory_submission" 섹션이 없다
- [ ] analytics.yaml에 "ARIA" 문자열이 없다
- [ ] analytics.yaml에 "regulatory_monitoring" 섹션이 없다
- [ ] analytics.yaml에 notion/google_workspace MCP 설정이 없다
- [ ] multilingual-triggers.yaml에 "mcp-notion" 섹션이 없다
- [ ] 모든 YAML 파일이 유효한 YAML이다

### AC-005: 잔여물 부재 검증
- [ ] 변경 대상 파일에서 grep "aria|ARIA" 검색 결과가 0건이다 (accessibility의 aria-labels 등 표준 HTML 속성은 예외)
- [ ] 변경 대상 파일에서 grep "notion" 검색 결과가 0건이다
- [ ] 변경 대상 파일에서 grep "google.workspace" 검색 결과가 0건이다
