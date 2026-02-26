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

## Consuming a Handoff (Resume)

Writing a handoff is only half the lifecycle. The receiving session must **consume** the handoff actively — not just read it, but verify it, prioritize it, and act on it.

### Verify Before Trusting

A handoff is a snapshot from the past. Before trusting its claims:
- **Check the branch** — is the current branch the one the handoff describes? If not, the context may not apply.
- **Check recent commits** — have new commits landed since the handoff was written? If so, some claims about "current state" may be stale.
- **Check file existence** — do the key files listed still exist at those paths? Files move, get renamed, get deleted.
- **Check uncommitted changes** — are there changes the handoff doesn't mention? Someone (or another session) may have worked on this since.

Any discrepancy between the handoff and reality is a **context clash** — flag it explicitly rather than silently resolving it.

### Parse and Prioritize

Don't consume a handoff linearly. Prioritize by actionability:
1. **In-progress work** (P1) — continue what's already started
2. **Next steps** (P2) — the outgoing session's recommended actions
3. **Open questions** (P3) — unresolved decisions that may block progress

Layer the remaining sections as constraints:
- **Dead ends** → "do not attempt" list
- **Gotchas** → warnings to keep in mind
- **Decisions** → context to preserve (not reverse without cause)

### Dead Ends Are Sacred

Dead ends documented in a handoff should never be re-attempted without new evidence that the constraint has changed. "Tried X, failed because Y" means X is off the table unless Y is no longer true. This is the single highest-value property of a good handoff.

### Decisions Carry Forward

Decisions in the handoff carry forward unless explicitly reconsidered. Reversing a documented decision requires:
1. Understanding the original rationale
2. Identifying what has changed to invalidate it
3. Stating the new rationale explicitly

Silent reversal — changing a decision without acknowledging or understanding the original constraint — is one of the most common failure modes in AI-to-AI handoffs.

### Delete After Consumption

By default, a consumed handoff file should be deleted. Stale handoff files left in the repository become **context rot** — a future session may read them, trust outdated claims, and make decisions based on obsolete state. If the handoff is still needed (e.g., work is being paused, not completed), keep it but be aware of the risk.

## Context Failure Modes

These failure modes are specific to context transfer across session boundaries. They're especially dangerous in AI-to-AI handoffs because the receiving agent has no independent memory to cross-reference against.

### Context Poisoning
- **Pattern:** An error or hallucination in the handoff (wrong file path, incorrect claim about behavior, misremembered decision) gets loaded into the new session and treated as ground truth.
- **Why it's dangerous:** The receiving agent has no reason to doubt structured input. One bad claim can cascade through an entire action plan.
- **Mitigation:** Verify handoff claims against git state and actual file contents. Trust evidence over assertions.

### Context Rot
- **Pattern:** An old handoff file sits in the repo. A future session reads it and acts on stale information — file paths that moved, decisions that were reversed, state that changed.
- **Why it's dangerous:** The handoff *looks* authoritative. Nothing in the document signals that it's out of date.
- **Mitigation:** Consume and delete handoffs by default. If keeping one, always compare the handoff date against recent commit history before trusting it.

### Context Clash
- **Pattern:** The handoff says one thing, but the current state says another. Branch name doesn't match, files have changed, new commits exist that contradict the handoff's claims.
- **Why it's dangerous:** The receiving agent may silently resolve the contradiction — trusting the handoff over reality or vice versa — without flagging it.
- **Mitigation:** Explicitly flag every discrepancy between the handoff and current git state. Don't silently resolve conflicts.

### Assumption Cascading
- **Pattern:** One unverified claim from the handoff ("the auth module uses JWT") gets used as the basis for an action plan. If the claim is wrong, every downstream action built on it is also wrong.
- **Why it's dangerous:** The error compounds. By the time it surfaces, multiple files may have been modified based on a false premise.
- **Mitigation:** Ground every handoff claim in evidence before building on it. Check the actual code, not just the handoff's description of it.

### Stale Consumption
- **Pattern:** A handoff written days or weeks ago is consumed without checking whether it's still current. Work may have continued, branches may have merged, decisions may have changed.
- **Why it's dangerous:** The handoff represents a point in time. The longer the gap, the more likely it's diverged from reality.
- **Mitigation:** Compare the handoff date to the most recent commits. If significant work has happened since, treat the handoff as partial context, not complete truth.

### Decision Reversal Without Audit
- **Pattern:** The new session overrides a decision from the handoff without understanding why it was made. "Using PostgreSQL" gets changed to "using SQLite" because it seems simpler — without realizing the decision was made for concurrent write support.
- **Why it's dangerous:** The original constraint still exists. The reversal reintroduces the problem the decision was designed to solve.
- **Mitigation:** Never reverse a documented decision without first reading its rationale and confirming the constraint no longer applies.
