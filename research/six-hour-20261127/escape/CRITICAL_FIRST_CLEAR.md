# The first ordinary integer and the sharp critical endpoint tail

Use the six-lift reduced rational population of [the critical source sector](CRITICAL_SOURCE_SECTOR.md). Its initial numerator is uniform on the passing sources, its height interval is \([Q/2,13Q/2)\), \(p=\log_3 2\), \(Q=2^n\), \(K=\lceil pn\rceil\) and \(q=3^K\). Write \(\mathbb P_n\) for this conditional law, \(\lambda=(1-p)/p\), \(\delta=K-pn\), \(\beta=-\log_3\lambda\) and \(\alpha=-\log_2(1-p)>1\).

The reduced denominator loses exactly one power of three on each of the first \(K\) odd departures and none on even departures. Before an odd departure at denominator \(3^d\) with \(d\ge2\), the new numerator after cancellation is \((v+3^{d-1})/2\) with \(3\nmid v\), hence is again prime to three. At \(d=1\) the new integer is \((v+1)/2\). Let \(\tau\) be the clock just after the \(K\)-th odd departure, \(Y=T^\tau(a/q)\) this first ordinary integer, \(h=n-\tau\), and \(z=T^n(a/q)=T^hY\) the census endpoint. Then \(Y\not\equiv2\bmod3\).

**Written estimates.** With \(w(y)=(1+\log y)y^{-\alpha}\), there are absolute constants \(A,C,c,Y_0>0\) such that
\[
 \mathbb P_n(Y=y)\le C w(y)\quad\text{for all }n,y\ge1,\qquad
 \mathbb P_n(Y=y)\ge c w(y)\quad
 \begin{cases}
 y\ge Y_0,\ y\not\equiv2\pmod3,\\
 n\ge A(1+\log y)^2.
 \end{cases}                                                          \tag{1}
\]
The lower estimate is attained at the particular clock \(\tau=n-h\) uniquely fixed by \(29/8\le y/2^h<29/4\). Thus every subsequential limiting distribution of \(Y\) has comparable mass at each sufficiently large admissible ordinary integer. Tightness follows by summing the upper bound. It follows as well that \(\liminf_{n\to\infty}\mathbb P_n(Y\ge R)\gg (1+\log R)R^{1-\alpha}\) with the matching upper bound uniform in \(n\), by summing through \([R,2R]\) for the lower estimate.

At the later census endpoint the preceding paper's upper tail is sharp:
\[
 \mathbb P_n(z\ge R)\asymp (1+\log R)R^{-\beta}
 \qquad(R\ge2,\ n\ge A(1+\log R)^2) .                                \tag{2}
\]
Enlarging \(A\) is harmless throughout. In particular \(\liminf_{n\to\infty}\mathbb E_n z^\beta=\infty\), by the tail-integral formula truncated at any fixed height and then passage to infinity.

## Counting cyclic rotations

Consider a binary word of length \(m\) with \(g\) ones and positive total surplus \(s=g-pm\). Extend its walk to all integer times by \(S_{i+m}=S_i+s\). A cyclic starting position is passing precisely when every forward partial sum from that position is nonnegative; positivity holds at each positive time since \(p\) is irrational. Equivalently its height is strictly smaller than every later height on the extended walk. These positions exist because every forward tail tends to infinity and has a unique least height. They repeat with period \(m\). At one such position \(i\), the next such position is the minimum over the tail starting at \(i+1\), so its height exceeds \(S_i\) by at most \(S_{i+1}-S_i\le1-p\). If \(r\) offsets pass, summing their consecutive height increments through one period gives
\[
                         s\le r(1-p).                                  \tag{3}
\]
Offsets are counted with multiplicity even for a periodic word. Summing over all words of this grade, every passing rotation has exactly \(m\) preimages when the starting offset is retained. Hence the number of passing words is at least \(\max(1,s/(1-p))\binom mg/m\).

Under iid bits of mean \(p\), for \(0<s\le c_0\sqrt m\) the single endpoint probability \(\Pr(g_m=g)\gg_{c_0}(m+1)^{-1/2}\) uniformly by Stirling. The constrained endpoint mass is therefore \(\gg_{c_0}(1+s)(m+1)^{-3/2}\), matching the upper one-sided killed transition estimate from the [critical sector](CRITICAL_SOURCE_SECTOR.md). Apply this at \(m=n\), \(s=k+\delta\). Undo the Bernoulli tilt and the exact four reduced lifts to obtain \(\mathbb P_n(g_n=K+k)\gg(1+k)\lambda^k\) whenever \(n\ge C(k+1)^2\). Since \(z\ge3^k/2\), the choice \(k=\lceil\log_3(2R)\rceil\) gives (2). This lower bound involves actual source counts and no assumption on subsequent trajectories.

## All physical first-clear targets

At a fixed \(t=n-h\), for a word of grade exactly \(K\), one target \(y\) can have at most one numerator, namely
\[
 a=2^t y-C_t,\qquad y/2^h=a/Q+(q/Q)(C_t/3^K).                       \tag{4}
\]
This gives \(h\le\log_2(2y)\). The same marked bound as (6) in the critical sector gives \(y/2^h\le13/2+V_t\), with \(V_t=\sum_{i\le t}3^{-(g_i-pi)}\). Its required terminal surplus is \(s=\delta+ph\). Discard the condition on the last bit for an upper bound and apply the exponential marked estimate (8) in that note. At this word length, removing the tilt gives the factor \(2^{H_2(p)t}\lambda^{\delta+ph}\). After dividing by the lower total mass at \(n\) the time factor is exactly \(2^{-H_2(p)h}\lambda^{ph}=(1-p)^h\). Also \(t\ge K\ge pn\) whenever such a word exists. We obtain, uniformly,
\[
 \mathbb P_n(n-\tau=h,\ Y=y)
       \ \ll (1+h)(1-p)^h\exp(-c y/2^h),                              \tag{5}
\]
where \(h\) is the specified remaining clock. The counting bound has accounted for the actual complete initial gate. Once grade \(K\) is reached at \(t\), every possible ordinary continuation through the next \(h\) ticks passes it: at any \(t+j\le n\) the grade is at least \(K\ge pn\). Summing (5) downward from \(\lfloor\log_2(2y)\rfloor\) proves the upper part of (1); the geometrically larger weights at smaller \(h\) are dominated by \(\exp(-c2^u)\) at distance \(u\) from the top.

For the lower part, take \(h\) as in (1). Use \(b\) initial ones, a middle word of length \(m=n-h-b-1\) and grade \(l=K-b-1\), and a final one. For this middle word alone require the walk of slope **\(p\)** to stay nonnegative and stop at \(s=\delta+ph-(1-p)(b+1)\). Once \(h\) is sufficiently large compared to \(b\), one has \(s\asymp h\); once \(n\ge A(1+\log y)^2\) one also has \(s\le\sqrt m\). By (3) the probability of the constrained middle event under \(p\) is at least \(c(1+s)(m+1)^{-3/2}\). The marked exponential bound divided by this lower bound shows that at least half these words have \(V_m\le C_*\) for one universal \(C_*\), independent of \(h,b,y\). In particular \(C_{\rm mid}/3^l\le C_*\).

Choose \(b\) once with \((2/3)^b(C_*+2)<1/32\). The initial normalized intercept is \(1-(2/3)^b\). The middle contributes at most \((2/3)^b C_*\) and the last one contributes at most \((2/3)^b\), since \(2^m/3^l=3^{-s}\le1\). Therefore \(31/32\le C_t/3^K\le33/32\), and (4) gives \(1/2\le a/Q<13/2\). The initial bit forces odd \(a\). The last bit is the \(K\)-th odd departure, so \(a\equiv2^{t-1}(2y-1)\pmod3\); this is a unit precisely for the claimed \(y\). Inverse binary branches on odd denominators realize the full specified parity word, and the positive source evolves through positive states. Its continuation to the census passes automatically. Different middle words give disjoint sources. Under the tilt each fixed initial and final one costs just the constant factor \(p^{b+1}\). Removing the tilt at length \(t\) as above and dividing by the upper count at \(n\) gives \(\gg(1+h)(1-p)^h\asymp w(y)\). This proves (1).

## What this measures on eventual ordinary trajectories

Let \(\mathcal E\) be the set of positive ordinary integers whose trajectories escape. Use the published verification below \(2^{71}\) and the [finite simple-path residue estimate](../OrdinaryGeodesic.lean). Every finite prefix from \(y\in\mathcal E\) has distinct states all at least \(2^{71}\), and hence
\[
        2^j T^j y < (3/2)3^{g_j(y)}y .
\]
For the protected first-clear clocks of (1), \((3/2)y/2^h<11\), so \(2^j\le2^h3^{g_j(y)}\) for every \(j\). These entire source families pass every continuation. The verification is the external input to this uniform assertion for every escaping \(y\); the preceding finite census law and (2) do not use it. [Bařina, The Journal of Supercomputing 81 (2025), article 810](https://doi.org/10.1007/s11227-025-07337-0)

There are absolute constants \(c',C'>0\) such that
\[
 c'\sum_{y\in\mathcal E}w(y)\ \le\
 \liminf_{n\to\infty}\inf_{L\ge0}P_{n,L}\ \le\
 \lim_{L\to\infty}\sup_{n\ge1}P_{n,L}\ \le\
 C'\sum_{y\in\mathcal E}w(y).                                         \tag{6}
\]
For the lower bound, sum (1) first over any finite set of eligible escaping targets. Different true first-clear integers give disjoint sources even when \(h\) differs. Pass to the full sum by monotone convergence. Each omitted large \(y\equiv2\bmod3\) gives the eligible \(2y\), still escaping and with comparable weight. Each of the finitely many \(y<Y_0\) can be doubled into \([Y_0,4Y_0)\) with eligible residue. The weight loss and these finite multiplicities are absorbed in absolute constants. For the upper bound first discard \(Y>R\) at cost \(C\sum_{y>R}w(y)\). For each \(y\le R\) the bank at its first clearance is at most \(1+p\log_2(2R)\). If it is eventually periodic its strict lap deficit defeats that bank uniformly in \(n\) by one sufficiently long continuation. Every remaining \(y\) is escaping and its mass is bounded by (1). Send \(R\) to infinity.

In particular, if some escaping ordinary input \(x\le B\) exists, then for all \(n\ge A'(1+\log B)^2\) and all \(L\ge0\),
\[
                      P_{n,L}\ge c''(1+\log B)B^{-\alpha}.             \tag{7}
\]
Take its protected first-clear target directly or after one of the bounded doubling repairs above. Its height is at most \(\max(4Y_0,2B)\), so the onset and weight follow from (1), enlarging constants to cover bounded \(B\). These absolute constants have not been numerically optimized or evaluated; (7) is an analytic finite implication. Establishing a smaller observed survival fraction uniformly in \(B\) remains open. The comparison controls the sum of positive weights of actual escaping integers and leaves nontrivial positive cycles to the separate subcritical criterion.

The [Lean interfaces](CriticalFirstClear.lean) check the first-clear residue obstruction and converse, the exact real interval margins, and automatic passage from clearance to the census clock. The cyclic path count, marked estimates and population inequalities are written proofs. The [checker](check_critical_first_clear.py) enumerates all positive-surplus binary words and all their cyclic offsets through length 12 using exact integer inequalities, scans every reduced source at three complete depths, and executes two prescribed long positive histories to their actual first-clear targets. [Retained exact output](CRITICAL_FIRST_CLEAR_CONTROLS.json)
