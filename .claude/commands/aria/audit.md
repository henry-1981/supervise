---
name: aria-audit
description: >
  ARIA 감사 추적(Audit Trail) 조회 명령어 - Notion Audit Log 데이터베이스에서
  결정 이력, 문서 변경, 승인 기록을 검색합니다. 에이전트, 날짜 범위,
  행동 유형별 필터링을 지원하며, CSV/PDF 보고서 내보내기 기능을 제공합니다.
license: Apache-2.0
compatibility: Designed for Claude Code
user-invocable: true
metadata:
  version: "1.0.0"
  category: "aria"
  status: "active"
  updated: "2026-02-09"
  tags: "aria, audit, trail, log, compliance"
  argument-hint: "search [--agent name] [--date range] [--action type] [--export format]"
---

# ARIA 감사 추적(Audit Trail) 조회 명령어

## 목적

Notion Audit Log 데이터베이스에서 모든 결정 이력, 문서 변경, 승인 기록을 검색하고 감사 추적 보고서를 생성합니다. 규제 컴플라이언스 증빙을 지원합니다.

## 사용법

```
/aria audit search "CAPA approval" --agent expert-regulatory
/aria audit search --date "2024-01-01:2024-01-31" --action Approve
/aria audit search "document approval" --export csv
/aria audit search --agent orchestrator --export pdf
```

## Audit Log 데이터베이스 구조

### 필드

- **Timestamp:** 작업 날짜/시간 (Created time)
- **Agent:** 에이전트 유형 (orchestrator, expert-regulatory, expert-risk 등)
- **Action:** 행동 유형 (Create, Update, Delete, Approve, Reject)
- **Entity:** 엔티티 유형 (Document, CAPA, Risk, Submission, Requirement)
- **Entity ID:** 관련 엔티티 ID (예: CAPA-2024-003)
- **Decision:** 결정 내용 (Text)
- **Rationale:** 결정 근거 (Rich Text)
- **Outcome:** 결과 (Approved, Rejected, Pending, Deferred)
- **Related Docs:** 관련 문서 (Relation)

### 검색 가능 필드

Timestamp, Agent, Action, Entity, Entity ID, Decision, Outcome

## 검색 프로세스

### 단계 1: 검색 쿼리 구성

```
입력: "CAPA approval" --agent expert-regulatory --date "2024-01-01:2024-01-31"

쿼리 구성:
1. Text 검색: Decision, Rationale 필드에서 "CAPA" AND "approval" 검색
2. 필터: Agent = "expert-regulatory"
3. 필터: Timestamp >= "2024-01-01" AND <= "2024-01-31"
4. 정렬: Timestamp 내림차순 (최신 먼저)
```

### 단계 2: 검색 결과 표시

```markdown
## 감사 추적 검색 결과: "CAPA approval"

검색 조건:
- Agent: expert-regulatory
- 날짜: 2024-01-01 ~ 2024-01-31
- Action: Approve

### 발견된 항목 (12건)

1. **2024-01-28 14:32** - expert-regulatory
   - Action: Approve
   - Entity: CAPA
   - Entity ID: CAPA-2024-008
   - Decision: Supplier qualification CAPA 승인
   - Rationale: Supplier가 ISO 13485 인증을 획득하여 요구사항 충족
   - Outcome: Approved
   - Related Docs: DOC-REP-112 (Supplier Audit Report)
   - [Notion 페이지 보기](https://notion.so/audit-log-xxx)

2. **2024-01-25 10:15** - expert-regulatory
   - Action: Approve
   - Entity: CAPA
   - Entity ID: CAPA-2024-007
   - Decision: Design validation CAPA 승인
   - Rationale: 모든 validation test가 pass함, USability study 완료
   - Outcome: Approved
   - Related Docs: DOC-REP-108 (Validation Report)
   - [Notion 페이지 보기](https://notion.so/audit-log-xxx)

...

### 요약
- 전체 검색: 12건
- Approved: 10건
- Rejected: 1건
- Pending: 1건
```

## 필터 옵션

### 에이전트 필터

```
--agent orchestrator           # MoAI orchestrator
--agent expert-regulatory      # 규제 전문가
--agent expert-risk            # 위험 관리 전문가
--agent expert-capa            # CAPA 전문가
--agent expert-document        # 문서 관리 전문가
--agent all                    # 모든 에이전트 (기본값)
```

### 날짜 필터

```
--date "2024-01-01:2024-01-31"  # 기간 지정
--date "today"                   # 오늘
--date "last-7-days"             # 최근 7일
--date "last-30-days"            # 최근 30일
--date "this-month"              # 이번 달
--date "last-month"              # 지난 달
```

### 행동(Action) 필터

```
--action Create                 # 생성
--action Update                 # 수정
--action Delete                 # 삭제
--action Approve                # 승인
--action Reject                 # 거부
--action all                    # 모든 행동 (기본값)
```

### 엔티티(Entity) 필터

```
--entity Document              # 문서
--entity CAPA                  # CAPA
--entity Risk                  # 위험
--entity Submission            # 제출
--entity Requirement           # 요구사항
--entity all                   # 모든 엔티티 (기본값)
```

## 보고서 내보내기

### CSV 내보내기

```csv
Timestamp,Agent,Action,Entity,Entity ID,Decision,Outcome
2024-01-28 14:32,expert-regulatory,Approve,CAPA,CAPA-2024-008,"Supplier qualification CAPA 승인",Approved
2024-01-25 10:15,expert-regulatory,Approve,CAPA,CAPA-2024-007,"Design validation CAPA 승인",Approved
...
```

사용법:
```
/aria audit search "CAPA approval" --export csv
→ audit-trail-20240129.csv 파일로 저장
```

### PDF 내보내기

감사 추적 보고서를 PDF 형식으로 생성합니다:

```
/aria audit search --date "2024-01-01:2024-01-31" --export pdf
→ audit-trail-report-202401.pdf 파일로 저장
```

PDF 보고서 구조:
```markdown
# ARIA 감사 추적 보고서

**보고서 기간:** 2024-01-01 ~ 2024-01-31
**생성일:** 2024-02-09
**생성자:** ARIA System

## 요약
- 전체 항목: 156건
- 에이전트별 분포: orchestrator (45), expert-regulatory (32), ...
- 행동별 분포: Create (42), Update (68), Approve (28), ...
- 엔티티별 분포: Document (58), CAPA (32), Risk (28), ...

## 타임라인

### 2024-01-31 (5건)
...

### 2024-01-30 (8건)
...

## 상세 내역
...
```

## 타임라인 뷰

시간 순서대로 감사 추적 이력을 표시합니다:

```markdown
## 감사 추적 타임라인: 2024-01-29

### 14:32 - expert-regulatory
📝 CAPA-2024-008 승인
   - 결정: Supplier qualification CAPA 승인
   - 근거: ISO 13485 인증 획득
   - 결과: Approved

### 14:15 - orchestrator
🔧 CAPA-2024-008 생성
   - 결정: Supplier qualification gap으로 인한 CAPA 개시
   - 근거: NB audit finding
   - 결과: Pending

### 13:45 - expert-risk
📊 RISK-022 재평가
   - 결정: Risk level down-grade (15 → 9)
   - 근거: 추가 통제 조치 시행
   - 결과: Approved

### 11:20 - expert-document
📄 DOC-SOP-045 승인
   - 결정: MDR classification procedure 승인
   - 근거: NB 코멘트 반영 완료
   - 결과: Approved

[전체 타임라인 보기]
```

## 감사 추적 무결성

### 불변성 보장

```yaml
Audit Log 불변성:
  - 생성된 Audit Log 항목은 수정 불가
  - 삭제 금지 (Read-only 권한)
  - Notion Page Version History로 변경 이력 추적

위조 방지:
  - Timestamp는 Notion Created time (자동 생성)
  - Agent는 시스템에서 자동 기록
  - 사용자가 직접 수정 불가
```

### 완전성 검증

```yaml
감사 추적 완전성 체크:
  1. 모든 결정은 Audit Log에 기록되어야 함
  2. Related Docs Relation으로 연결 검증
  3. Timestamp 연속성 검증 (gap 없는지)
  4. Agent 활동 내역 일치 검증

불일치 감지 시:
  - 경고: "Audit Log gap detected: 2024-01-15 14:00 ~ 16:00"
  - 조치: 관리자에게 알림, 수동 조사 필요
```

## 규제 컴플라이언스 지원

### ISO 13485 요구사항

```
ISO 13485 Clause 4.2.4: Quality management system documentation
- 모든 결정이 문서화되어야 함
- 변경 이력이 유지되어야 함
- 감사 추적이 가능해야 함

ARIA Audit Log는 다음을 제공:
- Decision: 결정 내용 문서화
- Rationale: 결정 근거 기록
- Timestamp: 변경 시간 기록
- Related Docs: 관련 문서 연결
```

### FDA 21 CFR 820 요구사항

```
21 CFR 820.40: Management responsibility
- 모든 품질 활동이 문서화되어야 함
- 관리자 검토 기록 유지

21 CFR 820.180: General records
- 기록의 보존 기간: 제품 수명 기간 + 2년
- 기록의 검색 가능성 보장

ARIA Audit Log는 다음을 제공:
- 모든 에이전트 활동 기록
- Notion DB로 영구 보존
- 전체 텍스트 검색 지원
```

### EU MDR 요구사항

```
EU MDR Annex IX: Quality management system
- 내부 감사 기록 유지
- 경영 검토 기록
- CAPA 추적 가능성

ARIA Audit Log는 다음을 제공:
- 내부 감사 추적
- 관리자 결정 기록
- CAPA lifecycle 추적
```

## 고급 검색

### 복합 조건 검색

```
/aria audit search --agent expert-regulatory --action Approve --entity CAPA --date "last-30-days"

결과: 최근 30일간 expert-regulatory가 승인한 모든 CAPA 결정
```

### 결정 근거 검색

```
/aria audit search "ISO 13485"

결과: Decision 또는 Rationale 필드에 "ISO 13485"를 포함한 모든 감사 추적
```

### 결과 필터링

```
/aria audit search --outcome Approved --date "this-month"

결과: 이번 달 승인된 모든 결정
```

## 오류 처리

### Audit Log 없음

```
검색 결과: 해당 조건에 맞는 Audit Log가 없습니다.

제안:
1. 검색 조건을 완화하세요 (날짜 범위 확장)
2. 다른 필터를 사용해 보세요
3. 전체 Audit Log 확인: /aria audit search --date "last-30-days"
```

### 권한 없음

```
오류: Audit Log에 접근할 권한이 없습니다.

해결 방법:
1. Notion Integration에 Audit Log DB 접근 권한 부여
2. /aria init notion을 실행하여 권한 재설정
```

### 내보내기 실패

```
오류: CSV/PDF 내보내기에 실패했습니다.

해결 방법:
1. 검색 결과가 너무 많습니다 (1000건 이상). 날짜 범위를 축소하세요
2. 디스크 공간을 확인하세요
3. 파일 권한을 확인하세요
```

## 사용 예시

### 예시 1: CAPA 결정 이력

```
/aria audit search --entity CAPA --action Approve --date "last-30-days"

결과:
- 최근 30일간 승인된 CAPA 결정 8건
- 각 CAPA의 결정 근거, 관련 문서
- CAPA-2024-008, CAPA-2024-007, ... 상세 정보
```

### 예시 2: 문서 변경 추적

```
/aria audit search --entity Document --action Update --date "2024-01-01:2024-01-31"

결과:
- 1월 중 문서 변경 이력 42건
- 변경된 문서: DOC-SOP-015, DOC-WI-028, ...
- 변경 시간, 담당 에이전트, 변경 사유
```

### 예시 3: 에이전트 활동 보고서

```
/aria audit search --agent expert-regulatory --date "last-month" --export pdf

결과:
- expert-regulatory 활동 보고서 (PDF)
- 전체 활동 32건
- 활동 유형별 분포
- 타임라인 뷰
```

### 예시 4: 규제 준수 증빙

```
/aria audit search "NB audit" --date "2024-01-01:2024-01-31" --export csv

결과:
- NB audit 관련 모든 활동
- CSV 파일로 규제 증빙 자료 제공
- CAPA, Risk, Document 변경 추적
```

## 완료 마커

검색 완료 시 `<aria:audit:complete results=N exported=Y>` 마커를 추가합니다.
(N: 결과 수, Y: 내보내기 여부)

## 참고

- Audit Log는 수정 불가한 영구 기록입니다
- 모든 결정은 Audit Log에 기록되어야 합니다 (감사 추적 완전성)
- CSV/PDF 내보내기는 규제 컴플라이언스 증빙을 지원합니다
- 검색 결과는 1000건까지만 내보낼 수 있습니다
- Audit Log는 제품 수명 기간 + 2년간 보존됩니다 (FDA 21 CFR 820.180)
