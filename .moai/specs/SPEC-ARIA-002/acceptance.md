# SPEC-ARIA-002: Acceptance Criteria

**TAG:** SPEC-ARIA-002
**Related:** spec.md, plan.md
**Created:** 2025-02-09

---

## 1. 인수 조건 개요 (Acceptance Criteria Overview)

이 문서는 ARIA Phase 2 (Universal Business Agents)의 인수 조건을 정의합니다. 각 요구사항에 대한 Given-When-Then 형식의 테스트 시나리오와 성공 기준을 제공합니다.

### 1.1 테스트 전략

**테스트 레벨:**
1. **단위 테스트 (Unit Tests)**: 개별 에이전트 및 스킬 기능
2. **통합 테스트 (Integration Tests)**: 에이전트 간 협업
3. **E2E 테스트 (End-to-End Tests)**: 전체 워크플로우
4. **품질 게이트 (Quality Gates)**: TRUST 5 및 VALID 검증

**테스트 도구:**
- pytest (Python 기반 테스트)
- Bash 스크립트 (통합 테스트)
- 수동 테스트 시나리오 (E2E)

---

## 2. Core Layer 인수 조건 (Core Layer Acceptance)

### 2.1 manager-docs (문서 관리자)

**AC-DOC-001: 문서 생성**
```gherkin
Given: 사용자가 규제 문서 생성을 요청
When: manager-docs에 문서 생성 명령을 전달
Then:
  - 적절한 템플릿이 선택되어야 함
  - 문서 구조가 템플릿을 따라야 함
  - 생성된 문서가 저장되어야 함
  - 문서 메타데이터가 기록되어야 함
```

**AC-DOC-002: 문서 버전 관리**
```gherkin
Given: 기존 문서가 존재
When: 사용자가 문서를 수정
Then:
  - 새 버전이 생성되어야 함
  - 변경 사항이 추적되어야 함
  - 이전 버전이 보존되어야 함
  - 버전 간 비교가 가능해야 함
```

**AC-DOC-003: 다중 형식 내보내기**
```gherkin
Given: 완성된 문서가 존재
When: 사용자가 PDF 형식 내보내기를 요청
Then:
  - PDF 파일이 생성되어야 함
  - 형식이 유지되어야 함
  - 서명 및 날짜가 포함되어야 함
```

**성공 기준:**
- [ ] 문서 생성이 30초 이내에 완료
- [ ] 버전 관리가 자동으로 수행
- [ ] PDF/Word/Markdown 형식 모두 지원
- [ ] 문서 메타데이터가 정확히 기록

### 2.2 manager-quality (품질 관리자)

**AC-QUAL-001: VALID Verified 차원 검증**
```gherkin
Given: 규제 문서 초안이 존재
When: manager-quality가 Verified 차원을 검증
Then:
  - 모든 규제 주장에 출처가 인용되어야 함
  - 인용이 원본 텍스트와 일치해야 함
  - 누락된 인용이 식별되어야 함
  - 부정확한 인용이 보고되어야 함
```

**AC-QUAL-002: VALID Accurate 차원 검증**
```gherkin
Given: 데이터와 수치가 포함된 문서
When: manager-quality가 Accurate 차원을 검증
Then:
  - 모든 데이터가 출처로부터 검증되어야 함
  - 수치가 정확해야 함
  - 날짜가 최신이어야 함
  - 모순되는 정보가 식별되어야 함
```

**AC-QUAL-003: 품질 보고서 생성**
```gherkin
Given: 문서 품질 검증이 완료됨
When: manager-quality가 품질 보고서를 생성
Then:
  - 각 VALID 차원별 점수가 포함되어야 함
  - 발견된 문제가 나열되어야 함
  - 개선 권장사항이 제공되어야 함
  - 전체 품질 등급이 할당되어야 함
```

**성공 기준:**
- [ ] VALID 5차원 모두 검증 가능
- [ ] 품질 점수 계산이 정확함
- [ ] 보고서가 5분 이내에 생성
- [ ] 개선 권장사항이 실행 가능함

### 2.3 manager-project (프로젝트 관리자)

**AC-PRJ-001: 마일스톤 추적**
```gherkin
Given: 프로젝트에 정의된 마일스톤이 존재
When: manager-project가 마일스톤 진행 상황을 확인
Then:
  - 각 마일스톤의 상태가 표시되어야 함
  - 완료율이 계산되어야 함
  - 지연된 마일스톤이 식별되어야 함
  - 다음 마일스톤이 제안되어야 함
```

**AC-PRJ-002: 진행 상황 보고**
```gherkin
Given: 프로젝트가 진행 중
When: 사용자가 진행 상황 보고를 요청
Then:
  - 완료된 작업 목록이 제공되어야 함
  - 진행 중인 작업이 표시되어야 함
  - 예상 완료 날짜가 제공되어야 함
  - 리스크 및 문제가 보고되어야 함
```

**성공 기준:**
- [ ] 마일스톤 추적이 실시간으로 업데이트
- [ ] 진행 상황 보고가 명확함
- [ ] 리스크가 적시에 식별됨
- [ ] 프로젝트 상태가 한눈에 파악 가능

---

## 3. Business Layer 인수 조건 (Business Layer Acceptance)

### 3.1 expert-writer (기술 작성 전문가)

**AC-WRT-001: 템플릿 기반 문서 작성**
```gherkin
Given: 문서 템플릿이 존재
When: expert-writer가 문서를 작성
Then:
  - 템플릿 구조를 따라야 함
  - 필수 섹션이 모두 포함되어야 함
  - 문체가 일관되어야 함
  - 용어가 표준을 따라야 함
```

**AC-WRT-002: 명확한 문체 유지**
```gherkin
Given: 기술 정보가 제공됨
When: expert-writer가 문서를 작성
Then:
  - 문장이 명확하고 간결해야 함
  - 수동태 과도 사용이 없어야 함
  - 전문 용어가 적절히 사용되어야 함
  - 불필요한 반복이 없어야 함
```

**성공 기준:**
- [ ] 작성된 문서가 템플릿을 준수
- [ ] 문체가 일관되고 명확함
- [ ] 기술 정확성이 유지됨
- [ ] 문서 작성 시간이 50% 단축

### 3.2 expert-analyst (데이터 분석 전문가)

**AC-ANL-001: 통계 분석 수행**
```gherkin
Given: 분석할 데이터 세트가 존재
When: expert-analyst가 통계 분석을 수행
Then:
  - 적절한 통계 기법이 적용되어야 함
  - 결과가 통계적으로 유의미해야 함
  - 추세가 식별되어야 함
  - 이상치가 보고되어야 함
```

**AC-ANL-002: 시각화 제공**
```gherkin
Given: 분석 결과가 존재
When: expert-analyst가 시각화를 생성
Then:
  - 차트 유형이 데이터에 적합해야 함
  - 축이 명확하게 라벨링되어야 함
  - 범례가 포함되어야 함
  - 인사이트가 강조되어야 함
```

**성공 기준:**
- [ ] 통계 분석이 정확함
- [ ] 시각화가 명확함
- [ ] 분석 결과가 실행 가능한 인사이트 제공
- [ ] 분석 시간이 10분 이내

### 3.3 expert-reviewer (문서 검토 전문가)

**AC-REV-001: 규제 준수성 검증**
```gherkin
Given: 검토할 문서가 존재
When: expert-reviewer가 규제 준수성을 검증
Then:
  - 모든 규제 요구사항이 충족되어야 함
  - 누락된 요구사항이 식별되어야 함
  - 비준수 사항이 보고되어야 함
  - 수정 권장사항이 제공되어야 함
```

**AC-REV-002: 일관성 검사**
```gherkin
Given: 문서 초안이 존재
When: expert-reviewer가 일관성을 검사
Then:
  - 용어 사용이 일관되어야 함
  - 형식이 통일되어야 함
  - 인용 스타일이 일관되어야 함
  - 모순되는 내용이 식별되어야 함
```

**성공 기준:**
- [ ] 규제 준수성이 100% 검증
- [ ] 일관성 문제가 모두 식별됨
- [ ] 피드백이 구체적이고 실행 가능함
- [ ] 검토 시간이 30분 이내

### 3.4 expert-researcher (규제 리서치 전문가)

**AC-RSR-001: 규제 정보 수집**
```gherkin
Given: 리서치 주제가 제공됨
When: expert-researcher가 정보를 수집
Then:
  - 관련 규제 문서가 식별되어야 함
  - 정보가 최신이어야 함
  - 출처가 신뢰할 수 있어야 함
  - 정보가 포괄적이어야 함
```

**AC-RSR-002: 출처 인용**
```gherkin
Given: 수집된 정보가 존재
When: expert-researcher가 출처를 인용
Then:
  - 각 정보에 출처가 인용되어야 함
  - 인용 형식이 표준을 따라야 함
  - 링크가 정확해야 함
  - 접근 날짜가 포함되어야 함
```

**성공 기준:**
- [ ] 리서치가 포괄적이고 정확함
- [ ] 출처 인용이 완전함
- [ ] 정보가 최신 상태 유지
- [ ] 리서치 시간이 20분 이내

---

## 4. 스킬 인수 조건 (Skill Acceptance)

### 4.1 aria-quality-valid 스킬

**AC-SKILL-001: VALID 5차원 정의**
```gherkin
Given: aria-quality-valid 스킬이 로드됨
When: VALID 프레임워크가 적용됨
Then:
  - Verified 차원 검증이 가능해야 함
  - Accurate 차원 검증이 가능해야 함
  - Linked 차원 검증이 가능해야 함
  - Inspectable 차원 검증이 가능해야 함
  - Deliverable 차원 검증이 가능해야 함
```

**AC-SKILL-002: 품질 점수 계산**
```gherkin
Given: 문서 품질 검증이 완료됨
When: 품질 점수가 계산됨
Then:
  - 각 차원별 점수가 계산되어야 함
  - 가중 평균이 적용되어야 함
  - 전체 점수가 0-100 범위여야 함
  - 등급이 할당되어야 함 (A/B/C/D/F)
```

**성공 기준:**
- [ ] VALID 5차원이 모두 구현됨
- [ ] 점수 계산이 정확함
- [ ] 품질 등급이 의미 있음
- [ ] 개선 권고사항이 실행 가능함

### 4.2 aria-writing-style 스킬

**AC-SKILL-003: 문체 가이드 제공**
```gherkin
Given: 기술 문서 작성이 필요함
When: aria-writing-style 스킬이 적용됨
Then:
  - 문체 가이드라인이 제공되어야 함
  - 용어 사용 표준이 정의되어야 함
  - 문장 구조 가이드가 있어야 함
  - 예제가 포함되어야 함
```

**성공 기준:**
- [ ] 문체 가이드가 포괄적임
- [ ] 용어 표준이 일관됨
- [ ] 예제가 실용적임
- [ ] 가이드가 쉽게 접근 가능함

### 4.3 aria-templates 스킬

**AC-SKILL-004: 템플릿 라이브러리 제공**
```gherkin
Given: 문서 생성이 필요함
When: aria-templates 스킬이 사용됨
Then:
  - 템플릿 목록이 표시되어야 함
  - 템플릿 카테고리가 제공되어야 함
  - 템플릿 미리보기가 가능해야 함
  - 템플릿 사용 가이드가 있어야 함
```

**성공 기준:**
- [ ] 템플릿 라이브러리가 포괄적임
- [ ] 템플릿이 고품질임
- [ ] 사용자 정의 템플릿이 지원됨
- [ ] 템플릿 검색이 효율적임

---

## 5. 커맨드 인수 조건 (Command Acceptance)

### 5.1 brief 커맨드

**AC-CMD-001: 작업 이해**
```gherkin
Given: 사용자가 새 작업을 시작함
When: /aria brief 커맨드가 실행됨
Then:
  - 작업 목적이 명확해져야 함
  - 범위가 정의되어야 함
  - 제약 조건이 식별되어야 함
  - 실행 계획이 제시되어야 함
```

**AC-CMD-002: 사용자 질의**
```gherkin
Given: 작업 범위가 불명확함
When: /aria brief가 명확성을 확보
Then:
  - 최대 4개 옵션의 질문이 제시되어야 함
  - 질문이 명확해야 함
  - 사용자 선택이 가능해야 함
  - 선택 후 계획이 업데이트되어야 함
```

**성공 기준:**
- [ ] 작업 이해가 5분 이내에 완료
- [ ] 실행 계획이 실행 가능함
- [ ] 사용자 질의가 효과적임
- [ ] 명확성이 90% 이상 확보됨

### 5.2 execute 커맨드

**AC-CMD-003: 워크플로우 실행**
```gherkin
Given: 실행 계획이 승인됨
When: /aria execute 커맨드가 실행됨
Then:
  - 연구 단계가 완료되어야 함
  - 작성 단계가 완료되어야 함
  - 검토 단계가 완료되어야 함
  - 정제 단계가 완료되어야 함
```

**AC-CMD-004: 진행 상황 보고**
```gherkin
Given: 워크플로우가 실행 중
When: /aria execute가 진행 상황을 보고
Then:
  - 현재 단계가 표시되어야 함
  - 완료율이 표시되어야 함
  - 남은 시간이 추정되어야 함
  - 문제가 보고되어야 함 (있는 경우)
```

**성공 기준:**
- [ ] 워크플로우가 순차적으로 실행됨
- [ ] 에이전트 협업이 원활함
- [ ] 진행 상황이 실시간으로 보고됨
- [ ] 오류가 적절히 처리됨

### 5.3 deliver 커맨드

**AC-CMD-005: 최종 산출물 생성**
```gherkin
Given: 워크플로우가 완료됨
When: /aria deliver 커맨드가 실행됨
Then:
  - 품질 검증이 통과되어야 함
  - 최종 문서가 생성되어야 함
  - 형식 변환이 완료되어야 함
  - 배포가 완료되어야 함
```

**성공 기준:**
- [ ] 품질 검증이 100% 통과
- [ ] 최종 산출물이 기대를 충족
- [ ] 배포가 자동으로 완료
- [ ] 사용자 알림이 전송됨

---

## 6. MCP 통합 인수 조건 (MCP Integration Acceptance)

### 6.1 Context7 MCP

**AC-MCP-001: 규제 문서 조회**
```gherkin
Given: 리서치 주제가 제공됨
When: Context7 MCP로 규제 문서 조회
Then:
  - 관련 문서가 식별되어야 함
  - 문서 내용이 검색 가능해야 함
  - 인용이 가능해야 함
  - 출처가 확인되어야 함
```

**성공 기준:**
- [ ] 문서 조회가 10초 이내에 완료
- [ ] 검색 결과가 정확함
- [ ] 인용 형식이 표준을 준수
- [ ] 연결이 안정적임

### 6.2 Sequential Thinking MCP

**AC-MCP-002: 복잡한 분석**
```gherkin
Given: 복잡한 규제 경로 분석이 필요함
When: Sequential Thinking MCP가 실행됨
Then:
  - 문제가 단계적으로 분석되어야 함
  - 각 단계의 논리가 명확해야 함
  - 결론이 도출되어야 함
  - 대안이 제시되어야 함
```

**성공 기준:**
- [ ] 분석이 체계적임
- [ ] 결론이 타당함
- [ ] 분석 시간이 5분 이내
- [ ] 결과가 문서화됨

### 6.3 Notion MCP

**AC-MCP-003: 지식 베이스 동기화**
```gherkin
Given: 새 문서가 생성됨
When: Notion MCP로 동기화
Then:
  - 문서가 Notion에 생성되어야 함
  - 메타데이터가 포함되어야 함
  - 태그가 할당되어야 함
  - 링크가 생성되어야 함
```

**성공 기준:**
- [ ] 동기화가 자동으로 완료
- [ ] 데이터가 정확히 전송
- [ ] 형식이 유지됨
- [ ] 오류 처리가 적절함

---

## 7. E2E 테스트 시나리오 (End-to-End Test Scenarios)

### 7.1 시나리오 1: 규제 문서 작성 워크플로우

```gherkin
Scenario: 완전한 규제 문서 작성

Given: 사용자가 "의료기기 소프트웨어 검증 보고서" 작성을 원함
When: /aria brief "의료기기 소프트웨어 검증 보고서 작성" 실행
Then:
  - 작업 목적이 명확해짐
  - 필요한 정보가 식별됨
  - 실행 계획이 제시됨

When: 사용자가 계획을 승인
And: /aria execute가 실행됨
Then:
  - expert-researcher가 관련 규제를 수집
  - expert-writer가 문서 초안 작성
  - expert-reviewer가 문서 검토
  - expert-analyst가 데이터 분석 제공
  - manager-quality가 품질 검증

When: /aria deliver가 실행됨
Then:
  - 최종 문서가 생성됨
  - PDF 형식으로 변환됨
  - Notion에 동기화됨
  - 사용자에게 알림 전송

Then:
  - 전체 워크플로우가 2시간 이내에 완료
  - 품질 등급이 A 또는 B
  - 사용자 만족도가 90% 이상
```

### 7.2 시나리오 2: 다중 에이전트 협업

```gherkin
Scenario: CAPA 작성 및 검토

Given: CAPA 문서 작성이 필요함
When: /aria brief "CAPA-001: 문서화 오류 수정" 실행
Then:
  - 문제가 명확히 정의됨
  - 근본 원본이 분석됨
  - 수정 계획이 수립됨

When: /aria execute가 실행됨
Then:
  - expert-analyst가 데이터 분석
  - expert-writer가 CAPA 작성
  - expert-reviewer가 적절성 검토
  - manager-quality가 VALID 검증

When: /aria deliver가 실행됨
Then:
  - CAPA가 승인됨
  - 이해관계자에게 배포됨
  - 관련 SPEC에 연결됨
  - 완료 날짜가 설정됨

Then:
  - CAPA 품질 기준 충족
  - 규제 준수성 확인
  - 추적성 유지
```

---

## 8. 품질 게이트 (Quality Gates)

### 8.1 Phase 2.1 품질 게이트

**Gate 1: Core Layer 기능**
- [ ] 모든 Core 에이전트가 단위 테스트 통과
- [ ] VALID 프레임워크가 규제 문서 검증에 적용 가능
- [ ] 기본 워크플로우가 작동
- [ ] 코드 커버리지 85%+ 달성

**Gate 2: 문서 및 품질**
- [ ] 모든 에이전트에 설명 문서 존재
- [ ] TRUST 5 기준 충족
- [ ] MCP 연결이 안정적
- [ ] 사용자 가이드 제공

### 8.2 Phase 2.2 품질 게이트

**Gate 3: Business Layer 기능**
- [ ] 모든 Business 에이전트가 단위 테스트 통과
- [ ] 문서 작성-검토 워크플로우가 작동
- [ ] 템플릿 기반 문서 생성 가능
- [ ] 에이전트 협업이 원활

**Gate 4: 워크플로우 완성**
- [ ] Brief-Execute-Deliver가 완전히 작동
- [ ] 품질 게이트가 통과
- [ ] 사용자 피드백이 긍정적
- [ ] 성능 기준 충족

### 8.3 Phase 2.3 품질 게이트

**Gate 5: MCP 통합**
- [ ] 모든 MCP 연결이 정상 작동
- [ ] 리서치/분석 워크플로우가 작동
- [ ] Notion 데이터 동기화 가능
- [ ] Context7 조회가 정확

**Gate 6: 전체 시스템**
- [ ] E2E 테스트가 통과
- [ ] 실제 RA/QA 워크플로우 지원
- [ ] 사용자 만족도 90%+
- [ ] 프로덕션 준비 완료

---

## 9. Definition of Done

각 기능은 다음 기준을 모두 충족해야 "완료"로 간주됩니다:

### 9.1 기능 완료 기준

- [ ] 요구사항의 모든 인수 조건 충족
- [ ] 단위 테스트 85%+ 커버리지
- [ ] 통합 테스트 통과
- [ ] 코드 리뷰 완료 및 승인
- [ ] 문서화 완료 (API, 사용자 가이드)
- [ ] TRUST 5 품질 기준 충족
- [ ] 성능 기준 충족
- [ ] 보안 검토 통과

### 9.2 Phase 완료 기준

- [ ] 해당 Phase의 모든 기능이 완료 상태
- [ ] E2E 테스트 시나리오 통과
- [ ] 품질 게이트 통과
- [ ] 사용자 승인 획득
- [ ] 프로덕션 배포 준비 완료

---

**TAG BLOCK END**

**다음 단계:**
- Phase 2.1 개발 시작
- Core Layer 에이전트 구현
- VALID 프레임워크 스킬 개발
