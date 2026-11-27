# From a finite carry scan to every later synchronized clock

**KERNEL-CHECKED finite arithmetic and an all-clock implication.** The new
module [FrozenPeakSeparation.lean](FrozenPeakSeparation.lean) uses the actual
positive shortcut map

\[
T(x)=\begin{cases}x/2&x\text{ even},\\(3x+1)/2&x\text{ odd},\end{cases}
\]

and its actual odd-departure count \(p_h(x)\). It does not assume that the
Collatz conjecture holds. Its two project imports are the current packet's
[finite offset scan](../ordinary/FrozenOffset.lean) and
[physical clock identities](../ordinary/ClockSeparation.lean).

## Carry growth supplies the missing clock quantifier

Define the signed carry

\[
c_h(x)=2^hT^h(x)-3^{p_h(x)}(x+1).
\]

At an even departure it stays unchanged. At an odd departure at time \(h\),
it changes to \(3c_h(x)+2^h\). Consequently, for an even positive source
\(x\), one has \(c_h(x)\ge-1\) for \(h\ge1\), and the carry is
nondecreasing from that time onward. If

\[
c_H(x)+3<2^K,\qquad 1\le K\le H,
\]

then there is no odd departure at any time \(K\le i<H\). Indeed, an odd
departure there would make the next carry at least \(2^i-3\), already too
large. In particular \(p_H(x)=p_K(x)\). The declarations `carry_lower`,
`carry_monotone`, `no_late_odds`, and `frozen_count` prove these statements
for every supplied clock, without a clock search.

## The original Mersenne peaks

Write \(P_j=3^j-1\), and let \(C\) be the exact positive integer `frozenC`
in `FrozenOffset.lean`. The previously checked anchor has

\[
p_{498}(P_{173})=240,\qquad
2^{498}T^{498}(P_{173})=3^{413}+C,\qquad C+3<2^{497}.
\]

The theorem `no_earlier_paid_peak` proves the following implication:

> For any natural numbers \(H,j,t\) with \(H\ge498\) and \(t<j\),
> suppose \(p_H(P_j)=240\) and \(c_H(P_j)=C\). Then the two equalities
> \(T^H(P_j)=T^H(P_t)\) and
> \(j+p_H(P_j)=t+p_H(P_t)\) cannot both hold.

The second equality is the precise augmented-grade payment; the theorem
does not silently grant it from an ungraded physical meeting. Equal physical
endpoints and paid grades would force the earlier peak to have the same
carry \(C\). Carry growth then gives

\[
p_H(P_t)=p_{497}(P_t)\le497,
\qquad 1\le d=j-t\le257.
\]

The native carry identity also forces
\(3^j\equiv3^{173}\pmod{2^{498}}\). Cancelling the odd power \(3^d\)
places the earlier leading value in the exact residue
\(3^{173-d}\pmod{2^{498}}\). Odd-count invariance under an ordinary
binary lift now contradicts the existing 257-entry scan. Thus that finite
scan excludes every later synchronized paid clock under the displayed
native carry and count hypotheses.

## Verification and limit

A direct strict compilation with Lean 4.34.1 passed on 27 November 2026.
The eight selected declarations report only `propext`, `Classical.choice`
and `Quot.sound` (some use fewer). The final packet replay is recorded in
the packet's common report, when run; this direct compile alone is not
described as that replay.

The hypotheses that the **actual positive source** retains carry \(C\) and
count 240 are essential. They are not asserted at all future clocks for a
fixed positive source. The module does not exclude unequal-clock meetings,
unpaid meetings, eventual descent, or the full original family. Its role is
the exact finite-to-all-clock step in the
[sharp odd-power obstruction](../ordinary/SHARP_ODD_POWER.md).
