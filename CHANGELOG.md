# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-02-09

### Added - ARIA Phase 4 MCP 통합 시스템

#### MCP 통합 (MCP Integration)
- Notion MCP 서버 통합
  - 6개 데이터베이스 자동 생성 (Regulatory Requirements, Document Registry, CAPA Tracker, Risk Register, Submission Tracker, Knowledge Base)
  - CRUD 작업 지원 (생성, 조회, 수정, 삭제)
  - 관계(Relation) 설정으로 데이터 연결
  - 감사 추적(Audit Trail) 자동 기록
  - 뷰(View) 생성 및 사용자 정의

- Google Workspace MCP 서버 통합
  - Gmail: 규제 서신 검색 및 요약
  - Google Docs: 협업 문서 생성 및 편집
  - Google Sheets: 데이터 분석 및 시각화
  - Google Calendar: 데드라인 관리 및 알림
  - Google Drive: 파일 저장 및 버전 관리
  - OAuth 2.0 인증 플로우 구현

- Context7 MCP 서버 통합
  - 최신 규정 검색 (FDA 21 CFR 820, ISO 13485, EU MDR)
  - 자동 지식 베이스 업데이트
  - 규정 변경 알림

#### ARIA 에이전트 시스템 (9개)
- **aria-orchestrator**: 워크플로우 조정 및 MCP 통합 관리
- **aria-regulatory**: FDA, MDR, MFDS 규정 전문
- **aria-clinical**: 임상 평가 요구사항 전문
- **aria-quality**: QMS, CAPA, 감사 준비 전문
- **aria-risk**: ISO 14971 위험 관리 전문
- **aria-postmarket**: 시판 후 조사, PMCF, 불만 전문
- **aria-document**: 기술 문서, 라벨링 전문
- **aria-submission**: 510(k), CE, PMA 제출 전문
- **aria-labeling**: IFU, 라벨, UDI 전문

#### ARIA 스킬 시스템 (3개)
- **aria-integration-notion**: Notion MCP 통합 스킬
  - Notion DB 스키마 정의
  - CRUD 작업 가이드
  - 감사 추적 기능
  - MCP 도구 사용법

- **aria-integration-google**: Google Workspace MCP 통합 스킬
  - Google 서비스별 통합 가이드
  - OAuth 2.0 인증 플로우
  - 협업 도구 사용법

- **aria-integration-context7**: Context7 MCP 통합 스킬
  - 규제 검색 패턴
  - 지식 베이스 자동 업데이트
  - 캐시 전략

#### ARIA 명령어 시스템 (5개)
- **/aria init**: 초기화 명령어
  - Notion DB 생성 및 설정
  - Google Workspace OAuth 설정
  - MCP 서버 설정 가이드

- **/aria search**: 통합 검색 명령어
  - Notion DB 검색
  - Context7 규정 검색
  - Google Workspace 검색
  - 관련성 점수 기반 정렬

- **/aria knowledge**: 지식 베이스 조회 명령어
  - Notion Knowledge Base 조회
  - Context7 자동 검색 및 저장
  - 관련 문서 연결

- **/aria status**: 상태 대시보드 명령어
  - CAPA 추적 현황
  - 위험 등록부 현황
  - 제출 추적 현황
  - 문서 등록부 현황
  - Google Calendar 이벤트

- **/aria audit**: 감사 추적 명령어
  - 감사 로그 검색
  - 필터링 기능 (Agent, Date, Action, Entity)
  - CSV/PDF 내보내기

#### 워크플로우 및 품질 시스템
- Brief-Execute-Deliver 방법론 구현
- VALID 품질 프레임워크 (Verified, Accurate, Linked, Inspectable, Deliverable)
- 추적성 매트릭스 (요구사항 → 문서 → 증거)
- 감사 추적 자동 기록

#### 문서화
- README.md: 시스템 개요, 설치, 사용법
- CHANGELOG.md: 변경 이력 (본 문서)
- SPEC-ARIA-004/spec.md: 상세 기술 사양서
- MCP 설정 가이드 (.mcp.json)
- 데이터베이스 스키마 정의

### Features
- 통합 검색 엔진 (Notion, Google, Context7)
- 상태 대시보드 실시간 업데이트
- 감사 추적 무결성 보장
- 자동 지식 베이스 업데이트
- 규정 변경 알림 시스템
- 관계(Relation) 설정으로 데이터 연결
- 뷰(View) 생성 및 사용자 정의
- OAuth 2.0 인증 플로우
- API 할당량 모니터링
- 오류 처리 및 재시도 메커니즘

### Technical Details
- MCP 서버: Notion, Google Workspace, Context7
- 데이터베이스: 6개 Notion DB
- 에이전트: 9개 ARIA 전문가 에이전트
- 스킬: 3개 MCP 통합 스킬
- 명령어: 5개 ARIA 명령어
- 언어: 한국어 (주), 영어 (보조)
- 라이선스: Apache-2.0

### Dependencies
- Claude Code with MCP support
- Notion API
- Google Workspace APIs
- Context7 MCP
- Node.js (MCP 서버 실행)

### Breaking Changes
- 기존 Cowork Supervisor 플러그인에서 ARIA Phase 4로 완전히 교체
- Notion workspace 및 API 키 필요
- Google Workspace 계정 필요

### Migration Guide
기존 Cowork Supervisor 사용자를 위한 마이그레이션 가이드:

1. Notion workspace 준비
   - Notion Integration Token 발급
   - 환경 변수 설정: `export NOTION_API_KEY=your_token`

2. Google Cloud 프로젝트 설정
   - Google Cloud Console에서 프로젝트 생성
   - API 활성화: Gmail, Docs, Sheets, Calendar, Drive
   - OAuth 클라이언트 ID 생성

3. MCP 서버 설정
   - `.mcp.json` 파일에 MCP 서버 추가
   - 환경 변수 설정

4. ARIA 초기화
   - `/aria init notion` 실행
   - `/aria init google` 실행

### Known Issues
- Google API 할당량 초과 시 재시도 필요
- Notion API 속도 제한 준수 필요
- Context7 검색 결과 캐시 만료 기간: 30일

### Future Plans
- 추가 MCP 서버 통합 (Slack, Microsoft Teams)
- 고급 검색 필터링
- 자화서 기능 강화
- 다국어 지원 확대
- 모바일 앱 지원

---

## [0.1.0] - 2026-02-05

### Added
- Initial release of Cowork Supervisor plugin
- Intent Clarifier agent for understanding user requests
- Capability Discoverer agent for plugin detection
- Supervisor Planner agent for execution planning
- Orchestra agent for multi-plugin coordination
- Aggregator agent for result synthesis
- `/supervise` command for easy invocation

### Features
- Multi-plugin orchestration with parallel/sequential execution
- Automatic plugin capability discovery
- User approval checkpoints for execution plans
- Error handling with fallback strategies
- Cross-domain result aggregation with conflict resolution
- Source attribution in final responses
