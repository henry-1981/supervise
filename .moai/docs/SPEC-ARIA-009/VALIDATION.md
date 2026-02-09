# SPEC-ARIA-009: EARS 요구사항 검증

**SPEC ID**: SPEC-ARIA-009
**검증 날짜**: 2026-02-10
**검증자**: MoAI Documentation Manager

---

## 검증 개요

본 문서는 SPEC-ARIA-009의 EARS(Easy Approach to Requirements Syntax) 요구사항이 충족되었는지 검증하는 체크리스트입니다.

---

## EARS 요구사항 매핑

### EARS-001: Ubiquitous Requirement
**요구사항**: 시스템은 항상 .mcp.json에서 ARIA 전용 MCP 서버(notion, google-workspace)를 포함하지 않아야 한다.

| 검증 항목 | 확인 사항 | 상태 | 비고 |
|----------|---------|------|------|
| `.mcp.json` 파싱 | JSON 유효성 | ⏳ 대기 | JSON 형식 확인 |
| `notion` 서버 제거 | "notion" 키 부재 | ⏳ 대기 | grep 검색 |
| `google-workspace` 서버 제거 | "google-workspace" 키 부재 | ⏳ 대기 | grep 검색 |
| 다른 서버 존속 | context7, sequential-thinking 유지 | ⏳ 대기 | 필수 서버 확인 |

**검증 명령어:**
```bash
# JSON 유효성
python -m json.tool .mcp.json > /dev/null && echo "PASS: Valid JSON"

# 제거 확인
[ $(grep -c "notion" .mcp.json) -eq 0 ] && echo "PASS: notion 제거됨"
[ $(grep -c "google-workspace" .mcp.json) -eq 0 ] && echo "PASS: google-workspace 제거됨"

# 유지 확인
[ $(grep -c "context7" .mcp.json) -gt 0 ] && echo "PASS: context7 유지됨"
[ $(grep -c "sequential-thinking" .mcp.json) -gt 0 ] && echo "PASS: sequential-thinking 유지됨"
```

**상태**: ⏳ 대기

---

### EARS-002: Ubiquitous Requirement
**요구사항**: 시스템은 항상 .claude/settings.local.json의 enabledMcpjsonServers에서 ARIA 전용 서버 참조를 포함하지 않아야 한다.

| 검증 항목 | 확인 사항 | 상태 | 비고 |
|----------|---------|------|------|
| `.claude/settings.local.json` 파싱 | JSON 유효성 | ⏳ 대기 | JSON 형식 확인 |
| `notion` 참조 제거 | enabledMcpjsonServers에서 부재 | ⏳ 대기 | 배열 검사 |
| `google-workspace` 참조 제거 | enabledMcpjsonServers에서 부재 | ⏳ 대기 | 배열 검사 |
| 필수 서버 참조 유지 | context7, sequential-thinking 포함 | ⏳ 대기 | 배열 포함 확인 |

**검증 명령어:**
```bash
# JSON 유효성
python -m json.tool .claude/settings.local.json > /dev/null && echo "PASS: Valid JSON"

# enabledMcpjsonServers 검증
python -c "
import json
with open('.claude/settings.local.json') as f:
    config = json.load(f)
    enabled = config.get('enabledMcpjsonServers', [])
    assert 'notion' not in enabled, 'notion 제거 필요'
    assert 'google-workspace' not in enabled, 'google-workspace 제거 필요'
    assert 'context7' in enabled, 'context7 필수'
    assert 'sequential-thinking' in enabled, 'sequential-thinking 필수'
    print('PASS: enabledMcpjsonServers 검증 완료')
"
```

**상태**: ⏳ 대기

---

### EARS-003: Ubiquitous Requirement
**요구사항**: 시스템은 항상 MCP 서버 description을 MoAI-ADK 범용 표현으로 유지해야 한다.

| 검증 항목 | 확인 사항 | 상태 | 비고 |
|----------|---------|------|------|
| `context7` description | "regulatory" 문자열 부재 | ⏳ 대기 | 범용 표현 확인 |
| `sequential-thinking` description | "regulatory" 문자열 부재 | ⏳ 대기 | 범용 표현 확인 |
| Description 예시 | "Library documentation lookup" | ⏳ 대기 | 권장 표현 |
| Description 예시 | "Complex problem analysis" | ⏳ 대기 | 권장 표현 |

**검증 명령어:**
```bash
# context7 description 확인
python -c "
import json
with open('.mcp.json') as f:
    config = json.load(f)
    c7_desc = config.get('mcpServers', {}).get('context7', {}).get('description', '')
    assert 'regulatory' not in c7_desc.lower(), 'regulatory 문자열 제거 필요'
    print('PASS: context7 description 검증 완료')
"

# sequential-thinking description 확인
python -c "
import json
with open('.mcp.json') as f:
    config = json.load(f)
    st_desc = config.get('mcpServers', {}).get('sequential-thinking', {}).get('description', '')
    assert 'regulatory' not in st_desc.lower(), 'regulatory 문자열 제거 필요'
    print('PASS: sequential-thinking description 검증 완료')
"
```

**상태**: ⏳ 대기

---

### EARS-004: Event-Driven Requirement
**요구사항**: WHEN ARIA 플러그인 디렉토리(.claude-plugin/)가 존재할 때, 시스템은 해당 디렉토리를 제거해야 한다.

| 검증 항목 | 확인 사항 | 상태 | 비고 |
|----------|---------|------|------|
| `.claude-plugin/` 디렉토리 존재 | 파일 시스템 상태 | ⏳ 대기 | 디렉토리 부재 확인 |
| `plugin.json` 제거 | 파일 부재 | ⏳ 대기 | 삭제 확인 |
| `capabilities.yaml` 제거 | 파일 부재 | ⏳ 대기 | 삭제 확인 |
| ARIA 플러그인 참조 | 프로젝트 내 부재 | ⏳ 대기 | Grep 검색 |

**검증 명령어:**
```bash
# 디렉토리 부재 확인
[ ! -d ".claude-plugin" ] && echo "PASS: .claude-plugin 디렉토리 제거됨"

# 플러그인 참조 검색
grep -r "\.claude-plugin\|aria.*plugin" . --exclude-dir=.git 2>/dev/null | wc -l
# 결과가 0이어야 함 (PASS)
```

**상태**: ⏳ 대기

---

### EARS-005: Event-Driven Requirement
**요구사항**: WHEN config 파일에 ARIA 전용 설정이 존재할 때, 시스템은 MoAI-ADK 범용 설정으로 대체해야 한다.

| 검증 항목 | 확인 사항 | 상태 | 비고 |
|----------|---------|------|------|
| `output.yaml` 정리 | "ARIA" 문자열 부재 | ⏳ 대기 | 헤더 주석 확인 |
| `output.yaml` 정리 | "regulatory_submission" 섹션 부재 | ⏳ 대기 | 섹션 삭제 확인 |
| `analytics.yaml` 정리 | "ARIA" 문자열 부재 | ⏳ 대기 | 헤더 주석 확인 |
| `analytics.yaml` 정리 | "regulatory_monitoring" 섹션 부재 | ⏳ 대기 | 섹션 삭제 확인 |
| `analytics.yaml` 정리 | Notion/Google 설정 부재 | ⏳ 대기 | MCP 설정 삭제 확인 |
| YAML 유효성 | 모든 config 파일 | ⏳ 대기 | YAML 파싱 확인 |

**검증 명령어:**
```bash
# output.yaml 검증
python -c "
import yaml
with open('.moai/config/sections/output.yaml') as f:
    content = f.read()
    assert 'ARIA' not in content, 'ARIA 문자열 제거 필요'
    assert 'regulatory_submission' not in content, 'regulatory_submission 섹션 제거 필요'
    yaml.safe_load(content)  # 유효성 확인
    print('PASS: output.yaml 검증 완료')
"

# analytics.yaml 검증
python -c "
import yaml
with open('.moai/config/sections/analytics.yaml') as f:
    content = f.read()
    assert 'ARIA' not in content, 'ARIA 문자열 제거 필요'
    assert 'regulatory_monitoring' not in content, 'regulatory_monitoring 섹션 제거 필요'
    assert 'notion' not in content.lower(), 'notion 참조 제거 필요'
    assert 'google_workspace' not in content.lower(), 'google_workspace 참조 제거 필요'
    yaml.safe_load(content)  # 유효성 확인
    print('PASS: analytics.yaml 검증 완료')
"
```

**상태**: ⏳ 대기

---

### EARS-006: Ubiquitous Requirement
**요구사항**: 시스템은 항상 multilingual-triggers.yaml에서 ARIA 전용 MCP 트리거(mcp-notion)를 포함하지 않아야 한다.

| 검증 항목 | 확인 사항 | 상태 | 비고 |
|----------|---------|------|------|
| `multilingual-triggers.yaml` 파싱 | YAML 유효성 | ⏳ 대기 | YAML 형식 확인 |
| `mcp-notion` 섹션 제거 | 섹션 부재 | ⏳ 대기 | Grep 검색 |
| 다른 MCP 트리거 유지 | context7, sequential-thinking 유지 | ⏳ 대기 | 필수 트리거 확인 |

**검증 명령어:**
```bash
# multilingual-triggers.yaml 검증
python -c "
import yaml
with open('.moai/config/multilingual-triggers.yaml') as f:
    content = f.read()
    assert 'mcp-notion' not in content, 'mcp-notion 섹션 제거 필요'
    yaml.safe_load(content)  # 유효성 확인
    print('PASS: multilingual-triggers.yaml 검증 완료')
"
```

**상태**: ⏳ 대기

---

## 전체 검증 체크리스트

### 필수 검증 항목

- [ ] EARS-001: notion, google-workspace 제거, 필수 서버 유지
- [ ] EARS-002: enabledMcpjsonServers 정리
- [ ] EARS-003: MCP description 범용화
- [ ] EARS-004: .claude-plugin 디렉토리 삭제
- [ ] EARS-005: Config 파일 범용화 (output, analytics)
- [ ] EARS-006: multilingual-triggers 정리

### 추가 검증 항목

- [ ] 모든 JSON 파일이 유효한 JSON 형식
- [ ] 모든 YAML 파일이 유효한 YAML 형식
- [ ] "aria", "ARIA" 문자열 완전 제거 (표준 속성 제외)
- [ ] "notion", "google-workspace" 참조 완전 제거
- [ ] "regulatory" 도메인 표현 완전 제거
- [ ] 깃 커밋 메시지가 명확함
- [ ] PR 설명이 완전함

---

## 검증 결과

### 최종 상태

| 요구사항 | 상태 | 검증일시 | 검증자 |
|----------|------|---------|--------|
| EARS-001 | ⏳ 대기 | - | - |
| EARS-002 | ⏳ 대기 | - | - |
| EARS-003 | ⏳ 대기 | - | - |
| EARS-004 | ⏳ 대기 | - | - |
| EARS-005 | ⏳ 대기 | - | - |
| EARS-006 | ⏳ 대기 | - | - |

### 종합 평가

**전체 검증 상태**: ⏳ 대기

모든 EARS 요구사항의 구현 후 검증이 필요합니다.

---

## 참고 자료

- **SPEC 문서**: `.moai/specs/SPEC-ARIA-009/spec.md`
- **인수 조건**: `.moai/specs/SPEC-ARIA-009/acceptance.md`
- **구현 가이드**: `.moai/docs/SPEC-ARIA-009/IMPLEMENTATION.md`
