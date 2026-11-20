# Odd steps after the Mersenne checkpoint

**Proposed theorem.** Use the positive shortcut map $T(n)=n/2$ for even $n$ and $T(n)=(3n+1)/2$ for odd $n$. Let $q\ge1$ and $a$ be positive integers with $a$ odd. If a finite path from $a3^q-1$ reaches a positive integer $m$, let $b$ count its steps whose input is odd. There is an effective absolute constant $C>1$ such that

$$
 q\le C\bigl(1+b+\log(2am)\bigr)
 \bigl[C\log(q+b+\log(2a)+2)\bigr]^{b+1}. \tag{1}
$$

Here and below $\log$ is natural. Fix $0\le\delta<1$ and $K>0$. Uniformly for $\log(2am)\le K q^\delta$, every such path as $q\to\infty$ has

$$
 b\ge (1-\delta-o_{\delta,K}(1))\frac{\log q}{\log\log q}. \tag{2}
$$

In particular, for $a=1$, reaching *any* power of two from $3^q-1$ requires at least $(1-o(1))\log q/\log\log q$ odd steps. Once a power of two is reached, the path can be extended to $m=1$ using only halvings, independently of the size of that power of two. All claims apply to finite paths with the specified endpoints. Whether such paths exist for every $q$ remains open.

## Separating one odd integer from a succession of even integers

Write $z=a3^q-1$ and let $L$ be the path length. If $L=0$, then $m=z$ and (1) follows directly. Otherwise let $d_1<\cdots<d_b$ be the zero-indexed odd input positions. Since $z$ is even, every $d_i\ge1$. Multiplying the individual steps by the accumulated power of two gives the integer identity

$$
 m2^L=a3^{q+b}-3^b+\sum_{i=1}^b 3^{b-i}2^{d_i}. \tag{3}
$$

At each step $2T(n)/n$ is 1 or $3+1/n\le4$. In particular

$$
 z\le m2^L\le z4^b. \tag{4}
$$

Put $e_0=0$, $e_j=L-d_{b+1-j}$ for $1\le j\le b$ and $e_{b+1}=L$. For $0\le j\le b$ define the positive integer $A_j$ by

$$
 P_j=m2^L-\sum_{i=1}^j3^{i-1}2^{L-e_i}=2^{L-e_j}A_j.
$$

Indeed $P_j\ge 3^b z>0$ by (3) and $A_j\le m2^{e_j}$. Because $L-e_j\ge1$ in this range, $P_j$ is even while $a3^{q+b}$ is odd. Thus

$$
 \Lambda_j=2^{L-e_j}3^{-(q+b)}(A_j/a)-1
$$

is nonzero at every truncation, including the last. Equations (3) and (4) give

$$
 |\Lambda_j|\le \frac{1}{a3^q}
 +\frac{2^L}{a3^q}\sum_{i=j+1}^b3^{i-1-b}2^{-e_i}
 \le \frac{3}{2}\,4^b 2^{-e_{j+1}}. \tag{5}
$$

For the last inequality the geometric coefficient sum is at most $1/2$, $2^L/(a3^q)\le4^b/m$ and $e_{j+1}\le L$.

## Bounding the distance between successive exponents

Use Matveev's lower bound for a nonzero product of powers of positive rationals minus 1. For at most three bases $\alpha_i$, integer exponents $u_i$ with $|u_i|\le B$, $B\ge2$, and rational logarithmic height $h(c/d)=\log\max(c,d)$ in lowest positive terms, it gives

$$
 \log\left|\prod_i\alpha_i^{u_i}-1\right|
 >-C_0(1+\log B)\prod_i \max(1,h(\alpha_i))
$$

with an effective absolute $C_0$. This is the real degree-one case of Theorem 9.4 of Bugeaud, Mignotte and Siksek, which they derive from Matveev's Corollary 2.3. For a positive rational, $|\log\alpha_i|\le h(\alpha_i)$; a base of 1 may be omitted. [Theorem 9.4, p. 989](https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n3-p05.pdf) · [Matveev's paper](https://doi.org/10.1070/IM2000v064n06ABEH000314)

For $\Lambda_j$ the bases $2$ and $3$ have bounded heights, and $h(A_j/a)\le \log(2am)+e_j\log 2$. Equation (4) gives $L\le q\log_2 3+\log_2 a+2b$, so the exponent bound $B$ can be taken to be an absolute constant times $q+b+\log(2a)+2$. Combining the lower bound with (5) gives, for an effective absolute $C_1$,

$$
 e_{j+1}\le 2b+1+C_1\bigl(1+\log(2am)+e_j\bigr)
 \log\bigl(q+b+\log(2a)+2\bigr).
$$

Set $D=1+b+\log(2am)$. By enlarging an absolute $C_2$ we have $D+e_{j+1}\le H(D+e_j)$, where $H=C_2\log(q+b+\log(2a)+2)\ge2$. Starting with $e_0=0$ gives $L=e_{b+1}\le D H^{b+1}$. Since $a3^q-1\ge3^q/2$, (4) also gives $q\log 3\le L\log 2+\log(2m)$. This proves (1).

Under the hypotheses of (2), the conclusion holds directly if $b>\log q$. Otherwise $\log D\le\delta\log q+O_{\delta,K}(\log\log q)$ and $\log H\le\log\log q+O_{\delta,K}(1)$. Taking logarithms in (1) and rearranging proves (2).
