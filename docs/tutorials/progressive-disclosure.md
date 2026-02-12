# Progressive Disclosure

## The Problem

You open the Settings app on your phone. There are maybe fifteen options visible. But your phone has hundreds of settings — where are they? Behind taps labeled "Advanced," "Developer Options," "Accessibility." Showing everything at once would overwhelm most users. But hiding *everything* behind menus would frustrate the people who know exactly what they want. The design challenge is serving both audiences at once.

Documentation has the same problem, and it usually fails in one of two directions. The first failure mode is the wall of text: a single 5000-line README that covers installation, configuration, architecture, API reference, troubleshooting, and philosophy — all in one file. New users can't find the getting-started section. Experienced users can't jump to the configuration option they need. And when you point an AI at it, the AI loads the entire file and wastes context on thousands of lines of detail it doesn't need for the current question.

The second failure mode is the opposite: 50 tiny, unstructured files scattered across the repo. There's no entry point. There's no indication of what to read first or what's advanced. A new user finds `config-options.md` before they've read `getting-started.md` and gets lost in details they don't have context for. An AI scanning the docs directory has no idea which file is relevant — it either loads everything (too much) or picks the wrong one (too little).

Then there's the expert trapped behind the beginner content. Your team's documentation starts with "What is a REST API?" and doesn't get to the deployment configuration until page 12. The senior engineer who needs to change a timeout value has to scroll past an introduction they could teach. They stop using the docs and start grepping the source code instead.

## How It Helps

Progressive disclosure solves this by organizing content into levels:

1. **Level 1: Overview** — What is this? Who is it for? The 30-second pitch.
2. **Level 2: Getting Started** — Minimum viable usage. Hands-on, no theory.
3. **Level 3: Guides** — How to do specific tasks, assuming basic knowledge.
4. **Level 4: Reference** — Complete, exhaustive documentation of every option.
5. **Level 5: Deep Dives** — Architecture, design decisions, advanced theory.

Each level links to the next. A reader at Level 1 can stop if they got what they needed, or drill down to Level 5 if they're debugging an edge case at 2 AM. The key constraint: **each file should stand alone.** You can read the overview without the reference, or the reference without the guides.

## Why It Works

Different people need different amounts of detail at different times. A single document that tries to serve everyone serves no one — beginners drown in detail, experts wade through basics. Progressive disclosure creates a navigation structure that supports two reading strategies simultaneously: scan-and-stop (read until you have enough, then leave) and targeted deep-dive (jump to the level that matches your current need).

The 200-500 line target per file isn't arbitrary — it's sized to fit comfortably in an AI context window alongside the user's code and conversation history. When documentation follows progressive disclosure, the AI can load the overview first, then drill into the relevant guide — the same strategy a human expert uses. This is dramatically more efficient than loading a single massive file or guessing which of 50 unstructured files is relevant.

The structure also makes maintenance tractable. When you need to update the API reference, you edit the reference file. When you need to add a new tutorial, you add a file at Level 2 or 3. The levels are independent enough that one person can update the reference while another rewrites the getting-started guide, without merge conflicts or structural disruption.

## In Practice

**CLI tools and layered help.** `git` is a masterclass in progressive disclosure — whether the designers intended it or not. `git commit --help` gives you the common flags in a screenful of text. `man git-commit` gives you every flag, every option, every edge case. The Git book gives you the conceptual model behind commits, the object store, and the DAG. Three levels of disclosure, each serving a different need. A new user runs `--help` and learns enough to commit code. An experienced developer hits `man` when they need the exact syntax for `--fixup`. A contributor reads the book when they need to understand the reflog. The same pattern appears in every well-designed CLI: `--help` for the common case, `man` for the complete reference, and documentation for the conceptual model.

**API documentation and the Stripe pattern.** Stripe's API docs are often cited as best-in-class, and their structure is progressive disclosure made explicit. The quickstart gets you making API calls in under five minutes — it shows one endpoint, one request, one response. The guides cover specific tasks: subscriptions, webhooks, error handling. The full API reference documents every endpoint, every parameter, every error code. A developer integrating Stripe for the first time reads the quickstart. A developer adding webhook handling reads the guide. A developer debugging a specific error code goes straight to the reference. Each level is useful on its own, and the navigation makes it obvious where to go next.

## The Command

The `/spell:progressive-disclosure <topic>` command applies this concept by:

1. Determining the scope (existing docs, codebase area, or new topic)
2. Designing a 4-7 file structure following the progressive levels
3. Confirming the plan with the user
4. Generating the files with cross-links and navigation headers
5. Numbering files (`00-`, `01-`, etc.) so `ls` shows them in reading order

The numbered prefix is a small detail that matters — it means AI tools that alphabetize file lists present them in the correct reading order too.

## Background

Progressive disclosure was coined by J.M. Keller in 1983 as part of his motivational design framework for instruction, though the underlying principle predates the term. The concept was popularized in UX design by the Nielsen Norman Group, who applied it to interface design: "show only the most important options first; secondary, less-used options are hidden but accessible." Don Norman's *The Design of Everyday Things* (1988) established the broader principle that good design reveals complexity gradually. Error messages are a small-scale example of the same idea: good error messages show the simple fix first, with a link to "learn more" for the full explanation. Rust's compiler errors are a masterclass in this — they tell you what went wrong, suggest a fix, and link to a detailed explanation.

## Further Reading

- [Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/) — Nielsen Norman Group's authoritative overview
- [The Design of Everyday Things](https://www.basicbooks.com/titles/don-norman/the-design-of-everyday-things/9780465050659/) by Don Norman — Broader design principles including progressive disclosure
- J.M. Keller, "Motivational Design of Instruction" (1983) — The original paper coining the term
