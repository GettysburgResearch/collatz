# Late source comparison and a second derivation

24 November 2026. **Collatz remains OPEN.** This is a selected-claim
comparison at frozen heads, not a certification of every file in either
PR. The source objects and review scope are recorded in SOURCES.json.

## PR193: central bank, prescribed ordinary pairs, and exact clocks

The refreshed head is `fbe870ec44239e6b6c753bab9d1c7537acfff701`.
Its [paired theorem](https://github.com/GettysburgResearch/collatz/blob/fbe870ec44239e6b6c753bab9d1c7537acfff701/research/astra-prescribed-closure-20261124/paired/README.md),
Git blob `ba4c46df76eda2e46fa2f64cbe9dc15b76f41c32`, independently obtains
a central bank of at least `c 2^e/H` complete marked words with
`e` comparable to `H`, `|2p-e| <= C sqrt(H)`, a fixed real offset cap
`B`, and at least `c' sqrt(H)` interior marks. Its named probabilistic
input is the PR146 iid marked-gap law. The coordinator and the paired
worker read this proof; the coordinator reconstructed the stopped
fractional-moment bound and the central counting step. That input law
remains source-qualified.

This already contains the central polynomial bank; that priority must
not be assigned to the present continuation. It also gives a short
second derivation of our many-cell conclusion. Choose one fixed
integer `a >= 6` so that `(9B+7)/2^a <= 1/2`, and append the padded
A-block with endpoint map `(9z+7)/2^a` to every word. The new common type
is `E=e+a, P=p+2`. Completeness, distinctness and all earlier marks are
retained, and the number of words is at least `c_a 2^E/H`.

Each such word is compatible with exactly two unit cells modulo
`3^(P+1)`. Hence the sum of the fine-cell multiplicities is at least
`2 c_a 2^E/H`. Distinct carries in `[0,2^(E-1)]` in one congruence class
modulo `3^P` give the ceiling `1+G'/2`, where `G'=2^E/3^P`.
Discard cells of multiplicity less than `c_a G'/(2H)`. Their total
contribution is at most `c_a 2^E/H`; the remaining contribution and
the ceiling force at least `c'_a 3^P/H` cells. Each remaining cell has
at least `c'_a G'/H` words. The fixed append changes the clock and
balance only by constants. Rescaling the initial `H` by a fixed factor
puts the clocks in the convention `H <= E <= D H`.

Thus the many-cell statement has both the frozen joint-coordinate
proof in LOCAL_FIBER_ROWS.md and this direct consequence of PR193's bank.
The latter retains its many interior marks and needs no separate
reverse-prefix input. This is a source-qualified synthesis, not a new
independent proof of PR146 or a full Lean formalization.

PR193 then chooses a common pattern of at least `cN/log N` sources in
an interval of width `N`, and translates that same pattern into the
literal inverse tree of every supplied ordinary pair `(q,5q)`. Its
source position and common suffix clock may be much larger than the
width of that interval. In this continuation, the favorable fine
cells can instead be placed in every prescribed coarse class at one
controlled physical clock and odd count. The final fine representatives
may change with the scale. Neither statement is the fixed-target
balanced-pressure lower bound PT.

The new [head theorem](https://github.com/GettysburgResearch/collatz/blob/fbe870ec44239e6b6c753bab9d1c7537acfff701/research/astra-prescribed-closure-20261124/head/README.md)
and [prescribed-residue extension](https://github.com/GettysburgResearch/collatz/blob/fbe870ec44239e6b6c753bab9d1c7537acfff701/research/astra-prescribed-closure-20261124/head/PRESCRIBED_RESIDUES.md)
control smaller ordered tripling-component representatives for most
parents. Different requested residue words may use different physical
chains. The [orbit theorem](https://github.com/GettysburgResearch/collatz/blob/fbe870ec44239e6b6c753bab9d1c7537acfff701/research/astra-prescribed-closure-20261124/orbit/README.md)
bounds short independently timed returns on the two exact lines
`(x,3x)` and `(x,9x+2)`. These results supply neither ratio-five
multiplicity at one prescribed ordinary endpoint nor a uniform
opposing estimate on the favorable paired fibers. Their original
exceptions and input hypotheses are retained in this comparison.

## PR201: exact-clock scalar amplification and directed closure

The refreshed head is `2978d84f8a1fda9083593b26c6bf724d5976d859`.
The earlier two-end bridge files are unchanged. Its new
[exact-clock amplification](https://github.com/GettysburgResearch/collatz/blob/2978d84f8a1fda9083593b26c6bf724d5976d859/research/killed-green-head-closure-20261124/escape-analysis/README.md)
counts one-arm paths with relative real offset `beta >= epsilon q`;
the endpoint may be chosen separately at each clock. This continuation
counts completed ratio-five pairs with absolute first offset
`beta <= 1/2`. Those conditions are disjoint when
`q > 1/(2 epsilon)`. Its fixed-target near-maximal-relative-offset
criterion concerns scalar periodicity, not a paired central row.

The [directed-cover theorem](https://github.com/GettysburgResearch/collatz/blob/2978d84f8a1fda9083593b26c6bf724d5976d859/research/killed-green-head-closure-20261124/global-bridge/README.md)
gives a complete affine cover for either selected odd unit class
modulo six. It derives a lower exponent `0.84` in each selected
tripling direction if Collatz fails, using its cited PR146 cut and
classical predecessor theorem. That implication does not require the
separate premise M; some additional head consequences do. We credit
this as prior work on single-residue directed closure. It supplies
neither the fixed-target multiplier-five paired count nor the opposing
upper bound needed by the proposed route here.

This intake does not claim to replay the other PRs' Lean modules.
Our seven-module replay covers only the exact files in LEAN_RECEIPT.json.
The frozen proofs in this checkpoint remain unchanged and retain their
separate independent review hashes.
