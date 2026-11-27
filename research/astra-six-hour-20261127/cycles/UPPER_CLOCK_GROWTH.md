# An explicit unrestricted-clock lower bound on upper odd complexity

Let $s$ be the minimum of a restricted cycle as in [the lower strip theorem](UPPER_LANGUAGES.md), and $x$ one of its odd phases. Fix one of $M(x)=3x,x-1,x+1,2x-1$. If $M(x)>0$ reaches one after $K$ odd departures, then
\[
  K\ge \log_2^*(s)-O(1).
\]
Here $\log_2^*$ counts iterated binary logarithms down to at most one. The bound is weak, but uniform in all upper halving gaps, the four marks and the physical clocks. It applies at every eligible phase, including the upward tripling marks known to be good. It gives no upper bound on $K$.

## Finite signed rational shadow

Suppose a finite path starts at a signed odd integer $w$, follows $N$ exact odd edges with gaps in $\{1,2\}$, and all pairwise ratios of its observed odd coefficients are at most 6 in either direction. At any of these odd sites the affine solution of the lower recurrence gives $|w_i|\le6|w|+12i$ and $w_i/c_i\ge w+i/18$, normalizing $c_0=1$. A negative odd integer remains negative under an odd step, so $N<18|w|$ in that case.

For $w>0$ let $m$ be the number of sites before the first repeat, or all $N+1$ sites if none repeats. They are distinct positive integers at most $X=6w+12m$. All except their first ten have a ten-gap past. The resulting $2^{10}$ permitted residue classes modulo $3^{10}$ give
\[
m\le 10+2^{10}+(2/3)^{10}(6w+12m)
 < 1034+(6w+12m)/50.
\]
Thus $m<(51700+6w)/38$. Determinism after any first repeat keeps all remaining observed states at most $X$. The lower bound at the last site is $w_N\ge N/108$. Substitution gives $N\le1000w+2,000,000$. This bound holds with $|w|$ in place of $w$ for both signs.

Now let the initial lower rational $\xi$ have denominator dividing $3^k$ and be odd in $\mathbb Z_2$. After $k$ odd steps it has an ordinary integer value: each factor 3 removes a ternary denominator and division by powers of two cannot introduce any reduced denominator at two for an observed odd site. The integer so obtained has absolute value at most $6|\xi|+12k$ by the same affine solution. If $N<k$ the estimate below is immediate. Otherwise restart on the remaining observed path, whose pairwise coefficient ratios still meet the same bound. This proves
\[
 N\le 6000|\xi|+12001k+2,000,000. \tag{1}
\]

## Upper odd clocks

Write $M(x)=Ax+B$. Denote the physical clocks of its consecutive odd departures before its first hit by $t_1<\cdots<t_K$ and add $t_{K+1}$ for the terminal clock at one. Put $t_0=0$. The affine formula at each of these upper odd states gives
\[
 \xi_i=\frac{-B-\sum_{j<i}2^{t_j}/3^j}{A},\qquad
 x-\xi_i=\frac{2^{t_i}T^{t_i}(M(x))}{A3^{i-1}}. \tag{2}
\]
For $t_i>v_2(A)$ this ensures an odd dyadic rational $\xi_i$ with $k\le i$ in (1), because $A\in\{1,2,3\}$. Its absolute value is at most $1+2^{t_{i-1}}/2$, using the geometric series in $1/3$. Its lower parity agrees with that of $x$ for $t_i-v_2(A)$ shortcuts.

For $s\ge7$ the physical strip gives pairwise coefficient ratios at most $6$ on the first $\lfloor s/6\rfloor$ shortcuts, by precisely the geometric correction product used for [the explicit tree](FIFTEEN_ODDS.md). Set $t=\min(\lfloor s/6\rfloor,t_i-v_2(A))$. There are at least $\lfloor(t-1)/2\rfloor$ completed lower odd edges with both endpoints observable in these $t$ parity bits. Take $t\ge1$ here; smaller $t$ already meets the upper bound below. Equations (1) and (2) imply
\[
 t\le 12000(1+2^{t_{i-1}}/2)+24002i+4,000,003.\tag{3}
\]
This comparison needs the genuine lower phase only to the truncated depth $t$.

For an explicit bound set $B_0=0$, $B_i=6,000,000(2^{B_{i-1}}+i+1)$ for $i\ge1$. Either $s\le6(B_{K+1}+1)$ or $t_i\le B_i$ successively for every $i\le K+1$, by (3) and $v_2(A)\le1$. The early cases $t_i\le v_2(A)$ satisfy the same bound. In the latter alternative $M(x)\le2^{t_{K+1}}$ by running the physical map backwards, so $s\le 2^{B_{K+1}}+1$. Both alternatives give an explicit bound on $s$. To obtain the displayed iterated-log estimate observe that $i+1\le2\,2^{B_{i-1}}$ and therefore $B_i+26\le 2^{B_{i-1}+26}$. Iterating $u\mapsto2^u$ from 26 bounds $B_i+26$ after $i$ stages. The two final height alternatives cost a fixed number of additional iterations.
