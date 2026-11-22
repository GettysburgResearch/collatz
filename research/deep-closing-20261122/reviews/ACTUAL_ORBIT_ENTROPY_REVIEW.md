# Independent review: finite actual-orbit entropy

Date: 2026-11-22. Authoring agent: `deep_escape`; reviewing agent:
`deep_cycles`. Reviewed file:
`collatz_work/deep_escape/ACTUAL_ORBIT_ENTROPY.md`.
SHA256: `958344f44fdd06acb771e8abd8af3b70f6c47c7069f035f8eb13f0209ca28d98`.

**Verdict: VERIFIED as written at the pinned source bytes, for E1--E12.**
This is an independent written derivation, not a Lean compilation or
independent audit of the external manuscripts discussed in Section 7.
It does not establish the missing entropy lower bound or Collatz.

The earlier reviewed edition had SHA256
`1568032bdc162c9c550a26d61a45e358f6025f2ae4bd0ed3894635e9e8718840`.
The final edition updates the review-status header and the formalization
paragraph. Those editorial changes have been inspected and the review is
rebound to the final bytes above. The mathematical claims E1--E12 and the
derivations reviewed below are unchanged. In particular, the final paragraph
correctly leaves the observed-window construction, complete E1 composition,
and asymptotic conclusions as written proofs; this review does not promote
them to Lean-checked statements or independently audit the Lean module.

## Reconstruction of the finite estimate

Let L=N-m+1 and a=A_N/L. Choose K uniformly from m,...,N and put
W=(g_(K-m+1),...,g_K). Iterating
q_i=(3q_(i-1)+1)/2^(g_i) gives exactly

\[
q_K=3^m2^{-\sum_{i=K-m+1}^K g_i}q_{K-m}
 +\sum_{j=0}^{m-1}3^j2^{-\sum_{i=K-j}^K g_i}.
\]

At precision 3^m the first term vanishes and all powers of two are
invertible. Thus the terminal residue is a function of the actual
window. The cases K=m and K=N use respectively the first and last
available gaps and require no external gap.

Here is a second proof of the entropy bound that does not repeat the
author's marginal-subadditivity/Jensen route. For a>1, compare the
**joint** finite-support law of W with the product law r_a^m, where
r_a(j)=a^(-1)(1-1/a)^(j-1). Nonnegative relative entropy gives

\[
H(W)\le m\log a-
 \left(\mathbb E\sum_{j=0}^{m-1}g_{K-j}-m\right)
 \log(1-1/a).
\]

Every one of g_1,...,g_N occurs in at most m of the selected windows.
Consequently the expected sum is at most m A_N/L=ma. Since
-log(1-1/a)>0, the preceding upper bound is at most
m[a log a-(a-1)log(a-1)]. Data processing proves E1. The reference
product distribution is used only in the entropy inequality; no
independence is imposed on the actual window.

At a=1, A_N>=N and L<=N force m=1 and A_N=N. Every positive gap is
then one, so both the window and residue are deterministic. This also
checks the endpoint Phi(1)=0 without a logarithm of zero.

## Reconstruction of the limiting passage

The absence of repeated states implies that, for any fixed B, the
orbit visits {1,...,B} only finitely many times. Hence q_i tends to
infinity in the real ordering. Taking logarithms of each exact odd
transition and telescoping yields

\[
A_N=N\log_2 3+\log_2 q_0-\log_2 q_N+
 \sum_{i=1}^N\log_2(1+1/(3q_{i-1})).
\]

The final sum is o(N) by Cesaro, while -log_2 q_N<=0. Thus
limsup A_N/N<=log_2 3. This argument does not require the sum of
reciprocal states to converge and does not impose a speed.

For each fixed m, deleting indices 0,...,m-1 from the N+1 samples
costs total variation at most m/(N+1). Clopen ternary residue cells
therefore have converging probabilities on the chosen weak subsequence.
Finite-alphabet entropy is continuous, including on the boundary of
the simplex. Apply E1 before passing to the limit, and use monotonicity
and continuity of Phi. This proves E2 for every m on that same
subsequence. The order is fixed m, then N to infinity, then m to
infinity; there is no unjustified moving-precision passage.

The identity Phi(log_2 3)/log 3=H_2(log_3 2) follows by putting
alpha=1/log_2 3 and expanding both sides. Its strict inequality from
one follows from strict maximality of binary entropy at alpha=1/2;
that equality would imply 3=4. No decimal approximation is needed.

## Collision and speed checks

Jensen for log under the residue law gives
sum p log p <= log(sum p^2), so collision mass is at least exp(-H).
There are 2*3^(m-1) unit cells. Their normalized Haar law h_m has
that reciprocal mass per cell, and

\[
\|d\mu_m/dh_m\|_{L^2(h_m)}^2
=2\,3^{m-1}\sum_r p(r)^2.
\]

This gives E10 and the exact factor 2/3 in E11.

If log q_N/N tends to v along the empirical subsequence, the same
telescope gives A_N/N -> (log3-v)/log2. Since U(q)+1 <=
(3/2)(q+1), the speed is at most log(3/2); real positivity makes it
nonnegative. The effective mean lies in [1,log_2 3], so the same
finite argument proves E12, including its endpoint. Extracting a
further speed-convergent subsequence preserves the empirical limit.

## Scope retained

These results constrain the actual ternary time-sampling law of one
hypothetical nonperiodic positive integer orbit. They neither identify
it with an independent-gap inverse policy nor show it is Haar. Entropy
dimension below one does not by itself mean the whole measure is
singular; a mixture can retain positive absolutely continuous mass.
The manuscript makes those distinctions correctly. No external
canonical potential or population assertion is needed for E1--E12.
