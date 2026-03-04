# Ritual: Architect

**Spells:** deep-dive → task-graph
**Type:** Sequential
**Plan mode:** Compatible

**Use when:** You need to understand how code works AND plan work on it. Deep-dive maps the architecture; task-graph turns understanding into an execution plan.

---

## Phase 1: deep-dive

Run `deep-dive` with the user's topic as the argument.

**Full spell execution** — run the entire deep-dive process without modification.

---

## Bridge: deep-dive → task-graph

**Extract** from deep-dive output:
- **ARCHITECTURE** — the Mermaid diagram showing module/component relationships
- **KEY FILES** — the most important files and their roles
- **DESIGN DECISIONS** — patterns and conventions the codebase follows
- **DATA FLOW** — how data moves through the system

**Reframe** as input for task-graph:
- Topic becomes: "plan the tasks for <user's work goal> on the <explored subsystem>"
- Context: Carry forward the key files (these become task locations), the design decisions (these become constraints on task approach), and the data flow (this informs dependency ordering — upstream changes must happen before downstream ones). The architecture diagram provides the dependency structure.

**Gate check:**
- If deep-dive produced a clear architecture map → proceed normally, task-graph will plan work informed by the structure
- If deep-dive found the codebase is too tangled to map clearly → reframe task-graph to start with "untangle <specific coupling>" as the first task, using deep-dive's findings to identify what needs decoupling
- If deep-dive found the scope is too large → stop and report to user; ask them to narrow the scope before planning work

**User checkpoint:** Present the bridge content and ask:
1. Proceed with task-graph using this framing
2. Modify the framing (adjust the work goal or scope)
3. Skip to synthesis (deep-dive output is sufficient)
4. Redirect to a different spell

---

## Phase 2: task-graph

Run `task-graph` with the reframed topic from the bridge.

**Full spell execution** — run the entire task-graph process without modification.

---

## Synthesis

Produce a synthesis that cross-references the two outputs:

**Convergent findings:** Where deep-dive's architecture map and task-graph's dependency ordering align (e.g., if the architecture shows module A depends on module B, and task-graph independently placed B's tasks before A's — that validates the plan).

**Divergent findings:** Where the architecture and the task plan tension each other (e.g., if task-graph suggests parallel work on components that deep-dive showed are tightly coupled — that's a risk).

**Emergent insights:** Patterns visible only in combination — the architecture map may reveal that the critical path runs through the most complex module, or that the parallelizable tasks happen to be in the best-understood areas (lower risk) while serial tasks are in poorly-understood areas (higher risk).
