# Idiomatic Code

## The Problem

You join a new team that uses Go. You know Go's syntax fine, but your first pull request comes back covered in comments: "use `:=` not `var`," "receivers should be value types here," "don't return errors like that." You weren't *wrong* — your code compiled and passed tests. But it wasn't Go. It was Java written in Go syntax.

AI code generation has the same problem, but worse. LLMs are trained on a mix of everything — old code, new code, deprecated tutorials, Stack Overflow answers from 2014. Without constraints, they'll mix React 16 class components and React 19 hooks in the same response, hallucinate API signatures that don't exist in your version, or confidently use a library method that was removed two major releases ago. The AI doesn't know which version you're using unless you tell it.

The third angle is subtler: code that compiles, passes tests, and even works correctly — but that nobody on the team can read comfortably. It uses clever tricks instead of standard patterns. It imports a utility library for something the standard library handles. It structures error handling in a way that's technically valid but that no one who's worked in the language for more than a year would write. The code works, but it generates friction in every review and every future modification.

## How It Helps

Every programming language community converges on patterns — canonical ways of doing things that go beyond syntax. Idiomatic code follows these conventions. When you write idiomatically, you're doing two things:

1. **Using documented, canonical patterns** — not inventing new ways to do things that already have a standard approach
2. **Matching community expectations** — so other developers can read your code without a decoder ring

Constraining to documented patterns also dramatically reduces AI hallucination. When the AI is told "be idiomatic for Python 3.12," it stops making up methods and starts referencing what actually exists in the 3.12 documentation.

## Why It Works

The value of idiomatic code isn't aesthetic — it's practical:

- **Predictable:** Other developers know where to look for things and how they'll behave
- **Maintainable:** The next person doesn't need to learn your personal style before they can modify the code
- **Safer:** Canonical patterns are well-tested; novel approaches may have edge cases nobody's hit yet
- **Searchable:** When you Google an error with idiomatic code, you find answers. When you Google an error with a creative approach, you're on your own

For AI assistants specifically, the constraint works mechanistically. LLMs generate text by predicting likely next tokens based on training data. When you constrain to "idiomatic Python 3.12," you're biasing the model toward patterns that appeared frequently in well-regarded, version-specific documentation — exactly the patterns most likely to be correct.

## In Practice

**Style guides and linters.** PEP 8 (Python), `gofmt` (Go), Prettier (JavaScript) — these tools encode what "idiomatic" means for a language. But they go further than formatting. PEP 8 doesn't just say "use 4 spaces." It establishes patterns like "explicit is better than implicit" that shape how experienced Python developers think about code. `gofmt` takes it even further: there is exactly one way to format Go code, and the tool enforces it. The result is that any Go codebase looks familiar to any Go developer — you spend your review time on logic, not on learning someone's personal formatting preferences.

**Framework conventions.** Rails' "convention over configuration" is idiomatic thinking applied to an entire framework. There's a canonical way to structure a Rails app, name your models, define your routes. Developers who follow the conventions get massive productivity benefits — scaffolding works, generators produce the right structure, and any Rails developer can navigate any Rails project. Developers who fight the conventions spend their time configuring things that should have been automatic. React's hooks patterns work the same way: `useState`, `useEffect`, and the rules of hooks are idiomatic React. Code that follows them is predictable; code that works around them is a maintenance burden.

## The Command

The `/spell:idiomatic <tool>` command applies this concept by:

1. Detecting the tool version from the codebase (package.json, pyproject.toml, etc.)
2. Researching current idiomatic patterns via web search
3. Outputting session constraints — "use this, avoid that"
4. Staying active as a behavioral guardrail for the session

Set it once at the start of a session, then work normally. If the AI drifts, say "be idiomatic" and it self-corrects.

## Background

The word "idiomatic" comes from natural language — it means "the way a native speaker would say it." The concept migrated to programming as communities grew large enough to develop shared norms. Early examples include Kernighan and Ritchie's *The C Programming Language* (1978), which didn't just teach C syntax — it established how C *should* be written. The tradition continued with every major language's "Effective" books — *Effective Java* by Joshua Bloch, *Effective Go*, *Effective C++* — entire books dedicated to "here's how experienced practitioners actually write this language." It evolved through PEP 8 (2001) to Go's insistence on `gofmt` as the single canonical style (2009).

## Further Reading

- [Go Proverbs](https://go-proverbs.github.io/) — A great example of language-specific idiomatic principles
- [PEP 8](https://peps.python.org/pep-0008/) — Python's style guide, the canonical example of "idiomatic Python"
- [Effective Java](https://www.oreilly.com/library/view/effective-java/9780134686097/) by Joshua Bloch — Idiomatic Java, the book
