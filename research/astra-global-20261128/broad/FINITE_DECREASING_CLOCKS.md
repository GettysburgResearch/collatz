# Finite decreasing progressions and changes of slope on every nonperiodic orbit

**PROPOSED, elementary finite proof.** For $a,b\ge0$, $h\ge1$ form
$$
 1^a0\,1^b0\,1^{b-h}0\,1^{b-2h}0\cdots
$$
through the last nonnegative gap, stopping before a negative exponent. Any prefix of this finite word matched by an ordinary positive source $x$ has length
$$
 L\le20\,000\log_2(x+1). \tag{1}
$$
No infinite dyadic series exists for the formally continued decreasing schedule. The proof only uses even positions that the observed finite prefix actually contains.

Together with [the increasing case](QUADRATIC_CLOCK_PADE.md), this bounds the physical time in any finite progression of successive odd-gap lengths, uniformly in its slope and arity. Zero slope requires the cycle exception in §4.

## 1. Finite affine remainders

Put $B=\log_2(x+1)$, $C(j)=j(j-1)/2$, $\gamma=\log_23$, $c=\gamma-1$. If $t_j$ is the time of the $j$th even input (numbered from zero), $u_j=t_j-j$ is the odd input count up to that time. As soon as the initial zero is observed, let $a=t_0$ and $y=-(x+1)(3/2)^a\in\mathbb Z$. For any actually observed $j$,
$$
 y-\sum_{l<j} 2^l(2/3)^{u_l-a}
    =-\frac{2^{t_j-a}3^a}{3^{u_j}}(T^{t_j}x+1).
 \tag{2}
$$
Thus its valuation is exactly $t_j-a$, since $T^{t_j}x$ is even. Formula (2) follows by multiplying the finite shifted affine identity through time $t_j$; it uses no subsequent parity bit. Also $\log_2(1+|y|)\le1+\gamma B$.

Here $u_j=a+bj-hC(j)$. Use $q=(2/3)^h$, $z=2(2/3)^b$, $Z=v_2(z)=b+1$, $p_l=z^l q^{-C(l)}$. Then $v_2(p_j)=t_j-a=jZ-hC(j)$. As in the increasing proof, set $n=2s$, $m=s$, $N=n(n+m)$, $M=C(m)$, $E_k=C(k)+km$, $R(X)=\prod_{j=1}^n(1-q^jX)=\sum c_kX^k$ and $D=z_1^n z_2^m q_1^M q_2^N$ with positive reduced numerators and denominators.

## 2. Truncated interpolation and common factors

Let
$$
 B_k=Dc_k z^{-k}q^{E_k},\quad B_*=\sum_{k=0}^nB_k,\quad
 A_*=\sum_{k=0}^n B_k \sum_{l=0}^{m+k}p_l.
$$
The exponent ranges in the increasing proof give $B_k,B_*,A_*\in\mathbb Z$ also for this $q<1$. This time each cleared $q$-monomial is bounded by $q_2^{M+N}=3^{h(M+N)}$. The same bound (6) there holds for $\max(|A_*|,|B_*|)$.

Choose $s\ge1$ such that the even input of index $2n+m+2=5s+2$ has been observed and $b\ge200hs$. Let $j_k=n+m+k+2$. Splitting each sum at $j_k$ gives the *finite* identity
$$
 B_* y-A_* =
 D\,R(q^{-(n+1)})z^{n+m+1}q^{-C(n+m+1)}
  +\sum_{k=0}^n B_k\left(y-\sum_{l<j_k}p_l\right). \tag{3}
$$
Indeed the interior terms aggregate over $t=1,\ldots,n+1$ with $l=t+m+k$. The terms $1\le t\le n$ vanish from $R(q^{-t})=0$, and the last term is the one displayed.

In $c_k$ the least power $q^{C(k+1)}$ occurs once, so its valuation is $hC(k+1)$. Consequently
$$
 v_2(B_k)=nZ+hM-kZ+h(k^2+km).
$$
These decrease strictly to $v_2(B_n)=h(M+N)=:D_0$ under $b\ge200hs$. All $p_l$ with $l\le n+m$ are dyadic integers, so $A_*,B_*$ are divisible by $2^{D_0}$ and $B_* /2^{D_0}$ is odd. The first term on the right of (3) has valuation
$$
 W=(2n+m+1)Z-h(n+1)(n+m).
$$
In fact $v_2(R(q^{-(n+1)}))=-hC(n+1)$, by evaluating each factor. Every tail term in (3) has strictly greater valuation. By (2) its valuation equals that of $B_kp_{j_k}$. For $t=n+2$, the identity for $C(k+m+t)$ gives
$$
 v_2(B_kp_{j_k})=v_2(D)+(t+m)Z-h C(t+m)+h[C(k+1)-kt].
$$
The last bracket is minimized at $k=n$. Subtracting $W$ at this minimum gives $Z-h(2n+m+1)>0$. Therefore $B_* y-A_*$ is nonzero and its valuation is exactly $W$.

Write $H'=\max(|A_*|,|B_*|)/2^{D_0}$. Dividing the previous height bound by $2^{D_0}$ gives
$$
 H'\le(3s+1)2^{2s}(2\cdot3^b)^{3s}(3/2)^{h(13s^2-s)/2}.
$$
The exact valuation after division is
$$
 W'=W-D_0=(5s+1)(b+1)-h(25s^2+5s)/2 .
$$
Since the nonzero integer $(B_*y-A_*)/2^{D_0}$ has absolute value at most $(1+|y|)H'$,
$$
 \log_2(1+|y|)\ge W'-\log_2 H'\ge (5-3\gamma)bs-21hs^2\ge bs/8. \tag{4}
$$
For the middle estimate use $\log_2(3s+1)\le2s$, $c<3/5$, and $h,s\ge1$; the combined quadratic and linear $h$-cost is at most $(30+12c)hs^2/2$, in addition to $2hs^2$ covering the logarithm. For the final inequality use $5-3\gamma>4/17$ and $b\ge200hs$.

## 3. Every cutoff

If the prefix includes at most two zeros, its length is below $8B$ by the same three-run estimate as in the increasing case. Otherwise let $K\ge2$ be its last observed even index. The initial gaps satisfy $a\le B$, $b\le\gamma B$, and $K\le b/h+1$, since the schedule stops before a negative gap. Including a possibly incomplete last odd run,
$$
 L\le a+(K+1)(b+1).
$$
Put $s=\lfloor\min((K-2)/5,b/(200h))\rfloor$. If $s=0$, then either $K<7$ or $b/h<200$, so $K\le201$. This gives $L<530B$. If $s\ge1$ then (4) applies, while either $K<5(s+1)+2$ or $K<200(s+1)+1$. Hence $K+1\le402s$. Since $b\ge200hs\ge1$, (4) gives $L\le B+804bs\le B+6432(1+\gamma B)<20\,000B$, as claimed.

## 4. The zero slope and a changing-curvature consequence

For $1^a0(1^b0)^\infty$, compare the state just after the first zero to the rational periodic phase for $1^b0$, of height at most $3^{b+1}$. Unless it equals this rational phase, its remaining match length is at most $\log_2(T^{a+1}x+1)+\gamma(b+1)$. Once two zeros have been seen, $a\le B$, $b\le\gamma B$ and $\log_2(T^{a+1}x+1)\le\gamma B$. Cutoffs before two zeros have length at most $B+\gamma B+1$. Exact periodic equality cannot occur on a non-eventually-periodic orbit. In fact $b=0$ gives fixed point zero, $b\ge2$ gives a negative periodic point since $3^b>2^{b+1}$ and the affine constant is positive, and $b=1$ gives the usual positive cycle.

For any non-eventually-periodic ordinary orbit, write the infinite word as blocks $1^{g_i}0$, $i=0,1,\ldots$, with consecutive evens allowed when $g_i=0$. Partition its gap sequence greedily into disjoint maximal arithmetic progressions, starting a new block of gaps after the preceding maximal block ends. If a progression were infinite, it would give an infinite positive-slope match, an eventually periodic tail, or eventually negative gap lengths. Each physical time block, including the initial run of its progression, is therefore finite and has length at most $C B_i$, $C=20\,000$, by (1), (2) of the increasing proof or the zero-slope bound. If a partial final block cuts off before seeing the first two gaps the same bound applies. Along a block $B_{\rm end}\le B_{\rm start}+c\,(\text{length})$. Thus a time segment from the original start through $t$ using $r$ such blocks satisfies
$$
 t\le \frac{B_0}{c}\big((1+cC)^r-1\big).
$$
Every completed block except the last witnesses a nonzero second difference $g_{i+2}-2g_{i+1}+g_i$ at its boundary, once the next gap is known. This yields at least $\log(1+ct/B_0)/\log(1+cC)-O(1)$ slope changes witnessed by time $t$. The possible final incomplete gap affects at most one boundary. The lower bound concerns an arithmetic regularity of the gap sequence; it allows the frequency of evens to tend to zero.
