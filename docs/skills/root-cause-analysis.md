# Root Cause Analysis — Skill Reference for AI Assistants

> Systematic techniques for tracing symptoms to their actual causes. Use this reference when diagnosing bugs, failures, or unexpected behavior.

## The 5 Whys Technique

### How It Works

Start with the symptom. Ask "Why did this happen?" Answer. Then ask "Why?" about the answer. Repeat until you reach a cause that is actionable — a design decision, missing constraint, false assumption, or environmental difference.

### Example

1. **Why** did the page crash? → A `TypeError: Cannot read property 'name' of undefined` was thrown.
2. **Why** was the variable undefined? → The API response didn't include the `user` field.
3. **Why** didn't the API include `user`? → The authentication middleware short-circuited and returned a partial response.
4. **Why** did the middleware short-circuit? → The session token was expired but the refresh logic silently failed.
5. **Why** did the refresh fail silently? → The error handler catches all exceptions and returns `null` instead of propagating.

**Root cause:** Silent error swallowing in the token refresh handler. The fix is in the error handler, not in the component that crashed.

### Stopping Criteria

Stop when the answer is one of:
- **A design decision:** "Because the API was designed to return partial responses" → Fix: change the design
- **A missing constraint:** "Because nothing validates the response shape" → Fix: add validation
- **A false assumption:** "Because the code assumes tokens never expire" → Fix: handle expiration
- **An environmental difference:** "Because the CI environment doesn't have the config file" → Fix: ensure environment parity

### Common Mistakes

| Mistake | Problem | Instead |
|---------|---------|---------|
| Stopping too early | You fix a symptom, not the cause | Keep asking "why" until you hit a design/constraint/assumption |
| Going too deep | "Why does JavaScript exist?" isn't helpful | Stop when the cause is actionable by the team |
| Branching | Following multiple causal chains simultaneously | Trace one chain completely, then backtrack if needed |
| Accepting "human error" | "Someone forgot to..." isn't a root cause | Ask why the system allowed the mistake |
| Guessing without evidence | "I think it's probably..." | Every hypothesis must have a testable prediction |

## Fault Tree Analysis (Simplified)

### When to Use

When a symptom could have multiple independent causes. The 5 Whys traces a single chain; fault tree analysis maps all possible causes.

### How It Works

1. **Top event:** The symptom (e.g., "API returns 500")
2. **Gates:** Connect causes using AND (all must be true) or OR (any one is sufficient)
3. **Leaves:** Testable conditions you can verify

```
API returns 500
├── OR ─┬── Database connection fails
│       │   ├── AND ─┬── Connection pool exhausted
│       │   │        └── No connection timeout configured
│       │   └── OR ──┬── Database server down
│       │            └── Wrong connection string
│       └── Unhandled exception in handler
│           ├── OR ──┬── Null reference on missing field
│                    └── Type coercion error
```

### Testing the Tree

Start at the leaves. Test each condition:
- **Confirmed:** This branch is (part of) the cause
- **Eliminated:** Prune this branch
- **Inconclusive:** Gather more evidence

Work from leaves to root. The path from root to confirmed leaf is your causal chain.

## Root Cause Categories

| Category | Signals | Example |
|----------|---------|---------|
| **Logic error** | Wrong condition, off-by-one, incorrect algorithm | `if (i <= arr.length)` instead of `< arr.length` |
| **State management** | Stale state, unexpected mutation, initialization order | Component reads state before it's populated |
| **Race condition** | Timing-dependent, works in debugger, intermittent | Two async operations write to the same variable |
| **Type mismatch** | Wrong type passed, implicit conversion, null/undefined | String `"5"` compared with `===` to number `5` |
| **Missing validation** | Bad input reaches code that assumes good input | API handler doesn't check for required fields |
| **Configuration error** | Wrong setting, env var, or feature flag | `DATABASE_URL` points to staging in production |
| **Dependency issue** | Version mismatch, breaking change, missing dep | Library updated with breaking API change |
| **Design flaw** | Architecture doesn't support the use case | Synchronous API trying to handle streaming data |
| **Environmental** | Works on one machine/OS/version but not another | Path separator differences between OS, timezone issues |

### Choosing the Right Category

- If the code does the wrong thing with correct input → **Logic error**
- If the code does the right thing but at the wrong time → **State management** or **Race condition**
- If the code does the right thing but with wrong input → **Missing validation** or **Type mismatch**
- If the code is correct but the environment is wrong → **Configuration error** or **Environmental**
- If no local fix is sufficient → **Design flaw**

## Hypothesis Testing Checklist

For each hypothesis during root cause tracing:

- [ ] **State the hypothesis clearly:** "The bug occurs because [X]"
- [ ] **Predict observable evidence:** "If true, we should see [Y] in [location]"
- [ ] **Test one variable at a time:** Don't change multiple things
- [ ] **Record the result:** Confirmed, rejected, or inconclusive
- [ ] **If confirmed:** Ask "Why does [X] happen?" — go deeper
- [ ] **If rejected:** Form a new hypothesis based on what you learned
- [ ] **If inconclusive:** Gather more evidence before proceeding

## Reporting Template

Use this format when reporting root cause analysis results:

```
DIAGNOSIS
══════════════════════════════════════════════════════════════

Symptom:       <one-line summary of what was observed>
Root Cause:    <one-line summary of the fundamental issue>
Category:      <from categories table>

CAUSAL CHAIN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<symptom>
  ← <cause 1>
    ← <cause 2>
      ← <ROOT CAUSE>

FIX RECOMMENDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Specific changes that address the root cause>

DEFENSE IN DEPTH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Additional safeguards to prevent recurrence>

VERIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Steps to confirm the fix works>
```
