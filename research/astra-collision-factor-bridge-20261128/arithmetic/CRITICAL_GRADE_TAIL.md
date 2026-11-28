# A one-copy critical odd-count tail sufficient for full Collatz

Date: 2026-11-28. **Source-qualified written theorem and stationary
consumer.** The lower bound identified below remains unproved. The
reduction removes both the second stationary copy and the endpoint
coincidence test from the sufficient estimate for full Collatz. It retains
the shrinking ordinary-integer selector; an unconditional binomial law
for the driving bits does not supply the estimate.

Use the native shortcut map

\[
T(n)=\begin{cases}n/2,&2\mid n,\\(3n+1)/2,&2\nmid n,\end{cases}
\]

and let \(a_h(n)\) count odd departures among the first \(h\) steps.
All logarithms below are natural. Set

\[
\delta_1=\log2-\tfrac12\log3,\qquad
\mu=\delta_1^{-1},\qquad
\sigma^2=\frac{2(\log3)^2}{\log^3(4/3)},\qquad
h_X=\lfloor\mu\log X\rfloor,
\tag{1}
\]

\[
W_X(n)=\frac{a_{h_X}(n)-h_X/2}{\sqrt{h_X}/2},\qquad
L_X(n)=X\,3^{a_{h_X}(n)}2^{-h_X}.
\tag{2}
\]

The random source is uniform on \(1,\ldots,X\). We use the published
proper minimum law and its joint Gaussian first-attainment clock, as
specified in the earlier
[synchronous collision note](../../astra-critical-rigidity-20261128/ordinary/SYNCHRONOUS_PHASE_DISPERSION.md).
We also use the uniform orbit-set sparsity theorem of Leen's *Teeth*
paper, in the elementary consequence (5) below. Positive predecessor
density is used only for the final upgrade from density-one convergence
to universal convergence.

## 1. The exact negative-tail formula

For each genuine positive shortcut cycle \(C\), let \(P_C\) be its
period, \(q_C\) its number of odd states, and \(d_C\) the natural density
of its entire basin. Define

\[
\alpha_C=q_C/P_C,\qquad
\delta_C=\log2-\alpha_C\log3>0,\qquad
r_C=\delta_C/\delta_1.
\tag{3}
\]

Then, for every fixed \(z>0\),

\[
\boxed{
\lim_{X\to\infty}\Pr\{W_X\le-z\}
=\sum_{C\ \mathrm{cyclic}}d_C\,\Phi(-z/r_C).}
\tag{4}
\]

Escaping components contribute zero to this strictly negative tail.
They need not be excluded or assigned a fresh random parity law to prove
(4). No phase equidistribution or two-source merger theorem is needed
for this formula.

### 1.1. A uniform lower bound before a cycle

The orbit-packing input says that for some \(\theta<1\) and
\(C_\theta<\infty\), every set \(O\) of distinct values from a native
shortcut orbit obeys
\(\#(O\cap[b,b+M))\le C_\theta M^\theta\).
Summing over dyadic intervals therefore supplies an absolute finite
constant \(B\) such that

\[
\sum_{v\in O,\ v\ \mathrm{odd}}
\log(1+1/(3v))\le B.
\tag{5}
\]

This is a bound on distinct states. It does not hold for an indefinitely
repeated cycle with multiplicity. That distinction is used throughout.

For the exact finite native path \(x_0=n,\ldots,x_h=y\), multiplication
of the one-step identities gives

\[
\frac{3^{a_h(n)}2^{-h}n}{y}
=\prod_{\substack{0\le j<h\\x_j\ \mathrm{odd}}}
\frac{3x_j}{3x_j+1}.
\tag{6}
\]

If \(y\) is nonperiodic, no state of this finite path repeats: a
repetition would put every later state, including \(y\), on a cycle.
Hence (5) and (6) give

\[
L_X(n)\ge e^{-B}y\,X/n\ge e^{-B}
\qquad(n\le X,\ y\ \mathrm{nonperiodic}).
\tag{7}
\]

On the other hand,

\[
\log L_X(n)
=\frac{\log3}{2}\sqrt{h_X}\,W_X(n)
+\log X-\delta_1h_X,
\qquad 0\le\log X-\delta_1h_X<\delta_1.
\tag{8}
\]

For each fixed \(z>0\), the right side tends uniformly to \(-\infty\)
on \(\{W_X\le-z\}\). Thus, for all sufficiently large \(X\), every
source in this event already has a periodic endpoint at time \(h_X\).
In particular a source from an escaping component cannot be in the event.

### 1.2. Each cyclic component has its own contraction scale

Let \(t_C(n)\) be first entry into \(C\). Before entry the path is
distinct, so its logarithmic product in (6) lies in \([-B,0]\).
Around one complete turn of \(C\), (6) gives

\[
\prod_{v\in C,\ v\ \mathrm{odd}}\frac{3v}{3v+1}
=\frac{3^{q_C}}{2^{P_C}}
=e^{-\delta_CP_C}<1.
\tag{9}
\]

For any already-entered source \(n\) and any remaining number of
steps, the incomplete last turn contributes a bounded error depending
only on \(C\). Since the endpoint belongs to the fixed finite cycle,
(6) therefore yields

\[
\log L_X(n)
=-\delta_C(h_X-t_C(n))+
\log(X/n)+O_C(1),\qquad t_C(n)\le h_X.
\tag{10}
\]

The error is uniform over such \(n,X\). The random term \(\log(X/n)\)
is tight even without conditioning, because its upper-tail probability
is at most \(e^{-u}\). This remains negligible after normalization on
any component, with its unnormalized source mass.

Write \(m(n)\) for the global orbit minimum and \(\tau_*(n)\) for its
first attainment. The proper minimum law makes the minimum tight. On
the basin of a fixed cycle, \(t_C-\tau_*\) is tight: entry before the
minimum costs fewer than \(P_C\) further steps, while entry after it
costs the fixed time from the attained minimum to the cycle; truncate the
minimum to a finite set. The joint minimum/clock theorem consequently
gives the finite-measure convergence

\[
\Pr\left\{n\in\operatorname{Basin}(C),
\frac{t_C(n)-h_X}{\sigma\sqrt{\log X}}\le u\right\}
\longrightarrow d_C\Phi(u).
\tag{11}
\]

The normalizing constants satisfy

\[
\sigma\delta_1=\frac{\log3}{2}\sqrt\mu.
\tag{12}
\]

Combining (8), (10), and (12), on entered sources,

\[
W_X(n)=r_C\frac{t_C(n)-h_X}
{\sigma\sqrt{\log X}}+o_{\Pr}(1).
\tag{13}
\]

For the strictly negative threshold \(-z\), the clock on the right is
bounded away from zero, so it already guarantees entry. Sources not yet
entered are excluded by (7). Sandwich the event using a fixed small
error in (13), apply the continuity in (11), and then let the error tend
to zero. This proves the \(C\)-term of (4).

Finally, a source and its global minimum belong to the same asynchronous
component. The proper discrete minimum law therefore pushes forward to
the entire component law in total variation. Given \(\varepsilon>0\),
retain finitely many cycles whose omitted cyclic basin density is less
than \(\varepsilon\). Their complement has the same limiting mass,
and escaping components contribute nothing by (7). This justifies the
countable sum in (4); no uniform error over all cycles is assumed.

## 2. A uniform gap for every other positive cycle

The known cycle \(C_1=\{1,2\}\) has \(\alpha_1=1/2\) and \(r_1=1\).
A different positive cycle cannot contain 1 or 2, and every odd state
on it is at least 3. Multiplying the exact value ratios around the cycle
gives

\[
2^{P_C}=\prod_{v\in C,\ v\ \mathrm{odd}}(3+1/v)
\le(10/3)^{q_C}.
\tag{14}
\]

Consequently

\[
\alpha_C\ge\frac{\log2}{\log(10/3)}>\frac12,
\qquad
0<r_C\le r_*:=
\frac{\log2\,[1-\log3/\log(10/3)]}
{\log2-\tfrac12\log3}<1.
\tag{15}
\]

The lower positivity in (3) also follows from (9): the cycle product is
strictly less than one. Numerically \(r_*\approx0.42170026\); no decimal
estimate is used in the proof.

Let \(b=d_{C_1}\). Formula (4) now gives the explicit universal bound

\[
\boxed{
\lim_{X\to\infty}\Pr\{W_X\le-z\}
\le b\Phi(-z)+(1-b)\Phi(-z/r_*)\le\Phi(-z).}
\tag{16}
\]

Escaping mass is allowed inside \(1-b\) on the right; assigning it the
larger nontrivial-cycle contribution only weakens the inequality. Thus

\[
\Phi(-z)-\lim_X\Pr\{W_X\le-z\}
\ge(1-b)\,[\Phi(-z)-\Phi(-z/r_*)].
\tag{17}
\]

For example \(z=1\) gives a positive coefficient approximately
0.14979 multiplying \(1-b\). The exact positive coefficient in (17),
not this numerical illustration, is the relevant assertion.

### One quantile is enough

With the named positive-predecessor input, the following are equivalent:

1. every positive integer reaches the known cycle;
2. for one fixed \(z>0\),
   \(\liminf_X\Pr\{W_X\le-z\}\ge\Phi(-z)\);
3. for every fixed \(z>0\), the limit in (4) equals \(\Phi(-z)\).

Indeed, universal convergence makes \(d_{C_1}=1\), which proves the
tail equalities by (4). Conversely (17) forces \(b=1\). A positive
integer outside the known basin has a disjoint positive-density
predecessor population, so \(b=1\) is impossible unless the conjecture
holds. Without positive predecessors, the same argument proves only
density-one convergence.

This uses one strictly negative critical quantile. Sending \(z\downarrow0\)
after the limit in (4) detects one half of the total cyclic mass, and
does not separate the known cycle from other cycles. An assertion at
the exact finite-cutoff threshold \(W_X\le0\) would need a separate
boundary argument and is not claimed here. A full fresh binomial law
after the minimum is neither used nor claimed.

## 3. The stationary condition has one path and no endpoint label

Use the fair jointly stationary real/ternary affine pair from
[STATIONARY_COLLISION_CONSUMER.md](../factoring/STATIONARY_COLLISION_CONSUMER.md),
driven for \(h=h_X\) future steps by fair bits, and let \(A_h\) be
their grade. Put \(q_a=3^a\), \(L_a=q_a2^{-h}X\), and let \(r_a\) be
the least nonnegative representative of \(Z_h\bmod q_a\). Define

\[
K_{h,X}=
\left\lfloor\frac{R_h+L_{A_h}-r_{A_h}}{q_{A_h}}\right\rfloor
-\left\lfloor\frac{R_h-r_{A_h}}{q_{A_h}}\right\rfloor.
\tag{18}
\]

In this regime \(X\le2^h\) for large \(X\), hence \(K_{h,X}\in\{0,1\}\).
It is the one-copy positive ordinary selector, with its full ternary
conductor and real interval retained. In particular

\[
\Pr\{K_{h,X}=1\}=X/2^h
\tag{19}
\]

exactly. No target \(y\), target sum, or second copy occurs in (18).
Let

\[
b_{h,z}=\left\lfloor h/2-z\sqrt h/2\right\rfloor.
\tag{20}
\]

The full grade-and-endpoint total-variation transfer in the linked note
applies to the union of all bins whose grade is at most \(b_{h,z}\).
Its fair-seed error is \(O(\log X/X)\), uniformly in \(h\). Therefore

\[
\boxed{
\frac{2^h}{X}
\Pr\{K_{h,X}=1,\ A_h\le b_{h,z}\}
=\Pr\{W_X\le-z\}+O(\log X/X).}
\tag{21}
\]

Combining (4) and (21) gives the exact limiting relative mass of this
one-copy stationary event. A sufficient estimate for full Collatz is
just

\[
\boxed{
\Pr\{K_{h_X,X}=1,\ A_{h_X}\le b_{h_X,z}\}
\ge[\Phi(-z)-o(1)]\frac X{2^{h_X}}
\quad\text{for one fixed }z>0.}
\tag{22}
\]

This would imply the maximal median collision coefficient \(1/8\)
through the already established synchronous theorem. It also follows
directly from full Collatz, by (4) and (21). The unresolved estimate is
relative to \(X/2^h\), rather than the smaller two-copy scale
\(X^2/4^h\). Its grade threshold is explicit, and the two comparisons
in (18) can be evaluated from one real interval and one ternary residue.

Under the original fair driving law \(A_h\sim\operatorname{Bin}(h,1/2)\).
It does not follow that this binomial law survives conditioning on the
rare event \(K_{h,X}=1\). Equation (17) specifies quantitatively what
failure would encode. A proposed estimator may target (22) directly;
dropping the selector would erase the arithmetic claim.

## 4. Why the product-Haar Jacobian does not give the missing bound

Each fair affine branch has product-Haar Jacobian \(1/2\), equal to its
driving probability. This does not make the stationary measure Haar,
absolutely continuous, or a disjoint finite-volume tile. Weaver's
original [joint-law manuscript](https://rstation.ai/r/collatz/posts/33)
(Paper 19/v2, Sections 1--7 and 10) proves pure singularity. For a fixed
unit rectangle, its finite-depth image union has Haar volume of order
\(h^{-1/2}\), while image multiplicity has growing moments. The same
law has full product-metric dimension two. These facts coexist because
cross-grade image overlap produces logarithmic entropy loss.

Thus an absolutely continuous tile premise is not available for the
actual law. The earlier source already makes explicit that its compact
quotient collapses integer diagonals and supplies no uniform
moving-integer trace. Neither full dimension nor weak quotient mixing
proves the relative, grade-selected bound (22). This note has not proved
that bound; it identifies a smaller one-copy target for a genuinely new
arithmetic estimate.

## 5. Provenance and verification scope

The native finite product (6), cycle estimate (14), quantile mixture
(4), and stationary consumer (22) are reconstructed here from their
stated inputs. No exhaustive priority claim is made. The orbit-packing
argument is prior Leen; the stationary joint affine law and its
singularity are prior Weaver; the joint minimum/clock theorem is prior
Leen; positive predecessors are prior Mazur. The ordinary-to-stationary
finite-window transfer is the factoring lane's work in this pass.

The parallel [PR 218 signed first-moment
note](https://github.com/GettysburgResearch/collatz/blob/aea80e35b6fc23cc909252a23e1ef5c945e1ca7e/research/astra-full-proof-20261128/descent/FIRST_MOMENT.md)
already uses the bound \(3+1/v\le10/3\) on bad positive orbits and
gives a postcritical signed first-moment sufficient condition. Its
observation time is the critical time plus a superdiffusive increment,
and its target is a signed averaged excess. Here the observation time
is the median critical clock itself, the statistic is one fixed negative
diffusive quantile, and (4) identifies its complete cyclic mixture. The
elementary \(10/3\) bound is shared prior arithmetic, not a new estimate.

The packing source inspected is *Gaussian but not locally Gaussian:
the teeth of the Collatz stopping-time histogram*,
[Zenodo 23252397](https://doi.org/10.5281/zenodo.23252397), Input
"Uniform sparsity of orbit sets" and the final appendix. The retained
source `collatz-teeth.tex` has SHA256
`a58e9bf970aed4700c1338770270ae8bf983278c593f5b5a87351ac473ea4b3a`.
Its proof uses synchronous injectivity on an orbit set, exact parity
cylinders, and a dyadic recurrence; it does not import positive
predecessors. A hash-pinned source/review receipt accompanies this note.
The minimum/clock source is Leen's
[Zenodo 23269488](https://doi.org/10.5281/zenodo.23269488), already pinned
in this pass's independent reconstruction.

This is a written theorem conditional on those named external analytic
inputs. No new Lean certification of (4), (21), or (22) is claimed.
