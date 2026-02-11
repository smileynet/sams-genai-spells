# The Idiomatic Technique

## Where This Came From

The word "idiomatic" comes from natural language — it means "the way a native speaker would say it." In programming, idiomatic code means writing code the way the community expects it to be written. Not the cleverest way. Not your way. The community's way.

Sam didn't invent this concept (obviously). Every language community has been arguing about "the right way" since the first style guide was published. What Sam noticed was that AI assistants are *terrible* at being idiomatic — they hallucinate APIs that don't exist, mix patterns from different framework versions, and confidently use deprecated approaches.

So Sam started every session with the same speech: "Use the real APIs. Check the docs. Don't make stuff up." After typing this roughly four hundred times, he made it a button.

## The Core Idea

When you write idiomatic code, you're doing two things:

1. **Using documented, canonical patterns** — not inventing new ways to do things that already have a standard approach
2. **Matching community expectations** — so other developers (and AI assistants in future sessions) can read your code without a decoder ring

For AI assistants specifically, "be idiomatic" means:
- Don't hallucinate API signatures — use the ones in the actual documentation
- Don't mix patterns from different versions of a framework
- Prefer the approach recommended by official docs, not Stack Overflow answers from 2017
- If you're not sure an API exists, say so

## Why It Works With AI

Large language models are trained on a mix of everything — old code, new code, blog posts, wrong answers, deprecated tutorials. When you ask an LLM to write React code, it might pull from React 16, React 18, and React 19 all in the same response. It doesn't inherently know which version you're using.

The idiomatic spell constrains the AI by:
- Establishing which version of a tool you're actually using
- Listing the correct import paths and API signatures up front
- Flagging deprecated patterns that should be avoided
- Creating a "contract" the AI follows for the rest of the session

This is essentially the same technique as giving a style guide to a new team member — except the team member has read the entire internet and needs help filtering.

## How Sam Uses It

At the start of any session involving a specific tool or framework, Sam runs `/spell:idiomatic <tool>`. The spell:

1. Detects the tool version from the codebase (package.json, pyproject.toml, etc.)
2. Researches current idiomatic patterns via web search
3. Outputs a set of session constraints — "use this, avoid that"
4. Stays active for the session as a behavioral guardrail

The key insight is that this only needs to happen once per session. Set the constraints, then work normally. If the AI drifts, say "be idiomatic" and it self-corrects.

## Beyond This Spell

The idiomatic principle applies wherever you're working with AI:

- **In any AI chat:** Start by telling the AI what version of tools you're using and to stick to documented APIs
- **In code review:** When reviewing AI-generated code, check that it uses canonical patterns for your stack
- **In team onboarding:** Share your team's style guide with AI assistants the same way you'd share it with new hires
- **In prompt engineering generally:** Constraining AI behavior up front is always cheaper than fixing mistakes afterward

## Further Reading

- [Go Proverbs](https://go-proverbs.github.io/) — A great example of language-specific idiomatic principles
- [PEP 8](https://peps.python.org/pep-0008/) — Python's style guide, the canonical example of "idiomatic Python"
- [Effective Java](https://www.oreilly.com/library/view/effective-java/9780134686097/) by Joshua Bloch — Idiomatic Java, the book
