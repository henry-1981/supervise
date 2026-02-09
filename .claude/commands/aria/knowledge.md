---
name: aria-knowledge
description: >
  ARIA 지식 베이스 조회 명령어 - Notion Knowledge Base 데이터베이스에서
  규제 지식, 표준 해석, 모범 사례를 조회합니다. Knowledge Base에
  해당 항목이 없으면 Context7 MCP에서 자동 검색하고 저장합니다.
license: Apache-2.0
compatibility: Designed for Claude Code
user-invocable: true
metadata:
  version: "1.0.0"
  category: "aria"
  status: "active"
  updated: "2026-02-09"
  tags: "aria, knowledge, base, query, context7"
  argument-hint: "\"topic or question\" [--auto-expand]"
---

# ARIA 지식 베이스 조회 명령어

## 목적

Notion Knowledge Base 데이터베이스에서 규제 지식을 조회하고, 해당 항목이 없으면 Context7 MCP에서 자동 검색하여 Knowledge Base를 확장합니다.

## 사용법

```
/aria knowledge "MDR classification rules"
/aria knowledge "ISO 13485 clause 8.5.2" --auto-expand
/aria knowledge "software validation requirements"
/aria knowledge "risk management principles"
```

## Knowledge Base 구조

### 데이터베이스 필드

- **ID (Title):** 지식 항목 고유 번호 (예: KB-001)
- **Topic:** 주제/제목
- **Category:** 카테고리 (Regulation, Standard, Guidance, Best Practice)
- **Content:** 지식 내용 (Rich Text)
- **Source:** 출처 (FDA, ISO, NB, MFDS 등)
- **Applicable To:** 적용 범위 (Design, Risk, CAPA, Submission)
- **Last Updated:** 마지막 업데이트 일자
- **Confidence:** 신뢰도 (High, Medium, Low)
- **Tags:** 검색용 태그

### 관계(Relations)

- **Regulatory Requirements:** 관련 규제 요구사항
- **Document Registry:** 관련 문서

## 조회 프로세스

### 단계 1: Notion Knowledge Base 검색

```
입력: "MDR classification rules"

검색:
1. Topic 필드에서 "MDR" AND "classification" 검색
2. Content 필드에서 "rules" 키워드 검색
3. Tags 필드에서 관련 태그 검색
```

### 단계 2: 검색 결과 표시

```markdown
## Knowledge Base 검색 결과: "MDR classification rules"

### 🔍 발견된 항목 (3건)

1. **[KB-089] EU MDR Classification Rules** (신뢰도: High)
   - 출처: EU MDR 2017/745 Annex VIII
   - 업데이트: 2024-01-15
   - 내용: MDR 분류 규칙 22개항, Rule 1-21 상세 설명
   - 적용: Submission, Risk
   - 태그: #mdr #classification #rule-based

   [Notion 페이지 보기](https://notion.so/kb-089)

2. **[KB-142] MDR vs MDD Classification Comparison** (신뢰도: Medium)
   - 출처: NB Guidance Document
   - 업데이트: 2023-11-20
   - 내용: MDR과 MDD 분류 규칙 비교, 주요 변경사항
   - 적용: Submission
   - 태그: #mdr #mdd #comparison

### 📎 관련 규제 요구사항
- REQ-156: MDR Classification Requirements
- REQ-201: Device Classification Criteria

### 📄 관련 문서
- DOC-SOP-045: MDR Classification Procedure
- DOC-REP-112: MDR Classification Analysis Report
```

### 단계 3: Knowledge Base 확장 (--auto-expand)

Knowledge Base에 해당 항목이 없거나 결과가 불충분할 때:

```yaml
조건:
  - 검색 결과 0건 또는
  --auto-expand 플래그 지정 시

자동 확장 프로세스:
  1. Context7 MCP 검색 실행
  2. 검색 결과를 Knowledge Base 형식으로 변환
  3. Notion Knowledge Base DB에 새 항목 생성
  4. 사용자에게 "새 지식 항목 추가됨" 알림
```

## Context7 자동 검색

### 라이브러리 매핑

질문 유형에 따라 적절한 Context7 라이브러리를 선택합니다:

| 질문 키워드 | Context7 라이브러리 |
|-----------|-------------------|
| FDA, 21 CFR, 510(k), QSR | fda-21-cfr-820 |
| ISO 13485, ISO 14971 | iso-13485, iso-14971 |
| MDR, CE marking, European | eu-mdr-2017-745 |
| IEC 60601, IEC 62366 | iec-60601, iec-62366 |
| Software, SaMD | aami-tir45, fda-guidance |

### 검색 프로세스

```
입력: "software validation requirements"

1. 라이브러리 식별: aami-tir45, fda-guidance
2. mcp__context7__resolve-library-id 호출
3. mcp__context7__get-library-docs로 검색
4. 관련 문서 추출 및 요약
5. Knowledge Base에 저장:
   - ID: KB-XXX (자동 생성)
   - Topic: "Software Validation Requirements"
   - Category: "Guidance"
   - Content: [Context7 검색 결과 요약]
   - Source: "AAMI TIR45, FDA Guidance"
   - Confidence: "High" (공식 문서)
   - Tags: #software #validation #samd
```

## 지식 항목 자동 업데이트

### 주간 업데이트 확인

매주 Context7에서 최신 규정 변경사항을 확인합니다:

```yaml
일정: 매주 일요일 00:00
프로세스:
  1. Knowledge Base의 모든 항목 순회
  2. Context7에서 최신 버전 확인
  3. 버전 변경사항 있으면:
     - Content 업데이트
     - Last Updated 갱신
     - 변경사항 요약 추가
  4. 사용자에게 주요 변경사항 알림
```

### 만료된 지식 항목 탐지

```yaml
기준: Last Updated > 12개월
동작:
  1. "Confidence"를 "Medium" 또는 "Low"로 down-grade
  2. 사용자에게 "지식 항목 업데이트 필요" 알림
  3. Context7에서 최신 정보 검색 제안
```

## 카테고리별 조회 패턴

### Regulation (규정)

```
/aria knowledge "21 CFR 820.30 design controls"
→ FDA QSR Design Control 요구사항
→ 관련 SOP, Work Instruction 추천
```

### Standard (표준)

```
/aria knowledge "ISO 13485 management review"
→ ISO 13485 경영 검토 요건
→ 관련 Evidence, Checklist 추천
```

### Guidance (가이드라인)

```
/aria knowledge "FDA SaMD guidance"
→ FDA Software as Medical Device 가이드라인
→ 관련 510(k) submission 예시
```

### Best Practice (모범 사례)

```
/aria knowledge "CAPA effectiveness verification"
→ CAPA 유효성 검증 모범 사례
→ 관련 Template, Form 추천
```

## 고급 기능

### 지식 그래프 탐색

관련 지식 항목을 그래프 형태로 탐색합니다:

```markdown
## 지식 그래프: "Risk Management"

[중심: KB-034 ISO 14971 Risk Management]
  ├─ [관련] KB-089 Risk Analysis Techniques
  ├─ [관련] KB-112 Risk Evaluation Criteria
  ├─ [파생] KB-156 SaMD Risk Considerations
  └─ [적용] KB-201 IEC 62366 Usability Risk

탐색:
1. KB-089: Risk Analysis Techniques (상세보기)
2. KB-112: Risk Evaluation Criteria (상세보기)
...
```

### 지식 요약 보고서

주제별 지식 요약 보고서를 생성합니다:

```
/aria knowledge "21 CFR 820" --summary

주제: 21 CFR 820 Quality System Regulation 요약
섹션:
  1. Subpart A - General Provisions
  2. Subpart B - Quality System Requirements
  3. Subpart C - Design Controls
  ...
관련 지식 항목: 42건
관련 문서: 15건
```

## 오류 처리

### 지식 항목 없음

```
검색 결과: "xyz abc"에 대한 지식 항목이 없습니다.

선택사항:
1. Context7에서 검색하여 Knowledge Base에 추가 (--auto-expand)
2. 검색어를 일반화하여 다시 검색
3. /aria search "xyz abc"으로 전체 검색
```

### Context7 검색 실패

```
안내: Context7에서 해당 주제를 찾을 수 없습니다.

제안:
1. 관련 키워드로 검색 (예: "validation" → "software validation")
2. 다른 라이브러리 검색 (예: FDA → ISO)
3. Google Workspace에서 문서 검색: /aria search "xyz abc" --source google
```

### Knowledge Base 업데이트 실패

```
오류: Knowledge Base 항목 업데이트에 실패했습니다.
원인: Notion API rate limit

해결 방법:
1. 1분 후 다시 시도하세요
2. 나중에 자동 재시도됩니다
3. 수동으로 Notion 페이지 편집 가능
```

## 사용 예시

### 예시 1: 규정 해석

```
/aria knowledge "ISO 13485 clause 8.5.2"

결과:
- ISO 13485 Clause 8.5.2: Nonconformity의 수정
- 요건: 불일치 발생 시 원인 파악, 수정 조치, 영향 평가
- 관련 CAPA Tracker: CAPA-2024-005
- 관련 문서: DOC-SOP-025 Nonconformity Procedure
```

### 예시 2: 모범 사례

```
/aria knowledge "design validation best practices"

결과:
- Design Validation 모범 사례 (KB-178)
- 내용: 사용자 요구사항 충족 확인, 실사용 조건 테스트
- 관련: 21 CFR 820.30(g), IEC 62366-1
- Template: DOC-TMP-011 Validation Protocol
```

### 예시 3: 자동 확장

```
/aria knowledge "MDR clinical evaluation requirements" --auto-expand

1. Knowledge Base 검색: 결과 없음
2. Context7 검색: EU MDR Annex XIV, MEDDEV 2.12/1
3. Knowledge Base 항목 생성:
   - ID: KB-XXX
   - Topic: "MDR Clinical Evaluation Requirements"
   - Content: [Context7 검색 결과]
4. 알림: "새 지식 항목 KB-XXX가 추가되었습니다"
```

## 완료 마커

조회 완료 시 `<aria:knowledge:complete results=N expanded=Y>` 마커를 추가합니다.
(N: 결과 수, Y: 자동 확장 여부)

## 참고

- Knowledge Base는 Notion DB로 중앙 관리됩니다
- Context7 검색 결과는 자동으로 캐싱됩니다 (TTL: 30일)
- 모든 지식 항목은 출처를 명시해야 합니다
- 신뢰도(Confidence)는 출처의 공식성에 따라 결정됩니다
- 주간 자동 업데이트로 최신 상태를 유지합니다
