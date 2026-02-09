# ARIA - AI Regulatory Intelligence Assistant

## 종합 아키텍처 설계 문서

작성일: 2026-02-09
버전: 1.0.0
상태: 전략 설계 (Strategy Design)
대상 도메인: 의료기기 RA/QA (Regulatory Affairs / Quality Assurance)

---

## 목차

1. [시스템 아키텍처 개요](#1-시스템-아키텍처-개요)
2. [에이전트 카탈로그 설계](#2-에이전트-카탈로그-설계)
3. [워크플로우 설계](#3-워크플로우-설계)
4. [MCP 서버 통합 아키텍처](#4-mcp-서버-통합-아키텍처)
5. [RA/QA 도메인 설계](#5-raqa-도메인-설계)
6. [플러그인 생태계](#6-플러그인-생태계)
7. [프로젝트 구조](#7-프로젝트-구조)
8. [구현 로드맵](#8-구현-로드맵)

---

## 1. 시스템 아키텍처 개요

### 1.1 시스템 명칭 및 아이덴티티

**ARIA** - AI Regulatory Intelligence Assistant

ARIA는 의료기기 규제 업무(RA/QA)에 특화된 AI 비서 시스템이다. Claude Code 플러그인으로 구동되며, 비개발자 비즈니스 사용자가 자연어로 복잡한 규제 업무를 수행할 수 있도록 지원한다.

**명칭 후보 비교:**

| 명칭 | 장점 | 단점 | 적합도 |
|------|------|------|--------|
| ARIA (AI Regulatory Intelligence Assistant) | 기억하기 쉬움, 전문적, 확장성 높음 | 동명 프로젝트 존재 가능 | 9/10 |
| PRISM (Platform for Regulatory Intelligence & Standards Management) | 다기능 의미 전달 | 약간 길고 기술적 | 7/10 |
| RegFlow | 직관적, 워크플로우 강조 | 규제 외 영역 확장 시 이름 부적합 | 6/10 |
| Nexus-RA | 허브/연결 의미, RA 명시 | 일반적 느낌 | 5/10 |

**최종 권장: ARIA**
- 발음이 자연스럽고 기억에 남음
- "Intelligence Assistant"가 AI 비서 역할을 명확히 전달
- "Regulatory"가 도메인 전문성을 강조
- 향후 도메인 확장 시에도 부자연스럽지 않음 (AI + 도메인명 + Intelligence Assistant)

### 1.2 핵심 철학

**Read-Think-Write-Verify: 모든 정보 노동자의 보편적 패턴**

ARIA는 "Read-Think-Write-Verify"가 모든 정보 노동자의 보편적 작업 패턴임을 전제로 합니다. RA/QA 업무는 이 패턴의 전형적인 예입니다:

- **Read**: 규정/표준 문서 읽기, 기존 문서 검토, 선행 사례 조사
- **Think**: 규제 해석, 요구사항 분석, 규제 전략 수립
- **Write**: 규제 문서 작성, 보고서 작성, 제출 패키지 구성
- **Verify**: 규정 준수 검토, 동료 검토, 품질 게이트 통과

**MoAI-ADK와의 관계: 원칙 차용, 경쟁 아님**

ARIA는 MoAI-ADK의 "복제"가 아니라 MoAI-ADK의 "원칙"을 RA/QA 도메인에 재해석한 것입니다.

| 측면 | MoAI-ADK (개발) | ARIA (RA/QA) | 관계 |
|------|-----------------|---------------|------|
| **핵심 원칙** | 에이전트 기반 오케스트레이션 | 에이전트 기반 오케스트레이션 | 동일 원칙 |
| **품질 프레임워크** | TRUST 5 (코드 품질) | VALID (규제 준수) | 원칙 차용 |
| **단계적 워크플로우** | Plan-Run-Sync | Brief-Execute-Deliver | 도메인 언어 적응 |
| **플러그인 구조** | 코어 + 도메인 분리 | Cowork 생태계 통합 | 구조 차용 |
| **토큰 최적화** | Progressive Disclosure | Progressive Disclosure | 동일 전략 |

**차별점: 도메인 특화**

| 측면 | MoAI-ADK | ARIA |
|------|----------|-------|
| 대상 사용자 | 개발자 | RA/QA 실무자 (비개발자) |
| 산출물 | 코드, 테스트, API | 규제 문서, 보고서, 제출 패키지 |
| 품질 기준 | TRUST 5 (코드 품질) | VALID (규제 준수) |
| 워크플로우 | Plan-Run-Sync (균형적) | Brief 중심 (비균형적) |
| 버전 관리 | Git (코드) | Notion DB (문서) |

**MoAI-ADK와의 결정적 차이: "파일 소유권" vs "상호참조"**

- MoAI-ADK: frontend/*.tsx vs backend/*.go (명확한 소유권)
- ARIA: 모든 문서 섹션이 상호참조 (Traceability Matrix)

이 차이로 인해 ARIA는 MoAI의 "고정 팀" 모델 대신 "동적 팀 결합" 모델을 채택합니다.

**ARIA 설계 원칙:**

1. **자연어 우선 (Natural Language First)**: 모든 상호작용은 자연어로 이루어진다. 명령어, 코드, 설정 파일을 사용자에게 노출하지 않는다.

2. **규제 정확성 (Regulatory Accuracy)**: AI가 생성한 모든 내용은 해당 규정/표준의 원문과 대조 검증 가능해야 한다. 출처가 불확실한 정보는 명확히 표시한다.

3. **추적 가능성 (Traceability)**: 모든 결정, 변경, 승인은 감사 추적(audit trail)이 유지된다. 규제 심사 시 "왜 이 결정을 했는가"를 소급 확인할 수 있다.

4. **단계별 확인 (Progressive Confirmation)**: 중요한 규제 결정에는 사용자 승인 체크포인트가 존재한다. AI가 단독으로 규제 판단을 확정하지 않는다.

5. **지식 누적 (Knowledge Accumulation)**: 프로젝트별로 학습한 규제 해석, 선례, 결정 근거가 축적되어 시간이 지날수록 정확도가 향상된다.

6. **Cowork 생태계 통합** (확장성): ARIA는 Cowork 플러그인 생태계의 일부로, 독립적으로 실행 가능하면서 Cowork 공통 기능과 호환됩니다.

### 1.3 시스템 아키텍처 다이어그램

```
+------------------------------------------------------------------+
|                         ARIA Orchestrator                         |
|                    (Claude Code Plugin Core)                      |
+------------------------------------------------------------------+
         |                    |                    |
    [Brief Phase]       [Execute Phase]      [Deliver Phase]
         |                    |                    |
+--------+--------+  +-------+--------+  +--------+--------+
| Intent Analysis  |  | Agent Dispatch |  | Quality Review  |
| Scope Definition |  | Task Execution |  | Format & Export |
| Reg. Mapping     |  | Quality Gates  |  | Distribution    |
+------------------+  +----------------+  +-----------------+
         |                    |                    |
+------------------------------------------------------------------+
|                      Agent Layer (2-Tier)                          |
+-------------------+----------------------+-----------------------+
| Core Agents       | Business Agents      | RA/QA Agents          |
| - orchestrator    | - expert-writer      | - expert-regulatory   |
| - manager-docs    | - expert-analyst     | - expert-standards    |
| - manager-quality | - expert-reviewer    | - expert-risk         |
| - manager-project | - expert-researcher  | - expert-design-ctrl  |
|                   |                      | - expert-capa         |
|                   |                      | - expert-clinical     |
|                   |                      | - expert-submission   |
|                   |                      | - expert-audit        |
+-------------------+----------------------+-----------------------+
         |                    |                    |
+------------------------------------------------------------------+
|                     Integration Layer                              |
+------------------+------------------+------------------+----------+
| Notion MCP       | Google Workspace | Sequential       | Context7 |
| (Knowledge Hub)  | (Collaboration)  | Thinking MCP     | MCP      |
+------------------+------------------+------------------+----------+
```

---

## 2. 에이전트 카탈로그 설계

### 2.1 에이전트 아키텍처 개요

ARIA는 3계층 에이전트 구조를 채택한다:

- **Core Layer**: 시스템 운영 및 오케스트레이션
- **Business Layer**: 범용 비즈니스 업무 수행
- **Domain Layer**: RA/QA 전문 업무 수행

### 2.2 에이전트 명명 규칙

```
패턴: {역할}-{전문분야}
역할: manager | expert | builder
전문분야: 소문자-하이픈 연결

예시:
  manager-docs          (Core: 문서 관리)
  expert-writer         (Business: 기술 작성)
  expert-regulatory     (Domain: 규제 전문)
```

### 2.3 Core Layer 에이전트 (4개)

#### orchestrator - 메인 오케스트레이터

```yaml
name: orchestrator
description: >
  ARIA의 중앙 오케스트레이터. 사용자 요청을 분석하고
  적절한 전문 에이전트에 위임한다. 모든 사용자 상호작용의
  단일 진입점 역할을 수행한다.
model: opus
permissionMode: default
tools: Task, AskUserQuestion, Read, Grep, Glob, Bash
skills: aria-core, aria-domain-raqa, aria-workflow
```

**역할 및 책임:**
- 사용자 의도 분석 및 워크플로우 라우팅
- 에이전트 위임 및 결과 통합
- 사용자 승인 체크포인트 관리
- 오류 발생 시 평이한 언어로 안내

#### manager-docs - 문서 관리자

```yaml
name: manager-docs
description: >
  문서 생성, 버전 관리, 승인 워크플로우 관리.
  Notion MCP를 통한 문서 저장 및 검색을 담당한다.
model: sonnet
permissionMode: default
tools: Read, Write, Edit, Grep, Glob, Bash, mcp__claude_ai_Notion
skills: aria-core, aria-templates, aria-domain-raqa
```

**역할 및 책임:**
- 문서 생성 및 편집 오케스트레이션
- 문서 버전 관리 (Notion DB 연동)
- 리뷰/승인 워크플로우 실행
- 문서 템플릿 관리 및 적용
- 문서 간 상호참조(cross-reference) 관리

#### manager-quality - 품질 관리자

```yaml
name: manager-quality
description: >
  VALID 프레임워크 기반 품질 게이트 관리.
  규제 준수 여부 검증 및 감사 추적 유지.
model: sonnet
permissionMode: plan
tools: Read, Grep, Glob
skills: aria-core, aria-quality-valid, aria-domain-raqa
```

**역할 및 책임:**
- VALID 프레임워크 품질 게이트 실행
- 규정 준수 체크리스트 관리
- 감사 추적(audit trail) 유지
- 품질 보고서 생성
- 인용 출처 검증

#### manager-project - 프로젝트 관리자

```yaml
name: manager-project
description: >
  프로젝트 일정 관리, 마일스톤 추적, 담당자 할당.
  규제 제출 타임라인 및 데드라인 관리를 담당한다.
model: sonnet
permissionMode: default
tools: Read, Write, Grep, Glob, mcp__claude_ai_Notion, mcp__google-calendar
skills: aria-core, aria-workflow
```

**역할 및 책임:**
- 프로젝트 타임라인 관리
- 규제 제출 데드라인 추적
- 작업 할당 및 진행 상태 모니터링
- Notion/Google Calendar 연동

### 2.4 Business Layer 에이전트 (4개)

#### expert-writer - 기술 작성 전문가

```yaml
name: expert-writer
description: >
  기술 문서 작성 전문가. 규제 문서, 보고서, 기술 파일을
  표준 형식에 맞게 작성한다. 명확하고 간결한 기술 문체를
  사용하며, 규제 용어를 정확히 적용한다.
model: sonnet
permissionMode: acceptEdits
tools: Read, Write, Edit, Grep, Glob
skills: aria-core, aria-templates, aria-writing-style
```

**역할 및 책임:**
- 규제 문서 초안 작성
- 템플릿 기반 문서 생성
- 용어 일관성 검증
- 문서 포맷팅 및 스타일 적용
- 다국어 문서 지원 (영어/한국어)

#### expert-analyst - 데이터 분석 전문가

```yaml
name: expert-analyst
description: >
  데이터 분석 및 해석 전문가. 임상 데이터, 성능 데이터,
  불만 동향, 시장 데이터를 분석하여 의미 있는 통찰을 제공한다.
model: sonnet
permissionMode: plan
tools: Read, Grep, Glob, Bash, mcp__claude_ai_Notion
skills: aria-core, aria-analysis
```

**역할 및 책임:**
- 임상 데이터 분석 및 해석
- 불만(complaint) 동향 분석
- 성능 데이터 통계 분석
- Predicate device 비교 분석
- 위험-편익(risk-benefit) 분석 지원

#### expert-reviewer - 문서 검토 전문가

```yaml
name: expert-reviewer
description: >
  문서 검토 및 규정 준수 확인 전문가. 작성된 문서가
  해당 규정/표준 요구사항을 충족하는지 검증한다.
model: opus
permissionMode: plan
tools: Read, Grep, Glob, mcp__context7
skills: aria-core, aria-quality-valid, aria-domain-raqa
```

**역할 및 책임:**
- 문서 내용의 규정 준수 검토
- 누락된 요구사항 식별
- 용어 및 참조의 정확성 확인
- 검토 의견 문서화
- 최종 승인 전 품질 확인

#### expert-researcher - 규제 리서치 전문가

```yaml
name: expert-researcher
description: >
  규제 정보 수집 및 조사 전문가. FDA 가이던스, 표준 업데이트,
  선행 기기(predicate device) 검색, 규제 동향 파악을 담당한다.
model: haiku
permissionMode: plan
tools: Read, Grep, Glob, WebSearch, WebFetch, mcp__context7
skills: aria-core, aria-research
```

**역할 및 책임:**
- FDA 데이터베이스 검색 (510(k) Summary, MAUDE, Classification)
- 표준/가이던스 최신 버전 확인
- Predicate device 검색 및 비교
- 규제 동향 및 변경사항 모니터링
- 경쟁 기기 규제 현황 조사

### 2.5 Domain Layer - RA/QA 전문 에이전트 (8개)

#### expert-regulatory - 규제 전략 전문가

```yaml
name: expert-regulatory
description: >
  의료기기 규제 전략 수립 전문가. FDA, EU MDR, MFDS 등
  각국 규제 요구사항을 분석하고 최적의 인허가 전략을 수립한다.
  510(k), PMA, De Novo, CE Marking 경로 분석을 담당한다.
model: opus
permissionMode: plan
tools: Read, Grep, Glob, WebSearch, WebFetch, mcp__context7, mcp__sequential-thinking
skills: aria-core, aria-domain-raqa, aria-knowledge-fda, aria-knowledge-eumdr
```

**핵심 역량:**
- FDA 분류(Classification) 결정 지원
- 규제 경로(Regulatory Pathway) 분석: 510(k) vs PMA vs De Novo
- EU MDR 분류 및 적합성 평가 경로 결정
- 한국 MFDS 인허가 전략
- 각국 규제 요구사항 비교 분석
- 규제 전략 문서(Regulatory Strategy Document) 작성 지원

#### expert-standards - 표준 해석 전문가

```yaml
name: expert-standards
description: >
  의료기기 관련 국제 표준 해석 및 적용 전문가.
  ISO 13485, IEC 62304, IEC 60601, ISO 14971 등
  핵심 표준의 요구사항을 해석하고 적용 방안을 제시한다.
model: opus
permissionMode: plan
tools: Read, Grep, Glob, mcp__context7, mcp__sequential-thinking
skills: aria-core, aria-domain-raqa, aria-knowledge-standards
```

**핵심 역량:**
- ISO 13485:2016 품질경영시스템 요구사항 해석
- IEC 62304:2006+A1:2015 소프트웨어 수명주기 프로세스
- IEC 60601-1:2005+A1+A2 의료용 전기기기 안전
- ISO 14971:2019 위험관리 적용
- IEC 62366-1:2015 유저빌리티 엔지니어링
- ISO 10993 시리즈 생체적합성 평가
- 표준 간 상호참조 및 갭 분석(Gap Analysis)

#### expert-risk - 위험관리 전문가

```yaml
name: expert-risk
description: >
  ISO 14971 기반 위험관리 프로세스 전문가.
  위험 식별, 분석, 평가, 통제, 잔여위험 수용성 판단을
  체계적으로 수행하고 위험관리 파일을 관리한다.
model: opus
permissionMode: acceptEdits
tools: Read, Write, Edit, Grep, Glob, mcp__claude_ai_Notion
skills: aria-core, aria-domain-raqa, aria-risk-management
```

**핵심 역량:**
- Hazard Identification (위험원 식별)
- Failure Mode and Effects Analysis (FMEA)
- Fault Tree Analysis (FTA)
- Risk Estimation (심각도 x 발생확률)
- Risk Evaluation (허용 가능성 판단)
- Risk Control Measures (위험 통제 수단)
- Residual Risk Assessment (잔여위험 평가)
- Risk-Benefit Analysis (위험-편익 분석)
- 위험관리 보고서 생성
- Risk Matrix / Risk Register 관리

#### expert-design-control - 설계관리 전문가

```yaml
name: expert-design-control
description: >
  의료기기 설계관리(Design Control) 프로세스 전문가.
  21 CFR 820.30 및 ISO 13485 Clause 7.3 요구사항에 따른
  DHF, DMR, DHR 관리를 담당한다.
model: sonnet
permissionMode: acceptEdits
tools: Read, Write, Edit, Grep, Glob, mcp__claude_ai_Notion
skills: aria-core, aria-domain-raqa, aria-design-control
```

**핵심 역량:**
- Design Input 캡처 및 문서화
- Design Output 문서 작성
- Design Review 체크리스트 및 회의록 지원
- Design Verification Plan/Report 작성
- Design Validation Protocol/Report 작성
- Design Transfer 체크리스트
- Traceability Matrix 생성 및 유지
- Design History File (DHF) 구성
- Device Master Record (DMR) 관리
- Device History Record (DHR) 추적

#### expert-capa - CAPA 관리 전문가

```yaml
name: expert-capa
description: >
  CAPA(Corrective and Preventive Action) 프로세스 전문가.
  문제 식별, 근본원인 분석, 시정/예방 조치 수립,
  효과성 검증까지의 전체 CAPA 수명주기를 관리한다.
model: sonnet
permissionMode: acceptEdits
tools: Read, Write, Edit, Grep, Glob, mcp__claude_ai_Notion
skills: aria-core, aria-domain-raqa, aria-capa-process
```

**핵심 역량:**
- CAPA 개시(Initiation) 문서 작성
- 근본원인 분석(Root Cause Analysis): 5 Whys, Fishbone, Pareto
- 시정조치(Corrective Action) 계획 수립
- 예방조치(Preventive Action) 계획 수립
- CAPA 실행 모니터링
- 효과성 검증(Effectiveness Verification) 계획 및 실행
- CAPA 종료(Closure) 문서화
- CAPA 동향 분석 및 보고

#### expert-clinical - 임상평가 전문가

```yaml
name: expert-clinical
description: >
  임상평가(Clinical Evaluation) 및 시판후조사(Post-Market Surveillance)
  전문가. CER/PMCF/PMS 보고서 작성, 임상 문헌 검토,
  부작용 보고를 담당한다.
model: opus
permissionMode: acceptEdits
tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch, mcp__claude_ai_Notion
skills: aria-core, aria-domain-raqa, aria-clinical-evaluation
```

**핵심 역량:**
- Clinical Evaluation Report (CER) 작성 - EU MDR
- Clinical Evaluation Plan (CEP) 수립
- Literature Review 수행 (체계적 문헌 검색)
- Post-Market Clinical Follow-up (PMCF) 계획/보고
- Post-Market Surveillance Report (PMSR) 작성
- Periodic Safety Update Report (PSUR) 작성
- 부작용 보고서 (MedWatch, MDR Report) 작성
- Clinical Investigation Plan 지원

#### expert-submission - 인허가 제출 전문가

```yaml
name: expert-submission
description: >
  규제 제출물(Regulatory Submission) 준비 전문가.
  510(k), PMA, De Novo, CE Technical Documentation 등
  제출 패키지 구성 및 검토를 담당한다.
model: sonnet
permissionMode: acceptEdits
tools: Read, Write, Edit, Grep, Glob, mcp__claude_ai_Notion
skills: aria-core, aria-domain-raqa, aria-submission-templates
```

**핵심 역량:**
- 510(k) Submission 패키지 구성
  - Indications for Use Statement
  - Device Description
  - Substantial Equivalence Comparison
  - Performance Data Summary
  - Biocompatibility Assessment
  - Software Documentation (IEC 62304)
  - Labeling
  - Sterilization Information
- PMA Application 지원
- De Novo Classification Request 지원
- EU MDR Technical Documentation 구성
- STED (Summary Technical Documentation) 작성
- FDA eCopy 준비 체크리스트
- eSTAR 템플릿 작성 지원

#### expert-audit - 감사 관리 전문가

```yaml
name: expert-audit
description: >
  내부/외부 감사 준비 및 관리 전문가.
  ISO 13485 감사 체크리스트 작성, Finding 관리,
  감사 대응 문서 준비를 담당한다.
model: sonnet
permissionMode: acceptEdits
tools: Read, Write, Edit, Grep, Glob, mcp__claude_ai_Notion
skills: aria-core, aria-domain-raqa, aria-audit-management
```

**핵심 역량:**
- 내부감사 프로그램 수립
- 감사 체크리스트 생성 (ISO 13485, 21 CFR 820 기반)
- 감사 Finding 문서화 및 분류 (Major/Minor/Observation)
- Corrective Action Response 작성
- CAPA 연계 관리
- FDA 실사(Inspection) 대응 준비
- Notified Body 감사 대응
- 감사 보고서 작성
- 감사 이력 관리 및 동향 분석

### 2.6 에이전트 역량 매트릭스

| 에이전트 | 모델 | 계층 | 읽기 | 쓰기 | Notion | Google | Web | 비고 |
|----------|------|------|------|------|--------|--------|-----|------|
| orchestrator | opus | Core | O | X | X | X | X | 위임 전용, 직접 작업 금지 |
| manager-docs | sonnet | Core | O | O | O | X | X | 문서 수명주기 관리 |
| manager-quality | sonnet | Core | O | X | X | X | X | 읽기 전용, 품질 검증 |
| manager-project | sonnet | Core | O | O | O | O | X | 프로젝트/일정 관리 |
| expert-writer | sonnet | Business | O | O | X | X | X | 문서 작성 |
| expert-analyst | sonnet | Business | O | X | O | X | X | 데이터 분석 |
| expert-reviewer | opus | Business | O | X | X | X | O | 검토/검증 (고정확도) |
| expert-researcher | haiku | Business | O | X | X | X | O | 대량 검색 (비용 효율) |
| expert-regulatory | opus | Domain | O | X | X | X | O | 규제 전략 (고정확도) |
| expert-standards | opus | Domain | O | X | X | X | X | 표준 해석 (고정확도) |
| expert-risk | opus | Domain | O | O | O | X | X | 위험관리 |
| expert-design-control | sonnet | Domain | O | O | O | X | X | 설계관리 |
| expert-capa | sonnet | Domain | O | O | O | X | X | CAPA 관리 |
| expert-clinical | opus | Domain | O | O | O | X | O | 임상평가 (고정확도) |
| expert-submission | sonnet | Domain | O | O | O | X | X | 제출물 준비 |
| expert-audit | sonnet | Domain | O | O | O | X | X | 감사 관리 |

**모델 선택 기준:**
- **opus**: 규제 해석, 전략 수립 등 정확성이 극히 중요한 업무. 잘못된 규제 해석은 인허가 실패로 이어질 수 있음.
- **sonnet**: 문서 작성, 프로세스 관리 등 품질과 비용의 균형이 필요한 업무. 충분한 정확도를 유지하면서 비용 효율적.
- **haiku**: 대량 검색, 초기 스크리닝 등 속도와 비용 효율이 중요한 업무. 결과는 상위 에이전트가 검증.

---

## 3. 워크플로우 설계

### 3.1 Brief-Execute-Deliver 워크플로우

MoAI의 Plan-Run-Sync를 비즈니스 맥락에 맞게 재설계한 3단계 워크플로우이다.

**핵심 차이점**: 개발 워크플로우와 달리 RA/QA는 **Brief 단계(규제 분석 및 전략 수립)**이 가장 중요하다. 이 단계에서의 결정이 전체 프로젝트의 방향성과 성패를 결정한다.

#### Phase 1: BRIEF (업무 이해 및 전략 수립)

**MoAI 대응**: Plan Phase (SPEC 생성)
**토큰 예산**: 120,000 (60%)
**핵심 활동**: 규제 분석 및 전략 수립

**목적**: 사용자의 요청을 이해하고, 관련 규정/표준을 식별하며, **데이터베이스 중심의 규제 전략**을 수립한다.

**세부 단계:**

1. **Intent Analysis (의도 분석)**
   - 사용자 요청의 자연어 분석
   - 업무 유형 분류 (문서 작성, 분석, 검토, 제출 준비 등)
   - 해당 규정/표준 자동 매핑
   - 필요 에이전트 식별

2. **Regulatory Strategy Brief (규제 전략 브리프)**
   - **Notion 규제 지식 베이스 조회**
   - 적용 법령 식별 (의료기기법/체외진단기기법/디지털의료제품법)
   - MFDS 등급 분류 결정 (Class I/II/III/IV)
   - 기존 선례/유사 사례 검색
   - Predicate device 후보군 추출

3. **Scope Definition (범위 정의)**
   - AskUserQuestion으로 범위 확인
   - 제품/기기 정보 수집
   - 적용 규제 시장 확인 (FDA, EU, MFDS 등)
   - 기존 문서/데이터 확인

4. **Gatekeeper Checkpoint (승인 체크포인트)**
   - 규제 전략 브리프 사용자 승인
   - 전략 수정 요청 시 재분석 수행
   - **승인 후에만 Execute 단계 진입**

5. **Action Plan (실행 계획)**
   - 필요 작업 목록 생성
   - 에이전트 위임 계획
   - 예상 산출물 정의
   - 추가 승인 체크포인트 설정

**Regulatory Strategy Brief 템플릿:**

```markdown
# 규제 전략 브리프 (Regulatory Strategy Brief)

## 1. 제품/기기 정보
- 제품명: [입력 필요]
- 기기 유형: [의료기기/체외진단/디지털치료제]
- 적용 법령: [의료기기법/체외진단의료기기법/디지털의료제품법]
- MFDS 등급: [Class I/II/III/IV]

## 2. 규제 분석
### 2.1 한국 (MFDS)
- 법적 분류: Class [I/II/III/IV]
- 인허가 경로: [등록/허가/신고/심사]
- 필요 문서: [목록]

### 2.2 미국 (FDA)
- Product Code: [코드]
- Regulation Number: [21 CFR xxx.xxx]
- 규제 경로: [510(k)/PMA/De Novo/HDE]

### 2.3 유럽 (EU MDR)
- 분류: [Class I/IIa/IIb/III]
- 적합성 평가 경로: [Module 선택]

## 3. 데이터베이스 조회 결과
- Predicate 후보군: [N개 목록]
- 유사 사례: [N건]
- 관련 가이던스: [N건]

## 4. 전략 제안
- [전략 요약]

## 5. 승인
- [ ] 규제 전략 승인 및 Execute 단계 진입
- [ ] 수정 요청 (사유 입력)
```

**Wave Parallelism 모델:**

Brief 단계 내에서 Wave 기반 병렬 처리를 수행한다:

```
Wave 1: 기초 분석 (Database 중심)
├─ expert-researcher: 데이터베이스 검색 (병렬)
├─ expert-regulatory: 법령 식별 (병렬)
└─ expert-standards: 표준 매핑 (병렬)

Wave 2: 종합 분석 (Wave 1 결과 기반)
├─ expert-regulatory: 규제 전략 수립 (직렬 의존)
├─ expert-analyst: 데이터 시장 분석 (병렬)
└─ orchestrator: 종합 브리프 작성 (종합)

Wave 3: Gatekeeper Review (순차적)
└─ 사용자 승인: 브리프 검토 및 결정
```

**예시 - 사용자 요청:** "510(k) 제출을 준비해야 합니다"

```
ARIA Brief:

1. 의도: 510(k) 제출 패키지 준비
2. 확인 사항:
   - 제품명 및 분류 (Product Code)
   - Predicate device 정보
   - 기존 테스트 데이터 유무
   - 소프트웨어 포함 여부
   - 목표 제출 일정
3. 실행 계획:
   - [expert-researcher] Predicate device 검색
   - [expert-regulatory] 규제 전략 검토
   - [expert-submission] 제출 패키지 구성
   - [expert-writer] 각 섹션 문서 작성
   - [expert-reviewer] 최종 검토
4. 승인 체크포인트:
   - Predicate device 선정 승인
   - Substantial Equivalence 논리 승인
   - 최종 패키지 승인
```

#### Phase 2: EXECUTE (실행)

**MoAI 대응**: Run Phase (DDD 구현)
**토큰 예산**: 60,000 (30%)
**핵심 활동**: 문서 작성 및 검토

**목적**: Brief에서 수립된 계획에 따라 실제 업무를 수행한다.

**Dynamic Team Composition (동적 팀 구성):**

RA/QA 워크플로우는 파일 소유권이 아닌 **문서 섹션/단계별 책임**을 기반으로 동적 팀을 구성한다.

| 업무 단계 | 참여 에이전트 | 작업 방식 |
|-----------|--------------|-----------|
| Research | expert-researcher + expert-regulatory | 병렬 |
| Draft | expert-writer + [domain expert] | 협업 |
| Review | expert-reviewer + manager-quality | 순차 |
| Refine | expert-writer (수정) | 단일 |

**세부 단계:**

1. **Research (조사)**
   - expert-researcher가 필요 정보 수집
   - 규정/표준 원문 참조
   - 선행 사례 조사
   - Notion 데이터베이스에서 유사 문서 검색

2. **Draft (초안 작성)**
   - expert-writer가 문서 초안 생성
   - 템플릿 기반 구조화
   - 데이터/근거 삽입
   - Domain 전문가 협업 (해당 시)

3. **Review (검토)**
   - expert-reviewer가 규정 준수 확인
   - manager-quality가 VALID 게이트 실행
   - 수정 필요 사항 피드백

4. **Refine (보완)**
   - 검토 의견 반영
   - 추가 데이터/근거 보강
   - 최종 품질 확인

**품질 체크포인트 (각 작업 완료 시):**
- 규정 참조의 정확성
- 데이터 출처의 명시성
- 문서 형식의 적합성
- 용어 일관성

#### Phase 3: DELIVER (전달)

**MoAI 대응**: Sync Phase (문서 동기화)
**토큰 예산**: 20,000 (10%)
**핵심 활동**: 최종 검토 및 전달

**목적**: 완성된 산출물을 최종 검토하고, 적절한 형식으로 전달한다.

**세부 단계:**

1. **Final Quality Review (최종 품질 검토)**
   - VALID 프레임워크 전체 게이트 통과 확인
   - 문서 간 상호참조 정합성 확인
   - 감사 추적 완전성 확인

2. **Format & Export (형식 변환 및 내보내기)**
   - 목적에 맞는 형식으로 변환 (PDF, Word, Notion 페이지)
   - 제출용 패키지 구성
   - eCopy/eSTAR 형식 적합성 확인 (해당 시)

3. **Distribution (배포)**
   - Notion에 최종 버전 저장
   - 관련 이해관계자에 알림
   - 버전 이력 기록
   - 다음 단계 안내

4. **Knowledge Update (지식 업데이트)**
   - 학습된 내용을 지식 베이스에 반영
   - 새로운 선례/해석 기록
   - 향후 유사 업무를 위한 참고자료 축적

### 3.2 VALID 품질 프레임워크

MoAI의 TRUST 5를 규제 비즈니스 맥락에 맞게 재설계한 품질 프레임워크이다.

| VALID 차원 | 정의 | MoAI TRUST 대응 | 검증 방법 |
|------------|------|-----------------|-----------|
| **V**erified | 규정/표준 원문과 대조하여 내용 정확성 검증 | Tested | 규정 참조 대조, 출처 확인 |
| **A**ccurate | 데이터, 수치, 참조가 정확하고 최신 상태 | Readable | 데이터 소스 확인, 날짜 검증 |
| **L**inked | 요구사항-문서-근거 간 추적성(traceability) 확보 | Trackable | Traceability Matrix 검증 |
| **I**nspectable | 감사 추적이 유지되고, 결정 근거가 문서화됨 | Secured | Audit Trail 완전성 확인 |
| **D**eliverable | 산출물이 제출/보고 형식 요구사항 충족 | Unified | 템플릿 적합성, 형식 검증 |

**VALID 게이트 실행 체크리스트:**

```
V - Verified (검증됨)
  [ ] 인용된 규정/표준 조항이 실제 원문과 일치하는가?
  [ ] 규제 해석이 현행 가이던스에 부합하는가?
  [ ] 기술적 주장이 근거 데이터로 뒷받침되는가?

A - Accurate (정확함)
  [ ] 모든 수치/데이터가 출처와 일치하는가?
  [ ] 참조된 문서/표준이 최신 버전인가?
  [ ] 날짜, 버전, 식별번호가 정확한가?

L - Linked (연결됨)
  [ ] 모든 요구사항이 해당 문서/근거와 연결되어 있는가?
  [ ] Traceability Matrix가 완전한가?
  [ ] 변경사항이 영향받는 문서에 반영되어 있는가?

I - Inspectable (검사 가능)
  [ ] 모든 결정의 근거(rationale)가 기록되어 있는가?
  [ ] 변경 이력이 추적 가능한가?
  [ ] 검토/승인 기록이 존재하는가?

D - Deliverable (전달 가능)
  [ ] 산출물이 요구된 형식(template)에 맞는가?
  [ ] 제출 기관의 형식 요구사항을 충족하는가?
  [ ] 첨부 파일, 참조 문서가 모두 포함되어 있는가?
```

### 3.3 사용자 상호작용 설계

비개발자 사용자를 위한 상호작용 원칙:

**입력 방식:**
- 자연어 텍스트 (한국어/영어)
- 파일 첨부 (기존 문서, 데이터)
- 선택형 응답 (AskUserQuestion: 최대 4개 옵션)

**출력 방식:**
- 구조화된 Markdown 보고서
- 진행 상황 안내 (현재 단계, 다음 단계)
- 결정 필요 사항 하이라이트
- 평이한 언어 사용 (기술 용어 최소화)

**오류 처리:**
```
-- 기술적 오류 메시지 (사용하지 않음) --
"Error: MCP connection timeout after 15000ms. Retry with exponential backoff."

-- ARIA 오류 메시지 (사용) --
"Notion 데이터베이스 연결에 일시적인 문제가 발생했습니다.
 자동으로 재시도하고 있습니다.
 문제가 계속되면 Notion 접속 상태를 확인해 주세요.
 (3회 재시도 중 1회차)"
```

**승인 체크포인트 예시:**
```
[검토 요청] Predicate Device 선정

제안된 Predicate Device:
  - K201234: XYZ Medical Monitor (Class II, Product Code: DQA)
  - 선정 근거: 동일 기술 원리, 유사 사용 목적

비교 분석 요약:
  - 기술적 특성: 5개 항목 중 4개 동등, 1개 차이 (해상도)
  - 사용 목적: 동일
  - 환자 접촉: 동일 (비침습)

이 Predicate Device로 진행하시겠습니까?
  1. 승인 - 이 기기로 진행
  2. 대안 검토 - 다른 후보 기기 제시 요청
  3. 수정 요청 - 비교 분석 보완 필요
  4. 보류 - 추가 검토 후 결정
```

### 3.4 커맨드 구조

ARIA의 사용자 진입점은 `/aria` 슬래시 커맨드이다.

```
/aria                          -- 자연어 업무 요청 (기본)
/aria brief "510(k) 제출 준비"  -- BRIEF 단계 시작
/aria execute TASK-001          -- EXECUTE 단계 실행
/aria deliver TASK-001          -- DELIVER 단계 실행
/aria search "predicate device" -- 규제 정보 검색
/aria template "510k"           -- 템플릿 조회/생성
/aria status                    -- 현재 진행 상태 확인
/aria knowledge                 -- 지식 베이스 조회
```

**자연어 라우팅 예시:**

| 사용자 입력 | 라우팅 | 에이전트 체인 |
|-------------|--------|---------------|
| "510(k) 제출을 준비해야 해" | brief + execute | regulatory -> submission -> writer |
| "이 기기의 위험분석을 해줘" | execute | risk -> analyst |
| "CAPA를 열어야 해" | execute | capa |
| "이 문서가 규정에 맞는지 확인해줘" | execute | reviewer -> standards |
| "FDA 가이던스 최신 버전이 뭐야?" | search | researcher |
| "내부감사 체크리스트를 만들어줘" | execute | audit -> writer |
| "CER을 작성해야 해" | brief + execute | clinical -> writer |

---

## 4. MCP 서버 통합 아키텍처

### 4.1 MCP 서버 구성

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "claude_ai_Notion"],
      "env": {
        "NOTION_API_KEY": "${NOTION_API_KEY}"
      }
    },
    "google-workspace": {
      "command": "npx",
      "args": ["-y", "@anthropic/google-workspace-mcp"],
      "env": {
        "GOOGLE_CREDENTIALS": "${GOOGLE_CREDENTIALS}"
      }
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

### 4.2 Notion MCP - 중앙 지식 허브

Notion은 ARIA의 중앙 데이터 저장소이자 사용자 인터페이스 역할을 한다.

**Notion 데이터베이스 스키마:**

#### DB 1: Regulatory Requirements (규제 요구사항)

| 필드명 | 타입 | 설명 |
|--------|------|------|
| ID | Title | 요구사항 고유 ID (예: REQ-FDA-001) |
| Standard | Select | 적용 표준/규정 (ISO 13485, 21 CFR 820 등) |
| Section | Text | 조항 번호 (예: 7.3.2) |
| Requirement | Rich Text | 요구사항 전문 |
| Category | Multi-Select | 분류 (Design Control, Risk, CAPA 등) |
| Applicability | Select | 적용 대상 (SW, HW, General) |
| Evidence | Relation | 연결된 근거 문서 |
| Status | Select | 준수 상태 (Compliant, Gap, N/A) |
| Notes | Rich Text | 해석/적용 노트 |

#### DB 2: Document Registry (문서 등록부)

| 필드명 | 타입 | 설명 |
|--------|------|------|
| Doc ID | Title | 문서 고유 ID (예: DOC-DHF-001) |
| Title | Text | 문서 제목 |
| Type | Select | 문서 유형 (SOP, WI, Form, Report 등) |
| Version | Text | 현재 버전 |
| Status | Select | 상태 (Draft, Review, Approved, Obsolete) |
| Owner | People | 문서 책임자 |
| Review Date | Date | 다음 정기 검토일 |
| Related Reqs | Relation | 연결된 요구사항 |
| Change History | Rich Text | 변경 이력 |

#### DB 3: CAPA Tracker

| 필드명 | 타입 | 설명 |
|--------|------|------|
| CAPA ID | Title | CAPA 번호 (예: CAPA-2026-001) |
| Type | Select | 유형 (Corrective, Preventive, Both) |
| Source | Select | 출처 (Complaint, Audit, NCR, Trend) |
| Description | Rich Text | 문제 설명 |
| Root Cause | Rich Text | 근본원인 |
| Action Plan | Rich Text | 조치 계획 |
| Status | Select | 상태 (Open, In Progress, Verification, Closed) |
| Due Date | Date | 완료 기한 |
| Assignee | People | 담당자 |
| Effectiveness | Select | 효과성 (Pending, Effective, Not Effective) |

#### DB 4: Risk Register (위험 등록부)

| 필드명 | 타입 | 설명 |
|--------|------|------|
| Risk ID | Title | 위험 ID (예: RISK-001) |
| Hazard | Text | 위험원 |
| Hazardous Situation | Rich Text | 위험 상황 |
| Harm | Text | 피해 |
| Severity | Select | 심각도 (1-5) |
| Probability | Select | 발생확률 (1-5) |
| Risk Level | Formula | 위험 수준 (심각도 x 확률) |
| Acceptability | Select | 허용 가능성 (Acceptable, ALARP, Unacceptable) |
| Control Measures | Rich Text | 통제 수단 |
| Residual Risk | Number | 잔여 위험 수준 |
| Verification | Relation | 검증 근거 |

#### DB 5: Submission Tracker (제출 추적)

| 필드명 | 타입 | 설명 |
|--------|------|------|
| Submission ID | Title | 제출 ID |
| Type | Select | 유형 (510(k), PMA, De Novo, CE) |
| Device Name | Text | 기기명 |
| Product Code | Text | 제품 코드 |
| Predicate | Text | Predicate Device |
| Status | Select | 상태 (Preparation, Submitted, Review, Cleared) |
| Target Date | Date | 목표 제출일 |
| FDA Number | Text | FDA 접수번호 |
| Documents | Relation | 제출 문서 목록 |
| Notes | Rich Text | 비고 |

#### DB 6: Knowledge Base (지식 베이스)

| 필드명 | 타입 | 설명 |
|--------|------|------|
| ID | Title | 지식 항목 ID |
| Topic | Text | 주제 |
| Category | Multi-Select | 분류 (Regulation, Standard, Guidance, Precedent) |
| Content | Rich Text | 내용 |
| Source | URL | 출처 |
| Applicable To | Multi-Select | 적용 대상 |
| Last Updated | Date | 최종 갱신일 |
| Confidence | Select | 신뢰도 (High, Medium, Low) |
| Tags | Multi-Select | 태그 |

#### DB 7: Audit Log (감사 로그)

| 필드명 | 타입 | 설명 |
|--------|------|------|
| Log ID | Title | 로그 ID |
| Timestamp | Date | 타임스탬프 |
| Agent | Select | 에이전트 |
| Action | Text | 작업 |
| Entity | Text | 대상 |
| Decision | Text | 결정 |
| Rationale | Rich Text | 근거 |
| Outcome | Select | 결과 (Success, Failure, Pending) |

### 4.3 Google Workspace 통합

| 서비스 | 사용 목적 | 통합 방식 |
|--------|----------|-----------|
| Gmail | FDA/NB 서신 추적, 규제 관련 이메일 관리 | MCP 읽기 + 검색 |
| Google Docs | 협업 문서 편집, 검토 의견 교환 | MCP 읽기/쓰기 |
| Google Sheets | 데이터 분석, 위험 매트릭스, 준수 체크리스트 | MCP 읽기/쓰기 |
| Google Calendar | 규제 데드라인, 감사 일정, 리뷰 회의 | MCP 읽기/쓰기 |
| Google Drive | 대용량 파일 저장, 제출 패키지 관리 | MCP 파일 접근 |

### 4.4 Context7 MCP - 규제/표준 문서 검색

Context7를 활용하여 최신 규제 문서 및 표준 정보를 실시간으로 참조한다.

**주요 활용 시나리오:**
- 특정 표준 조항의 최신 해석 확인
- FDA 가이던스 문서 검색
- IEC/ISO 표준 요구사항 조회
- 라이브러리/도구 문서 참조

### 4.5 Sequential Thinking MCP - 복합 규제 분석

복잡한 규제 판단이 필요한 경우 Sequential Thinking MCP를 활성화한다.

**활성화 시나리오:**
- 규제 경로(Pathway) 결정: 510(k) vs PMA vs De Novo
- Substantial Equivalence 논리 구성
- 복합적 위험-편익 분석
- 멀티마켓 규제 전략 수립
- 표준 간 충돌/갭 분석

---

## 5. RA/QA 도메인 설계

### 5.1 규제 지식 베이스 구조

ARIA의 규제 지식은 3계층으로 구성된다:

```
Layer 1: Regulatory Framework (규제 체계)
├── FDA (미국)
│   ├── 21 CFR Part 820 (QSR / CGMP)
│   ├── 21 CFR Part 807 (Registration & Listing)
│   ├── 21 CFR Part 801 (Labeling)
│   ├── 510(k) Guidance Documents
│   ├── PMA Guidance Documents
│   └── De Novo Guidance Documents
├── EU (유럽)
│   ├── MDR 2017/745
│   ├── IVDR 2017/746
│   ├── Harmonized Standards
│   └── MDCG Guidance Documents
├── Korea (한국)
│   ├── 의료기기법
│   ├── 의료기기 허가/인증/신고 기준
│   └── MFDS 가이드라인
└── Others
    ├── PMDA (일본)
    ├── TGA (호주)
    └── Health Canada

Layer 2: Standards & Best Practices (표준 및 모범사례)
├── Quality Management
│   ├── ISO 13485:2016
│   └── ISO 9001:2015 (참조)
├── Risk Management
│   └── ISO 14971:2019
├── Software
│   ├── IEC 62304:2006+A1:2015
│   └── IEC 82304-1:2016
├── Electrical Safety
│   ├── IEC 60601-1:2005+A1+A2
│   └── IEC 60601-1-2 (EMC)
├── Usability
│   └── IEC 62366-1:2015
├── Biocompatibility
│   └── ISO 10993 Series
├── Sterilization
│   └── ISO 11607 Series
└── Clinical
    ├── ISO 14155:2020
    └── MEDDEV 2.7/1 Rev 4

Layer 3: Company-Specific Knowledge (회사 고유 지식)
├── SOPs (Standard Operating Procedures)
├── Work Instructions
├── Templates & Forms
├── Previous Submissions
├── Audit History
├── CAPA History
└── Design History Files
```

### 5.2 문서 템플릿 시스템

ARIA는 주요 규제 문서에 대한 사전 구성된 템플릿을 제공한다.

#### 템플릿 디렉토리 구조

```
templates/
├── 510k/
│   ├── cover-letter.md
│   ├── indications-for-use.md
│   ├── device-description.md
│   ├── substantial-equivalence.md
│   ├── performance-data.md
│   ├── biocompatibility.md
│   ├── software-documentation.md
│   ├── labeling.md
│   ├── sterilization.md
│   └── checklist.md
├── design-control/
│   ├── design-input.md
│   ├── design-output.md
│   ├── design-review.md
│   ├── design-verification.md
│   ├── design-validation.md
│   ├── design-transfer.md
│   └── traceability-matrix.md
├── risk-management/
│   ├── risk-management-plan.md
│   ├── hazard-analysis.md
│   ├── fmea.md
│   ├── fault-tree-analysis.md
│   ├── risk-benefit-analysis.md
│   └── risk-management-report.md
├── capa/
│   ├── capa-form.md
│   ├── root-cause-analysis.md
│   ├── action-plan.md
│   └── effectiveness-verification.md
├── clinical/
│   ├── clinical-evaluation-plan.md
│   ├── clinical-evaluation-report.md
│   ├── literature-review.md
│   ├── pmcf-plan.md
│   ├── pmcf-report.md
│   └── psur.md
├── qms/
│   ├── quality-manual.md
│   ├── sop-template.md
│   ├── work-instruction-template.md
│   └── form-template.md
├── audit/
│   ├── audit-plan.md
│   ├── audit-checklist-iso13485.md
│   ├── audit-checklist-21cfr820.md
│   ├── audit-report.md
│   └── finding-response.md
└── eu-mdr/
    ├── technical-documentation.md
    ├── declaration-of-conformity.md
    ├── udi-assignment.md
    └── post-market-surveillance-plan.md
```

#### 템플릿 형식 표준

각 템플릿은 다음 구조를 따른다:

```markdown
---
template_id: TPL-510K-001
name: "510(k) Cover Letter"
version: "1.0"
applicable_standard: "21 CFR 807.87"
document_type: "submission"
required_fields:
  - device_name
  - product_code
  - applicant_name
  - predicate_device
optional_fields:
  - additional_info
last_updated: "2026-02-09"
---

# 510(k) Premarket Notification - Cover Letter

## [회사명]
## [주소]
## [날짜]

Food and Drug Administration
Center for Devices and Radiological Health
Document Mail Center - WO66-G609
10903 New Hampshire Avenue
Silver Spring, MD 20993-0002

Re: 510(k) Premarket Notification for [제품명]

Dear Sir or Madam:

[회사명] hereby submits this 510(k) premarket notification
for the [제품명], classified under product code [제품코드],
regulation number [규정번호].

...
```

### 5.3 규정 준수 검사 워크플로우

ARIA의 규정 준수 검사는 자동화된 체크리스트 기반으로 수행된다.

**검사 수준:**

| 수준 | 검사 내용 | 자동화 | 에이전트 |
|------|----------|--------|----------|
| L1 - 형식 검사 | 템플릿 구조, 필수 필드, 형식 | 완전 자동 | manager-quality |
| L2 - 참조 검사 | 규정 인용 정확성, 표준 버전 | 반자동 | expert-reviewer |
| L3 - 내용 검사 | 기술적 정확성, 논리 일관성 | 반자동 | expert-standards |
| L4 - 전략 검사 | 규제 전략 적합성, 리스크 | 수동+AI | expert-regulatory |

**자동 검사 항목 예시:**

```
[L1] 형식 검사
  [자동] 필수 섹션 존재 여부
  [자동] 문서 ID 형식 (DOC-XXX-NNN)
  [자동] 버전 번호 형식
  [자동] 날짜 형식 (ISO 8601)
  [자동] 서명란 존재 여부

[L2] 참조 검사
  [반자동] ISO 13485 조항 번호 유효성
  [반자동] 21 CFR 파트/섹션 존재 확인
  [반자동] 참조 문서 최신 버전 확인
  [반자동] 교차 참조(cross-reference) 정합성

[L3] 내용 검사
  [반자동] Intended Use 일관성 (모든 문서 동일)
  [반자동] 위험 수준과 분류 등급 일치
  [반자동] 테스트 결과와 사양(specification) 비교
  [사용자 확인 필요] 기술적 주장의 타당성
```

### 5.4 추적성 매트릭스 지원

Traceability Matrix는 의료기기 개발에서 핵심적인 품질 도구이다. ARIA는 이를 자동으로 생성하고 유지한다.

**추적성 구조:**

```
사용자 요구사항 (User Needs)
    ↓ (traces to)
설계 입력 (Design Input)
    ↓ (satisfied by)
설계 출력 (Design Output)
    ↓ (verified by)
검증 활동 (Verification)
    ↓ (validated by)
확인 활동 (Validation)
    ↓ (controlled by)
위험 통제 (Risk Control)
```

**Traceability Matrix 형식:**

| User Need | Design Input | Design Output | Verification | Validation | Risk ID |
|-----------|-------------|---------------|-------------|------------|---------|
| UN-001 | DI-001 | DO-001 | VER-001 | VAL-001 | RISK-001 |
| UN-001 | DI-002 | DO-002 | VER-002 | - | RISK-003 |
| UN-002 | DI-003 | DO-003 | VER-003 | VAL-002 | - |

ARIA는 Notion DB의 Relation 필드를 활용하여 이 매트릭스를 자동으로 구성하고, 누락된 연결을 식별하여 사용자에게 알린다.

### 5.5 핵심 RA/QA 워크플로우

#### 워크플로우 1: 510(k) 제출 준비

```
단계 1: 기기 분류 및 규제 경로 확인
  [expert-regulatory] 제품 코드/분류 확인
  [expert-researcher] Predicate device 검색 (FDA 510(k) DB)
  [승인 체크포인트] 규제 경로 및 Predicate 승인

단계 2: Substantial Equivalence 분석
  [expert-regulatory] SE 논리 구성
  [expert-analyst] 기술 특성 비교 분석
  [expert-risk] 신규/변경 위험 식별
  [승인 체크포인트] SE 분석 결과 승인

단계 3: 성능 데이터 정리
  [expert-analyst] 테스트 데이터 분석/정리
  [expert-writer] Performance Data Summary 작성
  [expert-reviewer] 데이터 적합성 검토

단계 4: 제출 문서 작성
  [expert-submission] 패키지 구성 (eSTAR 기반)
  [expert-writer] 각 섹션 문서 작성
    - Cover Letter
    - Indications for Use
    - Device Description
    - SE Comparison
    - Performance Data
    - Software Documentation (해당 시)
    - Biocompatibility
    - Labeling
  [승인 체크포인트] 각 섹션 내용 승인

단계 5: 최종 검토 및 제출
  [expert-reviewer] 전체 패키지 검토
  [manager-quality] VALID 게이트 실행
  [승인 체크포인트] 최종 제출 승인
  [expert-submission] eCopy 준비 / FDA 제출
```

#### 워크플로우 2: CAPA 관리

```
단계 1: CAPA 개시
  [expert-capa] CAPA 양식 생성
  [expert-analyst] 문제/부적합 분석
  [승인 체크포인트] CAPA 개시 승인

단계 2: 근본원인 분석
  [expert-capa] RCA 수행 (5 Whys, Fishbone)
  [expert-analyst] 관련 데이터 동향 분석
  [expert-risk] 위험 영향도 평가
  [승인 체크포인트] 근본원인 승인

단계 3: 조치 계획 수립
  [expert-capa] 시정/예방 조치 계획 작성
  [manager-project] 일정 및 담당자 할당
  [승인 체크포인트] 조치 계획 승인

단계 4: 실행 및 모니터링
  [manager-project] 진행 상태 추적
  [expert-capa] 실행 기록 문서화

단계 5: 효과성 검증
  [expert-capa] 효과성 검증 계획 실행
  [expert-analyst] 검증 데이터 분석
  [승인 체크포인트] 효과성 승인 및 CAPA 종료
```

#### 워크플로우 3: 설계 검토 (Design Review)

```
단계 1: 검토 준비
  [expert-design-control] 검토 대상 문서 수집
  [expert-design-control] 설계 입력/출력 매핑 확인
  [expert-risk] 해당 단계 위험분석 현황 확인

단계 2: 검토 체크리스트 생성
  [expert-design-control] 단계별 체크리스트 자동 생성
    - 설계 입력 완전성
    - 설계 출력 적합성
    - 추적성 매트릭스 정합성
    - 위험관리 현황
    - 규제 요구사항 충족

단계 3: 검토 실행 지원
  [expert-reviewer] AI 사전 검토 수행
  [expert-design-control] 지적사항(Action Item) 문서화
  [승인 체크포인트] 검토 결과 승인

단계 4: 후속 조치
  [expert-design-control] Action Item 추적
  [manager-project] 일정 관리
```

#### 워크플로우 4: 내부감사

```
단계 1: 감사 계획
  [expert-audit] 연간 감사 프로그램 검토
  [expert-audit] 감사 범위 및 기준 설정
  [expert-audit] 감사 체크리스트 생성

단계 2: 감사 준비
  [expert-researcher] 관련 문서/기록 수집
  [expert-audit] 이전 감사 Finding 현황 확인
  [expert-audit] 감사 일정 및 인터뷰 계획

단계 3: 감사 지원
  [expert-audit] 실시간 Finding 문서화
  [expert-standards] 표준 요구사항 해석 지원
  [expert-audit] Finding 분류 (Major/Minor/OFI)

단계 4: 감사 보고 및 후속조치
  [expert-audit] 감사 보고서 작성
  [expert-capa] Finding 기반 CAPA 연계
  [승인 체크포인트] 감사 보고서 승인
```

#### 워크플로우 5: 임상평가 보고서 (CER) 작성

```
단계 1: 임상평가 계획
  [expert-clinical] Clinical Evaluation Plan 작성
  [expert-regulatory] 해당 규제 요구사항 확인 (EU MDR)
  [승인 체크포인트] CEP 승인

단계 2: 문헌 검색 및 검토
  [expert-researcher] 체계적 문헌 검색 수행
  [expert-clinical] 문헌 평가 (적합성, 품질)
  [expert-analyst] 데이터 추출 및 분석

단계 3: CER 작성
  [expert-clinical] CER 본문 작성
    - 기기 설명 및 분류
    - 임상 배경 및 현재 치료법
    - 임상 데이터 분석
    - 성능 및 안전성 평가
    - 위험-편익 분석
    - 결론 및 시판후 감시 계획
  [expert-risk] 위험-편익 분석 기여
  [expert-standards] MEDDEV 2.7/1 Rev 4 준수 확인

단계 4: 검토 및 완성
  [expert-reviewer] CER 전체 검토
  [manager-quality] VALID 게이트 실행
  [승인 체크포인트] CER 최종 승인
```

---

## 6. 플러그인 생태계

### 6.1 플러그인 아키텍처

ARIA는 Claude Code 플러그인 표준을 따르며, 도메인별 확장을 지원한다.

```
Base Plugin (aria-core)
├── 핵심 오케스트레이터
├── 공통 비즈니스 에이전트
├── VALID 품질 프레임워크
├── Brief-Execute-Deliver 워크플로우
└── 기본 MCP 통합

Domain Plugins (독립 설치)
├── aria-domain-raqa         -- 의료기기 RA/QA
├── aria-domain-finance      -- 재무/회계 (향후)
├── aria-domain-legal        -- 법무 (향후)
├── aria-domain-marketing    -- 마케팅 (향후)
└── aria-domain-hr           -- 인사 (향후)
```

### 6.2 도메인 플러그인 구조

각 도메인 플러그인은 다음 구조를 따른다:

```
aria-domain-raqa/
├── .claude-plugin/
│   └── plugin.json
├── .claude/
│   ├── agents/
│   │   ├── expert-regulatory.md
│   │   ├── expert-standards.md
│   │   ├── expert-risk.md
│   │   ├── expert-design-control.md
│   │   ├── expert-capa.md
│   │   ├── expert-clinical.md
│   │   ├── expert-submission.md
│   │   └── expert-audit.md
│   ├── skills/
│   │   ├── aria-domain-raqa/
│   │   │   ├── SKILL.md
│   │   │   └── modules/
│   │   │       ├── fda-regulations.md
│   │   │       ├── eu-mdr.md
│   │   │       ├── iso-standards.md
│   │   │       └── submission-workflows.md
│   │   ├── aria-knowledge-fda/
│   │   │   ├── SKILL.md
│   │   │   └── modules/
│   │   ├── aria-knowledge-eumdr/
│   │   │   ├── SKILL.md
│   │   │   └── modules/
│   │   ├── aria-knowledge-standards/
│   │   │   ├── SKILL.md
│   │   │   └── modules/
│   │   ├── aria-risk-management/
│   │   │   └── SKILL.md
│   │   ├── aria-design-control/
│   │   │   └── SKILL.md
│   │   ├── aria-capa-process/
│   │   │   └── SKILL.md
│   │   ├── aria-clinical-evaluation/
│   │   │   └── SKILL.md
│   │   ├── aria-submission-templates/
│   │   │   └── SKILL.md
│   │   └── aria-audit-management/
│   │       └── SKILL.md
│   └── commands/
│       ├── regulatory-strategy.md
│       ├── risk-analysis.md
│       └── submission-prep.md
├── templates/
│   ├── 510k/
│   ├── design-control/
│   ├── risk-management/
│   ├── capa/
│   ├── clinical/
│   ├── qms/
│   ├── audit/
│   └── eu-mdr/
└── hooks/
    └── hooks.json
```

### 6.3 플러그인 매니페스트 (plugin.json)

**Base Plugin (aria-core):**

```json
{
  "name": "aria-core",
  "description": "ARIA - AI Regulatory Intelligence Assistant. Core orchestration framework for business workflow automation with Claude Code.",
  "version": "1.0.0",
  "author": {
    "name": "ARIA Team"
  },
  "keywords": [
    "business-automation",
    "workflow",
    "orchestration",
    "document-management",
    "quality-framework"
  ],
  "commands": ".claude/commands/",
  "agents": ".claude/agents/",
  "skills": ".claude/skills/",
  "hooks": ".claude/hooks/hooks.json"
}
```

**Domain Plugin (aria-domain-raqa):**

```json
{
  "name": "aria-domain-raqa",
  "description": "Medical Device RA/QA domain specialization for ARIA. FDA 510(k), EU MDR, ISO 13485, risk management, CAPA, design controls, and regulatory submissions.",
  "version": "1.0.0",
  "author": {
    "name": "ARIA Team"
  },
  "keywords": [
    "medical-device",
    "regulatory-affairs",
    "quality-assurance",
    "fda",
    "iso-13485",
    "510k",
    "eu-mdr",
    "risk-management",
    "capa",
    "design-controls"
  ],
  "commands": ".claude/commands/",
  "agents": ".claude/agents/",
  "skills": ".claude/skills/",
  "hooks": ".claude/hooks/hooks.json"
}
```

### 6.4 플러그인 발견 및 역량 선언

각 도메인 플러그인은 자신의 역량을 선언하여 orchestrator가 자동으로 인식하고 라우팅할 수 있도록 한다.

**역량 선언 (Capability Declaration):**

도메인 플러그인의 SKILL.md에 다음 메타데이터를 포함한다:

```yaml
---
name: aria-domain-raqa
description: >
  Medical Device RA/QA domain expertise.
  Provides specialized agents and workflows for FDA,
  EU MDR, ISO 13485, risk management, CAPA,
  design controls, and regulatory submissions.
metadata:
  version: "1.0.0"
  category: "domain"
  status: "active"
  domain: "medical-device-raqa"
  capabilities: "regulatory-strategy, risk-management, design-control, capa, clinical-evaluation, submission, audit, standards-interpretation"
  trigger-keywords: "510k, PMA, FDA, EU MDR, ISO 13485, IEC 62304, risk, CAPA, DHF, design control, clinical evaluation, audit, submission, regulatory"
  supported-markets: "FDA, EU, MFDS, PMDA, TGA"
triggers:
  keywords:
    - "510k"
    - "pma"
    - "fda"
    - "eu mdr"
    - "iso 13485"
    - "iec 62304"
    - "risk management"
    - "capa"
    - "design control"
    - "clinical evaluation"
    - "regulatory"
    - "submission"
    - "audit"
    - "medical device"
---
```

### 6.5 확장성 모델

새로운 도메인을 추가하려면:

1. **플러그인 생성**: `aria-domain-{name}/` 디렉토리 구조 생성
2. **에이전트 정의**: 도메인 전문 에이전트를 `.md` 파일로 작성
3. **스킬 정의**: 도메인 지식을 스킬로 구조화 (Progressive Disclosure)
4. **템플릿 추가**: 도메인별 문서 템플릿 작성
5. **워크플로우 정의**: Brief-Execute-Deliver에 맞는 도메인 워크플로우
6. **역량 선언**: SKILL.md에 trigger keywords와 capabilities 선언
7. **플러그인 설치**: `/plugin install {repo}` 또는 수동 복사

---

## 7. 프로젝트 구조

### 7.1 디렉토리 레이아웃

```
Agent-RA/                              # 프로젝트 루트
├── .claude-plugin/
│   └── plugin.json                    # 플러그인 매니페스트
│
├── .claude/
│   ├── settings.json                  # Claude Code 설정
│   ├── settings.local.json            # 로컬 설정 (gitignore)
│   ├── agents/                        # 에이전트 정의
│   │   ├── core/                      # Core Layer
│   │   │   ├── orchestrator.md
│   │   │   ├── manager-docs.md
│   │   │   ├── manager-quality.md
│   │   │   └── manager-project.md
│   │   ├── business/                  # Business Layer
│   │   │   ├── expert-writer.md
│   │   │   ├── expert-analyst.md
│   │   │   ├── expert-reviewer.md
│   │   │   └── expert-researcher.md
│   │   └── raqa/                      # Domain Layer (RA/QA)
│   │       ├── expert-regulatory.md
│   │       ├── expert-standards.md
│   │       ├── expert-risk.md
│   │       ├── expert-design-control.md
│   │       ├── expert-capa.md
│   │       ├── expert-clinical.md
│   │       ├── expert-submission.md
│   │       └── expert-audit.md
│   ├── skills/                        # 스킬 정의
│   │   ├── aria/                      # 메인 오케스트레이터 스킬
│   │   │   ├── SKILL.md
│   │   │   └── workflows/
│   │   │       ├── brief.md
│   │   │       ├── execute.md
│   │   │       ├── deliver.md
│   │   │       └── search.md
│   │   ├── aria-core/                 # 핵심 기능 스킬
│   │   │   ├── SKILL.md
│   │   │   └── modules/
│   │   │       ├── valid-framework.md
│   │   │       ├── user-interaction.md
│   │   │       └── error-handling.md
│   │   ├── aria-templates/            # 템플릿 관리 스킬
│   │   │   └── SKILL.md
│   │   ├── aria-domain-raqa/          # RA/QA 도메인 스킬
│   │   │   ├── SKILL.md
│   │   │   └── modules/
│   │   │       ├── fda-regulations.md
│   │   │       ├── eu-mdr.md
│   │   │       ├── iso-standards.md
│   │   │       └── submission-workflows.md
│   │   ├── aria-knowledge-fda/        # FDA 지식 베이스
│   │   │   ├── SKILL.md
│   │   │   └── modules/
│   │   │       ├── classification.md
│   │   │       ├── 510k-process.md
│   │   │       ├── pma-process.md
│   │   │       └── guidance-documents.md
│   │   ├── aria-knowledge-eumdr/      # EU MDR 지식 베이스
│   │   │   └── SKILL.md
│   │   ├── aria-knowledge-standards/  # 표준 지식 베이스
│   │   │   ├── SKILL.md
│   │   │   └── modules/
│   │   │       ├── iso-13485.md
│   │   │       ├── iec-62304.md
│   │   │       ├── iec-60601.md
│   │   │       ├── iso-14971.md
│   │   │       └── iec-62366.md
│   │   ├── aria-risk-management/      # 위험관리 스킬
│   │   │   └── SKILL.md
│   │   ├── aria-design-control/       # 설계관리 스킬
│   │   │   └── SKILL.md
│   │   ├── aria-capa-process/         # CAPA 프로세스 스킬
│   │   │   └── SKILL.md
│   │   ├── aria-clinical-evaluation/  # 임상평가 스킬
│   │   │   └── SKILL.md
│   │   ├── aria-submission-templates/ # 제출 템플릿 스킬
│   │   │   └── SKILL.md
│   │   ├── aria-audit-management/     # 감사관리 스킬
│   │   │   └── SKILL.md
│   │   ├── aria-quality-valid/        # VALID 품질 프레임워크
│   │   │   └── SKILL.md
│   │   ├── aria-writing-style/        # 기술 문서 작성 스타일
│   │   │   └── SKILL.md
│   │   ├── aria-research/             # 리서치 방법론
│   │   │   └── SKILL.md
│   │   └── aria-analysis/             # 데이터 분석 스킬
│   │       └── SKILL.md
│   └── commands/                      # 슬래시 커맨드
│       ├── aria.md                    # /aria 메인 커맨드
│       ├── brief.md                   # /aria brief
│       ├── execute.md                 # /aria execute
│       ├── deliver.md                 # /aria deliver
│       ├── search.md                  # /aria search
│       ├── template.md                # /aria template
│       ├── status.md                  # /aria status
│       └── knowledge.md               # /aria knowledge
│
├── .mcp.json                          # MCP 서버 구성
│
├── hooks/                             # 훅 스크립트
│   ├── hooks.json                     # 훅 정의
│   └── scripts/
│       ├── quality-check.sh           # VALID 게이트 훅
│       ├── audit-trail.sh             # 감사 추적 훅
│       └── template-validate.sh       # 템플릿 검증 훅
│
├── templates/                         # 문서 템플릿
│   ├── 510k/
│   ├── design-control/
│   ├── risk-management/
│   ├── capa/
│   ├── clinical/
│   ├── qms/
│   ├── audit/
│   └── eu-mdr/
│
├── config/                            # ARIA 설정
│   ├── aria.yaml                      # 메인 설정
│   ├── notion-schema.yaml             # Notion DB 스키마 정의
│   ├── quality.yaml                   # VALID 프레임워크 설정
│   └── templates.yaml                 # 템플릿 설정
│
├── CLAUDE.md                          # Claude Code 지시 파일
├── .gitignore
└── README.md
```

### 7.2 파일 명명 규칙

| 항목 | 규칙 | 예시 |
|------|------|------|
| 에이전트 파일 | `{역할}-{전문분야}.md` | `expert-regulatory.md` |
| 스킬 디렉토리 | `aria-{카테고리}-{이름}/` | `aria-domain-raqa/` |
| 스킬 파일 | `SKILL.md` (항상 대문자) | `SKILL.md` |
| 모듈 파일 | `{주제}.md` (소문자-하이픈) | `fda-regulations.md` |
| 커맨드 파일 | `{커맨드명}.md` | `brief.md` |
| 템플릿 파일 | `{문서유형}.md` | `cover-letter.md` |
| 설정 파일 | `{설정명}.yaml` | `aria.yaml` |
| 훅 스크립트 | `{기능}.sh` | `quality-check.sh` |

### 7.3 설정 시스템

#### aria.yaml - 메인 설정

```yaml
# ARIA Configuration
aria:
  version: "1.0.0"
  name: "ARIA"
  description: "AI Regulatory Intelligence Assistant"

# User Profile
user:
  name: ""
  role: ""  # RA Manager, QA Engineer, etc.
  organization: ""

# Language
language:
  conversation: "ko"
  documents: "en"  # 규제 문서는 보통 영어
  templates: "en"

# Active Domain Plugins
domains:
  - raqa  # Medical Device RA/QA

# Workflow Settings
workflow:
  # Brief phase token budget
  brief_tokens: 30000
  # Execute phase token budget
  execute_tokens: 180000
  # Deliver phase token budget
  deliver_tokens: 40000
  # Auto-clear between phases
  auto_clear: true
  # Require user approval at checkpoints
  approval_required: true

# Quality Framework
quality:
  framework: "valid"  # VALID framework
  auto_check: true
  levels:
    - L1  # 형식 검사 (자동)
    - L2  # 참조 검사 (반자동)
    - L3  # 내용 검사 (반자동)
    # L4 (전략 검사)는 명시적 요청 시에만

# Integration
integration:
  notion:
    enabled: true
    workspace: ""
    databases: {}  # 자동 생성 또는 기존 연결
  google:
    enabled: false  # 초기에는 비활성
    services: []
  context7:
    enabled: true
  sequential_thinking:
    enabled: true

# Audit Trail
audit_trail:
  enabled: true
  storage: "notion"  # notion, local, both
  retention_days: null  # 영구 보관

# Knowledge Base
knowledge:
  auto_update: true
  confidence_threshold: "medium"
```

#### notion-schema.yaml - Notion DB 스키마

```yaml
# Notion Database Schema for ARIA
databases:
  regulatory_requirements:
    name: "Regulatory Requirements"
    icon: "clipboard"
    properties:
      - { name: "ID", type: "title" }
      - { name: "Standard", type: "select", options: ["ISO 13485", "21 CFR 820", "EU MDR", "IEC 62304", "ISO 14971"] }
      - { name: "Section", type: "rich_text" }
      - { name: "Requirement", type: "rich_text" }
      - { name: "Category", type: "multi_select" }
      - { name: "Status", type: "select", options: ["Compliant", "Gap", "N/A", "In Progress"] }

  document_registry:
    name: "Document Registry"
    icon: "page_with_curl"
    properties:
      - { name: "Doc ID", type: "title" }
      - { name: "Title", type: "rich_text" }
      - { name: "Type", type: "select" }
      - { name: "Version", type: "rich_text" }
      - { name: "Status", type: "select", options: ["Draft", "Review", "Approved", "Obsolete"] }
      - { name: "Owner", type: "people" }
      - { name: "Review Date", type: "date" }

  capa_tracker:
    name: "CAPA Tracker"
    icon: "warning"
    properties:
      - { name: "CAPA ID", type: "title" }
      - { name: "Type", type: "select", options: ["Corrective", "Preventive", "Both"] }
      - { name: "Source", type: "select" }
      - { name: "Status", type: "select", options: ["Open", "In Progress", "Verification", "Closed"] }
      - { name: "Due Date", type: "date" }
      - { name: "Assignee", type: "people" }

  risk_register:
    name: "Risk Register"
    icon: "shield"
    properties:
      - { name: "Risk ID", type: "title" }
      - { name: "Hazard", type: "rich_text" }
      - { name: "Severity", type: "select", options: ["1", "2", "3", "4", "5"] }
      - { name: "Probability", type: "select", options: ["1", "2", "3", "4", "5"] }
      - { name: "Acceptability", type: "select", options: ["Acceptable", "ALARP", "Unacceptable"] }

  submission_tracker:
    name: "Submission Tracker"
    icon: "rocket"
    properties:
      - { name: "Submission ID", type: "title" }
      - { name: "Type", type: "select", options: ["510(k)", "PMA", "De Novo", "CE", "MFDS"] }
      - { name: "Device Name", type: "rich_text" }
      - { name: "Status", type: "select" }
      - { name: "Target Date", type: "date" }

  knowledge_base:
    name: "Knowledge Base"
    icon: "books"
    properties:
      - { name: "ID", type: "title" }
      - { name: "Topic", type: "rich_text" }
      - { name: "Category", type: "multi_select" }
      - { name: "Content", type: "rich_text" }
      - { name: "Confidence", type: "select", options: ["High", "Medium", "Low"] }
      - { name: "Last Updated", type: "date" }
```

---

## 8. 구현 로드맵

### Phase 1: 핵심 프레임워크 (Core Framework)

**목표**: ARIA 플러그인 기본 골격 구축

**범위:**
- [ ] 플러그인 디렉토리 구조 생성
- [ ] `plugin.json` 매니페스트 작성
- [ ] `CLAUDE.md` ARIA 전용 지시 파일 작성
- [ ] orchestrator 에이전트 정의
- [ ] `/aria` 메인 슬래시 커맨드 구현
- [ ] `aria.yaml` 설정 파일 구조
- [ ] Brief-Execute-Deliver 워크플로우 기본 스켈레톤
- [ ] 기본 에러 핸들링 (평이한 언어)
- [ ] AskUserQuestion 기반 사용자 상호작용 패턴
- [ ] `.mcp.json` Sequential Thinking + Context7 설정

**산출물:**
- 동작하는 플러그인 구조
- orchestrator 에이전트가 자연어 입력을 받아 의도를 분류하는 기본 라우팅
- `/aria` 커맨드로 기본 상호작용 가능

**의존성:** 없음 (시작점)

### Phase 2: 범용 비즈니스 에이전트 (Generic Business Agents)

**목표**: 도메인 독립적 비즈니스 에이전트 구현

**범위:**
- [ ] expert-writer 에이전트 (문서 작성)
- [ ] expert-analyst 에이전트 (데이터 분석)
- [ ] expert-reviewer 에이전트 (문서 검토)
- [ ] expert-researcher 에이전트 (정보 검색)
- [ ] manager-docs 에이전트 (문서 관리)
- [ ] manager-quality 에이전트 (VALID 프레임워크 기본)
- [ ] manager-project 에이전트 (프로젝트 관리)
- [ ] aria-core 스킬 (핵심 기능)
- [ ] aria-quality-valid 스킬 (VALID 프레임워크)
- [ ] aria-writing-style 스킬 (작성 스타일)
- [ ] aria-templates 스킬 (템플릿 관리)

**산출물:**
- 범용 문서 작성/검토/분석 기능
- VALID 품질 프레임워크 기본 동작
- Brief-Execute-Deliver 워크플로우 완성

**의존성:** Phase 1

### Phase 3: RA/QA 전문화 (RA/QA Specialization)

**목표**: 의료기기 RA/QA 도메인 에이전트 및 지식 구현

**범위:**
- [ ] expert-regulatory 에이전트 (규제 전략)
- [ ] expert-standards 에이전트 (표준 해석)
- [ ] expert-risk 에이전트 (위험관리)
- [ ] expert-design-control 에이전트 (설계관리)
- [ ] expert-capa 에이전트 (CAPA)
- [ ] expert-clinical 에이전트 (임상평가)
- [ ] expert-submission 에이전트 (인허가 제출)
- [ ] expert-audit 에이전트 (감사관리)
- [ ] aria-domain-raqa 스킬 (RA/QA 도메인 종합)
- [ ] aria-knowledge-fda 스킬 (FDA 지식)
- [ ] aria-knowledge-eumdr 스킬 (EU MDR 지식)
- [ ] aria-knowledge-standards 스킬 (표준 지식)
- [ ] aria-risk-management 스킬
- [ ] aria-design-control 스킬
- [ ] aria-capa-process 스킬
- [ ] aria-clinical-evaluation 스킬
- [ ] aria-submission-templates 스킬
- [ ] aria-audit-management 스킬
- [ ] 510(k) 제출 워크플로우 구현
- [ ] CAPA 관리 워크플로우 구현
- [ ] 설계검토 워크플로우 구현
- [ ] 문서 템플릿 (510k, design-control, risk, capa)
- [ ] Traceability Matrix 자동 생성

**산출물:**
- 완전한 RA/QA 전문 에이전트 세트
- 주요 규제 워크플로우 동작
- 핵심 문서 템플릿
- 규제 지식 베이스 기본 구조

**의존성:** Phase 2

### Phase 4: MCP 통합 (MCP Integrations)

**목표**: Notion, Google Workspace 등 외부 서비스 통합

**범위:**
- [ ] Notion MCP 통합
  - [ ] Notion DB 스키마 자동 생성
  - [ ] 문서 저장/검색/업데이트
  - [ ] Traceability Matrix Notion 연동
  - [ ] CAPA Tracker Notion 연동
  - [ ] Risk Register Notion 연동
  - [ ] Submission Tracker Notion 연동
- [ ] Google Workspace MCP 통합
  - [ ] Gmail 규제 서신 검색
  - [ ] Google Docs 문서 편집
  - [ ] Google Sheets 데이터 분석
  - [ ] Google Calendar 데드라인 관리
- [ ] Context7 MCP 규제 문서 검색 최적화
- [ ] 감사 추적(Audit Trail) Notion 기반 구현
- [ ] `/aria search` 통합 검색 기능
- [ ] `/aria knowledge` 지식 베이스 조회 기능
- [ ] `/aria status` 프로젝트 상태 대시보드

**산출물:**
- Notion 기반 중앙 데이터 관리
- Google Workspace 협업 기능
- 통합 검색 및 지식 관리
- 감사 추적 시스템

**의존성:** Phase 3

### Phase 5: 고급 기능 (Advanced Features)

**목표**: 팀 모드, 메모리, 고급 분석 기능

**범위:**
- [ ] Agent Memory (프로젝트 스코프)
  - [ ] 이전 규제 결정/해석 기억
  - [ ] 회사별 선호도/관행 학습
  - [ ] 반복 업무 패턴 인식
- [ ] Agent Teams 모드 (실험적)
  - [ ] 510(k) 제출 병렬 준비 팀
  - [ ] 감사 대응 병렬 팀
- [ ] 고급 분석 기능
  - [ ] 불만 동향 자동 분석 및 경고
  - [ ] 규제 변경 영향 분석
  - [ ] Cross-submission 지식 활용
- [ ] 임상평가 워크플로우 완성
- [ ] 내부감사 워크플로우 완성
- [ ] 시판후조사 워크플로우
- [ ] 다국가 규제 전략 비교 기능
- [ ] 추가 템플릿 (clinical, qms, audit, eu-mdr)
- [ ] 훅 시스템 (품질 체크, 감사 추적, 템플릿 검증)
- [ ] Output Styles (보고서 형식 커스터마이징)

**산출물:**
- 지능형 지식 누적 시스템
- 병렬 작업 지원
- 고급 분석 및 인사이트
- 완전한 워크플로우 커버리지
- 완전한 템플릿 라이브러리

**의존성:** Phase 4

---

## 부록

### A. MoAI-ADK 대비 ARIA 매핑 테이블

| MoAI-ADK 개념 | ARIA 대응 | 비고 |
|---------------|-----------|------|
| MoAI Orchestrator | ARIA Orchestrator | 동일 패턴, 다른 도메인 |
| SPEC Document | Task Brief | EARS 형식 대신 자연어 기반 |
| Plan-Run-Sync | Brief-Execute-Deliver | 비즈니스 맥락 적응 |
| TRUST 5 | VALID | 규제 준수 중심 재설계 |
| DDD (ANALYZE-PRESERVE-IMPROVE) | Research-Draft-Review-Refine | 문서 작성 중심 |
| manager-ddd | manager-docs | 코드 → 문서 |
| expert-backend | expert-regulatory | 기술 → 규제 |
| expert-frontend | expert-writer | UI → 문서 작성 |
| expert-testing | expert-reviewer | 테스트 → 검토 |
| expert-security | expert-standards | 보안 → 표준 준수 |
| SPEC files (.moai/specs/) | Notion DB + Task Brief | 파일 → DB 기반 |
| Git version control | Notion version history | 코드 버전 → 문서 버전 |
| package.json / pyproject.toml | aria.yaml | 프로젝트 설정 |
| Progressive Disclosure | 동일 적용 | 토큰 최적화 |
| Agent Teams | 동일 적용 (향후) | 병렬 실행 |
| Agent Memory | 동일 적용 | 지식 누적 |
| MCP (Context7, Pencil) | MCP (Notion, Google, Context7) | 다른 MCP 세트 |

### B. 주요 규제 참조 목록

**FDA (미국)**
- 21 CFR Part 820 - Quality System Regulation
- 21 CFR Part 807 - Establishment Registration and Device Listing
- 21 CFR Part 801 - Labeling
- 21 CFR Part 812 - Investigational Device Exemptions
- 21 CFR Part 814 - Premarket Approval
- FDA Guidance: Content of Premarket Submissions for Device Software Functions
- FDA Guidance: Deciding When to Submit a 510(k) for a Software Change

**EU**
- Regulation (EU) 2017/745 - Medical Device Regulation (MDR)
- Regulation (EU) 2017/746 - In Vitro Diagnostic Regulation (IVDR)
- MDCG Guidance Documents (전체 시리즈)

**국제 표준**
- ISO 13485:2016 - Medical devices - Quality management systems
- ISO 14971:2019 - Application of risk management to medical devices
- IEC 62304:2006+A1:2015 - Medical device software - Software life cycle processes
- IEC 60601-1:2005+A1:2012+A2:2020 - Medical electrical equipment - General requirements
- IEC 62366-1:2015+A1:2020 - Usability engineering
- ISO 10993 Series - Biological evaluation of medical devices
- ISO 14155:2020 - Clinical investigation of medical devices
- ISO 11607 Series - Packaging for terminally sterilized medical devices

### C. 용어 정의

| 용어 | 정의 |
|------|------|
| 510(k) | FDA에 제출하는 시판전 신고. Predicate device와의 실질적 동등성 입증 |
| PMA | 시판전 승인 신청. Class III 기기에 필요한 가장 엄격한 인허가 경로 |
| De Novo | 새로운 기기 유형에 대한 분류 요청. Predicate 없는 Class I/II 기기 |
| DHF | Design History File. 설계 과정의 전체 기록 |
| DMR | Device Master Record. 완성된 기기의 제조 사양 |
| DHR | Device History Record. 개별 기기의 제조 기록 |
| CAPA | Corrective and Preventive Action. 시정 및 예방 조치 |
| CER | Clinical Evaluation Report. 임상평가 보고서 (EU MDR) |
| PMCF | Post-Market Clinical Follow-up. 시판후 임상 추적 |
| PSUR | Periodic Safety Update Report. 정기 안전성 업데이트 보고서 |
| STED | Summary Technical Documentation. 요약 기술 문서 |
| eSTAR | FDA의 전자 제출 템플릿 및 리소스 |
| MAUDE | FDA Manufacturer and User Facility Device Experience 데이터베이스 |
| NB | Notified Body. EU MDR 적합성 평가 기관 |
| QMS | Quality Management System. 품질경영시스템 |
| SOP | Standard Operating Procedure. 표준 운영 절차 |
| WI | Work Instruction. 작업 지시서 |
| FMEA | Failure Mode and Effects Analysis. 고장 모드 및 영향 분석 |
| FTA | Fault Tree Analysis. 결함 트리 분석 |
| ALARP | As Low As Reasonably Practicable. 합리적으로 실행 가능한 한 낮은 수준 |

---

## 문서 이력

| 버전 | 날짜 | 변경 내용 |
|------|------|----------|
| 1.0.0 | 2026-02-09 | 초기 아키텍처 설계 문서 작성 |

---

**작성**: ARIA Architecture Design
**검토 상태**: 사용자 승인 대기
**다음 단계**: 사용자 검토 및 승인 후 Phase 1 구현 착수
