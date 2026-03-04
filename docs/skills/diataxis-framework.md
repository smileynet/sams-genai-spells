# Diataxis Framework — Skill Reference for AI Assistants

> Four-quadrant documentation classification for separating content by purpose.

## History

Developed by Daniele Procida while working on Django's documentation. Presented at Write the Docs EU 2017 as "The Four Kinds of Documentation." Published at [diataxis.fr](https://diataxis.fr/). Adopted by Django, Gatsby, NumPy, and numerous open-source projects. The framework observes that documentation consistently fails when it mixes different types of content — each type has fundamentally different goals, audience assumptions, and reading patterns.

## Core Mechanics

Documentation serves four distinct purposes, organized along two axes:

|  | Practical | Theoretical |
|--|-----------|-------------|
| **Learning** | Tutorials | Explanation |
| **Working** | How-to Guides | Reference |

### Quadrant Characteristics

| Quadrant | Goal | Audience assumption | Reading pattern | Writing style |
|----------|------|---------------------|-----------------|---------------|
| **Tutorial** | Learn by doing | Knows nothing | Sequential, guided | Step-by-step, encouraging, every step produces a visible result |
| **How-to** | Accomplish a task | Knows the basics | Goal-oriented, scan | Concise, numbered steps, "How to X" titles |
| **Reference** | Look up facts | Needs specific info | Random access, lookup | Exhaustive, accurate, tables, no opinions |
| **Explanation** | Understand why | Wants context | Linear reading | Opinionated, expansive, architecture decisions and trade-offs |

### Classification Signals

**Tutorial indicators:**
- "Follow along," "by the end you will have," step-by-step instructions
- Assumes no prior knowledge, builds from zero
- Every step produces a visible result

**How-to indicators:**
- "How to [accomplish X]," goal-oriented framing
- Assumes basic knowledge, skips fundamentals
- Multiple guides for different tasks

**Reference indicators:**
- API signatures, configuration tables, parameter lists
- Organized for lookup (alphabetical or logical), not for reading
- No opinions — just facts

**Explanation indicators:**
- "Why does this work this way?" context and background
- Architecture decisions, trade-offs, history
- Can be opinionated

### Mixed-Quadrant Detection

A document mixes quadrants when it:
- Interrupts tutorial steps with exhaustive option tables (tutorial + reference)
- Explains architecture in a how-to guide (how-to + explanation)
- Puts step-by-step instructions inside a reference page (reference + tutorial)
- Adds "why" digressions to task-oriented guides (how-to + explanation)

Mixed docs serve both audiences badly — too advanced for beginners, too basic for experts.

## Standard Directory Structure

```
docs/<topic>/
├── tutorials/
│   └── <tutorial-files>.md
├── how-to/
│   └── <guide-files>.md
├── reference/
│   └── <reference-files>.md
├── explanation/
│   └── <explanation-files>.md
└── index.md
```

## ASCII Quadrant Grid Format

Use this format for audit and coverage reports:

```
               ┌─────────────┬─────────────┐
               │  PRACTICAL  │  THEORETICAL│
  ┌────────────┼─────────────┼─────────────┤
  │ LEARNING   │ Tutorials   │ Explanation │
  │            │ <count>     │ <count>     │
  ├────────────┼─────────────┼─────────────┤
  │ WORKING    │ How-to      │ Reference   │
  │            │ <count>     │ <count>     │
  └────────────┴─────────────┴─────────────┘
```

## Coverage Analysis

Not every topic needs all four quadrants:
- A simple CLI tool may only need tutorial + reference
- An internal library may only need reference + explanation
- A complex platform likely needs all four

The gap matters more than the count. Missing tutorials = hard to learn. Missing reference = hard to use daily. Missing explanation = no one understands the design.

## Reporting Template

> **Note:** The spell templates are the canonical source for output format. This reference provides the classification framework; defer to the spell if they differ.
