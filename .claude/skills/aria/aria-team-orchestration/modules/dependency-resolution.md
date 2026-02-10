# Dependency Resolution Module

Manages task dependency graphs, detects circular dependencies, and builds optimal execution waves.

## Dependency Graph

### Graph Structure

```python
class DependencyGraph:
    def __init__(self):
        self.nodes = {}      # task_id -> task
        self.edges = []      # (from_task, to_task)

    def add_task(self, task):
        self.nodes[task.id] = task

    def add_dependency(self, from_task, to_task):
        self.edges.append((from_task, to_task))

    def get_dependencies(self, task_id):
        """Get all tasks that task_id depends on"""
        return [to_task for (from_task, to_task) in self.edges
                if from_task == task_id]

    def get_dependents(self, task_id):
        """Get all tasks that depend on task_id"""
        return [from_task for (from_task, to_task) in self.edges
                if to_task == task_id]
```

### Example Graph

```
                synthesis
                    |
        +-----------+-----------+
        |           |           |
    fda-analysis eu-analysis korea-analysis
        |           |           |
    (none)     (none)     (none)
```

## Dependency Detection

### Automatic Dependency Detection

```python
def detect_dependencies(subtasks):
    """
    Automatically detect dependencies between subtasks

    Detection Rules:
    1. Synthesis tasks depend on all analysis tasks
    2. Review tasks depend on drafting tasks
    3. Risk tasks depend on clinical data tasks
    4. Compliance tasks depend on document tasks
    """

    dependencies = []

    for task in subtasks:
        # Rule 1: Synthesis depends on all non-synthesis tasks
        if task.task_type == "synthesis":
            for other in subtasks:
                if other.id != task.id and other.task_type != "synthesis":
                    dependencies.append((task.id, other.id))

        # Rule 2: Review depends on draft
        elif task.task_type == "review":
            for other in subtasks:
                if other.task_type == "draft":
                    dependencies.append((task.id, other.id))

        # Rule 3: Risk depends on clinical data
        elif task.task_type == "risk":
            for other in subtasks:
                if other.task_type == "clinical_data":
                    dependencies.append((task.id, other.id))

    return dependencies
```

### Manual Dependency Specification

```yaml
# Subtask can specify dependencies explicitly

subtask_spec:
  subtask_id: "compliance_check"
  description: "Regulatory compliance verification"
  dependencies:
    - "document_draft"     # Explicit dependency
    - "risk_assessment"    # Multiple dependencies
```

## Wave Builder

### Topological Sort Algorithm

```python
def build_execution_waves(subtasks, dependencies):
    """
    Group tasks into waves using topological sort

    Args:
        subtasks: List of all subtasks
        dependencies: List of (from_id, to_id) tuples

    Returns:
        waves: List of lists, where each inner list is a wave
    """

    # Build dependency graph
    graph = DependencyGraph()
    for task in subtasks:
        graph.add_task(task)

    for (from_id, to_id) in dependencies:
        graph.add_dependency(from_id, to_id)

    # Perform topological sort with wave grouping
    waves = []
    remaining = set(task.id for task in subtasks)

    while remaining:
        # Find tasks with no unmet dependencies
        ready = []

        for task_id in remaining:
            deps = graph.get_dependencies(task_id)
            unmet = [d for d in deps if d in remaining]

            if not unmet:
                ready.append(task_id)

        if not ready:
            raise CircularDependencyError(
                f"Circular dependency detected among: {remaining}"
            )

        # Create wave from ready tasks
        waves.append(ready)

        # Mark as completed
        for task_id in ready:
            remaining.remove(task_id)

    return waves
```

### Example Wave Building

**Input**:
```yaml
subtasks:
  - id: "A" (literature_search)
    deps: []
  - id: "B" (clinical_data)
    deps: []
  - id: "C" (risk_assessment)
    deps: ["B"]
  - id: "D" (document_draft)
    deps: ["A", "C"]
  - id: "E" (synthesis)
    deps: ["A", "B", "C", "D"]
```

**Process**:
1. Wave 1: Find tasks with no dependencies → A, B
2. Remove A, B from remaining
3. Wave 2: Find tasks with remaining deps met → C
4. Remove C from remaining
5. Wave 3: Find tasks with remaining deps met → D
6. Remove D from remaining
7. Wave 4: Find tasks with remaining deps met → E

**Output**:
```yaml
waves:
  - [A, B]      # Wave 1: No dependencies
  - [C]        # Wave 2: Depends on B (now complete)
  - [D]        # Wave 3: Depends on A, C (now complete)
  - [E]        # Wave 4: Depends on all (now complete)
```

## Circular Dependency Detection

### Detection Algorithm

```python
def detect_circular_dependencies(graph):
    """
    Detect cycles in dependency graph using DFS

    Returns:
        cycles: List of cycles found
    """

    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph.nodes}

    cycles = []

    def dfs(node, path):
        color[node] = GRAY

        for neighbor in graph.get_dependents(node):
            if color[neighbor] == GRAY:
                # Found cycle
                cycle_start = path.index(neighbor)
                cycles.append(path[cycle_start:] + [neighbor])

            if color[neighbor] == WHITE:
                dfs(neighbor, path + [node])

        color[node] = BLACK

    for node in graph.nodes:
        if color[node] == WHITE:
            dfs(node, [node])

    return cycles
```

### Cycle Resolution

When circular dependencies are detected:

1. **Report Error**: "Circular dependency: A → B → A"
2. **Suggest Break**: "Remove dependency: A → B or B → A"
3. **Request Decision**: Ask user which dependency to remove

```yaml
error_message: |
  Circular dependency detected:
  - Task A (literature_search) depends on Task B (clinical_data)
  - Task B (clinical_data) depends on Task A (literature_search)

  Resolution options:
  1. Remove A → B dependency
  2. Remove B → A dependency
  3. Split into iterative approach
```

## Dependency Validation

### Validation Checks

```python
def validate_dependencies(subtasks, dependencies):
    """
    Validate dependency configuration
    """

    errors = []

    # Check 1: All dependency targets exist
    for (from_id, to_id) in dependencies:
        if to_id not in [s.id for s in subtasks]:
            errors.append(f"Unknown dependency target: {to_id}")

    # Check 2: No self-dependencies
    for (from_id, to_id) in dependencies:
        if from_id == to_id:
            errors.append(f"Self-dependency: {from_id}")

    # Check 3: No circular dependencies
    graph = build_graph(subtasks, dependencies)
    cycles = detect_circular_dependencies(graph)
    if cycles:
        errors.append(f"Circular dependencies: {cycles}")

    return errors
```

## Optimal Wave Reordering

### Load Balancing

For tasks within a wave, optimize order based on:

1. **Estimated Duration**: Longer tasks first
2. **Agent Availability**: Balance agent load
3. **User Priority**: User-specified priority

```python
def optimize_wave_order(wave):
    """Optimize task execution order within a wave"""

    # Sort by estimated duration (longest first)
    wave.sort(key=lambda t: t.estimated_duration, reverse=True)

    # Consider agent load balancing
    agent_load = count_agent_tasks(wave)
    wave.sort(key=lambda t: agent_load[t.agent])

    return wave
```
