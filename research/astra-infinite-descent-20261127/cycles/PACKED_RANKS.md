# Occupation, summed clock ranks and the width-three source count

Consider a nontrivial primitive positive integer cycle, with $m,p,h,g,a,b,\Lambda=h-p\gamma,W,K$ as in [the folded-rank argument](FOLDED_FAREY.md). Thus $m$ is the minimum, $p$ is the odd period, $a/b=h/p$ is in lowest terms, $g=p/b$ and $W$ is the spread of the integral levels $d_i=\lfloor ia/b\rfloor-E_i$ at the actual minimum cut. Let $\nu>4.116201$ and $\delta=1/(1+\nu)$. Set $\kappa=1-\ln6561/\ln8192$.

The once-around occupation estimate for a simple positive integer trajectory gives, uniformly in its least period,
\[
         \Lambda\ll m^{-\kappa},\qquad b\gg_\nu(pm^\kappa)^\delta,
 \quad
 K[W+\log(2p)]\gg_\nu
           \max\{(p m^\kappa)^\delta,m^\delta\}.                        \tag{1}
\]
Indeed take $k=\lfloor\log_{8192}m\rfloor$ in [CycleOccupation.logarithmic_gap](../root/CycleOccupation.lean) and divide the natural logarithm by $\ln2$. Its rate is $(6561/8192)^k$. The reduced two-logarithm bound $b^{-\nu}\ll_\nu (h-p\gamma)/g$ gives $b^{1+\nu}\gg_\nu p/\Lambda$. The positive-displacement inequality and the lower-convergent construction in [the folded-rank proof, equations (6)–(8)](FOLDED_FAREY.md) give $K(W+\log(2p))\gg_\nu(p/\Lambda)^\delta$. Use the occupation bound and the independent elementary bound $\Lambda\ll p/m$ to obtain (1). The positive displacement from that proof exists eventually because $b\to\infty$ and $\Lambda$ is bounded. Along growing distinct cycles $m\to\infty$. This use of integer occupation concerns the folded profile after all equal-rank visits have been added.

There is a second estimate for cycles of small width. Put $\lambda=h/p$ and $X=\max_{i<p}x_i$ over odd sources. At the minimum cut $d_0=0$, and the positive orbit product yields $\log_2(x_i/m)=d_i+\{i\lambda\}+\theta_i$ with $|\theta_i|\le\Lambda$. Thus $X\le 2^{W+1+\Lambda}m$. For
\[
 n=\max\!\left(1,\left\lceil(\log_2(X+1)+W+1)/\lambda\right\rceil\right)
\]
the $p$ length-$n$ native exponent words of the cycle are pairwise distinct. Indeed each has total exponent $T$ between $n\lambda-W-1$ and $n\lambda+W+1$ by the telescoped formula for $d$. Two equal words force the difference of the two corresponding odd integer sources to be divisible by $2^T$, greater than $X$. The sources would therefore coincide contrary to primitivity. This is valid even if $n$ exceeds the odd period. Counting positive compositions gives the finite bound
\[
               p\le\binom{\lfloor n\lambda+W+1\rfloor}{n}.             \tag{2}
\]

Suppose $p\to\infty$ with $W=o(\log p)$. Distinct sources give $p\le X$, hence $\log m\ge(1-o(1))\log p$ and $W=o(\log m)$ by (1). Since $\lambda\to\gamma$, (2) and the binomial entropy bound give
\[
             p\le m^{H_2(1/\gamma)+o(1)}.
\]
The general exponent here is already superseded by reported universal orbit-set packing, which gives an exponent below $H_2(\log_3 2)$. We include (2) to isolate exactly the finite injectivity argument and the combinatorial input that can be replaced at a prescribed width. [Weaver, Paper 145, prior orbit-set results and narrow-source comparisons](https://rstation.ai/problems/collatz/papers/145)

At $W\le3$, write $M_{256}$ for the certified maximum number of length-256 native grade paths on a fixed mechanical schedule in [the primary-spectrum transfer](PRIMARY_SPECTRA.md), and $\theta_3=\log_3(M_{256})/256=0.7980587\ldots<4/5$. For the fixed slope $\lambda$ a starting phase for the $n$ adjacent mechanical increments has at most $n+1$ possible schedules, by the circle cuts $-j\lambda\bmod1$, $0\le j\le n$. For each such schedule the $n+1$ native grades lie in a translated copy of $\{0,1,2,3\}$; translate all grades by their common minimum to see the same transfer constraints. The starting grade and these increments recover the exponent word from the grade path. The number of paths is at most $M_{256}^{\lceil(n+1)/256\rceil}$ by partition into 256-site blocks, with a shorter final block extendible along the native orbit. For all sufficiently large periods the slope lies in the certified open bracket used by that count. Equations (1)–(2) now imply
\[
 p\le m^{\theta_3+o(1)},\quad
 \Lambda\le p^{1-1/\theta_3+o(1)},\quad
 b\ge p^{1/[\theta_3(1+\nu)]-o(1)},\quad
 K\ge p^{1/[\theta_3(1+\nu)]-o(1)}.                                  \tag{3}
\]
The last two estimates also use $\Lambda\ll p/m$, and $W+\log(2p)=p^{o(1)}$. At the baseline two-logarithm bound (taking $\nu\downarrow4.116201$ in the limiting exponents), $m\ge p^{1.2530-o(1)}$ and the lower exponent for both $b$ and $K$ exceeds $0.2449$. All constants in the finite rank estimates may depend on $\nu$. These are necessary restrictions on ordinary cycles of width at most three. For widths one and two, Paper 145 gives stronger source-count estimates with additional harmonic analysis, and the prior phase-order theorem gives $g=1$.

The occupation inequality is imported from the packet's compiled Lean kernel. The transfer computation and entropy deductions are written results. The two-logarithm input is the homogeneous specialization of Bondareva, Luchin and Salikhov's Theorem 1. [Primary theorem (2018)](https://doi.org/10.22405/2226-8383-2018-19-1-15-25)
