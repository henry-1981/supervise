---
name: aria-status
description: >
  ARIA 프로젝트 상태 대시보드 명령어 - CAPA Tracker, Risk Register,
  Submission Tracker, Document Registry, Google Calendar의 현재 상태를
  종합적으로 표시합니다. 위험 상황(Overdue, Unacceptable risk)을
  감지하고 경고를 표시합니다.
license: Apache-2.0
compatibility: Designed for Claude Code
user-invocable: true
metadata:
  version: "1.0.0"
  category: "aria"
  status: "active"
  updated: "2026-02-09"
  tags: "aria, status, dashboard, overview"
  argument-hint: "[--summary] [--detailed] [--alert-only]"
---

# ARIA 프로젝트 상태 대시보드 명령어

## 목적

ARIA 시스템의 모든 데이터베이스와 Google Calendar의 현재 상태를 종합적으로 표시하고, 위험 상황을 경고합니다.

## 사용법

```
/aria status              # 전체 대시보드
/aria status --summary    # 요약 보기
/aria status --detailed   # 상세 보기
/aria status --alert-only # 경고 항목만
```

## 대시보드 구성

### 1. CAPA Tracker 상태

```markdown
## CAPA Tracker

### 요약
- 전체 CAPA: 15건
- Open: 5건 (🟡 주의)
- In Progress: 7건
- Verified: 2건
- Closed: 1건

### 경고 항목

🔴 **CRITICAL: Overdue (2건)**
- CAPA-2024-003: Design Validation Failure
  - 마감일: 2024-01-15 (15일 초과)
  - 담당자: 홍길동
  - 조치: 즉시 리뷰 필요, 일정 재조정

🔴 **CRITICAL: Overdue (1건)**
- CAPA-2024-008: Supplier Qualification Gap
  - 마감일: 2024-01-20 (10일 초과)
  - 담당자: 김철수
  - 조치: 공급사 re-qualification 진행

🟡 **WARNING: Due within 7 days (3건)**
- CAPA-2024-012: Risk Assessment Update
  - 마감일: 2024-02-05 (3일 남음)
- CAPA-2024-013: Document Revision
  - 마감일: 2024-02-07 (5일 남음)
- CAPA-2024-014: Training Completion
  - 마감일: 2024-02-08 (6일 남음)

### Notion 페이지: [CAPA Tracker Dashboard](https://notion.so/capa-dashboard)
```

### 2. Risk Register 상태

```markdown
## Risk Register

### 요약
- 전체 위험: 42건
- Acceptable: 35건 (🟢)
- Unacceptable: 1건 (🔴 위험)
- Review Overdue: 4건 (🟡 주의)

### 경고 항목

🔴 **CRITICAL: Unacceptable Risk (1건)**
- RISK-015: Software Failure - Patient Safety Impact
  - Severity: S5 (치명적)
  - Probability: P3 (보통)
  - Risk Level: 15 (높음)
  - 현재 통제 조치: 불충분
  - 조치: 즉시 추가 통제 조치 필요, CAPA 생성 권장

🟡 **WARNING: Review Overdue (4건)**
- RISK-008: Electrical Safety
  - 마감일: 2024-01-10 (20일 초과)
- RISK-012: Software Compatibility
  - 마감일: 2024-01-15 (15일 초과)
- RISK-022: Sterile Packaging
  - 마감일: 2024-01-18 (12일 초과)
- RISK-028: Labeling Requirements
  - 마감일: 2024-01-20 (10일 초과)

### Notion 페이지: [Risk Register Dashboard](https://notion.so/risk-dashboard)
```

### 3. Submission Tracker 상태

```markdown
## Submission Tracker

### 요약
- 진행 중 제출: 3건
- 계획된 제출: 2건
- 완료된 제출: 8건 (2024년)

### 다가오는 제출

🔴 **CRITICAL: Deadline < 7 days (1건)**
- SUB-510K-045: [Device Name] 510(k) Submission
  - 목표일: 2024-02-10 (5일 남음)
  - 현재 상태: Preparation (80% 완료)
  - 남은 작업: Final Review, Pre-submission Meeting
  - 담당자: 이영희
  - 조치: 일정 확인, 완료되지 않은 항목 우선 완료

🟡 **WARNING: Deadline 7-30 days (2건)**
- SUB-CE-012: CE Mark Technical Documentation
  - 목표일: 2024-03-15 (35일 남음)
  - 현재 상태: Early Preparation
- SUB-PMA-003: PMA Submission
  - 목표일: 2024-04-20 (71일 남음)
  - 현재 상태: Planning

### Notion 페이지: [Submission Tracker Dashboard](https://notion.so/submission-dashboard)
```

### 4. Document Registry 상태

```markdown
## Document Registry

### 요약
- 전체 문서: 285건
- 승인 대기: 8건 (🟡 주의)
- 리뷰 마감 초과: 3건 (🔴 위험)
- 예정된 리뷰: 12건 (30일 이내)

### 경고 항목

🔴 **CRITICAL: Review Overdue (3건)**
- DOC-SOP-015: 510(k) Submission Process SOP
  - 리뷰 마감: 2024-01-10 (20일 초과)
  - 상태: Approved (재검토 필요)
- DOC-WI-028: Software Validation WI
  - 리뷰 마감: 2024-01-15 (15일 초과)
  - 상태: Under Review
- DOC-REP-034: Risk Assessment Report
  - 리뷰 마감: 2024-01-20 (10일 초과)
  - 상태: Draft

🟡 **WARNING: Pending Approval (8건)**
- DOC-SOP-045: MDR Classification Procedure
  - 제출일: 2024-01-25
  - 승인 대기: 5일 경과
- DOC-TMP-011: Validation Protocol Template
  - 제출일: 2024-01-28
  - 승인 대기: 2일 경과
... (총 8건)

### Notion 페이지: [Document Registry Dashboard](https://notion.so/document-dashboard)
```

### 5. Google Calendar 이벤트

```markdown
## Google Calendar - Regulatory Events

### 다가오는 이벤트

🔴 **CRITICAL: 이번 주 (2건)**
- 2024-02-05: FDA Pre-submission Meeting
  - 시간: 14:00-15:00
  - 준비사항: Presentation, Q&A准备
- 2024-02-08: NB Audit - Design Control
  - 시간: 09:00-17:00
  - 준비사항: Design dossier, Evidence documents

🟡 **WARNING: 다음 주 (3건)**
- 2024-02-12: Management Review Meeting
  - 시간: 10:00-12:00
- 2024-02-14: CAPA Review Committee
  - 시간: 15:00-16:00
- 2024-02-15: Risk Assessment Workshop
  - 시간: 13:00-17:00

🔵 **INFO: 예정된 이벤트 (8건)**
- 2024-02-20: ISO 13485 Internal Audit
- 2024-02-25: 510(k) Submission Target Date
- 2024-03-10: Notified Body Surveillance Audit
- ...

### Google Calendar: [Regulatory Calendar](https://calendar.google.com/aria)
```

## 경고 시스템

### 경고 레벨

| 레벨 | 색상 | 조건 | 예시 |
|------|------|------|------|
| Critical | 🔴 | CAPA overdue, Unacceptable risk, Deadline < 7 days | 즉시 조치 필요 |
| Warning | 🟡 | Review overdue, Pending approval, Deadline 7-30 days | 주의 필요 |
| Info | 🔵 | 예정된 이벤트, 상태 변경 | 참고용 |

### 경고 표시

```markdown
🔴 **CRITICAL: [카테고리]**
  - 항목 제목
  - 상세 정보
  - 마감일/기한
  - 조치 제안
  - Notion 페이지 링크
```

## 옵션 상세

### --summary (요약 보기)

```markdown
## ARIA Status Summary

### 경고 요약
🔴 Critical: 6건
  - CAPA Overdue: 2건
  - Unacceptable Risk: 1건
  - Submission Deadline < 7 days: 1건
  - Document Review Overdue: 3건

🟡 Warning: 12건
  - CAPA Due within 7 days: 3건
  - Risk Review Overdue: 4건
  - Pending Approval: 8건

### 주요 지표
- CAPA Open: 5/15 (33%)
- Risk Unacceptable: 1/42 (2.4%)
- Submission Progress: 80% (1건 마감 임박)
- Document Pending Approval: 8/285 (2.8%)

### 즉시 조치 필요 항목
1. CAPA-2024-003: Design Validation Failure (15일 초과)
2. RISK-015: Software Failure - Patient Safety Impact
3. SUB-510K-045: 510(k) Submission (5일 남음)

자세한 내용은 /aria status --detailed를 확인하세요.
```

### --detailed (상세 보기)

모든 항목의 상세 정보를 표시합니다 (기본값).

### --alert-only (경고 항목만)

Critical 및 Warning 항목만 표시합니다.

```markdown
## Alert-Only View

### 🔴 CRITICAL (6건)
... (모든 Critical 항목 상세)

### 🟡 WARNING (12건)
... (모든 Warning 항목 상세)
```

## 대시보드 업데이트

### 실시간 업데이트

```yaml
조건: Notion DB 변경 시
동작:
  1. Notion API webhook 또는 polling으로 변경 감지
  2. 대시보드 자동 갱신
  3. 변경사항 사용자에게 알림 (Critical 항목)

주기: 5분마다 자동 새로고침
```

### 푸시 알림

```yaml
조건: 새로운 Critical 항목 발생 시
동작:
  1. 사용자에게 푸시 알림 전송
  2. 이메일 알림 (선택사항)
  3. Notion 페이지 링크 포함

예시:
  "새로운 CAPA Overdue 항목이 발생했습니다:
   CAPA-2024-015, 마감일: 2024-01-30
   자세한 내용: [Notion 페이지]"
```

## 통계 및 추이

### 월간 보고서

```markdown
## ARIA Monthly Status Report (2024-01)

### CAPA 성과
- 신규 CAPA: 5건
- 완료 CAPA: 3건
- 평균 완료 기간: 18일 (목표: 14일)
- overdue发生率: 13% (목표: 5% 미만)

### Risk 관리
- 신규 위험: 8건
- 완화된 위험: 6건
- Unacceptable risk: 1건 (지속 모니터링)

### Submission 진행률
- 제출 완료: 2건
- 진행 중: 3건
- 평균 준비 기간: 85일

### Document 관리
- 신규 문서: 12건
- 승인 완료: 10건
- 평균 승인 기간: 5일
```

## 오류 처리

### Notion API 연결 실패

```
오류: Notion 데이터베이스에 연결할 수 없습니다.

해결 방법:
1. 인터넷 연결을 확인하세요
2. Notion API 키가 유효한지 확인하세요
3. /aria init notion을 실행하여 재설정하세요
```

### Google Calendar 연결 실패

```
오류: Google Calendar에 연결할 수 없습니다.

해결 방법:
1. OAuth 인증이 유효한지 확인하세요
2. /aria init google을 실행하여 재인증하세요
```

## 완료 마커

상태 조회 완료 시 `<aria:status:complete alerts=N>` 마커를 추가합니다. (N: 경고 수)

## 참고

- 대시보드는 Notion DB와 Google Calendar의 실시간 데이터를 기반으로 합니다
- 모든 항목은 Notion 페이지와 직접 연결됩니다
- 경고 임계값은 설정에서 조정 가능합니다
- 월간 보고서는 자정에 자동 생성됩니다
