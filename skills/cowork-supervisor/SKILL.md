---
name: cowork-supervisor
description: >
  Strategic orchestrator for Cowork multi-plugin coordination. Receives user prompts,
  clarifies intent through iterative questioning, discovers available plugin capabilities,
  creates execution plans, orchestrates multiple plugins, and aggregates results.
  Use when users need to combine multiple business plugins (Finance, Legal, Marketing,
  Data, etc.) to solve complex problems.
license: Apache-2.0
compatibility: Designed for Claude Code and Cowork
allowed-tools: Task AskUserQuestion Read Glob Grep
metadata:
  version: "1.0.0"
  category: "workflow"
  status: "active"
  updated: "2026-02-04"
  user-invocable: "true"
  tags: "supervisor, orchestrator, multi-plugin, cowork, coordination"
  argument-hint: "\"natural language task description\""

progressive_disclosure:
  enabled: true
  level1_tokens: 150
  level2_tokens: 3000

triggers:
  keywords:
    - "supervisor"
    - "orchestrate"
    - "coordinate"
    - "multiple plugins"
    - "combine"
    - "cross-domain"
    - "multi-domain"
  agents:
    - "supervisor"
  phases:
    - "plan"
    - "run"
---

# Cowork Supervisor

Strategic orchestrator that coordinates multiple Cowork plugins to solve complex user requests.

## When to Use

- User needs analysis spanning multiple domains (Finance + Legal + Marketing)
- Task requires data from multiple plugins
- User describes a complex goal without specifying which plugins to use
- Cross-domain insights are needed

## Architecture

```
User Prompt
    |
    v
[Intent Clarifier] --> Clarified Intent Document
    |
    v
[Capability Discoverer] --> Capability Matrix
    |
    v
[Supervisor Planner] --> Execution Plan
    |
    v
[Orchestra] --> Execution Results
    |
    v
[Aggregator] --> Final Response
```

## Core Components

| Component | Purpose |
|-----------|---------|
| Intent Clarifier | Transform vague prompts into precise specifications |
| Capability Discoverer | Scan and catalog available plugin capabilities |
| Supervisor Planner | Create execution plans mapping tasks to plugins |
| Orchestra | Execute plans, dispatch to plugins, handle failures |
| Aggregator | Combine multi-plugin results into coherent response |

## Execution Flow

### Phase 1: Intent Clarification

Supervisor delegates to intent-clarifier agent which:
- Captures original prompt
- Identifies ambiguities (Scope, Domain, Priority, Constraints)
- Asks clarifying questions via AskUserQuestion
- Produces Clarified Intent Document

### Phase 2: Capability Discovery

Supervisor delegates to capability-discoverer agent which:
- Reads installed plugins registry
- Scans marketplace directories
- Builds capability matrix with domain and keyword indexes

### Phase 3: Planning

Supervisor delegates to supervisor-planner agent which:
- Decomposes intent into discrete tasks
- Maps tasks to plugins based on capability matching
- Determines parallel vs sequential execution
- Defines fallback strategies

User approves plan before execution.

### Phase 4: Orchestration

Supervisor delegates to orchestra agent which:
- Executes plan phases in order
- Dispatches tasks to plugins via Task()
- Handles failures with retry/fallback/skip strategies
- Collects results for aggregation

### Phase 5: Aggregation

Supervisor delegates to aggregator agent which:
- Merges non-overlapping results
- Synthesizes cross-domain insights
- Resolves conflicts with explicit reasoning
- Formats final response with source attribution

## User Interaction Points

1. **After Clarification**: Confirm understanding
2. **After Planning**: Approve execution plan
3. **On Error**: Choose recovery action
4. **After Completion**: Select next steps

## Example Usage

**User**: "Analyze our main competitor's position - I need to understand their financial health and any IP risks"

**Supervisor Flow**:
1. Clarifies: Which competitor? What aspects? Timeframe?
2. Discovers: Finance plugin, Legal plugin available
3. Plans: Parallel data gathering, then parallel analysis
4. Orchestrates: Dispatches to Finance and Legal plugins
5. Aggregates: Combines financial health + IP analysis + cross-domain insights

**Output**: Comprehensive competitive analysis with source attribution

## Execution Directive

When this skill is activated:

1. Parse $ARGUMENTS for task description
2. Delegate to intent-clarifier for clarification
3. Delegate to capability-discoverer for plugin discovery
4. Delegate to supervisor-planner for plan creation
5. Present plan to user via AskUserQuestion
6. On approval, delegate to orchestra for execution
7. Delegate to aggregator for result synthesis
8. Present final response in user's conversation_language
9. Offer next steps via AskUserQuestion

## Available Agents

- supervisor: Main orchestrator entry point
- intent-clarifier: Clarification specialist
- capability-discoverer: Plugin discovery specialist
- supervisor-planner: Execution planning specialist
- orchestra: Multi-plugin coordination specialist
- aggregator: Result synthesis specialist
