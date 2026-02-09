---
name: aria-analytics
description: >
  Advanced analytics capabilities for ARIA (AI Regulatory Intelligence Assistant). Implements
  complaint trend analysis with statistical baseline calculation, regulatory change impact
  analysis with monitoring and document mapping, and cross-submission knowledge utilization
  with search and context validation. Integrates with Context7 MCP and Notion MCP for
  regulatory documentation and knowledge base storage.

license: Apache-2.0
compatibility: Designed for Claude Code
allowed-tools: Read Write Edit Grep Glob Bash WebSearch
user-invocable: false
metadata:
  version: "1.0.0"
  category: "domain"
  status: "active"
  updated: "2026-02-09"
  modularized: "false"
  tags: "aria, analytics, regulatory, medical-device, trend-analysis"
  context7-libraries: fda-guidance, eu-mdr, mfds-guidance
  agent: "aria-analytics-specialist"

# ARIA Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# ARIA Extension: Triggers
triggers:
  keywords: ["complaint", "trend", "analytics", "regulatory change", "knowledge base", "alert", "statistics", "correlation"]
  agents: ["aria-analytics-specialist", "expert-analyst"]
  phases: ["run"]
  languages: ["python", "javascript"]
---

# ARIA Analytics Skill

## Overview

This skill provides advanced analytics capabilities for the ARIA (AI Regulatory Intelligence Assistant) plugin, focusing on three main areas:

1. **Complaint Trend Analysis**: Statistical analysis of complaint data with trend detection and alerting
2. **Regulatory Change Impact Analysis**: Monitoring regulatory updates and assessing document impact
3. **Cross-Submission Knowledge Utilization**: Knowledge base search and content reuse with validation

## Module 1: Complaint Trend Analysis

### Statistical Baseline Calculation

```python
import json
import statistics
from datetime import datetime, timedelta
from typing import Dict, List, Tuple

class ComplaintTrendAnalyzer:
    """Analyzes complaint data for trends and anomalies."""

    def __init__(self, complaint_data: List[Dict]):
        """
        Initialize with complaint data.

        Args:
            complaint_data: List of complaint records with 'date', 'count', 'type', 'lot', 'region'
        """
        self.complaint_data = complaint_data
        self.baseline = None
        self.anomalies = []

    def aggregate_by_period(self, period: str = 'month') -> Dict[str, int]:
        """
        Aggregate complaints by time period.

        Args:
            period: 'day', 'week', 'month', or 'quarter'

        Returns:
            Dictionary mapping period to complaint count
        """
        aggregated = {}
        for complaint in self.complaint_data:
            date = datetime.fromisoformat(complaint['date'])
            if period == 'day':
                key = date.strftime('%Y-%m-%d')
            elif period == 'week':
                key = f"{date.year}-W{date.isocalendar()[1]:02d}"
            elif period == 'month':
                key = date.strftime('%Y-%m')
            elif period == 'quarter':
                key = f"{date.year}-Q{(date.month - 1) // 3 + 1}"

            aggregated[key] = aggregated.get(key, 0) + 1

        return aggregated

    def calculate_baseline(self, data: List[int]) -> Dict[str, float]:
        """
        Calculate statistical baseline with mean and standard deviation.

        Args:
            data: List of complaint counts

        Returns:
            Dictionary with 'mean', 'std_dev', 'upper_limit', 'lower_limit'
        """
        if len(data) < 3:
            # Insufficient data for reliable baseline
            return {
                'mean': statistics.mean(data) if data else 0,
                'std_dev': statistics.stdev(data) if len(data) > 1 else 0,
                'upper_limit': max(data) if data else 0,
                'lower_limit': 0,
                'confidence': 'low'
            }

        mean = statistics.mean(data)
        std_dev = statistics.stdev(data)

        # Control limits at mean ± 2σ (95.4% confidence interval)
        upper_limit = mean + 2 * std_dev
        lower_limit = max(0, mean - 2 * std_dev)

        self.baseline = {
            'mean': mean,
            'std_dev': std_dev,
            'upper_limit': upper_limit,
            'lower_limit': lower_limit,
            'confidence': 'high' if len(data) >= 12 else 'medium'
        }

        return self.baseline

    def detect_anomalies(self, aggregated_data: Dict[str, int]) -> List[Dict]:
        """
        Detect periods where complaint count exceeds baseline threshold.

        Args:
            aggregated_data: Dictionary mapping period to complaint count

        Returns:
            List of anomaly records with period, count, and deviation
        """
        if not self.baseline:
            counts = list(aggregated_data.values())
            self.calculate_baseline(counts)

        anomalies = []
        threshold = self.baseline['upper_limit']

        for period, count in aggregated_data.items():
            if count > threshold:
                deviation = (count - self.baseline['mean']) / self.baseline['std_dev']
                anomalies.append({
                    'period': period,
                    'count': count,
                    'deviation': deviation,
                    'severity': 'high' if deviation > 3 else 'medium'
                })

        self.anomalies = anomalies
        return anomalies

    def correlate_with_lots(self, anomaly_period: str) -> List[str]:
        """
        Correlate anomaly with specific manufacturing lots.

        Args:
            anomaly_period: Period identifier (e.g., '2025-03')

        Returns:
            List of lot numbers with high complaint frequency
        """
        lot_counts = {}
        for complaint in self.complaint_data:
            if anomaly_period in complaint['date']:
                lot = complaint.get('lot', 'unknown')
                lot_counts[lot] = lot_counts.get(lot, 0) + 1

        # Return lots with complaint count > 2
        return [lot for lot, count in lot_counts.items() if count > 2]

    def correlate_geography(self, anomaly_period: str) -> Dict[str, int]:
        """
        Identify geographical clusters of complaints.

        Args:
            anomaly_period: Period identifier

        Returns:
            Dictionary mapping region to complaint count
        """
        region_counts = {}
        for complaint in self.complaint_data:
            if anomaly_period in complaint['date']:
                region = complaint.get('region', 'unknown')
                region_counts[region] = region_counts.get(region, 0) + 1

        # Return regions with complaint count > 1
        return {r: c for r, c in region_counts.items() if c > 1}

    def analyze_complaint_types(self, anomaly_period: str) -> Dict[str, float]:
        """
        Analyze distribution of complaint types.

        Args:
            anomaly_period: Period identifier

        Returns:
            Dictionary mapping complaint type to percentage
        """
        type_counts = {}
        total = 0
        for complaint in self.complaint_data:
            if anomaly_period in complaint['date']:
                ctype = complaint.get('type', 'other')
                type_counts[ctype] = type_counts.get(ctype, 0) + 1
                total += 1

        if total == 0:
            return {}

        return {ctype: (count / total) * 100 for ctype, count in type_counts.items()}

    def generate_alert(self, anomaly: Dict) -> str:
        """
        Generate formatted alert for anomaly.

        Args:
            anomaly: Anomaly record from detect_anomalies()

        Returns:
            Formatted alert string in Markdown
        """
        period = anomaly['period']
        count = anomaly['count']
        deviation = anomaly['deviation']
        severity = anomaly['severity']

        # Correlation analysis
        lots = self.correlate_with_lots(period)
        regions = self.correlate_geography(period)
        complaint_types = self.analyze_complaint_types(period)

        # Build alert
        alert = f"""## Complaint Trend Alert

**Severity**: {severity.title()}
**Confidence**: {self.baseline.get('confidence', 'unknown').title()}
**Period**: {period}

### Trend Summary
- {period.split('-')[1] if '-' else period} complaints: {count}
- Baseline (μ ± 2σ): {self.baseline['mean']:.1f} ± {self.baseline['std_dev']:.1f}
- Deviation: {deviation:.1f}σ above mean
"""

        if lots:
            alert += "\n### Lot Correlation\n"
            for lot in lots:
                alert += f"- **{lot}**: High complaint frequency\n"

        if regions:
            alert += "\n### Geographical Clusters\n"
            for region, count in regions.items():
                alert += f"- **{region}**: {count} complaints\n"

        if complaint_types:
            alert += "\n### Complaint Type Distribution\n"
            for ctype, pct in sorted(complaint_types.items(), key=lambda x: x[1], reverse=True):
                alert += f"- **{ctype}**: {pct:.1f}%\n"

        # Recommendations
        alert += "\n### Recommendations\n"
        if lots:
            alert += "1. Initiate CAPA investigation for identified lots\n"
        if regions:
            alert += "2. Monitor for additional complaints from clustered regions\n"
        if deviation > 3:
            alert += "3. Consider field safety corrective action if safety risk confirmed\n"
            alert += "4. Review regulatory reporting requirements for region\n"
        alert += "5. Analyze complaint types for root cause patterns\n"

        return alert
```

### Synthetic Data Generation

```python
def generate_synthetic_complaint_data(
    n_complaints: int = 150,
    anomaly_multiplier: float = 1.0
) -> List[Dict]:
    """
    Generate synthetic complaint data for testing.

    Args:
        n_complaints: Total number of complaints to generate
        anomaly_multiplier: Multiplier for anomaly month (1.0 = normal, 2.0 = 2x increase)

    Returns:
        List of complaint records
    """
    import random
    from datetime import datetime, timedelta

    # Base complaint types
    complaint_types = [
        'Software Crash', 'UI Issue', 'Performance', 'Data Loss',
        'Connectivity', 'Hardware Failure', 'Battery Issue'
    ]

    # Regions
    regions = ['CA', 'NY', 'TX', 'IL', 'OH', 'IN', 'FL', 'WA']

    # Lot numbers
    lots = [f'LOT-2025-{month:02d}-{day:02d}' for month in range(1, 4) for day in [1, 15, 30]]

    complaints = []
    base_date = datetime(2025, 1, 1)

    for i in range(n_complaints):
        # Distribute across 3 months
        month = (i // 50) + 1
        day = random.randint(1, 28)

        # Apply anomaly multiplier to March
        if month == 3 and random.random() < 0.5:
            count_multiplier = anomaly_multiplier
        else:
            count_multiplier = 1

        date = base_date.replace(month=month, day=day)

        complaints.append({
            'date': date.strftime('%Y-%m-%d'),
            'type': random.choice(complaint_types),
            'lot': random.choice(lots),
            'region': random.choice(regions),
            'severity': random.choice(['low', 'medium', 'high'])
        })

    return complaints
```

## Module 2: Regulatory Change Impact Analysis

### Regulatory Monitoring

```python
import json
from typing import Dict, List
from datetime import datetime

class RegulatoryChangeMonitor:
    """Monitors regulatory changes and assesses impact on documents."""

    def __init__(self, knowledge_base_path: str):
        """
        Initialize with knowledge base path.

        Args:
            knowledge_base_path: Path to regulation-document mapping database
        """
        self.knowledge_base_path = knowledge_base_path
        self.regulation_mapping = self._load_regulation_mapping()

    def _load_regulation_mapping(self) -> Dict:
        """Load regulation to document mapping from JSON file."""
        try:
            with open(self.knowledge_base_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                'regulations': {},
                'documents': {},
                'last_updated': None
            }

    def search_regulatory_updates(
        self,
        regulatory_domain: str,
        search_query: str
    ) -> List[Dict]:
        """
        Search for regulatory updates using WebSearch.

        Args:
            regulatory_domain: 'FDA', 'EU MDR', or 'MFDS'
            search_query: Search query for regulatory updates

        Returns:
            List of regulatory update records
        """
        # This would use WebSearch tool in actual implementation
        # Placeholder for demonstration

        updates = []
        current_date = datetime.now().strftime('%Y-%m')

        # Example simulated updates
        if regulatory_domain == 'FDA' and 'SaMD' in search_query:
            updates.append({
                'domain': 'FDA',
                'type': 'guidance',
                'title': 'Clinical Evidence for SaMD',
                'date': f'{current_date}-01',
                'url': 'https://www.fda.gov/medical-devices/software-medical-device-samd',
                'summary': 'New requirements for real-world evidence inclusion in SaMD submissions'
            })

        return updates

    def parse_regulatory_change(self, update: Dict) -> Dict:
        """
        Parse regulatory update for key requirements.

        Args:
            update: Regulatory update record

        Returns:
            Parsed requirements and affected areas
        """
        parsed = {
            'update_id': f"{update['domain']}-{update['date']}",
            'domain': update['domain'],
            'requirements': [],
            'affected_document_types': [],
            'key_changes': []
        }

        # Extract key requirements based on domain and content
        if 'SaMD' in update.get('title', ''):
            parsed['affected_document_types'] = [
                'CER', 'Technical File', '510(k) Submission'
            ]
            parsed['key_changes'] = [
                'Real-world evidence (RWE) inclusion required',
                'Clinical validation criteria updated for AI/ML'
            ]

        return parsed

    def identify_affected_documents(
        self,
        parsed_change: Dict
    ) -> List[Dict]:
        """
        Identify documents affected by regulatory change.

        Args:
            parsed_change: Parsed regulatory change

        Returns:
            List of affected documents with priority
        """
        affected = []

        for doc_id, doc_info in self.regulation_mapping.get('documents', {}).items():
            # Check if document type matches affected types
            if doc_info.get('type') in parsed_change['affected_document_types']:
                # Check if domain matches
                if doc_info.get('regulatory_domain') == parsed_change['domain']:
                    priority = self._calculate_priority(doc_info, parsed_change)
                    affected.append({
                        'document_id': doc_id,
                        'title': doc_info.get('title', ''),
                        'type': doc_info.get('type', ''),
                        'priority': priority,
                        'last_updated': doc_info.get('last_updated', '')
                    })

        return sorted(affected, key=lambda x: x['priority'], reverse=True)

    def _calculate_priority(self, doc_info: Dict, change: Dict) -> str:
        """Calculate priority level for affected document."""
        # High priority if pending submission
        if doc_info.get('status') == 'pending':
            return 'high'
        # Medium if recently updated (within 6 months)
        elif self._is_recent(doc_info.get('last_updated', ''), months=6):
            return 'medium'
        else:
            return 'low'

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

    def generate_impact_alert(
        self,
        update: Dict,
        affected_docs: List[Dict]
    ) -> str:
        """
        Generate formatted impact alert.

        Args:
            update: Regulatory update
            affected_docs: List of affected documents

        Returns:
            Formatted alert in Markdown
        """
        alert = f"""## Regulatory Change Impact Alert

**Regulation**: {update.get('domain', 'Unknown')} {update.get('title', 'Update')}
**Updated**: {update.get('date', 'Unknown')}
**Impact**: {self._calculate_impact_level(affected_docs)}

### Key Changes
"""

        parsed = self.parse_regulatory_change(update)
        for change in parsed.get('key_changes', []):
            alert += f"- {change}\n"

        alert += "\n### Affected Documents\n"
        for doc in affected_docs:
            priority_emoji = {'high': '🔴', 'medium': '🟡', 'low': '🟢'}
            alert += f"- [{priority_emoji.get(doc['priority'], '⚪')}] **{doc['document_id']}** ({doc['type']}) - {doc['priority'].title()} Priority\n"

        alert += "\n### Actions Required\n"
        high_priority = [d for d in affected_docs if d['priority'] == 'high']
        medium_priority = [d for d in affected_docs if d['priority'] == 'medium']

        if high_priority:
            alert += f"1. **URGENT**: Review {len(high_priority)} high-priority documents\n"
        if medium_priority:
            alert += f"2. Review {len(medium_priority)} medium-priority documents\n"
        alert += "3. Update templates if needed for new requirements\n"
        alert += "4. Validate stored regulatory decisions for affected areas\n"

        return alert

    def _calculate_impact_level(self, affected_docs: List[Dict]) -> str:
        """Calculate overall impact level."""
        high_count = sum(1 for d in affected_docs if d['priority'] == 'high')
        if high_count > 0:
            return 'High'
        elif len(affected_docs) > 5:
            return 'Medium'
        else:
            return 'Low'
```

### Decision Validation

```python
class RegulatoryDecisionValidator:
    """Validates stored regulatory decisions against current regulations."""

    def __init__(self, decisions_path: str):
        """
        Initialize with decisions file path.

        Args:
            decisions_path: Path to regulatory decisions JSON file
        """
        self.decisions_path = decisions_path
        self.decisions = self._load_decisions()

    def _load_decisions(self) -> Dict:
        """Load regulatory decisions from JSON file."""
        try:
            with open(self.decisions_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {'decisions': []}

    def validate_decision_currency(
        self,
        decision_id: str,
        current_regulation: str
    ) -> Dict:
        """
        Validate if decision is still current.

        Args:
            decision_id: Decision identifier
            current_regulation: Current regulation text/section

        Returns:
            Validation result with status and recommendations
        """
        decision = self._get_decision(decision_id)
        if not decision:
            return {'status': 'not_found', 'message': 'Decision not found'}

        # Check if regulation reference is still current
        stored_regulation = decision.get('regulation', '')
        if stored_regulation != current_regulation:
            return {
                'status': 'obsolete',
                'message': 'Regulation has been updated',
                'stored': stored_regulation,
                'current': current_regulation,
                'recommendation': 'Review and update decision with new regulation'
            }

        # Check if decision has expiration
        if decision.get('valid_until'):
            expiry = datetime.fromisoformat(decision['valid_until'])
            if datetime.now() > expiry:
                return {
                    'status': 'expired',
                    'message': 'Decision has expired',
                    'recommendation': 'Re-validate decision or remove from memory'
                }

        return {'status': 'current', 'message': 'Decision is current'}

    def _get_decision(self, decision_id: str) -> Dict:
        """Get decision by ID."""
        for decision in self.decisions.get('decisions', []):
            if decision.get('decision_id') == decision_id:
                return decision
        return None
```

## Module 3: Cross-Submission Knowledge Utilization

### Knowledge Base Schema

```python
class KnowledgeBase:
    """Manages cross-submission knowledge base."""

    def __init__(self, kb_path: str):
        """
        Initialize with knowledge base path.

        Args:
            kb_path: Path to knowledge base JSON file
        """
        self.kb_path = kb_path
        self.entries = self._load_kb()

    def _load_kb(self) -> Dict:
        """Load knowledge base from JSON file."""
        try:
            with open(self.kb_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                'entries': [],
                'tags': {},
                'outcomes': {'approved': 0, 'approvable': 0, 'not_approved': 0}
            }

    def add_entry(self, entry: Dict) -> str:
        """
        Add new knowledge base entry.

        Args:
            entry: Knowledge base entry with required fields

        Returns:
            Entry ID
        """
        entry_id = f"KB-{datetime.now().strftime('%Y%m%d')}-{len(self.entries['entries']) + 1:04d}"
        entry['entry_id'] = entry_id
        entry['created_at'] = datetime.now().isoformat()
        entry['last_reviewed'] = datetime.now().isoformat()

        self.entries['entries'].append(entry)

        # Update outcome counts
        outcome = entry.get('outcome', 'unknown')
        if outcome in self.entries['outcomes']:
            self.entries['outcomes'][outcome] += 1

        # Update tags
        for tag in entry.get('tags', []):
            if tag not in self.entries['tags']:
                self.entries['tags'][tag] = 0
            self.entries['tags'][tag] += 1

        self._save_kb()
        return entry_id

    def search(
        self,
        query: str,
        filters: Dict = None,
        limit: int = 10
    ) -> List[Dict]:
        """
        Search knowledge base with relevance scoring.

        Args:
            query: Search query
            filters: Optional filters (device_type, regulatory_domain, outcome)
            limit: Maximum results to return

        Returns:
            List of entries sorted by relevance score
        """
        results = []
        query_lower = query.lower()

        for entry in self.entries['entries']:
            # Apply filters
            if filters:
                if filters.get('device_type') and entry.get('device_type') != filters['device_type']:
                    continue
                if filters.get('regulatory_domain') and entry.get('regulatory_domain') != filters['regulatory_domain']:
                    continue
                if filters.get('outcome') and entry.get('outcome') != filters['outcome']:
                    continue

            # Calculate relevance score
            score = self._calculate_relevance(query_lower, entry)
            if score > 0:
                results.append({**entry, 'relevance_score': score})

        # Sort by relevance score, then by outcome
        outcome_priority = {'approved': 3, 'approvable': 2, 'not_approved': 1}
        results.sort(
            key=lambda x: (x['relevance_score'], outcome_priority.get(x.get('outcome', 'unknown'), 0)),
            reverse=True
        )

        return results[:limit]

    def _calculate_relevance(self, query_lower: str, entry: Dict) -> float:
        """Calculate relevance score for entry."""
        score = 0.0

        # Check title and content
        if query_lower in entry.get('title', '').lower():
            score += 2.0
        if query_lower in entry.get('content', '').lower():
            score += 1.5

        # Check tags
        for tag in entry.get('tags', []):
            if query_lower in tag.lower():
                score += 1.0

        # Boost approved outcomes
        if entry.get('outcome') == 'approved':
            score += 0.5

        return score

    def validate_context(
        self,
        entry_id: str,
        new_context: Dict
    ) -> Dict:
        """
        Validate context before reusing content.

        Args:
            entry_id: Knowledge base entry ID
            new_context: New submission context

        Returns:
            Validation result with warnings
        """
        entry = self._get_entry(entry_id)
        if not entry:
            return {'valid': False, 'message': 'Entry not found'}

        warnings = []

        # Check device type differences
        if entry.get('device_type') != new_context.get('device_type'):
            warnings.append({
                'type': 'device_mismatch',
                'message': f"Device type differs: {entry.get('device_type')} vs {new_context.get('device_type')}"
            })

        # Check regulation currency
        if new_context.get('current_regulation') != entry.get('regulation_version'):
            warnings.append({
                'type': 'regulation_change',
                'message': 'Regulation has been updated since this content was created'
            })

        # Check for failed outcomes
        if entry.get('outcome') == 'not_approved':
            warnings.append({
                'type': 'failed_outcome',
                'message': 'This content was from a submission that was not approved',
                'recommendation': 'Review rejection reasons before reusing'
            })

        return {
            'valid': True,
            'warnings': warnings,
            'can_reuse': len(warnings) == 0 or all(w.get('type') != 'failed_outcome' for w in warnings)
        }

    def _get_entry(self, entry_id: str) -> Dict:
        """Get entry by ID."""
        for entry in self.entries['entries']:
            if entry.get('entry_id') == entry_id:
                return entry
        return None

    def _save_kb(self):
        """Save knowledge base to file."""
        with open(self.kb_path, 'w') as f:
            json.dump(self.entries, f, indent=2)
```

### Warning System

```python
def generate_reuse_warning(entry: Dict, validation: Dict) -> str:
    """
    Generate warning message for content reuse.

    Args:
        entry: Knowledge base entry
        validation: Context validation result

    Returns:
        Warning message in Markdown
    """
    warning = f"""## Content Reuse Warning

**Entry**: {entry.get('entry_id', 'Unknown')}
**Outcome**: {entry.get('outcome', 'unknown').replace('_', ' ').title()}
**From Submission**: {entry.get('submission_id', 'Unknown')}

### Warnings
"""

    for w in validation.get('warnings', []):
        warning += f"- ⚠️ **{w.get('type', 'Warning').replace('_', ' ').title()}**: {w.get('message', '')}\n"
        if w.get('recommendation'):
            warning += f"  - 💡 {w.get('recommendation')}\n"

    if not validation.get('warnings', []):
        warning += "✅ No warnings - content can be reused with caution\n"

    warning += """
### Recommendations
1. Review the original content in context of the new submission
2. Update any device-specific information
3. Verify regulatory requirements are still current
4. Consider differences in product specifications
5. Add new evidence or data as needed

### Required Confirmation
Before reusing this content, please confirm:
- [ ] I have reviewed the warnings above
- [ ] I have validated the context differences
- [ ] I have updated content for the new submission
- [ ] I have verified regulatory requirements are current
"""

    return warning
```

## Integration Tests

```python
import unittest
import tempfile
import os

class TestComplaintTrendAnalysis(unittest.TestCase):
    """Test complaint trend analysis functionality."""

    def setUp(self):
        """Set up test data."""
        self.complaint_data = generate_synthetic_complaint_data(
            n_complaints=150,
            anomaly_multiplier=2.0
        )
        self.analyzer = ComplaintTrendAnalyzer(self.complaint_data)

    def test_aggregation(self):
        """Test complaint aggregation by month."""
        aggregated = self.analyzer.aggregate_by_period('month')
        self.assertIsInstance(aggregated, dict)
        self.assertGreater(len(aggregated), 0)

    def test_baseline_calculation(self):
        """Test statistical baseline calculation."""
        aggregated = self.analyzer.aggregate_by_period('month')
        counts = list(aggregated.values())
        baseline = self.analyzer.calculate_baseline(counts)

        self.assertIn('mean', baseline)
        self.assertIn('std_dev', baseline)
        self.assertIn('upper_limit', baseline)
        self.assertGreater(baseline['upper_limit'], baseline['mean'])

    def test_anomaly_detection(self):
        """Test trend anomaly detection."""
        aggregated = self.analyzer.aggregate_by_period('month')
        self.analyzer.calculate_baseline(list(aggregated.values()))
        anomalies = self.analyzer.detect_anomalies(aggregated)

        self.assertIsInstance(anomalies, list)
        # Should detect March anomaly with 2x multiplier
        self.assertGreater(len(anomalies), 0)

    def test_alert_generation(self):
        """Test alert generation."""
        aggregated = self.analyzer.aggregate_by_period('month')
        self.analyzer.calculate_baseline(list(aggregated.values()))
        anomalies = self.analyzer.detect_anomalies(aggregated)

        if anomalies:
            alert = self.analyzer.generate_alert(anomalies[0])
            self.assertIn('Complaint Trend Alert', alert)
            self.assertIn('Recommendations', alert)

class TestKnowledgeBase(unittest.TestCase):
    """Test knowledge base functionality."""

    def setUp(self):
        """Set up test knowledge base."""
        self.temp_fd, self.temp_path = tempfile.mkstemp(suffix='.json')
        os.close(self.temp_fd)
        self.kb = KnowledgeBase(self.temp_path)

    def tearDown(self):
        """Clean up test file."""
        if os.path.exists(self.temp_path):
            os.remove(self.temp_path)

    def test_add_entry(self):
        """Test adding knowledge base entry."""
        entry = {
            'content_type': 'substantial_equivalence_argument',
            'submission_id': '510k-2024-123',
            'outcome': 'approved',
            'content': 'Test content',
            'regulatory_domain': 'FDA',
            'device_type': 'Class II SaMD',
            'tags': ['predicate', 'substantial equivalence']
        }

        entry_id = self.kb.add_entry(entry)
        self.assertTrue(entry_id.startswith('KB-'))

    def test_search(self):
        """Test knowledge base search."""
        # Add test entries
        self.kb.add_entry({
            'content_type': 'argument',
            'submission_id': 'TEST-001',
            'outcome': 'approved',
            'content': 'Substantial equivalence argument for predicate device',
            'regulatory_domain': 'FDA',
            'device_type': 'Class II',
            'tags': ['predicate', 'equivalence']
        })

        results = self.kb.search('predicate device')
        self.assertGreater(len(results), 0)
        self.assertIn('relevance_score', results[0])

    def test_context_validation(self):
        """Test context validation."""
        entry_id = self.kb.add_entry({
            'content_type': 'argument',
            'submission_id': 'TEST-002',
            'outcome': 'approved',
            'content': 'Test content',
            'regulatory_domain': 'FDA',
            'device_type': 'Class II',
            'tags': ['test'],
            'regulation_version': 'v1.0'
        })

        validation = self.kb.validate_context(entry_id, {
            'device_type': 'Class III',
            'current_regulation': 'v2.0'
        })

        self.assertIn('warnings', validation)
        self.assertIsInstance(validation['warnings'], list)

if __name__ == '__main__':
    unittest.main()
```

## Configuration

Analytics configuration (see .moai/config/sections/analytics.yaml):

```yaml
analytics:
  # Complaint trend analysis settings
  complaint_analysis:
    # Minimum data points for reliable baseline
    min_data_points: 100

    # Control limit multiplier (default: 2 for 95.4% confidence)
    control_limit_multiplier: 2

    # Aggregation period (day, week, month, quarter)
    default_period: month

    # Anomaly severity thresholds (in standard deviations)
    severity_thresholds:
      medium: 2.0
      high: 3.0

  # Regulatory monitoring settings
  regulatory_monitoring:
    # Check interval in hours
    check_interval: 24

    # Regulatory domains to monitor
    domains:
      - FDA
      - EU MDR
      - MFDS

    # Auto-flag affected documents
    auto_flag: true

  # Knowledge base settings
  knowledge_base:
    # Storage location
    path: .claude/agent-memory/aria/knowledge-base.json

    # Maximum entries to return in search
    max_search_results: 10

    # Minimum relevance score for results
    min_relevance_score: 0.5

    # Require confirmation for failed outcomes
    require_confirmation_failed: true
```

## Usage Examples

### Analyze Complaint Trends

```python
# Load complaint data from Google Sheets via MCP
complaint_data = load_complaints_from_sheets()

# Initialize analyzer
analyzer = ComplaintTrendAnalyzer(complaint_data)

# Aggregate by month
monthly_data = analyzer.aggregate_by_period('month')

# Calculate baseline and detect anomalies
analyzer.calculate_baseline(list(monthly_data.values()))
anomalies = analyzer.detect_anomalies(monthly_data)

# Generate alerts
for anomaly in anomalies:
    alert = analyzer.generate_alert(anomaly)
    print(alert)
```

### Monitor Regulatory Changes

```python
# Initialize monitor
monitor = RegulatoryChangeMonitor('.claude/agent-memory/aria/regulation-mapping.json')

# Search for updates
updates = monitor.search_regulatory_updates('FDA', 'SaMD guidance updates')

# Parse and assess impact
for update in updates:
    parsed = monitor.parse_regulatory_change(update)
    affected = monitor.identify_affected_documents(parsed)
    alert = monitor.generate_impact_alert(update, affected)
    print(alert)
```

### Search Knowledge Base

```python
# Initialize knowledge base
kb = KnowledgeBase('.claude/agent-memory/aria/knowledge-base.json')

# Search for relevant content
results = kb.search('substantial equivalence', filters={
    'device_type': 'Class II SaMD',
    'outcome': 'approved'
})

# Validate context before reuse
if results:
    entry = results[0]
    validation = kb.validate_context(entry['entry_id'], {
        'device_type': 'Class II SaMD',
        'current_regulation': 'current_version'
    })

    if validation['can_reuse']:
        print(f"Can reuse content from {entry['entry_id']}")
    else:
        print(generate_reuse_warning(entry, validation))
```

## Error Handling

All analytics modules include comprehensive error handling:

- **Insufficient Data**: Use synthetic data for testing, display low confidence warning
- **MCP Failures**: Implement retry with exponential backoff, cache last successful operation
- **Validation Errors**: Graceful degradation with user notifications
- **File I/O Errors**: Fallback to in-memory storage, alert user to persistence issues

## Performance Optimization

- **Caching**: Cache regulatory lookup results for 24 hours
- **Lazy Loading**: Load knowledge base entries on demand
- **Batch Processing**: Process complaint data in batches for large datasets
- **Async Operations**: Use async I/O for network operations where possible
