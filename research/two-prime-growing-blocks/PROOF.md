# Two primes exclude every two-center linearly growing Syracuse schedule

**PROPOSED.** Let $A_1,\ldots,A_r$ be nonempty finite words of positive Syracuse exponents. Put $S=\sum_{j,e\in A_j}e$, let $\ell$ be the total number of exponents, and let $d$ be the number of changes between consecutive cyclic rational fixed points of the block maps. If $d\ge2$ and
$$
\rho=\frac{S}{\ell\log_2 3}>
\frac{4d^2-2d+1}{4d^2+2d+1},                                    \tag{1}
$$
the word $\prod_{K\ge1} A_1^K\cdots A_r^K$ has no rational 2-adic source. An arbitrary finite prefix can be added or deleted. For $d=2$, (1) holds for **every** collection of positive exponent blocks, since $S\ge\ell$ and $3^{13}<2^{21}$. In particular all $\prod_{K\ge1}1^{aK}2^{bK}$ with positive integers $a,b$ are excluded, including the previously undecided example $a=5,b=1$.

The fixed-point reduction, normalized Hankel determinant, dyadic noncancellation and height estimate are due to Lyapunov Weaver. Their fixed-shift threshold is $4d^2/(4d^2+2d+1)$ and their optimized two-block negative-shift result reaches $43/57$. We use their fixed-shift determinant and prove an additional cubic-order **3-adic** divisibility bound for that same determinant. [Paper 46, Sections 3–5](https://rstation.ai/problems/collatz/papers/46/v1)

## The determinant and the dyadic place

Write $q=2^S/3^\ell$, $Q=1/q$, and $F_q(z)=\sum_{k\ge0}z^k q^{\binom{k}{2}}$. The inverse of a block with $s$ divisions and $l$ odd steps is $x\mapsto p+(2^s/3^l)(x-p)$, where $p$ is its rational fixed point. In successive macroblocks telescope these affine maps. The source is a rational constant plus $\xi=\sum_{i=1}^d c_iF_q(z_i)$, where $c_i$ are the nonzero successive fixed-point differences and $z_i$ are the corresponding partial products of $2^{s_j}/3^{l_j}$. The terms at $k=0$ cause no change since $\sum c_i=0$. The $z_i$ have positive, distinct 2-valuations in an interval of width less than $S$. In fact the proof below excludes any rational $\xi$ for fixed nonzero rational $c_i$ and any such distinct-valuation $z_i$ that are positive rationals with denominators powers of three.

Assume $\xi$ rational. For every integer $n$ use the normalized rational tails
$$
w_n=Q^{\binom{n+1}2}\left(\xi-\sum_{k=0}^n\sum_i c_i z_i^k q^{\binom k2}\right),\qquad
w_n=Q^n\left(w_{n-1}-\sum_i c_i z_i^n\right),
$$
where for $n<-1$ the signed sum convention is minus the sum over $n+1\le k<0$. At 2 they equal the moments with bases $z_i q^j$ and weights $c_i z_i^{j+1}q^{\binom{j+1}2}$ for $j\ge0$. Choose a sufficiently large *fixed* $M\ge0$ as in paper 46, and put $H_N=\det(w_{M+u+v})_{0\le u,v<N}$. Ordering the bases by increasing 2-valuation orders the weights after multiplication by the $M$th powers of those bases. The Cauchy–Binet term with the first $N$ bases is uniquely least in valuation, giving
$$
v_2(H_N)=S\frac{2d+1}{6d^2}N^3+O(N^2).
$$
In particular $H_N\ne0$. Paper 46 clears denominators to form the integer $I_N=h^N Z^{J_N}2^{SC_N}H_N$, where $h,Z$ are fixed, $J_N=O(N^2)$ and $C_N=(2/3)N^3+O(N^2)$. Its bound is
$$
\log |I_N|\le C_N\log \max(2^S,3^\ell)+O(N^2+N\log N).
$$
These are exactly the fixed-shift estimates in Section 4 of that paper.

## Reverse recurrence and the prime three

Uniformly for integers $|t|\le 4N+M$, we have $v_3(w_t)\ge-O(N)$. Indeed the signed finite expression consists of $Q^{\binom{t+1}2}\xi$ and terms $c_i z_i^k Q^{\binom{t+1}2-\binom k2}$. In both index ranges the $Q$ exponents are nonnegative, $Q$ is 3-integral, and $|k|=O(N)$. Iterating the recurrence backward $J$ terms yields the exact identity
$$
w_n=-\sum_{h=1}^J\sum_i c_i z_i^{1-h}Q^{-\binom h2}(z_iQ^h)^n
       +Q^{Jn-\binom J2}w_{n-J}.                                 \tag{2}
$$
This is a finite identity over $\mathbb Q$, including for negative $n-J$.

Enumerate the reverse bases $z_iQ^h$ in successive full groups $h=1,2,\ldots$ (any fixed order within a group). Their 3-valuations equal $\ell t/d+O(1)$ at enumeration index $t$. For column $v$ let $p_v(X)$ be the monic polynomial whose roots are the first $v$ reverse bases, and replace that column by $p_v(\mathcal S)w_{M+u}$, where $\mathcal S$ shifts the tail index by one. This is a triangular column operation with determinant one. Each coefficient $[X^j]p_v$ is an elementary symmetric sum of products of $v-j$ distinct bases. The sum of the smallest possible valuations is at least $\ell(v-j)^2/(2d)-O(N)$: the $k$th index in any product is at least $k$.

With $J=\lfloor v/d\rfloor$, $p_v$ kills all the displayed pure modes in (2). At row $u$ set $n=M+u$. Each term of the surviving remainder has 3-valuation at least
$$
\ell\left[(n+j)J-\binom J2+\frac{(v-j)^2}{2d}\right]-O(N)
\ \ge\ \ell\left[\frac{nv}{d}+\frac{(d-1)v^2}{2d^2}\right]-O(N).
$$
Replacing $J$ by $v/d$ costs only $O(N)$. The discarded square is $j^2/(2d)\ge0$. Thus every determinant term has at least that valuation summed over its permutation. The square term has fixed sum; the minimum of $\sum u v$ occurs for opposite ordering, giving $N(N-1)(N-2)/6$. Consequently
$$
v_3(H_N)\ge\ell\frac{2d-1}{6d^2}N^3-O(N^2).                     \tag{3}
$$
This lower bound does not require 3-adic uniqueness or distinct 3-valuations. Multiplication by the clearing factors costs at most lower-order terms at 3.

If $2^S<3^\ell$, the integer inequality $\log|I_N|\ge v_2(I_N)\log2+v_3(I_N)\log3$ contradicts its stated upper bound exactly when
$$
\rho\left(\frac23+\frac{2d+1}{6d^2}\right)+\frac{2d-1}{6d^2}>\frac23,
$$
which is (1). If $2^S\ge3^\ell$, the positive additional dyadic term alone gives a contradiction. This proves the assertion. With exactly two distinct block centers cycling once, $d=2$; if the block centers were equal the fixed-point differences would instead vanish, a degenerate case outside the statement.
