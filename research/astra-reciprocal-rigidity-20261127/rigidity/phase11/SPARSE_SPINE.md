# What all-clock population estimates can distinguish

This comparison uses a different computable map on ordinary positive integers. Its exceptional ray is explicit. The purpose is to test a proposed inference from first-passage budgets and population estimates to strict positivity at an individual source. The comparison gives no counterexample to the Collatz map itself.

## A sparse change which preserves almost every complete trajectory

Let $T$ be the true shortcut map. Choose an odd multiple of three $z_0\ge 105$. Recursively let $z_{j+1}$ be the smallest odd multiple of three at least $T(z_j)=(3z_j+1)/2$. Define $S=T$ except for $S(z_j)=z_{j+1}$. At each altered edge $1\le S(z_j)-T(z_j)\le5$. All $z_j$ are computable, strictly increasing at least geometrically by factor $3/2$, and are odd. Membership in the altered set can be decided by generating it up to the tested input. The orbit of $z_0$ under $S$ escapes.

For the true map, the complete predecessor set of any $3\mid y$ is exactly $\{2^i y:i\ge0\}$. An odd departure always has successor congruent to 2 modulo three, and repeated even inverses preserve divisibility by three. Consequently the complete $S$-orbit and $T$-orbit starting at $n$ coincide whenever
\[
                  n\notin B=\{2^i z_j:i,j\ge0\}.
\]
At a first altered departure the preceding itinerary is still the true one, proving this claim in either direction. Members of $B$ follow their even prefix to the marked odd vertex and then stay on the new spine. No start outside $B$ enters $B$, by the same predecessor description applied before its first visit. In particular $B$ is one entire escaping component of $S$, with
\[
                      \#(B\cap[1,X])=O((1+\log X)^2).
\]
Taking $z_0$ above any prescribed finite list of seeds preserves their entire original trajectories, even if their eventual fates are unknown. All first-crossing counts of that fixed list at **every** threshold are therefore identical. Every natural-density statement about the complete forward trajectory of a single source retains its value, whenever that density exists, since the exceptional sources have density zero.

## An optional component with positive lower density

To test arguments also using positivity of a component's basin, choose a fixed large $a=(4^e-1)/3$ with $3\nmid e$. It is an odd positive ternary unit, and its true first step is $2^{2e-1}$ followed by the powers of two down to 1. Take $z_0$ to be the least odd multiple of three at least $T(a)$, and additionally set $S(a)=z_0$. Every altered edge still differs from its true step by at most five, and the true standard cycle stays intact. By choosing $a$ above the peaks of any finite collection of verified convergent starts, the modified map preserves all their complete verification traces.

The exact forward-exception set in this version is contained in $B\cup\{n:T^j n=a\text{ for some }j\}$. Every true predecessor of $a$ outside $B$ reaches $a$ along its original path and then escapes under $S$. If the true predecessor set of $a$ has positive lower natural density, the exhibited escaping component therefore has positive lower natural density. The only external predecessor-positivity premise enters here. The same premise for 5 gives a positive-density family still reaching 1. Indeed choose $a>8$; no true predecessor of 5 can pass through $a$ before 5, since the true future of $a$ contains only powers of two after its first step. After 5 its true future avoids $a$. Removing $B$ still leaves the same positive lower density. [Mazur's predecessor-positivity result, with source and scope in the existing packet](../phase7/SHORT_WINDOW_CLOCKS.md)

The positive-density version makes no claim that almost every individual *complete forward trajectory* is unchanged. The finite original clocks and arbitrary visitor clocks below still have the same population limits.

## Arbitrary smaller visitors to a finite original deadline

Fix a shell $X\le n<2X$, an original deadline $d\ge0$, and any designated subset $\mathcal M(n)\subseteq\{1,\ldots,n-1\}$ of potential visitors. Use the same subset in both maps. It may be the set of all smaller positive integers or the singleton $(n-1)/2$ on an odd-source cylinder. The event being compared is
\[
       \exists m\in\mathcal M(n),\ b\ge0:\quad T^b m=T^d n,
\]
and its version with $S$ everywhere. An earlier hit on the original prefix is equivalent to hitting its endpoint, since the visitor may continue forward. Its clock $b$ has no cutoff.

Assume $d\le(\log_2 X)/90$ and $X$ is sufficiently large, depending on $a$ when it is present. A source $n$ outside $B$ cannot encounter $a$ in its first $d$ steps in this shell, as $n\le2^d a$ would be necessary before the two maps first differ. Thus outside $B$ the original target $Y=T^d n=S^d n$ and its entire prefix agree, and $Y\le Z=2^{d+1}X$. Both maps obey $S(x),T(x)\le2x$ for our large altered sites.

If the membership of the visitor event differs, choose an affirmative witness on one side. Its forward path under the two maps must disagree before it reaches $Y$ on that side. At its first altered departure it is either at $a$ or at $z_j$. In the latter case the prior path was true and $m$ is a dyadic multiple of $z_j$, so $z_j\le m<2X$. For a lost true hit, $Y$ belongs to the original forward path of $a$ (a fixed finite set, only in the optional version) or to the true forward paths of one of the $O(1+\log X)$ marked $z_j\le2X$. For a gained hit, $Y$ belongs to the new spine after its first altered departure, giving $O(1+\log Z)$ possibilities through $Z$. This argument applies to the symmetric difference even though there may be many candidate witnesses and their clocks can be arbitrarily late.

The true complete forward path from any one positive seed has at most $O(Z^{39/40}(1+\log Z))$ distinct values through $Z$, with an absolute constant. To see this, apply T-A3-651 to distinct odd states up to the first repeat, or to every finite prefix of a simple infinite path. This gives at most $5 Z^{39/40}$ odd values. Every even value at most $Z$ is a dyadic multiple of an odd value in this same complete path through $Z$, and each odd value admits at most $1+\lfloor\log_2 Z\rfloor$ such lifts. The sum counts distinct values only. [Finite-path packing T-A3-651, equation (1)](../../../astra-three-routes/pass3/FINITE_RECORDS.md)

It follows that the number of possible symmetric-difference targets is $O(Z^{39/40}(1+\log Z)(1+\log X))$, plus a fixed finite set. On any one true $d$-letter binary cylinder the ordinary map $n\mapsto T^d n$ is injective, being affine with positive slope. The two maps' cylinder assignments themselves can differ only on the short-prefix exceptional sources already counted. The true shell has $X/2^d+O(1)$ starts per cylinder, and a modified cylinder differs by at most $O((1+\log X)^2)$ starts. Therefore the difference in relative event proportions, uniformly over these cylinders and choices of visitors, is
\[
 O\left(X^{-1/40}2^{(1+39/40)d}(1+\log X)^2\right)
         =O\left(X^{-11/3600}(1+\log X)^2\right).                    \tag{1}
\]
The fixed finite set is absorbed for all sufficiently large $X$. A union over all earlier deadlines costs at most another factor $d+1$, since on a fixed full cylinder each earlier endpoint is also injective. For fixed $d$, summing shells gives zero difference in the corresponding natural-density limits. For $H\le(\log_2 X)/120$, $6(t+1)\le H$, the whole $O^Hw$ experiment with $|w|=t$ lies within (1). The error is smaller than $(t+1)^{-1/2}$. Thus the growing-shell upper and lower first-smaller-meeting estimates of the existing packet persist for this genuinely escaping nearby map. [Ordinary all-clock post-ascent estimates](../../descent/postpeak/stopped/SYNCHRONIZATION.md)

## Loss of fixed-source positivity

Continue to use $a_0(x)=1/2,3/2$ according to the departing parity when forming prefix products; this symbol is separate from the optional special source $a$. The marked ray has product $(3/2)^t$ through every $t$ consecutive edges. For a lower gate cutoff tending to infinity, every initial finite segment of that ray is eventually below every gate. Hence the stopped squared-reciprocal envelopes tend to zero at the **fixed ordinary input** $z_0$. They do the same at $a$ in the positive-density variant.

The basic gate construction and its small weighted losses are available on the perturbed graph as well. Every step is at least $a_0(x)x$, since each modification was upward; true cycles outside the ray retain their strictly contracting slope product, and a path meeting the ray never cycles. First crossings of thresholds by an initial list of seeds are decidable by a finite search, exactly as in [the genuine-map proof](../phase9/ESCAPE_FLUX.md). For explicit constants use integer thresholds $R_k=\lceil(7/4)^k\rceil$ starting sufficiently high. Every departure above 100 increases height by at most factor $8/5$, and a first crossing of a sufficiently high threshold must depart above 100. Thus $R_k\le y\le(8/5)R_k<R_{k+1}$ for a crossing $y$, and $(8/5)R_{k+1}/R_k<3$. At a gate the ordinary slope product through the next gate is bounded by the maximum height divided by that gate height, giving squared positive log defect at most $2\log3$. Off gates the stopped-maximum recurrence gives zero positive defect. Taking the first $\min(k,F(k))$ seeds at each level for any nondecreasing computable $F\to\infty$ gives a strictly positive bounded computable envelope, with positive-power Dirichlet defect sums tending to zero as lower levels are deleted. Its fixed-source limit still vanishes on the planted ray.

These conclusions establish a limitation on deductions based on the cited population measurements, gate costs, and checked finite traces. The true affine step, in particular its exact output modulo three at every individual odd multiple of three, forbids the altered edges. The argument gives no embedding of the modified ray into genuine Collatz dynamics and no conclusion about the fate of a genuine unverified seed.
