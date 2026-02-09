---
name: aria-integration-context7
description: >
  Context7 MCP 최적화를 위한 ARIA 스킬. FDA, ISO, EU MDR 규정 검색 패턴과
  TTL 캐싱을 통한 지식 기반 자동 업데이트를 제공합니다. 의료기기 규제 준수 문서 검색에 사용합니다.
license: Apache-2.0
compatibility: Designed for Claude Code
allowed-tools: Read Grep Glob
user-invocable: true
metadata:
  version: "1.0.0"
  category: "domain"
  status: "active"
  updated: "2026-02-09"
  modularized: "false"
  tags: "context7, mcp, regulatory, search, fda, iso, mdr, cache, aria"
  author: "MoAI-ARIA"
  context7-libraries: "fda-regulations,iso-standards,eu-mdr"
  argument-hint: "규정 검색 및 지식 기반 업데이트"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords:
    - "context7"
    - "regulatory search"
    - "fda"
    - "iso"
    - "eu mdr"
    - "mdr"
    - "regulation"
    - "standard"
    - "cache"
    - "ttl"
    - "규정"
    - "검색"
    - "표준"
  agents:
    - "expert-backend"
    - "manager-spec"
  phases:
    - "plan"
    - "run"
  languages:
    - "typescript"
    - "python"
---

# ARIA Context7 Integration

ARIA 규제 관리 시스템을 위한 Context7 MCP 최적화 스킬입니다. 의료기기 규정 검색 패턴과 지식 기반 자동 업데이트를 제공합니다.

## 빠른 시작

### MCP 서버 설정

.mcp.json에 Context7 MCP 서버가 이미 구성되어 있는지 확인합니다:

```json
{
  "mcpServers": {
    "context7": {
      "command": "/bin/bash",
      "args": ["-l", "-c", "exec npx -y @upstash/context7-mcp@latest"]
    }
  }
}
```

### 라이브러리 식별자 확인

```bash
# 사용 가능한 규정 라이브러리 검색
ToolSearch("fda regulations")
ToolSearch("iso 13485")
ToolSearch("eu mdr")
```

## 규정 검색 패턴

### FDA (미국 식약처)

#### 주요 규정 라이브러리

| 라이브러리 ID | 설명 | 검색 키워드 |
|---------------|------|------------|
| fda-21-cfr-part-11 | 전자 서명/전자 기록 | electronic, signature, record, part 11 |
| fda-21-cfr-part-820 | 품질 시스템 규정 (QSR) | quality, system, qsr, 21 cfr 820 |
| fda-510k | 시판 전 통지 | 510k, premarket, notification |
| fda-pma | 시판 전 승인 | pma, premarket, approval |

#### FDA 검색 패턴

```javascript
// 21 CFR Part 11 관련 검색
mcp__context7__resolve-library-id({
  query: "fda 21 cfr part 11 electronic signature"
});

// QSR 요구사항 검색
mcp__context7__get-library-docs({
  libraryId: "fda-21-cfr-part-820",
  query: "design controls validation"
});
```

### ISO (국제 표준화 기구)

#### 주요 표준 라이브러리

| 라이브러리 ID | 설명 | 검색 키워드 |
|---------------|------|------------|
| iso-13485 | 의료기기 품질 경영 시스템 | quality, management, system, qms |
| iso-14971 | 의료기기 위험 관리 | risk, management, hazard |
| iso-14971-2019 | 위험 관리 (2019 개정) | risk, 2019, application |
| iso-9001 | 품질 경영 시스템 | quality, management, standard |

#### ISO 검색 패턴

```javascript
// ISO 13485 품질 경영 시스템 검색
mcp__context7__resolve-library-id({
  query: "iso 13485 quality management system"
});

// 위험 관리 프로세스 검색
mcp__context7__get-library-docs({
  libraryId: "iso-14971",
  query: "risk analysis evaluation benefit risk"
});
```

### EU MDR (유럽 의료기기 규정)

#### 주요 규정 라이브러리

| 라이브러리 ID | 설명 | 검색 키워드 |
|---------------|------|------------|
| eu-mdr-2017-745 | 의료기기 규정 | mdr, 2017/745, regulation |
| eu-mdr-annex-i | 일반 안전/성능 요구사항 | annex i, essential requirements |
| eu-mdr-annex-ix | CE 마크 프로세스 | annex ix, conformity assessment |
| eu-mdr-annex-xv | 임상 평가/조사 | clinical, investigation, performance |

#### EU MDR 검색 패턴

```javascript
// MDR 규정 전체 검색
mcp__context7__resolve-library-id({
  query: "eu mdr 2017/745 medical device regulation"
});

// 임상 평가 요구사항 검색
mcp__context7__get-library-docs({
  libraryId: "eu-mdr-annex-xv",
  query: "clinical evaluation investigation plan"
});
```

## 검색 최적화

### 검색어 구성

효율적인 검색을 위해 다음 패턴을 사용합니다:

1. **규정 코드 우선**: "21 CFR 820", "ISO 13485", "MDR 2017/745"
2. **키워드 조합**: "design validation", "risk assessment", "clinical evaluation"
3. **섹션 지정**: "part 11", "annex i", "chapter 4"
4. **버전 지정**: "2019 revision", "2024 update"

### 검색 결과 캐싱

```javascript
// 캐시 구조
const searchCache = {
  key: "fda-21-cfr-820-design-controls",
  query: "design controls validation",
  timestamp: Date.now(),
  ttl: 3600000, // 1시간 (밀리초)
  results: [...]
};

// 캐시 확인
function getCachedResult(key) {
  const cached = cacheStore.get(key);
  if (cached && (Date.now() - cached.timestamp) < cached.ttl) {
    return cached.results;
  }
  return null;
}
```

## 지식 기반 자동 업데이트

### Notion Knowledge Base 연동

```javascript
// Context7 검색 결과를 Notion에 자동 저장
async function updateKnowledgeBase(query, results) {
  const page = await notion.pages.create({
    parent: { database_id: KNOWLEDGE_BASE_DB },
    properties: {
      "Article ID": { title: [{ text: { content: `KB-${Date.now()}` } }] },
      "Category": { select: { name: "Guideline" } },
      "Tags": { multi_select: [{ name: "FDA" }, { name: "QSR" }] },
      "Content": { rich_text: [{ text: { content: results.summary } }] },
      "Source": { url: results.sourceUrl },
      "Last Updated": { date: { start: new Date().toISOString() } },
      "TTL": { number: 3600 } // 1시간 캐시
    }
  });
}
```

### TTL (Time To Live) 캐싱 전략

| 콘텐츠 유형 | TTL | 갱신 주기 |
|-------------|-----|----------|
| 규정 원문 | 7일 (604800초) | 주간 |
| 규정 해석 | 3일 (259200초) | 3일 |
| 가이드라인 | 1일 (86400초) | 일일 |
| 뉴스/업데이트 | 1시간 (3600초) | 시간별 |

### 캐시 무효화 조건

다음 조건에서 캐시를 무효화합니다:

1. TTL 만료
2. 규정 변경 감지
3. 사용자 요청에 의한 갱신
4. 정기 업데이트 스케줄

## MCP 도구 사용

### ToolSearch로 도구 로드

```javascript
// Context7 MCP 도구 검색 및 로드
ToolSearch("context7 fda regulations")
ToolSearch("context7 iso standards")
ToolSearch("context7 eu mdr")
```

### 사용 가능한 도구

| 도구 | 기능 | 사용 사례 |
|------|------|-----------|
| `mcp__context7__resolve-library-id` | 라이브러리 식별자 확인 | 규정 라이브러리 검색 |
| `mcp__context7__get-library-docs` | 문서 내용 가져오기 | 특정 규정 섹션 조회 |
| `mcp__context7__search-docs` | 전체 검색 | 여러 규정 동시 검색 |

## 통합 검색 예시

### 규정 준수 확인

```javascript
// 여러 규정에서 동시에 검색
async function checkCompliance(requirement) {
  const searches = [
    {
      source: "FDA 21 CFR 820",
      query: requirement,
      libraryId: "fda-21-cfr-part-820"
    },
    {
      source: "ISO 13485",
      query: requirement,
      libraryId: "iso-13485"
    },
    {
      source: "EU MDR",
      query: requirement,
      libraryId: "eu-mdr-2017-745"
    }
  ];

  const results = await Promise.all(
    searches.map(s =>
      mcp__context7__get-library-docs({
        libraryId: s.libraryId,
        query: s.query
      })
    )
  );

  return aggregateResults(results);
}
```

### 위험 평가 지원

```javascript
// 위험 관리 관련 규정 검색
async function searchRiskManagementRequirements() {
  return {
    iso14971: await getLibraryDocs("iso-14971", "risk management process"),
    fdaQsr: await getLibraryDocs("fda-21-cfr-part-820", "risk analysis"),
    euMdr: await getLibraryDocs("eu-mdr-annex-i", "risk mitigation")
  };
}
```

## 모범 사례

1. **검색어 최적화**: 구체적인 규정 코드와 섹션 번호 사용
2. **캐시 활용**: TTL 설정으로 불필요한 API 호출 최소화
3. **결과 검증**: 공식 소스와 교차 확인
4. **정기 업데이트**: 규정 변경사항 주기적 확인
5. **버전 관리**: 검색 결과에 버전/날짜 정보 포함

## MoAI 통합

- manager-spec: 규정 요구사항 분석
- expert-backend: 검색 API 구현
- manager-quality: 준수 검증

버전 기록:
- v1.0.0 (2026-02-09): 초기 릴리스
