"""
메모리 스토리지 기본 클래스

VCS 호환 JSON 파일 저장소를 제공합니다.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional
import threading


class MemoryStorage:
    """VCS 호환 메모리 스토리지 기본 클래스"""

    def __init__(self, memory_path: str):
        """
        메모리 스토리지 초기화

        Args:
            memory_path: 메모리 파일 경로
        """
        self.memory_path = Path(memory_path)
        self.memory_dir = self.memory_path.parent
        self._lock = threading.Lock()
        self._ensure_directory()

    def _ensure_directory(self) -> None:
        """메모리 디렉토리 생성"""
        self.memory_dir.mkdir(parents=True, exist_ok=True)

    def _load(self) -> Dict[str, Any]:
        """
        메모리 파일 로드

        Returns:
            로드된 데이터 또는 빈 딕셔너리
        """
        if not self.memory_path.exists():
            return {}

        try:
            with open(self.memory_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}

    def _save(self, data: Dict[str, Any]) -> bool:
        """
        메모리 파일 저장 (스레드 안전)

        Args:
            data: 저장할 데이터

        Returns:
            저장 성공 여부
        """
        with self._lock:
            try:
                # 임시 파일에 쓰기 (원자적 업데이트)
                temp_path = self.memory_path.with_suffix('.tmp')
                with open(temp_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)

                # 원자적 교체
                temp_path.replace(self.memory_path)
                return True
            except (IOError, OSError):
                # 임시 파일 정리
                if temp_path.exists():
                    temp_path.unlink()
                return False

    def validate_schema(self, data: Dict[str, Any], schema_path: Optional[str] = None) -> bool:
        """
        JSON 스키마 유효성 검사

        Args:
            data: 검증할 데이터
            schema_path: 스키마 파일 경로 (선택사항)

        Returns:
            유효성 검사 결과
        """
        if schema_path is None:
            schema_path = self.memory_path.parent / 'schemas' / f'{self.memory_path.stem}-schema.json'

        if not Path(schema_path).exists():
            # 스키마가 없으면 기본 구조 검증
            return isinstance(data, dict) and 'version' in data

        try:
            # jsonschema가 있으면 사용, 없으면 기본 검증
            try:
                from jsonschema import validate, ValidationError
                with open(schema_path, 'r', encoding='utf-8') as f:
                    schema = json.load(f)
                validate(instance=data, schema=schema)
                return True
            except ImportError:
                # jsonschema가 없으면 기본 구조 검증
                return isinstance(data, dict) and 'version' in data
        except Exception:
            return False

    def get_metadata(self) -> Dict[str, Any]:
        """
        메모리 메타데이터 조회

        Returns:
            메타데이터 딕셔너리
        """
        data = self._load()
        return data.get('metadata', {})

    def update_timestamp(self) -> str:
        """
        현재 타임스탬프 반환

        Returns:
            ISO 8601 형식 타임스탬프
        """
        return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
