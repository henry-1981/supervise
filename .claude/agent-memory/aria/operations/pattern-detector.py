#!/usr/bin/env python3
"""
ARIA Pattern Detector

Implements repetitive task pattern recognition for SPEC-ARIA-005 UR-015 to UR-021.

Features:
- Identify repetitive task sequences in RA/QA workflows
- Maintain library of common task patterns
- Suggest automation for patterns repeated 3+ times
- Merge overlapping patterns into generalized templates

Usage:
    python pattern-detector.py analyze --session-log "..."
    python pattern-detector.py suggest --task-sequence [...]
    python pattern-detector.py merge --pattern-ids "PAT-001,PAT-002"
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
import argparse
from collections import defaultdict


class PatternDetector:
    """Detects and manages repetitive task patterns."""

    def __init__(self, memory_dir: Optional[Path] = None):
        """Initialize pattern detector with memory directory."""
        if memory_dir is None:
            script_dir = Path(__file__).parent.parent
            memory_dir = script_dir

        self.memory_dir = Path(memory_dir)
        self.patterns_file = self.memory_dir / 'task-patterns-enhanced.json'
        self.metrics_file = self.memory_dir / 'learning-metrics-enhanced.json'

        self.patterns = self._load_json(self.patterns_file)
        self.metrics = self._load_json(self.metrics_file)

    def _load_json(self, file_path: Path) -> Dict[str, Any]:
        """Load JSON file."""
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError as e:
                print(f"Error loading {file_path}: {e}", file=sys.stderr)
                return {}
        return {}

    def _save_json(self, file_path: Path, data: Dict[str, Any]) -> bool:
        """Save JSON file with atomic write."""
        temp_file = file_path.with_suffix('.tmp')
        try:
            with open(temp_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            temp_file.replace(file_path)
            return True
        except Exception as e:
            print(f"Error saving {file_path}: {e}", file=sys.stderr)
            return False

    def analyze_session_log(self, session_log: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Analyze session log for repetitive patterns.

        UR-015: Identify and remember repetitive task patterns
        """
        # Extract task sequences from session log
        task_sequences = self._extract_sequences(session_log)

        # Analyze each sequence for patterns
        detected_patterns = []

        for sequence in task_sequences:
            pattern = self._detect_pattern_in_sequence(sequence)
            if pattern:
                detected_patterns.append(pattern)

        return detected_patterns

    def _extract_sequences(self, session_log: List[Dict[str, Any]]) -> List[List[Dict[str, Any]]]:
        """Extract task sequences from session log."""
        sequences = []
        current_sequence = []
        last_timestamp = None

        for entry in session_log:
            if entry.get('type') == 'task_execution':
                task = {
                    'action': entry.get('action', ''),
                    'agent': entry.get('agent', ''),
                    'timestamp': entry.get('timestamp')
                }

                # Check if this is part of a continuous sequence
                if last_timestamp:
                    time_diff = self._calculate_time_diff(last_timestamp, task['timestamp'])
                    if time_diff and time_diff > 3600:  # 1 hour gap
                        if current_sequence:
                            sequences.append(current_sequence)
                        current_sequence = []

                current_sequence.append(task)
                last_timestamp = task['timestamp']

        if current_sequence:
            sequences.append(current_sequence)

        return sequences

    def _calculate_time_diff(self, time1: str, time2: str) -> Optional[int]:
        """Calculate time difference in seconds."""
        try:
            t1 = datetime.fromisoformat(time1.replace('Z', '+00:00'))
            t2 = datetime.fromisoformat(time2.replace('Z', '+00:00'))
            return int((t2 - t1).total_seconds())
        except:
            return None

    def _detect_pattern_in_sequence(self, sequence: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Detect if sequence matches known patterns."""
        if len(sequence) < 2:
            return None

        sequence_signature = self._generate_sequence_signature(sequence)

        # Check against existing patterns
        for pattern in self.patterns.get('patterns', []):
            pattern_signature = self._generate_pattern_signature(pattern)
            if sequence_signature == pattern_signature:
                # Increment occurrence count
                pattern['occurrence_count'] += 1
                pattern['last_suggested_at'] = datetime.now().isoformat() + 'Z'

                # Recalculate confidence
                pattern['confidence'] = min(0.5 + (pattern['occurrence_count'] * 0.1), 1.0)

                self._save_json(self.patterns_file, self.patterns)

                return {
                    'type': 'existing_pattern',
                    'pattern': pattern,
                    'match_quality': 'exact'
                }

        # Check against pattern library
        for library_pattern in self.patterns.get('pattern_library', {}).get('common_sequences', []):
            library_signature = self._generate_library_signature(library_pattern)
            if sequence_signature == library_signature:
                # Suggest promoting to active patterns
                return {
                    'type': 'library_match',
                    'pattern': library_pattern,
                    'suggestion': 'Promote to active patterns',
                    'match_quality': 'exact'
                }

        # Check for partial matches (similar but not identical)
        for pattern in self.patterns.get('patterns', []):
            if self._sequences_similar(sequence, pattern.get('steps', [])):
                return {
                    'type': 'similar_pattern',
                    'pattern': pattern,
                    'suggestion': 'Pattern variation detected',
                    'match_quality': 'similar'
                }

        return None

    def _generate_sequence_signature(self, sequence: List[Dict[str, Any]]) -> str:
        """Generate signature for task sequence."""
        actions = [task.get('action', '') for task in sequence]
        return ' -> '.join(actions)

    def _generate_pattern_signature(self, pattern: Dict[str, Any]) -> str:
        """Generate signature for pattern."""
        steps = pattern.get('steps', [])
        actions = [step.get('action', '') for step in steps]
        return ' -> '.join(actions)

    def _generate_library_signature(self, library_pattern: Dict[str, Any]) -> str:
        """Generate signature for library pattern."""
        steps = library_pattern.get('steps', [])
        actions = [step.get('action', '') for step in steps]
        return ' -> '.join(actions)

    def _sequences_similar(self, seq1: List[Dict[str, Any]],
                          seq2: List[Dict[str, Any]], threshold: float = 0.7) -> bool:
        """Check if two sequences are similar."""
        if len(seq1) != len(seq2):
            return False

        matches = sum(
            1 for s1, s2 in zip(seq1, seq2)
            if s1.get('action', '') == s2.get('action', '')
        )

        similarity = matches / len(seq1)
        return similarity >= threshold

    def suggest_automation(self, task_sequence: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """
        Suggest automation for task sequence.

        UR-018: Suggest automation for patterns repeated 3+ times
        UR-019: Offer to execute learned patterns when recognized
        """
        pattern = self._detect_pattern_in_sequence(task_sequence)

        if not pattern:
            return None

        if pattern['type'] == 'existing_pattern':
            pattern_data = pattern['pattern']

            if pattern_data['occurrence_count'] >= 3:
                suggestion = {
                    'pattern_id': pattern_data['id'],
                    'pattern_name': pattern_data['name'],
                    'occurrence_count': pattern_data['occurrence_count'],
                    'confidence': pattern_data['confidence'],
                    'automatable': pattern_data.get('automatable', False),
                    'estimated_duration_hours': pattern_data.get('estimated_duration_hours', 0),
                    'suggestion': 'Create reusable workflow template',
                    'steps': pattern_data.get('steps', []),
                    'created_at': datetime.now().isoformat() + 'Z'
                }

                # Update suggestion metrics
                self.metrics['adoption']['feature_usage']['task_patterns']['suggestions_shown'] += 1
                self._save_json(self.metrics_file, self.metrics)

                return suggestion

        elif pattern['type'] == 'library_match':
            library_pattern = pattern['pattern']

            return {
                'pattern_id': library_pattern['id'],
                'pattern_name': library_pattern['name'],
                'description': library_pattern.get('description', ''),
                'suggestion': 'Add to active patterns',
                'automatable': library_pattern.get('automatable', False),
                'estimated_duration_hours': library_pattern.get('estimated_duration_hours', 0),
                'steps': library_pattern.get('steps', []),
                'created_at': datetime.now().isoformat() + 'Z'
            }

        return None

    def merge_patterns(self, pattern_ids: List[str]) -> Optional[Dict[str, Any]]:
        """
        Merge overlapping patterns into generalized template.

        UR-021: Merge overlapping patterns into generalized templates
        """
        if len(pattern_ids) < 2:
            print("Need at least 2 patterns to merge", file=sys.stderr)
            return None

        # Load patterns
        patterns_to_merge = []
        for pattern_id in pattern_ids:
            for pattern in self.patterns.get('patterns', []):
                if pattern['id'] == pattern_id:
                    patterns_to_merge.append(pattern)
                    break

        if len(patterns_to_merge) != len(pattern_ids):
            print(f"Could not find all patterns: {pattern_ids}", file=sys.stderr)
            return None

        # Check if patterns can be merged (similar structure)
        if not self._can_merge_patterns(patterns_to_merge):
            print("Patterns are too different to merge", file=sys.stderr)
            return None

        # Create merged pattern
        merged_pattern = self._create_merged_pattern(patterns_to_merge)

        # Add merged pattern to library
        self.patterns['patterns'].append(merged_pattern)

        # Mark original patterns as merged
        for pattern in self.patterns['patterns']:
            if pattern['id'] in pattern_ids:
                pattern['merged_into'] = merged_pattern['id']
                pattern['is_valid'] = False

        self.patterns['last_updated'] = datetime.now().isoformat() + 'Z'
        self._save_json(self.patterns_file, self.patterns)

        # Update metrics
        self.metrics['learning']['new_patterns_learned'] += 1
        self._save_json(self.metrics_file, self.metrics)

        return merged_pattern

    def _can_merge_patterns(self, patterns: List[Dict[str, Any]]) -> bool:
        """Check if patterns can be merged."""
        if len(patterns) < 2:
            return False

        # All patterns must have same number of steps
        step_counts = [len(p.get('steps', [])) for p in patterns]
        if len(set(step_counts)) > 1:
            return False

        # Steps must be similar
        reference_steps = patterns[0].get('steps', [])

        for pattern in patterns[1:]:
            steps = pattern.get('steps', [])
            if not self._sequences_similar(reference_steps, steps, threshold=0.6):
                return False

        return True

    def _create_merged_pattern(self, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Create merged pattern from multiple patterns."""
        # Use first pattern as base
        base_pattern = patterns[0].copy()

        # Generate new ID
        year = datetime.now().year
        existing_ids = [p['id'] for p in self.patterns.get('patterns', [])]
        max_num = 0
        for pid in existing_ids:
            if pid.startswith(f'PAT-{year}-'):
                num = int(pid.split('-')[-1])
                max_num = max(max_num, num)

        merged_id = f'PAT-{year}-{max_num + 1:03d}'

        # Merge names
        names = [p.get('name', '') for p in patterns]
        merged_name = f"Merged: {', '.join(names[:2])}"
        if len(names) > 2:
            merged_name += f" (+{len(names) - 2} more)"

        # Merge descriptions
        descriptions = [p.get('description', '') for p in patterns if p.get('description')]
        merged_description = ' | '.join(descriptions)

        # Sum occurrence counts
        total_occurrences = sum(p.get('occurrence_count', 0) for p in patterns)

        # Average confidence
        avg_confidence = sum(p.get('confidence', 0) for p in patterns) / len(patterns)

        # Merge tags
        all_tags = set()
        for pattern in patterns:
            all_tags.update(pattern.get('tags', []))

        merged_pattern = {
            'id': merged_id,
            'name': merged_name,
            'description': merged_description,
            'occurrence_count': total_occurrences,
            'confidence': min(avg_confidence + 0.1, 1.0),  # Boost confidence for merged pattern
            'steps': base_pattern.get('steps', []),
            'estimated_duration_hours': base_pattern.get('estimated_duration_hours', 0),
            'automatable': base_pattern.get('automatable', False),
            'created_at': datetime.now().isoformat() + 'Z',
            'updated_at': datetime.now().isoformat() + 'Z',
            'last_suggested_at': None,
            'suggestion_count': 0,
            'tags': list(all_tags),
            'merged_from': [p['id'] for p in patterns],
            'is_valid': True
        }

        return merged_pattern

    def get_pattern_statistics(self) -> Dict[str, Any]:
        """Get statistics about detected patterns."""
        patterns = self.patterns.get('patterns', [])

        stats = {
            'total_patterns': len(patterns),
            'high_confidence_patterns': len([p for p in patterns if p.get('confidence', 0) >= 0.7]),
            'automatable_patterns': len([p for p in patterns if p.get('automatable', False)]),
            'total_occurrences': sum(p.get('occurrence_count', 0) for p in patterns),
            'average_confidence': sum(p.get('confidence', 0) for p in patterns) / len(patterns) if patterns else 0,
            'patterns_by_domain': defaultdict(int),
            'most_common_patterns': []
        }

        # Count by domain/tags
        for pattern in patterns:
            for tag in pattern.get('tags', []):
                stats['patterns_by_domain'][tag] += 1

        # Sort by occurrence count
        sorted_patterns = sorted(patterns, key=lambda p: p.get('occurrence_count', 0), reverse=True)
        stats['most_common_patterns'] = [
            {
                'id': p['id'],
                'name': p['name'],
                'occurrence_count': p.get('occurrence_count', 0),
                'confidence': p.get('confidence', 0)
            }
            for p in sorted_patterns[:5]
        ]

        return stats


def main():
    """Command-line interface for pattern detection."""
    parser = argparse.ArgumentParser(description='ARIA Pattern Detector')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze session log for patterns')
    analyze_parser.add_argument('--session-log', required=True, help='Path to session log file')

    # Suggest command
    suggest_parser = subparsers.add_parser('suggest', help='Suggest automation for task sequence')
    suggest_parser.add_argument('--task-sequence', required=True, help='JSON array of task sequence')

    # Merge command
    merge_parser = subparsers.add_parser('merge', help='Merge overlapping patterns')
    merge_parser.add_argument('--pattern-ids', required=True, help='Comma-separated pattern IDs')

    # Statistics command
    subparsers.add_parser('stats', help='Get pattern statistics')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    detector = PatternDetector()

    if args.command == 'analyze':
        try:
            with open(args.session_log, 'r') as f:
                session_log = json.load(f)
        except Exception as e:
            print(f"Error loading session log: {e}", file=sys.stderr)
            return 1

        patterns = detector.analyze_session_log(session_log)
        print(f"\nDetected {len(patterns)} patterns:")
        for pattern in patterns:
            print(f"\n- {pattern['type']}: {pattern.get('pattern', {}).get('name', 'Unknown')}")
            print(f"  Match Quality: {pattern['match_quality']}")

    elif args.command == 'suggest':
        try:
            task_sequence = json.loads(args.task_sequence)
        except Exception as e:
            print(f"Error parsing task sequence: {e}", file=sys.stderr)
            return 1

        suggestion = detector.suggest_automation(task_sequence)
        if suggestion:
            print("\nAutomation Suggestion:")
            print(f"Pattern: {suggestion.get('pattern_name')}")
            print(f"Occurrences: {suggestion.get('occurrence_count', 'N/A')}")
            print(f"Confidence: {suggestion.get('confidence', 0):.2f}")
            print(f"Automatable: {suggestion.get('automatable', False)}")
            print(f"Suggestion: {suggestion.get('suggestion')}")
        else:
            print("No automation suggestion available")

    elif args.command == 'merge':
        pattern_ids = args.pattern_ids.split(',')
        pattern_ids = [pid.strip() for pid in pattern_ids]

        merged = detector.merge_patterns(pattern_ids)
        if merged:
            print(f"\nMerged pattern created: {merged['id']}")
            print(f"Name: {merged['name']}")
            print(f"Occurrences: {merged['occurrence_count']}")
            print(f"Confidence: {merged['confidence']:.2f}")
        else:
            print("Failed to merge patterns", file=sys.stderr)
            return 1

    elif args.command == 'stats':
        stats = detector.get_pattern_statistics()
        print("\nPattern Statistics:")
        print(f"Total Patterns: {stats['total_patterns']}")
        print(f"High Confidence: {stats['high_confidence_patterns']}")
        print(f"Automatable: {stats['automatable_patterns']}")
        print(f"Total Occurrences: {stats['total_occurrences']}")
        print(f"Average Confidence: {stats['average_confidence']:.2f}")

        if stats['most_common_patterns']:
            print("\nMost Common Patterns:")
            for pattern in stats['most_common_patterns']:
                print(f"  - {pattern['name']}: {pattern['occurrence_count']} occurrences")

    return 0


if __name__ == '__main__':
    sys.exit(main())
