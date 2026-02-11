# Topological Sort & Scheduling — Skill Reference for AI Assistants

> Algorithms for ordering tasks with dependencies. Use this reference when computing execution order, critical paths, and parallel scheduling waves.

## Algorithm Selection

### Kahn's Algorithm (BFS-based)
**Prefer for:** Scheduling, execution order, parallel wave grouping.

1. Compute in-degree for every node
2. Enqueue all nodes with in-degree 0
3. While queue is not empty:
   - Dequeue node (using priority queue for deterministic ordering)
   - Add to sorted output
   - For each neighbor: decrement in-degree; if 0, enqueue
4. If sorted output has fewer nodes than the graph → cycle detected

**Why Kahn's for scheduling:** Naturally produces level-based grouping. Nodes dequeued in the same round can execute in parallel.

### DFS-based Topological Sort
**Prefer for:** Critical path analysis, dependency chain exploration.

1. Mark all nodes unvisited
2. For each unvisited node: DFS, pushing to stack on finish
3. Reverse stack = topological order
4. Cycle detection: if you visit a node that's in-progress (on the current DFS path) → cycle

**Why DFS for critical path:** Naturally follows the longest chains, making it easier to accumulate path weights.

## Critical Path Method (CPM)

### Computing CPM

**Forward pass** (earliest times):
- ES (Earliest Start) = max(EF of all predecessors), or 0 for root nodes
- EF (Earliest Finish) = ES + duration

**Backward pass** (latest times):
- LF (Latest Finish) = min(LS of all successors), or EF for terminal nodes
- LS (Latest Start) = LF - duration

**Slack** = LS - ES (or LF - EF, same value)

**Critical path** = all nodes where slack = 0

### Practical Meaning

| Value | What It Tells You |
|-------|-------------------|
| **ES** | Soonest this task can begin (all deps satisfied) |
| **EF** | Soonest this task can finish |
| **LS** | Latest this task can start without delaying the project |
| **LF** | Latest this task can finish without delaying the project |
| **Slack** | How much this task can slip without affecting end date |
| **Critical path** | The sequence of tasks that determines project duration — delay any one and the whole project slips |

### When Tasks Lack Duration Estimates

If durations are unknown, use unit duration (1) for all tasks. The critical path becomes the longest chain by node count, which still identifies the bottleneck sequence.

## Level-Based Grouping (Parallel Waves)

### Wave Algorithm

1. Run Kahn's algorithm, but track which "wave" each node belongs to
2. Wave 0 = all root nodes (in-degree 0)
3. Wave N = nodes whose last predecessor was in wave N-1
4. Each wave's tasks can execute in parallel

### Within-Wave Ordering

When multiple tasks are in the same wave, order them by priority:

1. **Critical path first**: Tasks on the critical path get priority (slack = 0)
2. **Longest Processing Time (LPT)**: Longer tasks first (start them early to maximize parallelism)
3. **Fan-out**: Tasks that unblock more successors go first
4. **Deterministic tie-break**: Alphabetical by task name (for reproducible output)

### Example

```
Wave 1:  [A, B, C]     ← all independent, start together
Wave 2:  [D, E]         ← D needs A; E needs A and B
Wave 3:  [F]            ← F needs D and E
Wave 4:  [G]            ← G needs C and F
```

## Priority Rules Summary

When choosing which task to schedule next (e.g., in a priority queue for Kahn's):

| Priority | Rule | Rationale |
|----------|------|-----------|
| 1 | Critical path (slack = 0) | Delay here delays everything |
| 2 | Higher fan-out | Unblocks more downstream work |
| 3 | Longer duration | Start long tasks early |
| 4 | Alphabetical name | Reproducible, deterministic output |

## Edge Case Handling

### Multiple Valid Orderings
Topological sort is not unique — many valid orderings may exist. Use the priority rules above to produce a single deterministic order. Always note when multiple valid orderings exist (it means there's scheduling flexibility).

### Optional Dependencies
Some dependencies are "nice to have" but not blocking. Model these as:
- Dotted edges in the diagram (visual distinction)
- Excluded from critical path computation
- Included in the ideal execution order but allowed to be violated

### Cycle Detection
If a cycle is detected:
1. **Report it immediately** — cycles in a task graph mean circular dependencies
2. **Identify the cycle** — list the nodes involved (e.g., A→B→C→A)
3. **Suggest resolution** — usually one edge in the cycle is wrong or should be an optional dependency
4. **Do not silently ignore cycles** — they invalidate the entire topological sort

### Disconnected Components
If the graph has disconnected components (groups of tasks with no dependencies between them):
- Sort each component independently
- They can execute in any interleaving
- Note the independence in the output ("these groups are fully independent")

## Anti-Patterns

### Over-Serialization
**Symptom:** Long critical path with few parallel waves.
**Cause:** Adding dependencies "just to be safe."
**Fix:** For each edge, prove the dependency is real. Remove speculative ordering.

### Missing Transitive Dependencies
**Symptom:** Tasks fail when run in the computed order.
**Cause:** An implicit dependency wasn't captured as an edge.
**Fix:** Check for shared resources, files, or environment state between tasks.

### Redundant Explicit Dependencies
**Symptom:** Edge/node ratio is high; graph looks cluttered.
**Cause:** Explicitly stating A→C when A→B→C already exists.
**Fix:** Apply transitive reduction — remove edges implied by longer paths.
