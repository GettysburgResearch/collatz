# The actual all-clock resolvent retains ordinary component mass

**Status: source-qualified written deductions, with the elementary scalar
kernel identified separately for Lean replay. Full Collatz remains OPEN.**
The new result is an exact asymptotic identity for the original positive
source law, retaining every source pair and allowing independent meeting
clocks. It upgrades the fixed-clock collision identity in PR185 to an
ordinary-component identity. A separate second-order pole retains all
possible nontrivial cycles.

The purpose is to attack the missing global step using the spectral
interpretation of actual ordinary transport. A bounded or decreasing energy
does not close that step. The calculation below identifies precisely the
boundary energy that must vanish, and shows why averaging the clock alone
does not make it vanish.

## 1. Exact ordinary objects and the imported harmonic reference

Use the accelerated odd map

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}
\]

on the positive odd ternary units \(\mathcal O^*\). It preserves this
state space. Let \(N\) be the units **not themselves on a periodic
orbit**. They can be preperiodic. On \(N\), ordinary transport is
killed when it enters a periodic state:

\[
(Lb)(q)=\sum_{\substack{x\in N\\U(x)=q}}b(x),\qquad q\in N.
\tag{A1}
\]

There is no reweighting in \(L\). In particular \(L^k b(q)\) sums
the original masses of the sources at that actual endpoint and clock.

The reference imported from PR185 is a positive function \(\nu\) on
\(N\) with

\[
L\nu=\nu,\qquad
\frac{\gamma}{q}\le\nu(q)\le A<\infty
\quad(q\in N),\qquad \gamma>0.
\tag{A2}
\]

Its exact source is PR185, commit
`276be8154f4e867acc0230466b34d9cb224aacf5`,
`research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`,
equations (11)--(15), with the positive floor supplied by its harmonicized
potential. This is a written, source-qualified analytic input. Its
population and finite-envelope dependencies remain those stated there;
this packet neither re-proves their analytic input nor installs it as a
Lean axiom. Every theorem below is valid for any actual reference satisfying
(A2). The upper constant may be taken as that source's \(203/(3c)\).

For an escaping component \(\mathcal C\), the actual values
\(\nu(U^j x)\) increase, because \(U^j x\) is one parent of
\(U^{j+1}x\). Thus

\[
C_{\mathcal C}:=\lim_{j\to\infty}\nu(U^j x)
\quad\hbox{satisfies}\quad
0<\nu(x)\le C_{\mathcal C}\le A.
\tag{A3}
\]

It is independent of \(x\) within that ordinary component: two such
orbits share a tail after possibly **different** finite clocks. This is
the component capacity already constructed in PR185, not a new existence
claim. An escaping component here contains no eventually periodic source.

## 2. A source class large enough to contain the original law

For a nonnegative source mass \(a\) on \(N\), put

\[
S(a)=\sum_{x\in N}\frac{a(x)}{\sqrt{\nu(x)}}.
\tag{A4}
\]

We assume \(S(a)<\infty\). This implies finite total source mass,
since \(\nu\le A\). It is stronger than finite collision energy,
and it is proved below for the original \(n^{-4}\) source law; it is
not an unproved regularity premise in that application.

Let

\[
\mathcal E_\nu(b)=\sum_{q\in N}\frac{b(q)^2}{\nu(q)},
\quad
B_r a=\sum_{k\ge0}r^kL^k a\quad(0<r<1),
\quad
C_J a=\frac1J\sum_{0\le k<J}L^k a\quad(J\ge1).
\tag{A5}
\]

The resolvent sums **all ordinary odd clocks**. It is not the induced
first-return resolvent, nor a replacement by a logarithmic window law.
The killing convention in (A1) remains in force throughout sections 2--5.

### A-1: uniform renormalized energy bounds

\[
\boxed{
(1-r^2)\mathcal E_\nu(B_ra)\le S(a)^2,
\qquad J\mathcal E_\nu(C_Ja)\le S(a)^2.
}
\tag{A6}
\]

**Proof.** The orbit of a source, until its first periodic state, has no
repeated values. Every surviving endpoint \(U^k x\) has reference
mass at least \(\nu(x)\). Thus a unit source at \(x\) contributes
at most

\[
\mathcal E_\nu(B_r\delta_x)
\le\frac1{\nu(x)}\sum_{k\ge0}r^{2k}
=\frac1{\nu(x)(1-r^2)},
\quad
\mathcal E_\nu\left(\sum_{k<J}L^k\delta_x\right)
\le\frac J{\nu(x)}.
\tag{A7}
\]

The triangle inequality in the actual weighted \(\ell^2\) space
and (A4) prove (A6), first for finite supports and then for increasing
finite source sets. Equivalently, apply Cauchy--Schwarz to each exact
source-pair kernel and sum its dominating product. This also proves the
finiteness of every quantity asserted finite in (A5). QED.

These bounds include the actual collisions. They do not estimate collision
pairs by independent draws from another law.

## 3. Exact asynchronous residues

Write \(a(\mathcal C)=\sum_{x\in\mathcal C}a(x)\) for an
escaping component's entire original mass. Define

\[
\Gamma(a)=\sum_{\mathcal C\text{ escaping}}
\frac{a(\mathcal C)^2}{C_{\mathcal C}}.
\tag{A8}
\]

### A-2: the Abel and Cesaro limits have the same component residue

\[
\boxed{
\lim_{r\uparrow1}(1-r^2)\mathcal E_\nu(B_ra)
=\lim_{J\to\infty}J\mathcal E_\nu(C_Ja)
=\Gamma(a)\le S(a)^2.
}
\tag{A9}

**Proof, keeping both physical clocks.** Expand each squared endpoint
mass before summing over endpoints. Nonnegative summation gives

\[
(1-r^2)\mathcal E_\nu(B_ra)
=\sum_{x,y}a(x)a(y)K_r(x,y),
\tag{A10}
\]

where

\[
K_r(x,y)=(1-r^2)
\sum_{\substack{k,l\ge0\\U^kx=U^ly\in N}}
\frac{r^{k+l}}{\nu(U^kx)}.
\tag{A11}
\]

If the two trajectories never intersect, this is zero. If their common
tail is finite before it enters a cycle, only finitely many endpoint pairs
occur, so the kernel tends to zero. If they belong to one escaping
component, choose the first common point \(z=U^p x=U^q y\).
Injectivity before periodicity gives exactly

\[
K_r(x,y)=r^{p+q}(1-r^2)
\sum_{j\ge0}\frac{r^{2j}}{\nu(U^jz)}.
\tag{A12}
\]

By (A3), \(1/\nu(U^jz)\to1/C_{\mathcal C}\). The elementary
Abelian lemma for a bounded convergent sequence gives the limit
\(1/C_{\mathcal C}\). One can prove that lemma by separating a
finite initial segment from a tail whose terms are uniformly within any
prescribed error of their limit; the geometric weights sum to one.
The factor \(r^{p+q}\) tends to one. This is where asynchronous
meeting clocks disappear, with their finite offsets retained until the
limit is taken.

For the Cesaro kernel the exact common-tail expression is

\[
K_J(x,y)=\frac1J
\sum_{0\le j<J-\max(p,q)}\frac1{\nu(U^jz)}.
\tag{A13}
\]

A negative or zero upper bound means an empty sum. The ordinary Cesaro
lemma gives the same limit \(1/C_{\mathcal C}\). A finite common
tail again contributes zero in the limit.

The source-pair Cauchy--Schwarz bound from (A7) is

\[
0\le K_r(x,y),K_J(x,y)
\le\frac1{\sqrt{\nu(x)\nu(y)}}.
\tag{A14}
\]

Its product with \(a(x)a(y)\) has total sum \(S(a)^2\), so dominated
convergence applies to every original source pair. Grouping those pairs
by their ordinary escaping component yields exactly (A8), proving (A9).
This does not require a uniform bound on meeting clocks or a finite number
of components. QED.

The result is stronger than grouping only simultaneous mergers. In PR185's
fixed-time energy limit, two sources meeting at different clocks can remain
in different synchronous classes forever. Here they contribute their full
cross term \(2a(x)a(y)/C_{\mathcal C}\). The accompanying
[operator note](../operator/WOLD_CHANNELS.md) identifies those clock classes
as the bilateral-shift coordinates; its spectral result explains this
zero-frequency residue.

## 4. The full original \(n^{-4}\) law is admissible

For an arbitrary positive integer \(n\), remove all initial factors of
two to obtain \(o(n)\). Define the first odd-unit projection

\[
\pi(n)=
\begin{cases}
o(n),&3\nmid o(n),\\
U(o(n)),&3\mid o(n).
\end{cases}
\tag{A15}
\]

It is an actual finite orbit point, is a positive odd ternary unit, and
obeys \(\pi(n)\le2n\). The only inequality needed is
\(U(o)\le(3o+1)/2\le2o\). Every odd unit satisfies \(\pi(n)=n\).

Push the original law through this **fixed actual map**:

\[
\mu=\sum_{n\ge1}n^{-4}\delta_n,
\qquad
a(q)=\sum_{\pi(n)=q}n^{-4}.
\tag{A16}
\]

For the nonperiodic part \(a_N\), the floor in (A2) gives

\[
\begin{aligned}
S(a_N)
&=\sum_{\pi(n)\in N}\frac{n^{-4}}{\sqrt{\nu(\pi(n))}}\\
&\le\sqrt{\frac2\gamma}\sum_{n\ge1}n^{-7/2}
\le\frac7{5}\sqrt{\frac2\gamma}.
\end{aligned}
\tag{A17}
\]

The final inequality is the elementary integral estimate
\(\sum n^{-7/2}\le1+\int_1^\infty t^{-7/2}dt=7/5\).
Every collision in \(\pi\) remains in the first equality; no source
weight becomes an endpoint weight.

### A-3: an actual all-source, all-clock bound and its exact limit

\[
\boxed{
(1-r^2)\mathcal E_\nu(B_ra_N),\quad
J\mathcal E_\nu(C_Ja_N)
\le\frac{98}{25\gamma},
}
\tag{A18}
\]

and both expressions tend to

\[
\boxed{
\sum_{\mathcal C\text{ escaping}}
\frac{\bigl(\mu\{n:\pi(n)\in\mathcal C\}\bigr)^2}{C_{\mathcal C}}.
}
\tag{A19}
\]

This limit is strictly positive whenever an escaping source exists.
Indeed its component contains a positive ordinary source and hence a
strictly positive original atom, while its capacity is finite. Thus a
uniform renormalized bound such as (A18) does not force absorption.

## 5. The nontrivial cycles have a different, retained pole

The killing in (A1) is useful for identifying escapes but is insufficient
for the full theorem. We now use the actual forward map killed **only at
one**. Let \(\widehat L\) push forward unchanged source masses on
\(\mathcal O^*\setminus\{1\}\), deleting a mass precisely when it
reaches one. Set

\[
\widehat B_r a=\sum_{k\ge0}r^k\widehat L^k a,
\]

where the initial mass at one is deleted. Let \(P_*\) be the union
of all positive odd cycles except \(\{1\}\), whether or not any
such cycle exists. For such a cycle \(C\), let \(p_C=|C|\) and

\[
\beta_C=\mu\{n:\pi(n)\text{ eventually enters }C\}.
\tag{A20}
\]

### A-4: the exact periodic second-order residue

\[
\boxed{
\lim_{r\uparrow1}(1-r)^2
\sum_{q\in P_*}(\widehat B_ra(q))^2
=\sum_{C\ne\{1\}}\frac{\beta_C^2}{p_C}.
}
\tag{A21}

**Proof.** For one original unit atom whose orbit enters a cycle of
length \(p\), its weighted visits to a specified cycle point are
\(r^t/(1-r^p)\) for an appropriate actual finite first hitting clock
\(t\). Hence its \((1-r)\)-scaled mass tends to \(1/p\) at every
cycle point. A source entering one or escaping contributes zero on \(P_*\).
The \(\ell^1(P_*)\) norm of each scaled unit-source vector is at most
one, so its \(\ell^2\) norm is at most one as well. Since the full
source law is summable, the series of original-source vectors converges
uniformly in that norm. We may therefore pass the limit through the source
sum. The resulting vector is \(\beta_C/p_C\) at each point of
\(C\); squaring its norm gives (A21). The argument permits infinitely
many possible cycles and arbitrarily late entrances. QED.

This is an identity about actual periodic trajectories. It neither assumes
their classification nor transfers their masses to the escape part.

## 6. One norm now distinguishes all three outcomes

Define a reference on the states killed only at one by

\[
w(q)=\begin{cases}\nu(q),&q\in N,\\1,&q\in P_*.
\end{cases}
\quad
\mathcal E_w(b)=\sum_{q\ne1}\frac{b(q)^2}{w(q)}.
\tag{A22}
\]

The definition uses the mathematical periodic/nonperiodic partition, not
an algorithm for deciding it. It is positive and finite at every state.
The nonperiodic restriction of \(\widehat B_ra\) is exactly
\(B_ra_N\). Its energy is finite by (A18); the periodic restriction
has finite energy since its total mass is at most \(\zeta(4)/(1-r)\).

### A-5: complete boundary-residue alternative

The extended limit

\[
\mathscr R=
\lim_{r\uparrow1}(1-r^2)\mathcal E_w(\widehat B_ra)
\tag{A23}
\]

exists and has the following values:

| Actual ordinary dynamics | Exact residue |
|---|---|
| Every positive source reaches one | \(\mathscr R=0\) |
| No nontrivial cycle, but at least one escaping source | \(0<\mathscr R=\Gamma(a_N)\le98/(25\gamma)\) |
| At least one nontrivial positive cycle | \(\mathscr R=+\infty\) |

For the last case, the sum in (A21) is positive because the original law
has positive mass at every integer. Multiplication by
\((1-r^2)/(1-r)^2=(1+r)/(1-r)\) then forces infinity. If that sum
is zero, there are no nontrivial cycles and (A9) supplies the remaining
limit. Every positive integer orbit is eventually periodic or has distinct
values tending to infinity, so the cases exhaust the possibilities.

This yields a cycle-sensitive closing target:

\[
\boxed{(1-r^2)\mathcal E_w(\widehat B_ra)\longrightarrow0.}
\tag{A24}
\]

No such vanishing estimate is proved here. The unconditional algebra of
the actual source-pair kernels, and the source-qualified harmonic reference,
give the explicit values a proof of (A24) must eliminate. In particular,
ordinary mean-ergodic decay of \(\mathcal E_\nu(C_Ja_N)\) is too
weak: (A9) already gives a \(\Gamma/J\) term on an escaping component.
Discarding that first-order coefficient would discard the original atom.

## 7. Literature connection, verification, and the next mathematical step

The operator-theoretic inspiration is the shift decomposition of an
isometry and its spectral channels, developed in the accompanying
[Wold note](../operator/WOLD_CHANNELS.md). Sections 2--6 above are direct
source-pair proofs: no general ergodic theorem is needed to justify a limit
or change its source law. The source bibliography and exact branch pins
are in [SOURCES.md](SOURCES.md).

`AsynchronousKernel.lean` is restricted to the scalar geometric weights,
their summability, the normalized one-path bound, and finite-clock overlap
facts stated in that module. It does not formalize the imported harmonic
reference, the infinite source-pair limit, the component decomposition, or
the cycle residue. Its actual compilation status belongs to the packet's
execution report, not to this written statement.

The next possible profound step is an **arithmetic upper bound on this
specific boundary norm**. A spectral gap for an averaged residue model,
a finite reference obtained by replacing \(\nu\), or a bound that
already kills every periodic orbit would change (A23). The kernel here is
the actual map, and its two pole orders display exactly what must survive
any successful comparison.
