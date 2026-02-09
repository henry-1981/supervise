"""
학습 메트릭 추적 시스템

Learning Metrics 구현
"""

from datetime import datetime
from typing import Any, Dict
from .memory_storage import MemoryStorage


class MetricsTracker(MemoryStorage):
    """
    학습 메트릭 추적기

    기능:
    - 채택 및 효과성 추적
    - 패턴 정확도 추적
    - 결정 관련성 추적
    -偏好 적용 추적
    """

    def __init__(self, project_dir: str):
        """
        메트릭 추적기 초기화

        Args:
            project_dir: 프로젝트 루트 디렉토리
        """
        memory_path = f"{project_dir}/.claude/agent-memory/aria/learning-metrics.json"
        super().__init__(memory_path)
        self.schema_path = f"{project_dir}/.claude/agent-memory/aria/schemas/learning-metrics-schema.json"
        self._initialize_metrics()

    def _initialize_metrics(self) -> None:
        """메트릭 초기화"""
        data = self._load()

        if not data or 'adoption' not in data:
            initial_data = {
                'version': '1.0.0',
                'last_updated': self.update_timestamp(),
                'adoption': {
                    'total_interactions': 0,
                    'unique_sessions': 0,
                    'feature_usage': {
                        'regulatory_decisions': {
                            'access_count': 0,
                            'contribution_count': 0,
                            'last_accessed': None
                        },
                        'company_preferences': {
                            'access_count': 0,
                            'contribution_count': 0,
                            'last_accessed': None
                        },
                        'task_patterns': {
                            'suggestions_shown': 0,
                            'suggestions_accepted': 0,
                            'last_suggested': None
                        }
                    }
                },
                'effectiveness': {
                    'pattern_accuracy': {
                        'correct': 0,
                        'incorrect': 0,
                        'ignored': 0
                    },
                    'decision_relevance': {
                        'relevant': 0,
                        'not_relevant': 0,
                        'neutral': 0
                    },
                    'preference_application': {
                        'applied': 0,
                        'overridden': 0,
                        'conflicts': 0
                    }
                },
                'learning': {
                    'new_patterns_learned': 0,
                    'preferences_extracted': 0,
                    'decisions_stored': 0,
                    'confidence_updates': 0
                },
                'quality': {
                    'memory_integrity': 100,
                    'schema_validations': {
                        'passed': 0,
                        'failed': 0
                    },
                    'merge_conflicts_resolved': 0
                },
                'metadata': {
                    'first_tracked': self.update_timestamp(),
                    'tracking_period_days': 0,
                    'data_retention_days': 365
                }
            }
            self._save(initial_data)

    def track_decision_access(self) -> None:
        """규제 결정 접근 추적"""
        data = self._load()
        data['adoption']['feature_usage']['regulatory_decisions']['access_count'] += 1
        data['adoption']['feature_usage']['regulatory_decisions']['last_accessed'] = self.update_timestamp()
        data['adoption']['total_interactions'] += 1
        data['last_updated'] = self.update_timestamp()
        self._save(data)

    def track_decision_storage(self) -> None:
        """규제 결정 저장 추적"""
        data = self._load()
        data['adoption']['feature_usage']['regulatory_decisions']['contribution_count'] += 1
        data['learning']['decisions_stored'] += 1
        data['last_updated'] = self.update_timestamp()
        self._save(data)

    def track_preference_access(self) -> None:
        """偏好 접근 추적"""
        data = self._load()
        data['adoption']['feature_usage']['company_preferences']['access_count'] += 1
        data['adoption']['feature_usage']['company_preferences']['last_accessed'] = self.update_timestamp()
        data['adoption']['total_interactions'] += 1
        data['last_updated'] = self.update_timestamp()
        self._save(data)

    def track_preference_extraction(self) -> None:
        """偏好 추출 추적"""
        data = self._load()
        data['adoption']['feature_usage']['company_preferences']['contribution_count'] += 1
        data['learning']['preferences_extracted'] += 1
        data['last_updated'] = self.update_timestamp()
        self._save(data)

    def track_pattern_suggestion(self, accepted: bool = False) -> None:
        """
        패턴 제안 추적

        Args:
            accepted: 제안이 수락되었는지 여부
        """
        data = self._load()
        data['adoption']['feature_usage']['task_patterns']['suggestions_shown'] += 1
        data['adoption']['feature_usage']['task_patterns']['last_suggested'] = self.update_timestamp()

        if accepted:
            data['adoption']['feature_usage']['task_patterns']['suggestions_accepted'] += 1
            data['effectiveness']['pattern_accuracy']['correct'] += 1
        else:
            data['effectiveness']['pattern_accuracy']['incorrect'] += 1

        data['last_updated'] = self.update_timestamp()
        self._save(data)

    def track_pattern_learned(self) -> None:
        """새 패턴 학습 추적"""
        data = self._load()
        data['learning']['new_patterns_learned'] += 1
        data['last_updated'] = self.update_timestamp()
        self._save(data)

    def track_decision_feedback(self, relevant: str) -> None:
        """
        결정 관련성 피드백 추적

        Args:
            relevant: 관련성 ('relevant', 'not_relevant', 'neutral')
        """
        data = self._load()

        if relevant in data['effectiveness']['decision_relevance']:
            data['effectiveness']['decision_relevance'][relevant] += 1

        data['last_updated'] = self.update_timestamp()
        self._save(data)

    def track_preference_application(self, applied: bool = True, conflict: bool = False) -> None:
        """
       偏好 적용 추적

        Args:
            applied: 적용되었는지 여부
            conflict: 충돌이 발생했는지 여부
        """
        data = self._load()

        if applied:
            data['effectiveness']['preference_application']['applied'] += 1
        else:
            data['effectiveness']['preference_application']['overridden'] += 1

        if conflict:
            data['effectiveness']['preference_application']['conflicts'] += 1

        data['last_updated'] = self.update_timestamp()
        self._save(data)

    def track_schema_validation(self, passed: bool) -> None:
        """
        스키마 검증 추적

        Args:
            passed: 검증 통과 여부
        """
        data = self._load()

        if passed:
            data['quality']['schema_validations']['passed'] += 1
        else:
            data['quality']['schema_validations']['failed'] += 1
            # 실패 시 메모리 무결성 감소
            data['quality']['memory_integrity'] = max(
                data['quality']['memory_integrity'] - 5,
                0
            )

        data['last_updated'] = self.update_timestamp()
        self._save(data)

    def get_adoption_summary(self) -> Dict[str, Any]:
        """
        채택 요약 조회

        Returns:
            채택 요약 딕셔너리
        """
        data = self._load()
        adoption = data.get('adoption', {})

        return {
            'total_interactions': adoption.get('total_interactions', 0),
            'unique_sessions': adoption.get('unique_sessions', 0),
            'feature_usage': adoption.get('feature_usage', {})
        }

    def get_effectiveness_summary(self) -> Dict[str, Any]:
        """
        효과성 요약 조회

        Returns:
            효과성 요약 딕셔너리
        """
        data = self._load()
        effectiveness = data.get('effectiveness', {})

        # 패턴 정확도 계산
        pattern_acc = effectiveness.get('pattern_accuracy', {})
        total_pattern_attempts = (
            pattern_acc.get('correct', 0) +
            pattern_acc.get('incorrect', 0) +
            pattern_acc.get('ignored', 0)
        )
        pattern_accuracy = (
            pattern_acc.get('correct', 0) / total_pattern_attempts
            if total_pattern_attempts > 0
            else 0.0
        )

        # 결정 관련성 계산
        decision_rel = effectiveness.get('decision_relevance', {})
        total_decision_feedback = (
            decision_rel.get('relevant', 0) +
            decision_rel.get('not_relevant', 0) +
            decision_rel.get('neutral', 0)
        )
        decision_relevance_rate = (
            decision_rel.get('relevant', 0) / total_decision_feedback
            if total_decision_feedback > 0
            else 0.0
        )

        return {
            'pattern_accuracy': pattern_accuracy,
            'decision_relevance_rate': decision_relevance_rate,
            'preference_application_rate': self._calculate_preference_application_rate(effectiveness),
            'raw_data': effectiveness
        }

    def _calculate_preference_application_rate(self, effectiveness: Dict[str, Any]) -> float:
        """
       偏好 적용률 계산

        Args:
            effectiveness: 효과성 데이터

        Returns:
            적용률 (0-1)
        """
        pref_app = effectiveness.get('preference_application', {})
        total = (
            pref_app.get('applied', 0) +
            pref_app.get('overridden', 0)
        )

        return (
            pref_app.get('applied', 0) / total
            if total > 0
            else 0.0
        )

    def get_learning_progress(self) -> Dict[str, Any]:
        """
        학습 진행 조회

        Returns:
            학습 진행 딕셔너리
        """
        data = self._load()
        learning = data.get('learning', {})

        return {
            'new_patterns_learned': learning.get('new_patterns_learned', 0),
            'preferences_extracted': learning.get('preferences_extracted', 0),
            'decisions_stored': learning.get('decisions_stored', 0),
            'confidence_updates': learning.get('confidence_updates', 0),
            'total_learning_activities': sum([
                learning.get('new_patterns_learned', 0),
                learning.get('preferences_extracted', 0),
                learning.get('decisions_stored', 0),
                learning.get('confidence_updates', 0)
            ])
        }

    def get_quality_report(self) -> Dict[str, Any]:
        """
        품질 보고서 조회

        Returns:
            품질 보고서 딕셔너리
        """
        data = self._load()
        quality = data.get('quality', {})

        schema_validations = quality.get('schema_validations', {})
        total_validations = (
            schema_validations.get('passed', 0) +
            schema_validations.get('failed', 0)
        )
        validation_success_rate = (
            schema_validations.get('passed', 0) / total_validations
            if total_validations > 0
            else 1.0
        )

        return {
            'memory_integrity': quality.get('memory_integrity', 100),
            'validation_success_rate': validation_success_rate,
            'merge_conflicts_resolved': quality.get('merge_conflicts_resolved', 0),
            'schema_validations': schema_validations
        }

    def start_new_session(self) -> None:
        """새 세션 시작 추적"""
        data = self._load()
        data['adoption']['unique_sessions'] += 1
        data['last_updated'] = self.update_timestamp()
        self._save(data)
