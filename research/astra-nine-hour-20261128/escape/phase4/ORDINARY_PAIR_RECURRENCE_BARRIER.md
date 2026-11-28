# Infinite affine-pair recurrence fails on some terminating ordinary pairs

The [affine-pair return theorem](AFFINE_PAIR_RETURNS.md) has a genuine ordinary obstruction even among parameters where **both arms reach one**. There exist fixed positive odd integers \(A,B\), \(B/A\notin3^{\mathbb Z}\), such that the set of positive \(n\) satisfying all three properties below has positive **upper** natural density.

* Both \(A n\) and \(B n\) reach the cycle \(1,2\).
* \(F_t(A n)\ne F_t(B n)\) for every sufficiently large physical date \(t\), with the cutoff allowed to depend on \(n\).
* As a consequence, the corresponding true positive trajectory has only finitely many of the equal-grade bounded-offset returns which occur infinitely often at Haar-almost every dyadic parameter for these same two slopes.

Here \(F_t\) is the number of odd departures through \(t\) shortcut steps. This obstruction uses positivity of the convergence basin, original-residue equidistribution for that basin, and symbolic counted absorption at powers of three. It does not assume existence of an escaping source.

Let \(B_1\) be the complete basin of one with natural density \(p>0\). For each fixed positive odd \(a\), the proportion of \(n\le X\) with \(a n\in B_1\) tends to \(p\). Indeed the ordinary indicator at adjacent starts agrees outside relative frequency \(o(1)\), by true adjacent fusion, since both the start and its actual future have the same complete component. Grouping into consecutive blocks of length \(a\) gives original residue classes the same asymptotic conditional proportion. This also follows from the original-AP comparison in the [moving-clock theorem](../phase2/MOVING_CLOCKS.md). Positivity is a genuine ordinary predecessor input. [Mazur's fixed-target positive-density source](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/)

Take many fixed powers \(1,5,\ldots,5^{K-1}\), with \(Kp>2\). The number of successful starts among \(5^i n\) has limiting mean \(Kp\). Its second factorial moment is bounded below by the square of its mean minus its mean. By a finite union there are \(i<j\) and a sequence \(X\to\infty\) where a positive proportion of \(n\le X\) have both \(x=5^i n\) and \(w=5^j n\) in \(B_1\). No convergence of the individual pair correlations is needed.

The two starts \(w,9w\) have a symbolic same-clock merger for all but \(o(X)\) of these original parameters, using the finite resonant absorption theorem with initial ternary level two. At that merger and thereafter,
\[
                F_t(9w)=F_t(w)-2.
\]
The equality follows by comparing the affine lift slopes at the symbolic merger: the starting slopes in variable \(w\) are 1 and 9, and the physical denominators agree. This uses the proof's absorption at matched level and zero offset, rather than an accidental point meeting. Sampling \(w=5^j n\) preserves complete dyadic residue blocks because \(5^j\) is odd; alternatively for these fixed coefficients bound the failures by those on the full interval through \(5^jX\). [PR146, Theorem (1) and the symbolic oriented process](https://github.com/GettysburgResearch/collatz/blob/0410811710af2f7da71522ec67233528048adb9a/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md)

For each successful parameter beyond the negligible failures, \(9w\) also reaches one. At all sufficiently late dates \(x,w\) follow the physical two-cycle. The difference \(F_t(w)-F_t(x)\) then takes either one value or two consecutive values, since it has period two and the two alternating odd indicators differ by at most one. It cannot include both 0 and 2. Therefore either the pair \((x,w)\) eventually avoids equal grades, or the pair \((x,9w)\) eventually avoids them. A further finite union gives one fixed pair with positive upper density of the claimed ordinary failures. Both slope ratios are powers of five times a ternary power and are nonresonant.

The result does not assert positive upper density for the particular pair \((n,5n)\). It refutes a general density-one transfer of **infinite** dyadic equal-grade recurrence for all nonresonant odd slope pairs, using only terminating positive trajectories. For every fixed lower date, the forward finite prefix finding a return beyond it still has ordinary density one by the dyadic theorem. The two statements have different quantifier order.
