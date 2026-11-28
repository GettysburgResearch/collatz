# Logarithmic capacity for simultaneous Collatz fusion

**Status.** Proposed written proof, conditional only on an explicitly cited scalar theorem. The central compression estimate is elementary. The growing-family bound improves the fourth-power logarithmic upper bound in Weaver, Paper 124/v1, to the order of the existing lower bound. The result supplies actual common futures in long intervals. It does not prove that two prescribed positive components meet.

## The population and the estimate

Use the shortcut map \(T(x)=x/2\) on even inputs and \(T(x)=(3x+1)/2\) on odd inputs. For Haar \(x\in\mathbb Z_2\), start the \(D\) arms \(x+d\), \(0\le d<D\). Write \(q_j(y)\) for the odd count before shortcut date \(j\). Let \(T_D\) be the first shortcut date at which all arms have both equal values and equal odd counts. This agreement persists at all later dates.

**Theorem 1.** There is an absolute constant \(C\) such that for every \(D\ge2\) and integer \(t\ge0\),
\[
 \Pr(T_D>t)\le \min\{1,C(1+\log D)/\sqrt{t+1}\}.                 \tag{1}
\]
For \(0<p<1/2\), it follows that \(\mathbb E T_D^p\ll_p(1+\log D)^{2p}\). The fixed-family coefficients \(\kappa_D=\lim_{t\to\infty}\sqrt t\,\Pr(T_D>t)\) consequently satisfy \(\kappa_D\asymp\log(2+D)\), using the known existence theorem and logarithmic lower bound. Weaver's Brownian lower comparison at time \(u(\log D)^2\) shows that (1) also attains the correct order of the growing-family time scale.

The imported scalar estimate is the remaining-absorption theorem of David Leen, *Exact rates in Collatz synchronization*, restated as (3) in Lyapunov Weaver, *Synchronization of growing Collatz blocks and selected references*, version 1. Fix any \(0<\alpha<1\). For a Haar lower arm \(y\) and upper arm \(3^k y+c\), started at effective odd grades differing by \(k\ge0\), the remaining counted-fusion time satisfies
\[
 \Pr(\tau>s)\le A_\alpha(1+k+(|c|/3^k)^\alpha)/\sqrt{s+1}.     \tag{2}
\]
Here \(c\) is any integer and time counts shortcut iterations. The estimate is uniform in the specified canonical state. We use (2) on individual prefix cylinders. No independence between different pairs is used. [Leen, 9 October 2026](https://doi.org/10.5281/zenodo.23268751) · [Weaver, §Scalar inputs, equation (3), lower comparisons, and prior family bound](https://rstation.ai/problems/collatz/papers/124/v1).

## Residuals and lattice packing

Expose the first \(j\) low binary digits of the *one original source*, writing \(x=r+2^j z\), \(0\le r<2^j\). Conditional on this cylinder, \(z\) is Haar. Every arm then has a fixed odd grade \(q\) and endpoint
\[
             3^q z+c,\qquad c=T^j(r+d)\in\mathbb Z .
\]
Identical pairs \((q,c)\) have fused throughout the cylinder. Retain one representative per distinct pair. Associate to it the real number
\[
                      R=c-3^q r/2^j.                               \tag{3}
\]
At \(j=0\), \(R=d\ge0\). If the next source digit is \(e\), then \(r'=r+2^j e\). The arm parity is \(b=(3^q e+c)\bmod2\). The new grade and constant are
\[
 q'=q+b,\qquad
 c'=\{3^b(3^q e+c)+b\}/2 .
\]
Substitution into (3) gives the exact update
\[
                  R'=(3^bR+b)/2 .                                 \tag{4}
\]
In particular all residuals stay nonnegative. For each individual retained arm, \(b\) is fair over the two refinements because \(3^q\) is odd. Different arms use the same digit \(e\) and need not have independent parities.

At any fixed grade \(q\), the retained residuals are distinct members of the unit-spaced translate \(\mathbb Z-3^q r/2^j\). Define
\[
 W_j=\sum_{\rm retained}(1+R^\alpha),\qquad N_j=\#\{\text{retained labels}\}.
\]
For each \(H\ge1\), grades range from \(0\) to \(j\), so counting points with \(R<H\) and then those with \(R\ge H\) gives the pathwise inequality
\[
 N_j\le(H+1)(j+1)+H^{-\alpha}W_j .                               \tag{5}
\]
This uses the actual integer intercepts. A collection of independent real affine paths would lack the packing bound at one grade.

By concavity and (4),
\[
 \mathbb E((R')^\alpha\mid r)
     \le \chi R^\alpha+2^{-1-\alpha},\qquad
 \chi=\big[(1/2)^\alpha+(3/2)^\alpha\big]/2<1 .
\]
Strict concavity applied to the two slopes of mean one gives the strict inequality. Removing duplicate labels at the next date can only reduce the sum of nonnegative weights. With \(B=1+2^{-1-\alpha}-\chi>0\),
\[
 \mathbb E(W_{j+1}\mid r)\le \chi W_j+B N_j
     \le \rho W_j+B(H+1)(j+1),\qquad \rho=\chi+BH^{-\alpha}.
\]
Choose a fixed \(H\) large enough that \(\rho<1\). For a fixed \(\alpha\), e.g. \(1/2\), all constants now are absolute. Iteration and \(W_0\le 2D^{1+\alpha}\) give
\[
       \mathbb E W_j\le 2\rho^jD^{1+\alpha}
                  +\frac{B(H+1)}{1-\rho}(j+1).                    \tag{6}
\]
Thus for an integer \(m=\lceil C_0\log(2+D)\rceil\), with \(C_0\) a sufficiently large absolute constant, \(\mathbb E W_m\ll m+1\). The exponential number of original paths is compressed in expectation to logarithmically many distinct integer labels, including the cost of their residuals.

## Joining the retained arms

Condition on the common length-\(m\) prefix. Sort the retained labels by nondecreasing grade, breaking ties by their integer intercept. Consider two consecutive labels \((q_i,c_i),(q_{i+1},c_{i+1})\). Write \(k_i=q_{i+1}-q_i\). Their conditional lower endpoint \(y=3^{q_i}z+c_i\) is Haar, and their upper endpoint equals
\[
        3^{k_i}y+c_{i+1}-3^{k_i}c_i .
\]
Its normalized offset is bounded by
\[
 |3^{-k_i}c_{i+1}-c_i|
    =|3^{-k_i}R_{i+1}-R_i|\le R_{i+1}+R_i.                        \tag{7}
\]
Agreement of every consecutive pair by the same deadline forces agreement of the whole family by persistence and transitivity. Apply (2) to each pair and use a union bound. The grade gaps telescope to at most \(m\); each residual occurs in at most two comparisons. Consequently
\[
 \Pr(T_D>m+s\mid r)\le A_\alpha(m+2W_m)/\sqrt{s+1}.
\]
If only one label remains, the left side vanishes. Taking expectation and using (6) proves (1) when \(t\ge2m\); below that range the trivial probability bound suffices after increasing the absolute constant. Splitting the tail integral at \((1+\log D)^2\) yields the asserted moments. The capacity and time-scale lower bounds are the cited outside results.

## Ordinary sources and the global boundary

The event of collective counted fusion by date \(t\) depends only on the residue of the original start modulo \(2^t\). Equal grades give identical slopes on the entire cylinder, so a counted fusion is a genuine equality for *every* positive integer completion. On any interval of \(X\) consecutive positive integer anchors,
\[
 \frac{\#\{n:T_D(n)>t\}}X
  \le \frac{C(1+\log D)}{\sqrt{t+1}}+\frac{2^t}{X}.              \tag{8}
\]
In particular \(\log D=o(\sqrt{\log X})\) permits simultaneous counted fusion of *every* member by \(\lfloor\delta\log_2 X\rfloor\) on density one for any fixed \(0<\delta<1\). They then agree on the ordinary, unshortened clock by date \(2\lfloor\delta\log_2 X\rfloor\), since passing \(t\) shortcut steps consumes \(t+q_t\le2t\) unshortened steps and common grades synchronize those clocks. The fixed-horizon lower comparison transfers exactly to complete binary periods. At the critical square-root spatial logarithm the generic failure probability cannot uniformly tend to zero for deadlines of this order.

Equation (8) permits arbitrary selection of offsets **inside** this one interval, even after observing all the starts. For a fixed positive-density target event on the anchor, divide its error by the lower bound on that event's frequency. It gives no prescribed absolute location of an ancestor of 1 within a given block. In particular the indicator of visiting 5 has a genuine defective edge at 5, two positive lower-density colours, and satisfies the same large-block constancy on strictly native horizons: a path from a large source cannot yet have reached the defect by a fixed fractional binary horizon. Exact integration of low-height information is still needed to obtain a full component merger.

**Repository comparisons.** PR217 at `3d700eaf6aac6617cab81b59cbeb8f75c5d38aaf`, `research/astra-collision-factor-bridge-20261128/collision/DYADIC_BOUNDARY_ZERO_ONE.md`, treats the summable adjacent discrepancy criterion. PR219 at `b1f2276c45218b0a05a6c4c0e413fec1e4e4dd46`, `research/astra-wild-nine-hour-20261128/dynamics/ORDINARY_COLOUR_OBSTRUCTION.md`, distinguishes precritical constancy from full invariance. Neither comparison is used in (3)–(7).

## Finite verification

[BlockResidual.lean](BlockResidual.lean) has five locally compiled public roots for the true integer parity update, fair two-digit comparison, scaled residual transport, offset cancellation, and lattice spacing. The strict check used Lean 4.34.1 (commit `5045d0056413266e57c625dcd7c365b10e377c52`) with `-DwarningAsError=true` and only the standard library. The five axiom reports use subsets of `propext`, `Classical.choice`, and `Quot.sound`. No formalization of (1), (2), or (6)'s probabilistic iteration is claimed.

[check_growing_blocks.py](check_growing_blocks.py) passed in both normal and optimized Python modes with the same output. The deterministic replay covers 60,556 individual digit residual updates, 6,132 complete child label sets, 11,543 grade lists, 12,264 integer packing bounds, 27,212 sorted offset cancellations, 3,066 grade telescopes, 3,066 two-child rounded-weight drifts, and 9,198 whole-block lifts at positive ordinary source tails.
