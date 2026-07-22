# L-8302 — Farey-neighbor mechanical blocks have a monomial Collatz commutator

Claim ID: `L-8302`  
Title: Reversing two Farey-neighbor lower mechanical blocks changes the accelerated numerator by one pure `{2,3}`-unit  
Status: `PROPOSED / EXACT REPLACEMENT LEMMA`  
Authoring agent: `gpt56-cycle-02`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: none  
Scope: lower rational mechanical words attached to accelerated valuations `1` and `2`  
Related counterexample candidates: none

## Statement

Let

\[
 0<\frac pq<\frac rs<1,
 \qquad
 rq-ps=1,                                                     \tag{1}
\]

with both fractions reduced. Let `L(p,q)` denote the lower binary mechanical word

\[
 L(p,q)_j=\left\lfloor\frac{(j+1)p}{q}\right\rfloor
          -\left\lfloor\frac{jp}{q}\right\rfloor.             \tag{2}
\]

Put

\[
 U=L(p,q),\qquad V=L(r,s).                                    \tag{3}
\]

Then:

1. the chronological concatenation is the mediant word
   \[
   \boxed{UV=L(p+r,q+s);}                                     \tag{4}
   \]
2. `UV` and `VU` agree at every position except `s-1,s`, where
   \[
   \boxed{UV:\ 01,\qquad VU:\ 10;}                           \tag{5}
   \]
3. attach accelerated valuation `1+epsilon` to binary symbol `epsilon`, and let `C_W` be the standard affine numerator of a valuation word `W`. Then
   \[
   \boxed{
   C_{UV}-C_{VU}
    =-2^{r+s-1}3^{q-1}.}                                     \tag{6}
   \]

Thus a transposition of adjacent standard mechanical blocks preserves total length and valuation exactly while changing the full cycle numerator by one monomial.

### PR #45 specialization

The adjacent fractions

```text
440,541,600,217 / 753,110,839,881,
 80,448,749,305 / 137,528,045,312
```

satisfy determinant one in the order displayed. The PR #45 target decomposes as

```text
4 * lower block + 1 * upper block.
```

Their block commutator has exact magnitude

\[
 \boxed{2^{217976794616}3^{753110839880}.}                    \tag{7}
\]

## Motivation

PR #45 can compile critical mechanical words but originally repaired only individual adjacent letters near one boundary. PR #34 shows that full-denominator construction needs factorwise paths and noncommuting compressed blocks. Equation (6) provides the exact bridge: every Euclidean/Farey scale supplies a proof-carrying replacement whose change is already factored completely over `{2,3}`.

A hierarchy of such transpositions can be evaluated without expanding the underlying trillion-letter blocks and can be passed directly to factorwise Hensel and CRT compilers.

## Proof

Put

\[
 \alpha=\frac{p+r}{q+s}.
\]

For `0<=t<=q`,

\[
 0\le t\left(\alpha-\frac pq\right)
   =\frac{t}{q(q+s)}<\frac1q.
\]

For `0<t<q`, the nonintegral fractional part of `tp/q` is at least `1/q`; hence the displayed perturbation crosses no integer. At `t=q` it gives exactly `p`. Therefore the first `q` symbols of `L(p+r,q+s)` are `L(p,q)`.

For `t=q+u`, `0<=u<=s`,

\[
 (q+u)\alpha-\left(p+\frac{ur}{s}\right)
 =\frac{s-u}{s(q+s)}.                                        \tag{8}
\]

The same fractional-part argument gives the remaining block `L(r,s)`, proving (4).

Now compare `VU` with `L(p+r,q+s)`. For `0<=t<s`,

\[
 \frac{tr}{s}-t\alpha=\frac{t}{s(q+s)}<\frac1s,
\]

so their prefix counts agree. At `t=s`, `VU` has prefix count `r`, while

\[
 \lfloor s\alpha\rfloor=r-1.                                 \tag{9}
\]

For `t=s+u`, `1<=u<=q`,

\[
 (s+u)\alpha-
 \left(r+\frac{up}{q}\right)
 =\frac{u-q}{q(q+s)},                                        \tag{10}
\]

whose magnitude is too small to change the floor for `u<q`, and which is zero at `u=q`. Thus the prefix counts differ only at `t=s`, proving the adjacent transposition (5).

The prefix of `UV=L(p+r,q+s)` before position `s-1` contains

\[
 \left\lfloor\frac{(s-1)(p+r)}{q+s}\right\rfloor=r-1         \tag{11}
\]

ones. Indeed both bounding inequalities follow from `rq-ps=1` and `q-p+s-r>=2`. Consequently its accelerated valuation total before that position is

\[
 (s-1)+(r-1)=r+s-2.                                          \tag{12}
\]

Swapping accelerated letters `(1,2)` to `(2,1)` at position `s-1` changes the numerator by

\[
 3^{(q+s)-(s-1)-2}2^{r+s-2}(2^2-2^1)
 =2^{r+s-1}3^{q-1}.                                          \tag{13}
\]

Since `VU` is obtained from `UV` by that forward swap, (6) follows with the displayed orientation. **QED**

## Dependency audit

Everything is proved from floor arithmetic and the elementary affine numerator formula.

## Gap audit

- A monomial commutator is a replacement primitive, not a full cycle identity.
- Reordering a multiset of two blocks may produce only cyclic rotations when one multiplicity is one; genuinely new circuits require a richer Euclidean hierarchy or at least two copies of each relevant macroblock.
- Divisibility by sampled factors remains insufficient.

## Adversarial tests

`X-8302` checks all 720 oriented Farey-neighbor pairs with denominators at most 36 and verifies both the word identity and the exact numerator difference. It separately checks the trillion-scale determinant and exponent pair in (7).

## Remaining uncertainty

None in the finite identity. Its effectiveness in a full-denominator synthesis is open.

## Suggested next attack

Use the monomial replacements as columns in `L-8303` quotient-target congruences. At each prime power, select block scales whose multiplicative orders differ so that the combined local periods span the primitive word, as required by the cross-prime compiler of PR #34.
