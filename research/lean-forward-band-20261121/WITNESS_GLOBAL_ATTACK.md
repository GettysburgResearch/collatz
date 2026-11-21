# Complete source words, terminal gaps, and the remaining Mersenne query

**Status: the terminal-language results and exact path identities in sections
1–3 are proved in `lean/WitnessGlobal.lean`; the packet's execution receipt
records the actual kernel replay. Section 4 is a separate written analysis of
the attempted dispatcher. The global comparison selector remains OPEN.**

This attack uses the ordinary shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]

It works with an entire supplied convergence word, including its final state
one. It does not replace that word by a bounded parity observation.

## Sources and the attempted closing argument

The starting comparison kernel is PR177 at
`00a611094043afeb256d6532b477c0709e8ed270`, especially
`research/lean-exact-witness-global-20261121/lean/Collatz/{GapMultiset,GapComparison,GapHandoffs,LowGapToPsi}.lean`.
Its highest-changed-exponent order permits a removed large gap to pay for an
arbitrarily long list of smaller gaps. Its source and target splices have
literal arithmetic guards; no complete dispatcher is asserted there.

The complementary comparison is identified in this PR's earlier
`BandParityBridge.lean` at
`9010a8790535002b6d9ff92304f0ba289e2e98fe`. The current PR184 merger interface was
also inspected at `366dab89ee9548084ab9b5e4e90ff82abf287a20`, in
`research/lean-band-coupling-20261121/lean/OffsetHorizon.lean` and its packet
README. That interface requires an actual alternate history and a saving;
it does not supply a source-word rewrite for free.

The proposed global move was to transport the wanted comparison through an
arbitrary low-gap prefix, then spend the last genuine high gap. At that point
the *known* source really reaches one, so the final endpoint is much more
specific than the arbitrary endpoint in the published guarded resets. The
question is whether this specificity forces a terminating rewrite on the
wanted side.

The new module isolates two exact answers: a complete base language at final
gap four, and the actual unresolved terminal family for arbitrary high gaps.
It imports only the existing `ShellCover` foundation. No result from PR177 is
silently added as an axiom or copied with a changed hypothesis.

## 1. A full low-gap language has a finite terminal base

Write a gap word as a chain

\[
3x_i+1=2^{a_i}x_{i+1},\qquad a_i\ge1.
\]

`GapTrace n q word` retains every intermediate ordinary integer in this
chain. `trace_orbit` proves that its actual shortcut clock is the sum of the
gaps. For a complete word, the endpoint is one.

If every gap is at most three and the endpoint is one, then the source is
one. Backward induction proves this: an odd parent of one with gap in
\(\{1,2,3\}\) can only use gap two, and that parent is one again.
This is `low_complete_is_one`. Consequently, terminal copies of gap two are
only padding at the trivial odd cycle, and every nontrivial complete source
word has a genuine gap of at least four.

Now let the final genuine gap be four and let every preceding gap be at most
three. Immediately before that gap the source is five. The complete
low-gap predecessor tree of five is backward closed on the following set:

\[
\{3,5,7,9,11,13,17,19,25,29,33,45,51,77,205,273\}.
\]

The tree, arranged by odd-step distance to five, is:

| Distance | Sources |
|---:|---|
| 0 | 5 |
| 1 | 3, 13 |
| 2 | 17 |
| 3 | 11, 45 |
| 4 | 7, 29 |
| 5 | 9, 19, 77 |
| 6 | 25, 51, 205 |
| 7 | 33, 273 |

To check closure, for each listed endpoint \(q\), inspect every
\(a\in\{1,2,3\}\) for which \((2^a q-1)/3\) is a positive integer.
Every such parent is the listed node on the next row; the last row has no
such parent. This finite arithmetic statement is the induction step for
**all word lengths**. Seven is a theorem about the closed tree, not an
imposed exploration depth.

The Lean declarations `one_four_parent`, `low_trace_to_five`, and
`single_four_language` prove this closure and the depth bound, including
arbitrarily many terminal gap-two padding steps. `single_four_psi` proves
convergence of every wanted target \(2n-1\) in this whole language by
ordinary kernel-computed witnesses at its finite set of sources. The
longest of those displayed shortcut witnesses has length thirty.

This closes the entire one-four language. It does not close words containing
another gap at least four, or an arbitrary final gap.

## 2. The arbitrary terminal gap leaves an exact Mersenne query

Suppose

\[
3n+1=2^M,\qquad M\ge2.
\]

The source has the explicit complete shortcut witness \(T^M(n)=1\).
Its psi target satisfies the equally explicit path

\[
2n-1\longmapsto 2^M-2\longmapsto 2^{M-1}-1.
\]

Therefore

\[
\operatorname{Basin}(2n-1)
\iff \operatorname{Basin}(2^{M-1}-1).
\]

These are `terminal_gap_source`, `terminal_gap_psi_path`, and
`terminal_gap_psi_boundary`. For every even \(M\), the ordinary source
\(n=(2^M-1)/3\) exists, so the statement includes every odd-exponent
Mersenne number on the wanted side. At \(M\ge4\), that wanted endpoint is
at least seven; the fact that the known source is one after its supplied
clock does not make the wanted query terminal.

This identity is a positive reduction to a concrete family. It does not
assert that the Mersenne family fails to converge, or that no other reset
can solve it. It identifies the base family which the proposed last-gap
dispatcher still has to handle.

## 3. Actual arbitrarily long low-gap words retain that same boundary

The terminal issue is present after arbitrarily long **complete ordinary**
low-gap prefixes, not just after a hypothetical compatible word. Define

\[
A_0=1,\qquad
A_{k+1}=A_k+3^{k+1}A_k^2+3^{2k+1}A_k^3.
\]

Cubing the preceding identity gives, for every \(k\ge0\),

\[
4^{3^k}=1+3^{k+1}A_k.
\]

Put

\[
M_k=2\,3^k+2,\qquad N_k=1+4^{k+1}A_k.
\]

The source \(N_k\) has the complete gap word

\[
\underbrace{(2,\ldots,2)}_{k\text{ gaps}}\mathbin\Vert(M_k).
\]

Indeed, the first \(k\) gaps take
\(1+4^k s\) to \(1+3^k s\), with \(s=4A_k\), and

\[
3(1+3^k\,4A_k)+1=2^{M_k}.
\]

Each gap-two source move also carries the psi target through exactly two
shortcut steps. Thus the full, actual wanted path is

\[
T^{2k+2}(2N_k-1)=2^{M_k-1}-1.
\]

`long_terminal_certificate` and `long_terminal_psi_boundary` formalize these
statements for every \(k\), with the explicit coefficient recursion supplying
all integrality. In particular the source is already proved to converge;
there is no all-time realization hypothesis. The first sources are
\(N_0=5\), \(N_1=113\), and \(N_2=621377\), with final gaps
\(4,8,20\). These examples illustrate the theorem and are not its evidence.

The supplied source word can therefore be shortened completely and the
wanted side can still be the same nontrivial Mersenne boundary. The new
identities do not exclude a different rule that spends the large terminal
grade on an appropriately constructed known-source certificate.

## 4. The signed carry which a complete selector must pay

In a parallel attempt, track a known source \(3t+2\) against the wanted
source \(t\), with \(t\) odd. If the known source's next odd gap is one,
both actual sources take a single odd step and the pair keeps the form
\((3t'+2,t')\). If its gap is at least three, the two arms have an exact
ordinary merger. At gap two the pair becomes \((3m+1,m)\), with \(m\)
even. In the subcase \(m=2z\) with \(z\) odd, one further ordinary step on
both sides gives

\[
(\text{known }9z+2,\ \text{wanted }z).
\]

This is the same complementary comparison already identified by
`BandParityBridge`, rather than an independently discharged subproblem.
When both members are next moved through their odd step, the affine
correction changes sign:

\[
T(9z+2)=9T(z)-1\qquad(z\text{ odd}).
\]

Thus an induction preserving only a nonnegative affine correction is not a
complete dispatcher. A successful common rank must accommodate this signed
carry and the actual terminal Mersenne query, or supply a different ordinary
merger before those states. The new finite base and unbounded exact family
are available to that construction; neither is asserted to discharge its
universal coverage obligation.
