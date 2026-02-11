# The Progressive Disclosure Technique

## Where This Came From

Progressive disclosure was coined by J.M. Keller in 1983, though the idea predates the term. The principle: show people the simplest useful information first, and reveal complexity only when they ask for it. Don't hit a beginner with every option at once; don't hide power features from experts.

You see progressive disclosure everywhere — iPhone settings that hide "Advanced" behind a tap, cooking recipes that put the quick version at the top and the detailed notes at the bottom, textbooks that start with "Introduction to X" and end with "Advanced X for People Who Really Like X."

Sam stumbled onto this technique while trying to feed documentation to AI assistants. He kept hitting context window limits because the docs were giant monolithic files. Breaking them into linked files at progressive detail levels solved two problems at once: the AI could load only what it needed, and the docs became better for humans too.

## The Core Idea

Progressive disclosure in documentation means organizing content into levels:

1. **Level 1: Overview** — What is this? Who is it for? The 30-second pitch.
2. **Level 2: Getting Started** — Minimum viable usage. Hands-on, no theory.
3. **Level 3: Guides** — How to do specific tasks, assuming basic knowledge.
4. **Level 4: Reference** — Complete, exhaustive documentation of every option.
5. **Level 5: Deep Dives** — Architecture, design decisions, advanced theory.

Each level links to the next. A reader at Level 1 can stop if they got what they needed, or drill down to Level 5 if they're debugging an edge case at 2 AM.

The key constraint: **each file should stand alone.** You should be able to read the overview without the reference, or the reference without the guides. They link to each other, but they don't require each other.

## Why It Works With AI

AI context windows are finite. When you point an AI at documentation, it has to decide what to load. If your docs are a single 5000-line file, the AI loads everything and wastes context on details it doesn't need. If your docs are 50 tiny files with no structure, the AI doesn't know where to start.

Progressive disclosure gives the AI a strategy:
1. Load the overview (Level 1) — get the big picture
2. Load the relevant guide (Level 3) — get task-specific detail
3. Load the reference (Level 4) — only if it needs exact API signatures

This is the same strategy a human expert uses, but AI needs the structure to be explicit. You can't rely on an AI to "skim" a long document the way a human would.

The 200-500 line target per file isn't arbitrary — it's sized to fit comfortably in an AI context window alongside the user's code and conversation history.

## How Sam Uses It

When Sam has documentation that's too big or too disorganized for AI consumption, he runs `/spell:progressive-disclosure <topic>`. The spell:

1. Determines the scope (existing docs, codebase area, or new topic)
2. Designs a 4-7 file structure following the progressive levels
3. Confirms the plan with the user
4. Generates the files with cross-links and navigation headers
5. Numbers files (`00-`, `01-`, etc.) for consistent ordering

The numbered prefix is a small detail that matters — it means `ls` shows the files in reading order, and AI tools that alphabetize file lists present them correctly too.

## Beyond This Spell

Progressive disclosure is a general design principle:

- **API design:** Start with simple defaults, expose advanced configuration only when requested
- **CLI tools:** Provide a simple interface with `--help` for details and man pages for the full reference
- **Onboarding:** New team members get the overview doc on day one, not the architecture deep dive
- **Meeting agendas:** Put the TL;DR at the top, details below, links to background docs
- **Error messages:** Show the simple fix first, with a link to "learn more" for the full explanation

## Further Reading

- [Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/) — Nielsen Norman Group's authoritative overview
- [The Design of Everyday Things](https://www.basicbooks.com/titles/don-norman/the-design-of-everyday-things/9780465050659/) by Don Norman — Broader design principles including progressive disclosure
- J.M. Keller, "Motivational Design of Instruction" (1983) — The original paper coining the term
