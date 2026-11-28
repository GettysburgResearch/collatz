# Moving sparse coefficients and arbitrary repairs inside short windows

Let $n,u$ be positive integers, $D=2^n-3^u>0$, $g=\gcd(n,u)$ and $n\to\infty$. Let $k,C,\delta>0$ be fixed, with $k$ an integer. We allow $k$ rational coefficients $c_i$ to vary with the clocks, each of logarithmic Weil height $o(n)$. Assume

$$
 G=\sum_{i=1}^k c_i2^{t_i}3^{s_i}\ne0,\qquad |t_i|,|s_i|\le Cn.
$$

For a rational $G$ in lowest terms let $(D,G)$ denote the gcd of $D$ and its numerator. Clearing the varying coefficient denominators or removing powers of two and three changes its logarithm by $o(n)$. If the binary exponent diameter is at most $(1-\delta)n$, then

$$
                \log_2(D,G)\le (1-1/\min(k,g))n+o(n).                 \tag{1}
$$

A ternary diameter at most $(1-\delta)u$ suffices as well provided $u\gg n$. The latter condition measures the gap against the scale on which coefficient heights are negligible. No effectivity is asserted. For bounded coefficients the sharper ternary form that requires only $u\to\infty$ is proved separately. [Fixed-target estimate and Weaver 22 antecedent](SPARSE_FULL_MODULUS.md)

**Native consequence.** Take any two distinct rooted binary shortcut words of the same length $n$ and weight $u$. Suppose that they agree outside at most $k$ disjoint cyclic intervals of total length $o(n)$ and that their weights on *each* interval agree. The two complete positive rational denominators $q,q'$ then satisfy

$$
             \log_2\operatorname{lcm}(q,q')\ge n/\min(k,g)-o(n).       \tag{2}
$$

There is no bound on the internal number of changes, runs or distinct subwords in those windows. At coprime clocks one subexponential denominator forces the other to be $2^{n-o(n)}$. On arbitrary clocks the coefficient $1/k$ is sharp even with two-bit windows, both words primitive and their common slope tending to the Collatz slope. [Optimal examples](SPARSE_FULL_MODULUS.md)

## Concurrent prior work and exact overlap

[PR215 at d444e332, published before this packet's checkpoint 7](https://github.com/GettysburgResearch/collatz/blob/d444e332d111115daa650c58a917dd46dacd4c1e/research/astra-nine-hour-20261128/cycles/phase4/MOVING_SPARSE_SUMS.md)
already uses the quotient by limiting exponent relations, the moving gcd
theorem and the finite Fourier support bound for coefficients of sublinear
height. Its positive, adjusted-dyadic-separated and nearcritical stable-real
cases give the sharp reciprocal-support rate and rational limit quantization.
Its [moving-template application](https://github.com/GettysburgResearch/collatz/blob/d444e332d111115daa650c58a917dd46dacd4c1e/research/astra-nine-hour-20261128/cycles/phase4/MOVING_POWERED_WORDS.md)
directly overlaps the separated junction application below, after its zero
or submacroscopic pieces are handled. The general moving-coefficient method
and that overlapping denominator conclusion are not first claims of this
packet. Root read both complete pinned notes during checkpoint 9 and checked
their relation to the independently developed checkpoint-7 proof.

The proper-arc hypothesis here also treats arbitrary signs with equal
adjusted dyadic dates, without positivity or a nearcritical stable evaluation.
The short-window edit lcm, the explicit native repairs and genuine-cycle
exception, the smallest irrational-spacing class, and the formal endpoint
ideal are retained as the distinct formulations of this note. PR215 also
has a stronger positive full-rate criterion when every prime in the clock
gcd exceeds the support size, and separate [proper physical-arc results](https://github.com/GettysburgResearch/collatz/blob/d444e332d111115daa650c58a917dd46dacd4c1e/research/astra-nine-hour-20261128/cycles/phase4/MOVING_RESIDUES.md).
No completeness claim is made for this comparison.

## Small characters and the moving gcd theorem

Argue on any infinite proposed violating sequence. Retain a subsequence with all the ratios $u/n,t_i/n,s_i/n$ convergent and with either constant $g<k$ or $g\ge k$ throughout. Evaluate a character lattice $M=\mathbb Z^{k+1}$ on the rational unit coordinates $R=2^n3^{-u}$ and $Z_i=2^{t_i}3^{s_i}$. The two vectors of limiting prime exponents per $n$ give a real linear map $M\to\mathbb R^2$. Its integer kernel $L$ is saturated. Choose a direct summand complementary to $L$. Each fixed character in $L$ evaluates to a rational $\{2,3\}$-unit of height $o(n)$. Every fixed nonzero character in the complementary lattice has height bounded below by a positive constant times $n$, also along every further subsequence. Indeed the logarithmic height of $2^t3^s$ is at least $\max(|t|\log 2,|s|\log 3)$ and at most the sum of those terms.

The image of $R$ in $M/L$ is nonzero. Write it as $d$ times a primitive character $T$ and complete $T$ to a basis $T,\mathbf W$ of the complementary lattice. At each input this gives $R=T^d/c$ for a positive rational $\{2,3\}$-unit $c$ of height $o(n)$. The determinant on these arguments is, up to an outside-$\{2,3\}$ unit, $F=T^d-c$. Write

$$
 G=\sum_b \mathbf W^b G_b(T),\qquad G_b(T)=\sum_{i:b_i=b}\eta_i T^{a_i}.
$$

The integer exponents $a_i,b_i$ are fixed along the retained sequence. The individual rational coefficients $\eta_i$ have heights $o(n)$ by construction. Multiply $G$ by a monomial to clear negative character exponents. Its numerical value changes only by a unit outside two and three. If $b_i=b_j$ and $a_i-a_j=m d$, then prime valuations give

$$
                t_i-t_j=m n+o(n),\qquad s_i-s_j=-m u+o(n).
$$

Either proper-gap hypothesis forces $m=0$. At every index at least one $G_b$ therefore has nonzero remainder modulo $F$. Otherwise the coefficients sharing each exact character exponent cancel, contradicting the nonzero numerical sum.

At each index form the monic rational polynomial $A=\gcd(F,\{G_b\}_b)$ and write $F=AB$, $G=AJ$. The degrees and supports of these polynomials are bounded. Their individual coefficient heights are $o(n)$. For instance Euclidean division with the monic inputs, terminating whenever a degree drops, uses only boundedly many additions, products and inversions on coefficients of height $o(n)$, since the degrees are fixed. Divide each coefficient polynomial $G_b$ by $A$ to obtain $J$. Pass further to fix all needed degrees. The polynomial $B$ has nonzero constant coefficient. If $J$ is constant its individual height gives residual gcd $o(n)$ directly. Otherwise $B,J$ are coprime multivariate polynomials of fixed positive degrees. Clearing the original negative powers of $G$ introduced only coordinate factors, and $B$ is coprime to each coordinate.

Apply Grieve and Wang's moving-target gcd theorem to $B,J$ on the rational $S$-units $T,\mathbf W$, $S=\{\infty,2,3\}$. The projective coefficient heights are $o(n)$ and the largest coordinate height is of order $n$. Its proper-subgroup alternative would imply, on an infinite further subsequence, that a fixed nonzero character of the complementary lattice has height $o(n)$. The limiting prime exponent construction excludes this. For every $\epsilon>0$ the theorem thus obtains arbitrarily large indices with generalized logarithmic gcd below $\epsilon O(n)$. Applying it to any putative bad subsequence gives outside-$S$ logarithmic gcd $o(n)$. Its nonnegative local terms dominate all the outside-$S$ terms used here. [Grieve and Wang, Theorems 1.2 and 3.1, Proposition 3.5 and §3.3](https://arxiv.org/pdf/1902.09109)

Write $h=\deg A$. At least $d/k$ of the $d$ complex roots of $F$ survive by the finite Fourier support inequality proved in the fixed-target note. Every root of degree $e$ has $\operatorname{Norm}(\alpha)^d=c^e$. As $R=T^d/c$, the prime valuations of $c$ modulo $d$ are $-n,u$. Hence $d\mid e n,e u$ and $e\ge d/g$. The surviving set is rationally invariant and nonempty. Thus $h/d\le1-1/\min(k,g)$ at every retained index.

For the size bound, the rational number $T$ has dyadic valuation $n/d+o(n)$ and ternary valuation $-u/d+o(n)$, with no other prime factors. Its logarithmic height is at most $(n/d)\log 2+o(n)$ because $3^u<2^n$. Evaluating the degree-$h$ polynomial $A$ gives $h_{\rm Weil}(A(T))\le (h/d)n\log 2+o(n)$. At a prime outside two and three the valuations of $A(T),B(T),J(T,\mathbf W)$ are bounded below by the minimum valuations of their individual coefficients, whose total denominator cost is $o(n)$. The sum of the positive common valuations of $F,G$ is accordingly bounded by the height of $A(T)$ plus the residual gcd and $o(n)$. This proves (1) on the violating subsequence and hence the theorem. The rational-coefficient positive valuations from clearing denominators remain within the same $o(n)$ allowance.

## Interval edits and the endpoint obstruction

Rotate both words to a common seam inside their largest uninterrupted agreement. Complete denominators are rotation invariant. After the rotation all the edit onsets lie in a proper binary interval of length at most $(1-1/k)n+o(n)$, with the case $k=1$ giving a single onset. The carry differences are a sum of at most $k$ terms

$$
            2^{t_i}3^{s_i}\big(C(v_i)-C(w_i)\big),
$$

where $t_i$ counts preceding sites and $s_i$ counts subsequent ones. Equality of each window weight guarantees that the unchanged parts cancel and these two counts agree. Each nonzero integer coefficient has height $O(|w_i|)=o(n)$ by the usual positive affine carry formula. The whole difference is nonzero. Indeed if two rooted words have the same $C,n,u$ then they have the same initial parity residue $-3^{-u}C\bmod 2^n$, which determines the entire $n$-word by forward shortcuts. Since $D/\operatorname{lcm}(q,q')=\gcd(D,C(w),C(v))$ and $\log_2D=n-O(\log n)$ by the two-logarithm estimate, (1) yields (2).

## Gluing arbitrarily complex macroscopic native segments

For a fixed number $k$ of finite native shortcut paths, let $x_i,y_i$ be their respective actual initial and terminal positive rationals with odd denominators, $l_i$ their lengths and $u_i$ their odd counts. Concatenate their words in a specified circular order. The paths may come from any orbits. Write $n=\sum_i l_i$, $u=\sum_i u_i$, $D=2^n-3^u>0$, $t_i=\sum_{j\le i}l_j$, $U_i=\sum_{j\le i}u_j$, and $\Delta_i=y_i-x_{i+1}$, with $x_{k+1}=x_1$. Suppose the logarithmic heights of all $x_i,y_i$ are $o(n)$. Each interior can use an arbitrary parity word, can reach large states, and can occupy a fixed positive fraction of the whole period.

If every $l_i\ge\delta n$ for some fixed $\delta>0$, there is the following dichotomy. Matching all junctions gives the actual closed native path over its original denominator. If at least one junction fails, the complete denominator $q$ of the concatenated word satisfies

$$
                   \log_2 q\ge n/\min(s,g)-o(n),                        \tag{3}
$$

where $s$ counts the nonzero junction discrepancies. In particular every discontinuous macroscopic gluing has $q=2^{n-o(n)}$ at coprime clocks. A noncyclic permutation of macroscopic pieces of a single least-period integer cycle has a nonzero junction by distinctness of its boundary states. Thus the bound applies whenever the selected boundary heights are subexponential, without controlling the internal complexity of that integer cycle.

For the proof, the normalized affine map of the $i$th recorded word is $z\mapsto a_i z+y_i-a_i x_i$, where $a_i=3^{u_i}/2^{l_i}$. Let $C$ be the full carry of their concatenation. Ordinary composition gives the exact residual

$$
          C-Dx_1=\sum_{i=1}^k 2^{t_i}3^{u-U_i}\Delta_i.                \tag{4}
$$

This includes the last junction with $t_k=n,U_k=u$. Cut before a long piece, so the $t_i$ lie in an interval of diameter at most $(1-\delta)n$. Clear all endpoint denominators by an integer $Q=e^{o(n)}$. Each nonzero $Q\Delta_i$ has logarithmic height $o(n)$. The dyadic valuations of the nonzero terms on the right of (4) are distinct for large $n$, since their $t_i$ differ by at least $\delta n$. The residual is nonzero. Furthermore $\gcd(D,C)\mid\gcd(D,Q(C-Dx_1))$ because $Qx_1$ is integral. Applying (1) to the right and using $\log_2D=n-O(\log n)$ proves (3). Even a nonzero discrepancy of sign opposite to the others satisfies the argument.

More generally take any fixed $k$ of positive segment lengths. On each subsequence pass further so the normalized positions $t_i/n$ converge on the circle. Group the junctions into consecutive clusters when their limiting circular positions coincide. Distinct clusters are separated by a positive multiple of $n$. For a cluster from its first junction $i$ through its last junction $j$, form its effective discrepancy

$$
 E=\sum_{h=i}^j\Delta_h\prod_{r=h+1}^j a_r.
$$

In a circular representation choose the seam immediately following a cluster and before a longest intervening piece. The intermediate pieces inside each cluster have total length $o(n)$, so $h_{\rm Weil}(E)=o(n)$. In (4) the cluster's exact combined contribution is $2^{t_j}3^{u-U_j}E$. If every effective discrepancy vanishes, the intermediate words in each cluster carry the previous long piece's endpoint to the next long piece's actual source. Indeed $E$ is exactly the affine output from that preceding endpoint minus the next actual source. The intervening word is native there: for a positive odd-denominator input, a prescribed $L$-bit affine word ending in a rational that is integral at two requires the canonical input residue modulo $2^L$, which determines all $L$ parity bits. Thus the concatenated word replays as one genuine closed path, even if the originally recorded short pieces used other sources. Its reduced denominator is that of a boundary on a long piece, since a closed positive shortcut path preserves its common reduced denominator. Indeed an even step preserves the reduced odd denominator, and an odd step can only remove a factor of three. A positive closed path has an odd step, so its denominator must be prime to three and cannot change around the cycle.

If at least one effective discrepancy is nonzero, fix which clusters survive on a further subsequence and take $s$ to be their number. Clearing the fixed number of new denominators costs $o(n)$ in the logarithm, including any powers of two introduced by short pieces. The distinct representative $t_j$ are separated by a linear gap and contained in a proper binary interval. Their nonzero effective terms have different dyadic valuations, so (3) follows again. These statements on every retained subsequence also give a uniform consequence: if $q=2^{o(n)}$, the long pieces necessarily glue through the short pieces after clustering on every such subsequence, eventually.

**Irrational spacings.** On a retained subsequence let $f_1,\ldots,f_s$ be the distinct limiting normalized positions of the surviving effective discrepancies. Partitions by $f_i-f_j\in\mathbb Q$ can strengthen (3) even when the clocks have large gcd. If $s_*$ is the size of the smallest class, then $s$ in (3) can be replaced by $s_*$. Indeed the class of a common $\mathbf W$ monomial in the moving proof above can only contain two terms when their time difference divided by $n$ tends to $(a_i-a_j)/d$, a rational number. Every occupied $\mathbf W$ group has nonzero remainder because the limiting times are distinct in a proper interval. Select a group contained in a smallest class and use its size in the Fourier support argument. In particular one seam whose limiting spacings to every other surviving seam are irrational forces $q=2^{n-o(n)}$ at all clocks. The branch with every effective discrepancy zero is a real exception at any slope.

## Unrestricted formal endpoint identities

A limitation of replacing arbitrary macroscopic blocks by their observed small endpoints is exact. Let a field $K$ have characteristic zero and allow nonzero symbolic slopes $a_i$ and independent symbolic block offsets $b_i$, with indices $1\le i\le k$. Define

$$
 P=\prod_i a_i,\qquad L=\sum_i b_i\prod_{j>i}a_j.
$$

In the Laurent ring $K[a_i^{\pm1},b_i]$, the ideal obtained by eliminating endpoint labels $x_1,\ldots,x_k$ from $P-1$ and the cyclic block equations $b_i=x_{i+1}-a_ix_i$ is exactly $(P-1,L)$. To see this, eliminate $x_2,\ldots,x_k$ using the first $k-1$ equations. The last equation is $(1-P)x_1=L$. Modulo $P-1$ this becomes exactly $L=0$ and $x_1$ is free. Intersecting back with the original ring introduces no further relation. Consequently even nonlinear polynomial consequences of the unrestricted endpoint equations on the neutral slope specialize through the same full-lap carry. Additional arithmetic structure of the internal unit offsets or of the endpoint labels would be needed to produce an independent sparse witness. On a positive real neutral slope, strict positivity of every $b_i$ is incompatible with $L=0$. A neutral positive tilt for the original atomic carry terms cannot be justified merely by substituting small boundary labels.
