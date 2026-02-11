# ACCEPTANCE-ARIA-003: 인수 기준

## TAG BLOCK

```yaml
SPEC_ID: SPEC-ARIA-003
ACCEPTANCE_ID: ACCEPTANCE-ARIA-003
STATUS: Planned
TYPE: Functional & Quality
APPROVER: ARIA Quality Team
CREATED: 2026-02-09
LANGUAGE: ko
```

## 개요 (Overview)

본 문서는 SPEC-ARIA-003의 인수 기준을 정의합니다. Given-When-Then 형식의 시나리오 기반 테스트와 VALID 품질 프레임워크 검증을 포함합니다.

## 에이전트별 인수 기준

### AC-1: expert-regulatory 에이전트

#### AC-1.1: 규제 전략 분석

**Given:** 사용자가 "미국 시장 진입을 위한 규제 전략"을 요청
**When:** expert-regulatory 에이전트가 요청 수신
**Then:**
- [ ] FDA 510(k) vs PMA 경로 분석 제공
- [ ] 결정 트리 (Decision Tree) 시각화
- [ ] 모든 규제 주장에 [FDA 21 CFR 섹션] 형식 인용
- [ ] 타임라인 추정 (510(k): ~3-6개월, PMA: ~6-12개월)
- [ ] 사용자 요금 계산 (510(k): ~$20K, PMA: ~$350K)

#### AC-1.2: 복수국 시장 요구사항 매트릭스

**Given:** 사용자가 "미국, 유럽, 한국 동시 진입" 요청
**When:** expert-regulatory 에이전트가 요청 수신
**Then:**
- [ ] 국가별 요구사항 비교표 생성
- [ ] FDA: 510(k) vs PMA, QSR (21 CFR 820)
- [ ] EU: CE Marking, MDR 2017/745, Technical File
- [ ] Korea: MFDS 승인, Korea MDR, Class별 요구사항
- [ ] 공통 요구사항: ISO 13485 QMS
- [ ] 차이점 하이라이트 (예: 임상 데이터 요구사항)

#### AC-1.3: 규정 변경 영향도 분석

**Given:** EU MDR 2017/745 개정안 발효
**When:** expert-regulatory 에이전트가 변경사항 감지
**Then:**
- [ ] 영향받는 기술 문서 파일 목록 제공
- [ ] Annex I Essential Requirements 변경사항 식별
- [ ] Clinical Evaluation Report 업데이트 필요성 확인
- [ ] Technical Documentation Structure 변경사항 요약
- [ ] 마감일까지 업데이트 계획 제안

#### AC-1.4: 규정 원문 인용 (Verified)

**Given:** 사용자가 "FDA Design Control 요구사항" 요청
**When:** expert-regulatory 에이전트가 응답 생성
**Then:**
- [ ] 모든 요구사항에 [FDA 21 CFR 820.30] 형식 인용
- [ ] Context7 MCP로 규정 원문 대조 검증
- [ ] 인용 형식 정확성 검증 (Standard, Section, Subsection)
- [ ] 만료된 규정 사용 방지

#### AC-1.5: 최신 규정 반영 (Accurate)

**Given:** FY 2026 FDA 사용자 요금 변경
**When:** expert-regulatory 에이전트가 요금 계산
**Then:**
- [ ] 최신 FY 요금 반영 (예: 510(k) FY2026 요금)
- [ ] Federal Register 출처 인용
- [ ] Small Business fee减免 정보 제공
- [ ] 요금 변경일 명시

### AC-2: expert-standards 에이전트

#### AC-2.1: 표준 해석

**Given:** 사용자가 "ISO 13485 Section 8.5.2 수정 조치" 요청
**When:** expert-standards 에이전트가 요청 수신
**Then:**
- [ ] 조항별 상세 분석 제공
- [ ] 적용 범위 (Scope) 설명
- [ ] 문서화 요구사항 (Documentation requirements)
- [ ] 증거 자료 (Evidence) 목록
- [ ] 관련 조항 참조 (예: Section 10.2 CAPA)
- [ ] [ISO 13485:2016 8.5.2] 형식 인용

#### AC-2.2: 표준 충돌 해결

**Given:** ISO 14971 위험관리 vs IEC 62304 소프트웨어 안전 충돌
**When:** expert-standards 에이전트가 충돌 감지
**Then:**
- [ ] 충돌 지점 명확히 식별
- [ ] 규제 계층 구조 (Regulatory Hierarchy) 기반 우선순위 제안
- [ ] 위험관리 우선 (Risk management takes precedence)
- [ ] 통합 해결책 제시 (Integrated approach)
- [ ] 관련 규제 기관 가이드라인 인용 (IMDRF, FDA guidance)

#### AC-2.3: ISO 13485 인증 체크리스트

**Given:** 사용자가 "ISO 13485:2016 인증 준비" 요청
**When:** expert-standards 에이전트가 요청 수신
**Then:**
- [ ] CB (Certification Body) 문서 요구사항 목록
- [ ] Quality Manual 포함 항목 체크리스트
- [ ] Procedures (SOPs) 필수 목록
- [ ] Records & Forms 필수 목록
- [ ] Stage 1 audit 준비 항목
- [ ] Stage 2 audit 준비 항목
- [ ] [ISO 13485:2016] 모든 클라우스 참조

#### AC-2.4: IEC 62304 Safety Class 분석

**Given:** SaMD (Software as Medical Device) 요청
**When:** expert-standards 에이전트가 Safety Class 분석
**Then:**
- [ ] Class A (No injury or damage) 정의 및 예시
- [ ] Class B (Non-serious injury) 정의 및 예시
- [ ] Class C (Death or serious injury) 정의 및 예시
- [ ] Safety Class 결정 트리 제공
- [ ] 각 Class별 문서화 요구사항
- [ ] [IEC 62304:2006/amd1:2010] 형식 인용

#### AC-2.5: 표준 버전 명시 (Verified)

**Given:** 사용자가 표준 인용 요청
**When:** expert-standards 에이전트가 응답 생성
**Then:**
- [ ] 모든 표준에 [ISO 13485:2016] 형식 버전 명시
- [ ] 만료된 표준 사용 시 경고 표시
- [ ] 최신 버전 제안 (예: ISO 14971:2019 vs ISO 14971:2007)
- [ ] Context7 MCP로 최신 버전 검증

### AC-3: expert-risk 에이전트

#### AC-3.1: ISO 14971 위험관리 절차

**Given:** 새로운 의료기기 위험 평가 요청
**When:** expert-risk 에이전트가 요청 수신
**Then:**
- [ ] 위험 식별 (Risk Identification) 목록
- [ ] 위험 추정 (Risk Estimation) - Severity, Probability
- [ ] 위험 평가 (Risk Evaluation) - Risk Index, Acceptability
- [ ] 위험 경감 (Risk Control) - Inherent safety, Protective measures, Information for safety
- [ ] 잔여 위험 평가 (Residual Risk Evaluation)
- [ ] 각 단계별 [ISO 14971:2019] 섹션 인용

#### AC-3.2: 위험-이익 분석 (Risk-Benefit Analysis)

**Given:** 위험이 허용 불가능 수준 (Unacceptable)
**When:** expert-risk 에이전트가 평가
**Then:**
- [ ] Clinical benefits 명확히 정량화
- [ ] Risks 정량화 (Severity, Probability)
- [ ] Benefit-Renefit Ratio 계산
- [ ] ALARP (As Low As Reasonably Practicable) 원칙 적용
- [ ] Sequential Thinking MCP로 체계적 분석
- [ ] 근거 문서화 (Inspectable)

#### AC-3.3: Risk Register Notion DB 동기화 (Linked)

**Given:** 새로운 위험 식별
**When:** expert-risk 에이전트가 위험 등록
**Then:**
- [ ] Risk Register Notion DB page 자동 생성
- [ ] 필드 자동 채움 (Risk ID, Hazard, Harm, Severity, Probability)
- [ ] Risk Index 자동 계산 (Severity × Probability)
- [ ] Risk Acceptability 평가 (Acceptable, ALARP, Unacceptable)
- [ ] Relations: CAPA Tracker (if applicable)

#### AC-3.4: FMEA 템플릿 완전성

**Given:** FMEA (Failure Mode and Effects Analysis) 요청
**When:** expert-risk 에이전트가 템플릿 생성
**Then:**
- [ ] Failure Mode 컬럼
- [ ] Failure Effect 컬럼
- [ ] Failure Cause 컬럼
- [ ] Severity (1-10) 컬럼
- [ ] Probability (1-10) 컬럼
- [ ] Detection (1-10) 컬럼
- [ ] RPN (Risk Priority Number) 자동 계산 (S × P × D)
- [ ] Control Measures 컬럼
- [ ] Recommended Actions 컬럼
- [ ] [ISO 14971:2019 Annex C] 참조

### AC-4: expert-design-control 에이전트

#### AC-4.1: DHF (Design History File) 구조 생성

**Given:** 새로운 설계 프로젝트 개시
**When:** expert-design-control 에이전트가 요청 수신
**Then:**
- [ ] DHF 템플릿 생성 (FDA 21 CFR 820.30 기반)
- [ ] Design Plan 섹션
- [ ] Design Input 섹션 (Requirements)
- [ ] Design Output 섹션 (Specifications)
- [ ] Design Review 섹션
- [ ] Design Verification 섹션
- [ ] Design Validation 섹션
- [ ] Design Transfer 섹션
- [ ] Design Changes 섹션
- [ ] 모든 섹션에 [FDA 21 CFR 820.30] 인용

#### AC-4.2: 설계 입력-추적성 매트릭스 (Linked)

**Given:** 설계 요구사항 정의
**When:** expert-design-control 에이전트가 추적성 생성
**Then:**
- [ ] Design Input → Design Output 링크
- [ ] Design Output → Verification 링크
- [ ] Verification → Validation 링크
- [ ] 양방향 추적성 확보
- [ ] Notion Document Registry에 동기화
- [ ] 고립 문서 (Orphaned document) 없음

#### AC-4.3: DMR (Device Master Record) 관리

**Given:** 설계 검증(Verification) 완료
**When:** expert-design-control 에이전트가 DMR 업데이트
**Then:**
- [ ] DMR 관련 섹션 자동 업데이트
- [ ] Production specifications 반영
- [ ] Quality assurance procedures 반영
- [ ] Packaging and labeling specifications 반영
- [ ] [FDA 21 CFR 820.181] 인용

#### AC-4.4: DHR (Device History Record) 생성

**Given:** 설계 이관(Design Transfer) 완료
**When:** expert-design-control 에이전트가 DHR 생성
**Then:**
- [ ] Production lot 추적용 DHR 생성
- [ ] Manufacturing dates 포함
- [ ] Quantities produced 포함
- [ ] Acceptance records 포함
- [ ] Primary identification label 포함
- [ ] [FDA 21 CFR 820.184] 인용

### AC-5: expert-capa 에이전트

#### AC-5.1: CAPA 절차 자동 개시

**Given:** Non-conformance report 제출
**When:** expert-capa 에이전트가 요청 수신
**Then:**
- [ ] CAPA 절차 4단계 자동 개시
  1. 근본 원인 분석 (Root Cause Analysis)
  2. 수정 조치 (Corrective Action)
  3. 예방 조치 (Preventive Action)
  4. 효성 검증 (Effectiveness Check)
- [ ] CAPA Tracker Notion DB page 자동 생성
- [ ] Due date 자동 설정 (30일 이내)
- [ ] Responsible Person 할당

#### AC-5.2: 5 Whys 근본 원인 분석

**Given:** Quality issue 발생
**When:** expert-capa 에이전트가 근본 원인 분석
**Then:**
- [ ] 5단계 왜(Why) 질문 자동 생성
  1. Why: 문제 발생 (Surface problem)
  2. Why: 1차 원인 (First cause)
  3. Why: 2차 원인 (Underlying cause)
  4. Why: 3차 원인 (Systemic cause)
  5. Why: 근본 원인 (Root cause)
- [ ] 각 단계별 답변 필드 제공
- [ ] 근본 원인 도출 시 Corrective Action 제안

#### AC-5.3: CAPA Tracker Notion DB 동기화 (Linked)

**Given:** CAPA 생성
**When:** expert-capa 에이전트가 CAPA 등록
**Then:**
- [ ] CAPA Tracker Notion DB page 자동 생성
- [ ] 필드 자동 채움 (CAPA ID, Issue Date, Problem Description, Root Cause)
- [ ] Relations: Risk Register (if applicable)
- [ ] Relations: Document Registry (related SOPs)
- [ ] Due date alerts 설정

#### AC-5.4: CAPA 추세 분석

**Given:** CAPA 데이터 10건 이상 축적
**When:** expert-capa 에이전트가 추세 분석 요청
**Then:**
- [ ] 부서별 CAPA 발생 추이 (차트)
- [ ] 유형별 CAPA 발생 추이 (차트)
- [ ] 기간별 CAPA 발생 추이 (차트)
- [ ] Management Review 보고서 자동 생성
- [ ] [ISO 13485:2016 Section 10] 인용

#### AC-5.5: CAPA 효성 검증

**Given:** CAPA 마감일 도래
**When:** expert-capa 에이전트가 효성 검증
**Then:**
- [ ] Effectiveness Verification checklist 제공
- [ ] 재발 여부 확인 (90일 이내)
- [ ] 미준비 시 재평가 요구
- [ ] 효성 확인 시 CAPA close-out

### AC-6: expert-clinical 에이전트

#### AC-6.1: CER (Clinical Evaluation Report) 작성

**Given:** CE Marking을 위한 임상 평가 요청
**When:** expert-clinical 에이전트가 요청 수신
**Then:**
- [ ] MDR Annex XV 요구사항 기반 CER 템플릿 생성
- [ ] Section 1: Scope and device identification
- [ ] Section 2: Clinical evaluation approach
- [ ] Section 3: Clinical data
- [ ] Section 4: Appraisal of clinical data
- [ ] Section 5: Clinical evaluation report
- [ ] Section 6: Conclusions
- [ ] 각 섹션별 [MDR Annex XV] 인용

#### AC-6.2: 임상 문헌 검색 (PRISMA)

**Given:** Clinical evidence 수집 요청
**When:** expert-clinical 에이전트가 문헌 검색
**Then:**
- [ ] PRISMA flow diagram 생성
- [ ] Identification: PubMed, Cochrane, ClinicalTrials.gov 검색
- [ ] Screening: 제목/초록 필터링
- [ ] Eligibility: 전문 기준 적용
- [ ] Included: 최종 포함 문헌 목록
- [ ] [PRISMA 2020] 가이드라인 준수

#### AC-6.3: 유사 장치 분석 (Equivalence)

**Given:** Predicate device 식별
**When:** expert-clinical 에이전트가 유사성 분석
**Then:**
- [ ] Technical equivalence 체크리스트
- [ ] Biological equivalence 체크리스트
- [ ] Clinical equivalence 체크리스트
- [ ] Equivalence decision tree 제공
- [ ] [MDR Annex IX] 인용

#### AC-6.4: PMCF (Post-Market Clinical Follow-up) 계획

**Given:** PMS 데이터 신호 감지
**When:** expert-clinical 에이전트가 PMCF 필요성 확인
**Then:**
- [ ] PMCF study plan 생성
- [ ] Study objectives 정의
- [ ] Study design (Prospective, Retrospective)
- [ ] Sample size calculation
- [ ] Data collection methods
- [ ] Analysis plan
- [ ] [MDR Annex XIV] 인용

### AC-7: expert-submission 에이전트

#### AC-7.1: 510(k) 제출 준비

**Given:** 510(k) submission 준비 요청
**When:** expert-submission 에이전트가 요청 수신
**Then:**
- [ ] eCopy format 문서 구조 생성
- [ ] Section 1: User Fee Cover Sheet
- [ ] Section 2: Indications for Use
- [ ] Section 3: 510(k) Statement
- [ ] Section 4: Device Description
- [ ] Section 5: Truthful and Accuracy Statement
- [ ] Section 6: Class III Summary (if applicable)
- [ ] Section 7: Financial Certifications
- [ ] Section 8: Declarations
- [ ] Section 9: Class II Special Controls
- [ ] Section 10: Proposed Label
- [ ] Section 11: Sterility and Pyrogenicity (if applicable)
- [ ] Section 12: Biocompatibility (if applicable)
- [ ] Section 13: 510(k) Summary
- [ ] Section 14: Attachments
- [ ] RTA (Refuse to Accept) criteria 체크리스트

#### AC-7.2: PMA 제출 준비

**Given:** Class III device PMA 요청
**When:** expert-submission 에이전트가 요청 수신
**Then:**
- [ ] Original PMA format 문서 구조 생성
- [ ] Volume 1: User Fee, Administrative
- [ ] Volume 2: Nonclinical Lab Studies
- [ ] Volume 3: Clinical Studies
- [ ] Volume 4: Manufacturing
- [ ] Volume 5: Case Histories
- [ ] 각 섹션별 [FDA 21 CFR 814] 인용

#### AC-7.3: CE Marking Technical File

**Given:** CE Marking 제출 요청
**When:** expert-submission 에이전트가 요청 수신
**Then:**
- [ ] Annex II Technical Documentation 구조
- [ ] Annex III Summary of Safety and Performance
- [ ] Device description and specification
- [ ] Labeling and IFU
- [ ] Risk analysis (ISO 14971)
- [ ] Clinical evaluation (Annex XIV)
- [ ] Proof of conformity assessment
- [ ] Declaration of Conformity
- [ ] 각 섹션별 [MDR 2017/745] 인용

#### AC-7.4: 제출 체크리스트 (Deliverable)

**Given:** 제출 전 최종 검증
**When:** expert-submission 에이전트가 체크리스트 실행
**Then:**
- [ ] RTA criteria 충족 (FDA)
- [ ] eCopy format 준수 (FDA)
- [ ] File naming 규칙 준수
- [ ] PDF/A format 준수
- [ ] Digital signature 준비
- [ ] Submission fee 결제 확인
- [ ] [FDA eCopy Guide] 인용

### AC-8: expert-audit 에이전트

#### AC-8.1: 감사 계획 수립

**Given:** Notified body audit 예정 (30일 전)
**When:** expert-audit 에이전트가 요청 수신
**Then:**
- [ ] ISO 13485 체크리스트 생성
- [ ] MDR Annex IX 체크리스트 생성
- [ ] Audit scope 정의
- [ ] Audit team 구성 제안
- [ ] Document readiness assessment
- [ ] Opening meeting agenda
- [ ] Closing meeting agenda
- [ ] [ISO 19011] 인용

#### AC-8.2: 감사 준비 상태 모니터링

**Given:** Upcoming audit within 30 days
**When:** expert-audit 에이전트가 Readiness assessment
**Then:**
- [ ] Missing documents 식별
- [ ] Open CAPA items 식별
- [ ] Overdue training 식별
- [ ] Readiness score 계산 (0-100%)
- [ ] Action items for gaps
- [ ] Daily countdown dashboard

#### AC-8.3: 비적합(NC) 대응 전략

**Given:** Major/Minor NC 발행
**When:** expert-audit 에이전트가 NC 수신
**Then:**
- [ ] NC 분석 (Major vs Minor)
- [ ] Root cause analysis 제안 (5 Whys)
- [ ] CAPA plan template 제공
- [ ] Response timeline 제안 (Major: 3개월, Minor: 1개월)
- [ ] Appeal process 가이드 (if needed)
- [ ] [ISO 13485:2016 Section 9.2] 인용

#### AC-8.4: Digital Audit Room (Notion)

**Given:** Audit 준비 시작
**When:** expert-audit 에이전트가 Audit room 생성
**Then:**
- [ ] Notion workspace 자동 생성
- [ ] Documents 섹션 (Procedures, Records, Forms)
- [ ] CAPA logs 섹션
- [ ] Audit trail 섹션
- [ ] Team collaboration space
- [ ] External auditor access (read-only)

## VALID 품질 게이트 검증

### AC-V.1: Verified 차원

**AC-V.1.1: 규정 원문 대조**

**Given:** 사용자가 규제 주장 요청
**When:** 에이전트가 응답 생성
**Then:**
- [ ] 모든 규제 주장에 출처 인용
- [ ] [Standard] Section [Number] 형식 준수
- [ ] Context7 MCP로 규정 원문 대조 검증
- [ ] 만료된 규정 사용 시 경고 표시

**AC-V.1.2: 표준 버전 검증**

**Given:** 표준 인용 포함 응답
**When:** expert-standards 에이전트가 응답 생성
**Then:**
- [ ] 모든 표준에 [ISO 13485:2016] 형식 버전 명시
- [ ] 만료된 표준 사용 방지
- [ ] 최신 버전 제안 (예: ISO 14971:2019)
- [ ] Context7 MCP로 최신 버전 검증

### AC-V.2: Accurate 차원

**AC-V.2.1: 데이터 출처 검증**

**Given:** 데이터/수치 포함 응답
**When:** 에이전트가 응답 생성
**Then:**
- [ ] 모든 데이터에 출처 인용
- [ ] 출처 신뢰도 검증 (Federal Register, Official Journal, MFDS)
- [ ] 날짜/버전 정확성 확인
- [ ] 모순 데이터 해결 완료

**AC-V.2.2: 사용자 요금 정확성**

**Given:** 제출 수수료 계산 요청
**When:** expert-submission 에이전트가 계산
**Then:**
- [ ] 최신 FY 요금 반영
- [ ] Small Business fee减免 적용
- [ ] FDA, EU MFDS 요금 비교
- [ ] Federal Register 출처 인용

### AC-V.3: Linked 차원

**AC-V.3.1: 추적성 매트릭스**

**Given:** 설계 요구사항 정의
**When:** expert-design-control 에이전트가 추적성 생성
**Then:**
- [ ] Requirements ↔ Documents ↔ Evidence 양방향 링크
- [ ] Design Input → Design Output → Verification → Validation 추적성
- [ ] Notion DB 관계 설정 (Relations)
- [ ] 고립 문서 (Orphaned document) 없음

**AC-V.3.2: CAPA ↔ Risk 연동**

**Given:** CAPA 생성
**When:** expert-capa 에이전트가 CAPA 등록
**Then:**
- [ ] CAPA Tracker ↔ Risk Register Relation 설정
- [ ] CAPA Tracker ↔ Document Registry Relation 설정
- [ ] Relations 양방향 작동 확인
- [ ] 관련 문서 자동 링크

### AC-V.4: Inspectable 차원

**AC-V.4.1: 결정 근거 문서화**

**Given:** 복잡한 규제 전략 결정
**When:** expert-regulatory 에이전트가 Sequential Thinking 적용
**Then:**
- [ ] 결정 근거 문서화 (Assumptions, Alternatives, Trade-offs)
- [ ] 타임스탬프 기록 (Agent, Date, Reasoning, Outcome)
- [ ] 감사 추적 완전성 (Audit trail completeness)
- [ ] Sequential Thinking MCP로 체계적 사과 유도

**AC-V.4.2: 위험-이익 분석 근거**

**Given:** 위험-이익 분석 수행
**When:** expert-risk 에이전트가 평가
**Then:**
- [ ] Clinical benefits 정량화 근거
- [ ] Risks 정량화 근거
- [ ] Benefit-Risk Ratio 계산 근거
- [ ] ALARP 적용 근거
- [ ] 근거 문서 Notion DB 저장

### AC-V.5: Deliverable 차원

**AC-V.5.1: 제출 형식 준수**

**Given:** 510(k) 제출 준비 완료
**When:** expert-submission 에이전트가 최종 검증
**Then:**
- [ ] eCopy format 준수 (FDA requirements)
- [ ] PDF/A format 준수
- [ ] File naming 규칙 준수
- [ ] RTA criteria 충족 (Refuse to Accept 방지)

**AC-V.5.2: 템플릿 적합성**

**Given:** CER 작성 완료
**When:** expert-clinical 에이전트가 최종 검증
**Then:**
- [ ] MDR Annex XV 템플릿 구조 준수
- [ ] 모든 필수 섹션 포함 (Section 1-6)
- [ ] PRISMA flow diagram 포함
- [ ] Clinical evidence 목록 완전성

## E2E (End-to-End) 시나리오

### AC-E2E.1: 미국 시장 진입 시나리오

**Given:** 제조사가 새로운 Class II 의료기기 미국 시장 진입 계획
**When:** 사용자가 "미국 시장 진입 전략" 요청
**Then:**
- [ ] **Step 1 (Regulatory):** expert-regulatory가 510(k) vs PMA 경로 분석
- [ ] **Step 2 (Standards):** expert-standards가 FDA 21 CFR 820.30 Design Control 요구사항 확인
- [ ] **Step 3 (Risk):** expert-risk가 ISO 14971 위험관리 절차 수행
- [ ] **Step 4 (Design Control):** expert-design-control가 DHF 템플릿 생성
- [ ] **Step 5 (Submission):** expert-submission가 510(k) eCopy 준비
- [ ] **Step 6 (Validation):** VALID 품질 게이트 5차원 모두 통과
- [ ] **Step 7 (Documentation):** Document Registry에 모든 문서 등록

### AC-E2E.2: CAPA 라이프사이클 시나리오

**Given:** Non-conformance report 제출 (불일치 식별)
**When:** 사용자가 "CAPA 생성" 요청
**Then:**
- [ ] **Step 1 (Risk):** expert-risk가 위험 등록 (Risk Register)
- [ ] **Step 2 (CAPA):** expert-capa가 CAPA 절차 개시 (CAPA Tracker)
- [ ] **Step 3 (Root Cause):** 5 Whys 기법으로 근본 원인 분석
- [ ] **Step 4 (Corrective Action):** 수정 조치 계획 수립
- [ ] **Step 5 (Preventive Action):** 예방 조치 계획 수립
- [ ] **Step 6 (Effectiveness):** 효성 검증 (90일 이내 재발 여부)
- [ ] **Step 7 (Audit):** expert-audit가 감사 준비 상태 확인
- [ ] **Step 8 (Validation):** VALID 품질 게이트 통과
- [ ] **Step 9 (Close-out):** CAPA 마감 및 Document Registry 업데이트

### AC-E2E.3: 임상 평가 시나리오

**Given:** CE Marking을 위한 임상 평가 필요
**When:** 사용자가 "CER 작성" 요청
**Then:**
- [ ] **Step 1 (Clinical):** expert-clinical이 MDR Annex XV CER 템플릿 생성
- [ ] **Step 2 (Literature Search):** PRISMA flow diagram으로 문헌 검색
- [ ] **Step 3 (Equivalence):** 유사 장치 분석 (Technical, Biological, Clinical)
- [ ] **Step 4 (Regulatory):** expert-regulatory가 MDR 요구사항 확인
- [ ] **Step 5 (Risk):** expert-risk가 임상 위험-이익 분석 수행
- [ ] **Step 6 (Submission):** expert-submission가 Technical File 준비
- [ ] **Step 7 (Validation):** VALID 품질 게이트 통과
- [ ] **Step 8 (Documentation):** Document Registry에 CER 등록

## Wave Parallelism 테스트

### AC-WP.1: 병렬 실행 테스트

**Given:** 3개 독립적 도메인 에이전트 필요
**When:** 사용자가 "미국, 유럽, 한국 규제 요구사항 비교" 요청
**Then:**
- [ ] **Parallel Execution:** expert-regulatory (FDA), expert-regulatory (EU), expert-regulatory (Korea) 동시 호출
- [ ] **Result Collection:** 3개 결과 동시 수집
- [ ] **Conflict Detection:** 충돌/모순 식별 (예: 임상 데이터 요구사항 차이)
- [ ] **Synthesis:** 비교표 생성 (공통 요구사항, 차이점 하이라이트)
- [ ] **Validation:** VALID 품질 게이트 통과

### AC-WP.2: 순차 실행 테스트

**Given:** 2개 의존적 도메인 에이전트 필요
**When:** 사용자가 "CAPA 생성 (Risk ID 필요)" 요청
**Then:**
- [ ] **Step 1 (Sequential):** expert-risk가 위험 분석 → Risk ID 생성
- [ ] **Step 2 (Handoff):** Risk ID를 expert-capa에 전달
- [ ] **Step 3 (Sequential):** expert-capa가 CAPA 생성 (Risk ID 연동)
- [ ] **Validation:** CAPA Tracker ↔ Risk Register Relation 확인
- [ ] **Quality:** VALID (Linked) 차원 통과

### AC-WP.3: 결과 통합 테스트

**Given:** 3개 에이전트 병렬 실행 완료
**When:** 결과 통합 단계
**Then:**
- [ ] **Merge:** 3개 에이전트 결과 통합
- [ ] **Conflict Resolution:** 충돌 시 Regulatory hierarchy 기반 우선순위
- [ ] **User Confirmation:** 해결 필요한 충돌 시 사용자에게 확인 요청
- [ ] **Final Report:** 통합 보고서 생성
- [ ] **Quality:** VALID (Verified, Accurate) 차원 통과

## 성능 기준

### AC-PERF.1: 응답 시간

**Given:** 일반 쿼리 (단일 도메인 에이전트)
**When:** 사용자가 요청
**Then:**
- [ ] **30초 이내** 응답 (Opus: 복잡한 규제 분석 제외)
- [ ] 타임아웃 설정 (2분)
- [ ] 타임아웃 시 진행 상태 알림

**Given:** 복잡한 쿼리 (Sequential Thinking 필요)
**When:** 사용자가 위험-이익 분석 요청
**Then:**
- [ ] **2분 이내** 응답 (Opus + Sequential Thinking MCP)
- [ ] 진행 상태 실시간 표시
- [ ] 단계별 결과 중간 보고

### AC-PERF.2: Notion DB 동기화

**Given:** Risk Register page 생성 요청
**When:** expert-risk 에이전트가 요청
**Then:**
- [ ] **5초 이내** page 생성 완료
- [ ] Risk Index 자동 계산 (Severity × Probability)
- [ ] Relations 설정 (CAPA Tracker, Document Registry)
- [ ] 동기화 실패 시 Retry (3회)

### AC-PERF.3: Progressive Disclosure 토큰 목표

**Given:** 스킬 로드
**When:** 에이전트가 스킬 로드
**Then:**
- [ ] **Level 1:** ~100 tokens 소비 (Metadata)
- [ ] **Level 2:** ~5000 tokens 소비 (Body)
- [ ] **Level 3:** On-demand (modules/)
- [ ] 전체 토큰 예산 준수 (30K plan, 180K run, 40K sync)

## Definition of Done (완료 정의)

### Wave 3.1 완료 기준
- [ ] 3개 에이전트 (expert-regulatory, expert-standards, expert-risk) 정상 작동
- [ ] 4개 스킬 (aria-domain-raqa, aria-knowledge-fda, aria-knowledge-eumdr, aria-knowledge-standards, aria-risk-management) 로드 가능
- [ ] Risk Register Notion DB 연동 완료
- [ ] AC-1 ~ AC-3 (Regulatory, Standards, Risk) 모두 통과
- [ ] VALID (Verified, Accurate) 차원 통과

### Wave 3.2 완료 기준
- [ ] 3개 에이전트 (expert-design-control, expert-capa, expert-clinical) 정상 작동
- [ ] 2개 스킬 (aria-design-control, aria-capa-process) 로드 가능
- [ ] CAPA Tracker, Document Registry Notion DB 연동 완료
- [ ] AC-4 ~ AC-6 (Design Control, CAPA, Clinical) 모두 통과
- [ ] VALID (Linked, Inspectable) 차원 통과

### Wave 3.3 완료 기준
- [ ] 2개 에이전트 (expert-submission, expert-audit) 정상 작동
- [ ] 2개 스킬 (aria-submission-templates, aria-knowledge-mfds) 로드 가능
- [ ] 모든 Notion DB (Risk Register, CAPA Tracker, Document Registry) 통합 완료
- [ ] AC-7 ~ AC-8 (Submission, Audit) 모두 통과
- [ ] VALID (Deliverable) 차원 통과
- [ ] E2E 시나리오 3개 모두 통과
- [ ] Wave Parallelism 테스트 3개 모두 통과
- [ ] 성능 기준 모두 충족

### 전체 프로젝트 완료 기준
- [ ] 8개 RA/QA 도메인 에이전트 구현 완료
- [ ] 9개 도메인 스킬 구현 완료
- [ ] 3개 Notion DB 연동 완료
- [ ] VALID 품질 프레임워크 5차원 모두 통과
- [ ] Wave Parallelism 모델 검증 완료
- [ ] E2E 시나리오 테스트 3개 모두 통과
- [ ] 성능 기준 모두 충족
- [ ] 사용자 승인 획득 (User Acceptance)

---

## 변경 이력

| 버전 | 날짜 | 변경 사항 | 작성자 |
|------|------|-----------|--------|
| 1.0.0 | 2026-02-09 | 초기 인수 기준 작성 | ARIA Quality Team |
