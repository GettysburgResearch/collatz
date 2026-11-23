# A logarithmic gain in the exact same-source collision obstruction

Date: 2026-11-23. Baseline: PR185,
`39ba48e6a8af781193e28c679ea8ab64663c3aa6`.

**Status: new written finite deductions and a Lean-checked finite arithmetic
core. This does not exclude an escaping orbit.** The result strengthens the
collision lower bound for the exact ordinary inverse endpoint laws already
used in `research/rigidity-closing-20261122/SAME_SOURCE_INVERSE_ENTROPY.md`.
It supplies a factor of the square root of the ternary precision, uniformly
in every inverse clock. Consequently a matching upper bound at the critical
exponent, rather than at a strictly larger exponent, would suffice for a
contradiction. Such an upper bound is not proved here.

The argument first concerns one actual positive ordinary source and its
finite gap words. The ordinary harmonic flow enters only in the last
comparison with the inverse endpoint law. Its original source-qualified
analytic dependencies are retained. No independent or resampled source is
introduced.

## 1. Exact composition budgets

Let `m >= 1`. For a positive integer word
`w=(g_1,...,g_m)`, write

\[
 S(w)=g_1+\cdots+g_m.
\]

There are exactly `binom(s-1,m-1)` such words with total `s`. For integers
`K >= 0`, put

\[
 Q_1(K,m)=\sum_{s=m}^{K-1}(K-s){s-1\choose m-1},
 \qquad
 Q_2(K,m)=\sum_{s=m}^{K-1}(K-s)^2{s-1\choose m-1}.
\]

The empty sums have value zero. Two finite hockey-stick identities give

\[
 \boxed{Q_1(K,m)={K\choose m+1}},
 \qquad
 \boxed{Q_2(K,m)={K\choose m+1}+2{K\choose m+2}}.
 \tag{1}
\]

For example, the first identity follows by writing `K-s` as the number
of integers `t` with `s <= t < K` and summing twice. For the second,
increase `K` by one. Every old deficit `d` changes its square by `2d+1`,
and the new terminal term has zero deficit. The first identity and the
ordinary hockey-stick sum then give (1) by Pascal's identity.

### Proposition 1: distinct words with bounded mean cost

Let `W` be a finite set of **distinct** positive words of length `m`, with
`L=|W| > 0`, and suppose

\[
 \frac1L\sum_{w\in W}S(w)\le B.
\]

For every integer `K > B`,

\[
 \boxed{(K-B)L\le {K\choose m+1}}.
 \tag{2}
\]

Indeed,

\[
 (K-B)L\le\sum_{w\in W}(K-S(w))
 \le\sum_{w\in W}(K-S(w))_+
 \le Q_1(K,m).
\]

Distinctness is needed in the last inequality. In particular,
`K=ceil(B)+1` gives `L <= binom(K,m+1)`.

### Proposition 2: a collision budget for an arbitrary finite word law

Let `p_w` be a probability law on a finite set of positive words of length
`m`. Repeated occurrences of one word are combined into its single mass
`p_w`. If

\[
 \sum_w p_w S(w)\le B,
\]

then, for every integer `K > B`,

\[
 \boxed{\sum_w p_w^2\ge
   \frac{(K-B)^2}{\binom K{m+1}+2\binom K{m+2}}.}
 \tag{3}
\]

**Proof.** Put `d_w=(K-S(w))_+`. The mean-cost assumption gives

\[
 K-B\le\sum_w p_w d_w.
\]

Cauchy's inequality gives

\[
 (K-B)^2\le
 \left(\sum_w p_w^2\right)\left(\sum_w d_w^2\right)
 \le Q_2(K,m)\sum_w p_w^2.
\]

The last sum of squared deficits is an **unweighted count over distinct
support words**. It is bounded by (1); it is not an expectation under
another law. Since `B >= m` for any such probability law and `K > B`,
the denominator is positive. This proves (3). ∎

Unlike (2), (3) does not require distinct ordinary endpoints or a height
cutoff. Its masses may be very uneven.

## 2. Apply the budget to one actual positive orbit

Use the accelerated odd map

\[
 U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

Fix one positive odd ordinary source `q_0`. Write

\[
 q_j=U^j(q_0),\quad 2^{g_j}q_j=3q_{j-1}+1,
 \qquad A_M=\sum_{j=1}^M g_j.
 \tag{4}
\]

For `1 <= m <= M`, let `L=M-m+1`. Choose `J` uniformly from
`{m,...,M}`, and take its actual length-`m` past word

\[
 W_J=(g_{J-m+1},\ldots,g_J).
\]

Every gap is counted in at most `m` of these windows. Hence

\[
 \mathbb E S(W_J)\le B_{M,m}:=\frac{m A_M}{M-m+1}.
 \tag{5}
\]

The exact affine relation for a word `w=(g_1,...,g_m)`, with
`a_i=g_1+...+g_i` and `a_0=0`, is

\[
 2^{S(w)}q_J
 =3^m q_{J-m}+\sum_{i=0}^{m-1}3^{m-1-i}2^{a_i}.
 \tag{6}
\]

Thus `w` determines `q_J mod 3^m`: powers of two are invertible modulo
`3^m`. No ordinary source is replaced by a freely chosen residue.

Write

\[
 \widehat\pi_{M,m}=\frac1L\sum_{j=m}^M\delta_{q_j},
 \qquad
 \operatorname{Col}_m(\mu)
   =\sum_{a\bmod3^m}\mu(a+3^m\mathbb Z)^2.
\]

Projecting a word law to an endpoint residue groups its masses, which can
only increase its collision sum. Proposition 2 gives the exact finite
bound

\[
 \boxed{
 \operatorname{Col}_m(\widehat\pi_{M,m})\ge
   \frac{(K-B_{M,m})^2}{Q_2(K,m)}
 }
 \quad(K\in\mathbb Z,\ K>B_{M,m}).
 \tag{7}
\]

For the original uniform window

\[
 \pi_M=\frac1{M+1}\sum_{j=0}^M\delta_{q_j},
\]

the measure domination
`pi_M >= (L/(M+1)) * hat_pi_(M,m)` gives

\[
 \boxed{
 \operatorname{Col}_m(\pi_M)\ge
 \left(\frac{M-m+1}{M+1}\right)^2
 \frac{(K-B_{M,m})^2}{Q_2(K,m)}.
 }
 \tag{8}
\]

The endpoint window in (7) and the original window in (8) are different;
the displayed factor accounts for every omitted early endpoint.

## 3. Exact transfer to every moving inverse clock

Assume now that this source is a ternary unit, has a non-eventually-periodic orbit, and that
the source-qualified ordinary harmonic flow of the pinned PR185 note is
available. A positive odd source divisible by three can first be shifted
by one actual odd step; the following law then uses that fixed shifted
source throughout:

\[
 0<\nu(q)\le A,\qquad
 \nu(q)=\sum_{Ux=q}\nu(x).
\]

Put `v_j=nu(q_j)`, so `v_j` increases to `C > 0`, and use exactly the
kernel and root law from that note:

\[
 K_\nu(q,x)=\frac{\nu(x)}{\nu(q)}\mathbf1_{\{Ux=q\}},
 \qquad
 \zeta_{M,r}=(K_\nu^r)_*
       \left(\frac1{M+1}\sum_{j=0}^M\delta_{q_{r+j}}\right).
 \tag{9}
\]

Retain the original source and the original integer clock `r >= 0`.
The exact retracing calculation, including ordinary endpoint uniqueness,
gives

\[
 \zeta_{M,r}(q_j)=\frac{v_j}{(M+1)v_{r+j}}
 \ge\frac{v_0}{C(M+1)}\qquad(0\le j\le M).
 \tag{10}
\]

Let `c_0=v_0/C > 0`. Consequently, as measures on ordinary integers,

\[
 \zeta_{M,r}\ge c_0\pi_M
 \ge c_0\frac{L}{M+1}\widehat\pi_{M,m}.
 \tag{11}
\]

Projection preserves this domination and all masses are nonnegative.
Combining with (7), for **every** finite inverse clock `r`,

\[
 \boxed{
 \operatorname{Col}_m(\zeta_{M,r})\ge
 c_0^2\left(\frac{M-m+1}{M+1}\right)^2
 \frac{(K-B_{M,m})^2}{\binom K{m+1}+2\binom K{m+2}}.
 }
 \tag{12}
\]

This argument does not subtract a total-variation error from an
exponentially small collision sum. It needs no rate for the capacity
defect `eta_M`, no mixing statement, no compact-kernel limit, and no
restriction on how large `r` is relative to `M`.

One may replace `c_0` by `v_a/C` after restricting the endpoint window to
`j >= a+m` and paying its exact window-length factor. The positive fixed
constant in (12) already suffices below.

## 4. The square-root gain at the critical entropy exponent

Put

\[
 \ell=\log_2 3,
 \qquad \Phi(a)=a\log a-(a-1)\log(a-1),
 \qquad \theta=\frac{\Phi(\ell)}{\log3}
              =0.949955527188\ldots.
 \tag{13}
\]

We use an elementary quantitative form of the real telescoping argument,
so the precision range is explicit. From (4),

\[
 A_M=M\ell+\log_2(q_0/q_M)
       +\sum_{j=0}^{M-1}\log_2\left(1+\frac1{3q_j}\right).
 \tag{14}
\]

On an injective positive segment, its `M` source states are distinct
positive integers, so their reciprocal sum is at most `1+log M`. Thus

\[
 A_M\le M\ell+\log_2q_0+
                \frac{1+\log M}{3\log2}.
 \tag{15}
\]

This estimate does not use an external orbit-packing theorem. On an
escaping orbit it holds for every `M`.

### Theorem 3: all-clock collision lower bound

Fix `0 < T < infinity`. There are positive constants `c` and `M_0`, allowed
to depend on `T`, the fixed source, and the same harmonic flow, such that
for `M >= M_0`, `m >= 1`, `m <= M`, and `m^2 <= T M`,

\[
 \boxed{
 \inf_{r\ge0}\operatorname{Col}_m(\zeta_{M,r})
       \ge c\sqrt m\,3^{-\theta m}.
 }
 \tag{16}
\]

The same assertion for `pi_M` needs no harmonic-flow input and has no
factor `c_0`.

**Proof.** Under these restrictions, (5) and (15) give

\[
 B_{M,m}\le\ell m+O_{q_0,T}(1).
 \tag{17}
\]

Indeed, the boundary contribution is `O(m^2/M)`, and the remaining
correction is `O_{q_0}(m log(M+1)/M)`, which is bounded and tends to zero
uniformly in `m <= sqrt(T M)`. Choose an integer
`K=ceil(ell m+D)+1`, where the fixed `D` bounds the error in (17).
Then `K-B_(M,m) >= 1` and `K=ell m+O_{q_0,T}(1)`.

Stirling's formula, or its elementary two-sided factorial bounds, gives
for fixed `D` and all `m >= 1`

\[
 \binom K{m+1}+2\binom K{m+2}
     \le C_D\,m^{-1/2}\exp(m\Phi(\ell)).
 \tag{18}
\]

For large `m` both binomial coefficients have arguments in fixed compact
proportional ranges; bounded `m` is absorbed into `C_D`. Since
`exp(m Phi(ell))=3^(theta m)` and `L/(M+1)` tends uniformly to one in
the stated range, (12) proves (16). ∎

Equivalently the order-two Renyi entropy obeys, uniformly over every `r`,

\[
 -\log\operatorname{Col}_m(\zeta_{M,r})
 \le \theta m\log3-\frac12\log m+O_{q_0,T,\nu}(1).
 \tag{19}
\]

This is a statement about collision entropy. It is not asserted as the
same logarithmic improvement for Shannon entropy.

### A sharper closing target, still unproved

Take any sequence with `M_i -> infinity`, `m_i -> infinity`,
`m_i^2=O(M_i)`, and arbitrary finite inverse clocks `r_i`. On the exact
same law (9), an arithmetic upper bound

\[
 \operatorname{Col}_{m_i}(\zeta_{M_i,r_i})
             =O(3^{-\theta m_i})
 \tag{20}
\]

would contradict (16). More generally an upper bound
`o(sqrt(m_i) 3^(-theta m_i))` would suffice.

The original entropy criterion requested an upper bound with exponent
`theta+delta`, `delta > 0`. The new finite argument removes that strict
exponent surplus; it does not establish (20). The precision restriction
includes `m_i` of logarithmic size in `M_i`, the scale already forced by
the ordinary diagonal atoms for any useful collision upper estimate.

The remaining problem is still arithmetic branching or endpoint
anti-concentration for these very same source laws. Fixed-root mixing
for another root distribution cannot replace (20).

## 5. An unconditional ordinary-height consequence

The distinct-word budget (2) also improves the running-height restriction.
It is independent of the harmonic flow and of escape-specific analytic
inputs.

### Theorem 4: uniform duration of a bounded-height injective segment

There is an absolute constant `C_1` such that every injective actual
positive odd segment `q_0,...,q_N` with

\[
 H=1+\max_{0\le j\le N}q_j\ge3
\]

satisfies

\[
 \boxed{N+1\le C_1\frac{H^\theta}{\sqrt{\log H}}.}
 \tag{21}
\]

**Proof.** Choose `m=ceil(log_3 H)`. If `N<m`, (21) follows after
increasing the absolute constant. Otherwise (6) shows that equal
length-`m` past words give equal residues for their endpoints. All
endpoints lie in `[1,H-1]`, and `3^m >= H`; distinct endpoints therefore
have distinct past words. There are `L=N-m+1` of them.

Set `t=log H`. Since the whole segment is injective, `N+1 <= H`,
`q_0 <= H`, and the elementary version of (15) gives

\[
 A_N\le\ell N+O(t).
\]

If `N < t^2`, the claimed upper bound follows from
`t^2 = O(H^theta/sqrt(t))`. In the other case `m=O(t)` and

\[
 \frac{mA_N}{N-m+1}\le\ell m+O(t^2/N)=\ell m+O(1),
\]

with absolute constants, after absorbing bounded `H`. Apply (2) with
an integer `K=ell m+O(1)` exceeding this mean by at least one. The
single-binomial version of (18) yields

\[
 L\le C\frac{\exp(m\Phi(\ell))}{\sqrt m}
   \le C'\frac{H^\theta}{\sqrt{\log H}}.
\]

The omitted `m-1=O(log H)` endpoints are absorbed into the right side.
This proves (21). ∎

Inverting (21), and using `H >= N+1`, gives an absolute `c_1 > 0` such
that every sufficiently long such segment satisfies

\[
 \boxed{
 1+\max_{0\le j\le N}q_j
 \ge c_1(N+1)^{1/\theta}
                  (\log(N+1))^{1/(2\theta)}.}
 \tag{22}
\]

Numerically the powers are

\[
 1/\theta=1.052680858607\ldots,
 \qquad 1/(2\theta)=0.526340429303\ldots.
\]

For an escaping orbit, (22) applies to **every shifted time window**
with the same absolute constant. Equivalently, its visits above height
`H` have gaps `O(H^theta/sqrt(log H))`.

This strengthens the running-maximum consequence of the previously
used exponent `39/40` occupation bound. It does **not** replace that
bound for total visits below `H`: an orbit can make large excursions
between its low-height visits. Selecting future tail minima does not
bound those intervening excursion maxima, so it does not remove this
remaining distinction.

## 6. Formal and source boundaries

`SOURCES.json` records the full PR185 commit, Git blob hashes and SHA-256
hashes of every baseline file used. In particular the source pins are:

| Baseline source at `39ba48e6a8af781193e28c679ea8ab64663c3aa6` | Exact role |
|---|---|
| `research/rigidity-closing-20261122/SAME_SOURCE_INVERSE_ENTROPY.md`, Sections 1--2, equations (1) and (7a) | The original harmonic-flow law and exact ordinary endpoint masses used in (9)--(12). |
| `research/deep-closing-20261122/ACTUAL_ORBIT_ENTROPY.md`, Sections 2--4 | Actual past-word residue projection, the finite sliding-window cost and the real telescope. |
| `research/deep-closing-20261122/lean/OriginalSourceEntropy.lean`, `sliding_window_cost_le` | The pre-existing formal sliding-window arithmetic. |

`DistinctWordBudget.lean` proves the ordinary and squared hockey-stick
identities, both histogram deficit inequalities, the mean-cost count
bound, and the finite Cauchy collision inequality. Its histogram
capacity assumption is explicit. The file does not assert a Lean
formalization of stars-and-bars, the Collatz word-to-residue projection,
the Stirling estimate, or the ordinary harmonic-flow construction.
All nine public theorem declarations compiled under Lean 4.34.1 with
Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`; the axiom audit reports
only `propext`, `Classical.choice` and `Quot.sound`, with no `sorryAx`.
`verification.json` and `lean-check.log` record this check. The small
exact-integer checker also checks the word-indexing and window-size
factors on bounded actual prefixes; its explicit range is recorded in
the receipt and does not support an asymptotic claim.

The actual sliding-window estimate already has a finite Lean proof in
the baseline `OriginalSourceEntropy.lean`; its mathematical role is (5).
The present proof retains that source and clock.

Latest overlap check: the canonical time/entropy attempt on PR178,
`7e4569476e152f6b8537bdc1711df595ec1ffd89`, was read in full. Its
all-shift KL comparison and stationary-kernel entropy formula are not
claimed here as new results. The fixed-source shadow entropy note on
PR175, `8a8b1eea6c9fdfbce7b0bbf0af4eb771791e3a73`, was also inspected,
including its zero-entropy symbolic control. Its rational-shadow
criterion is not assumed to follow from an entropy bound.

Primary literature consulted during the closing attack included
[*Critical barriers and memory costs in Collatz inverse dynamics*,
Paper 150/v2](https://rstation.ai/problems/collatz/papers/150), especially
the original-source prefix cover and the theorem statements, and
[*Ternary harmonic moments and Collatz orbit occupation*, Paper 176/v1](https://rstation.ai/problems/collatz/papers/176), the statement section
and inverse-path identities. These are not prerequisites for (1)--(22),
and no full-proof certification of those papers is claimed. Their
additional regularity, population averaging, or moment-decay inputs
have not supplied the missing same-law upper bound (20).

No full Collatz conclusion or global historical novelty claim is made.
