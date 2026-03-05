# Best Practices & Antipatterns

## The Problem

A new developer joins your team and asks "what's our approach to error handling?" You know the answer — it's scattered across years of code review comments, Slack threads, and hard lessons learned. But there's no document. So you spend 30 minutes explaining it, knowing you'll do the same thing next quarter when the next person joins. The knowledge exists, but it's trapped in people's heads and in the search history of a chat app.

This isn't just an onboarding problem. The same mistakes get made again because the lessons aren't documented. Someone silently swallows an exception in a catch block — the same bug that caused a production incident six months ago, the one you discussed in a post-mortem that nobody can find anymore. Without a written record, institutional knowledge has a half-life measured in employee tenure. People leave, memories fade, and hard-won lessons evaporate.

AI makes the gap more visible. Ask an AI to generate best practices for your codebase and you get generic truisms: "write clean code," "use meaningful variable names," "handle errors gracefully." These aren't wrong — they're useless. Without a structured format that demands specific advice and rationale for each point, AI output devolves into the kind of platitudes you'd find in a freshman textbook. The format is the forcing function that makes the content useful.

## How It Helps

A best-practices and antipatterns document does four things:

1. **Tells you what to do** — numbered best practices with specific, actionable advice and rationale (not "write clean code")
2. **Names the traps** — antipatterns that look reasonable until they blow up, with analysis of why people fall into them
3. **Says when to break the rules** — because "best practice" means "best for most situations," and specific exceptions beat blanket disclaimers
4. **Links related guides** — cross-references to other bpap documents by stable BP/AP IDs, so your knowledge base connects instead of siloing

The structure matters as much as the content. A wall of text doesn't work. The BP/AP format is scannable — you can find what you need in seconds, not minutes.

## Why It Works

Knowledge that isn't written down gets lost. The structured format survives because it matches how practitioners actually think about their craft:

- **It's scannable:** You find what you need in seconds, not by reading a 20-page document
- **It's auditable:** Each point has a rationale, so you can evaluate whether it still applies
- **It's maintainable:** Adding a new point doesn't require restructuring the whole document
- **It composes well:** Different documents for different topics can coexist without conflict

The rationale requirement is the key constraint. "Don't use `eval()`" is a rule. "Don't use `eval()` — it executes arbitrary code, creating injection vulnerabilities" is a best practice. The rationale filters out cargo-cult advice and gives readers enough context to know when the rule doesn't apply.

For AI assistants, the structured format acts as a quality gate. When the output format demands specific do's, don'ts, and rationale for each, the AI can't get away with vague advice. The format forces precision.

## Antipatterns vs. Don'ts

A **don't** is a simple prohibition: "Don't store passwords in plaintext." It tells you what to avoid. Clear, direct, no ambiguity.

An **antipattern** is a named, recognizable pattern that *looks reasonable* but leads to problems. The key difference is trap analysis — understanding *why people fall into it*:

- **Golden Hammer** — using one tool for everything because you're comfortable with it. It's tempting because expertise feels like efficiency. It goes wrong when the tool doesn't fit the problem and you spend more time fighting it than solving anything.
- **God Object** — one class that does everything. It's tempting because centralizing logic feels simpler than distributing it. It goes wrong when every change touches the same file and nobody can work in parallel.
- **Lava Flow** — dead code that nobody dares remove. It's tempting because deletion feels risky when you're not sure what depends on it. It goes wrong when the codebase grows incomprehensible under layers of fossilized experiments.

Antipatterns have names because they recur. The names make knowledge transferable — saying "that's a Golden Hammer" in a code review is faster and more precise than explaining the whole dynamic from scratch. The trap analysis ("why it's tempting") is what distinguishes an antipattern from a don't: it acknowledges that smart people make this mistake for understandable reasons, and explains what makes the seemingly-reasonable choice go wrong.

The decision rule is mechanical: an antipattern has a **name**, a **temptation**, and **consequences**. If you can fill all three, it's an antipattern. If you can't — if there's no seductive rationale, just a thing you shouldn't do — fold it into a best practice as a "don't" with rationale. The old template had a separate DON'T section, but in practice the distinction collapsed. Twenty real outputs later, the lesson is clear: two categories (BP and AP) are enough.

## In Practice

**The OWASP Top 10.** The Open Web Application Security Project maintains a [ranked list](https://owasp.org/www-project-top-ten/) of the ten most critical web security risks — and it's structured as a best-practices document. Each entry names the vulnerability (injection, broken authentication, etc.), explains why it's dangerous with real-world impact data, and provides specific prevention steps. "Do: use parameterized queries. Don't: concatenate user input into SQL strings." The format is so effective that it's become an industry standard — security audits reference it, compliance frameworks require it, and developers actually read it because they can scan for what's relevant to their code.

**Google Engineering Practices.** Google published their [code review guidelines](https://google.github.io/eng-practices/) as a structured best-practices document, and it's a case study in how the format scales. The reviewer guide has specific do's ("look for design problems first") and don'ts ("don't nitpick style in the same review as logic"), each with enough context to understand the reasoning. It works because a new Googler can read the relevant section in five minutes before their first review, while experienced reviewers use it as a reference when disagreements arise. The format makes institutional knowledge transferable.

**Brown et al.'s *AntiPatterns*.** The 1998 book *AntiPatterns: Refactoring Software, Architectures, and Projects in Crisis* gave names to recurring failure modes in software development. "The Blob" (God Object), "Lava Flow" (dead code nobody removes), "Golden Hammer" (one tool for everything) — these names entered the industry vocabulary because naming a problem makes it discussable. The book's key insight: antipatterns aren't just mistakes, they're *attractive* mistakes. Each one has a seductive rationale that makes it seem like a good idea at the time.

## The Command

The `/spell:bpap <topic>` command applies this concept in three phases:

1. **Extract** — Research the topic via web search (with graceful fallback to built-in knowledge), scan the codebase for existing patterns, look for related bpap files to cross-reference, and check `.claude/rules/` for idiomatic constraint files on the same topic
2. **Compose** — Choose a structure based on topic scope (flat for narrow topics, sectioned for broad ones), apply BP-X.Y/AP-X.Y numbering, and write the document in standard markdown. Each document includes freshness metadata (generation date, source, review-after date) and an AI Rules Distillation appendix
3. **Verify** — Self-check the output against a quality rubric before presenting it: does every BP have rationale? Does every AP have trap analysis? Are there specific "when to break" items instead of blanket disclaimers?

By default, the output is saved to `docs/bpap-<topic-slug>.md` — this is what makes cross-referencing work. Other spells (including `/spell:idiomatic`) discover and incorporate bpap files during their research phase. Use `--no-save` for exploratory runs where you're not ready to commit to a file.

The output adapts to the topic. A narrow topic like "Git commit messages" gets a **flat** structure — one Best Practices section, one Antipatterns section, numbered `BP-1`, `AP-1`. A broad topic like "React application architecture" gets a **sectioned** structure — multiple sections with their own BPs and APs, numbered `BP-1.1`, `AP-2.3`. The decision rule is simple: if the topic has 3+ distinct subtopics, use sectioned.

Every item gets a stable ID (BP-1.2, AP-3.1) that other bpap documents can reference. This matters once you have a library of bpap files — you can say "see BP-2.1 in bpap-error-handling.md" instead of vaguely gesturing at "the error handling doc." The IDs use max two levels of hierarchy, matching what every mature standard (OWASP, NIST, ISO) has converged on.

The output is standard markdown — no Unicode box-drawing characters, no custom formatting. This isn't an aesthetic choice: AI models reproduce standard markdown with near-100% fidelity, while rare Unicode characters get tokenized into fragments the model barely saw in training. Twenty real outputs proved this — zero followed the old Unicode format, all produced clean markdown.

## Cross-Referencing

Once you have more than one bpap document, they start referencing each other. "Don't inline SVG without optimization" in a logo design guide points at "Use SVGO before committing" in an SVG guide. The BP-X.Y numbering system gives these references stable anchors.

Each document also includes an **AI Rules Distillation** appendix — a terse USE/AVOID block designed for copy-pasting into AI rules files (`.claude/rules/`, `AGENTS.md`). This isn't a replacement for the full guide; it's a compressed version for contexts where brevity matters more than rationale. The full guide with its reasoning and trap analysis remains the source of truth.

Documents include **freshness metadata** — a generation date, source (web research vs. training knowledge), and a review-after date six months out. When other spells discover a bpap file during research, this metadata tells them whether the advice is current or potentially stale.

Cross-references go in a dedicated section at the end of each document, before Sources:

```markdown
## Cross-References

- [SVG Best Practices (BP-3)](./bpap-svg.md) — optimization pipeline for inline SVGs
- [Visual QA (AP-2.1)](./bpap-visual-qa.md) — screenshot testing catches logo regressions
```

The IDs serve as stable anchors because they're tied to section position, not heading text. Auto-generated heading slugs are fragile across renderers — GitHub, VS Code, and Obsidian all generate different slugs for the same heading. `BP-2.3` is unambiguous everywhere.

When retrofitting existing bpap documents, add the Cross-References section at the end (before Sources), and only reference documents that genuinely relate. A cross-reference should help the reader find complementary advice, not serve as an exhaustive index of every bpap file in the repo.

## Background

The do's-and-don'ts format is as old as engineering itself. In software, the tradition runs from Kernighan and Plauger's *The Elements of Programming Style* (1978) through McConnell's *Code Complete* (1993) to modern living documents like Google's engineering practices. IEEE, ACM, and ISO standards are formalized versions of the same idea — "Do use TLS 1.3. Don't use SSL 3.0 — here's the CVE." The shift from static books to continuously-updated guides reflects the faster pace of software evolution. Architecture Decision Records (ADRs) apply the same principle to design choices: "We chose X over Y because..." — structured decision documentation that survives team turnover.

The antipattern literature adds a complementary lens. Where best practices say "do this," antipatterns say "you'll be tempted to do *that* — here's why it fails." Brown et al.'s *AntiPatterns* (1998) catalogued recurring failure modes in software development, architecture, and project management. The Gang of Four's *Design Patterns* (1994) had shown that good solutions recur; *AntiPatterns* showed that bad solutions recur too, and that naming them is the first step to avoiding them.

## Further Reading

- [Google Engineering Practices](https://google.github.io/eng-practices/) — Well-structured best practices for code review
- [The Pragmatic Programmer](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/) — Timeless software best practices
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) — Security best practices in the do/don't format
- [AntiPatterns](https://en.wikipedia.org/wiki/AntiPatterns_(book)) — Brown, Malveau, McCormick & Mowbray (1998). The book that named the traps.
