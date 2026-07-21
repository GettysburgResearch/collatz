# Adelic cusp Fourier program

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Branch:** `agent/gpt56-pro-04/15-adelic-cusp-fourier`  
**Date:** 2026-07-21  
**Packet status:** theory-first independent attempt; no counterexample claimed

## Executive thesis

The depth-dependent Fourier products in the active `64 -> 81` survivor program come from one fixed Bernoulli self-similar measure on `Z_2`. The issue-#4 Cantor-class products similarly come from one fixed Bernoulli self-similar measure on `Z_3`.

On the room-relevant CRT orbit, the two local systems are not independent. They are local components of one rational character

\[
r=\frac h{64^n81^j},
\]

and their factors stitch one reciprocal phase chain. Every CRT split is therefore asymptotically equivalent to the original survivor coefficient—both in absolute value and against arbitrary bounded harmonic tests—in every range `H=o(64^K)`.

The decisive additional observation is combinatorial. Exact prefixes of the reciprocal lift chain are in bijection with residue classes modulo powers of `81`. This yields an explicit exponential-moment bound for low-energy prefixes. From that entropy deficit one obtains:

1. a power-saving count of exceptional frequencies in every interval;
2. an unconditional uniform harmonic high-frequency tail at every depth;
3. a completely self-contained proof that the full weighted EQ criterion holds on a natural-density-one set of depths.

The remaining all-depth obstruction is now confined to a growing collection of the smallest frequencies and to a zero-density exceptional set of depths.

No result here decides whether one exceptional infinite ordinary integer lies in the survivor attractor. That direct M1 question remains a separate integer-section problem.

## Fixed local measures

Set

\[
\rho=\frac{64}{81},
\qquad
d=\frac{17}{81}.
\]

For `epsilon in {0,1}^N`, define

\[
\pi_2(\varepsilon)
=
\sum_{t\ge0}d\varepsilon_t\rho^t
\in\mathbb Z_2,
\]

and let `mu` be the fair Bernoulli pushforward.

For the triadic mirror put

\[
\lambda=\frac{81}{64},
\qquad
c=-\frac{17}{64},
\]

and define

\[
\pi_3(\eta)
=
\sum_{r\ge0}c\eta_r\lambda^r
\in\mathbb Z_3,
\]

with fair Bernoulli pushforward `nu`.

For the depth-`K` survivor set `R_K`, put

\[
S_K(h)
=
\sum_{A\in R_K}
\exp\!\left(2\pi i\frac{hA}{64^K}\right),
\qquad
F_K(h)=\frac{|S_K(h)|}{2^K}.
\]

The all-depth EQ target is

\[
E_K
=
\sum_{1\le h\le2^K}
\frac{F_K(h)}h
\longrightarrow0.
\]

## Active claim map

| ID | Status | Content |
|---|---|---|
| `D-9301` | `PROPOSED` | Fixed self-similar survivor measure on `Z_2` |
| `D-9302` | `PROPOSED` | `{2,3,infinity}`-solenoid natural extension and integer section |
| `D-9303` | `PROPOSED` | Fixed triadic mirror measure whose reductions are `C_j` |
| `L-9301` | `PROPOSED` | `mu-hat(h/64^K)=2^{-K}S_K(h)` |
| `L-9302` | `PROPOSED` | Conditional shell tail from an arbitrary-block mean |
| `L-9303` | `PROPOSED` | Squared phase energy controls the survivor product |
| `L-9304` | `PROPOSED` | Exact `64`/`81` phase reciprocity and valuation loss |
| `L-9305` | `PROPOSED` | `nu-hat(h/81^j)=2^{-j}C_j-hat(h)` |
| `L-9306` | `PROPOSED` | Complete-group absolute Fourier moments factor |
| `L-9307` | `PROPOSED` | Global rational diagonal and absolute phase stitching |
| `L-9308` | `PROPOSED` | Complex bilateral phase stitching |
| `L-9309` | `PROPOSED` | Lift-digit prefixes biject with residues modulo `81^L` |
| `T-9301` | `SUPERSEDED` | Earlier conditional polynomial-window reduction |
| `T-9302` | `SUPERSEDED` | Earlier conditional density-one synthesis |
| `T-9303` | `PROPOSED` | Valuation-stratified complete depth-period decay |
| `T-9304` | `PROPOSED` | Exact two-place CRT transform factorization |
| `T-9305` | `PROPOSED` | Absolute split collapse and weighted equivalence |
| `T-9306` | `PROPOSED` | Complex coefficient and bounded-test equivalence |
| `T-9307` | `PROPOSED` | Low-energy lift prefixes have an explicit entropy deficit |
| `T-9308` | `PROPOSED` | Uniform harmonic high-frequency tail at every depth |
| `T-9309` | `PROPOSED` | Unconditional full weighted EQ on density-one depths |
| `R-9301` | `PROPOSED` | Exact prefixes do not amplify to consecutive intervals |
| `C-9301` | `IDEA` | All-depth logarithmic energy / low-frequency theorem |
| `Q-9301` | `IDEA` | Nontrivial ordinary-integer section intersection |
| `Q-9302` | `IDEA` | Better proof mechanism after split-target equivalence |
| `O-9301` / `X-9301` | `EMPIRICAL` | Exact bounded scattering census through `K=80`, `h<=K^2` |

Every complete-looking argument remains `PROPOSED` pending independent review. `SUPERSEDED` means replaced by a stronger theorem, not refuted.

## 1. Survivor stationarization

`D-9301` and `L-9301` give

\[
\boxed{
\widehat\mu(h/64^K)=2^{-K}S_K(h).
}
\]

Thus the changing finite products are one fixed transform sampled along a rational cusp.

The self-similar measure alone does not supply Fourier decay. The hard question is uniform behavior along characters whose real height shrinks while their `2`-adic height grows.

## 2. Exact reciprocal phase chain

For

\[
0\le\ell<K,
\]

put

\[
M_\ell=64^{K-\ell},
\qquad
N_\ell=81^{\ell+1},
\]

and define

\[
q_\ell(h)
\equiv
-17hM_\ell^{-1}
\pmod{N_\ell},
\qquad
0\le q_\ell<N_\ell.
\]

Write

\[
y_\ell(h)=\frac{q_\ell(h)}{N_\ell}.
\]

Universal circle reciprocity gives the dyadic phase as

\[
y_\ell(h)
+
\frac{17h}{M_\ell N_\ell}
\pmod1.
\]

This is the exact bridge between the original power-of-`64` phases and reciprocal residues modulo powers of `81`.

## 3. Valuation-stratified depth averaging

The reciprocal phase vector has period

\[
P_m=9\cdot81^m
\]

in depth. Multiplication by a frequency divisible by `3` collapses initial phase grids, so a uniform first-factor proof is invalid.

`T-9303` corrects this exactly. For

\[
e(h)=\left\lceil\frac{v_3(h)}4\right\rceil,
\]

every complete depth period beginning at `K_0` satisfies

\[
\boxed{
\frac1{P_m}
\sum_{K\in J}F_K(h)
\le
2^{-\frac12\max\{0,m+1-e(h)\}}
+
\frac{\pi h}{64^{K_0}}.
}
\]

The loss is summable over a growing frequency window because one lost contraction costs frequency density approximately `1/81`, while recovering the contraction gains only `sqrt(2)`.

## 4. Triadic mirror and two-place CRT factorization

The admissible Cantor classes are finite reductions of `nu`, and

\[
\boxed{
\widehat\nu(h/81^j)=2^{-j}\widehat C_j(h).
}
\]

For

\[
Q=64^n81^j,
\qquad
u=(81^j)^{-1}\pmod{64^n},
\qquad
v=(64^n)^{-1}\pmod{81^j},
\]

the normalized CRT-product coefficient is

\[
\boxed{
G_{n,j}(h)
=
\widehat\mu(hu/64^n)
\widehat\nu(hv/81^j).
}
\]

Every absolute Fourier moment over the complete dual group factors. In particular,

\[
\frac1Q
\sum_{h\bmod Q}|G_{n,j}(h)|^2
=
2^{-(n+j)}.
\]

This complete-group decorrelation does not control a short initial frequency interval, which traces a thin rational diagonal.

## 5. Global rational diagonal and split collapse

The CRT local characters are the local representations of one rational:

\[
\frac{hu}{64^n}
\equiv
\frac hQ
\pmod{\mathbb Z_2},
\qquad
\frac{hv}{81^j}
\equiv
\frac hQ
\pmod{\mathbb Z_3}.
\]

For `K=n+j`, the triadic factor supplies the low indices of the reciprocal phase chain and the dyadic factor supplies the high indices. This holds before taking absolute values.

Quantitatively,

\[
\boxed{
\left|
G_{n,j}(h)
-
\widehat\mu(h/64^K)
\right|
<
\frac{2\pi|h|}{64^K}.
}
\]

For any bounded complex weights `|w_h|<=1`,

\[
\boxed{
\left|
\sum_{h\le H}\frac{w_h}{h}G_{n,j}(h)
-
\sum_{h\le H}
\frac{w_h}{h}
\widehat\mu(h/64^K)
\right|
<
\frac{2\pi H}{64^K}.
}
\]

At the EQ cutoff `H=2^K`, the error is below

\[
2\pi2^{-5K}.
\]

Therefore a two-place or room Fourier proof automatically proves the corresponding original survivor statement. The representation may still provide a better proof mechanism, but not a weaker target.

## 6. Lift-digit cylinders

Define

\[
d_\ell(h)
=
\left\lfloor
\frac{q_{\ell+1}(h)}{81^{\ell+1}}
\right\rfloor
\in\{0,\ldots,80\}.
\]

The exact recurrence is

\[
q_{\ell+1}
=
\left(64q_\ell\bmod81^{\ell+1}\right)
+
d_\ell81^{\ell+1},
\]

or, in normalized form,

\[
\boxed{
y_{\ell+1}
=
\frac{\{64y_\ell\}+d_\ell}{81}.
}
\]

`L-9309` proves that

\[
h\pmod{81^L}
\longleftrightarrow
(q_0,d_0,\ldots,d_{L-2})
\]

is a bijection. Thus fixing one exact length-`L` prefix gives exactly one residue class modulo `81^L`.

`R-9301` consequently refutes the naive claim that one exact prefix persists on a consecutive frequency neighborhood. The correct amplification problem concerns **unions of approximate cylinders**, not one exact cylinder.

## 7. Prefix entropy theorem

Define the length-`L` reciprocal energy

\[
\mathcal E_{K,L}(h)
=
\sum_{\ell=0}^{L-1}
\|y_\ell(h)\|^2.
\]

Put

\[
\beta=\frac{17\sqrt2}{27}<1,
\qquad
\eta=-\log_{81}\beta>0.
\]

`T-9307` proves that every interval of exactly `81^L` consecutive frequencies contains at most

\[
\boxed{81^L\beta^L}
\]

frequencies satisfying

\[
\mathcal E_{K,L}(h)
\le
L/64.
\]

For an arbitrary interval of length `H`, with `L=floor(log_81 H)`, the exceptional count is

\[
O(H^{1-\eta}).
\]

Every nonexceptional frequency has

\[
\left|
\widehat\nu(h/81^K)
\right|
\le
\exp(-L/32),
\]

a fixed power saving in `H`.

The proof is self-contained: the lift digits are exactly uniform on complete blocks, and every shifted `81`-point phase grid has a fixed positive fraction of points at distance at least `1/4` from an integer.

## 8. Uniform harmonic high-frequency tail

Put

\[
\gamma=\frac1{32\log81},
\qquad
\delta=\min\{\eta,\gamma\}>0.
\]

`T-9308` shells frequency intervals dyadically. The power-small exceptional count contributes `O(X^-eta)` on a shell `[X,2X)`, while the nonexceptional coefficient decay contributes `O(X^-gamma)`.

Therefore, uniformly in every depth,

\[
\boxed{
\sum_{M\le h\le2^K}
\frac{F_K(h)}h
\le
C_{\rm tail}M^{-\delta}
+
\pi2^{-5K}.
}
\]

This theorem removes the entire high-frequency range without the branch-qualified frequency-block mean.

It gives a self-contained all-depth reduction:

\[
E_K
\le
\sum_{h<M_K}
\frac{F_K(h)}h
+
C_{\rm tail}M_K^{-\delta}
+
\pi2^{-5K}
\]

for every growing cutoff `M_K`.

Thus all-depth EQ follows from any theorem making the weighted sum over the smallest growing window vanish. Polynomial maximal decay on a polynomial window is one sufficient condition, but no external average theorem is needed.

## 9. Unconditional density-one full EQ

Combine the uniform tail with `T-9303` on a slowly growing low-frequency window

\[
H_m=81^{\alpha m},
\qquad
0<\alpha<\log_{81}\sqrt2.
\]

On every depth annulus

\[
[P_m,P_{m+1}),
\]

all but an exponentially small fraction of depths have low-frequency mass

\[
O\!\left(
81^{-\frac12(\log_{81}\sqrt2-\alpha)m}
\right).
\]

The uniform tail contributes

\[
O(81^{-\alpha\delta m}).
\]

Therefore `T-9309` proves:

\[
\boxed{
E_K\longrightarrow0
\quad\text{along a natural-density-one set of depths.}
}
\]

This theorem is unconditional within the packet. It uses no branch-qualified frequency theorem, external Fourier-decay theorem, computation, or probabilistic independence assumption.

It is a quantitative near-emptiness theorem for finite survivors. It does not prove all-depth EQ and does not decide whether the infinite attractor contains one ordinary positive integer.

## 10. Relation to issue #4's room tower

Issue #4 identifies base-`81` room digits with wrap counts of successive `H`-steps and shows that finite marginals form an inverse-limit tower: modulus `81^m` is driven by information at modulus `81^(m+1)`.

The stationary crosswalk identifies the fixed local measures under that tower. The split-collapse theorems show that absolute and bounded harmonic complex targets are the original EQ target in another representation.

What remains genuinely new on the room side is therefore nonlinear:

- a positive transfer operator for interval mass or relative entropy;
- a carry-template inverse theorem;
- a harmonic-location theorem for the sparse exceptional cylinders;
- a hyperbolic renewal theorem on the rational diagonal.

Ordered-position rigidity remains useful for geometric and recursive counting. It is not needed for the coefficient, entropy, tail, or density-one theorems above.

## 11. Current research offenses

### A. All-depth low-frequency theorem

The uniform tail leaves only the smallest growing frequencies. Prove, for some `M_K->infinity`,

\[
\sum_{h<M_K}
\frac{F_K(h)}h
\longrightarrow0.
\]

A maximal theorem is sufficient but not necessary.

### B. Harmonic location of exceptional cylinders

`T-9307` proves that low-energy prefixes are power-sparse in every interval. The remaining danger is that they may concentrate at harmonically expensive small locations.

Stratify exceptional residue classes by valuation, first nondegenerate level, and carry template. Show that their harmonic mass—not merely their count—is small.

### C. Carry-template inverse theorem

Classify polynomial-height low-energy lift paths. Every template should either:

1. reduce by a power of `64` or `81`;
2. be arithmetically impossible;
3. or persist on enough approximate cylinders to violate the entropy bound.

### D. Positive room-tower operator

Prove contraction of interval mass, entropy, or room imbalance after a full period-9 twist while controlling information imported from the next tower level.

### E. Exceptional-depth coherence

A depth bad across adjacent scales must defeat the period mean, prefix entropy, and room marginal contraction simultaneously. Expose and eliminate the resulting coherent carry word.

### F. Direct M1 intersection

Determine whether the symbolic stable leaf meets the ordinary-integer section outside `0` and `1`. Density-one and even all-depth finite equidistribution would not settle this exceptional existence question.

## Computation boundary

`X-9301` is the only computation in this packet. It uses exact modular arithmetic through `K=80`, `h<=K^2` to falsify lemma shapes. The next permissible extension is to emit lift-digit paths for existing argmins. Increasing the depth bound alone is not progress.

## Review order

1. `claims/L-9309-lift-digit-cylinder-bijection.md`
2. `claims/T-9307-low-energy-prefix-entropy.md`
3. `claims/T-9308-uniform-harmonic-tail.md`
4. `claims/L-9304-phase-reciprocity.md`
5. `claims/T-9303-valuation-stratified-depth-mean.md`
6. `claims/T-9309-unconditional-density-one-eq.md`
7. `claims/L-9307-global-rational-phase-stitching.md`
8. `claims/T-9305-split-collapse-weighted-equivalence.md`
9. `claims/L-9308-complex-bilateral-stitching.md`
10. `claims/T-9306-complex-test-sequence-equivalence.md`
11. `claims/R-9301-exact-prefix-interval-amplification.md`
12. `claims/L-9301-moving-character-identity.md`
13. `claims/D-9303-stationary-triadic-mirror.md`
14. `claims/L-9305-triadic-moving-character.md`
15. `claims/T-9304-two-place-crt-factorization.md`
16. `claims/D-9302-adelic-natural-extension.md`
17. `PROOF_PROGRAM.md`
18. `../../experiments/X-9301-cusp-scattering/README.md`

## Acceptance boundary

A review of `L-9309 -> T-9307 -> T-9308 -> T-9303 -> T-9309` would establish or reject the packet's strongest integrated result: unconditional density-one full weighted EQ.

A proof of the remaining all-depth low-frequency theorem would close full EQ and quantitative near-emptiness for every depth. It would still not exclude one exceptional infinite ordinary integer.

A nontrivial point in the integer section of `D-9302` would instead supply an M1 witness and, after the chart translation is independently checked, a candidate divergent Collatz orbit. No such point is presented here.