# Positive cycles force delayed mass in the original marked-depth differences

At positive odd $y$ let $L_{d,y}(t)$ be the original raw all-visit CDF of the normalized complementary mark $B=A_wx/y$, where $x$ is the odd source of a length-$d$ inverse word of total division clock $s$, $A_w=3^d2^{-s}$, and the word weight is $A_w\rho_1(x)$ with $\rho_1(x)=x\bmod3$. Let
\[
  \pi(y)=\frac1{y(3y+1)},\qquad
  D_d=\sum_y\pi(y)\sup_{0\le t\le1}|L_{d+1,y}(t)-L_{d,y}(t)|,\qquad
  \mathcal T_D=\sum_{d\ge D}D_d .
\]
These nonnegative quantities use a separate unrestricted CDF threshold at each site. Their summability is the same-pass [original marked trace theorem](../escape/SUMMABLE_ORIGINAL_TRACE.md). The lower bounds below use the finite rows directly, so remain valid as extended-real inequalities without this external convergence input.

For every positive integer cycle $C$ of least odd period $p$, put
\[
      \lambda=\prod_{x\in C}\frac{3x}{3x+1},\qquad
      g=-\log\lambda,\qquad S=\sum_{x\in C}1/x .
\]
For each integer $K\ge0$,
\[
           \mathcal T_{Kp}\ge\frac{\lambda^{K+1} S^2}{8(1-\lambda)}.
                                                              \tag{1}
\]
For $K=\lceil1/g\rceil$ in particular,
\[
        (Kp)\mathcal T_{Kp}
            \ge\frac98 e^{-1-2g}\,p.                         \tag{2}
\]
Separate cycles make additive contributions in (1) whenever their respective starting depths are at or above the chosen cutoff. The circular pair sum in (1) retains all $p$ offsets, including returns at nonintegral fractions of a lap.

Hence $\mathcal T_D=O(1/D)$ would force **finitely many positive integer cycles**. For an explicit full exclusion criterion, the published bound $p>137{,}500{,}000{,}000$ at every additional cycle and the separate bound $g<0.024$, both using the computational verification below $2^{71}$, give
\[
             \sup_{D\ge1}D\mathcal T_D
                     \le51{,}562{,}500{,}000
              \quad\Longrightarrow\quad
              \text{only the known positive cycle exists}.     \tag{3}
\]
The estimate on the left remains open. At a possible extra cycle the witnessing depth in (2) is at least $3\min(C)$, since $g\le p/[3\min(C)]$. Mere summability of $D_d$ guarantees $\mathcal T_D\to0$ without supplying the rate in (3). [Hercher, Corollary 29 and corrigendum](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html) · [Paper 217, total gap of extra cycles](https://rstation.ai/problems/collatz/papers/217/v1)

## Native atoms cannot cancel at the next depth

At positive depth all positive-weight words have $3\nmid x,y$. The target is an odd image, and a terminal nonunit has $\rho_1(x)=0$. At depth zero the nonunit target has zero mass as well. Every positive-mass atom has
\[
                   v_3(B)=v_3(3^d2^{-s}x/y)=d .
\]
Thus the sets of actual atom locations at adjacent depths are disjoint, including after a sum over different positive targets. Their closures may still intersect. At a fixed target and depth, $B$ also determines the word: after cancelling $3^d/y$, equality reads $2^{-s}x=2^{-s'}x'$. Oddness forces $s=s'$, then $x=x'$, and the actual length-$d$ forward path from that source is unique. The mass at an atom is exactly its word weight.

The jump of the difference of the two CDFs at an old positive-mass atom is its entire old weight in absolute value. At least one of the value or its left limit therefore has absolute value at least half that weight. All these marks are positive, so their left limits are accessible from the CDF interval, including at the right endpoint. This gives a lower bound on $D_d$ by **half the summed largest positive atom** at each target. Adjacent pure atomic measures may converge to one another in CDF distance even though their atoms never coincide.

Fix a cycle, write $x_i$ for its actual odd vertices with indices modulo $p$, and choose $d=kp+r$, $0\le r<p$. The path starting at $x_{i-r}$ and ending at $x_i$ after these $d$ forward odd steps has survival product at least $\lambda^{k+1}$. The remaining $r$ consecutive factors of a lap have product at least $\lambda$. Its affine multiplier equals this survival times $x_i/x_{i-r}$ by the single-edge identity. After multiplication by $\pi(x_i)$, its positive atom contributes at least $\lambda^{k+1}/[x_{i-r}(3x_i+1)]$, since $\rho_1(x_{i-r})\ge1$. Consequently
\[
       D_{kp+r}\ge \frac{\lambda^{k+1}}8
                     \sum_{i\bmod p}\frac1{x_i x_{i-r}}.       \tag{4}
\]
All $p$ values of $r$ together enumerate every ordered pair of cycle sites exactly once, giving $S^2$. Summing the geometric series at $k\ge K$ proves (1). The inequalities $g\le S/3$, $1-\lambda\le g$, $Kg\ge1$ and $(K+1)g\le1+2g$ prove (2). With $g<0.024$, $e^{1+2g}<3$, giving a strict $3p/8$ lower bound and (3). For finiteness without *any* separate gap input, distinct positive odds give
\[
       g\le\tfrac13\sum_{j=1}^p(2j-1)^{-1}
         \le\tfrac13+\tfrac16\log(2p-1).
\]
Thus the right side of (2) tends to infinity at least as a constant times $p^{2/3}$. For any fixed $p$ there are only finitely many positive integer cycles: their full clock satisfies $2^h/3^p\le(4/3)^p$, hence $h\le2p$, and the finitely many words specify their rational roots. An infinite collection must have unbounded $p$.

As another consequence of (4), without choosing a separate depth per cycle,
\[
      \sum_{d\ge0}dD_d
             \ge \sum_C \frac{p_C\lambda_C^2 S_C^2}
                              {8(1-\lambda_C)^2}
             \ge\frac98\sum_C p_C\lambda_C^2 .                 \tag{5}
\]
In the first inequality use $kp+r\ge kp$ and sum $k\lambda^{k+1}$. Disjoint targets permit Tonelli's theorem even for infinitely many cycles. These lower bounds expose the precise extra information required from depth cancellation.

## The same delay at one common physical threshold

There is a complementary stationary proof which keeps the same threshold at every target and time. Let $c_0>0$ be a uniform survival floor on distinct-state segments and put $t=c_0/4$. At a nonperiodic target all finite inverse paths are simple, so $L_{d,y}(t)=0$ at every depth. At a site on $C$, remove the complete initial reverse laps from any inverse path; at most $\lfloor d/p\rfloor$ were removed and the remaining departed vertices are distinct. Thus every supported mark is at least $c_0\lambda^{\lfloor d/p\rfloor}$. In particular the finite CDF vanishes at this threshold for $d\le p\log 2/g$.

Write $L_{\infty,y}(t)=h(y)\nu_y([0,t])$ for its limiting original row. The geometric renewal law gives $\nu_y([0,t])\ge\lambda t\ge c_0t$. Let $c=17\alpha_0/336$ be the constant of [the raw cycle floor](CYCLE_TRACE_LAW.md). Then each invisible site contributes at least $cc_0t/y$ to the weighted absolute CDF error. For
\[
             E_d(t)=\sum_y\pi(y)|L_{d,y}(t)-L_{\infty,y}(t)|,
\]
we obtain
\[
 \mathcal T_d\ge E_d(t)\ge
        3cc_0t\sum_{C:\,dg_C\le p_C\log2}g_C,\qquad
 \sum_{d\ge0}E_d(t)\ge3cc_0t\log2\sum_C p_C.                 \tag{6}
\]
The first upper comparison is the triangle inequality and pointwise CDF convergence in the marked trace theorem. Unlike the finite-atom proof, this test never adapts to the cycle clock or the site. It shows why arbitrary late positive cycles impede quantitative convergence of a single marked observable even after removing target one.

The [exact finite control](check_cycle_trace.py) checks the ordinary unit-parent floor, native marks and adjacent CDF jumps with per-step exponents at most eight, and the all-offset lap identities on primitive positive rational traces. [Recorded counts](../../../reports/astra-global-20261128/cycles/CYCLE_TRACE.json)
