#!/usr/bin/env python3
"""
Integration Test for Multi-Country Regulatory Strategy Comparison
Tests all components working together
"""

import json
import sys
import os
import importlib.util

# Load modules dynamically from current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

def load_module(name, file_path):
    spec = importlib.util.spec_from_file_location(name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

# Load all required modules
comparison_matrix_generator = load_module(
    "comparison_matrix_generator",
    os.path.join(current_dir, "comparison-matrix-generator.py")
)
timeline_analyzer = load_module(
    "timeline_analyzer",
    os.path.join(current_dir, "timeline-analyzer.py")
)
strategic_recommender = load_module(
    "strategic_recommender",
    os.path.join(current_dir, "strategic-recommender.py")
)

RegulatoryComparisonGenerator = comparison_matrix_generator.RegulatoryComparisonGenerator
TimelineAnalyzer = timeline_analyzer.TimelineAnalyzer
StrategicRecommender = strategic_recommender.StrategicRecommender


def test_comparison_matrix():
    """Test comparison matrix generation"""
    print("Testing Comparison Matrix Generator...")
    generator = RegulatoryComparisonGenerator("regulatory-database-schema.json")

    matrix = generator.generate_comparison_matrix(
        device_class="Class II",
        target_markets=["FDA", "EU_MDR", "MFDS", "PMDA"],
        include_special_programs=True
    )

    assert "requirements_comparison" in matrix
    assert "missing_requirements" in matrix
    assert "conflicts" in matrix
    assert "harmonization_strategies" in matrix

    print(f"✅ Comparison matrix generated for {len(matrix['requirements_comparison'])} markets")
    print(f"✅ Found {len(matrix['conflicts'])} conflicts")
    print(f"✅ Generated {len(matrix['harmonization_strategies'])} harmonization strategies")

    return matrix


def test_timeline_analyzer():
    """Test timeline analysis"""
    print("\nTesting Timeline Analyzer...")
    analyzer = TimelineAnalyzer("regulatory-database-schema.json")

    analysis = analyzer.analyze_submission_sequencing(
        device_class="Class II",
        target_markets=["FDA", "EU_MDR", "MFDS", "PMDA"],
        submission_start_date="2025-03-01",
        available_resources="medium"
    )

    assert "sequencing_strategies" in analysis
    assert "recommended_strategy" in analysis
    assert "timeline_projection" in analysis
    assert "resource_allocation" in analysis

    print(f"✅ Recommended strategy: {analysis['recommended_strategy']['strategy_name']}")
    confidence = analysis['recommended_strategy'].get('confidence', 'N/A')
    print(f"✅ Confidence: {confidence}%")
    print(f"✅ Team size: {analysis['resource_allocation']['regulatory_affairs']['fte_required']} RA FTE")

    return analysis


def test_strategic_recommender():
    """Test strategic recommendations"""
    print("\nTesting Strategic Recommender...")
    recommender = StrategicRecommender("regulatory-database-schema.json")

    recommendations = recommender.generate_comprehensive_recommendations(
        device_class="Class II",
        target_markets=["FDA", "EU_MDR", "MFDS", "PMDA", "ANVISA"],
        submission_start_date="2025-03-01",
        available_resources="medium",
        strategic_priorities={"speed": 0.8, "cost": 0.5, "risk": 0.6}
    )

    assert "submission_strategy" in recommendations
    assert "market_prioritization" in recommendations
    assert "risk_mitigation" in recommendations
    assert "resource_optimization" in recommendations
    assert "action_items" in recommendations

    print(f"✅ Strategy: {recommendations['submission_strategy']['recommended_strategy']}")
    print(f"✅ Tier 1 markets: {len(recommendations['market_prioritization']['tier_1_markets'])}")
    print(f"✅ Action items: {len(recommendations['action_items'])}")

    return recommendations


def test_database_integrity():
    """Test database integrity"""
    print("\nTesting Database Integrity...")

    with open("regulatory-database-schema.json", "r") as f:
        database = json.load(f)

    assert "markets" in database
    assert "FDA" in database["markets"]
    assert "EU_MDR" in database["markets"]
    assert "MFDS" in database["markets"]
    assert "PMDA" in database["markets"]
    assert "ANVISA" in database["markets"]
    assert "Health_Canada" in database["markets"]

    print(f"✅ Database contains {len(database['markets'])} markets")

    # Check each market has required fields
    for market_code, market_data in database["markets"].items():
        assert "name" in market_data
        assert "region" in market_data
        assert "official_sources" in market_data
        assert "device_classifications" in market_data
        print(f"✅ {market_code}: {market_data['name']}")

    print(f"✅ Common conflicts: {len(database['common_conflicts'])}")


def test_end_to_end_workflow():
    """Test complete end-to-end workflow"""
    print("\n=== END-TO-END WORKFLOW TEST ===\n")

    # Step 1: Generate comparison matrix
    print("Step 1: Comparing regulatory requirements...")
    generator = RegulatoryComparisonGenerator("regulatory-database-schema.json")
    matrix = generator.generate_comparison_matrix(
        device_class="Class II",
        target_markets=["FDA", "EU_MDR", "MFDS", "PMDA"],
        include_special_programs=True
    )
    print(f"✅ Compared {len(matrix['requirements_comparison'])} markets\n")

    # Step 2: Analyze timelines
    print("Step 2: Analyzing submission timelines...")
    analyzer = TimelineAnalyzer("regulatory-database-schema.json")
    timeline_analysis = analyzer.analyze_submission_sequencing(
        device_class="Class II",
        target_markets=["FDA", "EU_MDR", "MFDS", "PMDA"],
        available_resources="medium"
    )
    strategy = timeline_analysis['recommended_strategy']['strategy_name']
    print(f"✅ Optimal strategy: {strategy}\n")

    # Step 3: Generate strategic recommendations
    print("Step 3: Generating strategic recommendations...")
    recommender = StrategicRecommender("regulatory-database-schema.json")
    recommendations = recommender.generate_comprehensive_recommendations(
        device_class="Class II",
        target_markets=["FDA", "EU_MDR", "MFDS", "PMDA"],
        available_resources="medium"
    )

    tier_1 = recommendations['market_prioritization']['tier_1_markets']
    print(f"✅ Tier 1 markets: {', '.join(tier_1)}\n")

    # Step 4: Generate reports
    print("Step 4: Generating formatted reports...")
    comparison_report = generator.generate_markdown_report(matrix)
    strategic_report = recommender.generate_markdown_report(recommendations)
    print(f"✅ Comparison report: {len(comparison_report)} characters")
    print(f"✅ Strategic report: {len(strategic_report)} characters\n")

    print("=== END-TO-END WORKFLOW TEST PASSED ✅ ===")


def main():
    """Run all tests"""
    print("=" * 60)
    print("Multi-Country Regulatory Strategy Comparison")
    print("Integration Test Suite")
    print("=" * 60)

    try:
        # Test individual components
        test_database_integrity()
        test_comparison_matrix()
        test_timeline_analyzer()
        test_strategic_recommender()

        # Test end-to-end workflow
        test_end_to_end_workflow()

        print("\n" + "=" * 60)
        print("ALL TESTS PASSED ✅")
        print("=" * 60)
        print("\nImplementation Status:")
        print("  ✅ Regulatory Database")
        print("  ✅ Comparison Matrix Generator")
        print("  ✅ Timeline Analyzer")
        print("  ✅ Strategic Recommendation Engine")
        print("\nMilestone 5: COMPLETE")

        return 0

    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
