# Problem Framing & Reframing — Skill Reference for AI Assistants

> Techniques for questioning whether you're solving the right problem. Use this reference when challenging the framing of a plan, decision, or direction — not optimizing within a frame, but questioning the frame itself.

## Problem Setting vs Problem Solving (Schon 1983)

Donald Schon's *The Reflective Practitioner* identifies a critical distinction: expert practitioners spend most of their effort on **problem setting** — naming what to attend to and framing the context — before attempting to solve anything.

### The High Ground vs. The Swamp

Schon's metaphor: some problems sit on the "high ground" — well-defined, amenable to technical analysis. But the most important problems live in the "swamp" — messy, ambiguous, resistant to clean formulation. Practitioners who stay on the high ground solve clean problems that may not matter; those who descend into the swamp grapple with the problems that do.

### Five Evaluation Criteria for Candidate Frames

When evaluating a problem frame, check:

1. **Can it work?** — Does the frame suggest actionable solutions?
2. **Satisfying results?** — Would solving the problem-as-framed produce a satisfying outcome?
3. **Coherent?** — Is the frame internally consistent? Does it account for the key facts?
4. **Aligned with values?** — Does it fit the practitioner's (or organization's) beliefs and priorities?
5. **Maintains inquiry momentum?** — Does it open further exploration, or shut it down prematurely?

### Reflection-in-Action

Experts don't frame once and commit. They run small experiments against the frame — probing whether it holds, adjusting when it doesn't. This is "reflection-in-action": framing, testing, reframing, in a continuous loop. The frame is a hypothesis, not a commitment.

### Expert vs. Novice Time Allocation

Research on engineering problem-solving (ASEE) found that experts spent 17% of their time solving the problem and the rest understanding and framing it. Novices spent 55% of their time solving — jumping to solutions before understanding what they were solving. The experts' investment in framing produced better solutions faster, not slower.

## Frame Innovation (Dorst 2011/2015)

Kees Dorst's *Frame Innovation* extends Schon's work into a systematic methodology for creating new frames.

### Abductive Logic

Standard reasoning works from WHAT + HOW → VALUE (given a thing and a method, predict the outcome). Frame innovation reverses this: given only the desired VALUE, create both the WHAT and the HOW. This is abductive reasoning — reasoning backward from desired outcome to a frame that produces it.

### Problem-Solution Co-Evolution (Dorst & Cross 2001)

Dorst and Cross observed that problems and solutions do not proceed sequentially (understand the problem, then solve it). Instead, they co-evolve — working on the solution deepens understanding of the problem, which changes the solution, which further refines the problem. Creative insight occurs when a stable problem-solution pairing "frames" — when the evolving understanding of problem and solution click into alignment.

**Implication:** Don't wait for perfect problem understanding before starting work. But don't commit to early solutions either. Hold both loosely while they co-evolve.

### Nine-Step Frame Creation Process

Dorst's full methodology:
1. Archaeology — dig into the problem history
2. Paradox — identify the core tension
3. Context — map the broader situation
4. Field — identify relevant stakeholders and their frames
5. Themes — find recurring patterns across stakeholder perspectives
6. Frames — generate candidate frames
7. Futures — explore where each frame leads
8. Transformation — select and develop the most promising frame
9. Integration — embed the new frame into practice

## Reframing Techniques

### Six Reframing Moves

| Move | What changes | Example |
|------|-------------|---------|
| **Shift beneficiary** | Who the solution serves | "How do we help users find content?" → "How do we help content find users?" |
| **Shift system boundary** | What's inside vs. outside the problem | "How do we speed up deploys?" → "How do we make deploy speed irrelevant?" |
| **Shift time horizon** | When success is measured | "How do we ship by Q3?" → "How do we build something we won't need to rewrite in 2 years?" |
| **Shift abstraction level** | How specific or general the problem is | "How do we reduce checkout errors?" → "Why are users reaching checkout in a confused state?" |
| **Shift success metric** | What counts as a good outcome | "How do we increase sign-ups?" → "How do we increase retained users at 30 days?" |
| **Negate the constraint** | Question whether a constraint is real | "Given we need a database migration..." → "What if we didn't migrate?" |

### Abstraction Laddering (Hayakawa)

S.I. Hayakawa's abstraction ladder provides a simple technique for reframing:

- **Ask "Why?"** to go up — more strategic, more causal, broader scope. "Why do we need faster deploys?" → "Because feedback loops are too slow." → "Why are feedback loops slow?" → "Because we batch changes."
- **Ask "How?"** to go down — more concrete, more tactical, narrower scope. "How do we speed up feedback loops?" → "Ship smaller changes more often."

**The sweet spot:** Find the level where creative but actionable solutions emerge. Too high and you get philosophy ("How do we create value?"). Too low and you're back to the original frame ("How do we optimize the deploy script?").

### Wedell-Wedellsborg's Seven Practices (HBR 2017)

Thomas Wedell-Wedellsborg's research found 85% of executives said their organizations were bad at problem diagnosis. His seven reframing practices:

1. **Establish legitimacy** — Make it safe to question the problem definition
2. **Bring outsiders in** — People outside the problem bring different frames
3. **Get definitions in writing** — Forces precision; reveals disagreements hidden by vague language
4. **Ask what's missing** — Look for the dog that didn't bark
5. **Consider multiple categories** — Is this a usability problem, an emotional problem, or a process problem?
6. **Analyze positive exceptions** — When does the problem NOT occur? What's different about those cases?
7. **Question the objective** — Why do we want this? Is there a deeper goal?

**The Nickelodeon example:** Nickelodeon ran hundreds of A/B tests on their sign-up flow, framing the problem as usability. None worked. Reframing revealed an emotional problem — children were afraid of the password creation prompt. The fix wasn't a better form; it was reassurance.

## Problem Dissolution (Ackoff)

Russell Ackoff identified four responses to problems:

| Response | Description | Example |
|----------|-------------|---------|
| **Absolution** | Ignore the problem — hope it goes away | "Let's wait and see" |
| **Resolution** | Apply a good-enough fix — satisficing | "Add a retry with backoff" |
| **Solution** | Find the optimal fix — optimizing | "Re-architect the retry logic with circuit breakers" |
| **Dissolution** | Redesign the system so the problem ceases to exist | "Eliminate the fragile dependency entirely" |

Ackoff's key insight: **"We fail more often because we solve the wrong problem than because we get the wrong solution to the right problem."**

Most effort goes to resolution and solution. Dissolution — the highest-leverage response — requires stepping outside the problem frame entirely. It asks not "How do we fix this?" but "How do we make this impossible?"

## Design Fixation (Jansson & Smith 1991)

### The Phenomenon

Jansson and Smith demonstrated that designers anchor on initial frames and solutions even when explicitly told those examples are flawed. Participants shown a flawed example design incorporated its features into their own solutions at high rates — even after being warned about the flaws.

### Related Cognitive Biases

- **Einstellung effect** (Luchins 1942) — Applying a known method even when a better one exists, because the known method "comes to mind" first
- **Functional fixedness** (Duncker 1945) — Inability to see an object (or component) serving a function other than its conventional one

### Mitigation Strategies

- **Abstraction** — Work at a higher abstraction level before going concrete. Abstract descriptions are less prone to fixation than concrete examples.
- **Cross-domain analogies** — Import frames from unrelated fields. They break the fixation anchor because they don't share surface features.
- **Diverse prior art** — Survey multiple existing solutions before ideating. Exposure to variety reduces anchoring on any single example.
- **Explicit frame testing** — Regularly ask: "Are we solving this because it's the right problem, or because we've been staring at it too long?"

## Wicked Problems (Rittel & Webber 1973)

Horst Rittel and Melvin Webber identified a class of problems — "wicked problems" — that resist traditional problem-solving:

- **No definitive formulation** — The problem definition depends on your viewpoint
- **No stopping rule** — There's no clear point where the problem is "solved"
- **No true/false, only better/worse** — Solutions can't be objectively correct
- **No immediate or ultimate test** — Consequences play out over time in unpredictable ways
- **Every solution is a "one-shot operation"** — You can't experiment cheaply; every attempt changes the situation
- **No enumerable set of solutions** — There's no complete list of possible approaches
- **Every wicked problem is unique** — Transferring solutions from similar problems may not work
- **Every wicked problem is a symptom of another problem** — Solving one layer reveals the next

**Key insight for AI application:** Formulating the problem IS the problem. When you encounter a wicked problem, the most valuable work is reframing — not solving. Multiple stakeholder frames, Schon's reflection-in-action, and Dorst's frame innovation are more appropriate tools than optimization.

## Antipatterns

**AP: THE COSMETIC REFRAME**
Rewording the problem without changing its substance — same frame, different words. "How do we increase throughput?" becomes "How do we improve performance?" The test: does the new frame suggest solutions the old frame would have excluded? If not, it's cosmetic. A genuine reframe opens a different solution space.

**AP: THE PREMATURE FRAME**
Locking in a problem definition before sufficient understanding. The first framing becomes authoritative and drives all subsequent work. Requirements errors cost 15x more to fix post-coding (NASA/NIST). Kodak's fatal frame: "How do we sell more prints?" instead of "What is the future of sharing memories?"

**AP: THE SOLUTION IN DISGUISE**
A problem statement that encodes the desired solution. "How can we use 360-degree feedback more effectively?" presupposes 360-degree feedback is the answer. "How can we build a better notification system?" presupposes notifications are the solution. The test: if only one category of solution is generated, a solution is embedded in the frame.

**AP: THE LAW OF THE INSTRUMENT**
Experts frame problems through their specialty. To a database engineer, it's a data modeling problem. To a frontend developer, it's a UX problem. To a manager, it's a process problem. The test: does the frame reflect available toolkit or actual problem structure? Actively seek framings from outside your specialty.

**AP: REFRAMING PARALYSIS**
Generating alternative frames without committing to any of them. Reframing becomes a substitute for action — endlessly re-questioning without forward progress. Mitigation: time-box framing work. "Good enough to start" is the correct standard. Schon's reflection-in-action treats frames as hypotheses to test, not conclusions to reach.

## Sources

- Schon, D. (1983). *The Reflective Practitioner: How Professionals Think in Action*. Basic Books.
- Dorst, K. (2011). "The core of 'design thinking' and its application." *Design Studies*.
- Dorst, K. (2015). *Frame Innovation: Create New Thinking by Design*. MIT Press.
- Dorst, K. & Cross, N. (2001). "Creativity in the design process: co-evolution of problem–solution." *Design Studies*.
- Wedell-Wedellsborg, T. (2017). "Are You Solving the Right Problems?" *Harvard Business Review*.
- Hayakawa, S.I. (1949). *Language in Thought and Action*. Harcourt.
- Ackoff, R. (1974). *Redesigning the Future*. Wiley.
- Jansson, D. & Smith, S. (1991). "Design fixation." *Design Studies*.
- Luchins, A. (1942). "Mechanization in problem solving: The effect of Einstellung." *Psychological Monographs*.
- Duncker, K. (1945). "On problem-solving." *Psychological Monographs*.
- Rittel, H. & Webber, M. (1973). "Dilemmas in a General Theory of Planning." *Policy Sciences*.
- Kahneman, D. & Tversky, A. (1981). "The Framing of Decisions and the Psychology of Choice." *Science*.
