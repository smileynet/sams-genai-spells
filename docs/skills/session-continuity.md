# Session Continuity — Skill Reference for AI Assistants

> Techniques for maintaining work continuity across AI session boundaries. Use this reference when capturing or consuming handoff documents, especially for AI-to-AI transitions where the receiving agent has zero prior context.

## The Context Window Problem

AI coding sessions have a hard boundary: when the context window fills, compresses, or the session ends, all accumulated context disappears. Unlike human developers who retain partial memory, an AI agent in a new session has **literally zero** knowledge of:

- What was being worked on
- What was tried and failed
- Why specific decisions were made
- What state the code is in
- What should happen next

This makes session transitions the highest-risk moment for context loss. A structured handoff document is the only reliable bridge.

## What to Capture

### Decisions With Rationale

**Capture format:** `[Decision] — Reason: [why this over alternatives]`

Not just the choice, but the reasoning. Decisions without rationale are dangerous because:
- The next session may reverse them without understanding the constraint
- Alternatives that were considered and rejected may be re-evaluated unnecessarily
- The decision may have been based on context that isn't obvious from the code

**Examples:**
- Good: "Used SQLite for local dev — Reason: team has no Docker requirement, PostgreSQL would add setup friction for contributors"
- Bad: "Using SQLite" (why? when should this change? what was considered?)

### Dead Ends With Reasons

**Capture format:** `Tried: [approach] — Abandoned because: [specific reason]`

This is the highest-value section of any handoff. Dead ends are invisible in code — the code only shows what was kept, not what was tried and rejected. Without documenting dead ends, the next session will:
1. Consider the same approach (it looks reasonable from the outside)
2. Spend time implementing it
3. Hit the same wall
4. Abandon it for the same reason

This loop can repeat indefinitely across sessions.

**Examples:**
- Good: "Tried: native `fetch` for HTTP requests — Abandoned because: no built-in timeout support in Node 18, would need AbortController wrapper that adds more complexity than using `got`"
- Bad: "Tried fetch, didn't work" (didn't work how? would it work with a workaround?)

### Current State

Categorize work items into three buckets:
- **Completed** — done and verified
- **In progress** — started but not finished (include where it stands)
- **Not started** — planned but not begun

This prevents the next session from re-doing completed work or skipping incomplete work.

### Next Steps

**Must be specific and actionable.** Each step should tell the reader:
- What to do (the action)
- Where to do it (file paths, function names, endpoints)
- Why (enough context to understand the purpose)

**Examples:**
- Good: "Add input validation to `POST /api/users` in `src/routes/users.ts:47` — currently accepts any request body, needs to validate against the `CreateUserSchema` in `src/types/user.ts`"
- Bad: "Continue working on the API" (which endpoint? what's left? what's the goal?)

### Open Questions

Unresolved decisions or uncertainties that need input. Each question should note:
- What the question is
- Who or what can answer it (stakeholder, tech investigation, design review)
- What assumption is being made in the absence of an answer

## Git State as Evidence

Git commands provide objective evidence about the state of work:

| Command | What it reveals |
|---------|----------------|
| `git status` | Modified, staged, and untracked files — what's actively being worked on |
| `git log --oneline -N` | Recent commit history — what's been completed |
| `git diff` | Current uncommitted changes — work in progress |
| `git diff --cached` | Staged changes — work about to be committed |
| `git stash list` | Stashed work — partially completed or experimental changes |
| `git branch --show-current` | Current branch — context for the work |

Use git state to **ground** the handoff in reality. Assertions like "the feature is almost done" should be backed by evidence: what's committed, what's still changed, what tests pass.

## Anti-Patterns

### Vague Next Steps
- **Pattern:** "Continue working on the feature" / "Finish the implementation"
- **Why it fails:** The next session doesn't know what "continue" means or where to start
- **Fix:** Specific actions with file paths: "Add error handling to `processPayment()` in `src/billing/processor.ts`"

### Missing Dead Ends
- **Pattern:** Handoff only describes what was done, not what was tried and abandoned
- **Why it fails:** The next session retries failed approaches, wasting identical time
- **Fix:** Explicitly document dead ends even when there are few: "None identified" proves you checked

### Omitting Rationale
- **Pattern:** "Using React" / "Chose PostgreSQL" — the decision without the why
- **Why it fails:** Decisions get reversed without understanding the constraint that motivated them
- **Fix:** Always include "Reason: [why this over alternatives]"

### Assuming Reader Context
- **Pattern:** "As discussed earlier..." / "The issue we identified..." / "Per our conversation..."
- **Why it fails:** The reader has no access to prior conversations. AI agents have zero memory.
- **Fix:** Write as if the reader is starting from absolute zero. Explain everything.

### Status Without Evidence
- **Pattern:** "The feature is almost done" / "Tests are passing"
- **Why it fails:** Subjective assertions can't be verified. "Almost done" means nothing.
- **Fix:** Ground claims in git state: "5 of 7 endpoints implemented (see commits abc..def), 2 remaining: DELETE /users and PATCH /users/:id"

## AI-to-AI Specifics

When one AI session hands off to another:

1. **Zero shared memory** — there is no "as we discussed." Everything must be explicit.
2. **No ambient awareness** — the receiving session doesn't know what tools were tried, what errors appeared, or what the user's preferences are.
3. **No inferring from absence** — if a section is missing, the receiving session can't distinguish "checked and found nothing" from "forgot to check."
4. **Context window is precious** — the handoff document will consume part of the receiving session's context window. Be comprehensive but not verbose. Every sentence should earn its space.
5. **Structure aids parsing** — consistent section headers, bullet formats, and labeling help the receiving AI quickly locate specific information rather than reading the entire document linearly.
