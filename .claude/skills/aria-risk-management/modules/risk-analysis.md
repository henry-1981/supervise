# Risk Analysis Methods

의료기기 위험 분석 방법론.

## FMEA (Failure Mode and Effects Analysis)

### 개요

고장 모드 및 영향 분석 (FMEA)은 시스템의 각 구성 요소에 대해 잠재적 고장 모드를 식별하고 그 영향을 분석하는 체계적인 방법입니다.

### FMEA 절차

#### 1. FMEA 준비
- 분석 범위 정의
- FMEA 팀 구성
- 템플릿트 준비

#### 2. 시스템 구조 분석
- 기기를 하위 시스템/구성요소로 분해
- 기능 블록 다이어그램 작성

#### 3. 고장 모드 식별
- 각 구성요소별 잠재적 고장 모드 식별
- 고장 원인 분석
- 고장 영향 파악

#### 4. 위험 평가
- Severity (심각성): 1-10 척도
- Occurrence (발생빈도): 1-10 척도
- Detection (검출가능성): 1-10 척도

#### 5. RPN 계산
```
RPN (Risk Priority Number) = Severity × Occurrence × Detection
```

#### 6. 우선순위 결정
- RPN ≥ 100: 즉시 조치 필요
- 50 ≤ RPN < 100: 계획적 조치
- RPN < 50: 모니터링

#### 7. 경감 조치 수립
- 설계 변경
- 보호 장치 추가
- 검사 강화
- 예방 유지보전

#### 8. 재평가
- 경감 조치 후 재평가
- 새로운 RPN 계산
- 잔여 위험 수용성 확인

### FMEA 템플릿

| 항목 | 내용 |
|------|------|
| Component | 구성요소 |
| Function | 기능 |
| Failure Mode | 고장 모드 |
| Failure Effect | 고장 영향 |
| Severity | 심각성 (1-10) |
| Occurrence | 발생빈도 (1-10) |
| Detection | 검출가능성 (1-10) |
| RPN | 위험 우선순위 |
| Control Measures | 경감 조치 |
| Recommended Actions | 권장 조치 |

## FTA (Fault Tree Analysis)

### 개요

고장 트리 분석 (FTA)은 최종 위험 사건으로부터 근본 원인을 거슬러 올라가며 분석하는 하향식 방법입니다.

### FTA 절차

#### 1. Top Event 정의
- 분석할 최종 위험 사건 정의
- 예: Patient injury due to device failure

#### 2. Fault Tree 구성
- 논리 게이트 사용
  - AND 게이트: 모든 입력이 발생해야 출력 발생
  - OR 게이트: 입력 중 하나만 발생해도 출력 발생
- 계층별 원인 분석

#### 3. 정량적 분석 (옵션)
- 각 기본 사건의 발생 확률 할당
- 최종 사건 발생 확률 계산
- 중요도 (Criticality) 분석
- 최소 컷 세트 (Minimal Cut Set) 식별

#### 4. 결과 해석
- 주요 경로 식별
- 개선 기회 파악
- 경감 조치 우선순위 결정

### FTA 예시

```
                  [Patient Harm]
                         |
          ┌──────────────┴──────────────┐
          |                              |
    [Device Failure]              [User Error]
          |                              |
    ┌─────┴─────┐                  ┌─────┴─────┐
    |           |                  |           |
[Power Fail] [Sensor Fail]      [Misuse]   [Training Gap]
    |           |                  |           |
[Supplier]  [Design Defect]    [Labeling] [Manual]
```

## STA (Software Threat Analysis)

### 개요

소프트웨어 위협 분석 (STA)은 의료기기 소프트웨어에 대한 보안 위협을 식별하고 분석합니다.

### STA 절차 (IEC 62304)

#### 1. 소프트웨어 시스템 정의
- Software of Unknown Provenance (SOUP)
- Software of Known Provenance (SKP)
- Software of Unknown Vulnerability (SOUV)

#### 2. Threat Identification
- 악성 소프트웨어
- 데이터 무결성
- 비밀성 침해
- 가용성 저하

#### 3. Threat Analysis
- STRIDE 모델 (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege)
- Attack Tree Analysis
- Threat Modeling

#### 4. Security Control Measures
- 인증 및 권한 관리
- 데이터 암호화
- 보안 커뮤니케이션
- 정기 보안 업데이트

### Safety Class별 STA

| Class | 위협 분석 요구사항 |
|-------|---------------------|
| Class A | 기본 분석 |
| Class B | 상세 분석 + 문서화 |
| Class C | 엄격한 분석 + 검증 |

## 비교

| 방법 | 특징 | 장점 | 단점 |
|------|------|------|------|
| FMEA | 하향식, 구성요소 중심 | 체계적 | 조합 효과 분석 어려움 |
| FTA | 상향식, 사건 중심 | 논리적 분석 가능 | 전문 지식 필요 |
| STA | 소프트웨어 중심 | 보안 위협 식별 | 전문가 필요 |

## 참고 문헌

- IEC 60812:2006 - Analysis techniques for system reliability
- ISO 26262:2018 - Road vehicles functional safety
- NIST SP 800-30 - Risk assessment guide
