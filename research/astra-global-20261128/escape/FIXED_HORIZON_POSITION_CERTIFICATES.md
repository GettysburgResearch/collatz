# Arbitrary fixed shortcut horizons and position-dependent ternary rankings

Write $O_s(n)$ for the number of odd departures among the first $s$ shortcut steps, $T(n)=n/2$ or $(3n+1)/2$ according to parity, and $\alpha=\log_3 2$.

**Theorem.** For every fixed horizon $s\ge1$ and radius $r\ge1$, there are a rational $p>s\alpha$ and one finite integer-weighted seed which extends to every sufficiently large ternary length $L$. Its positive sources are prime to three. The source $n$ and its actual $s$-step endpoint $T^s(n)$ each have $L$ trits. At each individual position their width-$(2r+1)$ window histograms agree exactly, including boundary padding. The average of $O_s(n)$ is $p$. In particular an arbitrary additive score with coefficients depending jointly on length, position and window cannot certify

$$F(T^s n)-F(n)\le s\alpha-O_s(n)$$

above any fixed floor. Every departure on these finite segments also exceeds any specified floor once $L$ is large, since $T^j(n)\ge n/2^j$. The theorem fixes the horizon before the length and certifies the two endpoint lengths. The intermediate heights need not stay within the same ternary band.

The case $s=1$, including the signed layer splicing and positivity argument, is proved in [the one-step theorem](ALL_POSITION_CERTIFICATES.md). The extension below describes the changed branch, window delay and lower-support conditions. It uses the same classical matrix-pencil and real rotation inputs. It yields existence with a terminating search; no explicit general-width numerical seed is furnished.

## 1. Genuine branch tags and the upper source

Assume $s\ge2$ and put $m=2^s$, $a=\lfloor s\alpha\rfloor\ge1$. The integers $a$ and $a+1$ are distinct possibilities for the endpoint height normalization, and $a<s$. For each $s$-bit word $b$ of Hamming weight $h_b$ there is exactly one residue $a_b\in[0,m)$ whose shortcut departures have that parity word. Induct on $s$: starting at $2u$ leaves $u$ after one step, and starting at $2u+1$ leaves $3u+2$, a bijection on residues at the remaining dyadic precision. For a nonnegative source $n=mq+a_b$ substitution gives

$$T^s(n)=3^{h_b}q+d_b,\qquad d_b=T^s(a_b),\qquad 0\le d_b<3^{h_b}.\tag{1}$$

At intermediate time $j$ its form is $3^{h_j}2^{s-j}q+c_j$ with $0\le c_j<3^{h_j}2^{s-j}$. An even step divides both terms by two; an odd step replaces $c_j$ by $(3c_j+1)/2$, bounded above by $3^{h_j+1}2^{s-j-1}-1$. This proves (1) and preservation of the tags. The corresponding affine map on $\mathbb Z_3$ is $F_b(z)=(3^{h_b}z+C_b)/m$, with $C_b=m d_b-3^{h_b}a_b$. For $h_b>0$ this map preserves the unit space, by the successive shortcut formulas. These formulas on $\mathbb Z_3$ use the separately prescribed word, without assigning a parity to a 3-adic integer.

On the real band $[1,3)$ normalize $x$ by $S_s x=3^{h(x)}x/m$, with $h(x)=a+1$ for $x<m/3^a$ and $a$ otherwise. In $\log_3 x$ this is rotation by $-s\alpha$. The smooth [real position balance](REAL_POSITION_WINDOW_BALANCE.md) applies with this rotation: take the same negative separated-digit mixed difference with positive log moment and solve its smooth coboundary by Fourier inversion. The fixed logarithmic Diophantine bound applies to $s n$ with $s$ fixed. The resulting smooth positive density balances the input and $S_s$-image window laws at every individual position. Since $\log S_s x-\log x=(h(x)-s\alpha)\log3$, one can choose a rational mean $p=\mathbb E h>s\alpha$ in an open interval. Conditional on each of the two values of $h$, distribute the tag uniformly among *all* words with that weight. Denote the resulting strictly positive rational tag probabilities by $\pi_b$. In particular the low law below can use the same probabilities independently of its source.

Long division of the input by $m$ has remainders $0,\ldots,m-1$. If its prefix represents $P$ then the quotient is $\lfloor P/m\rfloor$. In the tag $b$ this quotient supplies the endpoint trits $h_b$ positions earlier in the numeral. At the top the first $h_b$ quotient trits are zero and the next is nonzero, by the normalized real branch. At the bottom one appends the $h_b$ trits of $d_b$ with left zeros as needed, by (1). All interior arc weights of this upper law have a uniform positive lower bound once sufficiently many leading trits have been read: for each tag its real branch interval has positive length, its conditional density is bounded below there, and residues of $\lfloor3^j x\rfloor$ modulo a fixed integer occupy asymptotically equal volumes in each interval.

## 2. The delayed carry equations

Set $W=2r+1$, $M=3^{W-1}$, $H=a+1$. For each tag an interior arc is represented by $w=P\bmod(m3^W)$. The start and end state maps are $\lfloor w/3\rfloor$ and $w\bmod(mM)$. The input and quotient window maps are $X=w\bmod3^W$ and $Y=\lfloor w/m\rfloor$. Each completed input window at index $j$ must equal the sum of the tag-$b$ quotient windows read at index $j+h_b$. For an arc-vector layer $A$ denote its total input histogram by $X(A)$ and its quotient output histograms for tags with $h_b=i$ by $Y_i(A)$.

Augment each arc layer by $H-1$ free signed histogram vectors $u_1,\ldots,u_{H-1}$, each of length $3^W$. The start port consists of the tagged starting states followed by

$$(u_1,\ldots,u_{H-1},Y_H(A));$$

the end port consists of the tagged ending states followed by

$$(X(A)-Y_0(A),\ u_1-Y_1(A),\ldots,u_{H-1}-Y_{H-1}(A)).$$

These are linear maps $P,Q$ of the augmented layer. At the start of layer $j$, the $i$th histogram is what remains to be supplied for the input position $j-i$. Propagating inputs to their last allowed arrival gives exactly the stated delay balance. On a fully compatible bounded positive string the histograms are bounded by the masses of the future contributions; at any cut away from padding there are at most $H$ layers involved. The physical arc variables require nonnegativity. The auxiliary coordinates record linear equalities and do not enter path decomposition.

For a left null covector of $Q-\lambda P$ write $U_b\in\mathcal S_{mM}$ for its tagged states and $V_i\in\mathcal S_{3^W}$ for its histograms. The free $u_i$ give $V_{i+1}=\lambda V_i$. With $V=V_1$ use the circle grids as in the one-step proof to obtain

$$(D_3-\lambda)U_b=\lambda^{h_b}V-D_m V.\tag{2}$$

For $\lambda\ne0,1$, subtract the equations for two words with consecutive weights. As $\lambda^a(\lambda-1)\ne0$ this gives $V=(D_3-\lambda)Z$, $U_b=(\lambda^{h_b}I-D_m)Z$. The argument using the three nontriadic preimages of each nontriadic jump again forces $Z\in\mathcal S_M$; $m$ is a power of two. The generic null dimension is exactly $M$. At $\lambda=1$, summing the primitive-to-three Fourier strings of (2) gives $B(n)=\mathbf1_{m\mid n}B(n/m)$, hence $B(n)=0$ for every nonzero primitive $n$. The same transfer sum as in the one-step proof gives $V=\bar V+(D_3-I)Z$, $U_b=(I-D_m)Z+c_b$ with mean-zero $Z\in\mathcal S_M$. The dimension is $M+\#\{b\}$. The only possible other finite exceptional scalar is zero. Its nilpotent Jordan trajectories vanish in the interior when enough layers to the left are specified.

The finite pencil therefore has one unit Jordan block per tag. Their sizes are all one, because independent conserved tag totals pair with the same number of constant uniform tagged physical arc laws. For a pure tag with delay $h$, the constant pending histogram on coordinate $i$ is unit uniform for $1\le i\le h$ and zero when $i>h$. Free right blocks contribute nothing to these conserved totals; a longer unit Jordan block contributes nothing on its constant eigenvectors, as proved in the one-step manuscript. Right singular windows can be spliced in bounded time, and the left singular, nilpotent and infinite components vanish away from boundaries. Hence bounded signed connectors with a fixed finite transition span again exist between any two sufficiently deep compatible strings with the same tag masses. The physical uniform mixture $U$ with masses $\pi_b$ is strictly positive on every tagged arc.

## 3. Positive low arcs on a single finite band

Take a stationary Feller law $\sigma$ on $\mathbb Z_3^\times$ for the random maps $F_b$, choosing the tag independently with probabilities $\pi_b$. Compactness gives existence and its support $K$ contains $F_b(K)$ for each tag. The input and output suffixes agree in law. Unlike the single-step proof, each branch at this horizon can contract in the 3-adic metric. We only need all arcs to have positive mass on *one* sufficiently long interior band, and we prove this directly.

The set $K$ is uncountable. There are two words with the same count $a$, differing by an adjacent exchange of $01$ and $10$. In the two-step affine formula these two orders add respectively $2$ and $1$ in the numerator; composing with their common prefix and suffix leaves distinct affine constants. The maps have the same strictly 3-adically contracting slope, so their rational fixed points are distinct. Both fixed points belong to $K$. Iterating each branch sufficiently many times sends $K$ into disjoint 3-adic balls around its respective fixed point. Independent choices of these two iterated maps then give an injective binary Cantor coding inside $K$. Choose one map, with fixed point $z_*=C_b/(m-3^a)\in\mathbb Q\cap\mathbb Z_3$. Its iterates have exactly the form required by [the simultaneous remote-trit lemma](REMOTE_TRIT_SUPPORT.md).

To see which cylinders to request, suppose there are $k$ unread input trits below a $W$-trit window. In tag $b$ put $q=(z-a_b)/m\in\mathbb Z_3$. For an ordinary eventual lift this is exactly the quotient by $m$. Writing $q_\ell=[q]_k$ and $q_W=\lfloor[q]_{k+W}/3^k\rfloor$, the carry at the low end of this window is $c=\lfloor(m q_\ell+a_b)/3^k\rfloor\in[0,m)$. Its actual arc code is

$$m q_W+c=\left\lfloor m3^W\frac{[q]_{k+W}}{3^{k+W}}+\frac{a_b}{3^k}\right\rfloor.\tag{3}$$

For large $k$, any specified arc code is forced by taking the normalized residue strictly inside the corresponding one of $m3^W$ equal real-circle cells, with a fixed margin smaller than half the cell width. Use one such interval for each tag, each arc code and each of a fixed finite list of consecutive depths. The remote-trit lemma realizes every request at one arbitrarily large common band, with possibly different support points. Strict containment gives a positive-measure $\sigma$ cylinder per request. Independence of the tag gives positive *tagged* mass. The finitely many entries on the selected band thus have a positive minimum.

The bottom quotient and residue synchronize by taking at every cut the unique $c\in[0,m)$ such that $3^k c+[z]_k\equiv a_b\pmod m$. Then $(3^k c+[z]_k-a_b)/m$ lies in $[0,3^k)$ and gives the low $k$ quotient trits. Indeed its numerator is a multiple of $m$ in $[-(m-1),m3^k-1]$. At the terminal cut the remainder equals $a_b$. The appended trits from (1) give the actual endpoint, and stationary equality of $z,F_b(z)$ gives all the required bottom and interior window equalities. The input unit condition supplies a nonzero bottom trit.

## 4. Conclusion

Apply the positive joining argument of the one-step theorem with the lower band just constructed as its final transition block. The leading process and the uniform interior dominate all signed corrections in the upper join. In the lower join its initial uniform share decreases geometrically, then vanishes on the chosen positive lower band. Leave two identical prescribed uniform layers in the middle (or at least $H+1$ successive layers when using the direct delayed-window interpretation). The entire finite network has rational constraints and tag masses, so it admits rational nonnegative physical flows, with rational auxiliary values. Integer decomposition of the tagged state flows yields true sources with the prescribed dyadic residues, an ordinary $s$-step path and endpoint trits given by (1). The augmented-port equalities include all the delayed contributions. The uniform augmented layers have identical starting and ending ports, allowing arbitrary middle repetitions. All lengths thereafter work, and the mean odd count is $p$.

[NativeWindowBlock.lean](NativeWindowBlock.lean) certifies the actual count and endpoint dyadic lift, the residual bound for the low trits, and the native cut formula for every positive divisor and window width. The [finite controls](check_horizon_pencil.py) check 147,312 ordinary path/carry instances and seven delayed finite pencils over the field of 101 elements. The analytic joins, all-radius existence and real-torus support lemma are the written proof. [Replay receipt](../../../reports/astra-global-20261128/escape/HORIZON_PENCIL_CHECKS.json)
