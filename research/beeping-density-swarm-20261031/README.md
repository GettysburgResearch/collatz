# Contact transport and harmonic inverse dynamics

**Collatz remains open.** This second swarm pass contains constructive results,
infinite-family obstructions, and exact operator statements. All new claims
remain **PROPOSED**, with written proofs, internal independent reconstruction,
and bounded exact checks. The packet does not assert a convergent orbit for
every positive integer, exclude every nontrivial positive cycle, or supply a
divergent positive orbit.

The starting point is [PR142](https://github.com/GettysburgResearch/collatz/pull/142)
at `d0f48c472d45a336e9083b37b45e1a8d39a2cf16`. Its
[first packet](../beeping-density-swarm-20261030/README.md) established the
beeping-machine equivalence, computable rank envelope, complete contact fans,
and positive-source inverse-density bounds. This pass tests the unresolved
transport steps. It also compares PR140's concentration work, PR141's rewriting
work, and newly located external manuscripts before making novelty claims.

## 1. A constructive extension with a precise remaining inequality

Let S be shortcut Collatz, absorbed at one. The inherited finite rank Gamma
has the computable envelope

\[
\Phi(n)=\max_{j\ge0}\left\lceil\Gamma(S^j n)/3^j\right\rceil,
\qquad C=\{n\ge2:\Phi(n)=\Gamma(n)\}.
\]

Every source reaches C or one in a proved finite time. Let r(x) be the first
positive return clock from a contact x, killed at one. A weight w on C has an
occupation extension A_w to every n>=2: sum w(x) over the actual return arcs
which visit n, counting the starting contact and excluding the endpoint.

The new construction has a **complete finite evaluator at every integer**.
It is positive everywhere whenever w is positive on C, agrees with w on C,
and satisfies

\[
(I-K)A_w=\iota_C(w-K_Cw),\qquad
\sum_{n\ge2}A_w(n)=\sum_{x\in C}r(x)w(x).
\]

Here K is unweighted shortcut pushforward killed at one, and K_C is its
contact-return operator. Thus all failure of flow balance is exactly on the
contact set. There is no unevaluated inverse boundary at infinity. The
extension is unique among functions with the prescribed contact values and
exact balance away from C.

For every computable s>1/2, w=Phi^(-s) gives a positive computable summable
extension. An explicit return-height estimate gives finite p-th height
moment when `s>p theta+1/2`, where `theta=log(2)/log(4/3)`. In particular
s=6 supplies an exact rational evaluator and a finite second height moment.
Combined with the actual inverse bounds below, this gives a finite uniform
depth-average pairing for this transported population.

**The missing step is the inequality on C.** The extension does not produce
it automatically. Read [CONTACT_TRANSPORT.md](CONTACT_TRANSPORT.md),
CT-004--005, and the [independent review](CONTACT_REVIEW.md).

## 2. Infinite families close the finite-patch escape route

The previous pass found particular bad inverse rows. This pass proves failures
outside **every fixed finite terminal set**:

* Contact return is unbounded on every fixed positive Phi-moment space. A
  full-support input with finite such moment can acquire infinite moment
  after just one return. Extra source integrability is necessary for the
  displayed moment estimate; one-step rank control does not survive induction
  in the same space.
* For every k>=12, the ordinary positive integers
  `n_k=243*4^k+115` and `y_k=(3*n_k+1)/2` are odd unit contacts, with
  `Phi(n_k)=(n_k+5)^2/3` and `Phi(y_k)=(y_k+1)^2/3`.
  Their single contact edge has height ratio tending to 3/2 and rank ratio
  tending to 9/4.
* Consequently no positive weight eventually equal to
  `n^a Phi(n)^(-s) h(v2(n),v3(n))`, s>0, can be both summable and satisfy
  `K_C w<=w`. If a<2s the explicit edge violates the inequality; if a>=2s
  the summands do not tend to zero. Arbitrary finite corrections, finite
  terminal cores, and further restriction to odd unit contacts do not repair
  this class.

The proof covers the growing prefix cutoff for every k; finite samples are
not extrapolated. Full residue dependence and other arithmetic features
remain outside this obstruction. See CT-001--003 in the
[contact proof](CONTACT_TRANSPORT.md).

## 3. Actual inverse transport has useful budgets on its stated domain

On positive odd integers let `U(x)=(3x+1)/2^a(x)` and

\[
(Lf)(t)=\sum_{Ux=t}\frac3{2^{a(x)}}f(x),\qquad
H(f)=\sum_x\frac{f(x)}x.
\]

For nonnegative f with finite H, the exact harmonic loss is

\[
H(Lf)+\sum_x\frac{f(x)}{x(3x+1)}=H(f).
\]

It gives all-depth pointwise Green bounds for the **actually transported**
distributions. First-hit injectivity and exact periodic renewal also give

\[
\sum_{q=0}^Q\rho_q(t)
\le\kappa_t\left[t(1+Q\log96)+\frac98(64/81)^Q\right],
\qquad \rho_q=L^q1,\quad\kappa_t\le3t+1.
\]

The qualitative linear cumulative bound and renewal argument already occur
in Valbuena's manuscript and are credited, not claimed as new discoveries.
The displayed root dependence and domain/frontier formulations are spelled
out here. For a prefix-free actual inverse frontier of maximum depth D,
the weighted sum of endpoint depth averages is bounded by the original
root's cumulative mass through D+Q. This removes the endpoint-height factor
when D=O(Q), while retaining the same root and literal clocks.

A decaying-source Green potential `V_epsilon=sum_q L^q(x^(-epsilon))`
also gives a finite budget on arbitrary prefix-free stopping frontiers,
without a length bound. These are weighted inverse statements. They do not
imply the missing unweighted contact inequality. See
[INVERSE_GREEN.md](INVERSE_GREEN.md), IFT-001--006; the positive Abel lower
bound there is separately **SOURCE-QUALIFIED** through its external density
premise.

## 4. Exact spectrum and the computational cost of the potential

For the harmonic Banach space `H={f:sum |f(x)|/x<infinity}`, and after killing
any finite set K, the complete result is

\[
\sigma(L_K)=\sigma_{\mathrm{ess,Fredholm}}(L_K)
=\{z:|z|\le1\}.
\]

Every interior point has an infinite-dimensional eigenspace. Every point of
the unit circle is an approximate eigenvalue, although each nonzero vector
loses norm strictly in one step. Genuine positive inverse rays into one give
the eigenvectors. These rays exist regardless of the truth of Collatz.
Equivalent norms, compact corrections, and finite terminal sets therefore
cannot create a spectral gap in this space. Other arithmetic spaces and
other operators remain available.

The inherited finite-simple-path reciprocal estimate identifies the remaining
harmonic mass exactly with escape mass. Strong stability of L_K is equivalent
to eventual periodicity of every positive orbit, **with a separate cycle
exclusion still required for full Collatz**.

There is also an effective distinction: the pointwise finite potential
`V_1(t)=sum_q L^q(x -> 1/x)(t)` is a computable real if and only if the actual
predecessor basin of t is decidable. Uniform computability is equivalent to
uniform reachability decidability. This is not a noncomputability claim; it
shows exactly what information an effective evaluator would need.
See [HARMONIC_SPECTRUM_AND_COMPUTABILITY.md](HARMONIC_SPECTRUM_AND_COMPUTABILITY.md),
HS-001--004, and the [root reconstruction](ROOT_REVIEW.md).

## 5. Literature comparison strengthens a specific failed census

Valbuena's short non-L2 stationary-law argument was independently reconstructed
for the finite ternary reference laws. An exact energy identity and layer cake
then exclude every integrable uniform clipping envelope. In particular a
polynomial clipping error `C U^(-delta)` must have delta<=1.

For the particular global clipping/source-charge census used in the first
packet, this raises its target-loss exponent obstruction from log_2(3) to 2.
This is a limit on that mechanism, not on actual predecessor density.
Newly located papers claim stronger reciprocal density estimates using
different inputs. Their reported formalization was not replayed here.
See [CRITICAL_ENERGY.md](CRITICAL_ENERGY.md), the
[energy review](CRITICAL_ENERGY_REVIEW.md), and the
[source ledger](../../reports/beeping-density-swarm-20261031/EXTERNAL_SOURCES.md).

## 6. What remains open, and how to reproduce this pass

The concentration track did not turn PR140's collision bound into the
source-height-violating repeated blocks needed for descent. Fixed-window
limits, rare collisions at late times, and moving positive witnesses remain
distinct from a contradiction for one ordinary starting integer.

The best next targets are now precise:

1. Construct an arithmetic contact trace beyond the excluded weight class,
   controlling every complete incoming fan; or give a total physical merger
   selector on the same section.
2. Control prescribed-depth inverse profiles or inverse-exponent boundary
   flux for the actual transported law, beyond the averages established here.
3. Prove concentration for the actual stopping observable using information
   absent from generic almost-invariant functions and finite completion models.

The [experiment instructions](../../experiments/beeping-density-swarm-20261031/README.md)
describe the bounded exact replay. The
[execution and provenance record](../../reports/beeping-density-swarm-20261031/README.md)
pins dependencies, review scope, complete saved outputs, and file hashes.
Repository integrity, bounded computation, and a universal mathematical proof
are separate evidence levels throughout.
