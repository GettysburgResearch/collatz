# R-6601 — the two coefficient lanes do not fuse by compactness

**Claim ID:** `R-6601`  
**Type:** exact proof-strategy obstruction  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01`  
**Created:** 2026-07-31  
**Dependencies:** `T-6602`; repository ordinary-extraction criterion from PRs #56/#57/#60  

## Refuted inference

The following reasoning is invalid:

```text
A divergent orbit has ordinary no-descent starts with longer and longer
coefficient-supercritical prefixes.

Compactness selects one infinite all-supercritical parity word.

Therefore one fixed positive ordinary integer realizes that word.
```

`T-6602` gives the exact opposite two-place behavior:

```text
ordinary realizing starts -> +infinity in R,
while a subsequence -> one point in Z_2.
```

The compact limit is an inverse-limit point. It is ordinary only if the canonical representatives of its nested parity cylinders are Archimedeanly bounded and eventually stabilize.

## Exact missing assertion

For the tangent word `v`, let `r_L` be the canonical residue in `[0,2^L)` realizing its first `L` parity bits. Ordinary extraction requires

\[
\boxed{\sup_L r_L<\infty,}
\]

or equivalently eventual stabilization of `r_L`.

The actual wave minima supplied by `T-6602` prove only

\[
\forall L\;\exists\text{ arbitrarily large }h
\quad
h\equiv r_L\pmod{2^L}.
\]

They provide no uniform upper bound on `h` or `r_L`. The quantifiers are in the wrong order.

## Why current global tools do not repair it

The following remain compatible with a nonordinary tangent:

- exact realization of every finite prefix;
- infinitely many ordinary realizers per prefix;
- one orbit supplying infinitely many of those realizers;
- coefficient-supercriticality at every tangent prefix;
- conditional divergence of any positive ordinary tangent;
- compactness, positive entropy, or positive 2-adic dimension;
- ensemble or residue-class balance;
- fresh-prime turnover conditional on divergence.

A valid fusion theorem must add one architecture-specific statement that bounds canonical least representatives, proves eventual zero high blocks, or forces a descent/merge before the representative can escape.

## Consequence for the current positive program

PR #76's finite-crossing gate and PR #77's `tau=infinity` growth theorem are both genuine. They do not close the existence problem when combined. A divergent trajectory may produce:

```text
finite tau(h_i) increasing without bound,
```

or an all-supercritical 2-adic tangent whose ordinary prefix roots escape.

The next theorem should therefore target the least ordinary roots of the **orbit-pruned supercritical cylinder tree**, not add another compact limit or drift estimate.
