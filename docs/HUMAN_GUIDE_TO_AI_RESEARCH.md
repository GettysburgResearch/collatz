# Human Guide to Steering AI Mathematical Research

AI research agents can be unusually productive, especially when they can read a
large repository, write code, compare branches, and preserve their work.

They also have characteristic failure modes. Human steering should preserve
creative range while interrupting unproductive loops.

## What models are often good at

- generating many candidate viewpoints;
- exact symbolic manipulation;
- translating among formalisms;
- building computational checkers;
- finding small counterexamples;
- mapping dependencies;
- synthesizing literature;
- producing detailed proof drafts;
- revisiting a program from an adversarial role;
- leaving a durable written record.

## What models often do badly

- distinguishing a new reduction from an equivalent restatement;
- noticing that the same global gap survives a new notation;
- respecting the difference between finite consistency and infinite existence;
- remembering that a `2`-adic object may not be an ordinary integer;
- keeping source-qualified theorems separate from native results;
- calibrating “breakthrough” language;
- stopping a familiar proof pattern after it has become circular;
- preserving the exact target over many sessions.

## Do not over-steer too early

A broad new idea often needs room.

Allow an agent to:

- build definitions;
- try examples;
- test analogies;
- search remote literature;
- run exploratory code;
- discover why a route fails.

Intervene when the work repeatedly returns to the same unresolved implication
without acknowledging it.

## Signs of a circular loop

- each pass creates a new encoding of the same compatible-prefix tree;
- increasingly long finite witnesses are presented without one ordinary
  infinite witness;
- the agent proves more consequences conditioned on existence;
- the agent alternates between two equivalent formulations;
- the same theorem is rediscovered under a new claim ID;
- a negative result applies only to a guessed family but is narrated as global;
- a literature search finds the target open and the agent stops;
- the agent repeatedly says “we are close” without a measurable new
  implication;
- a computation grows while the logical gap stays fixed.

## Gentle loop-breaker prompt

```text
Pause the current development and perform a blocker audit.

State:
1. the exact final target;
2. the first unsupported inference;
3. what changed mathematically in the last three passes;
4. whether the current target is weaker than Collatz, equivalent to it, or
   stronger;
5. what exhaustive class a negative result would eliminate;
6. what explicit candidate a positive result would produce.

Do not introduce a new formalism in this pass unless it directly changes one of
those implications. Try to refute the current route before continuing it.
```

## Strong loop-breaker prompt

```text
Stop extending finite-prefix, conditional-growth, or encoding machinery.

Choose one global blocker:
- ordinary-integer extraction;
- all-time legality of one explicit seed;
- full-denominator divisibility;
- exact physical replay;
- an exhaustive architecture-level exclusion.

Either supply the missing inference or prove that the current architecture
cannot supply it. Preserve all valid partial results, but do not call another
equivalent reformulation progress toward the final objective.
```

## Open-problem continuation prompt

Use this when a model becomes over-conservative:

```text
The fact that the target is a known open problem is context, not a stop signal.
Record the exact literature boundary and continue the attempt.

Do not claim the result is known.
Do not refuse merely because it would be significant.
Try a new proof, disproof, reduction, computation, or formalization, and state
your uncertainty honestly.
```

## Novelty-delta prompt

```text
Compare the proposed result with the closest repository and literature results.

Produce a table:
- prior statement;
- new statement;
- logical difference;
- new hypothesis;
- new conclusion;
- new proof mechanism;
- remaining blocker.

If the new statement is equivalent to an existing open question, say so and
explain what new attack remains.
```

## Adversarial-role switch

```text
For this pass, act as a hostile verifier.

Assume the previous author is intelligent but may have hidden:
- a quantifier swap;
- a finite-to-infinite leap;
- a 2-adic/ordinary confusion;
- a denominator gap;
- a source-normalization error;
- a circular dependency.

Find the first invalid inference or independently reconstruct the chain.
```

## When to redirect rather than stop

Redirect when:

- the route produced reusable lemmas;
- a broad class can be eliminated;
- a computation can become a certificate;
- the literature connection suggests a remote method;
- the failed proof exposes an exact global blocker;
- a formalization would clarify the statement.

## When to archive a route

Archive as inactive when:

- no new implication has appeared across several documented passes;
- the same blocker is acknowledged and no new mechanism addresses it;
- the program has been subsumed by a stronger one;
- the key premise has been refuted;
- the required source theorem does not say what the program assumed.

Archiving is not deletion and not a declaration that the direction can never
work.

## Encourage organizational insight

Models should be asked occasionally:

```text
What repository or coordination change would have made this work easier to
verify, continue, compare, or refute?
```

Some of the most valuable outputs may be:

- a dependency map;
- a claim schema;
- a better task split;
- a compact checker;
- a clearer current-state document;
- a warning about a recurring model failure.
