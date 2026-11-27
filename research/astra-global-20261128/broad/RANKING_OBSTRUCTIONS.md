# What local corrections to a logarithmic ranking can detect

**PROPOSED, written proofs.** The map is the shortcut map $T$ on ordinary positive integers. The constructions give long intervals on which specified rankings fail to decrease. They allow the constructed orbits to converge later.

## 1. A logarithmic waiting time with finitely many local observations

Fix $\alpha>0$. Let $P$ be a finite set of primes. At each $p\in P$ take finitely many nonzero polynomials over $\mathbb Q_p$ and observe the $p$-adic valuations of their values at $n$. Also allow the residue of $n$ modulo any one fixed positive integer. Write $A(n)$ for the combined observations and take an arbitrary real function $f$ on the observation tuples. One may choose any convention at a zero of a sensor. Let $b$ be any bounded real function on the positive integers. Set

$$
 V(n)=\alpha\log_2 n+f(A(n))+b(n).
$$

**Proposition 1.** There is a constant $C$ for which arbitrarily large ordinary integers $N$ satisfy

$$
 V(T^jN)>V(N)\quad(1\le j\le\lfloor\log_2 N-C\rfloor).
$$

The minimum integer on the displayed path tends to infinity. In particular an adaptive choice among these times cannot guarantee a drop.

**Proof.** Include in $P$ all prime divisors of the specified modulus, as well as 2 and 3. Choose arbitrarily large $h$ divisible by the orders of 2 and 3 modulo each $p\in P\setminus\{2,3\}$. Put $D=3^h-2^{h+1}$. This positive odd number is prime to every $p\in P$, since $D\equiv-1\bmod p$ at the auxiliary primes and $3\nmid D$. For $0\le i\le h$ put

$$
 r_i=-1-\frac{2^{h-i}3^i}{D}.
$$

These rationals have reduced denominator $D$ and are all negative. Each is integral at all the selected primes. The first $h$ states are odd in $\mathbb Z_2$ and the last is even. The $h$ odd branches and one even branch send $r_0$ to itself in that order. The real multiplier over the period $P_0=h+1$ is $\lambda=3^h/2^{h+1}>1$. Since $D$ grows without bound with $h$, choose one $h$ whose phase points avoid every zero of every sensor at every selected prime. There are only finitely many such zeros and each rational can have only one reduced denominator.

For each prime choose a fixed precision $B_p$ on which all sensor valuations and the required residues are constant around every $r_i$. Take $B_2\ge1$. Given a large $L$, the Chinese remainder theorem produces an ordinary integer $n_L$ between $2^L$ and $C_0 2^L$, congruent to $r_0$ modulo $2^{L+B_2}$ and congruent to it modulo $p^{B_p}$ at each odd selected prime. The constant $C_0$ is independent of $L$. Through time $L$ all prescribed observations coincide with those at the corresponding phases. At 2 each step costs one digit of precision. At an odd prime the common affine slope $1/2$ or $3/2$ preserves the claimed precision. The parity at 2 ensures that these are the actual ordinary branches.

Write $n_t=T^t(n_L)$. With $j<P_0$, whenever $qP_0+j\le L$ one has the real identity

$$
 n_{qP_0+j}=r_j+\lambda^q(n_j-r_j).
$$

The $n_j$ at the first phases are bounded above and below by positive constant multiples of $2^L$, uniformly in $L$ large. The finitely many phase corrections and the global bound on $b$ therefore give an integer $q_0$, independent of $L$, such that every displayed state at time at least $q_0P_0$ has strictly greater $V$ than $V(n_L)$. Take the last global minimum of $V$ on the finite path. It lies before $q_0P_0$, so its state $N$ is again between positive constants times $2^L$. Every later displayed state has strictly greater $V$. At least $L-q_0P_0\ge\log_2 N-C$ such steps remain. All displayed ordinary states are bounded below by a positive constant times $2^L$. This proves the proposition.

The same proof allows a correction that is locally bounded above and below on a product of neighborhoods of the finitely many diagonal phase points. In particular finite joint nonlinear combinations of valuations need no global bound on their values.

**Prior scope.** Rational-period shadows and the last-minimum argument appear in Sodelin's unreviewed Theorem 6A.1 for the odd-to-odd map. The growing-period word underlying the display is also present there. Nashida studies staged logarithm-plus-valuation rankings. A recent window-score preprint gives a $1/100$-bit-length deadline for a broader class allowing arbitrary binary-window scores. The argument here isolates the elementary shortcut-map consequence for nonlinear joint finite-prime observations, with an additive constant at one full bit length. See [the primary-source map](PRIMARY_SOURCES.md).

## 2. Countably many weighted singularities

Let $\mathcal R$ be the nonpositive rationals of odd denominator. For reduced $r=A/B$ with $B>0$, set $H(r)=1+|A|+B$. Let $(c_r)$ be real weights with

$$
 \sum_{r\in\mathcal R}|c_r|(1+\log_2 H(r))<\infty,\qquad
 P(n)=\sum_{r\in\mathcal R}c_r v_2(n-r).
$$

For positive $n$, the rational $n-r$ is nonzero and $v_2(n-r)\le\log_2 n+\log_2 H(r)$. Thus the series is absolutely convergent.

**Proposition 2.** For any $\alpha>0$, the function $\alpha\log_2 n+P(n)$ fails eventual one-step non-increase. An additional bounded correction is allowed.

**Proof.** Fix $d\ge0$ and take $k=2^t$. On the positive path starting at $n_k=2^d(3\cdot2^k-1)$, $d$ even steps and then $k$ odd steps reach $y_k=3^{k+1}-1$. Every intermediate state tends to infinity with $k$. The initial states tend 2-adically to $-2^d$, with $v_2(n_k+2^d)=d+k$. The terminal states tend to the positive 2-adic limit $2$ since $3^{2^t}\to1$ in $\mathbb Z_2$. The latter follows, for example, by successive squaring of $3^2=1\bmod 8$.

For each fixed $r\ne-2^d$, $v_2(n_k-r)$ is eventually constant. For every $r\in\mathcal R$, $v_2(y_k-r)$ is eventually constant. After division by $k$ both integrands are bounded in absolute value by a constant depending on $d$ plus $\log_2 H(r)$. Dominated convergence in the two series gives

$$
 P(n_k)/k\to c_{-2^d},\qquad P(y_k)/k\to0.
$$

On the other hand $k^{-1}\log_2(y_k/n_k)\to\log_2(3/2)>0$. Eventual non-increase on the displayed paths would force $c_{-2^d}\ge\alpha\log_2(3/2)$ for every $d$. This contradicts absolute summability.

**All backward phases.** In fact the same necessary lower bound holds at every negative rational $r_w$ whose shortcut orbit follows a fixed length-$d$ parity word and then stays at $-1$. Write $s$ for the number of ones and $B$ for the affine numerator, so $r_w=(-2^d-B)/3^s$. Take a fixed integer $v>1$ satisfying $2^d(v-1)\equiv B\bmod 3^s$. Let $k$ tend to infinity along integers divisible by the multiplicative order of $2\bmod 3^s$ and by successively larger powers of two. At $s=0$ impose only the second condition. The ordinary positive integer

$$
 n_k=r_w+2^{k+d}v/3^s
$$

follows $w$, reaches $2^kv-1$, then follows $k$ odd steps to $v3^k-1$. The last state tends 2-adically to $v-1>0$. Before $w$ finishes all finitely many intermediate states grow proportionally to $2^k$. Through the odd run they increase. Applying the same dominated-convergence argument forces $c_{r_w}\ge\alpha\log_2(3/2)$. At depth $d$ the $2^d$ words have distinct $r_w$ because their first $d$ parity symbols differ.

The summability and support assumptions matter. Arbitrary kernels concentrated extraordinarily close to particular positive integers need not have the ordinary limiting behavior above. The exact supremum in [the pin representation](PIN_APPROXIMATION.md) lies outside this linear class.
