# LIT-KTHM-0021 — Greatest safe kernel of a finite relation

**Verdict:** `FOLKLORE / STANDARD`; complete proof supplied.  
**Maps to:** `REG/L-9103` in PR #12.

Let \(Q\) be finite, \(R\subseteq Q\times Q\), and \(B\subseteq Q\) be forbidden. A set \(F\subseteq Q\) is safe when \(F\cap B=\varnothing\) and \(p\in F,\ pRq\) imply \(q\in F\).

## Theorem

The unique largest safe set is

\[
\boxed{F_{\max}=Q\setminus\operatorname{Pre}_R^*(B)},
\]

where \(\operatorname{Pre}_R^*(B)\) is the set of states from which a finite \(R\)-path reaches \(B\).

## Proof

Any safe set excludes \(B\). If a state has an edge to a state that every safe set must exclude, it too must be excluded; induction along paths shows every safe set is disjoint from \(\operatorname{Pre}_R^*(B)\).

Conversely, if \(p\notin\operatorname{Pre}_R^*(B)\) and \(pRq\), then \(q\notin\operatorname{Pre}_R^*(B)\), since otherwise \(p\) would reach \(B\). Thus the complement is forward closed and avoids \(B\). It contains every other safe set. ∎

## Boundary

A nonempty state kernel supports a sanctuary only when some canonical positive word reaches it. The theorem optimizes accepting states for a fixed transition skeleton; it does not synthesize that skeleton.