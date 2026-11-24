# All fixed-triple first-fusion moments below three halves

Fix three ordinary affine arms $3^{a_i}n+c_i$ and give the binary parameter its fair prefix law. Let $\sigma$ be the first clock when any two complete affine profiles agree and set $A_t=\{\sigma>t\}$, $P(t)=\Pr(A_t)$. The labeled grades are $L_i(t)=a_i+p_i(t)$. At every clock sort the three grades, writing their adjacent gaps as $u,v\ge0$ and their spread as $U=u+v$. All constants can depend on the fixed triple and the chosen moment.

**Theorem.** For every $p<3/2$ with $p>0$,
$$
                 \mathbb E(1+\sigma)^p<\infty,\qquad
                 P(t)=o(t^{-p}).                                  \tag{1}
$$
Consequently every interval of $N$ ordinary parameters on which the forms are positive contains $o(N/(\log N)^p)$ sources still showing three distinct affine profiles at clock $\lfloor\log_2N\rfloor$, uniformly in interval location. The same assertion holds for the event of at least three surviving classes among any fixed finite family. The proof gives no lower bound or endpoint estimate at $p=3/2$. Exactly two surviving classes are outside its event.

## Pair input and low-level occupation

We use two written inputs. From [TRIPLE_FIRST_FUSION.md](TRIPLE_FIRST_FUSION.md), $P(t)\ll (1+t)^{-1}$ and the dyadic small-gap estimate, for $H\ge2$, is
$$
 \sum_{H\le t<2H}\Pr(A_t,\ \min_{i<j}|L_i(t)-L_j(t)|\le K)
 \ll (1+K)^2[P(\lfloor H/2\rfloor)+e^{-cH}].                      \tag{2}
$$
The second input is equation (21) within the proof of Theorem 6 of [Conditional clocks and source couplings for Collatz synchronization, v1](https://rstation.ai/problems/collatz/papers/13/v1). This finite, **unconditioned** bound starts a pair with arbitrary offset and gap $2\le k\le K_0$, stops after $\ell$ mixed jumps or at gap one, and denotes physical block duration by $S$ and completion of the quota by $F$. For $0<e\le1$, $R_*=\lceil\log_2(K_0+\ell+1)\rceil+6$ and $\ell\ge4R_*^2$, it states
$$
 \Pr(F,\ |S/\ell-2|>e)
 \le C\log^2(\ell+2)(R_*/\sqrt\ell)^{e^2/(18\log2)}.             \tag{3}
$$
This particular uniform initial-state estimate handles long common-branch holding times. The qualitative clock law for a completed excursion would not suffice here.

For a dyadic $H=2^j$ partition $[H,2H)$ into consecutive physical blocks of $B=2^{\lfloor j/4\rfloor}$ clocks, which divides $H$. Call a block deep if the triple is live and all its pair gaps at its starting prefix exceed $K_1B$, where $K_1\ge3$ is a fixed constant to be chosen. Throughout such a block every trajectory retains the same strict order and the triple remains live.

For every $\eta>0$ and sufficiently large $H$, uniformly over deep prefixes, each pair's expected mixed count $M_{ij}$ on the next $B$ physical steps satisfies
$$
           |\mathbb E(M_{ij}\mid\mathcal F_{\rm start})/B-1/2|
           \le \eta.                                               \tag{4}
$$
Indeed, choose $\ell_\pm=\lfloor(1/2\pm\eta/4)B\rfloor$ for $0<\eta\le1$ (larger $\eta$ is automatic). Choose fixed $e>0$ sufficiently small that $(2+e)\ell_-<B<(2-e)\ell_+$ for large $B$. Both quotas occur almost surely: each positive-level wait is finite, and starting above $K_1B$ the gap cannot get to one within $\ell_+$ mixed jumps. The pair has gap $O(H+\max_{i,j}|a_i-a_j|)$, the offset may be arbitrary, and $R_*=O(\log H)$. The right side of (3) tends to zero at either quota. Hence the pair's $B$-clock mixed count lies between the quotas except with probability $o(1)$, uniformly conditional on the shared triple prefix. The count is at most $B$ on the exceptional outcomes. Each pair separately has the exact fair canonical future from its state; pair independence is unnecessary.

## Drift of a power of the spread times the two adjacent gaps

Fix $0<\gamma<1$. On sorted gaps define
$$
              f(u,v)=uv(u+v)^\gamma,\qquad f(0,0)=0 .
$$
For a strictly ordered deep block, keep the labels in that order. At a step the two gap increments $d_1,d_2$ are a fixed pair or its simultaneous negative, each with probability $1/2$ given the whole past. Thus their conditional means vanish. The squares $d_1^2,d_2^2,(d_1+d_2)^2$ are the mixed-parity indicators for pairs $12,23,13$, respectively. By (4), the conditional expected sum of the one-step covariance matrices over a deep block, divided by $B$, is entrywise within $O(\eta)$ of
$$
               \Sigma=\begin{pmatrix}1/2&-1/4\\-1/4&1/2\end{pmatrix}.     \tag{5}
$$
In particular the off-diagonal entry follows from half the difference of the third mixed count and the first two. Equation (5) concerns accumulated conditional covariances; it never treats the two gaps as independent walks.

At $u,v\ge0$, $U=u+v>0$, direct differentiation gives
$$
 \frac12\sum_{i,j}\Sigma_{ij}\partial_{ij}f
 =\frac{\gamma-1}{4}
       \left(U^\gamma+\gamma uv\,U^{\gamma-2}\right)
 \le -\frac{1-\gamma}{4}U^\gamma.                                \tag{6}
$$
To verify the cancellation, the factor multiplying $1/4$ is
$f_{uu}+f_{vv}-f_{uv}$; substituting $f=uvU^\gamma$ simplifies to the expression shown. Also $|\partial^k f|\le C_\gamma U^{2+\gamma-k}$ for $k=2,3$. These bounds follow by differentiation, or by homogeneity and regularity on the compact segment $u+v=1$ with $u,v\ge0$. They remain valid at its endpoints because the real expression is smooth wherever $u+v>0$.

Let $U_*$ denote the initial spread of a deep block. The spread stays between $U_*-B$ and $U_*+B$, and both gaps change by at most $B$. Conditional Taylor expansion at each current state has no first-order expectation. Replacing the Hessian in its quadratic term by the Hessian at block start costs $O_\gamma(B U_*^{\gamma-1})$ per step, and the third-order remainder costs $O_\gamma(U_*^{\gamma-1})$ per step. This follows from the previous derivative bounds throughout each intervening segment; deep order keeps every such gap nonnegative and $U\asymp U_*$. Combining over the entire block with (5)--(6) gives
$$
 \mathbb E(f_{\rm end}-f_{\rm start}\mid\mathcal F_{\rm start})
 \le -\tfrac{1-\gamma}{4} B U_*^\gamma
      + C_\gamma(\eta+B/U_*) B U_*^\gamma.                        \tag{7}
$$
Choose $\eta$ small in terms of $\gamma$ and then $K_1$ large, so the last coefficient is less than $(1-\gamma)/8$. Fixed initial finitely many shells prior to the uniform threshold for (4) cause a finite additive cost. Since the spread on a deep block is comparable to $U_*$, its negative expected drift pays a fixed multiple of the expected sum of $U_t^\gamma$ over all clocks in that block.

## The cost of blocks near a tie

Set the potential to zero from first fusion onward. At a live, strictly ordered step, current integer gaps are at least one and can drop by at most one; the old order stays valid on the next step, with ties allowed. The next spread is at least $U-1$ for $U\ge2$. Taylor expansion to second order with bounded centered increments shows the one-step conditional positive drift of the killed potential is at most $C_\gamma(1+U)^\gamma$. At a grade tie the old potential is zero, at least one new gap is at most one, and the new spread is at most $U+1$. The one-step positive drift is then at most $(1+U)^{1+\gamma}$.

In a live block whose starting gaps fail the depth test, some labeled pair starts within $K_1B$ and stays within $(K_1+1)B$ throughout the block. The indicator of starting in this type of block is adapted at every later clock in the block, so the one-step drift bounds can be summed on it with $A_t$. Control the sum of the positive drift, **and** the expected sum of $U_t^\gamma$ over these live clocks, by charging two terms:
$$
 \begin{split}
 &\sum_{H\le t<2H}\mathbb E[(1+U_t)^\gamma
       {\bf1}_{A_t,\ \min\mathrm{\ gap}\le(K_1+1)B}],\\
 &\sum_{H\le t<2H}\mathbb E[(1+U_t)^{1+\gamma}
       {\bf1}_{A_t,\ \mathrm{tie}}].
 \end{split}                                                       \tag{8}
$$
Each signed difference of two fixed labeled grades has bounded, centered increments. At a fixed clock on the shell, Azuma therefore gives $U_t\ll_{\rm init}\sqrt{H\log(2H)}$ except with probability $O_{\rm init}(H^{-6})$, by choosing the constant large. The deterministic bound $U_t\ll_{\rm init} H$ controls exceptional contributions to (8), summably in dyadic $H$. On the remaining profiles use (2) with $K=(K_1+1)B$ and $K=0$, respectively, and the preliminary $P(H/2)\ll H^{-1}$. The two shell costs are
$$
 O_\gamma\!\left(
  H^{(\gamma-1)/2}(\log(2H))^{\gamma/2}
 +H^{(\gamma-1)/2}(\log(2H))^{(1+\gamma)/2}
 \right).                                                         \tag{9}
$$
Both are summable over dyadic shells precisely for the range $\gamma<1$ used here. Already-dead blocks cost zero.

Telescope the expected potential across all complete blocks up to any dyadic terminal endpoint. It is nonnegative. Thus the negative deep-block charge (7) is bounded by the initial potential and the total summable positive error (8). Combining the deep and remaining occupation charges yields
$$
                    \sum_{t\ge0}\mathbb E[U_t^\gamma{\bf1}_{A_t}]<\infty .
                                                                        \tag{10}
$$

## From spread occupation to a first-fusion moment

For dyadic $H$ split the live population at $U_t=\sqrt{\epsilon H}$, with fixed $\epsilon>0$. On the high-spread part, $H^{\gamma/2}\le\epsilon^{-\gamma/2} U_t^\gamma$, so its weighted total is finite by (10). On the rest at least one pair gap is at most $\sqrt{\epsilon H}$. Equation (2) bounds this shell's low-spread count after weighting by $O(H^{\gamma/2})$ by
$$
  C\epsilon H^{1+\gamma/2} P(H/2) + O_\epsilon(H^{1+\gamma/2}e^{-cH})
$$
for $H\ge1/\epsilon$, with finite earlier shells. The first term is at most $C'\epsilon$ times the weighted survival sum over the **earlier** shell $H/4\le t\le H/2$, because $P$ is nonincreasing and $t^{\gamma/2}\asymp H^{\gamma/2}$ there. Sum up to a finite dyadic cutoff. The earlier shells have bounded overlap. Taking $\epsilon$ so small that the resulting coefficient is below $1/2$ allows absorption in this finite sum, uniformly in the cutoff. Hence
$$
                   \sum_{t\ge0}(1+t)^{\gamma/2}P(t)<\infty.        \tag{11}
$$
Tail summation gives (1) at $p=1+\gamma/2$, covering every $1<p<3/2$ and thus all smaller positive moments. The little-o follows, for example, by applying the tail sum on $[t/2,t]$. The two-full-block upper bound for actual integer intervals and the finite union over triples complete the transfer.

The proof concerns the symbolic first fusion of three arms. Its $o((\log N)^{-p})$ normalized error is summable on the native exponentially spaced head rows. It leaves a two-class contribution to the weighted basin problem, including the explicit residual edge in [QUARTET_COLLAPSE.md](QUARTET_COLLAPSE.md).
