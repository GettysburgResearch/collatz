# An entropy bound for the actual ternary orbit law

Date: 2026-11-22. **Status: independently reviewed written deduction;
no full Collatz conclusion.** The scoped review is in
`reviews/ACTUAL_ORBIT_ENTROPY_REVIEW.md`. No predecessor-density, canonical
potential, GRH, or external Collatz theorem is an assumption of the result
below. The proof uses the exact positive-integer recurrence and elementary
finite-distribution entropy. It applies to every weak empirical limit of
one specified nonperiodic positive orbit, with its original sources and
physical gap sequence retained.

## 1. Statement

Write

\[
q_i=U^i(q_0),\qquad
g_i=v_2(3q_{i-1}+1),\qquad
2^{g_i}q_i=3q_{i-1}+1\quad(i\ge1),
\]

where `q_0` is a positive odd integer prime to three and the orbit is not
eventually periodic. An arbitrary nonperiodic positive orbit reaches this
domain after initial halvings and, if necessary, one odd step.
Put

\[
\ell=\log_2 3,\qquad
\Phi(a)=a\log a-(a-1)\log(a-1)\quad(a\ge1),
\qquad\Phi(1)=0.
\]

All unmarked logarithms and entropies use natural logarithms.
For `1 <= m <= N`, let `K` be uniform on `{m,...,N}` and let
`mu_(N,m)` be the law of `q_K mod 3^m`. Set `A_N=sum_(i=1)^N g_i`.

**Finite actual-source inequality.**

\[
\boxed{
H(\mu_{N,m})\le
m\Phi\!\left(\frac{A_N}{N-m+1}\right).
}
\tag{E1}
\]

The displayed argument of `Phi` is at least one, since `A_N >= N`.
This inequality uses no random model for the gaps: randomness consists only
of selecting a time from this finite segment of the one actual orbit.

Regard the positive integers as ternary-adic units, and let `mu` be any
weak subsequential limit of the actual empirical probabilities

\[
\mu_N=\frac1{N+1}\sum_{i=0}^N\delta_{q_i}
\quad\text{on }\mathbb Z_3^\times.
\]

Such limits exist because this space is compact. Let `H_m(mu)` be entropy
of its residue distribution modulo `3^m`. Then, simultaneously for every
positive integer `m`,

\[
\boxed{H_m(\mu)\le m\Phi(\ell).}
\tag{E2}
\]

In particular its upper entropy dimension satisfies

\[
\boxed{
\overline{\dim}_{\rm ent}\mu
:=\limsup_{m\to\infty}\frac{H_m(\mu)}{m\log3}
\le \frac{\Phi(\ell)}{\log3}
=H_2(\log_3 2)
=0.949955527188\ldots<1.
}
\tag{E3}
\]

The rightmost decimal is a numerical display of the exact expression, not
an input to the proof. `H_2` is binary entropy in bits.

This is an entropy-dimension assertion. It does **not** say that `mu` is
entirely singular, and it is not a statement about the canonical ternary
Syracuse law obtained from independent gaps. These are different laws.

## 2. The integer recurrence determines the residue from the actual past

For any `k >= m`, repeated substitution gives, as an exact rational
identity,

\[
q_k=
\frac{3^m q_{k-m}}{2^{g_{k-m+1}+\cdots+g_k}}
+\sum_{j=0}^{m-1}
 \frac{3^j}{2^{g_{k-j}+\cdots+g_k}}.
\tag{E4}
\]

All denominators are powers of two. They are units modulo `3^m`, while
the first term is zero modulo `3^m`. Thus `q_k mod 3^m` is a deterministic
function of the **actual last m gaps**, in reverse order if convenient.
No inverse word is freely selected and no ordinary source is replaced.

Let `W=(g_(K-m+1),...,g_K)`. Elementary data processing and entropy
subadditivity give

\[
H(q_K\bmod3^m)\le H(W)
\le\sum_{j=0}^{m-1}H(g_{K-j}).
\tag{E5}
\]

All these distributions have finite support for fixed `N`, even though
there is no uniform cap on the actual gaps.

## 3. Mean cost controls entropy without independence

For any positive-integer-valued finite distribution of mean `a >= 1`,

\[
H(G)\le\Phi(a).
\tag{E6}
\]

At `a=1`, positivity makes `G=1` surely. At `a>1`, compare its law `p`
with the geometric law

\[
r_a(j)=a^{-1}(1-a^{-1})^{j-1},\qquad j\ge1.
\]

Nonnegativity of relative entropy gives

\[
H(p)\le-\sum_jp(j)\log r_a(j)
=\log a-(a-1)\log(1-1/a)=\Phi(a).
\]

This elementary nonnegativity itself follows from `log t <= t-1`:
over the positive support of `p`,
`sum p log(r_a/p) <= sum r_a - sum p <= 0`.
No stationary law or independent geometric replacement of the actual
gaps is used.

The function `Phi` is continuous on `[1,infinity)`, increasing, and
concave. On `(1,infinity)`,

\[
\Phi'(a)=\log(a/(a-1))>0,\qquad
\Phi''(a)=-1/[a(a-1)]<0.
\]

Let `a_j=E g_(K-j)` for `0 <= j < m`. Each actual gap appears at most
`m` times in all the sliding blocks, so

\[
\frac1m\sum_{j=0}^{m-1}a_j
=\frac1{m(N-m+1)}
  \sum_{k=m}^N\sum_{j=0}^{m-1}g_{k-j}
\le\frac{A_N}{N-m+1}.
\tag{E7}
\]

Apply (E6) to each term of (E5), then concavity and monotonicity of
`Phi`. This proves (E1).

## 4. Real positivity supplies the required mean bound

A nonperiodic positive orbit has distinct states: any repetition would
make its future periodic. Consequently `q_N -> infinity` in the ordinary
real ordering. Taking logarithms of the exact recurrence gives

\[
A_N=N\ell+\log_2q_0-\log_2q_N
  +\sum_{i=1}^N\log_2\!\left(1+\frac1{3q_{i-1}}\right).
\tag{E8}
\]

The summands in the last sum tend to zero. Their Cesaro average therefore
tends to zero. Also `log_2 q_N >= 0`. It follows that

\[
\limsup_{N\to\infty}\frac{A_N}{N}\le\ell.
\tag{E9}
\]

This only needs escape of a nonperiodic sequence from bounded sets, not a
quantitative orbit sparsity bound or summability of reciprocal heights.

Fix `m` before taking any limit. Removing the first `m` samples from
`mu_N` changes total variation by at most `m/(N+1)`. Residue cells modulo
`3^m` are clopen, so weak convergence to `mu` gives convergence of the
finite residue probability vector. Entropy on that finite probability
simplex is continuous, including at zero coordinates. Equations (E1),
(E9), and continuity and monotonicity of `Phi` imply (E2).

The proof holds separately for every fixed positive integer `m` on the
same weak subsequence; no entropy limit for unbounded gaps, exchange of
two limits, or additional path-space compactification is needed.
Dividing by `m log3` and taking the upper limit proves (E3).

Finally, if `alpha=1/ell=log_3 2`, then direct algebra gives

\[
\frac{\Phi(\ell)}{\log3}
=-\alpha\log_2\alpha-(1-\alpha)\log_2(1-\alpha).
\]

Since `alpha != 1/2`, binary entropy is strictly less than one. This
establishes the strict gap without numerical approximation.

## 5. Collision energy forced by an actual escape

For a finite distribution `p`, Jensen's inequality under that distribution
gives

\[
\sum_rp(r)^2\ge e^{-H(p)}.
\]

With `theta=H_2(log_3 2)`, every empirical limit above therefore obeys

\[
\boxed{\sum_{r\in(\mathbb Z/3^m\mathbb Z)^\times}
               \mu(r+3^m\mathbb Z_3)^2\ge3^{-\theta m}.}
\tag{E10}
\]

The normalized unit Haar law gives each of the `2*3^(m-1)` cells the
same mass. Hence the squared `L2` norm of the level-`m` density relative
to that Haar law satisfies

\[
\boxed{
\|d\mu_m/dh_m\|_{L^2(h_m)}^2
\ge\frac23\,3^{(1-\theta)m}.}
\tag{E11}
\]

These are statements about the ternary distribution of time samples on
the same positive orbit. A bound proving entropy dimension greater than
`theta`, or a strictly smaller exponential collision rate, for at least
one such limit on every hypothesized escape would contradict them.
That lower entropy / upper collision estimate is **not proved here**.

## 6. A height-speed refinement

Suppose along the subsequence defining `mu` the real speed also converges:
`log(q_N)/N -> v`. The bound `q_N+1 <= (3/2)^N(q_0+1)` and real positivity
place `v` in `[0,log(3/2)]`. Equation (E8) then gives

\[
A_N/N\longrightarrow a_v=\frac{\log3-v}{\log2}\in[1,\ell].
\]

The same finite proof improves (E2)--(E3) to

\[
H_m(\mu)\le m\Phi(a_v),\qquad
\overline{\dim}_{\rm ent}\mu\le\Phi(a_v)/\log3.
\tag{E12}
\]

The base theorem does not assume existence of a speed. Along any empirical
weak subsequence, one may extract a further subsequence of the bounded
speed values if this refinement is useful; its empirical limit remains
the same. A smaller dimension bound at larger positive speed is a
restriction on a hypothetical escape, not an exclusion of it.

## 7. Relation to the literature and repository

The entropy ceiling for positive geometric inverse gaps is an existing
literature mechanism. The original-source coding inequality is explicit
in *Critical barriers and memory costs in Collatz inverse dynamics*,
Paper 150, version 2, Section 4, equations (18)--(19):
https://rstation.ai/problems/collatz/papers/150 . Its Corollary 4 in
Section 6.3 applies a critical stopping cover to the actual reversed past
of an escaping orbit and obtains a positive singular-mass requirement.
The note above combines the same coding principle with a finite sliding
block argument to give the explicit bound at **every** ternary precision
for **every** empirical limit. No claim of priority over all prior
entropy arguments is made.

Paper 127, *Stationary inverse laws, optimal window limits, and slow
terminating Collatz families*, Section 2, records a related legal-pair
entropy identity. Its stronger full-entropy classification uses an
actual positive capped inverse policy:
https://rstation.ai/problems/collatz/papers/127 . The deterministic
reversed past of an escape has not been shown to be such a policy.

PR180 at `a9f471543d7fed0a76f348e6d97a9d6d44fa369e`,
`research/central-step-20261122/CRITICAL_BOUNDARY.md`, identifies the
remaining sibling-current condition (OPEN-S) for persistent linear
canonical spikes. The arithmetic smoothing test in the companion
`SIBLING_SMOOTHING_ATTEMPT.md` explains why averaging the exact sibling
orbit does not establish the needed actual-orbit entropy lower bound.

The finite source-entropy inequality, its optimized bound for reference
mean `a>1`, the sliding-window sum inequality, and the exact finite
logarithmic telescope are formalized in
`lean/OriginalSourceEntropy.lean`. That module defines finite Shannon
entropy and proves its required comparison and projection inequalities;
it does not assume the entropy bound as an opaque hypothesis. The
observed-window construction and complete composition giving E1 remain
written, as do the weak-limit, entropy-dimension, collision, and
height-speed conclusions. No full proof of Collatz is claimed.
