# Complete finite birth accounting for the binary prefix criterion

**LEAN-CHECKED IMPLICATIONS AND EQUIVALENCE. The universal estimate remains OPEN.**

The map throughout is the shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

Write \(q_j(x)\) for the number of odd departures among the first \(j\) steps.
The inherited gate and its actual ordinary-source sum are

\[
G_N(x)\iff 5j\le8q_j(x)\quad(0\le j\le N),\qquad
H_N=\sum_{\substack{0<x<2^N\\G_N(x)}}\frac1x.
\]

PR201 at `d21bac748e705a64b6b57a7996a8ad6282f0bcbf`
already proves in Lean that a strict finite inequality \(H_N<1/B\), with
\(N>0\), certifies convergence of every positive input at most \(B\).
It also supplies the local reserve inequality and a written converse of
the universal criterion. This packet completes that converse inside Lean,
including the population of ordinary representatives introduced at all
later depths. The original six dependency modules are byte-identical and
listed in [their source manifest](../imports/pr201/SOURCES.json).

## What is now formal

The full equivalence is

\[
\bigl(\forall x>0\;\exists h\;T^h(x)=1\bigr)
\quad\Longleftrightarrow\quad
\bigl(\forall B>0\;\exists N>0\;H_N<1/B\bigr).
\]

This is `FiniteExtinction.collatz_iff_small_mass`. Neither side is
established universally. No external analytic theorem is a premise of the
equivalence. In particular, this proof does not replace a specified
ordinary input with a random parity sequence or with a changing witness.

There is a stronger finite transfer with an explicit time budget. Suppose
every positive \(x<2^M\) reaches 1 by a supplied clock \(H\). Set

\[
E(H)=H+2\lfloor H/38\rfloor+2.
\]

For every \(N\ge\max(M,E(H))\),

\[
H_N+R_N\le R_M,
\tag{1}
\]

where \(R_N\) is a fully specified finite rational reserve below. In
particular, if \(M=8k\),

\[
H_N+R_N\le (24k+5)\left(\frac{6561}{8192}\right)^k.
\tag{2}
\]

The finite supplied hit budget is essential. Equations (1)–(2) do not
assert that such a budget has been proved for every cutoff. The sharper
clock theorem is in [HitClock.lean](HitClock.lean); the initial, simpler
\(5H+2\) transfer remains in [FiniteExtinction.lean](FiniteExtinction.lean).

## The reserve pays for every later representative

For an accepted residue, define its debt \(d_N(x)=8q_N(x)-5N\). Let

\[
P_N=2^{-N}\#\{0\le x<2^N:G_N(x)\},\qquad
R_N=2^{-N}\sum_{\substack{0\le x<2^N\\G_N(x)}}(d_N(x)+5).
\]

The term \(x=0\) is intentionally permitted in this probability and
reserve. It matters at depth zero, where \(R_0=5\); its reciprocal mass
is zero. At positive depths it fails the gate.

The two extensions of a depth-\(N\) residue are \(x\) and \(x+2^N\).
Their first \(N\) parity digits agree, and their next digits are opposite.
An odd digit changes debt by \(+3\); an even digit changes it by \(-5\),
killing the branch if it becomes negative. The inherited local inequality
therefore sums to the **actual complete-population** inequality

\[
P_N+R_{N+1}\le R_N.
\tag{3}
\]

The new representative has weight
\(1/(x+2^N)\le2^{-N}\). Fix any source cutoff \(2^M\), and let

\[
J_{M,N}=\sum_{\substack{2^M\le x<2^N\\G_N(x)}}1/x.
\]

There is no assumption about the lifetimes of these sources. Directly
summing the two extensions proves
\(J_{M,N+1}\le J_{M,N}+P_N\). Combining this with (3), starting from
\(J_{M,M}=0\), gives

\[
J_{M,N}+R_N\le R_M\qquad(N\ge M).
\tag{4}
\]

This is the step that prevents an interchange of a growing source cutoff
with a time limit from hiding new ordinary mass.
[BirthReserve.lean](BirthReserve.lean) proves (3)–(4), with the exact finite
definitions used by the imported criterion.

## Explicit decay and the actual hit clock

Pairing the two binary extensions also proves the exact moment identity

\[
\sum_{0\le x<2^N}2^{q_N(x)}=3^N.
\]

At depth \(8k\), the gate requires \(q_{8k}\ge5k\). Hence
\(P_{8k}\le(6561/8192)^k\). Since accepted debt is at most \(3N\),

\[
R_{8k}\le(24k+5)(6561/8192)^k
          \le128(31/32)^k.
\tag{5}
\]

The last, looser geometric bound makes the Archimedean choice of a finite
depth entirely elementary in Lean. The moment calculation is in
[BinaryCylinder.lean](BinaryCylinder.lean).

If a positive ordinary source reaches 1 at time \(h\), its exact affine
identity gives \(3^{q_h(x)}\le2^h\). The integer comparison
\(2^{19}\le3^{12}\) therefore implies \(19q_h(x)\le12h\). Its debt at
that time is at most \(h/19\). Every subsequent pair of steps on
\(1\to2\to1\) removes two units of debt, so the gate has failed by
\(E(h)\). Once all the finitely supplied small sources have failed,
\(H_N=J_{M,N}\), and (4) gives (1).

Assuming universal convergence, any fixed finite cutoff has a finite
maximum hit time. Choose \(M=8k\) to make (5) as small as required, then
take a later depth after that finite budget. This proves the previously
written converse with all births accounted for. The forward implication
is exactly PR201's inherited least-bad-source argument.

## What the reserve cannot do

The actual potential \(V_N=H_N+R_N\) is nonincreasing, with
\(0\le V_N\le5\). This is proved in
[PotentialBoundary.lean](PotentialBoundary.lean), rather than inferred from
an empirical plot.

The same file proves a limitation on a possible bootstrap. The source
\(2^M-1\) has \(M\) consecutive odd departures, and passes every gate
prefix through \(M\). Its reserve contribution alone gives

\[
R_M\ge\frac{3M+5}{2^M}.
\]

Consequently, for any \(B\ge2^M\), one has \(1/B\le R_M\). A bound
of the form \(H_N\le R_M\), by itself, cannot meet the strict reciprocal
certificate for this same or a larger source range. This does not
preclude a stronger estimate of the actual \(H_N\). It identifies the
precise additional work a successful argument would need.

The outstanding task is to prove smallness of the finite ordinary sums
without importing universal convergence or an equally strong hypothesis.
Decay of the reserve, of the fraction of accepted residues, or of a
random trajectory probability leaves a possible fixed ordinary atom
uncontrolled.

## Unconditional packing of a simple physical orbit

[OrbitPacking.lean](OrbitPacking.lean) applies the same exact binary
moment to an actual finite trajectory whose vertices are distinct. For
every integer \(k\ge0\), such a trajectory has at most

\[
                  4\cdot6561^k
\]

vertices below \(8192^k\). The proof separates sources by their odd count
in the next \(13k\) steps. The high-count part is controlled by the
binary moment; the low-count part has distinct small forward images.
The last \(13k\) positions are discarded before claiming injectivity,
so a later cycle creates no hidden assumption.

Finite geometric bands then bound the reciprocal occupation of high
vertices, uniformly in the length of a simple trajectory. The escape
packet formalizes this transfer, the resulting positive lower bound on
each actual first-arrival mark, and the unconditional equivalence
between boundedness of all ordinary trajectories and uniform vanishing
of complete finite first-arrival rows at large odd targets. See
[HIGH_TARGET_ROWS.md](../escape/HIGH_TARGET_ROWS.md) and
[TargetExtinction.lean](../escape/TargetExtinction.lean). The target-row
vanishing estimate remains open; boundedness also permits finite cycles.

## A separate constructive phase theorem and exact examples

[PhaseNet.lean](PhaseNet.lean) proves the irrationality of
\(\log 3/\log 2\) and the following finite, uniform approximation statement:
for every \(\epsilon>0\), some finite \(D\) satisfies

\[
\forall u\ge1\quad\exists d\le D,\ m\ge0:
\qquad u<2^m/3^d<(1+\epsilon)u.
\]

The proof uses density of a two-generator additive subgroup and a finite
subcover of one compact interval. It assumes no quantitative irrationality
estimate. Combined with the actual inverse ladder and finite-gap routing,
it supplies the relative-window constructions in the other two packets.
This is a changing-source existence theorem, separate from the universal
finite-mass problem above.

[PhaseResidues.lean](PhaseResidues.lean) preserves independent requested
residues of both exponents. [PhaseMultiples.lean](PhaseMultiples.lean)
also restricts the ternary exponent to a prescribed positive multiple
that is congruent to one modulo the grade modulus. The latter feeds the
native ratio-five ladder: its physical macro groups have exactly
\(2Q+1\) odd departures on each arm. These remain finite existence
theorems with no quantitative irrationality-measure premise.

[fast_pair_witness.py](fast_pair_witness.py) independently implements the
finite-gap cylinder rows, the exact two-gap residue address, and a finite
inverse ladder using integers and rational comparisons throughout. It then
literally replays both sources to their first visit to 1. The default
certificates are:

| Gap | Required lower-source class | Source bit length | Common first-hit clock | Common odd departures |
| --- | --- | ---: | ---: | ---: |
| 1 | Unrestricted | 1,625 | 1,634 | 6 |
| 3 | 2 modulo 3 | 1,772 | 1,781 | 6 |
| 7 | 1 modulo 3 | 2,099 | 2,108 | 6 |
| 13 | 0 modulo 3 | 2,100 | 2,109 | 6 |

Each complete pair lies in its specified interval \([X,1.1X)\); its
clock is \(\lfloor\log_2 X\rfloor+10\). The finite phase mesh has depth
256 and is certified by exact multiplicative gap comparisons. Full
decimal sources, interval endpoints, trajectory hashes, and construction
parameters are in the [certificate receipt](../../../reports/astra-infinite-descent-20261127/root/FAST_PAIR_WITNESSES.json).
The generator uses explicit checks rather than Python assertions; normal
and optimized Python runs produced byte-identical receipts. Four selected
successful pairs are not evidence that all positive integers converge.
