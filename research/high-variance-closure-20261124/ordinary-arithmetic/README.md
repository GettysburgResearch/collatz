# An ordinary arithmetic companion and mergers across boundary levels

**Collatz remains OPEN.** This continuation starts at
`a30402b7849c437edf245974d9f436d1f105e08e` and attacks three remaining
steps: arithmetic finiteness at one positive integer, persistent component
boundaries, and the unpaid return cost of the previous proper score.
Three GPT-6.2 Astra research streams and the coordinator developed and
independently reconstructed the arguments. The new natural-number and
pair-process kernels have executed Lean evidence; their full analytic
applications are written proofs.

The strongest new results are a rationality classification for one
always-defined dyadic scalar, a uniform bound on its agreement with an
incorrect triadic candidate, and a merger argument that eliminates
specified persistent boundary rays even when their rational comparison
orbits are disjoint. A proposed reset repair is also decisively refuted
on actual ordinary edges, then replaced by a score with a smaller but
still unpaid loss elsewhere.

## 1. A second arithmetic coordinate with a contracting joint height

Use the shortcut `T(n)=n/2` at even inputs and `(3n+1)/2` at odd inputs.
Write `e_i=T^i(n) mod 2`, `P_i=sum_{j<i} e_j`, and retain the preceding
real series weights

\[
 A_i(n)=2^{i+P_i(n)}/3^i.
\]

Their dyadic companion is defined **without assuming convergence**:

\[
 D(n)=\sum_{i\ge0}e_iA_i(n)\in\mathbf Z_2.
\]

The written proof establishes, for every positive ordinary integer,

\[
 \boxed{D(n)\in\mathbf Q\iff n\text{ is eventually periodic},}
 \qquad
 \boxed{D(n)\in\mathbf Z[1/3]\iff\exists k,\ T^k(n)=1.}
\]

Here `Z[1/3]` means the rational numbers whose reduced denominator is a
power of three. The series converges in the 2-adic sense at every input;
its membership in that rational ring is not automatic.

The arithmetic mechanism is a joint height, not an assumption about
typical parities. If a rational companion is eventually negative, put
`w=-D/3`. Its actual updates, coupled to the ordinary source `x`, are

\[
 (x,w)\longmapsto
 \begin{cases}
 (x/2,3w/2),&x\text{ even},\\
 ((3x+1)/2,(3w+1)/4),&x\text{ odd}.
 \end{cases}
\]

For `x>=20` and `w>=64`, the height `x^2 w^3` contracts in both branches.
The even multiplier is `27/32`; the odd multiplier is at most
`26750481097/26843545600<1`. On an ordinary orbit that is not eventually
periodic, rational `D(n)` would make the positive tail values `w_i`
distinct with bounded denominators. Both `x_i` and `w_i` would tend to
infinity, contradicting this contraction.
For an integral companion, a finite check below 64 and the impossibility
of an all-odd positive orbit exclude the remaining cases.

Lean proves the **all-time impossibility of the positive integral
companion above the physical floor**, as well as the scaled numerator
contraction and the finite small-companion check. The dyadic construction
and the two displayed equivalences remain written mathematics.

[Full proof and arithmetic boundary](DYADIC_COMPANION.md)
· [Lean integer consumer](lean/DyadicCompanion.lean).

### An incorrect candidate cannot match arbitrarily many bits

For `a=A/3^h`, put

\[
 N=5+h+\lceil\log_2(n+1)\rceil+\lceil\log_2(|A|+2)\rceil.
\]

The proof gives the uniform, deliberately coarse bound

\[
 D(n)\ne a\quad\Longrightarrow\quad
 v_2(D(n)-a)\le10^6N.
\]

Enough matching bits force the trial companion to follow the same legal
ordinary branches. Either the physical orbit reaches the checked base
early, or the now-integral trial and the joint height force it there.
Rational height bounds finish the comparison at that base. This applies
to the supplied integer even if its fate is unknown. It decides equality
with each specified candidate, but it does not bound a successful
candidate's numerator or denominator for every `n`.

[Effective separation and its limit](TRIADIC_SEPARATION.md).

## 2. Merging across different levels removes a real boundary candidate

For any integer `s>=0` and signed integer `d`, every binary residue class
of the parameter `u` has a refining class on which the two arms
`u,3^s u+d` merge after a fixed finite common clock. The proof is
deterministic: reduce the affine grade, then the absolute offset. Lean
checks reachability of the absorbing state for **every** canonical
pair-process state, not just a finite list of offsets.

This permits a different comparison of a purported persistent dyadic
boundary. If a left rational seed and a right rational seed are both
eventually periodic, each with positive odd count per period, choose
different dyadic levels so their odd-count increments agree. Their
ordinary endpoints become fixed affine arms along one multiplicative
parameter orbit. Powers of three cover an open binary residue class;
the finite merger continuation then applies to a single actual pair
from the original fixed ordinary root.

In particular, the repeating address `1011 1011 ...`, which passes the
earlier forbidden-even-gap test, **cannot support a persistent ordinary
boundary**. Its left and right rational seeds enter different cycles,
with odd frequencies `1/3` and `3/5`. At levels `8+36h` and `8+20h`
their endpoints have equal odd grade `5+12h` and differ by exactly three.
This alignment is the step that permits an actual merger.

The finite controls give an explicit fixed-root witness: at root `17`,
left level `224` and right level `128` merge ten physical steps after
their respective native clocks. An exact residue computation also
certifies that **9,209 repetitions** of `1011` are forbidden after any
different preceding block of four bits. That numerical bound is a
Python certificate, not a Lean theorem.

There is a substantial early-clock obstruction on the same ray: for
each fixed root and every `0<=delta<4/15`, the two adjacent endpoints at
each sufficiently high level `i` have no meeting at any two physical
clocks up to `(1+delta)i`.
Only this quantitative delay uses a fixed two-logarithm theorem. The
merger across different levels and the exclusion of the periodic ray do
not use it.

The higher pure-triadic-denominator case is included as an independent
application, with its overlap explicitly credited: the prior forbidden
word already excluded it. Zero-grade seed degeneracies and general
aperiodic addresses remain unresolved.

[Statement, proof, prior overlap and finite-delay boundary](PERIODIC_BOUNDARIES.md)
· [Lean reachability and exact lifts](lean/PeriodicBoundary.lean).

A terminal extension keeps the ordinary center `b` fixed: every exponent
arithmetic progression contains a subprogression on which
`2^k b-1`, `2^(2k)b+1` and `2^(2k+1)b+1` all share a common future.
Thus the two punctured sides cannot have different eventual component
colors. This does not prove that either side shares the center's own
component. [Exact terminal recurrence](TERMINAL_RECURRENCE.md).

## 3. The previous reset toll has unbounded losses at level one

For **every** allowed separated cutoff bank and every positive summable
weight sequence giving a finite `G`, there are arbitrarily large genuine
nonperiodic ordinary edges `x -> Tx` with

\[
 J(x)=1,\qquad b_*(x)=b_*(Tx),\qquad t_1(Tx)\ge j+1,
 \qquad j\longrightarrow\infty.
\]

Thus the proposed score has exact debit

\[
 R_*(x)-R_*(Tx)=4\bigl(W_2-w_1t_1(Tx)\bigr)
 \le4W_2-4w_1(j+1)\longrightarrow-\infty.
\]

The proof constructs two ordinary branches with a prescribed later
collision; at least one whole tested prefix is nonperiodic. Unique
incoming edges at `x=8 mod 18` force the complete ancestor toll to be
equal at both endpoints. The construction uses different witnesses as
`j` grows and supplies no divergent orbit.

A new signed ancestor infimum is finite and proper and **does** pay the
whole refill at every marked edge, including periodic sources. It
allows a loss of

\[
 v(x)=\frac1{(K+\log(x+1))\log(K+\log(x+1))}
\]

on unmarked edges. Although this is `o(1/log x)`, its sum still diverges
along every infinite positive trajectory. Actual unmarked edges attain
that loss. The repair therefore does not prove descent.

A separate fixed-source theorem shows that strict improvements in
ancestor minimization occur on only `O_x(N^(1-epsilon))` dates of any
one hypothetical escape. It uses the pinned orbit-occupation bound
only on that orbit, never on its predecessor basin. The number of
discounts is controlled; their total size is not.

[Unbounded reset counterfamily and signed repair](RESET_EXIT.md)
· [Fixed-source origin count](ORIGIN_BIAS.md)
· [Lean ancestor equations and nonperiodic branch](lean/ResetAncestor.lean).

## 4. Further direct construction tests

The local smooth-bound attempt fails already on convergent ordinary
sources. In each fixed residue modulus there are source/endpoint pairs
arbitrarily close in relative size but forcing arbitrarily large ratios
in every finite nonnegative supersolution. A second construction gives
consecutive convergent integers with real series values tending to
infinity and to the global infimum `3`, respectively. The first uses
Monks's arithmetic-progression theorem; the second retains its stated
source-qualified almost-sure affine-merger input.

The coordinator also constructed a measure on negative **integer**
ancestors with a finite first height moment. Its potential is finite at
every positive integer, independently of convergence. The required
supersolution inequality fails because odd pullbacks require rational
poles absent from that measure. The argument excludes every measure in
that discrete finite-first-moment class, including sublinear additive
repairs. It does not exclude the original diffuse measure.

[Ordinary oscillation](ORDINARY_OSCILLATION.md)
· [Finite negative-integer potential and exact failure](NEGATIVE_INTEGER_KERNEL.md).

## Verification and the remaining step

The fresh replay compiles the three new modules and both pinned project
dependencies, from copied sources in an empty directory, using Lean
4.34.1 with warnings as errors and `autoImplicit=false`. It audits
**11 new public declarations and 10 dependency declarations**. Only
standard Lean axioms are accepted. Four finite control programs are run
in normal and optimized Python, with exact paired output comparison.
The dependency closure uses the pinned prebuilt Mathlib/package runtime.

```sh
python -X utf8 -B research/high-variance-closure-20261124/ordinary-arithmetic/checks/replay.py \
  --lean /path/to/lean-4.34.1/bin/lean \
  --mathlib /path/to/mathlib \
  --receipt /tmp/ordinary-arithmetic-replay.json
```

The infinite dyadic, approximation, periodic-address, marker and
asymptotic results are **written proofs with independent reconstruction**,
not full Lean formalizations. The finite controls do not verify those
infinite conclusions. [Sources](SOURCES.json) ·
[Exact execution receipt](../../../reports/2026-11-24-high-variance-closure/ordinary-arithmetic/REPLAY.json)
· [Coordinator reconstruction](../../../reports/2026-11-24-high-variance-closure/ordinary-arithmetic/ROOT_REVIEW.md).

No argument here proves `D(n) in Z[1/3]` for every positive ordinary
integer, eliminates every persistent boundary, or pays all losses in
one finite nonnegative score. Those are the still-missing universal
steps. The arithmetic criterion and boundary family are not presented
as a completed Collatz proof.
