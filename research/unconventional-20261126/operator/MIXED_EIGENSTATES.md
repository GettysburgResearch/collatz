# Dense mixed components with exact summable slope modes

**Status.** PROPOSED written theorem. It rules out an attempted proof by excluding atomic conformal probabilities throughout the compact product. The ordinary positive diagonal remains a separate arithmetic restriction.

Use $\mathbb Z_2\times\mathbb Z_3$ with a forward shortcut branch selected by its first coordinate, and inverse branches as in [OP-D2](HYBRID_DESCENT.md). Each directed edge carries its usual forward principal slope $c_E=1/2,c_O=3/2$. On an acyclic component rooted at $v_0$, write $P(v)$ for the product along the unique reduced walk from $v_0$ to $v$.

## OP-M1. Exact mixed modes for almost every ternary companion

For Haar-almost every $y\in\mathbb Z_3$, the component $D_y$ rooted at $(-1,y)$ is acyclic, is dense in $\mathbb Z_2\times\mathbb Z_3$, and satisfies simultaneously for every real $s>1$
$$
                           \sum_{v\in D_y}P(v)^{-s}<\infty.         \tag{M1}
$$
Thus its slope has a proper, attained positive minimum. There are uncountably many distinct such components. They can all be chosen to have irrational ternary coordinates at every vertex.

To prove this first fix $1<s<2$. The forward orbit of the root has first coordinate $-1$, second coordinate $y_j=-1+(3/2)^j(y+1)$ and slope $C_j=(3/2)^j$. Its points are distinct except when $y=-1$, so its entire functional component is acyclic. The ancestor cone of the $j$th forward point has weighted mass
$$
                 Z_j=C_j^{-s} W_s(y_j).
$$
Indeed every legal ternary inverse word lifts uniquely in the first coordinate, its full-root product equals $C_j/C_w$, and the acyclic property precludes repeated endpoints from distinct words. The cones increase and exhaust $D_y$ by coalescence. Thus it is enough to bound $\sup_j\mathbb E Z_j$ for a Haar initial $y$.

The ternary input $y_j$ agrees with $-1$ modulo $3^j$. Any inverse prefix having examined no more than $j$ odd-letter guards is legal precisely as at $-1$, since only an odd letter loses a ternary digit. For $j\ge1$ partition every legal word at its first $j$th odd letter, if there is one. Words without that many odds contribute their exact deterministic slope at the negative signed target $-1$. For a legal frontier word $w$ ending at the $j$th odd letter, of native length $k$, let $u$ be its endpoint when started at $-1$. At the random root its endpoint equals
$$
            u+\frac{C_j}{C_w}(y+1)=u+2^{k-j}(y+1).
$$
This is Haar distributed since multiplication by 2 is a ternary unit. No independence among the frontier words is needed. The expected continuation sum is consequently $\bar W_s=\int W_s\,dm_3=(1-\lambda_s)^{-1}$ by [OP-T1](TERNARY_TRANSFER.md). Nonnegative summation permits interchange with expectation. Therefore $\mathbb E W_s(y_j)$ is at most $\max(1,\bar W_s)$ times the sum of $C_w^s$ for all legal words at $-1$ with at most $j$ odd letters.

At the negative ordinary target every inverse word consists of some initial repetitions of its odd inverse self-loop and a simple first-arrival path read backwards to a negative integer $u$. The latter path is unique for each $u$, because its genuine forward dynamics is deterministic and the only cycle in this component is the fixed point $-1$. The empty path is included for $u=-1$. Its incoming multiplier is at most $K/(1+|u|)$, by the signed simple-path distortion estimate in [OP-T3](SIGNED_TARGETS.md), also following directly from PR210's negative simple-path reciprocal sum. Summing the at most $j+1$ possible loop counts geometrically gives
$$
 \sum_{w:\,q(w)\le j} C_w^s
   \le K_s(3/2)^{sj}\sum_{u<0}(1+|u|)^{-s}.
$$
Here the sum on the left is over scripts legal at $-1$. This proves the uniform expectation bound. At $j=0$ use the Haar integral of $W_s$ directly. Monotone convergence now gives finite total mass almost surely. Apply this argument simultaneously to a sequence of exponents in $(1,2)$ decreasing to one. Finiteness for one exponent makes the subset $P<1$ finite, and on $P\ge1$ increasing the exponent decreases the summand. This proves (M1) for all $s>1$, and also finiteness of every bounded slope sublevel.

For density, every root under consideration reaches a ternary unit after its first forward step. From any state with ternary unit $z$ the inverse even steps yield ternary phases $2^h z$ meeting every prescribed unit cylinder. Given a desired simultaneous cylinder of binary depth $a$ and ternary depth $b$, choose a positive ordinary seed representing it and follow $k\ge a$ forward letters to a ternary-unit endpoint $v$; a positive seed has an odd departure and thereafter remains a ternary unit. Let $q$ count its odd letters. Choose $h$ so that $2^h z\equiv v\pmod{3^{q+b}}$, and undo the prescribed $k$-letter script. Its source has the seed's ternary class modulo $3^b$ and its dyadic class modulo $2^k$, the latter because its affine formula has odd numerator coefficient $3^q$. This reaches the requested cylinder. Removing rational $y$ from the initial Haar set changes no full-measure assertion; rational affine maps with nonzero rational slopes preserve irrationality of the ternary coordinate. Each component is countable, so the retained uncountably many roots give uncountably many components.

## OP-M2. A conformal and spectral obstruction

On each such component the probability with atoms proportional to $P(v)^{-s}$ satisfies the exact conformal relations
$$
 \mu(EA)=2^{-s}\mu(A),\qquad
 \mu(OA)=(3/2)^s\mu(A)\quad(A\text{ in the admitted odd-inverse cylinder}).
$$
These identities hold for Borel target sets in the compact product, by summing the edge identity over their component atoms. The measure has full topological support by density while being purely atomic. Its ternary projection $\eta$ satisfies $\mathcal L_s^*\eta=\eta$, with the same $\mathcal L_s$ whose Haar integral contracts strictly for $1<s<2$. In particular an argument that required all its fixed probability measures to be nonatomic, or claimed that the Haar contraction excluded all such measures, already fails on these explicit components.

On unweighted counting $\ell^2(D_y)$ take $C_s g(v)=c(v)^{s/2}g(Tv)$ exactly as in [OP-S1](ESCAPE_SHIFT.md). Choose integer levels $t(Tv)=t(v)+1$. For every $|\lambda|=1$ the actual vector $g(v)=\lambda^{t(v)}P(v)^{-s/2}$ is square summable by (M1) and satisfies $C_sg=\lambda g$. Thus exact eigenvectors occur on dense mixed components even for all the exponents simultaneously. Their existence makes no assertion of an eigenvector on the physical positive integers. Any method using rationality of the *dyadic* coordinate alone would also include these examples: every first coordinate in the constructed components is rational and eventually reaches $-1$ under its genuine dyadic forward dynamics.
