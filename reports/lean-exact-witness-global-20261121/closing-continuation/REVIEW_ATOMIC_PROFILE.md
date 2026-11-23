# Independent review of the atomic continuation

Date: 23 November 2026.

Reviewer: `cycle_exclusion`, separate from the author `atomic_exclusion`.

## Frozen source and verdict

The source is the continuation for owned PR177, based on commit
`6de3e304bb49a93a6c5ef0e5563137e75c7defb4`:

`research/lean-exact-witness-global-20261121/ATOMIC_EXCLUSION_CONTINUATION.md`

The reviewed new file has SHA256
`c4d2c2124f51d4cd8dd59e9169197da7a79d45b4f290d2379151185c501db16a`.
This content hash, rather than an as-yet-uncreated checkpoint commit,
fixes the review boundary. The verdict does not extend to later edits.

**VERIFIED, at the written mathematical level:** AE-P3, AE-P4,
the finite product-cylinder routing and ordinary realization, and the
Section 7 lifted-operator identities and continuous-eigenfunction
obstruction. The reviewed source correctly keeps rational periodic
points, finite ordinary realizations, and ordinary infinite components
separate. No new gap or correction was needed in this version.

**VERIFIED RELATIVE TO THE STATED INHERITED INPUT:** the atom calculations,
total-variation limits, and barrier implications in Sections 2--4. Their
identification of the surviving atoms with escaping components uses
the explicitly cited HE2 and HE18--HE24a in `HIGH_VARIANCE_ESCAPE.md`
at the base commit. This review reconstructs the new deductions; it does
not claim a new independent verification of that earlier infinite-orbit
input or its earlier review.

**OPEN:** vanishing of the total ordinary escape remainder, existence
of the required pointwise positive integrable eigenfunction on an
ordinary escaping component, ordinary cycle exclusion, and the full
Collatz theorem. None follows from the reviewed profile obstruction.

This is proof reconstruction and primary-source inspection. It is not a
Lean verification and not a finite computation presented as an infinite
theorem.

## 1. Maps, domains, and affine normalization

I used the source's ordinary domain

\[
 O=\{n\in\mathbb Z_{>0}:2\nmid n,\ 3\nmid n\},\qquad
 U(n)=\frac{3n+1}{2^{a(n)}},\quad a(n)=v_2(3n+1),
\]

and the product domain
`Y=Z_2^times x Z_3^times`, with its two coordinates independent except
when an ordinary or rational diagonal point is explicitly selected.

For a word of `r` positive gaps with total `A`, write its forward affine
map as `F_W(t)=w t+b`, where `w=3^r/2^A` and `b=C/2^A>0`.
Iterating the actual barrier

\[
 3v(n)\le 1+2^{a(n)}v(Un)
\]

gives exactly

\[
 v(F_W(n))\ge w v(n)-b.                 \tag{R1}
\]

The accumulated error is the same affine correction `b` as in the
ordinary forward map, with the opposite sign. It is not replaced by
`r`, discarded, or presumed uniform over arbitrary words. This exact
identity is used both for fixed rational-cycle words and for the two
growing ordinary blocks below.

## 2. AE-P3: independently reconstructed joint cycle density

Take an actual positive prefix `W` of length `h`, total exponent `A`,
and correction `C`. Append `L` gap-one steps and one final gap `e`.
Direct composition gives

\[
 C_* =3^{L+1}(C+2^A)-2^{A+L+1},\qquad
 D=3^{h+L+1}-2^{A+L+e},\qquad x=-C_*/D.                 \tag{R2}
\]

The correction is positive, odd, and a ternary unit; the denominator
is also odd and a ternary unit. The same statements apply to the
correction of every cyclic rotation. Each rational state therefore
has both unit properties. The edge identities then imply
`v_2(3x_i+1)=a_i` exactly, since the next state is a binary unit.
There is no reliance on the reduced denominator remaining equal to
the displayed denominator.

For a positive ordinary root `q` whose prefix is `W`, let
`q_h=(3^h q+C)/2^A`. The identity

\[
 C_*+Dq
 =3^{L+1}2^A(q_h+1)-2^{A+L}(2+2^e q)
\]

is divisible by `2^(A+1)`. Thus `x=q mod 2^(A+1)` for every
`L>=0` and `e>=1`. Choosing a sufficiently long actual prefix places
the rational root in any prescribed binary unit cylinder.

If `L+1>=K`, reducing (R2) modulo `3^K` gives

\[
 x\equiv -2^{1-e}\pmod {3^K}.          \tag{R3}
\]

Since 2 generates the units modulo `3^K`, a congruence class of `e`
modulo `2*3^(K-1)` selects any desired ternary unit cylinder.
Fix such an `e` and increase `L`: then `D>0` eventually, giving a
negative cycle. Alternatively fix a sufficiently large `L` and
increase `e` in its congruence class: then `D<0`, giving a positive
cycle. All rotations have the same sign because their corrections
are positive and their common denominator has the chosen sign.

This proves separate density of positive and negative rational cycle
points in the full product `Y`. Neither primitivity nor integer
integrality is asserted or needed. The positive rational construction
does not give a positive ordinary integer cycle.

## 3. AE-P4 away from the exceptional power

Suppose

\[
 v(n)=h(n)F(n,n)+o(h(n)),\qquad
 h(n)=n^\beta(\log n)^\delta,
\]

where `beta>0`, `delta` is real, `F:Y->[0,infinity)` is continuous,
and the error is uniform over ordinary `n` tending to infinity.
The barrier may fail at finitely many ordinary values.

Fix one rational cycle point `x` and its whole word. Ordinary CRT
approximants can be chosen arbitrarily large, with precision
`2^(A+k)` and `3^k` at `x`. Their entire fixed word is exact.
Every real intermediate value tends to infinity, so all sufficiently
late approximants avoid the finite exceptional set. If `n_k` is a
start and `m_k=w n_k+b` its endpoint, both diagonal points converge
to `x` in `Y`. Equation (R1), continuity, and

\[
 \frac{h(w n_k+b)}{h(n_k)}\longrightarrow w^\beta,
 \qquad \frac b{h(n_k)}\longrightarrow0
\]

therefore imply `w^beta F(x)>=w F(x)`.

For `beta<1`, the negative cycles have `w>1`, and so force `F=0`
at their dense set of roots. For `beta>1`, the positive cycles have
`0<w<1` and do the same. Continuity yields `F=0` everywhere.
The ordinary approximants here are different positive integers as
precision increases; they are not an ordinary infinite realization of
the rational cycle.

## 4. The index-one case and finite product-cylinder routing

When `beta=1`, the same fixed-branch limiting argument gives
`F(z)<=F(Sz)` whenever the binary valuation
`a(z)=v_2(3z_2+1)` is finite, where

\[
 S(z_2,z_3)=
 \left((3z_2+1)/2^{a(z)},(3z_3+1)/2^{a(z)}\right).
\]

The binary pole is `z_2=-1/3`; it is not assigned an artificial finite
gap. Every other gap branch is open and closed, and the ternary
coordinate stays a unit because `3z_3+1=1 mod 3`.

I reconstructed a finite bridge between any two nonempty product
cylinders as follows.

1. Choose an actual positive prefix `W` whose binary cylinder lies
   inside the source binary cylinder.
2. After `W`, append `L` gap-one steps. On the ternary coordinate,
   these send `y` to `-1+(3/2)^L(y+1)`. For sufficiently large `L`,
   this is `-1` to the target ternary precision, uniformly in the
   original source ternary unit.
3. A final gap `e`, selected as in (R3), reaches the target ternary
   cylinder.
4. Choose any binary unit in the target binary cylinder and pull it
   back through this entire finite word using `(2^a y-1)/3`.
   Every pullback is a binary unit and has the prescribed next gap
   exactly. Pulling back the fixed initial prefix `W` places the
   start in its prescribed binary cylinder: any two odd tails
   differ by a multiple of 2, hence the starting values differ by
   a multiple of `2^(A+1)`.

The source ternary coordinate and pulled-back binary coordinate may be
chosen independently. The constructed finite orbit avoids the binary
pole because each succeeding binary tail is a unit. All finitely many
gap constraints and the endpoint cylinder persist on a sufficiently
small product neighborhood of the starting pair. CRT then provides
arbitrarily large positive ordinary integers in that neighborhood.
These integers realize the same finite bridge. This last assertion is
finite and does not claim an infinite ordinary orbit with arbitrarily
prescribed behavior.

Apply `F<=F composed with S` along the bridge, choose source and target
cylinders where `F` is as close as desired to any two specified values,
and route in both directions. This forces those values to be equal.
Continuity also covers the pole fiber. Thus `F` is constant. If it is
nonzero, write its constant value as `c>0`.

## 5. The logarithmic exponent and the full lower-order error

The logarithmic step does not assume differentiability, a modulus of
continuity, or a rate for the `o(h)` remainder.

For `delta<0`, take even `k` and

\[
 n_k=2^{k+1}-1,\quad
 q_k=2\,3^k-1,\quad w_k=(3/2)^k.
\]

The exact `k` intermediate steps are
`2^(k+1-j)3^j-1`, and have gap one for `j<k`.
Evenness of `k` makes the initial value a ternary unit; all subsequent
states are also units. All states tend to infinity with `k`, so
finitely many exceptional ordinary values do not enter. Equation (R1)
has error `b_k=w_k-1`. With `alpha=log(3)/log(2)`, the uniform asymptotic
formula gives

\[
 \frac{v(q_k)}{w_kv(n_k)}\longrightarrow\alpha^\delta<1,
 \qquad
 \frac{w_k-1}{w_kv(n_k)}\longrightarrow0,
\]

contradicting the barrier. The word stops after exactly `k` gap-one
steps; the following gap is not presumed to be one.

For `delta>0`, take

\[
 n_k=1+2^{2k+2},\quad
 q_k=1+4\,3^k,\quad w_k=(3/4)^k.
\]

Its states are `1+2^(2(k-j)+2)3^j`. Each of the first `k` gaps is
exactly two, all states are ternary units, and the smallest state is
the endpoint, which still tends to infinity. Here `b_k=1-w_k` and

\[
 \frac{v(q_k)}{w_kv(n_k)}\longrightarrow(\alpha/2)^\delta<1,
 \qquad
 \frac{1-w_k}{w_kv(n_k)}\longrightarrow0.
\]

The second limit uses `w_kv(n_k)` growing as a positive constant times
`3^k k^delta`. These endpoint comparisons keep the full lower-order
error; intermediate errors are not separately summed.

Therefore a nonzero profile has `beta=1`, `delta=0`, and constant
`F`. The exceptional case is real: `v(n)=c n` obeys the affine barrier.
The statement is a necessary classification of these leading profiles,
not a sufficiency assertion for every arbitrary `o(n)` perturbation.
The separate qualification concerning general slowly varying factors
is necessary and correctly retained: the two displayed logarithmic
ratios do not exclude, for example, all index-one iterated-log scales.

## 6. Section 7: product operator and its closing test

For the branch `I_e(q)=(2^e q-1)/3`, the binary image has measure
factor `2^-e` and consists exactly of the valuation-`e` stratum.
The ternary legality domain is the inverse image of the unit set;
on that domain `I_e` has measure factor 3. Thus its product Jacobian
is `3/2^e`, using normalized Haar probabilities on both unit groups.
Changing variables branch by branch gives

\[
 \int Q_s f\,dm_Y
 =\int (3/2^{a(z)})^{s-1}f(z)\,dm_Y(z).
\]

The strata partition all binary units except the pole, a null fiber.
In particular `m_Y Q_1=m_Y`. The multiplier is a valuation-dependent
function for general `s`, not the scalar multiplier of the old
ternary-only operator.

The component atom relation lifts to the ordinary diagonal because a
legal inverse branch of an ordinary unit root is a positive ordinary
odd unit parent. The proposed full-support construction also checks.
For a fixed component root `q` and initial word `W`, set

\[
 n=\frac{2^{A+e}q-2^A-3C}{3^{h+1}}.
\]

Solving the displayed congruence in the source modulo `3^(h+K+1)`
makes `n` integral and gives its desired unit class modulo `3^K`.
The right side of that congruence is a unit, so the primitive-root
property provides arbitrarily large suitable `e`. Backward binary
composition gives exact gaps and oddness. Integrality of the start
then propagates through these exact divisions, and large `e` makes
all intermediate ordinary values positive. Their ternary unit property
propagates forward. These parents lie in the component of `q` and in
the desired product cylinder.

If a nonnegative `h` satisfies `Q_s h=h` on the ordinary component,
is positive at an atom, and is integrable against its finite component
measure `mu`, then `nu=h mu` is a nonzero finite `S`-invariant measure.
The calculation is `Q_s[(f composed with S)h]=f Q_s h` followed by
`mu Q_s=mu`. Every future atom of an initial positive atom must then
have at least its mass. A nonperiodic ordinary orbit has infinitely
many distinct future vertices, contradicting finiteness. Thus the
claimed eigenfunction would close escape, but its existence is not
established.

At a negative rational cycle, a single return branch of `Q_s^r` has
weight `w^s>1`. Positivity implies `h(x)>=w^s h(x)` for any finite
nonnegative pointwise eigenfunction. Hence it vanishes at every such
cycle point. AE-P3 and continuity force `h=0` on all of `Y`.
This argument works for every `s>0`. It rules out nonzero continuous
right eigenfunctions of the specified kind, not measurable functions
defined only almost everywhere or functions confined to an ordinary
countable set.

## 7. Primary-source scope independently checked

I opened both primary PDFs and checked the cited statements directly.

- [Sarig, Theorem 4.9, PDF page 16](https://www.weizmann.ac.il/math/sarigo/sites/math.sarigo/files/uploads/tdf-survey.pdf)
  assumes a topologically mixing countable Markov shift, summable
  variations, and finite Gurevich pressure. Positive recurrence is
  equivalent to the normalized integrable positive eigenfunction and
  conservative conformal-measure pair; the eigenvalue is the exponential
  of pressure. It does not make an arbitrary finite conformal measure
  conservative, identify it with the theorem's measure, or supply the
  ordinary component presentation missing here.
- [Tao, arXiv:1909.03562v7, Remark 1.13 and Proposition 1.14, pages 11--12](https://arxiv.org/pdf/1909.03562v7)
  give compatible laws whose cylinder densities satisfy
  `||h_n-h_m||_1<=C_A m^-A` for `n>=m`. This superpolynomial bound
  makes the densities `L1`-Cauchy; no exponential estimate is used.
  The law is supported on ternary units and stationary for
  `X=(3X'+1)/2^e`, with independent gap probabilities `2^-e`.

I independently derived the density consequence: ternary change of
variables gives weights `3*2^-e` and therefore a binary-independent
`Q_1` eigenfunction almost everywhere. This deduction asserts no
pointwise regularity. The ordinary diagonal is product-Haar null, so
the statement supplies neither its pointwise values and equation nor
integrability against an ordinary atomic measure. Its parameter is
`s=1`; the finite component measures here use `s>1`. Both limitations
in the reviewed source are correct.

## 8. Earlier sections: reconstructed algebra and remaining dependence

The atom formula is
`(H_s P_s^N)({n})=n^-s Lambda_N(n)^s`, and domination by `n^-s`
for `s>1` justifies total-variation convergence. Finite telescoping
then gives the displayed global defect decomposition. Its
identification with the escape cone retains the inherited product
positivity input identified above; this review does not silently
remove that dependence.

The two mass formulas in Section 2 follow respectively by excluding
the 2- and 3-divisible integers and by separating `n=6j+1` and `n=6j+5`.
For the latter, the atoms are `(3/(18j+4))^s` and
`(3/(18j+16))^s`, giving the stated two Hurwitz-zeta arguments.
At `s=2`, `H_s(X)=pi^2/9`. None evaluates the defect Green integral
as the entire mass or proves that the remainder vanishes.

For shifted weights, the transported atom is
`n^-s Lambda_N(n)^s [U^N(n)/(U^N(n)+t)]^s`.
The two limiting orders are justified separately by dominated
convergence. The one-step excessivity condition is exactly
`1+(2^a-3)t>=0`; gap one occurs in the ordinary unit domain, so
the stated range `0<=t<=1` is exact.

For arithmetic shifts, direct cross-multiplication yields precisely
the affine barrier (R1), without any sign reversal. The proposed
trailing-ones candidate has equality along gap one and fails at the
actual edge `41 -> 31` with gap two. Its continuous leading profile
falls within AE-P4's excluded nonzero power cases. Those observations
refute that barrier construction; they do not refute the possibility
of discontinuous or differently scaled arithmetic barriers.

## 9. Result of the review

The new deductions survive independent reconstruction with all
requested ordinary-realization and error-term boundaries intact.
The strongest reviewed advance is the complete obstruction for the
specified nonzero continuous power-logarithm leading profiles,
together with the stronger product-space obstruction to continuous
right eigenfunctions. These determine what the proposed closing
mechanisms cannot supply. The full ordinary escape remainder and
integer-cycle denominator remain separate open arithmetic tasks.
