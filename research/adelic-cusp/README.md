# Adelic cusp Fourier program

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Branch:** `agent/gpt56-pro-04/15-adelic-cusp-fourier`  
**Date:** 2026-07-21  
**Status:** theory-first independent packet; all theorem-level claims remain `PROPOSED`; no counterexample claimed

## Executive result

The packet now proposes a self-contained proof of the complete weighted EQ criterion at **every** depth:

\[
\boxed{
E_K
=
\sum_{1\le h\le2^K}
\frac{|S_K(h)|}{2^Kh}
\longrightarrow0.
}
\]

The proof has two complementary halves:

1. `T-9308` gives a uniform power-saving harmonic tail above any growing cutoff at every depth.
2. `L-9310` and `T-9311` give deterministic pointwise decay below every subexponential cutoff at every depth.

Choosing the low/high cutoff `M_K=K` proves `T-9312`.

The new pointwise mechanism is **integral carry rigidity**. Signed reciprocal phases satisfy

\[
a_\ell
=64x_\ell-81x_{\ell+1}
\in\mathbb Z.
\]

Small phase energy permits few nonzero carries. Few nonzero carries force long exact zero-carry runs. Each zero run gives simultaneous very strong completion agreement and controlled archimedean height, and therefore cannot be too long. Chaining the runs from the terminal end yields logarithmic total energy for every primitive numerator.

This closes the former all-depth harmonic-location conjecture `C-9301` by a stronger pointwise theorem.

It does **not** settle the separate question whether the infinite `2`-adic survivor attractor contains one ordinary positive integer. No Collatz counterexample, divergent seed, nontrivial cycle, or proof of nonexistence is claimed.

## Core notation

Put

\[
\rho=\frac{64}{81},
\qquad
d=\frac{17}{81}.
\]

For a binary sequence `epsilon`, define the stationary survivor coding

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

with fair pushforward `nu`.

For the depth-`K` survivor set `R_K`, define

\[
S_K(h)
=
\sum_{A\in R_K}
\exp\!\left(2\pi i\frac{hA}{64^K}\right),
\qquad
F_K(h)=\frac{|S_K(h)|}{2^K}.
\]

The complete weighted EQ sum is

\[
E_K
=
\sum_{1\le h\le2^K}
\frac{F_K(h)}h.
\]

## Current theorem chain

```text
L-9309  exact reciprocal lift chain
   |
   v
L-9310  integral carries + completion-height rigidity
   |
   v
T-9311  pointwise decay on every subexponential window
   |
   +----------------------------------------+
   |                                        |
   |                                T-9307 prefix entropy
   |                                        |
   |                                        v
   |                                T-9308 uniform harmonic tail
   |                                        |
   +-------------------+--------------------+
                       |
                       v
                 T-9312 all-depth
                 complete weighted EQ
```

An independent depth-statistical chain remains:

```text
T-9303 translated depth-period mean
   + T-9308 uniform harmonic tail
   |
   v
T-9309 natural-density-one EQ
   |
   v
T-9310 upper-Banach-zero bad-depth sets
```

The second chain is no longer needed for all-depth convergence, but it gives independent translated-block information and is a valuable review cross-check.

## 1. Stationary local measures

`D-9301` and `L-9301` prove

\[
\boxed{
\widehat\mu(h/64^K)=2^{-K}S_K(h).
}
\]

Thus the changing finite survivor products are evaluations of one fixed transform on `Z_2`.

`D-9303` and `L-9305` prove

\[
\boxed{
\widehat\nu(h/81^j)=2^{-j}\widehat C_j(h),
}
\]

where the finite reductions of `nu` are the issue-#4 Cantor classes `C_j`.

## 2. One reciprocal phase chain

For fixed `K,h`, define

\[
q_\ell(h)
\equiv
-17h64^{\ell-K}
\pmod{81^{\ell+1}},
\qquad
0\le q_\ell<81^{\ell+1}.
\]

Let

\[
y_\ell(h)=\frac{q_\ell(h)}{81^{\ell+1}}.
\]

`L-9309` proves the exact recurrence

\[
y_{\ell+1}
=
\frac{\{64y_\ell\}+d_\ell}{81},
\qquad
0\le d_\ell<81,
\]

and the bijection

\[
\boxed{
h\pmod{81^L}
\longleftrightarrow
(q_0,d_0,\ldots,d_{L-2})
\in(\mathbb Z/81\mathbb Z)^L.
}
\]

The triadic mirror uses the unshifted phases `y_ell`. The original survivor product uses the same phases with an explicit reciprocity shift. Every dyadic/triadic CRT split merely changes where those shifts begin.

`T-9305` and `T-9306` quantify the collapse:

\[
\left|
F^{(2)}_K(h)-F^{(3)}_K(h)
\right|
\le
\frac{\pi|h|}{64^K},
\]

and the same scale controls arbitrary bounded harmonic complex tests.

## 3. General completion-height carry rigidity

`L-9310` steps back from the special constants. For any coprime expanding chart

\[
2\le M<N,
\]

with phase chain

\[
s_\ell
\equiv
-chM^{\ell-K}
\pmod{N^{\ell+1}},
\]

define signed normalized phases `x_ell=s_ell/N^(ell+1)` and carries

\[
\boxed{
a_\ell=Mx_\ell-Nx_{\ell+1}\in\mathbb Z.
}
\]

If

\[
\mathcal E_K(h)=\sum_{\ell<K}x_\ell^2,
\]

and `W` carries are nonzero, then

\[
W
\le
2(M^2+N^2)\mathcal E_K(h).
\]

A zero-carry run of length `r`, ending `t` phase levels from the terminal end, gives the nonzero divisibility relation

\[
N^r
\le
\frac12M^{r+t}+|ch|.
\]

Hence

\[
r
\le
\kappa_{M,N}t+\log_N(2|ch|),
\]

where

\[
\boxed{
\kappa_{M,N}
=
\frac{\log M}{\log(N/M)}
=
\frac1{\log_MN-1}.
}
\]

Chaining all zero runs from right to left gives

\[
K
\le
B_h(1+\kappa_{M,N})^{W+1}
\]

and therefore

\[
\mathcal E_K(h)
\gg_{M,N}
\left(
\log\frac{K}{1+\log|h|}
\right)_+.
\]

This theorem is deterministic and pointwise. It does not use a frequency average, depth average, random model, finite-state truncation, external Fourier theorem, or generic S-unit result.

For `M=64,N=81,c=17`,

\[
\kappa
\approx17.6548475770851.
\]

The identical constant independently appears in PR #20's ordinary-code repetition theorem. Both arguments express one product-formula criticality: completion agreement accumulates faster than rational height can support.

## 4. Pointwise cusp decay

The cosine-energy inequality

\[
|\cos(\pi x)|
\le
\exp(-2\|x\|^2)
\]

converts `L-9310` into `T-9311`.

Let

\[
b_*
=
\frac{2}{21314\log(1+\kappa)}
\approx3.2068\times10^{-5}.
\]

For a primitive numerator `64∤h`, the triadic mirror satisfies

\[
F^{(3)}_K(h)
\le
\exp\!\left[
-\frac2{21314}
\left(
\frac{\log(K/B(h))}{\log(1+\kappa)}-1
\right)_+
\right],
\]

where `B(h)=O(1+log|h|)`.

The original coefficient differs by at most `pi|h|/64^K`.

For arbitrary `h`, divide out the exact power `64^v|h` and use

\[
F_K(64^v h_0)=F_{K-v}(h_0).
\]

Consequently, if

\[
\log(2+H_K)=o(K),
\]

then

\[
\boxed{
\max_{1\le|h|\le H_K}F_K(h)	o0.
}
\]

For every fixed `R>0`,

\[
\boxed{
\max_{1\le|h|\le K^R}F_K(h)
\le
C_R
\left(
\frac{\log K}{K}
\right)^{b_*}.
}
\]

The exponent is crude and very small. Its positivity is enough.

## 5. Uniform high-frequency harmonic tail

`T-9307` uses the exact lift-prefix bijection to prove an entropy deficit for low-energy prefixes. With

\[
\beta=\frac{17\sqrt2}{27}<1,
\qquad
\eta=-\log_{81}\beta>0,
\]

every interval of `81^L` frequencies contains at most

\[
81^L\beta^L
\]

prefixes with energy at most `L/64`.

Dyadic shelling gives `T-9308`: there are `delta>0` and `C_tail` such that

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

uniformly in every depth and every `81<=M<=2^K`.

This closes the entire exponential frequency range.

## 6. All-depth weighted EQ

Choose `M_K=K`.

By `T-9311`,

\[
\sum_{h<K}\frac{F_K(h)}h
\le
C(1+\log K)
\left(
\frac{\log K}{K}
\right)^{b_*}
\longrightarrow0.
\]

By `T-9308`,

\[
\sum_{K\le h\le2^K}
\frac{F_K(h)}h
\le
C_{m tail}K^{-\delta}
+
\pi2^{-5K}
\longrightarrow0.
\]

Therefore `T-9312` proves

\[
\boxed{E_K\to0}
\]

for every depth.

The prior natural-density and uniform-density theorems remain correct-looking independent consequences, but no exceptional depth set is needed by the strongest chain.

## 7. Literature synthesis

The literature branch supplied several decisive methodological boundaries:

- fixed real self-similar Fourier-decay theorems do not directly apply to the moving finite-group cusp;
- finite-state tilted transfer bounds require a frozen truncation and uniform control of truncation dependence;
- graph-directed contractions construct completion points but not ordinary integers;
- generic S-unit terminology does not supply finiteness when cofactors vary dynamically;
- rational-base and Mahler/FLP methods are most useful through their separation of compact-state agreement from ordinary height.

The successful argument respects those boundaries. It does not import a black-box decay theorem. Instead it identifies a native integer-valued cocycle—`a_ell`—whose zero set has a direct height obstruction.

The finite-state pressure viewpoint remains conceptually useful: nonzero carries have a quantized positive cost. But the proof does not need a spectral-radius estimate, because integer quantization gives a state-independent gap.

## 8. Separate ordinary-integer frontier

`D-9302` embeds the real and `2`-adic codings into

\[
(\mathbb R\times\mathbb Q_2\times\mathbb Q_3)
/
\Delta\mathbb Z[1/6].
\]

Ordinary integer survivors are intersections with a rigid section. A nontrivial positive intersection in a valid chart class would yield an induced divergent orbit and then a candidate ordinary Collatz counterexample after independent verification of the chart translation.

All-depth EQ does not automatically exclude one such exceptional infinite point.

The strongest next synthesis is therefore between:

1. `D-9302` — ordinary-section realization;
2. PR #20 — every ordinary survivor code has factor-complexity slope at least `17.6548...`;
3. `L-9310` — the same criticality constant controls completion-height carry runs;
4. issue #4 — chart congruences and room/carry dynamics.

A decisive M1 theorem should show that one ordinary code cannot simultaneously meet the required symbolic novelty, carry structure, and bounded real/section constraints.

## Review order

The new all-depth chain should be reconstructed in this order:

```text
L-9310
  -> T-9311
  -> L-9309
  -> T-9307
  -> T-9308
  -> T-9312
```

Then review:

1. `L-9307` / `L-9308` and `T-9305` / `T-9306` for the survivor/mirror comparison;
2. `T-9303`, `T-9309`, and `T-9310` as independent depth-statistical checks;
3. `D-9301`, `D-9303`, `L-9301`, and `L-9305` for stationarization;
4. `D-9302` for the remaining ordinary-section problem.

## Claim boundary

- `L-9310`, `T-9311`, and `T-9312` are `PROPOSED`.
- `C-9301` is `SUPERSEDED`, not refuted.
- No existing issue-#4 claim is silently promoted.
- No positive-integer Collatz counterexample is constructed.
- No proof that no such counterexample exists is claimed.
- No claim in this packet resolves the Collatz conjecture.