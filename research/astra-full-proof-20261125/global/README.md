# Two tests for boundedness of a single ordinary Collatz trajectory

**PROPOSED.** For each fixed positive source, eventual periodicity is equivalent both to a rational dynamical representation of its heights and to a Mahler functional equation for its weighted parity series. The results also exclude finite-order, single-valued rational recurrences on any escaping trajectory. Neither representation is known for every source. Boundedness would still permit a nontrivial positive cycle.

Let \(x_0=x>0\), \(x_{n+1}=T(x_n)\), where \(T\) divides even inputs by two and sends odd inputs to \((3x_n+1)/2\). Put \(e_n=x_n\bmod 2\), \(Q_n=\sum_{j<n}e_j\), and \(E_n=n-Q_n\). A repeated height gives an eventually periodic trajectory by determinism. Otherwise all heights are distinct, and \(x_n\to\infty\).

## Finite-dimensional rational dynamics

Consider a finite-dimensional algebraic variety over a characteristic-zero field, a rational self-map \(f\), and a rational function \(g\). Suppose there is a point \(s\) such that, for every \(n\), \(s_n=f^n(s)\) and \(g(s_n)\) are defined, and \(g(s_n)=x_n\) in the field. Then the trajectory is eventually periodic. This includes models with additional hidden coordinates and arbitrary rational maps of unbounded polynomial degree. Conversely every eventually periodic trajectory has such a model, by interpolating its successor on the finite set of attained heights.

Indeed give \(S=\{s_n:n\ge0\}\) its induced Zariski topology. A subspace of a Noetherian space is Noetherian. The restriction \(S\to S\) of \(f\) is continuous, since its regular domain contains \(S\). The rational expression
\[
b(s_n)=\frac{2g(f(s_n))-g(s_n)}{2g(s_n)+1}
\]
is defined throughout \(S\) and takes exactly the actual parity value there. As a function to \(\{0,1\}\) with its finite discrete Zariski topology it is continuous. In particular the even fiber is both open and closed in \(S\). This uses positivity and characteristic zero to avoid the common affine-branch value at \(-1/2\). Poles at points outside \(S\) do not enter the argument.

An irreducible component \(C\) of \(S\) lies wholly inside or wholly outside the clopen set \((f^j)^{-1}(b^{-1}(0))\), for each \(j\). Consequently any two points in the *same* component have the same entire future parity sequence. Ordinary integers sharing \(h\) future parity bits are congruent modulo \(2^h\). This follows by backward induction through the common affine branches, canceling the odd factor three at an odd step. Taking \(2^h\) larger than both heights gives equality. Thus \(g\) is constant on each component. This remains true on intersections, where both constants must agree. Finitely many irreducible components cover \(S\), so it has only finitely many distinct observed heights. More generally the argument bounds the number of heights by the number of irreducible components of *any* Noetherian state space with a continuous update, clopen even fiber and an ordinary physical height at every state. [Formal topological and arithmetic core](RationalModel.lean)

It follows that no nonperiodic trajectory can satisfy, from any time onward,
\[
x_{n+d}=R(n,x_n,\ldots,x_{n+d-1})
\]
for a fixed \(d\ge1\) and a single rational function \(R\) defined at all subsequent tuples. Use the clock and the \(d\) consecutive states as hidden coordinates, shift the window, and evaluate the last coordinate using \(R\). This excludes every P-recursive height sequence on an escape, since a nonzero polynomial leading coefficient vanishes at only finitely many nonnegative integers. Conversely eventual periodicity gives a constant-coefficient linear recurrence on the tail, so the ordinary generating function of the heights is D-finite exactly when the trajectory is eventually periodic.

### What the actual branch equation supplies

The actual implicit quadratic relation
\[
(2x_{n+1}-x_n)(2x_{n+1}-3x_n-1)=0
\]
does hold everywhere. It gives a correspondence with both branches available algebraically. The following calculation tests whether adjoining a fixed number of previous heights makes the branch single-valued. On an injective trajectory, fix a length \(d\). A parity word \(w\) that occurs infinitely often gives the affine line
\[
L_w=\{(t,T_{w_0}(t),\ldots,T_{w_{d-1}}\cdots T_{w_0}(t)):t\in\overline{\mathbb Q}\}.
\]
Here \(T_0(t)=t/2\) and \(T_1(t)=(3t+1)/2\). Infinitely many distinct ordinary first coordinates occur on each such line, so the corresponding observed tuples are Zariski dense in it. After the last occurrence of each of the finitely occurring words, the Zariski closure of the delayed tuples is exactly the union of these lines. They are pairwise distinct because the two polynomials at the first differing letter are distinct on the nonconstant preceding affine coordinate. Each line is one irreducible component.

For every \(d\) some recurrent \(d\)-word has *both* continuations recurrently on an injective ordinary orbit. Otherwise discard the finitely occurring \((d+1)\)-words. Each remaining length-\(d\) word then determines the next letter, and a finite deterministic graph forces eventual periodicity of the word. Equality of future parity on two phases would repeat an ordinary height. Thus projections from \(d+1\) clocks to \(d\) clocks continue to branch at every depth, and the number of recurrent lines increases by at least one at each increment of \(d\). This is a statement about the changing delayed tuple of *one* orbit. It quantifies why the implicit algebraic relation alone does not provide a single-valued rational update, even though every finite delay variety has dimension one. Minimality of a bad source supplies lower bounds for ordinary heights or bases. Those inequalities do not choose an algebraic branch on a right-special word.

### Finite fits with no consistency requirement

Fix the order of a rational recurrence and a bound \(D\) for the total degrees of its numerator and denominator. Allow the clock as a variable. Suppose every finite prefix of an ordinary trajectory admits such a fit, with denominator nonzero at all its data, but allow entirely different coefficients for different prefixes. This already implies eventual periodicity.

Use a fixed monomial basis for the two polynomials. Each data point imposes one rational homogeneous linear equation on their joint coefficients. The kernels for increasing prefixes descend in a finite-dimensional space over \(\mathbb Q\) and eventually stabilize at \(V\). Allowing coefficients in any characteristic-zero extension does not change these rational matrix ranks. On \(V\), denominator evaluation at each individual data point is a nonzero linear functional. Indeed take a fitted prefix beyond stabilization containing that data point. For a rational basis \(v_0,\ldots,v_{m-1}\) of \(V\), the vector \(v_0+t v_1+\cdots+t^{m-1}v_{m-1}\) over \(\mathbb Q(t)\) satisfies every fitting equation and avoids every denominator zero simultaneously, since each evaluation is a nonzero polynomial in the indeterminate \(t\). This gives one rational dynamical representation in characteristic zero, to which the theorem applies. This argument addresses changing finite witnesses without extracting a limit of ordinary seeds.

When the predictor uses only consecutive heights, there is an explicit cost. Write its input as \((x_n,\ldots,x_{n+d})\) and target as \(x_{n+d+1}\). On any injective trajectory, a rational fit of degree \(D\) for the first \(N\) such observations must satisfy, for fixed \(d\),
\[
 D\ \ge\ \frac{N}{2\cdot 4^d}-O_{x,d}(1).
\]
To see this, discard a finite initial portion so only recurrent words and edges of the \(d\)-word graph remain. There are at most \(v=2^d\) vertices. Every consecutive \(v\) vertices on this tail include a right-special vertex, one with two recurrent successors. Otherwise these \(v\) vertices are all among at most \(v-1\) nonbranching vertices. A repeated vertex in this segment traps the infinite future on a deterministic cycle, contradicting injectivity. Some right-special word thus occurs at least \(N/v^2-O_{x,d}(1)\) times in the data. For all sufficiently large \(N\), both extensions of every right-special word have appeared in the data, even though the maximizing word can vary with \(N\).

Restrict the fitted numerator \(P\) and denominator \(Q\) to that word's line \(L_w\). The two next values along the line are affine polynomials \(A_0(t),A_1(t)\), unequal at every observed positive input. Neither \(P|_{L_w}-A_j Q|_{L_w}\) can vanish identically because the other branch occurs and its supplied denominator is nonzero. The degree of each difference is at most \(D+1\). Distinct observations of either extension give distinct roots of its difference, so at most \(2(D+1)\) observations on this word can be fitted. Combining the bounds proves the claim. For \(d=0\) there is the single empty word and both physical parities recur. The linear rate uses the absence of a clock variable. Uniformly bounded degrees are still impossible with a clock, by the previous stabilization argument.

## A scalar Mahler test without a prescribed substitution

Define the integer-coefficient formal series
\[
 F_x(z)=\sum_{n\ge0} e_n3^{E_n}z^n .
\]
Then the following statements are equivalent for every fixed positive \(x\).

1. The ordinary trajectory of \(x\) is eventually periodic.
2. \(F_x(z)\) is rational over \(\mathbb Q(z)\).
3. For some integer \(k\ge2\), \(F_x\) satisfies a scalar \(k\)-Mahler equation of any finite order over \(\mathbb Q(z)\). This means a nonzero relation \(\sum_{i=0}^d p_i(z)F_x(z^{k^i})=0\), with \(p_i\in\mathbb Q[z]\) and \(p_0p_d\ne0\).

A period of length \(L\) with \(v\) even inputs multiplies the coefficients of the tail by \(3^v\) each lap. Summing the geometric tail proves 1 implies 2. Rational functions satisfy such an equation for every \(k\), proving 2 implies 3.

For 3 implies 1, suppose instead the trajectory is injective. At \(\alpha=2/3\) the finite prefix identity reads
\[
 3x+\sum_{j<n} e_j3^{E_j}\alpha^j
    =3\frac{2^n}{3^{Q_n}}x_n
    =3x\prod_{j<n}\left(1+\frac{e_j}{3x_j}\right).
\]
The first equality follows by one-step telescoping. The second follows by multiplying the physical one-step ratios. In the dyadic field the right side in the **middle expression** tends to zero, since \(x_n\) is an integer and \(3\) is a unit. Hence \(F_{x,2}(\alpha)=-3x\). Its power series is analytic in the dyadic open unit disk, because its coefficients are integers. [Finite prefix and coefficient identities](ParitySeries.lean)

In the reals, the distinct positive heights satisfy \(\sum_{j<n}1/x_j\le H_n\), the \(n\)-th harmonic number. The last product is at most \(\exp(H_n/3)\). In particular the nonnegative partial sums at \(\alpha\) are \(O_x(n^{1/3})\), and the real radius is at least \(\alpha\). No convergence of the series at the boundary is needed. For \(0<t<\alpha\) the real sum is nonnegative. A Mahler function with this dyadic rational value would have a removable real specialization at \(\alpha\) taking the value \(-3x\), by the next argument. This contradicts positivity on approach from below.

### Transfer at a possibly singular specialization

Here is the needed statement. Let \(F\in\mathbb Q[[z]]\) be \(k\)-Mahler, and let \(0<\alpha<1\) be rational with \(|\alpha|_2<1\). Suppose its dyadic power series is analytic in a disk of radius strictly greater than \(|\alpha|_2\), and its value at \(\alpha\) is \(a\in\mathbb Q\). Then the complex meromorphic continuation of \(F\) to the unit disk is regular at \(\alpha\) and has value \(a\). At a real boundary of the original disk of convergence this concerns the meromorphic continuation. Its value gives the left limit if the series converges on \((0,\alpha)\).

Use the companion system of a scalar equation with nonzero first and last coefficients, adjoining the constant 1. It has the form \(V(z)=A(z)V(z^k)\) with \(A\) invertible over \(\mathbb Q(z)\). Its entries are the constant and finitely many iterates of \(F\). The standard analytic facts and the lifting theorem used here are in Section 4 of Adamczewski, Bell and Smertnig. Choose \(m\) so large that \(\beta=\alpha^{k^m}\) is in the ordinary and dyadic open disks of convergence of all entries, and that \(\beta^{k^j}\) avoids all poles of \(A,A^{-1}\) for every \(j\ge0\). There are finitely many nonzero forbidden points, and these powers are distinct and tend to zero. [Primary paper, Definition 4.1 and Theorem 4.3](https://adamczewski.perso.math.cnrs.fr/HeightMahler.pdf)

Iteration expresses \(F(z)-a=B(z)V(z^{k^m})\) with a rational row \(B\). Let \(h\ge0\) clear its poles at \(\alpha\), so every entry of \(D(z)=(z-\alpha)^hB(z)\) is regular there. The right side
\[
 N(z)=D(z)V(z^{k^m})
\]
is analytic near \(\alpha\) at both places. The iterated identity holds meromorphically there: clearing rational denominators gives the same formal series identity on the initial disks, followed by the usual continuation in the real or complex case. In the dyadic case all needed original sums converge at \(\alpha\) under the stated strict radius. Since \(F_2(\alpha)=a\), the Taylor coefficients of \(N\) of degrees \(0,\ldots,h\) at \(\alpha\) vanish dyadically.

Each of these coefficients is a rational linear combination of the entries of \(V^{(j)}(\beta)\) for \(0\le j\le h\). The vector of these derivatives has an invertible Mahler system: differentiating produces a block lower triangular matrix with diagonal blocks \((kz^{k-1})^j A(z)\). Derivatives of rational functions add no nonzero poles outside the existing poles. The inverse has no additional nonzero poles outside those of \(A,A^{-1}\), as follows from triangular inversion. Thus \(\beta\) is regular for this enlarged system. For each of the finitely many dyadic linear relations, Theorem 4.3 lifts it to a homogeneous formal polynomial relation that specializes to the supplied relation at \(\beta\). If its coefficients are algebraic, embed their common number field into \(\mathbb C\); all coefficients of the specialized original relation are rational. Evaluating the formal identity where the series converge at the complex place therefore gives the *same* vanishing relation there. All the Taylor coefficients through degree \(h\) of the complex \(N\) vanish. Dividing by \((z-\alpha)^h\) now gives a regular value zero for \(F-a\). This argument avoids applying a regular-point theorem to a singular input.

### An application to arbitrary automatic block codings

Choose any finite collection of length-\(L\) shortcut words, each with \(P\) odd letters, satisfying \(3^P>2^L\). Select the successive words by *any* \(k\)-automatic sequence of labels, allowing arbitrary auxiliary alphabets and codings. No positive integer realizes the resulting infinite script.

For each block write its exact update as \(2^L y=3^P x+C\) with nonnegative integer carry \(C\). Let \(C_j\) be its sequence of carries and \(G(z)=\sum C_jz^j\). The carries are a finite coding of an automatic sequence, hence automatic. Their generating series is \(k\)-Mahler. For example this follows by taking generating series of the finite \(k\)-kernel and splitting each coefficient sequence into its \(k\) decimations, the standard automatic-to-Mahler theorem cited by Adamczewski, Bell and Smertnig. The coefficients are bounded, so the series converges in the real and dyadic open unit disks. Put \(\alpha=2^L/3^P\). Telescoping the block equations gives
\[
 3^P x+\sum_{j<n} C_j\alpha^j=3^P\alpha^n x_{Ln}.
\]
For a positive ordinary realizer the right side tends to zero dyadically. The transfer theorem forces \(G(\alpha)=-3^P x\) in the reals too, inconsistent with its nonnegative coefficients. For the contracting case \(3^P<2^L\), bounded carries already bound every orbit with those blocks, hence force eventual periodicity. These conclusions apply to any tail after dropping a fixed finite prefix. [Automatic-to-Mahler background, introduction and §3](https://adamczewski.perso.math.cnrs.fr/HeightMahler.pdf)

For a concrete subcase of PR209's three-slot mask, prescribe either order of the two physical blocks 110 and 111 in each consecutive pair, selected by an arbitrary automatic word. The six-bit blocks have slope \(3^5/2^6>1\). Thus this entire family has no positive integer realizer. A general sequence of allowed three-bit blocks need not respect the pairing or have an automatic selector. PR190/194 treat binary-substitution fixed words and can allow unequal multipliers. The present application requires equal block multipliers and permits unrestricted automatic codings.

## Scope of the two tests

PR190 excludes nonperiodic fixed words of binary uniform or primitive substitutions in its physical two-block gap systems. PR194 extends the script exclusion to nonidentity non-erasing binary substitutions. Their proofs study two-variable prefix sums, reaction to substitution, and transcendence of the physical dyadic completion. The scalar test above has different hypotheses and conclusion. It applies to the fixed ordinary shortcut trajectory and an arbitrary-order equation for its weighted series, requires no substitution on a symbolic schedule, and supplies no conclusion about the transcendence of a prescribed nonordinary completion. The rational-state theorem instead has hypotheses on an update for ordinary heights. [PR190 at ba58227c](https://github.com/GettysburgResearch/collatz/tree/ba58227c5a047ff3859a148a5fdaac4fd1451e4c/research/mahler-physical-scripts-20261124) · [PR194 at b1bf1f15](https://github.com/GettysburgResearch/collatz/blob/b1bf1f151a2da8936f80d229f132d0b7539ba42c/research/astra-birth-rigidity-20261124/MAHLER_EXTENSION.md) · [PR209 parity cancellation at 2d0230aa](https://github.com/GettysburgResearch/collatz/blob/2d0230aa52d85732dbc85b5df20e30108dc1396f/research/astra-ultra-closure-20261125/machinery/PhysicalEcho.lean)

For every source, removing its first parity letter gives the exact identities \(F_{2a}(z)=3zF_a(z)\) and \(F_{2a+1}(z)=1+zF_{3a+2}(z)\). Their indices move between sources while the argument \(z\) stays fixed. The missing step is a reason, from the ordinary arithmetic of a first counterexample, for its *fixed* series to satisfy a finite dilation equation in \(z\), or for its full orbit to admit a rational dynamical representation. Neither the two source identities nor the implicit quadratic branch equation supplies this. The topological and analytic tests address escaping trajectories. Every positive cycle passes both tests, including any hypothetical nontrivial one.

## Verification

The Lean 4.34.1 kernel checked the chronological prefix identity, the coefficient formula, recovery of an ordinary height from all its parity bits, constancy on an irreducible component, and finiteness of the height range on a Noetherian state space. The rational-variety specialization, finite-fit bounds, Mahler lifting and automatic application are written proofs. The finite checker separately tested 16,384 prefixes, both positive six-bit cylinders, and exact fitting matrix ranks on the first 40 steps from 27. The latter is a finite control on a converging orbit. [Executable checks](check.py) · [Exact output](../../../reports/astra-full-proof-20261125/global/finite-check.json)
