# T-9308 — Uniform harmonic tail from prefix entropy

**Claim ID:** T-9308  
**Title:** The weighted Fourier mass above any growing cutoff decays uniformly at every depth without a frequency-block hypothesis  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `T-9307`, `T-9305`; elementary geometric shell summation  
**Scope:** unconditional high-frequency tail for the all-depth EQ criterion  
**Related counterexample candidates:** none

## Statement

Let

\[
F^{(2)}_K(h)=rac{|S_K(h)|}{2^K},
\qquad
F^{(3)}_K(h)=
\left|
\widehat\nu\!\left(\frac h{81^K}\right)
\right|.
\tag{1}
\]

Use the constants from `T-9307`:

\[
\beta=rac{17\sqrt2}{27},
\qquad
\eta=-\log_{81}\beta>0.
\tag{2}
\]

Put

\[
\gamma=rac1{32\log81},
\qquad
\delta=\min\{\eta,\gamma\}>0.
\tag{3}
\]

Numerically,

\[
\eta\approx0.0264,
\qquad
\gamma\approx0.00711,
\qquad
\delta=\gamma.
\]

Then there is an absolute constant `C_tail` such that, for every `K>=1` and every integer cutoff

\[
81\le M\le2^K,
\]

one has

\[
\boxed{
\sum_{M\le h\le2^K}
\frac{F^{(3)}_K(h)}h
\le
C_{\rm tail}M^{-\delta}.
}
\tag{4}
\]

For the original survivor coefficients,

\[
\boxed{
\sum_{M\le h\le2^K}
\frac{F^{(2)}_K(h)}h
\le
C_{\rm tail}M^{-\delta}
+
\pi2^{-5K}.
}
\tag{5}
\]

The estimate is uniform in `K`; no frequency-block mean, depth average, external Fourier theorem, or computation is assumed.

### Self-contained all-depth reduction

Let `M_K` be any integer sequence satisfying

\[
M_K\longrightarrow\infty,
\qquad
81\le M_K\le2^K.
\tag{6}
\]

Then

\[
\boxed{
E_K
=
\sum_{1\le h\le2^K}
\frac{F^{(2)}_K(h)}h
\le
\sum_{1\le h<M_K}
\frac{F^{(2)}_K(h)}h
+
C_{\rm tail}M_K^{-\delta}
+
\pi2^{-5K}.
}
\tag{7}
\]

Consequently, full all-depth EQ follows from **any** proof that the weighted low-frequency sum below one growing cutoff tends to zero.

A sufficient maximal condition is

\[
\max_{1\le h<M_K}F^{(2)}_K(h)
=
\varepsilon_K
\]

with

\[
\boxed{
\varepsilon_K\log M_K\longrightarrow0.
}
\tag{8}
\]

In particular, polynomial decay on a polynomial window proves all-depth EQ **without** importing issue #4's frequency-block theorem.

## Definitions

The cutoff tail in `(4)` begins at `M`. If `M>2^K`, the sum is empty and the claim is trivial.

The constant `gamma` is the Fourier-decay exponent supplied outside the low-energy exceptional prefixes in `T-9307`:

\[
e^{-L/32}
\asymp
H^{-\gamma}
\]

when

\[
L\asymp\log_{81}H.
\]

The exponent `delta` is the smaller of:

- the entropy saving `eta` in the number of exceptional frequencies;
- the pointwise decay exponent `gamma` outside that set.

## Motivation

`L-9302` previously removed the high-frequency tail by assuming the branch-qualified arbitrary-block mean from issue #4. `T-9307` provides a different input: every interval has a power-saving count of low-energy frequencies, and every other frequency has a power-saving coefficient bound.

On a shell `[X,2X)`, harmonic weights convert both savings directly into

\[
O(X^{-\eta})+O(X^{-\gamma}).
\]

These bounds are summable over dyadic shells. The resulting tail theorem is self-contained and uniform in depth.

This materially changes the proof frontier. The only all-depth obstruction lies in a growing set of the **smallest** frequencies; the exponential range no longer requires an external average theorem.

## Proof

### Step 1: one dyadic shell for the triadic mirror

Fix a real `X>=81` and let

\[
I_X=
\{h\in\mathbb Z:X\le h<2X\}.
\]

Its cardinality is at most `X+1`; enlarging by an absolute constant has no effect below. Apply `T-9307` to an interval of length comparable with `X`, with

\[
L=\lfloor\log_{81}X\rfloor.
\]

The exceptional set

\[
\mathcal B_X=
\left\{
h\in I_X:
\mathcal E_{K,L}(h)
\le L/64
\right\}
\]

has size

\[
|\mathcal B_X|
\le
C_*X^{1-\eta}.
\tag{9}
\]

Every exceptional coefficient is at most `1`. Since `h>=X`, its total weighted contribution is at most

\[
\sum_{h\in\mathcal B_X}
\frac{F^{(3)}_K(h)}h
\le
C_*X^{-\eta}.
\tag{10}
\]

For every nonexceptional `h`, `T-9307(9)` gives

\[
F^{(3)}_K(h)
\le
\exp(-L/32).
\]

Because

\[
L\ge
\frac{\log X}{\log81}-1,
\]

we have

\[
\exp(-L/32)
\le
\exp(1/32)X^{-\gamma}.
\tag{11}
\]

There are at most `X+1` such frequencies and each harmonic weight is at most `1/X`, so

\[
\sum_{h\in I_X\setminus\mathcal B_X}
\frac{F^{(3)}_K(h)}h
\le
C_1X^{-\gamma}
\tag{12}
\]

for an absolute `C_1`.

Combining `(10)` and `(12)`,

\[
\boxed{
\sum_{X\le h<2X}
\frac{F^{(3)}_K(h)}h
\le
C_2
\left(
X^{-\eta}+X^{-\gamma}
\right)
\le
2C_2X^{-\delta}.
}
\tag{13}
\]

The bound is uniform in `K` whenever the shell is contained in `h<=2^K`. The prefix length satisfies `L<K` automatically because

\[
\log_{81}(2^K)<K.
\]

### Step 2: sum the shells

Cover

\[
[M,2^K]
\]

by dyadic shells with left endpoints

\[
X_r=2^rM,
\qquad
r\ge0,
\]

stopping at the final nonempty shell. Equation `(13)` gives

\[
\begin{aligned}
\sum_{M\le h\le2^K}
\frac{F^{(3)}_K(h)}h
&\le
2C_2
\sum_{r\ge0}
(2^rM)^{-\delta}\\
&=
\frac{2C_2}{1-2^{-\delta}}
M^{-\delta}.
\end{aligned}
\]

This proves `(4)` with

\[
C_{\rm tail}
=
\frac{2C_2}{1-2^{-\delta}}.
\]

### Step 3: transfer to the survivor product

`T-9305(4)` gives

\[
\left|
F^{(2)}_K(h)-F^{(3)}_K(h)
\right|
\le
\frac{\pi h}{64^K}.
\]

After dividing by `h` and summing over at most `2^K` frequencies,

\[
\sum_{h=1}^{2^K}
\frac{
|F^{(2)}_K(h)-F^{(3)}_K(h)|
}{h}
\le
\frac{\pi2^K}{64^K}
=
\pi2^{-5K}.
\tag{14}
\]

Combining `(4)` and `(14)` proves `(5)`.

### Step 4: low/high reduction

Split `E_K` at `M_K`. Equation `(5)` gives `(7)`.

If the low-frequency maximum is `epsilon_K`, then

\[
\sum_{1\le h<M_K}
\frac{F^{(2)}_K(h)}h
\le
\varepsilon_K
\left(1+\log M_K\right).
\]

Condition `(8)` makes this vanish, while `(6)` makes the two tail errors vanish. QED.

## Dependency audit

- `T-9307` supplies the exceptional count and nonexceptional pointwise decay on every interval.
- `T-9305` transfers the tail from the triadic mirror to the survivor product.
- All remaining steps are elementary harmonic and geometric shell estimates.
- No branch-qualified frequency-block theorem is used.
- No computation or external result is used.

## Gap audit

- The theorem still leaves a growing low-frequency window.
- A sparse exceptional set can contain the smallest frequencies, so count bounds alone do not close the low part.
- The exponent `delta` is crude and small; its positivity, not optimization, is the structural result.
- The transfer error is negligible only because the EQ range is far below `64^K`.
- No pointwise all-frequency decay follows.
- The M1 integer-section question remains independent.

## Adversarial tests

1. If `M=81`, the estimate is finite but the constant may be crude.
2. If `M=2^K`, the tail contains one frequency and the theorem remains valid.
3. The dyadic-shell sum converges because `delta>0`; without the entropy saving or pointwise saving it would diverge.
4. A hypothetical exceptional frequency `h=1` is not controlled by the tail theorem, exactly matching the remaining obstruction.
5. At `H=2^K`, the survivor/mirror transfer error is exactly of scale `2^(-5K)`.

## Remaining uncertainty

The proof is complete-looking. Independent review should check the passage from `T-9307`'s arbitrary-interval statement to `(9)`, and the uniformity condition `L<=K` on the largest shell.

## Suggested next attack

Combine this tail theorem with `T-9303`'s valuation-stratified depth averages. That removes the final branch-qualified frequency-block dependency and yields a completely self-contained density-one full-EQ theorem in `T-9309`.