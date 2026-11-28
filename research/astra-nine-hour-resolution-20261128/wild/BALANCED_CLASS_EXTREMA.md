# Balanced merger classes and their dyadic extrema

Use the shortcut map $T$, let $q_t(n)$ count its odd inputs through time $t-1$, and put $y_t=T^t(n)$. Write $n\sim m$ if at some common time their values and their odd counts agree. This is an equivalence relation since each witness persists at later times. Write $K(n)$ for a whole class and $M(n)=\sup K(n)$ with infinity allowed. Define

$$ H_t(n)=2^t3^{-q_t(n)}y_t,\qquad H(n)=\sup_t H_t(n). $$

These definitions use ordinary positive integer sources.

## A variational identity for every source

For all $n\ge1$,

$$ \boxed{\lim_{a\to\infty}2^{-a}M(2^a n)=H(n).} $$

The limit exists in the extended reals. Moreover, every $K(n)$ on an escaping component is finite, and equality of $H$ is equivalent to balanced coalescence *within that component*.

To prove the formula, a length-$t$ parity word $w$ with ones at $j_1<\cdots<j_q$, using zero-based indices, has

$$ T^t(n)=3^q2^{-t}(n+L_w),\qquad L_w=\sum_{i=1}^q2^{j_i}3^{-i}. $$

Thus $H_t(n)=n+L_w$ increases in $t$. After balanced merger, $H(m)=H(n)$ by the common homogeneous multiplier. Also $H(2n)=2H(n)$. Consequently $2^{-a}M(2^a n)\le H(n)$. The left side is nondecreasing in $a$, since balanced merger of $n,m$ lifts to merger of $2n,2m$ one step later.

Fix any prefix $w$ of $n$. Let $a$ range through the positive multiples of the order of 2 modulo $3^q$ (any $a$ if $q=0$). The positive integer

$$ u_a=2^a n+(2^a-1)L_w $$

has the same first $t$ parities as $n$. Indeed $u_a-n=(2^a-1)(n+L_w)=(2^a-1)2^ty_t/3^q$ is a multiple of $2^t$. It reaches $2^ay_t$ at time $t$ and reaches $y_t$ after $a$ further halvings. The source $2^an$ reaches $y_t$ at the same total time and grade. Hence $u_a\in K(2^a n)$ and $u_a/2^a\to n+L_w=H_t(n)$. Taking all $t$ proves the limit.

If the trajectory escapes, interval compression gives a uniformly finite reciprocal sum on its distinct states. The identity

$$ H_t(n)=n\prod_{\substack{j<t\\ T^j(n)\ \mathrm{odd}}}\left(1+\frac1{3T^j(n)}\right) $$

therefore gives finite $H(n)$, and $m<H(n)$ for every $m\in K(n)$. On the same escaping component let $T^r(n)=T^s(m)$. The ratio $H(n)/H(m)$ is $2^{r-s}3^{q_s(m)-q_r(n)}$. Equality forces both exponent differences to vanish, by unique factorization. At an eventually periodic positive source the product diverges because the cycle includes an odd step. The real orbit series and the distinct-state reciprocal estimate are external inputs. [Mahler reduction, Paper 168](https://rstation.ai/problems/collatz/papers/168/v1) and [interval compression, Paper 28, §8.1](https://rstation.ai/problems/collatz/papers/28).

## Finite class maxima and the class of a terminating source

Let $\mathcal M$ be the positive integers with no larger balanced mate. Every finite class has one member of $\mathcal M$, and two different members of $\mathcal M$ never merge with equal clocks and odd counts. The labelled interval-compression theorem gives absolute $C$ and $\eta<1$ such that every interval $I$ of length $L$ has

$$ |\mathcal M\cap I|\le C L^\eta. $$

Indeed its elements remain distinct as *labelled* images at the common time in Paper 28, Theorem A. Every $m\in\mathcal M$ has $v_2(m)\le1$. For odd $b$, inputs $4b$ and $4b+1$ meet after three shortcut steps at $(3b+1)/2$ with one odd input each. Doubling gives a larger mate for every multiple of four. A partition into growing finite intervals already has density-one adjacent agreement. Density-one agreement alone cannot force an infinite class.

Every source $n$ reaching one has an infinite balanced class. If its path to one takes time $s_0$ with grade $q_0$, append $j$ full laps $1,2,1$ to give $s=s_0+2j$ and $q=q_0+j$. Then $s-2q=s_0-2q_0$ is fixed. The fixed-total estimate at odd unit root 1 and extra precision zero gives $\gg 2^s/(3^q\sqrt q)$ distinct positive odd inputs meeting one at shortcut time $s$ with grade $q$. Fixed-length inverse words at an odd positive integer target are positive throughout. Their roots all belong to $K(n)$, and the bound grows exponentially in $j$. The published fixed-total theorem is used as stated. Its reported formal dependencies were not rebuilt here. [Paper 200, Input 3.3](https://rstation.ai/problems/collatz/papers/200/v1).

## A faster realization on an escaping orbit

Suppose $n$ escapes. At an odd endpoint $y=T^t(n)$ after $q\ge1$ odd inputs, $y$ is prime to three. Put $a=2q-t$. Along these endpoints $q\to\infty$ and $a\to\infty$, since $2^t/3^q=H_t(n)/y\le H(n)/y$. For large $q$, central fixed-total sampling with $s=2q$ from $y$ gives

$$ \#K(2^a n)\gg (4/3)^q/\sqrt q,\qquad 0\le H(n)-2^{-a}M(2^a n)\le H(n)-H_t(n)+\frac{2^t}{3^q}F. $$

Indeed the sampled odd inputs are $2^{2q}3^{-q}(y-\beta)$ with $0\le\beta\le F$. They meet $2^a n$ at $y$ with identical time and grade. If $Y_t=\min_{j\ge t}T^j(n)$, the reciprocal estimate of Paper 28 bounds the right side by $O(H(n)Y_t^{\eta-1})$ for a fixed $\eta<1$. Thus the class has quantitatively many native members near its homogeneous endpoint on these dyadic scales.

The boundedness theorem concerns a fixed escaping source. Its dilated classes can grow without bound in size, as the last estimate proves. A density-one theorem for infinite balanced classes would exclude escape through positive predecessor density. Its proof, and the treatment of a possible nonstandard cyclic component, remain open. The dyadic formula reconstructs the real orbit correction from an extremum over integer sources having exact equal clocks and grades.

## A simultaneous forward and backward minimum

On an escaping component $C$, the set of homogeneous heights $\Lambda_C=\{H(n):n\in C\}$ meets every bounded interval in a finite set, since $H(n)\ge n$. It has a least height $\alpha_C$ attained by a finite class. If $u$ is in that class, every finite undirected Collatz walk out of $u$ has cumulative homogeneous multiplier at least one. Assign multiplier $1/2$ or $3/2$ to a forward even or odd step and its reciprocal to a reversed step. Multiplication along the walk is exactly $H(v)/H(u)$ by telescoping. Every ratio other than one exceeds $1+\epsilon_C$ for some component-dependent $\epsilon_C>0$ after decreasing $\epsilon_C$ if necessary. The next distinct height exists since $H(2u)=2H(u)$. In particular every minimizer is odd and starts with two odd steps, since either an initial even step or an odd step followed by an even step would have net multiplier below one.

This minimum involves the entire integer component, including a route that follows an arbitrary native forward prefix and then changes to a different legal predecessor. A single negative-log-multiplier walk out of each positive integer would rule out escape. The proof above gives no universal construction of such a walk.
