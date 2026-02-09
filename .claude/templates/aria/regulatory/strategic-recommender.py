#!/usr/bin/env python3
"""
Strategic Recommendation Engine for ARIA
Provides strategic recommendations for optimal submission sequencing
"""

import json
from typing import Dict, List, Any, Tuple
from datetime import datetime, timedelta
from enum import Enum


class RecommendationPriority(Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class StrategicRecommender:
    """Generate strategic recommendations for multi-market regulatory submissions"""

    def __init__(self, database_path: str):
        """Initialize with regulatory database"""
        self.database = self._load_database(database_path)

    def _load_database(self, path: str) -> Dict:
        """Load regulatory database from JSON file"""
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def generate_comprehensive_recommendations(
        self,
        device_class: str,
        target_markets: List[str],
        submission_start_date: str = None,
        available_resources: str = "medium",
        strategic_priorities: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """
        Generate comprehensive strategic recommendations

        Args:
            device_class: Device classification
            target_markets: Target markets for submission
            submission_start_date: Start date for submissions (ISO format)
            available_resources: low, medium, high (affects parallel capacity)
            strategic_priorities: Strategic priorities (speed, cost, risk)

        Returns:
            Comprehensive strategic recommendations
        """
        if strategic_priorities is None:
            strategic_priorities = {
                "speed": 0.7,
                "cost": 0.5,
                "risk": 0.6
            }

        recommendations = {
            "generated_at": datetime.now().isoformat(),
            "device_class": device_class,
            "target_markets": target_markets,
            "strategic_priorities": strategic_priorities,
            "submission_strategy": {},
            "market_prioritization": {},
            "risk_mitigation": {},
            "resource_optimization": {},
            "action_items": []
        }

        # Generate submission strategy recommendation
        recommendations["submission_strategy"] = self._recommend_submission_strategy(
            device_class, target_markets, available_resources, strategic_priorities
        )

        # Generate market prioritization
        recommendations["market_prioritization"] = self._prioritize_markets(
            device_class, target_markets, strategic_priorities
        )

        # Generate risk mitigation recommendations
        recommendations["risk_mitigation"] = self._generate_risk_mitigation(
            device_class, target_markets
        )

        # Generate resource optimization recommendations
        recommendations["resource_optimization"] = self._optimize_resources(
            device_class, target_markets, available_resources
        )

        # Generate action items
        recommendations["action_items"] = self._generate_action_items(
            recommendations
        )

        return recommendations

    def _recommend_submission_strategy(
        self,
        device_class: str,
        target_markets: List[str],
        resources: str,
        priorities: Dict[str, float]
    ) -> Dict[str, Any]:
        """Recommend optimal submission strategy"""

        # Calculate market complexity
        market_complexity = self._calculate_market_complexity(device_class, target_markets)

        # Score each strategy
        strategies = {
            "parallel": self._score_parallel_strategy(market_complexity, resources, priorities),
            "sequential": self._score_sequential_strategy(market_complexity, resources, priorities),
            "hybrid": self._score_hybrid_strategy(market_complexity, resources, priorities)
        }

        # Select best strategy
        best_strategy = max(strategies.items(), key=lambda x: x[1]["score"])

        return {
            "recommended_strategy": best_strategy[0],
            "confidence": best_strategy[1]["confidence"],
            "rationale": best_strategy[1]["rationale"],
            "alternative_strategies": [
                {
                    "strategy": name,
                    "score": data["score"],
                    "when_to_consider": data["when_to_consider"]
                }
                for name, data in strategies.items()
                if name != best_strategy[0]
            ],
            "implementation_notes": best_strategy[1]["implementation_notes"]
        }

    def _calculate_market_complexity(self, device_class: str, markets: List[str]) -> Dict[str, float]:
        """Calculate complexity metrics for markets"""

        complexity = {
            "total_markets": len(markets),
            "avg_timeline": 0,
            "notified_body_markets": 0,
            "clinical_required_markets": 0,
            "complexity_score": 0
        }

        timelines = []
        for market in markets:
            if market in self.database["markets"]:
                market_data = self.database["markets"][market]
                class_data = self._find_matching_class(market_data, device_class)

                if class_data:
                    timelines.append(class_data.get("typical_timeline_months", 0))

                    if class_data.get("notified_body_required", False):
                        complexity["notified_body_markets"] += 1

                    if class_data.get("clinical_evaluation_required", False):
                        complexity["clinical_required_markets"] += 1

        if timelines:
            complexity["avg_timeline"] = sum(timelines) / len(timelines)

        # Calculate complexity score (0-100)
        complexity["complexity_score"] = (
            complexity["total_markets"] * 10 +
            complexity["avg_timeline"] * 2 +
            complexity["notified_body_markets"] * 15 +
            complexity["clinical_required_markets"] * 10
        )

        return complexity

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

    def _score_parallel_strategy(
        self,
        complexity: Dict,
        resources: str,
        priorities: Dict
    ) -> Dict[str, Any]:
        """Score parallel submission strategy"""

        score = 0

        # Speed priority favors parallel
        score += priorities["speed"] * 40

        # Resource availability
        resource_scores = {"high": 30, "medium": 15, "low": 0}
        score += resource_scores.get(resources, 15)

        # Complexity penalty
        if complexity["complexity_score"] > 50:
            score -= 20

        # Notified body constraint
        if complexity["notified_body_markets"] > 0:
            score -= 10

        confidence = min(100, max(0, score))

        return {
            "score": score,
            "confidence": confidence,
            "rationale": self._generate_parallel_rationale(complexity, resources, priorities),
            "implementation_notes": self._get_parallel_implementation_notes(complexity),
            "when_to_consider": "When speed is critical and resources are available"
        }

    def _score_sequential_strategy(
        self,
        complexity: Dict,
        resources: str,
        priorities: Dict
    ) -> Dict[str, Any]:
        """Score sequential submission strategy"""

        score = 0

        # Cost priority favors sequential
        score += priorities["cost"] * 30

        # Resource constraint favors sequential
        resource_scores = {"high": 0, "medium": 15, "low": 30}
        score += resource_scores.get(resources, 15)

        # Low complexity favors sequential
        if complexity["complexity_score"] < 30:
            score += 20

        # Risk mitigation
        score += priorities["risk"] * 20

        confidence = min(100, max(0, score))

        return {
            "score": score,
            "confidence": confidence,
            "rationale": self._generate_sequential_rationale(complexity, resources, priorities),
            "implementation_notes": self._get_sequential_implementation_notes(),
            "when_to_consider": "When resources are limited or learning from each submission is valuable"
        }

    def _score_hybrid_strategy(
        self,
        complexity: Dict,
        resources: str,
        priorities: Dict
    ) -> Dict[str, Any]:
        """Score hybrid submission strategy"""

        score = 0

        # Balanced priorities favor hybrid
        speed_cost_balance = abs(priorities["speed"] - priorities["cost"])
        score += (1 - speed_cost_balance) * 30

        # Medium resources favor hybrid
        if resources == "medium":
            score += 25

        # Medium complexity favors hybrid
        if 30 <= complexity["complexity_score"] <= 60:
            score += 20

        # Risk mitigation
        score += priorities["risk"] * 15

        confidence = min(100, max(0, score))

        return {
            "score": score,
            "confidence": confidence,
            "rationale": self._generate_hybrid_rationale(complexity, resources, priorities),
            "implementation_notes": self._get_hybrid_implementation_notes(complexity),
            "when_to_consider": "When balancing speed, cost, and risk with medium resources"
        }

    def _generate_parallel_rationale(
        self,
        complexity: Dict,
        resources: str,
        priorities: Dict
    ) -> str:
        """Generate rationale for parallel strategy"""
        return (
            f"Parallel submission maximizes speed (priority: {priorities['speed']:.1f}) "
            f"across {complexity['total_markets']} markets. "
            f"Best for {resources} resource availability. "
            f"Requires {complexity['notified_body_markets']} Notified Body engagements. "
            f"Expected complexity: {complexity['complexity_score']:.0f}/100."
        )

    def _generate_sequential_rationale(
        self,
        complexity: Dict,
        resources: str,
        priorities: Dict
    ) -> str:
        """Generate rationale for sequential strategy"""
        return (
            f"Sequential submission optimizes cost (priority: {priorities['cost']:.1f}) "
            f"and minimizes resource requirements. "
            f"Best for {resources} resource availability. "
            f"Low complexity ({complexity['complexity_score']:.0f}/100) suits sequential approach."
        )

    def _generate_hybrid_rationale(
        self,
        complexity: Dict,
        resources: str,
        priorities: Dict
    ) -> str:
        """Generate rationale for hybrid strategy"""
        return (
            f"Hybrid submission balances priorities (speed: {priorities['speed']:.1f}, "
            f"cost: {priorities['cost']:.1f}). "
            f"Wave-based approach for {complexity['total_markets']} markets. "
            f"Medium complexity ({complexity['complexity_score']:.0f}/100) suits hybrid approach."
        )

    def _get_parallel_implementation_notes(self, complexity: Dict) -> List[str]:
        """Get parallel implementation notes"""
        notes = [
            "Prepare all submissions simultaneously",
            "Dedicated regulatory team for each market",
            "Centralized clinical evidence repository"
        ]

        if complexity["notified_body_markets"] > 0:
            notes.append(f"Engage {complexity['notified_body_markets']} Notified Bodies early")

        notes.append("Implement robust project management system")
        notes.append("Plan for significant upfront resource investment")

        return notes

    def _get_sequential_implementation_notes(self) -> List[str]:
        """Get sequential implementation notes"""
        return [
            "Start with fastest/easiest market",
            "Document lessons learned from each submission",
            "Reuse approved content for subsequent markets",
            "Leverage early approvals to support later submissions",
            "Maintain single regulatory team with market rotation"
        ]

    def _get_hybrid_implementation_notes(self, complexity: Dict) -> List[str]:
        """Get hybrid implementation notes"""
        notes = [
            "Group markets by timeline similarity",
            "Wave 1: Fast-track markets (≤4 months)",
            "Wave 2: Medium-duration markets (5-8 months)",
            "Wave 3: Long-duration markets (>8 months)",
            "Scale resources between waves"
        ]

        if complexity["notified_body_markets"] > 0:
            notes.append("Start Notified Body engagement in Wave 1")

        notes.append("Use Wave 1 approvals to support subsequent waves")

        return notes

    def _prioritize_markets(
        self,
        device_class: str,
        markets: List[str],
        priorities: Dict
    ) -> Dict[str, Any]:
        """Prioritize markets based on strategic objectives"""

        market_scores = []

        for market in markets:
            if market in self.database["markets"]:
                market_data = self.database["markets"][market]
                class_data = self._find_matching_class(market_data, device_class)

                if class_data:
                    score = self._calculate_market_score(
                        market,
                        class_data,
                        priorities
                    )

                    market_scores.append({
                        "market": market,
                        "region": market_data["region"],
                        "score": score,
                        "priority": self._get_priority_level(score),
                        "timeline_months": class_data.get("typical_timeline_months", 0),
                        "key_factors": self._get_market_key_factors(market, class_data)
                    })

        # Sort by score
        market_scores.sort(key=lambda x: x["score"], reverse=True)

        return {
            "ranking": market_scores,
            "tier_1_markets": [m["market"] for m in market_scores if m["priority"] == "HIGH"],
            "tier_2_markets": [m["market"] for m in market_scores if m["priority"] == "MEDIUM"],
            "tier_3_markets": [m["market"] for m in market_scores if m["priority"] == "LOW"]
        }

    def _calculate_market_score(
        self,
        market: str,
        class_data: Dict,
        priorities: Dict
    ) -> float:
        """Calculate strategic score for a market"""

        score = 50.0  # Base score

        # Timeline factor (speed priority)
        timeline = class_data.get("typical_timeline_months", 12)
        timeline_score = max(0, 100 - timeline * 5)
        score += timeline_score * priorities["speed"] * 0.3

        # Submission complexity (cost priority)
        if not class_data.get("submission_required", False):
            score += 20 * priorities["cost"]

        if not class_data.get("notified_body_required", False):
            score += 15 * priorities["cost"]

        if not class_data.get("clinical_evaluation_required", False):
            score += 10 * priorities["cost"]

        # Risk factor
        if class_data.get("notified_body_required", False):
            score -= 10 * priorities["risk"]

        return score

    def _get_priority_level(self, score: float) -> str:
        """Get priority level from score"""
        if score >= 70:
            return "HIGH"
        elif score >= 50:
            return "MEDIUM"
        else:
            return "LOW"

    def _get_market_key_factors(self, market: str, class_data: Dict) -> List[str]:
        """Get key strategic factors for a market"""
        factors = []

        timeline = class_data.get("typical_timeline_months", 0)
        if timeline <= 4:
            factors.append("Fast approval timeline")
        elif timeline >= 12:
            factors.append("Extended approval timeline")

        if class_data.get("notified_body_required", False):
            factors.append("Notified Body required")

        if class_data.get("clinical_evaluation_required", False):
            factors.append("Clinical evaluation required")

        if not class_data.get("submission_required", False):
            factors.append("No submission required")

        return factors

    def _generate_risk_mitigation(
        self,
        device_class: str,
        markets: List[str]
    ) -> Dict[str, Any]:
        """Generate risk mitigation recommendations"""

        risks = []
        mitigation_strategies = []

        # Analyze risks for each market
        for market in markets:
            if market in self.database["markets"]:
                market_data = self.database["markets"][market]
                class_data = self._find_matching_class(market_data, device_class)

                if class_data:
                    market_risks = self._identify_market_risks(market, class_data)
                    risks.extend(market_risks)

        # Generate mitigation strategies
        risk_categories = set(r["category"] for r in risks)

        for category in risk_categories:
            category_risks = [r for r in risks if r["category"] == category]

            mitigation_strategies.append({
                "risk_category": category,
                "severity": self._calculate_category_severity(category_risks),
                "affected_markets": list(set(r["market"] for r in category_risks)),
                "mitigation_actions": self._get_mitigation_actions(category),
                "timeline_impact": self._estimate_mitigation_timeline(category)
            })

        return {
            "identified_risks": risks,
            "mitigation_strategies": mitigation_strategies,
            "contingency_planning": self._generate_contingency_planning(risks)
        }

    def _identify_market_risks(self, market: str, class_data: Dict) -> List[Dict]:
        """Identify risks for a specific market"""
        risks = []

        # Timeline risk
        timeline = class_data.get("typical_timeline_months", 0)
        if timeline > 9:
            risks.append({
                "market": market,
                "category": "Timeline",
                "description": f"Extended approval timeline ({timeline} months)",
                "severity": "HIGH" if timeline > 12 else "MEDIUM"
            })

        # Notified Body risk
        if class_data.get("notified_body_required", False):
            risks.append({
                "market": market,
                "category": "Notified Body",
                "description": "Notified Body capacity constraints",
                "severity": "HIGH"
            })

        # Clinical evidence risk
        if class_data.get("clinical_evaluation_required", False):
            risks.append({
                "market": market,
                "category": "Clinical Evidence",
                "description": "Comprehensive clinical evaluation required",
                "severity": "MEDIUM"
            })

        return risks

    def _calculate_category_severity(self, risks: List[Dict]) -> str:
        """Calculate overall severity for a risk category"""
        if any(r["severity"] == "HIGH" for r in risks):
            return "HIGH"
        elif any(r["severity"] == "MEDIUM" for r in risks):
            return "MEDIUM"
        else:
            return "LOW"

    def _get_mitigation_actions(self, category: str) -> List[str]:
        """Get mitigation actions for a risk category"""
        actions = {
            "Timeline": [
                "Early submission preparation",
                "Consider expedited programs if eligible",
                "Parallel development activities",
                "Buffer time in project schedule"
            ],
            "Notified Body": [
                "Engage Notified Body 12-18 months early",
                "Consider multiple Notified Body options",
                "Pre-submission meetings",
                "Complete technical documentation in advance"
            ],
            "Clinical Evidence": [
                "Start clinical evaluation early",
                "Conduct comprehensive literature search",
                "Consider multi-center clinical studies",
                "Prepare detailed CER per MEDDEV 2.7.1 rev 4"
            ]
        }

        return actions.get(category, ["Standard risk mitigation practices"])

    def _estimate_mitigation_timeline(self, category: str) -> str:
        """Estimate timeline for mitigation implementation"""
        timelines = {
            "Timeline": "Immediate - 3 months",
            "Notified Body": "12-18 months before submission",
            "Clinical Evidence": "6-12 months before submission"
        }

        return timelines.get(category, "As needed")

    def _generate_contingency_planning(self, risks: List[Dict]) -> List[Dict]:
        """Generate contingency planning recommendations"""
        contingencies = []

        # Check for high-severity risks
        high_risk_markets = set(
            r["market"] for r in risks
            if r["severity"] == "HIGH"
        )

        if high_risk_markets:
            contingencies.append({
                "scenario": "Notified Body delays",
                "trigger": "Notified Body extends review beyond expected timeline",
                "contingency_actions": [
                    "Submit to other markets without Notified Body requirement",
                    "Consider alternative Notified Body",
                    "Plan for extended timeline in budget"
                ]
            })

        # Clinical evidence contingencies
        if any(r["category"] == "Clinical Evidence" for r in risks):
            contingencies.append({
                "scenario": "Insufficient clinical evidence",
                "trigger": "Regulator requests additional clinical data",
                "contingency_actions": [
                    "Initiate additional clinical study",
                    "Expand literature search",
                    "Consider predicate device with different clinical requirements"
                ]
            })

        return contingencies

    def _optimize_resources(
        self,
        device_class: str,
        markets: List[str],
        resources: str
    ) -> Dict[str, Any]:
        """Generate resource optimization recommendations"""

        # Calculate resource needs
        base_fte = {
            "regulatory_affairs": 1.5,
            "clinical_affairs": 1.0,
            "quality_assurance": 1.0,
            "project_management": 0.5
        }

        # Adjust for market count
        market_multiplier = 1 + (len(markets) - 1) * 0.3

        # Adjust for resource level
        resource_multiplier = {"high": 1.5, "medium": 1.0, "low": 0.7}

        multiplier = market_multiplier * resource_multiplier.get(resources, 1.0)

        optimized_fte = {
            role: round(base * multiplier, 1)
            for role, base in base_fte.items()
        }

        return {
            "recommended_team_size": sum(optimized_fte.values()),
            "role_allocation": optimized_fte,
            "resource_efficiency_tips": self._get_efficiency_tips(markets, resources),
            "outsourcing_opportunities": self._identify_outsourcing_opportunities(markets),
            "tool_recommendations": [
                "Regulatory submission management system",
                "Document control and version tracking",
                "Timeline visualization tools",
                "Compliance checklist automation"
            ]
        }

    def _get_efficiency_tips(self, markets: List[str], resources: str) -> List[str]:
        """Get efficiency tips based on markets and resources"""
        tips = []

        if len(markets) > 3:
            tips.append("Implement centralized document repository for reuse across markets")

        if resources == "low":
            tips.append("Prioritize markets with fastest approval times")
            tips.append("Consider sequential submission to manage workload")

        if resources == "high":
            tips.append("Parallel submission can maximize speed")
            tips.append("Dedicate specialists to each market")

        tips.append("Create reusable content templates for common requirements")
        tips.append("Establish clear review and approval processes")

        return tips

    def _identify_outsourcing_opportunities(self, markets: List[str]) -> List[Dict]:
        """Identify opportunities for outsourcing"""
        opportunities = [
            {
                "activity": "Clinical literature search",
                "rationale": "Specialized expertise required",
                "timing": "Early in submission process"
            },
            {
                "activity": "Translation services",
                "rationale": "Accurate regulatory translations critical",
                "timing": "During document preparation"
            },
            {
                "activity": "Local representation",
                "rationale": "Required for some markets (e.g., Japan, South Korea)",
                "timing": "Before submission"
            }
        ]

        # Add Notified Body consulting if needed
        for market in markets:
            if market in ["EU_MDR", "MFDS"]:
                opportunities.append({
                    "activity": f"Notified Body consulting - {market}",
                    "rationale": "Notified Body capacity constraints",
                    "timing": "12-18 months before submission"
                })

        return opportunities

    def _generate_action_items(self, recommendations: Dict) -> List[Dict[str, Any]]:
        """Generate prioritized action items"""

        action_items = []

        # Strategy implementation actions
        strategy = recommendations["submission_strategy"]["recommended_strategy"]
        if strategy == "parallel":
            action_items.append({
                "priority": "CRITICAL",
                "category": "Strategy",
                "action": "Prepare parallel submission infrastructure",
                "timeline": "Immediate",
                "responsible": "Regulatory Affairs Lead",
                "dependencies": []
            })
        elif strategy == "hybrid":
            action_items.append({
                "priority": "HIGH",
                "category": "Strategy",
                "action": "Define wave-based submission plan",
                "timeline": "Within 1 month",
                "responsible": "Project Manager",
                "dependencies": []
            })

        # Market prioritization actions
        tier_1 = recommendations["market_prioritization"].get("tier_1_markets", [])
        for market in tier_1:
            action_items.append({
                "priority": "HIGH",
                "category": "Market Preparation",
                "action": f"Initiate {market} submission preparation",
                "timeline": "Immediate",
                "responsible": "Regulatory Affairs",
                "dependencies": ["Strategy approval"]
            })

        # Risk mitigation actions
        for mitigation in recommendations["risk_mitigation"]["mitigation_strategies"]:
            if mitigation["severity"] == "HIGH":
                action_items.append({
                    "priority": "CRITICAL",
                    "category": "Risk Mitigation",
                    "action": f"Address {mitigation['risk_category']} risks",
                    "timeline": mitigation["timeline_impact"],
                    "responsible": "Compliance Manager",
                    "dependencies": []
                })

        # Resource optimization actions
        action_items.append({
            "priority": "MEDIUM",
            "category": "Resources",
            "action": "Assemble regulatory team per allocation plan",
            "timeline": "Within 1 month",
            "responsible": "HR / Regulatory Affairs",
            "dependencies": ["Budget approval"]
        })

        # Sort by priority
        priority_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
        action_items.sort(key=lambda x: priority_order.get(x["priority"], 4))

        return action_items

    def generate_markdown_report(self, recommendations: Dict[str, Any]) -> str:
        """Generate formatted Markdown report"""

        md = []
        md.append("# Strategic Regulatory Submission Recommendations")
        md.append(f"**Generated:** {recommendations['generated_at']}")
        md.append(f"**Device Class:** {recommendations['device_class']}")
        md.append(f"**Target Markets:** {', '.join(recommendations['target_markets'])}")
        md.append("")

        # Strategic Priorities
        md.append("## Strategic Priorities")
        md.append("")
        for priority, value in recommendations["strategic_priorities"].items():
            md.append(f"- **{priority.capitalize()}:** {value:.1f}/1.0")
        md.append("")

        # Submission Strategy
        strategy = recommendations["submission_strategy"]
        md.append("## Recommended Submission Strategy")
        md.append("")
        md.append(f"**Strategy:** {strategy['recommended_strategy'].upper()}")
        md.append(f"**Confidence:** {strategy['confidence']}%")
        md.append("")
        md.append(f"### Rationale")
        md.append(strategy['rationale'])
        md.append("")

        md.append("### Implementation Notes")
        for note in strategy['implementation_notes']:
            md.append(f"- {note}")
        md.append("")

        if strategy['alternative_strategies']:
            md.append("### Alternative Strategies")
            for alt in strategy['alternative_strategies']:
                md.append(f"**{alt['strategy'].capitalize()}:** {alt['when_to_consider']}")
            md.append("")

        # Market Prioritization
        prioritization = recommendations["market_prioritization"]
        md.append("## Market Prioritization")
        md.append("")

        md.append("### Tier 1 Markets (High Priority)")
        for market in prioritization.get("tier_1_markets", []):
            md.append(f"- **{market}**")
        md.append("")

        md.append("### Tier 2 Markets (Medium Priority)")
        for market in prioritization.get("tier_2_markets", []):
            md.append(f"- **{market}**")
        md.append("")

        md.append("### Tier 3 Markets (Low Priority)")
        for market in prioritization.get("tier_3_markets", []):
            md.append(f"- **{market}**")
        md.append("")

        # Risk Mitigation
        risk_mitigation = recommendations["risk_mitigation"]
        md.append("## Risk Mitigation")
        md.append("")

        for mitigation in risk_mitigation["mitigation_strategies"]:
            md.append(f"### {mitigation['risk_category']} ({mitigation['severity']})")
            md.append(f"**Affected Markets:** {', '.join(mitigation['affected_markets'])}")
            md.append("**Mitigation Actions:**")
            for action in mitigation["mitigation_actions"]:
                md.append(f"- {action}")
            md.append(f"**Timeline:** {mitigation['timeline_impact']}")
            md.append("")

        # Resource Optimization
        resources = recommendations["resource_optimization"]
        md.append("## Resource Optimization")
        md.append("")
        md.append(f"**Recommended Team Size:** {resources['recommended_team_size']} FTE")
        md.append("")
        md.append("### Role Allocation")
        for role, fte in resources["role_allocation"].items():
            md.append(f"- **{role.replace('_', ' ').title()}:** {fte} FTE")
        md.append("")

        # Action Items
        md.append("## Action Items")
        md.append("")

        for item in recommendations["action_items"]:
            md.append(f"### [{item['priority']}] {item['action']}")
            md.append(f"- **Category:** {item['category']}")
            md.append(f"- **Timeline:** {item['timeline']}")
            md.append(f"- **Responsible:** {item['responsible']}")
            if item['dependencies']:
                md.append(f"- **Dependencies:** {', '.join(item['dependencies'])}")
            md.append("")

        # Disclaimer
        md.append("---")
        md.append("*Disclaimer: These recommendations are for informational purposes only. Always verify requirements with official regulatory sources and consult with qualified regulatory professionals.*")

        return "\n".join(md)


def main():
    """Example usage"""
    recommender = StrategicRecommender(
        "/Users/hb/.moai/worktrees/Agent-Skills/SPEC-ARIA-005/.claude/templates/aria/regulatory/regulatory-database-schema.json"
    )

    # Generate comprehensive recommendations
    recommendations = recommender.generate_comprehensive_recommendations(
        device_class="Class II",
        target_markets=["FDA", "EU_MDR", "MFDS", "PMDA", "ANVISA"],
        submission_start_date="2025-03-01",
        available_resources="medium",
        strategic_priorities={"speed": 0.8, "cost": 0.5, "risk": 0.6}
    )

    # Print Markdown report
    report = recommender.generate_markdown_report(recommendations)
    print(report)

    # Save to file
    with open("/Users/hb/.moai/worktrees/Agent-Skills/SPEC-ARIA-005/.claude/templates/aria/regulatory/strategic-recommendations-example.md", "w") as f:
        f.write(report)


if __name__ == "__main__":
    main()
