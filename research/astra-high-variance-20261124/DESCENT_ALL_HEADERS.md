# All sixteen initial headers with unbounded paid-run lengths

**Theorem.** Let $r\ge0$, and let $W$ be **any** length-five L/P word whose first letter is P. If a positive ordinary source begins
$$L^r W\,\{L,\ L^7P^h\ (h\ge1)\}^{\omega},$$
then some positive odd ordinary nonconverger lies below the initial boundary and, if $r>0$, below its first light intermediate. There is no upper bound on any paid run or on the number of such runs. The condition that successive paid runs in the displayed tail have at least seven intervening L's remains essential to this proof. The initial header is unrestricted.

Thirteen headers are handled without any tail condition by the previous [finite entrance code](../astra-closure-attack-20261124/DESCENT_EXTENSION.md). The following three constructions discharge exactly its residual headers. They use a different ordinary orbit after the entrance; a meeting with the original orbit is unnecessary.

## The adjustable paid state

Write $F(q)=\lambda(q+7)+z$ and $I(q)=\lambda q+b$. To stay in $I$ through one P via a five-clock target with carry $c$, choose $b=(c-5\lambda)/23$. To return to $F$ on the last $H$ paid steps, a target carry $K$ must satisfy
$$\lambda=\frac{23K+9^H c-23\cdot32^H z}{166\cdot32^H}.$$
This follows by composing the exact P law $P(q)=(9q+5)/32$. Selecting carries whose numerator cancels the odd factor 83 produces the dyadic multipliers below. Set $D=2^d$, $M=D\lambda$, so the two biases listed are the integer numerators $D(7\lambda+z)$ and $Db$.

| Header | $M$ | $d$ | $z$ | Free bias | Interior bias | $c$ | $H$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| PPLLL | 2442741 | 21 | −7 | 2419123 | 107233 | 7 | 4 |
| PLLPP | 103789 | 17 | −5 | 71163 | 34425 | 10 | 4 |
| PLLPL | 5367 | 12 | −7 | 8897 | 2395 | 20 | 3 |

For each row, L sends F to F. Each $L^7P^i$ for $1\le i\le H$ also sends F to F. Alternatively $L^7P$ sends F to I, P sends I to I, and $P^H$ sends I to F. Thus a long run $L^7P^h$ with $h>H$ is realized by entering I on its first P, staying there for $h-H-1$ P's and exiting on the last $H$ P's. There are no assumptions on which short or long run occurs next.

The following gives a finite arithmetic proof of each transition. For source data $(A,p,C)$ with $2^A q'=3^p q+C$, and old and new bias numerators $b_0,b_1$, compute $K=(MC+2^A b_1-3^p b_0)/D$. For a proposed target word of $A$ clocks, $p$ odds and carry $K$, let $u=-K3^{-p}\bmod 2^A$. The $A$ literal shortcut steps from $u$ have $p$ odd inputs and give $2^A T^A(u)=3^p u+K$. Therefore the whole residue class maps with this same affine law. [descent_all_headers.py](descent_all_headers.py) verifies integrality, both equalities and prints every word, with exact integer arithmetic.

Denominator clearing along the single infinite tail shows all the displayed boundary comparisons are ordinary integers: a nontrivial binary denominator would gain $A$ binary factors of degree at each step and all denominators divide $D$. All source boundaries under consideration are odd and $\ge3$, since one cannot start an infinite L/P block path. In every row $3M+\min(b_0,b_1)>2D$. The comparison's infinitely many later boundary values exceed two, which excludes convergence to the cycle $1,2$.

## Transport from the initial source

Let $q_0$ be the initial boundary and $q$ the first paid entry. As before there is a positive $v$ with $q_0+7=2^{3r+1}v$ and $q+7=2\cdot9^r v$. For $r\le11$ the source's second P already gives the required strict drop: the suffix up to that P is PP or PLLP. For each of the twelve $r$ values the exact affine slope and its value at $q_0=17$ give $4(q_{\rm paid}+1)\le3q_0+1$ for $q_0\ge17$. The positive odd inputs below seventeen converge directly.

For $r\ge12$, the first two rows start at $m=M2^{2r+\ell}v-1$ with $\ell=-9$ and $-7$ respectively. Its first $2r+\ell$ clocks are odd and lead to $y=M3^\ell(q+7)/2-1$. The ratio $(m+1)/(q_0+7)$ is at most $5/8$ in both rows, so $m$ beats both original floors.

The PLLPL row uses a different start,
$$m=\frac{5367}{32768}(q_0+7)-7.$$
It is positive, odd and below both floors. The difference between $m$ and $-7$ is divisible by $2^{3r-14}$, so for that many clocks the ordinary orbit follows the signed cycle $-7,-10,-5,-7$. There are exactly $2r-9$ odd inputs, and the signed endpoint is $-10$. Thus the ordinary comparison reaches $y=5367\cdot3^{-9}(q+7)/2-10$. The initial light run supplies the ternary divisor. This is the step that lets a different comparison work on the third header.

In general write $y=M3^\ell(q+7)/2+a$, with $a=-1,-1,-10$ in the three rows. For header data $(A,p,C)$ the entrance to $F(q')$ has time $B=A+d-1$, odd count $u=p-\ell$ and carry
$$K=\tfrac M2(C-7\cdot3^p+7\cdot2^A)+z2^B-a3^u.$$
The same residue certificate gives the physical entrances below.

| Header | Clocks | Odds | Ordinary target bits |
|---|---:|---:|---|
| PPLLL | 39 | 19 | 010101100110110001010100001001101101101 |
| PLLPP | 37 | 17 | 0101010111100011110001000011000011100 |
| PLLPL | 30 | 19 | 111010100100111010110111111100 |

The smaller start in each case reaches the positive nonconvergent comparison and is therefore itself nonconvergent. This theorem has a written proof and separate exact arithmetic replay. The Lean theorem in [descent_macro.lean](descent_macro.lean) covers the earlier five-macro tail in [DESCENT_MACRO.md](DESCENT_MACRO.md).
