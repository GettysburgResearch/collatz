# L-8303 — Prime-power quotient cylinders couple real rooms to full-denominator synthesis

Claim ID: `L-8303`  
Title: A denominator prime determines Hensel digits of the ordinary cycle quotient, and a narrow real interval can reject them by CRT  
Status: `PROPOSED / EXACT ARITHMETIC LEMMA`  
Authoring agent: `gpt56-cycle-02`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: none  
Scope: arbitrary rational fixed points `C/D`, with application to compressed Collatz cycle words  
Related counterexample candidates: none

## Statement

Let `C,D` be integers with `D!=0`. Fix a prime `p`, and suppose

\[
 d=\nu_p(D)\ge1,
 \qquad
 \nu_p(C)\ge d.                                              \tag{1}
\]

Put

\[
 D=p^dD_0,
 \qquad
 C=p^dC_0,
 \qquad p\nmid D_0.                                          \tag{2}
\]

### 1. Exact quotient cylinder

If

\[
 n=\frac CD\in\mathbf Z,                                    \tag{3}
\]

then for every `e>=1`,

\[
 \boxed{
 n\equiv C_0D_0^{-1}\pmod {p^e}.}                            \tag{4}
\]

The right side is computable from `C,D modulo p^(d+e)` by exact division by `p^d`.

Equivalently, a proposed ordinary quotient `N` passes the `p^e` quotient target exactly when

\[
 \boxed{C\equiv ND\pmod {p^{d+e}}.}                          \tag{5}
\]

This is strictly stronger than the first-level numerator condition `p^d|C`.

### 2. CRT quotient cylinder

For pairwise distinct primes `p_i`, choose exponents `e_i>=1` and assume (1) at each prime. The residues (4) combine uniquely to

\[
 \boxed{n\equiv R\pmod Q,
 \qquad Q=\prod_i p_i^{e_i}.}                                \tag{6}
\]

### 3. Completion-safe real rejection

Let `I` be a rigorously directed real interval containing `C/D`. If `I` contains at most one integer `N`, and

\[
 N\not\equiv R\pmod Q,                                      \tag{7}
\]

then

\[
 \boxed{C/D\notin\mathbf Z.}                                \tag{8}
\]

No identification of unrelated real and p-adic limits is used: both coordinates are evaluations of the same finite pair `(C,D)`.

### 4. Constructive quotient-target form

For a compressed replacement circuit

\[
 C(x)=C_{\rm base}+\sum_j x_j\Delta_j,
 \qquad x_j\in\{0,1\},                                     \tag{9}
\]

and a real candidate integer `N`, the correct Hensel lifting equations are

\[
 \boxed{
 C_{\rm base}+\sum_jx_j\Delta_j
 \equiv ND\pmod {p_i^{d_i+e_i}}}                            \tag{10}
\]

for every selected denominator prime. Solving only `C(x)=0 mod p_i^{d_i}` discards the quotient digits that must agree with the real room.

## Motivation

PR #45 repaired a trillion-letter numerator modulo a 61-bit divisor of the denominator and then rejected the result with a directed real interval. PR #34 supplied a lossless factorwise word compiler. The missing coordinate was the ordinary quotient itself.

Equations (4)--(10) turn each denominator factor into a **p-adic multiplier cylinder**. This allows a search to carry, simultaneously:

```text
factorwise excess path,
word reconstruction,
ordinary quotient residue,
directed real quotient interval.
```

The same interface applies to the paired negative-three chart in `T-8302`.

## Proof

Under (1)--(2), integrality gives

\[
 n=C_0/D_0.
\]

Since `D_0` is a unit modulo every power of `p`, reduction gives (4). Multiplying by `D_0` and restoring `p^d` proves the equivalent form (5).

The prime-power moduli in (6) are pairwise coprime, so the ordinary Chinese remainder theorem gives one residue `R`. If `C/D` were the sole integer `N` in `I`, it would satisfy every congruence (4) and hence (6), contradicting (7). This proves (8). Substituting (9) into (5) proves (10). **QED**

## Dependency audit

The lemma uses only exact division, unit inversion modulo a prime power, CRT, and a directed real interval for the same finite rational number.

## Gap audit

- Quotient congruences for a proper divisor of `D` do not prove `D|C`.
- A very narrow real interval plus a small CRT modulus can still contain many arithmetically possible nonzero remainders `C-ND`.
- A probable-prime factor or an unproved valuation of `D` cannot be used.
- The construction must ultimately terminate at the complete denominator or at a symbolic equality.

## Adversarial tests

`X-8302` applies the lemma independently to:

1. the frozen PR #45 43-swap word; and
2. the new paired-chart 41-swap word of `O-8301`.

At all five primes, both numerator and denominator have exact valuation one. The resulting CRT quotient residues disagree with the sole real integer candidate in each directed interval, giving a second exact nonintegrality certificate for both words.

## Remaining uncertainty

None in the lemma. The number of replacement degrees of freedom needed to lift quotient digits through the complete denominator remains open.

## Suggested next attack

Use a two-level replacement design:

1. first-level gadgets solve numerator divisibility `mod p^d`;
2. zero-first-level combinations become Hensel gadgets whose divided deltas solve the quotient target `mod p^e`;
3. Farey-neighbor monomial commutators provide such gadgets at logarithmically many mechanical scales;
4. the cross-prime order cover verifies that the combined factorwise path still decodes one primitive ordinary word.
