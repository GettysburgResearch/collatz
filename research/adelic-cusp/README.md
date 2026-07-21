# Adelic cusp Fourier program

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Branch:** `agent/gpt56-pro-04/15-adelic-cusp-fourier`  
**Date:** 2026-07-21  
**Status:** theory-first independent packet; no counterexample claimed

## Executive summary

The `64 -> 81` survivor Fourier products are evaluations of one fixed Bernoulli self-similar measure on `Z_2`. The issue-#4 Cantor-class products are evaluations of one fixed Bernoulli self-similar measure on `Z_3`.

On the room-relevant CRT orbit, these local systems are the two local components of one rational character. Their factors stitch one reciprocal phase chain, so every CRT split is asymptotically equivalent to the original survivor coefficient in every sub-`64^K` frequency range.

The decisive finite state is the lift chain

\[
q_\ell(h)
\equiv
-17h64^{\ell-K}
\pmod{81^{\ell+1}}.
\]

Exact length-`L` lift prefixes are in bijection with residue classes modulo `81^L`. This yields an explicit entropy deficit for low-energy prefixes, which in turn gives:

1. a power-saving exceptional-frequency count in every interval;
2. a uniform power-saving harmonic tail at every depth;
3. unconditional weighted EQ on a natural-density-one set of depths;
4. the stronger conclusion that every fixed exceedance set has upper Banach density zero.

The remaining all-depth obstruction is harmonic location of the sparse low-energy residue classes among the smallest frequencies. The separate M1 problem asks whether the infinite `2`-adic attractor contains one ordinary positive integer. No density theorem in this packet settles that exceptional existence question.

## Core notation

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

and let `mu` be its fair Bernoulli pushforward.

For the triadic mirror put

\[
\lambda=\frac{81}{64},
\qquad
c=-\frac{17}{64},
\]

\[
\pi_3(\eta)
=
\sum_{r\ge0}c\eta_r\lambda^r
\in\mathbb Z_3,
\]

and let `nu` be its fair Bernoulli pushforward.

For the depth-`K` survivor set `R_K`, define

\[
S_K(h)
=
\sum_{A\in R_K}
\exp\!\left(2\pi i\frac{hA}{64^K}\right),
\qquad
F_K(h)=\frac{|S_K(h)|}{2^K},
\]

and the complete weighted EQ sum

\[
E_K
=
\sum_{1\le h\le2^K}
\frac{F_K(h)}h.
\]

## Current claim map

| ID | Status | Content |
|---|---|---|
| `D-9301` | `PROPOSED` | Fixed survivor measure on `Z_2` |
| `D-9302` | `PROPOSED` | S-arithmetic natural extension and integer section |
| `D-9303` | `PROPOSED` | Fixed triadic mirror measure on `Z_3` |
| `L-9301` | `PROPOSED` | `mu-hat(h/64^K)=2^{-K}S_K(h)` |
| `L-9302` | `PROPOSED` | Conditional shell lemma from frequency-block means |
| `L-9303` | `PROPOSED` | Quadratic phase energy controls the product |
| `L-9304` | `PROPOSED` | Exact `64`/`81` phase reciprocity and valuation shift |
| `L-9305` | `PROPOSED` | `nu-hat(h/81^j)=2^{-j}C_j-hat(h)` |
| `L-9306` | `PROPOSED` | Complete-group Fourier moments factor |
| `L-9307` | `PROPOSED` | Global rational diagonal and absolute stitching |
| `L-9308` | `PROPOSED` | Complex bilateral phase stitching |
| `L-9309` | `PROPOSED` | Lift-prefix / residue-class bijection |
| `T-9301` | `SUPERSEDED` | Earlier conditional low/high reduction |
| `T-9302` | `SUPERSEDED` | Earlier conditional density-one theorem |
| `T-9303` | `PROPOSED` | Valuation-stratified translated depth periods |
| `T-9304` | `PROPOSED` | Exact two-place CRT factorization |
| `T-9305` | `PROPOSED` | Absolute split collapse |
| `T-9306` | `PROPOSED` | Complex bounded-test split collapse |
| `T-9307` | `PROPOSED` | Low-energy prefix entropy deficit |
| `T-9308` | `PROPOSED` | Uniform harmonic tail at every depth |
| `T-9309` | `PROPOSED` | Unconditional natural-density-one weighted EQ |
| `T-9310` | `PROPOSED` | Uniform-density / upper-Banach-zero bad depths |
| `R-9301` | `PROPOSED` | Exact prefixes do not amplify to consecutive intervals |
| `C-9301` | `IDEA` | Harmonic exceptional-cylinder theorem for all-depth EQ |
| `Q-9301` | `IDEA` | Nontrivial ordinary-integer section intersection |
| `Q-9302` | `IDEA` | Better proof mechanism in the room/adelic representation |
| `O-9301` / `X-9301` | `EMPIRICAL` | Bounded exact scattering probe |

Every complete-looking proof remains `PROPOSED` pending independent review. `SUPERSEDED` means replaced by a stronger theorem, not refuted.

## 1. Stationary survivor and mirror measures

`D-9301` and `L-9301` prove

\[
\boxed{
\widehat\mu(h/64^K)=2^{-K}S_K(h).
}
\]

`D-9303` and `L-9305` prove

\[
\boxed{
\widehat\nu(h/81^j)=2^{-j}\widehat C_j(h).
}
\]

The changing finite modular products are restrictions of two fixed local transforms.

## 2. Exact phase reciprocity

For

\[
M_\ell=64^{K-\ell},
\qquad
N_\ell=81^{\ell+1},
\]

let

\[
q_\ell(h)
\equiv
-17hM_\ell^{-1}
\pmod{N_\ell},
\qquad
0\le q_\ell<N_\ell.
\]

Universal circle reciprocity identifies the dyadic phase with

\[
\frac{q_\ell(h)}{N_\ell}
+
\frac{17h}{M_\ell N_\ell}
\pmod1.
\]

This moves the modular inverse from a power of `81` modulo a power of `64` to the reciprocal setting where depth periods and lift digits are explicit.

## 3. Valuation-stratified depth periods

The reciprocal vector through level `m` has exact depth period

\[
P_m=9\cdot81^m.
\]

If

\[
e(h)=\left\lceil\frac{v_3(h)}4\right\rceil,
\]

then `T-9303` proves, over every sufficiently late translated `P_m` block,

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

The valuation loss is exact. It repairs an overuniform partial-product step in the issue-#4 depth-average proof without asserting that the full source theorem is false.

## 4. CRT product and split collapse

For

\[
Q=64^n81^j,
\qquad
u=(81^j)^{-1}\pmod{64^n},
\qquad
v=(64^n)^{-1}\pmod{81^j},
\]

`T-9304` gives

\[
G_{n,j}(h)
=
\widehat\mu(hu/64^n)
\widehat\nu(hv/81^j).
\]

The two local characters are the local representations of the same rational `h/Q`, and the two products are adjacent pieces of one phase chain.

For `K=n+j`,

\[
\boxed{
\left|
G_{n,j}(h)-\widehat\mu(h/64^K)
\right|
<
\frac{2\pi|h|}{64^K}.
}
\]

For arbitrary bounded complex weights `|w_h|<=1`,

\[
\boxed{
\left|
\sum_{h\le H}\frac{w_h}{h}G_{n,j}(h)
-
\sum_{h\le H}\frac{w_h}{h}\widehat\mu(h/64^K)
\right|
<
\frac{2\pi H}{64^K}.
}
\]

Thus a room/two-place Fourier proof is a proof of the original criterion in another representation. Its possible advantage is dynamical or combinatorial, not a weaker target.

## 5. Lift-prefix bijection

Define the lift digit

\[
d_\ell(h)
=
\left\lfloor
\frac{q_{\ell+1}(h)}{81^{\ell+1}}
\right\rfloor
\in\{0,\ldots,80\}.
\]

The normalized recurrence is

\[
\boxed{
y_{\ell+1}
=
\frac{\{64y_\ell\}+d_\ell}{81},
\qquad
y_\ell=q_\ell/81^{\ell+1}.
}
\]

`L-9309` proves

\[
h\pmod{81^L}
\longleftrightarrow
(q_0,d_0,\ldots,d_{L-2})
\]

is a bijection. One exact prefix is one arithmetic progression modulo `81^L`, so `R-9301` refutes exact-prefix persistence on a consecutive neighborhood.

## 6. Low-energy prefix entropy

Define

\[
\mathcal E_{K,L}(h)
=
\sum_{\ell<L}\|y_\ell(h)\|^2.
\]

Put

\[
\beta=\frac{17\sqrt2}{27}<1,
\qquad
\eta=-\log_{81}\beta>0.
\]

`T-9307` proves that every complete interval of length `81^L` contains at most

\[
\boxed{81^L\beta^L}
\]

frequencies with

\[
\mathcal E_{K,L}(h)\le L/64.
\]

In an arbitrary interval of length `H`, the exceptional count is `O(H^(1-eta))`. Every nonexceptional frequency has a fixed power-saving Fourier coefficient.

## 7. Uniform harmonic high-frequency tail

Put

\[
\gamma=\frac1{32\log81},
\qquad
\delta=\min\{\eta,\gamma\}>0.
\]

Dyadic shelling of the exceptional count and nonexceptional coefficient bound gives `T-9308`:

\[
\boxed{
\sum_{M\le h\le2^K}
\frac{F_K(h)}h
\le
C_{\rm tail}M^{-\delta}
+
\pi2^{-5K}
}
\]

uniformly in every depth.

Therefore, for every growing cutoff `M_K`,

\[
E_K
\le
\sum_{h<M_K}
\frac{F_K(h)}h
+
C_{\rm tail}M_K^{-\delta}
+
\pi2^{-5K}.
\]

The all-depth problem is confined to the smallest growing frequencies.

## 8. Unconditional density theorems

### Natural-density-one convergence

Combining `T-9303` on a slowly growing low window with `T-9308` on the high tail gives `T-9309`:

\[
\boxed{
E_K\to0
\quad\text{along a natural-density-one set of depths.}
}
\]

No branch-qualified frequency theorem, external Fourier theorem, or computation is used.

### Uniform-density convergence

The period estimate is valid on every translated complete block. `T-9310` therefore proves, for every `epsilon>0`,

\[
\boxed{
d^*\{K:E_K>\varepsilon\}=0,
}
\]

where `d^*` is upper Banach density.

Equivalently, every sufficiently long translated interval of depths is overwhelmingly good at any fixed accuracy. Bad depths can remain infinite, but they cannot form arbitrarily long dense clusters.

## 9. All-depth conjecture

`C-9301` asks for harmonic control of the sparse low-energy cylinders. For growing `L_K,H_K`, prove

\[
\boxed{
\sum_{\substack{1\le h\le H_K\\
\mathcal E_{K,L_K}(h)\le L_K/64}}
\frac1h
\longrightarrow0.
}
\]

Together with `T-9308`, this closes full all-depth EQ.

The exact terminal relation is

\[
h
\equiv
-17^{-1}64^{K-L+1}q_{L-1}(h)
\pmod{81^L}.
\]

Thus the remaining problem is real location of a low-energy subset of reciprocal terminal residues after multiplication by a depth-dependent unit.

Promising routes:

1. least-representative dispersion;
2. valuation and first-loss stratification;
3. carry-template classification;
4. a positive inverse-limit room operator;
5. rational-diagonal renewal;
6. coherence of depths exceptional at adjacent scales.

## 10. Separate M1 problem

`D-9302` embeds the real and `2`-adic codings in

\[
(\mathbb R\times\mathbb Q_2\times\mathbb Q_3)
/
\Delta\mathbb Z[1/6].
\]

Ordinary integer survivors are intersections with a rigid integer section. A nontrivial positive intersection in a valid chart class would yield an induced divergent orbit and then a candidate Collatz counterexample after independent verification of the chart translation.

No such point is presented here. Finite-depth equidistribution, even at every depth, does not automatically exclude one exceptional infinite ordinary point.

## Computation boundary

`X-9301` is the only committed experiment. It uses exact modular arithmetic through `K=80`, `h<=K^2` only to test lemma shapes. The next permissible computation is to emit lift-digit and least-representative data for existing argmins. Increasing the brute-force range alone is not progress.

## Review order

The load-bearing theorem chain is:

```text
L-9309 -> T-9307 -> T-9308 -> T-9303 -> T-9309 -> T-9310
```

Review those files first, followed by:

1. `L-9307` / `L-9308` and `T-9305` / `T-9306` for split collapse;
2. `D-9301`, `D-9303`, `L-9301`, and `L-9305` for stationarization;
3. `D-9302` for the direct integer-section route;
4. `C-9301` for the all-depth frontier.

## Acceptance boundary

Independent verification of the load-bearing chain would establish uniform-density convergence of the complete weighted EQ criterion.

A proof of `C-9301` would close all-depth EQ and quantitative near-emptiness of finite survivors. It would still not decide the direct M1 integer-section question.

No claim in this packet constructs or proves a positive-integer Collatz counterexample.