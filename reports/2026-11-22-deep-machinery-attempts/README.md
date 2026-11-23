# Review and reproduction scope for the deep-machinery attempts

**22 November 2026. No full Collatz proof; no new Lean execution.**

The [scientific entry point](../../research/deep-machinery-20261122/README.md)
separates the four routes and their unresolved closing statements. This
report records what was actually reviewed or replayed. Neither a written
review nor the repository validation gate is a substitute for a missing
universal proof.

## Written mathematical review

Three collaborating researchers owned the termination, boundary, and
rigidity routes. The principal researcher owned the Mahler route and
reviewed the new displayed algebra of the other three. The
[independent review](INDEPENDENT_REVIEW.md) was written by the boundary
researcher for the other three notes, before publication.

The principal review independently checked:

- **Mode refinement:** both affine compositions, exact rational roots,
  simultaneous 2-adic/3-adic congruence margins, physical parity words,
  maximal repetition counts one, rank denominators, unsafe-start
  indexing, and the paired valuation/rank transport. A direct comparison
  with every index of the infinite envelope was added after review;
  the principal researcher checked its valuation and exponent factors.
- **Boundary:** the triangular energy C_C/N, the oscillatory strong-sector
  contradiction on the actual clock-level space, the finite-word
  likelihood ratio and singular-law event, every implicit-renewal
  hypothesis and the constant 1/log(27/16), the reversal convention in
  the actual-prefix comparison, and the separately conditional
  moving-fibre resolution inequality. The cited strong-sector statement
  was located in indexed published primary text. The full applicable
  renewal statement was also opened in Alsmeyer's author-hosted research
  article, Propositions 4.1--4.2; the inaccessible original Goldie PDF
  is not described as read.
- **Rigidity:** logarithmic normalization, exact fixed-residue terms,
  finite-depth factors, positivity and Fourier coefficients of the
  continuous density, and the Boolean covariance constants. The pinned
  P1 theorem is Boolean; the note now explicitly extends it using
  invariant Boolean level sets and uniform approximation.
- **Direct sibling follow-up:** all six admissible exponent lists,
  their row sums, rank-based prefix preservation, the telescoping
  orientation of the path product, and the finite stopping-antichain
  inequality. This follow-up came after the initial independent review;
  its exact cost formula does not establish the needed amortized bound.

All three collaborating researchers independently checked the Mahler
note's displayed section identities and rationality-to-constancy
argument. Their scope included the zero section and the strict terminal
residue bound. This agreement does not establish the missing finite
Mahler system.

These reviews do not independently certify all inherited population,
stationary-density, canonical-envelope, FLOOR, or LOG inputs. Those
dependencies retain their source-qualified written status. The recent
joint-fibre manuscript is an additional explicit premise only in the
last section of the boundary note.

## Exact arithmetic replay actually run

The principal researcher executed both commands in the working checkout:

```text
python -X utf8 -B research/deep-machinery-20261122/termination/check_mode_refinement.py
python -O -X utf8 -B research/deep-machinery-20261122/termination/check_mode_refinement.py
```

Both returned exit code zero and the same summary:

```json
{
  "status": "all explicit checks passed; not a global Collatz proof",
  "case_count": 16,
  "pair_count": 60,
  "shortcut_clocks": 630
}
```

The script replays every literal shortcut step independently of the pair
affine formula. It checks active modes and maximality, the existing
rank implementation, the full stated no-repayment window, and the
repaired counter. It uses explicit exceptions, so optimization does not
disable the checks. The two executions are the same checker in two
Python modes, not two independent universal proofs.

The deterministic fixture contains no execution timestamp. Its integer
values are encoded as decimal strings to avoid machine-integer loss in
downstream readers. The implementation evaluates the inherited finite
envelope formula; the all-parameter proof separately compares the
infinite envelope directly. The finite replay does not extend its
coverage beyond the declared 16 parameter cases.

## Publication and earlier evidence

No existing Lean source or compiler driver is changed in this
continuation. Earlier receipts in PR178 still certify only their
original exact sources. This new packet is not added to their theorem
counts.

The complete clean-checkout execution of the five-command repository
validator and the exact publication identity are recorded in the
updated PR178 description. Its receipt is generated outside the tested
checkout. The staged source manifest pins the new scientific files;
the publication gate also verifies that the arithmetic fixture remains
unchanged when replayed in that checkout.

The [previous PR description](previous-pr-description.json) preserves the
earlier checkpoint's exact status and receipt links without relabeling
them as evidence for this continuation. The repository heads in
[SOURCE_SNAPSHOT.json](../../research/deep-machinery-20261122/SOURCE_SNAPSHOT.json)
were re-queried late in the pass and had not changed at that refresh.
