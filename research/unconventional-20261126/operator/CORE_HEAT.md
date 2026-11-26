# The pruned core and the ordinary heat kernel

**Status.** PROPOSED, with proofs. These statements concern the unweighted undirected counting-measure Laplacian of the shortcut graph defined in [the local-spectrum paper](LOCAL_SPECTRUM.md). Each oriented edge supplies one undirected conductance of size one. Thus the two edges between 1 and 2 give conductance two. Simple random walk chooses an incident edge uniformly with this multiplicity. The heat semigroup below instead uses rate one per incident edge.

## OP-G1. Expansion on the units, arbitrarily long paths off the units

Put $U=\{n>0:3\nmid n\}$. This set is forward invariant. Each vertex $u\in U$ has the predecessor $2u$ in $U$. There is a second unit predecessor $(2u-1)/3$ exactly at $u\pmod9\in\{2,8\}$; denote those branching vertices by $B$. At $u\equiv5\pmod9$ the odd predecessor exists but is a multiple of three; call these attachment vertices $H$. Every vertex outside $U$ belongs to precisely one half-line
$$
 h,\qquad m=(2h-1)/3,\qquad 2m,\qquad 4m,\ldots,\qquad h\in H .
$$
Here $m$ is an odd multiple of three. The edge to $h$ points from $m$ toward $h$. No vertex on the open half-line has another predecessor. This is the usual inverse-tree pruning, retained here in the full undirected operator.

The doubling cycle modulo nine is $1,2,4,8,7,5$. From any unit, the first branching residue occurs after $j\in\{0,1,2,3\}$ doublings. The first attachment occurs after at most five. Thus the fourth unit inverse level contains at least two vertices: take the all-even inverse word and a word using the odd inverse at the first branch, then double to complete depth four. Distinct inverse words at fixed depth yield distinct sources by determinism of forward parity. At $u=7$ the depth-three level is the singleton $\{56\}$ and the fourth level has exactly two vertices. Consequently
$$
 |(T|_U)^{-4} S|\ge 2|S|
$$
for every finite $S\subset U$, since different endpoints have disjoint fibers. Both the uniform depth four and its factor two are sharp for that assertion.

For the undirected edge boundary on the induced multigraph of $U$ we have
$$
 |\partial S|\ge |S|/7 .
$$
Indeed summing indegree minus outdegree on $S$ gives $|B\cap S|=\#\mathrm{entering}-\#\mathrm{leaving}\le|\partial S|$. Starting from $v\in S$, follow doubling to its first branch. If the segment remains in $S$, charge that branch; each branch receives at most four charges. Otherwise charge the first boundary edge in the segment; each such edge receives at most three charges because doubling is injective and the segment has length at most three. Hence $|S|\le4|B\cap S|+3|\partial S|$. The factor $1/7$ is a lower bound; its optimality is not asserted. This argument applies in every component, including the cycle $1\leftrightarrows2$ with its edge multiplicity.

Let $L_U$ denote the unit graph Laplacian, $L$ the full Laplacian, and write $g=1/294$. Then $L_U\ge gI$ componentwise. To see this, for finitely supported $f$ apply the boundary inequality to superlevel sets of $|f|^2$ and integrate. Cauchy–Schwarz bounds the resulting edge variation by
$$
 \left(\sum_{\{x,y\}}|f(x)-f(y)|^2\right)^{1/2}
 \left(\sum_{\{x,y\}}(|f(x)|+|f(y)|)^2\right)^{1/2}
 \le \langle f,L_U f\rangle^{1/2}\sqrt6\,\|f\|_2 .
$$
The left side of the coarea bound is $\|f\|_2^2/7$. Density proves the assertion.

Every full component contains a unit and a half-line. On disjoint intervals of increasing length along one such line, normalized cutoffs of $e^{ij\theta}$ have residual $O(\text{length}^{-1/2})$ for the eigenvalue $2-2\cos\theta$. The four possible error sites are the endpoints and their exterior neighbors. The cutoffs form a singular Weyl sequence. Thus $[0,4]\subseteq\sigma_{\rm ess}(L)$ on *each* component. Already the good component contains $3,6,12,\ldots$ attached to 5. An interval of $\ell$ vertices far out on a half-line has exactly two boundary edges, giving zero edge-isoperimetric constant in the full component.

## OP-G2. Elimination of the half-lines

View $P:\ell^2(\mathbb N_{>0})\to\ell^2(U)$ as restriction and $P^*$ as zero extension. Write $D$ for multiplication by $1_H$ on $\ell^2(U)$, and $G=L_U^{-1}$. For positive $z$,
$$
 P(L+zI)^{-1}P^*=\left(L_U+zI+s(z)D\right)^{-1},\qquad
 s(z)=\frac{\sqrt{z(z+4)}-z}{2}.
$$
For input supported on $U$, the square-summable solution on a half-line attached at $h$ has value $\rho^j f(h)$ at distance $j$, where $\rho=(2+z-\sqrt{z(z+4)})/2$ solves $\rho+\rho^{-1}=2+z$. The only other independent solution grows. Summing squares also across all half-lines is valid since $\sum_{j\ge1}|\rho|^{2j}<\infty$. Substitution at $h$ adds $(1-\rho)f(h)$ to the core equation. Invertibility on $U$ follows from OP-G1.

The exact threshold coefficient on the core is $Q=GDG$. In operator norm,
$$
 \boxed{\ P e^{-tL} P^*=\frac{Q}{2\sqrt\pi}\,t^{-3/2}+O(t^{-5/2})\quad(t\longrightarrow\infty).\ }
$$
For the proof put $z=w^2$ on the principal square-root branch. The right-hand resolvent is norm analytic for small $w$, since $s(w^2)=w\sqrt{1+w^2/4}-w^2/2$ and $L_U\ge gI$. Its series begins $G-wQ+O(w^2)$, with self-adjoint real Taylor coefficients (it is self-adjoint for small real $w$). The resolvent identity above continues from $z>0$ into the local slit plane by analyticity. For small $\lambda>0$, take $z=-\lambda+i0$ so $w=i\sqrt\lambda$. The negative imaginary part divided by $\pi$ is
$$
 \frac{\sqrt\lambda}{\pi}Q+O(\lambda^{3/2})
$$
in operator norm; terms of even degree in $w$ contribute zero imaginary part. Scalar Stieltjes inversion for each vector and polarization give this density for the compressed projection-valued spectral measure on a fixed interval $(0,\delta)$. More explicitly, the boundary values are continuous in operator norm there, so integration on compact subintervals identifies the measures by the usual Poisson-kernel approximation. There is no compressed atom at zero because the positive resolvent remains bounded as $z\downarrow0$. The part at $\lambda\ge\delta$ has norm at most $e^{-t\delta}$. Integrating the density and using $\Gamma(3/2)=\sqrt\pi/2$ proves the expansion. The conclusion is a norm estimate **after core compression**. The full semigroup has norm one.

## OP-G3. What the heat coefficient measures

Set $J=I-L_U/3$. This is a symmetric entrywise nonnegative kernel: at a degree-two vertex it has a holding weight $1/3$, and each edge contributes $1/3$ toward its other endpoint. Positivity of the entries gives $|\langle f,J f\rangle|\le\langle |f|,J|f|\rangle$. The upper form bound from OP-G1 yields $\|J\|\le\tau=1-g/3<1$. Therefore $G=(1/3)\sum_{k\ge0}J^k$ in norm. For unit vertices in the same component at distance $d$,
$$
 3^{-d-1}\le G(u,v)\le g^{-1}\tau^d.
$$
The lower bound uses one geodesic walk and the upper bound omits powers below $d$. Different components have zero Green entry.

In particular $Q(u,v)>0$ exactly when $u,v$ share a component. For a common-component pair one has the uniform estimates
$$
 3^{-d-12}\le Q(u,v)\le
 \frac{\tau^d}{9}\left(\frac{d+1}{1-\tau}+
                 \frac{\tau}{(1-\tau)^2}\right).
$$
For the lower bound take an attachment $h$ within five doublings of $u$ and retain $G(u,h)G(h,v)$. For the upper bound expand $GDG$ in powers $J^k D J^\ell$; only $k+\ell\ge d$ contribute, and each matrix element is bounded by $\tau^{k+\ell}$. Thus every diagonal entry of the leading heat coefficient $Q$ is at least $3^{-12}$. Its positivity on the diagonal and its universal exponent hold in every component. In contrast the entry at the two specified ordinary vertices $1,n$ is positive precisely for a good unit $n$. For such $n$, $d(1,n)$ equals its number of shortcut steps to first hit 1: deleting the redundant parallel edge yields a tree and the forward segment is its unique simple path.

Consequently a polynomial lower bound $Q(1,n)\ge c(1+n)^{-C}$ on *all* units, with $c,C>0$, is equivalent to the stronger assertion that every positive integer hits 1 in $O(\log(2+n))$ steps. For the forward implication, positivity gives membership in the good component and the upper exponential bound, absorbing the linear prefactor into a slower exponential, bounds its distance. To extend to odd multiples of three and their doubles, take $v_2(n)$ halving steps and one odd step to a unit at most $2n$. The reverse implication uses the displayed lower bound. Neither the polynomial lower bound nor universal positivity has been established.

Read [the inverse hitting probability](IMPEDANCE.md) for the explicit arithmetic cocycle on the physical route toward a marked good vertex.
