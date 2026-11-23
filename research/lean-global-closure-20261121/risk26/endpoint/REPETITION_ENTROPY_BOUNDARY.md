# The exact repetition cost of the critical stationary branch

23 November 2026. **Status: written theorem and a machinery-application
boundary. No ordinary escape exclusion is proved.**

The new result is a sharp calculation for the critical iid branch that the
actual-source entropy dichotomy already isolates. Its maximum demand under
the complete all-template repetition-height inequality grows with exponent

\[
 \boxed{\kappa_*={1\over\log_2(\log_2 3)}
             =1.5050070664\ldots .}
\]

In particular, all those repetition inequalities are simultaneously
compatible with a polynomial envelope. They do not force a contradiction
with the critical iid stationary branch. This calculation does **not**
identify the actual selected ordinary ray with a typical sample of its
stationary limit, and does not construct a positive integer realizing that
branch. Those are separate arithmetic requirements.

## 1. Frozen source and exact existing arithmetic input

The starting checkout is PR175 at
`bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17`. The refreshed inputs are:

| Input | Exact source |
|---|---|
| Actual stationary deficit/iid dichotomy | PR180, `7cfd911d35382d9d3bc988060ba88ade78a4267e`, `research/whole-source-20261123/COLLISION_CORE.md`, Sections 3–4 |
| Exact endpoint collision exponent in that iid branch | Same PR/head, `research/closing-step-20261123/COLLISION_CLOSURE.md`, Sections 4–5 |
| Uniform all-template ordinary repetition budget | PR178, `a9b23dcee61a4b65a63aa4e7ca653d875a405037`, `research/reassessment-20261123/collision/FINITE_CLOCK_AND_FIXED_SOURCE.md`, Section 4 |
| Critical generic rays need not be typical for recurrence | PR176, `81095581a1dccb8b5d89ee2ea3e9ba4a7b447e0a`, `research/lean-global-resolvent-20261121/overview/global-closing/GENERIC_RAY_CONSTRUCTION.md` |

Use the accelerated odd map

\[
 U(n)={3n+1\over2^{v_2(3n+1)}},\qquad q_i=U^i(q_0).
\]

Suppose this is one escaping positive ordinary orbit. If the gap sequence
beginning at time `i` has a consecutive repetition `w^k`, where `w` has
length `d>=1`, total `A`, and `k>=2`, then PR178 proves

\[
 2^{(k-1)A+1}\mid q_{i+d}-q_i,
 \qquad
 2^{(k-1)A+1}<(3/2)^d(q_i+1).
 \tag{R1}
\]

The no-cycle condition needed for the strict inequality holds on the
escaping orbit. The second statement follows from the divisibility and
`U(x)+1 <= (3/2)(x+1)`. Retaining the original source gives the weaker
but uniform consequence

\[
 2^{(k-1)A+1}<(3/2)^{i+d}(q_0+1).
 \tag{R2}
\]

Neither statement makes collisions of different endpoint words into
consecutive word repetitions. The present theorem grants that repetitions
are available and tests exactly how much source height they demand.

## 2. Repetition demand as a random variable

Put

\[
 b=\ell=\log_2 3,\quad p=1/b,\quad r=1-p,
 \qquad \gamma(g)=p r^{g-1}\quad(g\ge1).
\]

In the maximum-Shannon branch of PR180, the actual stationary gap law is
exactly `gamma^Z`. In this section that law, with no further substitution,
is the probability under consideration.

For an infinite gap sequence `G`, define

\[
 D_i(G)=\sup\left\{
 {2^{(k-1)A(w)+1}\over(3/2)^{|w|}}:
 k\ge2,\ |w|\ge1,\ G_{i+1}\cdots G_{i+k|w|}=w^k
 \right\},
 \tag{R3}
\]

with the supremum of the empty set equal to zero. A single occurrence is
counted for every template and power which describes it; this deliberate
overcount makes the upper estimate stronger. Let

\[
 D^*(N)=\max_{0\le i<N}D_i.
\]

Periods in (R3) may extend beyond `N`; no terminal truncation is used.
For the original escaping ray, (R1) says simply

\[
                         D_i\le q_i+1. \tag{R4}
\]

## 3. Every moment below the exact threshold is finite

Set `s_*=log_2 b`. For `0<s<s_*`, let

\[
 a_s=p2^s<1,\quad z_s=r2^s<1,
 \qquad
 \lambda_k(s)={3^{-s}a_s^k\over1-2^{-s}z_s^k}
 \quad(k\ge2).
 \tag{R5}
\]

**Lemma 1.** For every `0<s<s_*`,

\[
 \boxed{\mathbb E D_i^s
 \le 2^s\sum_{k\ge2}{\lambda_k(s)\over1-\lambda_k(s)}
 =:C_s<\infty.}
 \tag{R6}
\]

**Proof.** A specified repeated template `w^k` has probability
`gamma(w)^k`. At a fixed period length `d`, summing the nonnegative
`s`-powers of its demand gives

\[
 \begin{aligned}
 &\sum_{|w|=d}\gamma(w)^k
 \left({2^{(k-1)A(w)+1}\over(3/2)^d}\right)^s\\
 &\quad=2^s\left((3/2)^{-s}
       \sum_{g\ge1}\gamma(g)^k2^{s(k-1)g}\right)^d
 =2^s\lambda_k(s)^d.\tag{R7}
 \end{aligned}
\]

The single-letter sum is geometric, and gives exactly (R5).
For fixed `s<s_*`, `lambda_k(s)` decreases with `k`; moreover it is
bounded by a constant depending on `s` times `a_s^k`.

It remains to check `lambda_2(s)<1`. Its logarithm is convex in `s`,
as follows either from Holder or from its positive exponential sum.
At the two endpoints,

\[
 \lambda_2(0)={1\over2b-1}<1,
 \qquad
 \lambda_2(s_*)={b^{-b}\over1-(b-1)^2/b}<1.\tag{R8}
\]

The second inequality can be checked without a decimal estimate.
The exact inequalities `3^2>2^3` and `3^5<2^8` give
`3/2<b<8/5`. Hence `b^{-b}<2/3`, while
`(b-1)^2/b < (3/5)^2(2/3)=6/25`. Thus the second quantity in (R8)
is less than `50/57`. Convexity proves the claim throughout the interval.

Consequently the sums over `d` are geometric with a uniform ratio at
most `lambda_2(s)<1`; summing over `k` is finite because `a_s<1`.
The supremum in (R3), raised to `s`, is at most the sum of the same
nonnegative quantities over all occurring templates and powers. Tonelli
and (R7) now prove (R6). `QED`.

This argument charges arbitrarily large gaps, all period lengths, all
powers, and all overlaps. It has no finite-alphabet cutoff.

## 4. Sharp growth of the maximum demand

**Theorem 2.** Under the critical iid stationary law, almost surely,

\[
 \boxed{\lim_{N\to\infty}
 {\log\max(1,D^*(N))\over\log N}={1\over s_*}.}
 \tag{R9}
\]

**Upper bound.** For `t>1/s`, stationarity, (R6), and a union bound give

\[
 \Pr\{D^*(2^n)>2^{nt}\}
 \le C_s 2^{n(1-st)}.
\]

This is summable in `n`. Borel–Cantelli, followed by monotonicity between
successive powers of two, gives the upper exponent `t`. First let
`t` decrease to `1/s`, then let `s` increase to `s_*`, through countable
sequences.

**Lower bound.** Fix `0<epsilon<1`, and partition the first `N=2^n`
gaps into disjoint blocks of length

\[
 L_N=\left\lfloor{(1-\epsilon)\log N\over-\log p}\right\rfloor.
\]

The blocks are independent. Each is all ones with probability
`p^{L_N} >= N^{-(1-epsilon)}`. The probability that none is all ones
is at most

\[
 \exp[-\lfloor N/L_N\rfloor p^{L_N}]
 \le \exp[-c_\epsilon N^\epsilon/\log N],
\]

eventually. These failure probabilities are summable on the dyadic
sequence. Every such all-one run is the template `w=(1)` repeated
`k=L_N` times. Its demand is `2^{L_N}/(3/2)`. Thus the lower exponent
is at least `(1-epsilon)log 2/(-log p)`. Let epsilon decrease to zero,
and again use monotonicity between dyadic horizons. This is `1/s_*`,
proving (R9). `QED`.

**Corollary 3 (all starts with one constant).** For every `kappa>kappa_*`,
almost surely there is one finite `K=K(G,kappa)` such that

\[
                  D_i\le K(i+1)^\kappa\quad(i\ge0).\tag{R10}
\]

Choose `s<s_*` with `kappa s>1`. The expectation of
`sum_i D_i^s/(i+1)^{kappa s}` is finite by (R6). Its almost-sure finite
sum supplies `K`. This proves (R10) simultaneously for every repeated
template and every power.

Since a polynomial is bounded by a constant times `(3/2)^i`, it also
follows that `sup_i D_i/(3/2)^i` is almost surely finite. Consequently
there are fixed finite constants `B` for which the set of critical iid
words satisfying `D_i < B(3/2)^i` at **all** positions has positive
probability. Such a constant can be chosen in the form `q_0+1` for a
positive odd ternary unit. This is compatibility with the numerical
budget (R2), not with the infinitely many ordinary realization congruences
for that integer.

## 5. Why the deep repetition route does not close

Adamczewski–Bugeaud's published stammering condition requires prefixes
`U_n V_n^w` for a fixed `w>1`, with `|U_n|/|V_n|` bounded and
`|V_n|` tending to infinity. Its Subspace-Theorem saving is measured
relative to the height of the complete preperiod and period. A large
collision moment, which also counts separated repetitions and unequal
words with equal residues, supplies none of those conditions. Their
Theorem 6 concerns ordinary Hensel digits; Collatz gap digits require
their own affine approximation argument.

Ornstein–Weiss gives exponential recurrence-time scale `exp(hm)` for
typical stationary ergodic samples. Such widely separated repetitions
do not supply the bounded preperiod ratio used by stammering methods.
More basically, a selected ordinary ray with the same empirical
stationary law is not automatically a typical sample for a growing-word
recurrence theorem. The already constructed generic-ray examples in
PR176 make that quantifier distinction concrete.

The present result is a stronger test of the specific new source-height
budget: even after every template and every power is included, its
demand under the critical iid law is only polynomial with the exact
exponent (R9). There is no known ordinary upper bound below that exponent.
Even if there were one, applying (R9) to the selected ray would need a
separate orbitwise recurrence-rate theorem.

The endpoint law in this same iid branch already has the exact PR180
collision dimension `log(2 ell-1)/log 3=0.7051555980...`, whereas its
Shannon dimension is `Phi(ell)/log 3=0.9499555272...`. These are compatible
with (R9); no iid source was substituted in proving the branch's law.
A closing argument must exclude the actual iid branch using information
that is stronger than these repetition-height inequalities, or prove a
different arithmetic contradiction for the unchanged source.

## 6. Primary sources and verification scope

- Boris Adamczewski and Yann Bugeaud, *On the complexity of algebraic
  numbers I. Expansions in integer bases*, Annals of Mathematics 165
  (2007), 547–565. Section 4, Condition `(*)_w`, and Theorem 6 were read
  in the [publisher PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v165-n2-p04.pdf).
- Donald Ornstein and Benjamin Weiss, *Entropy and data compression
  schemes*, IEEE Transactions on Information Theory 39 (1993), 78–83,
  DOI `10.1109/18.179344`. The recurrence statement was read in the
  [authors' institutional record](https://cris.huji.ac.il/en/publications/entropy-and-data-compression-schemes/).
  The publisher page was blocked by an automated access screen, so no
  full-paper inspection is claimed. Theorems 1–2 above are proved directly
  and do not use Ornstein–Weiss as a premise.
- The more recent Collatz shadow criterion in
  [Weaver, rStation discussion 6](https://rstation.ai/r/collatz/posts/6)
  and its scope discussion in
  [Paper 16 v2](https://rstation.ai/problems/collatz/papers/16/v2)
  were read. They require precise approximation or substitution structure,
  not only a deficient collision exponent. No unreviewed theorem from
  those manuscripts is imported here.

`check_endpoint_machinery.py` checks 20 finite weighted tensor/geometric
identities using exact rational arithmetic. It is an arithmetic control
of (R7), not evidence for an almost-sure limit. The all-time claims above
are the written moment and Borel–Cantelli proofs; no new Lean verification
or complete escape argument is claimed.
