# The complete denominator and the possible clock gcds near one odd octave

Let a positive rational shortcut cycle have least period $h$, odd count $p$, determinant $D=2^h-3^p$, least odd state $m_0$, odd ratio $R$, and common reduced denominator $q$. Write
\[
 g=\gcd(h,p),\qquad a=h/g,\quad b=p/g,\quad
 \gamma=\log_2 3,\quad \Lambda=h-p\gamma,\quad
 \eta=\max(0,\log_2 R-1).
\]
Our main regime is $h\to\infty$, $m_0\ge h^{2-o(1)}$, $R\le2+h^{-1+o(1)}$. No restriction is placed on $g$, on the number of altered ranks, or on which visits to those ranks are altered. A divisor $k$ of $g$ is called active if a periodic rank sequence defined below has a nonzero Fourier coefficient of order $k$. The order one is always active. If $\mathcal A$ is the set of active orders and $J=\sum_{k\in\mathcal A}\varphi(k)$, then
\[
                 \log_2 q=(1+o(1))aJ,\qquad
                 \operatorname{lcm}(\mathcal A)=g.                     \tag{1}
\]
In particular prime $g$ forces $\log_2 q/h\to1$, including the fixed primes two and three. For $g=\ell^v$ one has $\log_2q/h\ge1-1/\ell-o(1)$. The [coprime resultant](COPRIME_NEAR_OCTAVE.md) gives a better error term when $g=1$.

An existence criterion follows for any prescribed sequence of positive integers $G_i$. Put $L_i=\max_{\ell^v\parallel G_i}\ell^v$, the largest full prime-power divisor, with $L_i=1$ if $G_i=1$. There are positive primitive rational cycles satisfying the main regime, with $\gcd(h_i,p_i)=G_i$ and $\log_2 q_i/h_i\to0$, **if and only if**
\[
                             G_i/L_i\to\infty.                          \tag{2}
\]
The statement concerns existence among rational cycles. The denominator scales do not give integer cycles.

## Rank columns and the exact inactive divisor

Root the odd word at $m_0$. Write $E_i$ for the cumulative odd division counts before odd phase $i$. Set $r_i=ia\bmod b$ and $d_i=\lfloor ia/b\rfloor-E_i$, with $0\le i<p$ and periodic extension of $d_i$. The [physical clipping argument](NEAR_OCTAVE_PACKING.md) shows, when $\eta+\Lambda<1/4$, that the only nonzero $d_i$ are $+1$ at $0\le r_i\le b(\eta+\Lambda)$ and $-1$ at $b(1-\Lambda)\le r_i<b$. These intervals are disjoint.

Choose integers $u,v$ with $ub+va=1$, put $i_r=vr\bmod b$ in $[0,b)$, and define
\[
 S_r(W)=\sum_{j=0}^{g-1}2^{-d_{i_r+jb}}W^j\quad (0\le r<b).
\]
Thus a column records the native rank on successive traversals of the reduced clock. For each $k\mid g$, let $k\in\mathcal A$ iff some $S_r(\zeta_k)\ne0$ at a primitive $k$th root of unity. This criterion is independent of the chosen conjugate. Every constant column has only its order-one component.

Write $A=2^a$, $B=3^b$, $w=A/B$, $X=2^{-u}3^{-v}$ and $F_k=B^{\varphi(k)}\Phi_k(A/B)$. Thus $\prod_{k\mid g}F_k=D$. Each $F_k$ is a positive integer prime to six. The equalities $X^b=w^v/2$ and $X^a=w^{-u}/3$ hold in $\mathbb Z[1/6]$. If $C=\sum_{i=0}^{p-1}3^{p-1-i}2^{E_i}$ is the full carry, then
\[
   3^{1-p} C=\sum_{r=0}^{b-1} X^r w^{-\lfloor vr/b\rfloor} S_r(w).    \tag{3}
\]
Indeed $v\lfloor ia/b\rfloor+ui=(i-vr_i)/b=j-\lfloor vr_i/b\rfloor$ for $i=i_{r_i}+jb$. If $k$ is inactive, $\Phi_k$ divides every $S_r$. All inactive cyclotomics together divide each $S_r$ in $\mathbb Z[1/2][W]$, by monic division and coprimality over $\mathbb Q$. Evaluation in (3) gives
\[
       \prod_{k\notin\mathcal A,\ k\mid g}F_k\mid C,\qquad
       q\le\prod_{k\in\mathcal A}F_k.                                  \tag{4}
\]
This uses the simultaneous polynomial divisor and remains valid if different integer values $F_k$ have common prime factors.

The least joint period in $j$ of all column sequences is $\operatorname{lcm}(\mathcal A)$, by finite Fourier inversion. If this integer were a proper divisor $l$ of $g$, then $d_{i+bl}=d_i$, and so the odd word $e_i=\lfloor(i+1)a/b\rfloor-\lfloor ia/b\rfloor+d_i-d_{i+1}$ would repeat after $bl$ odd phases. Its shortcut word would repeat after $al<h$ steps. A repeated parity word has a unique rational fixed point already at the shorter period, by the affine formula: the shorter slope is a positive power of $3$ divided by a positive power of $2$ and differs from one. This contradicts primitivity. It also shows how restricting to the least period enters (1).

## A short polynomial on each active component

Put $s=\lceil b(\eta+2\Lambda)\rceil+4$. For a fixed active $k>1$ work over $K=\mathbb Q(\zeta_k)$. The map $\mathbb Z[\zeta_k]\to\mathbb Z/F_k$ taking $\zeta_k$ to $w$ is well-defined, with denominators two and three invertible in the target. In (3) the constant entry one of each column contributes $\sum_{j<g}\zeta_k^j=0$. For each low rank let $J_r$ be the $0$–$1$ polynomial selecting dates with $d_i=1$, and for each high rank the one selecting dates with $d_i=-1$. After multiplication by two, the remaining terms of (3) are
\[
 \begin{cases}
 -X^r\zeta_k^{-\lfloor vr/b\rfloor}J_r(\zeta_k),&r\text{ low},\\
 X^{r-b}\zeta_k^{v-\lfloor vr/b\rfloor}J_r(\zeta_k),&r\text{ high}.
 \end{cases}                                                           \tag{5}
\]
The identity for the high terms uses $2X^r=w^v X^{r-b}$. All exponents of $X$ in (5) are distinct and lie in an interval of width $<s$. The resulting Laurent polynomial is nonzero by activity. Shift the least exponent to zero to give $H_k(T)\in \mathbb Z[\zeta_k][T]$ of degree at most $s$. Its evaluation at $X$ represents $C$ up to a unit modulo $F_k$. Every conjugate of each coefficient has modulus at most $g$.

For $k=1$, $F_1=A-B$, $w=1$ in its residue ring, and $X^b=1/2$. Hence $1-X$ is a unit there, even over the full composite modulus. Apply $2(1-X)$ to (3): the baseline of $g$ complete rank sums gives $g$ and the signed low and high selectors enter as in (5), multiplied by $1-X$. The integer Laurent polynomial evaluates to $g$ at $T=1$ and is nonzero. After shifting, the degree is at most $s$ and the coefficients are at most $3g$ in absolute value. These constructions include constant nonzero $H_k$ and $F_k=1$.

## Two independent short clock relations

Fix $\nu>4.1163051$ and $\delta=1/(1+\nu)$. For $\Lambda<1/4$ and large $b$, the rank-two integer lattice
\[
            \mathcal L=\{(bi+aj,j):i,j\in\mathbb Z\}
\]
has a basis whose two vectors have Euclidean length $O_\nu(b^{1-\delta})$. To see this, a vector of norm $M\ge1$ has $|i|\ll M$ and
\[
 |i+j\gamma|\le M/b+M\Lambda/p\ll M/b.
\]
Wu and Wang's homogeneous specialization gives $|i+j\gamma|\gg_\nu M^{-\nu}$ for any such nonzero vector. Thus a shortest vector has norm $\gg_\nu b^\delta$. Dirichlet approximation gives a nonzero vector of norm $O(\sqrt b)$ by considering $j$ up to $\lceil\sqrt b\rceil$. The shortest vector is primitive in this lattice and can be completed to an integral basis. The perpendicular component of the other basis vector has length $b/M$, the covolume divided by the first length. Reduce its parallel component to at most $M/2$ by an integral multiple of the first vector. This gives the asserted common bound $L\ll_\nu b^{1-\delta}$. [Wu and Wang, Theorem 1](https://doi.org/10.1016/j.jnt.2014.03.007)

For each of those two vectors $(t,j)$, $t=bi+aj$, the evaluated relation is
\[
                 X^t=2^{-i}3^{-j}w^{vi-uj}.
\]
For large $b$ one has $t\ne0$: otherwise $b\mid j$ and a nonzero such vector has norm at least $b$. Clear the Laurent monomial and powers of two and three to obtain two binomials $P_1,P_2\in\mathbb Z[\zeta_k][T]$. They vanish at $X$ modulo $F_k$, have degree $O_\nu(L)$ and conjugate coefficient sums at most $\exp(O_\nu(L))$. Both constant terms are nonzero. The two binomials have no common algebraic root. Otherwise raising their two relations to each other's exponents yields that $2^{i_1t_2-i_2t_1}3^{j_1t_2-j_2t_1}$ is a root of unity. Both integer exponents must be zero, contrary to independence of the basis vectors. This argument allows arbitrary algebraic-integer coefficients in $H_k$, including endpoints with nonzero ternary valuation.

Each root of $H_k$ rules out at most one integer $\lambda$ in $P_1+\lambda P_2$. Choose an integer $1\le\lambda\le s+1$ avoiding the roots. This linear combination is a nonzero polynomial (the two binomials are independent) and its resultant with $H_k$ is nonzero. Its reduction and the reduction of $H_k$ both vanish at $X$ modulo $\gcd(F_k,C)$. The integral Bézout identity for the resultant then gives
\[
 \gcd(F_k,C)\mid
 |N_{K/\mathbb Q}\operatorname{Res}(H_k,P_1+\lambda P_2)|.
\]
Indeed the resultant lies in the kernel of the evaluation homomorphism to that residue ring, and its norm is its product with other algebraic integers, hence also maps to zero. A constant $H_k$ can equivalently be bounded by its own nonzero norm.

For each conjugate use $|\operatorname{Res}(H,P)|\le\|P\|_1^{\deg H}M(H)^{\deg P}$, with $M(H)\le\|H\|_2\le3g\sqrt{s+1}$. This proves uniformly in all active orders that
\[
 \log\gcd(F_k,C)
 \ll_\nu \varphi(k)\,[s(L+\log(2+s))+L\log(2g(s+1))].                 \tag{6}
\]
For $k>1$, $(A/2)^{\varphi(k)}\le F_k\le (2A)^{\varphi(k)}$. The lower bound follows by setting $t=B/A\in(0,1)$ and using $|1-t\zeta|\ge |1-\zeta|/2$ on each primitive root, together with $|\Phi_k(1)|\ge1$. The order one satisfies $\log_2F_1=a+O_\nu(\log(2b))$ by Wu–Wang applied to $a\log2-b\log3>0$.

In particular equations (1) hold whenever $b\to\infty$, $\eta+\Lambda<1/4$ and $s+\log(2g b)=o(b^\delta)$. In this range the bracket of (6) is $o(b)$, uniformly in $k$. Combine (4) with the lower bound
\[
              q\ge\prod_{k\in\mathcal A}F_k/\gcd(F_k,C),
\]
which follows valuation by valuation even for overlapping numerical factors. The accumulated error is $o(b)J$, relative to the active degree. In the main regime one has $\eta+\Lambda\le h^{-1+o(1)}$ from the summed physical corrections, hence $s=h^{o(1)}$. Reduced power separation gives $b\ge h^{2/(1+\nu)-o(1)}$ as detailed in [the packing argument](NEAR_OCTAVE_PACKING.md). Therefore the stated sufficient range holds.

## Which gcd sequences admit small rational denominators?

Suppose first that such cycles exist. Some active order is divisible by the full largest prime power $L_i$, because the active orders have lcm $G_i$. Its totient is at least $\varphi(L_i)\ge L_i/2$. The case $G_i=1$ has $J=1$. Thus (1) proves necessity in (2).

Conversely, for each $G=G_i$ write its distinct primary factors as $M_1,\ldots,M_r$. In the [independent-cell construction](INDEPENDENT_CLOCKS.md), use $r$ disjoint mechanical-cell substitutions $10\to01$. Activate marker $j$ exactly in cells whose index is divisible by $M_j$. The argument there for physical admissibility and minimal period requires that these indicator periods be exact and have lcm $G$; it works for every prime power, including powers of two and three. In detail, for an upper convergent cell count $(n,b_0)$ with $\gcd(n,b_0)=1$, the full word has length $Gn$, weight $Gb_0$, and positive determinant. Any repetition multiplicity divides both counts and hence divides $G$, so an actual period shortening is a whole-cell shift. Every marker can be read from its own two sites, forcing such a shift to be divisible by each $M_j$.

Choose the upper convergent length $n$ larger than $G^i$, increasing further to fit the $r$ prescribed marker phases $1/n,\ldots,r/n$ and to make $n\to\infty$. The height calculation in that construction uses the estimate $0<n\log2-b_0\log3\ll1/b_0$, the number $r$ of slots, and the total number $G$ of cells. It yields $m_0\ge (Gn)^{2-o(1)}$, $R\le2+(Gn)^{-1+o(1)}$ and $\Lambda\le(Gn)^{-1+o(1)}$. All odd exponents are one and two. These estimates allow an arbitrary prescribed sequence $G_i$ in (2).

At cell boundaries the affine recurrence is $A x_{j+1}=B x_j+c_j$ with $A=2^n$, $B=3^{b_0}$ and $c_j=c_*+\sum_l d_l\mathbf1_{M_l\mid j}$. Each individual additive forcing of period $M_l$ has a rational periodic solution with denominator dividing $A^{M_l}-B^{M_l}$. Superposition and uniqueness at the full period show
\[
    q\ \mid\ \prod_{l=1}^r(A^{M_l}-B^{M_l}).
\]
The constant forcing has denominator dividing $A-B$, already a divisor of each factor. In stating this product one can add the constant forcing to any one of the $r$ periodic forcings before taking denominators. Consequently $\log_2q/(Gn)\le\sum_l M_l/G$. For bounded $r$ this tends to zero by (2). For $r\to\infty$ it is at most $r/2^{r-1}$. Splitting at any fixed upper bound on $r$ proves the limit without assuming $r$ converges. This proves sufficiency.

Prior repository work used cyclotomic resultants and Parseval for two equal-clock templates with a binary selector, proving full rate at prime block counts. It also used one short clock relation for monic unit-endpoint factors. Here the physical ranks yield many simultaneous selector columns, the active numerical factors have one *uniform relative* error, and a second independent short relation handles arbitrary coefficient endpoints in their changing cyclotomic fields. These steps give (1) and the exact realizability distinction (2). Both are written results using the stated published two-logarithm input. [Earlier block selectors and single-resultant bounds, §§2–4](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-ordinary-boundary-20261124/arithmetic/README.md)

## The sharp minimum at every prescribed gcd

There is also a closed formula for the best possible leading rate in (1):
\[
  J\ge J_{\min}(g):=1+\sum_{\ell^v\parallel g}\varphi(\ell^v).          \tag{7}
\]
For every prescribed sequence $g=G_i$, the main physical regime has primitive rational cycles attaining
\[
        \frac{\log_2 q_i}{h_i}
        =(1+o(1))\,\frac{J_{\min}(G_i)}{G_i}.                            \tag{8}
\]
The empty sum in (7) is zero. Thus (2) also follows from the sharp rate. For example, the minimum leading fractions at $g=2,4,6,8,9,12$ are $1,3/4,2/3,5/8,7/9,5/12$, respectively.

For the lower bound, first consider all full prime-power factors $Q_i=\ell_i^{v_i}$ with $\varphi(Q_i)\ge2$. Assign each such $Q_i$ to one active order $k$ divisible by it, which exists by the least joint period. Within each assigned nonempty group,
\[
        \varphi(k)\ge\prod_{i\text{ assigned}}\varphi(Q_i)
                        \ge\sum_{i\text{ assigned}}\varphi(Q_i).
\]
The singleton case has equality in the second comparison. The remaining cases follow from $xy\ge x+y$ for $x,y\ge2$ and induction. Together with the constant frequency this proves (7) except possibly when $2\parallel g$, where the only missing term is one.

Suppose in this last case that the one-unit saving occurs. Denote by $Q_i$ the **odd** full primary factors. If there are none, activity of order two is necessary for period two, giving (7) directly. Otherwise the charge comparison just made must be exact, with no extra active orders. Two distinct odd primary factors cannot both have totient two, as only $Q_i=3$ has that property. Thus a group with two or more assigned factors has product strictly greater than their sum. Every active nontrivial order is consequently $Q_i$ or $2Q_i$ for exactly one $i$. A partial factor from another odd prime would also increase its totient. At least one doubled order is needed to obtain lcm $g$.

Because each physical rank permits at most one sign of exception, after a rank-dependent translation and scaling every nonconstant column is a binary function. Those changes preserve its nontrivial active orders. On such a column use the CRT coordinates $j\bmod2$ and $j_i=j\bmod Q_i$. Fourier modes of order $Q_i$ are functions only of $j_i$ with mean zero. Modes of order $2Q_i$ are $(-1)^j$ times such mean-zero functions. Complex conjugate modes combine to real functions since the column is real. Its value therefore has the form
\[
 f(j)=c+\sum_{i\text{ undoubled}}A_i(j_i)+(-1)^j\sum_{i\text{ doubled}}B_i(j_i).
\]
Hold the parity fixed, leaving all the $j_i$ free independently. If at least two summands are nonconstant, their sum takes at least three distinct real values, by varying each between its minimum and maximum. This contradicts binarity. A column containing a doubled order must hence be $c+(-1)^j B_i(j_i)$. Looking at the two signs for a point with $B_i\ne0$ gives $c=1/2$. Binarity at every point now gives $B_i(j_i)\in\{-1/2,1/2\}$ at every point, incompatible with zero mean on the odd-sized set of residues modulo $Q_i$. No column can contain the required doubled order. This excludes the saving and completes (7).

For attainment use the same distinct marker slots in the construction above. Modify the indicator for each $Q=\ell^v$ to the cyclic interval $0\le j\bmod Q<Q/\ell$. Its list of one-period coefficients has polynomial $1+W+\cdots+W^{Q/\ell-1}$. On the $Q$th roots it is nonzero exactly at order one and at the primitive order $Q$; repetition to length $G_i$ preserves precisely these orders. Its least period is $Q$. The earlier native period and height calculations use only the allowed independent slot displacements and their least joint period, so are unchanged.

Take a fixed odd phase in each length-$n$ cell as the initial root, chosen away from the marked swaps (increase $n$ if necessary). A disjoint $10\to01$ moves the date of one specified odd occurrence by one without altering the date of any other odd occurrence. In this rooting each nonconstant column $2^{-d_{i_r+jb}}$ is thus a nonzero scalar multiple of $1+\mathbf1_{0\le j\bmod Q<Q/\ell}$, up to a cyclic translation of $j$. Its constant and primitive-$Q$ components are nonzero. All other columns are constant. Re-rooting the odd cycle permutes its $b$ reduced rank classes. Within a fixed rank it cyclically translates the $j$-coordinate and adds a rank-dependent integer to $d$: the floor difference $\lfloor(i+i_0)a/b\rfloor-\lfloor ia/b\rfloor$ depends only on the reduced rank of $i$. Hence re-rooting at the true minimum preserves the union of active orders. It follows that $\mathcal A=\{1\}\cup\{Q:Q\parallel G_i\text{ is a full prime power}\}$. If $G_i=1$, use the unchanged primitive mechanical cell. This proves (8).

The least rational representation dimension for a given cyclic order is the classical crystallographic restriction, and the cyclotomic rank description for arbitrary periodic integer sequences is also established. The last binary parity step and realization by admissible rank columns distinguish (7)–(8) from those unrestricted dimension statements. [Hiller, *The crystallographic restriction in higher dimensions*](https://doi.org/10.1107/S0108767385001180) · [Kreczman, Prigioniero, Rowland and Stipulanti, §§4–5](https://orbi.uliege.be/bitstream/2268/300422/1/paper-conf2023.pdf)

[Exact spectral replay](check_spectral.py) checks the complete determinant and inactive divisibility on 16 native positive rational cycles through period 14,550. For every $1\le g\le16$ it also enumerates every binary word and closes its actual support under arbitrary unions of columns, checking 131,070 words. A second recurrence enumeration proves the finite minimum over arbitrary column collections at 34 selected gcds through 210. It exhausts all smaller candidate frequency subspaces attaining the requested lcm and separately verifies attainability. [Archived controls](../../../reports/astra-infinite-descent-20261127/cycles/SPECTRAL_CONTROLS.json)
