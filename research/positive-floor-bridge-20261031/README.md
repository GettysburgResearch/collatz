# A positive-floor bridge for prescribed-depth inverse transport

**Status: PROPOSED local deductions, with proofs. The infinite-state Collatz
instantiation is SOURCE-QUALIFIED. Collatz is not resolved.**

This pass continues the recovered [inverse Green manuscript](../beeping-density-swarm-20261031/INVERSE_GREEN.md)
at PR142's frozen head `d0f48c472d45a336e9083b37b45e1a8d39a2cf16`.
It closes a specific conditional gap: an endpoint-uniform positive floor for
a superharmonic reference function upgrades averaged inverse budgets to
prescribed-depth budgets, even when the residual depth varies independently
at every leaf of a prefix-free frontier. The same hypothesis supplies the
inverse-exponent tail bound that was missing from IFT-006.

There is an important attribution boundary. The pinned external manuscript
already states pointwise first-hit bounds, a canonical harmonic trace, and a
uniform positive trace floor. We do **not** claim to discover these results,
to verify their external theorem chain, or to prove the uniform floor from
the older target-dependent lower bound. The contribution here is the short
explicit domination argument, its arbitrary leaf-clock formulation, its
connection to this repository's contact lift, and its sharp zero-clock
obstruction. These are elementary positive-operator arguments, not a new
general optional-stopping principle.

## 1. Map, operator, and all quantifiers

Let O be the positive odd integers. Use the **unabsorbed** Syracuse map

\[
 U(x)=(3x+1)/2^{a(x)},\qquad a(x)=v_2(3x+1),\qquad b(x)=3/2^{a(x)}.
\]

Thus U(1)=1 and b(1)=3/4. Define the nonnegative inverse operator

\[
 (Lf)(t)=\sum_{U(x)=t}b(x)f(x),\qquad \rho_q=L^q\mathbf1,\quad\rho_0=1.
\tag{1}
\]

The inverse letters at t are the positive integers a for which
x_a=(2^a t-1)/3 is a positive odd integer. Their weights are 3/2^a.
There are no inverse letters when 3 divides t. All series are nonnegative
series; finite values will be proved where used.

An inverse word w is traversed from its root t outward to its leaf s_w.
Its length is |w|, and its weight is B(w), the product of its letter
weights. A family W of finite legal words from **one fixed root** is
prefix-free when no distinct member is a prefix of another. It may be
finite or countably infinite, may have unbounded depth, and need not be a
complete frontier. The empty word is allowed, but then a prefix-free family
containing it has no other word. A residual clock is an integer q(w)
assigned separately to each leaf. It is not the total length |w|+q(w).

## 2. PFB-001: a uniform floor gives prescribed-depth and adaptive-clock budgets

**Hypotheses.** Let h:O -> [0,infinity) be finite at each point, satisfy

\[
 Lh\le h,
 \qquad h(t)\ge\alpha>0\quad\hbox{for every }t\in O\hbox{ with }3\nmid t.
\tag{2}
\]

The constant alpha is independent of the target. No lower bound at
multiples of three is required; no summability of h is assumed.

**Conclusions.** For every t in O and every q>=1,

\[
 \boxed{\rho_q(t)\le {2\over\alpha}h(t).}
\tag{3}
\]

For every prefix-free W rooted at t and every assignment q(w)>=1,

\[
 \boxed{\sum_{w\in W}B(w)\rho_{q(w)}(s_w)
       \le {2\over\alpha}h(t).}
\tag{4}
\]

The bound has no maximum frontier depth, maximum leaf height, or common
residual-clock requirement.

**Proof.** Sum the geometric series of legal first letters:

\[
 \rho_1(t)=\begin{cases}
 0,&t\equiv0\pmod3,\\
 1,&t\equiv1\pmod3,\\
 2,&t\equiv2\pmod3.
 \end{cases}
\tag{5}
\]

Consequently rho_1 <= (2/alpha)h. Positivity and Lh<=h give
rho_q=L^(q-1)rho_1 <= (2/alpha)L^(q-1)h <= (2/alpha)h.
This proves (3).

For a finite prefix-free family, expand its finite prefix tree. At every
internal node the sum of the charges of the selected children is at most
the full Lh charge, and hence at most h of that node. Induction from the
leaves gives

\[
 \sum_{w\in W}B(w)h(s_w)\le h(t).
\tag{6}
\]

For a countable family apply this to each finite subfamily and take the
supremum. Applying (3) separately at each leaf proves (4). This argument
allows omitted branches and repeated integer states at different word
positions. It does not identify words merely because their endpoints
coincide. QED.

## 3. PFB-002: uniform inverse-tail control and harmonic Abel limits

Under (2), for every 0<z<1 define

\[
 A_z(t)=(1-z)\sum_{q\ge0}z^q\rho_q(t).
\tag{7}
\]

Equation (3) proves finiteness and the estimate

\[
 A_z(t)\le (1-z)+{2z\over\alpha}h(t).
\tag{8}
\]

At any fixed root t, truncating the inverse letters above m yields

\[
 \boxed{\sum_{a>m\text{ legal}}{3\over2^a}A_z(x_a)
 \le 3\,2^{-m}+{2\over\alpha}
              \sum_{a>m\text{ legal}}{3\over2^a}h(x_a).}
\tag{9}
\]

Both terms on the right tend to zero as m tends to infinity, **uniformly
in z**. Indeed Lh(t)<=h(t)<infinity. The first term uses the full, possibly
larger, geometric sum over all a>m. This is fixed-root inverse-tail
uniformity, not a uniform estimate over all moving roots.

**Harmonic limit statement.** If a sequence z_j increases to 1 and
A_(z_j) has a pointwise limit k, then Lk=k.

To prove this, Tonelli and the power series give the exact resolvent identity

\[
 LA_z={A_z-(1-z)\over z}.
\tag{10}
\]

Pointwise convergence passes through each finite head of the inverse sum.
Equation (9) controls the remaining tail uniformly in j. The same bound
controls the tail of the limit, either by Fatou or by (8). Therefore the
left side of (10) converges to Lk; the right side converges to k. QED.

**Useful bootstrap.** Suppose instead that a finite pointwise Abel
subsequential limit g is already known and satisfies the uniform floor in
(2), but harmonicity is not known. Fatou applied to (10) first gives Lg<=g.
Now use h=g in PFB-001 and (9), and repeat the preceding argument. This
proves Lg=g without assuming the equality in the bootstrap.

No convergence of individual rho_q, uniqueness of subsequential limits,
effective convergence rate, or computability of g follows from this argument.
A polynomially decaying lower bound h(t)>=c*t^(-14/11), such as that in the
recovered IFT-006, is **not** the uniform positive floor in (2).

## 4. PFB-003: source-qualified application and the actual transported pairing

### External input, explicitly not independently established here

The source is Lucas Valbuena's `paper/tao-basin-densities.tex`, frozen at
`x1xhlol/collatz-two-coordinate-obstruction@a7275d5a73814d3d9a400c6fe6577de9542b03a3`,
Git blob `63ca82653986b0dfa4c54bac17ed80199b806448`.
The relevant statements are:

* `thm:ct-canonical-identification`: a finite canonical normalized Abel
  limit g of the actual rho sequence exists.
* `prop:ct-uniform-canonical-floor`:
  g(t)>=alpha=3*delta/(128*K_seed*P0)>0 whenever 3 does not divide t,
  with delta=log(4/3)/2 and constants independent of t.

The printed floor depends on the manuscript's preceding weighted-density
construction, a uniform inverse-linear basin lower bound, and external
coalescence and predecessor inputs. The current pass inspected the named
TeX statements and their local proofs, **not** their entire source chain or
Lean development. It therefore treats them as premises. In particular,
`varrho` in the external weighted construction is not silently identified
with the stationary sequence `rho` used here.

Conditional on these inputs, Fatou supplies Lg<=g and PFB-001--002 give

\[
 Lg=g,\qquad
 \sum_{w\in W}B(w)\rho_{q(w)}(s_w)\le {2\over\alpha}g(t),
 \quad q(w)\ge1.
\tag{11}
\]

The external source also proves first-hit depth bounds in
`prop:ct-first-hit-depth-bound`. Thus prescribed-depth scalar control and
canonical harmonicity are not presented as new external discoveries. The
explicit arbitrary leaf-clock formulation in (11) is the local bridge to
the earlier repository packet.

### An explicit root-only upper bound from the recovered packing estimate

IFT-003 gives

\[
 \sum_{q=0}^Q\rho_q(t)
 \le\kappa_t\left[t(1+Q\log96)+{9\over8}(64/81)^Q\right],
\tag{12}
\]

where kappa_t=1 for a nonperiodic target, and kappa_t=(1-eta)^(-1)
for a periodic target of cycle weight eta. Always kappa_t<=3t+1.
Applying elementary Abel summation to (12) gives

\[
 g(t)\le\kappa_t t\log96\le t(3t+1)\log96.
\tag{13}
\]

For completeness, if S_Q is the cumulative sum, then
A_z=(1-z)^2 sum_(Q>=0) z^Q S_Q. The constant and geometric-tail terms
in (12) vanish as z increases to 1, while the linear-Q term tends to
kappa_t*t*log96. The Q=0 term may be enlarged without changing the limit.
Consequently (11) has the explicit, root-only bound

\[
 {2\log96\over\alpha}t(3t+1).
\tag{14}
\]

The root-only right side does not decide whether the root converges.

Let A be any nonnegative population on O with finite moments
M_1=sum_t t A(t) and M_2=sum_t t^2 A(t). Then (3) and (13) give

\[
 \boxed{\sup_{q\ge1}\sum_t A(t)\rho_q(t)
 \le {2\log96\over\alpha}(3M_2+M_1).}
\tag{15}
\]

This can be applied to the positive computable contact occupation lift
A_6 from CT-004--005, restricted to odd states: its proved second height
moment is finite because 6>2*log(2)/log(4/3)+1/2. The earlier pairing
controlled a depth average. Equation (15), conditional on the external
floor, controls each prescribed positive depth. More generally, any
prefix-free frontier at each populated root, with arbitrary positive leaf
clocks, has the same moment-summed bound by (4).

This is still the **Jacobian-weighted inverse operator L**, not the
unweighted killed shortcut/contact operator K_C. The distinction is not
removed by choosing the actual occupation lift. No contraction factor below
one, survivor decay, or termination theorem is proved by (15).

## 5. PFB-004: an unconditional synchronized-clock budget

There is an unconditional companion statement. For every integer N>=0 and
any prefix-free W at root t,

\[
 \boxed{\sum_{w\in W,\ |w|\le N}B(w)
                   \rho_{N-|w|}(s_w)\le\rho_N(t).}
\tag{16}
\]

Here a residual clock of zero is allowed, because the **total** depth is
fixed. Expand each rho on the left into its inverse histories. Concatenating
with w gives a depth-N inverse word at t. Two different members of W cannot
produce the same completed word, since that would make one a prefix of the
other. Weights multiply exactly. Thus the left side counts a subset of the
nonnegative terms on the right. Finite truncations and monotone limits
justify countably many words and unbounded inverse exponents. QED.

Equation (16) does not bound the sequence rho_N uniformly in N. It must not
be substituted for (4) when the residual depths are assigned independently.

## 6. PFB-005: why zero residual clocks are a genuine obstruction

At t=3, rho_0(3)=1 and rho_q(3)=0 for every q>=1. Its normalized Abel
limit is g(3)=0, since A_z(3)=1-z. Therefore (4) with h=g cannot be
extended to q(w)=0, already for the singleton empty-word frontier at 3.

There is a stronger obstruction **conditional only on a positive Abel
residue at one unit root**. Let d(x)=1 when 3 divides x and zero otherwise.
For a unit t, dead-leaf predecessors satisfy
2^a t=1 mod 9, which is one class a=a0 mod 6 with 1<=a0<=6. Hence

\[
 Ld(t)={3\,2^{-a_0}\over1-2^{-6}}
       ={3\,2^{6-a_0}\over63}
       \ge {\rho_1(t)\over21}.
\tag{17}
\]

For t=0 mod 3 both sides are zero. To check the constant, if t=1 mod 3
then a0 is even and rho_1=1; the smallest ratio occurs at a0=6.
If t=2 mod 3 then a0 is odd and rho_1=2; the smallest ratio occurs at
 a0=5. Both ratios equal 1/21.

Positivity therefore gives L^q d>=rho_q/21 for all q>=1. If g(t)>0 is
an Abel subsequential limit at t, the sum of rho_q(t) cannot be finite:
a finite sum would force A_z(t) to zero. Thus

\[
 \sum_{q\ge1}L^q d(t)=\infty.
\tag{18}
\]

Every word counted in this sum ends at a multiple of three and so has no
legal inverse extension. The collection of all these words is prefix-free.
Its **unweighted terminal charge**, sum_w B(w)rho_0(s_w), is infinite.
Finite subfamilies consequently have arbitrarily large total charge.

This is not evidence against Collatz. It proves that unrestricted
zero-step terminal charges cannot be supplied by any finite root-only
budget on these frontiers when the positive-residue premise holds. The
positive-clock guard is doing real mathematical work.

## 7. Evidence, review boundary, and the first unsupported step

The [verifier](../../experiments/positive-floor-bridge-20261031/check_positive_floor.py)
uses exact rational arithmetic. Infinite geometric first-letter and ternary
residue-law tails are summed analytically. It tests the synchronized-clock
inequality, first/dead profiles, and the positive-floor theorem on exact
finite killed models whose superharmonic function is computed by finite
path decomposition and geometric cycle renewal. These finite models are
**not evidence that the infinite canonical floor holds**. Prefix overlap
and the zero-clock root provide explicit negative controls.

The proof was written and checked in a single assistant session. No new
independent agent review or proof-assistant certification is claimed. See
[the review checklist](REVIEW.md), [execution receipts](../../reports/positive-floor-bridge-20261031/README.md),
and the package recovery notice for the separate historical reviews.

**First unsupported step for an unconditional use of (11)--(15):** establish
or independently certify the named external canonical-limit and uniform-floor
premises, with their actual source dependencies. PFB-001--002 are implications
from those hypotheses, not a substitute proof of them.

**Remaining full-Collatz step even granting those premises:** convert this
weighted inverse control into a bound for actual unweighted persistent
survivors or prove global forward trace sublinearity and separately exclude
nontrivial cycles. Fixed-root inverse-tail tightness is not uniform forward
sublinearity. Finite weighted occupation, harmonicity, and the budget above
are compatible with periodic behavior. We have not proved those final
conditions.
