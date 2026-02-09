---
name: aria-capa-process
description: >
  의료기기 CAPA(Corrective and Preventive Action) 프로세스 전문 스킬.
  ISO 13485 Section 8.5.2, 8.5.3, 8.5.4, 10.2 요구사항을 기반으로
  불일치 관리, 근본 원인 분석, 수정/예방 조치, 효성 검증 등
  CAPA 전 과정을 지원합니다.

license: Apache-2.0
compatibility: Designed for Claude Code
allowed-tools: Read Grep Glob Bash mcp__context7__resolve-library-id mcp__context7__get-library-docs
user-invocable: false

metadata:
  version: "1.0.0"
  category: "domain"
  status: "active"
  updated: "2026-02-09"
  modularized: "true"
  tags: "capa, corrective-action, preventive-action, nonconformance, root-cause, iso13485"
  context7-libraries: "iso-13485"
  related-skills: "aria-domain-raqa, aria-risk-management"
  aliases: "capa-process, quality-improvement, corrective-preventive"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords:
    - "corrective action"
    - "preventive action"
    - "CAPA"
    - "nonconformance"
    - "root cause"
    - "5 whys"
    - "fishbone"
    - "effectiveness check"
    - "ISO 13485 8.5.2"
    - "ISO 13485 10.2"
  agents:
    - "expert-capa"
  phases:
    - "run"
  languages: []
---

# CAPA Process (Corrective and Preventive Action)

의료기기 품질 관리의 핵심인 CAPA 프로세스에 대한 포괄적인 지식을 제공합니다.

## CAPA 개요

### Purpose (목적)

CAPA는 불일치(Nonconformance)를 식별, 분석, 해결하고 재발을 방지하기 위한 체계적인 접근 방법입니다:

- **Corrective Action (수정 조치)**: 기존 불일치의 근본 원인 제거
- **Preventive Action (예방 조치)**: 잠재적 불일치 예방

### Regulatory Requirements (규제 요구사항)

- **ISO 13485:2016 Section 8.5.2**: Nonconforming Product Control
- **ISO 13485:2016 Section 8.5.3**: Corrective Action
- **ISO 13485:2016 Section 8.5.4**: Preventive Action
- **ISO 13485:2016 Section 10.2**: Nonconformance and CAPA
- **FDA 21 CFR 820.100**: Corrective and Preventive Action

## CAPA 프로세스 흐름

```
불일치 식별 → 문서화 → 근본 원인 분석 → 수정 조치 → 예방 조치 → 구현 → 효성 검증 → 마감
     │           │          │              │           │        │         │        │
     ▼           ▼          ▼              ▼           ▼        ▼         ▼        ▼
  [1]        [2]         [3]            [4]          [5]      [6]      [7]      [8]
```

### 1단계: 불일치 식별 (Identification)

- 제품 불일치: 기능/성능 불만족
- 프로세스 불일치: 절차 미준수
- 문서 불일치: 기록/문서 누락
- 공급업자 불일치: 자재/부품 불량

### 2단계: 문서화 (Documentation)

불일치 내용을 체계적으로 기록:
- 발생 일시
- 불일치 설명
- 영향 평가
- 심각도 분류

### 3단계: 근본 원인 분석 (Root Cause Analysis)

불일치의 근본 원인을 식별:
- 5 Whys 기법
- Fishbone diagram
- FMEA 분석

### 4단계: 수정 조치 (Corrective Action)

근본 원인을 제거하는 조치:
- 즉시 수정 (Immediate correction)
- 근본 원인 수정 (Root cause fix)
- 시스템 개선 (Systemic fix)

### 5단계: 예방 조치 (Preventive Action)

재발 방지를 위한 조치:
- 프로세스 개선
- 교육 강화
- SOP 업데이트
- 설계 변경

### 6단계: 구현 (Implementation)

계획된 조치를 실행:
- 책임자 할당
- 목표일 설정
- 진행 모니터링

### 7단계: 효성 검증 (Effectiveness Verification)

조치의 유효성을 확인:
- 30-90일 모니터링
- 재발 여부 확인
- 데이터 분석

### 8단계: 마감 (Closure)

CAPA 프로세스 완료:
- 효성 확인
- 문서화 완료
- 승인 및 마감

## 불일치 분류 (Nonconformance Classification)

### 심각도 등급 (Severity Levels)

| 등급 | 설명 | 예시 | CAPA 필수 |
|------|------|------|-----------|
| Critical | 환자 안전에 심각한 영향 | 치명적 고장, 안전 위반 | 즉시 CAPA |
| Major | 제품 성능에 영향 | 기능 불만족, 사양 위반 | CAPA 필수 |
| Minor | 문서/절차상 미흡 | 기록 오류, 절차 미준수 | CAPA 권장 |

### 불일치 유형 (Nonconformance Types)

1. **Product Nonconformance**
   - Functional failure
   - Performance deficiency
   - Cosmetic defect
   - Safety issue

2. **Process Nonconformance**
   - Procedure deviation
   - Equipment malfunction
   - Training gap
   - Resource constraint

3. **Documentation Nonconformance**
   - Missing record
   - Incomplete data
   - Incorrect specification
   - Unauthorized change

4. **Supplier Nonconformance**
   - Component defect
   - Late delivery
   - Specification deviation
   - Certification issue

## 근본 원인 분석 (Root Cause Analysis)

### 5 Whys 기법

질문을 5번 반복하여 근본 원인을 찾는 방법입니다.

#### 절차

1. **Why 1**: 표면 문제 정의
2. **Why 2**: 1차 원인 분석
3. **Why 3**: 2차 원인 분석
4. **Why 4**: 3차 원인 분석
5. **Why 5**: 근본 원인 도출

#### 예시: 센서 교정 실패

| 단계 | Why 질문 | 답변 | 분석 |
|------|----------|------|------|
| Why 1 | 센서 교정이 왜 실패했나? | 기준값 벗어남 | 표면 문제 |
| Why 2 | 기준값이 왜 벗어났나? | Reference 표준 만료됨 | 1차 원인 |
| Why 3 | Reference 표준이 왜 만료되었나? | 추적 시스템 없음 | 2차 원인 |
| Why 4 | 추적 시스템이 왜 없나? | 프로세스 정의되지 않음 | 3차 원인 |
| Why 5 | 프로세스가 왜 정의되지 않았나? | SOP 부재 | **근본 원인** |

### Fishbone Diagram (Ishikawa Diagram)

어류의 가능한 원인을 시스템적으로 분류합니다.

#### 5M 카테고리

1. **Man (사람)**
   - 교육 부족
   - 자격 미달
   - 피로
   - 실수

2. **Machine (기계)**
   - 장비 노후
   - 유지보수 부족
   - 설정 오류
   - 정비 불량

3. **Material (자재)**
   - 원자재 불량
   - 사양 위반
   - 저장 부적절
   - 혼합 오류

4. **Method (방법)**
   - 절차 불충분
   - 표준 미준수
   - 프로세스 모호
   - 단계 누락

5. **Environment (환경)**
   - 온도/습도
   - 조명
   - 진동/소음
   - 청결 상태

#### Fishbone 예시

```
                 센서 교정 실패
                       │
        ┌──────────────┼──────────────┐
        │              │              │
     People        Method        Equipment
        │              │              │
   ┌─────┴─────┐  ┌───┴────┐   ┌───┴────┐
   │           │  │        │   │        │
 Training   Fatigue  SOP    Timing  Calibration  Maintenance
```

## 수정 조치 vs 예방 조치

### 비교

| 구분 | 수정 조치 (Corrective) | 예방 조치 (Preventive) |
|------|------------------------|------------------------|
| 목적 | 기존 문제 해결 | 잠재적 문제 예방 |
| 대상 | 이미 발생한 불일치 | 발생 가능한 불일치 |
| 시점 | 반응적 (Reactive) | 예방적 (Proactive) |
| 범위 | 특정 이슈 | 시스템 전체 |
| 예시 | 불량품 교체, 재작업 | 프로세스 개선, 교육 |

### 수정 조치 (Corrective Action)

**목표**: 근본 원인을 제거하여 불일치 재발 방지

**단계**:
1. 즉시 수정 (Immediate Correction)
   - 불량품 격리
   - 대체품 제공
   - 프로세스 일시 중단

2. 근본 원인 수정 (Root Cause Fix)
   - 원인 제거
   - 시스템 개선
   - 절차 변경

3. 검증 (Verification)
   - 수정 조치 확인
   - 효과 입증

### 예방 조치 (Preventive Action)

**목표**: 유사 불일치를 예방하기 위한 시스템적 조치

**단계**:
1. 잠재적 위험 식별
   - 유사 프로세스 검토
   - FMEA 분석
   - 트렌드 분석

2. 예방 조치 계획
   - SOP 업데이트
   - 교육 프로그램
   - 설계 개선

3. 구현 및 검증
   - 조치 실행
   - 효과 모니터링

## 효성 검증 (Effectiveness Verification)

### 검증 기간

- **단기**: 30-90일 (구현 직후)
- **장기**: 6-12개월 (지속적 모니터링)

### 검증 방법

1. **모니터링 (Monitoring)**
   - 프로세스 지표
   - 품질 지표
   - 트렌드 분석

2. **감사 (Audit)**
   - 내부 감사
   - 프로세스 검토
   - 준수 확인

3. **데이터 분석 (Data Analysis)**
   - 불일치율
   - 고객 불만
   - 현장 불량

### 성공 기준

| 기준 | 성공 | 부분적 성공 | 실패 |
|------|------|-------------|------|
| 재발 | 없음 | 감소 | 지속 |
| 지표 | 개선됨 | 약간 개선 | 변화 없음 |
| 새로운 이슈 | 없음 | 일부 발생 | 지속 발생 |

## CAPA 추이 분석 (Trend Analysis)

### 분석 지표

1. **부서별 CAPA 발생**
   - 생산
   - 품질
   - R&D
   - 공급망

2. **유형별 CAPA 발생**
   - 제품 불일치
   - 프로세스 불일치
   - 문서 불일치
   - 공급업자 불일치

3. **심각도별 CAPA 발생**
   - Critical
   - Major
   - Minor

4. **기간별 CAPA 발생**
   - 월별 추이
   - 분기별 추이
   - 연간 추이

### Management Review 보고서

CAPA 추이는 Management Review에 포함됩니다 ([ISO 13485:2016 Section 9.3]):

- CAPA 발생 추이
- CAPA 완료율
- 반복 불일치 분석
- 효성 검증 결과
- 개선 기회 식별

## CAPA 프로세스 관리

### CAPA Tracker

CAPA Tracker는 모든 CAPA를 추적하는 Notion Database입니다.

#### 주요 필드

| 필드 | 타입 | 설명 |
|------|------|------|
| CAPA ID | 자동 생성 | 고유 식별자 |
| Issue Date | 날짜 | 발생 일시 |
| Problem | 텍스트 | 문제 설명 |
| Type | 선택 | 불일치 유형 |
| Severity | 선택 | 심각도 |
| Root Cause | 텍스트 | 근본 원인 |
| Corrective Action | 텍스트 | 수정 조치 |
| Preventive Action | 텍스트 | 예방 조치 |
| Status | 선택 | 상태 |
| Target Date | 날짜 | 목표일 |
| Completion Date | 날짜 | 완료일 |
| Effectiveness | 선택 | 효성 검증 |

### Relations 설정

- **Risk Register**: CAPA가 위험과 관련된 경우
- **Document Registry**: CAPA로 변경된 문서
- **Supplier**: 공급업자 관련 불일치

## CAPA Best Practices

### 1. 신속한 대응

- 불일치 발견 즉시 보고
- 24시간内 문서화
- 48시간内 근본 원인 분석 개시

### 2. 철저한 분석

- 5 Whys 깊이 유지
- 데이터 기반 결정
- 객관적 근거 확보

### 3. 시스템적 해결

- 증상 해결 NO
- 근본 원인 해결 YES
- 예방 조치 필수

### 4. 지속적 모니터링

- 90일간 재발 확인
- 데이터로 효성 입증
- 필요 시 재평가

## Common Mistakes

### 1. 수정과 수정 조치 혼동

- **Error**: 즉시 수정만 하고 근본 원인 분석 생략
- **Fix**: 두 단계 모두 수행

### 2. 예방 조치 생략

- **Error**: 수정 조치만 하고 예방 조치 생략
- **Fix**: 항상 예방 조치 포함

### 3. 불충분한 효성 검증

- **Error**: 구현 직후 효성 확인 후 종료
- **Fix**: 최소 90일 모니터링

### 4. 문서화 부족

- **Error**: 구현 위주, 문서화 소홀
- **Fix**: 철저한 기록 유지

---

## Modules

자세한 내용은 각 모듈을 참조하세요:

- `modules/root-cause-analysis.md` - 근본 원인 분석 상세 가이드
- `modules/corrective-action.md` - 수정 조치 상세 가이드
- `modules/preventive-action.md` - 예방 조치 상세 가이드
- `modules/effectiveness-check.md` - 효성 검증 상세 가이드

---

**Version**: 1.0.0
**Last Updated**: 2026-02-09
**Reference**: [ISO 13485:2016] Sections 8.5.2, 8.5.3, 8.5.4, 10.2
