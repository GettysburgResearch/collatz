# Direct attempts on the fixed ordinary source

**OPEN. This pass did not prove the closing implication.** It tested unrestricted competing paths, iteration of first-meeting estimates, and an adaptive construction in the full ordinary component graph. The new finite steering result does not establish descent below the original source. The concrete all-depth certificate below rejects a proposed short route to that descent. Neither statement excludes an escaping orbit or a nontrivial positive cycle.

## The obligation kept fixed

Use the shortcut map \(T(n)=n/2\) for even \(n\), and \(T(n)=(3n+1)/2\) for odd \(n\). If \(m>1\) is the least positive nonconvergent integer, the required contradiction would follow from

\[
  \exists\,0<b<m\;\exists i,j\ge0:\quad T^i(m)=T^j(b).
\]

The visitor clock \(j\) is unrestricted. A local decrease from a later, larger value does not establish this statement. An estimate for a random binary continuation does not establish it for the actual continuation of \(m\). We did not replace this obligation with a restricted word family or declare a conditional criterion to be closure.

## An exact test of the unrestricted competing paths

For the actual positive source 703, Lean proves

\[
 \forall\,0<b<703\;\forall j\ge0\;\forall i<81,
 \qquad T^j(b)\ne T^i(703).
\]

It also proves \(T^{81}(703)=628<703\). Thus the first meeting with the **complete** forward orbits of all smaller positive starts occurs at clock 81. The quantifier over \(j\) is infinite; this is not a search up to a selected inverse depth.

The certificate encodes a finite set \(A\) containing 1 through 702. The kernel checks that \(T(A)\subseteq A\) and that the first 81 states of 703 lie outside \(A\). Induction gives \(T^j(b)\in A\) for every visitor clock. An independent exact computation obtains \(A\) as the full forward hull: 1,106 elements, maximum 20,762. The Lean theorem needs its coverage and closure, rather than its cardinality or minimality.

[finite_certificate.lean](finite_certificate.lean) uses only `Std` and kernel `decide`. It has no native evaluation proof bridge. Its two public declarations are `Collatz.FiniteCertificate.no_earlier_meeting` and `Collatz.FiniteCertificate.meeting_at_81`.

This refutes a universal guarantee of smaller-source contact by shortcut clock 80. It does not exclude a component comparison that uses a later common future. The certified meeting at clock 81 explicitly supplies eventual descent for 703.

## The adaptive construction and its unpaid cost

In the shifted coordinate \(a=n+1\), literal Collatz component moves include

\[
 a\longleftrightarrow 2a-1,
 \qquad 2a\longleftrightarrow3a.
\]

The critical states of the construction have \(a=6k+2\). From \(k=3u\) there are physical component paths to critical coordinates \(4u\) and \(32u+2\). From \(k=3u+1\) there are paths to \(8u+3\) and \(16u+6\). At \(k=3u+2\), the current shifted value \(18u+14\) has a same-component value \(16u+12\), which is smaller.

An exact residue calculation, lifted to every natural input, shows that an adaptive choice reaches the last case after at most three switches. The associated Lean statements certify the physical switches and the universal finite steering calculation. See [termination.md](termination.md), [termination.lean](termination.lean), and [termination.py](termination.py).

The earlier switches can increase the value. The available proof does not make the final \(16u+12\) smaller than the original \(6k+2\). For example, from the shifted input 8 every partner of that displayed form is at least 12. Separately, the 703 certificate excludes every smaller inverse origin at each of its first 81 ordinary endpoints; it leaves comparisons using a later common future open. The missing argument is amortized repayment of all preceding increases on a fixed ordinary input.

We also tested arbitrarily many steering and restart rounds, rather than stopping at that example. [controller_pressure.md](controller_pressure.md) gives a written estimate for the specified controller: the ternary Haar measure of inputs admitting any finite path with cumulative homogeneous multiplier at most one is at most \(31/32\). An adjusted estimate accounts for the affine offsets before a first actual decrease from a large ordinary input. Thus a uniform ternary-input repayment argument for these switches fails. Positive integers form a Haar-null set; the estimate supplies no single positive integer that fails forever and does not cover every move in the component graph.

## The inverse-cost and density attacks

[arithmetic.md](arithmetic.md) permits arbitrary inverse depth \(h\), even beyond the forward depth \(t\), and keeps the original source \(m\). On an injective odd orbit with corrected height \(H(m)<\infty\), a competing source with real clock overhead \(D\) satisfies

\[
                              z<2^D H(m).
\]

Therefore every fixed overhead budget eventually reuses finitely many original sources. Allowing a deeper inverse search alone does not force a new, smaller one. Distinct side branches give a possible escape contradiction through their disjoint predecessor basins, but we did not prove the necessary nonsummable lower bound on their density.

The current uniform predecessor floor is proportional to \(1/z\), under the named primary inputs. It yields a weighted restriction on distinct branch entries, not the missing construction of enough entries. Recent counterexamples to a general inverse-logarithmic density gain have densities tending to zero. They do not refute a comparison assuming the fixed positive density retained along a hypothetical escaping orbit. We kept that stronger assumption throughout; no comparison under it was proved.

The first-meeting lane likewise did not obtain a shrinking all-time bound for this fixed source. Its source-preserving estimates have a finite resolution range. Replacing the original floor with a larger one can absorb the target being studied. Fixed-target inverse-law limits permit an arbitrarily long prescribed initial segment as the target moves along an escaping orbit. Neither operation removes the original source's contribution.

## Latest upstream interfaces inspected

The head SHAs and exact paths are in [SOURCES.json](../../reports/astra-fixed-atom-20261124/SOURCES.json). These are bounded reviews of the named interfaces, not independent certification of each entire manuscript.

| Source | Relevant result | Remaining step for the fixed source |
| --- | --- | --- |
| PR193, `ebeec2c` | All-depth repayment counts; actual first-passage and later-crossing distinctions | Force a successful competing path, or control the fixed orbit after all later returns |
| PR197, `9ab91d9` | First-fusion moments below (3/2) for three fixed affine arms | Eliminate the two surviving classes; the packet gives a physical two-class example |
| PR201, `3c9e444` | Summable low-grade occupation at a common original-source clock | Control the remaining separated pair beyond the finite source horizon |
| PR182, `a30402b` | Proper multiscale potential and sparse actual resets | Pay the first-return debit on every ordinary trajectory |
| PR195, `8edc24b` | Prime-coverage and independent-factor restrictions | Obtain an opposing bound that applies to every candidate |

The root tested whether the stronger triple estimate forces a third live class on a discordant edge. It does not: the explicit quartet collapse in PR197 leaves exactly the two needed classes. No stronger finite-family implication was established here.

## Evidence boundary

The Lean certificates establish finite physical identities, universal bounded steering, and the stated all-visitor-clock exclusion for the fixed 703 prefix. The inverse-cost and density arguments are written mathematics with named dependencies. No external density theorem was rebuilt in this pass. See the [review](../../reports/astra-fixed-atom-20261124/ROOT_REVIEW.md) and [verification record](../../reports/astra-fixed-atom-20261124/VERIFICATION.md) for the final source hashes and checks.

The result of this pass is a tested failure of the proposed closing bridges, together with a scoped finite construction. Universal smaller-source merging, elimination of the fixed surviving contribution, and exclusion of nontrivial positive cycles remain unproved.
