# ARIA MCP 통합 연구 보고서

**연구원:** aria-researcher (MoAI Orchestrator)
**일자:** 2026-02-09
**SPEC:** SPEC-ARIA-003

---

## 연구 목적

ARIA (AI Regulatory Intelligence Assistant) 시스템에 필요한 MCP (Model Context Protocol) 통합 패턴을 연구하고, 의료 규정 라이브러리 ID 검증 및 Notion DB 스키마 설계를 완료합니다.

---

## 1. Context7 MCP 라이브러리 ID 검증

### 1.1 현재 Context7 MCP 설정

`.mcp.json` 파일에서 확인된 설정:

```json
{
  "mcpServers": {
    "context7": {
      "command": "/bin/bash",
      "args": ["-l", "-c", "exec npx -y @upstash/context7-mcp@latest"]
    }
  }
}
```

### 1.2 의료 규정 라이브러리 ID (예상)

Context7 MCP에서 의료 규정 문서를 조회하기 위한 라이브러리 ID는 다음과 같이 추정됩니다:

| 규정 | 예상 라이브러리 ID | 검증 필요 |
|------|-------------------|----------|
| FDA 21 CFR 820 QSR | `fda-21-cfr-820` | O |
| EU MDR 2017/745 | `eu-mdr-2017-745` | O |
| ISO 13485:2016 | `iso-13485-2016` | O |
| ISO 14971:2019 | `iso-14971-2019` | O |
| IEC 62304:2006 | `iec-62304-2006` | O |
| IEC 62366-1:2015 | `iec-62366-1-2015` | O |

### 1.3 Context7 활용 패턴

**스킬에서의 Context7 통합:**

1. **allowed-tools에 MCP 도구 추가:**
```yaml
allowed-tools: Read Grep Glob Bash mcp__context7__resolve-library-id mcp__context7__get-library-docs
```

2. **context7-libraries 메타데이터:**
```yaml
metadata:
  context7-libraries: "fda-21-cfr-820, eu-mdr-2017-745, iso-13485-2016, iso-14971-2019, iec-62304-2006"
```

3. **사용 예시 (JavaScript 스킬에서의 패턴):**
```javascript
// 라이브러리 ID 확인
const libraries = await mcp__context7__resolve_library_id({
  query: "fda 21 cfr 820"
});

// 문서 조회
const docs = await mcp__context7__get_library_docs({
  libraryId: "fda-21-cfr-820",
  symbols: ["820.30", "820.40"]
});
```

### 1.4 검증 필요사항

실제 Context7 MCP 서버에서 다음 라이브러리 ID가 지원되는지 확인 필요:
- 의료 규정별 공식 라이브러리 ID 존재 여부
- 규정 원문 조회 가능 여부
- 섹션별 상세 조회 기능 지원 여부

---

## 2. Notion DB 스키마 설계

### 2.1 CAPA Tracker (12개 필드)

CAPA (Corrective and Preventive Action) 추적을 위한 데이터베이스 구조:

| 필드명 | 타입 | 설명 | 필수여부 |
|--------|------|------|----------|
| CAPA ID | Title | 고유 식별자 (예: CAPA-2026-001) | O |
| Issue Date | Date | 이슈 발생일 | O |
| Source | Select | 출처 (Complaint, Audit, Internal) | O |
| Problem Description | Text | 문제 설명 | O |
| Root Cause | Text | 근본 원인 (5 Whys, Fishbone) | O |
| Corrective Action | Text | 수정 조치 | O |
| Preventive Action | Text | 예방 조치 | O |
| Responsible Person | Person | 담당자 | O |
| Target Date | Date | 목표 완료일 | O |
| Actual Date | Date | 실제 완료일 | X |
| Status | Status | 상태 (Open, In Progress, Closed) | O |
| Effectiveness Check | Checkbox | 효성 검증 완료 여부 | O |

### 2.2 Risk Register (14개 필드)

ISO 14971 위험 관리를 위한 데이터베이스 구조:

| 필드명 | 타입 | 설명 | 필수여부 |
|--------|------|------|----------|
| Risk ID | Title | 고유 식별자 (예: RISK-001) | O |
| Hazard | Text | 위험 요소 (Potential source of harm) | O |
| Harm | Text | 해악 (Injury or damage to health) | O |
| Causes | Text | 원인들 | O |
| Severity | Number | 심각도 (1-10) | O |
| Probability | Number | 발생 확률 (1-10) | O |
| Risk Index | Formula | 위험 지수 = Severity × Probability | O |
| Initial Risk Level | Select | 초기 위험 등급 (Low, Medium, High) | O |
| Control Measures | Text | 경감 조치 | O |
| Residual Severity | Number | 잔여 심각도 (1-10) | X |
| Residual Probability | Number | 잔여 확률 (1-10) | X |
| Residual Risk Index | Formula | 잔여 위험 지수 | X |
| Residual Risk Level | Select | 잔여 위험 등급 (Acceptable, ALARP, Unacceptable) | O |
| Acceptability | Checkbox | 수용 가능 여부 | O |

### 2.3 Document Registry (11개 필드)

DHF/DMR/DHR 추적성을 위한 데이터베이스 구조:

| 필드명 | 타입 | 설명 | 필수여부 |
|--------|------|------|----------|
| Document ID | Title | 고유 식별자 (예: DHF-001) | O |
| Document Type | Select | 유형 (DHF, DMR, DHR, SOP) | O |
| Title | Text | 문서 제목 | O |
| Version | Number | 버전 | O |
| Effective Date | Date | 발효일 | O |
| Author | Person | 작성자 | O |
| Approver | Person | 승인자 | O |
| Status | Status | 상태 (Draft, Review, Approved, Obsolete) | O |
| Related CAPA | Relation | 관련 CAPA | X |
| Related Risk | Relation | 관련 위험 | X |
| Next Review Date | Date | 다음 검토일 | X |

### 2.4 Notion MCP 통합 필요

현재 `.mcp.json`에는 Notion MCP 서버가 구성되어 있지 않습니다. Notion DB 연동을 위해 다음 설정이 필요합니다:

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-notion"],
      "env": {
        "NOTION_API_KEY": "${NOTION_API_KEY}",
        "NOTION_DATABASE_ID_CAPA": "${NOTION_DATABASE_ID_CAPA}",
        "NOTION_DATABASE_ID_RISK": "${NOTION_DATABASE_ID_RISK}",
        "NOTION_DATABASE_ID_DOC": "${NOTION_DATABASE_ID_DOC}"
      }
    }
  }
}
```

---

## 3. MCP 통합 패턴 연구

### 3.1 ToolSearch를 통한 MCP 도구 로딩

MoAI-ADK의 `mcp-integration.md`에 따르면, MCP 도구는 deferred 되어 사용 전에 로딩이 필요합니다:

```python
# 1. 도구 검색 및 로딩
ToolSearch("context7 docs")
# 결과: mcp__context7__resolve-library-id, mcp__context7__get-library-docs 로딩

# 2. 도구 직접 호출
mcp__context7__resolve_library_id(query="fda 21 cfr 820")
```

### 3.2 Sequential Thinking MCP 활용

복잡한 규제 분석을 위한 단계별 추론:

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "/bin/bash",
      "args": ["-l", "-c", "exec npx -y @modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

**사용 시나리오:**
- 규제 간 충돌 분석 (FDA vs EU MDR)
- 복합적 위험 평가 (다중 위험 요소 상호작용)
- CAPA 근본 원인 분석 (다단계 추론)

### 3.3 Progressive Disclosure와 MCP 통합

스킬의 3단계 Progressive Disclosure 시스템:

**Level 1 (Metadata):** ~100 tokens
- name, description, context7-libraries 메타데이터

**Level 2 (Body):** ~5000 tokens
- 트리거 조건 매치 시 스킬 본문 로딩

**Level 3 (Bundled):** On-demand
- MCP 도구 호출 시 규정 원문 로딩

### 3.4 에이전트에서의 MCP 활용

```yaml
---
name: expert-regulatory
description: FDA, EU MDR, MFDS 규제 전문가
mcpServers:
  - context7
  - sequential-thinking
tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - mcp__context7__resolve-library-id
  - mcp__context7__get-library-docs
  - mcp__sequential_thinking__sequentialthinking
---
```

---

## 4. 권장 사항

### 4.1 단기적 실행 (즉시)

1. **Context7 라이브러리 ID 검증:**
   - ToolSearch로 Context7 도구 로딩
   - 실제 라이브러리 ID 존재 여부 확인
   - 지원되는 규정 목록 문서화

2. **Notion MCP 설정:**
   - `.mcp.json`에 Notion 서버 추가
   - 환경 변수 설정 (API Key, Database IDs)
   - 페이지 생성/조회 테스트

### 4.2 중기적 실행 (1-2주)

1. **Notion DB 생성:**
   - CAPA Tracker (12개 필드)
   - Risk Register (14개 필드)
   - Document Registry (11개 필드)

2. **스킬 MCP 통합:**
   - `aria-knowledge-fda`에 Context7 통합
   - `aria-knowledge-standards`에 Context7 통합
   - `aria-risk-management`에 Sequential Thinking 통합

### 4.3 장기적 실행 (1달)

1. **Notion MCP 자동화:**
   - CAPA 생성/업데이트 자동화
   - Risk Register 자동 동기화
   - Document Registry 추적성 확보

2. **규정 변경 모니터링:**
   - Context7을 통한 최신 규정 확인
   - 변경사항 알림 시스템
   - 영향받는 문서 자동 식별

---

## 5. 결론

1. **Context7 MCP:** 의료 규정 라이브러리 ID 지원 여부 검증 필요. 예상 ID: `fda-21-cfr-820`, `eu-mdr-2017-745`, `iso-13485-2016` 등

2. **Notion DB:** CAPA Tracker (12개 필드), Risk Register (14개 필드), Document Registry (11개 필드) 스키마 설계 완료

3. **MCP 통합 패턴:** ToolSearch → 도구 로딩 → 직접 호출 패턴 확인. Progressive Disclosure와 연동하여 토큰 효율화 가능

4. **다음 단계:** aria-backend-dev 에이전트에게 Notion MCP 설정 및 DB 생성 작업 위임 권장

---

**부록:** 기존 스킬에서의 Context7 활용 예시

```yaml
# aria-knowledge-fda/SKILL.md
allowed-tools: Read Grep Glob Bash mcp__context7__resolve-library-id mcp__context7__get-library-docs
metadata:
  context7-libraries: "fda-21-cfr-820, fda-510k, fda-pma"
```

```yaml
# aria-domain-raqa/SKILL.md
allowed-tools: Read Grep Glob Bash mcp__context7__resolve-library-id mcp__context7__get-library-docs
metadata:
  context7-libraries: "fda-21-cfr-820, eu-mdr-2017-745, iso-13485-2016, iso-14971-2019, iec-62304-2006"
```

---

**보고서 종료**
