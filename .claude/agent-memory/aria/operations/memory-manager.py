#!/usr/bin/env python3
"""
ARIA Memory Manager

Implements SPEC-ARIA-005 Agent Memory System operations for:
- Regulatory Decision Memory (UR-001 to UR-007)
- Company Preference Learning (UR-008 to UR-014)
- Repetitive Task Pattern Recognition (UR-015 to UR-021)

Usage:
    python memory-manager.py store-decision --question "..." --answer "..." --regulation "..."
    python memory-manager.py retrieve-decisions --query "..." --threshold 0.7
    python memory-manager.py learn-preference --category "formatting" --key "date_format" --value "DD/MM/YYYY"
    python memory-manager.py detect-patterns --task-sequence [...]
    python memory-manager.py validate --all
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
import argparse
import hashlib


class ARIAMemoryManager:
    """Manages ARIA agent memory operations."""

    def __init__(self, memory_dir: Optional[Path] = None):
        """Initialize memory manager with directory path."""
        if memory_dir is None:
            # Default to ARIA memory directory
            script_dir = Path(__file__).parent.parent
            memory_dir = script_dir

        self.memory_dir = Path(memory_dir)
        self.decisions_file = self.memory_dir / "regulatory-decisions-enhanced.json"
        self.preferences_file = self.memory_dir / "company-preferences-enhanced.json"
        self.patterns_file = self.memory_dir / "task-patterns-enhanced.json"
        self.metrics_file = self.memory_dir / "learning-metrics-enhanced.json"

        # Load memory data
        self.decisions = self._load_json(self.decisions_file)
        self.preferences = self._load_json(self.preferences_file)
        self.patterns = self._load_json(self.patterns_file)
        self.metrics = self._load_json(self.metrics_file)

    def _load_json(self, file_path: Path) -> Dict[str, Any]:
        """Load JSON file with error handling."""
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

    def generate_decision_id(self) -> str:
        """Generate unique decision ID."""
        year = datetime.now().year
        existing_ids = [
            d['decision_id'] for d in self.decisions.get('decisions', [])
        ]
        max_num = 0
        for decision_id in existing_ids:
            if decision_id.startswith(f'DEC-{year}-'):
                num = int(decision_id.split('-')[-1])
                max_num = max(max_num, num)
        return f'DEC-{year}-{max_num + 1:03d}'

    def store_decision(self, decision_data: Dict[str, Any]) -> str:
        """
        Store a regulatory decision in memory.

        UR-001: Persistent memory across sessions
        UR-004: Prompt to store decision during drafting
        """
        decision_id = self.generate_decision_id()

        decision = {
            'decision_id': decision_id,
            'question': decision_data.get('question', ''),
            'answer': decision_data.get('answer', ''),
            'regulation': decision_data.get('regulation', ''),
            'section': decision_data.get('section', ''),
            'rationale': decision_data.get('rationale', ''),
            'applicability': decision_data.get('applicability', []),
            'regulatory_domain': decision_data.get('regulatory_domain', 'FDA'),
            'company_specific': decision_data.get('company_specific', False),
            'confidence_score': decision_data.get('confidence_score', 0.8),
            'valid_until': decision_data.get('valid_until', None),
            'created_at': datetime.now().isoformat() + 'Z',
            'last_reviewed': datetime.now().isoformat() + 'Z',
            'created_by': decision_data.get('created_by', 'system'),
            'usage_count': 0,
            'last_used_at': None,
            'tags': decision_data.get('tags', []),
            'related_decisions': [],
            'evidence_citations': decision_data.get('evidence_citations', []),
            'is_valid': True
        }

        self.decisions['decisions'].append(decision)
        self.decisions['last_updated'] = datetime.now().isoformat() + 'Z'
        self.decisions['metadata']['total_decisions'] = len(self.decisions['decisions'])
        self.decisions['metadata']['active_decisions'] = len([
            d for d in self.decisions['decisions'] if d['is_valid']
        ])

        if self._save_json(self.decisions_file, self.decisions):
            # Update metrics
            self.metrics['learning']['decisions_stored'] += 1
            self._save_json(self.metrics_file, self.metrics)

            # Update index
            self._update_decision_index(decision)

            print(f"Decision stored: {decision_id}")
            return decision_id
        else:
            print("Failed to store decision", file=sys.stderr)
            return ""

    def _update_decision_index(self, decision: Dict[str, Any]):
        """Update decision search indexes."""
        decision_id = decision['decision_id']

        # Index by regulation
        regulation = decision.get('regulation', '')
        if regulation and 'index' in self.decisions:
            if 'by_regulation' not in self.decisions['index']:
                self.decisions['index']['by_regulation'] = {}
            if regulation not in self.decisions['index']['by_regulation']:
                self.decisions['index']['by_regulation'][regulation] = []
            self.decisions['index']['by_regulation'][regulation].append(decision_id)

        # Index by domain
        domain = decision.get('regulatory_domain', '')
        if domain and 'index' in self.decisions:
            if 'by_domain' not in self.decisions['index']:
                self.decisions['index']['by_domain'] = {}
            if domain not in self.decisions['index']['by_domain']:
                self.decisions['index']['by_domain'][domain] = []
            self.decisions['index']['by_domain'][domain].append(decision_id)

        self._save_json(self.decisions_file, self.decisions)

    def retrieve_decisions(self, query: str, threshold: float = 0.7,
                          domain: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Retrieve relevant decisions based on query.

        UR-005: Retrieve relevant past decisions when similar questions arise
        """
        results = []

        for decision in self.decisions.get('decisions', []):
            if not decision.get('is_valid', True):
                continue

            if domain and decision.get('regulatory_domain') != domain:
                continue

            # Simple keyword matching (can be enhanced with vector search)
            score = self._calculate_relevance(query, decision)

            if score >= threshold:
                # Update usage stats
                decision['usage_count'] = decision.get('usage_count', 0) + 1
                decision['last_used_at'] = datetime.now().isoformat() + 'Z'

                results.append({
                    'decision': decision,
                    'relevance_score': score
                })

        # Sort by relevance
        results.sort(key=lambda x: x['relevance_score'], reverse=True)

        # Save updated usage stats
        if results:
            self._save_json(self.decisions_file, self.decisions)

            # Update metrics
            self.metrics['effectiveness']['decision_relevance']['relevant'] += len(results)
            self._save_json(self.metrics_file, self.metrics)

        return results

    def _calculate_relevance(self, query: str, decision: Dict[str, Any]) -> float:
        """Calculate relevance score between query and decision."""
        query_lower = query.lower()
        score = 0.0

        # Question matching (highest weight)
        question = decision.get('question', '').lower()
        if query_lower in question or question in query_lower:
            score += 0.5

        # Applicability tags matching
        for tag in decision.get('applicability', []):
            if tag.lower() in query_lower:
                score += 0.2

        # Regulation matching
        regulation = decision.get('regulation', '').lower()
        if regulation and regulation in query_lower:
            score += 0.2

        # Tags matching
        for tag in decision.get('tags', []):
            if tag.lower() in query_lower:
                score += 0.1

        return min(score, 1.0)

    def flag_obsolete_decisions(self, regulation: str, change_date: str) -> List[str]:
        """
        Flag decisions as obsolete when regulations change.

        UR-006: Flag obsolete decisions when regulations change
        """
        flagged = []

        for decision in self.decisions.get('decisions', []):
            if decision.get('regulation', '') == regulation:
                if decision.get('is_valid', True):
                    decision['is_valid'] = False
                    decision['valid_until'] = change_date
                    flagged.append(decision['decision_id'])

        if flagged:
            self.decisions['last_updated'] = datetime.now().isoformat() + 'Z'
            self._save_json(self.decisions_file, self.decisions)

            # Update metrics
            self.metrics['learning']['regulation_changes_processed'] += 1
            self.metrics['regulatory_coverage']['regulation_change_monitoring']['decisions_flagged'] += len(flagged)
            self._save_json(self.metrics_file, self.metrics)

        return flagged

    def learn_preference(self, company_id: str, category: str,
                        key: str, value: Any, source: str = 'user_modification') -> bool:
        """
        Learn and store company preference.

        UR-008: Learn and remember company-specific preferences
        UR-012: Learn from user modifications to accepted suggestions
        """
        if 'companies' not in self.preferences:
            self.preferences['companies'] = {}

        if company_id not in self.preferences['companies']:
            self.preferences['companies'][company_id] = {
                'company_id': company_id,
                'company_name': company_id,
                'preferences': {},
                'suggestion_history': {
                    'accepted': [],
                    'rejected': [],
                    'modified': []
                },
                'created_at': datetime.now().isoformat() + 'Z',
                'updated_at': datetime.now().isoformat() + 'Z',
                'preference_conflicts': [],
                'user_overrides': {}
            }

        company = self.preferences['companies'][company_id]

        # Store preference
        if category not in company['preferences']:
            company['preferences'][category] = {}

        company['preferences'][category][key] = value
        company['updated_at'] = datetime.now().isoformat() + 'Z'

        # Record in suggestion history if from user modification
        if source == 'user_modification':
            company['suggestion_history']['modified'].append({
                'timestamp': datetime.now().isoformat() + 'Z',
                'category': category,
                'key': key,
                'value': value
            })

        self.preferences['last_updated'] = datetime.now().isoformat() + 'Z'
        self.preferences['metadata']['active_companies'] = len(self.preferences['companies'])

        if self._save_json(self.preferences_file, self.preferences):
            # Update metrics
            self.metrics['learning']['preferences_extracted'] += 1
            self._save_json(self.metrics_file, self.metrics)

            print(f"Preference learned: {category}.{key} = {value}")
            return True
        else:
            print("Failed to learn preference", file=sys.stderr)
            return False

    def record_suggestion_feedback(self, company_id: str, suggestion_type: str,
                                   feedback: str, reason: Optional[str] = None) -> bool:
        """
        Record user feedback on suggestions.

        UR-011: Record rejection reasons to avoid similar suggestions
        """
        if company_id not in self.preferences.get('companies', {}):
            print(f"Company {company_id} not found", file=sys.stderr)
            return False

        company = self.preferences['companies'][company_id]

        feedback_entry = {
            'timestamp': datetime.now().isoformat() + 'Z',
            'suggestion_type': suggestion_type,
            'feedback': feedback
        }

        if reason:
            feedback_entry['reason'] = reason

        if feedback == 'accepted':
            company['suggestion_history']['accepted'].append(feedback_entry)
        elif feedback == 'rejected':
            company['suggestion_history']['rejected'].append(feedback_entry)
        elif feedback == 'modified':
            company['suggestion_history']['modified'].append(feedback_entry)

        company['updated_at'] = datetime.now().isoformat() + 'Z'
        self.preferences['last_updated'] = datetime.now().isoformat() + 'Z'

        # Update metrics
        if feedback == 'accepted':
            self.metrics['user_feedback']['accepted_suggestions'] += 1
        elif feedback == 'rejected':
            self.metrics['user_feedback']['rejected_suggestions'] += 1
        elif feedback == 'modified':
            self.metrics['user_feedback']['modified_suggestions'] += 1

        self._save_json(self.preferences_file, self.preferences)
        self._save_json(self.metrics_file, self.metrics)

        print(f"Feedback recorded: {feedback}")
        return True

    def detect_pattern(self, task_sequence: List[Dict[str, Any]],
                      min_occurrences: int = 3) -> Optional[Dict[str, Any]]:
        """
        Detect if a task sequence matches known patterns.

        UR-015: Identify and remember repetitive task patterns
        UR-018: Suggest automation for patterns repeated 3+ times
        """
        # Generate pattern signature
        signature = self._generate_pattern_signature(task_sequence)

        # Check against existing patterns
        for pattern in self.patterns.get('patterns', []):
            if self._pattern_signatures_match(signature, pattern):
                pattern['occurrence_count'] += 1
                pattern['last_suggested_at'] = datetime.now().isoformat() + 'Z'

                if pattern['occurrence_count'] >= min_occurrences:
                    self.patterns['last_updated'] = datetime.now().isoformat() + 'Z'
                    self._save_json(self.patterns_file, self.patterns)

                    # Update metrics
                    self.metrics['effectiveness']['automation_savings']['patterns_recognized'] += 1
                    self._save_json(self.metrics_file, self.metrics)

                    return pattern

        # Check against pattern library
        for library_pattern in self.patterns.get('pattern_library', {}).get('common_sequences', []):
            if self._pattern_signatures_match(signature, library_pattern):
                # Promote to active patterns
                new_pattern = {
                    'id': library_pattern['id'],
                    'name': library_pattern['name'],
                    'description': library_pattern['description'],
                    'occurrence_count': 1,
                    'confidence': 0.7,
                    'steps': library_pattern['steps'],
                    'estimated_duration_hours': library_pattern.get('estimated_duration_hours', 0),
                    'automatable': library_pattern.get('automatable', False),
                    'created_at': datetime.now().isoformat() + 'Z',
                    'updated_at': datetime.now().isoformat() + 'Z',
                    'last_suggested_at': None,
                    'suggestion_count': 0,
                    'tags': library_pattern.get('tags', [])
                }

                self.patterns['patterns'].append(new_pattern)
                self.patterns['last_updated'] = datetime.now().isoformat() + 'Z'
                self._save_json(self.patterns_file, self.patterns)

                # Update metrics
                self.metrics['learning']['new_patterns_learned'] += 1
                self._save_json(self.metrics_file, self.metrics)

                return new_pattern

        return None

    def _generate_pattern_signature(self, task_sequence: List[Dict[str, Any]]) -> str:
        """Generate unique signature for task sequence."""
        actions = [task.get('action', '') for task in task_sequence]
        signature = ' -> '.join(actions)
        return hashlib.md5(signature.encode()).hexdigest()

    def _pattern_signatures_match(self, signature1: str, pattern: Dict[str, Any]) -> bool:
        """Check if pattern signatures match."""
        if 'steps' not in pattern:
            return False

        actions = [step.get('action', '') for step in pattern['steps']]
        pattern_signature = ' -> '.join(actions)
        pattern_hash = hashlib.md5(pattern_signature.encode()).hexdigest()

        return signature1 == pattern_hash

    def validate_all(self) -> Dict[str, Any]:
        """
        Validate all memory files against schemas.

        Returns validation results for all memory components.
        """
        results = {
            'decisions_valid': True,
            'preferences_valid': True,
            'patterns_valid': True,
            'metrics_valid': True,
            'errors': []
        }

        # Basic structure validation
        required_decision_keys = ['version', 'decisions', 'metadata']
        for key in required_decision_keys:
            if key not in self.decisions:
                results['decisions_valid'] = False
                results['errors'].append(f"Missing key in decisions: {key}")

        required_preference_keys = ['version', 'companies', 'metadata']
        for key in required_preference_keys:
            if key not in self.preferences:
                results['preferences_valid'] = False
                results['errors'].append(f"Missing key in preferences: {key}")

        required_pattern_keys = ['version', 'patterns', 'pattern_library']
        for key in required_pattern_keys:
            if key not in self.patterns:
                results['patterns_valid'] = False
                results['errors'].append(f"Missing key in patterns: {key}")

        required_metric_keys = ['version', 'adoption', 'effectiveness', 'learning', 'quality']
        for key in required_metric_keys:
            if key not in self.metrics:
                results['metrics_valid'] = False
                results['errors'].append(f"Missing key in metrics: {key}")

        # Update metrics
        self.metrics['quality']['schema_validations']['passed'] = sum([
            results['decisions_valid'],
            results['preferences_valid'],
            results['patterns_valid'],
            results['metrics_valid']
        ])
        self.metrics['quality']['schema_validations']['failed'] = 4 - self.metrics['quality']['schema_validations']['passed']
        self._save_json(self.metrics_file, self.metrics)

        return results


def main():
    """Command-line interface for memory operations."""
    parser = argparse.ArgumentParser(description='ARIA Memory Manager')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Store decision command
    store_parser = subparsers.add_parser('store-decision', help='Store a regulatory decision')
    store_parser.add_argument('--question', required=True, help='Regulatory question')
    store_parser.add_argument('--answer', required=True, help='Decision answer')
    store_parser.add_argument('--regulation', required=True, help='Source regulation')
    store_parser.add_argument('--section', help='Regulation section')
    store_parser.add_argument('--rationale', help='Decision rationale')
    store_parser.add_argument('--domain', default='FDA', help='Regulatory domain (FDA, EU MDR, MFDS)')
    store_parser.add_argument('--company-specific', action='store_true', help='Company-specific interpretation')
    store_parser.add_argument('--confidence', type=float, default=0.8, help='Confidence score (0-1)')

    # Retrieve decisions command
    retrieve_parser = subparsers.add_parser('retrieve-decisions', help='Retrieve relevant decisions')
    retrieve_parser.add_argument('--query', required=True, help='Search query')
    retrieve_parser.add_argument('--threshold', type=float, default=0.7, help='Relevance threshold')
    retrieve_parser.add_argument('--domain', help='Filter by regulatory domain')

    # Learn preference command
    preference_parser = subparsers.add_parser('learn-preference', help='Learn company preference')
    preference_parser.add_argument('--company-id', default='default', help='Company ID')
    preference_parser.add_argument('--category', required=True, help='Preference category')
    preference_parser.add_argument('--key', required=True, help='Preference key')
    preference_parser.add_argument('--value', required=True, help='Preference value')

    # Record feedback command
    feedback_parser = subparsers.add_parser('record-feedback', help='Record suggestion feedback')
    feedback_parser.add_argument('--company-id', default='default', help='Company ID')
    feedback_parser.add_argument('--suggestion-type', required=True, help='Suggestion type')
    feedback_parser.add_argument('--feedback', required=True, choices=['accepted', 'rejected', 'modified'], help='Feedback')
    feedback_parser.add_argument('--reason', help='Reason for feedback')

    # Validate command
    validate_parser = subparsers.add_parser('validate', help='Validate memory files')
    validate_parser.add_argument('--all', action='store_true', help='Validate all memory files')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    manager = ARIAMemoryManager()

    if args.command == 'store-decision':
        decision_data = {
            'question': args.question,
            'answer': args.answer,
            'regulation': args.regulation,
            'section': args.section,
            'rationale': args.rationale,
            'regulatory_domain': args.domain,
            'company_specific': args.company_specific,
            'confidence_score': args.confidence
        }
        manager.store_decision(decision_data)

    elif args.command == 'retrieve-decisions':
        results = manager.retrieve_decisions(args.query, args.threshold, args.domain)
        print(f"\nFound {len(results)} relevant decisions:")
        for result in results:
            decision = result['decision']
            print(f"\n[{decision['decision_id']}] Relevance: {result['relevance_score']:.2f}")
            print(f"Question: {decision['question']}")
            print(f"Answer: {decision['answer'][:100]}...")
            print(f"Regulation: {decision['regulation']}")

    elif args.command == 'learn-preference':
        manager.learn_preference(args.company_id, args.category, args.key, args.value)

    elif args.command == 'record-feedback':
        manager.record_suggestion_feedback(args.company_id, args.suggestion_type, args.feedback, args.reason)

    elif args.command == 'validate':
        results = manager.validate_all()
        print("\nValidation Results:")
        print(f"Decisions: {'VALID' if results['decisions_valid'] else 'INVALID'}")
        print(f"Preferences: {'VALID' if results['preferences_valid'] else 'INVALID'}")
        print(f"Patterns: {'VALID' if results['patterns_valid'] else 'INVALID'}")
        print(f"Metrics: {'VALID' if results['metrics_valid'] else 'INVALID'}")

        if results['errors']:
            print("\nErrors:")
            for error in results['errors']:
                print(f"  - {error}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
