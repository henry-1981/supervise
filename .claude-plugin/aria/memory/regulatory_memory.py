"""
규제 결정 메모리 시스템

Regulatory Decision Memory 구현
"""

from datetime import datetime
from typing import Any, Dict, List, Optional
from .memory_storage import MemoryStorage


class RegulatoryMemory(MemoryStorage):
    """
    규제 결정 메모리

    기능:
    - 결정 저장 API (메타데이터 태깅 포함)
    - 관련성 점수 기반 결정 검색
    - 결정 유효성 추적 (만료 플래그)
    - 회사별 결정 분리
    """

    def __init__(self, project_dir: str):
        """
        규제 결정 메모리 초기화

        Args:
            project_dir: 프로젝트 루트 디렉토리
        """
        memory_path = f"{project_dir}/.claude/agent-memory/aria/regulatory-decisions.json"
        super().__init__(memory_path)
        self.schema_path = f"{project_dir}/.claude/agent-memory/aria/schemas/regulatory-decisions-schema.json"

    def store_decision(
        self,
        decision: str,
        rationale: str,
        category: str,
        company_id: str = "default",
        regulation: Optional[str] = None,
        article: Optional[str] = None,
        evidence: Optional[List[str]] = None,
        tags: Optional[List[str]] = None,
        valid_until: str = "9999-12-31T23:59:59Z"
    ) -> Optional[str]:
        """
        규제 결정 저장

        Args:
            decision: 결정 내용
            rationale: 결정 근거
            category: 규제 카테고리 (mdr, ivdr, fda 등)
            company_id: 회사 ID
            regulation: 규정 참조
            article: 조항 참조
            evidence: 증거 인용 목록
            tags: 검색 태그
            valid_until: 유효 기간

        Returns:
            저장된 결정 ID 또는 None (실패 시)
        """
        data = self._load()

        # 결정 ID 생성
        timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        decision_count = len(data.get('decisions', [])) + 1
        decision_id = f"decision-{decision_count:03d}-{timestamp}"

        new_decision = {
            "id": decision_id,
            "company_id": company_id,
            "category": category,
            "regulation": regulation,
            "article": article,
            "decision": decision,
            "rationale": rationale,
            "evidence": evidence or [],
            "valid_until": valid_until,
            "is_valid": True,
            "created_at": self.update_timestamp(),
            "updated_at": self.update_timestamp(),
            "tags": tags or [],
            "usage_count": 0,
            "last_used_at": None
        }

        # 초기 데이터 구조
        if 'decisions' not in data:
            data.update({
                "version": "1.0.0",
                "last_updated": self.update_timestamp(),
                "decisions": [],
                "metadata": {
                    "total_decisions": 0,
                    "active_decisions": 0,
                    "companies": [],
                    "categories": []
                }
            })

        data['decisions'].append(new_decision)
        self._update_metadata(data)

        if self._save(data):
            return decision_id
        return None

    def retrieve_decision(
        self,
        decision_id: str,
        company_id: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """
        ID로 결정 조회

        Args:
            decision_id: 결정 ID
            company_id: 회사 ID (선택사항)

        Returns:
            결정 데이터 또는 None
        """
        data = self._load()
        decisions = data.get('decisions', [])

        for decision in decisions:
            if decision['id'] == decision_id:
                # 회사 ID 확인
                if company_id and decision['company_id'] != company_id:
                    continue

                # 사용 카운트 증가
                decision['usage_count'] += 1
                decision['last_used_at'] = self.update_timestamp()
                self._save(data)
                return decision

        return None

    def search_decisions(
        self,
        query: str,
        company_id: str = "default",
        category: Optional[str] = None,
        min_relevance: float = 0.0
    ) -> List[Dict[str, Any]]:
        """
        관련성 점수 기반 결정 검색

        Args:
            query: 검색 쿼리
            company_id: 회사 ID
            category: 카테고리 필터 (선택사항)
            min_relevance: 최소 관련성 점수

        Returns:
            관련성 점수가 정렬된 결정 목록
        """
        data = self._load()
        decisions = data.get('decisions', [])

        results = []
        query_lower = query.lower()

        for decision in decisions:
            # 회사 ID 확인
            if decision['company_id'] != company_id:
                continue

            # 카테고리 필터링
            if category and decision.get('category') != category:
                continue

            # 유효성 확인
            if not decision.get('is_valid', True):
                continue

            # 관련성 점수 계산
            score = self._calculate_relevance(query_lower, decision)

            if score >= min_relevance:
                result = decision.copy()
                result['relevance_score'] = score
                results.append(result)

        # 관련성 점수로 정렬
        results.sort(key=lambda x: x['relevance_score'], reverse=True)
        return results

    def _calculate_relevance(self, query: str, decision: Dict[str, Any]) -> float:
        """
        관련성 점수 계산

        Args:
            query: 검색 쿼리 (소문자)
            decision: 결정 데이터

        Returns:
            관련성 점수 (0-1)
        """
        score = 0.0

        # decision 텍스트 검색
        if query in decision.get('decision', '').lower():
            score += 0.4

        # rationale 검색
        if query in decision.get('rationale', '').lower():
            score += 0.3

        # 태그 검색
        for tag in decision.get('tags', []):
            if query in tag.lower():
                score += 0.15
                break

        # 규정/조항 검색
        if decision.get('regulation') and query in decision['regulation'].lower():
            score += 0.1

        if decision.get('article') and query in decision['article'].lower():
            score += 0.05

        return min(score, 1.0)

    def invalidate_expired_decisions(self) -> int:
        """
        만료된 결정 무효화

        Returns:
            무효화된 결정 수
        """
        data = self._load()
        decisions = data.get('decisions', [])

        current_time = datetime.now()
        invalidated_count = 0

        for decision in decisions:
            if not decision.get('is_valid', True):
                continue

            valid_until = decision.get('valid_until')
            if valid_until:
                try:
                    # Z 접미사 처리 (UTC)
                    iso_string = valid_until.replace('Z', '') if valid_until.endswith('Z') else valid_until
                    expiry_time = datetime.fromisoformat(iso_string)
                    if current_time > expiry_time:
                        decision['is_valid'] = False
                        invalidated_count += 1
                except (ValueError, AttributeError):
                    pass

        if invalidated_count > 0:
            self._update_metadata(data)
            self._save(data)

        return invalidated_count

    def get_company_decisions(self, company_id: str) -> List[Dict[str, Any]]:
        """
        회사별 결정 목록 조회

        Args:
            company_id: 회사 ID

        Returns:
            회사 결정 목록
        """
        data = self._load()
        decisions = data.get('decisions', [])

        return [
            d for d in decisions
            if d['company_id'] == company_id and d.get('is_valid', True)
        ]

    def _update_metadata(self, data: Dict[str, Any]) -> None:
        """
        메타데이터 업데이트

        Args:
            data: 메모리 데이터
        """
        decisions = data.get('decisions', [])

        data['metadata'] = {
            'total_decisions': len(decisions),
            'active_decisions': sum(1 for d in decisions if d.get('is_valid', True)),
            'companies': list(set(d.get('company_id', 'default') for d in decisions)),
            'categories': list(set(d.get('category', 'other') for d in decisions if d.get('category')))
        }
        data['last_updated'] = self.update_timestamp()
