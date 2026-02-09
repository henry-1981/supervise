---
name: aria
description: >
  Main entry point for ARIA workflows. Natural language interface for
  Medical Device RA/QA and business tasks.
allowed-tools: Task AskUserQuestion Read Glob Grep Bash
---

# /aria Command

ARIA's unified command interface for regulatory affairs and quality assurance workflows.

## Usage

```
/aria "natural language request"
/aria brief "task description"
/aria execute TASK-ID
/aria deliver TASK-ID
/aria search "query"
/aria status
```

## Subcommands

### Default (Natural Language)

When invoked with a natural language request, ARIA automatically routes through the Brief-Execute-Deliver pipeline.

Examples:
- `/aria "510(k) submission preparation"`
- `/aria "Perform risk analysis for this device"`
- `/aria "Create a CAPA for the complaint trend"`
- `/aria "Review this document for regulatory compliance"`
- `/aria "Find the latest FDA guidance on software validation"`
- `/aria "Prepare internal audit checklist"`

### brief

Start the Brief phase to scope and plan a task.

- Analyzes the request and identifies applicable regulations
- Collects device and market information from the user
- Creates an action plan with agent assignments
- Presents the plan for user approval before execution

Example: `/aria brief "Prepare 510(k) submission for our new monitor"`

### execute

Run the Execute phase for an active task.

- Delegates work to specialized agents per the approved plan
- Applies VALID quality checks at each stage
- Pauses at approval checkpoints for user confirmation

Example: `/aria execute TASK-001`

### deliver

Run the Deliver phase to finalize and output results.

- Runs final VALID quality gate
- Formats deliverables for the target audience
- Stores results in Notion (when configured)
- Provides next-step recommendations

Example: `/aria deliver TASK-001`

### search

Search for regulatory information, standards, guidance documents, or precedents.

- Searches FDA databases, standards references, and knowledge base
- Returns structured results with source citations
- Filters by market, standard, or document type

Example: `/aria search "predicate device for patient monitor class II"`

### status

Display current task progress and pending items.

- Shows active tasks and their current phase
- Lists pending approval checkpoints
- Displays upcoming deadlines

Example: `/aria status`

## Workflow

1. User submits a request via `/aria`
2. Orchestrator analyzes intent and routes to the appropriate workflow
3. BRIEF: Scope is defined and plan is presented for approval
4. EXECUTE: Specialized agents perform the work with quality gates
5. DELIVER: Final output is reviewed, formatted, and presented

## When to Use

| Scenario | Command |
|----------|---------|
| Start a new regulatory task | `/aria "description"` or `/aria brief "description"` |
| Continue work on an existing task | `/aria execute TASK-ID` |
| Finalize and deliver results | `/aria deliver TASK-ID` |
| Look up regulatory information | `/aria search "query"` |
| Check progress on tasks | `/aria status` |
