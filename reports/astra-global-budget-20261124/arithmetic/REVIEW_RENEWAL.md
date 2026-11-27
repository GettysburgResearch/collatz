# Review of the fixed-target paired cluster argument

**Verdict: VERIFIED within the stated source dependencies.** Target files under
`research/astra-global-budget-20261124/renewal/` at review time, SHA-256:

| File | Digest |
|---|---|
| README.md | b0795766591a06fb0e875048dd411f3e669b49a4f103a8daf5d5a0022fa7b00b |
| CellPressure.lean | 3fab8878494cbc49fa10e31a1f9d093db2efeb5b7c9145279349848513b8b4e3 |
| check.py | 5fe643d3ea026821e94d7e6cfd4c899bfea80ae6eee3bab157c708ef10d82e85 |

I checked the ratio-five mark dictionary against PR200
`39918be724038ac550d77c7fc95d17e05251dfc6`,
`research/regularity-rigidity-20261124/continuation/REVERSE_RENEWAL.md`, §1.
Specifying the initial bit and then including the terminal sentinel gives
mass exactly $2^{-e}$. PR146
`f431078244e868dc699fad011044f0d5e7f76437`,
`research/upper-bit-mergers/FIVE_RETURN_CLOCK_AND_TERMINALS.md`, supplies
the two-sided first-return tail conditional on the odd initial bit.
The real square-root moment appears in PR195
`1c6e750e2f6970e6d5456cba5a93c2f3de8c2a97`,
`research/astra-global-closure-20261124/round5/renewal/README.md`, §3.
I checked the imported statements and their orientation. I did not independently
re-prove the underlying full-state martingale recurrence.

At each of order √N mark indices, the lower length tail excludes a too-short total by its maximum. The upper tail and the truncated first moment exclude a too-long total. The independent-bit maximal inequality is applied on the deterministic horizon, and the real-offset bound uses reversal in law of the finite iid block list. These four conditions give a fixed positive probability jointly without conditioning on the random length. Different indices cannot parse the same complete word at a fixed row, so summing their masses before taking the best of $O(N^{3/2})$ rows gives the claimed $1/N$. The two surviving ternary extensions per word give the stated mean, and whole-word lifting plus source distinctness gives the upper bound from a real interval even for a small positive terminal. The sign issue there is resolved by exact lifting: no nonpositive integer forward iterate is positive.

For the every-coarse-prefix assertion, the 18 successive available powers of
two run through all units modulo 27. At an odd unit endpoint choose output
$2^h q$ congruent to 16 or 25 modulo 27, giving an odd unit inverse. Reverse
j = ⌈s/2⌉ chosen branches to obtain the single affine dictionary
word with ternary slope $3^{2j}/2^D$. Multiplication by this slope followed
by its carry is injective on the input cell labels at the increased precision.
All their images reduce to the selected $v$. There are
$3^{p+1+2j-s} ≤ 9·3^p$ potential finer cells over $v$. Every odd
lift of a selected cell has an integral predecessor in its original unit
cell, so the assertion is genuinely uniform over the ordinary lifts.

For the amplified interval count I read and reran PR200's
`research/regularity-rigidity-20261124/RATIO_PRESSURE.md`, §§2–3, and
`ratio_pressure.js` at the same full SHA. Its 4,374 classes gave minimum
312442229426789 at scale 281474976710656, with 473 records, 1,419 literal
return checks and 867 ordinary inverse checks. Strict increasing size and
unique first-return parents prevent collisions at every depth, independently
of root colors. A single sufficiently large ancestor of the prescribed root
therefore supplies at least a positive $q$-dependent constant times $Y^{1/9}$ distinct odd units in
$[Y/2^{400},Y]$. The padded output $Q$ encodes the intermediate uniquely,
since the factorization $9Q+7=2^h a$ with $a$ odd recovers $h$ and $a$.
Spacing in $Q$ makes the bounded-overlap selection valid. As
$P → ∞$ and $P=o(\log Y)$, the padding clears the fixed lower factor
$2^{400}$ while the upper endpoint stays $Y^{1+o(1)}$. The common
synchronization clock is asserted within each retained interval.

I compiled CellPressure.lean in Lean 4.34.1 with warnings as errors and
replayed the local checker in normal and optimized Python. Both gave 658
complete words, 1,316 cell memberships, 144 fixed-pair imports and 1,872
coarse-prefix two-arm lifts. These controls are finite; the positive row
mass and the every-scale asymptotics are written arguments. There is no
deduction that a particular prescribed full-depth ternary cell has high
mass, or that every ordinary orbit reaches 1.
