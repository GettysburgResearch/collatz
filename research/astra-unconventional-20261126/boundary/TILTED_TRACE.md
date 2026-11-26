# An atomic component measure above the earlier tilted trace

The component measure in (7)–(9) retains the simultaneous real coordinate and identifies each ordinary unit source. Equations (1)–(6), including **both** scalar tests and their exact exceptional-word issue, are a reconstruction of PR192's published criterion. They are included to identify what the additional coordinate retains. The singular expectation needed for universal convergence is open. No natural-density, predecessor-mixing, or typical-orbit assumption enters. [PR192, original theorem and failed estimates](https://github.com/GettysburgResearch/collatz/blob/045be43632f274dd64faf15714e42cc8de27a2e9/research/astra-high-variance-20261124/CENTRAL_CLOSURE.md)

## The actual integer attached to a word

Work in odd time. Fix a positive length $k$, and read positive exponents $e_1,\ldots,e_k$ **from the terminal backwards**. Let
$$
 S_i=e_1+\cdots+e_i,\qquad r_i=3^i2^{-S_i},\qquad
 B_i=\sum_{l=1}^i3^{l-1}2^{-S_l}.
$$
Write $S=S_k$, $r=r_k$, $B=B_k$. The real forward affine transformation of the chronological word is $x\mapsto B+rx$. Interpret $B$ also in the ternary integers using exactly the same rational number. Let $R$ be the unique odd representative of $B\bmod 3^k$ in $1,\ldots,2\cdot3^k-1$.

**Exact two-sided lift.** The actual odd terminals are precisely $R+2\cdot3^k m$, $m\ge0$. Their respective positive odd sources are $L+2^{S+1}m$ with
$$
                      L=(R-B)/r,\qquad 0<L<2^{S+1}.                 \tag{1}
$$
In particular $R>B$, even when the real offset is very large. To see this, peel $(2^{e_1}R-1)/3$. Its numerator is divisible by three by the first ternary digit. Positivity and oddness follow from $R\ge1$, $e_1\ge1$. The remaining $k-1$ digits give the same divisibility test at the new state by the affine identity. Iterate. Every inverse is an ordinary positive odd integer, and $3x+1=2^ey$ with $y$ odd proves each forward valuation is exact. The linear coefficient gives (1) and the two increments. Conversely every actual terminal is positive, odd and in the displayed ternary class. Thus $L$ is the least odd source of this complete word with an odd terminal.

## The two expectations

Fix one real $1<t<2$. Write
$$
 Z(t)=\frac{3^{t-1}}{2^t-1},\qquad p_t(e)=(2^t-1)2^{-te},\quad e\ge1 .
$$
Take the exponents independent with law $p_t$. This law is a device for summing all words. The function $\log(2^t-1)$ is strictly concave on $t>0$ and equals $(t-1)\log3$ at 1 and 2. Hence $Z(t)<1$ strictly. For each particular word,
$$
                   3^k Z(t)^k\,\mathbb P_t(w)=r^t.                 \tag{2}
$$
The two tests, each taken at this one fixed $t$, are
$$
 A_k=3^k Z(t)^k\,\mathbb E_t[R^{-t}],\qquad
 D_k=3^k Z(t)^k\,\mathbb E_t[{\bf1}_{R>1}(R-B)^{-t}].             \tag{3}
$$
The letter $B$ inside the second expectation remains the finite real offset. These are joint, depth-dependent evaluations at the least positive odd representative. Replacing the latter by a Haar point changes the question.

**Theorem.** $A_k\to0$ if and only if no positive ordinary orbit escapes. $D_k\to0$ if and only if every positive ordinary orbit reaches 1. In either test, a zero liminf is equivalent to a zero limit.

For the first test, complete the sum over the terminal progression. By (1)–(2) the result is
$$
 \sum_{\substack{x>0\\x\ {\rm odd}}}x^{-t}
 \prod_{i=0}^{k-1}\left(\frac{3U^i(x)}{3U^i(x)+1}\right)^t .       \tag{4}
$$
Indeed $rx/U^k(x)$ is the product inside (4) before taking its $t$-th power. The completed mass is decreasing. Repetition forces eventual periodicity, and then the product tends to zero. On an injective infinite trajectory the product is bounded below by a strictly positive constant. An elementary uniform reciprocal proof is given below. Bounded convergence against the summable weights $x^{-t}$ proves the first equivalence.

For the second test, sum at every actual terminal $q=R+2\cdot3^k m$ with $q>1$, replacing the denominator by $q-B$. The result is exactly
$$
                    \sum_{\substack{x>0\ {\rm odd}\\U^k(x)>1}}x^{-t}. \tag{5}
$$
This uses $q-B=rx$, and each actual source occurs in exactly one word. Since $U(1)=1$, the events in (5) decrease to failure to reach 1. Any single failure has strictly positive weight. Even starts first strip twos, so the equivalent assertion covers all positive integers.

In both tests the discarded $m\ge1$ terms (including those with $R=1$) have total at most
$$
 3^k Z(t)^k(2\cdot3^k)^{-t}\sum_{m\ge1}m^{-t}
 =2^{-t}\zeta(t)(2^t-1)^{-k}.                                     \tag{6}
$$
For the shifted test use $R-B>0$ before dropping the positive residual. The error decays exponentially. Thus the approximate tests have limits and zero liminf suffices.

The same calculation with $t=2$ gives the scalar tilted trace kernel of Weaver, Proposition 11, with the square of the actual multiplier. Here $1<t<2$ makes the unnormalized one-step mass strictly subunit. The scalar test (3) still contains $3^k$ and an unbounded test at the shrinking physical lattice scale. The subunit mass by itself gives no decay in (3). [Ternary Syracuse laws, §8.1](https://rstation.ai/problems/collatz/papers/9)

## Uniform simple-path correction, derived here

On an injective shortcut orbit, $T^n$ is injective on its states. Fix $X\ge2$ and $n=\lceil\log_2 X\rceil$. Each shortcut parity word occurs on one residue modulo $2^n$. This follows by the usual lifting induction. Starts differing by $2^n$ keep the first $n$ bits and have images differing by the odd number $3^b$. Thus the number of inputs in $[1,X]$ having $b>3n/5$ odd bits is at most $2^{H_2(3/5)n}$ by the elementary binomial bound. For the remaining inputs,
$$
 T^n x=3^b2^{-n}x+\beta\le3^{3n/5}+(3/2)^n .
$$
For the offset use $\beta+1\le(3/2)^n$ by induction on physical steps. The number of these distinct images is bounded by the last upper bound plus one. All three exponents relative to $X$, namely $H_2(3/5)$, $(3/5)\log_2 3$, and $\log_2(3/2)$, are strictly below one. Hence the number of visited states below $X$ is $O(X^\theta)$ for some absolute $\theta<1$. The odd states are a subset. Dyadic summation yields a uniform bound on $\sum 1/x$ over each such orbit, with $O(M^{\theta-1})$ for its contribution above $M$. A nonrepeating odd orbit gives a nonrepeating full shortcut orbit by determinism. This proves the positive lower bound used in (4). This elementary packing argument is included for self-containment. The repository contains stronger versions.

## A purely atomic limit on every escaping component

Let $a=a_0,a_1,\ldots$ be one injective forward **odd** orbit of positive ternary units. Discard an initial multiple of three if necessary. Put $r_{aj}=3^j/2^{S(a,j)}$ for its exact chronological multiplier up to $a_j$. At $a_j$, take every finite inverse word whose ordinary source $x$ is itself a ternary unit. This last condition has the exact residue test $v_3(a_j-B)=k$ for a word of depth $k$, including the empty word. Because $a_j$ is nonperiodic, each such $x$ has just one qualifying word. Its exact multiplier is $r_{xj}$. Form the finite-mass measure
$$
 \mu_j=\sum_{\substack{x\rightsquigarrow a_j\\x\ {\rm odd\ unit}}}
       \left(\frac{r_{xj}}{a r_{aj}}\right)^t\delta_{z_x},\qquad
 z_x=\frac{x r_{xj}}{a r_{aj}}.                                    \tag{7}
$$
Appending the same ordinary suffix to the two routes preserves $z_x$ exactly. The predecessor sets increase, and their union is the whole odd-unit component $E$ of trajectories eventually intersecting this ray. If $W_{xj}=x r_{xj}/a_j$, the simple-path bound gives $c\le W_{xj}\le1$ with absolute $c>0$, including the $a$-path. Thus $c\le z_x\le1/c$. The measures increase and converge in total variation to
$$
                       \mu_E=\sum_{x\in E}(z_x/x)^t\,\delta_{z_x}.  \tag{8}
$$
The proof is just tail convergence of $\sum x^{-t}$. Distinct units have distinct positive rational addresses. Equality would give $x/y=2^u3^v$ for integers $u,v$, but both $x,y$ are coprime to six. Therefore at every atom
$$
                     x=z_x\,\mu_E(\{z_x\})^{-1/t}.                 \tag{9}
$$
One limiting real measure remembers *each* ordinary unit source in this component. The normalization is anchored to the specified $a$. Restricting to units is essential for this arithmetic uniqueness. At $t=2$, (7) is the simultaneous real-coordinate version of the tilted Green trace with the one extra ternary digit. This atomic weighting differs from the canonically density-weighted fixed-root real fibre in Weaver's paper 19. [Geometry, integer fibres, and dyadic equidistribution, §9.2](https://rstation.ai/problems/collatz/papers/19)

The conclusions (4)–(9) exhibit the obstruction in the independent-exponent model. Under a hypothetical escape one positive source supplies a persistent term, and all of its component supplies the atomic limit. Independent-exponent tail or entropy estimates that discard exceptional shrinking residue cells cannot exclude those terms. No pointwise bound on either singular expectation in (3) has been obtained.
