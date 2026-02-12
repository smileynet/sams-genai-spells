# Codebase Exploration & Program Comprehension

## The Problem

You join a new project. There's a `src/` directory with 200 files, a few outdated README fragments, and a Slack message from 2023 that says "the architecture doc is in Confluence somewhere." You need to add a feature to the billing module. Where is the billing module? What calls it? What does it call? What are the key types? You open a random file, start reading, get lost in a utility function three levels deep, and realize 20 minutes later that you're reading the test helper for a module you don't care about.

AI assistants don't help much here. Ask "how does billing work?" and you'll get a grep for "billing", a list of file names, and maybe a summary of the first file the AI happened to read. There's no systematic exploration: no tracing the data flow from entry point to database, no mapping which modules depend on which, no identifying the key abstractions that make the system comprehensible. You get a bag of facts instead of a map.

The result is that developers spend hours building mental models through trial and error — opening files, grepping, getting distracted, backtracking. Studies of professional developers show they spend 60-70% of their time reading and understanding code, not writing it. And most of that reading is unstructured: start somewhere, follow a thread, lose it, start again.

## How It Helps

Program comprehension research has identified how expert developers read code — and it's not by starting at line 1 and reading sequentially. Experts use a top-down strategy: find the entry points (public APIs, route handlers, main functions), understand what the system exposes to the outside world, then trace inward along call chains and data flows. They build a mental model of the system's architecture before reading any implementation details.

This spell packages that strategy into a structured process:

1. **Determine scope** — What exactly are we exploring? A module, a feature, a question?
2. **Map the landscape** — How many files? What structure? What frameworks? Where are the boundaries?
3. **Trace the architecture** — Start at entry points, follow calls, track data flow, identify patterns and abstractions.
4. **Report** — Structured output: overview, architecture diagram, key files, data flow, design decisions, entry points.

The output is a map, not a pile of file contents. It tells you what the system does, how it's organized, where data flows, and what patterns it follows — the things you need to know before you can work in it productively.

## Why It Works

Program comprehension research consistently shows that strategy matters more than raw reading ability. A 1995 study by von Mayrhauser and Vans identified three mental models developers build when understanding code: a top-down model (what the system is supposed to do), a bottom-up model (what the code actually does), and a situation model (how the domain maps to the code). Expert developers switch fluidly between these models. Novices get stuck in bottom-up reading — line by line, function by function — and never build the top-down understanding that makes everything else make sense.

The key findings:

- **Entry points first.** Starting at the public API gives you a framework to organize everything else. Without that framework, you're memorizing disconnected facts.
- **Follow data, not control flow.** Understanding what data moves through a system reveals more than tracing every branch and loop. Data flow shows purpose; control flow shows mechanism.
- **Scope aggressively.** You can't understand an entire large codebase at once. Focus on one subsystem, understand it well, then expand. Breadth without depth is just a file listing.
- **Name the patterns.** Recognizing that a system uses MVC or event-driven architecture immediately tells you how it's organized, where to find things, and what conventions to expect. Pattern recognition is the expert's shortcut.

## In Practice

**Onboarding at a new job.** Every developer's first weeks involve building mental models of unfamiliar codebases. The traditional approach — read code, ask colleagues, attend architecture talks — works but is slow and unstructured. Companies with good onboarding docs are rare; companies with up-to-date onboarding docs are rarer. Systematic exploration produces a current, accurate map of the system as it actually is, not as someone documented it two years ago.

**Open source contribution.** You want to contribute to an open source project. The README explains how to use it, not how it works internally. You need to understand the codebase well enough to make a meaningful contribution, but you can't spend weeks on it. A focused exploration of the subsystem you want to change — its entry points, data flow, and design patterns — gives you enough context to write a good PR without becoming a project expert.

**Code review of unfamiliar modules.** You're asked to review a PR that touches a module you've never worked in. Reading just the diff isn't enough — you need to understand the module's architecture to evaluate whether the changes make sense. A quick exploration of the module's structure and patterns gives you the context to review effectively.

**Legacy system archaeology.** The system has been in production for years. The original authors have left. The docs are wrong. Nobody knows why certain design decisions were made. Systematic exploration — tracing entry points, mapping dependencies, identifying patterns — reconstructs the architecture from the code itself, which is always the source of truth.

## The Command

The `/spell:deep-dive <target>` command applies program comprehension techniques:

1. Parses the target (file path, module name, feature description, or question) and determines what to explore
2. Surveys the landscape — file counts, directory structure, languages, frameworks, module boundaries
3. Traces the architecture top-down — entry points, call chains, data flow, key abstractions, design decisions
4. Produces a structured report: overview, Mermaid architecture diagram, key files with roles, data flow, design decisions, and entry points

The process adjusts based on input. A file path starts the exploration at that location. A question ("how does auth work?") starts by finding where auth is implemented. A module name starts by finding its boundaries. The output is always the same structured format — a map you can reference while working.

## Background

Program comprehension has been studied since the 1970s. Ben Shneiderman's early work (1976) identified that programmers build internal mental models of programs, not just parse syntax. Letovsky's protocol studies (1987) showed that developers interleave three activities: reading code, forming hypotheses about what it does, and testing those hypotheses by reading more code.

Von Mayrhauser and Vans (1995) unified these findings into a three-model framework: the program model (what the code does), the domain model (what the real-world problem is), and the situation model (how the code maps to the domain). Expert developers build all three simultaneously. Novices tend to build only the program model, missing the larger context.

Vaclav Rajlich's work on change propagation (2000s) showed that understanding local changes requires understanding the module's architecture — you need to know what depends on what to assess the impact of a change. Andrew Ko's information foraging theory (2006) applied ecological foraging models to code navigation, explaining why developers follow certain paths through code and abandon others.

Gail Murphy's reflexion models (1995) introduced a practical technique for architecture recovery: compare the developer's mental model of the system's architecture with the actual dependencies in the code. Mismatches reveal either documentation bugs or architecture drift. David Parnas's foundational work on information hiding (1972) established that well-designed modules have clean boundaries — and that understanding those boundaries is the key to understanding the system.

## Further Reading

- [Program Comprehension During Software Maintenance and Evolution](https://en.wikipedia.org/wiki/Program_comprehension) — Overview of the field
- [Software Design for Flexibility](https://mitpress.mit.edu/9780262045490/) — Hanson & Sussman on understanding and designing adaptable systems
- [Working Effectively with Legacy Code](https://www.oreilly.com/library/view/working-effectively-with/0131177052/) — Michael Feathers on understanding and changing code you didn't write
- [Information Foraging Theory](https://doi.org/10.1145/1185448.1185489) — Ko et al.'s application of foraging theory to code navigation
- [On the Criteria To Be Used in Decomposing Systems into Modules](https://www.win.tue.nl/~wstomv/edu/2ip30/references/criteria_for_modularization.pdf) — Parnas 1972, foundational paper on module boundaries
