# First-hit packing, harmonic transport, and positive-source Green bounds

**Status: PROPOSED, with proofs; Collatz remains OPEN.** This continuation
improves the previous fixed-depth estimate to a uniform bound on depth
averages and supplies an actual transported inequality. It concerns the
Jacobian-weighted inverse operator defined below, not the unweighted killed
operator in the project's full-convergence criterion. The distinction is
essential: the weighted operator can have finite Green values even on a
positive cycle.

The base is PR142 at `d0f48c472d45a336e9083b37b45e1a8d39a2cf16`.
Its `NEGATIVE_SPIKE_BARRIER.md`, DSP-005, proved
`rho_q(t) <= 6qt+(64/81)^q`. Summing that bound loses a second factor of
depth. The main step of this continuation is injectivity **across different depths** after
first-hit reduction, followed by exact cycle renewal.

## 1. Map, operator, paths, and conventions

Let O be the positive odd integers and

\[
U(x)=\frac{3x+1}{2^{a(x)}},\qquad a(x)=v_2(3x+1),
\qquad b(x)=\frac3{2^{a(x)}}.
\]

The map is unabsorbed: `U(1)=1`, `a(1)=2`, and `b(1)=3/4`.
For nonnegative functions on O put

\[
(Lf)(t)=\sum_{U(x)=t}b(x)f(x).
\tag{1}
\]

Equivalently the sum runs over positive `a` with `3 | 2^a t-1`, using
`x=(2^a t-1)/3` and weight `3/2^a`. It is zero when `3|t`.
The mean-one ternary reference law of PR142 satisfies

\[
\rho_q(t)=L^q\mathbf1(t),\qquad \rho_0(t)=1.
\tag{2}
\]

For a physical q-step odd path from x to t, its weight is

\[
w_q(x)=\prod_{j=0}^{q-1}b(U^j x)
=3^q2^{-A},\qquad A=\sum_{j=0}^{q-1}a(U^jx).
\]

The exact product formula is

\[
\frac{w_q(x)}t
=\frac1x\prod_{j=0}^{q-1}\frac{3U^j x}{3U^j x+1}
\le\frac1x.
\tag{3}
\]

The empty path has q=A=0 and weight one. Nonnegative sums below are
interpreted by monotone limits; an inequality for them does not require a
finite source cutoff unless one is explicitly imposed.

## 2. IFT-001: exact harmonic transport and occupation budget

For `f>=0` define

\[
H(f)=\sum_{x\in O}\frac{f(x)}x,\qquad
D(f)=\sum_{x\in O}\frac{f(x)}{x(3x+1)}.
\]

If `H(f)<infinity`, then

\[
\boxed{H(Lf)+D(f)=H(f).}
\tag{4}
\]

Consequently, for every Q>=1,

\[
H(L^Qf)+\sum_{j=0}^{Q-1}D(L^jf)=H(f),
\qquad
\sum_{j\ge0}D(L^jf)\le H(f).
\tag{5}
\]

These are identities for the **actually transported distributions** L^j f;
no fresh-shell law is substituted at a return. For signed f the corresponding
norm inequality follows from positivity, `|Lf|<=L|f|`.

**Proof.** Every source has one forward endpoint, and
`b(x)/U(x)=3/(3x+1)`. Tonelli therefore gives

\[
H(Lf)=\sum_x\frac{3f(x)}{3x+1}
=\sum_x\frac{f(x)}x-\sum_x\frac{f(x)}{x(3x+1)}.
\]

Iterate and then use monotone convergence. This proves (4)--(5).

In particular the full Green transform `Gf=sum_{q>=0}L^qf` obeys

\[
\boxed{(Gf)(t)\le t(3t+1)H(f)\quad(t\in O).}
\tag{6}
\]

Indeed, the t-summand in the occupation sum (5) is
`Gf(t)/(t(3t+1))`. Formula (6) is a genuine all-depth, all-positive-source
bound on the stated domain, not just a fixed-depth estimate. For
`f=1_[X,BX)`, its input cost is the finite odd harmonic sum on that source
window, approximately `(log B)/2` as X tends to infinity.

**Why (4) is not a convergence proof.** The relative loss at x is
`1/(3x+1)`, with no positive lower bound as x increases. Moreover the
operator carries the Jacobian factor b(x). Even the unabsorbed fixed point
1 has `G(1_{1})(1)=sum_q(3/4)^q=4`. Finite weighted occupation does not
exclude a cycle or establish termination of its unweighted orbit.

## 3. IFT-002: first-hit kernels and exact cycle renewal

Fix a positive odd t. Let

\[
\tau_t(x)=\min\{q\ge0:U^qx=t\},
\quad
f_q(t)=\sum_{\tau_t(x)=q}w_q(x),
\quad F_Q(t)=\sum_{q=0}^Qf_q(t).
\tag{7}
\]

Infinity is permitted for tau. In particular `f_0(t)=1`, contributed by
`x=t`. A first-hit path, including its terminal state, has no repetition:
a repeat before its first hit would force an earlier visit to t along the
same periodic suffix. Thus different first-hit words, even at different
depths, have different sources.

For any nonnegative source function g,

\[
\sum_{q\ge0}\sum_{\tau_t(x)=q}w_q(x)g(x)
\le t\sum_{x\in O}\frac{g(x)}x.
\tag{8}
\]

This follows from (3) and cross-depth source injectivity. It applies in
particular to **all depths in one source window**, giving a bound independent
of the number or size of the excursions before the final first hit.

If t is not periodic under U, then `rho_q(t)=f_q(t)`. Here “not periodic”
includes a preperiodic target such as 5; it does not mean that its whole
forward orbit is infinite. If t has least positive odd period p, put

\[
\eta=\prod_{j=0}^{p-1}b(U^jt)
=\prod_{j=0}^{p-1}\frac{3U^jt}{3U^jt+1}<1.
\tag{9}
\]

If m is the minimum value on this cycle, then

\[
\eta\le\frac{3m}{3m+1},\qquad
\frac1{1-\eta}\le3m+1\le3t+1.
\tag{10}
\]

Each path ending at t consists of its unique first-hit path followed by k
full laps of this cycle. Therefore

\[
\boxed{\rho_q(t)=\sum_{kp\le q}\eta^k f_{q-kp}(t).}
\tag{11}
\]

The empty first-hit path is included. For t=1, `p=1, eta=3/4`;
`f_q(1)=rho_q(1)-(3/4)rho_{q-1}(1)` for q>=1. No nontrivial-cycle
exclusion is used anywhere in this argument.

Define `kappa_t=1` for a nonperiodic target and `kappa_t=(1-eta)^(-1)`
for a periodic target. Equations (8)--(11) sharpen (6) to

\[
(Gg)(t)\le\kappa_t t H(g).
\tag{12}
\]

The explicit universal majorant `kappa_t<=3t+1` makes this statement usable
without deciding whether t is periodic. The cycle-dependent formulation is
an exact conditional case distinction, not a claim of an algorithm deciding
cycle membership.

The coefficient in (12) is the exact norm of evaluation at t on this
harmonic input space:

\[
\sup_{g\ge0,\ H(g)=1}(Gg)(t)=\kappa_t t.
\tag{12a}
\]

Indeed (12) is the upper bound, and `g=t*1_{t}` attains it. Its only
contributions at t are the empty path and, if t is periodic, its complete
cycle laps. Thus the domain estimate is not based on an unexamined cutoff.

## 4. IFT-003: a linear cumulative reference bound

Put `r=64/81`. For every positive odd t and Q>=1,

\[
\boxed{F_Q(t)\le t(1+Q\log96)+\frac98r^Q.}
\tag{13}
\]

Thus

\[
\boxed{\sum_{q=0}^Q\rho_q(t)
\le\kappa_t\left[t(1+Q\log96)+\frac98r^Q\right].}
\tag{14}
\]

This improves the quadratic-in-Q result obtained by summing DSP-005 to
a linear-in-Q bound. It does **not** prove `sup_q rho_q(t)<infinity`.
The periodic case pays the finite, explicitly bounded renewal factor;
the nonperiodic case has no such charge.

### Proof of the common-depth packing

Take all first-hit words of lengths `0<=q<=Q` whose total valuation satisfies
`A<=6Q`. Their weights obey

\[
w=3^q2^{-A}\le K=(3/2)^Q.
\]

The affine identity `t=wx+beta`, beta>=0 (positive for q>0), also gives
`x<=M=t2^(6Q)`. By (3), `w<=t/x`. Cross-depth injectivity bounds their total
weight by

\[
\sum_{1\le x\le M}\min(K,t/x)
\le\int_0^M\min(K,t/u)\,du
=t\left[1+\log\left(\frac{MK}{t}\right)\right]
=t(1+Q\log96).
\tag{15}
\]

The integral comparison uses a decreasing nonnegative integrand; at zero it
is defined as K. We enlarged the positive odd source set to all positive
integers. This is why there is no unproved equidistribution or density
hypothesis in (15), and why a separate `log t` term is unnecessary.

For the omitted words with `A>6Q`, ignore the first-hit and congruence
conditions. With independent `P(A_i=a)=2^(-a)`,
`E[(3/2)^(A_i)]=3`. At each 1<=q<=Q, their total weight is at most

\[
3^q P(A_1+\cdots+A_q>6Q)
\le9^q(2/3)^{6Q}.
\]

Summing the geometric series over q gives less than `(9/8)r^Q`.
This proves (13); renewal proves (14).

### Abel form

Let

\[
\mathcal R_t(z)=\sum_{q\ge0}z^q\rho_q(t),\qquad
\mathcal F_t(z)=\sum_{q\ge0}z^qf_q(t),\quad0\le z<1.
\]

Using `F_0=1` and summation by parts in (13) gives the convenient upper bound

\[
\mathcal F_t(z)
\le1-z+tz+\frac{t\log96\,z}{1-z}
+\frac98\frac{(1-z)rz}{1-rz}.
\tag{16}
\]

For nonperiodic t, `R_t=F_t`. For periodic t,

\[
\mathcal R_t(z)=\frac{\mathcal F_t(z)}{1-\eta z^p}.
\tag{17}
\]

In particular,

\[
\limsup_{z\uparrow1}(1-z)\mathcal R_t(z)
\le\kappa_t t\log96.
\tag{18}
\]

“Simple-pole upper order” here means this real Abel bound. No meromorphic
extension, existence of a residue limit, or pointwise convergence of rho_q
is asserted.

## 5. IFT-004: an actual transported, endpoint-free depth average

Let W be any prefix-free family of legal inverse words from one positive
odd root t. Word order is from the root outwards. Assume every w in W has
length at most D; exponents and source values need not be bounded. Write
`s_w` for its positive source and `wt(w)` for its Jacobian weight. For Q>=0,

\[
\boxed{
\sum_{w\in W}\operatorname{wt}(w)
\frac1{Q+1}\sum_{q=0}^{Q}\rho_q(s_w)
\le\frac1{Q+1}\sum_{r=0}^{D+Q}\rho_r(t).
}
\tag{19}
\]

To prove this, expand each rho_q into its legal inverse extensions u. The
concatenated word wu has length at most D+Q and weight `wt(w)wt(u)`.
Prefix-freeness ensures that the same full word cannot be produced from two
different prefixes in W. Hence the whole sum before division by Q+1 is a
subsum of the right-hand cumulative reference law. This proof covers
countable W by monotone convergence.

Combining (19) with (14), when D<=cQ and Q>=1 the left side is bounded by a
constant depending only on c and the original root charge `kappa_t t`.
There is **no factor involving the transported endpoint s_w**. This repairs
one genuine defect of naively substituting `rho_q(s_w)<=6qs_w+...` along
a frontier. It uses an average over extension depths; it is not a bound for
one prescribed extension depth and cannot silently replace that profile
inside the external census.

The need for prefix-freeness is mathematical, not cosmetic: admitting both
a word and one of its proper extensions can count the same final history
more than once. Nothing in (19) permits resetting a different root or
discarding the actual prefix clocks.

An exact failure without the guard is t=1, W consisting of the empty word
and the one-letter word (2), D=Q=1. Here `rho_0(1)=rho_1(1)=1` and
`rho_2(1)=8/7`. The left side of (19) is `7/4`, while its right side is
`11/7`. The finite verifier retains this counterexample.

## 6. IFT-005: critical Green potentials and arbitrary stopping frontiers

For every epsilon>0 let `g_epsilon(x)=x^(-epsilon)` on positive odd x and set

\[
V_\epsilon(t)=\sum_{q\ge0}L^qg_\epsilon(t).
\]

By (12), this is finite at every positive odd t and

\[
\frac1{t^\epsilon}\le V_\epsilon(t)
\le\kappa_t t\sum_{x\in O}x^{-1-\epsilon}.
\tag{20}
\]

Tonelli and a shift of the series give the exact strict supersolution

\[
\boxed{LV_\epsilon=V_\epsilon-g_\epsilon.}
\tag{21}
\]

At epsilon=1, `sum_{x odd}x^(-2)=pi^2/8`, so
`V_1(t)<=(pi^2/8)t(3t+1)`. A constant 2 instead of pi^2/8 follows from
the elementary bound on the full integer reciprocal-square sum.

For every prefix-free inverse family W, now with **no bound on its word
lengths**, the standard tree induction applied to (21) gives

\[
\sum_{w\in W}\operatorname{wt}(w)V_\epsilon(s_w)
\le V_\epsilon(t).
\tag{22}
\]

One first proves the inequality for finite trees; truncation and monotone
convergence handle arbitrary countable W. At each expanded node the lost
amount is exactly its incoming weight times `g_epsilon` at that node.

Thus (22) is an actual transported budget valid for arbitrary stopping
frontiers. Its price is precise: the terminal profile is a Green potential
with a decaying source charge, not the unpenalized reference density rho_q.
The proof supplies finite bounds, not a uniform finite-time algorithm for
computing V_epsilon. Replacing V_epsilon by a simple pointwise majorant does
not preserve its supersolution inequality.

Equations (20)--(22) do not meet the project's unweighted inverse-weight
criterion: L has factors `3/2^a`, and V_epsilon is not asserted summable in
ordinary counting measure. This is a useful domain and clock control, not
a proof of Collatz.

## 7. IFT-006: the simple-pole order is nonzero under the external density premise

This section is **SOURCE-QUALIFIED through its external premise**, unlike
the preceding elementary upper bounds. Use the following form of the fast
predecessor theorem for a fixed positive odd target t with 3 not dividing t:
there are constants delta_t>0 and C>0 and a set B_t of positive odd sources
such that, for all sufficiently large X,

\[
\#(B_t\cap[1,X])\ge\delta_tX-O(1),\qquad
\tau_t(x)\le C\log(x/t)\quad(x\in B_t).
\tag{23}
\]

Lau's stated Theorem 1.3 in [Hexagon 2610.00249v2](https://hexagonmath.org/pdf/2610.00249v2)
supplies this with `C=3.4881` and
`delta_t=t^(-25/11)/D_A`, `D_A=2^(2^(2^163))`.
The primary theorem and map conventions were inspected; its analytic proof
and Lean development were not independently replayed here.

We also use the repository's **inherited**, explicit finite simple-path
budget T-A3-651 in
[`FINITE_RECORDS.md`](https://github.com/GettysburgResearch/collatz/blob/d0f48c472d45a336e9083b37b45e1a8d39a2cf16/research/astra-three-routes/pass3/FINITE_RECORDS.md):

\[
\sum_{u\text{ odd on a finite simple path}}\frac1u
\le200m^{-1/40}
\tag{24}
\]

when the path stays above m. Its proof counts exact parity cylinders after
discarding the terminal q odd states; it is not a basin counting theorem.
We inspected that proof and retain its claim identity and source scope.

Every first-hit path is simple. From (3), (24), and `log(1+v)<=v`,

\[
e^{-(200/3)m^{-1/40}}\frac tx
\le w_{\tau_t(x)}(x)\le\frac tx.
\tag{25}
\]

This also gives a two-sided comparison between first-hit weighted mass and
the actual basin's harmonic mass in every source window. It uses one path
at a time; it never applies orbit sparsity to the full predecessor basin.

Set `c_0=exp(-200/3)`. Partial summation in (23) gives

\[
\sum_{x\in B_t,\ x\le X}\frac1x
\ge\delta_t\log X-O_t(1).
\]

All these first-hit paths have length at most Q when `X=t exp(Q/C)`.
Consequently

\[
F_Q(t)\ge\frac{c_0t\delta_t}{C}\,Q-O_t(1).
\tag{26}
\]

Together with (13), (16)--(17), this proves

\[
0<\frac{c_0t\delta_t}{C}
\le\liminf_{z\uparrow1}(1-z)\mathcal R_t(z)
\le\limsup_{z\uparrow1}(1-z)\mathcal R_t(z)
\le\kappa_t t\log96<\infty.
\tag{27}
\]

For periodic t the lower constant can additionally be multiplied by kappa_t;
the weaker displayed value is sufficient. No limit of the normalized Abel
profile is claimed. For positive t divisible by 3, `rho_q(t)=0` for q>=1,
so the exclusion of these targets from the positive lower assertion matters.

### A limiting superharmonic profile, and its unresolved boundary flux

Under (23), choose z_j increasing to one. The upper bound (18) permits a
diagonal subsequence on the countable positive odd targets such that
`h(t)=lim_j(1-z_j)R_t(z_j)` exists. Formula (27) makes h(t)>0 for every
admissible target; h(t)=0 for multiples of three. The resolvent identity is

\[
L[(1-z)\mathcal R(z)]=(1-z)\mathcal R(z)/z-(1-z)/z.
\]

Fatou's lemma yields **only** `Lh<=h`. Equality would require controlling
mass escaping through inverse exponents a tending to infinity. Neither a
full harmonic equality nor uniqueness, computability, or mean regularity of
h follows from diagonal compactness. These profiles can exist independently
of whether all forward components join one; they do not settle Collatz.

## 8. What was attempted, what improves, and what still fails

1. **Pointwise power supersolutions.** Substituting a growing power of t
   into L either amplifies a bad residue branch or creates a divergent
   inverse-exponent sum at linear growth. The source charge in (13) cannot
   simply be reinserted pointwise at every changing endpoint.
2. **Summing the old bound separately in q.** This loses a factor Q. The
   first-hit reduction and common source packing remove that loss, including
   a rigorous renewal treatment of periodic targets.
3. **Removing the endpoint factor under transport.** Equation (19) does
   this for prefix-free actual frontiers and depth averages. Equation (22)
   supplies an arbitrary-depth budget for a different terminal potential.
   Neither proves a bound for the external census's prescribed-depth profile.
4. **Promoting average bounds to pointwise bounds.** This is unsupported:
   bounded Cesaro or Abel averages do not by themselves bound every term.
   The negative fixed-point spike remains outside the positive-source proof.
5. **Treating strict weighted loss as termination.** This fails already on
   U(1)=1, whose Jacobian mass decays geometrically. The operator and norm
   cannot be substituted for the unweighted Collatz survivor criterion.

The next useful target is a source-conditioned uniform-integrability or
boundary-flux estimate that upgrades (19) to the required prescribed-depth
profile while retaining the same root and actual stopping frontier. Another
specific target is control of the limiting inverse-exponent escape in Lh<=h.
Neither estimate is supplied here.

## 9. Evidence and novelty boundary

The accompanying verifier checks exact rational transport, first-hit renewal,
source injectivity, packing, prefix-free concatenation and infinite geometric
tails at bounded sizes. The logarithmic upper bounds are checked using the
safe rational enlargement `log96<5`; the displayed universal proofs do not
depend on finite tests or floating diagnostics.

The first-hit no-cycle injectivity and `wt<=t/source` inequality are already
explicit in Lau's paper (Section 2.2 and Lemma 3.3). The inverse law is also
inherited. During this pass the root located Valbuena's October 2026
manuscript *Collatz basin densities and canonical traces from first-passage
stabilization*, in
[collatz-two-coordinate-obstruction, pinned source](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/tao-basin-densities.tex).
The frozen commit is `a7275d5a73814d3d9a400c6fe6577de9542b03a3`,
path `paper/tao-basin-densities.tex`, and Git blob
`63ca82653986b0dfa4c54bac17ed80199b806448`.
We inspected its `Identification of the cylinder and Green limits` section.
It already contains the exact `(9/8)(64/81)^K` aggregate tail, periodic
renewal, and the unconditional statement `F_N(K)<=C_N(K+1)`; stronger
canonical trace identifications there use additional source-qualified input.
**Linear cumulative growth and simple-pole upper order are therefore
reconstructed here, not claimed as discoveries.**

Relative to that inspected argument, (13) makes the root dependence explicit
as `t(1+Q log96)` without a `log t` loss. The actual prefix-free transported
average (19), harmonic-space defect and exact Green evaluation norm, and
source-penalized arbitrary-frontier budget (22) are the local additions.
No exhaustive external priority claim is made for those formulations either.

The same external manuscript claims stronger pointwise first-hit bounds
through a uniform inverse-linear basin-density floor. Those stronger
source-qualified results are not used in (4)--(22), and our Cesaro argument
does not independently establish their density premise. No outside Lean
development was replayed in this track.

The deterministic receipt records 1,340 legal inverse words, including
1,291 first-hit words, across 26 positive odd targets, depth at most 6,
and total valuation at most 14; it makes 156 packing and 2,730 graded
renewal comparisons. Separate exact geometric-tail laws cover all 251
positive odd targets at most 501 through depth 6. There are 126 exact
harmonic transport/loss identities and 144 profile comparisons on 36
actual prefix-free frontiers. The non-prefix-free control fails in the
predicted direction, `7/4 > 11/7`. Normal and Python `-O` runs produced
byte-identical JSON, with SHA256
`482498967ecda13391859445781a664d4e691b3d75b5538c84abd69021f2da85`.
These finite checks audit the formulas; the displayed arguments supply
the universal claims.
