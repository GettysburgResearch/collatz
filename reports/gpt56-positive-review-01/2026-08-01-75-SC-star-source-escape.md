# Session report — SC* source-escape attack

**Agent:** `gpt56-positive-review-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Branch:** `agent/gpt56-positive-review-01/75-verify-supercritical`  
**Date:** 2026-08-01

## Requested objective

Sync with the current repository, especially draft PRs #77, #80, #81, and #83; reconstruct `T-6709`; then attempt to exclude every positive ordinary integer whose every coefficient prefix is supercritical by proving canonical least-source escape `SC*` or the strongest rigorous quantitative substitute.

## Repository synthesis

- **PR #77:** independently verifies `T-6708` and proposes `T-6709`, classifying an ordinary all-supercritical path as divergent to `+infinity`.
- **PR #80:** proves strong correction-product, mean-surplus, sparse-low-band, and critical-density restrictions, but supplies `R-6501`, showing that scalar profiles plus finite compatibility and one `2`-adic completion do not imply ordinary exclusion. It isolates simultaneous zero canonical source/endpoint rates.
- **PR #81:** defines the exact final source target
  ```text
  SC*: min_{w in W_N^sup} r_w -> infinity
  ```
  and separates it from the complete first-crossing target `FC*`.
- **PR #83:** proves exact shifted-denominator identities and polynomial sparsity for first-crossing failures, while explicitly preserving the distinction between thinness and emptiness. It does not close SC*.

## T-6709 reconstruction

A second independent pass checked:

1. the finite affine sum and all indices;
2. the first-future-odd-step low-band lemma;
3. the `M -> H -> K` quantifier order;
4. use of one fixed ordinary source;
5. compatibility with the newer canonical-source framework.

**Verdict: PASSED.** No error was found. The full orbit, not merely a subsequence, tends to `+infinity`.

## Main new theorem — T-6710

For

```text
S_N={n>=1: C_k(n)>=1 for every 1<=k<=N},
m_N=min S_N,
tau_c(n)=min{k>=1:C_k(n)<1},
```

one has the exact finite inverse identity

```text
m_N>B
iff
tau_c(n)<=N for every 1<=n<=B.
```

Hence, with

```text
H(B)=max_{1<=n<=B} tau_c(n),
```

whenever the right side is finite,

```text
m_N>B for every N>=H(B).
```

The cofinal statement is exact:

```text
SC*: m_N -> infinity
iff
every positive integer has finite coefficient stopping time.
```

Thus SC* is precisely the coefficient-stopping-time conjecture in canonical-source language.

## Verification-to-source transfer

If a proof-grade finite computation certifies that every `n<=B` reaches `1` within at most `R(B)` shortcut steps, then

```text
m_N>B for N>=max(2,R(B)).
```

Indeed, reaching `1` gives

```text
1=C_k n+E_k,
E_k>=0,
```

and therefore `C_k<1` for `n>1`; the start `1` has the subcritical word `10`.

This is the strongest unconditional quantitative source-escape transfer obtained in this pass. A theorem stating convergence below `B` without a frozen maximal hitting-time certificate proves existence of some finite threshold but does not supply its numerical value.

## Canonical low-band coupling — L-6711

For an all-supercritical word with canonical pair `(r_w,s_w)` and low-band odd-endpoint count `N_H(N)`, the exact remainder identity gives

```text
s_w >= 3^D_N r_w
       +(N_H(N)/2) 3^(D_N-H-(1-alpha)),
```

and hence

```text
s_w-r_w >= N_H(N)/(2*3^(H+1-alpha)).
```

This is the requested finite source/end coupling. It shows exactly how low-band contributions accumulate in the canonical endpoint for one source.

It does **not** force `r_w` to grow across different words. The endpoint can absorb the accumulated correction while a bounded source remains arithmetically compatible.

## Exact missing inequality

For

```text
T_w(x)=(3^q x+A_w)/2^N,
```

a fixed source `n` realizes `w` through depth `N` only if

```text
v_2(3^q n+A_w)>=N.
```

The missing theorem is therefore any source-dependent finite bound

```text
|w|<=Phi(n)
```

for all-supercritical words realized by `n`; equivalently, a uniform upper bound on the displayed `2`-adic valuation along all-supercritical prefixes from one fixed source.

A stronger two-boundary form would forbid simultaneous

```text
bounded canonical source,
subexponential canonical endpoint,
and arbitrarily deep all-supercritical divisibility.
```

This is exactly the canonical-boundary uncertainty target already isolated by PR #80, now written as a fixed-source valuation inequality.

## Outcome

Full SC* was **not proved**. Claiming otherwise would amount to claiming a proof of the coefficient-stopping-time conjecture, which the current repository estimates do not supply.

The rigorous advances are:

1. second `PASSED` reconstruction of `T-6709`;
2. exact equivalence between SC* and universal finite coefficient stopping;
3. a quantitative inverse source-escape theorem for every finite certified range;
4. an exact canonical low-band source–endpoint lower bound;
5. one sharply isolated missing fixed-source valuation inequality.

## Files added

```text
research/positive-coefficient-gate/T-6710-SC-star-inverse-stopping-equivalence.md
research/positive-coefficient-gate/L-6711-canonical-low-band-source-endpoint-bound.md
research/positive-coefficient-gate/reviews/T-6709-second-reconstruction.md
reports/gpt56-positive-review-01/2026-08-01-75-SC-star-source-escape.md
```

## Recommended next offense

Do not add another scalar surplus estimate. Attack one of these equivalent fixed-source forms:

1. prove `v_2(3^{q(w)}n+A_w)` is bounded as `w` ranges over all-supercritical words for fixed `n`;
2. prove a simultaneous canonical source/endpoint height lower envelope incompatible with PR #80 cusp times;
3. produce cofinal finite verification artifacts with explicit maximal coefficient-stopping depth, yielding a growing certified lower envelope for `m_N`;
4. exploit arithmetic relations between successive nested canonical residues from the same source, not independent words or arbitrary completions.
