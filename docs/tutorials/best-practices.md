# The Best-Practices Technique

## Where This Came From

The "best practices" document is as old as engineering itself. Don't use lead pipes for drinking water. Don't build on flood plains. Do wash your hands before surgery. Every field accumulates hard-won knowledge about what works and what doesn't, and the smart play is to write it down.

In software, best-practices documents range from terse style guides to sprawling standards documents. Sam's spell is somewhere in the middle — it uses AI's ability to research and synthesize to produce a practical do's-and-don'ts guide, structured enough to be useful but not so heavy that nobody reads it.

Sam didn't invent the concept of writing things down. He just got tired of Googling "React testing best practices" every three months when the ecosystem changed again.

## The Core Idea

A good best-practices document does three things:

1. **Tells you what to do** — with specific, actionable advice (not "write clean code")
2. **Tells you what NOT to do** — with explanations of why the anti-pattern is bad
3. **Acknowledges context** — because "best practice" often means "best for most situations, but check your situation"

The structure matters as much as the content. A wall of text doesn't work. The do/don't format works because it's scannable — you can find what you need in seconds, not minutes.

## Why It Works With AI

AI is excellent at research and synthesis. It can:
- Search current documentation and blog posts
- Cross-reference multiple sources
- Identify consensus patterns vs. one-person opinions
- Structure findings into a consistent format

What AI is *not* great at (without help) is:
- Knowing which sources to trust
- Distinguishing current best practices from deprecated ones
- Avoiding "sounds true" advice that's actually a truism

The best-practices spell provides the structure and quality checks that keep AI output useful. The "every point needs a rationale" rule is key — it forces the AI to explain *why*, which filters out cargo-cult advice.

## How Sam Uses It

When Sam starts working with a technology he's rusty on, or when a team member asks "what's the current thinking on X?", he runs `/spell:best-practices <topic>`. The spell:

1. Researches the topic via web search (with graceful fallback to built-in knowledge)
2. Scans the codebase for existing patterns
3. Organizes findings into do's, don'ts, and context-dependent advice
4. Cites sources so you can verify the advice

The output goes directly into the conversation — it's a reference document, not a file you need to maintain.

## Beyond This Spell

The structured best-practices approach is useful whenever you need to synthesize knowledge:

- **Team onboarding:** Generate best-practices docs for your team's stack, then review and customize them
- **Technology evaluation:** Generate best-practices for a technology you're considering — if the "don'ts" list is longer than the "do's," that's a signal
- **Code review checklists:** Use the output as a starting point for what reviewers should look for
- **Architecture decisions:** When choosing between approaches, generate best-practices for each and compare

## Further Reading

- [Google Engineering Practices](https://google.github.io/eng-practices/) — Well-structured best practices for code review
- [The Pragmatic Programmer](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/) — Timeless software best practices
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) — Security best practices in the do/don't format
