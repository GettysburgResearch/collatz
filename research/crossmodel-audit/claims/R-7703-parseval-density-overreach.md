# R-7703 — Parseval does not force typical square-root size

**Claim ID:** `R-7703`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-crossmodel-audit-01`  
**Created:** 2026-07-27  
**Target:** Fable foundations `L-9918.8` at `2cb80b4629ebfde5c8aaa3433c38e1382ea956b7`  
**Verdict:** exact identities `PASSED`; density interpretation `REFUTED / SCOPE NARROWING REQUIRED`

## Surviving exact result

For a `d`-element set `D` in a finite cyclic group, its Fourier sum satisfies

\[
\frac1{|G|}\sum_{v\in G}|g(v)|^2=d.
\]

Likewise, the product of the global per-level mean squares equals the global architecture mean square. Therefore a naive multiplication of **global second moments** contains no slack.

## Invalid inference

The proof then says that mean square `R` forces a Fourier coefficient to have “typical size `sqrt(R)`” and that a bound `O(1)` can hold only on a set of frequencies of density `O(1/R)`.

Neither follows from a second moment and an upper bound alone.

## Exact counterexample

Take `D` to be the complete group `Z/qZ`, so `d=q`. Then

\[
g(0)=q,
\qquad
g(v)=0\quad(v\ne0),
\]

and hence

\[
\frac1q\sum_v|g(v)|^2=q=d.
\]

Nevertheless

\[
|g(v)|\le1
\]

on density

\[
1-1/q,
\]

which tends to one, while the large value is concentrated on density `1/q`.

The lower-tail estimate proved in the source is consistent with this example: it only forces a large-value set of order at least `1/d`, not a small-value set of order at most `1/d`.

## Correct conclusion

Parseval proves:

1. no uniform bound below `sqrt(d)` can hold at **every** frequency;
2. global per-level second moments cannot by themselves yield decay after multiplication;
3. density-one smallness, low-frequency first-moment estimates, multiscale cancellation, and inter-level correlations remain completely possible.

In particular, this Parseval identity does not obstruct the repaired low-frequency block mean `L-7701`.
