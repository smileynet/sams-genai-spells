# Best Practices & Antipatterns

## The Problem

A new developer joins your team and asks "what's our approach to error handling?" You know the answer — it's scattered across years of code review comments, Slack threads, and hard lessons learned. But there's no document. So you spend 30 minutes explaining it, knowing you'll do the same thing next quarter when the next person joins. The knowledge exists, but it's trapped in people's heads and in the search history of a chat app.

This isn't just an onboarding problem. The same mistakes get made again because the lessons aren't documented. Someone silently swallows an exception in a catch block — the same bug that caused a production incident six months ago, the one you discussed in a post-mortem that nobody can find anymore. Without a written record, institutional knowledge has a half-life measured in employee tenure. People leave, memories fade, and hard-won lessons evaporate.

AI makes the gap more visible. Ask an AI to generate best practices for your codebase and you get generic truisms: "write clean code," "use meaningful variable names," "handle errors gracefully." These aren't wrong — they're useless. Without a structured format that demands specific advice and rationale for each point, AI output devolves into the kind of platitudes you'd find in a freshman textbook. The format is the forcing function that makes the content useful.

## How It Helps

A best-practices and antipatterns document does four things:

1. **Tells you what to do** — with specific, actionable advice (not "write clean code")
2. **Tells you what NOT to do** — with explanations of why the bad practice is harmful
3. **Names the traps** — antipatterns that look reasonable until they blow up, with analysis of why people fall into them
4. **Acknowledges context** — because "best practice" often means "best for most situations, but check your situation"

The structure matters as much as the content. A wall of text doesn't work. The do/don't/antipattern format is scannable — you can find what you need in seconds, not minutes.

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

## In Practice

**The OWASP Top 10.** The Open Web Application Security Project maintains a [ranked list](https://owasp.org/www-project-top-ten/) of the ten most critical web security risks — and it's structured as a best-practices document. Each entry names the vulnerability (injection, broken authentication, etc.), explains why it's dangerous with real-world impact data, and provides specific prevention steps. "Do: use parameterized queries. Don't: concatenate user input into SQL strings." The format is so effective that it's become an industry standard — security audits reference it, compliance frameworks require it, and developers actually read it because they can scan for what's relevant to their code.

**Google Engineering Practices.** Google published their [code review guidelines](https://google.github.io/eng-practices/) as a structured best-practices document, and it's a case study in how the format scales. The reviewer guide has specific do's ("look for design problems first") and don'ts ("don't nitpick style in the same review as logic"), each with enough context to understand the reasoning. It works because a new Googler can read the relevant section in five minutes before their first review, while experienced reviewers use it as a reference when disagreements arise. The format makes institutional knowledge transferable.

**Brown et al.'s *AntiPatterns*.** The 1998 book *AntiPatterns: Refactoring Software, Architectures, and Projects in Crisis* gave names to recurring failure modes in software development. "The Blob" (God Object), "Lava Flow" (dead code nobody removes), "Golden Hammer" (one tool for everything) — these names entered the industry vocabulary because naming a problem makes it discussable. The book's key insight: antipatterns aren't just mistakes, they're *attractive* mistakes. Each one has a seductive rationale that makes it seem like a good idea at the time.

## The Command

The `/spell:bpap <topic>` command applies this concept by:

1. Researching the topic via web search (with graceful fallback to built-in knowledge)
2. Scanning the codebase for existing patterns
3. Organizing findings into do's, don'ts, named antipatterns with trap analysis, and context-dependent advice
4. Citing sources so you can verify the advice

The output is a reference document in the conversation — structured enough to be useful, not so heavy that nobody reads it. The antipatterns section adds depth: not just "don't do this" but "here's why smart people keep doing this, and here's what happens when they do."

## Background

The do's-and-don'ts format is as old as engineering itself. In software, the tradition runs from Kernighan and Plauger's *The Elements of Programming Style* (1978) through McConnell's *Code Complete* (1993) to modern living documents like Google's engineering practices. IEEE, ACM, and ISO standards are formalized versions of the same idea — "Do use TLS 1.3. Don't use SSL 3.0 — here's the CVE." The shift from static books to continuously-updated guides reflects the faster pace of software evolution. Architecture Decision Records (ADRs) apply the same principle to design choices: "We chose X over Y because..." — structured decision documentation that survives team turnover.

The antipattern literature adds a complementary lens. Where best practices say "do this," antipatterns say "you'll be tempted to do *that* — here's why it fails." Brown et al.'s *AntiPatterns* (1998) catalogued recurring failure modes in software development, architecture, and project management. The Gang of Four's *Design Patterns* (1994) had shown that good solutions recur; *AntiPatterns* showed that bad solutions recur too, and that naming them is the first step to avoiding them.

## Further Reading

- [Google Engineering Practices](https://google.github.io/eng-practices/) — Well-structured best practices for code review
- [The Pragmatic Programmer](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/) — Timeless software best practices
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) — Security best practices in the do/don't format
- [AntiPatterns](https://en.wikipedia.org/wiki/AntiPatterns_(book)) — Brown, Malveau, McCormick & Mowbray (1998). The book that named the traps.
