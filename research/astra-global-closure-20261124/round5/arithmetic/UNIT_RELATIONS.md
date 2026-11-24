# A moving algebraic unit on two physical clocks

**PROPOSED written theorem.** Here $A,p\ge1$ need not be coprime. Write $D=2^A-3^p$. Fix a number field $K$. For any unit $\theta$ of its ring of integers, any integers $r,s$ with $\delta=As+pr\ne0$, and $v=2^r3^s$, define
\[
 W_\theta=\frac1{[K:\mathbb Q]}
 \sum_{\mathfrak q\mid D}\min\{\operatorname{ord}_{\mathfrak q}D,
                  \operatorname{ord}_{\mathfrak q}(v-\theta)\}\log N\mathfrak q,
 \qquad
 R_\theta=\sqrt{|\delta|+(A+p)(1+h(\theta))}.
\]
The sum runs over all prime ideals over rational primes dividing $D$. They lie away from two and three, so $v$ and $\theta$ are units at every contributing place. The height $h$ is the absolute logarithmic Weil height. Uniformly over these data,
\[
                     W_\theta=o_K(R_\theta)\quad(R_\theta\to\infty).           \tag{1}
\]
Both the algebraic unit and the exponents may move. The number field stays fixed.

For example let $F\in\mathbb Z[T]$ be monic, of uniformly bounded degree, with constant term $\pm1$ and splitting field contained in $K$. Suppose $A=O(p)$, $|\delta|=O(p^2)$ and each root has height $O(p)$. Then
\[
                   \log\gcd(|D|,|\operatorname{num}F(2^r3^s)|)=o_K(p),     \tag{2}
\]
uniformly when the indicated degree and implicit bounds are fixed. Here $\operatorname{num}$ is the numerator in reduced rational form. Indeed for each prime valuation $\min(a,\sum_j b_j)\le\sum_j\min(a,b_j)$. Sum over all roots with multiplicity, then over all $\mathfrak q\mid D$. Normalization by the field degree reproduces the entire rational gcd on the left before this bound. The denominator of $F(v)$ is supported at two and three. In (2), transversality also ensures $v\ne\theta$: a rational algebraic unit is $\pm1$, whereas $r,s$ cannot both be zero.

## Two independent small unit equations

Let $w=1+h(\theta)$. In the Euclidean plane spanned by the following vectors in $\mathbb R^3$, take their integral span
\[
               (A,-p,0),\qquad (r,s,-w).
\]
Its area is $\sqrt{\delta^2+w^2(A^2+p^2)}\le R_\theta^2$, by the Gram determinant. A vector $(b,c,wd)$ from this lattice determines the $S$-unit $U=2^b3^c\theta^d$, for the fixed places of $K$ over $2,3,\infty$. Its height is at most a fixed absolute multiple of the Euclidean length. At each contributing $\mathfrak q$, put $m_{\mathfrak q}=\min(\operatorname{ord}_{\mathfrak q}D,\operatorname{ord}_{\mathfrak q}(v-\theta))$. The units $2^A3^{-p}$ and $2^r3^s\theta^{-1}$ are both one modulo $\mathfrak q^{m_{\mathfrak q}}$. Thus every lattice unit satisfies the same congruence, with signed exponents allowed. Projection onto the first two coordinates has nonzero determinant $\delta$. Two independent lattice vectors give two multiplicatively independent $U,V$: any rational-integer dependence, evaluated at primes above two and three, forces the same linear dependence on the two projected vectors. This also proves $U\ne1$ for every nonzero vector. These statements concern the actual truncated prime powers before summing.

Take successive Euclidean minima $\lambda_1,\lambda_2$. The planar bound $\lambda_1\lambda_2\ll R_\theta^2$ follows directly by completing a primitive shortest lattice vector to a basis and subtracting a multiple of it from the second. The latter's parallel projection has size at most $\lambda_1/2$; its perpendicular projection has size $\mathrm{area}/\lambda_1$. Its length is at least $\lambda_1$ by minimality, giving $\mathrm{area}/\lambda_1\ge\sqrt3\,\lambda_1/2$, and its length is at most a constant times $\mathrm{area}/\lambda_1$. This is the two-dimensional successive-minima argument.

Choose $0<\epsilon<1$. If $\lambda_1\le\sqrt\epsilon R_\theta$, the elementary height bound $W_\theta\le h(U-1)\le h(U)+\log2$ for this vector gives $W_\theta\ll\sqrt\epsilon R_\theta+1$. In the remaining case select the two independent vectors with lengths $\le\lambda_2\ll R_\theta/\sqrt\epsilon$. Outside finitely many pairs, Corvaja–Zannier Proposition 2 bounds
\[
 -\sum_\nu \log^-\max\{|U-1|_\nu,|V-1|_\nu\}
            \le\epsilon\max\{h(U),h(V)\}
\]
for multiplicatively independent $S$-units in the fixed field. Absolute values are normalized with the number-field weights absorbed. Its only positive-dimensional exceptions are subgroups through the identity; the independence above excludes them. The left side dominates $W_\theta$. For the finite exceptional pairs the same left side is bounded by a constant depending on $\epsilon,K$, since neither entry equals one. This proves $W_\theta\ll\sqrt\epsilon R_\theta+O_{\epsilon,K}(1)$ in both cases. Taking $R_\theta\to\infty$ and then $\epsilon\downarrow0$ gives (1). The argument applies the theorem to the actual units $U,V$ in a fixed group of $S$-units. It invokes no theorem with a growing field or a changing set of places. [Corvaja and Zannier, Proposition 2, arXiv:math/0311030v2, pp. 7–8](https://arxiv.org/pdf/math/0311030v2)

## Factors of the physical carry

Use the Laurent polynomial
\[
 N(X,Y)=\sum_{i<p}X^{E_i}Y^{-i},\qquad
 L(X,Y)=X^A Y^{-p}-1 .
\]
At $(2,3)$ we have $C=3^{p-1}N(2,3)$, while $L(2,3)=D/3^p$. For $P,H,J$ in $\mathbb Z[X^{\pm1},Y^{\pm1}]$ suppose $P$ divides the carry modulo $L$ and
\[
                         F(X^rY^s)=P H+L J.                       \tag{3}
\]
If $G=\gcd(|D|,|\operatorname{num}P(2,3)|)$, both terms on the right vanish modulo the complete $G$. Denominators are units there. Equation (2) therefore bounds the full contribution of this subproduct, even when the quotient by $L$ has zero divisors or the original clocks have a common factor. Repeating a root a bounded number of times is already included. A universal upper bound does not follow when $P$ leaves a complementary carry factor uncontrolled.

For the coprime-clock mask in [the main note](README.md), choose $pr+As=m$ to represent $z^m$ by $v$ modulo $D$. If $P\mid M$ and $P(X)\mid F(X^m)$, then every prime-power gcd from $P(z)$ is bounded by (2). This allows every $1\le m=O(p^2)$, arbitrarily large degrees of $P$, and a moving bounded-degree core as above. In contrast a bounded-degree subproduct of the discrepancy polynomial itself had already been treated, with all multiplicities, in PR193. Substituting a growing power can give an irreducible factor of degree comparable to $p$ or $p^2$ even if the fixed core is quadratic. We require a divisibility witness for any actual word on which this estimate is used. [PR193, 5f160a843750f209ea1251dfb01ea0b23e532fd6, §§1–3](https://github.com/GettysburgResearch/collatz/blob/5f160a843750f209ea1251dfb01ea0b23e532fd6/research/astra-ordinary-boundary-20261124/arithmetic/README.md)

The finite algebra in [ClockLattice.lean](ClockLattice.lean) includes specialization of every signed lattice combination in any commutative group, the determinant and row independence, the weighted Gram identity, specialization of a factor modulo the clock, the Apéry edge relation, reflection and the finite counting step behind (7) of the main note. The height argument, prime-ideal summations, imported diophantine theorem and asymptotic conclusions are written proofs.

## A physical quadratic-degree, non-torsion family

There are contracting coprime clocks with $p=7L\to\infty$ and $A-p\log_2 3\to0^+$. To see this, take any upper continued-fraction convergent $(h,k)$ to $\alpha=\log_2 3$ followed by its next lower convergent $(h',k')$. The latter has strictly smaller absolute error $|h'-k'\alpha|$ than $h-k\alpha$. These columns form a unimodular basis. If $7\mid k$ use the upper convergent itself. Otherwise choose $1\le t\le7$ such that $7\mid tk+k'$ and use $(A,p)=(th+h',tk+k')$. The column has coprime coordinates because $(t,1)$ is primitive in the basis, and its positive error is at most $7(h-k\alpha)\to0$. In either case for $a=A-p$ we have $\gcd(a,7L)=1$ and $a/p\to\alpha-1$.

Take $w$ to be the largest positive integer with $w\equiv a\bmod7$ and $8w\le a$, and put $m=Lw\asymp p^2$. Use the set
\[
 S=\{ia+mt:0\le i<L,\ t\in B\},\qquad B=\{0,1,3,4,5,6,9\}.
\]
Its $p$ distinct residues follow by reducing first modulo $L$ and then dividing the resulting congruence by $L$ and using that $w$ is a unit modulo seven. The set $\Delta=S+p\mathbb N_0$ is closed under $+a$. For $i<L-1$ the next point remains in the same string. At $i=L-1$, choose $t'\in B$ with $t'\equiv t+1\bmod7$. The positive jump $t'-t$ is at most eight, and the same upper bound holds when it is negative. The difference $La+m(t-t')$ is nonnegative and divisible by $p$, since $La\equiv m\bmod p$. Thus $\Delta$ is a genuine physical semimodule by (2) of the main note.

Writing $S_b(X)=1+\cdots+X^{b-1}$, the mask is
\[
     M=S_L(X^a)S_7(X^m)P(X^m),\qquad P(X)=1-X^2+X^3,
\]
since $\sum_{t\in B}X^t=S_7(X)-X^2+X^9=S_7(X)P(X)$. The first two factors divide $X^{La}-1$ and $X^{7m}-1$, both of order $O(p^2)$, so each has gcd of logarithm $o(p)$ by (5) of the main note. The final factor of degree $3m\asymp p^2$ has a fixed cubic core. This monic cubic with constant one is irreducible by the rational-root test and has a real root strictly between $-1$ and $0$. No root is torsion, since otherwise all conjugates would have modulus one. Therefore (2) of this note gives $o(p)$ for its gcd too, in its fixed splitting field. Consequently $d=|D|\exp(-o(p))$ for these complete physical words. Every proper generalized arithmetic progression has a product of geometric masks and all roots of unity. This family has a non-torsion subproduct of quadratic degree and lies outside that class. No irreducibility of the growing pullback $P(X^m)$ is needed or asserted.

The same construction allows **any fixed** $b\ge2$ and any fixed $b$-element transversal $B\subset\mathbb N_0$ modulo $b$ containing zero. Put $c=\max_{t\in B}(t'-t)>0$, with $t'$ the next residue's representative. For clocks $p=bL$, choose $w\equiv a\bmod b$ maximal with $cw\le a$; then $w\sim a/c$ and $\gcd(w,b)=1$. The same two reductions give distinct residues. At the end of a string, $La+Lw(t-t')\ge0$ and is divisible by $p$. The mask is $S_L(X^a)H(X^{Lw})$ with $H=\sum_{t\in B}X^t$. This monic integer polynomial has constant one; all its roots are units in one fixed splitting field. The full logarithmic cancellation of $H(X^{Lw})$ is $o(p)$ by (2), and the geometric factor again has order $La=O(p^2)$. The degree of the pulled-back core is $\asymp_{b,B}p^2$ when $a/p\to\log_2 3-1$.

For arbitrary fixed composite $b$, coprime clocks with $b\mid p$ and $A-p\log_2 3\to0^+$ also exist. Apply continued fractions to $b\log_2 3$, taking adjacent upper and subsequent lower convergents $(h,k),(h',k')$. Choose $1\le t\le b$ by the Chinese remainder theorem so that $A=th+h'$ is coprime to $b$. For a prime $q\mid b$ with $q\mid h$, unimodularity gives $q\nmid h'$; otherwise at most one residue of $t$ modulo $q$ is forbidden. The combination $(A,L)=(th+h',tk+k')$ is primitive, hence $\gcd(A,bL)=1$. Its error $A-(bL)\log_2 3$ is positive and tends to zero as before. The core, its splitting field and $b$ are fixed while these clocks grow.
