# Green potentials, quantitative ergodic smoothing, and the arithmetic transfer

Date: 2026-11-22. **Status: new written deductions from the frozen ordinary
harmonic inputs. Full Collatz remains open.** No analytic assertion below
is installed as a Lean axiom or counted as a Lean theorem.

The literature suggested testing the mean ergodic theorem in the actual
stationary Hilbert space, and testing a Green potential through its
Dirichlet energy. These tests produce a quantitative result: the canonical
potential has finite energy along actual Collatz edges, and its Cesàro and
Abel averages have energy at most a displayed constant times \(1/N\) and
\((1-\alpha)/(1+\alpha)\), respectively. The normalized energies have an
exact common limit, the total quadratic escape capacity in (24). None of
these statements assumes that the potential itself belongs to that
Hilbert space.

The remaining transfer is specifically arithmetic. The companion
[FIVE_EDGE_TRANSPORT.md](FIVE_EDGE_TRANSPORT.md) proves that composition
does not have a uniform bound on the five-edge energy of arbitrary
finitely supported inputs, even after Cesàro averaging. Its exact
counterexamples cover the ordinary shortcut map \(T\), the accelerated
odd map \(U\), and the killed \(U\)-domain used below; the last assertion
uses explicitly selected test targets whose actual orbits reach one.
The explicit model in Section 7 also shows that harmonic summability of
every positive power, a bounded stationary reference, and a bounded pure Green potential
do not by themselves imply mean regularity of the forward boundary.

The actual-edge estimate was independently derived by the analytic and
certificate agents. The quantitative Cesàro/Abel identities below were
derived in the analytic lane and independently checked by the certificate
lane. The merger lane supplied the weak-convergence boundary argument
which upgrades the estimates to exact limiting identities. The companion
arithmetic transport calculation is the certificate lane's contribution.

## 1. The primary-source theorem tests

Three primary sources informed the calculation. The conclusions below
come from checking their hypotheses, not from treating the existence of
an operator representation as an absorption theorem.

* **Yosida and Kakutani (1938), page 333:** their mean ergodic theorem
  assumes power boundedness and weak compactness of the Cesàro orbit.
  On a Hilbert space, an isometry has both properties. In our application
  this applies to the square-integrable *gradient* of the canonical
  potential. Membership of the potential itself in the Hilbert space has
  not been proved. The quantitative estimates in Sections 4–5 are proved
  directly and are stronger than the rate-free application.
  [Original paper](https://www.jstage.jst.go.jp/article/pjab1912/14/9/14_9_333/_pdf/-char/en).

* **Assani (2024), Theorems 1.2 and 2.6:** the relevant recurrence theorem
  requires a finite measure equivalent to counting measure and power
  bounded composition in its \(L^1\) space. The corrected reference
  ν here has infinite total mass. The finite harmonic-weighted measures
  obtained from our moment estimates have no proved power bound. Thus
  that theorem cannot presently close this route. Its invariant finite
  measure assertion does not assert equivalence to counting measure.
  [Published article](https://doi.org/10.4064/sm230913-14-12),
  [author's arXiv version 3](https://arxiv.org/pdf/2208.11675v3).

* **Gaudillière and Landim, Section 2, equation (2.1) and its energy
  identity:** their treatment distinguishes an operator from its
  stationary adjoint and uses the symmetric quadratic energy even when
  the chain is not reversible. This distinction is essential here. Their
  irreducible continuous-time capacity theorem is not invoked for our
  directed inverse tree. We prove the needed discrete, killed-domain
  identity explicitly below.
  [Primary paper](https://arxiv.org/pdf/1111.2445v1).

There is also a precise potential-theory check: \(K^jR\to0\) states that
\(R\) is a pure potential for the **inverse** kernel \(K\). This does not
state that \(R\circ U^j\to0\) under the forward map. The model in Section 7
satisfies the first limit and violates the second at every state.

## 2. Frozen inputs and operators

The exact source pins remain those of
[LATE_GREEN_HARMONIC_MOMENT.md](LATE_GREEN_HARMONIC_MOMENT.md):

| Source | Frozen head | Input used here |
|---|---|---|
| PR185 | `276be8154f4e867acc0230466b34d9cb224aacf5` | Ordinary harmonic correction and global reference moments in `research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`. |
| PR182 | `9dacd610ba7735e89e2e29e4ab01795983317980` | `HARMONIC_CAPTURE_BRIDGE.md` and `CANONICAL_ESCAPE_LABEL.md` in `research/lean-dyadic-descent-20261121/`: complete Green identity and canonical component limit. |
| PR175 | `2bc2ad37b490a5aea63658eaf657bc048da4532e` | Upstream orbit-count and predecessor-floor inputs retained through the preceding Green-moment note. |

Let \(\mathcal N\) be the positive odd ternary units which are not
themselves periodic. A state may later enter a periodic orbit; transport
is killed at that first periodic state. Write

\[
\begin{gathered}
U(n)=(3n+1)/2^{v_2(3n+1)},\qquad
(Lf)(q)=\sum_{n\in\mathcal N:U(n)=q}f(n),\\
h(q)=G(q)/q,\qquad \lambda(q)=\frac{3q}{3q+1},\qquad
d(q)=(1-\lambda(q))h(q),\\
L\nu=\nu,\qquad 0<h\le\nu\le A,\qquad
A=\frac{203}{3c}.
\end{gathered}
\tag{1}
\]

Here \(c>0\) is the upstream predecessor-population constant, with the
same source-qualified status as in the pinned construction. The reference
moment at exponent one is

\[
\sum_{q\in\mathcal N}\frac{\nu(q)}q\le200A.
\tag{2}
\]

Set

\[
g=d/\nu,\qquad D=\sum_qd(q),\qquad
R=\sum_{j\ge0}K^jg=1-\lambda h/\nu,\qquad 0\le R\le1.
\tag{3}
\]

Since \(d(q)=h(q)/(3q+1)\le\nu(q)/(3q)\),

\[
0<D\le\frac{200A}{3}<\infty.
\tag{4}
\]

On the real Hilbert space \(H=\ell^2(\mathcal N,\nu)\), define

\[
(Cf)(n)=
\begin{cases}f(U(n)),&U(n)\in\mathcal N,\\0,&U(n)\notin\mathcal N,
\end{cases}
\qquad
(Kf)(q)=\frac1{\nu(q)}\sum_{U(n)=q}\nu(n)f(n).
\tag{5}
\]

Nonnegative summation and \(L\nu=\nu\) give

\[
\|Cf\|_H^2=\|f\|_H^2,\qquad K=C^*,\qquad KC=I.
\tag{6}
\]

Thus \(C\) is an isometry and \(K\) its coisometry. The inverse rows of
\(K\) sum to one. On \(L^1(\nu)\), \(K\) is a positive contraction: summing
its columns omits precisely the sources whose forward edge is killed.
It need not preserve total \(L^1(\nu)\) mass on this killed domain.

## 3. A finite global energy on actual edges

For any real point function \(f\), define the extended nonnegative sum

\[
\begin{split}
\mathcal D(f)
={}&\sum_{n:U(n)\in\mathcal N}
 \nu(n)|f(U(n))-f(n)|^2\\
&+\sum_{n:U(n)\notin\mathcal N}\nu(n)|f(n)|^2.
\end{split}
\tag{7}
\]

The second term retains the actual killed boundary. For \(f\in H\),
isometry and adjointness give

\[
\mathcal D(f)=\|(I-C)f\|_H^2
             =2\langle f,(I-K)f\rangle_H.
\tag{8}
\]

The positive finite Green truncations

\[
R_M=\sum_{j=0}^{M-1}K^jg\qquad(M\ge1)
\tag{9}
\]

belong to \(L^1(\nu)\cap H\): their \(L^1\) norms are at most \(MD\),
and \(0\le R_M\le R\le1\). Their exact Poisson equations are

\[
(I-K)R_M=g-K^Mg.
\tag{10}
\]

The rightmost term is nonnegative. Therefore

\[
\mathcal D(R_M)
\le2\langle R_M,g\rangle_H=2\sum_qd(q)R_M(q).
\]

Pointwise \(R_M\uparrow R\). Fatou applied to the nonnegative edge sum,
and dominated convergence against the finite measure \(d\), prove

\[
\boxed{\mathcal D(R)\le2\sum_qd(q)R(q)
                        \le2D\le\frac{400A}{3}.}
\tag{11}
\]

In particular \(a:=(I-C)R\in H\), even though \(R\in H\) has not been
established. This is global variation control on the same
ordinary canonical potential; all source collisions remain in \(R\).

## 4. Quantitative Cesàro smoothing

For \(N\ge1\), put

\[
\mathsf A_N=\frac1N\sum_{j=0}^{N-1}C^j.
\]

For any \(f\in H\), \(KC=I\) gives

\[
(I-K)\mathsf A_Nf
=\frac1N\left(C^{N-1}f-f+(I-K)f\right).
\tag{12}
\]

There is an exact isometry cancellation:

\[
\left\langle\mathsf A_Nf,C^{N-1}f-f\right\rangle_H=0.
\tag{13}
\]

Indeed, the terms of the first inner product are
\(\langle f,C^{N-1-j}f\rangle_H\), while those of the second are
\(\langle f,C^jf\rangle_H\). Reversing the finite list proves equality.
Combining (8), (12), and (13),

\[
\mathcal D(\mathsf A_Nf)
=\frac2N\langle\mathsf A_Nf,(I-K)f\rangle_H.
\tag{14}
\]

Apply this identity only to \(f=R_M\in H\). Positivity, (10), and
\(0\le\mathsf A_NR_M\le1\) yield

\[
\mathcal D(\mathsf A_NR_M)
\le\frac2N\sum_qd(q)(\mathsf A_NR_M)(q).
\]

Letting \(M\to\infty\) uses Fatou on the left and dominated convergence
against \(d\) on the right. Thus

\[
\boxed{
\mathcal D(\mathsf A_NR)
\le\frac2N\sum_qd(q)(\mathsf A_NR)(q)
\le\frac{2D}{N}\le\frac{400A}{3N}.}
\tag{15}
\]

The estimate applies at every averaging time and does not presume a rate
of forward convergence to the escape label.

## 5. Quantitative Abel smoothing

For \(0\le\alpha<1\), define

\[
\mathsf B_\alpha=(1-\alpha)\sum_{j\ge0}\alpha^jC^j.
\]

For \(f\in H\), the series converges in \(H\); write
\(u=\mathsf B_\alpha f\). The two exact identities

\[
u=(1-\alpha)f+\alpha Cu,
\qquad Ku=(1-\alpha)Kf+\alpha u
\tag{16}
\]

give

\[
\langle u,(I-K)f\rangle_H
=\frac{1+\alpha}{2(1-\alpha)}\mathcal D(u).
\tag{17}
\]

To check the coefficient, subtract the two inner-product expressions
for \(\langle u,f\rangle_H\) and
\(\langle u,Kf\rangle_H\) from (16), and use
\(\mathcal D(u)=2(\|u\|^2-\langle u,Cu\rangle_H)\).
This also covers \(\alpha=0\).

The same positive truncation and Fatou argument now proves

\[
\boxed{
\mathcal D(\mathsf B_\alpha R)
\le\frac{2(1-\alpha)}{1+\alpha}
       \sum_qd(q)(\mathsf B_\alpha R)(q)
\le\frac{400A}{3}\frac{1-\alpha}{1+\alpha}.}
\tag{18}
\]

This holds for **every** \(0\le\alpha<1\). It does not rely on summing
the cruder harmonic-norm pullback bound, which only directly sums for
\(\alpha<2/5\).

## 6. The applicable mean ergodic theorem and the exact boundary energy

For completeness, the fixed space of \(C\) in \(H\) is zero. If \(Cf=f\),
an eventually killed state has \(f(n)=0\). Otherwise its forward states
\(q_j=U^j(n)\) are distinct and

\[
f(q_j)=f(n),\qquad\nu(q_j)\ge\nu(n)>0.
\]

The latter follows because the harmonic equation at \(q_{j+1}\) includes
its actual predecessor \(q_j\). A nonzero value would contribute
infinitely to the square norm. Thus \(f=0\). Also \(Kf=f\) implies
\(\|Cf-f\|^2=0\), so the adjoint fixed space is zero as well.

Consequently the Hilbert-space mean ergodic theorem applies to
\(a=(I-C)R\in H\) and gives \(\mathsf A_Na\to0\) in \(H\).
This proves qualitative decay of (15) independently. Applying that
theorem to \(R\) itself would require an additional, currently unproved
square-integrability statement. In fact a hypothetical escaping orbit
has \(R(q_j)\to F_{\mathcal C}>0\) and
\(\nu(q_j)\ge\nu(q_0)>0\), and would force \(R\notin H\).

The boundary term can be identified, without subtracting two infinite
square norms. Let

\[
b_j=\sum_qd(q)(C^jR)(q),\qquad b_0=\sum_qd(q)R(q).
\]

All \(b_j\) are finite. Pointwise \(C^jR\to F\), where \(F\) is the
canonical escape label on \(\mathcal N\), with zero on eventually
killed states. Dominated convergence against the finite measure \(d\)
gives \(b_j\to b_\infty:=\sum_qd(q)F(q)\).

Put \(a_M=(I-C)R_M\). The bounds in Section 3 imply
\(\sup_M\|a_M\|_H^2\le2D\), and \(a_M\to a\) pointwise.
Testing against finite-support vectors and using their density in \(H\)
proves \(a_M\rightharpoonup a\) weakly. Furthermore \(Ka=-g\), since
\(KR=R-g\) and \(KCR=R\). All identities involving \(a\) now take
place inside \(H\). In particular,

\[
\begin{aligned}
\langle a,a_M\rangle_H
 &=\langle a+g,R_M\rangle_H\\
 &=\sum_{j=0}^{M-1}\langle C^ja,g\rangle_H
                                      +\sum_qd(q)R_M(q)\\
 &=b_0-b_M+\sum_qd(q)R_M(q).
\end{aligned}
\tag{19}
\]

Weak convergence on the left, bounded convergence for \(b_M\), and
monotone convergence for the last sum give the exact boundary identity

\[
\boxed{\mathcal D(R)=2\sum_qd(q)R(q)-\sum_qd(q)F(q)
                         =2b_0-b_\infty.}
\tag{20}
\]

To obtain the two quantitative limiting identities, use \(Ka=-g\) again.
For \(j\ge1\),

\[
\langle a,C^ja\rangle_H=-(b_{j-1}-b_j).
\]

Expanding the norm of \(\sum_{j<N}C^ja\) and telescoping the finite
correlation sum gives

\[
\boxed{
N\mathcal D(\mathsf A_NR)
=2\sum_qd(q)(\mathsf A_NR)(q)-b_\infty
\longrightarrow b_\infty.}
\tag{21}
\]

For the Abel average, the absolutely convergent correlation expansion
has coefficient \((1-\alpha)/(1+\alpha)\), because
\((1-\alpha)^2\sum_{j\ge0}\alpha^{2j}
=(1-\alpha)/(1+\alpha)\). The remaining correlation series telescopes:

\[
\sum_{j\ge1}\alpha^j(b_{j-1}-b_j)
=b_0-(1-\alpha)\sum_{j\ge0}\alpha^jb_j.
\]

Thus

\[
\boxed{
\frac{1+\alpha}{1-\alpha}\mathcal D(\mathsf B_\alpha R)
=2\sum_qd(q)(\mathsf B_\alpha R)(q)-b_\infty
\longrightarrow b_\infty\quad(\alpha\uparrow1).}
\tag{22}
\]

The endpoint \(\alpha=0\) is also covered by the displayed identity.
Both (21) and (22) improve the upper estimates by identifying the exact
boundary coefficient. Their right sides are nonnegative by their left
sides; no monotonicity of \(R\) along forward orbits is assumed.

Finally, the pinned PR182 component limit is

\[
F_{\mathcal C}=D_{\mathcal C}/C_{\mathcal C},\qquad
D_{\mathcal C}=\sum_{n\in\mathcal C}d(n),\qquad
C_{\mathcal C}=\lim_j\nu(U^jn)>0.
\tag{23}
\]

Grouping the nonnegative summation by escaping components gives

\[
\boxed{b_\infty=\sum_{\mathcal C\ \mathrm{escaping}}
                    \frac{D_{\mathcal C}^2}{C_{\mathcal C}}
              \le D<\infty.}
\tag{24}
\]

Every escaping component has \(D_{\mathcal C}>0\), because the canonical
charge is positive at each state. Consequently this coefficient is zero
exactly when there are no escaping components. The theorem computes the
coefficient; it does not prove that it is zero. If an escape exists, the
order \(1/N\) and the corresponding Abel order in the estimates are
therefore sharp. More precisely, the exact rates identify the closing target:

\[
\mathcal D(\mathsf A_NR)=o(1/N)
\quad\Longleftrightarrow\quad
b_\infty=0
\quad\Longleftrightarrow\quad
\text{there are no escaping components}.
\]

Equivalently, the Abel closing target is
\(\mathcal D(\mathsf B_\alpha R)=o(1-\alpha)\) as \(\alpha\uparrow1\).
The estimates proved above give \(O(1/N)\) and \(O(1-\alpha)\); replacing
them by these strictly smaller orders is not justified by the present
argument. Excluding nontrivial periodic cycles is still a separate task.

The actual estimates concern \(U\)-edges. The requested closing energy
instead uses the multiplicative pairs \(n,5n\):

\[
E_5(f)=\sum_{\substack{n>0\ \mathrm{odd}\\3\nmid n}}
           \frac{|f(5n)-f(n)|}{n}.
\tag{25}
\]

This is an absolute-value energy on a different set of pairs, whereas
\(\mathcal D\) is a squared energy on actual \(U\)-edges. No estimate
comparing (25) with (7) has been proved for the canonical averages.
The companion exact transport calculation proves that a uniform
composition bound for (25), over all finitely supported inputs, is
false. A successful application must use additional structure of this
specific \(R\), beyond the generic operator hypotheses tested above.

## 7. An explicit model testing the proposed regularity transfer

This is a counterexample to a generic functional-analytic inference,
not a counterexample to Collatz. It makes the failure of the inference
independent of any hypothetical Collatz escape.

### 7.1 A binary predecessor map with a bounded stationary reference

Define a map \(V:\mathbb N_{>0}\to\mathbb N_{>0}\) by

\[
V(n)=
\begin{cases}
2n,&n\text{ is a power of }2,\\
\lfloor n/2\rfloor,&\text{otherwise}.
\end{cases}
\tag{26}
\]

Every ordinary trajectory first reaches a power of two and then follows
the infinite power ladder. Put

\[
\eta(n)=\log\frac{n+1}{n}\quad(n\text{ not a power of }2),
\qquad
\eta(2^j)=\sum_{i=0}^j\log\frac{2^{i+1}+2}{2^{i+1}+1}.
\tag{27}
\]

A nonpower target \(q\) has predecessors \(2q,2q+1\), whose logarithmic
weights telescope to \(\log((q+1)/q)\). A power target \(q=2^j\) has
the predecessor \(2q+1\), together with \(q/2\) if \(j\ge1\).
The target 1 has only predecessor 3. These cases prove exactly

\[
\sum_{V(n)=q}\eta(n)=\eta(q).
\tag{28}
\]

Let \(a=\eta(1)=\log(4/3)\). The reference satisfies

\[
\frac an\le\eta(n)<1,\qquad
\sum_{n\le X}\eta(n)
\le\log(X+1)+1+\log_2X.
\tag{29}
\]

The first inequality follows from
\(\log(1+1/n)\ge1/(n+1)\) off the ladder and
\(\eta(2^j)\ge a\) on it. The upper bound on ladder values follows from
\(\log(1+x)\le x\) and \(\sum_i2^{-i-1}=1\).

This example even has predecessor population of order \(X/q\): for a
nonpower target \(q\), its depth-\(k\) predecessors are precisely
\([2^kq,2^k(q+1)-1]\). These intervals give a lower density at least
\(1/(2q)\). For a power target, use the contained predecessor set of
its nonpower parent \(2q+1\), giving lower density at least
\(1/(6q)\). The number of states at most \(X\) on any one supplied
forward orbit is \(O(\log X)\). Neither positive basin density nor
sparse single trajectories prevents the phenomenon below.

### 7.2 A pure Green potential with every harmonic moment

Use the inverse kernel formed from \(V,\eta\), and let the charge be

\[
d_0(n)=a\mathbf1_{n=1},\qquad g_0=d_0/\eta.
\]

The source 1 visits each ladder point exactly once and no other state.
Consequently its normalized Green potential is

\[
R_0(n)=\sum_{k\ge0}K_V^kg_0(n)=
\begin{cases}
a/\eta(2^j),&n=2^j,\\0,&\text{otherwise}.
\end{cases}
\tag{30}
\]

Thus \(0\le R_0\le1\), and for every \(p>0\),

\[
\sum_{n\ge1}\frac{R_0(n)^p}{n}\le\sum_{j\ge0}2^{-j}=2.
\tag{31}
\]

At each fixed target the finite Green series eventually includes its
only nonzero term, so \(K_V^kR_0\to0\). Let

\[
C_\infty=\lim_j\eta(2^j)\in(a,1),\qquad
F_0=a/C_\infty>0.
\]

Every actual forward orbit nevertheless has

\[
R_0(V^kn)\longrightarrow F_0.
\tag{32}
\]

Composition by \(V\) has harmonic \(L^1\) norm at most \(5/2\).
Indeed a nonpower target has two parents of size at least \(2q\), and a
power target has its half-size ladder parent and its parent \(2q+1\).
Thus every fixed iterate and every finite Cesàro average of \(R_0\)
is harmonic-summable and has ordinary mean zero. Their pointwise limit
is the positive constant \(F_0\). The corresponding fixed-parameter
Abel averages also have ordinary mean zero, by truncating the uniformly
bounded tail of the series. This refutes the proposed mean-limit
transfer under the displayed generic hypotheses.

### 7.3 Adding a periodic component and infinite five energy

An explicit residue encoding makes the limiting five energy infinite.
For \(r=1,2,3\), let

\[
\phi_r(m)=3(m-1)+r,\qquad W(m)=\max(1,\lfloor m/2\rfloor).
\]

Define \(V_*\) on all positive integers by

\[
V_*(\phi_2(m))=\phi_2(V(m)),\qquad
V_*(\phi_r(m))=\phi_r(W(m))\quad(r=1,3).
\tag{33}
\]

The points 1 and 3 are periodic. On the nonperiodic domain
\(\mathbb N_{>0}\setminus\{1,3\}\), use reference
\(\eta_*(\phi_2(m))=\eta(m)\) and, for \(r=1,3\) and \(m\ge2\),

\[
\eta_*(\phi_r(m))=\log((m+1)/m).
\]

The same two-parent telescoping proves harmonicity on the killed domain.
It is again a positive bounded reference with a harmonic lower bound and
logarithmic prefix mass.

Put \(R_*(\phi_2(m))=R_0(m)\) and zero on the other residue classes,
including the two periodic states. It is the normalized pure Green
potential of the charge \(a\delta_2\). Its positive harmonic moments
are all finite, since it is supported on \(3\cdot2^j-1\). Its forward
limit is the exact invariant function

\[
F_*(n)=F_0\mathbf1_{n\equiv2\pmod3},\qquad F_*(1)=0.
\tag{34}
\]

The harmonic pullback norm of \(V_*\) is at most 3. For an escaping
ladder target, the ratio contributed by its preceding ladder point is
at most \(5/2\), and its other parent contributes less than \(1/2\).
Other nonperiodic targets have two comparable-size parents. At the
periodic points 1 and 3 the respective total ratios are
\(1+1/4+1/7<3\) and \(1+1/2+1/3<3\).
Thus every finite-time approximant of \(R_*\) is harmonic-summable and
has finite \(E_5\).

Multiplication by 5 interchanges the two ternary-unit residue classes.
For every positive odd ternary unit \(n\),
\(|F_*(5n)-F_*(n)|=F_0\). Hence

\[
\boxed{E_5(F_*)=F_0\sum_{\substack{n>0\ \mathrm{odd}\\3\nmid n}}
                         \frac1n=\infty.}
\tag{35}
\]

The charge in this simplest model is supported at one point. Positivity
of a charge at every nonperiodic state does not repair the inference.
Here is an explicit extension. In each encoded component, add charge
\(\epsilon\eta_*(\phi_r(m))/(m+1)\) and take its Green potential, while
retaining one half of the atomic potential \(R_*\). Let

\[
S=\sum_{m\ge1}\frac{\eta(m)}{m+1}<\infty,
\qquad 0<\epsilon\le\min(1/4,a/(4S)).
\]

At a nonpower target of the escaping component, or any nonperiodic
target in the periodic components, inverse coordinates grow at least
as \(2^km\). The added normalized Green potential is therefore at most
\(2\epsilon/m\). At an escaping ladder target it is at most
\(\epsilon S/a\le1/4\). The full potential is bounded by \(3/4\),
has every positive harmonic moment, and has a strictly positive charge
at every state of the killed domain. Its forward limit is zero on the
periodic components and the positive constant
\((a/2+\epsilon S)/C_\infty\) on the escaping component. Its limiting
five energy is still infinite.

This model is not claimed to satisfy the Collatz affine identities or
the specific canonical formula \(d=(1-\lambda)h\). It proves the narrow
point required for the theorem test: inverse pure-potential status,
all positive harmonic moments, stationary-reference bounds, positive
charges, finite actual-edge energy, and quantitative ergodic smoothing
are compatible with an irregular, nonzero forward boundary. A closing
argument must extract more of the actual Collatz arithmetic.

## 8. What this attempt proves and the first unsupported transfer

The positive output is the global actual-edge budget (11), the explicit
Cesàro rate (15), the Abel rate (18), and the exact boundary and limiting
identities (20)–(24). They apply to the canonical ordinary potential under its pinned analytic
construction, retain killing, and do not replace its transported source.

The first unsupported closing inference would be to deduce a uniform
bound for \(E_5\) of these canonical averages, or ordinary mean
convergence to their invariant limit, from those operator estimates.
The companion transport theorem rules out a bound valid for arbitrary
finitely supported inputs. Section 7 rules out the generic
potential-theory implication even under stronger summability than the
canonical harmonic moment theorem supplies. Neither result rules out a
more specific Collatz estimate using its canonical density and its
unbounded family of affine carries.

No claim excluding all escaping Collatz components follows here, and
nontrivial periodic cycles remain a separate obligation.
