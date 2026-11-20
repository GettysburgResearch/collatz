# Shifted smooth classes, critical defects, and five-times carry resets

**PROPOSED research with cross-agent review. Full Collatz convergence remains
open.** This packet pursues the remaining arithmetic, analytic, and merger
obligations against the frozen sources in [SOURCES.md](SOURCES.md). It adds
a complete restricted-class result and exact obstructions to several proposed
global extensions. The reviews reconstruct the arguments independently;
they are agent reviews, not external peer review or formal verification.

Use the positive shortcut map `T(n)=n/2` on evens and `(3n+1)/2` on odds,
and the positive odd map `U(n)=(3n+1)/2^v2(3n+1)`. A shifted value means
`n+1` for an actual odd orbit state. All the statements below concern
ordinary positive integers.

## A restricted convergence class is closed

[Shifted smooth cycles](SHIFTED_SMOOTH_CYCLES.md) proves that the only
positive odd cycle whose every shifted value has prime factors in `{2,3}`
is `{1}`. Write a shifted value as `2^s 3^t`, and compress the consecutive
valuation-one steps. They preserve `k=s+t` and end at `2*3^(k-1)-1`.
If the next shifted value is again `{2,3}`-smooth, its new index is
strictly larger whenever `k>=16`. A universal inequality proves this;
the complementary exact table `1<=k<=15` admits only the transitions
`4 -> 2 -> 1 -> 1`. The largest index on any finite cycle therefore
excludes every nontrivial cycle in this class.

The same elementary proof gives the exact seven odd starts that reach 1
without ever leaving this shifted class:

\[
\{1,3,5,15,23,35,53\}.
\]

Their longest path is `15 -> 23 -> 35 -> 53 -> 5 -> 1`.

The shifted-core S-unit argument below also excludes an infinite
nonperiodic orbit confined to this class. Combining the two results proves:

> If all sufficiently late shifted odd values of one ordinary orbit have
> prime factors only in `{2,3}`, that orbit reaches 1.

The elementary cycle and finite-basin theorems do not use an external
theorem. This eventual-confinement corollary explicitly uses Evertse's
S-unit finiteness theorem through SC3. Starting with a shifted-smooth
value is insufficient: for example, `17` has shifted value `18`, but its
next odd state is `13`, whose shift is `14`.

[Sparse smooth excursions](SPARSE_SMOOTH_EXCURSIONS.md) removes the need
to assume eventual confinement in advance. Let `C_N` count the visits
outside the class through odd time `N`, including that endpoint. Every
counterexample, whether nonperiodic or eventually in a nontrivial cycle,
must satisfy

\[
\liminf_{N\to\infty}\frac{C_N}{\log N}
\ge \frac{1}{2\log(\log_2 3)}.
\]

In particular, `C_N=o(log N)` is a sufficient convergence condition.
The finite-prefix argument is `D_N <= B_2 + 2 C_N`: only finitely many
defect edges can have both shifted cores equal to one, and each outside
vertex touches at most two other defect edges. The explicit defect clock
then gives the lower bound. Nontrivial cycles have a positive frequency
of outside visits by the cycle theorem. No corresponding upper bound
for arbitrary ordinary sources has been established.

## Results by route

| Route | Result established in this packet | Remaining global obligation |
| --- | --- | --- |
| Shifted arithmetic | At most `B_s=(9*2^35)^(27(s+1))` distinct defect transitions for each fixed ordered pair of shifted cores over a fixed pool of `s` primes containing 2 and 3. A simple orbit prefix satisfies `D_N <= B_s K_N^2`. Eventual confinement to finitely many cores forces periodicity. | Control continuing creation of new cores along one actual orbit; a finite-core exit is not a numeric descent. |
| Restricted cycle exclusion | The shifted `{2,3}`-smooth class has only cycle `{1}` and the seven-state within-class basin above. It has an explicit, enormous hit-1-or-exit deadline. | Prove a suitable confinement or return property for arbitrary sources, or exclude cycles in a broader class. |
| Arithmetic visit frequency | Every counterexample has the explicit logarithmic lower bound on outside-class visits above; a strict lower liminf, including sublogarithmic visit growth, implies convergence. | Obtain an upper bound for this unweighted count along one fixed actual source. |
| Harmonic endpoint | Exact relaxed-cone examples show the critical loss cannot be removed using doubling, variation and the stated interval bounds alone. | Use additional exact odd-branch invariance or another property specific to actual orbit labels. |
| Actual composition operators | Normalized odd-part cutoffs are common approximate invariants in `ell^p(N,1/n)`, `p=1,2`, for actual Collatz, doubling and tripling composition. The unnormalized cutoffs have actual Collatz harmonic defect tending to `log(2)/2`. | An estimate for the particular positive transported source can still hold; these approximate invariants do not settle that source-specific question. |
| Five-times merger | A compact 13-cell symmetric certificate is accompanied by an exact carry-reset family. A fully convergent example increases source height, first-hit time and odd-step count simultaneously. | Prove the directed forward-five implication, using a valid repayment path and a rank that survives its resets. |

Here `D_N` counts transitions with `v2(3n+1)>=2` and `K_N` counts distinct
shifted cores among **all** endpoints from time 0 through time `N`.
`B_s` is a uniform bound on the number of nondegenerate S-unit solutions,
not on their heights. Its astronomical size is not presented as a
performed computation.

## Reading order and review boundaries

1. [SHIFTED_CORE_TRANSITIONS.md](SHIFTED_CORE_TRANSITIONS.md) proves SC1--SC3,
   gives an elementary defect clock, and isolates an optional stronger
   consequence of the proposed PR145 compressed-word theorem.
   [BOUNDED_CORE_HORIZON.md](BOUNDED_CORE_HORIZON.md) proves SC4's explicit
   repeat-or-exit horizon.
   [REVIEW_SHIFTED_CORE.md](REVIEW_SHIFTED_CORE.md) checks the coefficient
   uniformity in the primary S-unit source, exact degeneracy, injectivity,
   endpoint convention, clock and optional dependency.
2. [SHIFTED_SMOOTH_CYCLES.md](SHIFTED_SMOOTH_CYCLES.md) adds SS1--SS4 and
   closes the restricted class. Its
   [independent review](REVIEW_SHIFTED_SMOOTH_CYCLES.md) checks the universal
   inequality, cycle compression, exact basin and same-horizon corollary.
   [SPARSE_SMOOTH_EXCURSIONS.md](SPARSE_SMOOTH_EXCURSIONS.md) and its
   [separate review](REVIEW_SPARSE_SMOOTH_EXCURSIONS.md) give the quantitative
   necessary frequency for both possible counterexample types.
3. [ENDPOINT_CAPACITY.md](ENDPOINT_CAPACITY.md) proves EC1--EC5, including
   a fixed real-valued example satisfying the stated progression bound.
   [Its review](REVIEW_ENDPOINT_CAPACITY.md) retains the distinction between
   relaxed constraints and exact Collatz invariance.
4. [CRITICAL_APPROXIMATE_INVARIANTS.md](CRITICAL_APPROXIMATE_INVARIANTS.md)
   proves CA1--CA3 for the actual operators on the explicitly named
   harmonic spaces. [Its review](REVIEW_CRITICAL_APPROXIMATE_INVARIANTS.md)
   checks the infinite inverse-fiber tails and the Hilbert-space conclusion.
5. [SINGLE_LAYER_FIVE.md](SINGLE_LAYER_FIVE.md) supplies the compact alternative
   certificate; [CARRY_DEBT_RESET.md](CARRY_DEBT_RESET.md) proves the reset
   family and its precise induction obstruction.
   [Their review](REVIEW_MERGER_REMAINS.md) checks all infinite affine lifts
   and the explicit physical controls.
6. [CLOSURE_ATTEMPTS.md](CLOSURE_ATTEMPTS.md) records failed arithmetic
   extensions, an exact family creating unbounded new core at division cost
   two, and the next unsupported inference in the shifted approximation route.

The 13-cell certificate is **not a new global reduction**: concurrent
PR157 already proves the stronger one-way forward-five basin criterion.
The packet credits that result and PR146's newer bounded-rank and Mersenne
reductions. No all-depth nonclosure claim is inferred from a failed compiler
or a finite search.

The final check also found concurrent PR158--160. Their physical return,
unshifted prime-support and critical-mass work is compared at exact heads
in [LATEST_COMPARISON.md](LATEST_COMPARISON.md). It does not close the
missing shifted arithmetic upper bound or universal five-times transport.

## Replay and evidence

Run the local exact replays from a complete checkout with Python 3.11+:

```bash
python -X utf8 -B research/source-rigidity-20261120/replay.py --receipt ../source-rigidity-replay.json
```

The driver runs each listed checker in normal and `-OO` modes and compares
its entire output with the frozen report. Checks use integer or rational
arithmetic, explicit failure branches, targeted literal trajectories and
corruption controls. The written proofs supply their infinite quantifiers;
finite agreement does not prove those quantifiers or the external theorem.

The separate repository gate is:

```bash
python -X utf8 -B tools/validate.py --regressions --receipt ../collatz-validation.json
```

It requires a clean complete checkout and verifies repository integrity
and its existing bounded regressions. It is not a mathematical proof.
Exact artifact hashes, actual replay results, and publication receipts are
under [reports/2026-11-20-source-rigidity](../../reports/2026-11-20-source-rigidity/README.md).

The first unresolved inference for unrestricted Collatz remains visible in
each route. No accepted-baseline registry status is changed by this packet.
