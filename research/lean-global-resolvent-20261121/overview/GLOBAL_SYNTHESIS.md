# Global synthesis after the repository-wide pass

**Status: researched synthesis and new partial theorems; full Collatz OPEN.**
This pass looked beyond the most recently numbered PRs. Several important
updates occur on older branches. The inventory contains all 143 available
PR descriptions; selected source trees were read for the arguments below.
The mathematical verdicts are restricted to the stated claims and frozen
heads, rather than being blanket endorsements of those PRs.

## The source families now fit together

| Source | Frozen head | Contribution used | Boundary retained |
|---|---|---|---|
| PR173 | `fa0c9e2a2851e6324391e39c17afcb5913185aec` | Mandatory constant-70 band; explicit square-root entrance clock; return-map reduction | Individual marked returns can expand without bound |
| PR184 | `366dab89ee9548084ab9b5e4e90ff82abf287a20` | Independent floor/clock steering; exact high-bit rebasing; lower marked component partners; repair of both parities of the earlier explicit obstruction family | A prescribed source still needs an actual smaller partner |
| PR177 | `00a611094043afeb256d6532b477c0709e8ed270` | Arbitrary-gap certificate programs and multiset replacement by any finite collection of smaller grades | A well-founded order does not provide complete rule coverage |
| PR180 | `9010a8790535002b6d9ff92304f0ba289e2e98fe` | Source-qualified predecessor-density and linear-clock marked populations; rigidity interfaces | These are lower populations and conditional rigidity, not survivor upper estimates |
| PR146 | `f431078244e868dc699fad011044f0d5e7f76437` | Critical interval pairs, a sparse least-failure sieve, and the earlier comparison-center inverse-budget argument | Sparse survivor queries still need closure; inverse budgets can be unbounded |
| PR145 | `dd245a712f985909f541590e3f6c179b7ba011e4` | Future-minimum phase control, polynomial-clock equidistribution, and numerical discrepancy estimates | Rotation statistics do not force descent of each prescribed ordinary orbit |
| PR141 | `5025ef464d4b6d4f4a412a3e33c3477de68dfa8b` | Review of deletion-order and rewrite-scheduling claims | Changing the order of reductions does not manufacture missing coverage |
| This PR, checkpoint 5 | `3dbe5542fd6a5a1d63b354225d92391471c17002` | Finite marked-survivor criterion; marked ancestor and population transfer; exact source-weight transport | The required upper survivor count remains open |

The broader energy and pressure review also inspected the closing interfaces
in PR155, PR163, and PR167, and the pressure developments in PR143/144.
Their exact current heads are in the [PR snapshot](../../../reports/2026-11-21-lean-global-resolvent/checkpoint6-pr-snapshot.md).

Relevant source paths include:

- PR184: `research/lean-band-coupling-20261121/ClockSteering.lean` and its
  rebasing and lower-merger modules.
- PR177: `research/lean-exact-witness-global-20261121/UNBOUNDED_GAP_REWRITES.md`.
- PR180: `research/lean-ordinary-closure-20261121/LINEAR_BLOCK_ATOM_FLOOR.md`,
  `REPOSITORY_RIGIDITY_COROLLARY.md`, and
  `research/lean-forward-band-20261121/MARKED_PREDECESSOR_POPULATIONS.md`.
- PR146: `research/upper-bit-mergers/CRITICAL_INTERVALS.md`,
  `LEAST_FAILURE_SIEVE.md`, and `WHOLE_INTERVAL_SYNCHRONIZATION.md`.
- PR145: `research/binary-run-occupancy/MELLIN_PHASE.md` and
  `research/profinite-orbit-averages/ONE_STEP_LAG.md`.

### Later source update caught before publication

A final refresh found that PR180 advanced to
`cf91e46fa9fbadba3df7942202a5197c134d0ce0`. Its new
`JOINT_CLOCK_MIXING.md` and `GLOBAL_RENEWAL_ATTACK.md` give a written,
source-qualified uniform natural predecessor-density theorem: absolute
`c,C>0` satisfy

\[
X\ge Ca\quad\Longrightarrow\quad
\#\{0<n\le X:n\text{ odd},\ n\to a\}\ge cX/a
\]

for every positive ternary-unit target `a`, with unit sources available
at adjusted constants. The argument retains the full exponent total in
Tao's nonnegative renewal estimate; it is not a deduction of fixed-total
independence from marginal mixing. The constants are not numerically
specified, and this analytic theorem is not Lean formalized.

This removes the target-dependent onset from the earlier population
statement and permits simultaneous finite-scale packing. It is still a
lower bound on ancestors, with onset `X>=Ca`. It does not supply an
ancestor below the prescribed source, a survivor upper bound, or a loss of
a fixed source atom under actual marked return. The companion source itself
retains those renewal and incoming-weight estimates as open. None of the
new finite Lean theorems in this checkpoint assumes this analytic result.

The actual construction gives a useful further finite-clock corollary.
Put `L=log_2(X/a)` and `delta=2-log_2 3`. Its witnesses reach `a` at clocks

\[
h=\frac{2}{\delta}L+O(\sqrt L+1),
\]

with absolute constants. Indeed their depths satisfy
`s=L_b/delta+O(sqrt(L_b))`, where `L_b=log_2(X/b)` and the selected parent
has `b/a` between fixed positive constants; their ordinary clocks are
`floor(L_b+s*log_2 3)+e`, with `e` uniformly bounded. Thus only
`O(sqrt(1+L))` integer clocks occur. Pigeonholing the distinct population
shows that one clock carries at least
`c'X/(a*sqrt(1+log_2(X/a)))` sources. This is a written corollary of that
proof, not a new Lean assertion or a fixed-total independence assumption.

This also pinpoints a limitation of the direct composition: our `9Q`
entrance deadline for sources below `2^Q` may come after their approximately
`4.82*log_2(X/a)` arrival at the common target. Their subsequent marked
visits may coincide. Distinct predecessor counts therefore cannot be
carried unchanged through that forward entrance map.


## Attempt A: force a smaller component partner

The marked reduction makes this the most concrete constructive target.
The new finite theorem proves that a supplied partner `u<=2^Q` reaches an
actual marked value below `2^(10Q)` at a clock below `9Q`. If the original
marked source `n` is at least `2^(10Q)`, its supplied ordinary merger with
`u` therefore yields a strictly smaller marked component partner. This
preserves the original source and both physical merger clocks.

Using the published logarithmic irrationality bound, a sufficient partner
range for arbitrary large `n` is

\[
u\le\exp\bigl(c(\log n)^{1/4.117}\bigr)
\]

for a suitable fixed positive constant. This is a quantitative improvement
over the earlier square-root entrance budget. The improved range is still
an input condition: no universal theorem produces that partner.

The exact rebasing identity from PR184 is useful because it permits a
different finite inverse word after the old binary horizon. Writing

\[
n=2^h3^s v+r,\quad T^h(r)=y,
\]

let `p` count the odd inputs along the `h`-step path from `r`. If
`T^t(u)=y` and the latter path uses `a<=p+s` odd inputs, the rebased
ordinary partner is

\[
x=2^t3^{p+s-a}v+u,\qquad T^t(x)=T^h(n).
\]

Thus the first unsupported step is the existence of an eligible ordinary
path for which the exact inequality

\[
\bigl(2^h3^s-2^t3^{p+s-a}\bigr)v>u-r
\]

holds. Neither a large population of ancestors nor a finite residue match
implies this original-source inequality. For a small-source target `x<=2^Q`
with `v>=1` and a nonnegative offset, the same formula forces `t<=Q`.
Increasing the ternary reserve alone therefore does not remove the fixed
small-source clock constraint.

The new inverse-word theorem further shows why fixing a small odd-count
surplus cannot supply a universal selector during initial ascents. The
necessary surplus is unbounded even among marked sources. This is a
resource requirement for a complete construction, not an impossibility
theorem for merger methods.

## Attempt B: consume the whole supplied certificate

The existing multiset order now supports arbitrary exponent sizes and
replacements by arbitrarily many smaller grades. The structural order
itself is no longer the immediate issue. The new terminal carry compiler
compresses an arbitrary complete prefix into one finite signed carry and
retains the exact numerical debt to the original input.

This produces a useful full-language interface: zero carry is a complete
certificate; a minus-one carry can transfer to an explicitly certified
psi source; any finite signed continuation has an exact debt test. The
source and all clocks remain ordinary.

The prefix `[3]` proves an important boundary without a search cutoff. Its
Hplus companions reach `2^(h+1)-1` in three steps and remain above the
original input throughout the whole remaining binary horizon. Hence the
statement that a sufficiently large final gap always pays the whole
prefix debt within that horizon is false. The new handoff can leave that
horizon in the certificate program, but all resulting query states are
not yet covered by decreasing rules.

The final [closure pass](CARRY_CLOSURE_PASS.md) also disproves automatic
eligibility of the one-step minus-one handoff, using a real complete source
certificate and an arbitrary initial-loop language. It supplies a longer
repair interface: a deficit `D` is paid by an actual certificate for
`3^(D+1)` with gaps below the available terminal exponent. The concrete
shortfall is repaired; the universal auxiliary-certificate statement remains
open. This qualification matters: the counterexample refutes one automatic
handoff, not all longer rewrites.

The next useful target is a total ordinary rule selector for the complete
carry/comparison state. Proving another well-founded order without proving
its selector would leave the same logical gap.

## Attempt C: convert marked populations into extinction

Checkpoint 5 already supplies a finite, unconditional implication at every
admissible scale `Q`:

\[
|S_Q(t)|<2^Q\quad\Longrightarrow\quad
\text{every ternary unit }a\le2^Q\text{ reaches one by }\max(1,t).
\]

Here `S_Q(t)` counts actual marked starts below `2^(10Q)` that have not
hit one through ordinary time `t`. The same packet proves the equivalence
between full Collatz and passing this test at unbounded admissible scales.

The latest PR180 marked-population argument is stronger in a different
direction: under its cited analytic inputs, each fixed target has a
at least `gamma*2^d/(d+1)^2` marked ancestors at arbitrarily high
target-dependent dyadic scales, with linear ordinary clocks. This remains a lower bound on the footprint of a component. It
does not provide an upper bound for a surviving component.

The new forward clock improves the control of first entrance and first
positive return, including source-weighted moments of their logarithmic
heights. It does not make source mass disappear: the previous exact
transport theorem preserves every fixed surviving source atom. A finite
clock relative-descent theorem with a floor growing with the source is
also insufficient for a fixed-floor all-time survivor estimate.

The complete primitive-source moment from checkpoint 3 remains another
clean arithmetic target. Its exact decomposition removes the higher-lift
tail geometrically; the primitive term is the remaining global quantity.
It includes all positive valuation words and both possible kinds of
counterexample. Its decay has not been derived from the new band theorem.

## Attempt D: close the energy or pressure argument

The review did not produce the missing global upper bound in the energy
interfaces. In particular:

- Finiteness of the sparse retained-query energy does not establish the
  needed strictly contracting incoming-column bound. A bound on the
  number of queries made by each source controls the other direction.
- In the tested localization and inverse-fibre round trip, the two
  scaling factors cancel. A strict loss must come from an additional
  proved mechanism; it cannot be inserted into that equality.
- Discounting only growing trajectories can miss a finite nontrivial
  cycle. The primitive-source moment avoids this defect, but its decay
  remains an actual obligation.
- The new phase results were checked against older source trees before
  being treated as progress. In particular PR145 already contains the
  future-minimum phase and polynomial-clock equidistribution argument;
  those are credited there rather than republished as new.

These are the first unsupported steps of the attempted completion, not
claims that every possible energy or pressure approach is impossible.

## Assessment

The strongest positive advance of this pass is the uniform finite
denominator clock and its polylogarithmic analytic consequence. It makes
the mandatory-band reduction quantitatively much more usable. The other
two developments replace bounded dictionaries by unrestricted arithmetic
statements: one governs every inverse history within its stated budget,
and one normalizes every supplied complete prefix.

A full proof still needs a statement about **every prescribed ordinary
source**: an actual smaller partner, complete decreasing rule coverage,
or a survivor upper estimate. The new proofs strengthen those interfaces
without asserting that this final universal step has been obtained.
