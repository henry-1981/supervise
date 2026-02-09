"""
작업 패턴 메모리 시스템

Task Pattern Recognition 구현
"""

from typing import Any, Dict, List, Optional
from .memory_storage import MemoryStorage


class PatternMemory(MemoryStorage):
    """
    작업 패턴 메모리

    기능:
    - 작업 시퀀스 추적 (3회 이상 반복)
    - 패턴 제안 알고리즘
    - 워크플로우 템플릿 생성
    """

    def __init__(self, project_dir: str):
        """
        패턴 메모리 초기화

        Args:
            project_dir: 프로젝트 루트 디렉토리
        """
        memory_path = f"{project_dir}/.claude/agent-memory/aria/task-patterns.json"
        super().__init__(memory_path)
        self.schema_path = f"{project_dir}/.claude/agent-memory/aria/schemas/task-patterns-schema.json"
        self._task_history: List[Dict[str, Any]] = []

    def track_task(self, task_description: str, steps: List[Dict[str, Any]]) -> Optional[str]:
        """
        작업 시퀀스 추적

        Args:
            task_description: 작업 설명
            steps: 작업 단계 목록

        Returns:
            감지된 패턴 ID 또는 None
        """
        # 현재 작업의 기록 생성
        task_record = {
            'description': task_description,
            'steps': steps,
            'timestamp': self.update_timestamp()
        }

        # 현재 작업을 제외한 기록 수 확인
        history_count = len(self._task_history)

        # 현재 작업이 있는지 확인 (같은 작업인지)
        existing_similar_count = sum(
            1 for t in self._task_history
            if self._calculate_step_similarity(t['steps'], steps) >= 0.9
        )

        # 작업 기록 저장
        self._task_history.append(task_record)

        # 총 3회 이상 반복되면 패턴 감지
        if existing_similar_count >= 2:
            pattern_id = self._detect_pattern(task_description, steps)
            if pattern_id:
                return pattern_id

        return None

    def _detect_pattern(self, task_description: str, steps: List[Dict[str, Any]]) -> Optional[str]:
        """
        패턴 감지 알고리즘

        Args:
            task_description: 작업 설명
            steps: 작업 단계 목록

        Returns:
            감지된 패턴 ID 또는 None
        """
        data = self._load()

        # 초기 데이터 구조
        if 'patterns' not in data:
            data.update({
                'version': '1.0.0',
                'last_updated': self.update_timestamp(),
                'patterns': [],
                'metadata': {
                    'total_patterns': 0,
                    'high_confidence_patterns': 0,
                    'pattern_tags': []
                }
            })

        # 유사한 작업 검색
        similar_tasks = self._find_similar_tasks(task_description, steps)

        # 패턴 발생 횟수 확인 (현재 작업 포함하여 3회 이상)
        # similar_tasks는 현재 작업을 제외한 이전 작업들
        if len(similar_tasks) >= 2:  # 2개의 이전 유사 작업 + 현재 = 3회
            # 기존 패턴 확인
            for pattern in data['patterns']:
                if self._is_pattern_match(pattern, steps):
                    # 발생 횟수 증가
                    pattern['occurrence_count'] += 1
                    # 신뢰도 재계산
                    pattern['confidence'] = min(0.5 + (pattern['occurrence_count'] * 0.1), 1.0)
                    pattern['updated_at'] = self.update_timestamp()

                    self._update_metadata(data)
                    self._save(data)
                    return pattern['id']

            # 새 패턴 생성
            return self._create_pattern(data, task_description, steps)

        return None

    def _find_similar_tasks(self, task_description: str, steps: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        유사한 작업 찾기

        Args:
            task_description: 작업 설명
            steps: 작업 단계 목록

        Returns:
            유사한 작업 목록
        """
        similar_tasks = []
        history = self._task_history[:-1] if len(self._task_history) > 1 else []

        for task in history:
            # 단계 수 비교
            if len(task['steps']) != len(steps):
                continue

            # 단계 유사성 확인
            similarity = self._calculate_step_similarity(task['steps'], steps)
            if similarity >= 0.7:  # 70% 이상 유사하면 유사 작업으로 간주
                similar_tasks.append(task)

        return similar_tasks

    def _calculate_step_similarity(self, steps1: List[Dict[str, Any]], steps2: List[Dict[str, Any]]) -> float:
        """
        단계 유사성 계산

        Args:
            steps1: 첫 번째 단계 목록
            steps2: 두 번째 단계 목록

        Returns:
            유사성 점수 (0-1)
        """
        if len(steps1) != len(steps2):
            return 0.0

        match_count = 0
        for step1, step2 in zip(steps1, steps2):
            action1 = step1.get('action', '').lower()
            action2 = step2.get('action', '').lower()
            if action1 == action2:
                match_count += 1

        return match_count / len(steps1) if steps1 else 0.0

    def _is_pattern_match(self, pattern: Dict[str, Any], steps: List[Dict[str, Any]]) -> bool:
        """
        패턴 일치 확인

        Args:
            pattern: 패턴 데이터
            steps: 작업 단계 목록

        Returns:
            일치 여부
        """
        pattern_steps = pattern.get('steps', [])

        if len(pattern_steps) != len(steps):
            return False

        return self._calculate_step_similarity(pattern_steps, steps) >= 0.9

    def _create_pattern(self, data: Dict[str, Any], description: str, steps: List[Dict[str, Any]]) -> Optional[str]:
        """
        새 패턴 생성

        Args:
            data: 메모리 데이터
            description: 패턴 설명
            steps: 작업 단계 목록

        Returns:
            생성된 패턴 ID 또는 None
        """
        pattern_count = len(data['patterns']) + 1
        pattern_id = f"pattern-{pattern_count:03d}"

        # 태그 추출
        tags = self._extract_tags(description, steps)

        new_pattern = {
            'id': pattern_id,
            'name': self._generate_pattern_name(description),
            'description': description,
            'occurrence_count': 3,  # 최소 3회로 시작
            'confidence': 0.8,  # 초기 신뢰도
            'steps': [
                {
                    'order': i + 1,
                    'action': step.get('action', ''),
                    'description': step.get('description', ''),
                    'agent': step.get('agent', '')
                }
                for i, step in enumerate(steps)
            ],
            'created_at': self.update_timestamp(),
            'updated_at': self.update_timestamp(),
            'last_suggested_at': None,
            'suggestion_count': 0,
            'tags': tags
        }

        data['patterns'].append(new_pattern)
        self._update_metadata(data)

        if self._save(data):
            return pattern_id

        return None

    def _generate_pattern_name(self, description: str) -> str:
        """
        패턴 이름 생성

        Args:
            description: 작업 설명

        Returns:
            패턴 이름
        """
        # 설명에서 핵심 키워드 추출
        keywords = description.lower().split()
        important_words = [w for w in keywords if len(w) > 3][:3]

        if important_words:
            return ' '.join(w.capitalize() for w in important_words)

        return f"Pattern {len(self._task_history)}"

    def _extract_tags(self, description: str, steps: List[Dict[str, Any]]) -> List[str]:
        """
        패턴 태그 추출

        Args:
            description: 작업 설명
            steps: 작업 단계 목록

        Returns:
            태그 목록
        """
        tags = set()

        # 설명에서 키워드 추출
        keywords = ['mdr', 'ivdr', 'risk', 'technical', 'documentation', 'review', 'analysis', 'compliance']
        description_lower = description.lower()

        for keyword in keywords:
            if keyword in description_lower:
                tags.add(keyword)

        # 단계에서 에이전트 추출
        for step in steps:
            agent = step.get('agent', '').lower()
            if 'aria-' in agent:
                tags.add(agent.replace('aria-', '').replace('-', ' '))

        return list(tags)

    def suggest_patterns(self, task_description: str, steps: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        패턴 제안

        Args:
            task_description: 작업 설명
            steps: 현재 작업 단계 목록

        Returns:
            추천 패턴 목록
        """
        data = self._load()
        patterns = data.get('patterns', [])

        suggestions = []

        for pattern in patterns:
            # 신뢰도가 0.7 이상인 패턴만 제안
            if pattern.get('confidence', 0) < 0.7:
                continue

            # 유사성 계산
            similarity = self._calculate_pattern_similarity(pattern, task_description, steps)

            if similarity >= 0.6:  # 60% 이상 유사하면 제안
                suggestion = pattern.copy()
                suggestion['similarity_score'] = similarity
                suggestions.append(suggestion)

        # 유사성 점수로 정렬
        suggestions.sort(key=lambda x: x['similarity_score'], reverse=True)

        # 제안 횟수 업데이트
        for suggestion in suggestions[:3]:  # 상위 3개만 업데이트
            suggestion['suggestion_count'] += 1
            suggestion['last_suggested_at'] = self.update_timestamp()

        if suggestions:
            self._save(data)

        return suggestions

    def _calculate_pattern_similarity(self, pattern: Dict[str, Any], task_description: str, steps: List[Dict[str, Any]]) -> float:
        """
        패턴 유사성 계산

        Args:
            pattern: 패턴 데이터
            task_description: 작업 설명
            steps: 작업 단계 목록

        Returns:
            유사성 점수 (0-1)
        """
        score = 0.0

        # 태그 유사성
        pattern_tags = set(p.lower() for p in pattern.get('tags', []))
        desc_lower = task_description.lower()

        for tag in pattern_tags:
            if tag in desc_lower:
                score += 0.3

        # 단계 유사성
        pattern_steps = pattern.get('steps', [])
        if pattern_steps:
            step_similarity = self._calculate_step_similarity(pattern_steps, steps)
            score += step_similarity * 0.7

        return min(score, 1.0)

    def get_workflow_template(self, pattern_id: str) -> Optional[Dict[str, Any]]:
        """
        워크플로우 템플릿 조회

        Args:
            pattern_id: 패턴 ID

        Returns:
            워크플로우 템플릿 또는 None
        """
        data = self._load()
        patterns = data.get('patterns', [])

        for pattern in patterns:
            if pattern['id'] == pattern_id:
                return {
                    'pattern_id': pattern['id'],
                    'pattern_name': pattern['name'],
                    'steps': pattern['steps'],
                    'estimated_duration': self._estimate_duration(pattern),
                    'required_agents': self._extract_agents(pattern)
                }

        return None

    def _estimate_duration(self, pattern: Dict[str, Any]) -> str:
        """
        예상 소요 시간 추정

        Args:
            pattern: 패턴 데이터

        Returns:
            예상 소요 시간
        """
        step_count = len(pattern.get('steps', []))
        if step_count <= 2:
            return "< 5 minutes"
        elif step_count <= 4:
            return "5-15 minutes"
        elif step_count <= 6:
            return "15-30 minutes"
        else:
            return "> 30 minutes"

    def _extract_agents(self, pattern: Dict[str, Any]) -> List[str]:
        """
        필요한 에이전트 추출

        Args:
            pattern: 패턴 데이터

        Returns:
            에이전트 목록
        """
        agents = set()
        for step in pattern.get('steps', []):
            agent = step.get('agent', '')
            if agent:
                agents.add(agent)

        return list(agents)

    def _update_metadata(self, data: Dict[str, Any]) -> None:
        """
        메타데이터 업데이트

        Args:
            data: 메모리 데이터
        """
        patterns = data.get('patterns', [])

        all_tags = set()
        high_confidence = 0

        for pattern in patterns:
            all_tags.update(pattern.get('tags', []))
            if pattern.get('confidence', 0) >= 0.8:
                high_confidence += 1

        data['metadata'] = {
            'total_patterns': len(patterns),
            'high_confidence_patterns': high_confidence,
            'pattern_tags': list(all_tags)
        }
        data['last_updated'] = self.update_timestamp()
