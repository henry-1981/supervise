---
name: aria-template
description: >
  ARIA Template command skill for template library management, search,
  and preview functionality. Provides document templates for regulatory,
  quality, and clinical domains with customization support.
license: Apache-2.0
compatibility: Designed for Claude Code with ARIA orchestrator
user-invocable: false
metadata:
  version: "1.0.0"
  category: "workflow"
  status: "active"
  updated: "2026-02-09"
  modularized: "true"
  tags: "aria, templates, library, search, preview"
  author: "ARIA Phase 2 Implementation Team"

progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

triggers:
  keywords: ["template", "library", "search", "preview", "document"]
  agents: ["orchestrator", "manager-docs", "expert-writer"]
  phases: ["brief", "execute"]
---

# ARIA Template Command Skill

## 개요 (Overview)

Template 커맨드는 ARIA의 문서 템플릿 라이브러리를 관리하고 검색하는 기능을 제공합니다.

**주요 기능:**
- 템플릿 라이브러리 조회 (카테고리별)
- 키워드 기반 템플릿 검색
- 템플릿 미리보기
- 사용자 정의 템플릿 추가
- 템플릿 메타데이터 관리

## 템플릿 카탈로그 (Template Catalog)

### 1. 규제 문서 (Regulatory Documents)

```
┌─ FDA (US)
│  ├─ 510(k) Premarket Notification
│  │  ├─ Summary Template
│  │  ├─ Substantial Equivalence Template
│  │  └─ 510(k) Cover Letter
│  ├─ PMA (Premarket Approval)
│  ├─ De Novo Request
│  └─ IDE Application

├─ EU MDR
│  ├─ Technical File Structure
│  ├─ Clinical Evaluation Report (CER)
│  ├─ Quality Management Summary
│  ├─ Risk Management Report
│  └─ CE Declaration of Conformity

└─ MFDS (Korea)
   ├─ 의료기기 허가 신청서
   ├─ 임상 평가 보고서
   └─ 품질 관리 체계 문서
```

### 2. 품질 문서 (Quality Documents)

```
├─ CAPA (Corrective and Preventive Action)
│  ├─ CAPA Initiation Form
│  ├─ Root Cause Analysis Template
│  └─ Effectiveness Verification

├─ Risk Management
│  ├─ ISO 14971 Risk Analysis
│  ├─ FMEA Template
│  └─ Risk Control Measures

├─ Design Control
│  ├─ Design Input Document
│  ├─ Design Output Specification
│  ├─ Design Verification Protocol
│  └─ Design Validation Report

└─ Internal Audit
   ├─ Audit Checklist
   ├─ Audit Report
   └─ Audit Finding Log
```

### 3. 임상 문서 (Clinical Documents)

```
├─ Clinical Evaluation
│  ├─ Literature Review Structure
│  ├─ Clinical Evidence Summary
│  └─ CER (Clinical Evaluation Report)

├─ Post-Market Surveillance
│  ├─ PMCF Plan
│  ├─ Complaint Analysis Template
│  └─ Adverse Event Summary

└─ Clinical Investigation
   ├─ Protocol Template
   ├─ Informed Consent Form
   └─ Clinical Report
```

## 커맨드 사용법 (Command Usage)

### 1. 템플릿 목록 조회

```bash
/aria template list [category]
/aria template list regulatory      # FDA/EU/MFDS 템플릿
/aria template list quality         # 품질 관련 템플릿
/aria template list clinical        # 임상 관련 템플릿
```

**출력 예시:**
```
📋 Template Library - Regulatory Documents

🗂️ FDA (US)
  1. 510(k) Summary Template
  2. Substantial Equivalence Letter
  3. 510(k) Cover Letter
  4. PMA Application Template

🗂️ EU MDR
  5. Technical File Structure Guide
  6. Clinical Evaluation Report (CER)
  7. Quality Management Summary

🗂️ MFDS (Korea)
  8. 의료기기 허가 신청 양식
  9. 임상 평가 보고서 (한국어)
```

### 2. 템플릿 검색

```bash
/aria template search "keyword"
/aria template search "510(k)"
/aria template search "risk analysis"
/aria template search "capa"
```

**검색 필터:**
- 도메인: FDA, EU MDR, MFDS
- 문서 유형: Regulatory, Quality, Clinical
- 언어: 영어, 한국어
- 복잡도: 기본, 중간, 고급

### 3. 템플릿 미리보기

```bash
/aria template preview 1
/aria template preview "510(k) Summary"
```

**미리보기 내용:**
- 템플릿 구조 (섹션, 항목)
- 샘플 텍스트
- 작성 지침
- 예상 작성 시간
- 필수 정보

### 4. 템플릿 다운로드 및 사용

```bash
/aria template use 1                # 선택한 템플릿으로 문서 시작
/aria template download 1           # 템플릿 파일 다운로드
/aria template customize 1          # 조직 맞춤 템플릿 생성
```

## 템플릿 메타데이터 (Metadata)

각 템플릿이 포함하는 정보:

```yaml
Template Metadata:
  ID: "TMPL-FDA-510K-001"
  Name: "510(k) Premarket Notification Summary"
  Category: "Regulatory"
  Domain: ["FDA"]
  Language: ["English", "한국어"]

  Description: |
    510(k) submission을 위한 요약 템플릿.
    실질적 동등성 입증 필요.

  Sections:
    - Introduction
    - Device Description
    - Predicate Device Comparison
    - Substantial Equivalence Statement
    - Conclusion

  EstimatedTime: "3-5 hours"
  DifficultyLevel: "Intermediate"

  Requirements:
    - Predicate device information
    - 510(k) classification
    - Clinical data (if applicable)

  References:
    - FDA 510(k) Guidance
    - eCopy Format Requirements

  LastUpdated: "2026-02-09"
  Version: "1.0.0"
```

## 인수 조건 (Acceptance Criteria)

**AC-SKILL-004: 템플릿 라이브러리 제공**

```gherkin
Given: 문서 생성이 필요
When: aria-template 스킬 사용
Then:
  ✅ 템플릿 목록이 표시됨
  ✅ 템플릿 카테고리가 제공됨
  ✅ 템플릿 미리보기가 가능
  ✅ 템플릿 사용 가이드가 있음
```

**성공 기준:**
- 템플릿 라이브러리가 포괄적 (최소 50개 이상)
- 템플릿이 고품질 (VALID 준수)
- 사용자 정의 템플릿 지원
- 템플릿 검색이 효율적

## 관련 문서

- `.moai/specs/SPEC-ARIA-002/plan.md` - Template 커맨드 정의
- `aria-templates` - 템플릿 라이브러리 (aria-templates 스킬 참조)
