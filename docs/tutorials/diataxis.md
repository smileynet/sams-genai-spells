# The Diataxis Framework

## The Problem

Your project has documentation. Quite a lot, actually. But somehow it's simultaneously too much and not enough. The README tries to be a tutorial, a reference, and an architectural overview all at once. A new developer opens it looking for "how do I run this locally?" and wades through configuration option tables, design philosophy, and a history of the project before finding the setup command on page 3.

The second failure mode is audience confusion. New users are overwhelmed by reference material they don't have context for. Experienced users can't find the specific API signature they need because it's buried in a tutorial that explains concepts they already know. The same document serves both audiences badly — too advanced for beginners, too basic for experts, too long for anyone who's busy.

The third failure mode is the most counterintuitive: writing more docs makes things worse. The team knows the documentation is lacking, so people start adding pages. A how-to guide that also explains the architecture. A tutorial that doubles as a reference. An explanation doc that includes step-by-step instructions. Each individual document is well-written, but the collection is a maze. There's no organizing principle that tells a writer "this content goes here, not there" — so everything goes everywhere.

## How It Helps

Diataxis solves this by splitting documentation into four distinct quadrants, each with a clear purpose:

|  | Practical | Theoretical |
|--|-----------|-------------|
| **Learning** | Tutorials | Explanation |
| **Working** | How-to Guides | Reference |

Each quadrant has a different goal, a different audience assumption, and a different writing style:

- **Tutorials** (learning + practical): Step-by-step, hands-on, guided experiences. Assume the reader knows nothing.
- **How-to Guides** (working + practical): Goal-oriented, concise, assume basic knowledge. "How to deploy to production."
- **Reference** (working + theoretical): Complete, accurate facts. Every option, API, parameter. Organized for lookup, not reading.
- **Explanation** (learning + theoretical): Why things work the way they do. Background, context, architecture decisions.

## Why It Works

Mixing documentation types fails because each type has fundamentally different goals, audience assumptions, and reading patterns. A tutorial needs to be sequential and forgiving; a reference needs to be exhaustive and precise. A how-to guide needs to be concise and goal-oriented; an explanation needs to be expansive and conceptual. When you put tutorial steps inside a reference document, the tutorial readers get lost in details and the reference readers get frustrated by hand-holding. The content is good — it's the combination that fails.

The framework also works as a gap detector. Teams typically over-index on reference (exhaustive but hard to learn from) and explanation (interesting but not actionable), while under-investing in tutorials (time-consuming to write) and how-to guides (seem too simple to bother documenting). Auditing against the four quadrants makes the gap immediately visible.

For AI assistants, the separation is especially useful. A document that mixes "how" and "why" confuses the AI about what kind of response to give. With Diataxis-structured docs, the AI can load the right quadrant for the situation — user asks "how do I...?" then load the how-to; user asks "what does X do?" then load the reference; user asks "why is it designed this way?" then load the explanation. Each document is focused enough to fit in a context window and specific enough to generate the right kind of answer.

## In Practice

**Django documentation.** Diataxis was developed by Daniele Procida while working on Django, and Django's docs remain one of the best real-world examples. Tutorials walk new users through building their first app — every step is hands-on, every step produces a visible result. Topic guides explain Django's design decisions and architecture. The API reference documents every model field, every queryset method, every setting. How-to guides cover specific tasks: "How to deploy with WSGI," "How to write custom template tags." A new Django developer starts with the tutorial. Six months later, the same developer uses the reference daily and reads topic guides when they need to understand the ORM's lazy evaluation. The four types coexist because they serve different needs — and Django's docs are consistently rated among the best in open source.

**Rust documentation.** Rust's documentation ecosystem maps almost perfectly to the four quadrants — though it evolved that way organically, not by design. *The Rust Programming Language* ("the book") is a tutorial: it walks you from "Hello, World" through ownership, lifetimes, and concurrency, each chapter building on the last. *Rust by Example* is a collection of how-to guides: goal-oriented, minimal explanation, "here's how to do X." The standard library docs are pure reference: every type, every method, every trait implementation, organized for lookup. And *The Rustonomicon* is explanation: it covers the "why" behind unsafe Rust, memory layout, and the guarantees the compiler provides. A new Rust developer reads the book. A working developer uses the std docs daily and hits Rust by Example when they need a pattern. An advanced developer reads the Rustonomicon when they need to understand what the compiler actually does. Each document excels because it only tries to be one thing.

## The Command

The `/spell:diataxis` command applies this concept in three modes:

1. **Audit mode:** Analyzes existing docs, classifies each by quadrant, and reports gaps. The visual quadrant grid makes missing coverage obvious at a glance.
2. **Restructure mode:** Reads existing content, splits it by quadrant, and reorganizes into the proper directory structure.
3. **Generate mode:** Researches a topic and creates documentation in all four quadrants from scratch.

All three modes produce the same directory structure: `tutorials/`, `how-to/`, `reference/`, `explanation/`, and an `index.md` entry point.

## Background

Diataxis was created by Daniele Procida while working on Django's documentation. Procida observed that documentation consistently fails in predictable ways, and that the failures always trace back to mixing different types of content. He formalized the framework and published it at [diataxis.fr](https://diataxis.fr/), and presented it at Write the Docs EU 2017 in a talk called "The Four Kinds of Documentation, and Why You Need to Understand What They Are." The framework has since been adopted by numerous open-source projects and technical writing teams. Internal wikis have benefited from the same analysis — most teams have plenty of explanation and reference, but few tutorials or how-to guides. Auditing against the four quadrants reveals the gap immediately.

## Further Reading

- [Diataxis](https://diataxis.fr/) — Daniele Procida's official documentation of the framework (yes, it follows its own framework)
- [The Documentation System](https://www.writethedocs.org/videos/eu/2017/the-four-kinds-of-documentation-and-why-you-need-to-understand-what-they-are-daniele-procida/) — Procida's Write the Docs talk
- [Django Documentation](https://docs.djangoproject.com/) — One of the best examples of Diataxis in practice
