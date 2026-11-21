# A critical-exponent bound for images of every interval

**PROPOSED, unconditional.** Let $T$ be the positive shortcut Collatz map. Write $q_j(x)$ for the number of odd inputs in its first $j$ steps, and $P_j(x)=(q_j(x),T^j(x))$. Put $\lambda=\log_2 3$, $p=1/\lambda$ and $\rho=H_2(p)=0.949955527\ldots$, where $H_2$ is binary entropy. There are absolute constants $c,C$ such that for every interval $I$ of $N$ consecutive positive integers, at the common clock $D(N)=c\lceil\log_2(2N)\rceil^2$,

$$
 |P_{D(N)}(I)|\le C\,\frac{N^\rho}{(1+\log N)^{3/2}}. \tag{1}
$$

Here $c$ is a positive integer. Only the least member of each class can lack a smaller partner in $I$ with both the same endpoint and the same odd count at that clock. Projecting to endpoints gives the same upper bound on the number of distinct images. The same bound counts the vertices of any one positive cycle or nonrepeating orbit in $I$, since its distinct vertices remain distinct at a common clock. Thus (1) attains the critical power and gives a logarithmic saving. The earlier $O_\epsilon(N^{\rho+\epsilon})$ bound gives a shorter $O_\epsilon(\log(2N))$ clock. [Earlier interval proof and affine bounds](PREFIX_REPRESENTATIVES.md#a-stronger-bound-for-ordinary-intervals)

For $D=D(N)$, every integer shift by $2^D t$ that keeps the interval positive preserves exactly the partition of $I$ by these pairs. In fact, if $P_D(x)=(q,y)$, then
$$
 P_D(x+2^D t)=(q,y+3^q t).
$$
At step $j<D$, the two current values differ by $2^{D-j}3^{q_j(x)}t$, so their next input parities agree. This proves the identity by induction and works for either sign of $t$. The label map $(q,y)\mapsto(q,y+3^q t)$ is injective. Thus all the smaller partners chosen inside $I$ work simultaneously on every such translate.

## Critical reciprocal-power summability

The interval count also holds for every finite simple orbit segment, with an adjusted absolute constant. Remove its last $D(N)$ positions, or the entire segment if shorter. The earlier positions have distinct images at time $D(N)$ because their shifted positions still lie in the simple segment. Thus (1) leaves at most $C F(N)+D(N)$ vertices in $I$, where $F(N)=N^\rho/(1+\log N)^{3/2}$. Since $D(N)\ll F(N)$, this is $O(F(N))$. For an eventually periodic orbit, its initial segment before the first repeated value contains every distinct vertex. For a nonrepeating orbit, take arbitrarily long finite segments.

Let $S$ be all the distinct values of any one positive orbit, a simple segment, or a set containing at most one representative of each merger component. In the last case its elements have distinct images at every common clock, so (1) applies directly. For every real center $z$ and $R\ge1$,

$$
 \sum_{\substack{x\in S\\|x-z|\ge R}}(1+|x-z|)^{-\rho}
       \ll (1+\log R)^{-1/2}, \tag{2}
$$

uniformly in $S,z,R$. Split the terms into shells $2^jR\le |x-z|<2^{j+1}R$. Each shell meets at most two intervals of $\lceil 2^jR\rceil+1$ consecutive integers; intersect with the positive integers and pad if needed. By (1) its contribution is $O((1+\log R+j)^{-3/2})$. Summation proves (2). In particular $\sum_{x\in S}x^{-\rho}$ converges at the critical exponent. The simple reciprocal series and the supercritical coefficient tail for an infinite distinct orbit are established in earlier work. [Earlier orbitwise Mellin bounds](../astra-three-routes/pass2/ORBIT_MELLIN.md)

## Group at the first crossing

Write $h=\lceil\log_2 N\rceil$, and let $q_i$ be the odd count through $i$ steps. Put $S_i=\lambda q_i-i$. For fixed $i\le h$ and $q_i=q$, all images from $I$ lie in a single interval of real length at most $3N\,2^{S_i}$. Indeed the affine map is $2^{S_i}x+A/2^i$ with $0\le A/2^i\le(3/2)^q$ by the affine offset bound. The offset allowance divided by $2^{S_i}$ is at most $2^{i-q}\le2N$. This argument allows $I$ to be arbitrarily far from zero.

Choose $d>1/\rho$. Put $m_i=\min(i,h-i)$, and stop a word at the first $i\ge1$ with

$$
 S_i<-K-d\log_2(1+m_i).
$$

Here $K>0$ will be a fixed large constant. At a first crossing, $S_i$ is between the boundary and the boundary minus $1+d$, since a step decreases $S$ by at most 1 and the boundary changes by at most $d$. Thus at most a constant $B_d$ of the integer counts $q$ are possible at each $i$. For each of these counts, enclose the possible images in an interval of

$$
 M_i=\lceil 3N\,2^{-K}(1+m_i)^{-d}\rceil+1
$$

consecutive positive integers. For sufficiently large $N$ depending on $K,d$, all these $M_i$ lie between $\sqrt N$ and $N/2$, and $M_i\le4N\,2^{-K}(1+m_i)^{-d}$. With $F(N)=N^\rho/(1+\log N)^{3/2}$ this gives

$$
 B_d\sum_{i=1}^h F(M_i)\le C_d 2^{-K\rho} F(N)
           \sum_{r\ge0}(1+r)^{-d\rho}\le F(N)/2 \tag{3}
$$

after choosing $K$ once. The comparison of logarithms uses $M_i\ge\sqrt N$.

## Count the words that survive

Under independent bits with probability $p$ of an odd input, $S_i$ has bounded, independent, mean-zero increments with positive variance. Each word ending at $S_h=v$ has probability $2^{-\rho h}e^{\theta v}$, where $\theta=\log(p/(1-p))/\lambda>0$. We show that the number of surviving length-$h$ words is $O(2^{\rho h}/h^{3/2})$.

Here is an elementary random-walk estimate used for both ends of the word. For a walk $W_i$ starting at zero with independent identically distributed bounded centered increments of positive variance, and fixed $b\ge0$,

$$
 \Pr\{W_i\ge -a-b\log(1+i),\ 1\le i\le n\}\le C_b(1+a)/\sqrt n \qquad(a\ge0). \tag{4}
$$

The constant can depend on the increment law. First take $b=0$ and set $B=\sqrt n$. Stop at the first exit below $-a$ or above $B$, or at time $n$, whichever comes first. Call the stopped value $Z$ and time $\sigma$. If increments have absolute value at most $L$ and variance $v_0$, bounded optional stopping gives $\mathbb EZ=0$ and $\mathbb EZ^2=v_0\mathbb E\sigma$. The product $(Z+a+L)(B+L-Z)$ is nonnegative, giving $\mathbb E\sigma\le(a+L)(B+L)/v_0$. The chance of the upper exit is at most $(a+L)/B$ by the zero mean and the lower bound on $Z$. The probability of neither exit by time $n$ is at most $\mathbb E\sigma/n$. This proves the flat-boundary case.

Let $\tau$ now be the first crossing below the curved boundary. The flat bound implies $\Pr(\tau>j)\le C(1+a+b\log(1+j))/\sqrt j$. Consequently $\sup_n\mathbb E[\log^2(2+\min(\tau,n))]\le C_b(1+a)$ by summing the increments of $\log^2(2+j)$ against this tail. Stop at $\tau$, the first crossing above $B=\sqrt n$, or $n$. The negative part of the stopped value is at most $a+L+b\log(1+\min(\tau,n))$. Hence $\mathbb E Z^-\le C_b(1+a)$ and $\mathbb E[(Z^-)^2]\le C_b(1+a)^2$. Since $Z^+\le B+L$ and $\mathbb E Z^+=\mathbb E Z^-$, we get $v_0\mathbb E\sigma\le C_b((B+L)(1+a)+(1+a)^2)$. Bound the upper exit by $\mathbb E Z^+/B$, and neither exit by $\mathbb E\sigma/n$. For $a\le\sqrt n$ this gives (4), while for $a>\sqrt n$ the assertion is immediate.

For a fixed attainable endpoint $v\ge-K$, split the word into a first and last segment of $\lfloor h/3\rfloor$ steps each and the independent middle segment. The first segment must satisfy (4) with $a=K$. Reversing the last segment, its partial sums $S_h-S_{h-i}$ must stay below $v+K+d\log_2(1+i)$. Apply (4) to the negative increments with $a=v+K$. Conditional on both outer segments, at most one binomial count in the middle attains $v$, of probability $O(1/\sqrt h)$ by Stirling's formula. It follows that

$$
 \Pr(\text{survival},S_h=v)\le C_{K,d}(1+v+K)h^{-3/2}.
$$

Summing after multiplication by $2^{\rho h}e^{-\theta v}$ proves the word bound, since the possible $v$ lie on a lattice of spacing $\lambda$ with $v\ge-K$. Each such word specifies exactly one residue modulo $2^h$, hence at most one start in $I$. Bounded $h$ can be absorbed in the constant.

## Complete the induction

Suppose (1) holds for shorter intervals. In each group stopped at $i$ with fixed count $q$, the possible current values $z$ lie in one interval of length $M_i$. After a further $D(M_i)$ steps, the induction hypothesis bounds the number of pairs $(q_{D(M_i)}(z),T^{D(M_i)}(z))$ by $C F(M_i)$. The total odd count from the original start is $q+q_{D(M_i)}(z)$, so adding the same $q$ gives the same bound for its full pairs. For $M_i\le N/2$, $i+D(M_i)\le D(N)$ by the stated choice of clock (any integer $c\ge1$ suffices for padding). Padding a pair $(a,y)$ by $j$ steps sends it to $(a+q_j(y),T^j(y))$, a function of the pair alone. By (3) the stopped groups therefore contribute at most $C F(N)/2$ pairs. Each surviving source contributes at most one final pair, giving $O(F(N))$ by the word count. Choosing $C$ large enough for that estimate and for all bounded base cases closes the induction.

The factor $h^{-3/2}$ is attained in the surviving **word count** up to constants. Take $q=\lceil ph\rceil$. Every word with that count has some cyclic rotation whose partial sums $S_i$ are all nonnegative, by starting after a minimum of the partial sums. Thus at least $\binom hq/h\gg2^{\rho h}/h^{3/2}$ distinct words survive. This lower bound counts words before any subsequent mergers. It supplies no lower bound for the number of final images and leaves the convergence of individual exceptional starts open.
