# The least bad integer and both neighbors of each bounded cycle phase

Write $C(n)$ when the positive integer $n$ reaches 1 under the shortcut map $T(2v)=v$, $T(2v+1)=3v+2$. Call such an integer good. If there is a counterexample, let $q$ be the least positive odd integer with $C(q)\ne C(3q)$. The pinned minimum theorem proves that $q$ is good, $3q$ is bad, and every positive multiple of three below $3q$ is good. The bounded alternative of the separate excursion theorem has $q>3$, $q\equiv1\pmod{12}$, and $s=(3q-1)/2$ is itself the minimum of a nontrivial positive odd cycle. Every odd phase $x$ satisfies $s\le x<8q$ and $2^a x'=3x+1$ with $a\in\{1,2\}$. The number $3q=2s+1$ merges with the cycle; it cannot itself be an odd phase because the odd map never outputs a multiple of three. [Minimum and orientation](https://github.com/GettysburgResearch/collatz/blob/26f070c38ad9edd21ed7dac6efaab6554550c2a3/research/astra-minimum-source-20261124/README.md) · [Bounded and first-crossing alternatives](https://github.com/GettysburgResearch/collatz/blob/32d722c5d5597846da5dad842c8ea15742abc176/research/astra-fixed-target-closure-20261124/ordinary/README.md)

## Global floor in both alternatives

**Every positive bad $n$ has a positive bad multiple of three at most $2n+1$.** Consequently
$$2n+1\ge3q,$$
also for an orbit in the first-crossing alternative. In the bounded alternative **$s$ is the least positive bad integer over all components**.

One may prove the witness assertion by descent. Halve an even $n$. An odd $n\equiv2\pmod3$ has the smaller ordinary predecessor $(2n-1)/3$. A multiple of three is its own witness. For odd $n\equiv1\pmod3$, $n>1$, either $n$ merges with $(n-1)/2$, giving a smaller bad input, or it merges with $2n+1$, a multiple of three. The latter odd-run comparison follows upon writing $n+1=2^m b$ with $b$ odd and $R=3^m b$. When $R\equiv1\pmod4$, the paths from $n,(n-1)/2$ reach $R-1,R/3-1$ after $m,m-1$ shortcuts respectively; two further shortcuts on either path give $(R-1)/4$. When $R\equiv3\pmod4$, apply the first case to $2n+1$, whose run parameter is $3R\equiv1\pmod4$. All steps preserve the same ordinary component. The least bad triple bound now gives the inequality, and $s$ attains it on the bounded cycle.

The comparison with allowance $3u\le2n+1$ is already explicit in the primary literature; the resulting sharper minimum is used here in place of the earlier pinned $8n+1\ge9q$ bound. The Lean module proves the odd-run comparison, performs the decreasing induction and applies it to the actual hitting predicate from its definition. [*Sharp time and height bounds for tripling comparisons in the Collatz graph*, §2](https://rstation.ai/problems/collatz/papers/228/v1) · [GlobalFloor.lean](GlobalFloor.lean)

## The neighboring values and the closed list of tripling disagreements

**Theorem.** For every odd phase $x$ of the bounded bad cycle, the three integers $x-1$, $x+1$ and $2x-1$ are good. The lower neighbor $x-1$ was known in the pinned work. [Prior lower-neighbor proof](../../astra-global-closure-20261124/round9/critical/README.md)

To see the upper-neighbor assertion, put $G(x)=(x+1)/2$. On every exponent-one edge write $x=4u-1$, so $x'=6u-1<8q$. Then $3u\le4q$ and $2u+1<3q$ since $q>3$. The global floor makes $u$ good, and hence $G(x)=2u$ is good. On an exponent-two edge, $x=8v+1$, $x'=6v+1$, and $G(x)=4v+1$ reaches $G(x')=3v+1$ in two shortcuts. Follow exponent-two edges until the first exponent-one edge: the former strictly decrease $x>1$, so the latter exists. Thus $G(x)$ and $x+1$ are good everywhere. This argument only needs an infinite bounded path with the indicated physical edges and lower bound $x>1$.

Finally $T(2x-1)=3x-1=2^a x'-2$. For $a=1$ its label is the label of $x'-1$, and for $a=2$ it is the label of $2x'-1$. The same decreasing-edge argument proves that $2x-1$ is good.

**All run entries now give oriented tripling disagreements.** At each maximal odd-run entry $w$, write $w+1=2^m b$ with $b$ odd. The run has $m$ consecutive odd shortcut inputs and a single even input. Its next entry $z$ satisfies $2z+1=3^m b$. Along the odd sites $T^j w=2^{m-j}3^j b-1$, $0\le j<m$, the good upper neighbor proves that every $3^j b$ in this range is good. In particular $q_z=(2z+1)/3=3^{m-1}b$ is good. At $z$ the next run has a singleton exit, so the run comparison gives $z\sim2z+1$; thus $3q_z$ is bad. The entry ceiling $z\le6q$ puts $q\le q_z\le4q$, and $z=s$ yields the minimum $q$.

Writing $q_w=(2w+1)/3$, $t=v_2(3q_w+1)=m+1\ge2$, the entries obey
$$q_z=3^{t-2}U(q_w),\qquad v_3(q_z)=t-2,\qquad q_w\equiv1\pmod4.$$
The actual ordinary odd step is from $q_w$ to $U(q_w)=b$ in $t$ shortcuts. The multiplication by $3^{t-2}$ records the additional good levels of that tripling list. This gives a closed list of actual oriented disagreements at the cycle entries, but those multiplications are not ordinary edges.

[GoodNeighbors.lean](GoodNeighbors.lean)

## Native inverse-clock minima at every low-band phase

Write $x=2^j z_r$ at a phase of dyadic band $j\in\{0,1,2\}$ and normalized rank value $s\le z_r<2s$. A native segment of odd length $k\ge1$ from $x$ to $y$ has total clock $A$. Any positive ordinary path of the same odd length to the same $y$ has source $v$ and clock $B$. All its sites lie in the bad component. Whenever
$$k\le 3s\log(2s/z_r),$$
one has
$$ B\ge A-j,\qquad 3\mid v\ \Longrightarrow\ B\ge A-j+1.\tag{1}$$
Indeed the product of the native edge equations gives $2^A y/3^k\le x\exp(k/(3s))\le2^{j+1}s$. The competitor has $v<2^B y/3^k$, since each edge correction is strictly positive. Saving $j+1$ clocks would make $v<s$. Saving $j$ clocks from a triple would make $v<2s+1=3q$. Both contradict the corresponding global floor.

At all sufficiently large bounded candidates, the earlier rank estimate gives $\lvert\log(z_r/s)-(r/p)\log2\rvert\le\delta$, where $0<\delta<(\log2)/(2p)$. Thus $\log(2s/z_r)\ge(\log2)/(2p)$ uniformly in $r$, and (1) holds at **every** starting phase for **every** $k\le(3\log2/2)s/p$. In particular every native window beginning in band zero is an actual minimum-clock path through this range, which eventually contains arbitrarily many complete laps: the pinned bounded-cycle period estimate is $p\ll s^{49/100}$, so $p^2/s\ll s^{-1/50}$. [Pinned period estimate, §4](https://github.com/GettysburgResearch/collatz/blob/32d722c5d5597846da5dad842c8ea15742abc176/research/astra-fixed-target-closure-20261124/ordinary/HEIGHT_STRIP.md#the-exceptional-cycle) [Rank and pair estimates](../../astra-global-closure-20261124/round13/cycle/README.md) · [Earlier all-window comparisons](https://github.com/GettysburgResearch/collatz/blob/0e313e2cd42cfce1275dbef6129ac13e9a49abd5/research/astra-diagonal-closure-20261125/cycle/README.md)

The 41-phase rational control has no positive fixed-denominator ancestor below its numerator minimum in any of its 1,681 windows through one lap. The exhaustive test searches for the first offending reverse edge. If one occurred at depth $k$ with numerator $v<S$, its preceding sites would all be at least $S$, and $3v+d\ge2S$ would put every forward departure at least $(2S-d)/3$. The edge product would therefore give $2^E y(2S-d)^k<S(6S)^k$. This finite integer bound on the clock covers all first violations. The replay visits 6,886,529 nodes. This finite result allows stronger rational-basin controls to survive the new ordinary floor at one lap. It does not establish any convergence coloring on that large rational lattice.

A second search places an upper ceiling of $100000S$ on **every** intermediate numerator, permits arbitrary odd depth, and grows the complete inverse graph from all 41 phases until no new site remains. Its 823,827 sites have minimum $S$ and minimum multiple $2S+d$. Paths leaving the ceiling are outside this census. On this same rational example every $c_i-d$, $c_i+d$, $2c_i-d$, and every good entry/tower mark converges to a single other cycle of minimum numerator 10,875,918,040,073. The two smaller rational controls with $(d,p)=(13,5)$ and $(1631,8)$ also satisfy these common-reference comparisons, with respective good cycle minima 1 and 6625. For $d=13$ the positive reduced numerator 7 reaches 1 while 21 reaches a cycle of minimum 131, so the common reference for the marks does not supply the ordinary least-disagreement hypothesis at the claimed larger minimum. [Exact control and full numerical results](../../../reports/astra-unconventional-20261126/cycle/control.json) · [Earlier small-denominator census](../../astra-global-closure-20261124/round12/cycle/BASIN_CONTROL.md)

The bounded ordinary cycle and the first-crossing alternative remain open. The tripling disagreements can recur at many distinct values above their minimum, and (1) does not force a more efficient competing path to exist.
