# Closing attempts after the exact five-energy transport

**Status: analytical deductions and unresolved obligations, not a Collatz proof.**

## A. The local-density/coalescence scale calculation

At PR146 `e238c63a5d57f96bb063b7472498d1977df51951`, `GROWING_ADDITIVE_GAPS.md`, for any interval of N original sources and any fixed 1<=d<=L the same-component failure count is at most

\[
 C N\sqrt{\log(2+L)/\log(2N)}.
\]

Averaging the d values is legitimate because every comparison concerns the actual fixed source n and n+d. Suppose, as a separate hypothetical strengthening, that for every n in [X,2X] at least delta L(X) members of [n+1,n+L(X)] reach 1, with delta>0 independent of X. Every source n not in the basin of 1 disagrees in component with all those members. Positive double counting therefore gives

\[
 \#\{n\in[X,2X]:n\notin C\}
 \le(C/\delta)X\sqrt{\log(2+L(X))/\log(2X)}.
\]

If log L=o(log X), this would give density-one convergence and, with the separately source-qualified fixed-target positive-density theorem, full Collatz. More generally a sequence of widths X^epsilon and relative lower fractions delta(epsilon) would suffice if sqrt(epsilon)/delta(epsilon)->0. This is a sufficient *additional* theorem, not a conclusion from the existing lower counts.

The actual inspected lower-count source is PR146's older referenced commit `4e94f656236485ebf854711528b06c18b91d4ad3`, `research/critical-orbit-mellin/LOCAL_FIRST_LANDING.md`. Its shrinking physical intervals have width at least X/(log X)^(1/8.234), or X/sqrt(log X) on the stated convergent subsequences. These widths have log L/log X -> 1. They do not make the displayed error vanish. Its prescribed binary/ternary cylinders constrain low digits; they are not arbitrary short intervals specifying high digits. The new universal five-energy cover does not alter this scale calculation.

## B. Why harmonic predecessor mass remains source-qualified

Let U be the odd map. Fix a positive odd ternary-unit target R with no positive U-return. For each depth q>=1 and each exact valuation word w ending at R, write

\[
 R=J_w n_w+\beta_w,\qquad J_w=3^q2^{-A(w)},\quad\beta_w\ge0.
\]

The source n_w is a positive odd ordinary integer. Hence 1/n_w >= J_w/R. Distinct words at all depths have distinct n_w: two depths giving the same source would force a positive return at R. Let rho_q be the finite ternary density, normalized as in Mazur's positive-density paper,

\[
 \rho_q(t)=\tfrac23 3^q\Pr(Y_q=t\bmod3^q),\qquad
 Y_{j+1}=2^{-a_{j+1}}(3Y_j+1),\quad\Pr(a_j=a)=2^{-a}.
\]

The exact word congruence gives

\[
 \sum_{w:\,U^q(n_w)=R}J_w=\tfrac32\rho_q(R).
\]

Therefore the actual predecessor basin satisfies

\[
 \sum_{U^j(n)=R\text{ for some }j}1/n
 \ge \frac{3}{2R}\sum_{q\ge1}\rho_q(R).
\]

A nonperiodic predecessor R reaching any prescribed unit target can be chosen by the elementary inverse-fan argument (if the target is periodic, choose R above its finite cycle). Thus divergence of the right side at such one fixed ordinary predecessor would be a sufficient source-specific harmonic-mass theorem.

No such pointwise divergence was proved in this pass. Finite-ternary L1 mixing controls the average of rho_q over residue classes. It does not by itself force divergence at a specified ordinary R, or at a member of a prescribed countable inverse fan. Passing from an average to that one point is exactly an additional source-retention requirement. The inverse tree's children that become multiples of three are terminal; silently renewing their ternary-unit law would change the operator. A finite hidden-lift matrix is not a proof of this pointwise renewal.

Accordingly the harmonic rigidity corollary of FIVE_SLICE_ENERGY.md retains its named PD input. At exponent .84, the older predecessor-moment theorem suffices with its own source pin.

## C. Remaining positive-source occupation obligation

PR157 `64361ecca770092d6c8242dc6211e38818af2e50`, `research/global-closure-20261120/transport.md`, fixes an actual unsafe return B and an original full-support source f_0(u)=1_U(u)/(u(u+1)). Its positive Green charge is

\[
 G_N(f_0)=\sum_{j<N}\sum_y(H^jf_0)(y)/\psi(y).
\]

Its lower bound liminf G_N/log N >= m_infinity/log6 includes periodic and escaping sources. The required upper bound o(log N) has not been derived here. Finite harmonic five energy is a separate sufficient route. The exact five-energy transport does not convert the known reciprocal-height Green bound into the larger reciprocal-psi bound.

## D. PR162: an exact partial five-energy renewal, with its uncovered remainder

The new source is PR162, full head
`2279da37ac612dbe049777354cdedb3c0aa03282`,
`research/creative-closure-20261120/five_closure.md`, C5-001--002, and
`research/creative-closure-20261120/occupation.md`, OCC-001--004. Both
manuscripts were read at this head. The following is a direct deduction
from the physical C5-001 block, not a new proof of its global five law.

Let f be any ordinary shortcut-invariant metric label, and put

\[
e(x)=d(f(5x),f(x)),\qquad
\mathcal S=\{x>0:x\text{ odd},\ 3\nmid x,\ x\equiv49\pmod{64}\}.
\]

For every x in S, write

\[
q=\operatorname{oddpart}((9x+7)/64),\qquad
\ell=6+v_2((9x+7)/64).
\]

The C5-001 block gives actual simultaneous ordinary paths
T^ell(x)=q and T^ell(5x)=5q. Consequently q is an odd ternary unit,
e(x)=e(q), and q<=x/7. This retains the physical two-arm defect; it
does not replace it by a semigroup comparison.

For each odd ternary unit q, all inverse block sources are exactly

\[
x_\ell(q)=(2^\ell q-7)/9,\qquad \ell\ge6,
\quad 2^\ell q\equiv7\pmod9,\quad 3\nmid x_\ell(q).
\]

The legal clocks lie in one class modulo six, with some members removed
by the final unit guard. Consecutive clocks in that full class obey
x_(ell+6)=64 x_ell+49. Every legal first source is at least 7q.
Therefore, for s>0,

\[
\sum_{\ell\text{ legal}}x_\ell(q)^{-s}
\le\frac{7^{-s}}{1-64^{-s}}q^{-s}
=:\kappa_s q^{-s}.
\]

This also holds after restricting the sources to x<=M, in which case
q<=M/7. Define the finite positive sums

\[
E_5(s;M)=\sum_{\substack{x\le M\text{ odd}\\3\nmid x}}x^{-s}e(x),
\qquad
R_5(s;M)=\sum_{\substack{x\le M\text{ odd}\\3\nmid x,\ x\notin\mathcal S}}
x^{-s}e(x).
\]

The whole-source change of variables is then an exact positive partial
renewal with the rigorous truncated consequence

\[
\boxed{E_5(s;M)\le R_5(s;M)+\kappa_s E_5(s;M/7).}
\]

In particular kappa_1=64/441<1. At s=.84 it is also less than one:
both 7^(.84)>sqrt(7)>2 and 64^(-.84)<1/8 give
kappa_(.84)<4/7. Iterating the truncated inequality, or bounding its
rightmost smaller-scale energy by E_5(s;M), proves the precise
equivalence

\[
E_5(s)<\infty\quad\Longleftrightarrow\quad R_5(s)<\infty
\qquad(\kappa_s<1),
\]

and E_5(s)<=R_5(s)/(1-kappa_s) when these are finite. The truncation is
essential: an inequality between two infinite untruncated sums would
not justify subtracting kappa_s E_5(s).

This is a genuine positive renewal consequence of the new physical
block. Its missing input is a finite moment on **all remaining** odd
ternary-unit classes. That complement is not an endpoint error, a finite
set, or the support of a known summable source. No argument in C5-001
forces an arbitrary failed antecedent into S along a defect-preserving
path. The inverse block selector constructs larger sources; it does not
provide a smaller reduction on that complement. C5-002 settles one
entire supplied rank-two family, but it does not give a recursion for
arbitrary next letters of a convergence certificate. Thus the displayed
renewal does not furnish the finite E_5(.84) or E_5(1) needed by the
global energy theorem.

## E. PR162: why capacity, entropy, and finite Poisson repair do not pay that remainder

The same PR162 occupation manuscript makes three useful exact positive
constructions, but their domains and charges differ from the unresolved
spatial five-boundary remainder above.

1. OCC-001 gives an all-time finite total coalescence-information budget
   for the actual fixed input f_0, with every original atom retained.
   Its one-return unit-coefficient payment of occupation is explicitly
   refuted on that same input. A larger or amortized fixed-source
   comparison is left open. There is no identity making its entropy
   drop an ordinary component boundary charge.

2. OCC-002--003 define first-hit capacity C(y), counting each original
   source at most once at an endpoint. They prove a finite moment
   sum C(y)y^(-s) for s above the stated simple-path entropy exponent,
   including periodic states. Capacity is monotone along surviving
   returns, not invariant under ordinary T. It therefore cannot be
   inserted as the invariant label in FIVE_SLICE_ENERGY.md or in
   PR159's component-label circulation theorem. Moreover a surviving
   original atom contributes repeatedly to G_N but at most once to
   each C(y); on a cycle, infinitely many time charges are compressed
   into finitely many endpoint contributions. Positivity and Tonelli
   do not reverse this change of counting rule.

3. OCC-004 repairs a finitely supported positive defect r on certified
   terminating return orbits by V=sum_(j>=0) H^j r, giving
   (I-H)V=r without creating another defect. The mass of this repair
   is exactly the positive source sum of r(u) times the remaining
   return count of u (for the killed map). A proposed countable repair
   therefore requires both justified termination for every repaired
   source and a finite weighted total return count. Neither follows
   from the finite first-hit Dirichlet moment. Defining V formally on
   an unproved surviving source makes its mass infinite, rather than
   proving it a summable supersolution.

Accordingly the first unsupported inference in either attempted bridge
is explicit: a source-specific bound must pay repeated return occupation,
or a separate invariant-label argument must bound the entire R_5 moment.
The exact five transport, the partial paired-block renewal, and the
finite positive repair do not supply either bound. No cycle exclusion,
global convergence theorem, or full proof of Collatz is obtained here.
