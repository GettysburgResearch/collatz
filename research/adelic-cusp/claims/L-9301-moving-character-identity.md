# L-9301 — Moving-character Fourier identity

**Claim ID:** L-9301  
**Title:** Every depth-`K` Fourier product is one coefficient of the fixed survivor measure  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `D-9301`; exact definitions below  
**Scope:** Fourier analysis of the issue-#4 `64 -> 81` survivor sets  
**Related counterexample candidates:** none

## Statement

Let `mu` be the fixed measure from `D-9301`. Define the additive character

\[
\psi_2(x)=\exp(2\pi i\{x\}_2),
\]

where `{x}_2` is the unique dyadic rational in `[0,1)` such that

\[
x-\{x\}_2\in\mathbb Z_2.
\]

For `q in Q_2`, define

\[
\widehat\mu(q)=\int_{\mathbb Z_2}\psi_2(qx)\,d\mu(x).
\]

For `K >= 1`, let

\[
R_K=
\left\{
\sum_{t=0}^{K-1}d\varepsilon_t\rho^t
\pmod{64^K}:
\varepsilon_t\in\{0,1\}
\right\}.
\]

Every element of `R_K` is interpreted as its integer residue in
`{0,1,...,64^K-1}`. Put

\[
S_K(\theta)=\sum_{A\in R_K}
\exp\!\left(2\pi i\frac{\theta A}{64^K}\right).
\]

Then:

1. `R_K` has exactly `2^K` elements;
2. for every integer `theta`,
   \[
   \boxed{
   \widehat\mu\!\left(\frac{\theta}{64^K}\right)
   =\frac{S_K(\theta)}{2^K};
   }
   \]
3. for every `q in Q_2`,
   \[
   \boxed{
   \widehat\mu(q)
   =\prod_{t\ge0}
     \frac{1+\psi_2(qd\rho^t)}{2};
   }
   \]
   the product is actually finite whenever `q` represents a character of `Z_2`;
4. the exact functional equation is
   \[
   \boxed{
   \widehat\mu(q)
   =\frac{1+\psi_2(dq)}{2}\,\widehat\mu(\rho q);
   }
   \]
5. writing
   \[
   F_K(\theta)=\frac{|S_K(\theta)|}{2^K},
   \]
   one has the exact self-similarity
   \[
   \boxed{
   F_K(64^j\theta)=F_{K-j}(\theta)
   }
   \]
   for every `0 <= j < K`.

Thus the apparently depth-varying family is the restriction of one stationary Fourier transform to the moving rational cusp

\[
q_{K,\theta}=\frac{\theta}{64^K}.
\]

## Definitions

For `x in Q_2`, the class of `x` in `Q_2/Z_2` has a unique finite negative-power binary expansion; `{x}_2` is the corresponding rational in `[0,1)`. With this convention the displayed character has the same positive exponential sign as `S_K`.

The phrase *moving rational cusp* is descriptive: when `1 <= |theta| <= 2^K`, the rational number `theta/64^K` tends rapidly to zero in the real absolute value while its 2-adic absolute value is generally large. No mixing theorem is hidden in this terminology.

## Motivation

The literature audit correctly observed that the issue-#4 products form a changing finite-group triangular array, so fixed real self-similar Fourier-decay theorems cannot simply be quoted. This lemma supplies an exact stationary bridge. It does not supply decay: the hard question becomes uniform control of one fixed transform along a highly noncompact sequence of characters.

## Proof

### Cardinality of `R_K`

Suppose two length-`K` words first differ at position `j<K`. The same calculation as in `D-9301` gives

\[
v_2\!\left(
\sum_{t<K}d(\varepsilon_t-\varepsilon'_t)\rho^t
\right)=6j<6K=v_2(64^K).
\]

Their residues modulo `64^K` are therefore distinct. There are `2^K` words, so `|R_K|=2^K`.

### Product formula

Let the random variable

\[
X=\sum_{t\ge0}d\varepsilon_t\rho^t
\]

have law `mu`, with independent fair digits. Independence gives

\[
\begin{aligned}
\widehat\mu(q)
 &=\mathbb E\,\psi_2(qX)\\
 &=\mathbb E\prod_{t\ge0}\psi_2(qd\varepsilon_t\rho^t)\\
 &=\prod_{t\ge0}
   \mathbb E\,\psi_2(qd\varepsilon_t\rho^t)\\
 &=\prod_{t\ge0}
   \frac{1+\psi_2(qd\rho^t)}{2}.
\end{aligned}
\]

For a continuous character of `Z_2`, `q` is represented by an element of `2^{-N}Z_2` for some finite `N`. Since `v_2(d rho^t)=6t`, all sufficiently late products have `qd rho^t in Z_2`, so their character value is `1`. Hence the product is finite and no infinite-product interchange issue occurs.

### Evaluation at `theta/64^K`

Take

\[
q=\frac{\theta}{64^K}.
\]

For every `t >= K`,

\[
qd\rho^t
 =\frac{17\theta\,64^{t-K}}{81^{t+1}}
 \in\mathbb Z_2,
\]

so the corresponding factors equal `1`. Expanding the first `K` factors gives

\[
\widehat\mu\!\left(\frac{\theta}{64^K}\right)
 =2^{-K}\sum_{\varepsilon_0,\ldots,\varepsilon_{K-1}}
 \psi_2\!\left(
   \frac{\theta}{64^K}
   \sum_{t<K}d\varepsilon_t\rho^t
 \right).
\]

If `A` is the residue modulo `64^K` represented by the finite sum, then the definition of `{.}_2` gives

\[
\psi_2\!\left(\frac{\theta A}{64^K}\right)
 =\exp\!\left(2\pi i\frac{\theta A}{64^K}\right).
\]

The length-`K` words give the distinct set `R_K`, so the expanded product is exactly `2^{-K}S_K(theta)`.

### Functional equation

Split the random series at its first digit:

\[
X=d\varepsilon_0+\rho X',
\]

where `X'` is independent of `epsilon_0` and has the same law as `X`. Therefore

\[
\widehat\mu(q)
 =\frac{1+\psi_2(dq)}{2}\,\widehat\mu(\rho q).
\]

### Exact depth self-similarity

Using the moving-character identity,

\[
F_K(64^j\theta)
 =\left|\widehat\mu\!\left(
   \frac{64^j\theta}{64^K}
  \right)\right|
 =\left|\widehat\mu\!\left(
   \frac{\theta}{64^{K-j}}
  \right)\right|
 =F_{K-j}(\theta).
\]

QED.

## Dependency audit

- `D-9301` supplies the random series and independence of digits.
- No issue-#4 theorem is needed for the proof.
- The final crosswalk identifies this `S_K` with the same finite Fourier sum used in `EQ.md`; a reviewer should check notation and sign, but the identity above is self-contained.

## Gap audit

- Stationarizing the measure does not imply any Fourier decay along the cusp.
- The character group of `Z_2` is discrete; ordinary continuity at real frequency zero is irrelevant because `theta/64^K` escapes 2-adically.
- An external theorem for a fixed real IFS still does not automatically apply to this 2-adic character sequence.
- The equality uses the fair Bernoulli measure. It says nothing about a nonuniform selector or a different collision alphabet.
- Absolute values erase the character-sign convention, but the complex identity itself depends on the explicit convention fixed above.

## Adversarial tests

For `K=1`, `d ≡ 1 (mod 64)`, so

\[
R_1=\{0,1\},\qquad
\widehat\mu(\theta/64)
 =\frac{1+e^{2\pi i\theta/64}}2.
\]

For `theta=0`, both sides equal `1` for every `K`.

For `theta=64^j theta'`, the last displayed identity reproduces the exact depth reduction directly, including frequencies divisible by large powers of `64`.

## Remaining uncertainty

The proof is complete-looking. The highest-risk review point is the positive-sign convention for `{x}_2`; if the repository adopts the conjugate standard character, the complex identity is conjugated while every absolute-value consequence remains unchanged.

## Suggested next attack

Verify `L-9302` independently, then combine it with the frequency-block mean from issue #4. The objective is to remove the entire high-frequency range before attempting any pointwise cusp theorem.
