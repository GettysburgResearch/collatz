# The location of the minimum gives exact multiplier-cost refinements

**PROPOSED, source-qualified necessary condition for unbounded cycle
families.** This note adds arithmetic information to the abstract box
in [SQUARE_OBSTRUCTION.md](SQUARE_OBSTRUCTION.md). It does not contradict
that box certificate: the box uses upper multiplier costs, whereas the
ordinary word supplies parity counts that can lower the actual costs.

The conclusion is a restriction on possible limiting profiles. It is
not an effective exclusion of all cycles in a finite size range, nor a
proof that the remaining profiles are ordinarily realizable.

## MD-001: statement with all normalization choices

Suppose an unbounded sequence of primitive positive ordinary shortcut
cycles admits a cyclic parity factorization

\[
W_1^2W_2^2W_3^2V^2,
\]

where the three `W_i` factors increase, `V^2` decreases, and the global
least phase lies in the last copy of `V`. Start the tour at the exit
`x` of `V^2` and put `H=log_2(x+1)`. Let `w_i,q_i` be the widths and
weights of the three rising roots. Along any subsequence on which the
normalized quantities converge, write

\[
g_i=\lim\frac{cq_i-w_i}{H},\qquad
r_i=\lim\frac{w_i-q_i}{H},\qquad c=\log_2 3,\quad\gamma=c-1.
\]

Thus `r_i` counts even inputs per unit `H` in one copy of root i.
Assume the limiting gain vector belongs to the closed box

\[
\left\|g-(1/2,1/2,1)\right\|_\infty\le1/100.
\tag{1}
\]

Split the last copy of `V` as `A B`, where the path enters the minimum
immediately after `A`. Define

\[
a=\lim\frac{\#\{\text{odd inputs in }A\}}H,\qquad
b=\lim\frac{\#\{\text{even inputs in }B\}}H,\qquad
\kappa=\gamma a+b.
\tag{2}
\]

The position of the split, the root words, and all these counts may
vary along the sequence. After choosing a subsequence the limits exist
because their normalized widths are bounded. Then necessarily

\[
2r_1+\kappa
\le 2+g_1+g_2+g_3-
       \frac{3+3g_1+g_2+g_3}{c}
<\frac{11191}{48500}<\frac14.
\tag{3}
\]

In particular the limiting fraction of even inputs in the first rising
root is less than

\[
\frac{2003189}{19971815}<0.101.
\tag{4}
\]

This identifies an unresolved class of words: the first rising root
must be dominated by odd inputs, and the descending root must have
few odd inputs before the least phase and few even inputs after it,
in the weighted sense of (3). Counts tending to zero after division
by `H` may still be unbounded; they cannot be deleted from the word.

## 1. Why the polynomial-height minimum is used

The powered-block bounds in [PROOF.md, Section 1](PROOF.md) give
`L=O(H+1)` for this four-factor tour. Thus `H` tends to infinity and
`log L=o(H)`. Rhin's logarithmic-form input gives
`log(m+1)=O(log L)` for the global least phase `m`. It follows that

\[
\frac{\log_2(m+1)}H\longrightarrow0.
\tag{5}
\]

The ordinary multiplicative correction over any part of a primitive
tour has logarithm `O(log L)=o(H)`. This follows from the distinct-phase
product estimate (6) in that proof. Every normalized physical height
change therefore equals its homogeneous change in the limit.

Put

\[
h_0=1,\qquad h_i=h_{i-1}+2g_i,\qquad
D=(h_3-1)/2=g_1+g_2+g_3.
\]

In box (1), all rising gains and the descending drop are bounded away
from zero. Their leading displacement monomials consequently dominate
their companions exponentially. This strict positivity is needed for
the exact limiting identities below.

## 2. The multiplier costs are exact functions of the parity defects

Let `M_i` be the positive integer multiplier of rising square i and
let `P` be that of `V^2`, as in the endpoint-bracket identities.
Write `mu_i=lim log_2(M_i)/H` and `p_0=lim log_2(P)/H`. Define the
old upper costs

\[
u_i=h_{i-1}-\frac{2-c}{\gamma}g_i,
\qquad u_P=D+1-\frac c\gamma.
\]

Then the following are **equalities**, not just upper bounds:

\[
\boxed{\quad
\mu_i=u_i-\frac c\gamma r_i,\qquad
p_0=u_P-\frac c\gamma\kappa.
\quad}
\tag{6}
\]

For a rising square with entry `x_i` and exit `y_i`, the exact
displacement is `y_i-x_i=M_i(3^(q_i)+2^(w_i))`. Since `g_i>0`,
`y_i` dominates `x_i`, and `3^(q_i)` dominates `2^(w_i)`. Hence

\[
\mu_i=h_i-c\lim(q_i/H).
\]

The exact count identity `cq_i-w_i=gamma q_i-(w_i-q_i)` gives
`lim(q_i/H)=(g_i+r_i)/gamma`. Substitution yields the first equality
in (6).

For the descending root let `v,p` be its width and odd count. The
square displacement is `y-x=P(2^v+3^p)`. Here `D>0`, so the entry `y`
and the term `2^v` dominate. Using `h_3=1+2D` and
`lim(v/H)=c lim(p/H)+D` gives

\[
p_0=1+D-c\lim(p/H).
\tag{7}
\]

Now the suffix `B` carries the polynomial-height minimum to `x`.
By (5) and the `o(H)` correction estimate, its normalized homogeneous
gain tends to one. If `q_B` and `z_B` count its odd and even inputs,
this says

\[
\gamma\lim(q_B/H)-\lim(z_B/H)=1.
\]

Since `p=q_A+q_B`, definitions (2) imply

\[
\gamma\lim(p/H)=1+\gamma a+b=1+\kappa.
\tag{8}
\]

Combining (7) and (8) proves the second equality in (6). This is the
point where the location of the ordinary global minimum improves the
boundary-only model. Without (5), an additional normalized minimum
height would remain in (8).

There is also an exact finite identity behind the minimum split.
If `n` is the phase at the same root offset in the preceding copy of
`V`, `beta=|B|`, and `q_A` is the prefix's odd count, then

\[
n-m=P2^\beta3^{q_A}.
\tag{9}
\]

Indeed the first-copy endpoint drop is `P2^v`; applying the common
prefix `A` to the two endpoints multiplies their difference by
`3^(q_A)/2^(|A|)`. This proves (9) without an approximation. The local
checker replays this identity and the exact suffix product on ordinary
finite segments.

## 3. A positive margin really excludes an ordinary limiting profile

Transport **both** displacement terms of the first rising square
through `W_2^2W_3^2`. Let

\[
Q=\frac{3^{2q_2+2q_3}}{2^{2w_2+2w_3}},\qquad
R_0=QM_1 3^{q_1},\qquad R_1=QM_1 2^{w_1},\qquad S=P2^v.
\]

The three guaranteed relative savings for the comparison
`R_0+R_1-S` are `2g_1`, `D`, and `h_1/c`. The box has

\[
2g_1\le1.02<1.97\le D,\qquad
2g_1\le1.02<1.98/c\le h_1/c.
\]

Thus the relative error is at most `2^(-2g_1 H+o(H))`. Its saving
`2g_1` is strictly greater than the gap `g_1` between `R_0` and `R_1`.
The fixed three-coordinate comparison lemma in
[PROOF.md, Section 3](PROOF.md) therefore applies whenever

\[
2\mu_1+p_0<2g_1.
\tag{10}
\]

For completeness, the Subspace-Theorem conclusion in this case is
the exact equality `QM_1(3^(q_1)+2^(w_1))=P2^v` along an infinite
subsequence. The sum in parentheses is odd. The 2-adic valuation
would force

\[
\mu_1\ge\lim(v/H)\ge c/\gamma+D.
\]

This contradicts `mu_1<=u_1` throughout the box. With the outward
constant `C=485/306`, the difference between the divisibility lower
bound and the upper cost is at least `36043/8950>4`. The intervening
denominator `2^(2w_2+2w_3)` strengthens the contradiction; it is not
dropped with an incorrect sign. Thus (10) excludes an actual unbounded
ordinary-cycle family, not merely a formal charge assignment.

Using the exact cost refinement (6), failure of (10) requires

\[
2r_1+\kappa
\le\frac\gamma c(2u_1+u_P-2g_1)
=2+g_1+g_2+g_3-
       \frac{3+3g_1+g_2+g_3}{c}.
\]

This proves the first inequality in (3). The expression increases
with c; for `C=485/306>c`, its maximum on the box occurs at
`g=(49/100,51/100,101/100)` and equals `11191/48500`. The inequality
is strict for the actual c. A simpler robust exclusion follows from
`2r_1+kappa>=1/4`: the charge margin is then at least
`467/8950>1/20` throughout the box.

Finally (3) gives `r_1<11191/97000`. The first root's limiting even
fraction is

\[
\frac{r_1}{\lim(w_1/H)}
=\frac{\gamma r_1}{g_1+cr_1}.
\]

It increases with c and `r_1`, and decreases with `g_1`. Substituting
the outward bounds `C`, `r_1=11191/97000`, and `g_1=49/100` gives
the fraction in (4).

## 4. Exact finite checks and evidence boundary

Command actually run from the repository root on 20 November 2026:

```sh
python -X utf8 -B research/independent-attack-20261120/check_minimum_defect.py
```

Exit status: `0`.

```text
maximum necessary weighted-defect threshold: 11191/48500
quarter-height defect charge margin: 467/8950
divisibility margin: 36043/8950
first rising root even-density ceiling: 2003189/19971815
ordinary minimum-split replays: 186
negative control: zero-defect abstract profile not excluded
PASS: minimum-location refinement constants and exact local identities
```

The checker evaluates the affine extrema at all eight box vertices
with rational arithmetic, verifies the source/transport/descending
error ordering and the divisibility margin, and tests the exact local
identities on every contracting binary root of widths 1 through 7
with its two-copy ordinary realization. It does not generate cycles,
prove that actual multiplier costs attain the old upper bounds, or
implement the analytic Subspace Theorem.

The external inputs are exactly those identified in [PROOF.md,
Section 7](PROOF.md): a polynomial least-phase bound from the cited
logarithmic-form theorem and the rational p-adic Subspace Theorem.

## What remains

The abstract zero-defect profile at the box's center still fails the
charged comparison, as the checker explicitly confirms. Normalized
defects equal to zero can conceal a growing sublinear number of
exceptional parity inputs. We do not replace such words by a literal
run of ones or a literal descent followed by ascent. Controlling that
remaining small-defect class, or extracting further relations among
its integer multipliers, is the next unsupported step.
