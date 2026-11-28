# Positive evaluations and an exact denominator at macroscopic disorder

**Proposed written theorems.** Write $p=\log_3 2$, $u+v=n$, $\gcd(n,u)=1$, $D=2^n-3^u>0$. Use the [semigroup dictionary](SEMIGROUP_BOUNDARY.md). Denote the exponents of its successive nonzero boundary terms by $0=h_0<h_1<\cdots<h_{2s}$. Then $J=1-z^{h_1}+z^{h_2}-\cdots+z^{h_{2s}}$.

## A full evaluation at the physical primes

Choose integers $c_j,e_j$ with $h_j=c_j u+e_j n$. Normalize $c_0=e_0=0$ when convenient. In $\mathbb Z/D$, $z_0^{h_j}$ is represented by the positive rational $w_j=2^{c_j}3^{e_j}$. Both possible denominator primes are units. Write $\delta=np-u$. The exact identity
$$\log_3 w_j=(h_j+c_j\delta)/n                                      \tag{1}$$
shows that $w_j$ increase strictly if $\delta(\max c_j-\min c_j)<1$.

The same strict order holds, without the last numerical inequality, if $u=\lfloor np\rfloor$, $n$ is a lower record for $\{np\}$, and all $c_j$ lie in an interval of $n$ consecutive integers. Indeed a potential reversal between $h<h'$ must have $c-c'=k\in[1,n-1]$. Positivity of $h'-h=n(e'-e)-ku$ gives $e'-e\ge\lceil ku/n\rceil$. At a lower record $\lfloor ku/n\rfloor=\lfloor kp\rfloor$, since $\{kp\}>\delta>k\delta/n$; neither $ku/n$ nor $kp$ is integral. Consequently $e'-e>kp$ and $w'>w$.

Multiply all weights by $L=2^{-\min c_j}3^{-\min e_j}$, a positive rational unit modulo $D$. The resulting $Lw_j$ are positive integers. Under either strict-order condition their alternating sum $K$ satisfies
$$0<K\le Lw_{2s},\qquad d=D/\gcd(D,K).                               \tag{2}$$
The first bound follows by grouping adjacent increasing terms either from the left or the right. The equality follows from the additive-order formula. Thus all of $D$ survives outside one explicitly bounded ordinary integer. In particular, in any fixed family of signed boundary exponents $c_j u+e_jn$ with fixed ordered pairs $(c_j,e_j)$ and $\delta\to0$, the positive $K$ is one fixed integer for every sufficiently late member. The actual order-ideal and endpoint hypotheses matter, since an arbitrary signed polynomial need not describe a permissible boundary.

## A family changing a positive fraction of every mechanical schedule

Put $l=2v-u$, $r=u-v$. Whenever $0<l<r<v<u$, take as holes precisely the integers $l,\ldots,r-1$. This is a valid ideal since all holes are below $\min(u,v)$. Directly, in the full modulus,
$$z_0^l=(3/2)^2/2=9/8,\qquad z_0^r=2/(3/2)=4/3,\qquad
J(z_0)=1-9/8+4/3=29/24.$$
Thus the rational cycle of this word has exactly
$$                         d=D/\gcd(D,29).                             \tag{3}$$
There is no floor input, small-gap assumption, norm bound or continued-fraction restriction in (3).

**Every positive integral instance is excluded.** A denominator of one in (3) would give $D\mid29$, hence $D=1$ or $29$. The stated range forces $n\ge3,u\ge2$. Modulo eight, $D=2^n-3^u$ is either 5 or 7. If $D=29$, modulo nine we have $2^n\equiv2$, hence $n\equiv1\pmod6$. Modulo eight we get $u$ odd. Modulo seven, $2^n\equiv2$ and $29\equiv1$, so $3^u\equiv1$ and $u\equiv0\pmod6$, a contradiction. This argument covers every permitted type and uses no computed Collatz floor.

There is a direct cyclic identity behind the formal proof. At an actual cleared edge $2a'=3^b a+bd$ one has $2(4a'+d)=3^b(4a+2d)$. If $y=z_0^{h_i}$, $y'=z_0^{h_{i+1}}$ modulo $D$, then $3^b y'=2y$. Thus
$$y'(4a'+d)-y(4a+d)=d y.$$
Telescoping gives $d\sum_i y_i=0$. In the integral case $d=1$, and for this explicit interval its rank sum is $[n]_z+(z^n-1)\sum_{l\le j<r}z^j$. Multiplication by $z-1$ leaves $(z^n-1)(1-z^l+z^r)$, so in the full modulus the physical cycle implies $58=0$. The residues of powers of 2 and 3 modulo 504 exclude every positive divisor of 58 in $2^n-3^u$ for $n\ge3,u\ge2$. This is also an independent combined-modulus finish for the elementary exclusion above.


To quantify its departure from a mechanical word, order the physical clock indices by $a_i=ui\bmod n$. For the normalized ideal, $h_i=a_i+n{\bf1}_{[l,r)}(a_i)$. The recurrence $h_{i+1}=h_i+u-nb_i$ shows that its odd positions occupy the three disjoint rank intervals
$$[l,r),\quad [v,v+l),\quad [v+r,n).$$
Any mechanical parity schedule of this same rational mean, with any phase, occupies one cyclic rank interval of length $u$. The six alternating positive and negative runs of the actual circle have lengths $l,r-l,v-r,l,r-l,u-r$ in clockwise order starting at zero (with the first run negative). If the Hamming distance from any interval were below twice their minimum, each run would have a correctly matched position, since the two kinds of mismatch have the same count. Those six correctly matched positions alternate, which one circular interval cannot do. Therefore the Hamming distance is at least twice that minimum.

Along $u/n\to p$ with $D>0$, $l/n,v/n-r/n\to2-3p$, $(r-l)/n\to5p-3$, and $(u-r)/n\to1-p$. The smallest limit is $2-3p$. There are infinitely many such coprime types by the lower convergents of $p$. Thus (3) holds in a family at distance at least $(4-6p-o(1))n$, or approximately $0.21442n$, from every fixed-mean mechanical parity schedule. This Hamming distance counts shortcut bits. Paper 237 uses odd-site halving exponents for its own substitution metric.

## Exponentially many boundaries at each lower-record type

Fix $0<\eta<1$. At each lower record of sufficiently large length $n$, put $u=\lfloor np\rfloor$, $v=n-u$, $T=\lfloor\eta n\rfloor$. Form the set of permitted boundary sites
$$B_n=\{tu\bmod n:1\le t\le T,\ 0<tu\bmod n<v\}.$$
There are $(\eta(1-p)+o(1))n$ such sites. Indeed $\|tu/n-tp\|_{\mathbb R/\mathbb Z}\le\delta$ for $t\le n$, $\delta\to0$ along the records, and irrational rotation by $p$ is equidistributed. Distinct $t$ in the range give distinct residues.

Choose *any even subset* of these sites, in increasing order, as the consecutive endpoints of disjoint holes intervals. The empty subset is allowed. Every resulting set is a legal normalized ideal since its gaps are all below $v<u$. Distinct subsets give distinct primitive necklaces by the bijection. At a chosen site $h=tu\bmod n$, the weight
$$w_h=2^t3^{-\lfloor tu/n\rfloor}$$
has $c=t\in[0,T]$ and, by (1), $1\le w_h\le 3^{(v+T\delta)/n}<9$. The lower-record order proof applies. A common denominator is $3^{\lfloor Tu/n\rfloor}\le 2^T$. Therefore (2) gives $d\ge D/(9\,2^T)$. Lagarias's effective two-logarithm lower bound gives $\log_2D=n-O(\log n)$ here, just as in the [contracting-calendar note](../CONTRACTING_CALENDARS.md). Hence there are
$$2^{(\eta(1-p)+o(1))n}\quad\text{primitive necklaces each with}\quad
d\ge 2^{(1-\eta)n-O(\log n)}.                                          \tag{4}$$
For the empty subset the cardinal count formula uses $2^{|B_n|-1}$ once $|B_n|\ge1$. Nothing limits the number of boundary corners by an absolute constant. The estimate is pointwise on each member of an explicitly specified family at *each* lower record. It is not an estimate for all necklaces at that period.

## A cyclotomic special case

If $J(z)\mid z^M-1$ in $\mathbb Z[z]$, every common divisor $m$ of $C,D$ forces $z_0^M=1\pmod m$. Thus
$$m\mid 2^{M/\gcd(u,M)}-1,\qquad m\mid 3^{M/\gcd(n,M)}-1.$$
For $M=u v$, the first gives $d\ge D/(2^v-1)$. A numerical semigroup generated by two coprime $a,b$ has boundary polynomial $(1-z)(1-z^{ab})/((1-z^a)(1-z^b))$, by its unique representations with the $b$-coefficient below $a$. This polynomial divides $z^{ab}-1$, since $(1-z^a)(1-z^b)/(1-z)$ is a polynomial. The case $a=u,b=v$ recovers the familiar two-run denominator restriction. For arbitrary ideals, $J$ need not be cyclotomic.

## Remaining obligation

For an unrestricted word, its boundary exponents can have clock lifts spread around the entire circle, and its greatest height may be of order $n^2$. Then the elementary height of $K$ in (2) can exceed $D$. The colored extension likewise allows the holes to occupy many heights. The positivity and exact additive-order statements above do not force a small certificate for every word.

PR188 RN3 gives a uniform norm saving for a related single residue-interval profile and does not require fixed affine formulas for its endpoints. PR191 treats group-ring norms at noncoprime clocks. Paper 237 derives denominator bounds from retained mechanical arcs and sparse substitutions. Here (3) computes the exact residual factor and (4) permits an unbounded number of corners, using the actual physical-prime evaluation. [PR188, beed685ab713923191ae40c9559bf7400298d2d3](https://github.com/GettysburgResearch/collatz/blob/beed685ab713923191ae40c9559bf7400298d2d3/research/scalar-carry-cocycle-20261124/RESIDUE_NORM.md) · [Paper 237 v1](https://rstation.ai/problems/collatz/papers/237/v1)
