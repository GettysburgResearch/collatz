# Recursive canonical comparisons cover every parent with \(3^{11}\mid z+1\)

Use the ordinary shortcut $T(2v)=v$, $T(2v+1)=3v+2$, and write $\mathrm{Good}(v)$ if $T^h v=1$ for some $h\ge0$. Put $m=11+162j$, $N=2^m$, $M_m=N-1$ and $81z+271=128N$. Suppose the original positive parent satisfies

\[
\begin{aligned}
 0<y,\ 2^{40}y<z&\ \Longrightarrow\ \mathrm{Good}(y),\\
 0<w<z,\ w\equiv17\pmod{48},\ \mathrm{Good}(3w)
   &\ \Longrightarrow\ \mathrm{Good}(w).
\end{aligned}
\]

**Kernel theorem.** If $3^{11}\mid z+1$, then $\mathrm{Good}(z)$. More precisely, the entire ternary ball has a partition into 23 leaves. Nineteen require one canonical comparison, two require two comparisons, and two require three. Every query in every chain is positive, $17\bmod48$, and strictly smaller than the same original $z$. The physical prefix identities hold independently of the two goodness hypotheses. The $m=11$ case has $z=3233$ and fails the divisibility hypothesis. [Finite theorem](NestedCover.lean) · [Physical transport and induction](NestedCharts.lean)

## How one comparison pays for another

A state $(g,d,c)$ denotes the actual positive integer $Y=3^g2^{m-d}+c$. Start at $(0,0,-1)$, which denotes $M_m$. A directed link from $Y$ to $Y'$ records a smaller canonical ordinary $w$ and exact physical words with $T^Fw=Y$ and $T^h(3w)=Y'$. If $Y'$ is good, then $3w$ is good, the original canonical hypothesis makes $w$ good, and hence $Y$ is good. The intermediate values $Y$ and $Y'$ can exceed $z$. Only the actual query $w$ is compared with $z$. Apply this argument backwards through the finite list, then use $T^7z=M_m$.

At $s=v_3(64N-95)\ge15$, use $C=(64N-95)/3^{15}$, which need not be a ternary unit. The four multi-query leaves of the partition are as follows. Each congruence specifies the entire cylinder including all subsequent digits. The other 19 leaves use one query each.

| \(C\) | Intermediate and terminal states, starting after \(M_m\) |
|---|---|
| \(3\bmod9\) | \((0,4,-1)\), \((3,5,-17)\), \((0,4,0)\) |
| \(7\bmod27\) | \((4,9,-5)\), \((0,7,1)\) |
| \(27\bmod81\) | \((4,9,-5)\), \((0,7,1)\) |
| \(637\bmod729\) | \((5,9,-17)\), \((9,17,-5)\), \((9,20,-1)\) |

For example, the $7\bmod27$ branch has
\[
 w_1=(2^{26}N-2955047213)/3^{17},
 \qquad w_2=(2^{17}N-5686117)/3^{11}.
\]
The exact ordinary routes in that branch are
\[
\begin{array}{lll}
 T^{26}w_1=M_m&(17\text{ odd}),&
 T^{35}(3w_1)=Y=3^4 2^{m-9}-5\quad (20\text{ odd}),\\
 T^{26}w_2=Y&(15\text{ odd}),&
 T^{24}(3w_2)=2^{m-7}+1\quad (10\text{ odd}).
\end{array}
\]
The last expression drains under the ordinary positive-turn identity. In the first triple-query branch an intermediate state is $M_{m-4}$. The subsequent two comparisons pay this state on the general hard family with no delayed-only offset-four assumption.

## Positive transport, terminals and parameter counts

Write $X=2^{m-100}$; the original divisibility is equivalent to $X=3221021+3^{15}v$. A finite ternary tree divides this progression into leaves $X=x+St$. For each link let $r$ be its lower odd count, $p$ its upper odd count, and $B$ its stored debit. The input state $(g,d,c)$ gives
\[
                w_t=(3^g2^{100+F-d}(x+St)-B)/3^r.
\]
At the least positive representative the lower and upper physical words are iterated on $w_0,3w_0$. The coefficient $A=w_{t+1}-w_t$ is a multiple of $48$ and $2^F$, and $3A$ is a multiple of $2^h$. The two compensated slopes are tested separately against the input and output state slopes. Exact checks on $81w_0+271$ and $81A$ preserve $w_t<z$ for every $t\ge0$. The 29 links across all 23 leaves have $F\le35$ and $h\le43$.

The terminal state is always one of the following three forms. All further clocks and comparisons use the same ordinary trajectory and original floor.

- Nine leaves end at $2^{m-d}3^g-1$. After $m-d$ odd steps this reaches $3^{m-d+g}-1=T^{m-d+g}M_{m-d+g}$. The verified gap $d-g\ge5$ places that ordinary Mersenne under the already proved general earlier-offset theorem.
- Two leaves end at $2^{m-d}3^g$. Its $m-d$ even steps reach $3^g$, with $2^{40}3^g<2^{173}\le N<z$.
- Twelve leaves end at $2^{m-d}3^g+1$. Write $m-d=2n+r$, $r\in\{0,1\}$. Its next $2n$ steps reach $2^r3^{g+n}+1$. The strict forty-bit inequality is checked at $m=173$ and transported by $3^{81}<4^{81}$ for each increase of 162 in $m$.

The earlier LTE isometries yield $j=13193\bmod59049$ and, on $m=12\cdot2^{18k}-1$, $k=43954\bmod59049$. The ball has density $3^{-10}$ in either parameter. Combining it with the disjoint earlier single-unit tests at $6\le s\le14$ gives exactly $1/54+17/(18\cdot3^{10})=9850/531441$. This count concerns this specific union. [Original isometries and disjoint shells](TERNARY_PUMP.md) · [General earlier-offset proof](EARLIER_OFFSETS.md)

[The Python checker](check_nested_cover.py) recovers all 29 positive lower inverse words, both physical parity words, canonical residues, strict original bounds and both compensated slopes. It reconstructs the exhaustive tree and separately materializes the actual parent at $m=2137277$ and a three-query parent at $m=49966967$. In the latter control all three strict budgets and both identical ordinary intermediate endpoints are checked at full integer precision. [Archived control](NESTED_COVER_CONTROLS.json)

The depth-twelve companion has a separate completely checked one-query tree. Its ordinary transport and terminal payment facts are reused here together with the original earlier offsets. PR197's quantitative-return and finite directed-localization proofs already use multiple directed canonical steps with an original height bound. PR195 at 3fa7ef4a0011b35447a70f587b400878d5ea8ebe gives the common ordinary upper drain for noncanonical repeated odd ancestors. This packet supplies the 23 explicit original-parent branches, checks the actual strict canonical budget for each nested query, and reaches a funded terminal at every leaf. The hypotheses do not force $3^{11}\mid z+1$ for every parent. [Independent one-query certificate and PR195 comparison](VALUATION_COVER.md) · [PR197 quantitative directed return](https://github.com/GettysburgResearch/collatz/blob/1f0f496fbea37792439feada6106eaaff596bcd1/research/ayh-resource-reset-20261124/closing-proposal/QUANTITATIVE_RETURN.md)
