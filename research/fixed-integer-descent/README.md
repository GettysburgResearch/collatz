# Fixed ordinary sources: binary runs, merger demands, and interval records

**Status: exploratory research with proved local arguments and complete bounded
certificates. The Collatz conjecture is not resolved.** Claim-level agent
reconstructions are linked in the [investigation report](../../reports/2026-11-20-fixed-integer-descent/README.md).
They are not external mathematical acceptance or proof-assistant verification.

This pass targets the point where the recent inverse and merger programs
still stop: a conclusion about **every fixed positive ordinary integer**.
The strongest result is a complete decision and classification for a
bounded-complexity class of trajectories. Two further results improve the
local merger induction and the finite record mechanism. Their remaining
global assumptions are retained.

## 1. Binary one-runs give a finite core

Use the odd map

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

A one-run is a maximal block of consecutive ones in the ordinary binary
representation. Bounded one-run count permits arbitrarily long blocks of
ones, unlike bounded popcount. For example, every `2^a-1` has one run.

For every cap `R`, [RC-1--RC-3](arithmetic.md) construct a finite, effective
set `A_R` with the following property: an odd source with at most `R` runs
outside `A_R` must exceed that cap within a uniform number of actual odd
events. The proof cuts long zero-runs with a positive lower shadow and long
one-runs with a negative lower shadow, retaining the same positive source
throughout. Its homogeneous comparisons are `3^j u` and `3^j u-1`.

Consequently an ordinary positive orbit is eventually periodic if and only
if its binary run count is bounded. Every hypothetical escaping orbit must
exceed each fixed cap with bounded gaps after a sufficiently late time.
This is not a proof that run counts are bounded on arbitrary orbits.

The entire adaptive core through cap six was replayed, with a separate
inverse construction of the successful sources:

| Six-run certificate | Exact result |
|---|---:|
| Complete core sources | 19,371,072 |
| Sources reaching 1 without cap exit | 157,728 |
| Sources exiting the cap | 19,213,344 |
| Maximum core hitting clock | 107 odd events |
| Core witness attaining that clock | 74475 |
| Largest successful odd source | 68,719,605,301 |
| Nontrivial cycles within the cap | 0 |

The [independent modular certificate](modular_hitting.md) bounds every
outside-core exit by 21 odd events. Therefore **every positive odd input
starting with at most six one-runs reaches 1 or exceeds six runs within
107 odd events**. The proof and complete finite core justify the quantifier
over arbitrarily large inputs; it is not extrapolation from a numeric
search range. The analogous five-run clock is 68.

The classification does not assert convergence after cap exit. In fact,
[RC-4](arithmetic.md#6-the-uniform-sparse-run-descent-strengthening-is-false)
shows that a first-descent clock depending only on the initial run count
cannot exist: one-run Mersenne inputs have arbitrarily long initial
no-descent intervals.

The [rewriting transfer](rewriting.md) applies the six-run certificate to
all eleven Yolcu--Aaronson--Heule rules on properly encoded words with that
value guard. Its ordinal rank is below `omega^3`; the guard remains
essential, and the unrestricted string-rewriting problem is still open.

## 2. Infinite merger families with one smaller demand

For the shortcut map `T`, let `P(n)` mean that `n` and `3n` eventually meet
at independently chosen finite clocks. For an even integer `z`, put

\[
\operatorname{Good}(z)\iff
z/2^{v_2(z)}\equiv3^{v_2(z)}\pmod4.
\]

[FM-001--FM-003](mergers.md) give these exact implications:

| Guard | One sufficient smaller comparison |
|---|---|
| `n` odd, `n=2 mod3`, `Good(3n+1)` | `P((2n-1)/3)` |
| `n>1`, `n=1 mod16`, `Good(9n+7)` | `P((3n+1)/4)` |
| `n=3 mod16`, `Good(9n+5)` | `P((3n-1)/8)` |
| `n=25 mod64` | `P((9n-1)/32)` |

The first three accommodate unbounded valuations and corresponding
adaptive clocks. Eight compact certificates, combined with the pinned
PR #146 exclusion, eliminate 83 of 192 odd residue classes modulo 384
from containing a *least* failed tripling comparison. There are 35 new
classes beyond the inherited 48. This is not a density theorem for a
nonconvergent basin or a fraction of Collatz proved.

[FM-004](mergers.md) also proves that each pair of certified convergent
seeds `r,3r` generates a whole dyadic neighborhood where the smaller-demand
induction succeeds. The proof does not establish that these neighborhoods
cover every ordinary input. The parameter 9, for example, is outside the
four displayed guards even though its convergence is known by direct
replay.

## 3. A uniform translated-interval bound for one actual path

For any finite nonrepeating shortcut trajectory and any integer interval
of width `X`, [FID-DRIFT-001--005](drift.md) bound the number of its states
in that interval by an exact recursive integer function `F(X)`. For each

\[
H_2(\log_3 2)<\alpha<1,
\]

there is a finite constant `C_alpha`, uniform in the path and interval
location, such that `F(X)<=C_alpha X^alpha`. Explicit parameter margins
make that constant effective. In particular `alpha=19/20`
is certified by exact integer power comparisons. The constant for this
recursive bound is not evaluated numerically or claimed practical.

The key extra step is to apply the same occupancy bound to the low-odd-count
image intervals, whose states still belong to the same simple path.
The recursive widths strictly decrease. At width 4096 the exact recursive
bound is 2565, improving the one-pass value 2720.

Applied to the existing near-source coefficient-record window, this
replaces its trivial record count by `F(W_n)`. The explicit inherited
window gives `O(n^(741/800))`; its qualified sharper version gives
`O(n^(361/400))`. These improve a **conditional** stopping-or-repetition
clock. They do not prove the required coefficient crossing, exclude an
arbitrary cycle, or bound the mass of a predecessor basin.

## The remaining proof obligations

The run route needs a justified global control on run-cap increases and
exclusion of cycles outside the verified caps. The merger route needs
complete coverage by a successful well-founded guard. The record route
still needs totality of its coefficient-stopping blocks. None of those
missing statements is established here, and the three local improvements
are not silently combined into a complete proof.

Exact sources, bounded reports, review scopes, and execution receipts are
collected in the [investigation report](../../reports/2026-11-20-fixed-integer-descent/README.md).
