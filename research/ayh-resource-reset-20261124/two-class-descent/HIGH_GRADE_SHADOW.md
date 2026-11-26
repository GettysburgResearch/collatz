# The real offset of a surviving high-grade head pair

Let $T$ be the ordinary positive shortcut map. On a binary cylinder write the two affine profiles, in increasing order of their powers of three, as $X$ and $Y=3^s X+D$. A tie may use either order. The signed real offset used here is

$$W=-D/3^s=X-Y/3^s.$$

On ordinary inputs, $W\bmod1$ is exactly $-Y/3^s\bmod1$. Consequently a small interval for the fractional offset restricts the most significant trits of the length-$s$ residue of the larger-slope endpoint. The endpoint with larger slope need not have larger ordinary value. Write $\|z\|=\min_{k\in\mathbb Z}|z-k|$.

## A finite bound uniform in the entering pair

At a current positive grade, let $b,e\in\{0,1\}$ be the parities of $X,Y$ respectively. If the orientation is maintained and $s'=s+e-b$, direct substitution yields

$$W'=A_b(W)-e/(2\cdot3^{s'}),\qquad A_b(u)=(3^b u+b)/2. \tag{1}$$

If $s_0\ge2L$, all length-$L$ continuations keep the same orientation and $s_i\ge L$. For their base parity word $w$ and its chronological product $F_w$, this gives

$$|W_L-F_w(W_0)|\le 3^{-L}((3/2)^L-1)<2^{-L}.\tag{2}$$

Under the complete binary residue grid each lower parity word has probability $2^{-L}$. Indeed the coefficient of the still unexposed input quotient is odd. This remains true after specifying the entire earlier cylinder; the upper bits can depend arbitrarily on the lower word.

Set $p=|w|_1$ and $C(w)=\sum_{i:w_i=1}2^i3^{\#\{j>i:w_j=1\}}$. Then $F_w(a)=(3^p a+C(w))/2^L$. For fixed $p$, all the $C(w)$ are distinct modulo $2^L$. At the earliest differing index $i$, all earlier contributions agree because the total count and preceding bits agree. At $i$ the difference is $2^i$ times an odd number, and all later contributions are divisible by $2^{i+1}$. Thus at fixed $p$ the values $F_w(a)\bmod1$ form a subset of one translate of the mesh $2^{-L}\mathbb Z/\mathbb Z$. For every circle arc $I$ of length $\ell$ this proves

$$\Pr(W_L\bmod1\in I\mid\text{earlier cylinder})\le (L+1)(\ell+3\cdot 2^{-L}).\tag{3}$$

The bound is simultaneous for deterministic fixed-$p$ choices of the arc with common length. An arc depending on the upper odd count as well can be bounded by additionally summing over its $L+1$ possible values. An analogous real estimate holds for the ideal scalar process $F_w(0)$ at any entering grade, with $3$ in (3) replaced by $1$. The dyadic separation and exact pair arithmetic are verified in `HighGradeShadow.lean`.

For clarity on antecedents, Section 3 of [Geometry, integer fibres, and dyadic equidistribution of the joint Collatz affine law](https://rstation.ai/problems/collatz/papers/19) uses the same-count geometry of the pure scalar affine words. Its Section 10 studies the stationary real/ternary law. Here the translated finite mesh is used in the **perturbed, killed, oriented pair** and in the source-stopped estimates below. The scalar separation itself is elementary and no priority claim about it is needed.

## Native head rows

Set $R=81^j$, $d=\log_2R$, $7R\le x=81m+r<8R$, $0\le r<81$, and $h=\lfloor\log_2(R/81)\rfloor$. Write $s_t=|4+p_x(t)-p_m(t)|$, where the odd counts precede clock $t$. Let $\tau$ be symbolic pair absorption. For $1\le L\le h/2$, any $0\le\epsilon\le1/2$, and any circle center $\theta$, the normalized fraction of the row satisfying

$$\tau>h,\quad s_h\ge3L,\quad \|W_h-\theta\|\le\epsilon$$

is at most $C h^{-1/2}(L+1)(2\epsilon+3\,2^{-L})$. Indeed $s_{h-L}\ge2L$ on this event. Condition on that cylinder and apply (3); the probability of surviving to $h-L$ is $O(h^{-1/2})$ uniformly over the 81 initial states by the frozen pair theorem used in [KILLED_GRADE_OCCUPATION.md](../joint-renewal/KILLED_GRADE_OCCUPATION.md). Each actual fixed-suffix parent interval of length $R/81$ is covered by at most two full $2^h$ grids. This yields the claimed actual-source estimate. The center may even be chosen measurably from the earlier cylinder, separately at each $p$, in this native estimate.

For example take $\epsilon=h^{-B}$, $B>1/2$, and $L=\lceil B\log_2 h\rceil$. The normalized fractions form a convergent series over $j$. Together with the published summable low-grade bound for $s_h<3L$, this shows that the complete surviving head-pair mass within $h^{-B}$ of **any integer** is summable. The conclusion concerns the whole lattice in a single test and uses no cutoff on $|W|$.

## Every physical clock through the first of two polylogarithmic entrances

**Theorem.** Fix $A>0$, a buffer constant $G\ge0$, and a bound $J\ge0$. There are $B,D,C>0$ and $R_0$ such that the following holds for all head rows with $R\ge R_0$. For any deterministic set $\Theta_R$ of at most $d^J$ circle centers, at most $O_{A,G,J}(Rd^{-A})$ original children have some physical clock

$$0\le t\le\min(\tau_M(x),\tau_M(m))+G\log_2d,\quad s_t\ge C\log_2d,
\quad \min_{\theta\in\Theta_R}\|W_t-\theta\|\le d^{-B},\qquad M=d^D.\tag{4}$$

Here $\tau_M(z)$ is first entrance below $M$. Failure of timely entrance on either arm costs a further $O(Rd^{-A})$ from the same construction. In particular the counter uses no conditional probability statement about fresh bits of the pair at a stopped height. The two original arms individually have passage clocks $(d-\log_2 M)/\log_2(2/\sqrt3)+O_A(\sqrt{d\log d})$ outside an additional exception of the same size, by [LANDING_WEIGHT_TRANSFER.md](../joint-renewal/LANDING_WEIGHT_TRANSFER.md). The controlled clocks therefore extend well beyond $\log_2R$.

**Uniform deterministic contraction across changes of orientation.** Set $g_i(t)=a_i+p_i(t)$ for original arm $i$, with initial grades $4,0$, and $g(t)=\min_i g_i(t)$. For every step,

$$|W_{t+1}|\le 3^{g(t+1)-g(t)}|W_t|/2+1.\tag{5}$$

At a strict grade this follows from (1), including the step to a tie if the old order is retained there; changing order at a tie only changes the sign of $W$. At grade zero, if the two parities agree their common multiplier is $3^b/2$. If they differ the canonical lower at the next step is the even arm, the new grade is one and $W_{t+1}=\pm W_t/2-1/6$. This also verifies (5) from a tie. The products of the multipliers in (5) telescope to $3^{g(v)-g(u)}/2^{v-u}$. In particular if both original arms have at most $21b/40$ odd inputs on each controlled length-$b$ window, then each such product is at most $\lambda^b$, $\lambda=3^{21/40}/2<1$. Use the arm realizing $g(u)$ at the initial end to bound $g(v)-g(u)$. A partial product of length $r<b$ is at most $(3/2)^r$. Unrolling (5) and grouping backwards into length-$b$ blocks gives

$$|W_t|\le C(1+|W_0|)(3/2)^b,\tag{6}$$

because $\sum_{r=0}^{b-1}(3/2)^r\le2(3/2)^b$ and $\sum_{k\ge0}\lambda^{kb}\le(1-\lambda)^{-1}$. This controls all clocks in (4) on the scalar sliding-test complement.

**Scalar rare-word test.** Choose $B>A+J+8$. Keep the length $b=\lceil K\log_2d\rceil$ Hoeffding tests in [FIRST_PASSAGE_MARKS.md](../literature-step/FIRST_PASSAGE_MARKS.md), increasing the fixed passage exponent $D$ below. Equation (6) is $O(d^{K\log_2(3/2)})$. Let $L=n b$ for a fixed integer $n$ sufficiently large that $\lambda^L(1+(3/2)^b)\ll d^{-B-1}$ and $2^{-L}\ll d^{-B-1}$. Enlarge $D$ to accommodate $L$ and $G\log_2d$ in each stop grid. Choose $C$ so that $s_t\ge C\log_2d$ implies $s_t\ge3L$ and $t\ge L$ for large $d$, using $s_0=4$ and $|s_{i+1}-s_i|\le1$. The orientation is fixed during the last $L$ steps before such $t$. The word $w$ of the lower arm on this window obeys $3^{|w|_1}/2^L\le\lambda^L$ by $n$ successive scalar tests. Equations (2) and (6) now give

$$|W_t-F_w(0)|\le2^{-L}+\lambda^L|W_{t-L}|<d^{-B}.\tag{7}$$

Thus (4) entails a rare **scalar** word on one of the two original arms. Under a fair length-$L$ word the probability that $F_w(0)$ is within $2d^{-B}$ of any center in $\Theta_R$ is at most $d^J(L+1)(4d^{-B}+2^{-L})$ by the finite mesh. All constants are fixed before the row is sampled.

**Transfer of every scalar window from original sources.** In the decreasing schedule of FIRST_PASSAGE_MARKS, each threshold $Y_i>M$ has horizon $k_i=\lfloor(\log_2Y_i)/2\rfloor$. Its next actual threshold is reached within $k_i$ clocks outside the published exceptions. In addition to its old prefix-growth test, inspect every length-$L$ rare word and every length-$b$ Hoeffding test beginning at offsets $0$ through $k_i+\lceil G\log_2d\rceil$. The entire inspected prefix fits in $\log_2Y_i$ once $D>2((n+1)(K+1)+G+3)$, enlarged further as required by the original passage proof. The bad fair-grid fraction from the added rare words is $O(d^{1+J}(L+1)(d^{-B}+2^{-L}))$ at each stage. The added scalar growth-test error is $O(d e^{-b/800})$; choose $K$ for this exponent first. The initial stage uses complete-period covering. At each later stage the original-source entrance fiber bound (3) of FIRST_PASSAGE_MARKS costs at most $O(d^3)$ times the grid fraction; there are $O(\log d)$ stages. The choices above give $O(Rd^{-A})$ in total. The inspected starting intervals cover all scalar times from zero through each arm's first $M$-passage plus the stated buffer. Apply the estimate to the child and parent separately, charging the parent's multiplicity of 81. This proves (4) and allows arbitrary subsequent source restrictions by intersection.

## The ordinary eventual shadow and its timing

Suppose exactly one of the two ordinary starts reaches one. The other orbit stays above $600$ using the fixed finite verified range. Write $z_t$ for that other arm and $u_t$ for the converging arm. After a finite initial part $u_t\in\{1,2\}$ alternates, so $p_u(t)=t/2+O_{x,m}(1)$. Every odd factor in the exact multiplicative formula for $z_t$ is at most $1+1/1800$ beyond its linear multiplier. With $g_z,g_u$ the corrected grades, whether or not they have crossed yet,

$$0<z_t\,3^{-(g_z(t)-g_u(t))}\le C_{x,m}\left[(\sqrt3/2)(1+1/1800)\right]^t.\tag{8}$$

Since $z_t\ge1$, (8) forces $g_z(t)-g_u(t)\gg t$ eventually. Thus the nonconverging arm is eventually the larger-slope arm, and $W_t$ approaches the actual smaller-slope state $u_t\in\{1,2\}$ exponentially. This argument covers a nontrivial cycle and an unbounded orbit alike.

The prefix theorem and (8) concern genuinely different clock ranges. At the first arrival to $M$, on (6) with $D$ chosen larger than its power and a mesoscopic grade, the smaller-slope arm must be the one arriving: otherwise the larger-slope value is below $M$ and the other value is at least $M$, in contradiction to $Y/3^s=X-W$ and $|W|=o(M)$. The first landing lies in $[M/2,M)$, hence $U=Y/3^s\asymp M$ there. While orientation remains fixed, (1) in physical coordinates gives $U'\ge U/2$. Achieving the specific smallness $U\le d^{-B}$ therefore needs at least $(D+B)\log_2d-O(1)$ further clocks. A fresh full grid at an $M$-landing provides only $D\log_2d+O(1)$ input bits. More directly the two-step affine map along a lower arm already alternating through one has multiplier $3/4$. It drives different entering real offsets toward the same periodic phases, so a restart with new fair lower bits after reaching one would change the law. The post-descent bound of [PR 193](https://github.com/GettysburgResearch/collatz/blob/ebeec2cda24b1deafff17cb2a9ce6e1bed7d9784/research/astra-closure-20261124/transfer/RETURNS.md) controls rebound of each physical arm until a smaller barrier. Its stated estimates do not supply the needed joint lower-word law after the first arm passes its last controlled floor. A bound on the weighted mass entering the eventual shadow in this later regime remains open.
