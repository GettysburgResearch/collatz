# Restricting the global argument to a least bad component

**Status: the floor supplies a genuine finite run budget, but the needed
all-source estimate remains unproved.** This continuation uses the exact
ordinary floor from PR176 and the new written rigidity result from PR180.
It adds no Lean theorem and makes no full-convergence claim.

## The invariant support and what the floor actually removes

Let `T` be the ordinary shortcut map, and suppose that its positive
nonconvergent set `S` is nonempty. Write `N=min S`. Then

\[
f(n)=\mathbf 1_S(n),\qquad f(Tn)=f(n),\qquad f(n)=0\quad(0<n<N).
\]

The exact floor in
[PR176](https://github.com/GettysburgResearch/collatz/blob/d2303ea3144ba652d089c1ec38ad3879c3ea5ef7/research/lean-global-resolvent-20261121/EXACT_FORWARD_FLOOR.md)
identifies this situation with a least forward failure, without losing
height in the floor. The argument below only needs the displayed floor and
invariance; it does not assume any unproved congruence restriction on `N`.

For the accelerated odd map `U`, every legal predecessor of an odd member
of `S` belongs to `S`. Consequently, if

\[
(B_Sh)(m)=
\sum_{\substack{a\ge1,\ I_a(m)\text{ positive odd integer}\\I_a(m)\in S}}
\frac{81}{16^a}h(I_a(m)),\qquad I_a(m)=\frac{2^a m-1}{3},
\]

then **every term of the full operator survives at each endpoint in `S`**.
In particular,

\[
B^j\mathbf 1_S(m)=\mathbf 1_S(m)B^j1(m)
\]

for every finite `j` and every positive odd `m`. Restricting to the bad
support is legitimate and can eliminate the full-state counterexamples in
the companion note. It does not itself add a loss factor to an inverse row
whose endpoint is bad.

## A positive ordinary resource for cheap inverse runs

Consider `k` successive legal exponent-one inverse steps beginning at an
odd endpoint `m` in `S` and ending at `n`. Exact affine iteration gives

\[
n+1=(2/3)^k(m+1).
\]

Since `n>=N`, this gives the finite resource bound

\[
\boxed{(3/2)^k\le\frac{m+1}{N+1}.}
\]

Thus the least bad floor really does bound the length of every such run at
a bounded relative ordinary height. This is more information than the
formal ternary valuation alone.

There is also a useful local descent in the minimal inverse choices. If a
nonempty exponent-one run of length `k` can be followed by an exponent-two
inverse step, the resulting integer is

\[
I_2(I_1^k(m))=\frac43(2/3)^k(m+1)-\frac53<m.
\]

Both identities are elementary written consequences of the affine maps.
Neither asserts that every inverse itinerary is a sequence of these
descending excursions. Consecutive exponent-two steps and larger legal
exponents can increase height and replenish the available run budget. No
global accounting inequality paying those increases was obtained.

## What remains missing for the Green potential

Let `G(m)=sum_(j>=0) B^j1(m)` as in the companion note. Invariance gives

\[
G_S(m):=\sum_{j\ge0}B_S^j1(m)=G(m)\qquad(m\in S).
\]

The restriction therefore inherits the known fifth-denominator mass
bound. The second-denominator estimate

\[
\sum_{\substack{m\in S\\m\text{ odd}}}\frac{G(m)}{m^2}<\infty
\]

has not been proved. The lower endpoint bound `m>=N` does not upgrade the
fifth-denominator estimate: the factor that must be controlled is `m^3`,
which is unbounded on `S`. An estimate for the full-state weight family is
not being used to rule out this component-specific possibility.

## Effect of the latest predecessor-density result

At PR180 commit `995ae97b10e851e4f91f7c74395a5b28bcacfebc`,
[LINEAR_BLOCK_ATOM_FLOOR.md](https://github.com/GettysburgResearch/collatz/blob/995ae97b10e851e4f91f7c74395a5b28bcacfebc/research/lean-ordinary-closure-20261121/LINEAR_BLOCK_ATOM_FLOOR.md)
derives positive lower logarithmic predecessor density using Tao's stated
fine-scale mixing theorem. Its
[rigidity corollary](https://github.com/GettysburgResearch/collatz/blob/995ae97b10e851e4f91f7c74395a5b28bcacfebc/research/lean-ordinary-closure-20261121/REPOSITORY_RIGIDITY_COROLLARY.md)
removes the former separate component-density hypothesis: a metric-valued
ordinary invariant label with finite five energy at any exponent
`0<s<=1` must be constant. These are written analytic dependencies of
PR180, not declarations checked by this Lean project.

For the Boolean label above, the first missing estimate is now exactly

\[
\boxed{
E_5(1;f)=
\sum_{\substack{x>0\\x\text{ odd},\ 3\nmid x}}
\frac{|\mathbf1_S(5x)-\mathbf1_S(x)|}{x}<\infty.
}
\]

The floor proves that the summand vanishes when `5x<N`. Beyond that
initial region, boundedness of the label gives only the divergent
harmonic majorant. For example, defining the actual dyadic shell charges

\[
\eta_j=
\sum_{\substack{2^j\le x<2^{j+1}\\x\text{ odd},\ 3\nmid x}}
\frac{|\mathbf1_S(5x)-\mathbf1_S(x)|}{x},
\]

the floor annihilates finitely many initial `eta_j`; no summable bound for
the remaining actual charges has been established. The predecessor
density theorem supplies a contradiction **after** that summability is
proved. It supplies no upper bound for these boundary charges by itself.

The current global routes therefore still require an all-source tail or
energy estimate. The exact floor and the new density input sharpen where
that estimate must act; they do not establish it.
