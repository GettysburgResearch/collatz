# A polynomial bound for reinjection from small rational states

Let $N=2^k$, $f_N=N^{-1}\mathbf1_{(0,N]}$, and

$$
(Kf)(y)=\tfrac13\mathbf1_{y>1/2}\sum_{j\ge0}f\left(2^j(2y-1)/3\right).
$$

The transfer advances through the next odd departure after any initial halvings. At positive integer endpoints $K^r f_N(y)$ is the probability of landing at $y$ just after the $r$th odd departure, from a uniform original source $u/3^r$, $1\le u\le N3^r$. This is the exact denominator expansion of the parity lane. Here we bound its values on the intermediate rational meshes. All calculations are written proofs.

## Counting one fractional class

For integers $s,d\ge0$, a positive target $z=v/3^s$ need not be in lowest terms. Uniformly in its fractional class,

$$
\sum_{z>0:\, z\equiv v/3^s\pmod 1}K^d f_N(z)
\ \le\ C(1+d)(1+k+s+d). \tag{1}
$$

For $d=0$ the left side equals one. For $d>0$, every reverse word with $d$ odd departures, total binary length $t$, and starting point $x\in(0,N]$ gives a positive integer $U=3^{d+s}x$. In the affine formula $z=(3^d x+C_w)/2^t$ this integer satisfies

$$
U=2^t(3^s z)-3^s C_w\equiv2^t v\pmod{3^s},\qquad 1\le U\le N3^{d+s}.
$$

Each resulting $x$ follows this precise word in $\mathbf Z[1/3]$ under the true parity map. Indeed $(2z-1)/3$ is odd in the binary sense, and multiplying it by $2^j$ adds precisely $j$ initial even steps. Therefore at fixed $t$ the map $(z,w)\mapsto U$ is injective. The one numerator congruence gives at most $N3^d$ choices for $U$, and each contributes $1/(N3^d)$.

The possible values of $t$ are uniformly polynomial. Before the $d$th odd step a real state $x_i$ obeys $x_i+1\le(3/2)^d(N+1)$. Its reduced denominator divides $3^{d+s}$. The length of any initial run of halvings is the binary valuation of its positive numerator and is bounded by $\log_2(3^{d+s}(3/2)^d(N+1))$. Summing over $d$ runs and odd steps proves (1). This argument also bounds each individual point value. The number of possible denominators $3^s$ does not multiply the estimate.

## An upper bound after the critical odd count

Put $r_*=k/(2-\log_2 3)$. Fix $C_0>1/(2-\log_2 3)$ and $1<\beta<2$. For $r_*<r\le C_0k$ and $r-r_*=o(k)$, there are constants $c,C,L>0$ depending only on $C_0,\beta$ such that for every positive integer $y$,

$$
K^r f_N(y)\ \le\ C k^L(1+y)^{-\beta}
+ C\exp\!\left(-c\frac{(r-r_*)^2}{k}\right)(1+y)^{-1-u},
\quad u=c_1(r-r_*)/k, \tag{2}
$$

where $c_1>0$ is sufficiently small and fixed. This bound does not condition on the binary stopping date of the last odd departure.

For $1<p\le2$, use the telescoping barrier from the descent lane,

$$
H_p(y)=(1+y)^{-p}-(1+2y)^{-p},\qquad
KH_p(y)=\frac{3^{p-1}}{2^p}(1+y)^{-p}\quad(y>1/2).
$$

Writing $\rho_p=3^{p-1}/(2^p-1)$, one obtains $KH_p(y)/H_p(y)\le\rho_p(1+C/R)$ uniformly for $1\le p\le2$ and $y\ge R\ge2$. In particular $\rho_\beta<1$. Choose $R=k^3$. On $y>1/2$ one has $H_p(y)\asymp (1+y)^{-p}$ with absolute uniform constants in this range of $p$.

For $p=1+u$, inductively dominate the values at dates $1\le d\le r$ on meshes of remaining exponent $s\le r-d$ by

$$
K^d f_N(z)\le C N^u[\rho_p(1+C/R)]^{d} H_p(z)+Ck^2(1+R)^\beta H_\beta(z)\quad(z>1/2).\tag{3}
$$

At $0<z\le1/2$ the left side is zero. In $1/2<z\le R$ inequality (1) bounds it by $Ck^2$, absorbed by the second term. For $z>R$ every inverse argument exceeds $1/2$ and lies on an allowed mesh at the preceding date. Apply the two displayed barrier inequalities to obtain the induction step, using $\rho_\beta(1+C/R)<1$ for large $k$. To start the exterior induction at date one, every input argument exceeds $1/2$ and on that interval $f_N(x)\le C N^u H_p(x)$, directly from its support. These observations avoid any uniform real density near $1/2$.

Finally $\log\rho_{1+u}=-u\log(4/3)+O(u^2)$ as $u\downarrow0$. Since $r_*\log(4/3)=k\log2$, choosing $c_1$ small gives

$$
\log\{N^u[\rho_{1+u}(1+C/R)]^r\}
\le-c(r-r_*)^2/k+O(k/R).
$$

Together with (3) this proves (2).

If a set $B$ of bad positive integers has least element $a$ and satisfies $\#(B\cap[1,X])\le C_\theta X a^{-\theta}$ for every $X\ge a$, partial summation gives $\sum_{y\in B}(1+y)^{-\beta}\ll a^{1-\beta-\theta}$. Summing the second term of (2) over all integers costs $O(1/u)$. Thus at $r-r_*\gg\sqrt{k\log a}$, with an arbitrarily large enough constant and $\beta>2-\theta$, this rational entrance population can be much smaller than $1/a$ while polynomial losses in $k$ are retained explicitly. The uniform fixed-barrier bound for the complete set avoiding 1, for example with $0<\theta<0.05$, is an externally reported written input. Every bad source stays at least $a$. The source theorem and this assembly were not rebuilt in Lean. [Wren, *Collatz orbits above a fixed barrier*, Theorem 4](https://rstation.ai/problems/collatz/papers/55)

At $r=0$ the sampled sources are the original positive integers. Transferring their bad mass through the critical denominator levels to the population bounded in (2) remains open.

## Affine offsets in the cumulative scalar potential

For any eligible test $V$, any odd positive $x$, and $z=(3x+1)/2$, the kernel itself gives

$$
3V(z)-\sum_{j\ge0}V(2^jx)=3(I-K)V(z). \tag{4}
$$

Summing the left side over the odd roots of a whole component gives its signed starting-trit sum, when absolutely convergent. Indeed its doubling columns are disjoint and its elements congruent to $2\bmod3$ are precisely the $z$ in (4). In particular, for $V=\sum_{r=L}^R K^r f_N$, the bracket on each root is *exactly* $3(K^L f_N-K^{R+1}f_N)(z)$. A genuinely $K$-harmonic scalar potential gives zero on each individual column. A bare $1/y$ test would instead give $-2/[x(3x+1)]$ on the same column; harmonic summation at a source cutoff additionally retains the macroscopic upper boundary.

The affine correction is already forced in the first asymptotic terms at large arguments. With natural logarithms, $K(y^{-p})=\rho_p(y-1/2)^{-p}$ for $y>1/2$. Thus $K(y^{-1})-y^{-1}=1/(2y^2)+O(y^{-3})$, while $\rho_2=1$ and $\rho'_2=\log3-4\log2/3>0$. Differentiating the power formula at $p=2$ gives

$$
(I-K)\left(\frac{\log y}{y^2}\right)=\frac{\rho'_2}{y^2}+O\!\left(\frac{\log y}{y^3}\right).
$$

Consequently the test $1/y+(2\rho'_2)^{-1}y^{-2}\log y$ already cancels the apparent signed order-$y^{-2}$ loss. This expansion is a calculation on the displayed test functions. Equation (4) gives the exact cancellation for a harmonic potential without an asymptotic assumption. A one-sided normalized sign estimate must still control the source boundary, the terminal boundary, or an additional native clock mark.
