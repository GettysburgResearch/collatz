# All high recrossings before the first global minimum

**Source-qualified written theorem.** Use the positive odd map $U$, let $Y_B$ denote first odd entry at or below $B$, and let $m(x)$ be the minimum on the full ordinary orbit. A segment ending at the first global minimum is finite and simple, also for a nonterminating source. The following gives a quantitative bound on the time range where upward recrossings can occur during its initial descent. The later path from the minimum itself is a distinct part of the ordinary trajectory.

For $M\ge2$, every $0<\eta<1$, any uniform original odd octave with $X\ge B$, and also the limiting distant source law, one has
\[
 \limsup_{B\to\infty}\ \sup_{X\ge B}
 \Pr\left(\begin{array}{c}\text{after first reaching an odd state }\le B/M,\\
  \text{an odd state exceeds }B\text{ before the first global minimum}\end{array}\right)
              \ \ll_\eta M^{-\eta}.                                   \tag{1}
\]
The intermediate entrance must exist for the event to occur. Real cutoffs mean their integer floors. Together with [the true first-to-last conditional law](FIRST_AND_LAST_LANDING.md), (1) identifies the entire list of odd upcrossings above $B$ after the first entrance at $B$ and before the first minimum. From $B\to\infty$, $X/B\to\infty$, its discrete crossing dates, counted from that entrance, converge in total variation to those of
\[
       X_0=V,\qquad X_i=V\,3^i2^{-S_i},\qquad
       S_i=\sum_{j\le i}E_j,\quad \Pr(E_j=e)=2^{-e}.                  \tag{2}
\]
Here $V$ has the real Palm first-landing distribution $\lambda(u)du$ on $[0,1]$, independent of all subsequent iid gaps. An upcrossing in (2) is $X_{i-1}\le1<X_i$. Either the odd date $i$ or the pair $(i,S_i)$ may be marked. The list is finite almost surely, with an exponentially decaying limiting tail for its last date. Its joint law with the true eventual last exit at $B$ differs by $o(1)$ in sum norm from the product of this limiting list law and the actual outgoing marginal, using a default for bounded fates. The same applies after terminal-product reweighting on the escaping population. For normalized real heights at the crossing times, this is weak convergence in the height coordinates, with arbitrary tests of the discrete outgoing mark that are bounded and uniformly equicontinuous in the heights.

## An excursion from one octave to the next lower octave

Use real dyadic floors $L_j=B/2^j$, and, initially, $L=L_j$ above a large fixed cutoff $L_0^*$. For positive odd integer labels $y\le L$, call the interval of its orbit from $y$ to first odd entry at or below $L/2$ one stage. It can be empty or can fail to finish. Take $n=\lfloor c_0\log L\rfloor$ with $4c_0\log2<1/2$, and choose $\log_2 3<\beta<2$. Under uniform odd inputs through $L$, apart from a relative $O(L^{-c_1})$ set, the first $n$ gaps have total $\beta n\le S_n\le4n$. This is the ordinary iid geometric tail estimate with the $O(2^{4n+1}/L)$ incomplete binary cylinder error. If a good input exceeds $L/2$ and still has not completed the stage through date $n$, all departed odd states exceed $L/2$, so
\[
        U^n y\le y\,3^n2^{-S_n}\exp(2n/(3L)) < L/2
\]
for sufficiently large $L$, a contradiction. Thus it finishes in at most $n$ odd steps.

On this same good event, a visit $U^i y>B$ before stage completion requires $3^i2^{-S_i}\ge c B/L=c2^j$, using the identical product bound up to $i\le n$. Under the iid geometric law $A_i=3^i2^{-S_i}$ is a nonnegative mean-one martingale since $\sum_{e\ge1}3\,4^{-e}=1$. Its maximal inequality bounds the event by $C2^{-j}$ uniformly in $n$. Truncation to total $4n$ and the binary cylinder discrepancy just counted therefore bound the relative number of ordinary starting labels that fail the stage or exceed $B$ during it by $C(2^{-j}+L^{-c_1})$. Immediate landings have no such positive-time excursion.

The actual $Y_{L_j}$ is the first landing of the *original* sample, regardless of its intervening orbit. Apply the [arbitrary-set first-landing estimate](FIRST_LANDING_ENTROPY.md) to these bad labels. The chance that the stage starting at a finite $Y_{L_j}$ is bad is at most
\[
             C_{\eta,K}\big(2^{-\eta j}+(1+\log L_j)^{-K}\big)         \tag{3}
\]
for every fixed $K$. This holds simultaneously as a collection of marginal bounds, without any stochastic independence of the true successive stage labels.

Set $j_*=\lfloor\log_2 M\rfloor$, so the first entry to $L_{j_*}\ge B/M$ has already occurred by the specified entrance to $B/M$. Sum (3) over $j\ge j_*$ while $L_j\ge L_0^*$. The cost is $O_{\eta,K}(M^{-\eta}+(1+\log L_0^*)^{1-K})$. If the first entry at $B/M$ occurs, all predecessor stages there have been entered, and if every such stage is good the orbit reaches a positive label at most $L_0^*$ with no visit above $B$ in the intervening part. The finitely many labels through $L_0^*$ each have a fixed finite segment to their own first global minimum, of bounded maximum depending only on $L_0^*$. For $B$ exceeding all these maxima there can be no further preminimum upcrossing. If the global minimum already occurred before a relevant stage, its future does not contribute to the event either. Take first $B\to\infty$, then $L_0^*\to\infty$, proving (1) with constants uniform in the original source octave.

## The limiting crossing process and its scope

First stop the preminimum observation on first entry to $B/M$ for fixed $M$. The probability of failing to reach that floor in any specified long but fixed number $N$ of odd steps after $Y_B$ is bounded in the limit by the same quantity in (2). Indeed, truncate the first $N$ total gaps at a large fixed integer, apply (1) of [first and last landing](FIRST_AND_LAST_LANDING.md) to the required binary prefix and a fine real partition, and increase the truncation. For a fixed gap word, every finite scaled iterate differs from its multiplicative model by $O_N(1/B)$, and equality with either threshold has probability zero by absolute continuity of $V$. The possible comparisons use finitely many real cut points once the total is bounded. This gives convergence in sum norm for the finite list of crossing dates and the true outgoing mark, with a product limit; it also gives the indicated weak joint test version for any finite set of heights. When entry at $B/M$ occurs, the first global minimum cannot precede it: that earlier minimum would itself have been an entry. The exceptional case of never entering $B/M$ has vanishing probability as $B\to\infty$ by the smaller-floor cemetery estimate.

Under the limiting iid law $S_i/i\to2$, so entry at $1/M$ is almost surely finite. Let $N\to\infty$ for each fixed $M$. The probability of any subsequent crossing before the actual first minimum is bounded by (1). On the iid model the probability of a later return above one after that low entry is at most $1/M$ by the same martingale inequality conditional on the stopping time. Hence $M\to\infty$ gives the complete list claim. Bounded terminal weights determined by a subsequent smaller landing can be attached throughout, and replacement by $F$ uses the vanishing high simple-segment error as in equation (2) of the first-to-last theorem. A positive lower bound on a conditioning event gives the corresponding normalized conditional result.

The last limiting upcrossing has exponentially decaying date tails. Indeed $V\le1$ and $X_i>1$ requires $A_i>1$. For any $0<s<1$, $\mathbb E A_i^s=[3^s/(2^{1+s}-1)]^i$, with base less than one. Summing over $i\ge n$ proves the odd-date tail. When $X_i>1$ its native date also satisfies $S_i<i\log_23$, giving the same exponential conclusion there.

The expected number of upcrossings **in the limiting law** is
\[
                         \frac{\log(3/2)}{2D}.                         \tag{4}
\]
To compute it use a two-sided drift-$D$ walk $Z_j$ with increments $E_j\log2-\log3$. Since $Z_j\to-\infty$ as $j\to-\infty$, each real level has a unique first upward crossing from the infinite past apart from boundary points. For times $i<j$, let $M(i,j)$ be the Lebesgue measure of levels first crossed up at $i$ and subsequently crossed down at $j$. The downward levels at $j$ have total length $(Z_{j-1}-Z_j)_+$, and each was first crossed earlier. Translation invariance of the iid increments gives $\mathbb E\sum_{j>0}M(0,j)=\mathbb E\sum_{i<0}M(i,0)=\mathbb E(Z_{-1}-Z_0)_+$ by Tonelli. At time zero the first-crossed interval has length the record increment $L$ in the Palm formula of [the original profile](LOCAL_LANDING_PROFILE.md); the logarithmic overshoot is uniform along that interval and its future increments are independent. Thus the left side equals $D$ times the expected number of subsequent physical upcrossings in (2). The decreasing-step expectation on the right is $\log(3/2)/2$ since precisely the gap one gives a negative increment. This proves (4). Convergence of the original crossing-count distributions by itself does not imply convergence of their untruncated expectations. High excursions made *after* an attained ordinary minimum still depend on that minimum's true deterministic forward path.


## A lower bound on the true outward edge flux at every large floor

With $a_y=h(y)/y$, $w_y=3y/(3y+1)$, $\kappa=D/2$ and total escape charge $H$, the actual one-step outward flux satisfies
\[
    \liminf_{B\to\infty}
      \sum_{\substack{y\le B<U(y)\\y\mathrm{\ odd}}} w_y a_y
                \ \ge\ \frac{\log(3/2)}4+H .                            \tag{5}
\]
The vertices in this sum are exactly those with $(2B-1)/3<y\le B$ and $v_2(3y+1)=1$. The first term is paid by actual early excursions that subsequently descend through a much smaller floor; the second term is on the disjoint set of actual last exits. This sharp-shell lower bound is related to Valbuena's earlier integrated occupation and divergent-excess inequalities. [Valbuena, raw occupation and divergent excess](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/tao-basin-densities.tex).

Indeed fix $M,N$ and retain only upward crossings in the first $N$ odd steps after $Y_B$ for paths that also reach $B/M$ within those $N$ steps. Count only crossings **before** that lower passage. Every encountered departure $y$ has a finite subsequent visit to $B/M$. It cannot be a last exit at $B$. The original positive path to its first lower passage is simple, since all earlier states exceed $B/M$. Each counted $y$ is therefore a genuine first visit on this original source, and its full first-arrival and one-edge survival weights tend uniformly to one as $B/M\to\infty$ by simple-segment reciprocal packing. For each fixed $B$ the sum of these counted natural source weights, multiplied by $\kappa$, is bounded by the sum of $w_ya_y$ at the corresponding outward edges with future passage to $B/M$. This is the weighted first-arrival formula; on a periodic site the full harmonic mass dominates the first-visit mass, as in [the stationary interface](SPATIAL_TRACE_TAIL.md). In the $B\to\infty$ limit the bounded count approaches its analogue in (2). Send $N\to\infty$, then $M\to\infty$, using monotone convergence for these retained model counts. Their limiting mean is (4), multiplied here by $\kappa$. Finally the sum over actual last exits $E_B$ of $w_z a_z$ is at least $\sum_{z\in E_B}F(z)a_z\to H$ by the [stationary last-exit theorem](SPATIAL_TRACE_TAIL.md). This proves (5) without an interchange of untruncated actual expectations. An upper bound on the same raw, uncapped physical shell remains open.
