# The known basin carries the entire local essential spectrum

**Status.** PROPOSED, with proofs. All vertices are ordinary positive integers. The shortcut map is $T(n)=n/2$ for even $n$ and $(3n+1)/2$ for odd $n$. Make an oriented edge $n\to Tn$ per source. Distance uses the underlying undirected multigraph. The two edges between 1 and 2 retain their separate orientations and count as a cycle of length two. Write $G_1$ for the component containing 1. A vertex belongs to $G_1$ exactly when its forward orbit hits 1: adjacent vertices have coalescing forward orbits, and this property is transitive along paths.

## OP-L1. Exact copies in the known basin

Color every vertex by its residue modulo a fixed $M=2^a3^b$, and retain edge directions. Every finite rooted ball whose induced multigraph is a tree has infinitely many exactly isomorphic colored copies in $G_1$. The copies can be chosen pairwise disjoint and outside any prescribed finite set.

First fix $n>0$, $A,B\ge0$. There are arbitrarily large $n'\in G_1$ congruent to $n\pmod{2^A3^B}$. Choose a fixed $K\ge A$ large enough that $m=T^K n$ is a 3-unit. Every positive integer eventually has an odd step, its odd image is a 3-unit, and all later iterates remain units. If $q$ steps of this prefix are odd, translation by $2^K s$ changes its endpoint by $3^q s$ for integer $s$ whenever the new source is positive. This follows by preserving the parity word one step at a time. Choose arbitrarily large $2^j\equiv m\pmod{3^{q+B}}$, with no restriction for modulus one. The powers of 2 generate the units modulo $3^h$: modulo 3 its order is 2, and $v_3(4^{3^i}-1)=i+1$ by induction using the binomial expansion. Then
$$
 n'=n+2^K(2^j-m)/3^q
$$
is positive for large $j$, belongs to the required cylinder, and reaches $2^j$ in exactly $K$ steps, hence belongs to $G_1$.

For a finite tree ball rooted at $n$, take the unique simple path from its root to each vertex. The partial maps on such a path are the two forward branches and the two inverse branches $y\mapsto 2y$, $y\mapsto(2y-1)/3$. Once the branch choices are specified, each composite is rational affine in its source with positive slope and denominator of the form $2^i3^j$. Choosing $A,B$ sufficiently large preserves every required parity, ternary congruence, branch guard and terminal color for this finite list of paths. For example, one can first prescribe the images modulo $6M$ on every path, which preserves the parity of the forward branch and the guard $y\equiv2\pmod3$ of the odd inverse. All images are positive for large $n'$.

Transport each vertex by its path. Distinct vertices have distinct affine images at $n$, so affine collisions exclude at most finitely many $n'$. Every tree edge is preserved by construction, including its orientation. For a potential extra edge between two images, the chosen forward branch on its source gives an affine equality. It failed at $n$ and excludes at most one further $n'$. The complete neighbor list of each interior vertex has already been transported, using its branch guards. These observations give the exact induced ball. Each image tends to infinity with $n'$. The cylinder construction therefore supplies the disjoint copies. A source with a genuine cycle inside its ball need not have such copies.

There is also a counting version. Fix the cylinder above and an odd or even positive good unit $w$. Select $0\le j<J$ with $2^j w\equiv m\pmod{3^{q+B}}$, where $J=\varphi(3^{q+B})$ for nontrivial modulus and $J=1$ otherwise. Use $2^jw$ in place of $2^j$. The resulting seed is at most $C(1+w)$ for a fixed cylinder-dependent $C$, reaches the good integer $2^jw$, and has at most $J$ preimages $w$ under this construction. Excluding finitely many small values and accidental coincidences, the number of copies with root at most $X$ is at least $J^{-1}\#\{w\le X/C-1:w\in G_1,\ 3\nmid w\}-O(1)$. This counts roots and does not assert that all those balls are disjoint. By OP-G1 the last counting function is at least a constant times $X^{1/4}$: the $2^k$ distinct unit ancestors of 1 at depth $4k$ all lie below $2^{4k}$. No predecessor-density hypothesis enters.

## OP-L2. Spectral transfer from a single acyclic component

A bounded self-adjoint operator $A$ on counting-measure $\ell^2$ has *local coefficients* here if there are integers $r,s\ge0$ and one fixed $M=2^a3^b$ with these properties. The matrix coefficient $A_{uv}$ vanishes for $d(u,v)>r$, including distinct components. For $d(u,v)\le r$, it depends only on the isomorphism class of the oriented, residue-colored induced ball $B_s(u)$ with the ordered vertices $u,v$ marked; take $s\ge r$. The same rule is used at every vertex. Restrictions to components are reducing. Adjacency, the counting-measure Laplacian, and bounded combinations with periodic diagonal potentials of the given moduli are examples.

For every acyclic component $C$,
$$
 \sigma(A|_C)\subseteq \sigma_{\rm ess}(A|_{G_1}).
$$
For a spectral value take finitely supported unit approximate eigenvectors in $C$, which exist by bounded self-adjointness and density. For each vector choose one rooted ball large enough to contain its support, the output $r$-neighborhood and every radius-$s$ coefficient inspection around that output. The ball is a tree. OP-L1 copies the vector into $G_1$, preserving its residual exactly and avoiding every previously chosen support. The resulting orthonormal sequence is a singular Weyl sequence. In particular a local spectral obstruction that would require an escaping component to contribute a new spectral value cannot distinguish it from the known basin.

## OP-L3. Equality of essential spectra, including infinitely many hypothetical cycles

For every $A$ as in OP-L2,
$$
 \boxed{\quad \sigma_{\rm ess}(A)=\sigma_{\rm ess}(A|_{G_1}).\quad}
$$
The following localization handles Weyl vectors spread over different components or around long cycles.

Fix $N\ge1$. Let $\mu_v=N^{-1}\sum_{j=0}^{N-1}\delta_{T^j v}$ and $\phi_z(v)=\sqrt{\mu_v(z)}$. Then $\sum_z\phi_z(v)^2=1$, and the support of $\phi_z$ is in $B_N(z)$. Along any edge the two sums telescope, giving $\|\mu_v-\mu_{Tv}\|_1\le2/N$. Thus if $d(u,v)\le r$,
$$
 \sum_z|\phi_z(u)-\phi_z(v)|^2\le\|\mu_u-\mu_v\|_1\le 2r/N .
$$
Let $D_r=\sup_v|B_r(v)|<\infty$. Cauchy–Schwarz in each matrix row and $\sum_u|A_{uv}|^2\le\|A\|^2$ give
$$
 \sum_z\|[A,\phi_z]f\|^2\le (2rD_r/N)\|A\|^2\|f\|^2 .
$$
Here $\phi_z$ also denotes pointwise multiplication. By the triangle inequality in the direct sum and $\sum_z\|\phi_z f\|^2=\|f\|^2$, some nonzero $g=\phi_z f$ for finitely supported unit $f$ has
$$
 \|(A-\lambda)g\|/\|g\|\le\|(A-\lambda)f\|+\|A\|\sqrt{2rD_r/N}.
$$

Put $K=N+r+s+1$. Each connected functional multigraph has at most one undirected cycle, which consists of a directed periodic orbit. Indeed in a finite cycle there is one edge per vertex, so all those vertices have their unique outgoing edges on the cycle. Forward coalescence along every path prevents two different periodic orbits in one component. A cycle contained in a radius-$K$ ball has length at most $2K+1$, by taking the distance on the cycle from the unique point where the center's path first meets it. There are finitely many arithmetic cycles of length $\le2K+1$: for a fixed nonempty length-$k$ parity word of weight $q$, $T^k x=(3^qx+c)/2^k$ and $2^k\ne3^q$, giving at most one periodic initial value.

For $\lambda\in\sigma_{\rm ess}(A)$, choose $N$ so that the localization error is small. The $2K+2N$ neighborhood of the union of all cycles of length at most $2K+1$ is finite. A singular Weyl sequence has vanishing norm on this finite set, so a unit finite-support approximation $f$ can avoid it with arbitrarily small residual. The localized support meets $B_N(z)$; the ball $B_K(z)$ therefore avoids every short cycle, and cannot contain a long one. It is a tree with all the coefficient information needed for $g$. Transplant to disjoint supports in $G_1$ by OP-L1, and repeat with errors tending to zero. This proves inclusion into the right side. The opposite inclusion follows by extending its singular Weyl vectors by zero.

Compact perturbations leave essential spectra unchanged. In particular this equality tolerates bounded real diagonal potentials tending to zero at infinity, added on both sides. For example $\log(Tn/n)$ is a parity-only potential plus $0$ on even inputs and $\log(1+1/(3n))$ on odd inputs. The numerical size correction thus disappears from the essential spectrum. A fixed ordinary root in a matrix element, an exact compact-defect eigenvalue, or a coefficient with genuinely nonlocal height dependence lies outside the implication of OP-L3. The theorem decides no ordinary orbit.

## OP-L4. All components, and other moduli

In the self-contained cylinder argument, the destination can be any chosen ordinary component $D$. It contains a positive 3-unit $w$ after the first odd forward step. Use $2^jw$ in place of $2^j$, with $2^j w\equiv m\bmod 3^{q+B}$. Each resulting cylinder copy now lies in $D$ because its forward orbit hits $2^jw$, which reaches $w$. Arbitrarily large $j$ remain available. The proof of OP-L3 therefore gives, for every component $D$,
$$
 \sigma_{\rm ess}(A|_D)=\sigma_{\rm ess}(A).
$$
Also $\sigma(A|_C)=\sigma_{\rm ess}(A)$ for every acyclic component $C$: use the proof of OP-L2 with $D=C$, then the displayed equality. The two statements cover different spectra.

For an optional extension to labels modulo **any** fixed positive integer $M$, use K. M. Monks's published arithmetic-progression sufficiency theorem. His Theorem 1.1 says each progression $A+B\mathbb N$ with $A\ge0$, $B>0$ meets each merging class of this exact shortcut map. Apply it to any arbitrarily far shifted tail of a cylinder whose modulus is a multiple of $M2^A3^B$ large enough to preserve all path images modulo $M$ and all branch guards. This supplies arbitrarily large representatives in any chosen component, so the tree-transplant and essential-spectrum proofs apply verbatim. This corollary invokes Monks; the explicit power-of-two construction and its quantitative count were proved only for moduli supported on 2 and 3. [Monks, Theorem 1.1](https://monks.scranton.edu/content/pubs/SufficiencyRev4.pdf)

## Sources and scope

Applegate and Lagarias studied the ordinary pruned inverse trees modulo powers of three and computed leaf-count extrema. Mori's operator-algebra equivalences ask for irreducibility of specific representations; an essential-spectrum identity for local operators does not decide irreducibility. PR193 treats additive Fourier coefficients of an invariant color, and PR200 its conditional Fourier cancellation. Those operators and hypotheses are distinct from the physical multigraph and local coefficients above. Compare the project pins and primary sources in [the packet overview](README.md).
