# PLAN-ARIA-003: 구현 계획

## TAG BLOCK

```yaml
SPEC_ID: SPEC-ARIA-003
PLAN_ID: PLAN-ARIA-003
STATUS: Planned
PHASE: Implementation
APPROACH: 3-Phase Wave Parallelism
PRIORITY: High
ESTIMATED_EFFORT: 8 weeks (3 waves)
TEAM: ARIA Development Team
CREATED: 2026-02-09
LANGUAGE: ko
```

## 개요 (Overview)

본 문서는 SPEC-ARIA-003의 구현 전략을 정의합니다. 8개 RA/QA 도메인 에이전트와 9개 도메인 스킬을 3단계 Wave Parallelism 모델로 구현합니다.

### 구현 원칙

1. **Progressive Enhancement**: 각 Wave는 이전 Wave를 기반으로 구축
2. **Wave Parallelism**: 독립적인 에이전트는 병렬 개발, 의존성은 순차 개발
3. **VALID 품질**: 모든 단계에서 VALID 프레임워크 적용
4. **Notion DB 우선**: 데이터 구조 먼저 정의, 에이전트 나중 구현

## Wave 3.1: Core Foundation (2주)

### 목표

RA/QA 도메인의 핵심인 **Regulatory, Standards, Risk** 3개 에이전트와 관련 스킬을 구현합니다.

### Milestones

#### M-3.1.1: expert-regulatory 구현 (3일)

**Priority: High**

**작업 항목:**
1. 에이전트 정의 파일 생성
   - `.claude/agents/aria/expert-regulatory.md`
   - YAML frontmatter: model: opus, skills: [aria-domain-raqa, aria-knowledge-fda, aria-knowledge-eumdr]

2. 핵심 기능 구현
   - 규제 전략 분석 (FDA 510(k) vs PMA)
   - 복수국 시장 요구사항 매트릭스
   - 규정 변경 영향도 분석

3. Context7 MCP 통합
   - FDA 21 CFR 820 라이브러리 연동
   - EU MDR 2017/745 라이브러리 연동

4. 검증
   - [ ] 510(k) vs PMA 결정 트리 정확성
   - [ ] 규정 출처 인용 (Verified)
   - [ ] 최신 규정 반영 (Accurate)

**성공 기준:**
- "미국 시장 진입을 위한 규제 전략" 요청에 적절한 경로 제안
- 모든 규제 주장에 [Standard] Section [Number] 형식 인용

#### M-3.1.2: aria-knowledge-fda 스킬 구현 (2일)

**Priority: High**

**작업 항목:**
1. 스킬 정의 파일 생성
   - `.claude/skills/aria-knowledge-fda/SKILL.md`
   - Progressive Disclosure: Level 1 (100 tokens), Level 2 (5000 tokens)

2. 모듈 구조 생성
   - `modules/21cfr820.md` (Quality System Regulation)
   - `modules/510k.md` (Pre-market Notification)
   - `modules/pma.md` (Pre-market Approval)
   - `modules/de-novo.md` (De Novo Classification)

3. Context7 라이브러리 매핑
   - resolve-library-id: "fda regulations"
   - get-library-docs topics: ["510k", "pma", "qsr"]

4. 검증
   - [ ] 모든 섹션에 출처 인용
   - [ ] 최신 FY (Fiscal Year) 요금 반영

**성공 기준:**
- FDA 21 CFR 820.30 Design Control 섹션 정확한 인용
- 510(k) 사용자 요금 정확한 계산

#### M-3.1.3: aria-knowledge-eumdr 스킬 구현 (2일)

**Priority: High**

**작업 항목:**
1. 스킬 정의 파일 생성
   - `.claude/skills/aria-knowledge-eumdr/SKILL.md`

2. 모듈 구조 생성
   - `modules/annex-i.md` (Essential Requirements)
   - `modules/annex-ix.md` (Clinical Evaluation)
   - `modules/annex-xi.md` (Technical Documentation)
   - `modules/classification.md` (Medical Device Classification)

3. Context7 라이브러리 매핑
   - resolve-library-id: "eu mdr"
   - get-library-docs topics: ["annex-i", "clinical-evaluation", "technical-file"]

4. 검증
   - [ ] MDR 2017/745 vs MDD 93/42/EEC 차이점 명확
   - [ ] CE Marking 절차 정확한 설명

**성공 기준:**
- EU MDR Classification Rule 정확한 적용
- Clinical Evaluation Report (CER) 요구사항 완전한 목록

#### M-3.1.4: expert-standards 구현 (3일)

**Priority: High**

**작업 항목:**
1. 에이전트 정의 파일 생성
   - `.claude/agents/aria/expert-standards.md`
   - YAML frontmatter: model: opus, skills: [aria-domain-raqa, aria-knowledge-standards]

2. 핵심 기능 구현
   - 표준 해석 (ISO 13485, IEC 62304, ISO 14971)
   - 표준 충돌 해결 (Regulatory Hierarchy)
   - 표준 매트릭스 생성 (표준 간 참조 관계)

3. Context7 MCP 통합
   - ISO 13485:2016 라이브러리 연동
   - IEC 62304 라이브러리 연동
   - ISO 14971 라이브러리 연동

4. 검증
   - [ ] 모든 표준에 버전 명시
   - [ ] 표준 간 참조 관계 추적성

**성공 기준:**
- "ISO 13485 Section 8.5.2 수정 조치" 요청에 상세 분석 제공
- ISO 14971 vs IEC 62304 충돌 시 우선순위 제안

#### M-3.1.5: aria-knowledge-standards 스킬 구현 (2일)

**Priority: High**

**작업 항목:**
1. 스킬 정의 파일 생성
   - `.claude/skills/aria-knowledge-standards/SKILL.md`

2. 모듈 구조 생성
   - `modules/iso13485.md` (Quality Management System)
   - `modules/iec62304.md` (Software Life Cycle)
   - `modules/iso14971.md` (Risk Management)
   - `modules/iec62366-1.md` (Usability Engineering)

3. Context7 라이브러리 매핑
   - resolve-library-id: "iso 13485"
   - get-library-docs topics: ["clause-8", ["management-review"]]

4. 검증
   - [ ] 만료된 표준 사용 방지
   - [ ] 표준 간 참조 관계 매트릭스

**성공 기준:**
- ISO 13485:2016 vs ISO 13485:2012 차이점 명확
- IEC 62304 Safety Class 분석 정확

#### M-3.1.6: expert-risk 구현 (3일)

**Priority: High**

**작업 항목:**
1. 에이전트 정의 파일 생성
   - `.claude/agents/aria/expert-risk.md`
   - YAML frontmatter: model: opus, skills: [aria-domain-raqa, aria-risk-management]

2. 핵심 기능 구현
   - ISO 14971 위험관리 절차 (5단계)
   - 위험-이익 분석 (Risk-Benefit Analysis)
   - Risk Register Notion DB 연동

3. Notion MCP 통합
   - Risk Register DB page creation
   - Risk Index 자동 계산 (Severity × Probability)
   - ALARP 원칙 적용

4. 검증
   - [ ] 위험 식별 → 추정 → 평가 → 경감 → 잔여 위험 절차 준수
   - [ ] Risk Register 동기화

**성공 기준:**
- 새로운 의료기기 위험 평가 요청에 ISO 14971 5단계 절차 완료
- Risk Register Notion DB 실시간 업데이트

#### M-3.1.7: aria-risk-management 스킬 구현 (2일)

**Priority: High**

**작업 항목:**
1. 스킬 정의 파일 생성
   - `.claude/skills/aria-risk-management/SKILL.md`

2. 모듈 구조 생성
   - `modules/risk-analysis.md` (FMEA, FTA, STA)
   - `modules/fmea.md` (Failure Mode and Effects Analysis)
   - `modules/fsta.md` (Fault Tree Analysis)
   - `modules/risk-benefit.md` (Risk-Benefit Analysis)

3. Sequential Thinking MCP 통합
   - 복잡한 위험-이익 분석 시 체계적 사고 유도

4. 검증
   - [ ] FMEA 템플릿 완전성
   - [ ] Risk Index 계산 정확성

**성공 기준:**
- FMEA 템플릿 Severity, Probability, Detection 매개변수 완전
- Risk-Benefit Analysis 명확한 근거 제시

#### M-3.1.8: aria-domain-raqa 메인 스킬 구현 (2일)

**Priority: High**

**작업 항목:**
1. 스킬 정의 파일 생성
   - `.claude/skills/aria-domain-raqa/SKILL.md`

2. Progressive Disclosure 구조
   - Level 1: Metadata (~100 tokens)
   - Level 2: Body (~5000 tokens)
     - RA/QA domain overview
     - Common regulatory frameworks
     - Risk management principles
   - Level 3: Bundled modules/

3. 모듈 구조 생성
   - `modules/regulatory-overview.md`
   - `modules/standards-overview.md`
   - `modules/risk-overview.md`
   - `examples/regulatory-strategy-example.md`
   - `examples/risk-analysis-example.md`

4. 검증
   - [ ] Progressive Disclosure 토큰 목표 준수
   - [ ] 모든 서브 스킬 참조 포함

**성공 기준:**
- Level 1 로드 시 ~100 tokens 소비
- Level 2 로드 시 ~5000 tokens 소비
- RA/QA 도메인 전체 개관 제공

#### M-3.1.9: Notion DB 스키마 구현 (Risk Register) (1일)

**Priority: High**

**작업 항목:**
1. Notion DB 생성
   - Database Name: "Risk Register"
   - Properties: 14개 필드 (SPEC 참조)

2. MCP 연동
   - Notion MCP page creation 자동화
   - Risk Index 자동 계산 (Severity × Probability)
   - Relations: CAPA Tracker, Document Registry

3. 검증
   - [ ] 모든 필드 타입 정확
   - [ ] Relations 양방향 작동
   - [ ] Risk Index 계산 정확

**성공 기준:**
- expert-risk가 위험 식별 시 Risk Register page 자동 생성
- Risk Index 필드 자동 계산

### Wave 3.1 완료 조건

- [ ] 3개 에이전트 (expert-regulatory, expert-standards, expert-risk) 정상 작동
- [ ] 4개 스킬 (aria-domain-raqa, aria-knowledge-fda, aria-knowledge-eumdr, aria-knowledge-standards, aria-risk-management) 로드 가능
- [ ] Risk Register Notion DB 연동 완료
- [ ] VALID 품질 게이트 통과 (Verified, Accurate, Linked)

## Wave 3.2: Process Foundation (2주)

### 목표

RA/QA 프로세스의 핵심인 **Design Control, CAPA, Clinical** 3개 에이전트와 관련 스킬을 구현합니다.

### Milestones

#### M-3.2.1: expert-design-control 구현 (3일)

**Priority: High**

**작업 항목:**
1. 에이전트 정의 파일 생성
   - `.claude/agents/aria/expert-design-control.md`
   - YAML frontmatter: model: sonnet, skills: [aria-domain-raqa, aria-design-control]

2. 핵심 기능 구현
   - DHF (Design History File) 구조 생성
   - DMR (Device Master Record) 관리
   - DHR (Device History Record) 생성
   - 설계 입력-추적성 매트릭스

3. Notion MCP 통합
   - Document Registry DB page creation
   - DHF/DMR/DHR 자동 분류

4. 검증
   - [ ] FDA 21 CFR 820.30 Design Control 절차 준수
   - [ ] 추적성 매트릭스 완전성

**성공 기준:**
- 새로운 설계 프로젝트 개시 시 DHF 템플릿 자동 생성
- 설계 입력-추적성 매트릭스 자동 업데이트

#### M-3.2.2: aria-design-control 스킬 구현 (2일)

**Priority: High**

**작업 항목:**
1. 스킬 정의 파일 생성
   - `.claude/skills/aria-design-control/SKILL.md`

2. 모듈 구조 생성
   - `modules/dhf.md` (Design History File)
   - `modules/dmr.md` (Device Master Record)
   - `modules/dhr.md` (Device History Record)
   - `modules/traceability.md` (Design Input-Output Traceability)

3. 템플릿 생성
   - DHF Template (FDA 21 CFR 820.30 기반)
   - DMR Template (Production specifications)
   - DHR Template (Production lot tracking)

4. 검증
   - [ ] 모든 템플릿 FDA 요구사항 충족
   - [ ] 추적성 매트릭스 양방향 링크

**성공 기준:**
- DHF 템플릿에 Design Input, Output, Verification, Validation 섹션 완전
- 추적성 매트릭스 요구사항별 시험 결과 링크

#### M-3.2.3: expert-capa 구현 (3일)

**Priority: High**

**작업 항목:**
1. 에이전트 정의 파일 생성
   - `.claude/agents/aria/expert-capa.md`
   - YAML frontmatter: model: sonnet, skills: [aria-domain-raqa, aria-capa-process]

2. 핵심 기능 구현
   - CAPA 절차 (식별 → 근본 원인 → 수정/예방 → 효성 검증)
   - 5 Whys 기법 적용
   - CAPA 추세 분석

3. Notion MCP 통합
   - CAPA Tracker DB page creation
   - Due date alerts
   - Relations: Risk Register, Document Registry

4. 검증
   - [ ] CAPA 4단계 절차 준수
   - [ ] 근본 원인 분석 깊이 (5 Whys)

**성공 기준:**
- Non-conformance report 제출 시 CAPA 절차 자동 개시
- CAPA Tracker Notion DB 실시간 업데이트

#### M-3.2.4: aria-capa-process 스킬 구현 (2일)

**Priority: High**

**작업 항목:**
1. 스킬 정의 파일 생성
   - `.claude/skills/aria-capa-process/SKILL.md`

2. 모듈 구조 생성
   - `modules/root-cause-analysis.md` (5 Whys, Fishbone, 5M)
   - `modules/corrective-action.md` (Immediate correction vs Root cause fix)
   - `modules/preventive-action.md` (Systemic prevention)
   - `modules/effectiveness-check.md` (Verification timelines)

3. 템플릿 생성
   - CAPA Form (ISO 13485 Section 10.2 기반)
   - Root Cause Analysis Template

4. 검증
   - [ ] 5 Whys 깊이 충분 (최소 5단계)
   - [ ] CAPA Form ISO 13485 요구사항 충족

**성공 기준:**
- Root Cause Analysis Template에 Fishbone diagram 포함
- CAPA Form에 Effectiveness Verification 타임라인 포함

#### M-3.2.5: expert-clinical 구현 (3일)

**Priority: High**

**작업 항목:**
1. 에이전트 정의 파일 생성
   - `.claude/agents/aria/expert-clinical.md`
   - YAML frontmatter: model: opus, skills: [aria-domain-raqa]

2. 핵심 기능 구현
   - 임상 평가 (MDR Annex XV)
   - PMCF (Post-Market Clinical Follow-up)
   - 유사 장치 분석 (Equivalence)
   - 임상 문헌 검색 (PubMed, Cochrane)

3. Context7 MCP 통합
   - MDR Annex XV 라이브러리 연동
   - Clinical evaluation guidelines

4. 검증
   - [ ] CER (Clinical Evaluation Report) MDR 요구사항 충족
   - [ ] PRISMA flow diagram 준수

**성공 기준:**
- CER 작성 요청 시 MDR Annex XV 요구사항 기반 템플릿 생성
- 임상 문헌 검색 시 PRISMA flow diagram 생성

#### M-3.2.6: Notion DB 스키마 구현 (CAPA Tracker) (1일)

**Priority: High**

**작업 항목:**
1. Notion DB 생성
   - Database Name: "CAPA Tracker"
   - Properties: 12개 필드 (SPEC 참조)

2. MCP 연동
   - Notion MCP page creation 자동화
   - Due date alerts 설정
   - Relations: Risk Register, Document Registry

3. 검증
   - [ ] 모든 필드 타입 정확
   - [ ] Relations 양방향 작동
   - [ ] Due date alerts 정상 작동

**성공 기준:**
- expert-capa가 CAPA 생성 시 CAPA Tracker page 자동 생성
- Due date 미준비 시 알림 발생

#### M-3.2.7: Notion DB 스키마 구현 (Document Registry) (1일)

**Priority: High**

**작업 항목:**
1. Notion DB 생성
   - Database Name: "Document Registry"
   - Properties: 11개 필드 (SPEC 참조)

2. MCP 연동
   - Notion MCP page creation 자동화
   - Review date alerts 설정
   - Relations: CAPA Tracker, Risk Register

3. 검증
   - [ ] 모든 필드 타입 정확
   - [ ] Relations 양방향 작동
   - [ ] Version control 정상 작동

**성공 기준:**
- expert-design-control가 문서 생성 시 Document Registry page 자동 생성
- Review date 도달 시 알림 발생

### Wave 3.2 완료 조건

- [ ] 3개 에이전트 (expert-design-control, expert-capa, expert-clinical) 정상 작동
- [ ] 2개 스킬 (aria-design-control, aria-capa-process) 로드 가능
- [ ] CAPA Tracker, Document Registry Notion DB 연동 완료
- [ ] VALID 품질 게이트 통과 (Linked, Inspectable)

## Wave 3.3: Submission Foundation (2주)

### 목표

RA/QA 제출 및 감사의 핵심인 **Submission, Audit** 2개 에이전트와 관련 스킬을 구현합니다.

### Milestones

#### M-3.3.1: expert-submission 구현 (3일)

**Priority: High**

**작업 항목:**
1. 에이전트 정의 파일 생성
   - `.claude/agents/aria/expert-submission.md`
   - YAML frontmatter: model: sonnet, skills: [aria-domain-raqa, aria-submission-templates]

2. 핵심 기능 구현
   - 510(k) 제출 준비 (eCopy format)
   - PMA 제출 준비 (Original PMA format)
   - CE Marking 제출 준비 (Technical File)
   - 제출 체크리스트 (RTA criteria)

3. Notion MCP 통합
   - Document Registry에 제출 문서 연동
   - 제출 수수료 계산

4. 검증
   - [ ] eCopy format 준수
   - [ ] RTA criteria 충족

**성공 기준:**
- 510(k) 제출 준비 요청 시 eCopy 형식 문서 구조 생성
- 제출 전 RTA pass 자동 확인

#### M-3.3.2: aria-submission-templates 스킬 구현 (2일)

**Priority: High**

**작업 항목:**
1. 스킬 정의 파일 생성
   - `.claude/skills/aria-submission-templates/SKILL.md`

2. 모듈 구조 생성
   - `modules/510k-template.md` (510(k) submission)
   - `modules/pma-template.md` (PMA submission)
   - `modules/ce-marking.md` (CE Technical File)
   - `modules/e-copy.md` (eCopy format requirements)

3. 템플릿 생성
   - 510(k) Template (Traditional, Abbreviated, Special)
   - PMA Template (Original, Modular)
   - CE Technical File Template (Annex II, Annex III)

4. 검증
   - [ ] 모든 템플릿 규제 기관 요구사항 충족
   - [ ] eCopy format 정확

**성공 기준:**
- 510(k) Template에 Truthful and Accuracy statement 포함
- CE Technical File Template with Annex II/III 구조

#### M-3.3.3: expert-audit 구현 (3일)

**Priority: High**

**작업 항목:**
1. 에이전트 정의 파일 생성
   - `.claude/agents/aria/expert-audit.md`
   - YAML frontmatter: model: sonnet, skills: [aria-domain-raqa]

2. 핵심 기능 구현
   - 감사 계획 수립 (ISO 13485 + MDR 체크리스트)
   - 비적합(NC) 대응 전략
   - 감사 준비 상태 모니터링
   - Digital audit room (Notion)

3. Notion MCP 통합
   - Audit Trail DB page creation
   - Readiness assessment dashboard

4. 검증
   - [ ] ISO 13485 체크리스트 완전성
   - [ ] MDR Annex IX 체크리스트 완전성

**성공 기준:**
- Notified body audit 예정 시 ISO 13485 + MDR 기반 체크리스트 생성
- 30일 전 Readiness assessment 완료

#### M-3.3.4: aria-knowledge-mfds 스킬 구현 (2일)

**Priority: Medium**

**작업 항목:**
1. 스킬 정의 파일 생성
   - `.claude/skills/aria-knowledge-mfds/SKILL.md`

2. 모듈 구조 생성
   - `modules/korea-mdr.md` (Korea Medical Device Act)
   - `modules/device-approval.md` (Device approval process)
   - `modules/classification.md` (Korea classification rules)

3. Context7 MCP 통합
   - MFDS regulations 라이브러리 연동

4. 검증
   - [ ] Korea MDR 요구사항 정확
   - [ ] Classification rules 적용 정확

**성공 기준:**
- 한국 시장 진입 요청 시 MFDS 승인 절차 정확한 안내
- Korea classification rule 적용

#### M-3.3.5: 통합 테스트 및 검증 (3일)

**Priority: High**

**작업 항목:**
1. E2E 시나리오 테스트
   - Scenario 1: 미국 시장 진입 (Regulatory → Standards → Risk → Submission)
   - Scenario 2: CAPA 라이프사이클 (Risk → CAPA → Audit)
   - Scenario 3: 임상 평가 (Clinical → Regulatory → Submission)

2. Wave Parallelism 테스트
   - 병렬 실행 테스트 (3개 에이전트 동시 호출)
   - 순차 실행 테스트 (의존성 있는 에이전트)
   - 결과 통합 테스트 (충돌 해결)

3. Notion DB 통합 테스트
   - CAPA Tracker ↔ Risk Register ↔ Document Registry
   - Relations 양방향 작동
   - Automation triggers 정상 작동

4. VALID 품질 게이트 최종 검증
   - [ ] Verified: 모든 규제 주장에 출처 인용
   - [ ] Accurate: 모든 데이터 출처 검증
   - [ ] Linked: 추적성 매트릭스 완전
   - [ ] Inspectable: 감사 추적 완전
   - [ ] Deliverable: 제출 형식 준수

5. 성능 테스트
   - [ ] 일반 쿼리 30초 이내 응답
   - [ ] 복잡한 규제 전략 2분 이내 응답
   - [ ] Notion DB 동기화 5초 이내 완료

### Wave 3.3 완료 조건

- [ ] 2개 에이전트 (expert-submission, expert-audit) 정상 작동
- [ ] 2개 스킬 (aria-submission-templates, aria-knowledge-mfds) 로드 가능
- [ ] 모든 Notion DB (Risk Register, CAPA Tracker, Document Registry) 연동 완료
- [ ] VALID 품질 게이트 5차원 모두 통과
- [ ] E2E 시나리오 테스트 모두 통과

## 기술 접근 (Technical Approach)

### 아키텍처 원칙

1. **3계층 구조 유지**
   - Business Agents → Domain Agents → Skills
   - 의존성 방향: 하위 → 상위만 참조

2. **Progressive Disclosure 적용**
   - Level 1: ~100 tokens (항상 로드)
   - Level 2: ~5000 tokens (트리거 시 로드)
   - Level 3: modules/ (on-demand)

3. **Wave Parallelism 모델**
   - 독립적 에이전트: 병렬 개발 (Wave 내)
   - 의존적 에이전트: 순차 개발 (Wave 간)

### MCP 통합 전략

**Context7 MCP:**
- 규정 원문 검증 (Verified 차원)
- 최신 버전 확인 (Accurate 차원)
- 라이브러리: FDA, EU MDR, ISO standards

**Notion MCP:**
- CAPA Tracker, Risk Register, Document Registry
- 추적성 확보 (Linked 차원)
- Automation: Due date alerts, Status transitions

**Sequential Thinking MCP:**
- 복잡한 규제 전략 분석
- 위험-이익 분석
- 5단계 사고 과정 (Assumption → First Principles → Alternatives → Trade-offs → Bias Check)

### 파일 구조

**에이전트 정의:**
```
.claude/agents/aria/
├── expert-regulatory.md
├── expert-standards.md
├── expert-risk.md
├── expert-design-control.md
├── expert-capa.md
├── expert-clinical.md
├── expert-submission.md
└── expert-audit.md
```

**스킬 정의:**
```
.claude/skills/
├── aria-domain-raqa/
│   ├── SKILL.md
│   ├── modules/
│   │   ├── regulatory-overview.md
│   │   ├── standards-overview.md
│   │   └── risk-overview.md
│   └── examples/
├── aria-knowledge-fda/
│   ├── SKILL.md
│   └── modules/
│       ├── 21cfr820.md
│       ├── 510k.md
│       └── pma.md
├── aria-knowledge-eumdr/
│   ├── SKILL.md
│   └── modules/
├── aria-knowledge-standards/
│   ├── SKILL.md
│   └── modules/
├── aria-risk-management/
│   ├── SKILL.md
│   └── modules/
├── aria-design-control/
│   ├── SKILL.md
│   └── modules/
├── aria-capa-process/
│   ├── SKILL.md
│   └── modules/
├── aria-submission-templates/
│   ├── SKILL.md
│   └── modules/
└── aria-knowledge-mfds/
    ├── SKILL.md
    └── modules/
```

### 모델 할당 근거

**Opus (고복잡도):**
- expert-regulatory: 복수국 시장 규제 전략 최적화
- expert-standards: 표준 충돌 해석, 계층 구조 분석
- expert-risk: 위험-이익 분석, Sequential Thinking 필요
- expert-clinical: 임상 평가, 유사성 분석

**Sonnet (중복잡도):**
- expert-design-control: 프로세스 관리, 문서화
- expert-capa: 라이프사이클 관리, 근본 원인 분석
- expert-submission: 템플릿 기반, 구조화된 문서
- expert-audit: 체크리스트 기반, 준비 상태 확인

## 위험 완화 (Risk Mitigation)

### 식별된 위험

1. **위험 1:** 복잡한 규제 분석 시 Opus 응답 시간 초과
   - **확률:** Medium
   - **영향:** High (사용자 경험 저하)
   - **완화:** Sequential Thinking MCP로 체계적 분석, 응답 캐싱

2. **위험 2:** Notion DB API 속도 저하
   - **확률:** Low
   - **영향:** Medium (동기화 지연)
   - **완화:** Batch operations, Retry logic, Fallback to local cache

3. **위험 3:** 규정 원문 검증 실패 (Context7 MCP)
   - **확률:** Medium
   - **영향:** High (Verified 차원 실패)
   - **완화:** Multiple sources cross-reference, User confirmation prompt

4. **위험 4:** Wave Parallelism 결과 충돌
   - **확률:** Medium
   - **영향:** Medium (결과 통합 실패)
   - **완화:** Regulatory hierarchy 기반 우선순위, User resolution prompt

### 완화 계획

**위험 1 완화:**
- 사전: 응답 시간 모니터링, 타임아웃 설정 (2분)
- 사중: Progressive Disclosure로 토큰 최적화
- 사후: 성능 저하 시 Haiku fallback 고려

**위험 2 완화:**
- 사전: Notion API Rate Limit 확인, Batch 크기 최적화
- 사중: Exponential backoff 적용
- 사후: Local cache fallback 구현

**위험 3 완화:**
- 사전: Context7 라이브러리 ID 사전 검증
- 사중: Multiple sources cross-reference
- 사후: User confirmation workflow 구현

**위험 4 완화:**
- 사전: Regulatory hierarchy 문서화
- 사중: 충돌 감지 algorithm 구현
- 사후: User resolution template 준비

## 성공 기준 (Success Criteria)

### Wave 3.1 완료 기준
- [ ] 3개 에이전트 정상 작동
- [ ] 4개 스킬 로드 가능
- [ ] Risk Register Notion DB 연동
- [ ] VALID (V, A) 차원 통과

### Wave 3.2 완료 기준
- [ ] 3개 에이전트 정상 작동
- [ ] 2개 스킬 로드 가능
- [ ] CAPA Tracker, Document Registry Notion DB 연동
- [ ] VALID (L, I) 차원 통과

### Wave 3.3 완료 기준
- [ ] 2개 에이전트 정상 작동
- [ ] 2개 스킬 로드 가능
- [ ] 모든 Notion DB 통합 완료
- [ ] VALID (D) 차원 통과
- [ ] E2E 시나리오 테스트 통과

### 전체 프로젝트 완료 기준
- [ ] 8개 RA/QA 도메인 에이전트 구현
- [ ] 9개 도메인 스킬 구현
- [ ] 3개 Notion DB 연동
- [ ] VALID 품질 프레임워크 5차원 모두 통과
- [ ] Wave Parallelism 모델 검증
- [ ] E2E 시나리오 테스트 3개 모두 통과
- [ ] 성능 기준 충족 (30초 일반, 2분 복잡)

## 다음 단계 (Next Steps)

1. **Wave 3.1 시작:** expert-regulatory 에이전트 구현
2. **Notion DB 설정:** Risk Register 생성 및 MCP 연동
3. **스킬 구현:** aria-domain-raqa 메인 스킬부터 시작
4. **검증:** VALID 품질 게이트 각 Wave 완료 시 점검

---

## 변경 이력

| 버전 | 날짜 | 변경 사항 | 작성자 |
|------|------|-----------|--------|
| 1.0.0 | 2026-02-09 | 초기 구현 계획 작성 | ARIA Core Team |
