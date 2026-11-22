# The actual boundary under symmetrization

Date: 2026-11-22.

**Outcome: this attack does not eliminate an escaping component or prove
that the canonical boundary coefficient is zero.** It applies the
Dirichlet and Martin-boundary ideas to the exact ordinary operators.
The positive deduction is that their symmetric part is recurrent on
every hypothetical escaping component. The attempted recurrence transfer
then fails for a concrete reason: the required sector bound is false
already on the known basin of five. A separate calculation for the
unchanged canonical source shows exactly which term survives the
attempted symmetric Poisson estimate.

These are written deductions from the source-qualified ordinary harmonic
construction. They are not new Lean assumptions or a formal proof of the
infinite analytic statements. No pointwise convergence of the ordinary
ternary densities is used.

## 1. Sources and operator map

The starting point is the published central packet at
a9f471543d7fed0a76f348e6d97a9d6d44fa369e, especially
[CRITICAL_BOUNDARY.md](../central-step-20261122/CRITICAL_BOUNDARY.md).
Its frozen inputs are retained:

| Source | Pin and exact use |
|---|---|
| PR175 | 728389c2ad4796853948250a90188b0697483d92, LITERATURE_DIRICHLET_BOUNDARY.md: bounded canonical Green potential, finite gradient energy, and the exact escape coefficient. |
| PR183 | 68345f60a4f757acb42a69a4ac95910f8ce26163, research/profound-step-20261122/operator/WOLD_CHANNELS.md: synchronous levels have their component's total capacity. |
| PR185 | 53f01ca5b443ef57ef2160b4996dbb2cc87f7395, ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md: the stationary ordinary reference, comparison with the critical harmonic function, and finite original charge. |
| New PR175 | f63204765438c83def68154e7f253ee9b660979c, research/lean-global-closure-20261121/central/DIRECT_CANONICAL_CHARGE_ATTEMPT.md and ACTUAL_CAPACITY_CLOSURE_ATTEMPT.md: the actual terminal charge and its compensating capacity increments remain present. |
| New PR185 | 4b0c2c27812db555061f5d9006de82a87e7e364f, research/central-obstruction-20261122/ESCAPE_ATTEMPTS.md: a fixed-root inverse law cannot be made uniform over forward-moving roots, and local mean regularity does not supply the required global regularity. |
| PR186 | 1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493, literature/deep-machinery-20261122/: broad survey inspected; the present calculation tests actual sector and capacity hypotheses rather than adding another list of machinery. |

Let \(\mathcal N\) be the positive odd ternary units which are not
themselves periodic under
\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]
Forward motion is killed on entering a periodic vertex. Preperiodic
vertices stay in the domain until that time.

Write
\[
\begin{gathered}
(La)(q)=\sum_{Un=q}a(n),\qquad L\nu=\nu,\\
h(n)=G(n)/n,\qquad
\lambda(n)=\frac{3n}{3n+1},\qquad
d(n)=(1-\lambda(n))h(n),\\
0<\delta\nu\le h\le\nu\le A,\qquad
D=\sum_n d(n)<\infty,\qquad \delta=e^{-200/3}.
\end{gathered}
\tag{1}
\]
The predecessor-population and canonical-envelope qualifications
underlying these inputs are unchanged.

On the real Hilbert space \(\mathcal H=\ell^2(\mathcal N,\nu)\), set
\[
Cf(n)=
\begin{cases}
f(Un),&Un\in\mathcal N,\\
0,&Un\notin\mathcal N,
\end{cases}
\qquad
Kf(q)=\sum_{Un=q}\frac{\nu(n)}{\nu(q)}f(n).
\tag{2}
\]
Then \(C\) is an isometry, \(K=C^*\), and \(KC=I\). Define the
symmetric kernel and its energy by
\[
S=\frac{C+K}{2},\qquad
\mathcal E(f)=\langle f,(I-S)f\rangle_\nu
=\frac12\|(I-C)f\|_\nu^2.
\tag{3}
\]
The factor \(1/2\) matters: the earlier packet's energy
\(\mathcal D(f)\) equals \(2\mathcal E(f)\).
All of these operators are bounded on \(\mathcal H\).

On an escaping component there is no killing, \(S\) is an irreducible
reversible Markov kernel, and \(\nu\) is stationary for both \(C\) and
\(K\). On killed components \(S\) is substochastic. The inverse kernel
\(K\) has rows summing to one, but is not irreducible: it moves strictly
down the component clock.

The direct map into the continuous-time notation of the primary
Dirichlet paper is
\[
\mathscr L=K-I,\qquad
\mathscr L^*=C-I,\qquad
\mathscr S=S-I,\qquad
\mu=\nu.
\tag{4}
\]
It is the bounded, rate-one Poissonization. The paper's irreducibility
assumption is not asserted for \(\mathscr L\).

## 2. The primary theorems actually tested

**Gaudillière--Landim, arXiv:1111.2445v1.** Section 2 assumes an
irreducible continuous-time chain on a countable space with a stationary
measure. Theorem 2.4 treats disjoint \(A,B\) with \(B^c\) finite.
Lemma 2.6 gives \(\operatorname{cap}\le C_0\operatorname{cap}_s\) under
\[
|\langle\mathscr L f,g\rangle_\mu|^2
\le C_0\langle-\mathscr Lf,f\rangle_\mu
           \langle-\mathscr Lg,g\rangle_\mu.
\tag{5}
\]
Lemma 5.2 transfers symmetric recurrence under that condition.
Lemma 5.3 instead assumes
\(\sum c_a(x,y)^2/c_s(x,y)<\infty\).
[Primary paper](https://arxiv.org/pdf/1111.2445v1).

**Gouëzel, Annals of Probability 43 (2015), Theorems 1.2--1.3.**
These concern admissible measures on nonelementary hyperbolic groups,
with superexponential tails. Theorem 1.2 assumes Anc*:
some \(r>1\) makes \(r\mu\)'s Green function finite. Theorem 1.3
assumes finite Green function and additionally symmetry, a finitely
generated free group, or a cocompact lattice of \(\mathrm{PSL}(2,\mathbb R)\).
The conclusions are Ancona inequalities and identification of the
Martin boundary with the geometric boundary.
[Author's primary PDF](https://gouezel.pages.math.cnrs.fr/webpage/articles/infinite_ancona.pdf).

Neither theorem is imported with its hypotheses omitted.

## 3. Symmetric recurrence on an actual escaping component

Fix a hypothetical escaping component \(\mathcal C\). Choose its
integer clock \(\ell\), with
\[
\ell(Un)=\ell(n)+1.
\]
For a reference vertex \(x\), set \(\ell(x)=0\). The exact synchronous
mass theorem gives
\[
\sum_{\substack{n\in\mathcal C\\\ell(n)=r}}\nu(n)
=C_{\mathcal C}
:=\lim_{k\to\infty}\nu(U^kx)>0
\quad(r\in\mathbb Z).
\tag{6}
\]

For integers \(N\ge1\), define
\[
\phi_N(n)=\left(1-\frac{|\ell(n)|}{N}\right)_+
\quad(n\in\mathcal C).
\tag{7}
\]
Its support has finitely many clock levels, each of finite mass. Thus
\(\phi_N\in\mathcal H\), despite generally having infinite ordinary
support. There are exactly \(2N\) clock differences of size \(1/N\).
Equations (3) and (6) give
\[
\boxed{\mathcal E(\phi_N)=\frac{C_{\mathcal C}}{N}.}
\tag{8}
\]
Also \(0\le\phi_N\le1\), \(\phi_N(x)=1\), and
\(\phi_N(n)\to1\) for each \(n\in\mathcal C\).

To use finite-support capacity, enumerate the component and truncate
\(\phi_N\) to finite sets containing \(x\). These truncations converge
in \(\mathcal H\). Because \(I-S\) is bounded, their energies converge
to (8), while their value at \(x\) remains one. The reversible
Dirichlet principle therefore gives
\[
\operatorname{cap}_S(x,\infty)\le C_{\mathcal C}/N
\quad\text{for every }N,
\qquad
\operatorname{cap}_S(x,\infty)=0.
\tag{9}
\]
Consequently **\(S\) is recurrent on every escaping component**.

There is no local-finiteness assumption hidden here. Odd Collatz roots
have infinitely many inverse parents; the finite ordinary truncation
argument handles that fact. All vertex conductances are finite because
\(S\) is a Markov kernel and \(\nu(n)<\infty\).

This is a property of the actual graph and actual reference. It is not
recurrence of the directed inverse law, nor an escape-exclusion result.

## 4. The sector bound fails on the known basin of five

This obstruction does not assume an escaping orbit.
The actual odd orbit is \(5\mapsto1\), with \(1\) removed from the
domain. Let
\[
\mathcal B_5=\{n\in\mathcal N:U^jn=5\text{ for some }j\ge0\},
\qquad E_j=\{n\in\mathcal N:U^jn=5\}.
\]
The levels \(E_j\) are disjoint, and
\[
\sum_{n\in E_j}\nu(n)=\nu(5)
\quad(j\ge0)
\tag{10}
\]
by \(L^j\nu=\nu\). Functions constant on these levels and zero outside
\(\mathcal B_5\) form a reducing subspace. Identify them with sequences
on \(\mathbb N\), with weight \(\nu(5)\). Then
\[
Cf(j)=
\begin{cases}f(j-1),&j\ge1,\\0,&j=0,\end{cases}
\qquad Kf(j)=f(j+1).
\tag{11}
\]

For \(N\ge2\), take two overlapping hats:
\[
f_N(j)=
\begin{cases}
j/N,&0\le j\le N,\\
(2N-j)/N,&N\le j\le2N,\\
0,&\text{otherwise},
\end{cases}
\qquad
z_N(j)=f_N(j-N),
\tag{12}
\]
where the hat is extended by zero at negative indices.
Direct summation gives
\[
\mathcal E(f_N)=\mathcal E(z_N)=\frac{\nu(5)}N,
\qquad
\langle(I-K)f_N,z_N\rangle_\nu
=\frac{\nu(5)(N-1)}{2N}.
\tag{13}
\]
For the pairing, the only nonzero terms have \(N\le j<2N\);
they are \(\nu(5)(j-N)/N^2\).

Thus (5) would require
\[
\boxed{C_0\ge\frac{(N-1)^2}{4}\quad\text{for every }N.}
\tag{14}
\]
There is **no finite strong sector constant** for the actual
\(K-I\) on \(\ell^2(\mathcal N,\nu)\).

Although these hats have infinite ordinary support, they lie in the
full domain of the bounded generator. If (5) were required only on
finitely supported functions, Hilbert-space density and boundedness
would extend it to these hats and give the same contradiction.

Adding an \(L^2\) term changes the statement: the elementary estimate
\(|\langle(I-K)f,z\rangle|\le2\|f\|\|z\|\) is valid. It is not the
unshifted energy estimate used in Lemma 2.6, and cannot transfer (9).
Calling this shifted estimate a sector bound without the shift would
erase precisely the low-frequency obstruction in (14).

The alternative hypothesis in Lemma 5.3 also fails on an escaping
component. For each actual directed edge \(n\to Un\), its conductances
for (4) satisfy, up to orientation,
\[
|c_a|=c_s=\nu(n)/2.
\]
Each clock cut has total \(\nu\)-mass \(C_{\mathcal C}\), so
\(\sum c_a^2/c_s\) diverges over the infinitely many cuts.

## 5. Direct attempt with the original canonical source

Perhaps the full sector inequality is unnecessarily strong: the source
is not arbitrary. Keep its exact arithmetic definition:
\[
t(n)=\frac{h(n)}{\nu(n)}\in[\delta,1],
\qquad
g(n)=\frac{d(n)}{\nu(n)}
=\frac{t(n)}{3n+1}.
\tag{15}
\]
The already stated inequalities give
\[
d(n)\ge\frac{\delta\nu(n)}{3n+1}
\ge\frac{\delta\nu(n)}{4n},
\qquad
\sum_n\frac{\nu(n)}n\le\frac{4D}{\delta}<\infty.
\]
Thus this actual \(g\) belongs to
both \(L^1(\nu)\) and \(\mathcal H\); the simpler test \(1/n\)
also belongs to both spaces and has finite symmetric energy. The
failure below is not lack of source integrability.

The complete directed potential is
\[
R=\sum_{j\ge0}K^jg=1-\lambda t,\qquad
0\le R\le1,\qquad (I-K)R=g,
\qquad \mathcal E(R)<\infty.
\tag{16}
\]
The last energy is understood through the square-integrable gradient;
membership of \(R\) itself in \(\mathcal H\) is not assumed.

### 5.1 The actual canonical source fails the dual energy test under escape

Restrict to the component \(\mathcal C\) of Section 3, and write
\[
D_{\mathcal C}=\sum_{n\in\mathcal C}d(n)>0.
\]
The same clock hats satisfy
\[
\langle g,\phi_N\rangle_\nu
=\sum_{n\in\mathcal C}d(n)\phi_N(n)
\longrightarrow D_{\mathcal C}.
\tag{17}
\]
In combination with (8), for all sufficiently large \(N\),
\[
\boxed{
\frac{|\langle g,\phi_N\rangle_\nu|^2}
     {\mathcal E(\phi_N)}
\ge \frac{N D_{\mathcal C}^{\,2}}{4C_{\mathcal C}}.}
\tag{18}
\]
Therefore this unchanged canonical \(g\) has infinite homogeneous
symmetric \(H^{-1}\) norm if an escaping component exists. A finite-energy
weak solution to \((I-S)\psi=g\) on that component would give a uniform
upper bound in (18) by the energy Cauchy--Schwarz inequality, and is
therefore impossible in that case.

This calculation does not prove that such a component exists. It shows
that finite directed potential and reciprocal-height integrability
cannot be substituted for the missing symmetric dual-energy estimate.

### 5.2 Exact allocation of the canonical charge

There is a more explicit calculation of the attempted Poisson solution.
Set
\[
a_r=\frac1{C_{\mathcal C}}
       \sum_{\substack{n\in\mathcal C\\\ell(n)=r}}d(n),
\qquad
\sum_{r\in\mathbb Z}a_r
=\frac{D_{\mathcal C}}{C_{\mathcal C}}=:F_{\mathcal C}>0.
\tag{19}
\]
For any bounded \(f\), let its level mean be
\[
\bar f_r=\frac1{C_{\mathcal C}}
      \sum_{\ell(n)=r}\nu(n)f(n).
\]
Then \(\overline{Cf}_r=\bar f_{r+1}\) and
\(\overline{Kf}_r=\bar f_{r-1}\), by \(L\nu=\nu\).

The unchanged-source identity
\(\nu(q)R(q)=\sum_{n\in\operatorname{Pred}(q)}d(n)\)
gives, with no limit interchange beyond Tonelli,
\[
\boxed{\bar R_r=\sum_{j\le r}a_j.}
\tag{20}
\]
Indeed, every source of clock \(j\le r\) has exactly one forward
image of clock \(r\), and a source of larger clock has none.

Consequently the exact decomposition
\[
g=(I-S)R+\frac{C-K}{2}R
\]
has level means
\[
\boxed{
\overline{(I-S)R}_r=\frac{a_r-a_{r+1}}2,\qquad
\overline{\frac{C-K}{2}R}_r=\frac{a_r+a_{r+1}}2.}
\tag{21}
\]
The symmetric term sums to zero. The antisymmetric term retains the
entire positive mass \(F_{\mathcal C}\). Moreover,
\[
\langle(I-S)R,\phi_N\rangle_\nu\longrightarrow0,\qquad
\left\langle\frac{C-K}{2}R,\phi_N\right\rangle_\nu
\longrightarrow D_{\mathcal C}.
\tag{22}
\]
These assertions follow directly from (21), since
\(\sum_r a_r<\infty\). They also agree with the finite-energy bound
for the first pairing, whose absolute value is at most
\(\sqrt{\mathcal E(R)\mathcal E(\phi_N)}\).

Thus the actual factor \(1/(3n+1)\) produces a positive summable
first difference, not a zero-mass symmetric second difference.
The exact height identity
\[
1-\lambda(n)=\frac1{2^{v_2(3n+1)}\,Un}
\]
does not change the sign or mass in (19)--(21).
Discarding the antisymmetric term would discard the canonical charge
being tested.

For completeness, whenever level means of a candidate solution are
defined, the projected symmetric Poisson equation would be
\[
\psi_r-\frac{\psi_{r-1}+\psi_{r+1}}2=a_r.
\tag{23}
\]
With \(p_r=\psi_r-\psi_{r-1}\), it requires
\[
p_{r+1}-p_r=-2a_r.
\]
The two limiting slopes differ by \(-2F_{\mathcal C}\). Both slopes
would have to be zero for square-summable differences. This is the
explicit failure of the finite-energy construction; it is the same
positive coefficient tested quantitatively in (18).

## 6. Testing Ancona and Martin-boundary regularity

The actual inverse kernels already have exact Green factorization.
For the stationary inverse law,
\[
\mathcal G_\nu(q,n):=\sum_{j\ge0}K^j(q,n)
=
\begin{cases}
\nu(n)/\nu(q),&n\in\operatorname{Pred}(q),\\
0,&\text{otherwise}.
\end{cases}
\tag{24}
\]
A predecessor is reached at one depth only, because cycles were removed.
For the critical Doob kernel
\[
K_h(q,n)=\mathbf1_{\{Un=q\}}\lambda(n)\frac{h(n)}{h(q)},
\]
the analogous expression is
\[
\mathcal G_h(q,n)=
\begin{cases}
\Lambda_{n,q}\,h(n)/h(q),&n\in\operatorname{Pred}(q),\\
0,&\text{otherwise},
\end{cases}
\tag{25}
\]
where \(\Lambda_{n,q}\) is the product of \(\lambda\) along the
unique retained path.

For any reachable inverse geodesic \(q\to z\to n\), either Green
kernel satisfies
\[
\boxed{\mathcal G(q,n)=\mathcal G(q,z)\mathcal G(z,n).}
\tag{26}
\]
Thus an Ancona-type inequality along reachable paths already holds
with constant one. It does not compare incomparable branches.

For an actual retained edge \(Un=q\), the arithmetic sibling
\[
B(n)=64n+21
\]
is another positive odd ternary unit with
\[
3B(n)+1=64(3n+1),\qquad U(B(n))=q.
\]
The two siblings have disjoint inverse cones. Hence both
\(\mathcal G_\nu(n,B(n))\) and \(\mathcal G_\nu(B(n),n)\)
are zero. The irreducible Harnack transport required to move between
such branches is absent. Finite Green factorization does not supply
a comparison of \(G(B(n))\) with \(G(n)\).

Replacing \(K\) with \(S\) restores irreducibility on an escaping
component, but Section 3 then gives recurrence: its undiscounted
Green function is infinite. This replacement violates the finite-Green
hypothesis in the cited Martin-boundary theorems. The ordinary graph
also has not been identified with an admissible convolution kernel on
one of their groups.

The problem is therefore not a missing citation to Ancona inequalities.
The exact multiplicativity that would be their useful first consequence
is already present, while the arithmetic comparison between distinct
inverse cones is not.

## 7. What this attempt establishes

The new deductions are the actual-graph recurrence calculation (8)--(9),
the unconditional-in-the-orbit-graph sector obstruction (10)--(14),
and the exact canonical Poisson decomposition (19)--(22).
All retain the analytic source qualifications stated in Section 1.

They do not turn the previously known estimate
\[
N\mathcal D(A_NR)\longrightarrow
b_\infty
=\sum_{\mathcal C\ {\rm escaping}}
     \frac{D_{\mathcal C}^{\,2}}{C_{\mathcal C}}
\]
into a zero limit. The attempted deep-theorem application reaches the
positive canonical charge in the antisymmetric current and stops there.
Neither the full sector bridge nor a finite-energy symmetric Poisson
bound for this charge has been obtained.

No conclusion about nontrivial periodic cycles is made: those vertices
were killed throughout the analytic construction.
