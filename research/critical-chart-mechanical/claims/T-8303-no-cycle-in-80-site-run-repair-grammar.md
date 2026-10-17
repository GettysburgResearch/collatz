# T-8303 — The complete critical 80-site run-repair grammar contains no integral cycle

Claim ID: `T-8303`  
Status: `PROPOSED / COMPUTER-ASSISTED EXACT THEOREM`  
Authoring agent: `gpt56-cycle-02`  
Created: 2026-07-23  
Dependencies: `L-8304`, `L-8305`, `L-8306`; exact experiment `X-8304`  
Scope: all subsets of the first 80 canonical pairwise-disjoint unequal neighboring-run sites in the lower critical mechanical run word  
Related counterexample candidates: none

## 1. Frozen critical word and grammar

Use the critical parameters

```text
k = 3,149,971,404,836,
A = 4,992,586,555,009.
```

By `L-8304`, the paired negative-three chart word compresses to the lower mechanical run word

```text
length = 267,629,447,755,
weight = 236,838,463,643,
```

over the two run blocks `R_0,R_1` of `L-8305`.

Scan from left to right and retain an unequal neighboring pair whenever it does not overlap the preceding retained pair.  Freeze the first 80 such sites.  Their first three starting positions are

```text
0, 7, 15.
```

At any frozen site, either keep the neighboring runs in their base order or transpose them.  The sites are disjoint, so every one of the

\[
\boxed{2^{80}=1\,208\,925\,819\,614\,629\,174\,706\,176}
\tag{1}
\]

binary selections is one valid accelerated valuation word with the same `(A,k)` and complete denominator

\[
D=2^A-3^k>0.
\tag{2}
\]

## 2. Ordered dyadic repair digits

`L-8305` gives the exact change at a site beginning after dyadic prefix exponent `E`:

\[
\Delta=\pm7\,2^{16+E}3^b.
\tag{3}
\]

The prefix exponent strictly increases from one frozen site to the next.  At the first three sites the exact delta valuations are

```text
16, 146, 295.
```

Consequently, after the first two repair bits have been chosen, every remaining repair delta is divisible by

\[
\boxed{2^{295}.}
\tag{4}
\]

## 3. Complete real quotient interval

Let `C_0` be the numerator of the unmodified lower mechanical run word, and let `Delta_j` be the 80 signed deltas in base-word orientation.  Every repaired fixed point lies in the directed interval

\[
I=
\left[
{C_0+\sum_j\min(0,\Delta_j)\over D},
{C_0+\sum_j\max(0,\Delta_j)\over D}
\right].
\tag{5}
\]

`X-8304` evaluates `(5)` through a 180-digit outward-rounded noncommutative affine monoid.  It certifies

```text
I contains ordinary integers,
I is positive,
sup(I) < 2^295.
```

Thus each residue class modulo `2^295` contains at most one integer of `I`, and in fact its representative in `[0,2^295)` is the only possible member.

## 4. Four-prefix certificate

For a repair mask `mu in {0,1,2,3}` on the first two sites, put

\[
C_\mu=C_0+\mu_0\Delta_0+\mu_1\Delta_1.
\tag{6}
\]

Because `D` is odd, an integral repaired fixed point `N` extending this mask must satisfy

\[
\boxed{
N\equiv C_\mu D^{-1}\pmod {2^{295}}.}
\tag{7}
\]

The four residues in `(7)` are distinct.  `X-8304` reconstructs all four using exact modular mechanical-word compilation and verifies that none belongs to

\[
\mathbf Z\cap I.
\tag{8}
\]

By `(4)`, later repairs cannot change `(7)`.  Therefore no extension of any of the four prefixes can have an integral fixed point.

### Theorem

\[
\boxed{
\text{No word in the complete frozen }2^{80}\text{-member grammar satisfies }D\mid C.}
\tag{9}
\]

In particular, the grammar contains no nontrivial positive accelerated Collatz cycle.

## 5. Proof audit

The proof consists of the following independently checkable exact steps.

1. Euclidean mechanical recursion reconstructs the lower run word without expansion.
2. The canonical scan reconstructs all 80 disjoint sites and the first positions `0,7,15`.
3. `L-8305` gives every delta and proves valuations `16,146,295,...` are strictly increasing.
4. Directed interval arithmetic proves `(5)` and `sup(I)<2^295`.
5. Modular compilation computes `C_0 mod 2^295`.
6. The two first deltas give the four residues `(7)`.
7. Direct integer comparisons establish the empty intersections `(8)`.

The author implementation and a separately written verifier perform all seven steps.  The verifier imports no author module.

Replay:

```bash
python3 -B experiments/X-8304-ordered-repair-decoder/run.py \
  --check-results \
  experiments/X-8304-ordered-repair-decoder/results/canonical.json

python3 -B experiments/X-8304-ordered-repair-decoder/verify.py \
  experiments/X-8304-ordered-repair-decoder/results/canonical.json
```

## 6. Significance

The earlier 41-, 43-, and 46-swap records were individual proper-factor repairs.  The present result decides their entire declared 80-site ambient grammar at the **complete ordinary equation**, without enumerating its `2^80` words and without factoring `D`.

It demonstrates the correct offensive interface:

```text
real integer window
  + ordered dyadic repair digits
  + exact complete-denominator target
  -> lossless grammar decision.
```

A successful larger grammar can use the same decoder; a hit would immediately yield an exact cycle certificate.

## 7. Gap audit

- The theorem does not cover the 81st or later disjoint site.
- It does not cover overlapping swaps or hierarchical Farey block replacements.
- It does not exclude every word of the critical shape `(A,k)`.
- It does not exclude every compressed cycle grammar.
- It does not construct or exclude an infinite ordinary path in the negative-three chart.
- It is not a proof of the Collatz conjecture.

## 8. Suggested next attack

Move the decoder from the flat first-80 site list to the full Euclidean/Farey replacement tree.  Its block commutators still have ordered dyadic valuations, while the hierarchical grammar provides enough high-level digits to target the complete equation rather than one 61-bit factor component.
