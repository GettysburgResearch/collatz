# Eventual exact maxima of the fair first-arrival rows

Use the notation and the explicit source-qualified hypotheses of the [universal correction and cutoff theorem](FAIR_CLOCK_DIFFUSION.md). Let \(A_{d,m}(y)\) be the set of all positive integer starts first reaching the positive odd target \(y\) at shortcut clock \(m\) and odd grade \(d\). Put
\[
 B_{d,m}(y)=3^d2^{-m}|A_{d,m}(y)|/y,\qquad
 D(y)=\sup_{d,m} B_{d,m}(y),\qquad W_d=\sup_{y,m} B_{d,m}(y).
\]
The established cutoff bounds every row restricted to sources \(z>R\) by \(\tau(R)=|K_{1/R}|\to0\). The uniform lower bound on simple corrections is denoted by \(c>0\). All source-cutoff uses in this note also follow from the [independent uniform first-arrival argument](CLOCK_ANTICONCENTRATION.md), with \(\tau(R)\ll1/\sqrt{\log R}\). This provides a self-contained written proof of the maximizer statements below, while the stronger closed-support theorem retains its separate assumptions.

## Exact stabilization on every putative escaping component

On an escaping component let \(F(z)=\prod_{j\ge0} w(U^j u)\), where \(u\) is the odd part of \(z\), and \(P(z)=z/F(z)\). Two integer starts are *balanced* if their odd paths meet after the same number of odd departures and the same physical clock, including any initial halvings. This is equivalent to agreement at every sufficiently large grade and its physical clock. The common value of \(P\) on each such class \(G\) is denoted by \(P(G)\). Its mass is \(b(G)=|G|/P(G)\). Each class is finite because \(z\le P(G)\) for all its members. Distinct classes are disjoint. Every class disjoint from \([1,R]\) has \(b(G)\le\tau(R)\): follow all of its finitely many members to a common sufficiently late odd target at one clock and grade and take the limit in the cutoff estimate. Consequently, over *all* escaping components, there are only finitely many classes of mass at least any given \(\epsilon>0\).

For an odd \(y\) in the escaping component \(C\), let \({\rm Anc}(y)\) be the positive integer starts reaching \(y\), including \(y\) itself and initial even sources. Each nonempty first-arrival row at \(y\) is exactly \(G\cap{\rm Anc}(y)\) for one balanced class \(G\). All row members belong to a single balanced class by the physical meeting at \(y\). Conversely, if two members reach \(y\) before their equal-grade/equal-clock meeting, their remaining odd and shortcut travel times from \(y\) to a sufficiently late common successor are identical by determinism and the absence of a return to \(y\). Subtracting these common suffix times gives equal first-arrival grades and clocks at \(y\). Thus
\[
       F(y) D(y)=\sup_{G\subset C}\frac{|G\cap{\rm Anc}(y)|}{P(G)}.      \tag{1}
\]
Indeed the contribution per source after multiplying by \(F(y)\) is \(1/P(G)\), by the ordinary multiplicative transport.

For \(C\) the maximum \(M_C=\max_{G\subset C} b(G)>0\) is attained, and there are finitely many maximizing classes. Along **any** odd forward spine \(y_n=U^n a\) of \(C\), all members of all of these finite classes reach \(y_n\) for every sufficiently large \(n\). Therefore
\[
             F(y_n) D(y_n)= M_C \quad\text{for all sufficiently large }n.  \tag{2}
\]
The maximizing rows are exactly those finitely many full classes. A proper subset of a maximizing finite class has smaller mass, and an entire nonmaximal class has smaller mass. Hence \(D(y_n)\) strictly decreases to \(M_C\) from a finite point onward.

Now suppose any escaping orbit exists and let \(M=\max_G b(G)>0\), with finite attaining family \(\mathcal G_*\) over all components. Choose any \(z_G\in G\), write \(u_G\) for its odd part, and \(y_G(d)=U^d u_G\). For every sufficiently large grade the **global** maximum is exactly
\[
               W_d=M\max_{G\in\mathcal G_*}\frac{1}{F(y_G(d))}.           \tag{3}
\]
For every escaping-target row carried by a class of mass less than \(cM/2\), (1) bounds the entire row by \(M/2\). There are only finitely many remaining classes. At all sufficiently large grades \(d\), the members of each such class have already synchronized, so its one possible row is its full row at \(y_G(d)\) with mass \(b(G)/F(y_G(d))\). Since \(F(y_G(d))\to1\), the finitely many nonmaximal masses eventually all lie strictly below \(M\). For a bounded-orbit target, choose \(R\) with \(\tau(R)<M/2\). The bounded-orbit starts below \(R\) have only finitely many possible first visits in total. An escaping start cannot hit a bounded-orbit target. Beyond the largest of the finitely many grades there is no contribution below the cutoff. This proves (3), including uniformity over bounded components. Each of the finitely many displayed contenders is strictly decreasing at every odd step, by the factor \(3y_G(d)/(3y_G(d)+1)\). Thus \(W_d\) itself is eventually strictly decreasing to \(M\). Its maximizing rows are eventually drawn from a fixed finite list of actual finite sets of starting integers.

For each fixed \(\epsilon>0\), every odd target \(y\) with \(D(y)\ge\epsilon\) lies on one of finitely many ordinary forward orbits. Indeed choose a cutoff with \(\tau(R)<\epsilon/2\) and a row with mass greater than \(\epsilon/2\). It must receive a source at most \(R\). Elementary simple-orbit packing then gives \(O_\epsilon(Y^\theta)\) such targets at most \(Y\), for the absolute exponent \(\theta<1\) in the packing estimate; finitely many bounded orbits give only finitely many targets. Along each escaping orbit the limit is (2). Accordingly
\[
                  \limsup_{y\to\infty,\ y\ {\rm odd}}D(y)
                  =\lim_{d\to\infty}W_d=M,                            \tag{4}
\]
where both limits are zero when every positive orbit is bounded. In the escape case one of the finitely many globally maximal classes supplies a spine attaining the positive limsup. Finite verification of arbitrary fixed depth does not determine which case holds.

## The extrema use finite computable rows

Every \(W_d\) is a positive rational attained by finite ordinary searches. A word of length \(m\) with \(d\) odd shortcut inputs contributes at most one start to any given target. Thus
\(B_{d,m}(y)\le3^d2^{-m}\binom{m}{d}/y\). A positive witness row exists at every \(d\) by the monotone inverse ladder at 1, taking the first odd exponent at least three and choosing a positive unit exponent at least three at every further step; \(d=0\) uses the empty path. Having found any positive row weight \(b\), enumerate \(m\) only while \(3^d2^{-m}\binom{m}{d}\ge b\), including all \(m\le 2d\). The majorant is eventually decreasing to zero, by its successive ratio \((m+1)/(2(m+1-d))\). For each remaining \(m\), only \(y\le3^d2^{-m}\binom{m}{d}/b\) can attain or exceed \(b\). Enumerate starts up to \(2^my/3^d\), or reverse the finitely many words and check first arrival.

When all orbits are bounded, the *least* start of *any* maximizing row tends to infinity with \(d\) because a bounded finite pool has finite first-visit grades. If an orbit escapes, (3) puts **every** maximizing start in a fixed finite pool for every sufficiently large \(d\). This gives a dichotomy for a computable finite sequence of witnesses. Neither a bound on the onset nor the positive lower alternative is known.

## Ordinary forward and inverse inequalities at a maximum

Suppose \(G\) is a globally maximal escaping balanced class. For \(m\ge0\), \(0\le d\le m\), write \(\omega=3^d2^{-m}\) and \(O_m(x)\) for the number of odd departures. Put
\[
  I_{d,m}(G)=\{z:T^m z\in G,\ O_m(z)=d\},\qquad
  J_{d,m}(G)=\{T^m x:x\in G,\ O_m(x)=d\}.
\]
The target here may be even. Initial or final even coasts cause no change in the ordinary grade. Every member of \(I\) has corrected height \(P(G)/\omega\), and all the members belong to one balanced class: append the fixed \(m\)-step prefixes to a sufficiently late common synchronized visit by members of \(G\). For \(J\), take a sufficiently late such visit by all of \(G\) beyond \(m\) and remove its prefixes. Its distinct members belong to one balanced class at corrected height \(\omega P(G)\). Consequently a necessary pair of sharp inequalities is
\[
          \omega\,|I_{d,m}(G)|\le |G|,\qquad
          |J_{d,m}(G)|\le\omega\,|G|.                                 \tag{5}
\]
In particular, at a supplied binary history of an individual \(x\in G\), its forward multiplier can never fall below \(1/|G|\). At one step (5) also bounds the proportion of \(G\) congruent to \(2\bmod3\) by \(2/3\), and its even proportion by \(1/2\).

Every **finite horizon** of the simultaneous inequalities (5) has a positive ordinary synchronized example all of whose starts reach 1. Fix \(L\ge1\), choose \(W\) a multiple of \(6^L\) with \(W\ge2\cdot3^L+6\cdot2^L\), and take any interval \(G=[A,A+W)\cap\mathbb Z\), \(A\ge1\). Each length-\(m\) parity word with \(d\) odd steps has a unique admissible target residue modulo \(3^d\). This follows by composing the positive inverse branches \(2y\) and \((2y-1)/3\); at a compatible odd inverse step the target is \(2\bmod3\) and the resulting positive integer is odd. The compositional numerator has leading factor \(2^m\) prime to three, and successive integrality is equivalently the final congruence modulo \(3^d\). Distinct words at the same clock and target give distinct starts. For \(m\le L\) this gives exactly
\[
               \frac{\omega |I_{d,m}(G)|}{W}=2^{-m}\binom md\le1.
\]
For \(d=0\) the distinct forward image count is exactly \(W/2^m\). For \(d>0\) every forward image is a unit modulo three, since the last odd step gives a unit and subsequent halvings preserve units. All images are in a real interval of length at most \(\omega(W-1)+(3/2)^m-1\). This follows from the affine formula \(T^m x=\omega x+b\), \(0\le b\le (3/2)^m-1\), obtained by iterating the two shortcut cases. A real interval of length \(B\) contains at most \(2B/3+2\) integer units. Since \(\omega W\ge2(3/2)^m+6\), its upper bound is at most \(\omega W\). Thus (5) holds for all \(m\le L\). By the unconditional finite-pattern first-arrival window theorem one may choose \(A\) arbitrarily large so that *every member* of this entire interval first reaches 1 at the same later physical clock and grade. Taking \(A>2^L\) keeps all starts above 1 throughout the test horizon. This proves the insufficiency of the stated finite family of inequalities, even with actual synchronized coalescence. It does not assert that every possible constraint on a maximal class is included in (5). [Unconditional finite patterns](../merger/FINITE_BLOCKS.md) · [Window result](../merger/FastBlocks.lean)

## Exact bounded replay

The complete extrema through grade 11, including ties, are in the [JSON receipt](../../../reports/astra-infinite-descent-20261127/escape/EXTREMAL_CHECKS.json). The [replay](check_extrema.py) uses periodicity modulo \(3^d\) of all-visit rows, the finite cycle subtraction and the rigorous binomial outer bound. It independently reverses each maximizing row and runs every listed source forward to its first visit. The low-vertex menu from [the elementary target theorem](HIGH_TARGET_ROWS.md) contains every computed maximizing target. Ordinary and optimized Python runs gave identical receipt bytes.

For example, \(W_9=19683/561152\) is attained twice at \(y=137\): by source 27 at clock 12, and by sources 54 and 55 at clock 13. The same two sets attain the grade-10 and grade-11 extrema at \(103\) and \(155\). All of these starts have bounded orbits. The exhaustive finite observations give no evidence of an escaping extremal class.

