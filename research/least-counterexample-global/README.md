# Least-counterexample global proof attack

**Agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Issue:** #78  
**Namespace:** `65xx`  
**Status:** theorem-level claims are **PROPOSED** unless explicitly marked otherwise

**No proof of the Collatz conjecture is claimed.**

## Objective

This packet attacks only an exhaustive least-counterexample contradiction.

For

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd},
\end{cases}
\]

write

\[
C_k={3^{q_k}\over2^k},
\qquad
D_k=q_k-{\log2\over\log3}k.
\]

Branch-qualified PR #76--#77 reduces a least positive counterexample to:

```text
Lane A:
  C_k >= 1 for every k,
  and the actual ordinary orbit tends to +infinity;

Lane B:
  a finite first crossing C_j < 1,
  with j >= 217,976,794,617.
```

A nontrivial positive cycle belongs to Lane B after rotation to its minimum.

# I. Lane A — exact ordinary consequences

## 1. Polynomial correction product

For an all-prefix-supercritical ordinary orbit,

\[
{x_k\over n}
=C_k
\prod_{x_i\text{ odd}}
\left(1+{1\over3x_i}\right).
\]

The orbit cannot repeat. After the first step, every odd source is coprime to six. Distinctness gives

\[
\boxed{P_k\le e^{7/9}k^{1/9}.}
\]

This acts on the actual ordinary orbit values, not on a free symbolic word.

## 2. `8/9` logarithmic mean surplus

Distinct-state packing and the product bound give

\[
\boxed{
\sum_{k=1}^{K}D_k
\ge
{1\over\log3}
\left[
\log{(n+K)!\over n!n^K}
-{1\over9}\log(K!)-{7K\over9}
\right].}
\]

Hence

\[
\boxed{
{1\over K}\sum_{k=1}^{K}D_k
\ge {8\over9}\log_3K-O_n(1).}
\]

In particular

\[
\max_{k\le K}3^{D_k}
\ge {K^{8/9}\over n e^{5/3+o(1)}}.
\]

## 3. Fixed low-surplus bands have density zero

The correction product has the exact additive form

\[
P_k
=1+{1\over3n}
\sum_{\substack{i<k\\x_i\text{ odd}}}3^{-D_i}.
\]

For every fixed `H`,

\[
\boxed{
\#\{i<k:D_i\le H\}=O_{n,H}(k^{1/9}).}
\]

Therefore

\[
D_k\to+\infty
\quad\text{in natural density one}.
\]

## 4. Critical-density boundary and subexponential cusps

López--Stoll Theorem 1, source-qualified in `T-6506`, says that a rational `2`-adic integer with a divergent noncyclic Collatz orbit must satisfy

\[
\liminf q_k/k={\log2\over\log3}.
\]

Thus an ordinary Lane-A orbit must satisfy

\[
\boxed{\liminf D_k/k=0.}
\]

There is a subsequence `k_j` for which

\[
\boxed{\log T^{k_j}(n)=o(k_j).}
\]

So the remaining orbit has logarithmically growing mean bank and density-one bank escape, but also arbitrarily late subexponential physical cusp returns.

## 5. Canonical two-boundary collapse

At those cusp times, the exact parity-cylinder source/end representatives satisfy

\[
\boxed{r_{k_j}=n,\qquad s_{k_j}=T^{k_j}(n),}
\]

and

\[
\boxed{
{\log r_{k_j}\over k_j}\to0,
\qquad
{\log s_{k_j}\over q_{k_j}}\to0.}
\]

Lane A is therefore reduced to a simultaneous zero-rate `2`-adic source / `3`-adic endpoint problem. The recent exponent-code literature diagnoses this corner but does not prove it empty.

## 6. Tail-minimum ladder

Every divergent positive orbit has tail minima

\[
h_0<h_1<h_2<\cdots
\]

with infinite ordinary stopping time and

\[
\boxed{h_{i+1}\le(3h_i+1)/2.}
\]

Their coefficient-stopping depths tend to infinity. Thus one Lane-A orbit manufactures a multiplicatively `3/2`-syndetic ladder of increasingly deep infinite-stopping starts.

# II. A necessary firewall — the four scalar conditions are not a contradiction

`R-6501` gives the explicit binary word defined by

\[
q_k=\left\lceil
\alpha k+{8\over9}\log_3\left({k+2\over2}\right)
\right\rceil.
\]

Its increments are binary and its surplus satisfies

\[
D_k\ge0,
\]

\[
{1\over K}\sum_{k=1}^{K}D_k
\ge {8\over9}\log_3K-O(1),
\]

\[
3^{D_K}\gg K^{8/9},
\]

and every fixed low band is visited only finitely often. Also `D_k/k -> 0`.

Every finite prefix is an exact parity cylinder with infinitely many positive ordinary representatives, and the infinite word has one compatible `2`-adic realization.

Therefore these scalar estimates—even together with finite compatibility and a completed parity path—do not imply ordinary nonexistence. The missing theorem must use the ordinary canonical boundaries, inverse-tree minimality, or pointwise orbit mixing.

# III. Lane B — finite first crossings

## 1. Cofinal harmonic window

For an acyclic no-descent crossing with `q` odd sources,

\[
\lambda=j\log2-q\log3>0
\]

satisfies

\[
\lambda
\le
\min\left\{
{q\over3n},
{1\over3n}+{1\over6}\log\left(1+{2(q-1)\over n}\right),
{7\over9}+{1\over9}\log q
\right\}.
\]

## 2. Every word has a complete finite ordinary decision

For a first-crossing word `w`, let `r_w` be its least positive residue and `y_w=T^j(r_w)`. Every source is

\[
x=r_w+2^jt,
\]

and no descent occurs exactly for

\[
0\le t\le
\left\lfloor{y_w-r_w\over2^j-3^q}\right\rfloor.
\]

Lane B is missing a uniform theorem, not a local integrality test.

## 3. Low-complexity cofinal families

Using full dyadic separation of repeated parity factors and an effective logarithmic-form lower bound, `T-6505` proves that bounded-bank, uniformly low-complexity first-crossing families occur only finitely often. The mechanical/Sturmian extremizer cannot itself remain an ordinary least-counterexample prefix cofinally.

# IV. Literature position

- Rozier--Terracol is the live paradoxical-sequence source; its global finiteness assertion remains conjectural.
- Niu arXiv:2605.13886 is withdrawn and is not used independently.
- Angeltveit improves finite verification and supplies necessary constraints, not exceptional-orbit elimination.
- Chang proves map-level balance but leaves pointwise one-bit orbit mixing open.
- López--Stoll supplies the critical-density equality used in `T-6506`.
- Kramer supplies a useful `2`--`3`--infinity diagnostic and necessary zero residue rates, but no canonical-boundary lower bound.

See `LITERATURE_AUDIT.md`.

# V. Exact remaining proof target

A complete proof from this route must close both:

```text
A. no positive ordinary orbit occupies the zero-rate,
   sparse-return, logarithmically banked two-boundary cusp;

B. no positive first-crossing cylinder or positive cycle
   survives all time.
```

The clearest Lane-A target is a canonical-boundary uncertainty theorem: prove that every sufficiently long all-prefix-supercritical word has a source or endpoint representative with a positive—or otherwise quantitatively incompatible—height rate.

No such theorem is currently proved.

## Review order

1. `claims/R-6501-scalar-profile-does-not-imply-exclusion.md`
2. `claims/T-6506-critical-density-subexponential-cusp.md`
3. `claims/L-6504-two-boundary-cusp-subsequence.md`
4. `claims/L-6503-tail-minimum-syndetic-ladder.md`
5. `claims/T-6504-distinct-state-packing-mean-surplus.md`
6. `claims/L-6501-distinct-odd-source-product-bound.md`
7. `claims/T-6503-low-surplus-density-zero.md`
8. `claims/T-6505-low-complexity-first-crossings-are-finite.md`
9. `claims/T-6502-paradoxical-harmonic-window.md`
10. `claims/L-6502-first-crossing-cylinder-decision.md`
11. `Q-6501-close-two-coefficient-lanes.md`
12. `LITERATURE_AUDIT.md`

## Scope boundary

This packet makes real infinite-class progress, but does not exclude the final ordinary Lane-A profile. It introduces no counterexample architecture and does not promote a completion, scalar estimate, or almost-all theorem to a proof.
