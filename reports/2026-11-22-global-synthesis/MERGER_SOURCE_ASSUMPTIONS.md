# Quantitative inverse selector: source and interpretation audit

**Author self-audit, not independent review.** The root reviewer separately
checks the theorem and final published execution. The scope here is the
eleven public declarations in
`research/global-synthesis-20261122/lean/QuantitativeInverseSelector.lean`.
Full Collatz and the low-interval dispatcher remain OPEN.

## Source identity

| Item | SHA256 |
|---|---|
| Final `QuantitativeInverseSelector.lean` | `132f0cd8318e20271456a4f776a90621407bc0a69dce805382b5860a08a13048` |
| `AuditQuantitativeInverseSelector.lean` | `e4616dc039cf98029d9af16b854d62b450e7d184d4c77e9eaafeccf64c219ceb` |
| Frozen `research/band-return-20261121/lean/vendor/ShellCover.lean` | `76477e195c733e8b8c9fdf523d954d85375b3ac244ee0590127192743bffc88c` |
| Final `inverse_alphabet_selector.py` | `605f3b6d896836cfe1ec8601fab9006ba94ee0b0b4120b145d33d844ac69db24` |

The frozen ordinary-map dependency is present in owned PR178 at
`be5696cc45a95ad1903802b08ba1dc3ebba66930`. The inverse table is attributed
to PR177 at `a0a0d76f91b4e3846c1b1f0706cad56cb6098317`,
`research/lean-exact-witness-global-20261121/lean/Collatz/BoundedGapCofinal.lean`,
`unit_predecessor`. Its six arithmetic cases are reconstructed locally,
not assumed through an external computation or custom axiom.

The new module imports only `ShellCover`; the audit imports only the new
module. It uses `CollatzShell.step` and `CollatzShell.orbit` unchanged.
It introduces an explicit finite positive-odd-gap path proposition, not a
replacement Collatz map or a second ordinary clock.

## Exact hypotheses and conclusion of the strongest theorem

`bounded_window_literal_tail` has precisely three supplied mathematical
premises, besides natural parameters `q,N` and the finite list `tail`:

1. `GapPath q tail 1`: an actual complete odd convergence certificate.
2. `q % 3 != 0`: the certified root is a ternary unit.
3. `q <= N`: the requested threshold is at least that root.

Oddness and positivity of `q` follow from `GapPath`; they are not hidden
extra inputs. The returned positive odd source `p` is a unit and satisfies
`N < p` and `3*p < 16*N`. The returned prefix `word` has all letters in
`1..4`, length at most `unitWindow(N).card`, sum at most four times that
cardinality, and `GapPath p (word ++ tail) 1`. The tail is literally the
supplied list. There is no intermediate theorem call returning a fresh
uncontrolled convergence certificate.

`unitWindow(N)` is exactly the finite set of positive odd ternary units
at most `N`. The source note gives its elementary floor-count formula.
The Lean theorem uses the finite-set cardinality; the closed floor formula
is not claimed as a separate Lean declaration in this module.

No independent wanted target appears in this theorem. In particular, it
does not infer convergence of an arbitrary integer below the returned
source, and it does not invoke `LowIntervalStep`, `Universal`, a physical
merger selector, or any new claim about cap-three extinction.

## Why the inverse chain cannot repeat

`odd_gap_path` proves the ordinary clock exactly equals the positive gap.
`odd_gap_nonterminal` proves that, when the source exceeds one, none of the
states before the edge endpoint equals one. The six-row selector always
chooses such a source, even when the root is one.

`firstTime_increases` applies only to a root already in `Basin`. The least
ordinary hitting clock is then finite and strictly increases backwards
along the selected nonterminal edge. This handles supplied tails that
contain terminal `1 -> 2 -> 1` padding as well: their supplied length is
never falsely treated as a minimal hitting time.

`firstTime` is a noncomputable proof device using classical proposition
decidability and `Nat.find`. The selected predecessor, selected gap, walk,
and prefix word are computable. The finite cardinality argument proves
that the executable first-crossing loop stops within its stated budget.
No infinite path or profinite limit is substituted for that finite output.

`walk_injective` follows from the strictly increasing first-hit measure.
`crosses_within_window_card` puts the first `card+1` distinct selected
vertices into a set of cardinality `card` if they all stay below `N`, a
contradiction. The final theorem takes the first crossing; its immediately
preceding vertex is at most `N`, giving `3*p+1 <= 16*N` and the strict
displayed window. The proof makes no claim that every individual inverse
edge grows in ordinary height.

## Local execution and trust boundary

The development proof and all eleven public axiom audits compiled under
Lean 4.34.1 with `-j1 -DwarningAsError=true`. The audit output contains
only subsets of `propext`, `Classical.choice`, and `Quot.sound`; there is
no `sorryAx`, custom axiom, or `native_decide` in the new result.

After that development replay, the root reviewer requested one doc-comment
change from “No target convergence is assumed” to “Only the supplied root
certificate is used.” The final module hash above includes that comment
change. No proof term, statement, definition, import, or tactic changed.
The root's clean-checkout replay is responsible for certifying the exact
final file bytes and the freshly rebuilt frozen dependency.

The Python script passed in normal and optimized modes with identical
JSON: twelve literal-tail selector fixtures, four closed finite cap-three
graphs, fifteen instances of the written all-depth chain theorem G3, and
five fully certified G4 roots with their exact one-gap tails.
The four graph closures check every outgoing legal edge and confirm that
their depth assignments are acyclic. The graph counts do not assert
extinction at any other root. The G3 and G4 arithmetic proofs are written
in the source note; they are not included among the eleven Lean claims.

## Remaining global gap

The interval program's rank may spend a removed gap at least five or an
initial even run at least four on this alphabet-four prefix. It may not
spend one gap-four grade on arbitrarily many new gap-four letters. The
explicit window and clock bounds do not change that comparison.

The cap-three graph has critical unit outdegree counts, and the complete
symbolic finite-chain family G3 proves an exact finite maximum on that
family. Neither supplies cofinal cap-three ancestry for all required
tails, nor a total target-changing rule when it fails. This is the first
unproved global continuation of the present route.
