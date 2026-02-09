---
name: aria-knowledge
description: >
  ARIA Knowledge command skill for knowledge base management with Notion MCP
  integration. Provides search, tagging, and synchronization functionality for
  completed work, regulatory guidelines, case studies, and best practices.
license: Apache-2.0
compatibility: Designed for Claude Code with ARIA orchestrator
user-invocable: false
metadata:
  version: "1.0.0"
  category: "workflow"
  status: "active"
  updated: "2026-02-09"
  modularized: "true"
  tags: "aria, knowledge, notion, search, tagging"
  author: "ARIA Phase 2 Implementation Team"

progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

triggers:
  keywords: ["knowledge", "kb", "search", "tag", "sync", "learn"]
  agents: ["orchestrator", "manager-project", "expert-researcher"]
  phases: ["brief", "execute", "deliver"]
---

# ARIA Knowledge Command Skill

## 개요 (Overview)

Knowledge 커맨드는 ARIA의 지식 베이스 관리 기능을 제공합니다. Notion MCP를 통해 완료된 작업, 규제 가이드라인, 사례 연구, 베스트 프랙티스를 체계적으로 관리합니다.

**주요 기능:**
- Notion 기반 지식 베이스 검색
- 자동 태깅 시스템
- 지식 기여 워크플로우
- 로컬 ↔ Notion 자동 동기화
- 지식 인덱싱 및 검색 최적화

## 지식 베이스 구조 (Knowledge Base Structure)

### Notion 데이터베이스 구조

```
ARIA Knowledge Base (Notion Workspace)
├── 📋 Completed Works (완료된 작업)
│  ├─ Document Title
│  ├─ Regulatory Domain (FDA/EU/MFDS)
│  ├─ Document Type (510k/CER/CAPA/etc)
│  ├─ Quality Grade (A/B/C)
│  ├─ Completion Date
│  ├─ Key Learning Points
│  └─ Reference Link

├── 📚 Regulatory Guidelines (규제 가이드라인)
│  ├─ Guideline Title
│  ├─ Issuing Authority (FDA/EMA/MFDS)
│  ├─ Effective Date
│  ├─ Key Requirements
│  ├─ Implementation Status
│  └─ Related Documents

├── 🔬 Case Studies (사례 연구)
│  ├─ Company/Product Name
│  ├─ Device Classification
│  ├─ Regulatory Pathway
│  ├─ Key Challenges
│  ├─ Lessons Learned
│  └─ Outcome

├── ⭐ Best Practices (베스트 프랙티스)
│  ├─ Practice Title
│  ├─ Category (Documentation/Quality/Risk/etc)
│  ├─ Description
│  ├─ When to Apply
│  ├─ Success Rate
│  └─ Example

└── 🏷️ Taxonomy (분류 체계)
   ├─ Regulatory Domain
   ├─ Document Type
   ├─ Quality Level
   └─ Subject Matter
```

## 커맨드 사용법 (Command Usage)

### 1. 지식 검색

```bash
/aria knowledge search "term"
/aria knowledge search "510(k) predicate device"
/aria knowledge search "CAPA root cause"
/aria knowledge search "risk assessment ISO 14971"
```

**검색 필터:**
```bash
/aria knowledge search "term" \
  --domain FDA              # 규제 도메인
  --type CAPA              # 문서 유형
  --quality A              # 품질 등급
  --language ko            # 언어
```

**검색 결과 예시:**
```
🔍 Search Results: "510(k) predicate device" (4 results)

1. ✅ [Grade A] Patient Monitor 510(k) Submission
   Domain: FDA | Date: 2026-01-15
   Highlights: Predicate selection strategy, Substantial equivalence...
   Link: notion://...

2. ✅ [Grade A] Blood Glucose Meter 510(k)
   Domain: FDA | Date: 2025-11-20
   Highlights: Predicate device comparison, Risk assessment...
   Link: notion://...

3. ⭐ Best Practice: Predicate Device Selection
   Category: FDA Regulatory | Success Rate: 95%
   Key Points: Market research, FDA 510(k) list, Equivalence factors...
   Link: notion://...

4. 📚 FDA Guidance: Substantial Equivalence
   Authority: FDA | Date: 2023-04 | Status: Current
   Requirements: Comparison methodology, Documentation...
   Link: notion://...
```

### 2. 태그 기반 검색

```bash
/aria knowledge tags                    # 전체 태그 목록
/aria knowledge tag "FDA"              # FDA 관련 모든 문서
/aria knowledge tag "CAPA" "quality"   # CAPA 관련 품질 문서
```

**자동 태그 생성:**
- 규제 도메인: FDA, EU MDR, MFDS
- 문서 유형: 510k, PMA, CER, CAPA, Risk, Design Control
- 품질 등급: A, B, C
- 주제: Predicate Device, Substantial Equivalence, Clinical Data
- 언어: English, 한국어

### 3. 최신 콘텐츠 조회

```bash
/aria knowledge recent                 # 최근 추가된 문서
/aria knowledge trending              # 인기 검색어
/aria knowledge recommend             # 추천 학습 자료
```

### 4. 지식 기여

```bash
/aria knowledge contribute "title" "path/to/document"
/aria knowledge contribute "Patient Monitor 510k" "./completed/pm_510k.pdf"
```

**기여 프로세스:**
1. 문서 제출
2. 메타데이터 추가 (카테고리, 학습 포인트 등)
3. 검토 (quality-manager 승인)
4. Notion에 자동 발행

### 5. Notion 동기화

```bash
/aria knowledge sync                  # Notion과 동기화
/aria knowledge sync --full           # 전체 재동기화
/aria knowledge sync --schedule daily # 일일 자동 동기화
```

## 자동 태깅 시스템 (Auto-Tagging)

AI 기반 자동 태깅:

```python
Auto-Tagging Logic:
  1. 문서 제목 분석 → 도메인 + 유형 추출
  2. 문서 내용 분석 → 주제 태그 추출
  3. 메타데이터 분석 → 품질 등급 추론
  4. 사용자 확인 → 수정 후 최종 태그

예시:
Input: "Patient Monitor 510(k) Submission with Predicate Device Comparison"
Output Tags:
  - Domain: FDA
  - Type: 510k
  - Subject: Predicate Device, Substantial Equivalence
  - Language: English
  - Quality: (사용자 입력)
```

## Notion ↔ 로컬 동기화

```
로컬 파일 시스템          Notion 클라우드
    ↓↑                    ↓↑
   파일                  데이터베이스
    ├─ documents/       ← completed_works
    ├─ guidelines/      ← regulatory_guidelines
    └─ case_studies/    ← case_studies

동기화 주기:
- 자동: 일일 (선택)
- 수동: /aria knowledge sync
- 트리거: 새 문서 완료 시 자동
```

## 인수 조건 (Acceptance Criteria)

### AC-MCP-003: 지식 베이스 동기화

```gherkin
Given: 새 문서가 생성됨
When: Notion MCP로 동기화
Then:
  ✅ 문서가 Notion에 생성됨
  ✅ 메타데이터가 포함됨
  ✅ 태그가 할당됨
  ✅ 링크가 생성됨
```

**성공 기준:**
- 동기화가 자동으로 완료
- 데이터가 정확히 전송
- 형식이 유지됨
- 오류 처리가 적절

## 관련 문서

- `.moai/specs/SPEC-ARIA-002/plan.md` - Knowledge 커맨드 정의
- `.moai/specs/SPEC-ARIA-002/acceptance.md` - AC-MCP-003 기준
- `aria-integration-notion` - Notion MCP 통합
