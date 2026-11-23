# A least inverse envelope removes every ray atom

**Status: SOURCE-QUALIFIED written proof; not a Lean formalization.**
The finite excessive-envelope and uniform density inputs are those proved
in the companion `GLOBAL_RENEWAL_ATTACK.md`, with the complete-clock input
in `JOINT_CLOCK_MIXING.md`. The minimality argument below is a new
consequence, rather than an assumption that the specific Abel limit has
no atoms. The atom-removal argument has also been checked independently
in the parallel renewal attack. The ordinary fixed-target consequence in
section 5 uses the stronger population theorem `(PDU)`.

The construction preserves a uniform positive floor and removes the
actual-map atomic obstruction in `HARMONIC_RAY_OBSTRUCTION.md`. It proves
sublinearity uniformly on the entire predecessor basin of **each fixed
ordinary target**. It does not prove one upper bound uniform in a moving
target, and does not complete Collatz.

## 1. The all-positive operator and a finite obstacle majorant

On positive integers let

\[
(Pf)(q)=\sum_{\substack{e\ge1\\2^e q\equiv1\ (3)}}
 \frac3{2^e}f\!\left(\frac{2^e q-1}{3}\right),
\qquad g(q)=\mathbf 1_{3\nmid q}.
\tag{M1}
\]

Every argument of `f` is positive and odd. On odd targets these are
exactly the inverse edges of
\(U(n)=(3n+1)/2^{v_2(3n+1)}\). We work on all positive arguments,
including evens, throughout this construction.

The companion Abel argument supplies a finite nonnegative excessive
function with a uniform positive floor on odd units. It also supplies an
all-positive version directly. Alternatively, extend its odd values
\(F_o\) by \(F_e(q)=PF_o(q)\) at even `q`. If \(q=2^E r\), with
`r` odd, then

\[
F_e(q)=2^E\sum_{\substack{a>E\\2^a r\equiv1\ (3)}}
 \frac3{2^a}F_o\!\left(\frac{2^a r-1}{3}\right)
 \le 2^E F_o(r)<\infty.
\]

There is a unit odd parent with exponent at most six at every positive
unit target. Thus the extension retains a positive uniform floor after
decreasing its constant. Since `P` uses only odd arguments, it remains
excessive on odd targets and is harmonic on even targets. After one
constant rescaling, write the resulting all-positive function as `B`:

\[
                 g\le B<\infty,\qquad PB\le B.
\tag{M2}
\]

No sublinear upper estimate is used here.

## 2. A canonical least excessive majorant

Define successively

\[
V_0=g,\qquad V_{k+1}=\max(g,PV_k),\qquad
V=\lim_{k\to\infty}V_k.
\tag{M3}
\]

The maximum is pointwise. Positivity of `P` gives
\(V_k\le V_{k+1}\le B\) by induction. In particular the limit is
finite everywhere. Monotone convergence of the countable nonnegative
parent sum gives

\[
                  V=\max(g,PV),\qquad g\le V\le B.
\tag{M4}
\]

If `W` is any nonnegative excessive function with `W>=g`, induction in
(M3) gives `V_k<=W`, hence `V<=W`. Thus `V` is the **least excessive
majorant** of the fixed obstacle `g`, and is independent of the choice of
`B` used to prove finiteness. At multiples of three, `V=0`.

## 3. Minimality removes every positive simple-ray atom

Let \(q_0,q_1,q_2,\ldots\) be a simple infinite inverse ray of positive
odd units. Thus its nodes are distinct and, for positive integer
exponents \(e_j\),

\[
3q_{j+1}+1=2^{e_j}q_j.
\]

Put

\[
\omega_0=1,\qquad
\omega_j=\prod_{i<j}\frac3{2^{e_i}},\qquad
a_j=\omega_jV(q_j).
\tag{M5}
\]

Excessivity implies \(a_{j+1}\le a_j\). The affine edge equation gives
\(\omega_jq_j\le q_0\). Distinct positive integers tend to infinity
along a simple ray, so \(\omega_j\le q_0/q_j\to0\).

Suppose that \(a_j\downarrow a>0\). Choose `J>=1` so large that
\(\omega_j\le a/2\) for every \(j\ge J\). Define a function on
**all** positive integers by

\[
h(q_j)=\omega_j^{-1}\quad(j\ge J),\qquad
h(q)=0\quad\text{otherwise}.
\tag{M6}
\]

In particular its even values are zero. This is a truncated spike, not
the all-positive harmonic extension used in the earlier obstruction.

On a supported odd node, the next ray node is a supported odd parent, so

\[
(Ph)(q_j)\ge\frac3{2^{e_j}}\frac1{\omega_{j+1}}
          =\frac1{\omega_j}=h(q_j).
\]

At every other point `h=0` and `Ph>=0`, including all even targets.
Consequently

\[
                              Ph\ge h.
\tag{M7}
\]

The cut parent \(q_{J-1}\), when `J>0`, acquires a positive value in
`Ph`; this sign is exactly what is needed for the subtraction below.

Set \(W=V-(a/2)h\). At a supported node,

\[
W(q_j)=\frac{a_j-a/2}{\omega_j}
       \ge\frac{a}{2\omega_j}\ge1.
\]

Elsewhere `W=V`, so `W>=g` everywhere. Also `(a/2)h<=V`; the parent
series `PV(q)` is finite. Linearity of subtraction is therefore
legitimate in each series, and (M7) gives

\[
PW=PV-(a/2)Ph\le V-(a/2)h=W.
\]

This contradicts the leastness of `V`, because `W(q_J)<V(q_J)`.
Therefore

\[
\boxed{\omega_jV(q_j)\longrightarrow0
       \quad\text{on every simple infinite ordinary inverse ray}.}
\tag{NA}
\]

The proof does not subtract the whole harmonic ray function through its
root. Cutting it sufficiently far out makes room above the unit obstacle;
the favorable subharmonic boundary sign preserves excessivity.

## 4. Harmonicization retains both the floor and absence of atoms

Let \(D_s=P^s1\), with `1` the constant function, and let
\(D_s(q)\ge c_0>0\) on units for all \(s\ge s_0\), as supplied by
the companion atom floor. Exact summation gives

\[
D_1(q)=\begin{cases}
1&q\equiv1\pmod3,\\
2&q\equiv2\pmod3,\\
0&3\mid q.
\end{cases}
\]

Hence \(V\ge g\ge D_1/2\). The decreasing sequence \(P^kV\) has a
finite limit `G` and satisfies

\[
P^kV\ge\tfrac12D_{k+1}\ge\tfrac12c_0g
\quad(k+1\ge s_0).
\]

At each fixed target, the summands are dominated by the finite series
`PV(q)`. Dominated convergence therefore gives

\[
\boxed{PG=G,\qquad \tfrac12c_0g\le G\le V<\infty.}
\tag{M8}
\]

Since `G<=V`, conclusion (NA) holds with `G` as well. Thus there is an
actual finite harmonic envelope with a uniform positive floor and no
simple-ray atoms. The atomic additions in the earlier obstruction are
excluded by this construction, without an unsupported interchange of the
Abel parameter and the ray depth.

## 5. Uniform sublinearity on each fixed ordinary predecessor basin

The unit-source population theorem `(PDU)` supplies an absolute `c>0`
such that every
positive unit `b` has at least `cX/b` positive odd unit predecessors below
`X`, once `X>=Cb`. Write `Pred(b)` for this actual predecessor set.

### 5.1 A uniform reciprocal bound along simple nonperiodic paths

Consider a finite simple inverse path of odd units
\(q_0,q_1,\ldots,q_d\), with \(q_1,\ldots,q_d\) nonperiodic;
\(q_0\) is permitted to be periodic. At each \(q_i\), `1<=i<d`, select a short
unit odd parent \(b_i\ne q_{i+1}\), with exponent at most six. At
\(q_d\), select any short unit odd parent. Then

\[
                         b_i<\frac{64}{3}q_i.
\]

The sets \(\operatorname{Pred}(b_i)\) are pairwise disjoint. Indeed,
after the first hit of one branch, a deterministic forward orbit follows
the displayed path through the next lower node and cannot enter a
different off branch. Reentry from below would make one of
\(q_1,\ldots,q_d\) periodic,
which is excluded here.

For this finite family, let `X` tend to infinity after exceeding all of
its individual onset bounds. Applying `(PDU)` and disjointness gives

\[
\sum_{i=1}^d\frac1{b_i}\le\frac1c,
\qquad
\boxed{\sum_{i=1}^d\frac1{q_i}\le\frac{64}{3c}.}
\tag{M9}
\]

The constant is independent of the length, heights, and root of the
nonperiodic path. This is a finite-family counting argument; it does not
assert countable additivity of natural density.

For its inverse weight \(\omega_d\), the exact edge identities give

\[
\frac{\omega_dq_d}{q_0}
 =\prod_{i=1}^d\left(1+\frac1{3q_i}\right)^{-1}
 \ge \exp\left(-\frac13\sum_{i=1}^d\frac1{q_i}\right)
 \ge \exp\left(-\frac{64}{9c}\right)=:\kappa>0.
\tag{M10}
\]

Thus a cylinder's weighted value controls the ordinary normalized value:

\[
                  \frac{V(q_d)}{q_d}
           \le\frac{\omega_dV(q_d)}{\kappa q_0}.
\tag{M11}
\]

### 5.2 Heavy cylinders form a finite tree

Fix a positive odd unit root `q`. For each finite inverse word `w`, let
its cylinder weight be

\[
                    m(w)=\omega_wV(q_w).
\]

Excessivity says that the sum of the children's weights is at most the
weight of their parent. In particular each level has total weight at
most `V(q)`, and weights decrease under extension.

For any \(\varepsilon>0\), retain the cylinders of weight at least
\(\varepsilon\). This is a prefix-closed tree with finitely many
children at each vertex: a finite parent sum cannot contain infinitely
many summands at least \(\varepsilon\). If its depths were unbounded,
the elementary finitely branching tree argument would give an infinite
ray all of whose weights are at least \(\varepsilon\), contradicting
(NA).

For a nonperiodic root all inverse histories are simple. For a periodic
root, an infinite inverse history either eventually exits its finite
cycle and thereafter is simple, or stays on that cycle forever. In the
second case its multiplier per full cycle is

\[
\lambda=\prod_{n\text{ on the cycle}}\frac{3n}{3n+1}<1,
\]

so the cylinder weights also tend to zero. Thus the same contradiction
applies at every positive odd unit root.

The heavy tree therefore has bounded depth. Each level contains only
finitely many heavy cylinders, so the **whole** heavy tree is finite.
It follows that, as ordinary source values tend to infinity through
ancestors of this fixed root, their first-hit cylinder weights tend to
zero uniformly. This deals with bounded-depth sources having very large
exponents as well as with sources whose path depth tends to infinity.

If `q` is nonperiodic, combine this with (M11). If `q` is periodic, a
first-hit path has only a bounded initial reverse prefix on its fixed
cycle, followed by nonperiodic nodes. That finite prefix contributes a
positive root-dependent factor to (M10), and the rest has the same
absolute lower bound \(\kappa\). We obtain

\[
\boxed{\frac{V(n)}n\longrightarrow0
\quad\text{as }n\to\infty\text{ through positive odd unit ancestors
of any one fixed positive odd unit }q.}
\tag{BUE}
\]

The same conclusion holds for `G<=V`. Restricting to ancestors of a
fixed even target gives a subset of the ancestors of its odd part, so
the statement includes every fixed positive unit target. Multiples of
three have zero envelope value and add no obstruction.

## 6. The global boundary that remains

For each fixed target, (BUE) controls the full ordinary ancestor basin,
including all of its marked predecessors. This is substantially stronger
than decay along one dyadic ray or one chosen inverse branch. It removes
the previously exhibited atomic obstruction canonically while retaining
the positive floor.

The cutoff in (BUE) still depends on the fixed target. A forward orbit
that continues to distinct larger targets is not contained in the
predecessor basin of any one of those targets. Nor is the collection of
all ordinary components known to have one finite set of roots. A
compactness argument that silently identifies these moving roots would
assume the missing global control.

The next unsupported step is therefore a bound uniform over the moving
marked targets in `GLOBAL_ARITHMETIC_ATTACK.md`, or a separate argument
that confines all such targets to finitely many of the fixed basins.
No such step is claimed here, and no convergence axiom has been added.
