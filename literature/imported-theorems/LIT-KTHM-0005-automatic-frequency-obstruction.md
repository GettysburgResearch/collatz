# LIT-KTHM-0005 — automatic sequences have rational existing letter frequencies

**Sources:** [@Cobham1972]; explicit modern statement [@AlloucheShallitYassawi2022]
**Inspection:** original metadata; official modern article HTML
**Proof status:** reconstructed complete proof

## Statement

Let `k≥2`, and let `u=(u_n)_{n≥0}` be a `k`-automatic sequence over a finite alphabet. If the natural frequency

```text
lim_(N→∞) (1/N) #{0≤n<N : u_n=a}                 (1)
```

exists for a letter `a`, then it is rational.

Consequently, a finite-alphabet sequence with an existing irrational letter frequency is not `k`-automatic for any integer base `k≥2`.

## Proof

Choose a deterministic finite automaton with output (DFAO) producing `u_n` from the base-`k` digits of `n`, allowing leading zeroes. Let `Q` be its finite state set. Form the integer transition-count matrix `A`, where `A_{pq}` is the number of digits `d∈{0,...,k-1}` that send state `p` to state `q`. Every row sum is `k`. Put `P=A/k`, a rational stochastic matrix.

Let `e` be the row vector concentrated at the initial state and let `h_a` be the column indicator of states whose output is `a`. The `k^m` words of length `m` (with leading zeroes) represent exactly the integers `0≤n<k^m`, so

```text
(1/k^m) #{0≤n<k^m : u_n=a} = e P^m h_a.          (2)
```

The scalar sequence on the right is obtained from powers of a rational matrix. Let `mu(x)` be the minimal polynomial of `P` over `Q`. Factor

```text
mu(x) = (x-1)^r g(x),    gcd(x-1,g)=1.
```

Bezout's identity over `Q[x]` gives a rational polynomial `E(x)` that acts on the generalized eigenspace decomposition as the spectral projection onto the generalized `1`-eigenspace. Thus `E(P)` has rational entries.

Because `P` is stochastic, its powers are bounded. Hence there are no nontrivial Jordan blocks at eigenvalues of modulus `1` contributing to a convergent scalar. If the limit in (2) exists, every contribution from eigenvalues other than `1` either decays or has zero coefficient; the nilpotent part at `1` also has zero coefficient. Therefore

```text
lim_(m→∞) eP^m h_a = e E(P) h_a,
```

a rational number.

If the full natural frequency (1) exists, its subsequence along `N=k^m` has the same limit. Equation (2) therefore proves that frequency is rational. ∎

## Native application

Suppose the schedule in `CLAUDE/T-0003` is defined as a finite-alphabet word and the frequency of its `18`-gap letter is proved to equal the transcendental `alpha` in `LIT-KTHM-0004`. Then the schedule is not `k`-automatic for any `k≥2`.

## Citation correction

This is a result from Cobham's theory of uniform tag sequences. It is not the usual “automatic in two multiplicatively independent bases implies ultimately periodic” theorem, and no second base is needed.

## Non-applications

The theorem does not identify a nonautomatic sequence as Sturmian, S-adic, or Ostrowski-computable. It does not obstruct a nonautomatic finite algorithm or prove any regeneration congruence.
