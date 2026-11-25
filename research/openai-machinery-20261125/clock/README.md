# An exponential bound for the forward clock on complete ordinary rows

**Status.** The finite-row inequality and ordinary witness family below are kernel-checked. The upper Banach density corollary follows by the written interval argument. The pointwise crossing requirement and the cycle test in PR 206 remain **OPEN**.

## Statement

Let $T(a)=a/2$ for even inputs and $T(a)=(3a+1)/2$ for odd inputs. Starting at a positive odd ordinary source $a$, let $S_k(a)$ be the elapsed shortcut time of its $k$th odd return. Here $S_0=0$. PR 206 calls the source crossing when some $k$ satisfies
$$
 (k+1)3^{6k}<2^{6S_k(a)}.
$$
Fix any $m,n\ge0$ and any odd stride $d>0$. Take the **consecutive representatives in that progression** given by $a_r=2(dr+m)+1$, $0\le r<32^n$. Setting $d=3$ fixes a single class modulo six. Write $F$ for the number failing the strict test at $k=3n$, including equality. Then
$$
 108^n F\le3125^n,\qquad \frac F{32^n}\le\left(\frac{3125}{3456}\right)^n .
$$
The estimate is uniform in both $m$ and $d$, including $d=3^h$ for arbitrary $h$. The map, the clock and the crossing predicate are imported from PR 206 at `b2b56b94175174a680a296478f16c619a8828972`. The six files in `pr206/` are byte-identical to their counterparts under `research/clock-itineraries/` at that head. These files are under this repository's existing MIT license. The estimate uses elementary integer arithmetic. The finite Fourier and tensor modules in the neighboring packets play different roles.

## Proof

1. For $t$ shortcut inputs let $J_t(x)$ count the odd ones. For every ordinary $d\ge0$, the two sources $x$ and $x+2^td$ have the same first $t$ input parities. Their endpoints differ by $3^{J_t(x)}d$. The theorem `ordinary_lift` proves the count and endpoint identities by induction on the first even or odd step. Thus an odd stride $d$ gives opposite endpoint parities on sibling lifts.
2. Weight a length-$t$ history by $2^{t-J_t}3^{J_t}$. When the row is lifted one bit, one sibling multiplies this weight by 2 and the other by 3. Therefore the total weight on the $2^t$ ordinary inputs $b+dr$ of any odd-stride row is $5^t$. The Lean statements `ordinary_pressure` and `rowSum_eq_range` establish the mass identity and identify its domain with the actual contiguous list of representatives.
3. A $t$-step history with $J_t\ge k$ has weight at least $2^{t-k}3^k$ when $k\le t$. For an odd input $a$, $S_k(a)\le t$ implies $J_t(T(a))\ge k$. Indeed the $k$th odd return contributes the last of these $k$ odd inputs in positions 1 through $t$. Positions before the first odd successor are even. The formal proof uses the exact PR 206 odd-gap equations. For $a_r$ as above, $T(a_r)=3dr+3m+2$, where $3d$ is odd.
4. Failure at $k=3n$ forces $S_k\le5n$, since $(3n+1)3^{18n}<2^{6(5n+1)}$. One integer proof uses $3n+1\le2^{n+1}$ and $2\cdot3^{18}<2^{30}$. Substitution into the weight bound gives $2^{2n}3^{3n}F\le5^{5n}$. See `clock_failure_bound` for the variable-cutoff inequality and `exponentially_sparse_clock` for the numerical specialization. The empty horizon $n=0$ is included.

**Written corollary.** Within either eligible class modulo six, the positive ordinary sources that *never* cross have upper Banach density zero, meaning the fraction in long intervals tends to zero uniformly in the interval start. Fix $n$ and partition any interval of $L$ consecutive representatives of the class into blocks of length $B=32^n$ and one shorter tail. The offset parameter $m$ allows the same estimate on every block. A never-crossing source fails the $3n$th test. Its fraction in the interval is consequently at most $(3125/3456)^n+B/L$. First take $L\to\infty$, then $n\to\infty$. No independence assumption about successive states of a fixed orbit is used.

## What finite transfers leave open

For every $K$, the actual positive source $a=6\cdot2^K-1\equiv5\pmod6$ has $S_j(a)=j$ for all $0\le j\le K$. Each of those tests fails. Indeed the source $2^{K+1}u-1$ moves in one odd gap to $2^K(3u)-1$ as long as $K>0$. This is the formal theorem `arbitrarily_long_failure`. Also 1535 and 3071 share residue 511 modulo 512 and residue 2 modulo 3. Both have eight unit odd gaps. At return ten the elapsed times are respectively 19 and 11, giving opposite verdicts. Their finite comparison and `Proposal.Crosses 1535` are proved by kernel reduction. Finite survival of the second source does not assert infinite survival.

The missing assertion is that **every fixed** positive odd source in the two admissible classes has **some** crossing. A set of upper Banach density zero can contain specific ordinary integers. The other missing assertion is the arbitrarily late vanishing of the cycle witness test. Neither assertion follows from the bound. One sufficient next bridge would start with a single fixed never-crossing source and construct some $n,m,d$ with $d$ odd and more than $3125^n/108^n$ distinct representatives in that exact row failing that exact $3n$th test. The representatives can depend on $n$ and need only fail the one finite test. An inverse population at a different horizon or outside the row does not satisfy this requirement. The ordinary finite dyadic lift supplies no such lower bound.

## Attempt to connect the inverse renewal floor

An escaping ordinary ray has a minimum among the odd values on a tail that begins after at least one odd gap. The minimum is in one of the two admissible ternary classes, and its future cannot descend below it or reach a nontrivial cycle. PR 206's descent-or-cycle theorem then forces that specific source to fail every clock test. This implication is `minimum_tail_fails`. Positive upper Banach density of those minima, or of any family inheriting the same finite clock failures, is a further condition.

The conditional lower bound of PR 207 at `b56c4dc2c28a184cf55638bb80c49a9d4662fc81` counts sources $x$ of ordinary paths with $b$ odd returns, total clock $2b$, and terminal $q$ in a specified moving shell. The source-qualified renewal assumption F and the simple-path estimate S are inputs to that argument. The following checks use the actual ordinary path and need neither assumption.

* **Same horizon.** Every such $x$ for $b>0$ passes the $b$th strict clock test, since $(b+1)3^{6b}\le(2\cdot3^6)^b<(4^6)^b$. Thus the balanced lower population contributes exactly zero to the matched-horizon failure statistic. See `balanced_forces_cross`.
* **Later horizon.** For $j$ further odd returns, the same source clock is $S_{b+j}(x)=2b+S_j(q)$. Its exact failure condition is
  $$
  2^{12b}2^{6S_j(q)}\le (b+j+1)3^{6b}3^{6j}.
  $$
  Even knowing that $q$ fails its $j$th test only yields $2^{6S_j(q)}\le(j+1)3^{6j}$. This leaves the inherited exponential factor uncompensated. The Lean statement is `balanced_suffix_iff`.
* **Total available sources after the prefix.** Write $b+j=3n$. Failure gives $2b+j\le5n$ because every further gap costs at least one step. Hence $b\le2n$ and $j\ge n$. Enlarge PR 207's shell $q\le 2^{\lceil\sqrt b\rceil}$ to $q\le2^b$ for $b\ge1$. Positivity of the ordinary affine correction gives $3^b x\le4^bq\le8^b\le9^b$. Thus $x\le3^b\le9^n$ **across all these shells together**. There are at most $9^n$ distinct positive sources available even before row membership is imposed, whereas a contradiction from the clock estimate would require more than $(3125/108)^n$. The formal statements `balanced_failure_needs_suffix` and `aligned_balanced_height` give the index and height bounds. This argument addresses the original sources examined at or after the balanced prefix and leaves comparisons at earlier horizons open.
* **Earlier horizons in small shells.** For $n\ge9$ and $b\le9n$, the terminal bound is already $q\le2^n$, since $b\le n^2$. Then $x\le[2(4/3)^9]^n$ from the same affine estimate. The exact comparison $108\cdot2\cdot4^9<3125\cdot3^9$ implies that even the union across all these shells contains too few distinct originals to defeat the clock bound. This applies whether the $3n$th index is before or after the terminal. See `early_balanced_height`. More generally, with largest shell depth $B$, the necessary size condition is $(4/3)^B2^{\lceil\sqrt B\rceil}>(3125/108)^n$. At linearly growing comparable depths this requires a limiting ratio $B/(3n)$ of at least $\log(3125/108)/(3\log(4/3))\approx3.89905$. Cardinality alone still supplies no earlier-prefix failure or row localization at such depths.
* **Backward transport.** Every eligible odd target $q$ has a one-gap predecessor in its own ternary class with arbitrarily large first clock. Choose a compatible initial exponent from 1 through 6 by $q\bmod9$. Replacing $3x+1=2^e q$ with $3(64x+21)+1=2^{e+6}q$ preserves the source class. A sufficiently long first gap makes the predecessor pass **all** positive tests up to any specified horizon $K$, regardless of the subsequent common orbit. The kernel theorem `crossing_predecessor` establishes this for every eligible target. As a convergent ordinary control, $2389\mapsto7$ is a single odd gap of length 10, both starts are 1 modulo 6, and each reaches 1. At the third return, 7 has elapsed clock 4 and fails, while 2389 has elapsed clock 12 and passes. See `backward_transfer_control`.

A successful application of the renewal count at an earlier clock would need to select more than $(3125/108)^n$ **distinct original** sources in one row $2(dr+m)+1$ with $0\le r<32^n$, odd $d$, and $S_{3n}(x)\le H(3n)$ on that same source at $3n<b$. For asymptotically large horizons, shells bounded by $b\le9n$ have already been ruled out as a sufficient population. An alternative population outside the balanced construction could meet the same row target without a constraint on $b$. Neither the cardinality at moving terminals nor common forward basin membership supplies this time-localized lower bound.

## Executable checks

Run from the packet root with Lean 4.34.1 on PATH.

```sh
python -B clock/check_lean.py
python -B clock/replay.py --depth 64 --direct 8
python -O -B clock/replay.py --depth 64 --direct 8
```

The build checks each source hash, compiles all six prerequisites with fresh local objects, and compiles the new module with warnings as errors. The frozen `FixedGate.lean` produces one `if_false` deprecation on this compiler. The audit permits `propext` and `Quot.sound`, and additionally `Classical.choice` for the tail-minimum and matched-suffix theorems. The concrete source-pair controls use no axioms. The Python checks raise exceptions explicitly, including under optimization.

The finite replay uses the integer cutoff $H(k)=\lfloor\log_2((k+1)3^{6k})/6\rfloor$, computed with integer bit length. Every positive gap tuple of length $k$ and total $s$ selects one odd residue modulo $2^{s+1}$. Recursing backwards from an odd endpoint, a gap $e$ requires $3a+1=2^e y$; the odd multiplier 3 is invertible modulo the power of two, so an odd target cylinder lifts to one odd source cylinder. The tuples are disjoint by deterministic iteration. On a common row of $2^{H(k)}$ odd representatives this gives weight $2^{H(k)-s}$. To count histories failing *every* cut through $k$, accumulate multiplicities over predecessor clocks strictly less than the new clock and discard clocks above each prefix cutoff. To count the $k$th cut alone, use $\binom{s-1}{k-1}$ compositions. Direct enumeration independently applies the ordinary odd map on full joint mod-3/dyadic periods through the requested direct depth. At $k=8$ each class has 979 all-prefix failures and 2,380 last-cut failures out of 8,192. The exact row counts are finite arithmetic, distinct from the all-$n$ kernel theorem.
