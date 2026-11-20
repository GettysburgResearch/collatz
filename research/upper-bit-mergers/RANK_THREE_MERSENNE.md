# Three odd steps to 1 already include every Mersenne convergence problem

**PROPOSED.** Write $T(n)=n/2$ on evens and $T(n)=(3n+1)/2$ on odds. For a positive odd $n$, let $S(n)$ be the odd part of $3n+1$. For every $q\ge819$ there exists an explicit $x\equiv1\pmod {16}$ whose first arrival at 1 under $S$ is at step three, such that $2x-1$ and $2^q-1$ have a common ordinary iterate. Every $2^q-1$ with $1\le q<819$ reaches 1 by the finite replay. Consequently, proving the [one-sided implication](THREE_RAY_ONE_SIDED.md) only for starts that first reach 1 in exactly three odd steps would already prove convergence of **all** Mersenne numbers. Convergence on the three-step family remains open.

There is a uniform version with an arbitrary positive odd target $t$ prime to three. For every $q\ge819$ the construction gives $S^3(x)=t$, with all three preceding odd vertices greater than $t$, and the partner $2x-1$ reaches $3^q t-1$. This last value is exactly $T^q(2^qt-1)$. The proof uses eighteen finite words, independently of the sizes of $q$ and $t$. [Exact verifier](check_rank_three_mersenne.py)

For $t=1$, the Lean theorem `rank_three_all_large_mersenne` constructs the first arm for every $q\ge819$ and proves an ordinary meeting with the Mersenne start. It checks all eighteen signed paths and extends their integrality conditions by induction in steps of eighteen. The short-exponent replay begins at $3^q-1$ after the forced run of $q$ odd steps from $2^q-1$. [Lean source](HighBit.lean)

## Positive inverse paths and their companions

Take $c=d+2$ and a positive integer $A$. Define the three odd predecessors of $t$ by

$$
 v=(2^At-1)/3,\qquad u=(2^cv-1)/3,\qquad
 x=(4u-1)/3=(2^{A+c+2}t-2^{c+2}-21)/27.
$$

The divisibility condition $2^{A+c+2}t\equiv2^{c+2}+21\pmod{27}$ makes all three divisions integral. In fact its reductions modulo 3 and 9 first give integrality of $v$ and $u$. Their numerators are odd. The numerator of $x$ is $-21\equiv27\pmod {16}$, so $x\equiv1\pmod {16}$. For the choices below $A>q$, and $c\ge2$. Hence $x>u>v>t$ and the three indicated odd transitions land at $u,v,t$ in order.

Put $y=2x-1$. For $x=16k+1$ we have $T^4(y)=18k+1=(9x-1)/8=2^{c-1}v-1$. Whenever $m\ge0$, $T^m(2^m z-1)=3^m z-1$, by following $m$ odd inputs. Applying this identity with $m=c-1$ shows that $y$ reaches

$$
 3^{c-1}v-1=3^d 2^A t-(3^d+1).
$$

Suppose the ordinary signed shortcut from $-(3^d+1)$ visits $-1$ after $H$ steps with $b$ odd inputs. If $A\ge H$, the positive value above has the same first $H$ parities: their starting difference is a multiple of $2^H$, and each step halves this difference or multiplies it by $3/2$. Thus the positive endpoint is $3^{d+b}2^{A-H}t-1$. A final $A-H$ odd steps take it to $3^{A-H+d+b}t-1$. Our choice is $A=q+H-d-b$.

## Eighteen ordinary words certify all exponents

Let $j\in\{0,\ldots,17\}$ satisfy $t\equiv2^j\pmod{27}$, possible because 2 has order 18 there. Select the row $r=(q+j)\bmod18$. The number $A_0$ in the table satisfies $2^{A_0+c+2}\equiv2^{c+2}+21\pmod{27}$. It also satisfies $A_0+d+b-H\equiv r\pmod{18}$. Consequently $A=q+H-d-b\equiv A_0-j\pmod{18}$, giving the required integrality for the actual target $t$.

| $r$ | $d$ | $A_0$ | $H$ | $b$ |
|---:|---:|---:|---:|---:|
| 0 | 39 | 10 | 271 | 132 |
| 1 | 0 | 2 | 1 | 0 |
| 2 | 63 | 10 | 412 | 197 |
| 3 | 1 | 4 | 2 | 0 |
| 4 | 38 | 14 | 271 | 133 |
| 5 | 57 | 10 | 355 | 167 |
| 6 | 62 | 14 | 412 | 198 |
| 7 | 124 | 8 | 1027 | 524 |
| 8 | 78 | 2 | 569 | 281 |
| 9 | 56 | 14 | 355 | 168 |
| 10 | 79 | 4 | 569 | 280 |
| 11 | 169 | 4 | 1298 | 650 |
| 12 | 60 | 2 | 412 | 200 |
| 13 | 6 | 2 | 19 | 6 |
| 14 | 61 | 4 | 412 | 199 |
| 15 | 7 | 4 | 19 | 5 |
| 16 | 81 | 10 | 569 | 278 |
| 17 | 183 | 10 | 1298 | 636 |

The table gives $\max(d+b)=819$ and $H>d+b$ throughout. These inequalities give $A\ge H$ and $A>q$. The verifier replays the signed words, checks the divisibility for all $18^2$ exponent and target residue combinations, and follows $3^q-1$ to 1 for all 818 smaller positive exponents. The table proves the symbolic construction at every larger exponent, while the short-exponent replay is specific to $t=1$.

The construction also controls ordinary height. Write $n=2^qt-1$. For the selected row its source is exactly

$$
 x=\frac{2^{H-b+4}(n+1)-2^{d+4}-21}{27}.
$$

These are eighteen fixed affine functions of positive slope. In particular, an ordinary $n$ in this domain that fails to reach 1 while its core $t$ reaches 1 produces an actual failure of the directed implication at $x=O(n)$. Each such $x$ is charged by at most eighteen $n$, since each displayed function is injective. This statement retains the condition $q\ge819$ and the odd ternary-unit condition on $t$.
