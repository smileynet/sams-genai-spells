# The Task Graph Technique

## Where This Came From

In 1957, James Kelley and Morgan Walker were working at DuPont trying to figure out how to build chemical plants without everything taking forever. They came up with the Critical Path Method (CPM) — a way to map every task, figure out which ones depend on which, and identify the sequence that determines how long the whole project takes. The technique shaved months off construction schedules.

A year later, the U.S. Navy needed to build the Polaris submarine-launched ballistic missile. They developed PERT (Program Evaluation and Review Technique), a close cousin of CPM that added probabilistic time estimates. Polaris was delivered two years ahead of schedule. Whether that was because of PERT or because the Navy threw unlimited money at it is still debated.

Then in 1962, Arthur Kahn published "Topological sorting of large networks" — a clean algorithm for ordering nodes in a directed acyclic graph. If you've ever done a topological sort, you've used Kahn's algorithm (or the DFS variant). It's the foundation for build systems, package managers, and spreadsheet recalculation.

Sam didn't invent any of this. Sam just noticed that asking an AI "what order should I do these tasks in?" produces better results when you give it a formal framework for thinking about it.

## The Core Idea

Three concepts combine to make this work:

**Directed Acyclic Graphs (DAGs):** Your tasks are nodes. Dependencies are directed edges. "Task B needs Task A to finish first" becomes an arrow from A to B. The "acyclic" part means no circular dependencies — if A needs B and B needs A, something is wrong.

**Topological Sort:** Given a DAG, produce an ordering where every task comes after its dependencies. There might be multiple valid orderings (if tasks are independent, either can go first). The algorithm also naturally reveals which tasks can run in parallel — anything in the same "wave" has no dependencies between them.

**Critical Path:** The longest chain through the graph. This is the bottleneck — the sequence of tasks where a delay in any one delays the entire project. Everything not on the critical path has "slack" — room to slip without affecting the end date.

Put them together and you get: a visual map of what depends on what, a prioritized execution order, identification of what can be parallelized, and clarity on which tasks are the bottleneck.

## Why It Works With AI

AI assistants are surprisingly good at this, for a few specific reasons:

**They can hold the entire graph in memory.** Humans struggle to mentally track more than 5-7 dependencies at once. An AI can work with a 15-node graph and accurately compute the topological sort, critical path, and parallel waves without losing track.

**They generate Mermaid natively.** Mermaid is a text-based diagram format that AI models know well. Instead of describing a graph in words (which is confusing), the AI produces a diagram you can render immediately. The visual output catches errors that text descriptions hide.

**Structured output prevents hand-waving.** When you ask "what order should I do these tasks?", an AI might give you a reasonable-sounding but vague answer. When you ask it to produce a formal DAG with execution order, critical path, and parallel waves, there's no room for vagueness — the structure forces precision.

## How Sam Uses It

**Sprint planning:** Dump a list of tasks into the spell, specify which ones depend on each other. The output shows what to start first, what can be worked on in parallel, and which tasks are the bottleneck. Much faster than manually drawing dependency arrows on a whiteboard.

**Workflow documentation:** Need to document a deployment process, code review workflow, or onboarding procedure? The process flow mode produces a clean Mermaid diagram with decision points, parallel paths, and error handling. Beats writing 500 words of prose that nobody reads.

**CI/CD pipeline design:** Map out build stages, test suites, and deployment steps as a dependency graph. The critical path analysis shows where your pipeline is slowest and which stages could run in parallel.

**Dependency untangling:** When a project feels stuck — everything seems to depend on everything else — the spell forces you to make dependencies explicit. Often you discover that half the "dependencies" are just assumptions, and the critical path is much shorter than it felt.

## Beyond This Spell

The techniques behind this spell show up everywhere in computing:

- **Build systems** (Make, Bazel, Nx): Tasks are build targets, edges are file dependencies. Topological sort determines build order. Parallelism comes from independent targets.
- **Package managers** (npm, pip, cargo): Packages are nodes, version requirements are edges. The dependency resolver is computing a topological sort.
- **Spreadsheets:** Cells are nodes, formula references are edges. When you change a cell, the spreadsheet recomputes in topological order.
- **Git itself:** Commits form a DAG. Rebase is a topological operation. Merge-base computation walks the DAG.

For formal project management, the Critical Path Method is a core technique in PMBOK (the Project Management Body of Knowledge). If you want to go deep, that's the textbook.

## Further Reading

- [Critical Path Method](https://en.wikipedia.org/wiki/Critical_path_method) — Wikipedia's comprehensive overview of CPM
- [Kahn's Algorithm](https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm) — The original 1962 paper's approach, explained clearly
- [Mermaid Flowchart Documentation](https://mermaid.js.org/syntax/flowchart.html) — The diagramming tool this spell outputs to
- [PERT](https://en.wikipedia.org/wiki/Program_evaluation_and_review_technique) — CPM's probabilistic cousin, developed for the Polaris missile program
- [Graph Theory and Its Applications](https://www.routledge.com/Graph-Theory-and-Its-Applications/Gross-Yellen-Anderson/p/book/9781482249484) — If you want the math behind DAGs and topological sorting
