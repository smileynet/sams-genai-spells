# Task Graphs, Critical Paths, and Topological Sort

## The Problem

You have twelve tasks for a project. You write them in a list and start working top to bottom. Halfway through task 4, you discover it depends on task 9, which you haven't started yet. You switch to task 9, but that needs output from task 7. The list looked organized — but the dependencies were invisible, and you've been doing busywork while the actual bottleneck sat untouched.

The second problem is false sequentiality. You have three tasks that could run in parallel — they don't depend on each other at all — but because they're in a list, you work through them one at a time. A flat list implies an order even when none exists. The tasks that *could* have happened simultaneously take three times as long because the format obscured the parallelism.

The third problem is optimizing the wrong thing. You spend a week making the deployment script faster — shaving it from 10 minutes to 2. Meanwhile, the test suite takes 45 minutes and blocks every other stage. You optimized a task that wasn't on the critical path. The deployment script had slack; the test suite was the bottleneck. Without a map of the full dependency chain, you can't tell which improvements actually matter for the end-to-end timeline.

## How It Helps

Model the tasks as a graph: each task is a node, each dependency is an arrow. "Task B needs Task A to finish first" becomes an arrow from A to B. Now three concepts from operations research and computer science give you everything you need:

**Directed Acyclic Graphs (DAGs):** Your tasks are nodes, dependencies are directed edges. The "acyclic" part means no circular dependencies — if A needs B and B needs A, something is wrong with the plan, not the tool.

**Topological Sort:** Given a DAG, produce an ordering where every task comes after its dependencies. There might be multiple valid orderings — the algorithm also reveals which tasks can run in parallel (anything in the same "wave" has no dependencies between them).

**Critical Path:** The longest chain through the graph. This is the bottleneck — the sequence where a delay in any one task delays the entire project. Everything not on the critical path has "slack" — room to slip without affecting the end date.

Put them together: a visual map of what depends on what, a prioritized execution order, identification of what can be parallelized, and clarity on which tasks are the bottleneck.

## Why It Works

The formalism forces precision that narrative planning doesn't. You can hand-wave about dependencies in a bullet list — "we should probably do X before Y" — but you can't hand-wave when you have to draw arrows. Either task B depends on task A or it doesn't. The graph makes implicit assumptions explicit.

The specific benefits:

- **Execution order** that respects all dependencies — no surprises mid-task
- **Parallelism opportunities** that aren't obvious from a flat list
- **Bottleneck identification** through critical path analysis — optimize the thing that actually matters
- **Forced precision** — you can't draw a circular dependency without the tool telling you something is wrong with the plan

AI assistants are particularly good at this because they can hold an entire dependency graph in memory (humans struggle past 5-7 nodes), compute topological sorts accurately, and generate Mermaid diagrams natively. The structured output prevents vague "just do these in order" answers.

## In Practice

**Build systems.** Make, Bazel, and Nx all model builds as task graphs. Source files are nodes, compilation dependencies are edges, and the build system computes a topological sort to determine build order. Independent targets build in parallel automatically — Bazel can saturate all available CPU cores because it knows exactly which targets have no dependencies between them. When a build is slow, the critical path tells you which target to optimize: it's not the one that takes the longest in isolation, it's the one on the longest dependency chain. Build engineers who understand this focus their optimization work on the critical path and ignore targets with slack — even if those targets are individually slow.

**CI/CD pipelines.** A deployment pipeline is a task graph: build, then test, then deploy — with stages that can fan out and merge. Understanding the dependency structure reveals which stages could run in parallel (linting and unit tests don't depend on each other) and where the critical path lies (if the integration test suite takes 45 minutes and nothing else can proceed until it passes, that's your bottleneck). Teams that model their pipelines as graphs routinely cut deployment times by running independent stages in parallel — something that's obvious on the graph but invisible in a sequential YAML file.

## The Command

The `/spell:task-graph` command applies these concepts in two modes:

**Task dependency mode:** Dump a list of tasks, specify dependencies. The output shows topological execution order, parallel waves, critical path, and a Mermaid diagram. Faster than manually drawing dependency arrows on a whiteboard.

**Process flow mode:** Describe a workflow (deployment, code review, onboarding). The output produces a Mermaid diagram with decision points, parallel paths, and error handling.

Both modes produce structured output — a formal DAG with execution order, not a vague narrative about what to do first.

## Background

In 1957, James Kelley and Morgan Walker at DuPont developed the Critical Path Method (CPM) to figure out how to build chemical plants more efficiently. The technique shaved months off construction schedules. A year later, the U.S. Navy developed PERT (Program Evaluation and Review Technique) for the Polaris submarine-launched ballistic missile program. Polaris was delivered two years ahead of schedule. In 1962, Arthur Kahn published "Topological sorting of large networks" — a clean algorithm for ordering nodes in a directed acyclic graph. These three techniques — CPM, PERT, and topological sort — became the foundation for modern build systems, package managers, and project management tools. Spreadsheets use the same principle: cells are nodes, formula references are edges, and when you change a cell, the spreadsheet recomputes in topological order — which is why circular references are errors.

## Further Reading

- [Critical Path Method](https://en.wikipedia.org/wiki/Critical_path_method) — Wikipedia's comprehensive overview of CPM
- [Kahn's Algorithm](https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm) — The original 1962 approach, explained clearly
- [Mermaid Flowchart Documentation](https://mermaid.js.org/syntax/flowchart.html) — The diagramming tool the spell outputs to
- [PERT](https://en.wikipedia.org/wiki/Program_evaluation_and_review_technique) — CPM's probabilistic cousin
- [Graph Theory and Its Applications](https://www.routledge.com/Graph-Theory-and-Its-Applications/Gross-Yellen-Anderson/p/book/9781482249484) — The math behind DAGs and topological sorting
