# Finite ordinary certificates for every ternary radius and arbitrary position weights

Let $W=2r+1$, $r\ge1$. Use canonical ternary digits, with separate symbols above and below a numeral. A feature counts a single $W$-trit window at one particular position of integers of one particular length. Let $T(n)=n/2$ on evens and $(3n+1)/2$ on odds.

**Theorem.** At each fixed ternary radius there are a rational $f>\alpha=\log_3 2$ and $L_0<\infty$ such that for every $L\ge L_0$ a finite positively integer-weighted family of sources and their true images has the following properties. The sources are positive and prime to three. Both sides have exactly $L$ trits. At every individual position the two window histograms agree. The odd fraction is $f$. One finite seed with identical neighboring interior carry-arc counts gives all these lengths by inserting layers. Thus no additive score with arbitrary coefficients depending jointly on length, position and window can satisfy $F(Tn)-F(n)\le\alpha-\mathbf1_{2\nmid n}$ on all sources above any floor.

The proof gives finite existence with a terminating rational search. The explicit [width-three and width-five seeds](POSITION_WINDOW_PUMP.md) are much smaller examples. The general argument uses the [smooth real window law](REAL_POSITION_WINDOW_BALANCE.md), its fixed-base logarithmic Diophantine input, and the standard Kronecker canonical form of a complex matrix pencil. The integer transfer below needs no hypothesis about the global behavior of ordinary Collatz orbits.

## 1. The interior of long division

An input prefix $P$ has quotient $Q=\lfloor P/2\rfloor$ and remainder $c=P\bmod2$. For a true source with parity tag $e$, the quotient digits supply the output at the same index when $e=0$, and one index earlier when $e=1$. In the second case the initial quotient zero is dropped and a terminal trit 2 is appended. We restrict to leading source trit $2-e$. [The literal finite construction](POSITION_WINDOW_PUMP.md) derives these assertions.

Put $M=3^{W-1}$. At an interior index after reading a new digit, encode its arc by $e$ and $w=P\bmod (6M)$. The input and quotient windows completed at this layer, represented as integers with leading zeros permitted, are respectively $X(w)=w\bmod(3M)$ and $Y(w)=\lfloor w/2\rfloor$. Indeed $w=2(Q\bmod(3M))+c$. The starting and ending states of this arc are $s(w)=\lfloor w/3\rfloor$ and $d(w)=w\bmod(2M)$, with tag retained. These record the preceding and current prefixes modulo $2M$.

Let $a=(a_0,a_1)$ be the signed vectors on the two copies of $0\le w<6M$. For a map $h$ use $h_*$ for the induced summation of weights. Define two linear maps into a port space with two $2M$-vectors and one $3M$-vector,

$$
 P a=(s_*a_0,s_*a_1,Y_*a_1),\qquad
 Q a=(d_*a_0,d_*a_1,X_*(a_0+a_1)-Y_*a_0).
 \tag{1}
$$

Here and below the same letters $P,Q$ for the **maps** have arguments that are arc vectors. Consecutive layers are compatible precisely when $Qa_j=Pa_{j+1}$. The first two equations conserve the two tagged state flows. The last matches the input and even-image histograms at $j$ with the odd-image contribution that becomes available at $j+1$. Thus positivity and the two ordinary ends are the remaining requirements beyond (1).

## 2. Singularities of the finite pencil

Write $D_b h(u)=h(bu\bmod1)$ on the real unit circle, and $\mathcal S_m$ for the complex step functions on its uniform $m$-cell grid. Identify port covectors with $U_0,U_1\in\mathcal S_{2M}$ and $V\in\mathcal S_{3M}$. For $u$ in the $w$-th cell of the $6M$ grid, its starting-state coordinate reads $U_e(u)$, ending-state coordinate $U_e(3u)$, input-window coordinate $V(2u)$ and quotient-window coordinate $V(u)$. The left nullspace of $Q-\lambda P$ is therefore described by

$$
 (D_3-\lambda)U_e=\lambda^e V-D_2 V,\qquad e=0,1.
 \tag{2}
$$

For $\lambda\ne1$ subtract the two equations. With $Z=(U_1-U_0)/(\lambda-1)$ one obtains

$$V=(D_3-\lambda)Z,\quad U_0=(I-D_2)Z,\quad U_1=(\lambda I-D_2)Z.\tag{3}$$

Indeed $D_2,D_3$ commute; $D_3$ has no nonconstant eigenfunction in these finite step spaces (a nonempty finite set of jumps cannot contain all its threefold preimages), and its constant eigenvalue is 1. In (3), $Z\in\mathcal S_M$. To see this, any nontriadic jump of $Z\in\mathcal S_{2M}$ has three nontriadic preimages under tripling. Every one must again be a jump of $Z$, since $(D_3-\lambda)Z$ has only triadic jumps. This is impossible for a finite nonempty set. At $\lambda=0$ the same conclusion holds directly since a jump would produce a forbidden jump of $D_3 Z$. Conversely every $Z\in\mathcal S_M$ gives a solution. The dimension is $M$.

At $\lambda=1$, $U_1-U_0$ is constant. For an integer $n\ne0$ with $3\nmid n$ put $B(n)=\sum_{j\ge0}\widehat V(3^j n)$. The sum is finite: for $V$ on the $3^W$ grid its Fourier coefficients at nonzero multiples of $3^W$ vanish. Summing the Fourier coefficients of (2) along this string telescopes on the left, with zero terminal limit, and gives $B(n)=\mathbf1_{2\mid n} B(n/2)$. Induction on the power of two dividing $n$ gives $B(n)=0$. If $L_3$ denotes averaging over the three inverse images under tripling, let

$$Z=\sum_{j=1}^{W-1} L_3^j(V-\bar V)\in\mathcal S_M.$$

Now $L_3^W(V-\bar V)=0$. Applying $L_3$ to $V-\bar V-(D_3-I)Z$ gives zero, so this expression has zero Fourier coefficients at all multiples of three. At indices prime to three its coefficient is $B(n)=0$. Its mean also vanishes. Consequently

$$V=\bar V+(D_3-I)Z,\qquad U_e=(I-D_2)Z+c_e.$$

Every mean-zero $Z\in\mathcal S_M$ and the three constants give distinct solutions. Thus the left-null dimension at 1 is $M+2$.

## 3. Splicing signed layers

There exist an integer $K$ and constant $C$ depending only on the radius with the following property. Let $A_j,B_j$ be two bounded compatible layer strings on an interval with at least $K$ spare layers on each side of a cut. Assume they have the same two constant tag masses. A compatible real signed string $D_j$ can equal $A_j$ on the left of the cut and $B_j$ starting $K$ layers later. On the intervening layers $\|D_j\|_\infty\le C\max_j(\|A_j\|_\infty+\|B_j\|_\infty)$, using only a fixed neighborhood of the cut.

Here is the linear algebra, including why there are no unaccounted conserved coordinates. Apply constant invertible row and column changes to put the pencil $Q-\lambda P$ in Kronecker canonical form. A right singular block permits a scalar sequence of free entries with a fixed finite sliding window as its vector at time $j$. Explicitly its equations are $v_{i+1}(j)=v_i(j+1)$. The two scalar sequences can be joined at a chosen time, giving a transition no longer than the block size with bounded norm. A transposed singular block has the same relations and the two boundary entries forced to zero, hence has zero trajectory in the interior beyond its size. An infinite regular block has $v(j)=N v(j+1)$ for nilpotent $N$, hence also vanishes with sufficient space on the right. The formulas for these blocks and strict equivalence are the classical canonical-form theorem. [Kronecker canonical form, Theorem 1](https://gauss.uc3m.es/fdopico/papers/laa2016-2.pdf)

The number of finite regular Jordan blocks at a scalar is the increase over generic left-null dimension there: the singular blocks have constant finite-parameter rank. Section 2 therefore leaves exactly two regular Jordan blocks, both at 1. For every compatible trajectory its two tagged totals are constant. On a free right block each such conserved functional vanishes, since an arbitrary finite segment extends using a finitely supported free scalar sequence. On a $d$-dimensional unit Jordan block a conserved functional is a left fixed covector of $J_d(1)$; when $d>1$ it annihilates every fixed vector. There are two explicit constant arc strings with respective total tags $(1,0)$ and $(0,1)$: take uniform mass on all $6M$ arcs of the indicated tag, with none on the other. The pushforwards in (1) match because all four maps have equal-size fibres within their codomains. The two independent totals on these fixed strings require two size-one regular blocks. Thus the constant regular components agree exactly for strings with the same totals. Joining the right singular components and retaining the common regular components proves the claim. Choose $K$ larger than twice the maximum block size plus two; the fixed coordinate changes give $C$. For real inputs take real parts after converting back to the original coordinates.

## 4. Supplying the ordinary ends

Choose a rational $f>\alpha$ in the open interval of branch masses supplied by the smooth real law. Let $A$ denote its nonnegative true leading-prefix arc process. Read $x\in[1,3)$ and $Sx$ in ternary from the left. Their window laws agree at every position, and the index alignment is precisely (1), since flooring $x3^j/2$ gives the quotient of $\lfloor x3^j\rfloor$ by two. The two tag masses are $1-f,f$. At every sufficiently deep layer *each* of the $12M$ arc weights has a uniform lower bound $c>0$. In each of the two unit branch intervals the smooth positive density in $x$ is bounded below. Each residue class of $\lfloor x3^j\rfloor\bmod 6M$ occupies a fraction bounded below there as $j\to\infty$. The initial tagged prefixes supply the correct separate leading padding.

For the other end let $z$ lie in the compact group $\mathbb Z_3^\times$. Independently choose $e\in\{0,1\}$ with odd probability $f$, and send $z$ to $z'=(3^e z+e)/2$. Both maps preserve the unit space. The continuous random map has a stationary probability $\sigma$: take a weakly convergent subsequence of the Cesàro averages of iterates on the compact space. Its support is all units. The support is closed under the even map $z\mapsto z/2$ because that branch has positive chance from each neighborhood. The powers of $2$ are dense in $\mathbb Z_3^\times$: modulo 3 the order is two, and $v_3(4^{3^j}-1)=j+1$ by induction, giving full orders at all precisions. Start $z\sim\sigma$. Its image has exactly its law and every input is a unit.

This gives an infinite lower string $B$ read from large indices toward the least significant trit. At a cut with $k$ unread low trits $\ell=z\bmod3^k$, the required carry of the high prefix is $c=(e-\ell)\bmod2$, as $3^k$ is odd. Indeed for an ordinary representative $n=3^k p+\ell$ with $c=p\bmod2$ and terminal parity $e$,

$$ (n-e)/2=\lfloor p/2\rfloor 3^k+(c3^k+\ell-e)/2,\qquad 0\le(c3^k+\ell-e)/2<3^k. $$

The residual is an integer by the chosen carry. This identity gives compatible carries at all adjacent cuts and identifies the low quotient trits with those of $(z-e)/2$ in $\mathbb Z_3$. Thus and the output suffix is precisely that of $z'$, including the terminal digit 2 on the odd tag. Window balance, including all lower padding, follows by stationarity, and the terminal carry is $e$. For any interior layer with $k\ge1$ unread trits, each arc of each tag has positive probability. Prescribe the $W$ input trits just above the remaining $k$, and the terminal carry of this $W$-trit block, which together specify $w$ uniquely. Choose the lower $k$ trits with bottom trit 1 or 2 to obtain either required parity of $\ell$. The resulting nonempty unit cylinder has positive $\sigma$-mass, independently of the prescribed tag. This assertion is pointwise in the depth. We use a positive minimum only over **one fixed** finite lower block.

## 5. Positive joining and a rational seed

Let $U$ be the constant uniform layer with the same two tag masses. Every arc of $U$ is strictly positive. We first join $A$ to $U$. In any deep block of length $K$ take the signed connector of Section 3 from the first to the second. To change the mixture $(1-t)A+tU$ on the left to $(1-t-h)A+(t+h)U$ on the right, use

$$(1-t-h)A+tU+hD$$

in the block. The equations are linear and the strings agree at the joins. Since $A$ and $U$ have uniform positive lower bounds and $D$ is uniformly bounded, all layers stay nonnegative for a sufficiently small fixed $h>0$. Finitely many such blocks, using a smaller last increment if needed, take $t$ from zero to one. Leave at least two unmodified copies of $U$ in the middle.

For the join from $U$ to $B$, start above a fixed terminal block with at least $K$ extra unmodified layers before the true lower endpoint. Fix one length-$K$ transition block at this chosen lower depth. The entries of $B$ on it have a positive minimum $b$. For an earlier block transform $tU+(1-t)B$ to $(t-h)U+(1-t+h)B$ by using $(t-h)U+(1-t)B+hD$ there, for a uniformly bounded signed connector $D$ from $U$ to $B$. Choose $h=\eta t$ with fixed $0<\eta<1$ so small that $(1-\eta)\min U-\eta\sup\|D\|_\infty>0$. All these mixtures stay nonnegative using only the uniform mass of $U$. After finitely many blocks $t=(1-\eta)^N$ is as small as desired. In the fixed final transition block take $h=t$; $(1-t)B+tD$ is nonnegative there for sufficiently small $t$, since $b>0$. Place the earlier $N$ blocks immediately above this fixed region, where the lower string is defined to arbitrary height. Thereafter use only $B$ through the true last digit. Extra room can be filled with $U$.

This produces a finite feasible real layered flow with its two true ends, fixed rational tagged totals, and two identical prescribed uniform middle layers. All incidence, histogram, terminal and equality constraints have rational coefficients, and every entry of $U$ is rational. The nonempty rational polyhedron with these constraints and nonnegative variables has a rational point (equivalently, solve equalities on the support of the positive coordinates and approximate its free parameters by rationals). Clear denominators and decompose the layered integer flow into paths. Each path starts with trit $2-e$, ends with a nonzero trit and carry $e$, and reads the true ordinary $n,T(n)$; their equal length and all boundary windows were part of the end conditions. The rational parity fraction is unchanged. Repetition of the middle layer gives every greater length by the [integer splicing argument](POSITION_WINDOW_PUMP.md). An exhaustive search over lengths and rational flows, with exact comparison $3^{\#\mathrm{odd}}>2^{\#\mathrm{total}}$, terminates. No practical general bound on the first seed length or its weight follows here.
