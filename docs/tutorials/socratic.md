# The Socratic Technique

## Where This Came From

Around 400 BC, Socrates figured out something that most teachers still struggle with: people learn better when they discover answers themselves than when you just tell them. His method was simple — ask questions instead of giving lectures. Lead the student to the answer by asking the right questions in the right order.

This technique has been refined over two and a half millennia of education. Sam's contribution is approximately zero — he just noticed that AI assistants default to "here's the answer" mode, and that a simple mode switch to "ask me questions instead" makes the AI dramatically more useful for learning.

## The Core Idea

The Socratic method works through a cycle:

1. **Ask a question** that the student can reason about
2. **Listen to their reasoning** — don't just wait for the "right" answer
3. **Follow up** based on what they said — probe assumptions, explore implications
4. **Guide toward discovery** — the student should feel like they figured it out, not like they were told

The power isn't in the questions themselves — it's in the shift from passive consumption to active reasoning. When someone tells you the answer, you think "okay." When you figure it out yourself, you think "I understand why."

## Why It Works With AI

AI assistants are incredibly eager to help. Ask a question, get an answer. Ask how to fix a bug, get a code fix. Ask what a concept means, get a Wikipedia-level explanation. This is useful for getting things done, but terrible for learning.

The problem is that AI's default helpfulness creates a dependency loop:
1. You don't know how to do X
2. AI does X for you
3. Next time you need X, you still don't know how — so you ask AI again
4. Repeat forever

Socratic mode breaks this loop. Instead of giving answers, the AI asks questions that force you to reason through the problem. You still get help — but the help builds your understanding instead of replacing it.

## How Sam Uses It

When Sam is learning something new (a language feature, a design pattern, a debugging technique), he runs `/spell:socratic [topic]`. The spell:

1. Switches the AI from "answer mode" to "question mode"
2. If a topic is provided, starts with an opening question about that topic
3. Limits questions to 1-3 per response (not an interrogation)
4. Includes an escape hatch: say "just tell me" if you're stuck

The key design decisions:
- **It's a session modifier**, not a workflow — it changes behavior, doesn't produce files
- **It has an off switch** — real Socrates didn't, and that was occasionally fatal
- **It's not dogmatic** — for safety-critical issues or simple factual lookups, it breaks character

## Beyond This Spell

The Socratic principle is useful far beyond AI interactions:

- **In pair programming:** Instead of saying "you should use a map here," ask "what data structure would let you do this lookup in O(1)?"
- **In code review:** Instead of "this is wrong," ask "what happens when this input is null?"
- **In mentoring:** The best mentors are the ones who ask good questions, not the ones who have all the answers
- **In self-study:** When reading documentation, pause and ask yourself "why does this work this way?" before reading the explanation

## Further Reading

- *Plato's Meno* — The original demonstration of the Socratic method (Socrates teaches geometry to a slave boy through questions alone)
- [Socratic Questioning in Education](https://en.wikipedia.org/wiki/Socratic_questioning) — Modern pedagogical applications
- *Teaching with Your Mouth Shut* by Donald Finkel — Modern take on inquiry-based teaching
