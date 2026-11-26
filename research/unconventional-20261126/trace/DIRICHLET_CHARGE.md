# A damping sum rule and the first power of the raw cylinder trace

**Status.** Proposed, source-qualified. The sum of the escaping charges is represented both by an absolutely convergent positive ordinary series and by a renormalized harmonic sum of the original finite ternary cylinders. None of the identities establishes that the charge is zero.

**Prior-work correction after late intake.** [Weaver, Paper 176 v1, Theorems 1–2 and equation (6)](https://rstation.ai/problems/collatz/papers/176/v1) already proves the harmonic-head and stopping-loss formulas reconstructed here. These identities are not claimed as new. The explicit certificate of failure of global nonincrease and the companion reflection control are separate contributions of this packet.

Use the odd Syracuse map \(U(x)=(3x+1)/2^{e(x)}\), \(e(x)=v_2(3x+1)\), and put \(c(x)=3x/(3x+1)\). Let \(h\) be the ordinary Cesàro trace of the original Haar-normalized densities \(\rho_k\), with \(\rho_0=1\), and let \(b_C=\lim h(a_i)/a_i\) on an escaping component. Write \(c_*=\frac12\log(4/3)\). Then
\[
 \boxed{\ \sum_{a>0\ {\rm odd}}\frac{h(a)}{a(3a+1)}
       +\sum_{C\ {\rm escaping}} b_C = c_* .\ }                 \tag{1}
\]
In particular every finite subtotal bounds the total charge from above after subtraction from \(c_*\). Alternative positive finite cycles are included in the first term with their full lap multiplier.

For each \(k\) the periodic sequence \(\rho_k\) has mean one on the odd integers. Thus the following convergent, generally conditional Dirichlet constant is well-defined:
\[
 B_k=\sum_{a>0\ {\rm odd}}\frac{\rho_k(a)-1}{a}.
\]
It is a finite-cylinder observable; the sum can equally be evaluated by grouping one period and applying the digamma function. There are exact limits
\[
 B_{k+1}-B_k=c_*-\sum_{a>0\ {\rm odd}}\frac{\rho_k(a)}{a(3a+1)},
 \qquad
 \lim_{k\to\infty}\frac{B_k}{k}=\sum_{C\ {\rm escaping}} b_C.    \tag{2}
\]
Thus at the first power the raw trace has a linear background removed by ordinary harmonic centering. The right-hand side uses the charges themselves, without their higher moments. The proof of the increment is elementary and does not use existence of trace or basin densities.

### Loss along an individual orbit

For a positive ordinary start \(q\) use the shortcut trajectory, with an initial even halving chain carrying weight one. At step \(j\), let \(P_j\) be the product of all \(c(x)\) at odd states already left; take \(P_0=1\). The drop upon leaving an odd \(x\) is \(P_j/(3x+1)\). Consequently the sum of the drops is exactly \(1-P_\infty\). On a periodic component \(P_\infty=0\); on an escaping component it is the positive whole-orbit product \(W(q)\) used in [the physical current](ANNULAR_ESCAPE_CURRENT.md).

At an odd vertex \(a\), let \(w_a(q)\) be its weighted first hit and let \(\lambda_a=0\) if \(a\) is nonperiodic, or the product around its odd cycle otherwise. The total contribution of the drops at \(a\) from this source is
\[
 \frac{w_a(q)}{(1-\lambda_a)(3a+1)} .
\]
There is at most one visit off a cycle, and a geometric series of visits on a cycle. For a fixed \(a\) the ordinary natural source mean of \(w_a(q)\) is the physical \(D_a\); the canonical trace formula gives \(h(a)/a=c_*D_a/(1-\lambda_a)\). Multiples of three have zero trace. These are source-qualified inputs from Valbuena's pinned [basin article](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/tao-basin-densities.tex) and the same trace normalization as [the profile paper](ESCAPE_TRACE_PROFILE.md).

Here one may exchange the infinite target sum with the **limiting source mean**. For first visits above a height \(H\), the pathwise sum of drops is bounded by \(O(H^{-1/40})\), uniformly in the source, by the finite distinct-path reciprocal bound. Later visits occur only on cycles. Choose finitely many components whose complement has small limiting source mass; total-variation convergence of the empirical component law gives the same bound asymptotically for that complement. Above the largest cycle vertex of the selected cyclic components, all repeated-visit losses come from the complement and their sum per source is at most one. These two bounds give uniform tightness of the spatial loss distribution in the source limit. Finally the source means of \(1_{q\in C}W(q)\) converge to \(b_C/c_*\) in each escaping component by fixed-target truncation along its ray, as proved in (3) of the physical current. Finite-component truncation again justifies the sum. Averaging the pathwise loss identity now proves (1).

### The exact increment

At each odd endpoint \(a\), the forward transfer viewed as a sum over its actual positive odd parents gives
\[
 \frac{\rho_{k+1}(a)}{a}
   =\sum_{Ux=a} c(x)\frac{\rho_k(x)}{x}.
\]
Indeed \(3\,2^{-e(x)}/a=c(x)/x\). Every compatible inverse branch at a positive odd target gives a positive odd parent. At fixed \(k\) the sequence \(\rho_k\) is bounded and periodic modulo \(3^k\). Summing through \(a\le R\), subtracting the preceding row on the same range and sending \(R\to\infty\) yields
\[
 B_{k+1}-B_k
  =\lim_{R\to\infty}\sum_{x>0\ {\rm odd}}\frac{\rho_k(x)}x
       [\mathbf1_{Ux\le R}-\mathbf1_{x\le R}]
       -\sum_{x>0\ {\rm odd}}\frac{\rho_k(x)}{x(3x+1)}.
\]
The loss sum converges absolutely by boundedness at this fixed \(k\).

In the class \(e(x)=e\), the first bracket compares the cutoffs \((2^e R-1)/3\) and \(R\). This class is one odd residue modulo \(2^{e+1}\). By the Chinese remainder theorem the periodic coefficient \(\rho_k(x)\mathbf1_{e(x)=e}\) has mean \(2^{-e-1}\) on all integers. A bounded periodic sequence of mean \(m\) has harmonic sum \(m\log R+\text{constant}+o(1)\), by summation by parts. Hence the class contribution tends to \(2^{-e-1}(e\log2-\log3)\).

For \(e\ge2\) the interval contributes only positively for large \(R\). The first reciprocal in its progression is at most \(3/(2^e-1)\), since \(3x+1\ge2^e\); the rest is bounded by the integral of \(1/x\) over a ratio at most \(2^e\), divided by spacing \(2^{e+1}\). Therefore the class contribution is \(O(\|\rho_k\|_\infty(e+1)2^{-e})\), uniformly in \(R\). This permits summing over the exponents at fixed depth. The result is \(\sum_{e\ge1}2^{-e-1}(e\log2-\log3)=c_*\), proving the first equality of (2).

For the second equality use the source-qualified uniform domination \(\rho_k(a)\le B h(a)\) on positive odd units, \(k\ge1\). It follows from the canonical inverse kernel applied to the bounded observable \(\rho_1/h\) as in [the trace profile](ESCAPE_TRACE_PROFILE.md); its harmonicity holds at periodic units with the full trace. Both rows vanish at odd multiples of three. Fixed-root Cesàro convergence now passes through the absolutely summable majorant in (1). Telescope the first equality, divide by \(k\), and use \(B_0=0\). This identifies the complete limit. No estimate for a moving-root Cesàro error is required.

There is also a finite sum with ordinary rational coefficients and a known deterministic centering. Set \(Q=3^k\). On consecutive blocks of \(2Q\) integers, the odd subsequence of \(\rho_k-1\) has mean zero and absolute sum at most \(2Q\). Starting at odd \(a>2Q\), its partial sums are bounded by \(2Q\); Abel summation against \(1/a\) bounds that tail by an absolute constant, independently of \(k\). Since \(\sum_{a\le2Q,\ a\ \rm odd}1/a=\frac12\log Q+O(1)\), (2) gives
\[
 \lim_{k\to\infty}\left[\frac1k\sum_{\substack{a\le2\cdot3^k\\a\ {\rm odd}}}
             \frac{\rho_k(a)}a-\frac{\log3}{2}\right]=\sum_C b_C. \tag{3}
\]
This form scans one odd residue representative per class modulo \(3^k\). It requires no cycle detector. The baseline term is essential.

### A failed monotonicity shortcut

One might try to prove that every increment \(B_{k+1}-B_k\le0\). In fact \(B_{14}>B_{13}\). The integer-array checker [check_dirichlet_current.py](check_dirichlet_current.py) bounds \(\rho_{13}\) from above using fixed-point arithmetic. If the current column bounds \(2^{40}\rho_j\), take 50 exact legal transfer terms, round each quotient upward, and add \(\lceil2^{40}3^{j+1}2^{-50}\rceil\) for the omitted letter tail. The tail uses \(\rho_j\le3^j\), which follows from nonnegativity and total cell mass \(3^j\). For odd \(a\le3^{13}\) sum the rounded-up damping contributions. Beyond one period the remaining sum is at most \(2/(3\cdot3^{13})\), using the whole period mass and \(\sum_{j\ge1}j^{-2}\le2\). Finally \(c_*=\operatorname{arctanh}(1/7)>1/7+1/(3\cdot7^3)\). The exact positive margin is recorded by the checker. This finite obstruction does not establish a positive limiting slope.

An upper bound \(B_{k_j}=o(k_j)\) along some unbounded sequence would exclude all ordinary escape by (2) and positivity of each component charge. In (3) the required arithmetic estimate is an upper bound \((\frac12\log3+o(1))k\) on the actual harmonic head; the general total-mass bound only gives \(O(k)\) with a larger constant. Neither the local transfer nor the fixed-root trace law gives the sharp upper coefficient here.
