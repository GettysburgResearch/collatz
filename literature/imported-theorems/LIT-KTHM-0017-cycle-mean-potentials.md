# LIT-KTHM-0017 — Positive cycle mean and phase potentials

**Verdict:** `FOLKLORE / STANDARD`; complete proof supplied.  
**Maps to:** `PR3/T-0013`.  
**Literature context:** finite difference constraints, Bellman–Ford duality, and Karp's cycle-mean theorem.

Let a finite directed graph have edge multipliers \(\lambda_e>0\).

## Theorem

The following are equivalent:

1. every directed cycle \(C\) satisfies \(\prod_{e\in C}\lambda_e>1\);
2. there exist weights \(w_i>0\) and \(\eta>1\) such that, for every edge \(e:i\to j\),

\[
\lambda_e\frac{w_j}{w_i}\ge\eta.
\tag{1}
\]

If edges also carry \(F_e(q)=\lambda_eq+b_e\), then some finite \(Q\) satisfies

\[
\boxed{w_jF_e(q)>w_iq}
\]

for every edge and every \(q\ge Q\). Every admissible infinite path remaining above \(Q\) is unbounded.

## Proof

Put \(\ell_e=\log\lambda_e\). Under condition 1 choose

\[
0<\varepsilon<\min_C |C|^{-1}\sum_{e\in C}\ell_e.
\]

The difference constraints

\[
p_i-p_j\le\ell_e-\varepsilon
\]

are feasible: summing their right sides around any cycle gives a positive number, so there is no negative-cycle obstruction. Set \(w_i=e^{p_i}\) and \(\eta=e^\varepsilon\); exponentiation gives (1). Conversely, multiplying (1) around a cycle telescopes the weights and gives product at least \(\eta^{|C|}>1\).

Let \(B=\max_e|w_jb_e|\). Then

\[
w_jF_e(q)\ge\eta w_iq-B.
\]

Choose \(Q\) with \((\eta-1)w_iQ>B\) for every vertex. Weighted states then increase, and after enlarging \(Q\) beyond the affine recursion's unstable fixed point they diverge. The finite set of weights is bounded above and below, so the unweighted quotients diverge too. ∎

## Boundary

This theorem does not construct a deterministic arithmetic selector, an invariant cylinder set, or an ordinary initial quotient. Those are the load-bearing native tasks.