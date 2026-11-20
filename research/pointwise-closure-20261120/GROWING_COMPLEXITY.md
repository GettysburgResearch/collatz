# A growing popcount threshold on every distinct ordinary orbit segment

**PROPOSED, elementary.** For every fixed `0<c<1/sqrt(2)`, there is a constant `delta_c>0` such that, among any `N` pairwise distinct consecutive positive odd Collatz states, all but

\[
 O_c\!\left(N\,2^{-\delta_c\sqrt{\log_2N}}\right)
\]

have **more than `c sqrt(log_2 N)` set bits**. The constants are independent of the initial value and the location of the segment. This is a restriction on long distinct segments, including long terminating ones. It does not establish universal termination or exclude all cycles.

This proof uses no S-unit theorem. The finite homogeneous spectrum in `SPARSE_RETURN_SPECTRUM.md` gives a complementary, sharper result for a *fixed* popcount cap, `O_S(N^(1-1/S))` without logarithmic losses. Its S-unit cardinality constants are unnecessary for the growing-cap result below.

## 1. Exact all-N inequality

Use the odd map

\[
 U(n)=\frac{3n+1}{2^{v_2(3n+1)}},
 \qquad s(n)=\operatorname{popcount}_2(n).
\]

Let `S>=2`, `m>=3`, `N>=1` be integers. Put

\[
 L=2^{m-2},\qquad
 B_S(m)=\sum_{i=0}^{S-2}\binom{m-1}{i},
\]

where a binomial coefficient is zero when its lower index exceeds its upper index. If `x_0,...,x_(N-1)` are pairwise distinct positive odd states on one actual forward orbit, then

\[
 \boxed{
 \#\{0\le j<N:s(x_j)\le S\}
 \le \sum_{r=1}^{S}(2L)^{r-1}
       +\left\lceil\frac NL\right\rceil
          \min\{L,B_S(m)\}.}                            \tag{1}
\]

No estimate is asserted for `m<3`. The cases `S=2` and `N<L` are included: `B_2(m)=1`, and the final reserved window may be truncated. For `S=1`, an odd one-bit integer is 1, so distinctness separately bounds its count by one.

### 1.1 Short gaps form a finite set

An odd integer with exactly `r` set bits is determined by its `r-1` successive positive gaps between set-bit positions, starting at position zero. If every gap is at most `2L`, there are exactly `(2L)^(r-1)` possibilities, regardless of the orbit. Distinctness therefore bounds the number of all such low-popcount states by the first term of (1).

### 1.2 A long gap preserves one actual upper block

Suppose a state `n` with `s(n)<=S` has an adjacent set-bit gap `d>2L`. Cut there:

\[
 n=2^D u+v,
 \qquad u,v>0\text{ odd},\quad 0<v<2^{D-d+1}.
\]

Follow the shadow odd orbit `v_j`, extending `U(1)=1` for this calculation, and let `A_j` be its accumulated valuation. The elementary recurrence

\[
 P_j=2^{A_j}v_j,\quad P_{j+1}=3P_j+2^{A_j},\quad
 0<P_j\le4^jv<2^D\qquad(0\le j\le L)
\]

proves, by induction on the actual valuations,

\[
 U^j(n)=2^{D-A_j}3^ju+v_j,
 \qquad 0<v_j<2^{D-A_j}.                              \tag{2}
\]

The binary blocks in (2) are disjoint. A time with full popcount at most S consequently has `s(3^ju)<=S-1`, because the lower block is positive. The actual source in (2) remains above 1. Thus the shadow continuation of 1 has not introduced a physical step after termination.

### 1.3 Count the relevant homogeneous residues

The order of 3 modulo `2^m` is `L=2^(m-2)` for `m>=3`. Indeed, for `k>=1`,

\[
 v_2(3^{2^k}-1)=k+2,
\]

by the difference-of-squares factorization and induction; an odd exponent gives valuation one. Since u is odd, the residues `3^ju mod 2^m`, `0<=j<L`, are therefore distinct odd residues.

An odd m-bit residue with at most `S-1` ones has its low bit fixed to 1 and at most `S-2` ones in the remaining `m-1` positions. There are exactly `B_S(m)` such residues. Reduction modulo `2^m` cannot increase popcount. Hence at most `min(L,B_S(m))` indices of the L-position window starting at n can have full popcount at most S. The same upper bound holds for a truncated window.

### 1.4 Scan without changing the source of a cut

Scan the given N-position interval in time order. At a sparse state with a gap greater than `2L`, reserve the next L positions, truncated only at the end, and resume scanning after them. Otherwise advance one position. Reserved starts are separated by at least L positions, so there are at most `ceil(N/L)` windows. Section 1.3 bounds every such window using its own actual original source and cut. Each sparse visit outside those windows belongs to the finite short-gap set in Section 1.1. This proves (1).

The argument does not require any distributional independence between windows. It also does not attach a decreasing rank to successive cuts.

## 2. Choose a threshold growing like sqrt(log N)

Fix `0<c<1/sqrt(2)`. Select real parameters

\[
 2c<\alpha<1/c,
 \qquad c/\alpha<p<1/2.
\]

These intervals are nonempty exactly because `2c^2<1`. For sufficiently large N set

\[
 X=\log_2N,\qquad
 S=\lfloor c\sqrt X\rfloor,\qquad
 m=\lfloor\alpha\sqrt X\rfloor.
\]

Then `S>=2`, `m>=3`, and `L=2^(m-2)<=N`. Dividing the first term in (1) by N gives

\[
 \frac1N\sum_{r=1}^S(2L)^{r-1}
 \le\frac{S(2L)^S}{N}
 =2^{-(1-c\alpha)X+O_c(\sqrt X+\log X)}.             \tag{3}
\]

This decays exponentially in X since `c alpha<1`.

For the window term, eventually `S-2<=p(m-1)`. With

\[
 H_2(p)=-p\log_2p-(1-p)\log_2(1-p)<1,
\]

the elementary binomial-tail inequality gives

\[
 B_S(m)\le\sum_{i\le p(m-1)}\binom{m-1}{i}
       \le2^{(m-1)H_2(p)}.
\]

To verify the inequality directly, for `i<=pM` the weight `p^i(1-p)^(M-i)` is at least `2^(-MH_2(p))`. Multiply each binomial term by that weight and bound the resulting partial binomial probability by one.

Since `ceil(N/L)<=2N/L`, the window term divided by N is at most

\[
 \frac{2B_S(m)}L
 \le4\,2^{-(m-1)(1-H_2(p))}
 =2^{-\alpha(1-H_2(p))\sqrt X+O_c(1)}.               \tag{4}
\]

Combining (3) and (4), for example with any fixed

\[
 0<\delta_c<\alpha(1-H_2(p)),
\]

proves the asserted bound after enlarging its constant for finitely many small N. An integer popcount is at most `c sqrt X` exactly when it is at most its floor S, so the claimed real threshold follows without a rounding ambiguity.

The coefficient `1/sqrt(2)` is the limiting coefficient allowed by this particular choice of gap count and residue entropy. No optimality assertion is made for the actual Collatz map.

## 3. Relation to the existing growing-run theorem

PR #145 at `dd245a712f985909f541590e3f6c179b7ba011e4`, `research/binary-run-occupancy/README.md`, Section 4, proves the corresponding conclusion for the **number of runs of ones**, for every coefficient below `1/sqrt(8)`. Its signed-boundary representation needs `2R-1` gaps for R runs. This note counts positive set bits directly and needs only `S-1` gaps for S bits, which permits coefficients below `1/sqrt(2)`.

Because popcount is at least the number of runs, the earlier theorem already implies a growing-popcount threshold with coefficients below `1/sqrt(8)`. The new statement doubles this limiting coefficient **for popcount**. It is not an improvement of the run-count threshold, nor does it dominate the prior theorem as a structural statement: one very long run has large popcount and only one run.

For fixed S, the finite-spectrum method in `SPARSE_RETURN_SPECTRUM.md` replaces the residue count by a constant and removes logarithmic losses from the uniform power saving. Its sharper Evertse cardinality dependence `log K_S=O(S^3 log S)` is useful quantitative information, but its direct fourth-root growing-cap corollary would be weaker than the square-root result already available. No such weaker corollary is advertised as an advance here.

## 4. Remaining boundary and checks

The finite inequality and growing threshold constrain any nonperiodic positive orbit, since its odd values are distinct. They also apply to every long first-hit path in the basin of 1. They do not force a trajectory to return to simple binary shapes, give a source-dependent maximum popcount, or exclude a large cycle by repeating its primitive tour. The global carry replacement budget remains open.

`check_growing_complexity.py` independently enumerates the two homogeneous odd residue cosets at the specified finite moduli, counts their sparse residues, replays actual separated odd trajectories, checks the exact finite inequality on distinct ordinary segments, and tests the small S/m boundaries. Its finite execution is evidence for the arithmetic and counting implementation, not a proof by enumeration of the asymptotic claim.

The separated-source arithmetic is credited to PR #141 at `5025ef464d4b6d4f4a412a3e33c3477de68dfa8b`, `research/ay-persistent-20261031/PROOF.md`, HC-2. The window strategy and residue-period entropy method are credited to the stated PR #145 packet. The changed gap count, popcount residue threshold and constant are proved explicitly above.
