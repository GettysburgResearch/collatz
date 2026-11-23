# All terminal choices, the optimal selector, and forced denominator cost

23 November 2026. **The universal small-candidate construction remains OPEN.**

This attack varies the entire triadic candidate, rather than extending
only the previous terminal values one and two. The resulting minimum
retains the unchanged ordinary source and the improved PR176 horizon.
Two exact deductions identify what this broader search can and cannot
do: the quadratic denominator order is forced for every separable
all-state product of the relevant form, and every fixed nontriadic
rational target forces exponential cost for **all** triadic candidates.
The latter strengthens the restriction to one prescribed periodic
terminal stream. Neither deduction supplies the missing ordinary-source
small-residue estimate.

## 1. Frozen inputs and the fully optimized search

Use the literal shortcut map, `T(x)=x/2` on even inputs and
`T(x)=(3x+1)/2` on odd inputs. Fix one positive ordinary `n`, put
`x_K=T^K(n)`, `e_K=x_K mod 2`, and

\[
b_K=\sum_{j<K}(1-e_j),\qquad D_0=0,\qquad
D_{K+1}=3^{1-e_K}D_K+(1-e_K)2^K.
\tag{1}
\]

PR176 at `fb402404deb810bd8e32e596993739bb5a6967d1`,
`research/lean-global-resolvent-20261121/overview/triadic-height/TRIADIC_AMORTIZED_BUDGET.md`,
Sections 1--4, supplies the written sufficient certificate with

\[
F(0)=1,\qquad F(r)=\prod_{j<r}(1+3^j),\qquad
H(n,a,r)=9\operatorname{bl}\bigl(n\max(1,|a|)F(r)\bigr)+1.
\tag{2}
\]

Here `bl(B)` is the least positive `E` with `B<2^E`. A candidate
`a/3^r` passing the first `H(n,a,r)` complementary-parity tests forces
the original source to reach one by that clock. We use the pinned
written argument; this module does not re-formalize that theorem or
rebuild its dependency tree.

The fixed-denominator arithmetic is already derived in PR182 at
`a7fd3ac9e5bff7412858df23d776bb847e9c1371`,
`research/whole-repo-round3-20261123/TRIADIC_CLOSURE.md`, Sections 4
and 6. For `K>=1`, let

\[
\omega_K\equiv-3^{-b_K}D_K\pmod{2^K},\qquad
a_{K,r}=\operatorname{center}_{2^K}(3^r\omega_K),
\tag{3}
\]

where the centered representative belongs to
`[-2^(K-1),2^(K-1))`. Negative powers in (3) mean modular inverses.
Every compatible numerator is exactly `a_(K,r)+2^K z`, `z in Z`.
Thus the complete optimization for the new budget is

\[
\boxed{M_K(n)=\min_{r\ge0}
 F(r)\max(1,|a_{K,r}|).}
\tag{4}
\]

This minimum exists and is effectively finite. The choice `r=0` gives
`M_K<=2^(K-1)`, whereas `F(r)>=2^r`. No exponent with
`F(r)>2^(K-1)` can improve that bound. More strongly,
`F(r)>=3^(r(r-1)/2)` gives an `O(sqrt K)` exponent budget.
Reducing a numerator divisible by three strictly improves its cost
when `r>0`; the zero rational likewise has its cheapest representation
at exponent zero. Hence a minimizing rational can be taken in lowest
triadic terms.

The legal candidate sets are nested with `K`, so `M_K` is nondecreasing.
This follows also directly from (1): `omega_(K+1)=omega_K mod 2^K`.
The improved certificate has a successful candidate at clock `K` if
and only if

\[
\boxed{9\operatorname{bl}(nM_K(n))+1\le K.}
\tag{5}
\]

This is an exact optimization of an existing sufficient criterion,
not a new unconditional convergence theorem. Varying arbitrary signed
terminal values, including terminal triadic denominators, does not
create an extra free parameter in (4): after intersection with the
prescribed initial grid, its pullbacks are precisely the classes (3).

The construction sought a positive-source bound on (4), sufficient for
(5). Centering alone gives a numerator with roughly `K` bits; its
guarantee does not meet the clock charged by (2). No estimate better
than that guarantee was obtained for every fixed ordinary source.

## 2. Quadratic denominator order is forced in the separable product class

A possible escape from the restrictive exponent budget was to replace
`F(r)` by an exponentially smaller denominator weight. Consider any
positive weight `G(r)` for which

\[
                         P(x,w,r)=x|w|G(r)
\tag{6}
\]

is nonincreasing on every legal nonterminal paired step. The integer
pair represents `(x,w/3^r)`, with opposite parities, and the
original-even, positive-denominator step is

\[
(x,w,j+1)\longmapsto
\left(x/2,(w+3^j)/2,j\right).
\tag{7}
\]

Use `w=1`. Take `x=4` if `j` is even and `x=6` if `j` is odd.
The numerator `(1+3^j)/2` is odd in the first case and even in the
second, so **both** consecutive parity tests pass. The original states
are respectively `4 -> 2` and `6 -> 3`, all positive and nonterminal.
The nonincrease condition gives, after canceling the positive `x`,

\[
                    (1+3^j)G(j)\le4G(j+1).
\tag{8}
\]

Multiplying (8) for `j=0,...,r-1` yields

\[
\boxed{F(r)G(0)\le4^rG(r).}
\tag{9}
\]

Consequently every such weight obeys

\[
\boxed{\log_2G(r)\ge
 \frac{r(r-1)}2\log_2 3-2r+\log_2G(0).}
\tag{10}
\]

Thus PR176's quadratic logarithmic denominator order, including its
leading quadratic coefficient, cannot be removed by changing only
the denominator weight in this class. An exponential weight `c^r`
cannot be nonincreasing at every required step. The room in (10)
relative to `F(r)` is at most linear in `r` at logarithmic scale.

The statement concerns a family of legal candidates at the two known
ordinary sources four and six. It does not identify them as successive
states on one trajectory, or as the optimal candidates for an escaping
source. It leaves open nonseparable potentials, candidate-specific
estimates, and arguments that allow increases between longer blocks.
The finite product implication (8)--(9), for natural weights, is
checked in Lean; the same written multiplication proof works for
positive real weights. No universal selector estimate follows from it.

## 3. An exponential lower bound for every triadic match to a rational target

Let `alpha=u/d` be a reduced rational 2-adic integer, with `d>0` odd,
and suppose `d` has a prime factor other than three. Do **not** assume
an arbitrary ordinary source has such a rational dual. This section
is a conditional rational-target calculation.

If `a/3^r` agrees with `alpha` through `K` bits, then

\[
                       2^K\mid da-u3^r.
\tag{11}
\]

The integer on the right is nonzero: otherwise coprimality of `u,d`
would make `d` divide `3^r`. Therefore

\[
                       2^K\le d|a|+|u|3^r.
\tag{12}
\]

The new denominator weight satisfies the useful uniform inequality

\[
                         2\,3^r\le3F(r).
\tag{13}
\]

At `r=0` this is immediate, and at `r=1` equality holds. Every
following factor `1+3^r` is at least three, so induction proves (13).
Put `B=F(r)max(1,|a|)`. Since `|a|<=B`, (12)--(13) give

\[
\boxed{2^{K+1}\le(2d+3|u|)B.}
\tag{14}
\]

This bound is uniform over **every** exponent, numerator, terminal
choice, and terminal denominator. In particular, if `M_K(alpha)`
denotes (4) with `omega_K=alpha mod 2^K`, then

\[
\boxed{\frac{2^K}{d+\tfrac32|u|}\le M_K(\alpha)
       \le2^{K-1},\qquad
       \lim_{K\to\infty}\frac{\log_2M_K(\alpha)}K=1.}
\tag{15}
\]

This is elementary rational height separation specialized to the new
weight, not an imported irrationality theorem. The finite inequalities
(12)--(14) are checked in Lean with nonzero cross-product and congruence
as explicit hypotheses. The rational-target interpretation, (15), and
the application to hypothetical cycles have written-proof scope.

For a nontrivial positive integer cycle, the complementary dual is
rational by the exact periodic affine formula. The preceding triadic
convergence theorem implies that its reduced denominator cannot be a
power of three. Hence (15) applies. Merely allowing a different
triadic terminal value or denominator cannot make a periodic dual's
optimal cost subexponential. This conclusion does not rule out the
cycle; that still requires a separate arithmetic contradiction.

By contrast, if `alpha` itself is triadic, the legal costs are bounded
by the cost of that fixed rational. Since each bounded cost sublevel
contains only finitely many rationals, for all sufficiently large `K`
the minimum is exactly its reduced-representation cost. If `alpha` is
irrational, the same finite-sublevel argument gives `M_K(alpha)->infinity`,
with no uniform rate. No argument here determines the case for an
arbitrary fixed positive ordinary `n`.

## 4. Trying arbitrary odd denominators

Allowing a general odd denominator `q` changes the approximation target
to

\[
a\equiv q\omega_K\pmod{2^K}.
\tag{16}
\]

The rational obstruction above disappears when `q=d` and `a=u`:
the cross-product becomes zero. This is why a general rational-dual
certificate can be a distinct route to eventual periodicity, with
positive-cycle classification left as a separate task.

However, the elementary pigeonhole construction needs its denominator
and precision qualifications. Taking a close pair among
`j omega_K mod 2^K`, `0<=j<=Q`, with `1<=Q<2^K`, gives integers

\[
1\le q\le Q,\qquad |a|\le\lceil2^K/Q\rceil,
\qquad a\equiv q\omega_K\pmod{2^K}.
\tag{17}
\]

The resulting `q` need not be odd. If `v=v_2(q)<K`, division by
`2^v` gives an odd denominator but only a `K-v` bit match. The
clock loss cannot be omitted from a finite certificate.

There is no uniform same-clock odd-denominator version of the small
numerator guarantee in (17). Take
`omega_K=2^(K-1)-1`. For every odd `q` with
`1<=q<=Q<2^(K-1)`, its centered numerator is

\[
\operatorname{center}_{2^K}(q\omega_K)=2^{K-1}-q.
\tag{18}
\]

It is far from zero when `Q` is small. This residue actually has
complementary original word `0^(K-1)1`, whose least positive ordinary
source is `n=2^(K-1)`. Its bit length is `K`; it is **not** an example
inside a funded small-source horizon. Thus (18) does not refute a
source-specific construction. It identifies why that construction
requires information beyond an unrestricted residue argument.

Likewise, even when a supplied odd-denominator approximation has the
guaranteed size `2^K/Q`, a certificate charging a fixed multiple
greater than one of its numerator bit length, together with a polynomial
cost in `Q`, is not automatically funded by taking `Q` polynomial
in `K`. This compares the guarantee with the needed budget; it is
not a lower bound on the error of a fortunate actual approximation.

## 5. Other direct tests and the remaining step

I also checked the latest actual-parity Borel--Dwork setup in PR175,
`53ba1e1ffc46bf022433c2124a62682ad8dd4739`,
`research/lean-global-closure-20261121/risk24/literature/BOREL_DWORK_ACTUAL_PARITY_ATTEMPT.md`.
Its rational 2-adic value at two is already derived from the same
ordinary source, and later-state values are shifts of that one
specialization. They do not produce new interpolation abscissae.
No additional meromorphic continuation or algebraicity hypothesis
was obtained in this attack, and none is imported into (4).

The negative part of a signed paired trajectory does allow a smaller
local product cost: while `w` and its next numerator remain negative,
an original-even denominator drop decreases `x|w|` by at least a
factor four. A sign change occurs at most once. This does not pay
for the following positive fractional phase, where (7) can recharge
the numerator from one to `(1+3^j)/2`. The legal states in Section 2
make that obstruction explicit for the separable proposal.

The unresolved inference is a bound on the actual minimum (4) strong
enough to force (5), or a sufficiently small general odd-denominator
approximation at its **own** certified clock. No such estimate was
proved. The new results constrain complete candidate selection and a
whole class of potential improvements; they do not present those
constraints as a solution of the universal existence problem.

## Formal scope

[WeightedSelector.lean](lean/WeightedSelector.lean) defines the
denominator weight and proves five finite statements: positivity,
the power/weight comparison, nonzero congruence separation, its
weighted triadic consequence, and the forced weight-growth product.
[WeightedSelectorAudit.lean](lean/WeightedSelectorAudit.lean) audits
all five authored theorem declarations. The optimization, asymptotic
classification, actual-step interpretation, and approximation attempts
above are written mathematics. No universal small-candidate assertion
is added as an axiom or a formal theorem.
