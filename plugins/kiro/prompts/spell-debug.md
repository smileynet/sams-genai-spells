## Summary

**Systematic root cause analysis for bugs, errors, and unexpected behavior.** Uses hypothesis-driven debugging to trace symptoms back to their actual cause before attempting fixes. Applies the 5 Whys, fault tree analysis, and the scientific method to prevent shotgun debugging.

**Arguments:** `$ARGUMENTS` (required) - Error message, symptom description, stack trace, file path, or bug description

**Output:** Structured diagnosis report with root cause, causal chain, category, and fix recommendation

---

## Skill References

Before proceeding, load the relevant skill documents for reference:

Check the repository's `docs/skills/` directory for root cause analysis and debugging antipattern references.

---

## Process

### Step 1: Clarify the Symptom

Parse `$ARGUMENTS` to determine what the user is experiencing:

| Input type | Action |
|------------|--------|
| Stack trace or error message | Symptom is defined — extract error type, location, and message. Skip to Step 2. |
| File path | Read the file, look for recent changes and obvious issues. Ask what's wrong. |
| Bug description | Extract: what happened, what was expected, when it started. |
| Vague or incomplete | Clarify before proceeding (see below). |

**If the symptom is unclear:**
Ask the user to describe the symptom: what happened, what they expected, and when it started.

**Output the symptom summary:**

```
SYMPTOM
══════════════════════════════════════════════════════════════

Observed:  <what actually happens>
Expected:  <what should happen>
Context:   <when it started, frequency, environment>
```

---

### Step 2: Gather Evidence

Collect evidence from multiple sources before forming any hypothesis.

Examine the relevant code files, check recent git changes, search for related error messages and patterns, and search the web to understand what the error indicates (not to find fixes).

**Graceful degradation:** If web search is unavailable, rely on code analysis and built-in knowledge. Note this limitation.

**Output the evidence summary:**

```
EVIDENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Files examined:
- <file:line> — <what was found>

Recent changes:
- <commit or diff summary relevant to the symptom>

Related code:
- <other code paths that interact with the affected area>

External context:
- <what web research revealed about the error or behavior>
  (or "Web research unavailable — using built-in knowledge")
```

---

### Step 3: Root Cause Tracing (5 Whys)

Trace backward from the symptom through the causal chain. One hypothesis at a time, one variable at a time.

**For each level of the chain:**

1. **State a hypothesis:** "The symptom occurs because [X]"
2. **Predict evidence:** "If this hypothesis is correct, we should see [Y]"
3. **Test the prediction:** Check the code, run a command, or read a file to verify
4. **Confirm or reject:** If confirmed, ask "Why does [X] happen?" and go deeper. If rejected, form a new hypothesis.

**Stopping criteria — stop when you reach a cause that is:**
- A design decision (intentional but wrong for this case)
- A missing constraint (validation, type check, guard clause that should exist)
- A false assumption (code assumes something that isn't true)
- An environmental difference (works in one environment, fails in another)

**Pressure resistance:**
- If the user says "just fix it" or pushes to skip analysis, explain: root cause tracing IS the fastest path. Fixing symptoms creates new bugs.
- If the user has already tried 3+ fixes that didn't work, flag this as likely architectural — the root cause is probably deeper than the symptom suggests.

**Output the causal chain:**

```
ROOT CAUSE ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Why 1: <symptom occurs because...>
  Evidence: <what confirmed this>

Why 2: <that happens because...>
  Evidence: <what confirmed this>

Why 3: <that happens because...>
  Evidence: <what confirmed this>

[...continue until root cause reached]

Root cause: <the fundamental issue>
```

---

### Step 4: Verify and Report

Before reporting, verify the root cause:
- **Does it explain ALL symptoms?** If not, there may be multiple root causes or you stopped too early.
- **Is it actionable?** A root cause should suggest a specific fix, not a vague improvement.
- **Is it the root, not a symptom?** Apply one more "why" — if the answer is "because that's how it was designed," you've found the root.

**Categorize the root cause:**

| Category | Signals |
|----------|---------|
| **Logic error** | Wrong condition, off-by-one, incorrect algorithm |
| **State management** | Stale state, mutation side effects, initialization order |
| **Race condition** | Timing-dependent, works in debugger but fails in production |
| **Type mismatch** | Wrong type passed, implicit conversion, null where non-null expected |
| **Missing validation** | Bad input reaches code that assumes good input |
| **Configuration error** | Wrong setting, environment variable, or feature flag |
| **Dependency issue** | Version mismatch, breaking change, missing dependency |
| **Design flaw** | Architecture doesn't support the use case — fix requires redesign |
| **Environmental** | Works on one machine/OS/version but not another |

**Output the full diagnosis:**

```
DIAGNOSIS
══════════════════════════════════════════════════════════════

Symptom:       <one-line summary>
Root Cause:    <one-line summary>
Category:      <from table above>

CAUSAL CHAIN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<symptom>
  ← <cause 1>
    ← <cause 2>
      ← <ROOT CAUSE>

FIX RECOMMENDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Specific fix that addresses the root cause, not the symptom.
 Include file paths and what to change.>

DEFENSE IN DEPTH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<1-3 additional safeguards to prevent similar bugs:
 - Tests to add
 - Assertions or type guards
 - Monitoring or logging>

RELATED RISKS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Other places in the codebase where the same root cause pattern
 might exist. Check these proactively.>
  (or "None identified")

VERIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Steps to confirm the fix works:>
1. <verification step>
2. <verification step>
```

---

## Guidelines

- **Never fix before diagnosing.** The spell produces a diagnosis, not a patch. Fix comes after understanding.
- **One hypothesis at a time.** Changing multiple things simultaneously makes it impossible to know what worked.
- **Trace the chain, don't guess the root.** The root cause is rarely the first thing you suspect.
- **Web research is for understanding, not solution-hunting.** Search to understand what an error means, not to find code to copy.
- **Name the category.** If a bug doesn't fit the 9 categories, that's a signal — re-examine the diagnosis.
- **Check for siblings.** Once you find a root cause, check if the same pattern exists elsewhere in the codebase.
- **Credit:** This spell applies the 5 Whys (Ohno/Toyota Production System), fault tree analysis (Bell Labs, 1961), and systematic debugging principles from Zeller's *Why Programs Fail* and the scientific method.

---

## Example Usage

```
@spell-debug TypeError: Cannot read properties of undefined (reading 'map')
@spell-debug the login form submits but nothing happens — no error, no redirect
@spell-debug tests pass locally but fail in CI
@spell-debug src/api/handler.ts — intermittent 500 errors on the /users endpoint
```
