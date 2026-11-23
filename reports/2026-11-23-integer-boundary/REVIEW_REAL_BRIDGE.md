# Semantic review of the real inverse-path bridge

Reviewer: collaborating agent `full_denominator`.
Date: 2026-11-23.

Reviewed source snapshot: `InverseRealSeparation.lean`.
Snapshot SHA256: `7a6d060f2dd8920f5c97642309a1273aa6ca53d94140c5296ad40491b7120b50`.
This is a semantic review of the final declarations and their mathematical argument. The coordinating agent reported successful strict compilation and will perform the final repository compilation and axiom audit; this reviewer did not rerun the compiler. The review covers the final three dyadic/ordinary specializations as well as the seven earlier statements. A later changed file requires an explicit new source binding.

## Scope and result

The three definitions and ten stated theorems have the intended mathematical scope. The generalized real edge is

`c(i) q(i) = 3 q(i+1) + 1`,

with every `c(i)>0` and `q(i)>0`. The reciprocal-sum bound is a visible theorem premise. No count of ordinary vertices, 3-adic integrality, code irrationality, or cycle classification is asserted by this Lean file.

With `M(n)=product_(i<n) 3/c(i)` and
`S(n)=sum_(i<n) M(i)/c(i)`, expanding one edge gives
`M(i) q(i) = M(i+1) q(i+1) + M(i)/c(i)`.
Summing yields the exact affine telescope `S(n)+M(n)q(n)=q(0)`.

The correction product is
`C(n)=product_(i<n) [1+1/(3q(i+1))]`.
Multiplying the same edges yields `M(n)q(n) C(n)=q(0)`.
The exponential estimate `C(n)<=exp(B)` from
`sum_(i<n)1/(3q(i+1))<=B` consequently gives
`M(n)q(n)>=q(0)exp(-B)`.
Combining the two telescopes proves
`S(n)<=q(0)(1-exp(-B))`.
All inequality directions and positivity hypotheses in the file are correct.

The monotone-limit theorem uses nonnegative summands, the proved common upper bound, and completeness of the real numbers. Its strict final inequality follows from `q(0)>0` and `exp(-B)>0`. There is no need to separately assume `B>=0`: the sum bound at `n=0` implies it whenever the family of hypotheses is instantiated. Nothing in the proof assumes the desired limit vanishes.

## Application to the literal numen series

For the written note's gaps `e_1,e_2,...`, use

`q_Lean(i) = q_written(i)` and `c(i) = 2^(e_(i+1))`.

If `A_k=e_1+...+e_k`, then
`M(k)=3^k/2^A_k` and
`M(i)/c(i)=3^i/2^A_(i+1)`.
Therefore `partialSum c n` is exactly the first `n` terms of the displayed numen series, with the written one-indexed summation reindexed by `i+1`. There is no reversed-clock mismatch.

The written simple-inverse-path count gives
`sum_(i>=0)1/q_i<=200`.
Every finite sum beginning at `q_1` is therefore at most 200, so the exact Lean budget premise holds with `B=200/3`. The conclusion becomes

`L <= q_0 (1-exp(-200/3)) < q_0`,

as claimed. The final file now formalizes the coefficient identification in `multiplier_pow_two` and `partialSum_pow_two`, and the natural-state specialization in `ordinary_inverse_numen_separated`. The latter explicitly converts the reciprocal budget 200 into the correction budget 200/3 and concludes the literal real-series gap.

## Review of the three final additions

- `multiplier_pow_two` identifies the product of `3/2^(e i)` with `3^n/2^(sum_(i<n)e i)`. The finite-product distributivity and power-sum identity are exactly the needed algebra; no extra dynamical premise appears.
- `partialSum_pow_two` identifies every generic summand with `3^i/2^(sum_(j<i+1)e j)`. The successor range and `div_div` implement the intended cumulative exponent, so the literal series has the correct indexing.
- `ordinary_inverse_numen_separated` takes positive natural states, natural exponents, the exact natural-number affine edges, and the explicit finite reciprocal budget. It casts the edges into the reals, divides the budget by three, invokes the reviewed real theorem, and rewrites its partial sums into the literal series. Its tail lower bound is exactly `q(0) exp(-200/3)`.

The final natural-state theorem does **not** itself assert oddness of the states, positivity of each exponent, or that these edges are exact steps of the odd Collatz map. Those extra arithmetic properties are unnecessary for the general real separation result and are supplied by the written numen-to-ordinary-tail argument when it is applied. There is no hidden substitution of a weaker edge for an actual edge in that application.

## Limits

This Lean bridge does not classify cycles. On an inverse path that loops forever around a positive cycle, the reciprocal sums are unbounded, so the finite-budget premise fails. No contradiction with the known cycle is produced. The infinite integer-cylinder estimate and the proof that a 3-adic integer value supplies actual ordinary inverse tails remain written arguments unless separately formalized.

Verdict: the generic real theorem and its application to the written numen argument are mathematically correct at the reviewed statement level. No proof of nontrivial-cycle exclusion or of full Collatz is supplied by these declarations.
