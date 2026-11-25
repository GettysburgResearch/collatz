# A lower bound for a shared-source trit-query grid

**PROPOSED written theorem with two kernel-checked finite ingredients.** On the bounded seed menu specified below, the fraction of grid points passing PR197's many-clock test is at least $\lambda/4>0$ on every sufficiently large row. All clocks use the same bit string, the same initial seed pair and the same ordinary four-trit bisection program.

PR197 allows choices of seed and query admissibility in its one-sided transfer. Our lower bound applies when that finite menu contains the specified exponent/correction pair. Requiring a witnessing original parent for that pair in each native residue and coarse prefix imposes an additional restriction. Its population is unknown. The result leaves the original physical-parent statistic and ordinary convergence open.

## Finite obstruction inside the query menu

Use the positive shortcut map $T(2n)=n$, $T(2n+1)=3n+2$, and let $p_h(x)$ count odd departures through clock $h$. On one aligned window of $M=2^r$ consecutive indices $q$, the upper arm has value $Y(q)=3^Gq+c$. Write $x_e(q)=\lfloor Y(q)/3^{G-e}\rfloor$. A physical four-trit chain increments $e$ by four. Its columns satisfy
\[
 x_e(q)=3^eq+c_e,\qquad x_{e+4}(q)=81x_e(q)+u_e,\qquad 0\le u_e<81 .
\]
The suffix $u_e$ is constant on the window. Give each row the weighted label
\[
 F_e(q)=(T^h x_e(q),\,e+p_h(x_e(q))).
\]
Within each column this induces exactly PR197's $L_h$ partition.

**A binary cylinder for each suffix.** For every $0\le u<81$ the table in [TritChain.lean](TritChain.lean) supplies $a_u<2^{14}$ such that for every $x\equiv a_u\bmod 2^{14}$ and $h\ge14$,
\[
 T^h x=T^h(81x+u),\qquad p_h(x)=4+p_h(81x+u).
\]
Lean verifies all 81 entries by ordinary reduction at clock 14. The same module proves both identities on every lift and continues them to any common deadline $h\ge14$. For example, $a_{65}=15$. At clock four the two orbits from 15 and 1280 meet at 80, with odd counts four and zero. Since $3^e$ is odd, exactly $M/2^{14}$ rows of each aligned window with $r\ge14$ realize the certified residue for its edge. Thus **every adjacent pair of columns agrees on at least $M/2^{14}$ paired weighted labels.**

**Forced column variation.** Suppose $2D\le M/2^{14}$ and the two endpoint labels differ on at least $2D$ paired rows. Some column has deficiency at least $D$. Otherwise choose in each column a label omitting fewer than $D$ rows. For adjacent columns, fewer than $2D$ rows miss one of their chosen labels. At least one agreeing row therefore lies in both chosen classes, so their labels coincide. All chosen labels coincide along the chain. This would leave fewer than $2D$ unequal endpoint labels. The theorem `forcedColumn` checks this argument in Lean for an arbitrary finite set of rows and an arbitrary number of columns.

Individual grid partitions can be evaluated using a single common translated block, since translating the index by $2^h$ preserves each partition. Every column of an eligible chain occurs in some formal run of PR197's four-trit search. Give earlier chains equal endpoint replies, give this chain opposite replies, then retain the half containing the desired index until that column is queried. Endpoints are queried directly. This uses the existing union over formal reply paths. Enforcing feasibility under a single actual invariant coloring would shrink that union.

## One seed pair on the entire slab

Use PR197's $d=\log_2(81^j)$, $W=\lceil\sqrt{d\log d}\rceil$, $h=\lfloor d/3\rfloor$, $\Delta_t=t-t_0$, $k_0=\lfloor t_0/2\rfloor$ and $m=\lfloor3^{k_0}2^{-t_0}n\rfloor$. Start the slab of $W$ clocks at $\tau$, with $\Delta_\tau=\lceil KW\rceil$ for a sufficiently large fixed $K$. The grid precision is $H=\max_t\Delta_t+h$. Fix $0<\kappa\le1/8$ inside the grade envelope. Let $g_*=\lfloor\Delta_\tau/2\rfloor$ and choose the two opening exponent/correction pairs
\[
       (g_+,b_+)=(g_*+\lfloor\kappa W\rfloor,1),\qquad
       (g_-,b_-)=(g_*-\lfloor\kappa W\rfloor,1).
\]
Their opening ordinates are exactly $\lfloor3^{g_\pm}m/2^{\Delta_\tau}\rfloor+1$. Apply the shortcut step to each ordinate, using PR197's one-bit coefficient update at every clock. Choose public exponent bounds containing $|k-t/2|\le3\kappa W+3$ and the original good parameters. Choose public coarse-floor correction bounds at least the constant below and large enough to include the original good parameters. These are one-sided arithmetic bounds. Taking $K$ sufficiently large gives $g\ge4$ and $3^g2^{-\Delta_t}\le1$ on the prescribed exponents.

Fix a nonempty mantissa interval $\mathcal J=(a,b)\subset(7,8)$, or take $(7,8)$ itself. Write $\lambda=\log_3(b/a)$. Use zero ternary advice, any fixed threshold exponent $J'>0$, and $D=\lceil d^{J'}\rceil$. Choose the allowed logarithmic microblock constant so that at every tested clock $r\ge14$ and $2D\le2^{r-14}$ eventually. For any $0<c\le\lambda/8$ the following holds. At each native residue where the bounded-parameter menu admits the displayed opening pair throughout the coarse prefixes, at least $\lambda/4$ of uniform grid points pass the test of $cW$ clocks with a formal query of deficiency at least $D$, for all sufficiently large $d$. Use a smaller $c$ if required by the true-population transfer. The unrestricted bounded menu therefore has $P_d(h)\ge\lambda/4$. For a menu allowing this fixed pair on a fraction $\alpha_d$ of native residues throughout their coarse prefixes, the lower bound is $\alpha_d\lambda/4$.

### Proof

1. **Grade gap on one common string.** Conditional on the opening low bits, each arm separately has an odd coefficient in the unrevealed quotient. Its next $l$ parity decisions are uniform binary digits. Indeed each next parity fixes one new bit because the updated coefficient of the remaining quotient is odd. Its odd count has law $\operatorname{Bin}(l,1/2)$. The exponential moment of $p_l-l/2$ is $\cosh(z/2)^l\le\exp(lz^2/8)$. Exponential Markov and a union bound over both arms and $0\le l<W$ show that the counts differ from $l/2$ by at most $\kappa W/4$, except on $O(W e^{-c_\kappa W})$ of strings. The designated upper arm stays upper, the grade gap $s_t$ exceeds $\kappa W$ and both exponents satisfy the bounds throughout. The two arms may use fully dependent bits.

2. **Coarse-floor corrections.** For the designated upper arm let $E_t=Y_t-3^{g(t)}m/2^{\Delta_t}$. Its opening value lies in $(0,1]$. At parity $\epsilon$, one has $E_{t+1}=(3^\epsilon E_t+\epsilon)/2$. The previous bits determine $E_t$ since its dependence on the remaining quotient cancels. With $\rho=(1+\sqrt3)/(2\sqrt2)<1$ this gives $\mathbb E(\sqrt{E_{t+1}}\mid\text{past})\le\rho\sqrt{E_t}+1$. Consequently $\mathbb E\sqrt{E_t}\le B=1+(1-\rho)^{-1}$. At each prescribed clock,
   \[
     \Pr\big(E_t>(16B)^2\big)\le1/16 .
   \]
   On its complement every truncation has coarse-floor correction between zero and $\lceil(16B)^2\rceil+1$. Divide by its power of three and take floors to see this. Use this constant or a larger one in the formal public coarse-floor menu. Further conditions involving the unknown original parent are outside this enlargement.

3. **An explicit positive fraction of eligible clocks.** Choose $a<a'<b'<b$ with $\log_3(b'/a')>3\lambda/4$. Let $m_*$ be the first coarse integer in the row. In the first-period grid representatives and their exterior cells, $m/m_*=1+o(1)$ uniformly. Indeed $m_*\asymp c_0N$, and the displacement is $O(2^H+2^{O(W)})=o(c_0N)$ by the exponential margin in PR197's GRID_TRANSFER. Consider the clocks satisfying
   \[
      \log_3 m_*-\Delta_t\log_3 2 \pmod 1
           \ \in\ \log_3(a',b')\pmod 1 .
   \]
   The upper exponent adds an integer to this logarithm. One $i\in\{0,1,2,3\}$ puts the top truncation $\lfloor Y_t/3^i\rfloor$ inside $81^z\mathcal J$ for an integer $z$. The fixed interior margin absorbs the exterior-cell variation and all floor errors, including the bottom endpoint because all its ordinates are $2^{\Omega(d)}$. Further divisions by 81 preserve this check at every child. The same $i$ works throughout the exterior when the current low bits and exponent are fixed.

   At least $\lambda W/2$ clocks satisfy the phase condition, uniformly in the initial phase for large $W$. In detail, $\log_3 2$ is irrational by prime factorization. Pigeonhole its multiples to choose $j\ge1$ with $0<\theta=\|j\log_3 2\|<\lambda/32$, where $\|\cdot\|$ denotes distance to the nearest integer. In each clock progression modulo $j$, a block of $N_0=\lfloor1/\theta\rfloor$ points runs around the circle in steps $\pm\theta$ and its closing gap is smaller than $2\theta$. An arc of length $l>3\lambda/4$ contains at least $l/\theta-3$ points, giving fraction at least $l-3\theta>21\lambda/32$. In the $j$ progressions fewer than $jN_0$ clocks lie outside complete blocks. Discarding the original tiling's optional final incomplete microblock loses a further $O(\log d)=o(W)$ clocks. The strict phase margin still gives the asserted lower frequency for sufficiently large $W$.

4. **A deficient column at an eligible clock.** Condition only on the exposed low bits through $\Delta_t$, requiring the grade bounds and correction bound at this clock. At a phase clock from the previous step, the selected chain and endpoint exponents are fixed from these data and $m_*$. Their exponent difference is at least $s_t-6\ge\kappa W-6$. Each endpoint has $p_h(x_e(q))\sim\operatorname{Bin}(h,1/2)$ because $x_e$ is odd-affine in $q$, and its next $h$ bits are uniform. If the weighted labels agree, one of the two counts differs from $h/2$ by at least $(\kappa W-6)/2$. Chebyshev and a union bound give equality probability $O(h/(\kappa W-6)^2)=o(1)$. No conditional independence of the endpoints is used. Equally, the expected *fraction* of equal endpoint rows in the aligned block containing $q$ is $o(1)$, because resampling a uniform row in a uniformly sampled block preserves uniformity. By Markov, except in $o(1)$ of blocks, at least $M/2$ endpoint labels differ. The cylinder and forced-column theorems now give the prescribed deficiency in some query of this chain.

5. **Many clocks for one grid point.** At each of at least $\lambda W/2$ deterministic phase clocks, the success probability exceeds $3/4$ for sufficiently large $d$. Let $N_b$ count marks on the one shared string $b$. Linearity gives $\mathbb E(N_b/W)\ge3\lambda/8$. Since $0\le N_b/W\le1$, $\Pr(N_b/W\ge c)\ge\mathbb E(N_b/W)-c\ge\lambda/4$. Rounding the required integer count up implements exactly this event.

The proof uses the same seed pair even across different microblocks. It gives an obstruction in a polynomial menu of *concrete* trit formulas, without arbitrary query intercepts or replacement of the shared bits by independent bits. It does not construct an original parent whose two arms realize these seeds at $\tau\sim3d$. An estimate exploiting joint seed reachability with the actual native residue and low prefix, or actual reply feasibility, must retain the lower incidence of the original selected population after imposing those restrictions.

## Diffusive separation and an opening-cell restriction

The lower bound extends to gaps of order $\sqrt h$ and to a seed chosen from the physically allowed menu at an opening. Define an opening cell by the native residue $v$ and $\ell_\tau=m\bmod2^{\Delta_\tau}$. Suppose a fraction $\beta_d$ of these cells, with their uniform product weights, have some admissible pair with opening grade gap at least $A\sqrt h$, for fixed $A>0$. The selected seed and both corrections may vary with the opening cell. Assume the following concrete checks.

- The opening corrections are nonnegative and at most $d^C$ for a fixed $C$. Subsequent public correction bounds are as in the previous theorem.
- At time $\tau+l$, $0\le l<W$, the public exponent bounds admit both opening exponents plus $l/2$ with any rounding deviation at most $A\sqrt h/8$. The retained exponents satisfy the positivity and slope bounds of the rebase. This is an interior condition on the opening exponents.
- The fixed opening seed remains available on the full subsequent binary cube, subject to the same coarse-floor, mantissa and formal-query checks as above. A fresh test that the *whole* later grid point comes from an original parent is stronger.
- The omission threshold satisfies $D/M=o(1)$ uniformly over the slab. This uses an allowed increase of the microblock constant.

Put $\pi=A^2/(A^2+9)$. For $0<c\le\lambda\pi/12$ the grid event has probability at least $\beta_d\lambda\pi/12$ for every sufficiently large row. In particular an $o(d^{-3})$ upper bound on such an opening-filtered grid requires $\beta_d=o(d^{-3})$. This statement applies whether the opening witnesses were obtained from formal parameter bounds or from actual joint seed realizability, provided the subsequent full-cube test is the one specified. The result gives no unconditional lower bound on $\beta_d$ for the physical opening witnesses.

To prove it, freeze one admissible choice in each qualifying opening cell. The maximum binomial estimate in step 1 bounds the probability of a deviation $A\sqrt h/8$ by $O(W\exp(-c_A h/W))=o(1)$, uniformly in that cell. Thus at eligible clocks the endpoint exponents differ by at least $A\sqrt h/3$, including rounding the ends to the four-trit chain. The opening upper correction error may now lie in $(-1,d^C]$. Its absolute square-root obeys the same contraction as before. After $O_C(\log d)$ clocks its expectation is bounded by $B$. Also $E_t\ge-1$ always. A parity triple $0,0,1$ makes it positive, since the two halvings leave it at least $-1/4$. A nonnegative error then stays nonnegative. The probability that this triple is absent from the first $l$ parities is at most $(7/8)^{\lfloor l/3\rfloor}$ by testing disjoint triples in this single arm. Consequently, outside the logarithmic burn-in, the grade and coarse-floor checks pass at a given phase clock with probability at least $3/4$ for all large $d$.

There is a direct joint second-moment estimate for two columns. Conditional on their low prefix, order their exponents so their difference is $s>0$. Over the next $j$ decisions let $Z_j=s+p_j(x_{\rm high})-p_j(x_{\rm low})$. At each step both next parities are fair conditional on the same past bits, by oddness of both affine slopes. Their difference is either identically zero or takes the two values $+1,-1$ with equal probabilities. Thus $\mathbb E Z_h=s$ and $\mathbb E Z_h^2\le s^2+h$. By Cauchy–Schwarz,
\[
          \Pr(Z_h\ne0)\ \ge\ \frac{s^2}{s^2+h}.
\]
The proof uses neither separate future strings nor a real approximation to either ordinate. For the chain endpoints this gives weighted-label mismatch with probability at least $\pi$. Resampling one uniform row within the sampled aligned block preserves this lower bound for its expected mismatch fraction. On a block with no deficient column the fraction is below $2D/M$ by `forcedColumn`. Therefore the conditional probability of some deficient column is at least $\pi-2D/M$. After the burn-in there are at least $\lambda W/3$ phase clocks. Their per-clock success probability is at least $\pi/2$ for large $d$. The same bounded first moment used in step 5 finishes the claimed lower bound, first on that entire opening cell and then on their uniform union.

## The standard native-survival filter

A grid enlargement can retain a genuine necessary native condition and still fail the proposed upper rate. Set $a_0=\lfloor d/2\rfloor$. For each original suffix $u\in\{0,\ldots,80\}$, keep only native residues $n\bmod2^{a_0}$ on which the pair $(n,81n+u)$ has escaped symbolic absorption through the native clock. Suppose the bounded opening menu after this filter admits the explicit large-gap seed pair above. Then
\[
             P_d(h)\ \ge\ \frac{\lambda}{4}\frac{16}{16+a_0}\ \gg d^{-1}.
\]
Indeed apply the same signed-grade martingale directly to the native pair, starting at grade difference four. With $Z_j=4+p_j(81n+u)-p_j(n)$, the two current states are odd-affine in the same remaining quotient, so $\mathbb E Z_{a_0}=4$ and $\mathbb E Z_{a_0}^2\le16+a_0$. Cauchy–Schwarz gives the displayed fraction $16/(16+a_0)$ of all residues with $Z_{a_0}\ne0$. Symbolic absorption earlier would imply matching absolute grades at all later common clocks. Each of these residues therefore passes this genuine native filter.

At the directed suffix $u=57$ one may also require $n\equiv7\bmod8$. The first three native steps from 7 have three odd departures; those from $81\cdot7+57=624$ have zero. This holds on the full class. Conditioning on its three bits leaves starting grade difference one and a fresh native quotient. For $a_0\ge3$ the resulting fraction of all native residues with nonzero terminal grade difference is at least $1/(8(1+a_0-3))$. This gives the same order of obstruction on that directed class when no other eligibility filters are added. Both conclusions use symbolic native absorption and a bounded *late* menu. Neither supplies actual late physical seeds from those residues.

**Frozen sources.** PR197 head `156652e03fe7a78f9cd4442039779cc622fdf3de`, `research/ayh-resource-reset-20261124/source-progress/GRID_TRANSFER.md`, together with `closing-proposal/LOCAL_RESAMPLING.md`, `directed-return/SELECTED_TRIT_CELLS.md` and `unit-exit/LOCAL_COLOR_INFORMATION.md` at the same head. The finite cylinder proof is independent of the source's quantitative merger estimate.
