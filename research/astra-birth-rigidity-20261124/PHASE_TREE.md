# A binary inverse tree in one ordinary scalar phase

**Status. Proposed constructive result and finite arithmetic certificate.** Every vertex below is a positive odd integer that reaches 1. Its actual scalar has the same canonical phase as 1. At the common counting horizon, polynomially many of these sources charge to a single endpoint.

## Construction

Use the accelerated odd map $U(t)=(3t+1)/2^{v_2(3t+1)}$ and the actual scalar $h(t)=\sum_{i\ge0}v_2(3U^i(t)+1)/3^{i+1}$. Its recurrence is $h(q)=(g+h(t))/3$ when $U(q)=t$ via gap $g$. In particular $h(1)=1$. The canonical phase is chosen in $(1/2,3/2]$, so $h(t)=1+k$ with nonnegative integer $k$ gives phase 1. Only convergent vertices and the finite scalar recurrence are needed here. [PR182, actual scalar](https://github.com/GettysburgResearch/collatz/blob/f94a2ae1caba9a1857feda892ee1779695eea9d2/research/carry-tower-round10-20261123/ACTUAL_SCALAR_FORMALIZATION.md)

Put $w=t2^{-k}$, a positive rational number with a well-defined residue modulo every power of 3. Choose a prospective child carry $d$ and set

$$
g=2+3d-k,\qquad q=(2^g t-1)/3,\qquad
w'=q2^{-d}=(4\cdot4^d w-2^{-d})/3.
$$

Divisibility of the last numerator by 3 makes $q$ an integer. For $g\ge1$ it is odd and $3q+1=2^g t$ gives its exact gap and $U(q)=t$. The scalar recurrence then gives $h(q)=1+d$.

The table has rows indexed by $w\bmod 27=r$ and columns indexed by the three lifts of $r$ modulo 81. Each cell supplies two admissible child carries $d$.

| Residue $r$ | Lift $r$ | Lift $r+27$ | Lift $r+54$ |
|---:|---:|---:|---:|
| 1 | 6, 8 | 6, 8 | 10, 16 |
| 4 | 6, 12 | 6, 10 | 6, 10 |
| 5 | 7, 13 | 7, 11 | 7, 11 |
| 10 | 6, 8 | 6, 8 | 6, 8 |
| 13 | 8, 12 | 6, 8 | 6, 8 |
| 14 | 11, 15 | 9, 11 | 9, 11 |
| 17 | 7, 9 | 7, 9 | 7, 9 |
| 22 | 10, 14 | 8, 10 | 8, 10 |
| 23 | 7, 9 | 9, 13 | 7, 9 |
| 26 | 7, 13 | 7, 9 | 9, 11 |

For each lift $v$ and entry $d$, the representative of $4\cdot4^d v-2^{-d}\pmod{81}$ in $[0,81)$ is divisible by 3 and its quotient is a row of the table. These 60 integer congruences are a finite proof obligation checked exhaustively by the accompanying program. All entries are in $[6,16]$ and every pair sums to at most 26. Starting with $t=1,k=0$ gives a row, and induction supplies two actual children per node, all with $4\le g\le50$, carry at most 16, and phase 1. Indeed $g\ge2+3\cdot6-16=4$. Also $q\ge(16t-1)/3\ge5t$, so no child returns to an ancestor. The two child gaps differ. Every child has the unique parent $U(q)$, which keeps all branches and levels distinct. There are exactly $2^n$ vertices of depth $n$ in this selected tree.

## Many bounded sources charge to the same endpoint

Let $\alpha=\log_2 3$, $\delta=1/(28-\alpha)$, and $c(d)=2^{2+2d}/3$. The real identity for $w'$ gives $w'<c(d)w$. For a node with prescribed children $d_1,d_2$, convexity and $d_1+d_2\le26$ give

$$
 c(d_1)^{-\delta}+c(d_2)^{-\delta}\ \ge\ 2(2^{28}/3)^{-\delta}=1.
$$

Give the two branches probabilities proportional to $c(d)^{-\delta}$. Each branch probability is then at most $c(d)^{-\delta}$. Stop each path the first time the product of its $c(d)$ values reaches $Y>1$. The minimum multiplier exceeds one and the maximum multiplier $c(16)$ is fixed, so this is a finite cut meeting every infinite path exactly once. Each endpoint has probability at most $Y^{-\delta}$, so there are at least $Y^\delta$ distinct endpoints. Its product is at most $c(16)Y$ and its actual positive source is at most $2^{16}c(16)Y$. Taking $X=2^{16}c(16)Y$ yields

$$
 \#\{t\le X\mid t\text{ belongs to the constructed tree}\}\ \ge\ c_0 X^\delta
$$

for all sufficiently large $X$, with $c_0=(2^{16}c(16))^{-\delta}>0$.

Every such source has depth at most $\log_5 X$. For all large $X$, the occupation proof's common odd-step horizon $m=\lfloor\log_3(X/8)\rfloor$ exceeds $\log_5 X$, and $2m\ge\lfloor\log_2 X\rfloor$. Every branch gap is at least 4 and the gap at 1 is 2. Consequently every tree source below $X$ belongs to the high-clock lane at this horizon and has the **same endpoint 1**. A forward-invariant set on which $U$ is injective can contain at most one node at each fixed depth. Indeed, if such a set contains the fixed point 1, it cannot contain any nontrivial predecessor of 1.

This prevents extending the injective-endpoint argument to the full finite-phase basin. The exponent $\delta$ is below 0.68. A different proof could still give that upper exponent for the entire branching basin. A rational-phase contradiction for an injective escape would need another ordinary-orbit estimate. [PR189, S3 and its injectivity hypothesis](https://github.com/GettysburgResearch/collatz/blob/a0be70b1ffa075cbc50755ac76036108c028d120/research/stationary-carry-rigidity-20261124/README.md)

## The two-gap affine shadow cannot cover every residue

For PR191 TCP-5's two literal blocks $L=(2,1)$, $P=(1,4)$, write the maps as $(9q+7)/8$, $(9q+5)/32$. Classify every fixed real affine change $y=\lambda q+\mu$ intertwining these maps with two-odd-step maps of the same respective binary clocks. An output word with first gap $a$ has carry $3+2^a$, so the two output carries satisfy $e_L\in\{5,7\}$, $e_P\in\{5,7,11,19\}$. Comparing both affine equations gives

$$
 e_L=7\lambda-\mu,\qquad e_P=5\lambda+23\mu,\qquad
 \lambda=(23e_L+e_P)/166,\qquad y=\lambda(q+7)-e_L.
$$

The four slopes below one are $60/83,61/83,63/83,67/83$, all with $e_L=5$. Thus **every shrinking affine slope in this class requires $83\mid q+7$ for integer output**, and this condition is sufficient. It is invariant on either original block and makes every output odd since $q+7$ is even. Exact endpoint oddness and the affine equations force each prescribed pair of valuations. The other slopes are $1,84/83,86/83,90/83$.

Two shrinking slopes beat the intermediate-state floor $(3q+1)/4$ for all $q>0$, as the difference between that floor and $y$ equals $(3/4-\lambda)(q+7)$. Besides TCP-5's $60/83$, the slope $61/83$ yields $y=(61q+12)/83$, with target gaps $(1,2)$ and $(2,3)$. Every image along such a tail is positive. A literal infinite tail of these blocks cannot visit 1 since all subsequent gaps would equal two. The minimum comparison is with the minimum of the original literal tail, which need not be the minimum of an earlier trajectory. This classifies fixed, symbol-independent two-gap affine substitutions with the same clocks. State-dependent substitutions and variable clocks remain outside the theorem. [PR191, TCP-5](https://github.com/GettysburgResearch/collatz/blob/37b3916633cd32a0c173b20bb18ec3a7ec290a63/research/two-sided-cycle-packing-20261124/README.md)

## Exact controls

The supplied Python program checks the full congruence certificate, the exact tree through depth 12 with 8,191 distinct integer vertices, and all eight shadow coefficient pairs. The same output was reproduced with Python optimization enabled. No Lean compilation of these results is claimed.
