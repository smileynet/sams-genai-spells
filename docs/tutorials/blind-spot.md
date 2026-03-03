# Blind Spot Detection & Pre-Mortem Analysis

## The Problem

A team plans a database migration from PostgreSQL to DynamoDB. They identify every risk they can think of: data mapping challenges, downtime windows, query rewrites, team training. They build a migration plan that addresses all of it. Six months later, the migration is complete — and then things start breaking. The billing system relied on PostgreSQL's transactional guarantees in ways nobody documented. The analytics team was running ad-hoc SQL queries that DynamoDB can't support. A regulatory requirement for point-in-time data recovery assumed relational backup semantics. None of these were on the risk register because nobody thought to look for them.

This is the defining characteristic of blind spots: the problem isn't that you assessed the risk and got it wrong. The problem is that the risk never entered the conversation at all. You can't mitigate what you don't know exists.

AI assistants make this worse in a specific way. Ask an AI to help you plan a migration, and it'll optimize within the frame you give it — better timelines, cleaner data mapping, more thorough test coverage. What it won't do, unprompted, is challenge the frame. It won't ask whether the migration is the right move. It won't surface the assumption that DynamoDB's eventual consistency model is acceptable for your billing system. It won't check whether similar migrations at other organizations have failed, or look for critiques of the approach from people who've tried it. The AI is extraordinarily helpful at executing the plan — and completely silent about whether the plan is missing something fundamental.

## How It Helps

A blind spot analysis does four things:

1. **Surfaces hidden assumptions** — makes the implicit explicit, then stress-tests the dangerous ones (load-bearing but unverified)
2. **Explores failure modes through prospective hindsight** — "the project has failed spectacularly — what happened?" — which increases failure identification by 30% compared to standard risk assessment
3. **Imports cross-domain knowledge** — finds where adjacent fields solved structurally similar problems, revealing patterns and warnings your field hasn't internalized
4. **Maps what's missing** — identifies conspicuous absences by comparing what's discussed against what similar efforts typically cover

The output isn't a risk register. It's a structured map of what the current analysis might be missing, organized by plausibility and impact, with specific next steps for each finding. It also states what it *couldn't* check — because a blind spot analysis that claims to be comprehensive is worse than no analysis at all.

## Why It Works

Joseph Luft and Harrington Ingham introduced the Johari Window in 1955 as a model of interpersonal awareness. It divides knowledge into four quadrants: known knowns (what you know you know), known unknowns (what you know you don't know), blind spots (what others see but you don't), and unknown unknowns (what nobody in the room knows to ask about).

Standard planning addresses the first two quadrants. You build on your known knowns and create action items for your known unknowns. But the dangerous quadrants are the third and fourth — the things you're not even looking for.

No single technique can probe all blind spots. That's why the spell uses five distinct approaches, each attacking from a different angle:

- **Assumption surfacing** probes for load-bearing beliefs nobody has tested
- **Pre-mortem analysis** probes for failure modes by reframing success as given failure
- **Cross-domain transfer** probes for patterns visible from outside your field
- **Negative space analysis** probes for topics conspicuously absent from the discussion
- **Contrarian search** probes for substantive critiques with genuine reasoning

The multi-technique approach is itself informed by Charlan Nemeth's research on dissent: authentic disagreement — multiple independent perspectives challenging a conclusion — stimulates genuine divergent thinking, while a single assigned devil's advocate role-playing opposition does not. Five techniques probing independently are more likely to find real blind spots than one technique probing deeply.

## In Practice

**Pre-mortem analysis.** Gary Klein developed the pre-mortem in the late 1990s as a practical tool for project planning. The key insight is a cognitive reframing: instead of asking "what might go wrong?" (which triggers self-censoring — nobody wants to be the pessimist), you say "the project has failed — what happened?" This shift from hypothetical to definitive activates different cognitive processes. Mitchell, Russo, and Pennington (1989) demonstrated that prospective hindsight — imagining a future event has already occurred — generates significantly more plausible explanations than simply imagining a future event. Klein's pre-mortem applies this finding to project management, and teams consistently identify 30% more risks with this framing than with standard risk assessment.

**Intelligence community red teaming.** After the intelligence failures surrounding 9/11, the CIA established the Red Cell — a unit whose sole purpose is to challenge the agency's institutional assumptions. The Red Cell doesn't just play devil's advocate; it produces full alternative analyses based on different assumptions. The distinction matters. Nemeth's research shows that assigned devil's advocates, who role-play opposition without believing it, are dramatically less effective than authentic dissenters who hold genuinely different views. The Red Cell model works because the analysts actually believe their alternative framings and argue with conviction.

**Black Swans and fat tails.** Nassim Nicholas Taleb's *The Black Swan* (2007) argues that the most consequential events are precisely the ones that standard risk models don't predict — not because they're impossible, but because they lie outside the model's assumptions. Taleb's prescription is not to predict better but to build robustness: reduce exposure to catastrophic downside regardless of its probability. A blind spot analysis aligns with this — you can't enumerate all unknown unknowns, but you can systematically probe for them and build contingencies for the structural vulnerabilities you find.

**Government foresight and horizon scanning.** Several governments maintain dedicated foresight units that practice horizon scanning — the UK Government Office for Science, Singapore's Centre for Strategic Futures, Finland's Committee for the Future. These units don't try to predict the future. They systematically scan for weak signals, emerging patterns, and cross-domain developments that might affect national policy. The key discipline is relevance filtering: interesting is not the same as actionable. Every finding must answer "specifically, how does this change what we should do?"

## The Command

The `/spell:blind-spot <topic>` command applies these concepts by:

1. Establishing a baseline — mapping the known knowns and known unknowns before probing for what's missing
2. Running five independent probing techniques (assumption surfacing, pre-mortem, cross-domain transfer, negative space, contrarian search), each with specific guardrails against its characteristic failure mode
3. Triaging findings on plausibility and impact, requiring corroboration from multiple sources, and capping output at 7-10 actionable items
4. Producing a structured report that includes an honest coverage assessment, explicit limitations, and specific next steps anchored to findings

The spell encodes hard-won lessons from the techniques it applies. Pre-mortem must use "has failed" language, not "might fail" — the framing is the technique. Cross-domain analogies must validate structural similarity, not just surface resemblance. Assumptions must be rated on importance *and* certainty, not listed flat. Contrarian findings must cluster from independent sources, not leap from a single blog post. And the output states what it couldn't check, because the most dangerous output would be one that creates false confidence by appearing comprehensive.

## Background

The techniques assembled in this spell come from several fields:

**Pre-mortem analysis** was developed by Gary Klein, a psychologist studying naturalistic decision-making. His 1998 book *Sources of Power* and subsequent Harvard Business Review article "Performing a Project Premortem" (2007) introduced the technique. The underlying cognitive finding — prospective hindsight — was demonstrated by Mitchell, Russo, and Pennington in 1989.

**Strategic Assumption Surfacing and Testing (SAST)** was created by Richard Mason and Ian Mitroff, published in *Challenging Strategic Planning Assumptions* (1981). Their importance/certainty matrix remains the standard tool for identifying which assumptions are dangerous.

**The Johari Window** was created by Joseph Luft and Harrington Ingham at UCLA in 1955. Originally a model for interpersonal awareness in group dynamics, it became widely adopted as a framework for understanding knowledge boundaries in many fields.

**Cross-domain analogical reasoning** was researched extensively by Dedre Gentner, whose structure-mapping theory (1983) explains why structural analogies transfer better than surface analogies — and why people consistently retrieve the wrong type.

**Cynefin** was developed by Dave Snowden, published in Harvard Business Review in 2007. It categorizes situations by causal structure (clear, complicated, complex, chaotic) and prescribes different response strategies for each.

**The power of authentic dissent** was researched by Charlan Nemeth, whose work from 2001 onward demonstrated that assigned devil's advocates are dramatically less effective than authentic dissenters at stimulating divergent thinking.

**Black Swan theory** was articulated by Nassim Nicholas Taleb in *The Black Swan* (2007), building on his earlier work in *Fooled by Randomness* (2001).

## Further Reading

- [Klein, G. "Performing a Project Premortem" (HBR, 2007)](https://hbr.org/2007/09/performing-a-project-premortem) — The original pre-mortem technique article, concise and practical
- [Nemeth, C. *In Defense of Troublemakers* (2018)](https://www.basicbooks.com/titles/charlan-nemeth/in-defense-of-troublemakers/9780465096299/) — Why authentic dissent works and devil's advocates don't, with research evidence
- [Snowden, D. & Boone, M. "A Leader's Framework for Decision Making" (HBR, 2007)](https://hbr.org/2007/11/a-leaders-framework-for-decision-making) — The Cynefin framework for categorizing problems by causal structure
- [Taleb, N. N. *The Black Swan* (2007)](https://www.penguinrandomhouse.com/books/176226/the-black-swan-second-edition-by-nassim-nicholas-taleb/) — Why the most consequential events are the ones standard models don't predict
- [UK Government Office for Science Futures Toolkit](https://www.gov.uk/government/collections/futures-toolkit-for-policy-makers-and-analysts) — Horizon scanning and foresight methods used by government policy teams
- [Gentner, D. "Structure-Mapping" (1983)](https://groups.psych.northwestern.edu/gentner/papers/Gentner83.pdf) — Why structural analogies transfer and surface analogies mislead
