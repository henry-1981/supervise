---
name: aria-workflows
description: >
  Complete workflow implementations for Medical Device RA/QA professionals including
  Clinical Evaluation (MEDDEV 2.7.1 rev 4), Internal Audit (ISO 13485), and
  Post-Market Surveillance (EU MDR Article 83-85) with state machine management,
  step-by-step guidance, and context preservation.
license: Apache-2.0
compatibility: Designed for Claude Code with ARIA plugin
allowed-tools: Read Write Edit Grep Glob Bash TaskCreate TaskUpdate TaskList TaskGet AskUserQuestion
user-invocable: true
metadata:
  version: "1.0.0"
  category: "domain"
  status: "active"
  updated: "2026-02-09"
  modularized: "true"
  tags: "medical-device, regulatory, workflow, clinical-evaluation, audit, pms"
  author: "ARIA Team"
  context: "Milestone 4: Complete Workflows implementation for SPEC-ARIA-005"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 150
  level2_tokens: 8000

# MoAI Extension: Triggers
triggers:
  keywords: ["clinical evaluation", "internal audit", "post-market surveillance", "PMS", "CER", "CAPA", "PSUR", "FSCA", "MEDDEV", "ISO 13485", "EU MDR"]
  agents: ["expert-clinical", "expert-audit", "expert-pms", "orchestrator"]
  phases: ["run"]
---

# ARIA Workflows

Complete workflow implementations for Medical Device RA/QA professionals with state machine management and step-by-step guidance.

## Workflow State Machine

All ARIA workflows follow a unified state machine pattern:

### State Definition

```yaml
workflow_state:
  workflow_id: string
  workflow_type: "clinical_evaluation" | "internal_audit" | "post_market_surveillance"
  current_stage: string
  status: "not_started" | "in_progress" | "completed" | "on_hold" | "cancelled"
  progress: integer  # 0-100
  context: object
  history: array
  created_at: timestamp
  updated_at: timestamp
```

### State Transitions

```
not_started → in_progress: Workflow initiated
in_progress → in_progress: Stage progression
in_progress → on_hold: User interruption
on_hold → in_progress: Resume
in_progress → completed: All stages finished
any → cancelled: User cancellation
```

### Context Preservation

Each workflow maintains context across stages:

```yaml
workflow_context:
  device_identification: {}
  regulatory_requirements: []
  collected_data: {}
  generated_documents: []
  decisions_made: []
  flags: []
```

## Clinical Evaluation Workflow (MEDDEV 2.7.1 rev 4)

### State Machine

```yaml
clinical_evaluation_workflow:
  stages:
    - stage: "scope_definition"
      status: "pending"
      required_inputs:
        - device_name
        - intended_use
        - device_class
      outputs:
        - scope_document

    - stage: "literature_search"
      status: "pending"
      required_inputs:
        - search_strategy
        - databases
        - keywords
      outputs:
        - literature_summary
        - gap_analysis

    - stage: "data_analysis"
      status: "pending"
      required_inputs:
        - clinical_data
        - equivalence_assessment
      outputs:
        - analysis_report
        - benefit_risk_profile

    - stage: "cer_generation"
      status: "pending"
      required_inputs:
        - all_previous_outputs
      outputs:
        - cer_document
        - pmcf_requirements
```

### Stage 1: Scope Definition

**Purpose**: Define clinical evaluation scope per MEDDEV 2.7.1 rev 4, Section 1.1

**Guidance Questions**:
1. What is the device name and model?
2. What is the intended use and indications for use?
3. What is the device classification (I, IIa, IIb, III)?
4. What are the clinical safety and performance objectives?

**Data Collection**:
```yaml
scope_data:
  device_identification:
    name: string
    model: string
    manufacturer: string
    intended_use: string
    indications: [string]
    contraindications: [string]

  clinical_objectives:
    safety_performance: [string]
    target_patient_population: string
    clinical_benefits: [string]
    known_risks: [string]
```

**Validation Criteria**:
- Device identification complete
- Clinical objectives clearly defined
- Target population specified
- Benefit-risk profile outlined

### Stage 2: Literature Search

**Purpose**: Conduct systematic literature search per MEDDEV 2.7.1 rev 4, Section 5

**Guidance Questions**:
1. What databases will be searched? (PubMed, Google Scholar, Cochrane, etc.)
2. What is the search strategy with MeSH terms?
3. What inclusion/exclusion criteria apply?
4. What is the publication date range?

**Search Strategy Template**:
```yaml
literature_search:
  databases:
    - name: "PubMed"
      url: "https://pubmed.ncbi.nlm.nih.gov"
      search_query: ""
    - name: "Google Scholar"
      url: "https://scholar.google.com"
      search_query: ""
    - name: "Cochrane Library"
      url: "https://www.cochranelibrary.com"
      search_query: ""

  search_strategy:
    keywords: [string]
    mesh_terms: [string]
    boolean_operators: "AND | OR | NOT"
    inclusion_criteria: [string]
    exclusion_criteria: [string]
    date_range: "YYYY-MM to YYYY-MM"
    language_filter: ["English"]

  results:
    total_studies: integer
    included_studies: integer
    excluded_studies: integer
    prisma_flow_diagram: file_path
```

**Gap Analysis**:
```yaml
gap_analysis:
  identified_gaps:
    - clinical_domain: string
      gap_description: string
      severity: "critical | major | minor"
      pmcf_required: boolean
      suggested_investigation: string
```

### Stage 3: Data Analysis

**Purpose**: Analyze clinical data and assess equivalence per MEDDEV 2.7.1 rev 4, Section 6

**Guidance Questions**:
1. What equivalent devices are identified?
2. What is the equivalence justification?
3. What clinical data supports safety and performance?
4. What is the benefit-risk ratio?

**Analysis Framework**:
```yaml
data_analysis:
  equivalence_assessment:
    predicate_devices:
      - name: string
        manufacturer: string
        similarity_technical: "high | medium | low"
        similarity_clinical: "high | medium | low"
        justification: string

    clinical_data:
      studies:
        - study_id: string
          design: "RCT | Cohort | Case Control | Case Series"
          sample_size: integer
          endpoints: [string]
          results: string
          quality_rating: "high | medium | low"

  benefit_risk_analysis:
    clinical_benefits:
      - benefit: string
        evidence_level: string
        magnitude: "significant | moderate | minimal"

    risks:
      - risk: string
        probability: "high | medium | low"
        severity: "serious | moderate | mild"
        mitigation: string

    overall_assessment: "favorable | unfavorable | requires_pmcf"
```

### Stage 4: CER Generation

**Purpose**: Generate Clinical Evaluation Report per MEDDEV 2.7.1 rev 4, Annex XV

**CER Structure**:
```markdown
# Clinical Evaluation Report

## 1. Scope and Objectives
[Content from Stage 1]

## 2. Literature Search Strategy
[Content from Stage 2]

## 3. Clinical Data Analysis
[Content from Stage 3]

## 4. Equivalence Assessment
[Content from Stage 3]

## 5. Benefit-Risk Analysis
[Content from Stage 3]

## 6. Conclusions
- Clinical safety demonstrated: Yes/No
- Clinical performance demonstrated: Yes/No
- Overall benefit-ratio profile: Favorable/Unfavorable/Requires PMCF

## 7. PMCF Requirements
[List required post-market clinical follow-up activities]

## Appendix
- Literature search results
- Study quality assessments
- Data extraction tables
```

**PMCF Flagging**:
```yaml
pmcf_requirements:
  required: boolean
  justification: string
  activities:
    - activity: string
      timeline: string
      success_criteria: string
```

### Progress Indicators

```yaml
progress_tracking:
  stage_1_scope_definition:
    steps:
      - Device identification: "pending | in_progress | completed"
      - Clinical objectives: "pending | in_progress | completed"
      - Target population: "pending | in_progress | completed"
      - Benefit-risk outline: "pending | in_progress | completed"
    completion_threshold: 100%  # All steps completed

  stage_2_literature_search:
    steps:
      - Search strategy design: "pending | in_progress | completed"
      - Database searches: "pending | in_progress | completed"
      - Screening and selection: "pending | in_progress | completed"
      - Gap analysis: "pending | in_progress | completed"
    completion_threshold: 100%

  stage_3_data_analysis:
    steps:
      - Equivalence assessment: "pending | in_progress | completed"
      - Clinical data appraisal: "pending | in_progress | completed"
      - Benefit-risk analysis: "pending | in_progress | completed"
    completion_threshold: 100%

  stage_4_cer_generation:
    steps:
      - Report drafting: "pending | in_progress | completed"
      - Review and validation: "pending | in_progress | completed"
      - PMCF requirements identification: "pending | in_progress | completed"
    completion_threshold: 100%
```

## Internal Audit Workflow (ISO 13485)

### State Machine

```yaml
internal_audit_workflow:
  stages:
    - stage: "audit_planning"
      status: "pending"
      required_inputs:
        - audit_scope
        - audit_criteria
        - previous_findings
      outputs:
        - audit_agenda
        - checklists

    - stage: "audit_execution"
      status: "pending"
      required_inputs:
        - audit_agenda
        - checklists
      outputs:
        - findings_document
        - evidence_records

    - stage: "capa_planning"
      status: "pending"
      required_inputs:
        - findings
      outputs:
        - capa_plan
        - root_cause_analysis

    - stage: "verification"
      status: "pending"
      required_inputs:
        - capa_plan
      outputs:
        - effectiveness_report
```

### Stage 1: Audit Planning

**Purpose**: Generate comprehensive audit agenda based on risk areas

**Guidance Questions**:
1. What is the audit scope (departments, processes, clauses)?
2. What is the audit duration and available resources?
3. What were previous audit findings?
4. What are the current quality indicators?

**Agenda Generation Algorithm**:
```python
def generate_audit_audit_agenda(
    audit_scope: dict,
    previous_findings: list,
    quality_indicators: dict
) -> dict:
    """
    Generate audit agenda prioritized by risk areas.

    Priority Factors:
    - Repeat findings from previous audits (weight: 3x)
    - Critical nonconformities (weight: 2x)
    - Trending quality issues (weight: 1.5x)
    - High-risk processes (weight: 1.2x)
    """

    # Identify risk areas
    risk_areas = []

    # Check for repeat findings
    for finding in previous_findings:
        if finding.is_repeat():
            risk_areas.append({
                'area': finding.process_area,
                'priority': 'HIGH',
                'justification': f"Repeat finding: {finding.description}",
                'weight': 3.0
            })

    # Check critical processes
    for clause in audit_scope.clauses:
        if clause.is_critical_process():
            risk_areas.append({
                'area': clause.process,
                'priority': 'MEDIUM-HIGH',
                'justification': 'Critical process per ISO 13485',
                'weight': 1.2
            })

    # Sort by priority weight
    risk_areas.sort(key=lambda x: x['weight'], reverse=True)

    # Generate time allocations
    total_audit_hours = calculate_total_hours(audit_scope)
    agenda = allocate_time_slots(risk_areas, total_audit_hours)

    return agenda
```

**Agenda Template**:
```yaml
audit_agenda:
  metadata:
    audit_id: "AUD-2025-001"
    date: "YYYY-MM-DD"
    auditor: string
    scope: [string]

  schedule:
    - time_slot: "09:00 - 10:30"
      area: "Management Responsibility"
      iso_clause: "5.1-5.6"
      priority: "HIGH"
      activities:
        - Review quality policy
        - Review quality objectives
        - Review authority and responsibility

    - time_slot: "10:45 - 12:00"
      area: "Resource Management"
      iso_clause: "6.1-6.3"
      priority: "MEDIUM"
      activities:
        - Review competency records
        - Review infrastructure maintenance
        - Review work environment
```

### Stage 2: Audit Execution

**Purpose**: Document findings with evidence and categorization

**Finding Categorization**:
```yaml
finding_categories:
  critical:
    definition: "Total breakdown of QMS or serious regulatory risk"
    examples:
      - No design control process
      - No CAPA process
      - No management review
    escalation: "Immediate notification to top management"

  major:
    definition: "Significant nonconformity affecting product quality"
    examples:
      - Design validation not performed
      - Supplier not qualified
      - CAPA not verified for effectiveness
    escalation: "Notification to quality manager"

  minor:
    definition: "Isolated nonconformity with limited impact"
    examples:
      - Document not signed
      - Training record missing
      - Form version outdated
    escalation: "Document for corrective action"

  observation:
    definition: "Opportunity for improvement"
    examples:
      - Process could be optimized
      - Best practice not implemented
    escalation: "Suggestion for improvement"
```

**Finding Documentation Template**:
```yaml
finding_record:
  finding_id: "FIND-2025-001"
  category: "critical | major | minor | observation"
  iso_clause: string
  process_area: string

  description:
    what_was_observed: string
    what_should_be: string
    evidence: [string]

  root_cause_analysis:
    method: "5_whys | fishbone | ishikawa"
    findings:
      - causal_factor: string
        contributing_factors: [string]
    root_cause: string

  repeat_check:
    is_repeat: boolean
    previous_finding_id: string
    repeat_count: integer
```

### Stage 3: CAPA Planning

**Purpose**: Develop CAPA plans with root cause analysis

**Root Cause Analysis Methods**:

**5 Whys Method**:
```yaml
five_whys_analysis:
  problem_statement: string

  whys:
    - why_1: "Why did this happen?"
      answer: string
    - why_2: "Why did [answer from why_1] occur?"
      answer: string
    - why_3: "Why did [answer from why_2] occur?"
      answer: string
    - why_4: "Why did [answer from why_3] occur?"
      answer: string
    - why_5: "Why did [answer from why_4] occur?"
      answer: string

  root_cause: "Answer from why_5"
  systemic_issue_identified: boolean
```

**Fishbone (Ishikawa) Diagram**:
```yaml
fishbone_analysis:
  problem_statement: string

  categories:
    man:
      - "Training inadequate?"
      - "Competency lacking?"
      - "Communication failure?"
    machine:
      - "Equipment failure?"
      - "Tool not calibrated?"
      - "Software bug?"
    material:
      - "Raw material defect?"
      - "Component failure?"
      - "Spec not met?"
    method:
      - "Process not defined?"
      - "Procedure not followed?"
      - "Work instruction unclear?"
    environment:
      - "Temperature/humidity issue?"
      - "Lighting inadequate?"
      - "Workspace constraints?"
    management:
      - "Resource allocation?"
      - "Leadership oversight?"
      - "Policy inadequacy?"

  most_likely_causes: [string]
  root_cause: string
```

**CAPA Plan Template**:
```yaml
capa_plan:
  capa_id: "CAPA-2025-001"
  related_finding_id: string
  priority: "critical | major | minor"
  target_completion_date: date

  corrective_action:
    immediate_action: string
    containment_action: string
    responsible_person: string
    due_date: date
    status: "pending | in_progress | completed"

  preventive_action:
    systemic_correction: string
    process_update_required: boolean
    document_updates: [string]
    responsible_person: string
    due_date: date
    status: "pending | in_progress | completed"

  verification:
    verification_method: string
    effectiveness_criteria: string
    verification_date: date
    verified_by: string
    effectiveness_confirmed: boolean
```

### Stage 4: Verification and Trend Analysis

**Purpose**: Verify CAPA effectiveness and identify systemic issues

**Repeat Finding Detection**:
```yaml
repeat_finding_detection:
  algorithm: |
    1. Compare current findings with historical database
    2. Match by:
       - ISO 13485 clause
       - Process area
       - Nonconformity type
    3. Flag if:
       - Same finding occurred in last 3 audits
       - Same finding not closed effectively

  systemic_issue_flags:
    - trigger: "3+ findings in same process area"
      action: "Review process design"
    - trigger: "Repeat finding across multiple departments"
      action: "Review training program"
    - trigger: "Critical finding in management responsibility"
      action: "Executive leadership review"
```

**Trend Analysis**:
```yaml
audit_trends:
  findings_by_clause:
    - iso_clause: "8.3 Design and Development"
      finding_count: integer
      trend: "increasing | stable | decreasing"
      repeat_rate: float

  findings_by_department:
    - department: "R&D"
      finding_count: integer
      trend: "increasing | stable | decreasing"

  capa_effectiveness:
    total_capas: integer
    closed_on_time: integer
    effectiveness_verified: integer
    repeat_finding_rate: float

  continuous_improvement_opportunities:
    - opportunity: string
      priority: "high | medium | low"
      suggested_action: string
```

### Progress Indicators

```yaml
progress_tracking:
  stage_1_audit_planning:
    steps:
      - Scope definition: "pending | in_progress | completed"
      - Risk assessment: "pending | in_progress | completed"
      - Agenda generation: "pending | in_progress | completed"
      - Checklist preparation: "pending | in_progress | completed"
    completion_threshold: 100%

  stage_2_audit_execution:
    steps:
      - Opening meeting: "pending | in_progress | completed"
      - Document review: "pending | in_progress | completed"
      - Process interviews: "pending | in_progress | completed"
      - Finding documentation: "pending | in_progress | completed"
      - Closing meeting: "pending | in_progress | completed"
    completion_threshold: 100%

  stage_3_capa_planning:
    steps:
      - Root cause analysis: "pending | in_progress | completed"
      - Corrective action planning: "pending | in_progress | completed"
      - Preventive action planning: "pending | in_progress | completed"
      - CAPA approval: "pending | in_progress | completed"
    completion_threshold: 100%

  stage_4_verification:
    steps:
      - CAPA implementation monitoring: "pending | in_progress | completed"
      - Effectiveness verification: "pending | in_progress | completed"
      - Trend analysis: "pending | in_progress | completed"
      - Management review: "pending | in_progress | completed"
    completion_threshold: 100%
```

## Post-Market Surveillance Workflow (EU MDR Article 83-85)

### State Machine

```yaml
pms_workflow:
  stages:
    - stage: "data_collection"
      status: "pending"
      required_inputs:
        - data_sources
        - collection_frequency
      outputs:
        - pms_data_repository
        - incident_reports

    - stage: "trend_analysis"
      status: "pending"
      required_inputs:
        - pms_data
        - statistical_thresholds
      outputs:
        - trend_report
        - statistical_significance_results

    - stage: "reporting"
      status: "pending"
      required_inputs:
        - trend_analysis
        - reporting_period
      outputs:
        - psur_document
        - regulatory_notifications

    - stage: "fsca_trigger"
      status: "pending"
      condition: "safety_issue_detected"
      required_inputs:
        - safety_incident
        - risk_assessment
      outputs:
        - fsca_plan
        - field_safety_notice
```

### Stage 1: PMS Data Collection

**Purpose**: Collect post-market data from multiple sources

**Data Sources**:
```yaml
pms_data_sources:
  complaint_handling:
    source: "Customer complaint database"
    data_points:
      - complaint_description
      - product_id
      - lot_number
      - complaint_date
      - severity
      - outcome
    collection_method: "Continuous"

  adverse_events:
    source: "Adverse event reporting system"
    data_points:
      - event_description
      - patient_impact
      - device_involved
      - reporter
      - event_date
    collection_method: "Real-time"

  service_reports:
    source: "Field service records"
    data_points:
      - service_request
      - malfunction_description
      - repair_action
      - service_date
    collection_method: "Weekly aggregation"

  literature_monitoring:
    source: "PubMed, journals, conferences"
    data_points:
      - publication_title
      - device_mentioned
      - safety_concerns
      - publication_date
    collection_method: "Monthly review"

  feedback:
    source: "HCP and user feedback"
    data_points:
      - usability_issues
      - performance_concerns
      - suggestions
    collection_method: "Continuous"

  registries:
    source: "Clinical registries (if applicable)"
    data_points:
      - patient_outcomes
      - device_performance
      - complications
    collection_method: "Quarterly"
```

**Data Collection Template**:
```yaml
pms_data_record:
  record_id: "PMS-2025-001"
  source: string
  collection_date: date

  device_identification:
    device_name: string
    model: string
    serial_number: string
    lot_number: string
    implant_date: date  # if applicable

  event_information:
    event_type: "complaint | adverse_event | malfunction | literature"
    description: string
    severity: "serious | non-serious"
    patient_impact: "death | serious_injury | minor_injury | none"

  reporter_information:
    reporter_type: "healthcare_professional | patient | manufacturer | other"
    contact_provided: boolean

  initial_assessment:
    requires_regulatory_reporting: boolean
    requires_capa: boolean
    requires_trend_monitoring: boolean
    assigned_investigator: string
```

### Stage 2: Trend Analysis

**Purpose**: Detect statistically significant trends in PMS data

**Statistical Analysis Framework**:
```python
def analyze_pms_trends(
    pms_data: list,
    baseline_period: str = "12 months",
    current_period: str = "3 months"
) -> dict:
    """
    Analyze PMS data for statistically significant trends.

    Statistical Methods:
    1. Time series analysis for frequency trends
    2. Chi-square test for categorical distribution changes
    3. CUSUM (Cumulative Sum) for detecting small shifts
    4. Funnel plot for comparing lot-to-lot variation
    """

    # Calculate baseline statistics
    baseline_stats = calculate_baseline(pms_data, baseline_period)

    # Calculate current period statistics
    current_stats = calculate_current(pms_data, current_period)

    # Perform statistical tests
    trend_results = {
        'complaint_rate': test_complaint_rate_change(baseline_stats, current_stats),
        'severity_distribution': test_severity_shift(baseline_stats, current_stats),
        'lot_variation': test_lot_clustering(pms_data),
        'geographical_clustering': test_geographical_clustering(pms_data)
    }

    # Flag significant trends
    flagged_trends = []
    for trend_name, result in trend_results.items():
        if result['p_value'] < 0.05:  # 95% confidence level
            flagged_trends.append({
                'trend': trend_name,
                'significance': result['p_value'],
                'direction': result['direction'],
                'magnitude': result['effect_size'],
                'requires_action': True
            })

    return {
        'baseline': baseline_stats,
        'current': current_stats,
        'trends': trend_results,
        'flagged_trends': flagged_trends
    }
```

**Trend Reporting Template**:
```yaml
trend_report:
  report_id: "TREND-2025-Q1"
  reporting_period: "YYYY-MM to YYYY-MM"
  generated_at: timestamp

  summary_statistics:
    total_pms_records: integer
    serious_incidents: integer
    complaint_rate: float  # per 1000 devices
    incident_rate: float   # per 1000 devices

  trend_analysis:
    complaint_trends:
      - metric: "Overall complaint rate"
        baseline_value: float
        current_value: float
        change_percent: float
        p_value: float
        significant: boolean
        action_required: boolean

    severity_trends:
      - severity_level: "serious | non-serious"
        count_current_period: integer
        count_baseline_period: integer
        change_percent: float
        statistical_significance: boolean

    lot_analysis:
      - lot_number: string
        complaint_count: integer
        expected_range: [float, float]
        outside_expected_range: boolean
        action_required: boolean

    geographical_analysis:
      - region: string
        complaint_count: integer
        rate_per_1000: float
        cluster_detected: boolean
        action_required: boolean

  flagged_items:
    - flag_type: "statistical_trend | lot_cluster | geographical_cluster | safety_signal"
      description: string
      severity: "critical | high | medium | low"
      recommended_action: string
      deadline: date
      assigned_to: string
```

### Stage 3: PSUR Generation

**Purpose**: Generate Periodic Safety Update Report per EU MDR Annex XIII

**PSUR Structure** (per Annex XIII):
```markdown
# Periodic Safety Update Report (PSUR)

## 1. Device Identification and Manufacture
- Device name and trade name
- Device model and catalogue number
- UDI-DI (if applicable)
- Manufacturer information

## 2. Summary of Safety and Performance
- Overall benefit-risk profile
- Summary of conclusions
- Changes to benefit-risk profile

## 3. Sales Volume and Estimate of Usage
- Number of devices sold
- Number of devices in use
- Patient population size

## 4. Information from PMS
- Summary of PMS activities
- Complaint statistics
- Adverse event summary
- Trend analysis results
- Serious incidents breakdown

## 5. Relevant Publications
- Summary of relevant scientific literature
- Clinical study updates
- Registry data (if applicable)

## 6. Related Field Safety Corrective Actions (FSCA)
- FSCA initiated during reporting period
- FSCA effectiveness status

## 7. Summary of Trend Analysis
- Statistically significant trends
- Benefit-risk impact
- Actions taken or planned

## 8. Conclusions
- Overall safety conclusion
- Recommendations for continued monitoring
- Actions required to maintain safety

## 9. Appendix
- Detailed data tables
- Trend analysis charts
- References
```

**PSUR Data Compilation**:
```yaml
psur_data_compilation:
  period: "YYYY-MM to YYYY-MM"
  report_date: date

  device_identification:
    device_name: string
    udi_di: string
    device_class: "I | IIa | IIb | III"

  sales_and_usage:
    units_sold: integer
    units_in_use: integer
    patient_population: integer
    geographical_distribution: {region: count}

  pms_summary:
    total_pms_records: integer
    complaints: integer
    adverse_events: integer
    serious_incidents: integer
    non_serious_incidents: integer

  incident_breakdown:
    - incident_type: string
      count: integer
      rate_per_1000: float
      trend: "increasing | stable | decreasing"

  fsca_summary:
    fsca_initiated: integer
    fsca_closed: integer
    fsca_ongoing: integer

  trend_summary:
    significant_trends: integer
    safety_issues_identified: integer
    actions_required: integer
```

### Stage 4: FSCA Trigger Workflow

**Purpose**: Trigger Field Safety Corrective Action when safety issues detected

**FSCA Trigger Criteria**:
```yaml
fsca_trigger_criteria:
  automatic_triggers:
    - condition: "Death or serious injury reported"
      action: "Immediate FSCA assessment"
      timeline: "Within 24 hours"

    - condition: "Statistically significant increase in serious incidents"
      action: "Trend analysis and potential FSCA"
      timeline: "Within 5 days"

    - condition: "Lot-specific clustering of complaints"
      action: "Lot recall assessment"
      timeline: "Within 3 days"

    - condition: "Regulatory authority request for information"
      action: "Prepare FSCA if needed"
      timeline: "As requested"

  manual_triggers:
    - "New safety information from literature"
    - "Competitor device recalls in same category"
    - "Field service identifies recurring malfunction"
    - "Healthcare provider reports safety concerns"
```

**FSCA Assessment Process**:
```yaml
fsca_assessment:
  incident_id: string
  assessment_date: date

  incident_description:
    what_happened: string
    when_occurred: date
    patient_impact: string
    devices_affected: [string]
    lots_affected: [string]

  risk_assessment:
    hazard: string
    harm: string
    probability: "high | medium | low"
    severity: "serious | moderate | mild"
    risk_level: "acceptable | mitigated | unacceptable"

  regulatory_assessment:
    reportable_to_authorities: boolean
    reporting_deadlines:
      - authority: "Competent Authority"
        deadline: "10 days for serious incidents"
      - authority: "Notified Body"
        deadline: "Per agreement"
      - authority: "Other NBs (recipients)"
        deadline: "As required"

  fsca_decision:
    fsca_required: boolean
    fsca_type: "field_safety_notice | safety_alert | recall | advisory_notice"
    scope: "national | international"
    affected_markets: [string]
```

**FSCA Plan Template**:
```yaml
fsca_plan:
  fsca_id: "FSCA-2025-001"
  initiation_date: date

  action_summary:
    action_type: string
    scope: string
    affected_devices: [string]
    affected_lots: [string]
    estimated_quantity: integer

  communications_plan:
    field_safety_notice:
      draft_date: date
      distribution_date: date
      recipients: [string]
      content_summary: string

    regulatory_notifications:
      - authority: string
        notification_type: string
        deadline: date
        status: "pending | submitted | acknowledged"

  corrective_actions:
    immediate_actions:
      - action: string
        responsible: string
        deadline: date

    long_term_actions:
      - action: string
        responsible: string
        deadline: date

  effectiveness_checks:
    check_method: string
    check_frequency: string
    success_criteria: string
```

### Timeline Compliance Tracking

```yaml
timeline_tracking:
  serious_incident_reporting:
    - event: "Initial report to Competent Authority"
      timeline: "Within 10 days of becoming aware"
      consequence: "Regulatory non-compliance"

    - event: "Report to Notified Body"
      timeline: "Per NB agreement, typically 5-10 days"
      consequence: "Non-compliance with MDR Article 87"

    - event: "Report to other NBs where device distributed"
      timeline: "As required, typically within 10 days"
      consequence: "Non-compliance with MDR Article 87"

  fsca_deadlines:
    - event: "FSCA assessment completion"
      timeline: "Within 5 days of safety issue identification"
      consequence: "Delayed corrective action"

    - event: "Field Safety Notice distribution"
      timeline: "As soon as practicable"
      consequence: "Continued patient risk"
```

### Progress Indicators

```yaml
progress_tracking:
  stage_1_data_collection:
    steps:
      - Source configuration: "pending | in_progress | completed"
      - Data intake setup: "pending | in_progress | completed"
      - Validation rules: "pending | in_progress | completed"
      - Initial data collection: "pending | in_progress | completed"
    completion_threshold: 100%

  stage_2_trend_analysis:
    steps:
      - Data aggregation: "pending | in_progress | completed"
      - Statistical analysis: "pending | in_progress | completed"
      - Trend identification: "pending | in_progress | completed"
      - Report generation: "pending | in_progress | completed"
    completion_threshold: 100%

  stage_3_reporting:
    steps:
      - PSUR data compilation: "pending | in_progress | completed"
      - PSUR drafting: "pending | in_progress | completed"
      - Regulatory review: "pending | in_progress | completed"
      - PSUR submission: "pending | in_progress | completed"
    completion_threshold: 100%

  stage_4_fsca_trigger:
    steps:
      - Safety issue detection: "pending | in_progress | completed"
      - FSCA assessment: "pending | in_progress | completed"
      - Communications planning: "pending | in_progress | completed"
      - Corrective action execution: "pending | in_progress | completed"
    completion_threshold: 100%
    condition: "safety_issue_detected"
```

## Back Navigation Support

All workflows support returning to previous stages:

```yaml
navigation_rules:
  forward_navigation:
    - condition: "Current stage completed"
      action: "Proceed to next stage"
      validation: "All required outputs present"

    - condition: "Stage skipped with justification"
      action: "Skip to future stage"
      validation: "Justification documented"

  backward_navigation:
    - condition: "User requests to revisit previous stage"
      action: "Return to specified stage"
      context_preservation: "Maintain all current stage data"

    - condition: "New information affects previous stage"
      action: "Prompt user to revisit stage"
      context_preservation: "Update previous stage with new information"

  stage_skipping:
    - condition: "Stage already completed externally"
      requirement: "Evidence of completion"
      action: "Mark stage complete, proceed"

    - condition: "Stage not applicable to current device"
      requirement: "Justification for non-applicability"
      action: "Document and skip stage"
```

## State Persistence

```yaml
state_persistence:
  storage_location: ".claude/agent-memory/aria/workflows/"

  file_format: "JSON"

  auto_save:
    enabled: true
    trigger: "Stage completion"
    backup_frequency: "Every 5 minutes"

  state_recovery:
    - scenario: "Session interruption"
      action: "Restore last saved state on resume"

    - scenario: "System crash"
      action: "Recover from backup"

    - scenario: "User cancellation"
      action: "Save state for potential resumption"
```

## Integration with Templates

Workflows integrate with ARIA templates (Milestone 6):

```yaml
template_integration:
  clinical_evaluation_workflow:
    templates:
      - "cer-template.md"
      - "pmcf-plan-template.md"
      - "clinical-investigation-plan-template.md"
    usage: "Generate documents at workflow completion"

  internal_audit_workflow:
    templates:
      - "internal-audit-checklist-template.md"
      - "audit-report-template.md"
      - "capa-procedure-template.md"
    usage: "Generate documents throughout workflow"

  post_market_surveillance_workflow:
    templates:
      - "psur-template.md"
      - "field-safety-notice-template.md"
      - "trend-report-template.md"
    usage: "Generate documents at workflow completion"
```
