# Debugging Antipatterns — Skill Reference for AI Assistants

> Common debugging mistakes that waste time and create new bugs. Use this reference to avoid ineffective debugging patterns and maintain discipline during diagnosis.

## Seven Debugging Antipatterns

### 1. Shotgun Debugging

Change multiple things at once and hope something works.

**Why it's tempting:** Feels productive. Each change is a "try." Momentum feels like progress.
**Why it fails:** When something finally works, you don't know which change fixed it — or whether the other changes introduced new bugs. You've also lost the ability to reason about causality.
**Instead:** Change one thing at a time. Predict what will happen before each change. If the prediction is wrong, that's information.

### 2. Symptom Fixing

Add a null check, try/catch wrapper, or default value to suppress the error without understanding why it occurs.

**Why it's tempting:** The error goes away. Tests pass. The PR gets approved. Ship it.
**Why it fails:** The root cause is still there. The null check masks a state management bug. The try/catch hides a logic error. The default value silently produces wrong results. The bug resurfaces later in a harder-to-diagnose form.
**Instead:** Ask "Why is this value null/wrong/missing?" before adding any guard. The guard might still be the right fix — but only after you understand the cause.

### 3. Cargo Cult Fix

Copy a fix from Stack Overflow, an AI suggestion, or a similar-looking bug report without understanding why it works.

**Why it's tempting:** Someone else already solved this. Why waste time understanding it?
**Why it fails:** The fix addresses a different root cause that happens to produce similar symptoms. It may work in the other person's context but not yours. When it breaks, you have no mental model to debug from.
**Instead:** Read the fix. Understand what it changes. Predict what effect it should have. Then apply it and verify the prediction.

### 4. Printf Without Hypothesis

Add logging statements everywhere to "see what's happening" without a specific question to answer.

**Why it's tempting:** You don't know what's wrong, so you look at everything. More data must help.
**Why it fails:** You drown in output. You can't distinguish signal from noise because you didn't define what signal looks like. You end up scrolling through logs for patterns instead of testing theories.
**Instead:** Form a hypothesis first: "I think the value of X is wrong at line Y." Then add ONE log statement to test that specific prediction. Confirm or reject. Repeat.

### 5. Blame the Environment

Assume the bug is in the library, framework, compiler, OS, or hardware before investigating your own code.

**Why it's tempting:** "My code looks fine" is more comfortable than "I made a mistake." Libraries do have bugs.
**Why it fails:** Your code is almost always the problem. Library bugs exist but are rare in mature projects. Time spent investigating the framework is time not spent reading your own code. When it turns out to be your bug (it usually does), you've wasted hours.
**Instead:** Assume your code is wrong until you have strong evidence otherwise. If you suspect a library bug, write a minimal reproduction that isolates the library behavior from your code.

### 6. The Shallow Fix

Fix the bug at the first level of the causal chain without tracing deeper.

**Why it's tempting:** The first-level cause is real — it's not wrong. Fixing it does address the immediate problem.
**Why it fails:** The same root cause produces other symptoms you haven't seen yet. The fix addresses one manifestation but leaves the pattern intact. You'll be debugging a sibling bug next week.
**Instead:** Apply the 5 Whys. When you find a cause, ask "Why does this happen?" at least twice more before deciding where to fix.

### 7. Fixing Under Pressure

Skipping diagnosis because there's a deadline, an outage, or someone watching over your shoulder.

**Why it's tempting:** Urgency is real. Stakeholders want it fixed NOW. Spending time "analyzing" feels like stalling.
**Why it fails:** Pressure leads to symptom fixes, which leads to regressions, which leads to more pressure. The cycle accelerates. The "quick fix" becomes permanent, and the real bug becomes harder to find under layers of patches.
**Instead:** Triage first: can you mitigate (revert, feature-flag, redirect) without fixing? Mitigation buys time for proper diagnosis. If you must fix under pressure, document your assumptions so someone can verify the root cause later.

## Expert vs. Novice Debugging

| Dimension | Novice Pattern | Expert Pattern |
|-----------|---------------|----------------|
| **Starting point** | Starts at the symptom and guesses | Starts at the symptom and gathers evidence |
| **Hypothesis formation** | "Maybe it's this?" (vague) | "If X is wrong, then Y should show Z" (testable) |
| **Changes per test** | Multiple changes at once | One change at a time |
| **Response to failure** | Try something else randomly | Update mental model based on what was learned |
| **Error messages** | Googles the message for a fix | Reads the message to understand what happened |
| **Web research** | Looks for code to copy | Looks for explanations to understand |
| **When stuck** | Tries harder at the same approach | Steps back and questions assumptions |
| **Fix verification** | "It works now" (symptom gone) | "It works because [root cause] is addressed" |
| **After fixing** | Moves on | Checks for sibling bugs with same root cause |

## Pressure Resistance Guidance

### When the user says "just fix it"

Respond with understanding, then redirect:

> "I understand the urgency. Root cause tracing IS the fastest path — fixing symptoms creates new bugs that take longer to diagnose. Let me trace this quickly."

### When the user has tried 3+ fixes already

This is a strong signal that the root cause is deeper than the symptom suggests:

> "You've tried multiple fixes and the bug persists — that's a signal the root cause is deeper than it appears. Let me trace the causal chain from scratch instead of trying more surface-level fixes."

### When there's a production outage

Separate mitigation from diagnosis:

1. **Mitigate first:** Revert, feature-flag, or redirect traffic. This buys time.
2. **Diagnose second:** With pressure reduced, trace the root cause properly.
3. **Fix third:** Apply a fix that addresses the root cause, not just the symptom.
4. **Prevent fourth:** Add tests, monitoring, or validation to catch this class of bug.

## The Debugging Mindset

- **Bugs are not random.** Every bug has a deterministic cause. "It just started happening" means "something changed that I haven't identified yet."
- **The code is doing exactly what you told it to.** The bug is in your understanding, not in the computer's execution.
- **Reading is faster than guessing.** Read the code, read the error, read the docs. Most bugs are visible once you look at the right place.
- **Evidence over intuition.** Intuition suggests hypotheses. Evidence confirms or rejects them. Don't skip the evidence step.
