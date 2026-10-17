# L-9304 — Exact 2–3 phase reciprocity

**Claim ID:** L-9304  
**Title:** A Fourier phase modulo a power of 64 is a reciprocal residue modulo a power of 81 plus an explicit tiny term  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** elementary modular arithmetic; LTE for the displayed order formula is reproved below  
**Scope:** depth-period averaging for the `64 -> 81` survivor Fourier product  
**Related counterexample candidates:** none

## Statement

Fix integers

\[
K\ge1,\qquad 0\le t<K,\qquad \theta\ge1,
\]

and put

\[
M_{K,t}=64^{K-t},\qquad Q_t=81^{t+1}.
\]

Assume

\[
17\theta<M_{K,t}. \tag{1}
\]

Let `z_(K,t)(theta)` be the unique residue in `{0,...,M_(K,t)-1}` satisfying

\[
z_{K,t}(\theta)\equiv17\theta Q_t^{-1}\pmod{M_{K,t}},
\]

and let `q_(K,t)(theta)` be the unique residue in `{0,...,Q_t-1}` satisfying

\[
q_{K,t}(\theta)
\equiv-17\theta M_{K,t}^{-1}
\pmod{Q_t}. \tag{2}
\]

Then

\[
\boxed{
Q_t z_{K,t}(\theta)
=17\theta+q_{K,t}(\theta)M_{K,t}
} \tag{3}
\]

and hence

\[
\boxed{
\frac{z_{K,t}(\theta)}{M_{K,t}}
=
\frac{q_{K,t}(\theta)}{Q_t}
+
\frac{17\theta}{Q_tM_{K,t}}.
} \tag{4}
\]

The reciprocal residue has the alternate form

\[
q_{K,t}(\theta)
\equiv
-17\theta\,64^{t-K}
\pmod{81^{t+1}}. \tag{5}
\]

For every `m >= 0`, the vector

\[
(q_{K,0}(\theta),\ldots,q_{K,m}(\theta))
\]

is periodic in `K` with period

\[
\boxed{P_m=9\cdot81^m.} \tag{6}
\]

Over any `P_m` consecutive values of `K`, the variable

\[
V_K=64^{-K}\pmod{81^{m+1}}
\]

runs exactly once through

\[
1+9\mathbb Z/81^{m+1}\mathbb Z. \tag{7}
\]

Finally, write

\[
\theta=81^d\theta_0,\qquad 81\nmid\theta_0.
\]

For `t<d`,

\[
q_{K,t}(\theta)=0,
\]

while for `t>=d`,

\[
\boxed{
q_{K,t}(\theta)
=81^d q_{K-d,t-d}(\theta_0)
} \tag{8}
\]

with the residue on the right taken modulo `81^(t-d+1)`. Thus divisibility of the frequency by `81^d` removes exactly the first `d` reciprocal phase levels.

## Definitions

The phase factor appearing in the issue-#4 product is

\[
\left|\cos\!\left(
\pi\frac{z_{K,t}(\theta)}{64^{K-t}}
\right)\right|.
\]

Equation `(4)` moves the modular inverse from a power of `81` modulo a power of `64` to a power of `64` modulo a power of `81`. The final summand in `(4)` is called the *reciprocity error*. It is an exact rational number, not asymptotic notation.

## Motivation

The proposed fixed-frequency depth average on issue #4 is driven by the orbit of `64^{-K}` modulo powers of `81`. To use that orbit rigorously one first needs the exact bridge `(4)`, including the small term that informal phase arguments can accidentally discard.

The valuation shift `(8)` is equally important. A frequency divisible by a large power of `81` has several identically zero reciprocal phases. Any depth-period theorem that charges a contraction at every one of those levels has an invalid uniformity step.

## Proof

### Reciprocal identity

By `(2)`, the integer

\[
17\theta+q_{K,t}(\theta)M_{K,t}
\]

is divisible by `Q_t`. Define

\[
z'=
\frac{17\theta+q_{K,t}(\theta)M_{K,t}}{Q_t}.
\]

Because `0 <= q_(K,t) <= Q_t-1` and `17 theta < M_(K,t)`,

\[
0<z'<M_{K,t}.
\]

Moreover

\[
Q_tz'\equiv17\theta\pmod{M_{K,t}},
\]

so `z'` is exactly the chosen residue `z_(K,t)(theta)`. This proves `(3)`, and division by `Q_tM_(K,t)` gives `(4)`. Equation `(5)` is just `(2)` with `M_(K,t)=64^(K-t)`.

### Period and subgroup

For every positive integer `n`, LTE gives

\[
v_3(64^n-1)=v_3(64-1)+v_3(n)=2+v_3(n).
\]

Since

\[
81^{m+1}=3^{4m+4},
\]

the least positive `n` with `64^n=1 (mod 81^(m+1))` has

\[
v_3(n)=4m+2.
\]

Therefore

\[
\operatorname{ord}_{81^{m+1}}(64)
=3^{4m+2}
=9\cdot81^m=P_m.
\]

Every power of `64` is `1 mod 9`. The subgroup `1+9Z/81^(m+1)Z` also has exactly

\[
81^{m+1}/9=P_m
\]

elements. Hence the powers of `64`, and equally the powers of `64^{-1}`, run through that subgroup exactly. Equations `(5)` for `t<=m` are reductions of the same `V_K`, proving `(6)` and `(7)`.

### Valuation shift

Suppose `theta=81^d theta_0`. If `t<d`, the right side of `(5)` is divisible by the modulus `81^(t+1)`, so `q_(K,t)(theta)=0`.

If `t>=d`, the least residue in `(5)` is divisible by `81^d`. Dividing the congruence and modulus by `81^d` gives

\[
\frac{q_{K,t}(\theta)}{81^d}
\equiv
-17\theta_0\,64^{t-K}
\pmod{81^{t-d+1}}.
\]

Because

\[
t-K=(t-d)-(K-d),
\]

the quotient is exactly `q_(K-d,t-d)(theta_0)`. This proves `(8)`. QED.

## Dependency audit

- Only the definitions of the issue-#4 Fourier phases are used.
- The multiplicative-order formula is proved directly by LTE in this file; no branch-qualified theorem is imported as a black box.
- No frequency-block or depth-block mean is assumed.
- No Collatz trajectory statement is used.

## Gap audit

- Condition `(1)` is essential for the representative equality `(3)` with `q` in the displayed range. In the applications below it holds by an enormous margin.
- The residue identity remains valid without `(1)`, but an additional integer room can enter `(3)`; that form is not silently used here.
- Periodicity of the reciprocal residues does not by itself imply decay of the cosine product.
- Dividing by `81^d` removes phase levels; it does not assert that the remaining phases are independent.
- The result concerns positive frequencies. Absolute-value versions for negative frequencies follow by conjugation.

## Adversarial tests

1. At `K=1`, `t=0`, `theta=1`, one has `q=1` because `-17*64^(-1)=1 (mod 81)`, and `(4)` reproduces the phase `1/64`.
2. If `theta=81^d`, then the first `d` reciprocal residues are exactly zero. This is the test that catches an overstrong uniform depth contraction.
3. Shifting the start of a `P_m`-block changes the order of the subgroup traversal but not the multiset.
4. The error terms satisfy
   \[
   \sum_{t=0}^{m}
   \frac{17\theta}{81^{t+1}64^{K-t}}
   \le\frac{\theta}{64^K},
   \]
   an estimate used explicitly in `T-9303`.

## Remaining uncertainty

The lemma is complete-looking. The highest-value independent check is the sign in `(2)` against the issue-#4 convention; changing the additive-character convention conjugates the complex coefficient but does not affect the absolute-value consequences.

## Suggested next attack

Use the subgroup filtration in `(7)` one level at a time. Conditional on the lower residue, the next lift produces an equally spaced cosine grid. `T-9303` carries this out while charging the exact loss dictated by `v_3(theta)`.