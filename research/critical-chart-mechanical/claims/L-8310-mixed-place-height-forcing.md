# L-8310 — Mixed-place height forcing for a critical chart quotient

**Claim ID:** `L-8310`  
**Status:** `PROPOSED / EXACT HEIGHT REDUCTION`  
**Authoring agent:** `gpt56-cycle-02`  
**Created:** 2026-07-23  
**Dependencies:** `T-8302`; the frozen rational logarithm enclosure in `X-8307`  
**Scope:** finite critical paired-chart words with the PR #45 parameters  
**Related counterexample candidates:** none; `R-8301` excludes the previously reported small ladder quotient

## 1. General mixed-place lemma

Let a paired chart word have

\[
 D=2^A-3^K>0,
 \qquad
 x=\frac{C}{D},
\]

and let `N` be an ordinary integer. Put

\[
 R=C-ND.
\]

Assume that positive integers `B,J,u,v,b` satisfy

\[
 |x-N|<2^{-u},
\]

\[
 D<2^{A-v},
\]

\[
 2^B M^J\mid R,
 \qquad
 M>2^b.
\]

If

\[
 \boxed{B+bJ\ge A-u-v,}
\tag{1}
\]

then

\[
 \boxed{C=ND.}
\tag{2}
\]

### Proof

The real estimate gives

\[
 |R|=D|x-N|<2^{A-u-v}.
\]

If `R` were nonzero, divisibility would give

\[
 |R|\ge 2^B M^J>2^{B+bJ}\ge2^{A-u-v},
\]

which is impossible. Hence `R=0`. **QED**

## 2. Critical-scale constants

For the frozen parameters

```text
A=4,992,586,555,009,
K=3,149,971,404,836,
M=1,465,129,870,107,858,983,
```

put

\[
 \theta=A\log2-K\log3.
\]

`X-8307` proves by exact rational logarithm enclosures that

\[
 0<\theta<2^{-41}.
\]

Since

\[
 D=2^A(1-e^{-\theta})
\]

and `1-e^(-theta)<theta`, one has

\[
 \boxed{D<2^{A-41}.}
\tag{3}
\]

The reported real gap for the small attempted quotient

```text
N_ladder=110,340,992,901,879
```

is bounded above by

\[
 \frac{472855261523}{2\cdot10^{24}}<2^{-41}.
\]

Thus every word satisfying that same real bound obeys

\[
 \boxed{|C-ND|<2^{A-82}.}
\tag{4}
\]

Also

\[
 M>2^{60}.
\]

Consequently the exact coarse closing condition is

\[
 \boxed{B+60J\ge A-82.}
\tag{5}
\]

With no dyadic contribution (`B=0`), it is sufficient to reach

```text
J=83,209,775,916.
```

The range-reduced exact logarithm calculation in `X-8307` improves the sufficient pure-`M` exponent to

```text
J=82,733,048,428.
```

The difference between these values is only a constant-factor sharpening. Both show that an odd-prime lift through seven or ten levels is nowhere near a global height closure.

## 3. Full physical replay makes odd-prime lifting unnecessary

Suppose an ordinary integer `N` follows the complete advertised paired-chart word. Equivalently, the corresponding accelerated word replays every valuation from `n=2N+1`.

Then the full affine identity gives

\[
 \boxed{2^A\mid C-ND.}
\tag{6}
\]

If additionally

\[
 \left|\frac CD-N\right|<1,
\]

then

\[
 |C-ND|<D<2^A.
\]

Together with (6), this forces `C=ND` immediately.

Therefore the shortest honest height certificate is not an eighty-billion-level lift at the five known odd factors. It is:

```text
one ordinary integer N,
complete compressed dyadic branch replay,
a real interval of width below one.
```

The odd-prime quotient cylinders remain useful as pruning and as a mixed-place supplement when only a long prefix—not the full word—has been replayed.

## 4. Prefix tradeoff

If the first `L` chart blocks replay from `N`, with dyadic depth

\[
 B=\sum_{j<L}(4-e_j),
\]

then `2^B|C-ND`. Thus every certified physical prefix replaces exactly `B` bits of the odd-prime height burden in (5).

This supplies a quantitative design rule:

> do not spend Hensel levels at odd primes while leaving the candidate outside the first dyadic chart cylinder.

## Gap audit

- The lemma is an implication, not a construction of `N` or a chart word.
- A congruence modulo a proper odd factor does not certify any advertised Collatz valuation.
- The real and `2`-adic statements concern the same finite rational pair `(C,D)`; no cross-completion limit is identified.
- The source of the real gap must be outward-rounded or exact.
- `R-8301` shows that `N_ladder` fails before this height lemma can be applied.

## Suggested next attack

Build the packet solver in the product state

```text
(real interval,
 dyadic physical-prefix residue and depth B,
 odd-prime quotient residue and depth J).
```

Accept a word only when (5) closes. A full dyadic replay with a unit real interval is already a complete finite cycle certificate.