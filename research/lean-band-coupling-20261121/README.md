# Forward bands and smaller-source mergers

**Status: new finite transport, steering, return-clock and merger theorems;
the full Collatz theorem remains OPEN.** This packet attempts to continue the
actual-orbit band theorem from PR173 through its binary horizon. The constructive
route is to replace an expired offset history by a cheaper ordinary inverse
history, with a freely chosen reserve of powers of three.

The normalization throughout is the shortcut map

\[
T(n)=\begin{cases}n/2&n\equiv0\pmod2,\\(3n+1)/2&n\equiv1\pmod2.\end{cases}
\]

All inputs, offsets, partners and endpoints in the transport theorems are
ordinary natural numbers. No 2-adic limiting witness is used. No GRH assumption
is used. The theorem statements retain their actual hypotheses.

## Starting point: the new forward section

The upstream input is **PR173, head
`fa0c9e2a2851e6324391e39c17afcb5913185aec`**. Its four frozen files and SHA256
hashes are listed in [source-pins.json](source-pins.json).

Write \(d=\lfloor\log_2x\rfloor\). An odd positive integer is marked when

\[
(d+1)(x-2^d)\le70\,2^d.
\]

`ForwardSection.bounded_visit` proves that every positive ordinary source
\(n\) has a marked forward iterate at an ordinary clock

\[
t<4\lfloor\sqrt n\rfloor+\lfloor\log_2n\rfloor.
\]

This is a visit on each actual orbit. The source theorem also gives natural
density zero for the marked set. `SectionDynamics.collatz_iff_return_descent`
identifies the remaining forward-return descent statement exactly. The
upstream `RisingReturns` proves that a first marked return can increase by an
arbitrarily large factor. These are credited upstream inputs, not new claims
of this packet.

## 1. Tune the forcing clock to the binary horizon

[ClockSteering.lean](lean/ClockSteering.lean) separates the source theorem's
choice of square-root clock from its phase argument. For an arbitrary positive
odd-step budget \(N\), positive floor \(m\), and target phase \(\theta\),
`steer_window` finds \(0<q\le N\), with \(N+1\le4^q\), and \(j<q\), such
that either the odd orbit is below \(m\), or

\[
0\le\delta=\log_2 x_j-(\theta+z)
\le\frac3q+\frac jm
\qquad(z\in\mathbb Z).
\]

The term \(3/q\) is the rational rotation-grid error. The term \(j/m\)
bounds the actual positive logarithmic errors accumulated on that orbit.

If an odd source does not descend during this prefix, the hit is realized in
**fewer than \(2N\) ordinary shortcut clocks**. This follows from
\(2^t x_j\le4^j n\) and \(x_j\ge n\). We may therefore choose
\(2N\le d+1\) and keep the forced hit inside a \(d\)-bit parity shadow.

The integer \(z\) is retained. Choosing a phase immediately below the source
does not remove it: `no_descent_forces_height_gain` proves the actual resulting
height increase of at least \(1-\varepsilon\), under its stated precision
and non-descent hypotheses. The statement does not infer later descent from
that height increase.

## 2. Exact continuation past the binary horizon

[OffsetDescent.lean](lean/OffsetDescent.lean) makes the underlying parity
identity public. If \(p_t(r)\) counts odd shortcut steps before clock \(t\),
then for \(t\le d\),

\[
T^t(2^d+r)=3^{p_t(r)}2^{d-t}+T^t(r).
\]

In particular, any strict descent of \(r\) by clock \(d\) transports to
the lifted source. At clock \(d\), however, the difference becomes a power
of three:

\[
T^d(2^d+r)=3^p+y,
\qquad p=p_d(r),\quad y=T^d(r).
\]

Suppose an alternative ordinary history satisfies

\[
T^t(u)=y,\qquad a=p_t(u)\le p.
\]

Then the new source

\[
x=2^t3^{p-a}+u
\]

reaches **the same ordinary endpoint** as the original source. This is
`rebase_hits`, a finite merger theorem, not a heuristic about close trajectories.
Its exact smaller-source test is

\[
2^t3^p+3^a u<3^a(2^d+r).
\]

Replaying the original history gives \(x=2^d+r\) exactly, so a useful
induction step requires a genuinely different history or a different split.

### Additional ternary reserve

The more flexible split is

\[
n=2^h3^s v+r,\qquad v>0,
\]

where \(r\ge0\) need not be smaller than \(2^h\). Put
\(p=p_h(r)\), \(y=T^h(r)\). The new theorem proves

\[
T^h(n)=3^{p+s}v+y.
\]

An alternative history \(T^t(u)=y\) with \(a=p_t(u)\le p+s\) now gives

\[
\boxed{x=2^t3^{p+s-a}v+u,\qquad T^t(x)=T^h(n).}
\]

The extra \(s\) permits inverse odd steps that the original top-power-of-two
split disallowed. The strict saving is again an exact integer inequality:

\[
2^t3^{p+s}v+3^a u<3^a n.
\]

The library proves transfer of `Basin` through this merger and its precise
strong-induction consequence. It does not assert existence of a successful
alternative history for every source.

## 3. An infinite obstruction family has a constructive smaller partner

[OffsetHorizon.lean](lean/OffsetHorizon.lean) proves that for every \(m\ge2\),

\[
n_m=2^{4m}+2^{3m}-1
\]

is marked, has binary length exponent \(4m\), and satisfies

\[
T^t(n_m)\ge n_m\qquad(0\le t\le4m).
\]

Its offset is only about \(n_m^{3/4}\). Thus even a polynomially small offset
does not force descent within the native binary horizon.

[RisingMerge.lean](lean/RisingMerge.lean) supplies a constructive way past that
failure for **every member of this family**:

* If \(m\) is odd, \(x=(2n_m-1)/3\) is positive, smaller than \(n_m\),
  and \(T(x)=n_m\).
* If \(m\) is even, \(x=(3n_m-1)/4\) is positive, smaller than \(n_m\),
  and \(T^{3m}(x)=T^{3m+2}(n_m)\).

The even case is an instance of a stronger generic merger. For
\(n=2^k u-1\), \(k\ge2\), \(u>0\), if
\(3^{k-1}u\equiv3\pmod4\), then

\[
x=2^{k-2}(3u)-1=\frac{3n-1}{4}<n,
\qquad T^k(x)=T^{k+2}(n).
\]

These statements do not assume that either trajectory converges. They show
that the covered source cannot be the least positive counterexample. Their
`Basin` corollaries explicitly assume convergence of the smaller sources.

The examples include \(319\), which has no descent through clock eight but
has the smaller partner \(239\):
\(T^6(239)=T^8(319)=911\).

## 4. A universal lower bound on marked return clocks

[ReturnClock.lean](lean/ReturnClock.lean) proves

\[
n\text{ marked},\quad t>0,\quad T^t(n)\text{ marked}
\quad\Longrightarrow\quad
\lfloor\log_2 n\rfloor<1024\,4^t.
\]

This applies to all positive marked returns, in either height direction.
Its proof uses the exact affine equation
\(2^tT^t(n)=An+B\), with \(3\mid A\) and \(A,B\le3^t\).
If both endpoint bands were too narrow at a fixed clock, their main dyadic
terms would force \(A\) to be a power of two, an integer contradiction.

Consequently every fixed positive-clock budget eventually fails to contain
the first return from sufficiently large marked sources. This is compatible
with both increasing and decreasing returns; it supplies no sign for the
cumulative height change.

## 5. The exact remaining global target

[SourceBoundedMerge.lean](lean/SourceBoundedMerge.lean) makes the induction
scope explicit. Start from an arbitrary ordinary source \(n>1\), and let
\(q\) be its first marked forward point. A sufficient and necessary global
merger criterion is the existence of

\[
0<x<n,\qquad T^a(x)=T^b(q)
\]

for some ordinary clocks \(a,b\), **for every original source \(n>1\)**.
The comparison is with the original source \(n\). A saving only relative to
the later marked point \(q\), which can be larger, does not close that
induction. Likewise, a smaller unmarked partner cannot simply be inserted
into an induction whose hypothesis only covers smaller marked numbers.

The upstream alternative remains valid: prove eventual strict descent of
the actual induced marked return orbit. This packet proves neither universal
coverage of the source-bounded merger criterion nor that return descent.

The first unsupported step in the constructive route is therefore precise:
**produce a successful ordinary inverse/merger history with a saving below
the original source, or prove a well-founded rank that supplies the same
induction.** Phase forcing and the splice algebra do not by themselves
establish that existence statement.

### A second valid route: keep induction inside the marked set

The follow-up [LowerMarkedMerger.lean](lean/LowerMarkedMerger.lean) builds on
PR183's lower-mark height estimate at frozen head
`8659cf62ac685540cadeef320e596c852fbb0959`. Its source theorem assumes a
small directed forward endpoint. The new extension permits a positive
ordinary merger partner on any branch entering the same orbit.

Suppose \(T^a(x)=T^b(n)\), \(x>0\), \(n>0\), and

\[
4\lfloor\sqrt x\rfloor+2\lfloor\log_2x\rfloor
\le\lfloor\log_2n\rfloor.
\]

Then there is a marked \(y=T^t(x)<n\), with the explicit physical merger

\[
T^a(y)=T^{b+t}(n),\qquad \operatorname{Basin}(n)
\Longleftrightarrow\operatorname{Basin}(y).
\]

This need not put \(y\) on the forward orbit of \(n\). It gives the lower
marked component partner that strong induction on marked values actually
requires. The module proves the exact equivalence

\[
\mathrm{Universal}\quad\Longleftrightarrow\quad
\forall n\text{ marked},\ n>1:\quad
\exists y<n\text{ marked},\ \exists a,b:\ T^a(y)=T^b(n).
\]

It also proves an equivalent quantitative cover: every marked \(n\ge16\)
has an ordinary merger partner satisfying the displayed size budget. The
positive inputs below 16 are discharged by a kernel-checked finite proof.
The existence part of this quantitative cover remains open. The budget is
far stronger than merely \(x<n\); it is not silently assumed for the
partners in the earlier infinite-family theorem.

[Latest connections](LATEST_CONNECTIONS.md) records the targeted combination
attempts with simultaneous PR180, PR182 and PR183 updates. Their selected
contraction exponents, predecessor populations, and directed descent guards
are kept distinct from the required prescribed-source coverage.

## Exact finite search and replay

[reserve_search.py](experiments/reserve_search.py) searches finite inverse
trees using exact integers. Its successful witnesses are independently
replayed along both ordinary forward paths. Its fixed-decomposition depth
bound and pruning inequality are documented in the program. A node cap and
an exhausted finite menu are reported explicitly. The optional `partner_bound`
parameter enforces a bound below an earlier original source throughout the
success test, depth bound and pruning; a caller must separately supply the
actual forward visit from that source to the later input.

[reserve_witnesses.json](experiments/reserve_witnesses.json) records a focused
stress test on \(2^d+27\). The reserved split repairs some native-splice
failures, while several tested finite menus remain unresolved. Those outcomes
are not convergence counterexamples or a universal coverage claim. Some
successful repairs are already simple expanding inverse words; the packet
does not claim a new arithmetic phenomenon merely from finding them.
The small-clock cases \(d\le64\) test the merger mechanism: the section is
automatic on every octave with \(d\le69\). Additional \(d=128,256\) cases
lie in the genuinely narrowing regime. Their successful native certificates
do not establish coverage of the rest of those bands.

For example, the Lean-checked reserved witness is

\[
283=2^4\cdot3^2+139,\quad T^7(123)=T^4(139),\quad
x=2^7+123=251<283,
\]

and \(T^7(251)=T^4(283)\). The same partner satisfies the shorter direct
predecessor identity \(T^3(251)=283\).

## Reproduce the proof checks

Use Lean **4.34.1** and an already built mathlib checkout at
`d13f23b723b8a846827a245b89c10fc7d3f11612`:

```sh
python -X utf8 -B research/lean-band-coupling-20261121/check.py \
  --lean /absolute/path/to/lean \
  --mathlib /absolute/path/to/mathlib4 \
  --build-dir /absolute/path/outside/checkout/band-build
```

`check.py` first verifies all upstream source hashes. It then emits an explicit
module-format port into the external build directory: `module`, `public
import`, an exposed public section, and the listed visibility exports. It
does **not** change a definition body or a proof body. This avoids Lean
4.34.1's costly legacy-mode import of Mathlib private modules. The generated
diff and both original/generated source hashes are saved with the receipt.

The new modules compile with warnings treated as errors. `Audit.lean` prints
the dependencies of the central statements; the checker rejects `sorryAx`
and any reported axiom outside `propext`, `Classical.choice`, and `Quot.sound`.
These standard logical foundations are distinguished from an unproved
Collatz or coverage axiom.

The complete-checkout repository integrity command is separate:

```sh
python -X utf8 -B tools/validate.py
```

Exact execution receipts belong in `reports/lean-band-coupling-20261121/`.
Repository integrity is not used as evidence for a mathematical theorem.
