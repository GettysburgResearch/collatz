# A pointwise clock criterion for eventual repetition

Fix a positive odd unit $a$. Write $a_i$ for its $i$th odd iterate. At a chosen starting value $u$, let $s_k(u)$ denote the number of shortcut steps in its first $k$ odd gaps. Call $k$ a crossing when

\[
                      (2^{s_k(u)})^6>(k+1)(3^k)^6 .
\]

The following statements are equivalent for this one starting value. [Lean module](ClockRecurrence.lean)

1. The odd orbit of $a$ eventually repeats.
2. Every tail starting at $a_i$ has a crossing.
3. The original gate $a$ has crossings at arbitrarily large depths.
4. The original gate $a$ has more than $\lfloor a/2\rfloor$ distinct crossing depths.

For the finite formulation, `certificate a ks` checks that the list contains enough distinct depths and that each satisfies the strict integer inequality. The theorem `repeats_iff_certificate` proves equivalence to the existence of such a list. No prior knowledge of the period or repeated state is needed to check it.

If the path reaches a periodic state after $i$ gaps, a lap of $p>0$ odd gaps and shortcut clock $A$ has $2^A>3^p$. Repeating that lap yields an exponential gain. An integer Bernoulli estimate shows that this gain dominates both the fixed cost of the preperiod and the polynomial factor in the test at arbitrarily late depths. This applies to the cycle through one and to any hypothetical nontrivial cycle.

Conversely, each crossing at an odd unit greater than two gives either a strictly smaller odd iterate or a repeated component on the same ordinary orbit. Crossing on every tail therefore implies repetition by strong induction. On an orbit with no repetition, crossings measured from $a$ must all end at different odd values smaller than $a$. There are only $\lfloor a/2\rfloor$ such values. [Finite path estimate and cycle detection](CycleDetection.lean)

In particular an orbit without repetition has a tail on which the clock inequality fails at every depth. The outstanding pointwise statement is that every positive odd unit has a crossing. Combining that assertion with exclusion of the finite witnesses for nontrivial cycles would prove universal convergence. [Universal proposal](ClosureProposal.lean)
