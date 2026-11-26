# Component abundance in every short relative interval

**Status.** Proposed arithmetic counting theorem and operator consequence. One can place polynomially many ordinary predecessors in every sufficiently large fixed-ratio interval and every fixed residue cylinder supported at 2 and 3. Thus the essential-spectrum obstruction also retains uniformly continuous functions of the actual logarithmic heights.

## OP-L5. A bounded-multiplicity annular router

Write $P(a)=\{n\ge1:T^j n=a\text{ for some }j\ge0\}$ and $P_U(a)=\{n\in P(a):3\nmid n\}$. For each $\varepsilon>0$, $A,B\ge0$ and residue $r\bmod 2^A3^B$, there are constants $c,C>0$ and $X_0$, independent of the ordinary unit target $a$, such that for $X\ge X_0$
$$
 \#\{x\in P(a):X\le x\le(1+\varepsilon)X,\ x\equiv r\bmod2^A3^B\}
 \ \ge\ C^{-1}\#\{w\in P_U(a): w\le cX\}.
$$
In particular this left side is $\gg_{\varepsilon,A,B}(X/a)^{0.38764}$ once $X/a$ is sufficiently large, by [the explicit unit-predecessor bound](HEIGHT.md). Taking maxima over the finitely many residues makes the implied constants uniform in $r$. Every ordinary component contains a unit. Every sufficiently large such annular residue window thus meets every **fixed** component, with its initial size threshold allowed to depend on that component. For a growing list of components no common initial threshold is asserted.

First route an arbitrary positive 3-unit $w$ to an ancestor near a desired size $Y$ and in a prescribed unit residue $v\bmod3^b$, increasing $b$ to at least one if needed. Put $P=\varphi(3^b)$. For each odd-run length $j\ge b$ choose $K$ so that
$$
       2^K w\equiv -1+3^j2^{-j}(v+1)\pmod{3^{j+b}}.
$$
The right side is a unit and 2 generates all these unit groups. The first constraint modulo $3^b$ fixes $K\bmod P$ solely from $w\bmod3^b$, independent of $j$. The consecutive $j$ odd inverse steps from $2^K w$ reach
$$
                   h=2^j(2^K w+1)/3^j-1 .
$$
This is a positive odd unit congruent to $v\bmod3^b$ when $K$ is sufficiently large. The intervening ancestors are positive ordinary integers and $h$ reaches $w$. Increasing $K$ by full allowed periods gives, uniformly over $w\ge1$,
$$
  \log_2 h=\log_2 w+K+j(1-\log_2 3)+o(1).
$$
Fix a desired short interval width on the $\log_2$ scale. The irrational rotation $j(1-\log_2 3)\bmod P$ admits a finite set of indices $j\ge b$ forming a net with spacing less than a quarter of this width. Translating that net by $\log_2 w+K\bmod P$ preserves its spacing. For this finite stock of $j$, one can fix a common lower bound on $K$ making the displayed error less than a quarter of the width, then solve the congruences above it within a bounded maximum $K$, uniform over $w$. Hence the logarithms of the resulting $h$ still meet the interior of any prescribed arc of that width modulo $P$. Each $h\le C_1w$ for a fixed $C_1$. For $w\le Y/C_1$ choose one and multiply by $2^{tP}$, $t\ge0$, to place $z=2^{tP}h$ in $[Y,(1+\eta)Y]$ for any prescribed fixed $\eta>0$. Its residue $v$ is preserved. The map from input anchors $w$ to selected $z$ has bounded multiplicity: $h$ is odd, so $tP=v_2(z)$ and $h$ are recovered from $z$. Only boundedly many pairs $(j,K)$ are used and the displayed formula then recovers $w$.

For the full cylinder take one positive representative $r_0\equiv r$ and a fixed native forward prefix of $d\ge A$ steps reaching a ternary unit $m=T^d r_0$. Extend until at least one odd arrow has occurred and let $q\ge1$ be the odd grade. The identity for a source in its dyadic prefix class gives
$$
                 n=r_0+2^d(z-m)/3^q,\qquad T^dn=z .
$$
It suffices to place $z$ in the unit residue $m\bmod3^{q+B}$ and in the real inverse image of $[X,(1+\varepsilon)X]$ under this positive affine formula. For large $X$ that interval contains a fixed relative-width interval at a scale comparable to $X$. Apply the preceding router. The final affine map is injective and leaves the bounded multiplicity intact. Restricting anchors to $P_U(a)$ proves the theorem.

Consequently any set containing the indicated residue slice of $[X_i,(1+\varepsilon)X_i]$ at arbitrarily large $X_i$ meets every component. Certifying such slices good would suffice for full Collatz. More generally, if the number of unverified exceptions to goodness in a sequence of these slices is $o(X_i^{0.38764})$, OP-L5 also suffices. The theorem supplies no such verification. Ordinary arithmetic-progression sufficiency and examples of sparse sufficient sets were established previously; the bound above controls every moving relative window and compares its count with the full low-height ancestor count. [Monks 2006](https://monks.scranton.edu/content/pubs/SufficiencyRev4.pdf) · [Monks, Monks, Monks and Monks, §2](https://arxiv.org/abs/1204.3904)

## OP-L6. Logarithmic height retains the same essential spectrum

In the bounded self-adjoint finite-propagation setting of [OP-L2–L4](LOCAL_SPECTRUM.md), also mark the inspected ball by the vector of actual logarithmic heights $\log n_v$ at its vertices. For each finite oriented residue-ball type, allow the coefficient to be a bounded uniformly continuous function of these marks, invariant under the finite ball isomorphisms fixing the ordered matrix sites. The same rule applies throughout, and $M=2^a3^b$ here. Then still
$$
                     \sigma_{\rm ess}(A)=\sigma_{\rm ess}(A|_D)
$$
for every ordinary component $D$. In particular even nonperiodic bounded uniformly log-continuous height profiles are admitted. This concerns the essential spectrum. An eigenvalue concentrated around a fixed small arithmetic root is outside the conclusion.

Fix one requested residual tolerance and localize as in OP-L3. The support size, its graph radius, and all coefficient inspection radii are then bounded in terms of that tolerance. A finite list of branch paths of bounded length contains only finitely many rational affine maps $n\mapsto c n+d$ with $c>0$. Hence a single mixed modulus suffices at that radius to preserve all guards and the requested discrete colors, and only finitely many exceptional positive $n$ can produce accidental affine coincidences or exceptional extra edges among the entire finite path list. The old short-cycle exclusion also removes the finitely many neighborhoods whose tree copying is unavailable. The singular Weyl vectors and their localized roots can avoid arbitrarily large fixed finite sets. OP-L5 supplies a root $n'$ in $D$ with the same mixed residue and $n\le n'\le(1+\eta)n$ for every sufficiently large source root $n$. For each inspected affine image,
$$
 \left|\log(cn'+d)-\log(cn+d)\right|
 \ \le\ \log(1+\eta)+O(1/n)
$$
uniformly on this finite list. Thus all the corresponding bounded matrix entries differ by arbitrarily little, by taking $\eta$ sufficiently small and $n$ sufficiently large. The support and output row sizes are uniformly bounded at this fixed tolerance, so the residual changes by arbitrarily little as well. Roots can escape each previously used finite support in $D$, yielding an orthogonal singular sequence. The reverse inclusion is extension by zero. Absolute-height features that vary on arbitrarily small logarithmic scales, or imposed nonlocal conditions along a whole future, remain beyond this theorem.
