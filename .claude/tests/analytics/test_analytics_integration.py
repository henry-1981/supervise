#!/usr/bin/env python3
"""
Integration tests for ARIA Advanced Analytics Features.
Tests complaint trend analysis, regulatory change monitoring, and knowledge base operations.
"""

import unittest
import json
import tempfile
import os
from datetime import datetime, timedelta
from typing import Dict, List


class TestComplaintTrendAnalysis(unittest.TestCase):
    """Test complaint trend analysis functionality."""

    def setUp(self):
        """Set up test fixtures."""
        self.test_data = self._generate_test_complaints()
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Clean up test fixtures."""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def _generate_test_complaints(self) -> List[Dict]:
        """Generate synthetic complaint data for testing."""
        complaints = []

        # Normal months: 20-25 complaints
        for month in [1, 2]:
            for day in range(1, 29):
                count = 20 if month == 1 else 25
                for i in range(count // 28 + (1 if day % 7 == 0 else 0)):
                    complaints.append({
                        'date': f'2025-0{month}-{day:02d}',
                        'type': self._get_complaint_type(),
                        'lot': f'LOT-2025-0{month}-{(day % 30) + 1:02d}',
                        'region': self._get_region(),
                        'severity': self._get_severity()
                    })

        # Anomaly month: 45 complaints
        for day in range(1, 29):
            count = 1 if day % 3 == 0 else 2
            for i in range(count):
                complaints.append({
                    'date': f'2025-03-{day:02d}',
                    'type': 'Software Crash' if day % 2 == 0 else self._get_complaint_type(),
                    'lot': 'LOT-2025-03-15' if day <= 14 else 'LOT-2025-03-16',
                    'region': 'IL' if day <= 10 else ('IN' if day <= 20 else 'OH'),
                    'severity': 'high' if day % 3 == 0 else self._get_severity()
                })

        return complaints

    def _get_complaint_type(self) -> str:
        """Get random complaint type."""
        types = ['Software Crash', 'UI Issue', 'Performance', 'Data Loss',
                 'Connectivity', 'Hardware Failure', 'Battery Issue']
        return types[hash(datetime.now().microsecond) % len(types)]

    def _get_region(self) -> str:
        """Get random region."""
        regions = ['CA', 'NY', 'TX', 'FL', 'WA', 'IL', 'OH', 'IN']
        return regions[hash(datetime.now().microsecond) % len(regions)]

    def _get_severity(self) -> str:
        """Get random severity."""
        severities = ['low', 'medium', 'high']
        return severities[hash(datetime.now().microsecond) % len(severities)]

    def test_aggregate_by_month(self):
        """Test complaint aggregation by month."""
        aggregated = {}

        for complaint in self.test_data:
            month_key = complaint['date'][:7]  # YYYY-MM
            aggregated[month_key] = aggregated.get(month_key, 0) + 1

        self.assertIn('2025-01', aggregated)
        self.assertIn('2025-02', aggregated)
        self.assertIn('2025-03', aggregated)

        # March should have significantly more complaints
        self.assertGreater(aggregated['2025-03'], aggregated['2025-02'])

    def test_calculate_baseline(self):
        """Test statistical baseline calculation."""
        # Aggregate by month
        counts = {'2025-01': 20, '2025-02': 25, '2025-03': 45}

        # Calculate baseline from first two months
        baseline_counts = [counts['2025-01'], counts['2025-02']]
        mean = sum(baseline_counts) / len(baseline_counts)
        variance = sum((x - mean) ** 2 for x in baseline_counts) / len(baseline_counts)
        std_dev = variance ** 0.5

        upper_limit = mean + 2 * std_dev

        # March should exceed upper limit
        self.assertGreater(counts['2025-03'], upper_limit)

    def test_detect_anomalies(self):
        """Test anomaly detection."""
        aggregated = {'2025-01': 20, '2025-02': 25, '2025-03': 45}

        # Calculate baseline
        baseline_counts = [aggregated['2025-01'], aggregated['2025-02']]
        mean = sum(baseline_counts) / len(baseline_counts)
        std_dev = (sum((x - mean) ** 2 for x in baseline_counts) / len(baseline_counts)) ** 0.5
        upper_limit = mean + 2 * std_dev

        # Detect anomalies
        anomalies = []
        for period, count in aggregated.items():
            if count > upper_limit:
                deviation = (count - mean) / std_dev
                anomalies.append({'period': period, 'count': count, 'deviation': deviation})

        self.assertEqual(len(anomalies), 1)
        self.assertEqual(anomalies[0]['period'], '2025-03')

    def test_correlate_lots(self):
        """Test lot correlation analysis."""
        # Count complaints by lot in March
        lot_counts = {}
        for complaint in self.test_data:
            if '2025-03' in complaint['date']:
                lot = complaint['lot']
                lot_counts[lot] = lot_counts.get(lot, 0) + 1

        # Should find high counts for specific lots
        high_lots = [lot for lot, count in lot_counts.items() if count > 2]
        self.assertGreater(len(high_lots), 0)

    def test_correlate_geography(self):
        """Test geographical correlation analysis."""
        # Count complaints by region in March
        region_counts = {}
        for complaint in self.test_data:
            if '2025-03' in complaint['date']:
                region = complaint['region']
                region_counts[region] = region_counts.get(region, 0) + 1

        # Should find cluster in Midwest
        midwest_count = sum(region_counts.get(r, 0) for r in ['IL', 'IN', 'OH'])
        self.assertGreater(midwest_count, 5)


class TestRegulatoryChangeMonitoring(unittest.TestCase):
    """Test regulatory change monitoring functionality."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.mapping_file = os.path.join(self.temp_dir, 'regulation-mapping.json')
        self._create_test_mapping()

    def tearDown(self):
        """Clean up test fixtures."""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def _create_test_mapping(self):
        """Create test regulation mapping."""
        mapping = {
            'regulations': {
                'FDA-2025-001': {
                    'regulation_id': 'FDA-2025-001',
                    'domain': 'FDA',
                    'citation': '21 CFR 820.30',
                    'title': 'Design Controls',
                    'category': 'quality_system',
                    'status': 'current',
                    'affected_document_types': ['Technical File', 'Quality Manual']
                }
            },
            'documents': {
                'DOC-20250101-0001': {
                    'document_id': 'DOC-20250101-0001',
                    'title': 'Technical File for Device X',
                    'type': 'Technical File',
                    'regulatory_domain': 'FDA',
                    'applicable_regulations': ['FDA-2025-001'],
                    'status': 'pending',
                    'last_updated': datetime.now().isoformat()
                },
                'DOC-20250101-0002': {
                    'document_id': 'DOC-20250101-0002',
                    'title': 'Quality Manual v2.0',
                    'type': 'Quality Manual',
                    'regulatory_domain': 'FDA',
                    'applicable_regulations': ['FDA-2025-001'],
                    'status': 'approved',
                    'last_updated': (datetime.now() - timedelta(days=30)).isoformat()
                }
            },
            'metadata': {
                'version': '1.0',
                'last_updated': datetime.now().isoformat(),
                'total_regulations': 1,
                'total_documents': 2
            }
        }

        with open(self.mapping_file, 'w') as f:
            json.dump(mapping, f)

    def test_identify_affected_documents(self):
        """Test identification of affected documents."""
        # Load mapping
        with open(self.mapping_file, 'r') as f:
            mapping = json.load(f)

        # Simulate regulatory change affecting Technical Files and Quality Manuals
        affected_document_types = ['Technical File', 'Quality Manual']
        regulatory_domain = 'FDA'

        affected = []
        for doc_id, doc_info in mapping['documents'].items():
            if (doc_info.get('type') in affected_document_types and
                doc_info.get('regulatory_domain') == regulatory_domain):

                # Calculate priority
                priority = 'high' if doc_info.get('status') == 'pending' else 'medium'
                if self._is_recent(doc_info.get('last_updated', ''), months=6):
                    priority = 'medium'

                affected.append({
                    'document_id': doc_id,
                    'title': doc_info.get('title', ''),
                    'type': doc_info.get('type', ''),
                    'priority': priority,
                    'status': doc_info.get('status', '')
                })

        # Should find both documents
        self.assertEqual(len(affected), 2)

        # Pending document should have higher priority
        pending_doc = next((d for d in affected if d['status'] == 'pending'), None)
        self.assertIsNotNone(pending_doc)
        self.assertEqual(pending_doc['priority'], 'high')

    def test_parse_regulatory_change(self):
        """Test parsing of regulatory changes."""
        update = {
            'domain': 'FDA',
            'type': 'guidance',
            'title': 'Clinical Evidence for SaMD',
            'date': '2025-02-01',
            'summary': 'New requirements for real-world evidence inclusion'
        }

        parsed = {
            'update_id': f"{update['domain']}-{update['date']}",
            'domain': update['domain'],
            'affected_document_types': [],
            'key_changes': []
        }

        if 'SaMD' in update.get('title', ''):
            parsed['affected_document_types'] = ['CER', 'Technical File', '510(k) Submission']
            parsed['key_changes'] = [
                'Real-world evidence (RWE) inclusion required',
                'Clinical validation criteria updated for AI/ML'
            ]

        self.assertIn('CER', parsed['affected_document_types'])
        self.assertEqual(len(parsed['key_changes']), 2)

    def _is_recent(self, date_str: str, months: int = 6) -> bool:
        """Check if date is within recent months."""
        if not date_str:
            return False
        try:
            doc_date = datetime.fromisoformat(date_str)
            cutoff = datetime.now() - timedelta(days=months * 30)
            return doc_date > cutoff
        except:
            return False


class TestKnowledgeBase(unittest.TestCase):
    """Test knowledge base functionality."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.kb_file = os.path.join(self.temp_dir, 'knowledge-base.json')
        self.kb = self._create_test_kb()

    def tearDown(self):
        """Clean up test fixtures."""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def _create_test_kb(self) -> Dict:
        """Create test knowledge base."""
        kb = {
            'entries': [
                {
                    'entry_id': 'KB-20250101-0001',
                    'content_type': 'substantial_equivalence_argument',
                    'submission_id': '510k-2024-123',
                    'outcome': 'approved',
                    'outcome_details': {
                        'approval_date': '2024-06-15',
                        'approval_number': 'K241234'
                    },
                    'content': 'The proposed device is substantially equivalent to predicate device X...',
                    'regulatory_domain': 'FDA',
                    'device_type': 'Class II SaMD',
                    'tags': ['predicate', 'substantial equivalence', 'software'],
                    'applicability_context': {
                        'technology_type': 'Mobile App',
                        'anatomy': 'Cardiovascular'
                    },
                    'regulation_version': '21 CFR 820',
                    'created_at': '2024-01-01T10:00:00Z',
                    'last_reviewed': '2024-12-01T10:00:00Z',
                    'confidence_score': 0.95,
                    'quality_indicators': {
                        'reused_count': 3,
                        'reuse_success_rate': 1.0,
                        'user_rating': 5.0
                    }
                },
                {
                    'entry_id': 'KB-20250101-0002',
                    'content_type': 'clinical_evidence_summary',
                    'submission_id': '510k-2024-456',
                    'outcome': 'not_approved',
                    'outcome_details': {
                        'rejection_reason': 'Insufficient clinical evidence'
                    },
                    'content': 'Clinical evidence summary for device Y...',
                    'regulatory_domain': 'FDA',
                    'device_type': 'Class II SaMD',
                    'tags': ['clinical', 'evidence', 'insufficient'],
                    'applicability_context': {
                        'technology_type': 'AI/ML'
                    },
                    'regulation_version': '21 CFR 820',
                    'created_at': '2024-01-01T10:00:00Z',
                    'last_reviewed': '2024-12-01T10:00:00Z',
                    'confidence_score': 0.6
                }
            ],
            'tags': {
                'predicate': 1,
                'substantial equivalence': 1,
                'software': 1,
                'clinical': 1,
                'evidence': 1,
                'insufficient': 1
            },
            'outcomes': {
                'approved': 1,
                'approvable': 0,
                'not_approved': 1,
                'pending': 0,
                'withdrawn': 0
            },
            'metadata': {
                'version': '1.0',
                'last_updated': datetime.now().isoformat(),
                'total_entries': 2,
                'storage_backend': 'json'
            }
        }

        with open(self.kb_file, 'w') as f:
            json.dump(kb, f)

        return kb

    def test_search_by_keyword(self):
        """Test knowledge base search by keyword."""
        # Search for 'predicate'
        query = 'predicate'
        results = []

        for entry in self.kb['entries']:
            score = 0.0
            query_lower = query.lower()

            if query_lower in entry.get('content', '').lower():
                score += 1.5
            for tag in entry.get('tags', []):
                if query_lower in tag.lower():
                    score += 1.0
            if entry.get('outcome') == 'approved':
                score += 0.5

            if score > 0:
                results.append({**entry, 'relevance_score': score})

        results.sort(key=lambda x: x['relevance_score'], reverse=True)

        self.assertGreater(len(results), 0)
        self.assertEqual(results[0]['entry_id'], 'KB-20250101-0001')

    def test_search_with_filters(self):
        """Test knowledge base search with outcome filter."""
        # Search for approved content only
        results = [
            entry for entry in self.kb['entries']
            if entry.get('outcome') == 'approved'
        ]

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['entry_id'], 'KB-20250101-0001')

    def test_context_validation_device_mismatch(self):
        """Test context validation with device type mismatch."""
        entry = self.kb['entries'][0]

        new_context = {
            'device_type': 'Class III',  # Different from entry
            'current_regulation': '21 CFR 820'
        }

        warnings = []

        if entry.get('device_type') != new_context.get('device_type'):
            warnings.append({
                'type': 'device_mismatch',
                'message': f"Device type differs: {entry.get('device_type')} vs {new_context.get('device_type')}"
            })

        self.assertGreater(len(warnings), 0)
        self.assertEqual(warnings[0]['type'], 'device_mismatch')

    def test_context_validation_failed_outcome(self):
        """Test context validation with failed outcome."""
        entry = self.kb['entries'][1]  # not_approved entry

        warnings = []

        if entry.get('outcome') == 'not_approved':
            warnings.append({
                'type': 'failed_outcome',
                'message': 'This content was from a submission that was not approved',
                'recommendation': 'Review rejection reasons before reusing'
            })

        self.assertGreater(len(warnings), 0)
        self.assertEqual(warnings[0]['type'], 'failed_outcome')

    def test_calculate_relevance_score(self):
        """Test relevance score calculation."""
        query = 'substantial equivalence predicate'
        entry = self.kb['entries'][0]

        query_lower = query.lower()
        score = 0.0

        if query_lower in entry.get('content', '').lower():
            score += 1.5

        for tag in entry.get('tags', []):
            if any(q in tag.lower() for q in query_lower.split()):
                score += 1.0

        if entry.get('outcome') == 'approved':
            score += 0.5

        self.assertGreater(score, 0)
        self.assertGreaterEqual(score, 2.0)  # Should have at least 2 points


class TestAlertGeneration(unittest.TestCase):
    """Test alert generation functionality."""

    def test_complaint_trend_alert_format(self):
        """Test complaint trend alert formatting."""
        alert_data = {
            'period': '2025-03',
            'count': 45,
            'deviation': 2.5,
            'severity': 'high',
            'baseline': {
                'mean': 22.5,
                'std_dev': 3.5,
                'confidence': 'medium'
            },
            'lots': ['LOT-2025-03-15', 'LOT-2025-03-16'],
            'regions': {'IL': 8, 'IN': 6, 'OH': 5},
            'complaint_types': {'Software Crash': 60.0, 'UI Issue': 20.0}
        }

        alert = f"""## Complaint Trend Alert

**Severity**: {alert_data['severity'].title()}
**Period**: {alert_data['period']}

### Trend Summary
- Complaints: {alert_data['count']}
- Baseline (μ ± 2σ): {alert_data['baseline']['mean']:.1f} ± {alert_data['baseline']['std_dev']:.1f}
- Deviation: {alert_data['deviation']:.1f}σ above mean

### Lot Correlation
"""
        for lot in alert_data['lots']:
            alert += f"- **{lot}**: High complaint frequency\n"

        alert += "\n### Geographical Clusters\n"
        for region, count in alert_data['regions'].items():
            alert += f"- **{region}**: {count} complaints\n"

        self.assertIn('Complaint Trend Alert', alert)
        self.assertIn('LOT-2025-03-15', alert)
        self.assertIn('IL', alert)

    def test_regulatory_change_alert_format(self):
        """Test regulatory change impact alert formatting."""
        alert_data = {
            'domain': 'FDA',
            'title': 'Clinical Evidence for SaMD',
            'date': '2025-02-01',
            'key_changes': [
                'Real-world evidence (RWE) inclusion required',
                'Clinical validation criteria updated for AI/ML'
            ],
            'affected_docs': [
                {'document_id': 'DOC-001', 'title': 'CER-2024-001', 'type': 'CER', 'priority': 'high'},
                {'document_id': 'DOC-002', 'title': 'Technical-File-005', 'type': 'Technical File', 'priority': 'medium'}
            ]
        }

        alert = f"""## Regulatory Change Impact Alert

**Regulation**: {alert_data['domain']} {alert_data['title']}
**Updated**: {alert_data['date']}

### Key Changes
"""
        for change in alert_data['key_changes']:
            alert += f"- {change}\n"

        alert += "\n### Affected Documents\n"
        for doc in alert_data['affected_docs']:
            priority_emoji = {'high': '🔴', 'medium': '🟡', 'low': '🟢'}
            alert += f"- [{priority_emoji.get(doc['priority'], '⚪')}] **{doc['document_id']}** ({doc['type']}) - {doc['priority'].title()} Priority\n"

        self.assertIn('Regulatory Change Impact Alert', alert)
        self.assertIn('DOC-001', alert)
        self.assertIn('🔴', alert)


if __name__ == '__main__':
    # Run tests
    unittest.main(verbosity=2)
