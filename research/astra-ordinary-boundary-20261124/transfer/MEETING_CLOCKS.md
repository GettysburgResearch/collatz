# The critical clock for independent ordinary trajectories to meet

**PROPOSED written theorem, conditional on the specific published and repository estimates listed below.** On each resolved moving head patch there is an exact leading threshold for a positive fraction of independent ordinary pairs to have a common iterate. The clocks on the arms may differ. The eventual collision probability tending to one remains open. With the additional relative first-landing input, [ALL_EVENTUAL_MEETINGS.md](ALL_EVENTUAL_MEETINGS.md) captures the entire eventual meeting probability inside one centered finite window and identifies its limit. The independent law here is the law required in PR197's one-patch closing criterion. The head deletion pair has a different law.

Use $T(n)=n/2$ for even $n$ and $(3n+1)/2$ for odd $n$. Put $O(y)=\{T^k y:k\ge0\}$, $R_j=81^j$, $d=\log_2 R_j$, $a=1-(\log_2 3)/2$, and

$$ C_*=(a\log 2)^{-1}=2/\log(4/3). $$

Unsubscripted logarithms are natural. A logarithmic patch $W_j$ is an interval on the circle $[0,1)$, contained in the head arc $[\log_{81}7,\log_{81}8)$. Its ordinary sample is uniform on the integers $n$ with $\log_{81}(n/R_j)\in W_j$. For each $j$ choose a continued-fraction denominator $q_j$ of $\log_{81}2$, with $q_j\le j^{1/4}$. Write $e_j=q_j/\sqrt j+1/q_j$. Call the patch resolved when $e_j=o(|W_j|)$. In particular every fixed head subinterval qualifies when the largest such denominator is used. Patch locations and widths may vary independently on the two arms.

**Theorem.** Let $X,Y$ be independent ordinary samples in two resolved patches at row $j$. For every $A>0$, there is a constant $C_A$ such that, except with probability $O_A(d^{-A})$, every common iterate $T^iX=T^kY$ has

$$ \min(i,k)\ \ge C_*\log R_j-C_A\sqrt{d\log d}. \tag{1} $$

For every fixed $\epsilon>0$ the probability of a common iterate with $\max(i,k)\le(C_*+\epsilon)\log R_j$ has positive lower limit. In fact, a positive fraction of the pairs reach any prescribed fixed odd $b$ with $3\nmid b$ by that deadline on both arms. No assertion is made at equality. For a single sample the same lower-time exclusion holds against *any one prescribed full forward trajectory* $O(y_j)$ with constants uniform in $y_j$. The positive hit fraction applies to each fixed $O(y)$ by taking an odd ternary unit on it: strip twos, apply an odd transition and strip twos again. Its constant may depend on the chosen unit.

The two conclusions also hold for independent uniform positive integers up to $N$, replacing $R_j$ by $N$. In particular the infimum of coefficients $c$ for which the proportion of independent pairs meeting by $c\log N$ on both arms has positive lower limit is exactly $C_*$. The upper side gives a positive proportion, including thresholds arbitrarily close to $C_*$; the input does not give proportion one.

## Lower clocks: sample against the partner's entire forward trajectory

We use two inputs. Leen's uniform orbit-set sparsity says that for absolute $C>0$ and $0<\theta<1$, the *set of distinct values* on any one ordinary shortcut trajectory has at most $CL^\theta$ points in any integer interval of length $L\ge1$. The statement and a reference to Leen's proof are given in [Geometry, integer fibres, and dyadic equidistribution, §9, (B1)](https://rstation.ai/problems/collatz/papers/19/v2). Cyclic orbits are included.

The second input is the one-arm first-passage estimate at $M=d^D$ on an original fixed-ratio annulus, with $D$ sufficiently large for any prescribed absolute exception $O_A(R_jd^{-A})$. Off that exception the first hit $v=T^h n<M$ occurs in $[M/2,M)$ and

$$ ah=d-\log_2 M+O_A(\sqrt{d\log d}). \tag{2} $$

The normalized regular mass per single $v$ is at most $C_A\sqrt d(\log d)^{3/2}/M$. For clarity, (2) gives $O_A(\sqrt{d\log d})$ choices of $h$. On narrow source annuli, for fixed $v,h$ only $O(1)$ odd counts are possible. The sliding-window correction to the exact multiplier is $O_A((\log d)/M)$, leaving $O_A(1+R_j(\log d)/M)$ sources per $(v,h,p)$. A fixed-ratio annulus can be divided into finitely many narrow ones. These statements are [PR193, HEAD_ROOTS, last section](../../astra-closure-20261124/transfer/HEAD_ROOTS.md), and [(3)–(5) of PR197's landing-weight proof](https://github.com/GettysburgResearch/collatz/blob/9ab91d964b38fc870d1034bac628d62f59488467/research/ayh-resource-reset-20261124/joint-renewal/LANDING_WEIGHT_TRANSFER.md). Here we count the entire one-arm population, including early head fusions. There is no second independently drawn landing in the proof of this marginal bound.

The deterministic identity is

$$ \{\exists i\le h,\ k\ge0:T^i n=T^k y\}=\{T^h n\in O(y)\}. \tag{3} $$

An early common iterate propagates forward by $h-i$ additional steps on both paths. Conversely the event on the right already supplies a meeting. Take $h$ to be the realized first passage in (2). At most $CM^\theta$ possible landing heights lie in $O(y)$, even if the latter is unbounded. Thus the fraction on the fixed annulus hitting any point on this entire trajectory at or before first passage is at most

$$ O_A\!\left(d^{-A}+\sqrt d(\log d)^{3/2}M^{\theta-1}\right). \tag{4} $$

The constants are independent of $y$. The exponent $D$ may be enlarged so the second term is $O_A(d^{-A})$. More generally one prescribed dictionary of $d^B$ ordinary trajectories costs a factor $d^B$ on the second term, for arbitrary fixed $B$, with a single exceptional set. This includes a dictionary sampled independently of the tested source by conditioning on it. Passage to a patch costs $O(1/|W_j|)$ in absolute probability. Since $e_j\ge j^{-1/4}$ and the patch is resolved, increasing $A$ by one absorbs that factor. Condition first on $Y$, with the whole $O(Y)$ now fixed, then separately on $X$ for the reverse event. The two unioned exceptions and (2) prove (1). Even the unrestricted clock on the partner contributes no extra count.

For sampling from $[1,N]$, discard $n<N/(\log N)^{A+2}$ at cost $O((\log N)^{-A-2})$. Partition the remainder into ordinary dyadic annuli (cover a partial last interval by its full annulus). Their total lengths are $O(N)$ and their logarithms are $\log N+O_A(\log\log N)$. The same estimates hold there uniformly by applying the argument with the scale of each annulus. No density of a convergence basin is needed for (1).

## Upper clocks: positive timed mass on every resolved patch

Use [Idris Ali Shaik, *Positive density of Collatz convergence at every rate above $3/\log(4/3)$*, Hexagon v1, Theorems I.1–I.2, p. 2](https://hexagonmath.org/pdf/2610.00523v1). For every fixed positive $b$ coprime to three there is $\delta_b>0$ such that for every $c>3/\log(4/3)$ the integers whose **ordinary** first hit of $b$ takes at most $c\log n$ ordinary steps have lower natural density at least $\delta_b$. We choose odd $b$ to ensure the shortcut grouping retains it. This is a source-qualified input. Its external Lean package was not rebuilt.

Write $t,p,h$ for the shortcut length, odd count and ordinary length to the *first* hit of $b$. Then $h=t+p$. All shortcut states strictly before the first hit are distinct; summing the orbit-sparsity estimate over dyadic bands bounds their total $E=\sum_{u\text{ odd}}\log(1+1/(3u))$ by an absolute constant. The exact multiplier and clock conversion give

$$ t\log 6=\log(n/b)+h\log 3+E. \tag{5} $$

Indeed $b=n3^p2^{-t}e^E$. The identity $1+(3/\log(4/3))\log 3=(2/\log(4/3))\log 6$ now gives, for every $\eta>0$, lower natural density at least $\delta_b$ of shortcut hits by $(C_*+\eta)\log n$ (choose the ordinary slack sufficiently small, and absorb the bounded term). This already proves the asserted upper result for independent uniform integers up to $N$ using the same fixed $b$ on both arms.

The transport to small moving patches must preserve the deadline. Let $G_j^K(u)$ be the indicator of hitting $b$ by $K$ shortcut steps from $\lfloor R_j81^u\rfloor$, and $p_j^K=\int_0^1G_j^K(u)\,du$. The indicator can change along a trajectory near its deadline, so a theorem for an invariant component color cannot be applied directly.

We use the physical residue-grid estimate and the lifting identities of [PR197, MACROSCOPIC_PAIR_CLOSURE, proof of (1)](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/research/ayh-resource-reset-20261124/literature-step/MACROSCOPIC_PAIR_CLOSURE.md), from [PR146, GROWING_ADDITIVE_GAPS](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md). In the comparison of $m$ and $81m+r$, a common-clock fusion by $h_0=\lfloor d/2\rfloor$ is certified off relative error $O(j^{-1/2})$. Both prefixes stay above $b$ since every step loses at most a factor two, so the first-hit clocks, including $+\infty$, agree exactly on success. In particular

$$ \|G_{j+1}^K-G_j^K\|_1\ll j^{-1/2} \tag{6} $$

uniformly in the frozen $K$. For $0\le k<q_j$, write $v=\{u+k\log_{81}2\}$, $l=\lfloor u+k\log_{81}2\rfloor$. The new integer source is $2^km+s$ with $0\le s<2^k$. Its first $k$ physical steps give $3^a m+c$, $0\le a\le k$ and $0\le c/3^a<4/3$. The same grid theorem fuses this endpoint with $m$ above $b$ except on $O((k+1)/\sqrt j)$ log measure after averaging the digits. The initial $k$ steps from $2^km+s$ stay at least $m$; the comparison from $3^am+c$ and $m$ stays above $b$ through its $h_0$-step cap. The new first-hit clock is therefore exactly the old one plus $k$ whenever it is finite. Thus $G_j^K(u)\le G_{j+l}^{K+k}(v)$ except on the indicated set. The index $l$ takes at most two nonnegative values bounded by $k+1$. Telescoping (6) at the *same frozen deadline* $K+k$, rotation invariance of Lebesgue measure and monotonicity in the deadline permit replacement by $G_j^{K+q_j}(v)$ at an additional $O((k+1)/\sqrt j)$ cost.

Multiply this one-sided comparison by $\mathbf1_W(v)$ and integrate in $u$. Average $0\le k<q_j$. The translates by $k\log_{81}2$ differ by $<1/q_j$ from a permuted $q_j$-grid, giving uniform interval discrepancy $O(1/q_j)$. Consequently, for every interval $W$,

$$ \int_W G_j^{K+q_j}\,du\ \ge |W|p_j^K-O(e_j). \tag{7} $$

For $K=\lfloor(C_*+\epsilon/2)\log R_j\rfloor$, (5) with slack $\epsilon/4$ puts $\gg_b81R_j$ timed sources below $81R_j$ at this frozen deadline. Choose fixed $s=s(b)$ so the sources below $R_{j-s}$ use at most half that count. The log density on each of the finitely many remaining annuli converts counts to integrals with bounded annulus-scaled factors, giving $\max_{0\le l\le s}p_{j-l}^K\gg_b1$. Equation (6) yields $p_j^K\gg_b1$. Since $q_j=o(\log R_j)$, the wider deadline in (7) is below $(C_*+\epsilon)\log R_j$ for large $j$. On each resolved patch the error is $o(|W_j|)$. Each integer cell has log length comparable to $1/R_j$ on this annulus, with at most two partially covered cells. This proves the positive lower bound for the uniform ordinary sample. Independence gives the product bound on the two actual patches.

If a second component exists, take a fixed odd ternary unit on its trajectory and the target one. The same transport gives positive proportions in *both* fixed basins, already certified to have reached their respective targets by each supercritical deadline. Pairs assigned the different targets cannot ever meet. The sizes of the two proportions may depend on the targets. The reverse implication from a positive fast meeting fraction to uniqueness of the component would be false as an inference from these lower bounds.

## Evidence and remaining obligation

The three Std-only theorems in [TraceClocks.lean](TraceClocks.lean) check (3), the exact ordinary clock at every shortcut endpoint, and the converse endpoint representation of every ordinary hit at an odd target. Official Lean 4.34.1 checked these declarations with warnings as errors. The probabilistic and asymptotic claims above are written mathematics with the listed inputs. [Trace sampling and the surviving head pair](TRACE_SAMPLING.md) records the original two-arm estimate and its domain. For full closure, PR197 needs near-certain eventual meeting on some resolved independent patch, or summability of discordance on the correlated head pair. Neither the positive sharp-time mass nor the uniform early exclusion proves that conclusion.
