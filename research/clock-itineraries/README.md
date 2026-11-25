# Exact clocks with prescribed odd-state residues

**PROPOSED. The Collatz conjecture remains open.** Consider the ordinary shortcut map
`T(2n)=n`, `T(2n+1)=3n+2`. An odd gap from `x` to `y` has length `e≥1` and satisfies
`3x+1=2^e y`, with both ends positive and odd. A unit here is an odd positive integer prime to three.

The November 25 pass combines the window certificate, uncorrected pointwise clock bound, and cycle test. It also gives 513 consecutive tower ranks with one physical endpoint, quantitative restrictions on escaping records, and an all-period cycle occupation bound. The two global obligations remain open. [November 25 proof attempt](November25.md) · [Combined Lean theorem](NovemberProposal.lean) · [Fifty source PRs](FiftyPRs.md)

The [current full-conjecture proposal](Proposal.md) gives two explicit arithmetic obligations. The first asks for a cumulative clock crossing on each ordinary unit orbit. The second asks for arbitrarily large depths at which a finite cycle test returns false. Lean proves the equivalence and the correctness of the finite test. The two universal obligations remain open. [Main declaration](FinalProposal.lean)

## Which itineraries occur at a fixed clock?

Fix a unit endpoint $q$, precision $K\ge1$, $M=3^K$, $L=2\cdot3^{K-1}$, and $m\ge2$. Prescribe *every* source residue $r_0,\ldots,r_{m-1}$ modulo $M$ in chronological order. All are units modulo $M$. Ask for an ordinary path from some $x_0$ to this very $q$, with exactly $m$ odd steps, exactly $S$ shortcut steps, and $x_i\equiv r_i\pmod M$ before each odd step.

**Theorem.** For every $S\ge 3L(m+1)+1$, such a path exists if and only if

\[
  2^S q\prod_{i=1}^{m-1}r_i
    \equiv \prod_{i=0}^{m-1}(3r_i+1) \pmod M. \tag{1}
\]

At $M=3$ and $S\ge6m+7$, the only condition is the parity of the clock. This parity counts the residues equal to two among $r_1,\ldots,r_{m-1},q$. The first source residue $r_0$ carries no parity cost. The complete equivalence at $M=3$ and the connection to literal shortcut iteration are kernel-checked in [TernaryItinerary.lean](TernaryItinerary.lean), theorems `exact_clock`, `Route.follow` and `Route.readout`. The Lean list orders the prescribed marks backwards from the endpoint. The proof below treats every $K$.

**Proof.** Multiplying the $m$ gap equations and reducing modulo $M$ gives (1). The order of two modulo $3^j$ is $2\cdot3^{j-1}$. Indeed $4-1=3$, and cubing $1+3^j t$ with $3\nmid t$ raises the valuation of its difference from one by exactly one. The order divides the unit group size, is even, and the valuation calculation excludes every smaller divisor. Thus every unit has a positive discrete logarithm at most the group order.

First build the tail backwards, starting with $z=q$. For $i=m-1,\ldots,2$, choose $1\le e_i\le3L$ by

\[
  2^{e_i}z\equiv 1+3r_i\pmod{3M},
  \qquad z\leftarrow(2^{e_i}z-1)/3.
\]

The new $z$ is a positive odd unit in the requested class. Subtracting these gaps leaves a budget $t\ge9L+1$. Cancelling the tail equations in (1) gives
$2^t z r_1\equiv(3r_0+1)(3r_1+1)\pmod M$.
Choose $1\le f\le9L$ so that
$2^f\equiv2^t z-3-9r_0\pmod{9M}$. The right side is a unit. Put $g=t-f\ge1$.
Modulo three this gives $2^g z\equiv1$. The two starting values satisfy

\[
  y=(2^g z-1)/3,\qquad
  x=(2^f y-1)/3=(2^t z-2^f-3)/9.
\]

The congruence defining $f$ gives integral $x\equiv r_0\pmod M$. Reducing the cancelled signature gives $2^f r_1\equiv3r_0+1\equiv2^f y\pmod M$. Hence $y\equiv r_1$. All constructed gaps are exact because the next state is odd. This construction uses the supplied ordinary endpoint without changing its representative.

**One free internal mark.** Fix $S$ in the stated range and leave any one $r_j$ with $1\le j<m$ unspecified. Its contribution to the right side of (1), after division by $\prod_{i=1}^{m-1}r_i$, is $3+r_j^{-1}$. This permutes the units modulo $M$. Exactly one choice completes the signature. Consequently at least $L^{m-1}$ distinct ordinary starts reach the *same* $q$ at the *same* clock. Their freely prescribed $m-1$ marks can be read off the forward trajectory. In Lean `free_marks` frees the internal mark nearest $q$, and `Route.readout` proves recovery.

**Small clocks.** Incrementing the first gap by $3L$ preserves all marks because $2^{3L}=1\pmod{3M}$. Thus the entire feasible time set for the fixed prescription consists of three arithmetic progressions of step $3L$, one for each lift of the unique allowed residue modulo $L$. Each starts at its own least feasible time, at most $3L(m+1)+3L$. The high-clock theorem does not decide smaller times by congruence alone. At $K=1$, $q=13$, $m=2$, $r_0=r_1=1$, the clock 18 satisfies (1). Its first gap would obey $2^f=1\pmod{27}$ and $1\le f<18$, an impossibility. This makes 19 sharp in the uniform two-gap case. The source-only witness is already in PR #201.

## What a counterexample would force

**Lean theorem `rows_of_failure`.** If any positive integer fails to reach one, there is a single nonconverging unit $a$ such that for every $b,m$ satisfying

\[
  m\ge2,\qquad 22m+5a+35\le2b, \tag{2}
\]

one ordinary endpoint $q>2$ receives all $2^{m-1}$ binary residue words on the *first* $m-1$ odd states, with $b$ odd steps and $2b$ shortcut steps. The final mark before $a$ absorbs the parity condition. The prefix clock, the gate $a$, and the entire suffix from $a$ to $q$ are common across these words. In particular one can take $m=b/11-O_a(1)$ after rounding. `carry_through_gate` proves a relative carry of at least $1/(3a+1)$ for every such path with a nonempty suffix.

Here is the time budget. A kernel decision checks that every positive source below 32 reaches one. On a bad odd ray each state $x$ therefore satisfies $(3x+1)^5\le 2^8 x^5$. Multiplying along $b-m$ gaps of total $v$ yields $2^{5v}q^5\le2^{8(b-m)}a^5$. The elementary $a\le2^a$ gives $5v\le8(b-m)+5a$. Thus the clock $2b-v$ available at $a$ meets the exact itinerary bound (2). For carry, the first step out of $a$ contributes $3a+1$ where the multiplicative term alone would give $3a$. All other additive terms are nonnegative.

**A finite-row equivalence.** Fix $a,b,m$ and ask whether the common suffix and all the marked prefixes above exist, with $q>2$. This is the predicate `FullRow`. Its evaluation is finite: the gap lists are positive compositions of at most $2b$, and each list gives at most one starting integer from the supplied endpoint. The suffix from $a$ is deterministic. For $m=\lfloor b/12\rfloor$, Collatz holds exactly when every positive $a$ has arbitrarily large $b$ where this row is missing. If $a$ reaches one at time $k$, a suffix of $b-m\ge k$ odd steps ends in the shortcut cycle through one. Conversely (2) supplies every sufficiently large row at a fixed bad gate. The equivalence `universal_iff_missing_rows` is unconditional and kernel-checked.

In the forward-filtered statistic of PR #201 the same $q$ passes any future test for failing to hit one because its orbit stays outside that basin. This improves its elementary $2^{\lfloor b/16\rfloor}$ lower count to $2^{b/11-O_a(1)}$ for that statistic, and prescribes all the indicated prefix marks. The row here keeps its own small-gate definition. PR #201's additional choice of an arbitrarily fine initial ternary class is a separate result. We do not infer that every terminal in its other, internally filtered statistic meets our stronger count.

## The opposing estimate

There is an unconditional obstruction on the same balanced row. Write $h$ for the number of gaps of length one. Suppose $q>1$ and relative carry is at least $\epsilon>0$. If $b$ tends to infinity at fixed $\epsilon$, then $h$ tends to infinity at least logarithmically.

For details, write $q=3^b x/4^b+\beta$. A gap $e$ updates $\beta$ to $(3\beta+1)/2^e$. The quantity $1+\max(1,\beta)$ cannot increase for $e\ge2$, and grows by at most $3/2$ for $e=1$. It starts at two. Thus $q\le 2(3/2)^h/\epsilon$. Balance gives $\sum_{e>2}(e-2)=h$. There are at most $d\le2h$ exceptional gaps $e\ne2$ and their total length is $2d\le4h$.

Across a run of $k$ neutral gaps $e=2$ from $u$ to $v$, the exact identity is $4^k(v-1)=3^k(u-1)$. All states exceed one because the odd orbit of one is fixed and $q>1$. Therefore $3^k\mid v-1$, $k\le\log_3 v$, and $u\le (4/3)^k v\le v^\rho$ for $\rho=\log_3 4$. A reversed exceptional gap increases $\log_3 v$ by at most $e\log_3 2$. Reading the $d+1$ neutral runs backwards now gives

\[
 b\le d+(\log_3 q+2d\log_3 2)\frac{\rho^{d+1}-1}{\rho-1}.
\]

Indeed the length of the $j$th neutral run, starting the count at zero, is at most $\rho^j(\log_3 q+2d\log_3 2)$. With the carry bound this yields $b\le C_\epsilon(h+1)\rho^{2h}$ and $\liminf h/\log b\ge1/(2\log\rho)$ along unbounded qualifying rows. A gap one ends at residue two modulo three. In particular fixed-defect full itineraries cannot support these rows indefinitely.

For a relative carry of at least $2^{-j}$, Lean proves the explicit integer bound $b\le 2^{2h+1}(j+5h+1)+2h$. The second module also proves the shifted orbit identity and the nonvanishing of every nonempty subset of its exceptional and terminal terms when $q>1$. [SparseClock.lean](SparseClock.lean)

A separate written argument uses Evertse's Corollary 1 to strengthen the conclusion to $h/\log b\to\infty$ along any sequence of qualifying rows with $b\to\infty$ at fixed $\epsilon>0$. The application of that corollary and the resulting limit are proposed for mathematical review. [Derivation and source](SparseDefects.md)

**Remaining step in the itinerary argument.** The lower theorem prescribes the first $m-1$ residues. Both upper estimates count exceptions on the whole path. On a nonconverging ray the common suffix of length $n$ already has at least $2n/5-a$ gaps of length one. Every other gap costs at least two, and the suffix clock is at most $8n/5+a$. The subsequent fixed-gate calculation proves that at the depth used in the equivalence, a missing row is exactly an actual hit at one once the explicit clock budget is met. [Fixed-gate proof and sharp distortion bound](FixedGate.md)

## Sources and replay

The ordinary map and integrated stopping framework use main at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. The two-gap identity, the one-gap unit tree and the exact-row carry test come from [PR #201, escape analysis at 2978d84](https://github.com/GettysburgResearch/collatz/blob/2978d84f8a1fda9083593b26c6bf724d5976d859/research/killed-green-head-closure-20261124/escape-analysis/README.md). [PR #202, fixed-clock routing at 3b10b24](https://github.com/GettysburgResearch/collatz/blob/3b10b24d12d4b349cb20f4cbc83086c8a09f807e/research/synchronized-long-basin-blocks-20261124/README.md) and [PR #203, phase-marked depth slices at 3f2c89f](https://github.com/GettysburgResearch/collatz/blob/3f2c89f12b057b8bb8655bd6fc794c772aa8b65d/research/mixed-adic-basin-density-20261124/fixed_target_depth_bank.md) motivated keeping the exact clock and checking which observations may be fixed jointly. The Lean modules use elementary arithmetic and finite kernel decisions. Two related submissions consider paired rows at a fixed target and excursions along an ordinary orbit. [PR #204](https://github.com/GettysburgResearch/collatz/pull/204) and [PR #205](https://github.com/GettysburgResearch/collatz/pull/205)

From this directory, a Lean installation providing Std can build the modules in dependency order. This POSIX shell example writes compiled objects into a fresh temporary directory.

```sh
set -e
build=$(mktemp -d)
export LEAN_PATH="$build${LEAN_PATH:+:$LEAN_PATH}"
for mod in TernaryItinerary SparseClock FixedGate MinimumDescent CycleRows \
  SynchronousShadow OrbitAttack CycleDetection CycleAmplification DescentClocks \
  ClosureProposal ClockRecurrence FinalProposal MixedBarrier \
  BasinTransport WindowCapture CycleFrontier CycleFrontierCounting \
  EscapeFrontier EscapeRecords TowerFrontierAffine TowerFrontierRotation \
  TowerFrontier TowerFrontierMergers TowerFrontierLimit TowerFrontierPrescribed \
  NovemberProposal
do
  lean -j1 -DwarningAsError=true -Dlinter.deprecated=false -DautoImplicit=false -DElab.async=false \
    -o "$build/$mod.olean" "$mod.lean"
done
python -X utf8 -B replay.py
python -X utf8 -B proposal_replay.py
python -X utf8 -B window_replay.py
```

The November 25 build uses native Lean 4.34.1 at commit `5045d0056413266e57c625dcd7c365b10e377c52`. The command permits legacy theorem names that this release deprecates and treats other warnings as errors. The original fourteen modules were also checked with the Lean 4.33.0-pre WebAssembly CLI at `62b6a2291302d4bbeace37642a066b7510d0145c`. The theorem audits print their dependencies. [Earlier compiler distribution](https://github.com/live-codes/browser-lean/tree/a8aed095534e67061e2626b94e8e69193099091d)

The first Python control reads constructed paths forward, independently enumerates 2,628 exact rows, and checks the shifted identity on 36,285 ordinary segments. The second control checks 79,378 segments against the sixth-power bound, exhausts the finite cycle test through depth 16 and checks 114 translated paths. The common gate in the 512-source example reaches one at shortcut time 553. [Finite controls](proposal_replay.py) and [kernel-checked gate](FinalProposal.lean)
