# Three attempts at the remaining global step

Date: 23 November 2026. Starting PR180 head:
`5e29f56f6d44669a8aa9134e5617b78d65c074c2`.

**Collatz remains OPEN.** This pass pursued coherent analytic rigidity,
entropy of the actual integer orbit, and unrestricted complete-source
replacement in parallel. The strongest positive result is an exact
identification of the canonical inverse real boundary, its critical
change of measure, and the component charge. An additional, explicitly
qualified routing input makes that boundary's support have Hausdorff
dimension one. The attempted measure comparison needed for a contradiction
still retains the original-root cost.

The repository refresh covered metadata for all 122 open PRs and targeted
reading of the latest relevant heads. It did not re-audit every branch.
[SOURCE_SNAPSHOT.json](SOURCE_SNAPSHOT.json) records the refresh;
[SOURCES.json](SOURCES.json) pins the exact inspected files, and
[LITERATURE.json](LITERATURE.json) separates used manuscript inputs from
literature that was checked without producing a closing argument.

## 1. Put the actual component and its inverse fibre in one coordinate

For the odd accelerated map

\[
U(n)=(3n+1)/2^{v_2(3n+1)},
\]

fix one hypothetical escaping component of positive odd ternary units.
All finite paths in this construction are actual ordinary integer paths.
Coalescence supplies a rational homogeneous multiplier and coordinate

\[
\chi(Un)=\frac3{2^{v_2(3n+1)}}\chi(n),\qquad
y(n)=n/\chi(n),\qquad
y(Un)-y(n)=\frac1{3\chi(n)}.
\]

The established actual-path reciprocal bound makes every forward limit
the same finite number \(b_E\). On the existing two-sided canonical
path law \(\Pi_E\), the backward limit

\[
Z=\lim_{r\to-\infty}y(Q_r)
\]

exists and satisfies \(0<a_E\le Z\le b_E\). Its support is exactly
\(\overline{y(E)}\), a compact perfect set with both endpoints present.
In particular \(Z\) is nonconstant. Writing \(s_E=\mathbb E Z\),
the full path survival product is \(Z/b_E\), and the normalized
component charge is

\[
F_E=1-s_E/b_E.
\]

The ordinary inverse law from a vertex is the whole-path law conditioned
to pass through that vertex. The critical inverse law is exactly its
\(Z\)-size bias. Thus the limiting normalized critical real fibre is

\[
\widehat\mu_\infty^G
=\operatorname{Law}(1-Z/b_E)
\quad\text{under }(Z/s_E)\,d\Pi_E.
\]

This identifies the previously separate charge and real-fibre objects:

\[
\boxed{
F_E=1-\left(\int\frac{d\widehat\mu_\infty^G(t)}{1-t}\right)^{-1},
\qquad
F_E-\int t\,d\widehat\mu_\infty^G(t)
=\frac{\operatorname{Var}(Z)}{b_Es_E}>0.}
\]

The distinct trace fibre used in PR178 is retained as a further bounded
positive tilt; it is not silently substituted for this \(G\)-fibre.

Using the **Paper 37 v4** count of actual routes with common valuation
total, the note also proves

\[
\dim_H\operatorname{supp}\operatorname{Law}(Z)=1.
\]

The construction repeats \(R_b\) legal blocks with multiplier
\(X=(4/3)^b\), where \(R_b\) has order \(X/\sqrt b\).
Integer endpoint spacing and bounded real offsets give Frostman exponents
\(\log R_b/\log X\to1\). This is a theorem about the support,
conditional on the stated routing manuscript input. It is not a theorem
that the canonical probability has dimension one.

The exact finite comparison to the canonical inverse law is

\[
D_{\rm KL}(\mathsf S_j\Vert\mathsf K_{q,jb})
\le\log\frac{q\nu(q)}\gamma+j\log\frac X{R_b}.
\]

The original-root term survives. At a moving escaping root it is
\(\log q+O(1)\), so the support argument does not supply the desired
same-orbit entropy lower bound before the source clock.

The companion analytic attempt deforms every edge coherently by
\(x_t(n)=n+t\chi(n)\). Its component boundary is the explicit function
\(c_E(s_E+t)/(b_E+t)\). The zero lies outside the range in which all
real vertices remain positive. Requiring even one complete forward shadow
to remain integral forces \(t=0\): its initial parameter must be
divisible by unbounded powers of two. No additional ordinary interpolation
sample is obtained.

[Full argument and exact inputs](ANALYTIC_GLUING.md).

## 2. Test the entropy contradiction with the original probability law

Let \(q_j=U^j q_0\) and \(E_j=\{Q_j=q_j\}\). These are increasing
events and \(p_j=\Pi_E(E_j)=\nu(q_j)/c_E\to1\). Choose a time
label \(J\) uniformly from \(0,\ldots,M\), then sample the whole
actual path conditioned on \(E_J\). Relative to choosing that label
independently of the same whole-path law, the exact cost is

\[
\boxed{D_{\rm KL}(\mathsf Q_M\Vert\mathsf R_M)
=\frac1{M+1}\sum_{j=0}^M\log(1/p_j)\longrightarrow0.}
\]

Data processing makes the common boundary asymptotically independent
of every observation of the supplied time label, including arbitrarily
fine ternary digits of \(q_J\). The same argument applies to the
critical size bias. Thus the real boundary may carry information as a
separate factor without forcing entropy into the actual time marginal.

For each fixed nonperiodic root, the existing fixed-basin sublinearity
also makes the largest complete-word probability tend to zero. Its
complete-path law is nonatomic and its word entropy tends to infinity.
This supplies no rate at moving roots and no nonatomicity conclusion for
the real boundary pushforward, where different paths can overlap.

The physical normalized fibre is \(1-Z/y(q_J)\), however, and its
dilation depends on \(J\). Its known weak convergence does not extend
that independence assertion to arbitrary moving resolutions. The note
keeps this distinction explicit.

The alternative attempt imports the bulk stationary real/ternary affine
law and conditions on the moving ordinary integer cylinder. Existing
uniform scalar and joint traces permit a simultaneous depth
\(m_k=k+O(1)\) at which its cylinder probability is comparable to
\(q_k3^{-m_k}\). The selection cost is therefore

\[
m_k\log3-\log q_k+O(1)\ge k\log2-O(1).
\]

Even after conditioning on the real-height shell first, the cost remains

\[
m_k\log3-2\log q_k+O(1)\ge k\log(4/3)-O(1).
\]

These use the actual growth bound and preserve the source clock. Applying
the inspected Paper 9 shell moment estimate and Paper 19 geometry does
not remove this cost. The resulting inequality is compatible with the
actual orbit. A same-root trace comparison at an earlier precision, or
a suitable estimate on the physical moving fibre, remains missing.

[Full conditioning and entropy argument](ENTROPY_RIGIDITY.md).

## 3. Replace an entire source prefix by its complete inverse language

For a cut vertex \(v\) in the supplied complete source certificate, let
\(\mathcal C_3(v)\) contain every positive odd integer that reaches
\(v\) using gaps in \(\{1,2,3\}\), with no length limit. If the
deleted prefix contains a gap four, its removal pays for any word in
this entire language and any new initial exponent at most three at a
strictly smaller full multiset grade. The literal complete tail and
original target are retained.

Consequently, the existing joint bad-query reduction would force

\[
\boxed{x\in\mathcal C_3(v)\Longrightarrow16x+1<t.}
\]

This gives a finite complete cut at each such source position. Exact
unit-tree counting, height and harmonic-flow boundary identities are
derived. The flow identity puts its boundary mass on gaps at least four;
it does not place a large source inside the cheaper cluster.

An unrestricted adjacent-cluster coercivity claim is refuted by an
all-length family of actual complete convergent certificates. A separate
control stays within the bounded-four source domain: the complete census
of first-hit sources with at most two fours has **1371** elements. It
produces a true minimum-grade, maximum-source capturing interval at
\(t=2^{51}-1\), with the source floor and every literal prefix
contracting. Yet deleting through the internal \(37\to7\) gap four
leaves only \(\mathcal C_3(7)=\{7,9\}\); the best powered replacement
is 72 and cannot capture the original target.

The target itself descends at shortcut time 138 and reaches one at 384.
It is therefore not a bad query. The control isolates what the structural
source conditions alone cannot force, without claiming to refute the
full conditional descent frontier.

[Full source argument](GLOBAL_SOURCE_SYNTHESIS.md) ·
[Exact checker](check_global_source.py) ·
[Frozen output](global-source-control.json).

## Evidence and the remaining mathematical task

Two new public Lean declarations check the coherent-edge algebra and
the exact finite normalization, reciprocal moment and variance identities.
They compile in fresh output under pinned Lean and Mathlib, with warnings
as errors and a separate complete public-theorem axiom audit. The finite
reconstruction theorem permits signed weights; the probability
interpretation additionally needs positivity. No infinite construction,
external manuscript theorem or global convergence statement is supplied
as a Lean assumption.

The three proof notes have independent in-session reconstruction reviews.
The exact integer control passed normal and optimized Python with
identical output and verified complete closure, not a truncated search.
These are distinct evidence levels from the complete-checkout repository
integrity gate.

[Lean inventory](THEOREMS.json) ·
[Lean source](lean/FibreReconstruction.lean) ·
[Verification scope](../../reports/2026-11-23-high-variance/VERIFICATION.md).

The unproved global step is still a successful legal descent of the
original target, or an actual-source measure estimate excluding escape.
The analytic component here is nonperiodic; it supplies no exclusion
of nontrivial positive cycles. This checkpoint records the direct
attempts and their exact deductions, not a completion of either task.
