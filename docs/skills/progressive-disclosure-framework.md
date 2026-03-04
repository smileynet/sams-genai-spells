# Progressive Disclosure — Skill Reference for AI Assistants

> Layered content organization from simple to complex, revealing detail on demand.

## History

Coined by J.M. Keller in 1983 as part of his motivational design framework for instruction. Popularized in UX design by the Nielsen Norman Group: "show only the most important options first; secondary, less-used options are hidden but accessible." Don Norman's *The Design of Everyday Things* (1988) established the broader principle that good design reveals complexity gradually.

## Core Mechanics

Content is organized into depth levels. Each level is self-contained — readers stop when they have enough, or drill deeper when they need more.

### Five Standard Levels

| Level | Name | Purpose | Target size |
|-------|------|---------|-------------|
| 1 | Overview | What is this? Who is it for? Quick-start. Entry point to everything else. | 100–200 lines |
| 2 | Getting Started | Minimum viable usage. Hands-on, no theory. | 200–300 lines |
| 3 | Guides | How-to guides for common tasks. 1–3 files. | 200–500 lines each |
| 4 | Reference | Complete API/configuration reference. | 300–500 lines |
| 5 | Deep Dives | Architecture, design decisions, advanced topics. Optional. | 200–400 lines |

### File Sizing

- **200–500 lines per file** — sized for AI context windows. Longer files should be split.
- **4–7 files total** — more than 7 breaks the progressive model. Merge or reorganize.

### File Numbering Convention

```
00-overview.md
01-getting-started.md
02-guide-<name>.md
03-guide-<name>.md
04-reference.md
05-deep-dive-<name>.md
```

Numbered prefixes ensure `ls` and AI file listings show reading order.

## Design Technique

### Navigation Links

Every file includes navigation at top and bottom:

```markdown
> **Navigation:** [Overview](./00-overview.md) | [Getting Started](./01-getting-started.md) | **This Guide** | [Reference](./04-reference.md)
```

### Content Rules

- **Each file stands alone** — makes sense without reading the others, even though they link together
- **Overview is the index** — gives a complete (if shallow) picture and points to everything else
- **Don't repeat content** — link to it: "For details, see [Reference](./04-reference.md)"
- **Cross-reference inline** where relevant, not just in navigation headers

### Depth Assessment Criteria

When auditing existing docs for progressive disclosure:
- Does an entry point (overview) exist?
- Are there clear depth levels, or is everything at the same detail?
- Can you navigate from overview to any specific topic?
- Are files sized for context windows (200–500 lines)?
- Does each file include enough context to stand alone?

## Standard Directory Structure

```
docs/<topic>/
├── 00-overview.md
├── 01-getting-started.md
├── 02-guide-<name>.md
├── 03-guide-<name>.md
├── 04-reference.md
└── 05-deep-dive-<name>.md
```

## Reporting Template

> **Note:** The spell templates are the canonical source for output format. This reference provides the layering framework; defer to the spell if they differ.
