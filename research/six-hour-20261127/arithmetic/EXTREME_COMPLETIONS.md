# Two rotation numbers that must agree at an ordinary cycle

**PROPOSED.** A bounded positive integer cycle would survive two extremal monotone roundings on the entire surrounding octave. Its odd period and clock would give the same reduced rotation number for both. The computed strict inequality below covers a finite set of scales. At every large scale the two maps also have common exact paths of logarithmic length whose drift exceeds the minimum possible average drift of a physical cycle. These paths limit the use of bounded local corrections in a proof of universal strict inequality.

## The full ordinary grid

Choose an odd integer \(B>0\) and an integer \(B\le U<8B\). The normalized integer nodes are
\[
 \mathcal V=\{4B\le m<8B:\ c(m)=2^{v_2(m)}\le4,\quad B\le m/c(m)\le U\}.
\]
They represent all odd physical integers \(x\in [B,U]\) exactly once: \(m=2^j x\) for the unique \(j\in\{0,1,2\}\) that puts \(m\) in this octave. Extend the ordered grid by all dyadic scalings, and put
\[
 F(2^t m)=2^t(3m+c(m)),\qquad m\in\mathcal V,\quad t\in\mathbb Z .
\]
Inside the octave \(F\) is nondecreasing, since \(3(n-m)\ge3\ge c(m)-c(n)\) for \(m<n\). The first node is \(4B\) with \(c=4\). Every node below \(8B\) has \(3m+c(m)\le24B+1<2F(4B)\), giving the order across the seam. The same monotonicity for a true cyclic set of phases follows from the earlier dyadic inversion argument. The present grid includes all eligible integers, with possible plateaus. [Full dyadic cycle order](../../unconventional-20261126/adelic/DYADIC_CYCLE_ORDER.md)

Round \(F(v)\) to its nearest grid point from below for \(F_-(v)\), and from above for \(F_+(v)\), allowing equality in both cases. These maps commute with doubling and are nondecreasing. At normalized \(m\), choose \(b=\lfloor\log_2((3m+c(m))/(4B))\rfloor\). Then floor or ceil \((3m+c(m))/2^b\) to an eligible node. Rounding up to \(8B\) means the point \(4B\) in the next octave.

Let \(N=|\mathcal V|\). In increasing global grid indices a map \(f=F_\pm\) satisfies \(f(j+N)=f(j)+N\). Iteration modulo \(N\) eventually repeats; if a loop of \(p\) steps gains \(h\) octaves put \(\rho(f)=h/p\). This value is independent of the starting node. To see this for two cyclic nodes, choose representatives \(a\le b<a+N\). After a common multiple of their two periods their net gains, in octaves, are integers. Monotonicity traps the image of \(b\) between the images of \(a\) and \(a+N\). When \(a<b\) this forces the two octave gains to agree, and when \(a=b\) both gains describe the same position. The order gives \(\rho(F_-)\le\rho(F_+)\).

Any ordinary cycle entirely in \([B,U]\) has every native image exactly on the dyadic grid. Consequently **both rounded rotation numbers equal its native \(h/p\)**, where \(h=\sum_i v_2(3x_i+1)\) and \(p\) is its odd period. This also holds if two different bounded cycles fit inside the same \([B,U]\). Separation at one choice of \(B,U\) excludes every such cycle. No numerical estimate for an irrational logarithm is needed.

For the least-disagreement bounded alternative the upper ceiling is \(x_i\le(16s+7)/3\), \(s=\min x_i\). A single pair \(B,U=\lfloor(16L+7)/3\rfloor<8B\) tests all odd \(s\) in \([B,L]\). The exact control separates both rotations on 65 intervals covering odd \(3\le s\le1,000,001\). It computes one orbit in each finite rounded map by integer operations. This modest range is already covered by ordinary trajectory verification and is an independent test of the construction. At \(s=1\), both rotations really are \(2/1\). At \(B=9\) or \(11,\ U=8B-1\) both rotations are \(8/5\), although the grid contains no exact cycle. The replay checks every exact edge at these two false positives. Thus equality alone has genuine false positives in the larger monotone-support class. [Exact replay](check_completions.py) · [Output](COMPLETION_CONTROLS.json) · [Bounded alternative](https://github.com/GettysburgResearch/collatz/blob/51d97cbe17054415acaf95e422801a3532545033/research/astra-unconventional-20261126/cycle/CANONICAL_FLOOR.md)

## Long common paths at every scale

Take an odd \(s\) and \(B=s,\ U=\lfloor(16s+7)/3\rfloor\), with \(s>1\). For every \(L\ge1\) satisfying
\[
                      64(L+1)3^L\le s,                              \tag{1}
\]
both maps agree for \(L\) edges on a genuine ordinary path \(x_0,\ldots,x_L\) in the single band \([s,2s)\), where the normalized nodes are \(m_i=4x_i\). There are at least \(\lfloor s/[32(L+1)3^L]\rfloor\) choices of the initial source.

Write \(\gamma=\log_2 3\). The \(L+1\) points \(-j\gamma\bmod1\) for \(0\le j\le L\) leave an open circular arc of length at least \(1/(L+1)\). Its midpoint \(z\) has every \(\{z+j\gamma\}\) at distance at least \(1/(2(L+1))\) from either endpoint of \([0,1]\). Put \(A_j=\lfloor z+j\gamma\rfloor,\ b_j=A_{j+1}-A_j\in\{1,2\}\). Prescribing these \(L\) exact odd valuations puts the positive odd source in one class modulo \(2^{A_L+1}\le4\cdot3^L\). Indeed the odd terminal condition in the iterated affine equation specifies this unique class, or one may lift the prescribed parity bits successively.

Choose \(x_0\) in that class with \(|\log_2(x_0/s)-z|\le1/(8(L+1))\). The interval has length at least \(s/(8(L+1))\), since the derivative of \(2^u\) exceeds \(1/2\) there. The count follows. The homogeneous path for \(x_0\) has log heights \(\{z+j\gamma\}+\log_2(x_0/s)-z\), at least \(3/(8(L+1))\) from both cuts. The true affine recurrence adds to its \(j\)-th value
\[
      \frac13\sum_{i<j}3^{j-i}2^{-(A_j-A_i)} \le 2j/3 ,
\]
since each ratio equals \(2^{\{z+j\gamma\}-\{z+i\gamma\}}<2\). The extra log height is at most \(2L/(3s\ln2)<3/(8(L+1))\) by (1). Thus every site lies in the band, proving the claim at the actual scale. Earlier fixed-window CRT constructions additionally assure convergence of prescribed affine marks at *some* unbounded sources; the present elementary count places the long common paths at *every* scale satisfying (1). [Earlier two-sided finite windows](https://github.com/GettysburgResearch/collatz/blob/03b26119164664d08eaa04a1ea1d159dd4eccd7a/research/astra-six-hour-20261127/cycles/WINDOW_CONTROLS.md)

Let \(L\to\infty\) with (1). For each of these paths its scaled excess over homogeneous rotation satisfies
\[
 \frac{s}{L}\left(\log_2\frac{F_\pm^L(m_0)}{m_0}-L\gamma\right)
   =\frac{s}{L}\sum_{j<L}\log_2(1+1/(3x_j))
   \longrightarrow \frac{1}{6(\ln2)^2}.
\]
Uniformly, \(x_j/s=2^{\{z+j\gamma\}}(1+O(1/L+L/s))\). The irrational rotation averages \(2^{-v}\) uniformly over every starting \(z\), including the varying midpoints; this Riemann-integrable function has mean \(1/(2\ln2)\). Taylor's inequality for the small logarithms gives the displayed limit.

For example, any pathwise proof of an upper bound \(a<1/[6(\ln2)^2]\) on the lower map's scaled drift via
\[
 s(\log_2(F_-(v)/v)-\gamma)+P_s(F_-(v))-P_s(v)\le a
\]
at every grid node, with \(P_s\) invariant under doubling, needs oscillation \(\ge(1/[6(\ln2)^2]-a-o(1))L\). One can take \(L=(1-o(1))\log_3 s\) using (1). This applies to arbitrary such corrections, including ones that depend on residues or location. For a physical cycle the ceiling alone gives \(s(h/p-\gamma)\ge1/(16\ln2)-o(1)\). An upper rotation bound below that value would exclude all sufficiently large bounded cycles, but a uniformly bounded pathwise correction cannot establish it.

**First unsupported step.** No argument here separates the rotations for every large ordinary \(s\), or constructs a long-time lower orbit of sufficiently small average drift at every scale. The exact partial orbits above need not extend to periodic ones. The Lean file checks node monotonicity, equality of slopes for two periodic representatives of a monotone lift, and the telescoping cost of a correction. The grid construction, all-scale source count and asymptotic drift are written arguments. [Lean kernel](CompletionOrder.lean)
