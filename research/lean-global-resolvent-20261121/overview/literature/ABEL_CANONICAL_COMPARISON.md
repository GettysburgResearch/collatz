# The least envelope makes critical Abel limits harmonic

**Status:** written integration lemma, not Lean formalized. Its analytic
inputs are the finite positive excessive envelope and the uniform atom
floor in PR180 at `d0349de2108abb7c8fb8393c086610e3372df116`.
The canonical least envelope, its harmonicization, inverse-ray atom
removal, and fixed-basin decay are credited to that head's
`MINIMAL_ENVELOPE_ATOM_REMOVAL.md`. This note combines those results with
the actual Abel family; it does not claim a new proof of those inputs.
The new conclusion discharges the parent-tail uniform-integrability
obligation left explicit in `GLOBAL_RENEWAL_ATTACK.md`, Section 8.2.
The moving-target height bound remains open.

## 1. Definitions and exact imported hypotheses

Work on all positive integers. Let

\[
(Pf)(q)=\sum_{\substack{e\ge1\\2^e q\equiv1\ (3)}}
 \frac3{2^e}f\!\left(\frac{2^e q-1}{3}\right),\qquad
g(q)=\mathbf1_{3\nmid q},\qquad D_k=P^k1.
\]

Every parent in this sum is a positive odd integer. Let

\[
H_r(q)=(1-r)\sum_{k\ge0}r^kD_k(q),\qquad0<r<1.
\]

The frozen PR180 inputs give a finite nonnegative excessive majorant
\(B\ge g\). Its least excessive majorant is

\[
V_0=g,\quad V_{j+1}=\max(g,PV_j),\quad
V=\lim_jV_j\le B,
\]

so \(V\ge g\), \(PV\le V\), and any nonnegative excessive
\(W\ge g\) satisfies \(V\le W\). Its harmonicization is

\[
G=\lim_{j\to\infty}P^jV,\qquad PG=G,\qquad 0\le G\le V.
\]

The uniform atom floor is the all-positive statement: there are
\(\alpha>0\) and \(k_0\) with
\(D_k(q)\ge\alpha g(q)\) for every positive integer \(q\) and
\(k\ge k_0\). This is exactly the floor used in the frozen
`GLOBAL_RENEWAL_ATTACK.md`, Section 8.2; no extension of an odd-only floor
is silently presumed here. Its proof remains a source-qualified analytic
dependency, not a Lean axiom or a theorem proved in this note.

## 2. One majorant for every depth and every Abel parameter

Summing the geometric parent weights gives

\[
D_1(q)=
\begin{cases}
1,&q\equiv1\pmod3,\\
2,&q\equiv2\pmod3,\\
0,&3\mid q.
\end{cases}
\]

Consequently \(D_1\le2g\le2V\). Positivity of \(P\) yields,
for every \(k\ge1\),

\[
\boxed{D_k\le2P^{k-1}V\le2V.}\tag{1}
\]

In particular, for every \(q>0\) and \(0<r<1\),

\[
\boxed{0\le H_r(q)\le(1-r)+2rV(q)\le1+2V(q).}\tag{2}
\]

At multiples of three, \(D_k(q)=0\) for \(k\ge1\), so
\(H_r(q)=1-r\) exactly. The constant function in (2) is needed to
include these arguments.

For a fixed target \(q\), the majorant of the weighted parent series is
summable:

\[
P(1+2V)(q)=D_1(q)+2PV(q)<\infty.\tag{3}
\]

More explicitly, the tails over \(e>E\) of this nonnegative series
tend to zero as \(E\to\infty\), and bound the corresponding parent
tails of \(PH_r(q)\) simultaneously for every \(r\in(0,1)\).
This is the required uniform integrability of the actual Abel family.

For this conclusion alone, leastness is unnecessary: any one finite
nonnegative excessive majorant `B>=g` gives `D_k<=2B`, `H_r<=1+2B`, and
`P(1+2B)<infinity`. The canonical choice matters for the comparisons and
inherited decay below.

## 3. Every common Abel subsequential limit is harmonic

Countability of the positive integers and (2) give a common pointwise
convergent subsequence along every sequence \(r_j\uparrow1\). Write a
common limit as \(h(q)=\lim_jH_{r_j}(q)\).

Dominated convergence using (3) gives
\(PH_{r_j}(q)\to Ph(q)\) for each fixed \(q\). The exact equation

\[
H_r=(1-r)1+rPH_r
\]

therefore passes to the limit with equality:

\[
\boxed{Ph=h.}\tag{4}
\]

The uniform atom floor gives \(H_r\ge\alpha r^{k_0}g\), hence
\(h\ge\alpha g\). At multiples of three, \(h=0\).
No uniqueness of \(h\), convergence of the entire Abel family, or
pointwise convergence of \(D_k\) has been established.

## 4. Comparison with the canonical envelope and harmonic part

Since \(P^{k-1}V\downarrow G\), (1) implies

\[
\limsup_{k\to\infty}D_k(q)\le2G(q).
\]

The elementary Abel limsup inequality for a bounded sequence then gives
\(\limsup_{r\uparrow1}H_r(q)\le2G(q)\). This inequality can also
be obtained by splitting the sum at a fixed depth and using
\(D_k(q)\le2G(q)+\varepsilon\) on its tail.

For the other direction, \(h/\alpha\) is a nonnegative excessive
majorant of \(g\), so leastness of \(V\) gives
\(\alpha V\le h\). To bound the scalar liminf of the full Abel
family at one fixed \(q\), choose a sequence attaining that liminf
and extract a further common pointwise subsequence. Applying the last
inequality to its limit proves

\[
\boxed{
\alpha V(q)\le\liminf_{r\uparrow1}H_r(q)
\le\limsup_{r\uparrow1}H_r(q)
\le2G(q)\le2V(q).}\tag{5}
\]

In particular every common critical Abel limit satisfies
\(\alpha V\le h\le2G\le2V\). The lower comparison also holds
at nonunits, where all terms in (5) are zero.

It follows that a sublinear height estimate on all units, or only on the
marked units, is equivalent up to absolute constants for \(V\),
\(G\), any one common critical Abel limit, and the pointwise critical
Abel limsup. This is an equivalence of remaining height estimates; it
does not prove any of them.

### 4.1 The ordinary depth limits satisfy the same comparison

Put `d_*(q)=liminf_k D_k(q)`. It is finite and nonnegative by (1), and the
uniform atom floor gives `d_*>=alpha g`. Fatou's lemma for the nonnegative
parent series yields

\[
P d_*\le\liminf_{k\to\infty}P D_k
=\liminf_{k\to\infty}D_{k+1}=d_*.
\]

Thus `d_*/alpha` is another excessive majorant of `g`. Leastness of `V`
and (1) prove

\[
\boxed{
\alpha V\le\liminf_{k\to\infty}D_k
\le\limsup_{k\to\infty}D_k\le2G\le2V.
}\tag{6}
\]

A finite-depth spike also persists: for `j>=1` and `n>=j-1+k_0`,

\[
D_n=P^{j-1}D_{n-j+1}\ge\alpha P^{j-1}g
\ge\frac\alpha2D_j.
\tag{7}
\]

Equivalently, `F(q)=sup_{k>=1} D_k(q)` satisfies
`alpha V<=F<=2V`. Hence the marked-height problem can be posed as a uniform
bound over every finite word depth, without an Abel parameter. These
comparisons do not establish convergence in depth or a uniform height
bound; they show that one cannot dismiss a deep spike as a transient
finite-level artifact.

## 5. What now transfers, and what still does not

PR180 proves that \(V\) has no simple inverse-ray atoms and that
\(V(n)/n\to0\) uniformly as \(n\to\infty\) through the positive
odd unit predecessors of each one fixed positive ordinary target. By (5), both
properties hold for every common critical Abel limit. Generic atomic
harmonic additions are therefore excluded from this Abel construction.

In fact (1)--(2) give a stronger fixed-basin conclusion. As `n` grows
through the positive odd unit predecessors of any one fixed ordinary
target,

\[
\sup_{k\ge1}\frac{D_k(n)}n\longrightarrow0,
\qquad
\sup_{0<r<1}\frac{H_r(n)}n\longrightarrow0.
\]

The upper bounds are respectively `2V(n)/n` and `(1+2V(n))/n`.
The cutoff can still depend on the fixed root; this does not make it
uniform across all marked integers.

The actual-operator Green estimate in `ANCHORED_INVERSE_GREEN.md` can use
such a harmonic \(h\), or \(G\), in place of an arbitrary excessive
profile. Its anchored identity then has no profile defect
\(\epsilon=h-Ph\). The finite floor-boundary term and the terminal
transport term remain.

In particular, for a fixed positive odd unit source \(x\) whose forward
orbit survives above a fixed floor \(m\), its contribution at the moving endpoint
\(U^k(x)\) to \(L_m^k(h/\mathrm{id}^s)\) is still exactly
\(h(x)/x^s>0\). A pointwise bound for every target row cannot remove
that contribution from infinitely many different rows. Fixed-basin
sublinearity controls ancestors of a chosen root; future distinct states
of an escaping orbit are not all ancestors of one such root.

Thus harmonicity and uniform parent tails are now discharged. A uniform
height bound over moving marked targets, or a genuinely summed anchored
Green estimate retaining the initial source, is still required. There is
no proof here that the atom-removal result and the row Green bound imply
either statement.

## 6. Priority and integration boundaries

At the same frozen PR180 head:

- `ABEL_MARKED_UPPER_ATTACK.md` already proves a quantitative globally
  sublinear bound for every fixed subcritical Abel parameter, including
  periodic targets. It is stronger in scope than the nonperiodic-only
  calculation in our earlier trace-height note.
- `InverseDensityPotential.lean` already proves
  `two_short_unit_parents`, `additive_transfer_of_pair_floor`, and the
  all-unit finite-floor criterion. The explicit cycle ratio computation
  in our earlier note is a specialization of that existing transfer
  mechanism, not a new global reduction.
- `MarkedDensityPotential.lean` already proves
  `finite_marked_absorbing_floor` and
  `universal_of_marked_inverse_envelope_and_base`. These require upper
  decay only at the marked states, a weaker hypothesis than decay at
  every unit.
- `MINIMAL_ENVELOPE_ATOM_REMOVAL.md` supplies \(V\), \(G\),
  atom removal, and full fixed-basin sublinearity. None is attributed to
  the present integration lemma.

The result specific to this note is (1)--(5): the canonical finite
excessive majorant controls every exact finite-depth density, supplies
uniform domination of the actual Abel parent sums, upgrades all common
Abel limits to harmonic functions, and compares them with the canonical
envelope. The source-qualified provenance of the envelope and atom floor
is unchanged.
