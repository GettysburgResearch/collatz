# A uniform return at gap four on the delayed family

Write $T(n)=n/2$ on even sites and $T(n)=(3n+1)/2$ on odd sites, $M_n=2^n-1$, $P_n=3^n-1$, and $G(x)$ for ordinary reachability of one. For **every** $k\ge1$, set $m=12\cdot2^{18k}-1$ and $81z+271=128\cdot2^m$. Suppose the two general leastness consequences hold at $z$.

* Every positive $y$ with $2^{40}y<z$ satisfies $G(y)$.
* For each $0<w<z$ with $w\equiv17\pmod{48}$, $G(3w)$ implies $G(w)$.

Then $G(M_n)$ for **every positive $n\le m-3$**. Thus a least canonical disagreement at this delayed $z$ would force its first bad positive Mersenne exponent to be $m-2$ or $m$. The hypotheses come from the pinned PR 197 general forty-bit return and canonical minimality. The theorem uses neither a bound on the failed orbit nor the existence of a nontrivial cycle. [Kernel proof](OffsetFour.lean) · [Earlier gap-five theorem](EARLIER_OFFSETS.md) · [Source of the leastness implications](https://github.com/GettysburgResearch/collatz/tree/1f0f496fbea37792439feada6106eaaff596bcd1/research)

## The two physical paths from the canonical query

The source calculation holds on the **entire** $m=11+162j$ progression. Let $X=2^{m-5}=64+243v$ and $w=1601+6144v=(z-31)/2$. Its residue is 17 modulo 48. The lower path $T^{10}w=2X-1=M_{m-4}$ uses four odd departures. The upper path $T^{11}(3w)=27X-17$ uses six. The two base endpoints at $v=0$ are 127 and 1711. Their respective coefficients of $v$ are 486 and 6561. They follow from parity-cylinder lifting on the two positive sources 1601 and 4803.

For the delayed parameters, divide $m-5=11d+r$, $0\le r<11$. The negative integer $-17$ has a genuine eleven-clock shortcut cycle with seven odd departures. Therefore $11d$ ordinary clocks from $27X-17$ reach $2^r3^{7d+3}-17$. If $T^r(-17)=-a$ with $q$ odd departures then another $r$ clocks reach $3^n-a$, where $n=7d+3+q$. The following five end words on $3^n-a$ merge with $P_s$, $s=n+g$, at equal physical times. In each line $k=b+5t$ and $t\ge0$.

| $b$ | $r$ | $q$ | $a$ | $g$ | End clocks | End grades, upper and earlier |
|---:|---:|---:|---:|---:|---:|:---|
| 7 | 3 | 3 | 55 | 2 | 31 | 16, 14 |
| 8 | 10 | 7 | 34 | 1 | 109 | 57, 56 |
| 9 | 9 | 7 | 68 | −1 | 36 | 17, 18 |
| 10 | 6 | 5 | 61 | 1 | 64 | 28, 27 |
| 11 | 8 | 7 | 136 | 3 | 55 | 26, 23 |

The six initial parameters $1,\ldots,6$ use $(g,h)=(7,80),(2,31),(1,205),(-1,36),(1,64),(3,55)$, respectively. In each line $0<s<m-40$. Including all clocks, the upper path from $3w$ meets the path from $M_s$ at clocks $11+(m-5)+h$ and $s+h$, respectively. [Numerical base points and grades](OFFSET_FOUR_CONTROLS.json) · [Exact integer controls](check_offset_four.py)

To verify all positive parameters, let $L=\max(0,-g)$, $R=\max(0,g)$ and choose $N=3^{n-L}$. At the base parameter the two end-word sources have the forms $3^L N-a$ and $3^R N-1$. The certificate checks equality on the positive representatives modulo $2^h$ and checks equality of the total powers of three after both paths. Equality then lifts to every representative of the same binary residue. Since $2^{90}\equiv1\pmod{11}$ and $18b\ge h$, raising $k$ by $5t$ changes $d$ by a multiple of $2^h$. The unit $N\bmod2^h$ is fixed by $3^{2^h}\equiv1\pmod{2^h}$. The kernel checks the six initial parameters separately.

The gap-five theorem already supplies $G(M_s)$. The physical upper merger gives $G(3w)$, canonical minimality gives $G(w)$, and ten lower clocks give $G(M_{m-4})$. The ordinary adjacent even-index merger transfers this to $M_{m-3}$. The earlier theorem supplies every remaining $n\le m-5$.

The signed-cycle method previously appears in PR 197 on a different canonical row; our earlier two qualifying seed classes use the branch $27\cdot2^{m-3}-17$. The present result attaches $27\cdot2^{m-5}-17$ to a canonical query on **all** delayed parameters. The two residual exponents require further work. [Prior signed-cycle use](https://github.com/GettysburgResearch/collatz/tree/1f0f496fbea37792439feada6106eaaff596bcd1/research) · [Earlier two seed classes](PAID_CHECKPOINTS.md)
