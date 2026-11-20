# Positive occupation charges for the actual unsafe return

**Status: PROPOSED, with written deductions and exact bounded replay.**
This note gives a source-persistent positive closing functional which includes
cycles, transfers a one-path interval theorem to an all-return Green bound,
and identifies the gap between the two observables. **The required closing
estimate is not proved. Collatz remains unresolved.**

The principal improvement over the earlier signed-drift target is a completed
cycle interface: a sublogarithmic reciprocal-psi Green bound would exclude
every nonabsorbed ordinary atom, with no separate cycle hypothesis. This is
a sufficient condition, not an equivalence claimed from the available
interfaces. An explicit terminating control below shows why that distinction
matters.

## 1. Frozen maps, sources, and conventions

Use the positive ordinary shortcut map, killed at 1,

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.\end{cases}
\]

Use exactly the moving-rank acceleration and **quarter-safe** return from
[PR152, ACTUAL_TRANSPORT.md, AT2--AT3](https://github.com/GettysburgResearch/collatz/blob/2391a9c1e4a7f77233b951d2eb6da92e76652e7c/research/gemini-global-closure-20261120/ACTUAL_TRANSPORT.md).
For completeness, put

\[
z_a(n)=(3^a-2^{a+1})n+3^a-2^a,
\qquad R(n)=\min_{a\ge0}\frac{z_a(n)^2}{3^{v_3(z_a(n))}},
\]

with zero component rank when its numerator vanishes. For even \(n>1\),
the active mode is \(a=0\); for odd \(n>1\), it is \(a=v_2(n+1)\).
The acceleration \(A\) consumes \(k=\lfloor v_2(z_a(n))/(a+1)\rfloor\)
physical copies of \(1^a0\). The pinned interfaces prove totality, \(k\ge1\),
the rank reduction to \(a=0,1,2,h\), \(h=v_3(2n+1)\), and

\[
R(1)=0,\qquad n-1\le R(n)\le n^2\quad(n\ge2).
\tag{1}
\]

Let \(G=\{n>1:4R(A(n))\le R(n)\}\) and \(U=\{n>1\}\setminus G\).
The map \(B:U\to U\cup\{1\}\) applies \(A\) once and then follows \(G\)
until its first subsequent unsafe endpoint or 1. Safe excursions are finite
by positive-integer rank descent. Its killed pushforward has endpoint rows
and source columns:

\[
(Hf)(y)=\sum_{u\in U:B(u)=y}f(u),\qquad y\in U.
\]

There is no fresh input after a return. All sums below retain the weights
of their **original** ordinary sources. Set

\[
\psi(u)=1+\log\log(R(u)+6),\quad
\psi_*=1+\log\log7>0,\quad c=\log6.
\]

The proved actual-return budget is

\[
\psi(Bu)\le\psi(u)+c\quad(Bu>1),\qquad \psi(u)\ge\psi_*.
\tag{2}
\]

It comes from \(R(Bu)+6\le(R(u)+6)^6\), not a parity-averaged operator.
The resident moving-rank source is frozen on main
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`; its prior qualifications remain
those in the [resident transport guide](../integrated/renewal-transport/README.md).

## 2. GCT-001: a positive closing charge includes cycles

For any fixed nonnegative \(f\in\ell^1(U)\), define

\[
\mathcal G_N(f)=\sum_{j=0}^{N-1}\sum_{y\in U}
                 \frac{(H^jf)(y)}{\psi(y)}.
\tag{3}
\]

Every finite-horizon value is finite because
\(0\le\mathcal G_N(f)\le N\|f\|_1/\psi_*\). A finite initial
psi-moment is **not required** for this functional.

Let \(E\subset U\) be the set of original states never absorbed at 1,
including states that enter a nonabsorbing cycle, and put

\[
m_\infty=\sum_{u\in E}f(u)=\lim_{j\to\infty}\|H^jf\|_1.
\]

The equality follows by dominated convergence of the original-source
survival indicators, bounded by the summable input \(f\).

**Claim GCT-001.** For every integer \(N\ge1\),

\[
\mathcal G_N(f)\ge
\sum_{u\in E}f(u)\sum_{j=0}^{N-1}\frac1{\psi(u)+cj}
\ge\frac1c\sum_{u\in E}f(u)
       \log\left(1+\frac{cN}{\psi(u)}\right).
\tag{4}
\]

In particular,

\[
\boxed{\quad
\liminf_{N\to\infty}\frac{\mathcal G_N(f)}{\log N}
\ge\frac{m_\infty}{\log6}.
\quad}
\tag{5}
\]

**Proof.** A never-absorbed atom retains its exact weight \(f(u)\) at
every return, including after mergers with other sources. Iterating (2)
gives \(\psi(B^ju)\le\psi(u)+cj\). Positive source accounting gives
the first inequality in (4). Since \(t\mapsto1/(\psi(u)+ct)\) decreases,
the sum is at least its integral over \([0,N]\), proving the second.
For every fixed \(u\),
\(\log(1+cN/\psi(u))/\log N\to1\).
Fatou's lemma for the nonnegative source sum proves (5). No independence,
stationarity, mixing, or distributional reset is used. \(\square\)

Consequently, for **one fixed input positive at every member of \(U\)**,

\[
\boxed{\quad \mathcal G_N(f)=o(\log N)\quad}
\tag{6}
\]

would force \(E=\varnothing\). Every ordinary nonconvergent shortcut orbit
must visit \(U\) infinitely often, since an eventual safe tail would
decrease a positive integer rank indefinitely. Thus (6) would prove full
Collatz, including exclusion of nontrivial cycles. Finiteness of
\(\mathcal G_\infty(f)\) is a stronger sufficient condition.

This replaces the earlier sufficient requirement
\(N^{-1}\sum_{j<N}\|H^jf\|_\psi=o(\log\log N)\), plus cycle exclusion,
by a different positive functional. No implication between these two
unproved quantitative upper estimates is needed or asserted. Equation (6)
remains **OPEN**. An \(O(\log N)\) bound alone would not close (5).

## 3. GCT-002: every omitted original source is already controlled

Fix the same explicit input as
[PR152, FIXED_SOURCE_DRIFT.md](https://github.com/GettysburgResearch/collatz/blob/2391a9c1e4a7f77233b951d2eb6da92e76652e7c/research/gemini-global-closure-20261120/FIXED_SOURCE_DRIFT.md):

\[
f_0(u)=\frac{\mathbf1_U(u)}{u(u+1)}.
\tag{7}
\]

It is positive at every unsafe state and has total mass at most \(1/2\).
For integers \(M,N\ge1\), telescoping \(1/[u(u+1)]\) and (2) give

\[
\boxed{\quad
0\le\mathcal G_N(f_0)-\mathcal G_N(f_0\mathbf1_{u\le M})
\le\frac{N}{(M+1)\psi_*}.
\quad}
\tag{8}
\]

The bound uses only mass nonincrease and \(1/\psi\le1/\psi_*\);
it includes the complete actual future of every omitted source through
the specified finite horizon. There is no estimate of omitted *endpoints*.

Taking \(M=N\) leaves an \(O(1)\) tail. Thus the proposed full-solution
estimate (6) for (7) is equivalent to the same estimate for the finite
triangular array

\[
\boxed{\quad
\sum_{\substack{u\in U\\u\le N}}\frac1{u(u+1)}
\sum_{\substack{0\le j<N\\B^ju>1}}\frac1{\psi(B^ju)}
=o(\log N).
\quad}
\tag{9}
\]

More generally one may use any cutoff \(M(N)\) with
\(N/(M(N)+1)=o(\log N)\). This is a reduction of the source-tail task,
not a bound on the finite triangular array.

## 4. GCT-003: absorption does not supply the quantitative bound

The following is a **separate deterministic control map**, not a Collatz
orbit or a proposed counterexample to Collatz. It refutes a functional-
analytic shortcut using only the interfaces above, even with the same
ordinary-source weights.

Write \(n=2^kq\), \(q\) odd, and set \(L(q)=2^{q^3}\). On \(n\ge2\),
define the killed map

\[
J(n)=\begin{cases}2n,&k<L(q),\\1,&k\ge L(q).\end{cases}
\tag{10}
\]

Every individual source is absorbed after finitely many steps. Put
\(R_0(n)=n^2\) and \(\psi_0(n)=1+\log\log(n^2+6)\). The rank is proper,
has \(\#\{n\ge2:R_0(n)\le X\}<\sqrt X\), and satisfies the analogue
of (1). Every surviving step satisfies

\[
R_0(Jn)+6=4n^2+6\le(n^2+6)^2,
\qquad\psi_0(Jn)\le\psi_0(n)+\log2.
\tag{11}
\]

Moreover, a doubling path has at most
\(1+\lfloor\log_2 X\rfloor\) states in any translated integer interval
of width \(X\): if it has \(r\) such states, their extreme difference is
at least \(2^{r-1}-1\), and is at most \(X-1\).

Nevertheless, use \(f_0(n)=1/[n(n+1)]\) on the control's whole domain and
take an odd \(q\ge3\), \(N=L(q)\). Its original atom remains at
\(q2^j\), \(0\le j<N\), and

\[
\psi_0(q2^j)<3+\log N.
\]

Indeed \(\log(4^j q^2+6)\le2j\log2+\log(q^2+6)<3N\).
Hence its contribution alone gives

\[
\frac{\mathcal G_N(f_0)}{\log N}
\ge\frac{N}{q(q+1)(3+\log N)\log N}
\ge\frac{2^{q^3}}{4q^8}\longrightarrow\infty.
\tag{12}
\]

The last inequality uses \(\log N=q^3\log2<q^3\),
\(q(q+1)\le2q^2\), and \(3+q^3\le2q^3\).

Thus individual absorption, a proper rank, the additive psi budget,
full-support reciprocal-square source weights, and strong translated-path
sparsity do **not** imply (6). For each fixed atom its finite Green sum
divided by \(\log N\) tends to zero; the attempted domination uniformly
over original atoms is the missing step. This does not disprove (6) for
the actual Collatz return. It prevents presenting that bound as a necessary
consequence of convergence under the presently established interfaces.

## 5. GCT-004: a proved all-return Green bound for smaller charges

Here there is a valid interface to the one-path theorem in
[PR153, drift.md, FID-DRIFT-001/002/005](https://github.com/GettysburgResearch/collatz/blob/eb04a5d79020cefa0ba46794095b5766c5ff66a4/research/fixed-integer-descent/drift.md).
Its manuscript SHA-256 is
`d73a93d8a803996bde7b15f33e307d28385c8ffe2f9b99f449dfea35140c3338`.
Let \(F(X)\) denote the exact recursive integer envelope there. Every
finite simple ordinary shortcut path has at most \(F(X)\) states in
any translated interval of integer width \(X\), and

\[
F(X)\le10X^{29/30},\qquad
F(X)\le C_\alpha X^\alpha
\quad\bigl(H_2(\log_3 2)<\alpha<1\bigr).
\tag{13}
\]

The first constant is explicit. The recursive constants \(C_\alpha\) are
effective as proved in the source, but not numerically evaluated here.

Let \(\mathcal P\subset U\) be the set of periodic states of \(B\),
and \(f\ge0\) have finite unweighted mass. Then for every integer interval
\(I=[a,a+X)\), \(a\ge1\),

\[
\boxed{\quad
\sum_{j\ge0}\sum_{y\in I\setminus\mathcal P}(H^jf)(y)
\le F(X)\|f\|_1.
\quad}
\tag{14}
\]

**Proof.** Along one original \(B\)-orbit, each nonperiodic state appears
at most once. Any finite collection of its distinct states belongs to
the distinct value set of the same ordinary \(T\)-orbit. These values
are contained in a finite simple \(T\)-prefix: in the eventually periodic
case take the preperiod and one traversal of the cycle; otherwise take a
sufficiently long prefix. Thus (13) bounds each original source's visits
to \(I\setminus\mathcal P\). Multiply by that source's fixed weight and
use Tonelli's theorem. Different sources may merge arbitrarily; their
weights add, and no bound on the *number* of predecessor sources is used.
\(\square\)

This theorem permits nontrivial cycles by deleting their periodic states
from the observable. If cycle exclusion is supplied separately, the
deletion disappears. It is not legitimate to delete it silently.

For \(s>29/30\), \(H_0\ge1\), integration of the counting bound gives
the useful uniform consequence

\[
\boxed{\quad
\sum_{j\ge0}\sum_{\substack{y\ge H_0\\y\notin\mathcal P}}
y^{-s}(H^jf)(y)
\le \frac{10s}{s-29/30}\,H_0^{29/30-s}\|f\|_1.
\quad}
\tag{15}
\]

For a single original path let \(A(t)\) count its nonperiodic endpoints
in \([H_0,t]\). Equation (13) gives
\(A(t)\le10(\lfloor t\rfloor-H_0+1)^{29/30}\le10t^{29/30}\).
The identity
\(\sum y^{-s}=s\int_{H_0}^{\infty}A(t)t^{-s-1}\,dt\), followed by
positive source summation, proves (15). In particular,

\[
\sum_{j\ge0}\sum_{\substack{y\ge H_0\\y\notin\mathcal P}}
\frac{(H^jf)(y)}y\le300H_0^{-1/30}\|f\|_1.
\tag{16}
\]

Using the second part of (13) instead gives
\(C_\alpha sH_0^{\alpha-s}/(s-\alpha)\) for every \(s>\alpha\).
Thus an all-return Green bound exists for every
\(s>H_2(\log_3 2)\), and in particular for every \(s>19/20\).
This does not claim that the threshold is optimal for actual Collatz.

### An exact bounded corrector and a reusable original-source tail

Define the actual observable
\(a_{H_0}(u)=\mathbf1_{\{u\ge H_0,\ u\notin\mathcal P\}}/u\), and

\[
V_{H_0}(u)=\sum_{j\ge0,\ B^ju>1}a_{H_0}(B^ju),\qquad V_{H_0}(1)=0.
\]

Equation (16), applied to a point mass, proves

\[
0\le V_{H_0}(u)\le300H_0^{-1/30},\qquad
V_{H_0}(u)-V_{H_0}(Bu)=a_{H_0}(u).
\tag{17}
\]

Thus there is a bounded positive Poisson corrector for this smaller charge
on the actual return. It is defined by a convergent all-time series;
no algorithm deciding \(\mathcal P\) or computing that infinite series
to a prescribed error is asserted. The finite terminating paths in the
checker have exact rational correctors and exact telescoping identities.

For the input (7) restricted to its **original** sources above \(M\),
the entire all-return omitted charge is at most

\[
\frac{300H_0^{-1/30}}{M+1}.
\tag{18}
\]

Unlike a fresh-source estimate, (14)--(18) retain every correlation formed
by actual repeated transport. They establish an infinite-horizon bound
for decaying ordinary-height observables. They do not establish it for
the much larger closing observable \(1/\psi\).

For an explicit separation, the nonabsorbing control \(J(n)=n^2\),
\(n\ge2\), has extremely sparse simple paths and
\(\sum_{j\ge0}(J^j2)^{-1}=\sum_{j\ge0}2^{-2^j}<1\).
Its same model gauge satisfies the additive bound with \(\log2\), while
\(\psi_0(J^ju)=j\log2+O_u(1)\). Its reciprocal-psi Green sum has order
\(\log N\). Finite reciprocal-height charge, or a bounded corrector with
strict but vanishing charges, is therefore compatible with escape.
This is again a control map, not a Collatz counterexample.

## 6. Exact finite whole-source enclosures

The standalone checker is
[global_closure_transport.py](../../experiments/global_closure_transport.py).
It reconstructs \(R,A,B\), physically replays every encountered \(A\) word,
transports original-source mass with outward integer intervals, and evaluates
\(1/\psi\) with outward logarithm intervals. The default scope is every
unsafe source \(u\le8192\), through 64 actual returns. Formula (8)
includes every other original source.

The [frozen report](../../reports/2026-11-20-global-closure/transport-report.json)
gives these **whole-source** enclosures:

| Return horizon \(N\) | Lower bound on \(\mathcal G_N(f_0)\) | Upper bound |
|---:|---:|---:|
| 1 | 0.078505334875 | 0.078578609312 |
| 4 | 0.120180686698 | 0.120473784445 |
| 8 | 0.129521120082 | 0.130107315574 |
| 16 | 0.140638737116 | 0.141811128100 |
| 32 | 0.140870122044 | 0.143214904012 |
| 64 | 0.140870202043 | 0.145559765977 |

The finite part at \(N=64\) lies in
`[0.140870202043, 0.140870202044]`. Its omitted-source allowance is still
positive, at most `0.004689563934`. The disappearance of the enumerated
carriers is not an all-source zero theorem. With this fixed source cutoff,
the analytic error grows with the horizon; the table proves no asymptotic
trend or bound in (6).

The replay covers 2,941 unsafe original sources, 3,475 distinct actual
return edges, 9,117 physically replayed acceleration words and 25,037
shortcut edges. It checks 122,729 translated windows and 3,475 exact
rational reciprocal-height coboundaries. The largest physical value in
these replays is 4,076,810; the longest enumerated unsafe path has 37
states before absorption. These are finite evidence limits.

For logarithms, normalize a positive rational \(x=2^ky\), \(1\le y<2\),
and use the first 32 terms of
\(\log y=2\sum_{r\ge0}z^{2r+1}/(2r+1)\),
\(z=(y-1)/(y+1)\le1/3\). The omitted positive tail is bounded by
\(9/[4\cdot65\cdot3^{65}]\). Integer intervals at scale \(10^{30}\)
round every operation outwards. Eleven rational logarithms and nine nested
logarithms are cross-checked with a separate exact Fraction series.
No floating-point value is used for a verification gate.

Reproduce the frozen report in normal or optimized Python:

```bash
python -X utf8 -B experiments/global_closure_transport.py --compare reports/2026-11-20-global-closure/transport-report.json
python -O -X utf8 -B experiments/global_closure_transport.py --compare reports/2026-11-20-global-closure/transport-report.json
```

## 7. The first unsupported step

The completed estimates are (5), the complete original-source tail (8),
and the genuine all-return Green bound (15) for smaller observables.
The remaining concrete task is to prove (9), or another estimate strong
enough to make \(\mathcal G_N(f_0)=o(\log N)\). Neither interval sparsity,
finite reciprocal-height charge, initial negative drift, nor separate
finite termination of the enumerated sources supplies that estimate.

The new positive formulation keeps one fixed full-support atomic input
and would cover cycles as well as escape. Its missing upper bound concerns
the same arbitrarily long actual histories as before. It has not been
replaced by a finite matrix, a changing sequence of witnesses, or a
predecessor-basin density assertion.
