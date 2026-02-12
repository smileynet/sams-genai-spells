# The Socratic Method

## The Problem

You're trying to learn React hooks. You ask an AI "how does useEffect work?" and get a perfect, comprehensive explanation. You read it, nod, and move on. Two days later you need useEffect again and realize you have no idea how it works — you just remember that the AI told you. This is the read-nod-forget loop: passively consuming answers feels like learning, but nothing sticks.

AI assistants make this worse. They're so good at answering that they create a dependency loop:

1. You don't know how to do X
2. AI does X for you
3. Next time you need X, you still don't know how
4. Repeat forever

Every answer the AI gives is another rep of you *not* learning. You get faster at asking, not at understanding. The AI becomes a crutch that feels like a tool.

The same pattern shows up in mentoring and code review. A senior developer reviews a junior's pull request and writes "add a null check here." The junior adds the null check. Next time, same bug — because they never understood *why* the null check was needed, just that someone told them to add one. Giving answers creates dependence. The person you're "helping" never develops the mental model to solve the problem themselves.

## How It Helps

The Socratic method is teaching through guided questions instead of direct answers. The power isn't in the questions themselves — it's in the shift from passive consumption to active reasoning. When someone tells you the answer, you think "okay." When you figure it out yourself, you think "I understand why."

The cycle works like this:

1. **Ask a question** the learner can reason about
2. **Listen to their reasoning** — don't just wait for the "right" answer
3. **Follow up** based on what they said — probe assumptions, explore implications
4. **Guide toward discovery** — the learner should feel like they figured it out

## Why It Works

Active recall beats passive consumption every time. When you read an explanation, your brain files it under "something I saw." When you're forced to reason through a question, your brain has to retrieve what it knows, find the gaps, and build connections to fill them. That's encoding — the process that turns information into understanding.

Questioning also forces learners to organize their own mental model. When the AI asks "what do you think happens when a component re-renders — does the effect run again?" you can't just nod. You have to take your vague sense of how React works and make it specific enough to answer. The gaps in your understanding become obvious *to you*, not just to the person asking.

This is why the method works in any context — human or AI. The help builds understanding instead of replacing it. A well-placed question always teaches more than a well-written answer.

## In Practice

**Law school and the case method.** In 1870, Christopher Langdell introduced a teaching method at Harvard Law that still dominates legal education today. Instead of lecturing students on legal principles, professors present a court case and interrogate: "What was the court's reasoning? Do you agree with the outcome? What if the plaintiff had known about the defect — would the analysis change?" Students can't hide behind notes. They have to reason through the law in real time, with a professor probing every assumption. The method is uncomfortable — first-year law students universally dread being called on — but it produces lawyers who can *think* about law, not just recite it.

**Pair programming.** The best pair programming sessions don't involve one person dictating code while the other types. They sound like this: "What data structure would let you do this lookup in O(1)?" followed by "And what's the tradeoff with memory?" The navigator asks questions; the driver reasons through them. When it works, both people leave the session understanding the code deeply — not just the person who happened to be typing. The worst pair programming sessions are the ones where the senior developer just says "use a hash map" and moves on.

## The Command

The `/spell:socratic [topic]` command applies this concept by:

1. Switching the AI from "answer mode" to "question mode"
2. If a topic is provided, starting with an opening question about that topic
3. Limiting questions to 1-3 per response (not an interrogation)
4. Including an escape hatch: say "just tell me" if you're stuck

It's a session modifier — it changes behavior for the session, doesn't produce files. And unlike the real Socrates, it has an off switch.

## Background

Around 400 BC, Socrates figured out something most teachers still struggle with: people learn better when they discover answers themselves. His method was simple — ask questions instead of giving lectures. We know this primarily through Plato's dialogues, especially the *Meno*, where Socrates teaches geometry to an uneducated slave boy through questions alone, demonstrating that the knowledge was "already there" waiting to be drawn out.

The method has been refined over two and a half millennia of education — from medieval dialectic to modern inquiry-based learning. Good coaches and therapists use the same principle: "What do you think is holding you back?" is more powerful than "Here's your problem." The question forces the person to do the thinking, which is the whole point.

## Further Reading

- *Plato's Meno* — The original demonstration (Socrates teaches geometry through questions alone)
- [Socratic Questioning in Education](https://en.wikipedia.org/wiki/Socratic_questioning) — Modern pedagogical applications
- *Teaching with Your Mouth Shut* by Donald Finkel — Modern take on inquiry-based teaching
