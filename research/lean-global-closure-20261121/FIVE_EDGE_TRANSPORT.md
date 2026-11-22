# Exact five-edge transport and the finite-stencil obstruction

Date: 2026-11-22. Author: `global_certificate22`.

This note supplies the actual forward-transport part of the joint
Dirichlet-energy investigation. It proves whole-graph statements:
an exact one-step energy recurrence, unbounded affine slopes under
transport of five-edges, and failure of a uniform five-energy estimate
for arbitrary finitely supported inputs even after Cesaro averaging.
The last failure is proved separately for the shortcut map, the
accelerated odd map, and the precise killed operator used in the
Dirichlet calculation. None of the arguments is a finite residue census.

The accompanying analytic note owns the canonical Green-potential
Dirichlet theorem and the quantitative Cesaro/Abel energy bounds. The
obstructions here do not disprove an additional estimate specific to
that canonical potential.

## 1. Definitions and the exact energy recurrence

Use the ordinary shortcut map on positive integers:

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.\end{cases}
\]

For an arbitrary real-valued function on the positive integers, put

\[
\mathcal F_5(f)=\sum_{n\ge1}\frac{|f(5n)-f(n)|}{n},
\qquad
E_5(f)=\sum_{\substack{n\ge1\text{ odd}\\3\nmid n}}
\frac{|f(5n)-f(n)|}{n}.
\tag{1}
\]

The latter is the repository's odd ternary-unit energy. All identities
in this section hold as identities of extended nonnegative sums, so no
unstated summability assumption is needed.

For even `n`, `T(5n)=5T(n)`. For odd `n`, `T(5n)=5T(n)-2`.
Splitting the first sum into even and odd inputs and setting
`q=(3n+1)/2` on the odd part gives exactly

\[
\boxed{
\mathcal F_5(f\circ T)=\frac12\mathcal F_5(f)
+\sum_{\substack{q\ge2\\q\equiv2\pmod3}}
\frac{3}{2q-1}|f(5q-2)-f(q)|.}
\tag{2}
\]

For the repository energy, the input `n` is already odd. The allowed
classes `n=6a+1` and `n=6a+5` give respectively `q=9a+2` and `q=9a+8`.
Consequently

\[
\boxed{
E_5(f\circ T)=
\sum_{\substack{q\ge2\\q\equiv2,8\pmod9}}
\frac{3}{2q-1}|f(5q-2)-f(q)|.}
\tag{3}
\]

There is no even-input half term in (3). The change from (1) to the
offset `-2` is an actual forward identity, not an inequality or an
inverse-branch resampling step.

## 2. Translated five-edges do not form a closed finite stencil

Consider an edge with ordered endpoints `(5n+b,n)`, whenever both are
positive integers. If `b` is even, both endpoints have the same parity.
One simultaneous ordinary step gives

\[
\begin{array}{c|c|c}
\text{input}&\text{new base}&\text{new left endpoint}\\\hline
n=2k&k&5k+b/2\\
n=2k+1&3k+2&5(3k+2)+(3b-4)/2.
\end{array}
\tag{4}
\]

Thus an even offset changes to `b/2` or `(3b-4)/2`. Starting at `b=0`,
an odd first input gives `b=-2`; the next step gives `b=-1` or `b=-5`.
For an odd offset, the two endpoint parities differ, and the exact
formulas instead are

\[
\begin{array}{c|c|c}
\text{input}&\text{new base}&\text{new left endpoint}\\\hline
n=2k&k&15k+(3b+1)/2\\
n=2k+1&3k+2&5k+(5+b)/2.
\end{array}
\tag{5}
\]

The leading ratios in (5) are `15` and `5/3`. A family consisting only
of translates of slope five is therefore not closed under actual
forward transport.

The next theorem rules out repairing exact closure by adding merely a
finite number of other fixed affine slopes.

## 3. An ordinary positive ray generates infinitely many slopes

For every pair of integers `m,v>=1`, set

\[
k=3m,\qquad n=2^k v-1.
\]

Then

\[
\boxed{
T^k(n)=3^{3m}v-1,
\qquad T^k(5n)=5\,3^{2m}v-5.}
\tag{6}
\]

These are actual ordinary positive trajectories. One elementary proof
uses the signed shortcut map only as a finite parity template. Its
templates are

\[
-1\longmapsto-1,
\qquad -5\longmapsto-7\longmapsto-10\longmapsto-5.
\tag{7}
\]

The first template has one odd input per step. The second has two odd
inputs per three steps. If `z` is an integer seed and `j<=k`, the finite
affine-lift identity is

\[
T^j(2^k w+z)
=3^{o_j(z)}2^{k-j}w+S^j(z),
\tag{8}
\]

provided the initial left-hand argument is positive; its actual finite
trajectory is then positive throughout. Here `S` is the signed shortcut
map and `o_j(z)` is the number of odd inputs in its first `j` steps.
Identity (8) follows by induction, since the added term is even before
each remaining step. It is also exactly the finite-word positive-lift
mechanism formalized by `CollatzSignedCarry.finite_signed_lift`, after taking
the lift parameter at clock `j` to be `2^(k-j)w`.

Apply (8) to `z=-1,w=v` and `z=-5,w=5v`, and use (7). This proves (6).
No statement about convergence of negative or positive trajectories is
used. Restricting `v` to multiples of three makes the initial `n` and
`5n` odd ternary units, so the same rays are available inside the exact
domain of (1).

The ordered endpoint ray in (6) has leading ratio

\[
\frac{5\,3^{2m}}{3^{3m}}=\frac5{3^m}.
\tag{9}
\]

These ratios are all distinct. A fixed affine edge type
`(a x+b,x)` can contain infinitely many of the pairs on a given ray
only when its slope is exactly `a=5/3^m`: subtracting the two affine
functions of `v` otherwise gives a nonconstant linear equation, with
at most one solution. It follows that no finite list of fixed affine
edge types is exactly invariant under every simultaneous forward
iterate of the original five-edges. Allowing both orientations merely
adds reciprocal slopes and does not remove the obstruction.

### Bounded routing with finitely many translated five generators

Fix a finite set of integer offsets `B`, and allow a graph step

`x -> 5x+b` or its legal inverse `(x-b)/5`, with `b in B`.

Every fixed path word has rational affine form `x -> 5^a x+c`, with
integer `a` and rational `c`. For the two endpoint functions in (6),
equality of leading coefficients would require

\[
5\,3^{2m}=5^a3^{3m},\qquad\text{or}\qquad5=5^a3^m,
\]

which is impossible for `m>=1` by unique factorization. Thus a fixed
path word can join the endpoints for at most one parameter `v`.
For each finite length bound there are only finitely many words, so
they cannot route the entire positive ray. In particular, graph
distance along the ray has no uniform finite bound, even if an edge is
allowed to be traversed in either direction.

This conclusion does not exclude an unbounded path construction with
summable weighted congestion. It excludes exact finite-stencil closure
and bounded-length routing by finitely many translated five generators.

## 4. Uniform five-energy propagation is false for general inputs

The same ray gives a quantitative obstruction, including for forward
Cesaro averages. Let `m>=1`, `k=3m`, choose any positive multiple `v` of
30, and put

\[
n=2^kv-1,\qquad q=3^kv-1,\qquad f=\mathbf1_{\{q\}}.
\tag{10}
\]

The integer `q` is an odd ternary unit and is `4 mod 5`. The only
nonzero summand in `E_5(f)` is the one with base `q`, since `q/5` is not
an integer. Therefore

\[
E_5(f)=\frac1q.
\tag{11}
\]

For every `0<=j<=k`, the positive lift identities give

\[
T^j(n)=3^j2^{k-j}v-1,
\qquad
T^j(5n)=5\,3^{o_j(-5)}2^{k-j}v+s_j,
\tag{12}
\]

where `s_j` belongs to `{-5,-7,-10}`. The first expression equals `q`
exactly when `j=k`: equality of its leading coefficients requires
`2^(k-j)=3^(k-j)`. The second expression is `0` or `3 mod 5`, and hence
never equals `q`, which is `4 mod 5`. These statements hold for every
positive multiple of 30, without an exceptional-parameter removal.

Taking the original base `n` in the energy sum proves

\[
\frac{E_5(f\circ T^k)}{E_5(f)}\ge\frac qn
>\left(\frac32\right)^k.
\tag{13}
\]

Define the forward average, with exactly `N` time indices,

\[
A_Nf=\frac1N\sum_{j=0}^{N-1}f\circ T^j.
\]

By (12), `A_(k+1)f(n)=1/(k+1)` and `A_(k+1)f(5n)=0`. Hence

\[
\boxed{
\frac{E_5(A_{k+1}f)}{E_5(f)}
\ge\frac{q}{(k+1)n}
>\frac{(3/2)^k}{k+1}.}
\tag{14}
\]

Both sides concern finitely supported functions: a finite number of
ordinary shortcut inverse steps gives a finite set of predecessors.
Consequently the energies here are finite. Taking, for example, `v=30`
and allowing `m` to increase proves that no universal constant `C`
can satisfy either

`E_5(f o T^k) <= C E_5(f)` for all finitely supported `f,k`,

or

`E_5(A_N f) <= C E_5(f)` for all finitely supported `f,N`.

The input function depends on the time index in this counterexample.
It does not assert divergent averages for one fixed function, and it
does not refute an estimate for the canonical Green potential subject
to all its special identities.

## 5. Direct accelerated and killed-operator amplification

The operator in the accompanying Dirichlet calculation uses the
accelerated odd map

\[
U(x)=\frac{3x+1}{2^{v_2(3x+1)}}
\]

on positive odd ternary units. Its averages differ from shortcut-clock
averages. The following is a direct argument for `U`, followed by a
constructive choice that also makes it apply to the exact killed domain.

### 5.1 The actual accelerated ray

Fix any integer `k>=1` and any positive multiple `v` of 30, and set

\[
n=2^{2k}v-1,\qquad q=3^k2^kv-1,\qquad f=\mathbf1_{\{q\}}.
\tag{15}
\]

For `0<=j<=k`, the actual odd iterates are

\[
\begin{aligned}
U^j(n)&=3^j2^{2k-j}v-1,\\
U^j(5n)&=5\,3^j2^{2k-j-\lfloor j/2\rfloor}v+s_j,
\qquad
s_j=\begin{cases}-5,&j\text{ even},\\-7,&j\text{ odd}.
\end{cases}
\end{aligned}
\tag{16}
\]

The first ray has exactly one halving at each of these odd steps.
For the second ray, the signed odd template alternates `-5,-7`, with
halving gaps one and two. Its accumulated shortcut clock after `j`
odd steps is `j+floor(j/2)`. This is strictly less than `2k` for
`j<=k`. Thus the finite lift retains the parity at every intervening
shortcut step and at the odd endpoints. In particular the halving
gaps in (16) are exact, not merely lower bounds on divisibility.

All of `n,5n,q` are odd ternary units, and `q=4 mod 5`. The first
ray reaches `q` exactly at odd clock `j=k`. Every member of the second
ray in (16) is `0` or `3 mod 5` and never equals `q`. As before,
`E_5(f)=1/q`. With

\[
\mathsf A^U_Nf=\frac1N\sum_{j=0}^{N-1}f\circ U^j,
\]

the actual original source `n` gives

\[
\boxed{
\frac{E_5(f\circ U^k)}{E_5(f)}\ge\frac qn>
\left(\frac32\right)^k,
\qquad
\frac{E_5(\mathsf A^U_{k+1}f)}{E_5(f)}
\ge\frac{q}{(k+1)n}>
\frac{(3/2)^k}{k+1}.}
\tag{17}
\]

These energies are finite, although accelerated inverse fibers can be
infinite. Define the harmonic norm on odd ternary units by

\[
\|h\|_{\mathrm{harm}}=\sum_{x\in\mathcal O^*}\frac{|h(x)|}{x}.
\]

For each odd-unit target `q`, every legal inverse is
`x=(2^a q-1)/3` for an integer `a>=1`. Since `2^a q>=2`,

\[
\sum_{\substack{x\in\mathcal O^*\\Ux=q}}\frac1x
\le\sum_{a\ge1}\frac6{2^a q}=\frac6q.
\tag{18}
\]

The sum on the right deliberately allows illegal gaps as an upper
bound. Tonelli therefore gives
`||h o U||_harm <= 6 ||h||_harm`. Also
`E_5(h) <= 6 ||h||_harm`, by reindexing the `h(5n)` term.
Starting from `||f||_harm=1/q`, these inequalities prove finiteness
for every fixed iterate and finite accelerated average in (17).
Finite support is claimed for the input `f`, not its accelerated
pullbacks.

### 5.2 An elementary selection inside the known basin of one

For the full odd-map result (17), one may simply take `v=30`. For the
killed operator, one must ensure that `q` is nonperiodic. This cannot
be assumed for that fixed choice at every `k`. The following explicit
selection supplies a complete ordinary certificate for `q` and `n`.

For every `r>=1` there is a positive integer `b=1 mod 4` with

\[
3^r\mid 7\,2^b+1.
\tag{19}
\]

Here is a constructive lifting proof. Start with `b=1` at `r=1`.
The binomial identity, inductively cubed, gives

\[
16^{3^{r-1}}\equiv1+5\,3^r\pmod{3^{r+1}}.
\]

If `7*2^b+1=3^r c`, replace `b` by
`b+4j*3^(r-1)`, where `j in {0,1,2}` is chosen so `j=-c mod 3`.
The new quotient modulo three is `c-5j=c+j mod 3`, hence zero.
This lifts (19) by one power of three while preserving `b=1 mod 4`
and positivity. It proves the existence constructively without any
arithmetic-progression sufficiency theorem.

Apply (19) with `r=2k+2`, and set

\[
v=\frac{2(7\,2^b+1)}{3^{2k+1}}.
\tag{20}
\]

The quotient is integral and divisible by three. It is even, and
`b=1 mod 4` gives `7*2^b+1=0 mod 5`. Therefore `v` is a positive
multiple of 30, as required in (15)--(17).

For this choice, `q=2^k(3^k v)-1` has another `k` consecutive odd
gaps equal to one. Its resulting endpoint is

\[
U^k(q)=3^{2k}v-1
=\frac{7\,2^{b+1}-1}{3}=:p.
\tag{21}
\]

The next odd step has exact halving exponent `b+1` and reaches seven.
It is followed by the ordinary certified chain

\[
7\longmapsto11\longmapsto17\longmapsto13
\longmapsto5\longmapsto1,
\tag{22}
\]

whose halving gaps are `1,1,2,3,4`. Thus a complete gap word for `q`
is `k` copies of one followed by `b+1,1,1,2,3,4`. Prefixing another
`k` copies of one gives a complete word for `n`, since `U^k(n)=q`.
Both `n` and `q` exceed one and reach one, so neither is periodic.

### 5.3 The exact killed-domain consequence

Let `N` be all nonperiodic odd ternary units, and let `C` be the
operator which composes with `U` until a periodic vertex is reached,
then assigns zero. Extend its point functions by zero on the removed
periodic vertices when evaluating `E_5`.

For the nonperiodic `q` supplied above, all full `U`-pullbacks of
`f=1_q` agree with these zero-extended killed pullbacks. Indeed, a
trajectory which has reached a periodic state can never later hit
the nonperiodic target `q`. This applies whether or not `5n` is
nonperiodic. Therefore (17) also gives

\[
\boxed{
\frac{E_5(C^k f)}{E_5(f)}>
\left(\frac32\right)^k,
\qquad
\frac{E_5\!\left((k+1)^{-1}\sum_{j=0}^{k}C^j f\right)}{E_5(f)}
>\frac{(3/2)^k}{k+1}.}
\tag{23}
\]

All energies are finite by (18). This proves the absence of a uniform
five-energy operator bound on finitely supported inputs for the same
accelerated, killed operator used in the canonical Dirichlet theorem.
It still does not disprove a bound restricted to the particular
canonical Green potential or its additional structural identities.

The direct accelerated ray was supplied independently by the merger
and analytic agents during the final operator-scope review. The
explicit basin selector and complete source words were developed in
the certificate lane; the merger agent supplied the elementary
lifting induction above. All three lanes checked the resulting
killed-domain construction.

## 6. What an actual-edge Dirichlet estimate still has to supply

The joint analytic argument proves finite energy across actual
accelerated Collatz edges, and decreasing energy of forward averages
across those same edges. Those edges lie within an ordinary orbit
component. A translated five-edge can require a connection between
different such components.

A path estimate using actual orbit edges can compare its endpoint
values only after actual connecting paths have been constructed.
For example, a universal inequality comparing five-energy to the
actual-edge Dirichlet energy for every bounded function would already
force each five-edge to stay in one ordinary component: the indicator
of a component is constant across every ordinary edge. This is a
conditional implication, not an assertion that distinct nontrivial
Collatz components exist.

In the killed analytic domain, an invariant label is extended by zero
at the killing boundary; an escaping-component indicator still has
zero energy across all surviving and killed ordinary edges. A
nonzero five-defect for such a label cannot be bounded by that zero
energy. Thus the missing cross-component construction cannot be
silently supplied by the isometry or the inverse-superharmonic
identity.

Equations (2)--(23) identify concrete restrictions on a successful
network argument. It needs additional canonical-potential structure,
or unbounded/state-dependent routing with a justified global charging
estimate. Exact finite affine closure, bounded translated-five paths,
and a generic uniform five-energy operator bound do not provide it.

## Provenance and evidence level

The arguments above are new written deductions from the actual
shortcut map. Formula (8) is supported by the already compiled
`CollatzSignedCarry.finite_signed_lift` theorem in `SignedCarry.lean`, source
SHA256 `0729e2be27118d2f3c325b1f485a18c01da09b0e360d84b40effd851a2b0379f`
at published commit `75e4c3be98db839646ffbb76fc0ac33649747c99`.
The finite signed templates in (7) are displayed and are evaluated
directly by the definition. The energy/stencil conclusions in this
note have not themselves been ported into Lean. They make no global
Collatz claim and do not alter any frozen upstream source.
