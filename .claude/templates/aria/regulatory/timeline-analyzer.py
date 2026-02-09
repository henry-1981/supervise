#!/usr/bin/env python3
"""
Regulatory Timeline Analyzer for ARIA
Analyzes approval timelines and suggests optimal submission sequencing
"""

import json
from typing import Dict, List, Any, Tuple
from datetime import datetime, timedelta
from collections import defaultdict


class TimelineAnalyzer:
    """Analyze regulatory approval timelines and suggest sequencing strategies"""

    def __init__(self, database_path: str):
        """Initialize with regulatory database"""
        self.database = self._load_database(database_path)

    def _load_database(self, path: str) -> Dict:
        """Load regulatory database from JSON file"""
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def analyze_submission_sequencing(
        self,
        device_class: str,
        target_markets: List[str],
        submission_start_date: str = None,
        available_resources: str = "medium"
    ) -> Dict[str, Any]:
        """
        Analyze optimal submission sequencing strategy

        Args:
            device_class: Device classification
            target_markets: Target markets for submission
            submission_start_date: Start date for submissions (ISO format)
            available_resources: low, medium, high (affects parallel capacity)

        Returns:
            Timeline analysis with recommended sequencing
        """
        if submission_start_date is None:
            submission_start_date = datetime.now()
        else:
            submission_start_date = datetime.fromisoformat(submission_start_date)

        # Extract timeline data for each market
        market_timelines = {}
        for market in target_markets:
            if market in self.database["markets"]:
                market_data = self.database["markets"][market]
                class_data = self._find_matching_class(market_data, device_class)

                if class_data:
                    market_timelines[market] = {
                        "name": market_data["name"],
                        "region": market_data["region"],
                        "timeline_months": class_data.get("typical_timeline_months", 0),
                        "submission_required": class_data.get("submission_required", False),
                        "notified_body_required": class_data.get("notified_body_required", False),
                        "special_programs": market_data.get("special_programs", {})
                    }

        # Analyze sequencing strategies
        analysis = {
            "analyzed_at": datetime.now().isoformat(),
            "device_class": device_class,
            "target_markets": target_markets,
            "market_timelines": market_timelines,
            "sequencing_strategies": {},
            "recommended_strategy": None,
            "timeline_projection": {},
            "resource_allocation": {}
        }

        # Generate different sequencing strategies
        analysis["sequencing_strategies"]["parallel"] = self._calculate_parallel_timeline(
            market_timelines, submission_start_date, available_resources
        )

        analysis["sequencing_strategies"]["sequential"] = self._calculate_sequential_timeline(
            market_timelines, submission_start_date
        )

        analysis["sequencing_strategies"]["hybrid"] = self._calculate_hybrid_timeline(
            market_timelines, submission_start_date, available_resources
        )

        # Recommend best strategy
        analysis["recommended_strategy"] = self._recommend_strategy(
            analysis["sequencing_strategies"],
            available_resources
        )

        # Generate timeline projection
        analysis["timeline_projection"] = self._generate_timeline_projection(
            market_timelines,
            analysis["recommended_strategy"]["strategy_name"],
            submission_start_date
        )

        # Resource allocation recommendations
        analysis["resource_allocation"] = self._suggest_resource_allocation(
            market_timelines,
            analysis["recommended_strategy"]["strategy_name"]
        )

        return analysis

    def _find_matching_class(self, market_data: Dict, device_class: str) -> Dict:
        """Find matching device class in market data"""
        classifications = market_data.get("device_classifications", {})

        if device_class in classifications:
            return classifications[device_class]

        class_key = device_class.replace(" ", "").lower()
        for key, value in classifications.items():
            if key.replace(" ", "").lower() == class_key:
                return value

        return None

    def _calculate_parallel_timeline(
        self,
        market_timelines: Dict[str, Dict],
        start_date: datetime,
        resources: str
    ) -> Dict[str, Any]:
        """Calculate timeline for parallel submission strategy"""

        # Parallel timeline is determined by the longest timeline
        max_timeline = max(
            data["timeline_months"] for data in market_timelines.values()
        )

        # Adjust for resource constraints
        resource_multiplier = {
            "low": 1.5,
            "medium": 1.0,
            "high": 0.8
        }

        adjusted_timeline = max_timeline * resource_multiplier.get(resources, 1.0)

        # Calculate completion date
        completion_date = start_date + timedelta(days=adjusted_timeline * 30)

        return {
            "strategy": "parallel",
            "total_duration_months": adjusted_timeline,
            "start_date": start_date.isoformat(),
            "end_date": completion_date.isoformat(),
            "concurrent_submissions": len(market_timelines),
            "resource_intensity": "HIGH" if resources == "high" else "MEDIUM" if resources == "medium" else "LOW",
            "pros": [
                "Fastest overall time to market",
                "All markets approved in similar timeframe",
                "Leverages early approval for other markets"
            ],
            "cons": [
                "High resource requirement",
                "Complex coordination",
                "Cash flow impact from multiple fees"
            ],
            "market_completion_dates": {
                market: (
                    start_date + timedelta(days=data["timeline_months"] * 30)
                ).isoformat()
                for market, data in market_timelines.items()
            }
        }

    def _calculate_sequential_timeline(
        self,
        market_timelines: Dict[str, Dict],
        start_date: datetime
    ) -> Dict[str, Any]:
        """Calculate timeline for sequential submission strategy"""

        # Sort by timeline (fastest first)
        sorted_markets = sorted(
            market_timelines.items(),
            key=lambda x: x[1]["timeline_months"]
        )

        total_timeline = 0
        market_completion_dates = {}
        current_date = start_date

        for market, data in sorted_markets:
            timeline_months = data["timeline_months"]
            completion_date = current_date + timedelta(days=timeline_months * 30)

            market_completion_dates[market] = completion_date.isoformat()
            total_timeline += timeline_months
            current_date = completion_date

        return {
            "strategy": "sequential",
            "total_duration_months": total_timeline,
            "start_date": start_date.isoformat(),
            "end_date": current_date.isoformat(),
            "submission_order": [m for m, d in sorted_markets],
            "concurrent_submissions": 1,
            "resource_intensity": "LOW",
            "pros": [
                "Low resource requirement",
                "Learn from each submission",
                "Use early approvals for subsequent markets"
            ],
            "cons": [
                "Longest overall time to all markets",
                "Late market entry for slower markets",
                "Missed early revenue opportunities"
            ],
            "market_completion_dates": market_completion_dates
        }

    def _calculate_hybrid_timeline(
        self,
        market_timelines: Dict[str, Dict],
        start_date: datetime,
        resources: str
    ) -> Dict[str, Any]:
        """Calculate timeline for hybrid (parallel + sequential) strategy"""

        # Group markets by timeline similarity
        fast_track = []
        medium_track = []
        slow_track = []

        for market, data in market_timelines.items():
            timeline = data["timeline_months"]

            if timeline <= 4:
                fast_track.append((market, data))
            elif timeline <= 8:
                medium_track.append((market, data))
            else:
                slow_track.append((market, data))

        # Calculate hybrid timeline
        total_months = 0
        current_date = start_date
        market_completion_dates = {}
        waves = []

        # Wave 1: Fast track markets (parallel)
        if fast_track:
            wave_timeline = max(data["timeline_months"] for _, data in fast_track)
            wave_end = current_date + timedelta(days=wave_timeline * 30)

            for market, data in fast_track:
                market_completion_dates[market] = wave_end.isoformat()

            waves.append({
                "wave": 1,
                "markets": [m for m, _ in fast_track],
                "duration_months": wave_timeline,
                "approach": "parallel"
            })

            total_months = wave_timeline
            current_date = wave_end

        # Wave 2: Medium track markets
        if medium_track:
            wave_timeline = max(data["timeline_months"] for _, data in medium_track)
            wave_end = current_date + timedelta(days=wave_timeline * 30)

            for market, data in medium_track:
                market_completion_dates[market] = wave_end.isoformat()

            waves.append({
                "wave": len(waves) + 1,
                "markets": [m for m, _ in medium_track],
                "duration_months": wave_timeline,
                "approach": "sequential" if fast_track else "parallel"
            })

            total_months += wave_timeline
            current_date = wave_end

        # Wave 3: Slow track markets
        if slow_track:
            wave_timeline = max(data["timeline_months"] for _, data in slow_track)
            wave_end = current_date + timedelta(days=wave_timeline * 30)

            for market, data in slow_track:
                market_completion_dates[market] = wave_end.isoformat()

            waves.append({
                "wave": len(waves) + 1,
                "markets": [m for m, _ in slow_track],
                "duration_months": wave_timeline,
                "approach": "sequential"
            })

            total_months += wave_timeline

        return {
            "strategy": "hybrid",
            "total_duration_months": total_months,
            "start_date": start_date.isoformat(),
            "end_date": current_date.isoformat(),
            "waves": waves,
            "concurrent_submissions": max(len(w["markets"]) for w in waves),
            "resource_intensity": "MEDIUM",
            "pros": [
                "Balanced resource utilization",
                "Early wins from fast markets",
                "Uses early approvals for subsequent waves"
            ],
            "cons": [
                "Moderate coordination complexity",
                "Some markets delayed",
                "Requires careful planning"
            ],
            "market_completion_dates": market_completion_dates
        }

    def _recommend_strategy(
        self,
        strategies: Dict[str, Dict],
        resources: str
    ) -> Dict[str, Any]:
        """Recommend optimal strategy based on resources and timelines"""

        scores = {}
        for strategy_name, strategy_data in strategies.items():
            score = 0

            # Score based on total duration (lower is better)
            duration = strategy_data["total_duration_months"]
            if duration < 6:
                score += 30
            elif duration < 12:
                score += 20
            elif duration < 18:
                score += 10

            # Score based on resource intensity
            intensity = strategy_data["resource_intensity"]
            if resources == "high" and intensity == "HIGH":
                score += 25
            elif resources == "medium" and intensity == "MEDIUM":
                score += 25
            elif resources == "low" and intensity == "LOW":
                score += 25

            # Score based on pros
            score += len(strategy_data["pros"]) * 5

            # Deduct for cons
            score -= len(strategy_data["cons"]) * 3

            scores[strategy_name] = score

        # Find best strategy
        best_strategy = max(scores.items(), key=lambda x: x[1])

        return {
            "strategy_name": best_strategy[0],
            "score": best_strategy[1],
            "all_scores": scores,
            "rationale": self._generate_strategy_rationale(
                best_strategy[0],
                strategies[best_strategy[0]]
            )
        }

    def _generate_strategy_rationale(
        self,
        strategy_name: str,
        strategy_data: Dict
    ) -> str:
        """Generate rationale for strategy recommendation"""

        rationales = {
            "parallel": (
                f"Parallel submission offers fastest time to market ({strategy_data['total_duration_months']:.1f} months). "
                f"Best suited when resources are available and early market entry is critical."
            ),
            "sequential": (
                f"Sequential submission minimizes resource requirements while maintaining quality. "
                f"Best for limited resources or when learning from each submission is valuable."
            ),
            "hybrid": (
                f"Hybrid approach balances speed and resource utilization ({strategy_data['total_duration_months']:.1f} months). "
                f"Wave-based submission provides early wins while managing complexity."
            )
        }

        return rationales.get(strategy_name, "Strategy selected based on overall scoring.")

    def _generate_timeline_projection(
        self,
        market_timelines: Dict[str, Dict],
        strategy: str,
        start_date: datetime
    ) -> List[Dict[str, Any]]:
        """Generate detailed timeline projection"""

        projections = []

        if strategy == "parallel":
            for market, data in market_timelines.items():
                projections.append({
                    "market": market,
                    "submission_date": start_date.isoformat(),
                    "expected_approval": (
                        start_date + timedelta(days=data["timeline_months"] * 30)
                    ).isoformat(),
                    "duration_months": data["timeline_months"],
                    "parallel_wave": 1
                })

        elif strategy == "sequential":
            sorted_markets = sorted(
                market_timelines.items(),
                key=lambda x: x[1]["timeline_months"]
            )

            current_date = start_date
            for idx, (market, data) in enumerate(sorted_markets):
                projections.append({
                    "market": market,
                    "submission_date": current_date.isoformat(),
                    "expected_approval": (
                        current_date + timedelta(days=data["timeline_months"] * 30)
                    ).isoformat(),
                    "duration_months": data["timeline_months"],
                    "sequential_order": idx + 1
                })
                current_date += timedelta(days=data["timeline_months"] * 30)

        elif strategy == "hybrid":
            # Group by timeline buckets
            fast = []
            medium = []
            slow = []

            for market, data in market_timelines.items():
                timeline = data["timeline_months"]
                if timeline <= 4:
                    fast.append((market, data))
                elif timeline <= 8:
                    medium.append((market, data))
                else:
                    slow.append((market, data))

            wave_num = 0
            current_date = start_date

            for wave_data in [(fast, 1), (medium, 2), (slow, 3)]:
                markets, wave = wave_data
                if not markets:
                    continue

                wave_num += 1
                wave_timeline = max(data["timeline_months"] for _, data in markets)

                for market, data in markets:
                    projections.append({
                        "market": market,
                        "submission_date": current_date.isoformat(),
                        "expected_approval": (
                            current_date + timedelta(days=data["timeline_months"] * 30)
                        ).isoformat(),
                        "duration_months": data["timeline_months"],
                        "wave": wave_num
                    })

                current_date += timedelta(days=wave_timeline * 30)

        return projections

    def _suggest_resource_allocation(
        self,
        market_timelines: Dict[str, Dict],
        strategy: str
    ) -> Dict[str, Any]:
        """Suggest resource allocation for recommended strategy"""

        allocation = {
            "regulatory_affairs": {
                "fte_required": 0,
                "key_activities": []
            },
            "clinical_affairs": {
                "fte_required": 0,
                "key_activities": []
            },
            "quality_assurance": {
                "fte_required": 0,
                "key_activities": []
            }
        }

        # Base requirements
        allocation["regulatory_affairs"]["key_activities"] = [
            "Submission preparation",
            "Regulatory correspondence",
            "Application management"
        ]

        allocation["clinical_affairs"]["key_activities"] = [
            "Clinical evidence compilation",
            "Literature search",
            "CER preparation"
        ]

        allocation["quality_assurance"]["key_activities"] = [
            "QMS documentation",
            "Technical file preparation",
            "Compliance verification"
        ]

        # Strategy-specific adjustments
        if strategy == "parallel":
            allocation["regulatory_affairs"]["fte_required"] = 3.0
            allocation["clinical_affairs"]["fte_required"] = 2.0
            allocation["quality_assurance"]["fte_required"] = 2.0

            allocation["regulatory_affairs"]["key_activities"].extend([
                "Parallel submission coordination",
                "Timeline tracking across markets"
            ])

        elif strategy == "sequential":
            allocation["regulatory_affairs"]["fte_required"] = 1.5
            allocation["clinical_affairs"]["fte_required"] = 1.0
            allocation["quality_assurance"]["fte_required"] = 1.0

            allocation["regulatory_affairs"]["key_activities"].extend([
                "Sequential submission planning",
                "Lessons learned documentation"
            ])

        elif strategy == "hybrid":
            allocation["regulatory_affairs"]["fte_required"] = 2.0
            allocation["clinical_affairs"]["fte_required"] = 1.5
            allocation["quality_assurance"]["fte_required"] = 1.5

            allocation["regulatory_affairs"]["key_activities"].extend([
                "Wave coordination",
                "Resource leveling between waves"
            ])

        return allocation

    def identify_easy_win_markets(
        self,
        device_class: str,
        available_markets: List[str]
    ) -> List[Dict[str, Any]]:
        """Identify markets with fastest approval times and lowest complexity"""

        market_scores = []

        for market in available_markets:
            if market in self.database["markets"]:
                market_data = self.database["markets"][market]
                class_data = self._find_matching_class(market_data, device_class)

                if class_data:
                    # Score based on timeline and complexity
                    score = 100 - class_data.get("typical_timeline_months", 0) * 5

                    if class_data.get("notified_body_required", False):
                        score -= 20

                    if class_data.get("clinical_evaluation_required", False):
                        score -= 15

                    market_scores.append({
                        "market": market,
                        "region": market_data["region"],
                        "score": score,
                        "timeline_months": class_data.get("typical_timeline_months", 0),
                        "notified_body_required": class_data.get("notified_body_required", False),
                        "submission_required": class_data.get("submission_required", False)
                    })

        # Sort by score (highest first)
        market_scores.sort(key=lambda x: x["score"], reverse=True)

        return market_scores

    def identify_high_risk_markets(
        self,
        device_class: str,
        available_markets: List[str]
    ) -> List[Dict[str, Any]]:
        """Identify markets with longest timelines and highest complexity"""

        market_risks = []

        for market in available_markets:
            if market in self.database["markets"]:
                market_data = self.database["markets"][market]
                class_data = self._find_matching_class(market_data, device_class)

                if class_data:
                    # Risk score based on timeline and complexity
                    risk_score = class_data.get("typical_timeline_months", 0) * 3

                    if class_data.get("notified_body_required", False):
                        risk_score += 25

                    if class_data.get("clinical_evaluation_required", False):
                        risk_score += 20

                    market_risks.append({
                        "market": market,
                        "region": market_data["region"],
                        "risk_score": risk_score,
                        "timeline_months": class_data.get("typical_timeline_months", 0),
                        "notified_body_required": class_data.get("notified_body_required", False),
                        "clinical_evaluation_required": class_data.get("clinical_evaluation_required", False),
                        "risk_factors": self._identify_risk_factors(class_data)
                    })

        # Sort by risk score (highest first)
        market_risks.sort(key=lambda x: x["risk_score"], reverse=True)

        return market_risks

    def _identify_risk_factors(self, class_data: Dict) -> List[str]:
        """Identify specific risk factors for a market"""

        factors = []

        if class_data.get("typical_timeline_months", 0) > 12:
            factors.append("Extended approval timeline")

        if class_data.get("notified_body_required", False):
            factors.append("Notified Body capacity constraints")

        if class_data.get("clinical_evaluation_required", False):
            factors.append("Clinical evidence requirements")

        if class_data.get("submission_required", False):
            factors.append("Submission preparation complexity")

        return factors


def main():
    """Example usage"""
    analyzer = TimelineAnalyzer(
        "/Users/hb/.moai/worktrees/Agent-Skills/SPEC-ARIA-005/.claude/templates/aria/regulatory/regulatory-database-schema.json"
    )

    # Analyze submission sequencing for Class II
    analysis = analyzer.analyze_submission_sequencing(
        device_class="Class II",
        target_markets=["FDA", "EU_MDR", "MFDS", "PMDA"],
        submission_start_date="2025-03-01",
        available_resources="medium"
    )

    # Print analysis
    print(json.dumps(analysis, indent=2))

    # Identify easy win markets
    easy_wins = analyzer.identify_easy_win_markets("Class II", ["FDA", "EU_MDR", "MFDS", "PMDA"])
    print("\n=== EASY WIN MARKETS ===")
    for win in easy_wins:
        print(f"{win['market']}: Score {win['score']}, Timeline {win['timeline_months']} months")

    # Identify high-risk markets
    high_risk = analyzer.identify_high_risk_markets("Class II", ["FDA", "EU_MDR", "MFDS", "PMDA"])
    print("\n=== HIGH RISK MARKETS ===")
    for risk in high_risk:
        print(f"{risk['market']}: Risk Score {risk['risk_score']}, Timeline {risk['timeline_months']} months")


if __name__ == "__main__":
    main()
