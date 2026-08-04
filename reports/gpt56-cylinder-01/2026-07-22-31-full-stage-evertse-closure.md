# Full corrected-stage closure by Evertse admissibility

**Agent:** `gpt56-cylinder-01`  
**Issue:** `#31`  
**Branch:** `agent/gpt56-cylinder-01/31-residue-cylinder-dichotomy`  
**Date:** 2026-07-22  
**Status:** theorem-level claims `PROPOSED`; exact experiment independently replayed

## Starting point

The previous three theorem layers had established:

1. universal nonstabilization for the direct dyadic-boundary connector class;
2. extinction of the free ordinary quotient in the corrected 256-transition stage;
3. a factor-greater-than-275 completion-height collapse on every hypothetical cap chain.

The unresolved equation was exact cap stitching. Literature wave 5 recommended expanding it as a finite `{2,3}`-power equation and auditing all proper subsums.

## New mathematical step

At stabilized scales, the scaled connector coordinate

```text
Z_j=X_j+64 H_(t_(j+1)) z_j
```

obeys

```text
H_(t_(j+1)) Z_(j+1)=N_(t_j) Z_j+b_(i_j),
b_i in {9,54,36,24}.
```

All connector inverses disappear. One complete stage is

```text
2^(E_m) Z_(m+1)
 =3^(A_m) Z_m
  +sum_(j=0)^255 b_(i_j) 2^(U_(m,j)) 3^(V_(m,j)).
```

The 256 internal terms are exact `{2,3}`-units. The only outside-prime content is carried by the two ordinary endpoints.

The signed quotient was then audited rather than silently restricted to positivity. Every signed ordinary trajectory eventually has quotient `0` or `-1`. The first case is the cap chain; the second is a dual co-cap chain. After sign reversal, both give a positive endpoint sequence and a homogeneous 258-coordinate zero sum with exactly one positive term.

Primitive normalization costs at most

```text
2^3 * 3^3 = 216.
```

The cap/co-cap endpoint estimates give

```text
limsup log_2(U_m U_(m+1))/E_m
 <=6498/346819
 <1/50.
```

Therefore every sufficiently late primitive stage tuple satisfies Evertse's 1984 almost-`S`-unit admissibility condition for `S={2,3}`, `d=1/50`. Positivity rules out all proper vanishing subsums. A projective ratio containing `2^(E_m)` has strictly increasing 2-adic valuation, so the tuples are pairwise distinct. Evertse's theorem permits only finitely many. Contradiction.

## New claims

- `L-9704` — connector-free physical coordinate and fixed 256-term power sum;
- `L-9705` — signed quotient extinction and cap/co-cap dichotomy;
- `L-9706` — exact Evertse admissibility and projective distinctness;
- `T-9705` — universal ordinary exclusion for the full corrected-stage class;
- `X-9704` — exact finite derivation and independently written checker.

## Result

For every physically overlapping infinite corrected 256-stage directive,

```text
a_k != 0 infinitely often,
the unique Z_2 completion is not in Z.
```

This closes side A for the entire frozen class, including negative ordinary completions. It does not prove the Collatz conjecture; it proves that this specific proposed supercritical stage architecture cannot be initialized by any ordinary integer.

## External source

The only new black-box theorem is Corollary 1 of:

J.-H. Evertse, *On sums of S-units and linear recurrences*, Compositio Mathematica 53 (1984), 225--244.

The source's exact primitive tuple, nondegenerate zero-sum, and `0<=d<1` hypotheses are reproduced in `L-9706`. PR #13 may import this theorem under a future `LIT-KTHM` identifier; no literature-branch status is modified here.

## Verification

```text
local coordinate cases: 256
physical cofactor cases: 256
adjacent gcd cases: 256
prime turnover cases: 256
stable dictionary rows: 256
signed quotient integral cases: 4704
primitive gcd cap: 216
endpoint product ratio: 6498/346819 < 1/50
payload digest:
f3a4fd8a6f5074c488bd1a0d46a420a3f6f4425aaf30bef8245d5512a995a858
all independent connector-free checks passed
```

## Review priorities

1. rederive the scaled connector coordinate and physical identity;
2. check the `Y=-1` co-cap normalization;
3. independently reproduce the co-cap height transfer;
4. inspect Evertse's original Corollary 1;
5. audit the primitive gcd bound and outside-prime product;
6. verify projective distinctness after primitive normalization;
7. reconstruct the bridge from an ordinary initial completion to a signed stage trajectory.

## Candidate and ledger boundary

No `K-####` candidate is created. No competing root ledger is edited. Every source-branch claim retains its native status.
