# Separating an ordinary escape from all short predecessors simultaneously

**PROPOSED, elementary written proof.** Write $T(2z)=z$, $T(2z+1)=3z+2$, $x_i=T^ix_0$ for one fixed positive ordinary source, and $\tau(a)=\min\{j\ge0:T^ja=1\}$, with value infinity when necessary. Both $1,2$ are cycle points. Let $S$ be any fixed nonempty finite set of primes, $r=|S|$, and $R_S(d)=|d|/\prod_{p\in S}p^{v_p(d)}$ for nonzero integral $d$. All clocks here are shortcut ticks. The results apply to a genuinely escaping orbit, meaning $x_i\to\infty$, equivalently infinitely many distinct states for this deterministic map on positive integers. They supply no such orbit.

On an escaping orbit, for every $0<\beta<1$ and every nonnegative $h(H)=o(\log H)$, at time density one,
\[
 R_S(x_i-a)\ge x_i^\beta\quad\text{for every }a\notin\{1,2\}\text{ with }\tau(a)\le h(x_i). \tag{1}
\]
If the cycle points are included, the same simultaneous inequalities hold on a set of lower time density at least $2\log_3 2-1=0.26185\ldots$. For every $0<\eta<1$ one may take $h(H)=\kappa\log H$ with an explicit positive $\kappa=\kappa(\beta,S,\eta)$, at a loss of at most $\eta$ in either density bound. Thus the centers can be chosen *after seeing the state*, from an entire growing ordinary inverse tree. No absence of nonstandard cycles is assumed. Actual states of an escaping orbit cannot equal any center in the terminating tree.

## A finite prime-power estimate

Fix an interval of $L\ge1$ ticks and $K\ge0$. Permit any center $a>0$ with $\tau(a)\le K$, so $a\le 2^K$ by $Tz\ge z/2$. Choose
\[
                         D>3^L(2^K+1).                                 \tag{2}
\]
Mark an index $i$ in the interval when $x_i\equiv a\pmod{p^v}$ for some allowed center, $p\in S$, and prime power $p^v\ge D$. Congruence includes exact equality, without taking the valuation of zero. Write $s$ for the number of odd actual states in the interval. Then
\[
\begin{array}{ll}
 \#\{\text{marked, cycle centers omitted}\}\le r(K+1),\\[2mm]
 \#\{\text{marked, cycle centers allowed}\}\le 2(L-s)+r(K+2).
\end{array}                                                            \tag{3}
\]
The estimate is independent of how many eligible centers exist and permits a different one at each observation.

For a word $w$ of $d$ actual parities, let $F_w(z)=(3^q z+C_w)/2^d$ be its unconstrained affine map. The all-odd word maximizes the nonnegative intercept, so $0\le C_w\le3^d-2^d$. If two observations $i<j$ for the same prime have witnesses $a,b$, the smaller of their two prime powers divides
\[
                     2^{j-i}b-3^qa-C_w,
\]
because $2^{j-i}x_j=3^q x_i+C_w$. The absolute value is at most $3^L(2^K+1)$. Thus $F_w(a)=b$ exactly. An integral output of a shortcut word on an integer forces every branch to be physical. The first wrong parity gives reduced denominator two, and every subsequent letter doubles the reduced denominator of a nonintegral dyadic number. In particular $b=T^{j-i}a$, and all the intervening actual parity letters agree with those of $a$.

For a fixed prime, choose its first and last marked index in the block. If cycle centers were omitted, their gap is $<K$ whenever it is positive, since after $K$ steps the first center lies in the cycle forever. This proves the first bound, including an isolated mark and $K=0$. If cycle centers are permitted, the interval from $K$ steps after the first mark up to, and excluding, the last mark has alternating parity. With empty intervals allowed, their union $I$ misses at most $r(K+1)$ marked positions. Split the union into at most $r$ disjoint subintervals each contained in one of the alternating intervals, by sorting on the left endpoints and retaining each new right-hand extension. Thus $I$ has at most $(|I|+r)/2$ odd states. The complement has at most $L-|I|$ odd states. These facts give $3$.

**A fixed-depth improvement in scale.** For any fixed $K,S,\eta>0$, choose $L>r(K+2)/\eta$, and any $D$ as in $2$. Partition time into blocks of length $L$. At lower density at least $1-\eta$, all differences to the transient centers simultaneously have $S$-part $<D^r$. With cycle centers included the lower bound is $2\liminf s_N/N-1-\eta$, where $s_N$ is the odd count up to $N$. The constants do not depend on the source. These density conclusions about nonzero differences apply directly on escape. Unbounded prime powers at a specified transient ordinary center cannot form a positive-mass atom in any time-average limit.

## Moving centers and powers

Set $b=(1-\beta)/r$, $c=b/(8\log3)$, and $\kappa=\eta c/(10r)$. Start at an arbitrary sufficiently late time $t$ with $X=x_t$, and take $L=\lfloor c\log X\rfloor$. Every state in the block belongs to $[X2^{-L},X2^L]$, since $z/2\le Tz\le2z$. All centers allowed by the linear clock have hitting time at most $K=\lceil\kappa(1+c\log2)\log X\rceil$. For large $X$, $2^K<(X2^{-L})/2$. If $R_S(x_i-a)<x_i^\beta$, the $S$-part of the positive difference exceeds $x_i^{1-\beta}/2$. Some prime power in it exceeds or equals $D=2^{-1/r}(X2^{-L})^b$.

This $D$ satisfies $2$ for all large $X$. Indeed $c\log2<1/8$, and its logarithm has leading coefficient at least $7b/8$ in units of $\log X$, whereas $L\log3+\log(2^K+1)$ has leading coefficient at most $b/8+\kappa(1+c\log2)\log2<b/4$. Apply $3$, then begin the next block at $t+L$. Its length diverges on escape, so the number of blocks up to date $N$ is $o(N)$. The completed blocks contribute at most $r\kappa(1+c\log2)N/c+o(N)$ to the total $r(K+2)$ errors. For the final partial block use the same $K,D$ and its actual shorter length in $3$, retaining its own odd count. Its error is at most $r\kappa(1+c\log2)(\log x_0+N\log2)+O(r)$, since $x_t\le 2^t x_0$. The combined error is less than $\eta N+o(N)$. In the sublogarithmic version, for every $\eta>0$ the smaller $h(x_i)$ eventually lies under the resulting linear clock, so let $\eta\downarrow0$.

Finally,
\[
 \log(x_N/x_0)=s_N\log3-N\log2+
    \sum_{i<N,\ x_i\ {\rm odd}}\log(1+1/(3x_i)).
\]
The last sum is $o(N)$ because $x_i\to\infty$, and $\log x_N\ge0$. Hence $\liminf s_N/N\ge\log_3 2$, proving the asserted proportions. Any stronger lower bound for this specific orbit's odd density can be retained in $3$.

## The covering problem

A sufficient route to excluding escape would force, on every proposed escaping orbit, a positive upper proportion of times with a transient center of sublogarithmic hitting time and $R_S(x_i-a)<x_i^\beta$, at any one fixed $\beta<1$ and finite $S$. The center may depend on the observed time. No known coverage of this kind is used. Purely spatial abundance of short predecessors cannot supply it. In fact, for fixed $S,\beta$ and $K=o(\log X)$, the number of integers $x\in[X,2X]$ close to any center of depth $K$ in this sense is $o(X)$. Every such center is at most $2^K=X^{o(1)}$; for some $p\in S$ there is a congruence modulo the first power $p^v\ge 2^{-1/r}X^b$. Counting each progression and all centers gives $O_S(X^{o(1)}(X^{1-b}+1))$. Thus the proposed converse requires a bias of one escaping orbit toward a spatially sparse set.

## Scope against earlier results

Weaver's Theorem 7 controls unshifted cofactors along distinct odd trajectories by return valuations and orbit sparsity. PR159 derives peak bounds on a finite-prime-support subclass. PR161 studies $n+1$, finite core values and the signed all-one trajectory. PR215 obtains pairwise cofactor separation at fixed shifts under specified height and growth conditions using the Subspace Theorem, including the signed closed-word exception. Here the quantitative object is the union of congruences to *every* positive predecessor of 1 within a moving true clock, with no lower exponential growth assumption. The elementary common-prime step is related to the return-numerator argument. Its combination with finite transient length handles the whole increasing family uniformly. None of these comparisons supplies the missing coverage.

[Weaver 138, Theorem 7](https://rstation.ai/problems/collatz/papers/138/v1) · [PR159, peak estimate](https://github.com/GettysburgResearch/collatz/blob/0e7d2841b1591073c6399f91f3b6944ebcdbdbd5/research/allhands-global-closure-20261120/PRIME_SUPPORT_PEAKS.md) · [PR161, fixed shifted cores](https://github.com/GettysburgResearch/collatz/tree/4a0536b587fc91ee0c7bb1b160c06dda16ddbf23/research/source-rigidity-20261120) · [PR215, matched intercepts and smooth parts](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/machinery/phase2/MATCHED_INTERCEPT_AND_SMOOTH_PARTS.md)
