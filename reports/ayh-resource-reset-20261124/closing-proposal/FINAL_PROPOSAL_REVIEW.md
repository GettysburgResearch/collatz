# Independent review of the final assembly

Signed by the directed arithmetic reviewer, 2026-11-24.

I reviewed the uncommitted `FinalProofProposal.lean` with SHA-256
`3175f6206aa7567d23952ca68a36cd6da9c43dcc7afca1e78313551b1c653379`.
The root's fresh-build report records a successful kernel check and a clean
public-axiom audit of this revision. I reviewed the source and imported
theorem statements independently. I did not rerun that complete build for
this review.

**Finding.** The conditional proof is sound. It proves universal positive
convergence from the two arguments `QuantitativeReturn` and
`HigherRankProgress`. The latter is an open proposition. The closing
theorem does not furnish its witness. The equivalence in the file reports
the mathematical strength of that missing input accurately.

* A reverse defect has a positive residue-17-mod-48 source outside the basin
  whose triple is inside. From an actual membership proof for the triple,
  the assembly extracts an actual finite witness `Hits (3*z) j`. The first
  two shortcut inputs are odd because writing \(z=16t+1\) gives upper
  values \(48t+3,72t+5,108t+8\). The first two values exceed 1, excluding
  certificate lengths zero and one. The argument also works for padded
  certificates. It uses no first-hit assumption.
* The split into odd count two and odd count at least three is exhaustive.
  The former invokes the unconditional `two_odd_progress`. The latter
  invokes the stated open input at the same source and same certificate.
  This is a case split on odd counts. The well-founded induction is on
  ordinary source size.
* In the nontrivial progress branch, \(n>0\), \(2^{40}n<z\) and
  \(\mathrm{Basin}(n)\leftrightarrow\mathrm{Basin}(z)\). Assuming that
  \(z\) is outside the basin gives exactly the nonbasin input needed for
  quantitative return. Its output has \(w\le2^{40}n<z\) and is an actual
  reverse defect. The strong induction hypothesis at \(w\) uses both its
  residue and the basin proof for \(3w\), contradicting the supplied proof
  that \(w\) is outside the basin. No directed defect is assumed to recur
  merely because an ordinary endpoint is smaller.
* The imported `collatz_iff_reverse_seventeen` consumes exactly that reverse
  implication. Conversely, universal convergence implies the first
  disjunct of `SourceProgress` for every allowed \(z\). With quantitative
  return available this proves the advertised equivalence with
  `HigherRankProgress`. It neither proves the open premise nor turns a
  rank-three example into coverage of every higher rank.

## Quantitative-return candidate

I also examined the generic semantics and top-level theorem of
`QuantitativeReturn.lean` with SHA-256
`29385e0b50688db4a09ada4175fdd9a8b335e1a4c1191c112c31fa68e23f7e07`.
The candidate's `bounded_return` has the exact quantifiers, orientation and
constant required by the assembly. It imports the ordinary map and finite
certificates, and does not import the final assembly or its open premise.

The basin indicator is defined by actual basin membership. Affine bounds
check slope and intercept against the original positive row at the same
ordinary parameter. The ternary splits transport that parameter and the
full history together. At a directed hit, `checkedSound` supplies a query
with labels false and true in that order, and the 11-to-17 exchange
preserves the ordering. The descent checker only traverses unconditionally
ordinary segments between explicit tripling tests. If a triple is outside
the basin it continues the checked descent. If the triple is inside, it
forces a bounded directed defect through the odd-multiple and residue-16
exchanges. The finish case gives a positive strictly smaller ordinary
nonbasin integer; the second use of strong induction therefore terminates
on ordinary size. The numerical checks keep every required intermediate
factor within the final \(2^{40}\) bound. None of these implications uses
`HigherRankProgress` or assumes the desired global convergence.

This is a source-level assessment of the quantitative candidate at that
hash. At the time of this entry its complete literal-bank kernel run had
not been reported successful to the reviewer. A successful check and clean
axiom audit of the final source would discharge the backward-height input.
The higher-rank argument would still be required for a Collatz proof.

## Final wrapper addendum

Signed by the directed arithmetic reviewer, 2026-11-24.

I verified the revised wrapper at SHA-256
`3070f6afe46813eca5716e82c37cb8a338f0007612b77ff9cbab7bfc08a2d2d2`
and the staged quantitative module at the same SHA-256
`29385e0b50688db4a09ada4175fdd9a8b335e1a4c1191c112c31fa68e23f7e07`
reviewed above. The wrapper imports that module and directly assigns
`CollatzQuantitativeReturn.bounded_return` to the theorem
`quantitative_return : QuantitativeReturn`. Its conclusion includes the
genuine reverse-defect orientation, positivity of the starting endpoint
and height bound used in the induction.

The smaller-witness branch now invokes this theorem directly.
`collatz_from_proposal` has only the argument `higher : HigherRankProgress`.
The resulting equivalence `UniversalConvergence ↔ HigherRankProgress` has
no external mathematical premises. Its reverse direction remains
conditional on higher-rank progress when used to prove convergence. The
source supplies no inhabitant of that open proposition. The earlier checks
of quantifiers, directions, padding and well-founded induction continue to
apply. I found no new circular reasoning or dropped premise.

This addendum records inspection of the two specified source files. The
root's fresh rebuild and public-declaration audit for the final wrapper
were in progress at the time of signing; their outcome belongs to the
separate execution receipt.

## Quantitative certificate execution update

Signed by the directed arithmetic reviewer, 2026-11-24.

The transport author reports that a complete corrected execution of
`QuantitativeReturn.lean` at SHA-256
`29385e0b50688db4a09ada4175fdd9a8b335e1a4c1191c112c31fa68e23f7e07`
finished with exit code 0 in 335.537 seconds. Its axiom report for
`CollatzQuantitativeReturn.bounded_return` named only `propext`,
`Classical.choice` and `Quot.sound`. This resolves the pending literal
certificate check recorded earlier. The final wrapper directly consumes
this proved bound. Higher-rank progress remains open. I did not execute
that author run; the publisher's separate clean-rebuild receipt supplies
the independent final execution record.
