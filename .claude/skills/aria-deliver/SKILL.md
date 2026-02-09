---
name: aria-deliver
description: >
  ARIA Deliver Phase skill for final quality validation, format conversion,
  and deliverable distribution. Integrates Notion MCP for knowledge base sync
  and provides completion notifications.
license: Apache-2.0
compatibility: Designed for Claude Code with ARIA orchestrator
user-invocable: false
metadata:
  version: "1.0.0"
  category: "workflow"
  status: "active"
  updated: "2026-02-09"
  modularized: "true"
  tags: "aria, phase, deliver, quality, distribution"
  author: "ARIA Phase 2 Implementation Team"

progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

triggers:
  keywords: ["deliver", "finalize", "output", "distribute", "publish"]
  agents: ["orchestrator", "manager-quality", "manager-docs"]
  phases: ["deliver"]
---

# ARIA Deliver Phase Skill

## 개요 (Overview)

Deliver Phase는 Execute 단계에서 생성된 산출물을 최종 검증하고 배포하는 ARIA의 마지막 단계입니다.

**주요 기능:**
- VALID 5차원 최종 검증
- 문서 형식 변환 (Markdown → PDF/Word)
- 메타데이터 추가 (서명, 날짜, 버전)
- Notion MCP 자동 동기화
- 배포 채널 선택 및 전송
- 완료 알림 및 다음 단계 제시

## Deliver Phase 프로세스

```
┌──────────────────────────────────────┐
│ 1. 최종 검증 (Final Validation)     │
│    - VALID 5차원 모두 검증           │
│    - Verified: 인용 확인             │
│    - Accurate: 데이터 검증           │
│    - Linked: 추적성 확인             │
│    - Inspectable: 감사추적 확인      │
│    - Deliverable: 형식 확인          │
└────────────┬─────────────────────────┘
             │
┌────────────▼─────────────────────────┐
│ 2. 형식 변환 (Format Conversion)    │
│    - Markdown → PDF                  │
│    - Markdown → Word (.docx)         │
│    - 스타일 유지                     │
│    - 페이지 레이아웃 최적화          │
└────────────┬─────────────────────────┘
             │
┌────────────▼─────────────────────────┐
│ 3. 메타데이터 추가                   │
│    - 문서 제목, 버전                 │
│    - 작성자, 검토자, 승인자          │
│    - 생성일, 서명 필드               │
│    - 문서 ID, 분류 수준              │
└────────────┬─────────────────────────┘
             │
┌────────────▼─────────────────────────┐
│ 4. Notion 동기화 (Sync)             │
│    - 완성 문서 저장                  │
│    - 메타데이터 동기화               │
│    - 태그 할당                       │
│    - 링크 생성                       │
└────────────┬─────────────────────────┘
             │
┌────────────▼─────────────────────────┐
│ 5. 배포 (Distribution)              │
│    - 배포 채널 선택:                 │
│      • Notion (자동)                 │
│      • 이메일 (선택)                 │
│      • 로컬 저장 (선택)              │
│    - 배포 완료 로깅                  │
└────────────┬─────────────────────────┘
             │
┌────────────▼─────────────────────────┐
│ 6. 완료 알림 (Completion Notice)   │
│    - 사용자 알림                     │
│    - 품질 요약                       │
│    - 다음 단계 제시                  │
└──────────────────────────────────────┘
```

## 최종 품질 검증 (Quality Validation)

VALID 프레임워크 5차원 검증:

| 차원 | 검증 항목 | 기준 | 재시정 |
|------|---------|------|--------|
| **V**erified | 규제 출처 | 100% 인용 | 출처 추가 |
| **A**ccurate | 데이터 정확성 | 100% 검증됨 | 데이터 수정 |
| **L**inked | 추적성 | 요구사항↔증거 연결 | 연결 추가 |
| **I**nspectable | 감사추적 | 모든 결정 기록 | 기록 추가 |
| **D**eliverable | 형식 준수 | 제출 형식 충족 | 형식 조정 |

**최종 등급:**
- A (90-100%): 프로덕션 준비 완료
- B (80-89%): 경미한 수정 후 승인 가능
- C (70-79%): 중대 수정 필요
- F (<70%): 재작업 필요

## 배포 채널 (Distribution Channels)

### 1. Notion MCP (자동)

```yaml
Notion Sync:
  Database: "Completed Documents"
  Properties:
    - Title: 문서 제목
    - Status: "완료"
    - Quality Grade: "A/B/C"
    - Created Date: ISO 8601 형식
    - SPEC ID: 관련 SPEC
    - PDF Link: 저장된 파일 링크
    - Version: 문서 버전
  Tags:
    - 도메인 (FDA, EU MDR, MFDS)
    - 문서 유형 (510k, CER, Risk Assessment)
    - 완료 날짜
```

### 2. 이메일 (선택)

```yaml
Email Distribution:
  Recipients:
    - 사용자
    - 관련 이해관계자
    - 승인자
  Subject: "[완료] {작업명} - {품질등급}"
  Body:
    - 작업 요약
    - 배달 파일 링크 (Notion)
    - 품질 평가
    - 다음 단계
```

## 인수 조건 (Acceptance Criteria)

### AC-CMD-005: 최종 산출물 생성

```gherkin
Given: 워크플로우가 완료됨
When: /aria deliver 커맨드 실행
Then:
  ✅ 품질 검증이 통과
  ✅ 최종 문서가 생성됨
  ✅ 형식 변환이 완료됨
  ✅ 배포가 완료됨
```

**성공 기준:**
- 품질 검증이 100% 통과
- 최종 산출물이 기대를 충족
- 배포가 자동으로 완료
- 사용자 알림이 전송됨

## 관련 문서

- `.moai/specs/SPEC-ARIA-002/plan.md` - Deliver Phase 정의
- `.moai/specs/SPEC-ARIA-002/acceptance.md` - 인수 조건
- `aria-quality-valid` - VALID 프레임워크
- `aria-integration-notion` - Notion MCP 통합
