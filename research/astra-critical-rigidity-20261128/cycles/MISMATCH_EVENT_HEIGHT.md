# Mismatch dates carry unbounded logarithmic height on every ordinary rotation

**Proposed deduction from the exact open endpoint theorem.** On a primitive positive rational odd cycle let \(p\) be the odd period, \(q\) the full reduced denominator, \(x_i=y_i/q\) the odd phases, and \(e_i\) their native valuations. For a proper lag \(\ell\), let
\[
 B_\ell=\{\,i+1\bmod p:e_i\ne e_{i+\ell}\,\},\quad s=|B_\ell|,\quad
 \mathcal H_\ell=\sum_{b\in B_\ell}
       \log_2[(y_b+q)(y_{b+\ell}+q)] .
\]
The heights here are sampled **after** the unequal edges. The budget \(s\) may increase without bound. The following statements use the actual odd phases and complete denominator of one cycle throughout.

1. Uniformly on growing positive ordinary cycles, with no assumptions on the rotation, height spread, or locations of the mismatches,
   \[
                         \min_{0<\ell<p}\frac{\mathcal H_\ell}{p}
                                     \longrightarrow\infty.              \tag{1}
   \]
   In particular \(s\log_2(1+\max_i x_i)/p\to\infty\) at *every* lag, with the same uniformity. The event-height sum provides a more precise necessary condition when the largest values are rare.
2. For positive rational cycles, on every sequence of proper lags on which \(s=o(p)\) and \(\mathcal H_\ell=O(p)\),
   \[
                   \liminf\frac{s\log_2 q}{p}\ge\frac14 .                \tag{2}
   \]
   Consequently, for every **fixed** budget \(s_0\ge1\), every primitive positive rational family with some proper lag of at most \(s_0\) mismatches satisfies
   \[
                   \liminf_{p\to\infty}\frac{\log_2 q}{p}
                                      \ge\frac{1}{4s_0}.                  \tag{3}
   \]
   Indeed the bound \(\mathcal H_\ell=O(p)\) holds for bounded \(s\) whenever \(\log_2 q=O(p)\). At \(s_0=6\), (3) gives a coefficient \(1/24\). The period onset for a specified strictly smaller coefficient remains ineffective.
3. Write \(m=\min_i x_i\). Suppose the logarithmic height above the minimum has bounded mean,
   \[
                         \mathcal A=\sum_{i=0}^{p-1}\log_2(x_i/m)=O(p).
   \]
   Growing ordinary cycles in this class obey the stronger lower rate
   \[
                    \min_{\ell\ne0}\frac{s(\ell)\log_2 p}{p}
                                    \longrightarrow\infty.               \tag{4}
   \]
   This permits isolated peaks of superpolynomial height. On rational cycles in the same class, along any sequence with \(s(\log_2 q+\log_2 p)=O(p)\), conclusion (2) holds. For example, if \(\log_2 q=o(\log p)\) then (4) follows on this class as well. The area and the event heights are explicit restrictions when used in these consequences. No positive density of mismatches at every lag of an unrestricted cycle follows from (1).

## An exact count of overlapping mismatch intervals

For each fixed integer \(k\ge1\) and \(\epsilon>0\), the open endpoint theorem gives a finite \(C(k,\epsilon)\) on two unmatched positive trajectories with at most \(k\) unequal odd valuations in \(L\) steps:
\[
 (1-\epsilon)L\le H_{\rm start}+h_{\rm end}
                       +4(k+1)\log_2 q+C(k,\epsilon).                    \tag{5}
\]
Here \(H_t\) and \(h_t\) are respectively the larger and smaller of the two logarithms \(\log_2(y_{t,j}+q)\). The true terminal date in (5) is essential because a final division can be arbitrarily large. This input also applies to an interval wrapping a periodic trace several times: its two tracks remain distinct at each common date by the proper rotation and primitivity. [Exact open endpoint theorem, (1)–(3)](../ordinary/EXACT_ARC_ENDPOINTS.md) · [Physical open-path and large-denominator proof](../ordinary/OPEN_ARC_MISMATCHES.md)

List \(B_\ell\) in increasing cyclic order \(b_0,\ldots,b_{s-1}\) and extend by \(b_{j+s}=b_j+p\). Here \(s>0\) because a proper period of the valuations would repeat its positive affine block and its physical state. For each \(0\le j<s\), take the actual synchronized paths from date \(b_j\) through date \(b_{j+k}\). The unequal departures are \(b_{j+1}-1,\ldots,b_{j+k}-1\), exactly \(k\) counted with multiplicity. This remains correct for \(k>s\). Their lengths sum to \(kp\), since each cyclic gap occurs \(k\) times. Their starts run once through \(B_\ell\) and so do their terminal dates, in permuted order. Adding (5) over these \(s\) intervals proves the finite inequality
\[
 (1-\epsilon)kp\le
      \mathcal H_\ell+4(k+1)s\log_2q+C(k,\epsilon)s.                    \tag{6}
\]
The parameter \(k\) is a fixed **local** mismatch budget, chosen independently of the cycle's possibly increasing total \(s\). The constant is never applied at a growing budget.

## The two orders of limits

For (2), pass to a subsequence attaining the lower limit, the case of infinite lower limit being immediate. Write \(\mathcal H_\ell/p\le K_0\) there. Divide (6) by \(kp\), first let \(p\to\infty\) with \(k,\epsilon\) fixed, and use \(s/p\to0\). This gives
\[
             1-\epsilon\le K_0/k+4(1+1/k)\liminf s\log_2q/p .
\]
Now take \(k\to\infty\), then \(\epsilon\downarrow0\), proving (2).

For (1), a contrary sequence of lags has \(\mathcal H_\ell=O(p)\). Least ordinary minima tend to infinity along growing periods because every specified positive minimum determines only one forward orbit. Each of the \(s\) summands is at least \(2\log_2(m+1)\), so \(s=o(p)\). Then (2) contradicts \(q=1\). This choice of an offending lag on every candidate gives the stated uniform minimum. The peak corollary follows from \(\mathcal H_\ell\le2s\log_2(1+\max_i x_i)\).

For (3), work on a contrary subsequence with \(\log_2 q=O(p)\). The real minimum has \(\log_2(m+1)=O(\log(p+1))\), by the same actual lap product and published two-logarithm estimate as in the arbitrary-cluster proof; \(m<1\) needs no estimate. Shifted one-step growth gives
\[
              \max_i\log_2(y_i+q)\le\log_2 q+\log_2(m+1)+(\gamma-1)p,
                   \qquad\gamma=\log_2 3 .
\]
Hence bounded \(s\) gives \(\mathcal H_\ell=O(p)\) and \(s=o(p)\). Applying (2) gives (3). Equivalently one can use a \(K\)-fold traversal of a primitive pair as two open paths with \(Ks_0\) mismatches, fix \(K\) before the period limit, and then let \(K\) grow. The native period remains the original \(p\). [Minimum and original all-fixed-budget theorem](ALL_FIXED_ROTATION_DENOMINATORS.md) · [Bondareva, Luchin and Salikhov, Theorem 1](https://doi.org/10.22405/2226-8383-2018-19-1-15-25)

For (4), on every rational orbit one has
\[
 \mathcal H_\ell\le
       2s[\log_2q+\log_2(m+1)]+2\mathcal A,                              \tag{7}
\]
because \((x+1)/(m+1)\le x/m\), and each of the two lists of sampled origins is a subset of the full cycle. Thus bounded area and \(s(\log_2q+\log_2p)=O(p)\) imply \(s=o(p)\) and \(\mathcal H_\ell=O(p)\), proving the rational consequence. If (4) failed at \(q=1\), the same conditions would imply (2). For \(\log_2q=o(\log p)\) a sequence violating (4) would likewise have \(s\log_2q/p=o(1)\).

## Relation to the previous height bounds

The [elementary mixed-divisor occupation theorem](ROTATION_OCCUPATION.md) supplies a finite bound of order \(p/s\) on the average numerator bit length, and hence a constant lower bound on \(s\log(qX)/p\) with \(X=\max_i x_i\). Equation (1) forces a diverging cost already at the post-mismatch dates of arbitrary ordinary rotations. The [balanced-minimum theorem](BALANCED_MINIMUM_ROTATIONS.md) yields a constant \(p/\log p\) rate under a large harmonic-minimum ratio; bounded logarithmic area here yields a diverging multiple even with isolated high peaks. The [arbitrary-cluster theorem](ALL_FIXED_ROTATION_DENOMINATORS.md) established an explicit positive rate per fixed mismatch budget using one pair of complete laps. Repeated application of the stronger two-path endpoint estimate yields (3), and (2) covers selected growing budgets. The additive constants in (6) are not effective in \(k\), so the speed of divergence in (1) is not determined here.

[Exact event checker](check_mismatch_events.py) · [Finite receipt](mismatch_event_controls.json). It replays 16,620 actual windows on 172 primitive positive rational cycles, including 5,836 windows longer than a full lap, checks the physical endpoint products over 4,152 window systems, and verifies the multiplicative form of (7). The asymptotic implications use the separate open endpoint theorem.
