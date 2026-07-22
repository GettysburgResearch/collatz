# LIT-KTHM-0051 — The prime `233` excludes the complete `(k,A)=(8,13)` accelerated-cycle packet

**Type:** exact finite arithmetic certificate with a complete dynamic-programming proof interface.  
**Maps to:** issue #9, issue #41, `SYN/L-9904`, and the proof-producing positive-cycle verifier.

## 1. Accelerated cycle equation

For a positive valuation word

```text
w=(a_0,...,a_(k-1)),
a_i>=1,
A_j=sum_(i<j)a_i,
A=A_k,                                                    (1)
```

the odd accelerated map has affine form

```text
2^A S^k(x)=3^k x+C(w),
C(w)=sum_(j=0)^(k-1)3^(k-1-j)2^(A_j).                   (2)
```

A positive cycle requires

```text
D(k,A)=2^A-3^k>0,
D(k,A) divides C(w).                                     (3)
```

The repository's `SYN/L-9904` proves that `(3)` then supplies the exact positive replay and that repeated words reduce to their primitive root.

## 2. Frozen packet

Set

```text
k=8,
A=13.
```

Then

```text
D(8,13)=2^13-3^8=1631=7*233.                            (4)
```

There are

```text
binom(12,7)=792                                          (5)
```

ordered positive compositions of `13` into `8` parts. Since `gcd(8,13)=1`, every such word is primitive; modulo cyclic rotation this packet contains `792/8=99` primitive necklaces.

## 3. Residue dynamic program

For `0<=ell<=8` and `ell<=s<=13`, let `R_(ell,s)` be the set of residues modulo `233` attained by `C(v)` for all length-`ell` positive words `v` of total valuation `s`.

Initialize

```text
R_(0,0)={0}.                                             (6)
```

Appending a positive part `a` to a word of current total `s` gives

```text
C(va)=3C(v)+2^s.                                        (7)
```

Therefore the exact recursion is

```text
R_(ell+1,s+a)
 contains {3r+2^s mod233:r in R_(ell,s)},                (8)
```

for every `a>=1` compatible with the final total `13`. Conversely every positive composition is obtained exactly once by these append operations, so `(6)`–`(8)` are exhaustive.

## 4. Exact final certificate

Iterating `(8)` gives

```text
R_(8,13)=(Z/233Z) minus {0,138}.                         (9)
```

Equivalently, its 233-bit characteristic mask, with residue `r` stored in bit `r`, is

```text
0x1fffffffffffffffffffffffbfffffffffffffffffffffffffffffffffe.   (10)
```

In particular,

```text
C(w) not congruent to 0 mod233                           (11)
```

for every one of the `792` valuation words.

### Reproducible standard-library checker

```python
from collections import defaultdict

P = 233
state = {(0, 0): {0}}
for ell in range(8):
    nxt = defaultdict(set)
    for (e, s), residues in state.items():
        if e != ell:
            continue
        max_a = 13 - s - (8 - ell - 1)
        for a in range(1, max_a + 1):
            for r in residues:
                nxt[(ell + 1, s + a)].add((3*r + pow(2, s, P)) % P)
    state.update(nxt)

assert state[(8, 13)] == set(range(P)) - {0, 138}
```

The induction behind `(8)` proves that this finite computation covers the declared packet; no orbit heuristic is used.

## 5. Consequence

The prime factor `233` of the cycle denominator already obstructs every word, so

```text
boxed:
there is no positive accelerated Collatz cycle with
(k,A)=(8,13).                                           (12)
```

No factor or replay check at the second denominator prime `7` is needed.

## 6. Literature and project boundary

Hercher's theorem excludes every nontrivial positive cycle with at most `91` local minima. A length-eight valuation word has at most eight local minima, so `(12)` is not a new global cycle bound. Its value is methodological:

- it is a complete proof-producing packet;
- it tests primitive-necklace normalization;
- it demonstrates that one denominator prime can close an entire fixed-parameter family;
- and it supplies a regression control for the active smooth-denominator searches.

A constructive search must move beyond the known local-minimum frontier and must report the local-minimum parameter rather than substituting accelerated length.

## 7. Nonconsequences

The finite exclusion proves no statement about cycles outside `(8,13)`, divergent orbits, or the Collatz conjecture.