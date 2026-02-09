"""
회사偏好 메모리 시스템

Company Preference Learning 구현
"""

from typing import Any, Dict, List, Optional
from .memory_storage import MemoryStorage


class PreferenceMemory(MemoryStorage):
    """
    회사偏好 메모리

    기능:
    - 사용자 인터랙션에서偏好 추출
    -偏好 적용 엔진
    - 충돌 감지 및 해결
    """

    def __init__(self, project_dir: str):
        """
       偏好 메모리 초기화

        Args:
            project_dir: 프로젝트 루트 디렉토리
        """
        memory_path = f"{project_dir}/.claude/agent-memory/aria/company-preferences.json"
        super().__init__(memory_path)
        self.schema_path = f"{project_dir}/.claude/agent-memory/aria/schemas/company-preferences-schema.json"

    def get_preferences(self, company_id: str = "default") -> Dict[str, Any]:
        """
        회사偏好 조회

        Args:
            company_id: 회사 ID

        Returns:
           偏好 딕셔너리
        """
        data = self._load()
        companies = data.get('companies', {})

        # 기본偏好 반환 (회사가 없으면 생성)
        if company_id not in companies:
            return self._get_default_preferences(company_id)

        return companies[company_id].get('preferences', {})

    def _get_default_preferences(self, company_id: str) -> Dict[str, Any]:
        """
        기본偏好 반환

        Args:
            company_id: 회사 ID

        Returns:
            기본偏好 딕셔너리
        """
        # terminology를 깊은 복사하여 반환
        default_terminology = {
            'medical_device': 'medical device',
            'manufacturer': 'manufacturer',
            'authorized_representative': 'authorized representative',
            'pms': 'post-market surveillance',
            'pmcf': 'post-market clinical follow-up'
        }

        return {
            'formatting': {
                'document_template': 'imdrf',
                'date_format': 'iso-8601',
                'number_format': 'eu',
                'language': 'en',
                'terminology_style': 'harmonized'
            },
            'terminology': default_terminology.copy(),
            'regulatory_framework': {
                'primary': 'mdr',
                'secondary': ['ivdr'],
                'notified_body': 'default-nb',
                'iec_standards': ['iso-13485', 'iso-14971']
            },
            'workflow': {
                'default_reviewer': 'quality-manager',
                'approval_required': True,
                'version_control': 'semantic'
            }
        }

    def extract_preference(
        self,
        company_id: str,
        category: str,
        key: str,
        value: Any,
        confidence: float = 0.8
    ) -> bool:
        """
        사용자 인터랙션에서偏好 추출 및 저장

        Args:
            company_id: 회사 ID
            category:偏好 카테고리 (formatting, terminology 등)
            key:偏好 키
            value:偏好 값
            confidence: 추출 신뢰도

        Returns:
            저장 성공 여부
        """
        data = self._load()

        # 초기 데이터 구조
        if 'companies' not in data:
            data.update({
                'version': '1.0.0',
                'last_updated': self.update_timestamp(),
                'companies': {},
                'metadata': {
                    'total_companies': 0,
                    'active_companies': 0,
                    'preference_categories': []
                }
            })

        # 회사偏好 초기화
        if company_id not in data['companies']:
            data['companies'][company_id] = {
                'company_id': company_id,
                'company_name': f'Company {company_id}',
                'preferences': self._get_default_preferences(company_id),
                'created_at': self.update_timestamp(),
                'updated_at': self.update_timestamp(),
                'preference_conflicts': []
            }

        company = data['companies'][company_id]
        preferences = company['preferences']

        # 카테고리 초기화
        if category not in preferences:
            preferences[category] = {}

        # 기존 값 확인 및 충돌 감지
        if key in preferences[category]:
            existing_value = preferences[category][key]
            if existing_value != value:
                # 충돌 기록
                conflict = {
                    'conflict_id': f"conflict-{len(company['preference_conflicts']) + 1}",
                    'preference': f"{category}.{key}",
                    'existing_value': existing_value,
                    'new_value': value,
                    'detected_at': self.update_timestamp(),
                    'resolved': False,
                    'confidence': confidence
                }
                company['preference_conflicts'].append(conflict)

                # 충돌 해결: 신뢰도가 더 높은 값 선택
                # 여기서는 간단히 새 값으로 대체
                preferences[category][key] = value
        else:
            # 새偏好 저장
            preferences[category][key] = value

        company['updated_at'] = self.update_timestamp()
        self._update_metadata(data)

        return self._save(data)

    def apply_preferences(
        self,
        content: str,
        company_id: str = "default",
        categories: Optional[List[str]] = None
    ) -> str:
        """
       偏好 적용 엔진

        Args:
            content: 원본 콘텐츠
            company_id: 회사 ID
            categories: 적용할 카테고리 목록 (None이면 전체)

        Returns:
           偏好가 적용된 콘텐츠
        """
        preferences = self.get_preferences(company_id)

        if categories is None:
            categories = list(preferences.keys())

        result = content

        # terminology 적용
        if 'terminology' in categories and 'terminology' in preferences:
            terminology = preferences['terminology']
            for standard, company_term in terminology.items():
                # 키의 _를 공백으로 변환하여 검색
                search_term = standard.replace('_', ' ')
                result = result.replace(search_term, company_term)

        # formatting 적용
        if 'formatting' in categories and 'formatting' in preferences:
            formatting = preferences['formatting']

            # 날짜 형식 변환 (간단 구현)
            if formatting.get('date_format') == 'mm/dd/yyyy':
                # ISO 형식을 US 형식으로 변환
                import re
                result = re.sub(
                    r'(\d{4})-(\d{2})-(\d{2})',
                    r'\2/\3/\1',
                    result
                )

        return result

    def detect_conflicts(self, company_id: str) -> List[Dict[str, Any]]:
        """
       偏好 충돌 감지

        Args:
            company_id: 회사 ID

        Returns:
            충돌 목록
        """
        data = self._load()
        companies = data.get('companies', {})

        if company_id not in companies:
            return []

        return companies[company_id].get('preference_conflicts', [])

    def resolve_conflict(
        self,
        company_id: str,
        conflict_id: str,
        resolution: str
    ) -> bool:
        """
       偏好 충돌 해결

        Args:
            company_id: 회사 ID
            conflict_id: 충돌 ID
            resolution: 해결 방법 (keep_existing, use_new, custom)

        Returns:
            해결 성공 여부
        """
        data = self._load()
        companies = data.get('companies', {})

        if company_id not in companies:
            return False

        company = companies[company_id]
        conflicts = company.get('preference_conflicts', [])

        for conflict in conflicts:
            if conflict['conflict_id'] == conflict_id:
                if resolution == 'keep_existing':
                    # 기존 값 유지
                    pass
                elif resolution == 'use_new':
                    # 새 값으로 변경
                    pref_path = conflict['preference'].split('.')
                    if len(pref_path) == 2:
                        category, key = pref_path
                        preferences = company['preferences']
                        if category in preferences:
                            preferences[category][key] = conflict['new_value']

                conflict['resolved'] = True
                conflict['resolved_at'] = self.update_timestamp()
                company['updated_at'] = self.update_timestamp()

                return self._save(data)

        return False

    def _update_metadata(self, data: Dict[str, Any]) -> None:
        """
        메타데이터 업데이트

        Args:
            data: 메모리 데이터
        """
        companies = data.get('companies', {})

        all_categories = set()
        for company in companies.values():
            preferences = company.get('preferences', {})
            all_categories.update(preferences.keys())

        data['metadata'] = {
            'total_companies': len(companies),
            'active_companies': len(companies),
            'preference_categories': list(all_categories)
        }
        data['last_updated'] = self.update_timestamp()
