---
name: aria-search
description: >
  ARIA 통합 검색 명령어 - Notion 데이터베이스, Context7 MCP 규정 문서,
  Google Workspace(Gmail, Docs, Drive)를 동시에 검색하고 결과를 통합하여 표시합니다.
  관련성 순으로 정렬된 결과를 제공하며, 카테고리별 필터링을 지원합니다.
license: Apache-2.0
compatibility: Designed for Claude Code
user-invocable: true
metadata:
  version: "1.0.0"
  category: "aria"
  status: "active"
  updated: "2026-02-09"
  tags: "aria, search, notion, context7, google, unified"
  argument-hint: "\"search query\" [--filter category] [--date range]"
---

# ARIA 통합 검색 명령어

## 목적

ARIA 시스템의 모든 데이터 소스(Notion DB, Context7, Google Workspace)에서 통합 검색을 수행하고 관련성 높은 결과를 제공합니다.

## 사용법

```
/aria search "510(k) submission requirements"
/aria search "ISO 13485 clause 8.5.2" --filter standards
/aria search "CAPA overdue" --date "2024-01-01:2024-12-31"
/aria search "FDA 510(k) request" --filter emails
```

## 검색 소스

### 1. Notion 데이터베이스 검색

다음 6개 Notion DB를 검색합니다:

- **Regulatory Requirements:** 규제 요구사항, 표준 조항
- **Document Registry:** SOP, WI, Report 등 문서
- **CAPA Tracker:** CAPA 기록, 조치 계획
- **Risk Register:** 위험 분석, 통제 조치
- **Submission Tracker:** 제출 기록, 상태
- **Knowledge Base:** 지식 항목, 규정 해석

**검색 필드:** Title, Text, Rich Text 필드의 전체 텍스트 검색

### 2. Context7 MCP 검색

최신 규정 문서를 Context7에서 검색합니다:

**검색 라이브러리:**
- FDA 21 CFR 820 (Quality System Regulation)
- ISO 13485 (Medical devices - Quality management systems)
- EU MDR 2017/745 (Medical Device Regulation)
- IEC 62366 (Usability engineering)
- ISO 14971 (Risk management)

**검색 프로세스:**
1. `mcp__context7__resolve-library-id`로 라이브러리 ID 확인
2. `mcp__context7__get-library-docs`로 관련 문서 검색
3. 검색 결과를 Knowledge Base에 자동 저장 (캐싱)

### 3. Google Workspace 검색

Google 서비스에서 규제 관련 정보를 검색합니다:

- **Gmail:** FDA, NB(Nominated Body), MFDS로부터의 규제 서신
- **Google Docs:** 협업 문서, 검토 자료
- **Google Drive:** 규제 제출 패키지, 증거 문서

## 검색 프로세스

### 단계 1: 쿼리 분석

사용자 검색어를 분석하여 키워드와 의도를 파악합니다:

```
입력: "510(k) submission requirements for software medical device"
키워드 추출: ["510(k)", "submission", "requirements", "software", "medical device"]
의도 분류: 규제 요구사항 검색
데이터 소스 우선순위: Notion > Context7 > Google
```

### 단계 2: 병렬 검색 실행

세 데이터 소스에서 동시에 검색을 수행합니다:

```
[Parallel]
1. Notion DB 검색 (mcp__notion__query)
2. Context7 검색 (mcp__context7__get-library-docs)
3. Google 검색 (mcp__google__search)
```

### 단계 3: 결과 통합 및 점수 계산

검색 결과에 관련성 점수를 부여하고 정렬합니다:

```python
relevance_score = (
    keyword_match * 0.4 +        # 키워드 일치율
    semantic_similarity * 0.3 +   # 의미적 유사도
    recency * 0.2 +               # 최신성 (최근 문서 우선)
    source_authority * 0.1        # 출처 권위 (공식 문서 우선)
)
```

### 단계 4: 필터링 및 정렬

사용자가 지정한 필터를 적용하고 결과를 정렬합니다:

**카테고리 필터:**
- `requirements`: 규제 요구사항만
- `documents`: 문서 레지스트리만
- `capa`: CAPA 트래커만
- `risk`: 위험 등록부만
- `submissions`: 제출 트래커만
- `standards`: 표준/규격만
- `emails`: 이메일만
- `all`: 모든 카테고리 (기본값)

**날짜 범위 필터:**
```
--date "2024-01-01:2024-12-31"  # 기간 지정
--date "last-30-days"             # 최근 30일
--date "last-12-months"            # 최근 12개월
```

### 단계 5: 결과 표시

관련성 순으로 정렬된 결과를 표시합니다:

```markdown
## 검색 결과: "510(k) submission requirements"

총 23개 결과 발견 (Notion: 12, Context7: 8, Google: 3)

### 🔍 상위 결과 (관련성 90%+)

1. **[REQ-042] 21 CFR 807 Subpart E - 510(k) Requirements** (Notion)
   - 관련성: 95%
   - 출처: Regulatory Requirements DB
   - 요약: 510(k) 제출 요건, Predicate Device, Substantial Equivalence
   - 링크: [Notion 페이지](https://notion.so/req-042)

2. **[KB-156] 510(k) Software as Medical Device Guidance** (Context7)
   - 관련성: 92%
   - 출처: FDA Guidance Document
   - 요약: SaMD 510(k) 제출 가이드라인, 테스트 요건
   - 링크: [Context7 문서](...)

### 📋 카테고리별 결과

**Requirements (8건)**
- REQ-042: 21 CFR 807 Subpart E (95%)
- REQ-089: IEC 62304 Software Lifecycle (78%)
...

**Documents (5건)**
- DOC-SOP-015: 510(k) Submission Process SOP (85%)
...

**Standards (6건)**
- FDA Guidance: SaMD 510(k) (92%)
- ISO 13485 Clause 7.3 (72%)
...

**Emails (1건)**
- FDA 510(k) Request Letter (68%)
```

## 고급 기능

### 자동 Knowledge Base 업데이트

Context7 검색 결과를 자동으로 Knowledge Base에 저장합니다:

```yaml
조건: 관련성 점수 80% 이상且 Knowledge Base에 없는 항목
동작:
  1. Knowledge Base DB에 새 항목 생성
  2. 출처, 요약, 태그 저장
  3. 사용자에게 "새 지식 항목 추가됨" 알림
```

### 관련 문서 추천

검색 결과와 관련된 Notion 페이지를 추천합니다:

```
추천 문서:
- CAPA-2024-003: 510(k) Submission Gap Analysis
- RISK-012: Software Validation Risk
- DOC-REP-028: Previous 510(k) Submission Report
```

### 검색 기록 저장

모든 검색 쿼리를 Audit Log DB에 기록합니다:

```yaml
필드:
  - Timestamp: 검색 시간
  - Query: 검색어
  - Results Count: 결과 수
  - Top Result: 최상위 결과 ID
  - User: 사용자
```

## 필터 옵션 상세

### 카테고리 필터

```
--filter requirements    # 규제 요구사항
--filter documents       # 문서 레지스트리
--filter capa            # CAPA 트래커
--filter risk            # 위험 등록부
--filter submissions     # 제출 트래커
--filter standards       # 표준/규격 (Context7)
--filter emails          # 이메일 (Gmail)
--filter all             # 모든 카테고리 (기본값)
```

### 소스 필터

```
--source notion          # Notion DB만
--source context7        # Context7만
--source google          # Google Workspace만
--source all             # 모든 소스 (기본값)
```

### 정렬 옵션

```
--sort relevance         # 관련성 순 (기본값)
--sort date              # 최신순
--sort source            # 출처별 그룹
```

## 오류 처리

### 검색 결과 없음

```
검색 결과: "xyz abc"에 대한 결과가 없습니다.

제안:
1. 검색어를 일반화하여 다시 검색하세요 (예: "software validation")
2. Context7에서 규정 검색을 시도하세요
3. Knowledge Base에 새 항목 추가를 고려하세요
```

### API 속도 제한

```
안내: 검색 속도를 제한하고 있습니다 (Notion API rate limit)
예상 대기 시간: 30초
```

### 인증 만료

```
오류: Google OAuth 인증이 만료되었습니다.
해결: /aria init google을 실행하여 재인증하세요
```

## 사용 예시

### 예시 1: 규정 검색

```
/aria search "21 CFR 820.30 design controls"
→ Notion Regulatory Requirements, Context7 FDA docs 검색
→ Design Control 요구사항, 관련 문서 추천
```

### 예시 2: CAPA 검색

```
/aria search "CAPA overdue" --filter capa
→ CAPA Tracker DB에서 기한 초과 항목 검색
→ 관련 Risk Register 항목 표시
```

### 예시 3: 이메일 검색

```
/aria search "FDA 510(k) request" --filter emails --date "last-30-days"
→ Gmail에서 최근 30일간 FDA 510(k) 관련 이메일 검색
→ 관련 Notion 페이지와 연결 제안
```

### 예시 4: 종합 검색

```
/aria search "ISO 14971 risk management"
→ Notion Risk Register, Context7 ISO 14971, Google Docs 검색
→ 위험 관리 표준, 관련 CAPA, 문서 종합 표시
```

## 완료 마커

검색 완료 시 `<aria:search:complete results=N>` 마커를 추가합니다. (N: 결과 수)

## 참고

- 검색 결과는 관련성 점수 기준 100개까지만 표시합니다
- Context7 검색 결과는 자동으로 Knowledge Base에 캐싱됩니다 (TTL: 30일)
- Google Workspace 검색은 별도 OAuth 인증이 필요합니다
- 검색 기록은 Audit Log DB에 저장되어 감사 추적을 지원합니다
