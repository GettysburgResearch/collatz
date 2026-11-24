# Continued closing attacks: polynomial structure and canonical source mass

**Full Collatz remains open.** The previous work was confirmed on GitHub at
PR182 head `45354128f890fb479f6c23b547368bcddd9cebe6` before this continuation.
The fresh pass pursued three directions: ordinary invariant-label structure;
canonical source transport and contact; and deeper complete-certificate
rewrites. Two positive deductions and their small Lean interfaces are the
main results. The certificate investigation found no universal dispatcher
and did not repackage the existing signed-carry compiler as new work.

The [source ledger](CONTINUED_SOURCES.json) records the new PR176 and PR185
heads used here. The earlier 145-PR inventory remains the broad background;
this pass is not represented as another complete mathematical review of
all branches.

## 1. All polynomial phases, with a gap independent of degree

For an ordinary Boolean label satisfying the exact shortcut equation
`f(Tn)=f(n)`, put

\[
L_X(a)=\frac1{H_X}\sum_{n\le X}\frac{a(n)}n,
\qquad m(P)=\lim_{N\to\infty}\frac1N\sum_{n\le N}e(P(n)).
\]

The [new written proof](INVARIANT_CORRELATION.md) gives, for every fixed
real polynomial `P`,

\[
\boxed{L_X(fe(P))-L_X(f)m(P)\longrightarrow0.}
\]

The mean `m(P)` vanishes when a nonconstant coefficient is irrational.
Rational phases retain their correct mean; for example
`m(n^2/4)=(1+i)/2`. Existence of the label mean is not assumed.

For every nonconstant such label, one `eta_f>0` works for every fixed
finite polynomial-phase sum, regardless of degrees, coefficients, or
number of summands:

\[
\boxed{\liminf_X L_X\left|f-\sum_jc_je(P_j)\right|\ge\eta_f.}
\]

The bound extends to the bounded closure of these sums in the ordinary
Besicovitch seminorm. This class strictly contains the preceding
linear-phase approximation class. Membership of the actual basin-of-one
indicator would therefore force full convergence. The membership remains
unproved, and every approximant must be fixed before the cutoff tends to
infinity.

### The new mechanism

Finite polynomial families are realized with moment coordinates
`n^j omega_i` in powers of the six-solenoid. Polynomial Weyl
equidistribution supplies joint ordinary equidistribution. The shortcut
branches lift to Haar-preserving triangular affine automorphisms. Their
commutator generates the polynomial skew translation `n -> n+1`.

Higher-degree Fourier characters have infinite unipotent dual orbits.
An invariant square-integrable function has coefficients of equal magnitude
along each such orbit; square summability forces them to vanish. Rational
independence eliminates the remaining degree-one characters. The preceding
ordinary-Jacobian and nonsingular-transfer argument then applies.

[PolynomialLift.lean](PolynomialLift.lean) checks the substitution algebra
at every degree, including composition order, inverses, evaluation states,
the quarter-translation commutator, and unit-translation invariance. It
does not formalize the compact model or measurable ergodicity. The written
proof keeps the pinned marginal stationary-density/FLOOR inputs, and uses
LOG only for the positive gap. The newer joint-clock population claim is
not needed in this lane.

## 2. Exact doubling still does not manufacture regularity

The new control is

\[
c(n)=\left\lfloor\sqrt{\left\lfloor\log_2
       \operatorname{oddpart}(n)\right\rfloor}\right\rfloor\pmod2.
\]

It satisfies `c(2n)=c(n)` pointwise. It has zero topological entropy,
with the explicit arbitrary-offset bound
`p_c(L)<=4L+64L^2(L+1)`. Both colors have logarithmic mass one half in
the expected proportions in every fixed residue class. Its logarithmic
mean shortcut defect is `O(1/sqrt(log X))`.

Nevertheless its logarithmic distance from every `[0,1]`-valued sequence
having an ordinary Cesaro mean is exactly one half. This includes the
polynomial-phase models and the relevant nilsequence models. The distance
from the polynomial-phase Besicovitch class is exactly one half as well.

The odd equation fails at `11 -> 17`. This is an unconditional control,
not an actual invariant Collatz label. It shows that exact doubling,
low complexity, positive residue populations and averaged odd-branch
invariance do not suffice. General nilsequence decorrelation and
cutoff-uniform Gowers estimates for actual labels are not claimed.

## 3. The entire Green history of the unchanged canonical source

The [canonical-source proof](HARMONIC_CAPTURE_BRIDGE.md) works on actual
nonperiodic odd ternary units. Forward transport is killed on reaching
any periodic state. Write `L` for ordinary inverse counting,
`h(q)=G(q)/q`, `lambda(q)=3q/(3q+1)`, and
`d(q)=h(q)/(3q+1)`. The pinned PR185 construction gives
`L(lambda*h)=h` and `L^k h -> nu`, with `L nu=nu`.

For the unchanged original-source seed `a0(n)=h(n)/n`, put
`b_k=L^k a0`. Exact telescoping, including time zero, yields

\[
W(q)=\sum_{k\ge0}L^kd(q)=\nu(q)-\lambda(q)h(q).
\]

The identity `a0(n)=(3+1/n)d(n)` then gives

\[
\boxed{3W(q)\le\sum_{k\ge0}b_k(q)\le4W(q).}
\]

This controls every time and every original source hitting one actual
target. Different-source collisions are retained. The exact tail is
bounded by three and four times `nu(q)-L^(N-1)h(q)` for `N>=1`.

With the ordinary harmonic inverse kernel, the bounded potential
`z=lambda*h/nu` satisfies `Kz-z=d/nu` and tends to one along its
inverse sample paths. The complete normalized occupation lies between
`3(1-z)` and `4(1-z)`. If the target's **whole predecessor domain**
lies above `m`, it is at most

\[
\frac4{3m+1}+\frac{800}{3}m^{-1/40}.
\]

A later forward suffix cannot erase an original lower ancestor from that
hypothesis.

### A finite global weighted collision budget

With the pinned population constant `c>0` and `A=203/(3c)`, the full
space-time sum satisfies

\[
\boxed{\sum_{k\ge0}\sum_q
 \frac{b_k(q)^2}{\nu(q)q^s}
 \le\frac{80sA}{s-39/40}\qquad(s>39/40).}
\]

In particular these weighted energies tend to zero. For targets at most
`X`, the complete unweighted local occupation is at most `80A X^(39/40)`.
The reciprocal spatial weight in the global estimate is essential:
escape of energy toward increasing targets is still compatible with it.

[HarmonicCapture.lean](HarmonicCapture.lean) proves the finite and real-series
interfaces, with convergence and comparison hypotheses explicit. Existence
of the actual harmonic reference, global moments, countable transport,
path-law comparison, and the final Tonelli application remain separately
reviewed written deductions from their pinned sources.

## 4. A canonical bridge between the positive lanes

[CANONICAL_ESCAPE_LABEL.md](CANONICAL_ESCAPE_LABEL.md) constructs a specific
bounded ordinary invariant function from the same harmonic data. For an
escaping unit component `C`, the predecessor sets along any forward path
increase to `C`, while `nu(q_k)` increases to a positive finite limit.
Thus the component values

\[
D_C=\sum_{n\in C}d(n),\qquad C_C=\lim_k\nu(q_k),\qquad
F_C=D_C/C_C
\]

are well defined independently of the chosen starting point. They satisfy
`0<F_C<=1-delta_(min C)<1`. Set the value to zero on every eventually
periodic component and extend through the first ordinary odd ternary unit.
The resulting `Ftilde` is bounded, exactly shortcut invariant, and positive
precisely on escaping orbits.

The same note extends polynomial rigidity to every bounded complex
invariant label `J`. If `J(a)=alpha` and `J(b)=beta` are distinct values
at odd unit targets, its exact level indicators give

\[
\liminf_X L_X|J-Q|
\ge |\alpha-\beta|\min(c_{\log}/a,c_{\log}/b)>0
\]

for every fixed polynomial-phase sum `Q`. No mean existence or approximation
of those level indicators is assumed. Therefore polynomial-phase
Besicovitch regularity of the specific canonical escape label would force
it to vanish and exclude all escaping ordinary orbits.

This construction supplies a particular function to investigate; it does
not supply its approximants. Since every eventual cycle receives value
zero, nontrivial periodic cycles remain a separate obligation. The bridge
is independently reviewed written mathematics and adds no Lean statement
to the audit count.

## 5. What the fresh contact and certificate work changes

PR176's exact source envelope and inverse-contact program, and PR185's
literal-tail carry language, were read at the recorded new heads. They
leave an effective moving-root contact estimate or a complete independent-
clock merger selector open. The general signed-carry compiler already
exists upstream; it was not added again here.

For the analytic contact route, the new occupation cost is comparable to
`1/n`. The proved estimates supply no positive per-step cost floor on
the continuation set. The stopped `V`-Doob law is explicitly distinguished
from the harmonic `G`-Doob and ordinary `nu` laws in the new note. Their
bounded likelihood comparisons do not themselves supply a contact clock.

The stronger invariant-label conclusion and canonical-source occupation
estimate are thus positive advances with different remaining obligations:
actual label regularity in the first lane; spatial tightness or a useful
contact-cost lower bound in the second. Neither is silently inferred from
compact ergodicity, fixed-target convergence, or finite weighted energy.

## 6. Executed evidence

The [continued report](../../reports/2026-11-21-dyadic-descent/continued/README.md)
contains the actual fresh two-module replay, complete 22-statement axiom
inventory, independent internal review pins, and repository validation.
The previous 117 statements and their receipts are unchanged. The combined
inventory is 139 public statements across eleven added modules; this is
not a count of 139 novel mathematical theorems.
