# Round ten: ordinary towers, exact-clock tails and ordered cycle bands

**Collatz remains OPEN. This packet does not supply a complete proof.**
Three GPT-6.2 Astra agents, each explicitly run at `ultra` reasoning effort,
pursued ordinary descent, exact-row analysis and cycle arithmetic. The root
reconstructed the main deductions, added the ordinary minimum-source Lean
assembly, and rebuilt the seven project modules. The strongest new cycle
conclusion concerns every nonzero sorted-rank shift. The analytic bounds now
meet on the same hypothetical ordinary cycle; they remain compatible.

[Checked ordinary assembly](formal/README.md) ·
[Frozen repository intake](../../../reports/astra-global-closure-20261124/round10/INTAKE.md) ·
[Root review](../../../reports/astra-global-closure-20261124/round10/ROOT_REVIEW.md) ·
[Source ledger](SOURCES.json)

## 1. Short meetings and a family of longer physical returns

Use the shortcut map \(T(2v)=v\), \(T(2v+1)=3v+2\). Let
\(x=3^r w\), with \(w>0\) coprime to six. A literal lower source is
\(3^j b\) with \(0<b<w\), or with \(b=w\) and \(j<r\).
If \(2H\le r\), every meeting
\[
T^f x=T^h(3^j b),\qquad f,h\le H,
\]
must have \(b=w\) and \(f=h\). More precisely, such a meeting exists
exactly when an actual parity prefix has another word with the same length
and affine constant, but a larger odd count. This covers all literal lower
bases, not a selected finite list. Both directions are checked in Lean.

The proof puts both actual path formulas over denominator \(2^H\).
Their scaled constants lie in \([0,3^H)\). The height bound forces both
initial values to be divisible by \(3^H\), so the constants agree exactly.
Cancellation, coprimality and the two-adic valuation then force the same
base and the same clock. Conversely, a heavier word realizes the ordinary
source \(x/3^d\), where \(d\) is its extra odd count.
[Complete theorem and proof](closure/README.md)

There are also explicit arithmetic progressions at every \(H\ge1\),
with \(r=2H\), satisfying
\[
3^{2H}w+1=2^{H+1}a,\qquad
3^{H+1}a=2^{5H+2}b+1.
\]
On each progression the entire smooth reservoir, including free powers of
two, misses through clock \(H\) on both arms. The first direct entry into
that reservoir occurs at \(H+1\), at \(2^{5H+2}b\). The actual smaller
positive integer \(b<w\) is reached at \(6H+3\). For example,
\(T^9(15075)=265<1675\), with \(15075=3^2\cdot1675\).
The Chinese remainder theorem gives arbitrarily large ordinary members.
Lean verifies the all-quantified paths and inequalities under the two
displayed identities. The CRT infinitude argument is written.

The root assembly proves that none of these tuples can be the first bad
tower: every smaller positive base is good under that minimum hypothesis.
It also proves maximal odd count for each prefix through clock \(r\) of
any hypothetical first bad tower. The finite characterization alone does
not cover unrestricted clocks. The known convergent pair 15 and 5 supplies
a checked all-clock countercontrol: \(T^8(15)=5\), but the requisite
equal-constant heavier word never occurs. A general smooth source with a
free power of two also requires the endpoint qualification recorded in the
proof. [Lean consequences](formal/FinalProposal.lean)

## 2. Every nonzero rank shift must change a positive fraction of bands

Consider the primitive ordinary cycle in the existing bounded
least-tripling-disagreement alternative. Let \(s\) be its least odd site,
\(p\) its odd period and \(h\) its shortcut period. Normalize each odd
site to \([s,2s)\) by dividing by \(2^{k_r}\), with
\(k_r\in\{0,1,2\}\), and index by increasing normalized rank.
For each cyclic shift define
\[
E_t=\#\{0\le r<p:k_{r+t}\ne k_r\}.
\]
For every sufficiently large such cycle, the written argument proves
\[
E_t>p/747\quad(1\le t<p),\qquad
E_t>p/83\quad(1\le t\le p/10).
\]
These are necessary conditions on a hypothetical cycle, not its exclusion.
The theorem retains PR200's written strip estimate and the ordinary
minimum/excursion hypotheses on which that estimate depends.

The proof uses integer gaps between sorted normalized sites. Their exact
recurrence fixes the middle gap of a sufficiently long common word by a
product of a power of three from its past and a power of two from its
future. Approximate spacing limits how often the same gap can occur.
A sparse word count contradicts the resulting number of distinct gaps.
An explicit code accounts for the wrap boundaries and extends the bound to
linear-sized rank shifts. A second count on the actual physical exponent
word, followed by a finite coset argument, covers the remaining small-order
shifts. These counts assume no independence of the actual orbit.

The height range used is
\(s\gg p^{1000/479}\) from PR200 and \(s\ll p^{5.12}\) from the cycle
product and Wu–Wang's published linear-form bound. The extra power of
\(p\) in the second exponent is retained. The proof strengthens round
nine's \(E_1\gg p/\log s\), but permits high-mismatch legal decorations.
The complete physical denominator \(2^h-3^p\) remains essential.
[Gap proof](arithmetic/README.md) ·
[All-shift extension](arithmetic/EXTENDED_SHIFTS.md) ·
[Independent review](../../../reports/astra-global-closure-20261124/round10/rows/EXTENDED_SHIFTS_REVIEW.md)

## 3. The opposing exact-row bounds agree on their exponential scale

Let \(G_b=(4/3)^b\). For a fixed odd unit \(q\), let \(J_b(q,k)\)
count actual unit sources reaching \(q\) after \(b\) odd gaps and
\(2b\) shortcut steps, with residual
\(2^{-k-102}\le x/(qG_b)\le2^{-k}\). Under the explicitly
source-qualified central renewal floor F, a hypothetical nontrivial cycle
through the same fixed \(q>1\) satisfies
\[
\exp(-C_q k^2/b)
\le \frac{J_b(q,k)}{qG_b2^{-k}}
\le \exp(-c_q k^2/b)
\]
for \(K_q\sqrt{b\log b}\le k\le\delta_q b\), at all sufficiently
large \(b\). In particular the count at \(k=\lceil b^{2/3}\rceil\)
has normalized size \(\exp[-\Theta_q(b^{1/3})]\). At the trivial odd
cycle \(q=1\), the corresponding lower bound is \(c/\sqrt b\).

The lower theorem extends F beyond its original central clock window by
gluing paths at their actual ordinary endpoints. The complete word
determines its cuts, preventing overcounting, and the real offset stays
bounded. The upper theorem counts exceptional first passages from complete
ordinary source octaves and uses the actual cycle's accumulated clock
defect. Its proof does not use F. Both bounds concern the same row and
normalization, so the superpolynomial upper does not contradict the lower.
[Definitions, proofs and qualifications](rows/README.md)

The same construction gives matched moderate-deviation tails on a supplied
hypothetical escaping ray. For the statistic summed over all terminals,
suffixes at \(H_b\sqrt b\), with \(H_b\to\infty\) and
\(H_b=o(\sqrt{\log b})\), can still carry \(b^{-o(1)}\) aggregate
mass under F. The original PR207 aggregate has a separate terminal cutoff;
that cutoff is not silently removed. The required vanishing estimate on
its integer diagonal remains unproved.

## 4. Formal boundary, verification and the next decisive step

| Evidence | Scope |
|---|---|
| Seven rebuilt Lean modules | Four new modules plus three byte-identical PR192 dependencies; warnings treated as errors and an empty project output cache. |
| 65 selected axiom inventories | 28 from new modules and 37 from dependencies; only `propext`, `Classical.choice` and `Quot.sound` where used. |
| Six root finite replays | Three scripts run normally and with Python optimization; byte-identical outputs in each pair. |
| Independent reviews | Row and arithmetic agents reconstructed each other's arguments; the tower and final consumer have separate scope reviews. |
| Written theorems | CRT infinitude, first-passage concentration, conditional row asymptotics and full entropy/all-shift assembly are not claimed as Lean formalizations. |

[Lean receipt](../../../reports/astra-global-closure-20261124/round10/lean/receipt.json) ·
[Finite replay receipt](../../../reports/astra-global-closure-20261124/round10/controls/control-replay.json)

The final Lean consumer visibly retains PR192's `FrontierMerger` premise.
It requests an ordinary meeting with an earlier power or a smaller positive
base on every remaining arithmetic input. No term proving that premise is
supplied. The new tower families exclude actual minimum witnesses only on
their stated arithmetic conditions. The cycle theorem leaves the
high-mismatch whole-denominator case, and a first crossing out of the height
strip remains a separate unresolved branch. These are mathematical gaps in
the complete conjecture, not missing build steps.
