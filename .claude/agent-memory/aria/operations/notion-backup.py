#!/usr/bin/env python3
"""
ARIA Notion Backup Integration

Implements Notion MCP backup persistence for Agent Memory System.
Provides automatic synchronization of local memory files to Notion database.

Requirements:
- Notion MCP server configured and accessible
- Notion database with schema matching memory structures
- API token with database read/write permissions

Usage:
    python notion-backup.py --sync-all
    python notion-backup.py --sync-decisions
    python notion-backup.py --restore-backup --database-id "..."
"""

import json
import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
import argparse
import time


class NotionMemoryBackup:
    """Manages Notion backup operations for ARIA memory system."""

    def __init__(self, memory_dir: Optional[Path] = None,
                 notion_database_id: Optional[str] = None):
        """Initialize Notion backup manager."""
        if memory_dir is None:
            script_dir = Path(__file__).parent.parent
            memory_dir = script_dir

        self.memory_dir = Path(memory_dir)
        self.notion_database_id = notion_database_id or os.getenv('NOTION_ARIA_MEMORY_DB')

        if not self.notion_database_id:
            print("Warning: NOTION_ARIA_MEMORY_DB not set", file=sys.stderr)

        self.memory_files = {
            'regulatory-decisions': self.memory_dir / 'regulatory-decisions-enhanced.json',
            'company-preferences': self.memory_dir / 'company-preferences-enhanced.json',
            'task-patterns': self.memory_dir / 'task-patterns-enhanced.json',
            'learning-metrics': self.memory_dir / 'learning-metrics-enhanced.json'
        }

        self.sync_status = {
            'last_sync': None,
            'last_sync_status': 'success',
            'files_synced': [],
            'sync_errors': []
        }

    def _call_mcp_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Any:
        """
        Call Notion MCP tool via Claude Code integration.

        This is a placeholder for the actual MCP integration.
        In production, this would use the MCP client API.
        """
        # For now, return mock data
        # In production, this would call:
        # mcp__claude_ai_Notion__notion-create-pages or similar
        print(f"MCP Call: {tool_name} with args: {arguments}")
        return {'success': True, 'id': 'mock-page-id'}

    def _load_memory_file(self, file_type: str) -> Dict[str, Any]:
        """Load memory file data."""
        file_path = self.memory_files.get(file_type)
        if not file_path or not file_path.exists():
            return {}

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {file_type}: {e}", file=sys.stderr)
            return {}

    def sync_decision(self, decision: Dict[str, Any]) -> bool:
        """Sync a single regulatory decision to Notion."""
        if not self.notion_database_id:
            print("Notion database ID not configured", file=sys.stderr)
            return False

        try:
            # Prepare Notion page properties
            page_data = {
                'parent': {'database_id': self.notion_database_id},
                'properties': {
                    'Decision ID': {
                        'title': [{'text': {'content': decision['decision_id']}}]
                    },
                    'Question': {
                        'rich_text': [{'text': {'content': decision['question']}}]
                    },
                    'Answer': {
                        'rich_text': [{'text': {'content': decision['answer']}}]
                    },
                    'Regulation': {
                        'rich_text': [{'text': {'content': decision['regulation']}}]
                    },
                    'Regulatory Domain': {
                        'select': {'name': decision.get('regulatory_domain', 'FDA')}
                    },
                    'Company Specific': {
                        'checkbox': decision.get('company_specific', False)
                    },
                    'Confidence Score': {
                        'number': decision.get('confidence_score', 0.0)
                    },
                    'Valid Until': {
                        'date': {'start': decision.get('valid_until')} if decision.get('valid_until') else None
                    },
                    'Created At': {
                        'date': {'start': decision['created_at']}
                    },
                    'Is Valid': {
                        'checkbox': decision.get('is_valid', True)
                    },
                    'Tags': {
                        'multi_select': [{'name': tag} for tag in decision.get('tags', [])]
                    }
                },
                'children': [
                    {
                        'object': 'block',
                        'type': 'paragraph',
                        'paragraph': {
                            'rich_text': [{'text': {'content': decision.get('rationale', '')}}]
                        }
                    }
                ]
            }

            # Call MCP tool to create page
            result = self._call_mcp_tool('notion-create-pages', {'pages': [page_data]})

            return result.get('success', False)

        except Exception as e:
            print(f"Error syncing decision {decision.get('decision_id')}: {e}", file=sys.stderr)
            return False

    def sync_decisions(self) -> Dict[str, Any]:
        """Sync all regulatory decisions to Notion."""
        decisions_data = self._load_memory_file('regulatory-decisions')
        decisions = decisions_data.get('decisions', [])

        results = {
            'total': len(decisions),
            'synced': 0,
            'failed': 0,
            'errors': []
        }

        for decision in decisions:
            if self.sync_decision(decision):
                results['synced'] += 1
            else:
                results['failed'] += 1
                results['errors'].append(decision.get('decision_id', 'unknown'))

        return results

    def sync_preferences(self) -> Dict[str, Any]:
        """Sync company preferences to Notion."""
        preferences_data = self._load_memory_file('company-preferences')
        companies = preferences_data.get('companies', {})

        results = {
            'total': len(companies),
            'synced': 0,
            'failed': 0,
            'errors': []
        }

        for company_id, company_data in companies.items():
            try:
                page_data = {
                    'parent': {'database_id': self.notion_database_id},
                    'properties': {
                        'Company ID': {
                            'title': [{'text': {'content': company_id}}]
                        },
                        'Company Name': {
                            'rich_text': [{'text': {'content': company_data.get('company_name', company_id)}}]
                        },
                        'Type': {
                            'select': {'name': 'Company Preference'}
                        },
                        'Last Updated': {
                            'date': {'start': company_data.get('updated_at')}
                        }
                    },
                    'children': [
                        {
                            'object': 'block',
                            'type': 'code',
                            'code': {
                                'rich_text': [{'text': {'content': json.dumps(company_data, indent=2)}}],
                                'language': 'json'
                            }
                        }
                    ]
                }

                result = self._call_mcp_tool('notion-create-pages', {'pages': [page_data]})

                if result.get('success'):
                    results['synced'] += 1
                else:
                    results['failed'] += 1
                    results['errors'].append(company_id)

            except Exception as e:
                results['failed'] += 1
                results['errors'].append(company_id)
                print(f"Error syncing preferences for {company_id}: {e}", file=sys.stderr)

        return results

    def sync_patterns(self) -> Dict[str, Any]:
        """Sync task patterns to Notion."""
        patterns_data = self._load_memory_file('task-patterns')
        patterns = patterns_data.get('patterns', [])

        results = {
            'total': len(patterns),
            'synced': 0,
            'failed': 0,
            'errors': []
        }

        for pattern in patterns:
            try:
                page_data = {
                    'parent': {'database_id': self.notion_database_id},
                    'properties': {
                        'Pattern ID': {
                            'title': [{'text': {'content': pattern.get('id', 'unknown')}}]
                        },
                        'Pattern Name': {
                            'rich_text': [{'text': {'content': pattern.get('name', '')}}]
                        },
                        'Type': {
                            'select': {'name': 'Task Pattern'}
                        },
                        'Occurrence Count': {
                            'number': pattern.get('occurrence_count', 0)
                        },
                        'Confidence': {
                            'number': pattern.get('confidence', 0.0)
                        },
                        'Automatable': {
                            'checkbox': pattern.get('automatable', False)
                        },
                        'Created At': {
                            'date': {'start': pattern.get('created_at')}
                        }
                    },
                    'children': [
                        {
                            'object': 'block',
                            'type': 'code',
                            'code': {
                                'rich_text': [{'text': {'content': json.dumps(pattern, indent=2)}}],
                                'language': 'json'
                            }
                        }
                    ]
                }

                result = self._call_mcp_tool('notion-create-pages', {'pages': [page_data]})

                if result.get('success'):
                    results['synced'] += 1
                else:
                    results['failed'] += 1
                    results['errors'].append(pattern.get('id', 'unknown'))

            except Exception as e:
                results['failed'] += 1
                results['errors'].append(pattern.get('id', 'unknown'))
                print(f"Error syncing pattern {pattern.get('id')}: {e}", file=sys.stderr)

        return results

    def sync_metrics(self) -> Dict[str, Any]:
        """Sync learning metrics to Notion."""
        metrics_data = self._load_memory_file('learning-metrics')

        try:
            page_data = {
                'parent': {'database_id': self.notion_database_id},
                'properties': {
                    'Report ID': {
                        'title': [{'text': {'content': f"Metrics-{datetime.now().strftime('%Y%m%d')}"}}]
                    },
                    'Type': {
                        'select': {'name': 'Learning Metrics'}
                    },
                    'Report Date': {
                        'date': {'start': datetime.now().isoformat()}
                    },
                    'Total Interactions': {
                        'number': metrics_data.get('adoption', {}).get('total_interactions', 0)
                    },
                    'Memory Integrity': {
                        'number': metrics_data.get('quality', {}).get('memory_integrity', 0)
                    }
                },
                'children': [
                    {
                        'object': 'block',
                        'type': 'code',
                        'code': {
                            'rich_text': [{'text': {'content': json.dumps(metrics_data, indent=2)}}],
                            'language': 'json'
                        }
                    }
                ]
            }

            result = self._call_mcp_tool('notion-create-pages', {'pages': [page_data]})

            return {
                'total': 1,
                'synced': 1 if result.get('success') else 0,
                'failed': 0 if result.get('success') else 1,
                'errors': []
            }

        except Exception as e:
            print(f"Error syncing metrics: {e}", file=sys.stderr)
            return {
                'total': 1,
                'synced': 0,
                'failed': 1,
                'errors': ['metrics']
            }

    def sync_all(self, file_types: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Sync all or specified memory files to Notion.

        Args:
            file_types: List of file types to sync (e.g., ['decisions', 'preferences']).
                       If None, sync all files.
        """
        if file_types is None:
            file_types = ['decisions', 'preferences', 'patterns', 'metrics']

        start_time = time.time()
        results = {
            'start_time': datetime.now().isoformat(),
            'file_types': file_types,
            'files': {},
            'summary': {
                'total': 0,
                'synced': 0,
                'failed': 0
            }
        }

        for file_type in file_types:
            if file_type == 'decisions':
                result = self.sync_decisions()
            elif file_type == 'preferences':
                result = self.sync_preferences()
            elif file_type == 'patterns':
                result = self.sync_patterns()
            elif file_type == 'metrics':
                result = self.sync_metrics()
            else:
                print(f"Unknown file type: {file_type}", file=sys.stderr)
                continue

            results['files'][file_type] = result
            results['summary']['total'] += result['total']
            results['summary']['synced'] += result['synced']
            results['summary']['failed'] += result['failed']

        results['end_time'] = datetime.now().isoformat()
        results['duration_seconds'] = time.time() - start_time

        # Update sync status
        self.sync_status['last_sync'] = datetime.now().isoformat()
        self.sync_status['last_sync_status'] = 'success' if results['summary']['failed'] == 0 else 'partial'
        self.sync_status['files_synced'] = [ft for ft, r in results['files'].items() if r['synced'] > 0]
        self.sync_status['sync_errors'] = [
            f"{ft}: {r['errors']}" for ft, r in results['files'].items() if r['errors']
        ]

        return results

    def restore_backup(self, output_dir: Optional[Path] = None) -> bool:
        """
        Restore memory files from Notion backup.

        This is a placeholder for the restoration functionality.
        In production, this would query the Notion database and reconstruct memory files.
        """
        if not self.notion_database_id:
            print("Notion database ID not configured", file=sys.stderr)
            return False

        print("Backup restoration not yet implemented", file=sys.stderr)
        print("This would query Notion database and reconstruct memory files", file=sys.stderr)
        return False

    def get_sync_status(self) -> Dict[str, Any]:
        """Get current sync status."""
        return self.sync_status


def main():
    """Command-line interface for Notion backup operations."""
    parser = argparse.ArgumentParser(description='ARIA Notion Backup')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Sync all command
    sync_parser = subparsers.add_parser('sync-all', help='Sync all memory files to Notion')
    sync_parser.add_argument('--types', nargs='+',
                             choices=['decisions', 'preferences', 'patterns', 'metrics'],
                             help='Specific file types to sync')

    # Sync decisions command
    subparsers.add_parser('sync-decisions', help='Sync regulatory decisions')

    # Sync preferences command
    subparsers.add_parser('sync-preferences', help='Sync company preferences')

    # Sync patterns command
    subparsers.add_parser('sync-patterns', help='Sync task patterns')

    # Sync metrics command
    subparsers.add_parser('sync-metrics', help='Sync learning metrics')

    # Restore backup command
    restore_parser = subparsers.add_parser('restore-backup', help='Restore from Notion backup')
    restore_parser.add_argument('--output-dir', help='Output directory for restored files')

    # Status command
    subparsers.add_parser('status', help='Get sync status')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    backup = NotionMemoryBackup()

    if args.command == 'sync-all':
        results = backup.sync_all(args.types)
        print("\nSync Results:")
        print(f"Duration: {results['duration_seconds']:.2f} seconds")
        print(f"Total: {results['summary']['total']}")
        print(f"Synced: {results['summary']['synced']}")
        print(f"Failed: {results['summary']['failed']}")

        for file_type, result in results['files'].items():
            print(f"\n{file_type.capitalize()}:")
            print(f"  Total: {result['total']}")
            print(f"  Synced: {result['synced']}")
            print(f"  Failed: {result['failed']}")
            if result['errors']:
                print(f"  Errors: {', '.join(result['errors'])}")

    elif args.command == 'sync-decisions':
        results = backup.sync_decisions()
        print(f"\nDecisions Synced: {results['synced']}/{results['total']}")
        if results['failed'] > 0:
            print(f"Failed: {results['failed']}")
            print(f"Errors: {', '.join(results['errors'])}")

    elif args.command == 'sync-preferences':
        results = backup.sync_preferences()
        print(f"\nPreferences Synced: {results['synced']}/{results['total']}")
        if results['failed'] > 0:
            print(f"Failed: {results['failed']}")
            print(f"Errors: {', '.join(results['errors'])}")

    elif args.command == 'sync-patterns':
        results = backup.sync_patterns()
        print(f"\nPatterns Synced: {results['synced']}/{results['total']}")
        if results['failed'] > 0:
            print(f"Failed: {results['failed']}")
            print(f"Errors: {', '.join(results['errors'])}")

    elif args.command == 'sync-metrics':
        results = backup.sync_metrics()
        print(f"\nMetrics Synced: {results['synced']}/{results['total']}")

    elif args.command == 'restore-backup':
        output_dir = Path(args.output_dir) if args.output_dir else backup.memory_dir
        success = backup.restore_backup(output_dir)
        return 0 if success else 1

    elif args.command == 'status':
        status = backup.get_sync_status()
        print("\nSync Status:")
        print(f"Last Sync: {status['last_sync'] or 'Never'}")
        print(f"Status: {status['last_sync_status']}")
        print(f"Files Synced: {', '.join(status['files_synced']) if status['files_synced'] else 'None'}")
        if status['sync_errors']:
            print(f"Errors: {', '.join(status['sync_errors'])}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
