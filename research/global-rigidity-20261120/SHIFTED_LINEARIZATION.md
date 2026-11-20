# Shifting by one changes the adelic product, but leaves two open inputs

**OPEN architecture with exact identities.** This is a further full-proof
attempt, not a conditional inequality presented as a Collatz proof.
Unlike the unshifted pair in [FS3](FIXED_SOURCE_CLOSURE.md), the identity
below no longer supplies the universal unit floor; its stated lower bound
depends on smooth factors. No additional lower bound for actual escaping
orbits is refuted. A power saving requires information that has not been
proved for one arbitrary ordinary source.

Use the hypothetical nonperiodic ordinary odd-unit orbit and notation of
FS2: n_j, a_j, A_j, lambda_j=2^{A_j}/3^j, L_j=lambda_j n_j, and finite
L=lim L_j. The existence of L has exactly the source dependency specified
there. No algebraicity of L is known from these calculations.

## 1. A different affine cancellation

Set
\[
 M_j=\lambda_j(n_j+1),\qquad
 \mathcal P_j=(L-L_j)/\lambda_j.
\]
The shift removes the affine translation on every valuation-one step:
\[
 M_{j+1}-M_j=\frac{\lambda_j}{3}(2^{a_j}-2).             \tag{1}
\]
Since M_j tends to L, its exact future defect is
\[
 L-M_j=\frac13\sum_{i\ge j}\lambda_i(2^{a_i}-2)
       =\lambda_j(\mathcal P_j-1).                      \tag{2}
\]
Thus this is not merely the previous product with a different name: every
future gap-one letter contributes zero to (2).

Let s_j=v_2(n_j+1), t_j=v_3(n_j+1), and k_j=min(j,t_j). Define the
primitive integer pair
\[
 p'_j=\frac{2^{A_j}(n_j+1)}{3^{k_j}},\qquad
 q'_j=3^{j-k_j},\qquad H'_j=\max(p'_j,q'_j).             \tag{3}
\]
The gcd before normalization is exactly 3^{k_j}. This formula covers
t_j>j: then q'_j=1 and p'_j has 3-adic valuation t_j-j. In every case
\[
 v_2(p'_j)=A_j+s_j,\quad v_2(q'_j)=0,\quad
 v_3(p'_j)=t_j-k_j,\quad v_3(q'_j)=j-k_j.
\]
The two p-adic maximum norms of this primitive pair are one.

At infinity take the forms LX-Y and X on (X,Y)=(q'_j,p'_j), and at two
and three take X and Y. Their unnormalized product is exactly
\[
 \begin{split}
 \mathcal P'_j
 &=|Lq'_j-p'_j|q'_j\,2^{-A_j-s_j}
                  3^{-j-t_j+2k_j}\\
 &=\frac{\mathcal P_j-1}{2^{s_j}3^{t_j}}
   =\frac{L-M_j}{\lambda_j2^{s_j}3^{t_j}}.              \tag{4}
 \end{split}
\]
The common 3-power cancels across the real and 3-adic factors. It must
still be removed when computing the projective height H'_j.

The first future gap greater than one occurs after exactly s_j-1
valuation-one letters. Equation (1) therefore gives only
\[
 \mathcal P'_j\ge3^{-s_j-t_j}>0,                        \tag{5}
\]
whose displayed lower bound can shrink as the smooth factors of n_j+1
grow. This does not establish actual small products along any escaping
ordinary orbit. The unshifted product is always greater than one.

## 2. The exact hypotheses that would turn this into a contradiction

The elementary growth bound n_j+1<=(3/2)^j(n_0+1) implies
\[
 q'_j=3^{j-k_j}\ge\frac{2^j}{n_0+1},                    \tag{6}
\]
so H'_j tends to infinity even with the possible ternary cancellation.
Indeed 3^{k_j}<=3^{t_j}<=n_j+1, which proves (6).

If both of the following were proved for every hypothetical escaping
ordinary source, the two-dimensional Subspace Theorem would exclude it:

1. Its limiting real number L is algebraic, so the two forms at infinity
   are fixed algebraic forms.
2. For some eta>0, infinitely many j satisfy
   \[
    \mathcal P_j-1
      \le2^{s_j}3^{t_j}(H'_j)^{-\eta}.                  \tag{7}
   \]

Then the normalized product is at most (H'_j)^{-2-eta}. The primitive
pairs would lie in finitely many rational lines. Each rational line
contains at most two primitive integer points, while (6) gives unbounded
height, a contradiction. This is only a conditional implication.
Neither item 1 nor item 2 is established here.

Condition (7) asks for the smooth part of one ordinary n_j+1 to dominate
a weighted sum of *all* its future non-one gaps by a power of the
correct primitive height. Finite residue recurrence does not give this
estimate. Long valuation-one blocks and compressed words do yield
related small-product mechanisms; this overlaps the explicitly scoped
results in PR145 at `dd245a712f985909f541590e3f6c179b7ba011e4`,
`research/unsafe-return-weights/VALUATION_ONE_RUNS.md` and
`research/pointwise-run-defects/COMPRESSED_DESCENT.md`. Those sources do
not give (7) for an unrestricted escaping orbit.

## 3. Targeted attempts to remove the two assumptions

One might replace L by a known algebraic constant c to remove item 1.
For any fixed real c!=L, the product of the same shifted forms is
\[
 \mathcal P'_j(c)=
 \frac{|c-M_j|}{\lambda_j2^{s_j}3^{t_j}}
 \ge\frac{|c-M_j|}{M_j},                               \tag{8}
\]
because 2^{s_j}3^{t_j}<=n_j+1. Since M_j tends to L>0,
\[
 \liminf_j\mathcal P'_j(c)\ge |c-L|/L>0.
\]
Thus no fixed algebraic target different from the actual limit can
supply a power saving. Choosing a new algebraic approximation c_j at
each j instead makes the forms move; its coefficient heights require
new estimates. No such estimates are supplied here.

To remove item 2, the identity (2) supplies positivity and a lower bound,
whereas the needed statement is an upper bound coupled to the smooth
part of n_j+1. The exactly linearized gap-one runs alone are finite at
every ordinary state. The next valuation at least two restarts a positive
defect, and later defects remain unrestricted. No monotone ordinary
rank or deterministic descent estimate follows from this cancellation.

These calculations delimit a real change of architecture while keeping
the two global inputs visible. They neither prove that L is algebraic
nor that it is transcendental, and they do not establish any ordinary
escaping orbit. A full solution would need additional arithmetic beyond
these identities, or a different object entirely.

## 4. Exact finite controls

`check_shifted_linearization.py` checks primitive normalization, including
t_j>j, on actual finite ordinary prefixes. Its eventual valuation-one
tail is explicitly a *formal* continuation used to give an exact
rational value for L in the algebraic checks; it is not asserted to be
the actual continuation. The checker asserts (5) only when the observed
actual prefix already contains the first gap greater than one. It does
not test or claim either open hypothesis above.

The replay passed 17,008 primitive-product checks from 667 ordinary odd
ternary-unit sources up to 2,000, with actual prefixes of at most 100 odd
steps. It included 10,747 nontrivial ternary cancellations, 683 cases
with t_j>j, 16,341 observed first-defect lower bounds, and 51,024
fixed-target inequality checks. Normal and `-OO` reports were
byte-identical in `shifted-linearization-report.json`.
