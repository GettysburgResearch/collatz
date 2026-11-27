# Descent with unbounded runs of paid returns

**Theorem.** Consider an actual positive ordinary L/P input whose word is
$$L^r PP L^s P^t\,\{L,\ L^4P^h\ (h\ge1)\}^{\omega},\qquad r\ge0,\ s\ge6,\ t\ge3.$$
A smaller positive odd ordinary nonconverger exists below the initial boundary and, if $r>0$, its first light intermediate. The later paid runs may have unbounded lengths. Their grouping on the right side is part of the hypothesis. This result complements the arbitrary-close-pair theorem in [DESCENT_MACRO.md](DESCENT_MACRO.md).

## Two comparisons at the same slope

Put $M=5367$, $D=4096$. Use the values $F(q)=(Mq+8897)/D$ at free boundaries and $I(q)=(Mq+2395)/D$ inside a long paid run. If $2^A q'=3^p q+C$, the candidate transfer $(Mq+b)/D\to(Mq'+b')/D$ has target carry
$$K=\frac{MC+2^A b'-3^p b}{D}.$$
The basic certificate is exactly the ordinary lift test in [DESCENT_MACRO.md](DESCENT_MACRO.md). It gives these seven identities.

| Source word | Comparison transition | Ordinary target bits |
|---|---|---|
| L | F to F | 101 |
| $L^4P$ | F to F | 11111001010000111 |
| $L^4P^2$ | F to F | 1111101100010100000111 |
| $L^4P^3$ | F to F | 111110110000101110000000111 |
| $L^4P$ | F to I | 11111011000010110 |
| P | I to I | 00110 |
| $P^3$ | I to F | 001110000000111 |

To process $L^4P^h$ with $h\ge4$, use the F-to-I entrance, repeat the I-to-I paid step $h-4$ times, and exit on the last three P's. The free and interior denominators are both bounded by $4096$. Each target numerator has odd slope, so any nontrivial binary denominator would grow on every future edge of the given path. All comparison boundaries are integers. Both comparison values exceed two when $q\ge3$, and an infinite positive L/P source never hits one: from one its accelerated odd gaps are all two, incompatible with either L or P. Thus the comparison cannot have hit one because its infinitely many later boundaries stay outside $\{1,2\}$. This argument places no lower bound on the comparison's odd-step density.

## Entrance from the original floor

As in [DESCENT_PAIR.md](DESCENT_PAIR.md), write $q_0+7=2^{3r+1}v_0$. At the paid boundary $U$ after $PP L^s$, use $U+7=2\cdot9^s v_2$ and $2^{3s+10}v_2=9^{r+2}v_0+3403$. For $r\ge9$ put $m=M2^{2r-4}v_0-1$. Its ratio $(m+1)/(q_0+7)=5367/2^{r+5}$ is at most $5/8$, and it is odd, positive and below both original floors. After $2r-4$ odd steps its value is
$$3^{-8}M 2^{3s+10}v_2 + z,\qquad z=-1-3403M/3^8.$$
The signed rational $z$ has an odd denominator. Its first 27 shortcut steps have twelve odd inputs and end at $-10$. Each additional three steps from $-10$ return there with two odd inputs. Because the difference from the ordinary comparison is divisible by $2^{3s+10}$ in rationals of odd denominator, the comparison follows these signed bits for $3s+9$ steps, for all $s\ge6$. Its new value is the positive ordinary integer
$$H(U)=M(U+7)/3^8-10.$$

The transfer from $H(U)$ to $I(P(U))$ uses 17 clocks, ten odds and the word **00111011101110010**. The direct transfer to $F(P^3(U))$ uses 27 clocks, fourteen odds and the word **001110111011100110000000111**. For $j=1$ or $3$, use the source data $(A,p,C)$ of $P^j$. The two target carries are verified explicitly with
$$B=5j+12,\qquad u=2j+8,\qquad K=M(C-7\cdot3^p)+2^{5j}b'+10\cdot3^u,$$
where $b'=2395$ or $8897$ respectively. When $t=3$ use the direct transfer. When $t\ge4$ enter on the first P, continue in I, and use the I-to-F exit on the final three. In either case the small ordinary input has reached the nonconvergent F comparison at the start of the macro tail. For $r\le8$ direct evaluation of the first two paid returns gives an odd boundary below both original floors for $q_0\ge17$; smaller positive odd inputs converge directly.

The complete signed calculation, the nine ordinary target words and the short-prefix inequalities have exact finite replay in [descent_paid_runs.py](descent_paid_runs.py). This theorem is a written proof with executable arithmetic controls.
