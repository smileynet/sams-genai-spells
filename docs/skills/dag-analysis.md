# DAG Analysis — Skill Reference for AI Assistants

> Directed Acyclic Graphs for task dependency modeling. Use this reference when analyzing, validating, or restructuring task graphs.

## Good vs Bad DAG Structure

### Quality Metrics

| Metric | Healthy Range | Warning Sign |
|--------|--------------|--------------|
| **Parallelism ratio** (max-width / total-nodes) | 0.3–0.6 | < 0.2 = too serial, > 0.8 = likely missing deps |
| **Edge/node ratio** (edges / nodes) | 1.0–2.0 | < 0.8 = disconnected, > 3.0 = over-constrained |
| **Critical path ratio** (critical-path-length / total-nodes) | 0.3–0.5 | > 0.7 = over-serialized |
| **Max fan-in** (most deps on one node) | 1–4 | > 5 = potential bottleneck |
| **Max fan-out** (most dependents from one node) | 1–4 | > 5 = "god node" risk |

### What a Good DAG Looks Like

- **Wide, not tall**: Multiple tasks can execute in parallel at each level
- **Balanced fan-in/out**: No single node is a bottleneck
- **Explicit edges only**: Each dependency represents a real, necessary constraint
- **Transitive reduction applied**: No redundant edges (if A→B→C, remove A→C)

## Six Anti-Patterns

### 1. Overly Deep Chain
**Symptom:** Critical path ratio > 0.7. Nearly every task depends on the one before it.
**Fix:** Ask "does B *really* need A to finish first?" Often tasks share an input, not a dependency.

### 2. Unnecessary Dependencies
**Symptom:** Edge/node ratio > 3.0. Tasks have more dependencies than they need.
**Fix:** For each edge, ask: "If I removed this dependency, would the output change?" Remove if no.

### 3. Hidden Dependencies
**Symptom:** Tasks fail when run in parallel despite the graph saying they're independent.
**Fix:** Look for shared resources (files, databases, environment variables) that create implicit ordering.

### 4. Diamond Dependencies
**Symptom:** A→B, A→C, B→D, C→D — where B and C modify the same thing.
**Fix:** Make the merge explicit. Either serialize B and C, or add a reconciliation step before D.

### 5. Phantom Nodes
**Symptom:** Nodes with no inputs and no outputs (disconnected from the graph).
**Fix:** Either connect them or remove them. Orphan tasks are usually forgotten or misunderstood.

### 6. God Nodes
**Symptom:** One node with fan-in or fan-out > 5. Everything depends on it or it depends on everything.
**Fix:** Decompose into sub-tasks. A "deploy everything" node should become per-service deploys.

## Decomposition Strategies

When a graph exceeds 15 nodes or becomes hard to read, decompose it.

### Phase-Based Decomposition
Group tasks by execution phase (e.g., design → build → test → deploy). Each phase becomes a subgraph with a single entry and exit point.

**When to use:** Tasks naturally cluster into sequential stages.

### Component-Based Decomposition
Group tasks by system component (e.g., frontend, backend, database). Each component becomes a subgraph; cross-component edges become inter-subgraph dependencies.

**When to use:** Tasks are loosely coupled across components but tightly coupled within.

### Hierarchical Decomposition
Collapse a cluster of related tasks into a single summary node, with a separate sub-DAG for details. The summary node inherits the external dependencies.

**When to use:** Mixed phases and components; nested structure is the only way to manage complexity.

### Decomposition Limits

| Metric | Limit | Action |
|--------|-------|--------|
| Nodes per subgraph | ≤ 15 | Decompose further |
| Subgraph depth | ≤ 3 levels | Flatten or rethink structure |
| Max fan-in to subgraph | ≤ 4 | Split the subgraph |

## Validation Checklist

### Structural Checks
- [ ] No cycles (it's a DAG — cycles mean circular dependencies)
- [ ] Transitive reduction applied (no redundant edges)
- [ ] All nodes reachable from at least one root (no orphans)
- [ ] All nodes reach at least one terminal (no dead ends)

### Bottleneck Checks
- [ ] No node with fan-in > 5
- [ ] No node with fan-out > 5
- [ ] Critical path ratio < 0.7
- [ ] Parallelism ratio > 0.2

### Semantic Checks
- [ ] Every edge represents a real constraint ("B cannot start until A finishes")
- [ ] No implicit dependencies missing (shared resources, ordering assumptions)
- [ ] Node descriptions are actionable (verbs, not nouns)

### Scale Checks
- [ ] Total nodes ≤ 15 (or decomposed into subgraphs)
- [ ] Edge/node ratio between 0.8 and 3.0
- [ ] No level has more than 8 parallel tasks (readability limit)

## Reporting Template

Use this format when reporting DAG analysis results:

```
DAG ANALYSIS
══════════════════════════════════════════════════════════════

Nodes: <N>    Edges: <M>    Levels: <L>

METRICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Parallelism ratio:   <value>  (<assessment>)
Edge/node ratio:     <value>  (<assessment>)
Critical path ratio: <value>  (<assessment>)
Max fan-in:          <value>  (node: <name>)
Max fan-out:         <value>  (node: <name>)

CRITICAL PATH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<node1> → <node2> → ... → <nodeN>  (<L> steps)

ANTIPATTERNS DETECTED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- <antipattern>: <description and fix>
  (or "None detected")

PARALLELIZABLE WORK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Wave 1: <tasks>
Wave 2: <tasks>
...

RECOMMENDATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. <Most impactful improvement>
2. <Second improvement>
```
