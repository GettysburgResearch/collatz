# Sharp parity prices at every finite digit width

**Written theorem with the classical equidistribution input of the companion rigidity proof.** Use the shortcut map $T$, radix $p$, radius $r$, degree $D$, integer digit features $\Phi$ and parity $e$ of the [finite certificate theorem](DIGIT_RANKING_FINITE_WITNESSES.md). A bare score is $F=\theta\cdot\Phi$, without an additional arbitrary bounded term. The smallest $q$ for which a bare score satisfies
\[
                   F(Tn)-F(n)\le q-e(n)
\]
is a rational number $q_{p,r}$, independent of $D$ and of the input floor. The same number results if the test is restricted to sources prime to three. The minimum is attained by a radius-$r$, degree-zero score nonincreasing in the ordinary integer argument, valid simultaneously at **all positive integers**. At every fixed floor the supremum of the odd fractions of finite integer-weighted actual unit witnesses balancing all of $\Phi$ is also $q_{p,r}$. We do not need attainment of this latter supremum. For $r=0$ one has $q_{p,0}=1$. For $r\ge1$ and $M=p^{2r-1}$,
\[
      \log_3 2<q_{p,r}\le\log_3 2+\frac{\log(1+1/M)}{\log3}.          \tag{1}
\]
For ternary digits, a single finite deterministic integer orbit computes $q_{3,r}$ exactly. At widths three, five, seven, nine and eleven it gives respectively $2/3,7/11,12/19,171/271,983/1558$. The result gives sharp bare prices. The externally allowed bounded-correction family of the [root theorem](../root/DIGIT_POLYNOMIAL_RANKING.md) attains the smaller critical price $\log_3 2$. Earlier explicit ternary certificates for small widths, including the floor restrictions on width five, are due to [Paper 189, version two](https://rstation.ai/problems/collatz/papers/189).

## The same radius throughout polynomial degree reduction

For $r\ge1$ set $K=2r$. Any bare score having both branch increments bounded above on sufficiently high unit inputs has the exact form
\[
 F(n)=\gamma L(n)+A(h(n))+B(n\bmod p^K)\qquad(L(n)\ge K+1).          \tag{2}
\]
Here $h(n)$ is the integer specified by the most significant $K$ digits. The prior unit-core argument supplies the bulk coboundary at each degree and forces the highest boundary coefficient to be constant. We specify why that reduction preserves $r$ and separates the two endpoint functions.

At degree $d\ge1$ the interior positions are $i=r,\ldots,L-1-r$. The coboundary vertices $h_i$ in the summation-by-parts identity are words of length $2r$. Each remaining summand of degree at most $d-1$ uses a vertex contained in the original radius-$r$ window at its own position. If the first such interior position must be omitted or restored, the discrepancy has fixed index and reads only bottom digits. The lower endpoint in summation by parts reads digits $0,\ldots,2r-1$; so do all the original lower sentinel contributions. All resulting bottom terms have bounded indices and are a function of the last $K$ digits. Every upper sentinel contribution, and the upper de Bruijn endpoint, reads at most the first $K$ digits. The resulting upper polynomials in $L$ of degree $\le d-1$, with coefficient depending on those digits, are represented at $i=L-r$: its window has exactly one upper sentinel, at the uppermost position, and reads digits $L-2r,\ldots,L-1$. Insert the required polynomial in $i+r=L$ there. A bottom endpoint function is likewise represented at $i=r-1$, with a unique lowest sentinel and the entire bottom $K$-tuple. In particular degree reduction introduces no product of the two ends. The constant top term times $L^d$ is represented as the sum of $(i+1)^d-i^d$. All identities apply for $L\ge2r+1$; shorter inputs form a finite exception which never enters the high-input rigidity argument. Iterating down to the degree-zero coboundary gives (2). For $r=0$ there are no endpoint windows and the one-vertex interior graph has only constant cohomologous weights: the same reduction gives exactly $\gamma L$ at sufficiently large inputs. High odd inputs with unchanged length then force $q\ge1$, attained by zero.

## Finite leading-digit graph

Put $M=p^{K-1}$ and partition the positive reals into cells
\[
           C_{j,h}=[p^j h,p^j(h+1)),\qquad M\le h<pM,\ j\in\mathbb Z.
\]
Let $c_0=1/2$ and $c_1=3/2$. Form the finite directed graph on these $h$ with a separate edge $(h,h',k,e)$ for each strict interior intersection $c_e C_{0,h}^{\circ}\cap C_{k,h'}^{\circ}\ne\varnothing$. It has $k\in\{-1,0,1\}$. An endpoint at precisely a boundary is assigned the right-hand labels, realized at all sufficiently small positive perturbations. The integer $k$ is the change in physical digit length under the ideal scaling. The graph can be constructed using rational comparisons alone.

An eventual true price bound on unit sources, using (2), requires, for suitable $\gamma,V$,
\[
              \gamma k+V(h')-V(h)\le q-e
                          \qquad\text{on every graph edge}.             \tag{3}
\]
Indeed fix one open leading transition. Every compatible finite low pair for that branch occurs with these leading labels on arbitrarily high unit inputs by the Chinese remainder theorem: the mantissa interval grows proportionally to source height, and the positive odd correction is relatively vanishing. The low increment $B(\mathrm{out})-B(\mathrm{in})$ has a nonnegative possible value on each branch separately. On the odd branch choose the fixed class $-1$ at both ends by taking $n=-1\bmod 2p^K$ and $n=-1\bmod3$. On the even branch keep the lower binary factor zero and divide repeatedly by two modulo the entire odd part of $p^K$ and modulo three, starting from a ternary unit; this gives a finite cycle of accessible low pairs. The binary input may be chosen zero through one extra bit. Some cycle increment is nonnegative by telescoping. Choosing that low pair with the prescribed high edge proves (3), with $V=A$.

Conversely suppose (3) holds with $q\le1$. The lifted piecewise constant function $F_0(x)=\gamma j+V(h)$ on $C_{j,h}$ satisfies $F_0(c_e x)\le F_0(x)+q-e$ for every real $x>0$, by the right-hand convention. Iterating the ideal odd inequality and using $F_0(x)=\gamma\log_p x+O(1)$ gives $\gamma\log_p(3/2)\le q-1$, hence $\gamma\le0$. The finite tail envelope
\[
                        F_*(x)=\sup_{u\ge x}F_0(u)
\]
is nonincreasing, constant on each of the same cells, and obeys $F_*(px)=F_*(x)+\gamma$. By substituting $u=c_e v$ in the supremum it satisfies the same ideal inequalities. Since $Tn\ge c_{e(n)}n$, monotonicity proves the true price bound at every positive integer.

On numerals of length $L\ge K$, this score equals $\gamma L$ plus a leading-$K$ function, realized by a constant per digit and the one-upper-sentinel window at $i=L-r$. On a shorter numeral there exists a genuine position whose window sees both sentinels and every digit, since $L\le2r-1$: choose $i=\max(0,L-r)$. That marked window specifies the length, all digits and its own position, and never occurs on a longer numeral. Assign the remaining correction just at that window. This realizes the same function exactly as a bare degree-zero score on every positive integer. For $q\ge1$ the zero score already works.

The finite program minimizing $q$ in (3) is feasible at $q=1$. The finite-witness result bounds it below by $\alpha=\log_3 2$. A bounded-below finite rational linear program has an attained rational optimum. Since its feasible critical score would contradict the unit-core critical obstruction, the optimum is strictly greater than $\alpha$. Its usual finite linear-program dual maximizes $\sum\lambda_e e$ over nonnegative edge flows of total mass one, conserving mass at every vertex and with $\sum\lambda_e k=0$. These are leading-cell flows. They need not balance the original interior digit counts of their separate integer representatives. For each $q<q_{p,r}$ the full actual high-unit inequalities are infeasible by (2)–(3); the coercive finite subcover and rational separation argument of the [finite-witness theorem](DIGIT_RANKING_FINITE_WITNESSES.md) supplies an actual finite integer-weighted witness of fraction $>q$. Every such witness has fraction $\le q_{p,r}$ by the globally valid bare score. This proves the asserted supremum with the full features and every floor.

For the quantitative upper choose the finite leading approximation to $-\log_3 x$ which replaces $x\in C_{j,h}$ by its left endpoint $p^jh$. The discrepancy is in $[0,\log_3(1+1/M))$ on every cell. Its ideal branch increments therefore have upper bound $\alpha-e+\log_3(1+1/M)$. This gives the upper in (1), including when that bound exceeds one.

## Exact ternary price by downward rounding

Now take $p=3$ and $r\ge1$. The odd ideal multiplier is exactly three times the even multiplier. Both have the same reachable target mantissa labels; their respective length increments differ by one. In the lifted grid $\mathcal G=\{3^j h:M\le h<3M\}$ define $Q(x)$ to be its largest member at most $x$ and set $R(x)=Q(x/2)$ for $x\in\mathcal G$. This monotone map commutes with multiplication by three. At $x=h$ it has mantissa update and positive decrement indicator
\[
       b(h)=1_{\{h<2M\}},\qquad f(h)=\lfloor3^{b(h)}h/2\rfloor,
       \qquad R(h)=3^{-b(h)}f(h).                                    \tag{4}
\]
The edge from $h$ to $f(h)$ is admissible for the even graph, including when $h/2$ is exactly a boundary, since a sufficiently small positive perturbation preserves the right-hand cell. All other possible lifted even successors from this cell are at least $R(h)$. The map $f$ has a finite forward orbit from $M$. Let its eventual cycle have period $t$, with $s$ occurrences of $b=1$ there. Then
\[
                            \boxed{q_{3,r}=s/t.}                        \tag{5}
\]

For the lower bound take these $t$ cycle edges, choosing the odd version on exactly $s$ edges. The total length change is zero and the endpoint labels balance. Summing (3) proves $q_{3,r}\ge s/t$.

For the upper, monotonicity and homogeneity give $R^n(M)\le R^n(h)\le3R^n(M)$ for every initial mantissa. Thus $n^{-1}\log_3 R^n(x)\to-s/t$ at every grid point $x$. A lifted even graph walk starting at $x$ has its $n$th location at least $R^n(x)$ by induction. Repeating any graph cycle of length $l$ and integer total length change $k$ therefore gives $k/l\ge-s/t$. At $q=s/t$ the costs $q+k_e$ on the even graph (where $k_e$ here denotes that edge's even length increment) have nonnegative sum around every cycle. The finite difference inequalities $V(h')-V(h)\le q+k_e$ have a solution: join a fresh source to all vertices at zero cost and take shortest-path distances. Set $\gamma=-1$. For the odd version the length increment is $k_e+1$ and the price decreases by one, so the same inequality gives (3). This proves (5).

Along the cycle let $\epsilon_h=\log(3^{b(h)}h/[2f(h)])$. Telescoping (4) gives
\[
             (q_{3,r}-\alpha)\log3=t^{-1}\sum_{h\text{ on cycle}}\epsilon_h.
                                                                         \tag{6}
\]
An even $h$ has $\epsilon_h=0$, and each such step decreases $v_2(h)$ by exactly one. An odd $h$ has $\epsilon_h=\log(1+1/(2f(h)))\ge\log(1+1/(6M))$. Hence every cyclic run of $1+\lfloor\log_2(3M)\rfloor$ consecutive states contains an odd one. In particular
\[
 \frac{\log(1+1/(6M))}{(1+\lfloor\log_2(3M)\rfloor)\log3}
 \le q_{3,r}-\alpha
 \le\frac{\log(1+1/(2M))}{\log3}.                                    \tag{7}
\]
This proves $\lim_{r\to\infty}(q_{3,r}-\alpha)^{1/(2r)}=1/3$ and gives a width-dependent positive margin using ordinary integer arithmetic. The graph orbit is a rounded leading-digit calculation. It establishes a bound on possible ranking functions and gives no orbit of the positive Collatz map with this odd fraction.


The [independent integer checker](check_sharp_digit_price.py) verifies the width-seven staircase potential on all 1,458 labelled leading transitions, follows the rounded orbit at widths three through eleven in the opening list, and tests the exact critical-power comparisons. Its [receipt](../../../reports/astra-global-20261128/escape/SHARP_DIGIT_PRICE_CHECKS.json) records the 19-cycle and its sorted cuts.
