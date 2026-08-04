# Iteration 08: counterexample-first cycle and complexity barriers

All theorem-level claims remain `PROPOSED` pending independent review. The
finite certificate `X-9507` is an exact computation, not an infinite-orbit
claim. This iteration attacks structured counterexamples directly.

The exact block recurrence is

\[
p_{i+1}=a_{r_i}p_i+1,
\qquad
a_r={3^{2r+1}\over2^{3r+2}},
\tag{1}
\]

with exact positive states

\[
p_i=2^{3r_i+2}u_i,
\qquad u_i\equiv1\pmod4,
\qquad p_i\equiv1\pmod3.
\tag{2}
\]

Put

\[
\kappa={\log(4/3)\over\log(9/8)},
\qquad
K_n=\sum_{i<n}(r_i-\kappa).
\tag{3}
\]

---

## L-9521: a cycle has a small exact minimum

**Claim ID:** `L-9521`  
**Title:** Every positive block cycle has a minimum bounded by its period multiplier  
**Status:** `PROPOSED`  
**Dependencies:** `D-9501`  
**Scope:** positive periodic exact block orbits

### Statement

Suppose an exact positive cycle has block period `L`, letters
`r_0,...,r_(L-1)`, total

\[
R=\sum_{i<L}r_i,
\]

and period multiplier

\[
M=\left({3\over4}\right)^L
  \left({9\over8}\right)^R.
\tag{4}
\]

Then `M<1`, and some state of the cycle is at most

\[
\boxed{{L\over1-M}.}
\tag{5}
\]

Consequently the minimum state of the cycle obeys the same bound. Its outgoing
letter is at least three.

### Proof

Multiplying

\[
{p_{i+1}-1\over p_i}=a_{r_i}
\]

around the cycle gives

\[
M=\prod_{i<L}\left(1-{1\over p_i}\right)<1.
\tag{6}
\]

Let `b_i=log a_(r_i)`. Their cyclic sum is negative. The elementary cycle
lemma, applied to the reversed cyclic word, supplies an index `j` for which
every backward partial sum is nonpositive. Hence every backward partial
product ending just before `j` is at most one.

Unrolling one period backward from `p_j` gives

\[
(1-M)p_j
=1+a_{j-1}+a_{j-1}a_{j-2}+\cdots
 +a_{j-1}\cdots a_{j-L+1}
\le L,
\]

which proves (5).

At the minimum state, the next transition cannot have `r<=2`: direct
substitution in (1), together with the exact lower state in (2), gives
`p_(i+1)<p_i` for each of `r=0,1,2`. Thus the outgoing letter is at least
three. QED.

---

## T-9515: no positive cycle below 2,479,700,525 blocks

**Claim ID:** `T-9515`  
**Title:** Exact ordinary sweep plus Diophantine period compression excludes every positive cycle through 2,479,700,524 blocks  
**Status:** `PROPOSED`, with one internal exact finite dependency  
**Dependencies:** `L-9521`, `X-9506`, `X-9507`; elementary Legendre theorem for continued fractions

### Statement

There is no positive exact H block cycle with

\[
\boxed{L\le2,479,700,524.}
\tag{7}
\]

### Proof

The exact ordinary-state sweep `X-9506` checks every positive exact state

\[
p<B_0,
\qquad
B_0=3\cdot2^{65}=110,680,464,442,257,309,696,
\tag{8}
\]

and finds no cycle.

Assume a cycle of length `L` in the range (7). Let `R/L<kappa` be its mean
letter and put

\[
\epsilon=\kappa-{R\over L}>0,
\qquad
x=L\epsilon\log(9/8).
\]

Then `M=e^(-x)`. By `L-9521`, if the cycle minimum were not covered by
`X-9506`, one would have

\[
{L\over1-e^{-x}}\ge B_0.
\tag{9}
\]

Using

\[
1-e^{-x}\ge{x\over1+x}
\]

and `log(9/8)>1/9`, equation (9) implies

\[
0<\kappa-{R\over L}
<{9\over B_0-L}.
\tag{10}
\]

The endpoint in (7) is the largest integer satisfying

\[
18L^2+L<B_0.
\]

Therefore (10) is strictly smaller than `1/(2L^2)`. After reducing `R/L`,
Legendre's theorem forces it to be a continued-fraction convergent of
`kappa`.

`X-9507` reconstructs the relevant continued-fraction prefix from exact
rational upper and lower bounds for `log(4/3)` and `log(9/8)`. The lower
convergents through the range end with

\[
{2,733,776,749\over1,119,265,172},
\]

while the next convergent is the upper approximation

\[
{27,172,759,629\over11,125,094,063}.
\]

For every lower convergent and every multiple whose denominator is at most the
bound in (7), the same exact certificate proves

\[
{L\over1-M}<B_0.
\]

This contradicts (9). Hence the minimum lies below `B_0`, where `X-9506`
exhaustively proves termination. QED.

### Scope

This is a finite period exclusion, not a proof that no positive cycle exists.
It upgrades the raw period-fourteen word enumeration in `X-9506` by combining
that ordinary-state sweep with the exact minimum bound (5).

---

## L-9522: finite-alphabet entropy--capital barrier

**Claim ID:** `L-9522`  
**Title:** A slowly escaping finite-alphabet survivor must have quantitatively large factor entropy  
**Status:** `PROPOSED`  
**Dependencies:** `T-9502`, `L-9515`

### Definitions

Assume a hypothetical nonperiodic infinite exact orbit. Let its letters lie in
a finite alphabet `A`, with

\[
q=|A|,
\qquad
e_*=\min_{r\in A}(3r+2).
\]

Let `P(ell)` denote the number of distinct itinerary factors of length `ell`,
and let

\[
h=\lim_{\ell\to\infty}{\log P(\ell)\over\ell}
\]

be the factor entropy. Put

\[
H_N=\max_{0\le i<N}K_i,
\qquad
\Gamma=\limsup_{N\to\infty}{H_N\over\log N}.
\tag{11}
\]

### Statement

If `0<Gamma<infinity`, then

\[
\boxed{
h\ge{e_*\log2\over\Gamma\log(9/8)}.
}
\tag{12}
\]

In particular,

\[
\boxed{
\Gamma\ge{e_*\log2\over(\log q)\log(9/8)}.
}
\tag{13}
\]

If `Gamma=0`, no finite-alphabet nonperiodic survivor exists. More generally,
a zero-entropy itinerary cannot be an ordinary survivor when `H_N=O(log N)`.

For the binary alphabet `{2,3}`, equation (13) becomes

\[
\boxed{
\Gamma\ge{8\over\log(9/8)}
=67.9214961256\ldots .
}
\tag{14}
\]

### Proof

`T-9502` gives a bounded positive toll coordinate `Q_i`, so

\[
p_i\le Q_\infty(9/8)^{K_i}.
\tag{15}
\]

If the same factor `w` of length `ell` starts at two distinct positions
`i<j<N`, the exact affine difference formula gives

\[
2^{E_w}\mid p_j-p_i.
\]

The orbit is nonperiodic, so the difference is nonzero. Since every letter of
`w` contributes at least `e_*` to `E_w`,

\[
2^{e_*\ell}
\le |p_j-p_i|
\le2Q_\infty(9/8)^{H_N}.
\tag{16}
\]

Fix `varepsilon>0`. For large `N`,

\[
H_N\le(\Gamma+\varepsilon)\log N.
\]

Choose `N` exponentially in `ell`, with exponent just below

\[
{e_*\log2\over(\Gamma+\varepsilon)\log(9/8)}.
\]

Then (16) forbids any repeated length-`ell` factor among the first `N`
positions. Hence `P(ell)>=N`. Letting the two auxiliary margins tend to zero
proves (12). Since `P(ell)<=q^ell`, equation (13) follows. QED.

---

## R-9505: the natural low-complexity structured candidates are closed

**Claim ID:** `R-9505`  
**Title:** Logarithmically banked Sturmian, automatic, and substitution templates cannot realize an ordinary survivor  
**Status:** `PROPOSED`  
**Dependencies:** `L-9522`

Any finite-alphabet itinerary with zero factor entropy and

\[
\max_{i<N}K_i=O(\log N)
\]

is excluded by `L-9522`. This closes the most economical structured
counterexample templates:

- a critical Sturmian word with sparse logarithmic bank deposits;
- a logarithmically banked Beatty/mechanical word;
- bounded automatic or primitive-substitution templates with only polynomial
  factor complexity;
- lacunary sparse modifications of such words, provided the resulting factor
  entropy remains zero.

This is a method closure, not a statement about every finite-alphabet code.
A structured counterexample with logarithmic capital would need positive
entropy meeting (12); a zero-entropy directive cannot work.

---

## Q-9509: remaining structured counterexample interface

A counterexample can no longer be periodic below the bound (7), and the
low-complexity slow-bank templates above are excluded. A viable structured
counterexample must therefore expose at least one of the following:

1. a nonperiodic finite-alphabet directive with sufficiently large factor
   entropy and capital growth meeting (12);
2. an unbounded-letter reset--renewal directive satisfying the fresh-prime and
   discounted-budget constraints of Iteration 07;
3. an explicit positive integer whose exact carry sequence is eventually zero.

A candidate is not admitted until one finite initialization and an induction
prove exact legality, positivity, and nontermination for every step.