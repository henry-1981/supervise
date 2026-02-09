# SPEC-ARIA-003: ARIA Phase 3 - RA/QA 전문화

## TAG BLOCK

```yaml
SPEC_ID: SPEC-ARIA-003
TITLE: ARIA Phase 3 - RA/QA 도메인 전문화 시스템
STATUS: Planned
PRIORITY: High
ASSIGNED: ARIA Core Team
EPIC: ARIA Architecture Redesign
PHASE: Phase 3 (RA/QA Specialization)
CREATED: 2026-02-09
LANGUAGE: ko
```

## 환경 (Environment)

### 프로젝트 맥락

ARIA (AI Regulatory Intelligence Assistant)는 의료기기 RA/QA (Regulatory Affairs / Quality Assurance) 전문가를 위한 AI 어시스턴트 시스템입니다.

**현재 상태:**
- Phase 1 (Core Framework): 완료 - 기반 아키텍처 구축
- Phase 2 (Business Workflow): 미구현 - Brief-Execute-Deliver 워크플로우
- Phase 3 (RA/QA Specialization): 본 SPEC 대상 - 8개 도메인 전문가 에이전트 구현

**기술 스택:**
- Claude Code Plugin 아키텍처
- MoAI-ADK 패턴 (agent-authoring, skill-authoring)
- MCP 통합 (Context7, Notion, Sequential Thinking)
- Notion API (CAPA tracker, Risk register, Document registry)

### 기존 시스템 구조

**Phase 1 완료 항목:**
- ARIA 코어 에이전트 (orchestrator, manager-docs, manager-quality, manager-project)
- 비즈니스 에이전트 (expert-writer, expert-analyst, expert-reviewer, expert-researcher)
- Brief-Execute-Deliver 워크플로우 기반
- VALID 품질 프레임워크 정의

**Phase 3 목표:**
- 8개 RA/QA 도메인 전문가 에이전트 구현
- 9개 도메인 스킬 생성 (Progressive Disclosure)
- Notion DB 연동 및 추적성 확보
- Wave Parallelism 모델 적용

## 가정 (Assumptions)

### 사용자 가정

1. **언어 선호도:**
   - 사용자 대면 응답: 한국어 (conversation_language: ko)
   - 기술 문서: 한국어 (예: 코드 주석, API 문서)
   - 내부 에이전트 통신: 영어

2. **전문성 수준:**
   - 대상 사용자: 의료기기 RA/QA 전문가
   - 규정 지식: FDA 21 CFR Part 820, EU MDR, ISO 13485 숙지
   - 기술 역량: 비개발자, 자연어 인터페이스 선호

3. **업무 환경:**
   - 문서 중심 업무 (DHF, DMR, DHR 관리)
   - CAPA 라이프사이클 관리
   - 규제 제출 준비 (510(k), PMA, CE Marking)

### 기술적 가정

1. **MoAI-ADK 패턴:**
   - 에이전트 정의: `.claude/agents/**/*.md` (YAML frontmatter)
   - 스킬 정의: `.claude/skills/**/*.md` (Progressive Disclosure)
   - MCP 통합: Context7, Notion, Sequential Thinking

2. **모델 할당:**
   - Opus: 고복잡도 규제 분석 (expert-regulatory, expert-standards, expert-risk, expert-clinical)
   - Sonnet: 프로세스 및 제출 (expert-design-control, expert-capa, expert-submission, expert-audit)

3. **Notion DB 구조:**
   - CAPA Tracker: 이슈 식별부터 효성 검증까지
   - Risk Register: ISO 14971 위험관리
   - Document Registry: DHF/DMR/DHR 추적성

### 제약 사항

1. **비기능적 요구사항:**
   - 응답 시간: 일반 쿼리 30초 이내
   - 규정 인용: 모든 규제 주장에 출처 필수 (standard, section, version)
   - 사용자 승인: 최종 문서 완료 전 명시적 승인 필요

2. **품질 게이트:**
   - VALID 프레임워크 (Verified, Accurate, Linked, Inspectable, Deliverable)
   - 규정 원문 대조 검증
   - 추적성 매트릭스 자동 생성

## 요구사항 (Requirements)

### 1. expert-regulatory 에이전트

#### 1.1 Event-Driven Requirements

**[ER-001]** **WHEN** 사용자가 규제 전략을 요청하면, 시스템은 **SHALL** 적용 시장별 요구사항을 분석한다.

- **Given:** 사용자가 "미국 시장 진입을 위한 규제 전략" 요청
- **When:** expert-regulatory 에이전트가 요청 수신
- **Then:** FDA 21 CFR Part 820, 510(k) vs PMA 경로 분석 제공

**[ER-002]** **WHEN** 규제 변경사항이 발생하면, 시스템은 **SHALL** 영향받는 문서를 식별한다.

- **Given:** EU MDR 2017/745 개정안 발효
- **When:** 변경사항 감지
- **Then:** 영향받는 기술 문서 파일 (Technical File) 목록 제공

#### 1.2 State-Driven Requirements

**[SR-001]** **IF** 제품이 Class III 의료기기이면, 시스템은 **SHALL** PMA (Pre-Market Approval) 경로를 제안한다.

- **Condition:** FDA 분류 기준 확인
- **Action:** PMA 제출 요구사항 체크리스트 생성

**[SR-002]** **IF** 복수국 시장 진입이 계획되면, 시스템은 **SHALL** 국가별 요구사항 매트릭스를 제공한다.

- **Condition:** 미국, 유럽, 한국 동시 진입
- **Action:** FDA MDR, MFDS 요구사항 비교표 생성

#### 1.3 Ubiquitous Requirements

**[UR-001]** 시스템은 **항상** 모든 규제 주장에 출처를 **SHALL** 인용해야 한다.

- **Format:** [Standard] Section [Number] (예: FDA 21 CFR 820.30)
- **Verification:** Context7 MCP를 통한 규정 원문 대조

**[UR-002]** 시스템은 **항상** 최신 규정을 **SHALL** 반영해야 한다.

- **Source:** Federal Register, Official Journal of the EU, MFDS 공고
- **Update:** 주간 자동 업데이트 확인

### 2. expert-standards 에이전트

#### 2.1 Event-Driven Requirements

**[ER-003]** **WHEN** 표준 해석을 요청하면, 시스템은 **SHALL** 관련 조항을 상세히 분석한다.

- **Given:** "ISO 13485 Section 8.5.2 수정 조치" 요청
- **When:** expert-standards 에이전트가 요청 수신
- **Then:** 조항별 적용 범위, 문서화 요구사항, 증거 자료 상세 설명

**[ER-004]** **WHEN** 여러 표준이 충돌하면, 시스템은 **SHALL** 우선순위를 제안한다.

- **Given:** ISO 14971 위험관리 vs IEC 62304 소프트웨어 안전
- **When:** 충돌 감지
- **Then:** 규제 계층 구조 (Regulatory Hierarchy) 기준 우선순위 제안

#### 2.2 State-Driven Requirements

**[SR-003]** **IF** QMS가 ISO 13485 인증을 준비 중이면, 시스템은 **SHALL** 인증 체크리스트를 제공한다.

- **Condition:** ISO 13485:2016 인증 예정
- **Action:** CB (Certification Body) 문서 요구사항 목록 생성

**[SR-004]** **IF** 소프트웨어가 포함된 의료기기이면, 시스템은 **SHALL** IEC 62304 Safety Class 분석을 제공한다.

- **Condition:** SaMD (Software as Medical Device)
- **Action:** Class A/B/C 분석 및 문서화 요구사항

#### 2.3 Ubiquitous Requirements

**[UR-003]** 시스템은 **항상** 표준 버전을 **SHALL** 명시해야 한다.

- **Format:** [Standard Number]:[Year] (예: ISO 13485:2016)
- **Verification:** 만료된 표준 사용 방지

**[UR-004]** 시스템은 **항상** 표준 간 참조 관계를 **SHALL** 유지해야 한다.

- **Example:** ISO 14971 → ISO 13485 Section 8.2.3
- **Traceability:** 표준 매트릭스 자동 생성

### 3. expert-risk 에이전트

#### 3.1 Event-Driven Requirements

**[ER-005]** **WHEN** 위험 분석을 요청하면, 시스템은 **SHALL** ISO 14971 절차를 따른다.

- **Given:** 새로운 의료기기 위험 평가 요청
- **When:** expert-risk 에이전트가 요청 수신
- **Then:**
  1. 위험 식별 (Risk Identification)
  2. 위험 추정 (Risk Estimation)
  3. 위험 평가 (Risk Evaluation)
  4. 위험 경감 (Risk Control)
  5. 잔여 위험 평가 (Residual Risk Evaluation)

**[ER-006]** **WHEN** 위험이 허용 불가능하면, 시스템은 **SHALL** 추가 경감 조치를 제안한다.

- **Given:** 위험 점수 > 허용 기준 (Acceptability Threshold)
- **When:** 위험 평가 완료
- **Then:** 경감 옵션 (Inherent safety, Protective measures, Information for safety)

#### 3.2 State-Driven Requirements

**[SR-005]** **IF** 위험 경감 조치가 구현되면, 시스템은 **SHALL** 효성 검증을 요구한다.

- **Condition:** Risk control measure 구현 완료
- **Action:** Verification test plan 자동 생성

**[SR-006]** **IF** 잔여 위험이 존재하면, 시스템은 **SHALL** 경보 라벨링을 제안한다.

- **Condition:** All risks reduced as far as possible (AFAP)
- **Action:** Labeling warning, Contraindications

#### 3.3 Ubiquitous Requirements

**[UR-005]** 시스템은 **항상** Risk Register를 Notion DB에 **SHALL** 동기화해야 한다.

- **Fields:** Risk ID, Hazard, Harm, Severity, Probability, Risk Index, Control Measures
- **Update:** 위험 상태 변경 시 실시간 동기화

**[UR-006]** 시스템은 **항상** 위험-이익 분석 (Risk-Benefit Analysis)을 **SHALL** 지원해야 한다.

- **Format:** Clinical benefit vs Risk weighting
- **Threshold:** Benefit > Risk for market approval

### 4. expert-design-control 에이전트

#### 4.1 Event-Driven Requirements

**[ER-007]** **WHEN** 설계 통제 프로세스를 시작하면, 시스템은 **SHALL** DHF (Design History File) 구조를 생성한다.

- **Given:** 새로운 설계 프로젝트 개시
- **When:** expert-design-control 에이전트가 요청 수신
- **Then:** FDA 21 CFR 820.30 기반 DHF 템플릿 생성

**[ER-008]** **WHEN** 설계 검증이 완료되면, 시스템은 **SHALL** DMR (Device Master Record)를 업데이트한다.

- **Given:** Design verification 성공
- **When:** 검증 결과 입력
- **Then:** DMR 관련 섹션 자동 업데이트

#### 4.2 State-Driven Requirements

**[SR-007]** **IF** 설계 변경이 발생하면, 시스템은 **SHALL** 변경 영향도를 분석한다.

- **Condition:** Design change proposal
- **Action:** Validation vs Verification 범위 식별

**[SR-008]** **IF** 설계 이관이 발생하면, 시스템은 **SHALL** DHR (Device History Record)를 생성한다.

- **Condition:** Design to production transfer
- **Action:** Production lot 추적용 DHR 생성

#### 4.3 Ubiquitous Requirements

**[UR-007]** 시스템은 **항상** 설계 입력-추적성 매트릭스를 **SHALL** 유지해야 한다.

- **Format:** Design Input → Design Output → Verification → Validation
- **Traceability:** 요구사항별 시험 결과 링크

**[UR-008]** 시스템은 **항상** FDA Design Control 점검 체크리스트를 **SHALL** 지원해야 한다.

- **Checklist:** 21 CFR 820.30(a)-(g) 항목별 준수 여부

### 5. expert-capa 에이전트

#### 5.1 Event-Driven Requirements

**[ER-009]** **WHEN** 불일치가 식별되면, 시스템은 **SHALL** CAPA 절차를 개시한다.

- **Given:** Non-conformance report 제출
- **When:** expert-capa 에이전트가 요청 수신
- **Then:**
  1. 근본 원인 분석 (Root Cause Analysis)
  2. 수정 조치 (Corrective Action)
  3. 예방 조치 (Preventive Action)
  4. 효성 검증 (Effectiveness Check)

**[ER-010]** **WHEN** 근본 원인이 확인되면, 시스템은 **SHALL** 5 Whys 기법을 적용한다.

- **Given:** Quality issue 발생
- **When:** 원인 분석 단계
- **Then:** 5단계 왜(Why) 질문을 통한 근본 원인 도출

#### 5.2 State-Driven Requirements

**[SR-009]** **IF** CAPA가 효과적이지 않으면, 시스템은 **SHALL** 재평가를 요구한다.

- **Condition:** Effectiveness check 실패 (재발)
- **Action:** 새로운 근본 원인 분석 및 조치 계획

**[SR-010]** **IF** CAPA가 마감되면, 시스템은 **SHALL** 관련 문서를 업데이트한다.

- **Condition:** CAPA close-out
- **Action:** Quality manual, Procedure update 제안

#### 5.3 Ubiquitous Requirements

**[UR-009]** 시스템은 **항상** CAPA를 Notion DB에 **SHALL** 추적해야 한다.

- **Fields:** CAPA ID, Issue Description, Root Cause, Actions, Due Date, Status
- **Alert:** 마감일 미준비 시 알림

**[UR-010]** 시스템은 **항상** CAPA 추세 분석을 **SHALL** 제공해야 한다.

- **Analysis:** 부서별, 유형별, 기간별 추이
- **Output:** Management Review 보고서

### 6. expert-clinical 에이전트

#### 6.1 Event-Driven Requirements

**[ER-011]** **WHEN** 임상 평가를 요청하면, 시스템은 **SHALL** MDR 요구사항을 따른다.

- **Given:** CER (Clinical Evaluation Report) 작성 요청
- **When:** expert-clinical 에이전트가 요청 수신
- **Then:** Annex XV MDR 요구사항 기반 CER 생성

**[ER-012]** **WHEN** 시판 후 조사가 필요하면, 시스템은 **SHALL** PMCF (Post-Market Clinical Follow-up) 계획을 수립한다.

- **Given:** PMS 데이터 신호 감지
- **When:** PMCF 필요성 확인
- **Then:** PMCF study plan 생성

#### 6.2 State-Driven Requirements

**[SR-011]** **IF** 임상 데이터가 부족하면, 시스템은 **SHALL** 추가 임상 연구를 제안한다.

- **Condition:** Equivalence not demonstrated
- **Action:** Clinical study protocol 제안

**[SR-012]** **IF** 유사 장치가 존재하면, 시스템은 **SHALL** equivalent device 분석을 제공한다.

- **Condition:** Predicate device 식별
- **Action:** Technical, biological, clinical 비교 분석

#### 6.3 Ubiquitous Requirements

**[UR-011]** 시스템은 **항상** 임상 문헌 검색을 **SHALL** 지원해야 한다.

- **Sources:** PubMed, Cochrane, ClinicalTrials.gov
- **Format:** PRISMA flow diagram

**[UR-012]** 시스템은 **항상** 임상 안전성/유효성 데이터를 **SHALL** 요약해야 한다.

- **Metrics:** Sensitivity, Specificity, PPV, NPV
- **Visualization:** Forest plot for meta-analysis

### 7. expert-submission 에이전트

#### 7.1 Event-Driven Requirements

**[ER-013]** **WHEN** 510(k) 제출을 준비하면, 시스템은 **SHALL** eCopy 형식을 생성한다.

- **Given:** 510(k) submission 준비 요청
- **When:** expert-submission 에이전트가 요청 수신
- **Then:** FDA eCopy requirements 기반 문서 구조 생성

**[ER-014]** **WHEN** PMA 제출을 준비하면, 시스템은 **SHALL** Original PMA 서식을 따른다.

- **Given:** Class III device PMA 요청
- **When:** PMA 준비 단계
- **Then:** PMA 서식별 문서 조합 가이드 제공

#### 7.2 State-Driven Requirements

**[SR-013]** **IF** 규제 기관이 정보를 요청하면, 시스템은 **SHALL** AI (Additional Information) 답변을 준비한다.

- **Condition:** FDA AI Request 수신
- **Action:** 30일 이내 답변 초안 작성

**[SR-014]** **IF** 제출이 승인되면, 시스템은 **SHALL** post-approval 요구사항을 식별한다.

- **Condition:** 510(k) clearance or PMA approval
- **Action:** PMS report, Special controls requirements

#### 7.3 Ubiquitous Requirements

**[UR-013]** 시스템은 **항상** 제출 체크리스트를 **SHALL** 유지해야 한다.

- **Checklist:** FDA Refuse to Accept (RTA) criteria
- **Verification:** 제출 전 RTA pass 확인

**[UR-014]** 시스템은 **항상** 제출 수수료를 **SHALL** 계산해야 한다.

- **Fees:** User fee, 510(k) fee, PMA fee
- **Update:** FY (Fiscal Year)별 요금 업데이트

### 8. expert-audit 에이전트

#### 8.1 Event-Driven Requirements

**[ER-015]** **WHEN** 감사 계획을 수립하면, 시스템은 **SHALL** 체크리스트를 생성한다.

- **Given:** notified body audit 예정
- **When:** expert-audit 에이전트가 요청 수신
- **Then:** ISO 13485 + MDR 기반 감사 체크리스트 생성

**[ER-016]** **WHEN** 비적합(NC)이 발견되면, 시스템은 **SHALL** 대응 전략을 제안한다.

- **Given:** Major/Minor NC 발행
- **When:** NC 수신
- **Then:** Root cause analysis + CAPA plan 제안

#### 8.2 State-Driven Requirements

**[SR-015]** **IF** 감사가 예정되어 있으면, 시스템은 **SHALL** 준비 상태를 모니터링한다.

- **Condition:** Upcoming audit within 30 days
- **Action:** Readiness assessment, Missing documents 식별

**[SR-016]** **IF** 감사 결과가 부정적이면, 시스템은 **SHALL** 이의 제기 절차를 안내한다.

- **Condition:** Audit failure recommendation
- **Action:** Appeal process, Corrective action timeline

#### 8.3 Ubiquitous Requirements

**[UR-015]** 시스템은 **항상** 감사 추적성을 **SHALL** 유지해야 한다.

- **Fields:** Audit date, Auditor, Findings, CAPA link, Status
- **Dashboard:** Open items, Due dates

**[UR-016]** 시스템은 **항상** 감사 문서를 **SHALL** 구성해야 한다.

- **Documents:** Procedures, Records, Forms, CAPA logs
- **Organization:** Digital audit room (Notion)

## 추가 요구사항

### 9. MCP 통합

#### 9.1 Context7 MCP

**[ER-017]** **WHEN** 규정 검색이 필요하면, 시스템은 **SHALL** Context7 MCP를 사용한다.

- **Library:** FDA, EU MDR, ISO standards
- **Usage:** Latest regulation version verification

**[ER-018]** **WHEN** 표준 해석이 필요하면, 시스템은 **SHALL** Context7 문서를 참조한다.

- **Libraries:** ISO 13485, IEC 62304, ISO 14971
- **Output:** Official standard text + interpretation

#### 9.2 Notion MCP

**[ER-019]** **WHEN** CAPA를 생성하면, 시스템은 **SHALL** Notion DB에 기록한다.

- **Database:** CAPA Tracker
- **Fields:** ID, Description, Root Cause, Actions, Status, Due Date

**[ER-020]** **WHEN** 위험을 식별하면, 시스템은 **SHALL** Risk Register를 업데이트한다.

- **Database:** Risk Register
- **Fields:** Risk ID, Hazard, Severity, Probability, Risk Index, Controls

**[ER-021]** **WHEN** 문서가 생성되면, 시스템은 **SHALL** Document Registry에 등록한다.

- **Database:** Document Registry
- **Fields:** Doc ID, Type, Version, Date, Approved by, Link

#### 9.3 Sequential Thinking MCP

**[ER-022]** **WHEN** 복잡한 규제 전략이 필요하면, 시스템은 **SHALL** Sequential Thinking을 사용한다.

- **Use Case:** Multi-market regulatory pathway optimization
- **Output:** Structured reasoning with trade-off analysis

**[ER-023]** **WHEN** 위험-이익 분석이 필요하면, 시스템은 **SHALL** 체계적 분석을 수행한다.

- **Process:** Assumption audit → First principles → Alternative generation → Trade-off analysis
- **Output:** Justified risk-benefit decision

### 10. 스킬 시스템 (Progressive Disclosure)

#### 10.1 aria-domain-raqa 스킬

**[WR-001]** **WHERE** RA/QA 도메인 지식이 필요하면, 시스템은 **SHALL** aria-domain-raqa 스킬을 로드한다.

- **Level 1:** Metadata (~100 tokens)
  - Name, description, triggers (regulatory, standards, risk, capa)

- **Level 2:** Body (~5000 tokens)
  - RA/QA domain overview
  - Common regulatory frameworks
  - Risk management principles

- **Level 3:** Bundled (on-demand)
  - modules/fda-knowledge.md
  - modules/eumdr-knowledge.md
  - modules/standards-knowledge.md

#### 10.2 전문 지식 스킬 (8개)

**[WR-002]** **WHERE** FDA 지식이 필요하면, 시스템은 **SHALL** aria-knowledge-fda 스킬을 로드한다.

- **Structure:** modules/21cfr820.md, modules/510k.md, modules/pma.md

**[WR-003]** **WHERE** EU MDR 지식이 필요하면, 시스템은 **SHALL** aria-knowledge-eumdr 스킬을 로드한다.

- **Structure:** modules/annex-i.md, modules/annex-ix.md, modules/clinical-evaluation.md

**[WR-004]** **WHERE** 표준 지식이 필요하면, 시스템은 **SHALL** aria-knowledge-standards 스킬을 로드한다.

- **Structure:** modules/iso13485.md, modules/iec62304.md, modules/iso14971.md

**[WR-005]** **WHERE** MFDS 지식이 필요하면, 시스템은 **SHALL** aria-knowledge-mfds 스킬을 로드한다.

- **Structure:** modules/korea-mdr.md, modules/device-approval.md

**[WR-006]** **WHERE** 위험관리가 필요하면, 시스템은 **SHALL** aria-risk-management 스킬을 로드한다.

- **Structure:** modules/risk-analysis.md, modules/fmea.md, modules/fsta.md

**[WR-007]** **WHERE** 설계통제가 필요하면, 시스템은 **SHALL** aria-design-control 스킬을 로드한다.

- **Structure:** modules/dhf.md, modules/dmr.md, modules/dhr.md

**[WR-008]** **WHERE** CAPA가 필요하면, 시스템은 **SHALL** aria-capa-process 스킬을 로드한다.

- **Structure:** modules/root-cause-analysis.md, modules/corrective-action.md, modules/preventive-action.md

**[WR-009]** **WHERE** 제출 준비가 필요하면, 시스템은 **SHALL** aria-submission-templates 스킬을 로드한다.

- **Structure:** modules/510k-template.md, modules/pma-template.md, modules/ce-marking.md

### 11. Notion DB 스키마

#### 11.1 CAPA Tracker

**[ER-024]** **WHEN** CAPA가 생성되면, 시스템은 **SHALL** 다음 필드를 포함해야 한다.

- **Required Fields:**
  - CAPA ID (Auto-increment)
  - Issue Date (Date)
  - Source (Internal audit, Customer complaint, Non-conformance)
  - Problem Description (Text)
  - Root Cause (Text)
  - Corrective Action (Text)
  - Preventive Action (Text)
  - Responsible Person (Person)
  - Target Date (Date)
  - Actual Completion Date (Date)
  - Effectiveness Verification (Checkbox)
  - Status (Select: Open, In Progress, Verified, Closed)

- **Optional Fields:**
  - Related Risk ID (Relation to Risk Register)
  - Related Document ID (Relation to Document Registry)
  - Cost of Quality (Number)

#### 11.2 Risk Register

**[ER-025]** **WHEN** 위험이 식별되면, 시스템은 **SHALL** 다음 필드를 포함해야 한다.

- **Required Fields:**
  - Risk ID (Auto-increment)
  - Hazard (Text)
  - Harm (Text)
  - Causes (Text)
  - Initial Severity (Select: Negligible, Minor, Moderate, Major, Catastrophic)
  - Initial Probability (Select: Remote, Low, Medium, High, Frequent)
  - Initial Risk Index (Formula: Severity × Probability)
  - Control Measures (Text)
  - Residual Severity (Select)
  - Residual Probability (Select)
  - Residual Risk Index (Formula)
  - Risk Acceptability (Select: Acceptable, ALARP, Unacceptable)
  - Risk Evaluation Date (Date)
  - Review Date (Date)

- **Optional Fields:**
  - Related CAPA ID (Relation)
  - Related Standard (Text: ISO 14971 clause)
  - Benefit-Risk Analysis (Text)

#### 11.3 Document Registry

**[ER-026]** **WHEN** 문서가 생성되면, 시스템은 **SHALL** 다음 필드를 포함해야 한다.

- **Required Fields:**
  - Document ID (Auto-increment)
  - Document Type (Select: SOP, WI, Form, Record, Report)
  - Document Title (Text)
  - Version (Number)
  - Effective Date (Date)
  - Review Date (Date)
  - Author (Person)
  - Approver (Person)
  - Status (Select: Draft, Under Review, Approved, Superseded, Withdrawn)
  - Document Link (Files)

- **Optional Fields:**
  - Related CAPA ID (Relation)
  - Related Risk ID (Relation)
  - Applicable Standard (Text)
  - Change Description (Text)

### 12. VALID 품질 프레임워크

#### 12.1 Verified (검증됨)

**[ER-027]** **WHEN** 규제 주장을 하면, 시스템은 **SHALL** 규정 원문을 대조한다.

- **Requirement:** All regulatory claims cite source
- **Verification:** Context7 MCP cross-reference
- **Evidence:** [Standard] Section [Number] (예: FDA 21 CFR 820.30(a))

**[SR-017]** **IF** 규정이 만료되었으면, 시스템은 **SHALL** 경고를 표시한다.

- **Condition:** Outdated standard reference detected
- **Action:** Warning + Latest version suggestion

#### 12.2 Accurate (정확함)

**[ER-028]** **WHEN** 데이터를 제시하면, 시스템은 **SHALL** 출처를 검증한다.

- **Requirement:** All data sources validated
- **Verification:** Source credibility check
- **Evidence:** Date, URL, Authoritative source

**[SR-018]** **IF** 데이터 모순이 발견되면, 시스템은 **SHALL** 사용자에게 확인을 요청한다.

- **Condition:** Conflicting information from multiple sources
- **Action:** Present conflict + Request resolution

#### 12.3 Linked (연결됨)

**[ER-029]** **WHEN** 문서를 생성하면, 시스템은 **SHALL** 추적성을 확보한다.

- **Requirement:** Requirements ↔ Documents ↔ Evidence
- **Verification:** Traceability matrix generation
- **Evidence:** Bidirectional links in Notion DB

**[SR-019]** **IF** 추적성이 끊기면, 시스템은 **SHALL** 누락된 링크를 식별한다.

- **Condition:** Orphaned document or unreferenced requirement
- **Action:** Link missing alert

#### 12.4 Inspectable (검증 가능함)

**[ER-030]** **WHEN** 결정을 내리면, 시스템은 **SHALL** 근거를 문서화한다.

- **Requirement:** Decision rationale documented
- **Verification:** Audit trail completeness
- **Evidence:** Timestamp, Agent, Reasoning, Outcome

**[SR-020]** **IF** 감사 추적이 불충분하면, 시스템은 **SHALL** 추가 문서화를 요구한다.

- **Condition:** Missing decision rationale
- **Action:** Prompt for rationale documentation

#### 12.5 Deliverable (전달 가능함)

**[ER-031]** **WHEN** 제출 패키지를 준비하면, 시스템은 **SHALL** 형식 요구사항을 충족한다.

- **Requirement:** Submission format compliance
- **Verification:** Template conformance check
- **Evidence:** eCopy format, PDF structure, File naming

**[SR-021]** **IF** 형식 오류가 있으면, 시스템은 **SHALL** 제출 전 수정을 제안한다.

- **Condition:** Template non-compliance
- **Action:** Pre-submission format check

### 13. Wave Parallelism 모델

#### 13.1 Parallel Execution

**[ER-032]** **WHEN** 복수의 도메인 에이전트가 필요하면, 시스템은 **SHALL** 병렬 실행을 지원한다.

- **Use Case:** Regulatory + Standards + Risk 동시 분석
- **Execution:** 3개 에이전트 동시 호출
- **Synthesis:** 결과 통합 및 충돌 해결

**[ER-033]** **WHEN** 의존성이 존재하면, 시스템은 **SHALL** 순차 실행을 사용한다.

- **Use Case:** Risk analysis → CAPA creation (Risk ID 필요)
- **Execution:** 순차적 에이전트 호출
- **Handoff:** Risk ID를 CAPA 에이전트에 전달

#### 13.2 Result Synthesis

**[ER-034]** **WHEN** 병렬 실행이 완료되면, 시스템은 **SHALL** 결과를 통합한다.

- **Process:**
  1. 각 에이전트 결과 수집
  2. 충돌/모순 식별
  3. 우선순위 결정 (Regulatory hierarchy)
  4. 통합 보고서 생성

**[SR-022]** **IF** 결과가 충돌하면, 시스템은 **SHALL** 사용자에게 해결을 요청한다.

- **Condition:** Conflicting recommendations from multiple agents
- **Action:** Present conflict + Request resolution

## 스펙 (Specifications)

### S-1. 에이전트 아키텍처

**3계층 구조:**

1. **Business Agents** (기존 Phase 1)
   - expert-writer, expert-analyst, expert-reviewer, expert-researcher
   - 역할: 문서 작성, 분석, 검토, 연구 조정

2. **Domain Agents** (Phase 3 신규)
   - expert-regulatory, expert-standards, expert-risk
   - expert-design-control, expert-capa, expert-clinical
   - expert-submission, expert-audit
   - 역할: RA/QA 도메인 전문 지식 제공

3. **Core Agents** (기존 Phase 1)
   - orchestrator, manager-docs, manager-quality, manager-project
   - 역할: 워크플로우 조정, 품질 관리, 프로젝트 관리

**의존성 방향:**
- Business → Domain (Business agents가 Domain agents 호출)
- Domain → Skills (Domain agents가 Skills 로드)
- Core → Business + Domain (Core agents가 조정)

### S-2. 모델 할당 전략

**Opus 할당 (고복잡도):**
- expert-regulatory: 규제 전략, 복수국 시장 분석
- expert-standards: 표준 충돌 해석, 계층 구조 분석
- expert-risk: 위험-이익 분석, 복잡한 위험 경감
- expert-clinical: 임상 평가, 유사성 분석

**Sonnet 할당 (중복잡도):**
- expert-design-control: DHF/DMR/DHR 관리
- expert-capa: CAPA 라이프사이클, 근본 원인 분석
- expert-submission: 제출 패키지 준비
- expert-audit: 감사 준비, 대응

### S-3. 스킬 Progressive Disclosure 구조

**aria-domain-raqa (메인 스킬):**
```
.claude/skills/aria-domain-raqa/
├── SKILL.md (Level 1: ~100 tokens)
├── modules/
│   ├── regulatory-overview.md (Level 2)
│   ├── standards-overview.md
│   ├── risk-overview.md
│   ├── fda-knowledge.md (Level 3)
│   ├── eumdr-knowledge.md
│   └── standards-knowledge.md
└── examples/
    ├── regulatory-strategy-example.md
    └── risk-analysis-example.md
```

**전문 지식 스킬 구조 (8개):**
- 각 스킬은 독립적인 Progressive Disclosure 구조
- Level 1: Metadata (name, description, triggers)
- Level 2: Body (~5000 tokens, 핵심 개념)
- Level 3: Bundled (modules/ 디렉토리, 상세 참고 자료)

### S-4. Notion DB 스키마 상세

**CAPA Tracker:**
- Properties: 12개 필드
- Relations: Risk Register, Document Registry
- Automation: Due date alerts, Status transitions
- Views: By Status, By Responsible Person, Calendar view

**Risk Register:**
- Properties: 14개 필드
- Relations: CAPA Tracker, Document Registry
- Automation: Risk index calculation, Review date alerts
- Views: Risk Matrix (Heatmap), By Acceptability

**Document Registry:**
- Properties: 11개 필드
- Relations: CAPA Tracker, Risk Register
- Automation: Review date alerts, Version control
- Views: By Type, By Status, Effective Date calendar

### S-5. MCP 통합 패턴

**Context7 MCP 사용 패턴:**
```yaml
# 규정 검색 시
1. mcp__context7__resolve-library-id(query="FDA 21 CFR 820")
2. mcp__context7__get-library-docs(topics=["design-control", "risk-management"])

# 표준 검색 시
1. mcp__context7__resolve-library-id(query="ISO 13485")
2. mcp__context7__get-library-docs(topics=["clause-8", ["management-review"])
```

**Notion MCP 사용 패턴:**
```yaml
# CAPA 생성 시
1. Notion DB page creation in CAPA Tracker
2. Relation link to Risk Register (if applicable)
3. Automation trigger: Due date reminder setup

# 위험 등록 시
1. Notion DB page creation in Risk Register
2. Risk index calculation (Severity × Probability)
3. Acceptability assessment (ALARP principle)
```

**Sequential Thinking MCP 사용 패턴:**
```yaml
# 복잡한 규제 전략 분석 시
1. Assumption Audit: What are we assuming about market requirements?
2. First Principles: What is the core regulatory objective?
3. Alternative Generation: 510(k) vs PMA vs De Novo vs Exempt
4. Trade-off Analysis: Timeline vs Cost vs Success probability
5. Bias Check: Anchoring to familiar pathway?
```

### S-6. Wave Parallelism 실행 패턴

**병렬 실행 예시 (Regulatory Strategy):**
```python
# 동시에 3개 도메인 에이전트 호출
agents = [
    expert-regulatory("FDA pathway analysis"),
    expert-standards("ISO 13485 requirements"),
    expert-risk("Risk-based classification")
]
# 결과 통합
synthesis = merge_results(agents)
```

**순차 실행 예시 (CAPA with Risk):**
```python
# 1단계: 위험 분석
risk_result = expert-risk("Analyze non-conformance risk")
# 2단계: CAPA 생성 (Risk ID 활용)
capa_result = expert-capa(
    f"Create CAPA for Risk ID: {risk_result.id}"
)
```

### S-7. 품질 게이트 상세

**VALID 검증 체크리스트:**

1. **Verified:**
   - [ ] 모든 규제 주장에 출처 인용
   - [ ] 규정 원문 대조 검증 완료
   - [ ] 최신 버전 사용 확인

2. **Accurate:**
   - [ ] 데이터 출처 검증
   - [ ] 수치/날짜 정확성 확인
   - [ ] 모순 데이터 해결 완료

3. **Linked:**
   - [ ] 요구사항-문서-증거 간 추적성
   - [ ] Notion DB 관계 설정
   - [ ] 고립 문서 없음

4. **Inspectable:**
   - [ ] 모든 결정에 근거 문서화
   - [ ] 감사 추적 완전성
   - [ ] 타임스탬프 기록

5. **Deliverable:**
   - [ ] 제출 형식 준수
   - [ ] 템플릿 적합성
   - [ ] 파일 명명 규칙

## 추적성 (Traceability)

### 요구사항-에이전트 매트릭스

| REQ # | Requirement | Agent | Skill | Notion DB |
|-------|-------------|-------|-------|-----------|
| 1.1-1.3 | Regulatory Strategy | expert-regulatory | aria-knowledge-fda, aria-knowledge-eumdr | N/A |
| 2.1-2.3 | Standards Interpretation | expert-standards | aria-knowledge-standards | N/A |
| 3.1-3.3 | Risk Management | expert-risk | aria-risk-management | Risk Register |
| 4.1-4.3 | Design Control | expert-design-control | aria-design-control | Document Registry |
| 5.1-5.3 | CAPA | expert-capa | aria-capa-process | CAPA Tracker |
| 6.1-6.3 | Clinical Evaluation | expert-clinical | aria-domain-raqa (modules/clinical) | N/A |
| 7.1-7.3 | Submission | expert-submission | aria-submission-templates | Document Registry |
| 8.1-8.3 | Audit | expert-audit | aria-domain-raqa (modules/audit) | N/A |

### 에이전트-모델 할당

| Agent | Model | Complexity | Rationale |
|-------|-------|------------|-----------|
| expert-regulatory | Opus | High | Multi-market strategy, complex pathway analysis |
| expert-standards | Opus | High | Conflict resolution, hierarchy interpretation |
| expert-risk | Opus | High | Risk-benefit analysis, complex mitigation |
| expert-clinical | Opus | High | Clinical evaluation, equivalence analysis |
| expert-design-control | Sonnet | Medium | Process management, documentation |
| expert-capa | Sonnet | Medium | Lifecycle management, root cause |
| expert-submission | Sonnet | Medium | Template-based, structured |
| expert-audit | Sonnet | Medium | Checklist-based, preparation |

### 스킬 로드 트리거

**Keyword Triggers:**
- aria-domain-raqa: regulatory, standard, risk, capa, audit, clinical, submission
- aria-knowledge-fda: FDA, 21 CFR, 510(k), PMA
- aria-knowledge-eumdr: MDR, CE Marking, Technical File, Clinical Evaluation
- aria-knowledge-standards: ISO 13485, IEC 62304, ISO 14971
- aria-risk-management: FMEA, FTA, STA, Risk Index, ALARP
- aria-design-control: DHF, DMR, DHR, Design Input, Verification
- aria-capa-process: Root Cause, 5 Whys, Fishbone, Corrective Action
- aria-submission-templates: eCopy, Original PMA, CE Marking, Technical File
- aria-knowledge-mfds: MFDS, Korea MDR, Device Approval

**Agent Triggers:**
- expert-regulatory: manager-spec, manager-docs
- expert-standards: expert-regulatory, expert-design-control
- expert-risk: expert-regulatory, expert-design-control, expert-capa
- expert-design-control: manager-docs, expert-regulatory
- expert-capa: manager-quality, expert-audit
- expert-clinical: expert-regulatory, expert-submission
- expert-submission: expert-regulatory, expert-standards
- expert-audit: manager-quality, manager-project

**Phase Triggers:**
- plan: All agents (requirements analysis)
- run: All agents (implementation)
- sync: manager-docs (documentation generation)

---

## 변경 이력

| 버전 | 날짜 | 변경 사항 | 작성자 |
|------|------|-----------|--------|
| 1.0.0 | 2026-02-09 | 초기 SPEC 작성 | ARIA Core Team |

---

## 승인 기록

| 역할 | 이름 | 서명 | 날짜 |
|------|------|------|------|
| Spec Author | ARIA Core Team | | 2026-02-09 |
| Technical Reviewer | | | |
| Domain Expert | | | |
| Approval Authority | | | |
