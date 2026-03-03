# Problem Framing & Strategic Thinking

## The Problem

A team spends four months building a perfect notification system. Smart batching, user preference modeling, multi-channel delivery, A/B tested copy. When they ship, it's technically excellent. Three percent of users have notifications enabled. The top reason users churn isn't missing notifications — it's a confusing onboarding flow that loses them before they ever see a notification.

The notification system solved the wrong problem. Not because the solution was bad, but because nobody questioned whether notifications were the right problem to solve. The team optimized brilliantly within a frame that was pointing the wrong direction.

AI assistants make this worse in a specific way. Ask an AI to help you build a notification system, and it'll help you build the best notification system it can — architecture options, delivery strategies, batching algorithms. What it won't do, unprompted, is ask: "Why are only 3% of users subscribed?" or "What's actually causing churn?" or "What if the problem isn't notifications at all?" The AI is extraordinarily helpful at executing within a frame, and completely silent about whether the frame is right.

## How It Helps

A zoom-out analysis does four things:

1. **Challenges the problem framing itself** — restates the problem multiple ways to see if the current frame is actually the best one, or just the first one someone articulated
2. **Inverts the goal** to find failure modes hiding inside success — "If this succeeds perfectly, then what?" reveals scale problems, lock-in, and consequences nobody planned for
3. **Weighs what you're NOT doing** — every choice forecloses alternatives, and the best forgone option is the real cost of the current direction
4. **Traces consequences past the intended outcome** — "And then what?" at multiple time horizons catches ecosystem responses, feedback loops, and second-order effects that first-order analysis misses

The output isn't a list of worries. It's a strategic recommendation — stay course, adjust, pivot, or stop — backed by evidence from five independent lenses, with specific next actions calibrated to the recommendation level.

## Why It Works

Donald Schon studied how expert practitioners actually think. His key finding: experts spend most of their effort on "problem setting" — naming what to attend to and framing the context — before attempting to solve anything. Research on engineering problem-solving found that experts spent 17% of their time solving and the rest understanding and framing. Novices spent 55% solving — jumping to solutions before understanding what they were solving.

Russell Ackoff put it more bluntly: **"We fail more often because we solve the wrong problem than because we get the wrong solution to the right problem."**

Thomas Wedell-Wedellsborg's research found that 85% of executives said their organizations were bad at problem diagnosis. Not problem-solving — problem diagnosis. Organizations are full of people who are excellent at solving problems and terrible at checking whether they're solving the right ones.

The zoom-out spell applies this insight by attacking a direction from five angles that established research shows are systematically overlooked: the problem frame itself (Schon, Dorst), what failure and success reveal when inverted (Munger, Klein), the cost of forgone alternatives (opportunity cost analysis), downstream consequences (Marks, Hardin), and whether the intervention is at the right level of the system (Heath, Meadows).

## In Practice

**Nickelodeon's sign-up reframing.** Nickelodeon ran hundreds of A/B tests on their sign-up flow, framing the problem as usability — button placement, form layout, copy variations. None produced meaningful improvement. When they reframed — shifting from "usability problem" to "emotional problem" — they discovered that children were afraid of the password creation prompt. It felt official and scary. The fix wasn't a better form; it was reassurance. The solution was invisible to the original frame because "usability" doesn't include "emotional fear." (Wedell-Wedellsborg, HBR 2017)

**Kodak's fatal frame.** Kodak framed their strategic question as "How do we sell more prints?" Every analysis within that frame produced reasonable answers — better paper, more retail partnerships, online ordering. The frame that would have saved the company was "What is the future of sharing memories?" — but that frame threatened the print business, so it never gained traction. The problem wasn't bad analysis; it was the wrong problem. (Commonly cited in strategic management literature)

**Klein's pre-mortem.** Gary Klein's pre-mortem technique — "The project has failed. What happened?" — increases identified failure reasons by approximately 30% compared to standard risk assessment (Mitchell, Russo, & Pennington 1989). The key is the framing shift: "What might go wrong?" triggers self-censoring (nobody wants to be the pessimist). "It has failed — what happened?" legitimizes pessimism and activates different cognitive processes. Klein found this works because prospective hindsight — imagining a future event has already occurred — generates more plausible explanations than simply imagining a future event.

**EPA Toxic Release Inventory.** The EPA required companies to publicly report toxic emissions. No penalties, no regulations — just public information. Emissions dropped 40% within a decade. On Donella Meadows' leverage hierarchy, this is a level #6 intervention (information flows) — far more powerful than the level #12 interventions (adjusting parameters like emission caps) that consumed most regulatory attention. Most policy operates at the lowest leverage points because they're easiest to implement and easiest to understand. The highest-leverage interventions are often about changing what's visible, not what's regulated. (Meadows 1997)

## The Command

The `/spell:zoom-out <plan or direction>` command applies these concepts through five strategic lenses:

1. **Problem Reframing** — Restates the problem three different ways using abstraction laddering and frame-shifting techniques. Each reframing must open a solution space the original frame excluded — cosmetic rewording doesn't count.
2. **Inversion** — Designs failure ("How would we guarantee this fails?") and traces success consequences ("If this succeeds perfectly, then what?"). For technical topics, applies seven specific inversion questions covering catastrophic failure, silent degradation, rollback impossibility, scale breaks, and more.
3. **Opportunity Cost** — Identifies realistic alternatives and applies the next-dollar test: "If we hadn't spent anything yet, would we start this today?" Separates sunk cost (irretrievable) from switching cost (real cost of changing direction).
4. **Second-Order Effects** — Traces "And then what?" at three time horizons (10 minutes, 10 months, 10 years). Maps ecosystem responses from users, teams, competitors. Checks for feedback loops.
5. **Upstream/Downstream** — Checks Heath's three barriers (problem blindness, lack of ownership, tunneling). Rates the intervention on Meadows' leverage hierarchy. Looks for dissolution — could the system be redesigned so the problem ceases to exist?

The output converges on a mandatory recommendation — stay course, adjust, pivot, or stop — with evidence from converging lenses and specific next actions. "It depends" is not a valid output; the spell forces a commitment with stated rationale.

## Background

The techniques in this spell come from several fields:

**Problem framing** was studied by Donald Schon in *The Reflective Practitioner* (1983), which identified problem setting as the core expert skill. Kees Dorst extended this into *Frame Innovation* (2011/2015), showing how problems and solutions co-evolve. Thomas Wedell-Wedellsborg brought it to management practice in his HBR article "Are You Solving the Right Problems?" (2017).

**Inversion** as a thinking tool traces to mathematician Carl Jacobi ("invert, always invert") and was popularized by Charlie Munger. Gary Klein's pre-mortem technique (1998, HBR 2007) applies prospective hindsight to project planning.

**Second-order thinking** was articulated by Howard Marks in *The Most Important Thing* (2011) as the distinction between first-level and second-level thinking. Garrett Hardin's *Filters Against Folly* (1985) introduced "ecolacy" — the discipline of asking "And then what?" — as a third literacy alongside words and numbers.

**Upstream thinking** was synthesized by Dan Heath in *Upstream* (2020), identifying why organizations react instead of prevent. Donella Meadows' "Leverage Points" (1997) provides the hierarchy of system intervention points that explains why most interventions have little effect.

**Problem dissolution** was conceptualized by Russell Ackoff, who distinguished four responses to problems — absolution, resolution, solution, and dissolution — and argued that dissolution (redesigning the system so the problem ceases to exist) is the highest-leverage response.

## Further Reading

- [Wedell-Wedellsborg, T. "Are You Solving the Right Problems?" (HBR, 2017)](https://hbr.org/2017/01/are-you-solving-the-right-problems) — The Nickelodeon case study and seven reframing practices, accessible and practical
- [Klein, G. "Performing a Project Premortem" (HBR, 2007)](https://hbr.org/2007/09/performing-a-project-premortem) — The original pre-mortem technique, concise and immediately applicable
- [Meadows, D. "Leverage Points: Places to Intervene in a System" (1997)](https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/) — The twelve-level hierarchy of system interventions, from parameters to paradigms
- [Marks, H. *The Most Important Thing* (2011)](https://www.harpercollins.com/products/the-most-important-thing-howard-marks) — Second-level thinking applied to investment but broadly useful for any strategic reasoning
- [Heath, D. *Upstream* (2020)](https://heathbrothers.com/upstream/) — Why organizations fail to prevent problems they could prevent, with practical frameworks
- [Schon, D. *The Reflective Practitioner* (1983)](https://mitpress.mit.edu/9780465068784/the-reflective-practitioner/) — The foundational work on problem setting versus problem solving in expert practice
- [Dorst, K. *Frame Innovation* (2015)](https://mitpress.mit.edu/9780262324311/frame-innovation/) — Systematic methodology for creating new problem frames
