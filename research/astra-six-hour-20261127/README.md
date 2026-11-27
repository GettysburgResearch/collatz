# Ordinary clocks, actual good labels, and the global closure gap

**OPEN. This packet does not prove the Collatz conjecture.** It develops new exact ordinary mergers, proves a sharp limitation on their uniform clocks, and studies what actual convergence of neighboring trajectories forces on a hypothetical bounded cycle. A separate escape analysis obtains a height-to-entropy implication and a quantitative exclusion of growing parity blocks. The original global convergence consumers retain their explicit open premises.

Throughout, the shortcut map is

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

An odd departure counts once even when a later accelerated presentation combines several halving steps. “Good” means that the supplied positive ordinary source reaches one. A finite control constructed at a different source is not an orbit of the original source.

## 1. A sharp theorem about ordinary merger clocks

The remaining gap-six, three-odd canonical family on the bounded branch has

\[
j=11+162m,\qquad 81z+271=128\,2^j,
\qquad T^7z=2^j-1,\qquad T^j(2^j-1)=3^j-1.
\]

The preceding bounded-minimum argument supplies the conditional floor

\[
0<w,\quad1024w<243z\quad\Longrightarrow\quad \operatorname{Good}(w).
\]

At the original positive sources, both signs of the stabilized derivative now have a merger with the peak five exponents earlier. Their terminal blocks have **64 and 62 shortcuts**, respectively. The complete clock includes the preceding input-dependent perturbation segment. The smaller gap is paid by the stronger bounded-cycle floor.

For the supplied parameter \(m=b^{2^d}\), this proves the floor-conditional conclusion for **every base at \(d\ge494\)**, and for even bases already at \(d\ge63\). The odd-base branch uses the unconditional identity joining the peaks at exponents 173 and 164 after 499 postpeak shortcuts, with 241 and 250 odd departures.

The uniform-clock statement is sharp in a precise sense. Fix a positive degree \(n\), take **all positive odd bases** \(b\), and set \(j=11+162b^n\). Permit any earlier exponent \(1\le t<j\), the complete initial ascent on each Mersenne arm, and a common budget \(H\) for each arm's postpeak clock. The clocks may differ. Then

\[
\text{a finite uniform budget exists}
\quad\Longleftrightarrow\quad 2^{494}\mid n,
\]

and its least value is **499**. For every degree outside this class and every finite budget, arbitrarily large actual odd bases miss every allowed earlier arm. The proof constructs a rational binary control with a frozen carry, rules out all compensated savings by a complete 257-entry test, and lifts every required finite prefix to ordinary odd-base powers. A separation argument treats unequal clocks and both ascents. The lower bound does not assert failure of eventual convergence, and it does not bound a visitor allowed unlimited time.

All four new kernels, including the positive identities, elementary unequal-clock separation and the finite carry scan, have a fresh-project-cache replay. The infinite lifting and the full ascent separation have written proofs. [Ordinary packet](ordinary/README.md) · [Sharp statement and proof](ordinary/SHARP_ODD_POWER.md)

## 2. What good neighbors force on a bounded bad cycle

On the restricted bounded alternative, every odd phase lies in

\[
s\le x\le(16s+7)/3,
\]

and its native odd gap is one or two. The actual good marks include \(x-1,x+1,2x-1\), and the eligible tripled marks \(3x\).

An exact paired-word enumeration proves that **none of these four marks can reach one using at most fifteen odd departures** at a bad phase. It exhausts 128,545,757 search nodes and directly checks every surviving ordinary candidate. The Python engine and a separately written C++/GMP affine-carry engine agree on all nodes, depth bounds, candidates, hitting clocks and grades. This is an independently replayed exact computation, not a claim that the entire enumeration is formalized in Lean.

More generally, every fixed upper odd budget, and every fixed zero-entropy finite-state upper language, is excluded beyond a computable phase bound. The proof combines a signed rational critical-strip exclusion with a finite tree argument. The rational-strip kernel is formalized. A quantitative version forces at least \(\log_2^*s-O(1)\) odd departures at each applicable good mark.

A stronger population statement uses a supplied irrationality bound for \(\log_2 3\): almost every phase needs a positive multiple of \(\log s\) upper odds and evens during its first \(\log_2s\) shortcuts. The numerical constant \(1/20\) uses the source-qualified 2026 exponent-three result; a smaller positive constant follows from classical finite irrationality bounds. That literature-dependent input has not been rebuilt here.

The distinction between finite local data and an actual repeated cycle is essential. Every compatible finite two-sided window, including its good neighboring labels, has unbounded ordinary convergent controls. The packet constructs and replays 645 simultaneous marked starts on a 129-phase window. These controls never provide the missing bad repeat. [Cycle packet](cycles/README.md)

## 3. Arithmetic restrictions on one escaping orbit

The escape packet proves the following written implications and provides finite Lean kernels for the growing-block calculation.

* **Height and entropy.** For one injective ordinary shortcut orbit, an empirical parity limit has entropy at least \(\pi_B/B\) bits when \(\pi_B\) is its limiting upper fraction of observations below the polynomial height \(N^B\). A polynomial peak bound therefore forces positive entropy in every empirical limit. Applying the separately stated binary-window rigidity input gives a Lebesgue component in simultaneous time-and-depth window limits.
* **Uniform growing-block exclusion.** A positive ordinary source \(x\) cannot agree arbitrarily far with a specified noncommuting staircase \(U(VU)(V^2U)\cdots\). The agreement bound is an absolute constant times \(\log_2(2+x)+(\lvert U\rvert+\lvert V\rvert)^2/\lvert V\rvert\). For fixed words the leading logarithmic constant can be taken as 50. Qualitative staircase irrationality and the Tschakaloff method have prior art; the explicit uniform penalty and the finite arithmetic kernels are the contributions asserted here.
* **A restriction on descent-function searches.** Finite-prime digit corrections with the stated unnormalized linear total-mass budget across depths cannot turn logarithmic height into a function that decreases on every long high ordinary arc. The witnesses are actual finite ordinary arcs whose starting values vary with the horizon.

The same packet constructs critical, reciprocal-summable symbolic histories with high entropy and without high word powers. They have irrational binary seeds. They show why the written implications do not, by themselves, eliminate every possible history of one integer. [Escape packet](escape/README.md)

## 4. The remaining global implication

There are two outstanding kinds of supplied source:

1. A bounded least-disagreement cycle with unrestricted actual upper complexity and the full cycle denominator still intact.
2. An escaping positive integer whose entire history is not covered by a finite control or a fixed complexity template.

The retained Lean convergence consumers make the missing assumptions explicit: `FrontierMerger`, or the alternative pair `RecordLock` and `CycleExclusion`. Rebuilding those consumers verifies the conditional deductions; it does not discharge these premises. The latest source-qualified original-law collision criterion supplies another possible route to the escaping case. Its required decay remains a research obligation.

This pass is continuing with the full cyclic equality and the original-law collision statistic. The independently reviewed checkpoint is useful even if neither final obligation closes.

## Evidence and reproduction

[Source manifest](SOURCES.json) pins the project import closure and the reviewed external PR heads. [Review ledger](../../reports/astra-six-hour-20261127/REVIEW.md) records the exact claim boundaries and the distinction between proof, source-qualified input and computation. The independent enumeration lives in [check_upper_affine.cpp](check_upper_affine.cpp); the Lean runner is [check_lean.py](check_lean.py).

The first unified replay passed **25 modules, including all 9 new modules, and 166 selected axiom inventories (46 in new modules)**. [Root verification receipt](../../reports/astra-six-hour-20261127/ROOT_CHECKS.json)

The Lean replay rebuilds all current modules and their project dependencies from visible source in an empty project output cache. It reuses the pinned external Mathlib/package cache, checks warnings as errors, rejects `sorry`, `admit`, `native_decide` and added axioms in the project closure, and checks every selected axiom report against the standard logical axioms. It does not independently rebuild Lean or Mathlib. [Unified receipt](../../reports/astra-six-hour-20261127/lean/receipt.json)

```sh
python3 -B research/astra-six-hour-20261127/check_lean.py \
  --lean /path/to/lean-4.34.1/bin/lean \
  --mathlib /path/to/pinned/mathlib \
  --package-cache /path/to/external/packages \
  --report-dir /path/to/receipt-directory
g++ -std=c++20 -O3 -Wall -Wextra -pedantic \
  research/astra-six-hour-20261127/check_upper_affine.cpp \
  -lgmpxx -lgmp -o /tmp/collatz-upper-affine
/tmp/collatz-upper-affine
```

Repository integrity checks and mathematical checks are recorded separately. Neither a successful build nor an integrity validator is advertised as a proof of the open conjecture.
