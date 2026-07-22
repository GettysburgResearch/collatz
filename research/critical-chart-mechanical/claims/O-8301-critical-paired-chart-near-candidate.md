# O-8301 — A critical paired-chart word passes the PR #45 factor product but is not integral

Claim ID: `O-8301`  
Title: A trillion-block negative-three chart word admits a 41-swap 61-bit repair and a factorwise quotient rejection  
Status: `EMPIRICAL / EXACT FINITE-CIRCUIT AUDIT`  
Authoring agent: `gpt56-cycle-02`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: `T-8302`, `L-8303`; frozen PR #45 parameters and its five certified denominator primes  
Scope: one compressed paired-chart word  
Related counterexample candidates: none; the frozen word is refuted

## Frozen critical chart word

Use

```text
accelerated length k = 3,149,971,404,836,
total valuation A   = 4,992,586,555,009,
chart length m      = 1,574,985,702,418,
expanding symbols s = 1,307,356,254,663.
```

Let `e=L(s,m)` be the lower mechanical chart word of `T-8302`: symbol `1` is the exact `(1,2)` negative-three block and symbol `0` is `(2,2)`.

The full cycle denominator is exactly the PR #45 denominator

\[
 D=2^A-3^k.                                                  \tag{1}
\]

The five certified prime factors are

```text
7, 191, 281, 28,591, 136,398,329,
```

with product

```text
M=1,465,129,870,107,858,983.
```

## Exact order cover

Their multiplicative orders for base two are

```text
3, 95, 70, 14,295, 3,099,962.
```

The least common multiple is

```text
5,893,756,253,070
```

and exceeds the complete excess window

```text
A-k=1,842,615,150,173.
```

Thus these five factors already form an order-cover in the sense of the PR #34 cross-prime compiler: compatible local prefix-excess paths at the five factors reconstruct at most one trillion-letter ordinary valuation word. This does **not** turn the proper factor product into the full denominator.

## Frozen 41-swap repair

Generate the first 80 pairwise-disjoint adjacent unequal symbols of `e`. The frozen mask

```text
high = 46,478,
low  = 8,732,882,846,915,751,955
```

selects 41 replacements at positions

```text
0,4,22,69,75,81,87,93,99,134,140,146,163,169,193,199,204,
216,228,240,246,252,263,269,281,305,310,328,346,352,357,363,
381,387,393,416,422,434,446,452,463.
```

Each replacement is verified using the monomial delta in `T-8302/(14)`. The modified chart numerator satisfies

\[
 \boxed{C_e\equiv0\pmod M.}                                 \tag{2}
\]

## Directed real rejection

A 145-digit outward-rounded affine interval gives

```text
1567441266425753353472608.002804312818122854605656551438441267269013717272501660698482710228928102929253619708480614089546310869531692147085897640
< C_e/D <
1567441266425753353472608.002804312818122854605656551438441267269013717272501660698482710228928102929253619708480614089546431693597989690936299955.
```

Hence

```text
distance(C_e/D, Z) > 0.002804312818122854605656551438.
```

The word is not integral.

## Independent quotient-cylinder rejection

For each of the five primes, both `C_e` and `D` have exact valuation one. `L-8303` gives quotient residues

```text
p=7           -> x mod p = 4
p=191         -> x mod p = 175
p=281         -> x mod p = 139
p=28,591      -> x mod p = 22,561
p=136,398,329 -> x mod p = 97,639,464.
```

CRT gives

```text
x = 1,051,915,013,441,653,484 mod M.
```

The unique real floor is

```text
1,567,441,266,425,753,353,472,608,
```

whose residues for the floor and ceiling are respectively

```text
1,377,488,262,577,689,718,
1,377,488,262,577,689,719 mod M.
```

Neither equals the quotient cylinder. This gives an exact modular rejection independent of merely observing the nonzero decimal fraction.

## Motivation

This is the first frozen critical-scale object lying simultaneously in:

- the exact two-branch negative-three chart;
- the PR #45 denominator;
- a Euclidean mechanical SLP;
- a proof-carrying local monomial repair circuit;
- a factorwise order cover; and
- an ordinary quotient cylinder.

It is a failed object, but it unifies the two constructive lanes requested by the user and fixes the correct next search coordinate.

## Dependency audit

- `T-8302` supplies the chart/accelerated translation and local swap deltas.
- `L-8303` supplies the quotient residues and real/CRT comparison.
- `X-8302` independently reconstructs every numerical statement.
- Only the five displayed PR #45 factors are reused; they are rechecked directly.

## Gap audit

- `M` is a proper divisor of the enormous denominator.
- The order-cover reconstructs a word but does not annihilate omitted denominator primes.
- The word is refuted and receives no `K-####` identifier.
- The four-list discovery search is not a proof of optimality; many other replacements remain open.

## Adversarial tests

`X-8302` uses an author implementation and an independently written checker. Both rebuild the mechanical word, sites, modular deltas, prime-power quotient rows, CRT residue, and directed real interval.

## Remaining uncertainty

None about the frozen rejection. The full-denominator construction remains open.

## Suggested next attack

Do not optimize numerator divisibility alone. Search replacement circuits against the coupled target

\[
 C_e\equiv ND\pmod {p^{d+e}}
\]

where `N` is the integer selected by the directed real interval. Use Farey-neighbor block transpositions to generate enough zero-first-level Hensel gadgets to control the quotient digits.
