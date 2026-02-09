---
name: aria-knowledge-mfds
description: >
  MFDS (Ministry of Food and Drug Safety) 규정 전문 지식 스킬.
  Korea MDR (Medical Device Act), 의료기기 허가 절차,
  분류 규칙 등 한국 의료기기 규제에 대한 상세 지식을 제공합니다.

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
  tags: "mfds, korea-mdr, medical-device, korea, regulatory"
  context7-libraries: "korea-mdr, mfds-regulations"
  related-skills: "aria-domain-raqa, aria-knowledge-fda, aria-knowledge-eumdr"
  aliases: "korea-regulatory, mfds, korea-medical-device"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords:
    - "MFDS"
    "Korea MDR"
    "한국 의료기기"
    "식약처"
    "의료기기 허가"
    "MFDS 승인"
    "Korea classification"
  agents:
    - "expert-regulatory"
  phases:
    - "run"
  languages: []
---

# MFDS Regulations (Korea Medical Device Regulations)

대한민국 의료기기 규제에 대한 포괄적인 지식을 제공합니다.

## Korea MDR 개요

### Purpose (목적)

의료기기의 품질과 안전을 확보하고 국민 보건을 보호하기 위한 법률입니다.

### Key Laws

| 법률 | 내용 | 시행일 |
|------|------|--------|
| Medical Device Act | 의료기기법 | 2019-05-01 |
| Enforcement Rule | 시행령 | 2019-11-01 |
| Classification Rule | 분류 규칙 | 2019-11-01 |

## 의료기기 허가 절차

### 허가 절차 유형

| 등급 | 허가 대상 | 기관 | 심사 기간 |
|------|-----------|------|-----------|
| Class I | 저위험 기기 | MFDS | 15일 |
| Class II | 중간 위험 기기 | MFDS | 30일 |
| Class III | 고위험 기기 | MFDS | 60일 |
| Class IV | 고위험 기기 (신의학적 진단/치료) | MFDS | 90일 |

### 허가 절차 절차

```
┌─────────────────────────────────────────────────────────────┐
│              의료기기 허가 절차 프로세스                        │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌───────────────────┐
│ 1. 사전 준비        │ - 서류 준비, 임상/시체 데이터
└───────┬───────────┘
        │
        ▼
┌───────────────────────┐
│ 2. 신청서 제출        │ - MFDS 포털 신청, 서류 업로드
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│ 3. 서류 심사          │ - 형식 심사, completeness check
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│ 4. 보완 요청 (필요시) │ - 부족 서류 보완 요청
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│ 5. 기술 심사          │ - 기술 평가, 임상/시체 데이터 심사
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│ 6. 현장 심사          │ - 제조 시설 GMP 준수 여부 확인
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│ 7. 심사 결과 통보      │ - 허가/불불/보완 요청 결정
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│ 8. 허가증 발급         │ - 의료기기 허가증 발급
└───────────────────────┘
```

## 분류 규칙 (Classification Rules)

### 분류 원칙

의료기기는 4개 등급으로 분류됩니다:

| 등급 | 정의 | 예시 |
|------|------|------|
| Class I | 저위험 기기 | 안경대, 수술, 일반 의료기기 |
| Class II | 중간 위험 기기 | 진단기, 치료기, 모니터링 장치 |
| Class III | 고위험 기기 | 인공심장, 임플란트, 스�트 |
| Class IV | 최고위험 기기 | 신경회로 자극혈관 치료제, 심장박동매 |

### 분류 결정 트리

```
              의료기기 분류 결정 트리
                     │
         ┌─────────┴─────────┐
         │                   │
    Invasive?         Non-Invasive?
         │                   │
    ┌───┴───┐         ┌─────┴─────┐
    │       │         │           │
Used    Contact    Used       Body
with    Body   with     on     Surface
Body?   Surface?    Patient?    Only?
    │       │         │           │
    ┌───┴───┐   ┌───┴────┐   ┌───┴───┐
    │       │   │        │   │       │
Active  Passive  Life    Diagnostic  Therapeutic
Substance?   ?   Support?  ?    ?    ?
    │       │   │        │   │       │
    ┌───┴───┐   ┌───┴────┐   ┌───┴───┐ │
    │       │   │        │   │       │
    │   ┌───┴───┐┌──┴──┐   ┌──┴───┐ │
    │   │   │  ││    │   │    │  │
    │   │   │  ││    │   │    │  │
    │   │   │  ││    │   │    │  │
    └───┴───┴──┴┴────┴───┴────┴──┘
         │
         ▼
    [Classification]
```

### 분류별 요구사항

#### Class I

**요구사항**:
- 기술 문서
- 품질 시스템 (QMS) 준수 여부 확인 (외부 지정 가능)
- 사용 설명서 (IFU)

**예시**:
- 수술
- 안경대
- 일반 진단용 의료기기
- 차트

#### Class II

**요구사항**:
- 기술 문서
- 품질 시스템 (QMS) 준수 여부 확인
- 임상/시체 데이터 (필요시)
- 사용 설명서 (IFU)

**예시**:
- 진단기
- 치료기
- 모니터링 장치
- CT, MRI, X-ray

#### Class III

**요구사항**:
- 기술 문서
- 품질 시스템 (QMS) 준수 여부 확인
- 임상/시체 데이터 (필수)
- 사용 설명서 (IFU)
- 위험 분석 및 관리

**예시**:
- 인공심장
- 임플란트
- 스�트
- 혈관 조영제

#### Class IV

**요구사항**:
- 기술 문서
- 품질 시스템 (QMS) 준수 여부 확인
- 임상/시체 데이터 (필수)
- 사용 설명서 (IFU)
- 위험 분석 및 관리
- 임상시험 계획 승인

**예시**:
- 신경회로 자극혈관 치료제
- 심장박동매
- 조영개 조영제

## 허가 신청 서류

### 기본 서류

1. **의료기기 허가 신청서**
2. **사용자(설치자) 준수 서류**
   - 사업자등록증
   - 의료기기 제조/수입 판매업 허가증
   - 의료기기 유지관리사 허가증

3. **제품별 서류**
   - 기술 문서
   - 품질 매뉴얼(QMS) 관련 서류
   - 임상/시체 데이터
   - 사용 설명서 (IFU)

### 기술 문서 요구사항

| 항목 | 내용 | 비고 |
|------|------|------|
| 제품 개요 | 명칭, 모델, 형식, 구조 | KDFO 제품 특성 |
| 재료 명세서 | 재료명, 규격, 성능 | 시험성적서 |
| 설계도 | 제품 설계도, 회로도 | KDFO 설계 |
| 제조 방법 | 제조 공정 순서도 | GMP 준수 |
| 사용 방법 | 사용 설명서, 주의사항 | KDFO IFU |

### QMS 문서 요구사항

| 항목 | 내용 | 비고 |
|------|------|------|
| 품질 매뉴얼 | QMS 구성, 절차 | ISO 13485 준수 |
| GMP 준수 | 제조/품질 관리 | KGMP 준수 |
| 제품 설계 | DHF, DMR, DHR | KGMP 요구 |
| 위험 관리 | 위험 분석, 관리 계획 | ISO 14971 준수 |

## 임상/시체 데이터 요구사항

### 임상 데이터

**적용 대상**:
- Class II: 임상 데이터 권장
- Class III: 임상 데이터 필수
- Class IV: 임상 데이터 필수

**임상 데이터 유형**:
- 문헌 연구
- 임상 시험 (국외/국내)
- 동등성 평가

### 시체 데이터

**적용 대상**:
- Class III: 시체 데이터 권장 (필요 시)
- Class IV: 시체 데이터 필수

**시체 데이터 유형**:
- 동물 실험
- 시체 실험
- 시체 이용 연구

## 사용 설명서 (IFU) 요구사항

### 필수 항목

1. **제품 정보**
   - 제품명, 모델명
   - 제조사명
   - 제조일자

2. **적응증**
   - 적응 대상 질병
   - 효능/효과
   - 사용 방법

3. **구조/성분**
   - 구조/성분명
   - 규격/성분
   - 원재명

4. **사용 방법**
   - 사용 순서
   - 조작 방법
   - 사용 전 주의사항

5. **주의사항**
   - 금기 사항
   - 부작용 부작용
   - 상호작용

6. **저장 방법**
   - 보관 방법
   - 사용 기간
   - 폐기 방법

## GMP (의료기기 제조품질관리 기준)

### GMP 요구사항

| 항목 | 요구사항 | 비고 |
|------|----------|------|
| 품질 시스템 | 품질 매뉴얼 구축 | KGMP 준수 |
| 인력 | 교육, 훈련 | 직무 교육 |
| 시설 | 설비, 유지보수 | 설비 관리 |
| 자재 | 구매, 검사, 보관 | 자재 관리 |
| 제조 | 공정, 공정 관리 | 공정 검증 |
| 검사 | 입/공정 검사 | 검사 기록 |
| 출하 | 출하 검사 | 출하 기록 |
| 불량 | 불량 처리 | 리콜/폐기 |

## MFDS 포털

### 온라인 신청

**MFDS e-Submission System**: https://mfds.go.kr

**기능**:
- 온라인 신청서 제출
- 서류 업로드
- 진행 상황 조회
- 결과 확인

### 신청 절차

```
MFDS 포털 신청 절차
    │
    ▼
┌───────────────────┐
│ 1. 회원 가입         │ - 기관 회원 가입
└───────┬───────────┘
        │
        ▼
┌───────────────────────┐
│ 2. 온라인 신청      │ - 신청서 작성, 서류 업로드
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│ 3. 서류 심사          │ - 형식/내용 심사, 보완 요청
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│ 4. 기술 심사          │ - 기술 평가, 임상/시체 데이터 심사
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│ 5. GMP 현장 심사      │ - 제조 시설 GMP 준수 심사
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│ 6. 허가 결정          │ - 허가/불불/보완 요청
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│ 7. 허가증 발급         │ - 온라인 발급, 우편 송부
└───────────────────────┘
```

## Post-Market Surveillance

### PMS (Post-Market Surveillance)

**목적**: 시장 유통 의료기기 안전성 모니터링

**활동**:
1. 불만족 신고 접수
2. 이상 반응 보고
3. 안전성 정보 수집
4. 시장 조사

### PMCF (Post-Market Clinical Follow-up)

**목적**: 허가 후 임상 안전성/유효성 확인

**활동**:
1. 장기 안전성 모니터링
2. 임상 데이터 수집
3. 성능 유효성 확인
4. CER 업데이트

## 관련 법규

| 법규 | 내용 |
|------|------|
| Medical Device Act | 의료기기법 |
| Medical Device Enforcement Rule | 의료기기법 시행령 |
| Classification Rule | 의료기기 분류 규칙 |
| GMP Notification | 의료기기 제조품질관리 기준 |
| PMS Notification | 시판 후 관리 규정 |

## References

- Korea MFDS: https://mfds.go.kr
- Medical Device Act: Medical Device Act
- KGMP: Korea Good Manufacturing Practice
- ICH Q7: Good Manufacturing Practice

---

**Version**: 1.0.0
**Last Updated**: 2026-02-09
**Reference**: [Medical Device Act], [Korea MDR]
