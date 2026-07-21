# D-9303 — Stationary triadic mirror measure

**Claim ID:** D-9303  
**Title:** The admissible Cantor classes are finite reductions of one fixed Bernoulli self-similar measure on `Z_3`  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** elementary `3`-adic convergence and valuation algebra  
**Scope:** stationary form of the issue-#4 Cantor-class/room refinement  
**Related counterexample candidates:** none

## Statement

Put

\[
\lambda=\frac{81}{64},
\qquad
c=-\frac{17}{64}.
\]

For a binary sequence

\[
\eta=(\eta_0,\eta_1,\ldots)
\in\{0,1\}^{\mathbb N},
\]

define

\[
\boxed{
\pi_3(\eta)
=
\sum_{r\ge0}c\eta_r\lambda^r
=
-17\sum_{r\ge0}
\frac{81^r}{64^{r+1}}\eta_r
\in\mathbb Z_3.
} \tag{1}
\]

Let `nu` be the pushforward of fair Bernoulli measure under `pi_3`, and let

\[
W=\pi_3(\{0,1\}^{\mathbb N})
\subset\mathbb Z_3.
\]

Then:

1. the series `(1)` converges in `Z_3` and `pi_3` is continuous;
2. `pi_3` is injective, and if two sequences first differ at index `r`, then
   \[
   \boxed{
   v_3\!\left(\pi_3(\eta)-\pi_3(\eta')\right)=4r;
   } \tag{2}
   \]
3. `W` is the unique compact set satisfying
   \[
   \boxed{
   W=K_0(W)\sqcup K_1(W),
   \qquad
   K_\varepsilon(y)=\lambda y+c\varepsilon;
   } \tag{3}
   \]
4. `nu` satisfies the exact Hutchinson equation
   \[
   \boxed{
   \nu=\frac12(K_0)_*\nu+rac12(K_1)_*\nu;
   } \tag{4}
   \]
5. for every `j >= 1`, define the finite reduction
   \[
   C_j=
   \left\{
   \sum_{r=0}^{j-1}c\eta_r\lambda^r
   \pmod{81^j}:
   \eta_r\in\{0,1\}
   \right\}.
   \tag{5}
   \]
   Then `|C_j|=2^j`, `C_1={0,1}`, and
   \[
   \boxed{
   C_j=
   \left\{
   \frac{81x-17\varepsilon}{64}
   \pmod{81^j}:
   x\in C_{j-1},
   \ \varepsilon\in\{0,1\}
   \right\}.
   } \tag{6}
   \]

Thus the depth-dependent Cantor classes used in the issue-#4 room refinement are the successive finite quotients of one fixed triadic Bernoulli system.

## Definitions

All rational coefficients in `(1)` lie in `Z_3` because `64` is a `3`-adic unit. Moreover

\[
|\lambda|_3=|81/64|_3=3^{-4}=1/81.
\]

The word *mirror* refers to the exchange of roles between the two places:

- the survivor coding `D-9301` contracts by `64/81` in `Z_2`;
- the Cantor coding here contracts by `81/64` in `Z_3`.

No claim of probabilistic independence from the survivor coding is built into this definition.

## Motivation

The issue-#4 interchange work refined small survivors into a `2`-adically prescribed core `R_n` and an `81`-adically prescribed Cantor class set `C_j`. Its transform was then written as a second finite product. The finite products strongly suggest a stationary object, but that object had not been isolated in the same language as the fixed `Z_2` measure of `D-9301`.

Definition `(1)` supplies the missing fixed object. It permits one to treat the survivor and room/Cantor sides as Fourier coefficients of two stationary measures rather than two unrelated triangular arrays.

## Proof or construction

### Convergence and continuity

The `r`-th summand in `(1)` has valuation

\[
v_3(c\eta_r\lambda^r)
\ge4r.
\]

Hence the series converges in `Z_3`, uniformly in the digit sequence. Uniform convergence of the finite-prefix maps proves continuity.

### Exact separation

Suppose `eta` and `eta'` first differ at index `r`. Then

\[
\pi_3(\eta)-\pi_3(\eta')
=
c\lambda^r
\left(
\eta_r-\eta'_r
+
\lambda u
\right)
\]

for some `u in Z_3`. The first term in parentheses is `+1` or `-1`, while `lambda u` is divisible by `81`. Therefore the parenthesis is a `3`-adic unit. Since `c` is also a unit,

\[
v_3(\pi_3(\eta)-\pi_3(\eta'))=v_3(\lambda^r)=4r.
\]

This proves `(2)` and injectivity. It also shows that the two first-level images in `(3)` are disjoint.

### Self-similarity

Split off the first digit:

\[
\pi_3(\eta)
=c\eta_0+
\lambda\pi_3(\sigma\eta).
\]

This gives `(3)`. Applying fair Bernoulli measure to the same decomposition gives `(4)`.

### Finite reductions

If two length-`j` words first differ at index `r<j`, equation `(2)` gives valuation `4r<4j`, so their residues modulo

\[
81^j=3^{4j}
\]

are distinct. Hence `|C_j|=2^j`.

For `j=1`,

\[
c=-17\cdot64^{-1}\equiv1\pmod{81},
\]

because `64^{-1}=19 (mod 81)`. Thus `C_1={0,1}`.

Finally, split a length-`j` digit sequence at its first digit:

\[
\sum_{r=0}^{j-1}c\eta_r\lambda^r
=
c\eta_0+
\lambda
\sum_{r=0}^{j-2}c\eta_{r+1}\lambda^r.
\]

Writing the tail reduction as `x in C_(j-1)` gives

\[
c\eta_0+\lambda x
=
\frac{81x-17\eta_0}{64},
\]

which is exactly `(6)`. QED.

## Dependency audit

- No issue-#4 theorem is needed for the construction or proof.
- The final identification with the branch's `C_j` uses the same displayed recursion and base set; it is a notation crosswalk, not a proof dependency.
- No Fourier theorem, mixing theorem, or external self-similar-measure theorem is invoked.

## Gap audit

- Stationarization does not prove equidistribution of `C_j` in archimedean order.
- The measure is singular with respect to Haar measure on `Z_3`; it has only `2^j` classes modulo `81^j`.
- The shared arithmetic constant `17` does not imply that the `Z_2` and `Z_3` codings are independent when driven by related words.
- A fixed triadic measure does not by itself control the room index in the real ordering.
- The word order in `(5)` is the reverse of some low-word conventions; the set is unchanged because all binary words are present. Any pathwise coupling must freeze the order explicitly.

## Adversarial tests

1. `C_1={0,1}` because `-17/64=1 (mod 81)`.
2. For two words differing first at position `r`, their residues agree modulo `81^r` but not modulo `81^(r+1)`.
3. The all-zero word gives the triadic point `0`.
4. The all-one word gives
   \[
   \sum_{r\ge0}c\lambda^r
   =\frac{c}{1-\lambda}=1
   \]
   in `Q_3`, so the two trivial endpoints are again `0` and `1`.
5. Formula `(6)` preserves integrality in `Z_3` because `64` is a unit.

## Remaining uncertainty

The construction is complete-looking. Independent review should check the word-order crosswalk against `EQ-INTERCHANGE.md`; the set and measure are unaffected by reversal under fair independent digits, but a deterministic room-path statement is order-sensitive.

## Suggested next attack

Evaluate the Fourier transform of `nu` at the moving characters `psi/81^j`. This gives the exact finite Cantor product and, together with `L-9301`, produces a stationary two-place factorization for the CRT comparison sets.