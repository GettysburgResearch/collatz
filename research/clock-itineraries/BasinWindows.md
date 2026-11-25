# What a single convergent sequence of basin profiles would prove

Let $T$ be the positive shortcut map, let $f(n)$ be the indicator that $n$ reaches one, and put $F_X(t)=f(\lfloor Xt\rfloor)$ on $I=[1,2]$ for positive integers $X$. Endpoints of real intervals have measure zero throughout.

**Proposed written theorem.** Every strong $L^1(I)$ subsequential limit of $F_X$ as $X\to\infty$ is constant, with value zero or one. This assertion uses elementary measure theory and exact ordinary trajectories. With the published fixed-target positive lower density statement M, the following equivalence follows.

> Every positive integer reaches one if and only if $F_X$ has a strongly $L^1(I)$-convergent subsequence on one unbounded sequence of scales.

The scales may be chosen after looking at the profiles. PR #197 obtained strong convergence from summable errors between successive truncations in one ternary head. Here the two independent dilation directions come from actual trajectories at a single scale. The result requires neither a prescribed geometric sequence nor a rate for its convergence. The existence of a strongly convergent subsequence remains open. [PR #197 truncation argument](https://github.com/GettysburgResearch/collatz/blob/156652e03fe7a78f9cd4442039779cc622fdf3de/research/ayh-resource-reset-20261124/continuation/HEAD_EDGE_RIGIDITY.md)

## Integer rays force a constant limit

For $b,d,e\ge0$ and $m\ge2$, the two positive inputs

$$
       2^d(2^b m-1),\qquad 2^e(3^b m-1)
$$

meet after $d+b$ and $e$ shortcut steps. The first input loses $d$ factors of two and then makes $b$ odd shortcut steps. This identity also holds for any binary label constant along trajectories. [Lean proof](BasinTransport.lean)

Write the inputs as $Pm-A,Qm-B$ and set $c=Q/P$. Suppose $F_{X_j}\to g$ strongly. Choose a closed interval inside $I\cap c^{-1}I$, away from its endpoints. Select those $t$ there with $X_jt=Pm-A+u$, $0\le u<\eta=\min(1,1/c)/2$. The selection indicators have weak limit $\eta/P$ against integrable functions. Indeed, each period $P/X_j$ has exactly that fraction selected. Approximation by step functions gives the assertion for integrable tests.

On the selected set the exact ray identity gives

$$
       F_{X_j}(t)=F_{X_j}\big(ct+(cA-B)/X_j\big).
$$

Replacing both sides by $g(t)$ and $g(ct)$ costs $o(1)$ in the integral of their absolute difference. On the right this follows by a change of variables, strong convergence, and continuity of translations in $L^1$. The positive mask density therefore forces $g(t)=g(ct)$ almost everywhere on the overlap. Exhaust the interior by closed intervals. Reversing the comparison supplies reciprocal ratios. All ratios $2^z3^b$, $z,b\in\mathbb Z$, are thereby available. Their logarithms form a dense additive subgroup since powers of two and three are distinct. On the logarithmic interval, translation continuity extends the equality to every real shift on its overlap. Integrating over shifts gives equality at almost every pair of points. Thus $g$ is constant. Strong convergence of binary functions forces its constant value to be binary.

For either color, an octave containing $o(X)$ points of that color implies $o(X)$ points up to $X$ on the same scales. For each of the first $J$ lower dyadic intervals, doubling its members the requisite number of times injects them into $[X,2X$) with their label unchanged. The remaining part contributes at most $X2^{-J}+1$. Take $X\to\infty$ and then $J\to\infty$. The argument works with non-dyadic integer $X$.

Under M, the basin of one has positive lower natural density. If a bad trajectory exists, an odd unit on it has an ancestor set of positive lower natural density, entirely of the other color. Either constant limit would contradict one of these bounds. Universal convergence gives $F_X=1$ identically. M is used only at this last density step. Its external proof was not rebuilt here. [Mazur's exact fixed-target statement and release](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/)

## Quantitative comparison of moving windows

There is a second written result under the following separate input S. For a fixed block length $m\le4$, the fraction of binary classes of depth $h$ for which all $m$ consecutive affine profiles have failed to fuse by clock $h$ is $O(1/\sqrt h)$, uniformly over binary lifts. Equal profiles persist. We use the proposed bound (4) of the source, for its first group only. [PR #146 synchronization estimate](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/WHOLE_INTERVAL_SYNCHRONIZATION.md)

Let $\mu(J)$ be the empirical law of the forward component of a uniform integer in the interval $J$. Two starts belong to the same component when they meet, allowing unequal clocks. For $J=[u,u+L$), $L\to\infty$, S gives

$$
  \|\mu(J)-\mu(2J)\|_{\rm TV}
    +\|\mu(3J)-\mu(4J)\|_{\rm TV}=O(1/\sqrt{\log L})
$$

uniformly in $u\ge1$. To see this, take $h=\lfloor(\log_2 L)/2\rfloor$. Within each doubled pair use the exact step $2n\mapsto n$. In the blocks at $4n$ and $3n$, the centers $4n+1$ and $3n+1$ meet after two and zero clocks. If the entries in both small blocks have fused internally by $h$, all twelve pairings are actual meetings with clocks $h+2,h$. Uniform sampling of the child indices has the required uniform marginals. Sampling starts $2n,3n,4n$ costs a factor at most four in the binary-class bound and $O(2^h/L)$ at the interval edges. Rounding real endpoints costs $O(1/L)$. These couplings work simultaneously for every subset of components. [Finite physical identities](BasinTransport.lean)

For $0<w<1$, compare windows $[x,(1+w)x$) at any two starting points in $[X,2X]$. Let $p/q$ be a continued-fraction convergent to $\log_2 3$. Multiplying by three and dividing by two or four to stay inside the octave changes the law by $O(1/\sqrt{\log(wX)})$ per iteration, by the two estimates above. In fewer than $q$ iterations the orbit of the log phase comes within $2/q$ modulo one of any requested phase, by comparison with the equally spaced rational grid. At an octave boundary one extra doubling or halving fixes the wrap. Shifting the resulting window to the requested center costs $O(1/(qw)+1/(wX))$ in total variation, by counting its symmetric difference. Thus the discrepancy is

$$
       O\!\left(\frac{q}{\sqrt{\log(wX)}}+
                  \frac{1}{qw}+\frac{1}{wX}\right).
$$

If $w\to0$, comparison to the entire octave adds $O(w)$ by partitioning it into multiplicative windows and one residual interval. For every fixed $0<\sigma<1/2$, choose convergent denominators $q\to\infty$ and $X=\lceil\exp(q^\theta)\rceil$ with $2<\theta<1/\sigma$. For $w=(\log X)^{-\sigma}$ the discrepancy tends to zero, uniformly in the centers and component subsets, on these selected scales. With M, both colors under a counterexample occupy a proportion bounded away from zero in *every* such window. The lower bound in each entire octave follows from the preceding dyadic injection argument, applied by contradiction to a sequence of vanishing proportions. PRs #202 and #203 provide different fixed-target block results under their stated routing inputs. [PR #202](https://github.com/GettysburgResearch/collatz/blob/3b10b24d12d4b349cb20f4cbc83086c8a09f807e/research/synchronized-long-basin-blocks-20261124/README.md) · [PR #203](https://github.com/GettysburgResearch/collatz/blob/3f2c89f12b057b8bb8655bd6fc794c772aa8b65d/research/mixed-adic-basin-density-20261124/README.md)

## Why near invariance leaves a gap

For convergent denominators $q\to\infty$, consider the varying test colors $h_q(n)=\mathbf1_{\{q\log_2 n\}<1/2}$, with braces denoting fractional part. They are exactly invariant under doubling. On $X\le n<2X$ the odd shortcut step changes the phase modulo one by at most $1/q+O(q/X)$. The fraction of inputs in that distance of either color boundary is $O(1/q+q/X)$. To count them, use the log coordinate on one octave, whose Jacobian varies by at most a factor of two. There are $O(q)$ component intervals to round to integer endpoints. For $X=q^4$ these rescaled test colors tend weakly to $1/2$, by averaging the periodic square wave on the log interval. Their $L^1$ distance from $1/2$ is always $1/2$. Even arbitrarily small average shortcut errors permit arbitrarily fine oscillation.

The actual basin has exact trajectory invariance at every integer. A proof of strong compactness for its profiles on one sequence of large scales would settle the conjecture under M. The available adjacent mergers and the comparison of moving-window averages leave this step open.
