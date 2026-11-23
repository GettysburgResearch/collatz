# Testing an entire-function contradiction on the unchanged source

**Status: source-qualified written estimates and an unsuccessful closing
attempt.** The actual strict-Green resolvent has entire order strictly below
one. That makes a positive-Laplace-transform rigidity argument tempting.
The argument fails at its positivity hypothesis for the entire family,
and at its entire-continuation hypothesis for the positive family. Both
failures can be located on the same original ordinary source. They are
not properties of a replacement random orbit.

The two finite polynomial declarations in `lean/SurvivalCurvature.lean`
check the curvature calculation below. The infinite operator estimate,
Laplace argument and boundary products are written mathematics. No
universal escape or nontrivial-cycle exclusion is asserted.

## 1. The precise proposed contradiction

A nonconstant Laplace transform of a finite positive measure cannot be
entire with subexponential growth on the negative real axis. More
precisely, suppose

\[
 f(z)=\int_{[0,\infty)} e^{-zt}\,d\mu(t)\quad(z\ge0),
 \qquad |f(-r)|\le C(1+r)^d e^{Cr^\theta},\quad 0<\theta<1,
 \tag{A1}
\]

and `f` is entire. Then `mu` is supported at zero, and `f` is constant.
Here is the complete argument. Differentiating for positive `z` and
letting `z` decrease to zero by monotone convergence identifies all
moments with the finite derivatives at zero. The entire Taylor series
and Tonelli then give

\[
 f(-r)=\sum_{j\ge0}\frac{r^j}{j!}\int t^j\,d\mu(t)
      =\int e^{rt}\,d\mu(t).
\]

If `mu([a,infinity))>0` for any `a>0`, the right side is at least
`mu([a,infinity))*exp(a*r)`, contradicting (A1). This uses positivity of
the representing measure, not merely alternating Taylor coefficients.

Bernstein's representation theorem connects complete monotonicity on
the whole positive half-line with positive Laplace transforms. Its
standard reference is Schilling--Song--Vondracek, *Bernstein Functions*,
second edition, Chapter 1, Theorem 1.4,
<https://doi.org/10.1515/9783110269338.1>. The publisher's chapter contents
were accessible but the full chapter was not. The argument just given
only uses an explicitly supplied Laplace representation; no inaccessible
proof from that chapter is a dependency of the deductions below.

The attempted closing idea was to establish (A1) for the positive
boundary coefficient of the canonical surviving flow. That coefficient
would then be constant, in conflict with its strictly positive loss at
the physical parameter. The next sections test both hypotheses on the
actual operators.

## 2. The strict resolvent really does have order below one

Use the positive odd ternary units which are not periodic, with forward
transport killed upon entering a periodic vertex. On

\[
 X_s=\ell^1(N,n^{-s}),\qquad \theta<s\le1,
 \qquad \theta=39/40,
\]

write `L` for ordinary mass transport, `S=sum_(j>=0)L^j`,
`omega(n)=1/(3n+1)`, and

\[
 K=SLD,\qquad Da(n)=\omega(n)a(n).
\]

The exact source-qualified inputs are PR185 at
`980d40fc4afeaaf8f2a9256f322acf3e4568e013`,
`research/multiple-attacks-20261122/STRICT_GREEN_VOLTERRA.md`, equations
(1)--(12). In particular every retained actual path has distinct states
and obeys

\[
 N_x(X):=\#\{j:U^jx\le X\}\le5X^\theta,
 \qquad C_s=\frac{5s}{s-\theta},\quad A_s=C_s/3.
 \tag{A2}
\]

The published packet already proves compactness and the entire inverse
`R(z)=(I+zK)^(-1)`, with an exponential norm majorant. The following
improvement uses the full count (A2), rather than only its reciprocal
moment.

For any subset of one retained path and any `t>0`, Tonelli gives

\[
\begin{aligned}
 \sum_n\log\left(1+\frac{t}{3n+1}\right)
 &\le\sum_n\log\left(1+\frac{t}{3n}\right)\\
 &\le\int_0^\infty N_x(u)\frac{t}{u(3u+t)}\,du\\
 &\le 5(t/3)^\theta\int_0^\infty
                         \frac{v^{\theta-1}}{1+v}\,dv\\
 &\le B_\theta t^\theta,
 \qquad B_\theta=\frac{5\,3^{-\theta}}{\theta(1-\theta)}.
\end{aligned}
\tag{A3}
\]

The last bound splits the integral at one; both resulting power
integrals converge. The count is zero below the least positive state,
so extending the integral down to zero causes no endpoint problem.
The case `t=0` follows directly. Consequently, uniformly over all
original paths and their interior subsets,

\[
 \prod_n(1+t\omega(n))\le\exp(B_\theta t^\theta).
 \tag{A4}
\]

The exact finite-path kernel is

\[
 R(z)a(q)=a(q)-z\sum_{n\prec q}\omega(n)a(n)
                     \prod_{n\prec u\prec q}(1-z\omega(u)).
 \tag{A5}
\]

The endpoint `q` is not in the interior product. Bound its absolute
value by (A4), and use the unchanged positive column estimate
`||K||<=A_s`. This proves

\[
 \boxed{\|R(z)\|_{X_s\to X_s}
       \le1+|z|A_s\exp(B_\theta|z|^\theta).}
 \tag{A6}
\]

Thus this entire operator-valued inverse has order at most `theta<1`.
The conclusion is global in the complex parameter and keeps exactly the
same source space, killing convention, and strict intermediate states.
It does not upgrade raw `L` to a bounded operator on `X_s`.

## 3. The unchanged ordinary atom rejects the Laplace identification

Suppose that one positive ordinary source `p` escapes, and retain its
literal path `q_j=U^j p`. For the linear deformation

\[
 T_z=L(I-zD),
\]

the transported mass of this very same atom after `k` steps is

\[
 J_{p,k}(z)=\prod_{j=0}^{k-1}(1-z\omega(q_j)).
 \tag{A7}
\]

The corresponding infinite product converges locally uniformly, by
`sum_j omega(q_j)<infinity` from (A2). It defines an entire function
`J_p` of order at most `theta`, by (A4). It is not constant. At the
physical parameter `z=1` it is exactly the surviving path correction,
which is strictly positive under the retained occupation estimate.

This appears close to (A1), but the positive Laplace representation
already fails at its first two moments. Put
`s_1=sum_j omega(q_j)` and `s_2=sum_j omega(q_j)^2`. Locally uniform
product differentiation, or the finite formulas followed by convergence,
gives

\[
 J_p(0)=1,\quad J'_p(0)=-s_1,\quad
 J''_p(0)=s_1^2-s_2,
\]

and therefore

\[
 \boxed{J_p(0)J''_p(0)-J'_p(0)^2=-s_2<0.}
 \tag{A8}
\]

For a positive Laplace measure with these finite moments, Cauchy--Schwarz
would give the opposite inequality. The failure is strict already for
each nonempty finite actual path; no limiting pathology is needed.
Those finite product and ordinary-state statements are the two checked
Lean declarations in this packet.

The entire product also has a simple zero at every `3q_j+1`, since the
retained states are distinct. Positivity of the physical value at one
does not imply complete monotonicity on the whole positive half-line.

## 4. The positive parameter family has actual poles

To keep every edge weight positive for every `z>=0`, use instead

\[
 \lambda_z(n)=\frac{3n}{3n+z},\qquad
 H_p(z)=\prod_{j\ge0}\frac{3q_j}{3q_j+z}.
 \tag{A9}
\]

This has a direct positive Laplace representation. Conditional on the
unchanged path, let independent exponential variables have rates `3q_j`.
Their total has finite expectation `sum_j 1/(3q_j)`, so it is finite
almost surely. Its Laplace transform is (A9), first for finite sums and
then by bounded convergence. This construction randomizes auxiliary
holding times only; it does not choose new Collatz states or valuations.

The representation is nonconstant, but (A9) is meromorphic. If
`m=min_j q_j`, then

\[
 \lim_{z\to-3m}(z+3m)H_p(z)
 =3m\prod_{q_j\ne m}\frac{q_j}{q_j-m}>0.
 \tag{A10}
\]

The product is finite: there are finitely many states below `2m`, all
different from `m`, and the logarithms of the remaining factors are at
most a constant times `m/q_j`. The pole is simple and nonremovable.

The companion [CANONICAL_CHARGE.md](CANONICAL_CHARGE.md) reconstructs the
canonical two-sided ordinary path law and proves the same obstruction
for the complete component coefficient, where positive mixtures could
otherwise have concealed a cancellation. Its residue is at least
`3m*nu(m)>0` at the least ordinary vertex of that component.

The two families agree at `z=1`, but they do not agree as analytic
families. For the linear family the equation is
`h_z=L((1-z*omega)h_z)` and the strict-Green factorization applies. For
the rational family write `g_z=lambda_z*h_z`; then

\[
 (1+z/(3n))g_z(n)=L g_z(n).
\]

Its Green correction includes the time-zero diagonal term. The strict
quasinilpotent argument cannot be applied after deleting that term.
The poles in (A10) identify the actual cost of doing so.

## 5. Outcome and relation to the entropy attack

The entire-function idea was pursued because a positive Laplace
coefficient of order below one would force an immediate contradiction.
The operator growth hypothesis is now established under the existing
path-count input. The required positive representation does not belong
to that entire family. The family which has the positive representation
has a genuine pole with a positive ordinary-source residue.

The initial alternative was to combine the actual-orbit entropy ceiling
in PR185 `research/deep-closing-20261122/ACTUAL_ORBIT_ENTROPY.md` with the
stationary inverse-law classification in Paper 127 and the stationary
source-cost theorem in Paper 150. Their input laws require specified
inverse transition probabilities or absolute continuity of the same
source law. Neither has been established for the reversed past of the
one escaping source. PR176's coupled zero-entropy control already tests
the weaker compact-invariance argument. This pass therefore did not
promote that substitution into a fourth entropy theorem; it pursued the
explicit canonical parameter family above instead.

No conclusion here forces the canonical escape coefficient to be zero.
This is a precise outcome of a direct closing attempt, with its positive
global operator estimate and its failed final identification kept
together. Periodic vertices have been killed throughout the analytic
construction, so nontrivial positive cycles remain a separate obligation.
