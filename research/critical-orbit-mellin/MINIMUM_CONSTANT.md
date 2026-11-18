# A positive asymptotic constant for the least-predecessor law

Earlier minimum theorems compare prescribed words and depth ranges, and Paper 146 already uses dependent-branch implicit renewal for the stationary Syracuse density. [Prior-work comparison](PRIOR_WORK.md)

**PROPOSED.** There is a constant $c_*\in(0,1]$ such that the relative odd natural density of targets with least predecessor below $\theta t$ satisfies
$$
 d(\theta)\sim c_*\theta^2\quad(\theta\downarrow0).
$$
This identifies a limit beyond the [two-sided quadratic estimate](MINIMUM_SHARP.md). The proof uses a one-dimensional renewal theorem after exponential smoothing. No independence between inverse branches at a given ternary target is required.

At a Haar target let $M$ be the supremum of $J=3^q/2^A$ over legal words, with the empty word included. It is attained almost surely, since the sum of $J^{3/2}$ over words is finite almost surely by [FS-014](../fixed-floor-shells/PRESSURE_LAW.md). Put $f(t)=e^{2t}\Pr(M>e^t)$. The quadratic theorem bounds $f$ uniformly on the line and away from zero for all sufficiently large $t$ (strict tails follow by using a slightly larger threshold). For $t<0$, $f(t)=e^{2t}$.

Write $Y=\log(3/2^a)$ where $a$ has probabilities $3\cdot4^{-a}$ for $a\ge1$, and $\mu=\mathbb E Y=\log(3/2^{4/3})>0$. Let
$$
 D(t)=f(t)-\mathbb E f(t-Y).
$$
Indeed, on the legality cylinder of first letter $a$ the new target is Haar and its probability is $1/3$. A union bound for the branches giving $M>e^t$ for $t\ge0$ therefore gives $D(t)\le0$. For $t<0$ both terms are integrable, the second since $\mathbb E\int_{-\infty}^{-Y} f(s)ds\le1/2+\|f\|_\infty\mathbb E Y^-$. Also for every interval $[a,b]$, shifting an integral of bounded $f$ by $Y$ gives
$$
 \left|\int_a^b D(t)dt\right|\le2\|f\|_\infty\mathbb E|Y|.
$$
The fixed sign on the positive half-line consequently implies $D\in L^1(\mathbb R)$.

Use smoothing $\widehat v(t)=\int_{-\infty}^t e^{s-t}v(s)ds$. Then $\widehat f=\widehat D+\mathbb E\widehat f(\cdot-Y)$, and $\widehat D$ is directly Riemann integrable: the sum over integer intervals of the suprema of its absolute value is bounded by $C\int|D|$ using the summable unit-interval suprema of the one-sided exponential kernel, and continuity follows from continuity of $L^1$ translations of $D$ and the bounded kernel. The same upper-sum bound holds uniformly after any translation.

For a reduction to the ordinary positive-increment key renewal theorem, let $S_n$ sum iid copies of $Y$, $S_0=0$, $\tau=\min\{n:S_n>0\}$, and $H=S_\tau$. Since $\Pr(\tau>n)\le\Pr(S_n\le0)\ll e^{-cn}$, the ladder time has finite expectation. Stopping the smoothed identity gives
$$
 \widehat f(t)=G(t)+\mathbb E\widehat f(t-H),\qquad
 G(t)=\mathbb E\sum_{n<\tau}\widehat D(t-S_n).
$$
Stopping first at $\tau\wedge N$ and using boundedness and finite mean justifies the identity. The forcing $G$ is directly Riemann integrable by the translated upper-sum bound and finite pre-ladder mass, with $\int G=(\mathbb E\tau)\int D$. The positive ladder height is nonarithmetic: its support contains $\log(3/2)$ from the one-letter step and $\log(9/8)$ from letters $2,1$, whose ratio is irrational by unique factorization. Wald's identity gives $\mathbb EH=\mu\mathbb E\tau$. Iterating at independent ladder heights yields the renewal convolution with $G$, since $\widehat f$ is bounded and tends to zero at negative infinity. The key renewal theorem therefore yields
$$
 \lim_{t\to\infty}\widehat f(t)=\frac{\int G}{\mathbb E H}
      =\frac1\mu\int_{\mathbb R}D(t)dt=:c_*.
$$
Here the positive-increment theorem is the standard nonarithmetic key renewal theorem for directly Riemann integrable forcing. [Feller, *An Introduction to Probability Theory and Its Applications*, vol. II, chapter XI](https://doi.org/10.1002/9780470316590)

The established two-sided bounds keep this limit positive and at most one. Now $x\widehat f(\log x)=\int_0^x v^2\Pr(M>v)dv\sim c_*x$. Subtract at $x$ and $\lambda x$, or at $x/\lambda$ and $x$, then use monotonicity of the tail. The resulting lower and upper bounds on $x^2\Pr(M>x)$ tend to $c_*$ as $\lambda\downarrow1$. The same limit holds for $\Pr(M\ge x)$ by squeezing between strict tails at nearby thresholds. FS-010 identifies this last probability with $d(1/x)$ for $x>1$.

For a branch interpretation of the constant, let $B_a=(3/2^a)M((2^a\alpha-1)/3)$ on legal first letters and zero otherwise, and $B=\sup_a B_a$. Then
$$
 2\mu c_* = \mathbb E(1-B^2)_+
       -\mathbb E\left[\sum_a B_a^2-B^2\right].
$$
Indeed for a threshold $v$ the tail defect before multiplication by $v^2$ equals $\Pr(B\le v<1)-\mathbb E(\#\{a:B_a>v\}-1)_+$. Integrate against $2v\,dv$. The first term is integrable and the signed defect was just proved integrable, so Tonelli gives finite overlap cost for the second. This formula retains the actual common-target dependence among branches.

## Asymptotic constants for all supercritical pressures

For each $s>2$ there is $c_s\in(0,\infty)$ such that
$$
 \Pr(\mathcal H_s>u)\sim c_s u^{-2/s}.
$$
Set $p=2/s<1$, $H=\mathcal H_s$, $B_a=(3/2^a)^s H((2^a\alpha-1)/3)$ on legal branches and zero otherwise, and $B=\max_a B_a$ (zero if none are legal). Almost surely $H=1+\sum B_a<\infty$. Put $f_s(t)=e^{pt}\Pr(H>e^t)$, bounded on the line and bounded away from zero near positive infinity by the [supercritical pressure bounds](MINIMUM_SHARP.md). Define $D_s=f_s-\mathbb E f_s(\cdot-sY)$ with the same tilted letter law. This defect before multiplication by $e^{pt}$ is $\Pr(H>e^t)-\sum_a\Pr(B_a>e^t)$, since the power-$p$ tilt of each branch times legality is again $3\cdot4^{-a}$.

Integrate the defect through $t=\log T$ and multiply by $p$. The result is
$$
 I(T)=\mathbb E[\min(H,T)^p-\min(B,T)^p]
      -\mathbb E\left[\sum_a\min(B_a,T)^p-\min(B,T)^p\right].
$$
Both expectations are finite for fixed $T$, since negative-tail integrability follows as for $D$ and the clipped sum is the integral of its nonnegative marginal tails. Also $|I(T)|\le p\|f_s\|_\infty\mathbb E|sY|$ by shifting the integral from $-\infty$. Denote the nonnegative random variable in the second expectation by $V_T$.

For $x\ge b\ge0$, $ (x+b)^p-x^p\le(2^p-1)b^p$ by concavity. Keep the largest summand and apply this inequality to every subsequent summand. The added constant 1 contributes at most 1 to the $p$-power. For $B<T$ this yields
$$
 \min(H,T)^p-\min(B,T)^p\le1+(2^p-1)V_T;
$$
for $B\ge T$ the left side vanishes. Hence $I(T)\le1-(2-2^p)\mathbb EV_T$. The strict inequality $2^p-1<1$ and the uniform lower bound for $I(T)$ show that $\mathbb E[\sum_a B_a^p-B^p]<\infty$ by monotone convergence (remove a maximizer before taking the increasing clipped sum). The same estimate gives $\mathbb E[H^p-B^p]<\infty$. Splitting the tail defect about $\Pr(B>e^t)$ expresses it as the difference of two integrable nonnegative functions. Thus $D_s\in L^1$.

The preceding smoothed ladder argument applies with increments $sY$, of mean $s\mu$ and nonarithmetic ladder heights. Unsmoothing now uses $\int_0^x v^p\Pr(H>v)dv$ and the same monotone squeeze. The positive constant satisfies the finite difference formula
$$
 2\mu c_s=\mathbb E[H^p-B^p]
       -\mathbb E\left[\sum_a B_a^p-B^p\right].
$$
The strict concavity used to bound the overlap stops at $s=2$. The critical pressure still has the two-sided $1/u$ tail in the preceding packet, without a limiting constant established here.
