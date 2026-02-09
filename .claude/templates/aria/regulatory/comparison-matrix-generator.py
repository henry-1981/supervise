#!/usr/bin/env python3
"""
Regulatory Comparison Matrix Generator for ARIA
Generates side-by-side requirement comparisons across multiple markets
"""

import json
from typing import Dict, List, Any
from datetime import datetime


class RegulatoryComparisonGenerator:
    """Generate regulatory comparison matrices across markets"""

    def __init__(self, database_path: str):
        """Initialize with regulatory database"""
        self.database = self._load_database(database_path)

    def _load_database(self, path: str) -> Dict:
        """Load regulatory database from JSON file"""
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def generate_comparison_matrix(
        self,
        device_class: str,
        target_markets: List[str],
        include_special_programs: bool = True
    ) -> Dict[str, Any]:
        """
        Generate comparison matrix for specified device class across target markets

        Args:
            device_class: Device classification (e.g., "Class II", "Class III")
            target_markets: List of market codes (e.g., ["FDA", "EU_MDR", "MFDS"])
            include_special_programs: Include expedited programs

        Returns:
            Comparison matrix with requirements, timelines, and conflicts
        """
        matrix = {
            "generated_at": datetime.now().isoformat(),
            "device_class": device_class,
            "markets": target_markets,
            "requirements_comparison": {},
            "timeline_comparison": {},
            "missing_requirements": {},
            "conflicts": [],
            "harmonization_strategies": []
        }

        # Extract requirements for each market
        for market in target_markets:
            if market in self.database["markets"]:
                market_data = self.database["markets"][market]
                market_class = self._find_matching_class(market_data, device_class)

                if market_class:
                    matrix["requirements_comparison"][market] = {
                        "risk_level": market_class.get("risk_level", "N/A"),
                        "requirements": market_class.get("requirements", []),
                        "submission_required": market_class.get("submission_required", False),
                        "timeline_months": market_class.get("typical_timeline_months", 0),
                        "notified_body_required": market_class.get("notified_body_required", False),
                        "clinical_evaluation_required": market_class.get("clinical_evaluation_required", False)
                    }

                    if include_special_programs and "special_programs" in market_data:
                        matrix["requirements_comparison"][market]["special_programs"] = (
                            market_data["special_programs"]
                        )

        # Identify missing requirements
        matrix["missing_requirements"] = self._identify_missing_requirements(
            matrix["requirements_comparison"]
        )

        # Detect conflicts
        matrix["conflicts"] = self._detect_conflicts(
            matrix["requirements_comparison"],
            target_markets
        )

        # Suggest harmonization strategies
        matrix["harmonization_strategies"] = self._suggest_harmonization(
            matrix["conflicts"]
        )

        return matrix

    def _find_matching_class(self, market_data: Dict, device_class: str) -> Dict:
        """Find matching device class in market data"""
        classifications = market_data.get("device_classifications", {})

        # Direct match
        if device_class in classifications:
            return classifications[device_class]

        # Fuzzy match for class variations
        class_key = device_class.replace(" ", "").lower()
        for key, value in classifications.items():
            if key.replace(" ", "").lower() == class_key:
                return value

        return None

    def _identify_missing_requirements(
        self,
        requirements_comparison: Dict[str, Dict]
    ) -> Dict[str, List[str]]:
        """Identify requirements missing in specific markets"""

        # Collect all unique requirements
        all_requirements = set()
        for market, data in requirements_comparison.items():
            all_requirements.update(data.get("requirements", []))

        # Find missing requirements per market
        missing = {}
        for market, data in requirements_comparison.items():
            market_requirements = set(data.get("requirements", []))
            missing_in_market = all_requirements - market_requirements

            if missing_in_market:
                missing[market] = list(missing_in_market)

        return missing

    def _detect_conflicts(
        self,
        requirements_comparison: Dict[str, Dict],
        target_markets: List[str]
    ) -> List[Dict[str, Any]]:
        """Detect regulatory conflicts between markets"""

        conflicts = []

        # Check for notified body requirement conflicts
        markets_requiring_nb = [
            m for m, data in requirements_comparison.items()
            if data.get("notified_body_required", False)
        ]

        if len(markets_requiring_nb) > 0 and len(markets_requiring_nb) < len(target_markets):
            conflicts.append({
                "type": "Notified Body Availability",
                "severity": "HIGH",
                "affected_markets": markets_requiring_nb,
                "description": "Notified Body certification required with limited capacity",
                "impact": "Extended timeline for Notified Body engagement"
            })

        # Check for clinical evaluation conflicts
        clinical_requirements = {
            m: data.get("clinical_evaluation_required", False)
            for m, data in requirements_comparison.items()
        }

        if any(clinical_requirements.values()) and not all(clinical_requirements.values()):
            conflicts.append({
                "type": "Clinical Evidence Requirements",
                "severity": "MEDIUM",
                "affected_markets": [m for m, req in clinical_requirements.items() if req],
                "description": "Differing clinical evidence requirements",
                "impact": "May need comprehensive CER for EU, less for FDA"
            })

        # Check for timeline conflicts
        timelines = {
            m: data.get("timeline_months", 0)
            for m, data in requirements_comparison.items()
        }

        if timelines:
            max_timeline = max(timelines.values())
            min_timeline = min(timelines.values())

            if max_timeline > min_timeline * 2:
                conflicts.append({
                    "type": "Timeline Disparity",
                    "severity": "MEDIUM",
                    "affected_markets": [
                        m for m, t in timelines.items() if t == max_timeline
                    ],
                    "description": f"Significant timeline difference: {min_timeline} vs {max_timeline} months",
                    "impact": "Consider staggered submission strategy"
                })

        # Add known conflicts from database
        for known_conflict in self.database.get("common_conflicts", []):
            if any(m in target_markets for m in known_conflict.get("affected_markets", [])):
                conflicts.append({
                    "type": known_conflict.get("conflict_type"),
                    "severity": "MEDIUM",
                    "affected_markets": known_conflict.get("affected_markets", []),
                    "description": known_conflict.get("description", ""),
                    "impact": known_conflict.get("harmonization_strategy", "")
                })

        return conflicts

    def _suggest_harmonization(
        self,
        conflicts: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Suggest harmonization strategies for identified conflicts"""

        strategies = []

        for conflict in conflicts:
            conflict_type = conflict.get("type", "Unknown")

            if "Clinical Evidence" in conflict_type:
                strategies.append({
                    "conflict": conflict_type,
                    "strategy": "Generate comprehensive clinical evaluation report (CER) per MEDDEV 2.7.1 rev 4",
                    "actions": [
                        "Create detailed CER with literature search",
                        "Extract relevant portions for FDA 510(k)",
                        "Maintain traceability matrix for clinical evidence"
                    ],
                    "benefit": "Single comprehensive document serves multiple markets",
                    "effort": "HIGH - requires clinical expertise"
                })

            elif "Notified Body" in conflict_type:
                strategies.append({
                    "conflict": conflict_type,
                    "strategy": "Early Notified Body engagement",
                    "actions": [
                        "Engage Notified Body 12-18 months before submission",
                        "Parallel FDA submission while awaiting EU MDR approval",
                        "Consider multiple Notified Body options"
                    ],
                    "benefit": "Reduces EU MDR timeline through parallel processing",
                    "effort": "MEDIUM - requires planning and coordination"
                })

            elif "Timeline" in conflict_type:
                strategies.append({
                    "conflict": conflict_type,
                    "strategy": "Staggered submission approach",
                    "actions": [
                        "Submit to fast-track markets first (FDA Class II)",
                        "Use early approval to support other market submissions",
                        "Plan resource allocation based on timeline"
                    ],
                    "benefit": "Optimizes resource utilization and cash flow",
                    "effort": "LOW - requires planning"
                })

        return strategies

    def generate_markdown_report(self, matrix: Dict[str, Any]) -> str:
        """Generate formatted Markdown report from comparison matrix"""

        md = []
        md.append(f"# Regulatory Comparison Matrix")
        md.append(f"**Generated:** {matrix['generated_at']}")
        md.append(f"**Device Class:** {matrix['device_class']}")
        md.append(f"**Markets:** {', '.join(matrix['markets'])}")
        md.append("")

        # Requirements Comparison Table
        md.append("## Requirements Comparison")
        md.append("")
        md.append("| Market | Risk Level | Submission Required | Notified Body | Clinical | Timeline |")
        md.append("|--------|------------|---------------------|---------------|----------|----------|")

        for market, data in matrix["requirements_comparison"].items():
            md.append(
                f"| {market} | {data['risk_level']} | "
                f"{'Yes' if data['submission_required'] else 'No'} | "
                f"{'Yes' if data.get('notified_body_required', False) else 'No'} | "
                f"{'Yes' if data.get('clinical_evaluation_required', False) else 'No'} | "
                f"{data['timeline_months']} months |"
            )

        md.append("")

        # Detailed Requirements
        md.append("## Detailed Requirements by Market")
        md.append("")

        for market, data in matrix["requirements_comparison"].items():
            md.append(f"### {market}")
            md.append("")
            for req in data.get("requirements", []):
                md.append(f"- {req}")
            md.append("")

        # Missing Requirements
        if matrix["missing_requirements"]:
            md.append("## Missing Requirements")
            md.append("")
            for market, missing in matrix["missing_requirements"].items():
                md.append(f"### {market}")
                for req in missing:
                    md.append(f"- {req}")
                md.append("")

        # Conflicts
        if matrix["conflicts"]:
            md.append("## Identified Conflicts")
            md.append("")
            for conflict in matrix["conflicts"]:
                md.append(f"### {conflict['type']} ({conflict['severity']})")
                md.append(f"**Affected Markets:** {', '.join(conflict['affected_markets'])}")
                md.append(f"**Description:** {conflict['description']}")
                md.append(f"**Impact:** {conflict['impact']}")
                md.append("")

        # Harmonization Strategies
        if matrix["harmonization_strategies"]:
            md.append("## Harmonization Strategies")
            md.append("")
            for strategy in matrix["harmonization_strategies"]:
                md.append(f"### For: {strategy['conflict']}")
                md.append(f"**Strategy:** {strategy['strategy']}")
                md.append("**Actions:**")
                for action in strategy['actions']:
                    md.append(f"- {action}")
                md.append(f"**Benefit:** {strategy['benefit']}")
                md.append(f"**Effort:** {strategy['effort']}")
                md.append("")

        # Disclaimer
        md.append("---")
        md.append("*Disclaimer: This comparison is for informational purposes only. Always verify requirements with official regulatory sources.*")

        return "\n".join(md)


def main():
    """Example usage"""
    generator = RegulatoryComparisonGenerator(
        "/Users/hb/.moai/worktrees/Agent-Skills/SPEC-ARIA-005/.claude/templates/aria/regulatory/regulatory-database-schema.json"
    )

    # Generate comparison for Class II devices
    matrix = generator.generate_comparison_matrix(
        device_class="Class II",
        target_markets=["FDA", "EU_MDR", "MFDS", "PMDA"],
        include_special_programs=True
    )

    # Print Markdown report
    report = generator.generate_markdown_report(matrix)
    print(report)

    # Save to file
    with open("/Users/hb/.moai/worktrees/Agent-Skills/SPEC-ARIA-005/.claude/templates/aria/regulatory/comparison-matrix-example.md", "w") as f:
        f.write(report)


if __name__ == "__main__":
    main()
