# The Diataxis Technique

## Where This Came From

Diataxis was created by Daniele Procida, and it's one of those ideas that makes you feel slightly foolish for not having thought of it yourself. Procida observed that most documentation fails because it tries to do too many things at once — a tutorial that's also a reference, a how-to guide that's also an explanation, a README that's trying to be all four.

His solution: split documentation into four distinct quadrants, each with a clear purpose and audience. That's it. That's the whole framework.

Sam found Diataxis while trying to figure out why his project's docs kept getting worse even as he added more content. Turns out, mixing "here's how to get started" with "here's every configuration option" with "here's why we designed it this way" creates a document that serves nobody well. Splitting them apart fixed it.

## The Core Idea

Diataxis organizes documentation along two axes:

|  | Practical | Theoretical |
|--|-----------|-------------|
| **Learning** | Tutorials | Explanation |
| **Working** | How-to Guides | Reference |

Each quadrant has a distinct purpose:

**Tutorials** (learning + practical): "Follow along and learn by doing."
- Step-by-step, hands-on, guided experiences
- Assume the reader knows nothing
- Every step produces a visible result
- The reader learns by completing a journey

**How-to Guides** (working + practical): "How to accomplish a specific task."
- Goal-oriented: "How to deploy to production"
- Assume the reader has basic knowledge
- Concise, focused, get-it-done
- Multiple guides for different goals

**Reference** (working + theoretical): "The complete, accurate facts."
- Exhaustive documentation of every option, API, parameter
- No opinions, no tutorials — just facts
- Organized for lookup, not reading
- Must be accurate and up-to-date

**Explanation** (learning + theoretical): "Why things work the way they do."
- Background, context, architecture decisions
- Answers "why" questions
- Can be opinionated
- Helps the reader form a mental model

## Why It Works With AI

AI assistants, like humans, struggle with documents that mix purposes. When an AI reads a doc that's half tutorial and half reference, it doesn't know whether to give you step-by-step instructions or a complete API listing.

Diataxis separation helps AI in specific ways:
- **Tutorials** give the AI a script to follow when users are learning
- **How-to guides** give the AI focused, goal-oriented instructions
- **Reference** gives the AI accurate API details without narrative noise
- **Explanation** gives the AI context for architectural decisions

When you point an AI at Diataxis-structured docs, it can load the right quadrant for the right situation. User asks "how do I...?" → load the how-to. User asks "what does X do?" → load the reference. User asks "why is it designed this way?" → load the explanation.

## How Sam Uses It

The `/spell:diataxis` command has three modes because Sam kept needing it for different things:

1. **Audit mode:** "My docs exist but feel wrong." The spell analyzes existing docs, classifies each one by quadrant, and reports gaps. The visual quadrant grid makes missing coverage obvious at a glance.

2. **Restructure mode:** "My docs exist but they're mixed up." The spell reads existing content, splits it by quadrant, and reorganizes it into the proper directory structure.

3. **Generate mode:** "I don't have docs yet." The spell researches the topic and creates documentation in all four quadrants from scratch.

All three modes produce the same directory structure:
```
docs/<topic>/
├── tutorials/
├── how-to/
├── reference/
├── explanation/
└── index.md
```

The `index.md` is the entry point that links to all four quadrants and explains when to read each one.

## Beyond This Spell

Diataxis applies wherever documentation exists:

- **README files:** A good README is usually a mini-tutorial + reference. Consider whether it should link out to separate docs for the other quadrants.
- **API documentation:** Most API docs are pure reference. Adding a tutorial and some how-to guides dramatically improves usability.
- **Internal wikis:** Audit your wiki against the four quadrants. Most teams have lots of explanation and reference, but few tutorials or how-to guides.
- **Teaching:** If you're explaining something and it's not landing, you might be in the wrong quadrant. Switch from explanation (theory) to tutorial (hands-on) and see if it clicks.

## Further Reading

- [Diataxis](https://diataxis.fr/) — Daniele Procida's official documentation of the framework (yes, it follows its own framework)
- [The Documentation System](https://www.writethedocs.org/videos/eu/2017/the-four-kinds-of-documentation-and-why-you-need-to-understand-what-they-are-daniele-procida/) — Procida's Write the Docs talk
- [Django Documentation](https://docs.djangoproject.com/) — One of the best examples of Diataxis in practice (Procida developed it while working on Django)
