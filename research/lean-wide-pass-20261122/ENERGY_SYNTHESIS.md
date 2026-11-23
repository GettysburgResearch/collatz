# Canonical density normalization and an estimate over every prefix clock

**Status: SOURCE-QUALIFIED written deductions; not a full Collatz proof.**
This pass combines the ordinary component-energy program with the canonical
inverse envelope constructed in PR180. It obtains two additional estimates:

1. The canonical obstacle envelope has an exact normalization as a ternary
   stationary density. Its ordinary values and its harmonicization are
   comparable by an absolute constant. In particular harmonicization does
   not introduce an uncontrolled loss at a moving ordinary target.
2. A weighted counting bound over **all** prefix clocks replaces a finite
   clock cutoff by an explicit geometric tail. This applies to the actual
   positive ordinary inverse tree, including at a least unit in a putative
   second component. Its remaining resolution term is displayed explicitly.

Neither result proves the ordinary upper estimate needed for closure. The
finite-five-energy implication is already available from earlier work; it
cannot be applied to the inverse envelope as if that envelope were an
invariant component label. Sections 6--8 identify the precise failed
inferences in this synthesis.

The main new estimates in this file are written proofs. No Lean verification
of the measure-theoretic statements or of the all-clock estimate is claimed.
The existing Lean potential-closing theorems retain their upper-bound
hypotheses.

## 1. Source comparison and normalization

Use the positive shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n,\end{cases}
\]

and the odd map
\(U(n)=(3n+1)/2^{v_2(3n+1)}\). Two positive integers belong to the same
ordinary component when their actual forward orbits meet, with possibly
different finite clocks.

The sources relevant to the attempted global combination are as follows.
The complete open-PR inventory and its refresh boundary are in
`SOURCE_SNAPSHOT.json`.

| Source | Exact inspected head | Input or obstruction retained |
|---|---|---|
| PR137 | `2911b53930cbd31f623d3e0586ca3613854f0143` | `component-rigidity/pass2/PROOF.md`: every fixed component has residue-locked inverse ladders and fixed finite patterns in high relative windows. The pattern length is fixed before the height; macroscopic blocks are not supplied. |
| PR140 | `1092737688b0bbc159820d7095722ad680f1fa1d` | `novel-swarm-20261030/pass5/FINITE_DEFECT.md`: exact automatic invariant labels are rigid, with a complete finite-defect classification. Automaticity of an arbitrary component is not proved. |
| PR142 | `b21f94f5772df5cfcaa5f5afd073d5889e75d294` | `REGULARITY_BRIDGE.md` and `CRITICAL_ENERGY.md`: ordinary approximation is required before using completion ergodicity; the stationary law is not square integrable. The latter argument is credited there to its external source. |
| PR154 | `fe40bb6f88e8094290ef01207d9bf7c4798d35d0` | `structural-reset-20261120/component/PROOF.md`: restricted five-merger laws imply component collapse by a complete integer descent; those physical merger laws remain hypotheses. |
| PR155 | `92f499b9d340d1ff8cc643c3eef3477d61b477c1` | `ORDINARY_DIRICHLET_COERCIVITY.md` and `ENDPOINT_BOUNDARY.md`: ordinary variation gives subcritical coercivity and a constant profile limit under finite harmonic tripling defect. |
| PR156 | `c5cb84502c7289705d59a8781a65fd845b9b6b14` | `ORDINARY_ESSENTIAL_SPECTRUM.md`: the operators of PR143/144 already have the whole unit circle in their essential approximate spectrum on certified convergent basins. Its correction product is a bounded coboundary on an escaping sector. |
| PR160 | `6d877e718f5ef9d57fe1830912c444359718747a` | `critical/CRITICAL_SINGULARITY.md`: critical normalization loses fixed ordinary atoms and can lose all normalized separating-boundary mass. |
| PR163 | `051237135a34ae7d4b973ee5fcf5da04ded6f0fc` | `FIVE_SLICE_ENERGY.md`: a complete finite affine certificate transports single-slice multiplicative-five energy to full tripling energy. Finiteness of the five energy is not an output. |
| PR168 | `e4599b32e4b1a955ac9315d46782d4ad6a5db96c` | `TERNARY_STATIONARY_BOUNDARY.md`: stationary uniqueness, the exact density recursion, the non-\(L^2\) obstruction, and the source-qualified rapid \(L^1\) approximation. |
| PR171 | `2bd243b3e05eaa5543adeb2894637b053c9662ca` | `CRITICAL_NEGATIVE_MOMENT_INTERFACE.md`: critical orbit sparsity strengthens the necessary negative-moment summability on an escaping orbit. It does not establish the required arithmetic moment bound; cycles are separate. |
| PR180 baseline for this pass | `d0349de2108abb7c8fb8393c086610e3372df116` | `lean-forward-band-20261121/JOINT_CLOCK_MIXING.md`, `GLOBAL_RENEWAL_ATTACK.md`, `MINIMAL_ENVELOPE_ATOM_REMOVAL.md`, and `ABEL_MARKED_UPPER_ATTACK.md`: the uniform density floor, a finite ordinary excessive majorant, canonical minimality, fixed-target basin sublinearity, and sublinear bounds at every fixed discount. |

PR156 explicitly pins the underlying PR143 and PR144 operator definitions
at `41a408e5e617fb4e65142485f6f3ff3e6ef6c408` and
`df756794e1d8de5cabff148ef433df505e3b68b4`. Their essential-spectrum
boundary is used through that reconstruction, not through a claim that a
new diagonal-moment estimate has been established here.

## 2. The ternary and ordinary operators are the same at positive integers

On \(\mathbb Z_3\), with Haar probability \(m\), put

\[
(Pf)(x)=\sum_{\substack{e\ge1\\2^e x\equiv1\ (3)}}
 \frac3{2^e}f\!\left(\frac{2^e x-1}{3}\right),
\qquad g(x)=\mathbf1_{3\nmid x}.
\tag{E1}
\]

The same formula defines the ordinary operator on positive integers.
For a positive integer target every legal parent in (E1) is a positive
odd integer. Thus finite iterations and the obstacle iterations below
restrict to exactly the previously constructed ordinary objects. No
ordinary value is assigned by choosing an arbitrary almost-everywhere
representative of a density.

Set \(D_0=1\), \(D_s=P^s1\). These are the finite Syracuse densities,
constant modulo \(3^s\). They are consistent conditional densities of the
stationary Syracuse probability. Write \(D\) for its Haar density. The
source-qualified fine-scale theorem and the uniform atom floor in the
PR180 packet give

\[
D_s=\mathbb E_m(D\mid x\bmod3^s),\qquad
\int D\,dm=1,\qquad PD=D\quad\text{almost everywhere},
\tag{E2}
\]

\[
D\ge c_*g\quad\text{almost everywhere}
\quad\text{for some absolute }c_*>0.
\tag{E3}
\]

Define the exact constants

\[
\mu=\operatorname*{ess\,inf}_{3\nmid x}D(x),
\qquad \kappa=\mu^{-1}.
\tag{E4}
\]

They are finite and positive. In particular \(c_*\le\mu\le1\),
because the conditional mean of \(D\) on \(1\bmod3\) is
\(D_1=1\). Hence \(\kappa\ge1\). The constant \(c_*\) here is a supplied lower bound;
\(\mu\) denotes the essential infimum itself.

For every nonnegative integrable \(f\), change variables separately on
each legal ternary coset to obtain

\[
\int Pf\,dm
=\sum_{e\ge1}2^{-e}\int f\,dm
=\int f\,dm.
\tag{E5}
\]

The stationary probability is unique. One direct justification is to
drive two initial ternary states by the same affine maps
\((3x+1)/2^e\). After \(s\) such maps their difference is divisible
by \(3^s\). Their laws therefore agree on every fixed finite quotient
after enough steps. Consequently a nonnegative integrable fixed density
of \(P\) is a scalar multiple of \(D\).

## 3. Exact normalization of the canonical obstacle envelope

Define on \(\mathbb Z_3\), allowing an infinite value at exceptional
points,

\[
V_0=g,\qquad V_{k+1}=\max(g,PV_k),\qquad
V=\sup_kV_k.
\tag{E6}
\]

Every \(V_k\) is finite and constant modulo \(3^{k+1}\). The ordinary
restriction of \(V\) is finite by the finite-majorant construction in
PR180. That source also proves that it is the least nonnegative
excessive majorant of \(g\) on positive ordinary integers.

### Theorem E1: the exact almost-everywhere scalar

\[
\boxed{V=\kappa D\quad\text{almost everywhere},
\qquad \int V\,dm=\kappa.}
\tag{E7}
\]

**Proof.** Since \(g\le\kappa D\) almost everywhere and
\(P(\kappa D)=\kappa D\) almost everywhere, induction gives
\(V_k\le\kappa D\) almost everywhere. Positivity of \(P\) respects
almost-everywhere inequalities: each inverse branch is nonsingular, and
there are only countably many branches. Monotone convergence gives
\(V\le\kappa D\) almost everywhere, so \(V\) is integrable.

The obstacle identity \(V=\max(g,PV)\) follows by monotone
convergence in the parent series. Thus \(PV\le V\). Equation (E5)
makes the nonnegative difference have integral zero, so \(PV=V\)
almost everywhere. Stationary uniqueness gives \(V=aD\) almost
everywhere for a finite \(a\). The obstacle \(V\ge g\) implies
\(a\ge1/\mu=\kappa\), whereas the comparison above gives
\(a\le\kappa\). This proves (E7). QED.

This identifies the normalization of the canonical construction; it does
not choose its values at positive integers by the almost-everywhere
identity.

### Theorem E2: a comparison at every finite ordinary argument

For every \(x\in\mathbb Z_3\), every \(k\ge0\), and every
\(s\ge k+1\),

\[
\boxed{V_k(x)\le\kappa D_s(x).}
\tag{E8}
\]

**Proof.** The function \(V_k\) is constant on the depth-\(s\)
cylinder containing \(x\). Average the almost-everywhere inequality
\(V_k\le\kappa D\) over that cylinder and use (E2). Both sides of
the resulting inequality are the displayed finite, canonically defined
values. Thus (E8) holds at every point, including an ordinary integer.
QED.

In particular,

\[
\boxed{V(q)\le\kappa\liminf_{s\to\infty}D_s(q)}
\tag{E9}
\]

at every positive ordinary \(q\). The order of limits in this argument
is fixed: first fix \(k\), then let \(s\) increase, and only then
take the supremum over \(k\).

### Theorem E3: harmonicization retains a fixed fraction of all values

Let \(G(q)=\lim_{j\to\infty}P^jV(q)\) on positive ordinary
integers, as in the earlier packet. Then

\[
\boxed{\frac{V(q)}{2\kappa}\le G(q)\le V(q)
       \quad(q>0).}
\tag{E10}
\]

**Proof.** Direct summation gives \(D_1=1\) on \(1\bmod3\),
\(D_1=2\) on \(2\bmod3\), and zero on multiples of three. Hence
\(D_1\le2g\le2V\), and positivity gives

\[
D_s=P^{s-1}D_1\le2P^{s-1}V\quad(s\ge1).
\]

Since \(P^{s-1}V\) decreases pointwise to the finite \(G\),

\[
\limsup_sD_s(q)\le2G(q).
\]

Combine this with (E9). The upper inequality in (E10) is the original
decreasing-limit construction. QED.

The conclusions also give

\[
\mu V(q)\le\liminf_sD_s(q)
\le\limsup_sD_s(q)\le2G(q)\le2V(q).
\tag{E11}
\]

They do **not** assert that \(D_s(q)\) converges at every positive
ordinary point. Nor does (E10) supply a sublinear bound on either
\(V(q)\) or \(G(q)\). It does show that passing from the canonical
obstacle solution to a harmonic solution loses at most an absolute
factor, uniformly even when \(q\) changes.

## 4. A full-clock counting estimate on the positive ordinary inverse tree

Here take a positive odd ternary unit \(q\) and an inverse depth
\(d\ge1\). A legal word \(w\) has total clock \(A(w)\),
coefficient \(\omega_w=3^d2^{-A(w)}\), and forward affine identity

\[
q=\omega_w n_w+\beta_w,
\qquad n_w\in\mathbb N_{>0}\text{ odd},\qquad \beta_w\ge0.
\tag{E12}
\]

Thus \(n_w\le q/\omega_w\). For each fixed total \(A\),
different legal words give different ordinary sources \(n_w\): the
actual odd trajectory of a fixed source determines its word. This remains
true on a possible cycle. Repeated sources at different total clocks are
not identified or discarded.

Let \(H\) be any real or complex function periodic modulo
\(M=3^t\), and write

\[
\|H\|_{1,M}=M^{-1}\sum_{r\bmod M}|H(r)|.
\tag{E13}
\]

The following proof also permits deleting any subset of the prefix words.
Let \(\Omega\ge0\) be an upper bound on the coefficients of the retained
words. For the full positive inverse family one may always take
\(\Omega=q\), by (E12). Denote the retained operator by
\(P^d_{\mathcal F}\).

### Theorem E4: no unspecified clock cutoff

For every integer \(L\ge d\),

\[
\boxed{
|P^d_{\mathcal F}H(q)|\le
\left[q(L-d+1)+2M\Omega+
      M9^d(2/3)^L\right]\|H\|_{1,M}.}
\tag{E14}
\]

In particular, with

\[
L=6d+\max\!\left(0,
 \left\lceil\frac{\log(M/q)}{\log(3/2)}\right\rceil\right),
\tag{E15}
\]

one obtains

\[
\boxed{
|P^d_{\mathcal F}H(q)|\le
\left[q(L-d+1)+2M\Omega+
q(64/81)^d\right]\|H\|_{1,M}.}
\tag{E16}
\]

In particular \(L\le6d+\lceil t\log3/\log(3/2)\rceil\),
so the full prefactor is \(O(q(d+t+1)+3^t\Omega)\), with an
absolute implied constant.

**Proof.** Fix a total \(A\) and put \(\omega_A=3^d2^{-A}\).
The distinct sources at that total lie in \((0,q/\omega_A]\).
Each residue modulo \(M\) occurs at most
\(q/(M\omega_A)+1\) times. Therefore

\[
\sum_{\substack{w\in\mathcal F\\A(w)=A}}
 \omega_A|H(n_w)|
\le(q+M\omega_A)\|H\|_{1,M}.
\tag{E17}
\]

There are at most \(L-d+1\) totals from \(d\) through \(L\).
The nonempty retained totals have coefficients at most \(\Omega\),
and the coefficients halve each time the total increases by one. Thus
their sum is at most \(2\Omega\). Summing (E17) gives the first
two terms of (E14).

For the remaining totals use \(\|H\|_\infty\le M\|H\|_{1,M}\).
Over **all** words of length \(d\), the sum of their coefficients
with total greater than \(L\) is

\[
3^d\Pr(A_d>L),
\]

where \(A_d\) is the sum of \(d\) independent geometric letters
with probabilities \(2^{-a}\). The exact generating-function value

\[
\mathbb E(3/2)^{A_d}=3^d
\]

and Markov's inequality give
\(3^d\Pr(A_d>L)\le9^d(2/3)^L\). Deleting words only reduces
this nonnegative bound. This proves (E14).

The extra term in (E15) ensures
\(M(2/3)^{L-6d}\le q\). Since
\(9(2/3)^6=64/81\), the last term in (E14) is at most
\(q(64/81)^d\), proving (E16). QED.

The earlier weighted-counting statement retained a finite number of
totals as an explicit factor. Formula (E14) supplies the omitted full
clock tail for a finite-resolution input. It does not pretend that the
resolution of that input can be removed at no cost.

## 5. The least-component specialization and its remaining tail

Let \(q\) be the least **odd ternary unit** in one ordinary component.
If the input \(H\) vanishes on multiples of three, every contributing
source in (E12) is an odd unit in that same component. It is therefore
at least \(q\), and (E12) gives \(\omega_w\le1\). Formula (E16)
then becomes

\[
|P^dH(q)|\ll
\bigl(q(d+t+1)+3^t\bigr)\|H\|_{1,3^t}.
\tag{E18}
\]

This is a valid specialization for the density differences
\(H=D_t-D_m\), when \(t\ge m\ge1\). Both terms vanish on
multiples of three. A component's least ordinary integer itself need
not have been proved prime to three; using its least odd unit avoids
that domain mistake.

For such a difference the exact operator identity and the supplied
fine-scale estimate yield

\[
D_{d+t}(q)-P^dD_m(q)=P^d(D_t-D_m)(q),
\]

\[
\boxed{
|D_{d+t}(q)-P^dD_m(q)|
\ll_A\bigl(q(d+t+1)+3^t\bigr)m^{-A}.}
\tag{E19}
\]

Along moving parameters \(q,m,t,d\), if \(3^t\le Cq\) and
\(d+t=O(m^B)\) for fixed constants \(C,B\), choosing \(A>B\)
makes the right side \(o(q)\) as \(m\) increases. The arbitrary
fixed inverse-power saving can beat that polynomial. This is not a
limit with \(q\) fixed: then \(3^t\le Cq\) also bounds \(t\)
and \(m\le t\).
However it is not a uniform estimate in an unbounded final depth.
Holding \(m\) fixed and increasing \(t\) makes the displayed
\(3^t\) term grow. Holding \(t\) fixed and increasing \(d\)
leaves the growing number of effective clocks. These are displayed
terms, not errors that can be silently omitted before a critical limit.

The same obstruction appears if one first dominates a large-clock
suffix value by the known ordinary linear majorant: its source has
size on the order of \(2^{A}q/3^d\), which cancels the prefix
coefficient \(3^d2^{-A}\). Fixed-root basin sublinearity says the
resulting individual terms tend to zero. It supplies no uniform
summable rate in the prefix clock.

Thus the new all-clock estimate eliminates an unspecified cutoff but
does not establish the critical uniform integrability needed to bound
\(V(q)/q\) at a moving least source.

## 6. Component covariance survives every canonical operation

An ordinary invariant label \(\ell\) satisfies
\(\ell(Tn)=\ell(n)\). Every parent in (E1) is in the same ordinary
component as its target: if \(3n+1=2^eq\), its physical shortcut
orbit reaches \(q\) after exactly \(e\) steps. Consequently,
whenever the nonnegative sums are defined,

\[
\boxed{P(\ell F)(q)=\ell(q)PF(q)}
\tag{E20}
\]

for every nonnegative component label \(\ell\).

There is also an exact obstacle version. Start at \(W_0=\ell g\)
and iterate \(W_{k+1}=\max(\ell g,PW_k)\). Equation (E20) and
\(\max(\ell a,\ell b)=\ell\max(a,b)\) give

\[
W_k=\ell V_k,
\qquad W=\ell V.
\tag{E21}
\]

Discounted resolvents and harmonicization have the same covariance.
Thus choosing the least majorant removes arbitrary scaling **after
the obstacle is fixed**, but the operator and the construction still
act separately on ordinary components. They do not compare a component
with the component containing its products by five.

A concrete normalization consequence is

\[
\inf_{\substack{n\in\mathcal C\\3\nmid n}}V(n)=1
\tag{E22}
\]

for every ordinary component \(\mathcal C\). Indeed, if the infimum
were greater than one, divide \(V\) on that entire component by a
fixed constant strictly between one and the infimum. Leave the other
components unchanged. Covariance preserves excessivity, and the new
function still majorizes \(g\), contradicting leastness. Equation
(E22) involves all positive unit arguments; it does not assert that
the infimum occurs on a specified forward orbit or in a bounded region.

This explains why an argument based only on rescaling a whole component
does not force its disappearance. The obstacle has already fixed its
scale by (E22).

## 7. Where the five-energy program meets this construction

For an actual invariant metric label \(f\), the relevant energy is

\[
E_5(s;f)=\sum_{\substack{x>0\\x\ {
\rm odd},\ 3\nmid x}}x^{-s}d(f(5x),f(x)).
\tag{E23}
\]

PR163 proves, with the full comparison domains retained,

\[
\sum_{n>0}n^{-s}d(f(3n),f(n))
\le\frac{248(7153/21)^s}{(1-2^{-s})^2}E_5(s;f),
\tag{E24}
\]

and an upper constant of \(10000\) at \(s=1\). PR155's endpoint
profile theorem, together with the predecessor-density input now
derived in the PR180 packet, makes finite \(E_5(1;f)\) force
pointwise constancy. The metric-label reduction is retained from
PR160/163. No further finite-residue cover is needed at this stage.

The function \(V\), the harmonic function \(G\), and their
normalizations \(V(n)/n\), \(G(n)/n\) are not invariant component
labels. The exact transfer law is a weighted **sum over parents**,
not equality along each physical edge. Substituting one of these
functions for \(f\) in (E24) would therefore discard a hypothesis
of the comparison theorem.

On a hypothetical injective component, a corrected flow can instead
produce a component-invariant total capacity, as described in the root
synthesis. Its value is a limit along the forward direction. The
capacity at a node is bounded **above** by that total component
capacity. The reverse domination needed to control its five defect by
the local potential is not supplied. Incoming mass from branches that
join later cannot be charged to the earlier node without a new
estimate.

Finally, (E7) is not a regularity proof for an ordinary component
indicator. Such an indicator is specified on a countable, Haar-null
set. Formula (E20) explains exactly why its values are still visible
to the ordinary operator, despite being invisible in an
almost-everywhere stationary-density statement.

## 8. The critical limit and the first unsupported global inference

The preceding pass proves, for every fixed \(1/3<\rho<1\), a
global sublinear bound on

\[
F_\rho(q)=(1-\rho)\sum_{s\ge0}\rho^sD_s(q),
\qquad
F_\rho(q)\ll_\rho
q^{1+\log\rho/\log3}(1+\log q).
\tag{E25}
\]

The exact identity is

\[
F_\rho=(1-\rho)+\rho PF_\rho.
\tag{E26}
\]

The constants and exponents in (E25) are not uniform at \(\rho=1\),
and (E26) is not excessivity. The earlier note derives the explicit
negative term \(-(1-\rho)F_\rho(n)/n\) in the normalized
forward drift. A value-dependent discount cannot be substituted in
the excessive-potential Lean theorem without controlling that loss
and the change of parameter across an edge.

The new normalization (E7)--(E11) shows that harmonicization itself
does not cause a moving-root loss. The full-clock bound (E14)--(E19)
shows where the unresolved uniformity remains. Neither gives

\[
V(q)=o(q)
\]

uniformly on the marked section, or even uniformly over least odd
units of hypothetical distinct components. The source-qualified
non-\(L^2\) result also rules out inserting a uniform quadratic
density estimate at this point. Rapid \(L^1\) approximation and
divergent quadratic energy coexist in the stationary law.

The first unsupported global inference is therefore a bound on the
**actual ordinary critical tail** at such a moving target, or a
separate bound making the invariant label's five energy finite.
Component covariance, almost-everywhere uniqueness, fixed-root
nonatomicity, and fixed-discount sublinearity do not supply either
bound. Both divergent components and nontrivial positive cycles
remain unexcluded by this synthesis.
