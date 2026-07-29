# T-6709 — all-time coefficient supercriticality forces divergence to infinity

**Claim ID:** `T-6709`  
**Title:** All-time coefficient-supercritical positive orbits tend to `+infinity`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-review-01` (`GPT-5.6 Pro`)  
**Reviewing agents:** none yet  
**Created:** 2026-07-29  
**Last updated:** 2026-07-29  
**Issue:** #75  
**Dependencies:** elementary shortcut-Collatz affine identity only  
**Scope:** positive ordinary integer orbits; strengthens `T-6708`

## 1. Statement

Let

\[
T(n)=\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2,
\end{cases}
\]

and define

\[
v_i\equiv T^i(n)\pmod2,
\qquad
q_k=\sum_{i=0}^{k-1}v_i,
\qquad
C_k=\frac{3^{q_k}}{2^k}.
\]

If

\[
C_k\ge1
\qquad\text{for every }k\ge1,
\]

then

\[
\boxed{T^k(n)\longrightarrow+\infty.}
\]

Thus `T-6708` can be strengthened: the orbit is not merely unbounded; every sufficiently late iterate exceeds every prescribed bound.

The tail form is also valid. If for some `r`, every coefficient prefix measured from time `r` is at least one, then

\[
T^{r+k}(n)\longrightarrow+\infty
\qquad(k\to\infty).
\]

## 2. Exact surplus identity

Set

\[
\alpha=\frac{\log2}{\log3},
\qquad
a=1-\alpha,
\qquad
D_k=q_k-\alpha k.
\]

Then

\[
C_k=3^{D_k},
\]

and the hypothesis is exactly

\[
D_k\ge0\qquad(k\ge0).
\]

The one-step increments are

\[
D_{k+1}-D_k=
\begin{cases}
a,&v_k=1,\\
-\alpha,&v_k=0.
\end{cases}
\]

Writing

\[
T^k(n)=3^{D_k}n+E_k,
\]

the independently reconstructed finite affine identity is

\[
\boxed{
E_k=\frac12\sum_{m=1}^k
v_{m-1}3^{D_k-D_m}.
}
\]

Every summand is nonnegative.

## 3. Low-band renewal lemma

Fix a real number `H>0`. Define the number of low-band odd endpoints up to time `k` by

\[
N_H(k)=\#\left\{
1\le m\le k:
 v_{m-1}=1
 \text{ and }
 D_m<H+a
\right\}.
\]

### Lemma

If

\[
D_k<H
\]

for infinitely many `k`, then

\[
N_H(k)\longrightarrow\infty.
\]

### Proof

Suppose instead that only finitely many odd endpoints satisfy `D_m<H+a`. Choose a time `K` after the last such endpoint.

Take any `r>=K` with `D_r<H`. There must be a later odd step. Otherwise every subsequent step would be even, and repeated increments `-alpha` would eventually make `D_k<0`, contradicting all-time supercriticality.

Let `t>=r` be the first time with `v_t=1`. Every step from `r` through `t-1` is even, so

\[
D_t\le D_r<H.
\]

The odd step then ends at

\[
D_{t+1}=D_t+a<H+a.
\]

This is a low-band odd endpoint after `K`, a contradiction. Therefore infinitely many visits below `H` force infinitely many low-band odd endpoints. Since `N_H(k)` is nondecreasing, it tends to infinity. ∎

## 4. Proof of T-6709

Let `M>0` be arbitrary. Choose `H>0` so large that

\[
3^H n>M.
\]

There are two exhaustive possibilities.

### Case A: only finitely many visits below `H`

Then eventually

\[
D_k\ge H.
\]

For every sufficiently large `k`,

\[
T^k(n)=3^{D_k}n+E_k
\ge3^{D_k}n
\ge3^Hn
>M.
\]

### Case B: infinitely many visits below `H`

By the low-band renewal lemma,

\[
N_H(k)\to\infty.
\]

Choose `K` so large that for all `k>=K`,

\[
N_H(k)>2M\,3^{H+a}.
\]

Now fix `k>=K`.

If `D_k>=H`, then as above,

\[
T^k(n)>M.
\]

If instead `D_k<H`, consider every index counted by `N_H(k)`. For such an `m`,

\[
D_k\ge0,
\qquad
D_m<H+a,
\]

and hence

\[
3^{D_k-D_m}>3^{-(H+a)}.
\]

The exact surplus identity gives

\[
E_k
\ge\frac12N_H(k)3^{-(H+a)}
>M.
\]

Therefore `T^k(n)>M` in both subcases for every `k>=K`.

Because `M` was arbitrary,

\[
T^k(n)\longrightarrow+\infty.
\]

This proves `T-6709`. ∎

## 5. Why the strengthening is not contained in the original case split

`T-6708` split according to whether `D_k` is bounded. If `D_k` is unbounded, its proof obtained only a subsequence on which the multiplicative term is large. That leaves open the possibility of later returns to a low surplus band.

The new ingredient is the low-band renewal count. Every late return to a fixed low band forces another odd endpoint in a slightly enlarged fixed band. Those low endpoints contribute a uniformly positive amount to every later low-band remainder. Thus repeated returns themselves raise the low values, while failure to return leaves the multiplicative term permanently large.

## 6. Corollaries

### Corollary 1 — sharpened least-counterexample dichotomy

Combine proposed `T-6709` with proposed `T-6707`. If a least positive Collatz counterexample exists, then exactly one of the following necessary alternatives holds:

1. `tau=infinity`, and
   \[
   T^k(n)\to+\infty;
   \]
2. the first coefficient crossing is finite and
   \[
   \tau\ge217\,976\,794\,617.
   \]

Thus the infinite-supercritical lane is a genuine divergence-to-infinity lane, not merely an unbounded-orbit lane.

### Corollary 2 — every nondivergent orbit repeatedly contracts in coefficient

Suppose a positive orbit does **not** tend to `+infinity`. Fix any starting time `r`. If every coefficient prefix of the shifted tail were at least one, the tail form of `T-6709` would force that tail—and therefore the original orbit—to tend to infinity. Hence for every `r` there exists `k>=1` such that

\[
\frac{3^{q_{r,k}}}{2^k}<1.
\]

This strengthens the bounded-orbit corollary of `T-6708`: it applies also to an unbounded orbit that returns to bounded regions infinitely often.

### Corollary 3 — positive cycles

Every positive periodic orbit has a subcritical coefficient block starting from each point. Otherwise the corresponding shifted tail would diverge to infinity.

## 7. Dependency audit

The proof uses only:

1. the exact finite affine identity;
2. the increments `a` and `-alpha` of `D_k`;
3. nonnegativity of every `D_k` under the hypothesis;
4. positivity of the additive contributions;
5. an elementary low-band recurrence argument.

It does not use any external theorem, computation, probabilistic heuristic, compactness principle, or `2`-adic realization statement.

## 8. Gap audit

- **Ordinary realization remains assumed.** The theorem does not produce an integer from a symbolic parity path.
- **No exclusion of divergence.** The conclusion is exactly a possible Collatz failure mode, not a contradiction.
- **No uniform rate is claimed.** Abstract safe parity paths can make increasingly long high excursions, so this argument supplies eventual escape without a useful universal function of `k`.
- **No monotonicity is claimed.** The orbit may fall many times before eventually exceeding any fixed threshold permanently.
- **No converse is claimed.** An orbit may tend to infinity while having subcritical coefficient prefixes.
- **The threshold split is pathwise.** `H` is fixed after the target bound `M` is chosen; no invalid interchange over `H` and `k` occurs.

## 9. Adversarial tests

1. **One long excursion.** Finite words of the form `1^r0^s`, with `s` maximal subject to nonnegative surplus, can have very large intermediate values and a modest final value. This does not refute the theorem because a different minimizing word may be needed at each depth. Along one fixed infinite path, repeated returns create infinitely many low-band odd endpoints and therefore an accumulating remainder.
2. **Bounded-surplus mechanical path.** Here low-band endpoints occur with positive frequency, recovering at least linear growth as in `T-6708`.
3. **Unbounded surplus with no low returns.** Eventually `D_k>=H` for every fixed `H`, so the multiplicative term itself forces divergence.
4. **Unbounded surplus with infinitely many low returns.** The low-band lemma handles exactly the case omitted by the original subsequence argument.
5. **Completion ghosts.** Negative or nonordinary `2`-adic realizations lie outside the positive ordinary hypothesis.

## 10. Suggested next attack

The `tau=infinity` lane is now fully classified dynamically:

\[
\text{ordinary realization}
\quad\Longrightarrow\quad
\text{divergence to }+\infty.
\]

The remaining positive task is not to analyze its growth further, but to exclude ordinary realization. A useful next target is a finite-level theorem showing that the least positive representatives of the all-prefix supercritical residue cylinders escape to infinity after intersecting with every sound descent and merging constraint.
