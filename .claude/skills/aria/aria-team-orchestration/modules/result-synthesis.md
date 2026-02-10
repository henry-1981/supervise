# Result Synthesis Module

Combines outputs from multiple parallel agents into unified deliverables with VALID framework compliance.

## Synthesis Templates

### Multi-Market Strategy Template

```yaml
synthesis_template:
  document_title: "Multi-Market Regulatory Strategy"
  output_format: "markdown"

  sections:
    - section_id: "executive_summary"
      title: "Executive Summary"
      source: "synthesis"
      content:
        - "Device overview"
        - "Target markets summary"
        - "Recommended pathway for each market"
        - "Unified timeline"

    - section_id: "fda_strategy"
      title: "FDA 510(k) Strategy"
      source: "fda-analysis"
      content:
        - "Regulatory pathway"
        - "Predicate device selection"
        - "Key requirements"
        - "Timeline estimate"

    - section_id: "eu_strategy"
      title: "EU MDR CE Mark Strategy"
      source: "eu-analysis"
      content:
        - "Regulatory pathway"
        - "Classification determination"
        - "Key requirements"
        - "Timeline estimate"

    - section_id: "korea_strategy"
      title: "Korea MFDS Strategy"
      source: "korea-analysis"
      content:
        - "Regulatory pathway"
        - "Classification determination"
        - "Key requirements"
        - "Timeline estimate"

    - section_id: "timeline_synthesis"
      title: "Unified Timeline"
      source: "synthesis"
      content:
        - "Parallel execution opportunities"
        - "Critical path"
        - "Milestone alignment"
        - "Resource requirements"
```

### Clinical Evaluation Report Template

```yaml
synthesis_template:
  document_title: "Clinical Evaluation Report"
  output_format: "markdown"

  sections:
    - section_id: "executive_summary"
      title: "Executive Summary"
      source: "synthesis"
      content:
        - "Device description"
        - "Clinical evaluation conclusion"
        - "Key findings summary"

    - section_id: "literature_review"
      title: "Literature Review"
      source: "literature-search"
      content:
        - "Search strategy"
        - "Key studies identified"
        - "Evidence summary"

    - section_id: "clinical_data"
      title: "Clinical Data Analysis"
      source: "clinical-data"
      content:
        - "Data sources"
        - "Analysis methods"
        - "Key findings"

    - section_id: "predicate_analysis"
      title: "Predicate Device Analysis"
      source: "predicate-analysis"
      content:
        - "Predicate devices identified"
        - "Substantial equivalence"
        - "Key differences"

    - section_id: "risk_assessment"
      title: "Risk Assessment"
      source: "risk-assessment"
      content:
        - "Risk analysis summary"
        - "Risk-benefit analysis"
        - "Residual risks"

    - section_id: "cer_conclusion"
      title: "Clinical Evaluation Conclusion"
      source: "synthesis"
      content:
        - "Safety and performance summary"
        - "Clinical benefit determination"
        - "Regulatory compliance statement"
```

## Synthesis Engine

### Data Collection

```python
def collect_subtask_results(subtasks):
    """
    Collect outputs from all completed subtasks

    Returns:
        results: Dictionary mapping subtask_id to output
    """

    results = {}

    for subtask in subtasks:
        if subtask.status == "completed":
            # Read output file
            results[subtask.id] = read_output_file(subtask.output_location)

        elif subtask.status == "failed":
            results[subtask.id] = {
                "status": "failed",
                "error": subtask.error_message
            }

        elif subtask.status == "pending":
            results[subtask.id] = {
                "status": "skipped",
                "reason": "Not executed due to dependency failure"
            }

    return results
```

### Content Generation

```python
def generate_synthesis(template, results):
    """
    Generate synthesized document from template and results

    Args:
        template: Synthesis template
        results: Collected subtask results

    Returns:
        document: Synthesized document
    """

    document = {
        "title": template.document_title,
        "sections": [],
        "metadata": {
            "generated_at": datetime.now(),
            "subtask_count": len(results),
            "completion_rate": calculate_completion_rate(results)
        }
    }

    for section in template.sections:
        section_content = generate_section(section, results)
        document["sections"].append(section_content)

    return document
```

### Section Generation

```python
def generate_section(section_spec, results):
    """
    Generate individual section content

    Args:
        section_spec: Section specification from template
        results: Collected subtask results

    Returns:
        section: Generated section content
    """

    if section_spec.source == "synthesis":
        # Generate from synthesis logic
        content = synthesize_section(section_spec, results)

    elif section_spec.source in results:
        # Extract from specific subtask result
        subtask_result = results[section_spec.source]
        content = extract_section(subtask_result, section_spec)

    else:
        # Section source not available
        content = generate_placeholder(section_spec)

    return {
        "section_id": section_spec.section_id,
        "title": section_spec.title,
        "content": content,
        "source": section_spec.source
    }
```

## VALID Framework Integration

### Dimension Verification

```python
def validate_synthesized_document(document):
    """
    Validate document against VALID framework

    Returns:
        validation_result: VALID compliance check
    """

    validation = {
        "verified": False,
        "accurate": False,
        "linked": False,
        "inspectable": False,
        "deliverable": False
    }

    # V: Verified - Check regulation citations
    validation["verified"] = verify_regulation_citations(document)

    # A: Accurate - Check data and references
    validation["accurate"] = verify_data_accuracy(document)

    # L: Linked - Check traceability
    validation["linked"] = verify_traceability(document)

    # I: Inspectable - Check audit trail
    validation["inspectable"] = verify_audit_trail(document)

    # D: Deliverable - Check format compliance
    validation["deliverable"] = verify_format_compliance(document)

    return validation
```

### Validation Details

**Verified (V)**:
```python
def verify_regulation_citations(document):
    """Ensure all claims cite source regulations"""

    citations = extract_citations(document)
    for citation in citations:
        # Check citation format
        if not valid_citation_format(citation):
            return False

        # Check regulation exists
        if not regulation_exists(citation):
            return False

    return True
```

**Accurate (A)**:
```python
def verify_data_accuracy(document):
    """Ensure data and references are correct"""

    # Check dates are current
    # Check numerical values are correct
    # Check references resolve
    # Check no contradictions

    return True
```

**Linked (L)**:
```python
def verify_traceability(document):
    """Ensure traceability between sections"""

    # Build traceability matrix
    # Check all requirements traced to evidence
    # Check all evidence cited in conclusions

    return True
```

**Inspectable (I)**:
```python
def verify_audit_trail(document):
    """Ensure decision rationale is documented"""

    # Check all decisions have rationale
    # Check synthesis logic is documented
    # Check assumptions are stated

    return True
```

**Deliverable (D)**:
```python
def verify_format_compliance(document):
    """Ensure output meets submission format"""

    # Check template conformance
    # Check required sections present
    # Check formatting guidelines

    return True
```

## Error Handling

### Missing Subtask Output

```python
def handle_missing_output(subtask_id, results):
    """Handle case where subtask output is missing"""

    # Option 1: Use placeholder
    placeholder = generate_placeholder(subtask_id)

    # Option 2: Exclude section
    if subtask_id == "critical_section":
        raise SynthesisError(f"Critical section {subtask_id} missing")

    # Option 3: Use alternative source
    alternative = find_alternative_source(subtask_id)

    return placeholder
```

### Conflicting Information

```python
def resolve_conflicts(results):
    """Resolve conflicting information from different subtasks"""

    conflicts = detect_conflicts(results)

    for conflict in conflicts:
        # Log conflict
        log_warning(f"Conflict detected: {conflict.description}")

        # Resolution strategy
        if conflict.type == "timeline_mismatch":
            # Use latest estimate
            resolution = resolve_by_latest(conflict)

        elif conflict.type == "contradictory_claims":
            # Flag for user review
            resolution = flag_for_review(conflict)

        elif conflict.type == "different_classifications":
            # Use most conservative classification
            resolution = use_most_conservative(conflict)

        apply_resolution(resolution)
```

## Output Formatting

### Markdown Format

```python
def format_markdown(document):
    """Format document as Markdown"""

    output = f"# {document['title']}\n\n"

    for section in document['sections']:
        output += f"## {section['title']}\n\n"
        output += section['content']
        output += "\n\n"

    # Add metadata
    output += "---\n"
    output += f"Generated: {document['metadata']['generated_at']}\n"
    output += f"Completion Rate: {document['metadata']['completion_rate']}%\n"

    return output
```

### Word Format

```python
def format_word(document, template_path):
    """Format document as Word using template"""

    # Load template
    template = load_word_template(template_path)

    # Fill template
    for section in document['sections']:
        template.fill_section(section.section_id, section.content)

    # Save
    template.save(document['output_path'])

    return document['output_path']
```
