# A polynomial real-offset window and sparse-set bounds for ordinary trace

Use the positive odd map, the all-visit canonical real fibre $\mu_y$ at root $y$, the additive Haar stationary envelope $E$, $I_Y=[Y,\lambda Y]\cap(2\mathbb N+1)$, and the stationary joint law $(Z_*,R_*)$ from [the full marked theorem](REAL_OFFSET_ORDINARY_TRACE.md). Let $G_Y$ be the ordinary good set in [the power-capped theorem](POWER_CAPPED_ORDINARY_TRACE.md). The following are source-qualified written estimates for the original ordinary sites.

## A true growing offset cutoff at every site

Fix $0<s<1/64$. Let $w(y)\to\infty$ be any prescribed function with $w(y)\le y^s$ eventually. Then for every fixed ternary cylinder $C$,
\[
 \boxed{\quad
  \sum_{y\in I_Y\cap C}\frac{h(y)}y\,\mu_y([0,w(y)])
       \longrightarrow \frac{\log\lambda}{2}\Pr(Z_*\in C).
 \quad}                                                               \tag{1}
\]
All positive odd roots and repeated visits on every cycle are included. There is **no truncation of the trace amplitude** $h(y)$. The cutoff acts on the genuine absolute affine offset at that root. The same positive measures converge weakly on the whole real and ternary space to the stationary joint law times $(\log\lambda)/2$: compact real tests have their exact limit by the full marked theorem and (1) supplies total mass convergence. Subinterval testing gives the natural-source version and independent physical interval coordinate as in that theorem.

For the upper bound put $B=(\lambda Y)^s$, $Q=\lceil2\lambda Y\rceil$, $K=\lfloor(\log Y)/2\rfloor$, and $L=\lfloor Y/(6(B+1))\rfloor$. A visit to $y\in I_Y$ with original offset at most $B$ takes place before any departure from $z\le L$, and its entire trajectory has at most $O_\lambda(1+B)$ such visits. Both facts are proved in the full marked theorem. Drop the prehistory at the first landing at $Q$. The reset only *decreases* the affine offset, so the reset eligibility gives an upper bound, and all its visits still precede the first subsequent departure from $[1,L]$.

The bad landing labels are odd $z\le Q$ whose path fails to reach $[1,L]$ by $K$. Under a uniform odd $z\le Q$, the binary class error for its first $K$ gaps through $b=\lfloor0.9\log_2 Y\rfloor$ is $O(2^b/Y)$ and the iid overflow is $O(Y^{-1/50})$ as in the power-capped theorem. On agreement and failure the iid total $V_K=S_K\log2-K\log3$ is at most $s\log Y+O_\lambda(1)+K/(3L)$. The negative half tilt then gives
\[
     |\mathrm{Bad}|/Q\ll_\lambda Y^{-1/50}+Y^{s/2-1/40}.
\]
Both decay exponents are strictly larger than $s$. The **limiting** first-landing law through $Q$ gives this entire bad set mass at most $C\exp(C\sqrt{\log Q})(|\mathrm{Bad}|/Q+Q^{-g})$, with $g=1-H_2(\log_3 2)+1/351>1/64$. Hence (even using the $O_\lambda(B+1)$ trajectory maximum) these bad landings contribute $o(1)$ to the far-source upper bound. Failure at $Q$ contributes nothing. [Weaver 102/v1, Theorem 1 (1)–(3)](https://rstation.ai/problems/collatz/papers/102).

On good landings the reset marked count is at most $K+1$. Compare this bounded observable using Lemma 5 (20), (24) of the same source to a smooth local $\mathbf U_X$ with $X=Q^\xi$, $1.001<\xi_1\le\xi\le\xi_2<(1.001)^2$. The total comparison cost is $o(1)$. At the local source, failure to reach $L$ by $K$ has probability $O_\lambda(Y^{-c})$ for some $c>0$, by the same negative half tilt with $s$ replaced by $s+(1.001)^2-1$. Since the **good-label test** stays bounded by $K+1$ even there, these trajectories cost $o(1)$. On the others bound the good reset count by all visits to $I_Y\cap C$ before first reaching $L$, up to $K$, dropping the mark. The affine logarithmic discrepancy up to that crossing is at most $K/(3L)$. Thus the independent-prefix coupling and averaged height-window calculation in the full marked theorem apply with unit weight. For each bulk $j\ge k$ the fixed ternary cylinder of precision $k$ is read from the last $k$ iid gaps. The resulting limsup of the expected count is $(\log\lambda)\Pr(Z_*\in C)/D$. In the far-source density identification multiply by $\kappa=D/2$; with a sharp cutoff one can equivalently first bound continuous tests supported strictly below $B+1$ and approximate the indicator from above at the finitely many roots for fixed $Y$. The universal bounds above hold with $B+1$ as well. For the lower bound take any $0\le f\le1$ continuous with fixed compact support. Eventually its whole support is accepted in (1). The marked theorem and monotone exhaustion prove the lower. This establishes (1) for site-dependent cutoffs.

## A power estimate at the lower end of every true real fibre

Write $\tau_y=1$ off cycles and $1-\omega_y$ on a cycle of primitive survival $\omega_y$. For $\eta_0=1-H_2(\log_3 2)+7/2500$ and every $0<t\le1$,
\[
       \tau_y\,\frac{h(y)}y\,\mu_y([0,ty])
                    \ll t^{\eta_0}                                    \tag{2}
\]
uniformly in every positive odd $y$. The exponent can be replaced by any fixed number below the $g$ above, with its own constant. For small $t$ take $M=\lfloor1/(6t)\rfloor$. A first-arrival path from a source to $y$ with $R/y\le t$ has no preceding departure at a vertex $u\le M$, since that one factor would give $R/y\ge1/(3u+1)>t$. Its first landing through $M$ must equal the single label $\operatorname{Pass}_M(y)$, including possible failure. The first-hit weighted limiting mass is bounded by $\kappa$ times the limiting probability of that label. Weaver's (3) bounds it by $C M^{-\eta_0}$. To handle a closed cutoff without a continuity assumption use a slightly larger $t$ and the same argument for continuous upper majorants. At a periodic root the full marked measure is the sum of first-hit measures over laps of weights $\omega_y^j$ and maps $r\mapsto y-\omega_y^j(y-r)\ge r$. Multiplication by $1-\omega_y$ proves the same upper. The empty path is attained only by a single physical source and has zero limiting natural mass. Bounded $M$ are covered by $\tau_y h(y)/y\le\kappa$. This is a one-sided estimate at real offset zero.

In particular, on any fixed escaping ray with $h(y)/y\to H_C>0$, the probability of seeing true real mark $R\le y^s$ is $O_C(y^{-(1-s)\eta_0})$. At any fixed relative threshold $t>0$, a different deterministic observation identifies the possible carriers of the opposite tail. A simple first-arrival path avoiding every departure through $M$ has $R/y\le C M^{-1/50}$ by uniform reciprocal packing. Choose $M=M(t)$ so this is less than $t$. At high nonperiodic targets, a stationary path with $R/y\ge t$ therefore forces the target onto the forward orbit of an ordinary $m\le M$. Only finitely many ordinary rays can support this macroscopic tail outside a finite set. Repeated cycle laps require the first-hit restriction for this support assertion. [Elementary packing at pinned PR212](https://github.com/GettysburgResearch/collatz/blob/31311116eac06e87320c84e11de6c105292a6f78/research/astra-infinite-descent-20261127/escape/HIGH_TARGET_ROWS.md).

## Physical sparse-set regularity and moments above order one

Uniformly for every $A\subseteq I_Y$, fixed $1<p<2$, and every fixed $J>0$,
\[
       \sum_{y\in A\cap G_Y}\frac{h(y)}y
       \le C_{p,\lambda}(|A|/Y)^{1-1/p}
                        +O_{J,\lambda}((\log Y)^{-J}).                 \tag{3}
\]
Apply the good-site proof of the power-capped theorem with the subset $A$ retained throughout. The far-to-local comparison still costs $O_J((\log Y)^{-J})$ since its test is bounded by $K+1$. The true local prefix fails to reach the floor through $K$ with a power-saving probability; this exception costs the same negligible error. Average the local smooth source scales uniformly in $\log X$ on the interval there, of width comparable to $\log Y$. Because each contributing scale has $X\asymp x$ and mass $O(1/X)$ at the actual start $x$, this mixed source gives it mass $O(1/(x\log Y))$. For $j\le K$, each of its pre-floor visits to $y$ has $b_j(x)\ge1-K/(3L)\ge1/2$. Consequently
\[
  \sum_{x:U^jx=y,\ \text{pre-floor}}1/x
       \le2\sum_{U^jx=y} b_j(x)/x=2\rho_j(y)/y .
\]
The density $\rho_j(y)=3^j\Pr(Z_*\equiv y\bmod3^j)$ counts all compatible inverse words. At the depths used here $R_j\le(3/2)^j-1<Y$ for $j\le K=\lfloor(\log Y)/2\rfloor$, so the inverse image of $y\ge Y$ under each compatible word is a positive odd integer. This justifies exact equality of the column sums. The upper-bound direction alone suffices. Its period is $3^j\le3^K=o(Y)$. Its normalized Haar $p$-moment is uniformly bounded for each fixed $p<2$. Full periods on a slightly extended octave give $\sum_{y\in I_Y}\rho_j(y)^p=O_{p,\lambda}(Y)$ (one period in the odd enumeration has $3^j$ sites). Hölder bounds the resulting sum over $A$ at each $j$ by $C(|A|/Y)^{1-1/p}$. Sum the $K+1$ possible times and divide by the $\log Y$ from mixed source weights. Since $h(y)/y\le\kappa d_y$ on $G_Y$, this proves (3). [Weaver 9/v2, §1 and Theorem 16 (B3), with the prior finite-quotient regularity credited there](https://rstation.ai/problems/collatz/papers/9).

If $u(y)\to\infty$ and $u(y)\le(1+\log y)^A$ eventually for some fixed $A$, then for every $0<q<2$ the natural and harmonic physical average of $\min(h(y),u(y))^q$ converges to $\int E^q\,d\nu$, also with bounded continuous ternary and physical factors. To verify uniform integrability fix $\max(1,q)<p<2$. Let $v$ be the fraction in $I_Y$ of good sites with $h(y)>T$, $T\ge1$. Equation (3) implies $Tv\ll v^{1-1/p}+O_J((\log Y)^{-J})$. Splitting at which term is larger yields $v\ll_p T^{-p}+O_J((\log Y)^{-J}/T)$. Integrate the tail against $qT^{q-1}$ from a fixed large threshold to the largest polylogarithmic cap on the octave, choosing $J$ arbitrarily large. The omitted sites have fraction $O(Y^{-1/64}\log Y)$ and hence contribute $o(1)$. The unmarked physical joint weak law identifies the moment limit. At $q\ge2$ the Haar second moment is already infinite; nothing in these bounds supplies a finite limit there. [Physical unmarked joint law](POWER_CAPPED_ORDINARY_TRACE.md) · [Haar critical integrability](https://rstation.ai/problems/collatz/papers/9).
