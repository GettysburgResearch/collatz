# T-9307 — Low-energy prefix entropy bound

**Claim ID:** T-9307  
**Title:** Reciprocal phase prefixes with anomalously small quadratic energy occupy a power-small fraction of every frequency interval  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `L-9309`; elementary exponential moments; `L-9303` for the Fourier corollary  
**Scope:** uniform approximate-cylinder counting for the all-depth inverse program  
**Related counterexample candidates:** none

## Statement

Fix integers

\[
K\ge L\ge1.
\]

For every integer `h`, use the reciprocal phases from `L-9309` and put

\[
y_\ell(h)=
\frac{q_\ell(h)}{81^{\ell+1}},
\qquad
0\le\ell<L,
\]

where circle distance is

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
\tag{1}
\]

Put

\[
\boxed{
\beta=
\frac{17\sqrt2}{27}<1,
}
\tag{2}
\]

and

\[
\boxed{
\eta=-\log_{81}\beta>0.
}
\tag{3}
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
\tag{4}
\]

Equivalently, low-energy length-`L` prefixes occupy at most a `beta^L` fraction of every complete `81^L` frequency block.

### Arbitrary-interval corollary

Let `I` be any interval of `H>=81` consecutive integers and set

\[
L=\lfloor\log_{81}H\rfloor.
\tag{5}
\]

Assume `L<=K`. Then

\[
\boxed{
\#\left\{
h\in I:
\mathcal E_{K,L}(h)
\le\frac L{64}
\right\}
\le
81H^{1-\eta}.
}
\tag{6}
\]

### Fourier corollary for the triadic mirror

For every frequency outside the exceptional set in `(6)`,

\[
\boxed{
\left|
\widehat\nu\!\left(\frac h{81^K}\right)
\right|
\le
\exp(-L/32).
}
\tag{7}
\]

Hence, for an absolute constant `C`, all but `O(H^(1-eta))` frequencies in an interval of length `H` satisfy

\[
\left|
\widehat\nu\!\left(\frac h{81^K}\right)
\right|
\le
CH^{-1/(32\log81)}.
\tag{8}
\]

By `T-9305` and `T-9306`, analogous estimates transfer to the dyadic survivor and every CRT split with their explicit `O(|h|/64^K)` comparison errors.

## Definitions

The prefix energy uses the **unshifted reciprocal phases**. It is exactly the quadratic energy of the first `L` factors of the triadic mirror product.

The theorem is uniform in the ambient depth `K`: the unit twist `64^(-K)` only permutes the lift-prefix tuples, by `L-9309`.

All logarithms are natural unless a base is displayed.

## Motivation

`R-9301` shows that one exact prefix is too sparse to create a consecutive exceptional block. The next question is whether the **union** of low-energy exact prefixes can be large.

This theorem gives a quantitative answer. Low-energy prefixes lose a fixed exponential factor per level in every complete residue block. The result does not yet prove all-depth EQ, because a power-small exceptional set may still contain the harmonically most expensive small frequencies. It does give a uniform entropy budget for the remaining inverse problem.

## Proof

### Step 1: one-level exponential-moment bound

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

is an arc of length `1/2`. Such an arc contains at most `41` points of an equally spaced `81`-point grid. Therefore at least `40` grid points satisfy

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
\tag{9}
\]

Choose

\[
s=16\log4.
\tag{10}
\]

Then `e^(-s/16)=1/4`, so the right side of `(9)` is

\[
\boxed{
\kappa=
\frac{41+10}{81}
=
\frac{17}{27}.
}
\tag{11}
\]

### Step 2: iterate through the lift-digit bijection

Let `h` be uniform on any interval of `81^L` consecutive integers. This is a complete residue system modulo `81^L`.

By `L-9309`, the tuple

\[
(q_0,d_0,\ldots,d_{L-2})
\]

is uniform on

\[
(\mathbb Z/81\mathbb Z)^L.
\]

Equivalently, `q_0` is uniform modulo `81`, and each later lift digit is conditionally uniform on `{0,...,80}`.

The normalized recurrence is

\[
y_{\ell+1}
=
\frac{\{64y_\ell\}+d_\ell}{81}.
\tag{12}
\]

Conditioned on the preceding lift data, `(9)` applies with a shift determined by `y_ell`. Iterating conditional expectations gives

\[
\boxed{
\mathbb E
\exp\!\left(
-s\mathcal E_{K,L}(h)
\right)
\le
\kappa^L.
}
\tag{13}
\]

### Step 3: low-energy large deviation

On the event

\[
\mathcal E_{K,L}(h)
\le L/64,
\]

we have

\[
\exp(-s\mathcal E_{K,L}(h))
\ge
\exp(-sL/64).
\]

Markov's inequality therefore gives

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
\tag{14}
\]

Using `(10)` and `(11)`,

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

Multiplying the probability bound by `81^L` proves `(4)`.

### Step 4: arbitrary intervals

Let `L` be `(5)` and put

\[
B=81^L.
\]

Then

\[
B\le H<81B.
\]

Partition `I` into at most `80` complete blocks of length `B` and one remainder. Enlarge the remainder, if nonempty, to an interval of exactly `B` consecutive integers. Applying `(4)` to every block gives

\[
\#\{\text{low energy frequencies in }I\}
\le
81B\beta^L.
\tag{15}
\]

Since

\[
\beta^L=B^{-\eta},
\]

we have

\[
B\beta^L=B^{1-\eta}.
\]

Also `0<eta<1` and `B<=H`, so

\[
B^{1-\eta}
\le
H^{1-\eta}.
\]

Substitution into `(15)` proves `(6)`.

### Step 5: Fourier decay outside the exceptional set

By `L-9305`, the triadic coefficient is a product of cosine factors with phase distances `||y_ell||`. The elementary inequality from `L-9303`,

\[
|\cos(\pi x)|
\le
\exp(-2\|x\|^2),
\]

gives, after discarding all factors beyond level `L-1`,

\[
\left|
\widehat\nu(h/81^K)
\right|
\le
\exp\!\left(
-2\mathcal E_{K,L}(h)
\right).
\]

Outside the exceptional set,

\[
\mathcal E_{K,L}(h)>L/64,
\]

which proves `(7)`.

Finally,

\[
L\ge
\frac{\log H}{\log81}-1,
\]

so `(8)` follows after multiplying by the absolute factor `e^(1/32)`. QED.

## Dependency audit

- `L-9309` supplies exact conditional uniformity of the lift digits on complete residue blocks.
- The one-level estimate `(9)` is proved here.
- `L-9303` supplies the cosine-energy inequality used only for the Fourier corollary.
- No branch-qualified frequency theorem, computation, or external large-deviation theorem is used.

## Gap audit

- A power-small exceptional set may still contain the smallest frequencies, so the theorem alone does not prove the harmonic EQ sum tends to zero.
- The constants are deliberately crude; their positivity, not optimization, is the structural point.
- The theorem controls the first `L` reciprocal phases, not arbitrary scattered subsets of levels.
- The result is a count theorem, not a harmonic-location theorem.
- No conclusion about the M1 integer-section problem follows.

## Adversarial tests

1. At `L=1`, the theorem is a direct count over the `81` values of `q_0`.
2. The period-9 unit twist `64^(-K)` only permutes the lift tuples.
3. Frequencies divisible by `81` create zero initial phases but occupy correspondingly sparse residue classes.
4. If `H=81^L`, the arbitrary-interval proof reduces to the complete-block theorem.
5. The exceptional-count bound may be numerically crude for small `L`; it remains valid.

## Remaining uncertainty

The proof is complete-looking. Independent review should check the `41/40` grid split, the conditional-expectation iteration, the direction of Markov's inequality, and the corrected monotonicity step in the arbitrary-interval argument.

## Suggested next attack

Stratify the low-energy prefixes by valuation, first nondegenerate level, and terminal residue. The goal is a harmonic-location theorem showing that the power-small exceptional residue classes cannot all have unusually small least positive representatives.