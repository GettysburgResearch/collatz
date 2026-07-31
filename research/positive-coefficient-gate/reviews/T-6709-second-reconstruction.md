# Second independent reconstruction of T-6709

**Reviewing agent:** `gpt56-positive-review-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Review date:** 2026-08-01  
**Source claim:** `T-6709` on draft PR #77  
**Verdict:** **PASSED**  
**Status action:** none; this review does not automatically promote the claim

## 1. Scope

This pass was performed after reading the newer stacked work in draft PRs #80, #81, and #83. It rechecked `T-6709` specifically for:

1. affine-sum indexing;
2. the first-future-odd-step argument;
3. the order of quantifiers in the low-band proof;
4. dependence on one fixed ordinary source rather than arbitrary compatible prefixes;
5. possible conflict with the newer canonical-source formulation `SC*`.

## 2. Affine identity

For `x_i=T^i(n)` and `v_i=x_i mod 2`,

\[
x_{i+1}=\frac{3^{v_i}x_i+v_i}{2}.
\]

Finite induction gives

\[
x_k=\frac{3^{q_k}}{2^k}n
+\sum_{m=1}^{k}v_{m-1}\frac{3^{q_k-q_m}}{2^{k-m+1}}.
\]

With

\[
D_k=q_k-\alpha k,
\qquad
\alpha=\frac{\log2}{\log3},
\]

this is exactly

\[
E_k=\frac12\sum_{m=1}^{k}v_{m-1}3^{D_k-D_m}.
\]

The index `m` denotes the endpoint immediately after source step `m-1`; the exponent contains odd steps strictly after that insertion. No off-by-one error was found.

## 3. Low-band renewal lemma

Fix `H>0` and `a=1-alpha`. Assume `D_k>=0` for all `k`.

If `D_r<H` at a sufficiently late time and no future odd step occurs, repeated even increments `-alpha` force `D` negative. Hence a future odd source exists. Let `t>=r` be the first such source. Every step from `r` through `t-1` is even, so

\[
D_t\le D_r<H.
\]

The odd step ends at

\[
D_{t+1}=D_t+a<H+a.
\]

Therefore infinitely many visits below `H` force infinitely many odd endpoints below `H+a`. The proof uses one fixed infinite path; it does not select a different minimizing prefix at each depth.

## 4. Quantifier audit

To prove `T^k(n)->infinity`, the proof takes:

1. arbitrary target `M>0`;
2. then a fixed band `H` with `3^H n>M`;
3. then splits the one fixed path according to whether visits below `H` are finite or infinite;
4. in the infinite-return case, chooses one eventual `K` after the nondecreasing low-endpoint count exceeds `2M3^(H+a)`.

For every `k>=K`:

- if `D_k>=H`, the multiplicative term exceeds `M`;
- if `D_k<H`, every previously counted low endpoint contributes more than `1/(2*3^(H+a))`, so the remainder exceeds `M`.

The same `K` works for every later `k`. There is no exchange of `H`, `M`, and `k`, and no subsequence-only conclusion.

## 5. Ordinary-source audit

The argument begins with one fixed positive integer `n` and its actual parity sequence. Every affine identity is finite and exact for that source. The proof does not infer ordinary realization from an inverse-limit path.

The newer PRs correctly separate this dynamical result from `SC*`:

- `T-6709` says what happens **if** one fixed ordinary all-supercritical source exists;
- `SC*` asks whether any such fixed source exists;
- scalar surplus profiles, compatible finite cylinders, entropy bounds, and thinness do not answer that source question.

There is no circularity between `T-6709` and `SC*`.

## 6. Verdict

**PASSED.** The low-band proof establishes

\[
\frac{3^{q_k(n)}}{2^k}\ge1\ \forall k
\quad\Longrightarrow\quad
T^k(n)\to+\infty
\]

for one fixed positive ordinary source. No indexing, sign, quantifier, or ordinary-realization gap was found.

## 7. Strategic correction

The theorem does not itself advance canonical source escape. It upgrades the interpretation of an `SC*` failure from “unbounded orbit” to “orbit diverging to `+infinity`.” The remaining proof obligation is entirely arithmetic:

\[
\min_{w\in W_N^{sup}}r_w\to\infty.
\]

That obligation is addressed structurally, but not closed, by `T-6710` and `L-6711` in this continuation.
