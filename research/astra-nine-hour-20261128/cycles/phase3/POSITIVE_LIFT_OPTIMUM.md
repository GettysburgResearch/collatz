# The exact optimum over positive physical monomial lifts

**Proposed elementary theorem, followed by a source-qualified numerical extension.** For the complete positive sum of odd physical monomials, arbitrary independent representatives in the formal period lattice give exactly the minimum rotated affine numerator as their numerical optimum. At sufficiently large positive clocks, the same optimality applies to any prospective sub-determinant certificate using numerical congruences and positive two-three-smooth integers. The latter assertion uses Corvaja–Zannier. Signed polynomial identities can produce different certificates.

## Every common-cleared formal lift

Fix a mixed word of length $n$, proper weight $u$, and positive determinant $D=2^n-3^u$. Set $U_i=\sum_{j<i}b_j$. Its odd monomials have exponent vectors $(i,-U_i)$ in the full period lattice
$$ \mathcal L=\mathbb Z^2/\mathbb Z(n,-u). $$
This keeps the torsion even when $g=\gcd(n,u)>1$. A common-cleared formal lift consists of nonnegative integer pairs $(A_i,B_i)$ on odd clocks for which
$$                   (A_i,B_i)=(i,-U_i)+v\quad\text{in }\mathcal L   \tag{1}$$
with one common translate $v$. Arbitrary independent choices of representatives are permitted. Subtracting the coordinatewise minima gives an admissible common clearing. In fact when both minima equal zero the resulting sum is coprime to six: the $A_i$ are distinct modulo $n$ and the $B_i$ distinct modulo $u$, so the least exponent of either prime occurs once.

Write $C_k$ for the raw numerator of the word rotated to begin at chronological cut $k$, so its actual positive rational starting value is $x_k=C_k/D$. Then
$$ \min_{\text{formal lifts (1)}}\sum_{i:b_i=1}2^{A_i}3^{B_i}
                      = \min_k C_k =D\min_k x_k.                    \tag{2}$$
To prove the lower bound reduce each $A_i$ to its residue $r_i$ in $[0,n)$, adding $u\lfloor A_i/n\rfloor$ to $B_i$. All exponents stay nonnegative. Each replacement of $n$ twos by $u$ threes decreases its integer monomial because $2^n>3^u$. By (1), $r_i$ is the distance in $[0,n)$ from a single chronological cut $k$ to $i$. For that cut, the canonical numerator exponents are $(r_i,s_i)$, with $s_i=u-1$ minus the number of odd steps strictly before $i$ in that rotated lap. They obey (1) with a common translate of their own. Indeed the rotated prefix count changes by $u$ precisely on wrapping. Since the $r_i$ coincide, the second exponents of the reduced lift differ from the $s_i$ by one integer constant: a vector in $\mathbb Z(n,-u)$ with first coordinate zero is zero. The last odd position has $s_i=0$, so that constant is nonnegative. The reduced sum is therefore $3^b C_k$ for $b\ge0$. Conversely the canonical numerator at a minimizing cut is an allowed lift. The minimum physical phase is odd, since an even phase is followed by its smaller half. Hence both exponent minima are zero at this optimal cut.

## The separate optimal largest effective height

Suppose additionally that $g=1$, $u>1$. Put $v=n-u$, $T=\langle u,n\rangle$ and $f=un-u-n$. The elementary symmetry $j\in T$ if and only if $f-j\notin T$ holds for every integer $j$. Indeed write $j=a u+b n$ with $0\le a<n$ uniquely; then $j\in T$ is exactly $b\ge0$ while $f-j=(n-1-a)u+(-1-b)n$. If $I$ is a lower-bounded cofinite $T$-ideal and $F(I)$ its largest missing integer (negative integers included), this symmetry gives
$$ H+I\subseteq T \ \Longleftrightarrow\ f-H\notin I,\qquad
           \min\{H:H+I\subseteq T\}=f-F(I).                         \tag{3}$$
Indeed a failure is equivalent to $f-H\in I+T=I$.

Let $E$ be the set of normalized odd departure heights and $S$ the actual semimodule with conductor $c$. By the [physical odd-boundary identity](../phase2/SEMIGROUP_BOUNDARY.md), $E-v=S\setminus(S+u)$, and every element of $S$ lies on the $+u$-ray from a unique member of that set. Thus $E+T=v+S$, with $F(E+T)=v+c-1$. We also have $\max E=n-1+c$ by the leading term of $O=z^v[u]_zJ$, including $J=1$. A common shift allowing nonnegative monomial representatives is exactly an $H$ with $H+E\subset T$, since the full relation between the two generators is $(n,-u)$. Equation (3) gives the exact optimum
$$        \min_{H+E\subset T}\max_{h\in E}(h+H)=n(u-1).             \tag{4}$$
For $u=1$ the only odd term can be translated to zero and (4) likewise holds. At $\delta=n\log_3 2-u>0$, every nonnegative representation $A u+B n=h+H$ has $\log_3(2^A3^B)=(h+H+A\delta)/n$. Thus every lift has some monomial at least $3^{u-1}$. In particular this exceeds $D$ for $0<\delta<\log_3(4/3)$. For a signed boundary with support $E'$ the semigroup formula in (3) still gives $f+\max E'-F(E'+T)$ as the least maximum effective height. It gives no comparable lower bound for the absolute signed sum.

## When actual modular relations have linear exponent height

Let $\Lambda_D$ be the numerical relation lattice consisting of $(a,b)\in\mathbb Z^2$ with $2^a3^b=1\bmod D$. Fix any constant $C>0$. Along any sequence with $n\to\infty$, $0<u<n$ and $\log D\ge\eta n$ for fixed $\eta>0$, eventually
$$ \Lambda_D\cap\{|a|+|b|\le Cn\}
             =\mathbb Z(n,-u)\cap\{|a|+|b|\le Cn\}.                 \tag{5}$$
All sufficiently long positive clocks satisfy the determinant growth condition by the [two-logarithm separation](../CONTRACTING_CALENDARS.md). The threshold in (5) is ineffective here.

**External input.** Take $S=\{\infty,2,3\}$ and the two rational $S$-units $X=2^n3^{-u}$, $Y=2^a3^b$. Their logarithmic heights are bounded by $C'n$ for a fixed $C'$ depending only on $C$. At primes outside $S$, the negative log-absolute-value sum of the simultaneous congruences $X-1,Y-1$ is at most $-\log D$. The omitted local summands are nonpositive. For any fixed $\epsilon<\eta/C'$, Corvaja–Zannier, Corollary 1 (equivalently Proposition 2, inequality (2.8)), therefore permits only finitely many multiplicatively independent pairs. Their convention is $\log^- t=\min(0,\log t)$. Each fixed $X$ determines $n,u$ by its valuations, so finitely many pairs give finitely many clocks. This is a number-field Subspace Theorem input. [Corvaja–Zannier, author manuscript, Corollary 1 and Proposition 2](https://arxiv.org/pdf/math/0311030) · [Published article](https://doi.org/10.1007/s00605-004-0273-0)

For every remaining pair, multiplicative dependence over the rationals and the independence of two and three put $(a,b)=k(N,-U)$, where $n=gN,u=gU$ and $(N,U)=1$. Let $A=2^N,B=3^U$. The element $A/B$ modulo $D=A^g-B^g$ has order exactly $g$. Its $g$th power is one, and for every $0<j<g$ the nonzero integer $A^j-B^j$ is strictly between zero and $D$. Hence $g\mid k$, proving (5). The case $Y=1$ gives $(a,b)=(0,0)$ directly.

**Numerical certificate consequence.** Suppose an arbitrary common unit $\lambda\bmod D$ and positive ordinary two-three-smooth integers $w_i=2^{A_i}3^{B_i}$ at the odd clocks satisfy
$$ w_i\equiv\lambda\,2^i3^{-U_i}\pmod D,\qquad \sum w_i<D. $$
All exponents $A_i,B_i$ are nonnegative and $O(n)$ because $w_i<D\le2^n$. Compare every $i$ to one fixed odd position. The common unit disappears, giving a vector in $\Lambda_D$ of norm $O(n)$, uniformly over all pairs and words. By (5) every such vector eventually belongs to $\mathbb Z(n,-u)$, so the weights satisfy (1). Equation (2) now gives $\min x_i<1$. Conversely $\min x_i<1$ supplies the canonical smooth lift with sum below $D$. Thus, at all sufficiently large positive clocks, even arbitrary numerical smooth representatives give a sub-determinant positive certificate precisely when the physical minimum is already below one. Arbitrary nonsmooth positive residues and signed polynomial multiples are outside this assertion.

**Finite distinction.** For the primitive word $1100$, $n=4,u=2,D=7$, the formal optimum is five. The raw terms $3,2$ can instead be multiplied by the common unit five modulo seven and represented by the smooth integers $1,3$. Their sum is four. Thus extending exact formal numerical optimality to every small clock by mere definition of the selected root would be false. The [exact controls](positive_lift_controls.py) check 6,544 rotations of 608 positive necklaces, 288,834 independent zero/one-lap mixtures, and 352 Frobenius optimizations through length twelve.
