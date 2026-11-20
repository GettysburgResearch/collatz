# Every fixed endpoint has finite all-time weighted mass

**Status: PROPOSED, complete elementary proof.** This result is unconditional and handles hypothetical nontrivial cycles explicitly. It does not prove a uniform bound for the total arithmetic moment or resolve Collatz.

Use the accelerated odd map

$$U(n)=\frac{3n+1}{2^{v_2(3n+1)}}$$

on positive odd integers. Write

$$J_q(n)=\frac{3^q}{2^{A_q(n)}},\qquad J_0(n)=1,$$

where $A_q(n)$ is the sum of the actual division valuations in the first $q$ odd steps. For a fixed positive odd target $t$, define the nonnegative endpoint mass

$$M_q(t)=\sum_{\substack{n>0\text{ odd}\\U^q(n)=t}}
           \frac{J_q(n)^4}{t^2}.$$

The sum concerns all ordinary sources, not only a finite corpus or one inverse word. Let

$$C_4=\sum_{n>0\text{ odd}}n^{-4}<2.$$

No external occupancy or density theorem is required below.

## ES1. All-time endpoint bound

For every fixed positive odd $t$,

$$\boxed{\sum_{q\ge0}M_q(t)
 \le\frac{C_4t^2}{1-(3t/(3t+1))^4}
 <2t^2(3t+1).}\tag{1}$$

### Proof

Fix one positive odd source $n$. If it never reaches $t$, its contribution is zero. Otherwise let $h$ be its first hitting time. Exact multiplication of the ordinary odd steps gives

$$t=nJ_h(n)\prod_{j<h}\left(1+\frac1{3U^j(n)}\right).$$

The product is at least one, so the first-hit contribution obeys

$$\frac{J_h(n)^4}{t^2}\le\frac{t^2}{n^4}.\tag{2}$$

There are two possibilities.

* If $t$ is not periodic under $U$, the source can visit $t$ only once.
* If $t$ is periodic with least period $\ell\ge1$, its visits occur at exactly $h,h+\ell,h+2\ell,\ldots$. Let $c=J_\ell(t)$. Multiplying around that actual cycle gives

  $$1=c\prod_{j<\ell}\left(1+\frac1{3U^j(t)}\right),$$

  whence

  $$0<c\le\frac{3t}{3t+1}<1.$$

  The factor with $j=0$ already gives this inequality. By composition of the exact Jacobians, $J_{h+k\ell}(n)=J_h(n)c^k$.

Thus in either case the whole contribution of this fixed original source is at most

$$\frac{t^2}{n^4}\sum_{k\ge0}\left(\frac{3t}{3t+1}\right)^{4k}
 =\frac{t^2/n^4}{1-(3t/(3t+1))^4}.$$

Sum this nonnegative inequality over all odd $n$ and use Tonelli. This proves the first inequality in (1), without assuming in advance that the all-time sum converges. Finally, for $0<a<1$, $1-a^4\ge1-a$; hence the reciprocal denominator in (1) is at most $3t+1$. Together with $C_4<2$, this proves the stated rational upper bound. QED.

The proof includes the trivial fixed point $t=1$ and any hypothetical nontrivial positive cycle. It does not count cycle visits as distinct states or assume a reciprocal budget along a repeated cycle.

## ES2. The bounded-endpoint part of the primitive moment is summable

Use the word parameters $J_w,r_w,b_w$ and $P_q$ from `MOMENT_QUANTILES.md`, Section 2. This notation and its primitive-word decomposition are also frozen in PR165 at `78bdb31ccba608de3d089b751a0ab59a52007408`, `research/certificate-transfer-intake-20261120/questions/02_weighted_representatives.txt` and `reports/2026-11-20-certificate-transfer-intake/initial-review-and-problem-key.txt`.

For an integer $R\ge1$ put

$$P_q^{\le R}=\sum_{\substack{w\in\mathbb N_{>0}^q\\r_w\le R}}
               \frac{J_w^4}{r_w^2}.$$

Then

$$\boxed{\sum_{q\ge1}P_q^{\le R}
 \le C_4\sum_{\substack{1\le t\le R\\t\text{ odd}}}
       \frac{t^2}{1-(3t/(3t+1))^4}<\infty.}\tag{3}$$

In particular,

$$P_q^{\le R}\longrightarrow0\qquad(q\to\infty)\tag{4}$$

for every fixed finite $R$.

**Proof.** The exact primitive source $b_w$ is positive odd and satisfies $U^q(b_w)=r_w$ with precisely the word $w$. For fixed $q$, different words have different sources because an ordinary source has a unique first $q$ valuation word. Therefore the primitive-word sum is a sub-sum of the actual all-source endpoint mass:

$$P_q^{\le R}\le\sum_{\substack{1\le t\le R\\t\text{ odd}}}M_q(t).$$

Sum over $q$ and apply (1) to the finitely many endpoints. Positive-series summability proves (4). QED.

## ES3. A sharp per-source fifth-power Green bound

The preceding fixed-target bound can be strengthened to a global positive estimate that includes every endpoint. For one original source $n$, put $n_q=U^q(n)$ and

$$I_q=\prod_{j<q}\left(1+\frac1{3n_j}\right),\qquad
 V_q=\left(\frac{J_q(n)}{n_q}\right)^4=\frac1{n^4I_q^4}.$$

Define $\delta(t)=1-(3t/(3t+1))^4$. The exact telescoping identity is

$$V_q-V_{q+1}=V_q\delta(n_q).\tag{5}$$

For every integer $t\ge1$,

$$\delta(t)\ge\frac{175}{256t}.\tag{6}$$

To verify (6), clear its positive denominator. The resulting numerator is

$$(t-1)(13473t^3+8397t^2+2019t+175)\ge0.$$

Consequently

$$\frac{J_q(n)^4}{n_q^5}
 \le\frac{256}{175}(V_q-V_{q+1}).$$

Sum over a finite time interval, then take monotone limits. This proves

$$\boxed{\sum_{q\ge0}\frac{J_q(n)^4}{U^q(n)^5}
 \le\frac{256}{175n^4}.}\tag{7}$$

The constant $256/175$ is sharp in this per-source statement: for $n=1$, every endpoint is one and $J_q(1)=(3/4)^q$, giving exactly $\sum_{q\ge0}(3/4)^{4q}=256/175$. The estimate neither excludes nor deletes cycle visits; their Jacobian factors decay.

Summing (7) over all positive odd original sources and retaining the primitive-word sub-sum yields the unconditional arithmetic theorem

$$\boxed{\sum_{q\ge1}\sum_{w\in\mathbb N_{>0}^q}
 \frac{J_w^4}{r_w^5}
 \le\frac{256}{175}C_4<\frac{512}{175}.}\tag{8}$$

No simple-path, density, or conjectural convergence premise enters this proof. The root agent and arithmetic reviewer independently supplied the telescoping improvement; the arithmetic reviewer supplied the sharp rational constant in (6).

In particular (8) strengthens (3) to the simultaneous endpoint bound

$$\sum_{q\ge1}P_q^{\le R}
 \le\frac{256}{175}C_4R^3<\frac{512}{175}R^3.\tag{9}$$

There remains a gap of three endpoint powers between the unconditional all-time sum (8) and the original weight $r_w^{-2}$. Removing that gap has not been accomplished.

## ES4. Quantified bounds for growing endpoint cutoffs

At each fixed time $q$, distinct primitive words have distinct ordinary sources $b_w$. Their exact correction products are at least one, so

$$\frac{J_w^4}{r_w^2}=\frac{r_w^2}{b_w^4I_w^4}\le\frac{R^2}{b_w^4}
\qquad(r_w\le R).$$

Summing gives the additional unconditional bound

$$\boxed{P_q^{\le R}\le C_4R^2<2R^2.}\tag{10}$$

For every fixed $\beta\ge0$, (8) also gives

$$\boxed{\sum_{q\ge1}
 \frac{P_q^{\le\lfloor q^\beta\rfloor}}{q^{3\beta}}
 \le\frac{256}{175}C_4<\frac{512}{175}.}\tag{11}$$

Indeed each summand with $r_w\le q^\beta$ satisfies

$$q^{-3\beta}J_w^4/r_w^2\le J_w^4/r_w^5.$$

For $\beta>0$, the elementary positive-series form of Kronecker's lemma, or splitting off a fixed finite initial segment, gives

$$\sum_{q\le N}P_q^{\le\lfloor q^\beta\rfloor}=o(N^{3\beta}).\tag{12}$$

For clarity, after any cutoff $Q$, divide the first $N$ terms by $N^{3\beta}$. The initial $Q$ terms tend to zero and the remaining terms are bounded by the tail $\sum_{q>Q}q^{-3\beta}P_q^{\le\lfloor q^\beta\rfloor}$, which can be made arbitrarily small. At $\beta=0$, (11) instead gives finite total mass directly.

Two consequences are useful.

* For $0\le\beta\le1/3$, the moving-cutoff part has finite harmonic time sum $\sum_{q\ge1}P_q^{\le\lfloor q^\beta\rfloor}/q$ and therefore has Cesàro mean tending to zero.
* For every $\beta<20/19$, the fixed-time bound (10) makes its cumulative contribution $O(N^{1+2\beta})=o(N^{59/19})$ in the positive-average criterion PC. In particular the entire region $r_w\le q$ is harmless: (12) even gives a cumulative contribution $o(N^3)$. It is also harmless for the old pointwise condition $P_q=o(q^{40/19})$, because (10) bounds it by $2q^2=o(q^{40/19})$.

Thus PC is equivalent to the narrower tail question

$$\boxed{\liminf_{N\to\infty}N^{-59/19}
 \sum_{q=1}^N\sum_{\substack{w\in\mathbb N_{>0}^q\\r_w>q}}
 \frac{J_w^4}{r_w^2}=0.}\tag{13}$$

Both directions follow because the omitted nonnegative cumulative contribution is $o(N^{59/19})$. The region $r_w^4\le q^3$ suggested in the initial review is a smaller subset already covered by this larger removal. The adjacent standalone question uses the simpler exact guard $r_w>q$.

Equation (13) remains OPEN. The unconditional fifth-power sum and the removal of the low-endpoint region do not prove it.

## Meaning for the remaining arithmetic estimate

For each fixed $R$, all four closing questions in `MOMENT_QUANTILES.md` concern the part of the moment whose endpoint eventually exceeds $R$. In particular

$$\liminf_{q\to\infty}P_q
 =\liminf_{q\to\infty}\bigl(P_q-P_q^{\le R}\bigr).$$

A possible concentration at a "small representative" must therefore mean small compared with the exponentially growing ambient interval $[1,2\cdot3^q)$; it cannot mean persistent mass at one fixed finite set of endpoints.

The pointwise fixed-cutoff limit (4) alone does not supply an arbitrary moving-cutoff limit. Sections ES3–ES4 give specific averaged bounds where they do follow from the quantitative estimates. The rational bound in (1) grows cubically in $t$, so summing it over all endpoints diverges. Uncontrolled concentration at growing endpoints remains the first unsupported step. No bounded-liminf, quantile, finite-energy, or complete convergence conclusion is inferred.
