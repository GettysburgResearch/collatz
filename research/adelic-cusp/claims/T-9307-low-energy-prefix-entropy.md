# T-9307 — Low-energy prefix entropy bound

**Claim ID:** T-9307  
**Title:** Reciprocal phase prefixes with anomalously small quadratic energy occupy a power-small fraction of every frequency interval  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `L-9309`; elementary exponential moments and the cosine-energy inequality of `L-9303`  
**Scope:** uniform approximate-cylinder counting for the all-depth inverse program  
**Related counterexample candidates:** none

## Statement

Fix integers

\[
K\ge L\ge1.
\]

For each integer `h`, use the reciprocal phases from `L-9309` and put

\[
y_\ell(h)=
\frac{q_\ell(h)}{81^{\ell+1}},
\qquad
0\le\ell<L,
\tag{1}
\]

with circle distance

\[
\|y\|=
\operatorname{dist}(y,\mathbb Z).
\]

Define the length-`L` prefix energy

\[
\mathcal E_{K,L}(h)
=
\sum_{\ell=0}^{L-1}
\|y_\ell(h)\|^2.
\tag{2}
\]

Put

\[
\boxed{
\beta=
\frac{17\sqrt2}{27}
<1,
}
\tag{3}
\]

and

\[
\boxed{
\eta=-\log_{81}\beta>0.
}
\tag{4}
\]

Numerically,

\[
\beta\approx0.8905,
\qquad
\eta\approx0.0264.
\]

### Complete-block bound

For every interval `I` of exactly `81^L` consecutive integers,

\[
\boxed{
\#\left\{
h\in I:
\mathcal E_{K,L}(h)
\le\frac L{64}
\right\}
\le
81^L\beta^L.
}
\tag{5}
\]

Equivalently, low-energy length-`L` prefixes occupy at most a `beta^L` fraction of every complete `81^L` frequency block.

### Arbitrary-interval corollary

Let `I` be any interval of `H>=81` consecutive integers and put

\[
L=\lfloor\log_{81}H\rfloor.
\tag{6}
\]

Then

\[
\boxed{
\#\left\{
h\in I:
\mathcal E_{K,L}(h)
\le\frac L{64}
\right\}
\le
C_*H^{1-\eta},
}
\tag{7}
\]

where one valid absolute constant is

\[
C_*=82\cdot81^\eta.
\tag{8}
\]

### Fourier corollary for the triadic mirror

For all frequencies outside the exceptional set in `(7)`,

\[
\boxed{
\left|
\widehat\nu\!\left(\frac h{81^K}\right)
\right|
\le
\exp(-L/32).
}
\tag{9}
\]

Thus, in every interval of length `H`, all but `O(H^(1-eta))` frequencies have at least a fixed power of `H` decay in the triadic mirror coefficient:

\[
\exp(-L/32)
\le
C'H^{-1/(32\log81)}
\tag{10}
\]

for an absolute constant `C'`.

By `T-9305` and `T-9306`, the same conclusion transfers to the dyadic survivor and every CRT split up to their explicit `O(|h|/64^K)` coefficient errors.

## Definitions

The prefix energy uses the **unshifted reciprocal phases**. It is exactly the quadratic energy of the first `L` factors of the triadic mirror product.

The theorem is uniform in the ambient depth `K`: only the unit twist `64^(-K)` changes, and `L-9309` proves that the lift-prefix map remains a bijection for every fixed `K`.

The logarithms in `(4)`, `(6)`, and `(10)` are natural unless the base is displayed.

## Motivation

`R-9301` shows that one exact prefix is too sparse to create a consecutive exceptional block. The next question is whether a low-energy **union** of exact prefixes can be large.

`T-9307` gives the first quantitative answer. Low-energy prefixes lose an explicit exponential factor per level in every complete block. This is a self-contained energy version of the average-contraction philosophy, derived directly from the lift-digit bijection.

The result does not prove the maximal all-depth theorem: a power-small exceptional set can still contain the first few or harmonically most expensive frequencies. It does prove that any obstruction is combinatorially sparse at every scale and gives a concrete entropy budget for the next inverse theorem.

## Proof

### Step 1: a uniform one-level exponential-moment bound

For real `phi`, consider the shifted `81`-point grid

\[
\left\{
\frac{j+\phi}{81}\pmod1:
0\le j<81
\right\}.
\]

The set

\[
\{x\in\mathbb R/\mathbb Z:\|x\|<1/4\}
\]

is an arc of length `1/2`. An arc of length `1/2` contains at most `41` points of an equally spaced `81`-point grid. Therefore at least `40` grid points satisfy

\[
\|x\|\ge1/4.
\]

For every `s>0`,

\[
\frac1{81}
\sum_{j=0}^{80}
\exp\!\left(
-s\left\|
\frac{j+\phi}{81}
\right\|^2
\right)
\le
\frac{41}{81}
+
\frac{40}{81}e^{-s/16}.
\tag{11}
\]

Choose

\[
s=16\log4.
\tag{12}
\]

Then

\[
e^{-s/16}=1/4,
\]

so the right side of `(11)` is

\[
\boxed{
\kappa=
\frac{41+10}{81}
=
\frac{17}{27}.
}
\tag{13}
\]

### Step 2: iterate through the lift-digit bijection

Let `h` be uniform on any interval of `81^L` consecutive integers. Such an interval is a complete residue system modulo `81^L`.

By `L-9309`, the tuple

\[
(q_0,d_0,\ldots,d_{L-2})
\]

is uniform on

\[
(\mathbb Z/81\mathbb Z)^L.
\]

Equivalently, `q_0` is uniform modulo `81`, and at each later level the lift digit `d_ell` is conditionally uniform on `{0,...,80}`.

The normalized recurrence is

\[
y_{\ell+1}
=
\frac{\{64y_\ell\}+d_\ell}{81}.
\]

Conditioned on the history, equation `(11)` applies with a shift determined by `y_ell`. Iterating conditional expectations gives

\[
\boxed{
\mathbb E
\exp\!\left(
-s\mathcal E_{K,L}(h)
\right)
\le
\kappa^L.
}
\tag{14}
\]

### Step 3: low-energy large deviation

If

\[
\mathcal E_{K,L}(h)
\le L/64,
\]

then

\[
\exp(-s\mathcal E_{K,L}(h))
\ge
\exp(-sL/64).
\]

Markov's inequality applied to the nonnegative random variable

\[
\exp(-s\mathcal E_{K,L})
\]

gives

\[
\begin{aligned}
\mathbb P\left(
\mathcal E_{K,L}
\le L/64
\right)
&\le
\exp(sL/64)
\mathbb E e^{-s\mathcal E_{K,L}}\\
&\le
\left(
\exp(s/64)\kappa
\right)^L.
\end{aligned}
\tag{15}
\]

Using `(12)` and `(13)`,

\[
\exp(s/64)
=
\exp((\log4)/4)
=
\sqrt2,
\]

so

\[
\exp(s/64)\kappa
=
\frac{17\sqrt2}{27}
=
\beta.
\]

Multiplying the probability bound by `81^L` proves `(5)`.

### Step 4: arbitrary intervals

Let `L` be `(6)`. Then

\[
81^L\le H<81^{L+1}.
\]

Partition `I` into at most `81` complete blocks of length `81^L` and one final remainder. The remainder is contained in another interval of length `81^L`. Applying `(5)` to each gives

\[
\#\{\text{low energy in }I\}
\le
82\cdot81^L\beta^L.
\tag{16}
\]

Since

\[
\beta^L=(81^L)^{-\eta}
\]

and

\[
81^L>H/81,
\]

we have

\[
81^L\beta^L
=(81^L)^{1-\eta}
\le
81^\eta H^{1-\eta}.
\]

This proves `(7)` and `(8)`.

### Step 5: Fourier decay outside the exceptional set

By `L-9305`, the triadic coefficient is a product of cosine factors with phase distances `||y_ell||`. The elementary inequality from `L-9303`,

\[
|\cos(\pi x)|
\le
\exp(-2\|x\|^2),
\]

gives

\[
\left|
\widehat\nu(h/81^K)
\right|
\le
\exp\!\left(
-2\mathcal E_{K,L}(h)
\right),
\]

after discarding all factors beyond level `L-1`.

Outside the exceptional set,

\[
\mathcal E_{K,L}(h)>L/64,
\]

so `(9)` follows. Equation `(10)` is the consequence of `(6)`. QED.

## Dependency audit

- `L-9309` supplies exact conditional uniformity of the lift digits in every complete block.
- The one-level estimate `(11)` is proved in this file.
- `L-9303` supplies the cosine-energy inequality used only for the Fourier corollary.
- `T-9305` and `T-9306` provide optional transfer to other representations.
- No branch-qualified frequency theorem, computation, or external large-deviation theorem is used.

## Gap audit

- A power-small exceptional set may still contain all very small frequencies, so `(7)` does not prove the harmonic EQ sum tends to zero.
- The constants are deliberately crude; optimizing them does not resolve the maximal obstruction.
- The theorem controls the first `L` reciprocal phases, not arbitrary scattered subsets of levels.
- Uniformity holds on complete residue blocks; arbitrary intervals are handled by covering, which loses only a constant.
- The result gives no pointwise theorem for every frequency.
- No conclusion about the M1 integer-section problem follows.

## Adversarial tests

1. At `L=1`, the statement is a direct count over the `81` possible values of `q_0`.
2. The bound is invariant under the period-9 unit twist `64^(-K) mod81^L` because that twist only permutes the lift tuples.
3. Frequencies divisible by `81` contribute some zero initial phases, but form correspondingly sparse prefix classes and are included in the entropy count.
4. If `H=81^L`, the arbitrary-interval argument reduces to the complete-block theorem.
5. The exceptional-count estimate can exceed `1` for tiny `L`; it remains a valid upper bound.

## Remaining uncertainty

The proof is complete-looking. Independent review should check the `41/40` grid split, the conditional-independence interpretation of `L-9309`, and the direction of Markov's inequality in `(15)`.

## Suggested next attack

Stratify the low-energy prefixes by their earliest nondegenerate level and by `81`-adic valuation. The objective is to prove that the power-small exceptional residue classes cannot all cluster near the smallest positive frequencies. A harmonic-location theorem of that type, combined with `(7)`, would be a genuine route from almost-all polynomial-window decay to the full weighted criterion.