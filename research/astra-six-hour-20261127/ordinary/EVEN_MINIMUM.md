# Minimizing the true upper even count on the bounded gap-six branch

**PROPOSED.** Write $T(2u)=u, T(2u+1)=3u+2$ and $C(n)$ for an ordinary positive orbit reaching one. For a good positive $v$, let $H(v)$ be its **first** time at one, $P(v)$ its odd departures until then, and $E(v)=H(v)-P(v)$. Suppose the bounded least-tripling-disagreement alternative has least bad positive integer $s$ and least canonical reverse disagreement $z$, whose upper certificate has three odds at the surviving gap six. Then
$$
 j=11+162m,\quad N=2^j,\quad 81z=128N-271,\quad
 s\ge(3N/8)-1/32 .
$$
Here $s$ is an integer and $8\mid N$, so $s\ge3N/8$. Every positive multiple of three below $2s+1$ is good. A canonical parent is $17\bmod48$. These are the [bounded source theorem](../../astra-unconventional-20261126/renormalization/BOUNDED_RANK_THREE.md) and [least-tripling floor](../../astra-unconventional-20261126/cycle/GOOD_NEIGHBORS.md).

Minimize the ordered pair $(E(3x),x)$ over **all** positive $x$ with $\neg C(x)$ and $C(3x)$, with no residue restriction. Its minimum exists and is attained at an odd $x$. Its complete upper word has the following possibilities.

| Upper even departures | Upper odd departures |
|---|---|
| $j+3$ | $3$ or $4$ |
| $j+4$ | $4,5$ or $6$ |

In every row the second upper odd departure occurs by clock 15, with the first at clock zero. Both assertions apply to one actual globally minimizing positive source and its own first hit. Membership of $x$ in a cycle is unnecessary. The last two rows remain open.

## Why the upper word is sparse

The original $z=48t+17$ supplies a candidate. Another is $w=(2z-1)/3=32t+11$, since $Tw=z$, while $T^5(3w)=T^4(3z)=81t+29$. The prefixes have three and two odd departures, hence two even departures each. Before their meeting their inputs exceed one. Thus $E(3w)=E(3z)=j+4$ and $w<z$. The identical exchange at any canonical parent rules out canonicality at the unrestricted minimum. An even parent can be halved, saving one upper even departure. The natural-number minimum exists lexicographically. Moreover every finite even-count sublevel is finite, since multiplying along the upper word gives
$$
        3x(3/2)^p\le2^E,\qquad p=P(3x),\quad E=E(3x).
$$
For a fixed $E$, this bounds $x$, whose first-hit certificate is unique.

In the present branch $x\ge3N/8$ and $E\le j+4$. Consequently $E=j+d$, $1\le d\le4$, and $9\cdot3^p\le8\cdot2^{d+p}$. This gives the maxima $p=1,3,4,6$ respectively. When $d=4$, the height tie gives $x\le w=(256N-623)/243$. Every odd upper input before the first hit is at least three, hence multiplying $2T(v)\le(10/3)v$ at odds gives $2^E\le3x(5/3)^p$. If $p\le3$, then $16N\le(125/9)x<(125/9)(256/243)N<16N$, impossible.

For $p=1$, the exact shape $9x+1=2^{j+d+1}$ requires $6\mid j+d+1$. Since $j=5\bmod6$, it would require $6\mid d$. Thus $p\ge2$. The resulting universal cap $27x\le32N$ follows from the height tie at $d=4$ and the upper product at $d\le3$. If the next odd upper input occurs at clock $a\ge16$, then $2^{16}\mid9x+1$. In this class $x=29127+65536t$, and $T^{16}x=8749+19683t<3N/8$ by the cap. Thus $a\le15$.

For $p=2$, the remaining $d$ are 2 and 3, and $27x+3+2^a=2^{j+d+2}$. Modulo 27 this forces $a=17\bmod18$ at $d=2$, or $a=2\bmod18$ at $d=3$. The only possibility is $a=2,d=3$. Then $27x+7=32N$, and $2^{16}\mid27x+7$ since $j\ge11$. The class $x=2427+65536t$ has $T^{16}x=730+19683t<3N/8$. [Kernel minimum, product bounds, rank cap and physical lifts](EvenMinimum.lean)

## Exclusion at three odds and $E=j+2$

Write the upper odd clocks as $0,a,b$, $0<a<b<H=j+5$. Their exact equation is
$$
       81x+9+3\cdot2^a+2^b=2^H=32N .
$$
For $a\ge10$, $9x+1$ is divisible by $2^{10}$. The lower signed center $-1/9$ reaches 1 at clock 10 with six odd departures. This gives $T^{10}x=1+81(9x+1)/1024<3N/8$ using $81x<32N$ and $N\ge2048$.

For $1\le a\le9$, the ordinary exponent $b$ has the residue shown below, since $2^{H}=2^{16}\bmod81$ and $2$ has order 54. In the direct rows the first $h\le b$ lower parities are those of $-(3+2^a)/27$, whose endpoint $c$ and odd count $u$ are shown. Here parity of an odd-denominator rational means parity of its numerator. The true positive endpoint is
$$
 T^h x=c+3^u(32N-2^b)/(81\cdot2^h).
$$
The displayed values and $N\ge2048$ give $8T^h x<3N$ in each direct row.

| $a$ | $b\bmod54$ | $h$ | $u$ | $c$ or remaining argument |
|---:|---:|---:|---:|---|
|1|30|2|1|$1/9$|
|2|44|10|6|$1$|
|3|36|13|8|$1$|
|4|20|5|3|$0$|
|5|6| | |variable ordinary ascent below|
|6|32|7|4|$-1$|
|7|48| | |smaller canonical parent below|
|8|26|9|5|$-4$|
|9|0| | |bad triple below its floor|

At $a=5$, put $n=H-b$, $V=(2^n-1)/3$ and $F=2^{b-4}V$. Both $b$ and $n$ are even, $b\ge6, n\ge2$, so $V$ is a positive integer congruent to 1 modulo four. The first four lower shortcuts take $x$ to $F-1$. Put $k=b-5$ and $R=3^kV$. Here $k$ is odd and $R=3\bmod4$. The complete odd ascents of $F-1$ and $F/2-1$ end at $3R-1$ and $R-1$. For $R=4t+3$ these two sites both reach $3t+2$ in two shortcuts. Thus $F/2-1$ is bad, although $0<F/2-1<2^H/96=N/3<s$. The positive comparison uses a number of steps growing with the *supplied* last gap $b$.

At $a=7$, let $y=T^2x=(9x+5)/4$. The congruence $2^{10}\mid27x+131$ gives $y=1\bmod16$; and $4y=9x+5$ gives $y=2\bmod3$. The cap $81x<32N$ and $81z=128N-271$ imply $y<z$. The signed upper center is $-29$; its first eight steps send it through $-43,-64,-32,-16,-8,-4,-2$ to $-1$, with two odd departures. Hence
$$
       T^8(3y)=-1+9(27x+131)/1024
              =-1+3(32N-2^b)/1024<3N/8.
$$
This gives a strictly smaller genuine canonical reverse disagreement.

At $a=9$, $b\ge54$. After eighteen true lower steps, take respectively an odd inverse, an even inverse and two odd inverses. The positive visitor is
$$
            Y=(19683x+31371)/16384.
$$
The given binary class makes $Y$ an integer. It is a multiple of three, and the short forward word of $Y$ ends at $T^{18}x$; the exact residue computation verifies the four steps. Since $81x<32N$, one gets $Y<3N/4\le2s$. This contradicts the good triple floor. This exhausts every pair of upper gaps in the $d=2,p=3$ case with no maximum on $b$.

## Repeated odd ancestors retain a common ordinary upper certificate

More generally, let $z>1$ be any odd ordinary integer and write $z+1=3^\ell u$ with $\ell\ge2$. Its odd ancestor $w_\ell=2^\ell u-1$ reaches $z$ after $\ell$ odd shortcuts. Moreover
$$
      T^{\ell+1}(3w_\ell)=(z-1)/2
$$
with exactly two even departures. For $\ell\ge3$, the first three upper steps from $3w_\ell$ reach $9\cdot2^{\ell-3}u-1$. The next $\ell-3$ inputs are odd, reaching $3^{\ell-1}u-1$. This is odd since $z$ is odd, and its next step is $(z-1)/2$. At $\ell=2$, two steps reach $z-1$ with one odd departure and a halving finishes the claim.

On the gap-six source, $(z-1)/2=1616+8192t$, with $81t+16=2^{j-7}$. Thirteen more shortcuts reach $1+2^{j-7}$ with four odds, an automatically good positive integer below $s$. Thus every eligible $w_\ell$ is an actual reverse disagreement. Write $j-7=2L$. The first $2L$ steps from $1+4^L$ reach $1+3^L$ with $L$ even departures. A remaining first hit requires strictly more than $L$ even steps, since $2^{E(v)}\ge v=1+3^L>2^L$. All three prefixes stay above one, either by the displayed odd ramp and parity or by the positive lift from the $1,2$ cycle. Consequently $E(3w_\ell)>11+2L=j+4$ for every $\ell\ge2$, while $w_1=w$ attains $j+4$. [Kernel arbitrary-depth physical stack and common endpoint](AncestorExchange.lean)
