## Summary

**Map task dependencies into execution order, or diagram a process workflow.** Uses directed acyclic graphs (DAGs), topological sorting, and critical path analysis to produce Mermaid diagrams with structured analysis. Operates in two modes depending on input.

**Arguments:** `$ARGUMENTS` (required) - Task list, process description, or file path

**Output:** Mermaid diagram + structured text analysis (to conversation, not files)

---

## Skill References

Before proceeding, load the relevant skill documents for reference:

Read the following files from the repository root:
- `docs/skills/dag-analysis.md`
- `docs/skills/topological-sort.md`
- `docs/skills/mermaid-flowcharts.md`

---

## Process

### Step 1: Determine Mode

Parse `$ARGUMENTS` to determine which mode to operate in:

| Input | Mode | What happens |
|-------|------|--------------|
| A task list, backlog, or "tasks" keyword | **Task Mapping** | Build dependency DAG, compute execution order |
| "process", "flow", "pipeline", "workflow" keyword | **Process Flow** | Diagram a workflow with decision points |
| A file path or "codebase" | **Task Mapping** | Scan codebase for TODOs/tasks, build DAG |

**If `$ARGUMENTS` is ambiguous:**
Ask the user whether they want to map task dependencies or diagram a process flow.

---

### Mode A: Task Mapping

Build a dependency graph, compute execution order, and identify the critical path.

**Step A1: Gather tasks**

Collect tasks from one of these sources:

1. **User-provided list:** Parse tasks and dependencies from `$ARGUMENTS`
2. **Codebase scan:**
   Search the codebase for TODO, FIXME, and task markers.
3. **Interactive:** If the task list is unclear, ask the user to list their tasks

For each task, capture:
- **Name** (short, actionable — verb phrase)
- **Dependencies** (what must finish before this can start)
- **Duration estimate** (optional — use 1 if unknown)

**Step A2: Identify dependencies**

For each pair of tasks, determine if a dependency exists. Rules:
- **Never invent dependencies** — only include dependencies the user stated or that are logically necessary
- If dependencies aren't explicit, ask the user: "Which of these tasks depend on others?"
- Look for signals: "after", "needs", "requires", "blocks", "then"
- Shared resources (same file, same service) suggest possible dependencies — flag but don't assume

**Step A3: Build and validate the DAG**

1. Construct the directed graph from tasks and dependencies
2. **Detect cycles:** If found, report immediately with the cycle path and stop — ask the user to resolve
3. **Apply transitive reduction:** Remove redundant edges (if A→B→C exists, remove A→C)
4. **Validate against checklist** from `docs/skills/dag-analysis.md`:
   - No orphan nodes, no dead ends
   - Fan-in/fan-out within limits
   - Edge/node ratio reasonable
5. **Check node count:** If > 15 nodes, suggest decomposition per the skill doc

**Step A4: Compute execution order**

Using the approach from `docs/skills/topological-sort.md`:

1. **Topological sort** (Kahn's algorithm with priority queue):
   - Priority: critical path > fan-out > duration > alphabetical
2. **Critical path:** Compute ES/EF/LS/LF for each task, identify slack-0 chain
3. **Parallel waves:** Group tasks by wave (level-based grouping)
   - Wave 1 = all tasks with no dependencies
   - Wave N = tasks whose last dependency completes in wave N-1

**Step A5: Output results**

Generate a Mermaid diagram following `docs/skills/mermaid-flowcharts.md` conventions:
- Direction: `flowchart TD` (dependencies flow top-down)
- Thick edges (`==>`) for critical path
- Dotted edges (`-.->`) for optional dependencies
- `classDef` for task status if status is known
- Subgraphs if > 15 nodes

Then output the structured analysis:

```
TASK DEPENDENCY GRAPH
══════════════════════════════════════════════════════════════

<Mermaid diagram in a ```mermaid code block>

EXECUTION ORDER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. <task>
2. <task>
...

CRITICAL PATH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<task> → <task> → ... → <task>  (<N> steps, determines overall duration)

PARALLELIZABLE WORK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Wave 1: <tasks that can start immediately>
Wave 2: <tasks available after wave 1>
Wave 3: ...

BOTTLENECKS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- <task>: <why it's a bottleneck — fan-in, fan-out, or critical path position>
  (or "None detected")
```

---

### Mode B: Process Flow

Diagram a workflow, pipeline, or process with decision points and parallel paths.

**Step B1: Gather steps**

1. Parse the process description from `$ARGUMENTS`
2. If the description is vague:
   Research standard patterns for the described process via web search.
3. For each step, capture:
   - **Name** (short, actionable)
   - **Type** (action, decision, start, end)
   - **Connections** (what comes next, including branch conditions)

**Step B2: Identify flow elements**

- **Decision points:** Where the flow branches based on a condition
- **Parallel paths:** Where multiple steps execute simultaneously
- **Error paths:** Where failures redirect the flow
- **Loops/retries:** Where the flow returns to an earlier step
- **Start/end:** Entry and exit points of the process

**Step B3: Output results**

Generate a Mermaid diagram following `docs/skills/mermaid-flowcharts.md` conventions:
- Direction: `flowchart LR` (process flows left-to-right)
- Stadium shapes `([...])` for start/end
- Diamond shapes `{...}` for decisions
- Rectangle shapes `[...]` for action steps
- Always label decision branches

Then output the structured analysis:

```
PROCESS FLOW: <PROCESS NAME>
══════════════════════════════════════════════════════════════

<Mermaid diagram in a ```mermaid code block>

STEPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. <step> — <description>
2. <step> — <description>
...

DECISION POINTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- <decision>: <branches and their conditions>

PARALLEL PATHS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- <which steps can execute simultaneously>
  (or "Sequential process — no parallel paths")

ERROR HANDLING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- <error conditions and how they're handled>
  (or "No explicit error paths identified")
```

---

## Guidelines

- **Max 15 nodes** per diagram. If you exceed this, use subgraphs or suggest decomposition.
- **Transitive reduction:** Always remove redundant edges. If A→B→C, don't also draw A→C.
- **Detect and report cycles:** Circular dependencies invalidate the graph. Report them and ask the user to resolve.
- **Never invent dependencies:** Only include what the user stated or what is logically necessary.
- **Mermaid direction:** `flowchart TD` for task deps, `flowchart LR` for process flows.
- **Quote special characters:** See `docs/skills/mermaid-flowcharts.md` for escaping rules.
- **Credit:** This spell applies techniques from graph theory (DAGs), the Critical Path Method (Kelley & Walker, 1957), and Kahn's topological sort (1962).

---

## Example Usage

```
@spell-task-graph design API, implement endpoints, write tests, deploy — tests need endpoints, deploy needs tests and API design
@spell-task-graph process for code review from PR creation to merge
@spell-task-graph scan codebase for TODOs and map dependencies
```
