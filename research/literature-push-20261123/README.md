# Literature-driven attacks on complete cancellation and actual-source closure

23 November 2026. Parent commit:
a9b23dcee61a4b65a63aa4e7ca653d875a405037.

This checkpoint proves a full numerical cancellation bound for an explicit
family with **arbitrarily many cyclic coefficient patterns**, and formalizes
its decisive arithmetic in Lean. It also applies multipoint rationality
and implicit renewal theory to two current closure routes.

**Full Collatz remains OPEN.** The new cycle theorem covers the stated
family; the analytic routes retain explicit source and arithmetic-germ
hypotheses. No new universal candidate, unrestricted cycle exclusion or
same-source collision upper is claimed.

## 1. Start from the latest actual gaps

The parent checkpoint contains the whole-repository research map. This
pass refreshed the 30 most recently updated all-state PR records and
directly inspected the changed interfaces in PR175, PR176, PR177, PR180
and PR182. The [snapshot](../../reports/2026-11-23-literature-push/REPOSITORY_SNAPSHOT.json)
and lane ledgers pin full commits, paths, claim ranges and inspection
scope. PR descriptions were orientation; mathematical claims use the
pinned source files. This was not a new proof audit of every old branch.

Three attacks ran in parallel:

- **Complete cycle arithmetic:** retain the entire numerical denominator
  after every structural polynomial cancellation.
- **Arithmetic analytic continuation:** use the actual binary value as
  a possible second interpolation center, with all arithmetic-germ
  requirements retained.
- **Actual boundary comparison:** determine what the canonical
  trace-weighted fibre requires from a finite random-model conditioning.

The shortcut map is
\(T(n)=n/2\) on even integers and \(T(n)=(3n+1)/2\) on odd integers.
The odd map is \(U(n)=(3n+1)/2^{v_2(3n+1)}\).
Every ordinary source mentioned below is a positive integer. Rational
cycles are explicitly distinguished from ordinary integer cycles.

## 2. A complete numerical exclusion with unbounded pattern count

The [full proof](arithmetic/FULL_NUMERICAL_SEPARATION.md) starts from the
two-pattern family in PR185, Section 8 of CYCLOTOMIC_ZERO_FIBER.md at
39ba48e6a8af781193e28c679ea8ab64663c3aa6. That source computed the complete
polynomial residual and left its final numerical gcd unresolved.
This checkpoint settles that gcd and generalizes the family to any
finite number of disjoint congruence patterns.

Choose \(b\ge1,\ a-b\ge2\), with \(X=2^a>Y=3^b\), and put \(V=2^b\).
Choose \(k\ge2,\ r\ge k\), pairwise coprime \(n_1,\ldots,n_k\ge2\),
and distinct representatives \(0\le s_i<r\). With \(L=r\prod_i n_i\),
set

\[
c_j=1+\sum_i\mathbf1_{\{j\equiv s_i\pmod{rn_i}\}}=2^{e_j}.
\]

The supports are disjoint, so \(e_j\in\{0,1\}\). The actual shortcut
word has one positions

\[
d_{bj+t}=aj+t+e_j,\qquad 0\le j<L,\quad0\le t<b.
\]

The written proof establishes its legality, primitive period, positive
rational realization, and ordinary integer realizations of the full
finite word. Choosing the finite integer realizer above the rational
fixed point \(C/D\) makes it descend after the word. It is not an
integer cycle.

Put

\[
K=X^r-Y^r,\qquad
R_i=\frac{X^{rn_i}-Y^{rn_i}}K,\qquad R=\prod_iR_i,
\]
\[
B=\frac K{X-Y}R+
\sum_iX^{s_i}Y^{rn_i-1-s_i}\prod_{j\ne i}R_j.
\]

After the **complete polynomial gcd**, the residual denominator and
numerator are exactly

\[
D_{\rm pol}=KR,\qquad C_{\rm pol}=(Y-V)B.
\]

The decisive new arithmetic is

\[
\gcd(R_i,R_j)=1\ (i\ne j),\qquad \gcd(R_i,XY)=1,
\]
\[
B\equiv X^{s_i}Y^{rn_i-1-s_i}\prod_{j\ne i}R_j
\pmod{R_i}.
\]

The surviving residue is a unit at every factor \(R_i\). Therefore

\[
\boxed{\gcd(B,R)=1,\qquad
\gcd(D_{\rm pol},C_{\rm pol})\mid K(Y-V).}
\]

This includes prime powers shared by \(K\), \(R\), and \(Y-V\).
No factor-subset estimate, radical or other-conjugate norm replaces
the full numerical gcd.

Writing \(S=\sum_i(n_i-1)\), the final reduced denominator satisfies

\[
\boxed{
q>D_{\rm pol}^{\,1-(r+1)/(rS)}
\ge\sqrt{D_{\rm pol}}>1.
}
\]

Hence **every member of this family is excluded from positive integer
closure**, for all stated parameters.

The number of patterns and primitive period are unbounded. The fraction
of original polynomial degree retained is

\[
\frac{1+\sum_i(n_i-1)}{\prod_i n_i},
\]

which can tend to zero, while the fraction of the residual denominator's
logarithm surviving the final numerical cancellation tends to one.
The family also admits arbitrary prescribed rational-orbit floors and
slopes approaching the critical slope, by varying the embedding
parameters. These facts prevent the proof from depending on a fixed
period, pattern count or small-value cutoff.

The full global step remains a bound for arbitrary coefficient profiles.
Their overlapping factors and multiple surviving residues need not have
the unit-residue structure above.

### Lean scope

[HomogeneousRepunits.lean](rigidity/lean/HomogeneousRepunits.lean)
proves the full strong-divisibility identity

\[
\gcd(U_m(P,Q),U_n(P,Q))=U_{\gcd(m,n)}(P,Q)
\quad\text{if }\gcd(P,Q)=1,
\]

for the literal homogeneous sum
\(U_n(P,Q)=\sum_{j<n}P^jQ^{n-1-j}\).
The needed repunit coprimality is derived.

[PacketGCD.lean](rigidity/lean/PacketGCD.lean) then formalizes the actual
finite-pattern numerator and derives its coprimality from the base and
index hypotheses. Its final theorem is

**CollatzLiterature.PacketGCD.full_numerical_gcd_dvd**.

It proves the complete displayed numerical gcd divisibility for an
arbitrary finite index set. The full word construction and exact
cyclotomic polynomial gcd remain reviewed written mathematics.
They are not silently included in the formalization claim.

## 3. Arithmetic geometry reaches a strict two-center criterion

For one unchanged ordinary source, define

\[
x_k=T^k(n),\quad e_k=x_k\bmod2,\quad
p_k=\sum_{j<k}e_j,\quad
B_n(z)=\sum_{k\ge0}\frac{e_kz^k}{3^{p_{k+1}}}.
\]

The exact affine identity gives \(B_n(2)=-n\) in the binary completion.
Its real value is not identified with that binary value.

The [scalar theorem](rigidity/SCALAR_BOUNDARY_AND_SECOND_CENTER.md)
applies Bost--Chambert-Loir's primary rationality theorem:

> If \(p_k/k\to\rho\), then \(B_n\) is rational, or its individual
> convergence circle \(|z|=3^\rho\) is a natural boundary.

A local continuation increases the complex conformal radius. The
ternary radius can then be chosen so the adelic product is strictly
larger than one, giving rationality. This concerns one scalar source
under a density limit, not merely a norm boundary for a whole family.

The central attempt adds the actual Taylor germ

\[
J_n(t)=B_n(2+t)\in\mathbb Q_2[[t]].
\]

**Jet hypothesis J** requires every coefficient to be rational, all
coefficients to lie in one ring \(\mathbb Z[1/M]\), and positive
convergence radii at infinity and all primes dividing \(M\). The entire
binary germ is retained.

The original two-center proof treats critical density. The
[general-density addendum](rigidity/GENERAL_DENSITY_JET.md) proves:

> For a positive ordinary source with a limiting parity density,
> J holds if and only if its ordinary orbit is eventually periodic.

The implication uses Chambert-Loir--Noûs's primary multipoint
rationality theorem. A single binary disc joins the centers zero and
two, contributing the positive off-diagonal value \(\log2\).
For a complex radius above two, the new proof removes a small hole
around the second center and bounds its capacity loss by two
maximum-principle comparisons. The product of the two diagonal losses
has limiting upper bound

\[
\bigl(\log(3^\rho/2)\bigr)^2
\le(\log(3/2))^2<(\log2)^2.
\]

This supplies a strict positive potential-game value for every limiting
density, including those above the critical value.

**J remains unproved for an arbitrary source.** The value \(-n\) supplies
only its constant coefficient. The first unknown derivative is already
an arithmetic question; a full integral analytic germ requires more.
Eventual periodicity would still leave the unrestricted nontrivial-cycle
question.

The same lane records two exact tests of shorter routes. Deflating the
known binary zero has total convergence-disc product at most one.
[Finite rational filters](rigidity/FINITE_FILTER_TEST.md) have the
subexponential common-denominator property needed by the tested
Pólya--Carlson criterion only when the actual source is already
eventually periodic. These tests do not construct J.

## 4. Renewal theory makes the actual fibre's depth cost quadratic

The [boundary proof](boundary/CANONICAL_FIBRE_DEPTH.md) retains the precise
joint real/ternary iid model used in the latest Fourier work. Its real
coordinate satisfies the fair affine recurrence

\[
R\overset d=AR'+B,\qquad
(A,B)=(1/2,0)\text{ or }(3/2,1/2).
\]

Applying the checked one-child implicit-renewal theorem of
Jelenkovic--Olvera-Cravioto gives

\[
\lim_{x\to\infty}x\,\mathbb P(R>x)=\frac1{\log(27/16)}.
\]

The upstream canonical ordinary fibre is a trace-weighted Cesaro limit.
For depth \(m\), its finite approximating measure is

\[
\eta_m^q(dR)=3^m\nu(dR,\ Y\in q+3^m\mathbb Z_3),
\qquad
\overline\eta_M^q=\frac1M\sum_{m=1}^M\eta_m^q.
\]

Each measure retains its trace mass; it is not normalized separately.

On one original escaping spine \(q_j=U^j(q_0)\), the exact reversed
prefix back to \(q_0\) forces canonical boundary mass at a fixed fraction
of \(q_j\). The finite lower bound keeps the actual correction
\(\Lambda_j\). The uniform conclusion additionally retains the
source-qualified input \(\inf_j\Lambda_j>0\).

Compare the measures \(h(q_j)\mu_{q_j}\) and
\(\overline\eta_M^{q_j}\) in the one fixed scaled bounded test
\(f(R/q_j)\) specified in the proof. Comparing the original-prefix
lower bound with the model's \(1/x\) tail proves that approximation
with discrepancy \(o(q_j)\) in this test requires

\[
\boxed{\frac{3^M}{M}\gtrsim q_j^2,\qquad
M\log3-\log M\ge2\log q_j-O_{q_0}(1).}
\]

For positive weights \(w_m\) summing to one, the corresponding necessary
budget is \(\sum_m w_m3^m\gtrsim q_j^2\); the extra \(1/M\) belongs
to Cesaro averaging. The normalized-law corollary separately retains its
trace upper bound.

This is a necessary depth payment for the actual comparison. It supplies
neither a sufficient depth nor a frequency-dependent error bound.
Fixed-root weak convergence is not promoted to a uniform moving-root
Fourier theorem. The same-source collision upper required for an escape
contradiction remains open.

## 5. Evidence and remaining work

The [report index](../../reports/2026-11-23-literature-push/README.md)
collects full source pins, exact finite controls, mathematical reviews,
and build receipts.

All 22 new theorem declarations across the two arithmetic modules were
compiled by the author and again by an independent reviewer in separate
fresh output directories. The axiom audits report only propext,
Classical.choice and Quot.sound. Builds used Lean 4.34.1, compiler commit
5045d0056413266e57c625dcd7c365b10e377c52, with autoImplicit=false and
warningAsError=true, and mathlib
d13f23b723b8a846827a245b89c10fc7d3f11612.

Existing mathlib dependency objects were reused. The old proof corpus
was not rebuilt. The analytic results, root-of-unity argument and
ordinary word realization have written review boundaries.

The repository's integrity gate runs separately on the clean complete
checkout of the new exact commit. Its receipt verifies that execution
boundary; it is not a proof of the mathematical claims.

The strongest next obligations remain concrete: extend complete
arithmetic separation beyond the disjoint-pattern class; construct the
actual arithmetic germ or a different universal candidate; or prove a
same-source boundary comparison after paying its full depth and
normalization costs.
