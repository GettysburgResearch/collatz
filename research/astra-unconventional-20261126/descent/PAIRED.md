# A simultaneous cusp and the return-word grammar

**PROPOSED.** A paired return at ordinary $Y$ carries $(Y,3Y-1)$ to $(X,3X-1)$ in the same $H$ shortcut clocks, with the same number $p$ of odd departures on both trajectories. This preserves both component labels. A contextual return word works on all positive sources in its binary cylinder; a fixed endpoint must also belong to that word's ternary image. [Lean arithmetic](Portal.lean) · [Exact enumerator](returns.py) · [Finite replay](../../../reports/astra-unconventional-20261126/descent/finite.json)

## A return at every depth near one half

For $k\geq4$, $u>0$ odd and $2X=3^k u+1$, take
$$
  Y=4+4^{k+1}u.
$$
Both arms make a paired return with $H=2k+3,\ p=k$. The least-significant nonzero ternary digit of $2X-1$ can be either 1 or 2. One may also take any $4\leq j\leq v_3(2X-1)$, replacing $k,u$ by $j,(2X-1)/3^j$. When $j<v_3(2X-1)$, the resulting $Y$ is $1\bmod3$.

The identity comes from the ordinary seeds 4 and 11. Both reach 1 at clock 10 with four odds. Every subsequent pair of clocks in the cycle adds one odd. At clock $2k+2$, adding $2^{2k+2}u$ to 4 and $3\cdot2^{2k+2}u$ to 11 produces $1+3^ku=2X$ and $1+3^{k+1}u=2(3X-1)$. One common halving finishes. The second perturbed start is exactly $3Y-1$. The clock, both odd costs and ordinary output equations are formalized in theorem $\mathtt{paired\_cusp}$.

A related shallow return has $Y=4t+1$ or $8t+2$ and $X=3t+1$, with $(H,p)=(2,1)$ or $(3,1)$, respectively. The ordinary parameters in the canonical PR192 chart start with $q=17+48t$ and $X=(3q+1)/2=26+72t$. This $X$ itself is a source of the three-clock return. It reaches $X_1=(9q+7)/16=10+27t$. Two successive two-clock inverse returns from $X_1$ yield $q$. In particular, $3q$ and $3q-1$ merge at clock four with two odd departures. The original difficulty persists because these operations can go back to points already in the same two components. The cusp also increases ordinary height, approximately by a factor $8(4/3)^k$ when $u$ grows.

There is a second unrestricted-depth formula on one unit digit. For $p\geq1$, $u>0$ odd with $u\equiv1\bmod3$, let $X=(3^{p-1}u+1)/2$ and $Y=(4^pu+2)/3$. The two arms return in $2p+1$ clocks with $p$ odds. The lower first halves to $(2^{2p-1}u+1)/3$, then makes an odd step to $4^{p-1}u+1$. A block $4m+1\longmapsto 3m+1$ uses two clocks and one odd. Applying it $p-1$ times and then halving reaches $X$. The upper starts at $4^pu+1$, uses $p$ such blocks, then halves to $3X-1$. In contrast, following the full shared inverse $(4x-1)/3$ near the center 1 gives lower state $4^{v_3(2X-1)}u+1$, divisible by three when $u\equiv2\bmod3$. Stopping early and using the 4,11 seeds removes this killed state at all depths $k\geq4$.

## Exact enumeration by odd events

Let the current states be $U,V$, with lower and upper cumulative odd counts $p,s$, and set
$$
 m=\min(p,s+1),\qquad C=3^{p-m}V-3^{s+1-m}U.
$$
Initially $p=s=0,\ C=-1$. The upper state starts prime to three and remains so. If $p>0$, the lower is also a 3-unit. At an intermediate zero carry, the two powers of three can therefore balance only when $p=s+1$ and $U=V$. If $p=0$, the coefficient of $U$ is divisible by three and that of $V$ is one, excluding zero. After actual equality the two arms stay equal, so they cannot finish at the distinct positive $X,3X-1$. A zero carry can be discarded.

With lower/upper parity bits $a,b$, put $p'=p+a,\ s'=s+b,\ m'=\min(p',s'+1)$. The shortcut equations give
$$
 2C'=3^{a+b+m-m'}C+3^{p'-m'}b-3^{s'+1-m'}a.
$$
At any binary prefix, either choice of the next lower parity extends it in exactly one way. Indeed increasing the high parameter by one changes the current lower state by the odd number $3^p$. The next upper bit is forced by $b\equiv a+C\bmod2$. If both bits are zero, $C'=C/2$. Thus the number $j$ of consecutive common halvings before the next odd event ranges from zero to $v_2(C)$. At $j<v_2(C)$ both arms must be odd at the designated event. At $j=v_2(C)$, exactly one of the arms is odd and either orientation is possible. After the designated event at least one cumulative grade has increased.

At prescribed final grades $p=s=P$ the sole legal remaining clocks are common halvings. They complete a return exactly if $C=-2^h$ for an integer $h\geq0$; the tail is then unique. This gives a finite dynamic program by the number of odds remaining, covering every clock horizon. A first return followed by any return can be concatenated with a unique lift of the high binary parameter, since its multiplier is odd. So if $W_0=1$ and $f_P$ counts first returns, $W_P=\sum_{i=1}^P f_iW_{P-i}$.

| Odd count per arm | All contextual words | First returns | Longest clock |
|---:|---:|---:|---:|
|1|2|2|3|
|2|6|2|6|
|3|20|4|11|
|4|79|19|16|
|5|318|58|21|
|6|1,386|282|26|
|7|6,202|1,186|31|
|8|28,752|5,579|36|
|9|136,067|26,077|41|
|10|656,026|125,176|48|
|11|3,211,039|611,855|54|
|12|15,920,899|3,031,450|60|
|13|79,818,743|15,213,359|74|
|14|404,050,149|77,140,291|80|

The longest clock already exceeds $(\log_2 9)P$ at grade three. The all-clock counts treat different words at different lengths separately, even when they represent the same ternary target class. At $X=8$, for instance, ordinary replay gives the genuine return from $Y=927$ with $H=72,p=41$. Its existence does not cover the whole $8\bmod9$ class.

## How much branching would pay

For a fixed contextual word of grade $p$ the endpoint $X$ occupies exactly one class modulo $3^p$. Thus among ternary-unit endpoints a word covers at most a fraction $3/(2\cdot3^p)$. If an all-source procedure with grades $\leq P$ must reach every one of the $3^L$ ternary target classes, its mean number of legal words must be at least $3^L$, giving the necessary condition
$$
  3^L\leq 1+\frac32\sum_{p=1}^P W_p3^{-p}.
$$
The initial one allows an empty return. For a fixed word and fixed $X$, the starting $Y$ is uniquely determined. The bound needs no independence assumption. In particular an asymptotic upper rate strictly below $9^p$ would rule out covering all ternary targets while spending $p\leq L$. The finite data do not establish an asymptotic rate, and a procedure aimed at one special rational target need not cover every class.

For arbitrary one-arm inverse words, independently of any paired requirement, at most $\binom{H+1}{r+1}$ words use exactly $r$ odd stages and at most $H$ clocks. Each clock position chooses an odd inverse or an ordinary doubling. Covering all $3^L$ target classes at a fixed source therefore forces $H+1\geq(r+1)3^{L/(r+1)}/e$. In particular linear clocks and sublinear odd budgets are incompatible for all-class steering.
