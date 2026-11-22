# Late-source composition: stronger carry exits, exact overlap, and the remaining stop

Date: 2026-11-22. **Status: the return-cone composition is kernel checked in
`SignedCarryReturns.lean`; universal successful stopping remains OPEN.**
The pinned upstream sources were inspected, and their needed return proofs
were ported and compiled in the new adapter. No upstream packet compiler
replay was performed for this note.

## Delta sources

This continuation inspected only the mathematical additions after the
earlier source pins:

- PR177, `a0a0d76f91b4e3846c1b1f0706cad56cb6098317` to
  `2efabba9a341839b67ed011d6b878b23730ee51d`:
  `research/lean-exact-witness-global-20261121/LOW_GAP_GLOBAL.md`,
  `PSI_VALUATION_ONE.md`, `CLOCK_SYNCHRONIZATION.md`, and the exact
  `lean/Collatz/LowGapGlobal.lean` interfaces.
- PR180, `bfba8feaefb3d0910456cdd92d2afcf9e8785b4d` to
  `cfe70e02f246119a55fb5bf8fd573f148d746beb`:
  `research/lean-critical-20261122/WITNESS_ATTACK.md` and
  `lean/WitnessCritical.lean`.

The first new source contributes a uniform return cone and whole-prefix
clock repayment. The second independently develops a positive-debt carry
compiler and a larger successful regular language. Neither source asserts
universal successful coverage.

## 1. The exact new return hypotheses

Let `Interval(s,t)` mean `0<t<=2s+1`, and let `Hyp Interval old` be the
existing hypothesis granting all valid interval queries with a supplied
complete source certificate of grade strictly below `old`.

At PR177's frozen new head, `nine_lattice_return` has exactly these inputs:

```
Certificate q gaps
0 < target
target <= 9*q+3
target % 4 = (q+3) % 4
Hyp Interval (grades 0 gaps)
```

Its conclusion is `Basin target`. The source is the odd integer represented
by `Certificate q gaps`; it is not an arbitrary even powered source.

The same file proves `odd_source_cap` for all positive targets at most
`3*q+2`, with the same source certificate and the same induction
hypothesis. It advances the actual odd source once, so its genuine child
interval ceiling is `2*T(q)+1=3*q+2`. At source one it uses the explicitly
proved finite base cases.

The nine-cone theorem splits the source modulo four. When `q=1 mod 4`,
the target is divisible by four and its quotient is inside the odd-source
cap. When `q=3 mod 4`, the target is `2 mod 4`; its half is inside the
odd-source cap of the actual next odd source `T(q)`. That latter application
uses the actual complete child certificate and composes two strict grade
decreases. It does not reuse an uncontrolled output certificate.

Consequently `negative_nine_return` proves `Basin(9*q-1)` under the
displayed interval hypothesis, uniformly over every complete source word.
The result is a conditional step rule in the common induction, not an
unconditional assertion `Basin(q) -> Basin(9*q-1)`.

## 2. Composition with the signed compiler gives a larger absorbing set

Suppose the signed compiler consumes a nonempty prefix of an actual
complete certificate, retains `Certificate(u,tail)`, and proves

\[
T^A(n)=3^p u-c>0.
\]

The compiler also proves

\[
\Gamma(0;\mathrm{tail})\prec\Gamma(0;\mathrm{original\ word}).
\]

Restrict the original interval induction hypothesis to queries below
`grades 0 tail` by transitivity of that same order. This gives exactly the
hypothesis required by the new PR177 returns. Therefore the following
state tests are sound, with no restriction on the remaining suffix:

| Signed carry state | Exact reason the original target closes |
|---|---|
| `p=0`, `c>=0` | The actual target is at most `u`, hence directly inside the retained source interval. |
| `p=1`, `c>=-2` | The actual target is at most `3u+2`; apply `odd_source_cap` to the literal retained certificate. |
| `p=2`, `c>=-3`, `c=1 mod 4` | The actual target is at most `9u+3` and congruent to `u+3 mod 4`; apply `nine_lattice_return`. |

For the original carry `(2,-2)`, its first source gap `a` gives `(a+1,1)`.
Thus a first gap one immediately reaches the last row, regardless of every
later source gap. A first gap two followed by one gives

\[
(2,-2)\longmapsto(3,1)\longmapsto(2,5),
\]

and also closes. These agree exactly with PR177's `positive_nine_first_one`
and `positive_nine_two_one`; they are not additional priority claims.

This changes the proposed compiler policy: it can stop on either of the
larger uniform tests instead of waiting for power zero. Its finite-word
correctness and exact source-rank accounting remain unchanged.

## 3. Why the larger absorbing set still does not close every supplied word

An allowed complete cap-four source already demonstrates that the combined
tests are not exhaustive. Take the odd ternary unit `r=17` and its exact
complete word `[2,3,4]`. The original target is `9*r+2=155`. The successive
compiler states and ordinary target values are

| Consumed prefix | Retained source | Carry state | Actual target |
|---|---:|---|---:|
| `[2]` | 13 | `(3,1)` | 350 |
| `[2,3]` | 5 | `(4,10)` | 395 |
| `[2,3,4]` | 1 | `(6,61)` | 668 |

None meets the enlarged state tests, and the literal source word is now
exhausted. The Lean theorem `cap_four_guard_not_total` checks the actual
certificate, the alphabet bound, enabled compilation, absence of an
absorbing state at all four prefixes, the final carry, and the ordinary
endpoint. This is a failure of the proposed combined guard, not a
counterexample to Collatz or a census used to infer global behavior.

The consumed source gap two can fund the child powered certificate `2u`
under the original grade: its new initial-even grade three is below the
removed odd-gap grade four. But its ordinary interval ceiling is only
`4u+1`, whereas the new carry is `27u-1`. The nine-cone theorem cannot be
applied to `2u`, because it requires an odd complete source certificate.
The first actual source step from `2u` halves back to `u` and creates no
new larger return cone. This is the specific missing inference in that
otherwise tempting handoff.

More generally, after consuming the whole complete word the actual
remaining target is `3^p-c` at source one. PR180's new
`terminal_padding_transport` proves that literal gap-two padding reproduces
the ordinary positive map `T^2` on that target. With positive target and
positive debt, the exponent stays positive: a zero exponent would express
one as the sum of two positive integers. Its `every_target_terminal_debt`
also shows that every positive integer admits such a terminal representation.
Thus terminal padding supplies neither an independent termination theorem
nor a harmless bounded residual set.

## 4. What the new clock rules add, and what they do not

PR177's `ClockSynchronization` gives sound original-rank returns after a
whole source/target prefix with equal odd-step count. If their total clocks
are `A,B`, an inserted initial even exponent `f` can pay the target when
`e+A<=f+B`, under the stated correction domination. The rank is paid when
`f=e` or some consumed source gap exceeds `f`. A first clock repayment
controls the corrections through all the preceding partial clock sums.

These rules permit intermediate rank increases and arbitrary prefix
lengths, but the final strict decrease is still in the original grade.
They do not authorize arbitrary clock-decreasing source overrides.

The same new packet gives a precise failure of a universal funded-repayment
policy: source `34=2*17`, target `63`, source word `[2,3,4]`. At all three
nonempty source prefixes the required exponent exceeds every funded one.
Its exact replay and terminal cycle invariant extend that failure to any
number of appended source gap-two loops. The target does converge, so this
is an obstruction to that particular universal selector.

The new valuation-one psi theorem is broader than the earlier individual
handoff families: under `Hyp Interval (grades 1 gaps)`, every target
`4q-1` closes for every complete odd certificate of `q`. It deletes the
initial-even grade and uses the uniform negative-nine return. It does not
supply a psi-only induction hypothesis, close all valuation-one interval
queries, or automatically cover initial valuations two and three.

## 5. Overlap and independent contributions

PR180's new `WitnessCritical.lean` independently proves the positive-debt
reflection identity, arbitrary-gap update, literal-word compiler, zero
exponent interval rule, and the two terminal fixed states representing one
and two. These substantially overlap the corresponding positive-debt part
of our `SignedCarry.lean`; they must be credited as concurrent work.

The signed module additionally proves the unrestricted integer-debt form,
the equality with the actual target odd count, the exact whole-word budget
`p_final+source_prefix_length=p_initial+actual_target_odd_count`, and
`finite_signed_lift`. The latter is used by the independent analytic
argument to legalize positive ordinary rays from finite negative paths.

PR180's three-state accepted language allows arbitrarily many gap fours,
but its positive-nine application always starts with source gap one.
PR177's newer uniform return covers every suffix after that first gap one,
so it already contains that successful language's positive-nine conclusion.
The general compiler itself remains useful outside the accepted grammar.

**Remaining full-closure claim:** every reachable low-interval state must
admit one of these successful common-rank returns, another complete-source
replacement, or an independently proved terminal resolution. The new
arithmetic compilation and return families do not yet establish that total
successful selection. No such claim is assumed in this composition.

## 6. Actual formal integration and evidence

`SignedCarryReturns.lean` imports only the existing `SignedCarry` module.
It reproduces the body of the exact powered-source `Hyp Interval old`
interface and ports the credited PR177 odd-source cap and nine-lattice
proofs. The only local terminal check is the needed fixed range through
twelve. No old vendored file is modified and no new unproved return-cone
hypothesis is introduced.

The new theorem `absorbing_return` proves the three state tests above.
`compiled_return_rule` combines them with any enabled, nonempty actual
source prefix, reconstructs the literal tail, and restricts the original
interval hypothesis by the proved common-grade decrease.
`positive_nine_compiled_rule` supplies the signed initialization. The
earlier new-source results on prefixes `[1]`, `[2,1]`, and valuation-one
psi are then recovered as credited corollaries in this same packet.

The final development build passed with Lean 4.34.1, one worker, warnings
as errors, and `autoImplicit=false`. All eleven public declarations have
individual axiom reports, with union exactly `propext`, `Classical.choice`,
and `Quot.sound`. `SignedCarryReturns.receipt.json` records the actual
command, source/log hashes, output, and 1.806-second execution. Its imports
are the root's already completed fresh core build at scientific checkpoint
`75e4c3be98db839646ffbb76fc0ac33649747c99`; the integrating root's new
full-packet replay is a separate event.

`SignedCarryReturns.sources.json` records the exact upstream head, paths,
SHA256 hashes and Git blob IDs for the two ported/interface source files.
The new adapter source SHA256 is
`0af50217b1da102d8fdaf7f9d61fedcdaad75cbf059452d02dcd8b82b59fe5d7`.

## 7. An unbounded gap-one resource lemma, without universal coverage

The continuation also gives the following written lemma. For the positive
minus map `S`, if `E>=1` and `z>2^(E-1)`, the trajectory from `z` makes at
least `E` even-input steps in finite time. Suppose otherwise. After its
last even step it would stay odd forever. If that odd tail starts at `w`,
then for every `j` its exact recurrence gives

\[
2^j S^j(w)=3^j(w-1)+2^j.
\]

Coprimality forces `2^j` to divide `w-1` for every `j`, hence `w=1`.
But an odd minus step never decreases a positive integer, and fewer than
`E` halvings cannot take `z>2^(E-1)` to one. This is a contradiction.
The proof makes no assumption about negative cycles or eventual negative
convergence.

For any carry `3^p q-c` with `p>=1,c>=0`, apply this to `z=3^p+c` and
`E=p`. A sufficiently long **actual supplied run of source gap ones**
spends all `p` powers: the target scaffold has made `p` even steps while
each source step is odd, so the exact relative budget gives final power
zero. The original positive target then lies below the literal retained
source and the existing common-grade rule applies. The required finite
run length depends on `(p,c)` and is not bounded uniformly here.

This does not give a universal alternative to the failed guards. An
arbitrary supplied cap-four certificate need not contain that run at the
required position, and no rank-preserving operation forcing such a run
has been proved. The resource lemma is therefore preserved as an
all-parameter written observation, not another asserted total dispatcher
or a new Lean module.
