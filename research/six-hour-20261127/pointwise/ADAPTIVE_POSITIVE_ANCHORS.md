# Positive anchors for ordinary inverse minima

Let $U(x)=(3x+1)/2^{v_2(3x+1)}$ on positive odd integers. A path with $q$ odd departures has $q$ exact division exponents $e_i\ge1$, with physical clock $d=\sum e_i$. $M_R(X)$ is the least positive odd source reaching the odd target $X$ in at most $R$ odd departures, with no bound imposed on $d$.

## Positive projection at any supplied ordinary endpoint

**Theorem 1.** Fix positive odd $a<X$ and integers $R\ge0,z\ge1$ with $X-a=2\cdot3^R z$. For any source cutoff $N\ge1$, every $y\le N$ reaching $X$ in $q\le R$ departures projects to a positive odd $w$ reaching $a$ with the same exponent word, and
\[
      y=w+2^{d+1}3^{R-q}z,\qquad w\le\lfloor Na/X\rfloor.
\]
Conversely every such actual hit of $a$ from one of the indicated $w$ lifts with the displayed formula. Retain exactly those lifts at most $N$. The result includes the empty word. For the minimum, only the first visit to $a$ from each $w$ is required.

Indeed the inverse exponent-$e$ branch $I_e(v)=(2^ev-1)/3$ multiplies the displacement by $2^e/3$. After $j$ inverse edges it is $2^{E_j+1}3^{R-j}z$. The next divisibility test therefore agrees while $j<R$, and each displacement stays even. At a legal positive odd anchor the inverse numerator $2^ev-1$ is a **positive odd** integer, since $v\ge1$ and $e\ge1$. Dividing by three when integral leaves a positive odd integer. This proves both directions at every intermediate step, including the last funded division. The earlier source is $w=\beta a-c$ for $\beta=2^d/3^q$ and $c\ge0$, by composing the inverse letters. Thus $w\le\beta a$ and $y=w+\beta(X-a)$ imply $Xw\le ay$. If $w$ visits $a$ again, the additional segment is a positive cycle at $a$. Its inverse multiplier is $\prod(3v+1)/(3v)>1$, by telescoping around the cycle. Its later lift is strictly larger since $X>a$.

For **any** supplied positive odd target $X$ and budget $R$, the least positive odd representative of its class modulo $3^R$ is at most $2\cdot3^R-1$; if it is below $X$, the theorem applies with that representative. For an arbitrary fixed ordinary start $N$ and any of its actual odd forward endpoints $X$, the criterion therefore tests all budget-limited smaller visitors by forward iteration of at most $\lfloor Na/X\rfloor$ candidate integers through $R$ departures. If the representative equals $X$, choosing it gives no reduction. The procedure requires no convergence assertion for the smaller sources. Taking $N=X$ gives a uniform fixed-positive-anchor conclusion. For each fixed $a$, the finitely many odd $w\le a$ have at most one first-visit word to $a$. For all sufficiently large $R$, all first visits that exist are in budget, and $M_R(a+2\cdot3^Rz)$ is obtained from the least slope among those words, with the least $w$ as tiebreaker, uniformly over $z\ge1$. This is a finiteness assertion: an unconditional algorithm deciding that a specific unbounded orbit never hits $a$ is not part of it. Every supplied finite $R$ is decidable by the preceding finite forward scan. The signed original-depth correspondence in Paper 108 is a close antecedent. [Paper 108/v1, Lemma 2](https://rstation.ai/problems/collatz/papers/108)

## A positive displacement at every matching-depth cut for the 17-cycle

Use the seven-phase notation of the baseline theorem. Write $t_i=(17,25,37,55,41,61,91)_{i\bmod 7}$ for its forward odd phases. Take an endpoint $t=t_a$, corresponding physical prefix $h$, and $R=7k+a\ge7$, $H=11k+h$. Here the principal path uses all $R$ departures. For any $z\ge1$ put
\[
              X=2\cdot3^Rz-t,\quad n=2^{H+1}z-17.
\]
The baseline gives $M_R(X)=n$, attained by the $R$-step lift from signed $-17$.

**Theorem 2.** Every $R$-step ancestor $u$ of $X$ is the principal $n$ or has the form
\[
                  u=2^D n+c,\qquad D\in\mathbb Z_{\ge1},\quad 0<c<17\cdot2^D,
\]
where $c$ is odd and $m=17\cdot2^D-c$ is its reflected positive magnitude. If the competing word has physical clock $d$, then $D=d-H$. The strict lower bound on $c$ is essential for the further positive anchor below.

Let $f(v)=1-1/(3v)$ and let the inverse exponents run from $t$. The signed inverse magnitudes satisfy $v_i=(2^{e_i}v_{i-1}+1)/3$. Hence $2^{e_i}/3=(v_i/v_{i-1})f(v_i)$. In the ratio of two equal-depth multipliers all common initial inverse edges cancel. If a distinct signed word departs the cycle with $b\ge1$ departing odd edges left, its subsequent $b$ signed odd magnitudes are distinct and off-cycle and have first forward cycle entrance at phase $t_{b\bmod7}$. The reference path uses the remaining same $b$ edges to terminate at 17. Consequently its factors are exactly $f(t_0),\ldots,f(t_{b-1})$, in reverse order. If the distinct signed word never departs, the determinism of the cycle gives exactly the principal path. Distinct paths that re-enter the cycle in reverse, or repeat a signed off-cycle magnitude, would give an off-cycle forward image of a cycle and cannot occur.

The following finite classification is of all positive odd $u\le91$ outside the cycle, by their first marked odd phase under the reflected map. Every missing $u$ enters a disjoint explicitly detected cycle.

| First marked phase | All off-cycle $u\le91$ in this class |
|---:|---|
| 17 | 21, 23, 31, 83 |
| 25 | 45, 67 |
| 37 | none |
| 55 | none |
| 41 | none |
| 61 | 33, 49, 73 |
| 91 | none |

For the given entry class, sort its listed small magnitudes and append $93,95,97,\ldots$. Let $L_b$ be the product of $f$ at the first $b$ elements of this list. This bounds the true off-cycle product **below** since $f$ is increasing. Exact rational arithmetic gives
\[
         L_b>\prod_{i=0}^{b-1}f(t_i)\qquad(1\le b\le14).
\]
The smallest ratio is the $b=7$ ratio, exceeding $1009/1000$. For $b\ge8$, the next seven appended elements in the same class are all at least $93$; the seven next reference phases are at most $91$. Thus propagation by seven proves the strict inequality for every $b$. Telescoping gives
\[
       2^{d-H}=(m/17)\,\frac{\prod_{\rm off} f}{\prod_{\rm ref} f}>m/17.
\]
Every off-cycle magnitude lies above 17 by the finite classification. Therefore $d-H$ is a positive integer and $m<17\cdot2^{d-H}$. The ordinary displacement at original depth $R$ gives $u+m=2^{d-H}(n+17)$. This proves the theorem at every phase, including the case where the signed path's first visit to 17 comes strictly after its original arrival at $t$.

## A second ordinary anchor protects as many extra steps as $v_3(n)$

**Theorem 3.** In the matching-depth setup of Theorem 2, for every $s\ge0$ satisfying $3^s\mid n$,
\[
                              M_{R+s}(X)=n.
\]
For $s\ge1$, the cofactor $z$ is necessarily a unit modulo three. The original terminal congruence at $-t$ then has exactly rank $R$; none of the extra $s$ inverse steps can be obtained by applying the first signed correspondence past its hypotheses.

Any possible cheaper witness through extra depth $j$, $1\le j\le s$, reaches an $R$-step cut $u$. A principal cut $u=n$ has no proper odd ancestor because $3\mid n$. At a distinct cut write $u=2^D n+c$ as in Theorem 2. Since $3^j\mid n$ and $D\ge1$, transport these $j$ remaining ordinary inverse exponents to the *positive odd* anchor $c$. Their endpoint $w$ is positive odd, $U^j(w)=c$, and if $E$ is their total division exponent,
\[
               y=(2^{D+E}/3^j)n+w,\qquad 0<w<(2^E/3^j)c.
\]
The strict upper bound holds because $j>0$ and each inverse affine letter subtracts a positive constant. A cheaper $y<n$ would imply $2^{D+E}/3^j<1$, hence
\[
                     1\le w<c/2^D<17.
\]
Follow all eight odd $w\le15$ to 1 using exact positive ordinary steps, including the fixed point $U(1)=1$. Their complete odd forward union is
\[
                 \mathcal C=\{1,3,5,7,9,11,13,15,17,23,35,53\}.
\]
Thus $c\in\mathcal C$, $2^D<c\le53$, and $1\le D\le5$. It remains a finite test. For each such $D$ and $c\in\mathcal C$ with $2^D<c<17\cdot2^D$, start the reflected odd dynamics at $m=17\cdot2^D-c$ and stop at the first 17 or repeated state. A compatible first 17 entrance with odd count $b$ and physical clock $e$ would require $b=7\ell$ and $e-11\ell=D$. To see this, continue the signed path and the reference from their common $t$ to a later 17, then use the uniqueness of the signed period. Any earlier visits to 17 precede that endpoint by full laps. Among the tested first arrivals only $(D,c,b,e)=(1,17,0,0),(2,35,7,12)$ have $7\mid b$, and neither matches its $D$. All other such candidates are excluded by a different residue or a disjoint cycle. This exhausts every cheaper visitor and proves the equality. The finite checks run over the full positive cheap pool and the complete indicated signed states, without a conjectural termination assumption.

A fixed-cofactor example makes the extra range unbounded. Take $t=25$, $z=17$, $k=2(3^{5j}-1)/11$, $j\ge1$, so $R=7k+1$ and $H+1=2\cdot3^{5j}$. As $3^5\equiv1\pmod{11}$ these are integers. Now $n=17(4^{3^{5j}}-1)$ has $v_3(n)=5j+1$ by $v_3(4^b-1)=1+v_3(b)$, which follows by repeated cubing. The opposite primitive-cofactor family $3^s\mid n+1$ in the extra-budget note attains the exact contracted value $(2/3)^s(n+1)-1$. The additional source-side digits can thus enforce opposite extremal behaviors at the same named terminal phase and budget.

Paper 1/v3 proves protection through $r+k$ when $3^k\mid n$ for observed safe words using only exponents one and two with no successive twos, subject to its starting conditions. The full repeated seven-phase word here includes exponent four. The comparison and ordinary finite-pool proof above concern this word and all its marked phases. [Paper 1/v3, introduction and extra-depth theorem](https://rstation.ai/problems/collatz/papers/1)

## General source-side positive residues

**Theorem 4.** Keep the matching-depth seven-phase setup, and let $A$ be a positive odd ordinary integer with $A<n$ and $3^s\mid n-A$. For every candidate $y\le n$ with $R+j$ steps, $0\le j\le s$, let $D,c$ be those of Theorem 2, also allowing $D=c=0$ for the principal cut. There is a positive odd $w<A+17$, with $U^j(w)=v_A=2^D A+c$, for which
\[
                y=\alpha(n-A)+w,\qquad \alpha=2^{D+E}/3^j.
\]
Conversely each such actual positive hit lifts with the displayed formula, provided its cut $m=17\cdot2^D-c$ actually realizes the required reflected $R$-step word of physical length $H+D$. Retain exactly the lifts with $y\le n$ as candidates. This yields a finite forward search on $w<A+17$. At fixed $A$ whose listed positive starts have finite orbits, the same finite positive pool suffices at *every* $s$ and $R$.

The cut displacement $u-v_A=2^D(n-A)$ is even and a multiple of $3^j$; evenness holds also at $D=0$ since $A,n$ are odd. All transported inverse exponents are ordinary and positive as in Theorem 1. If $\alpha>1$, $y\le n$ forces $w<A$. If $\alpha\le1$, then $w\le(2^E/3^j)v_A=\alpha(A+c/2^D)<A+17$. For a nonprincipal cut $v_A\ge2^D A$, so its finite forward maximum bounds $D$. Repeated visits from the same $w$ to any $v_A$ add a positive cycle and increase $\alpha$; they cannot improve the minimum. With no knowledge of all-time termination for the pool, following its members for the indicated finite $s$ still decides the supplied instance. For each such hit, $D\le\log_2(v_A/A)$ is a finite test, $c=v_A-2^DA$ is determined and the required reflected word can be checked directly at the supplied $R$. Checking the principal baseline separately takes care of all depths through $R$.

The endpoint projection in Theorem 1 applies to one arbitrary ordinary source and one arbitrary actual endpoint. The stronger seven-phase source-side estimates require the specified matching-depth cylinder. None of these results forces a cheaper visitor within these budgets at some point of every positive orbit.
