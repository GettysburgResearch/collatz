# Certificate transfer: supplied manuscripts, useful identities, and the remaining gap

**PROPOSED research and scoped source review. Collatz remains unresolved.**
This packet takes ownership of two user-supplied code archives, a separate
unfinished 18-page manuscript, and the preceding research review and six
standalone problem statements. It preserves the originals, reconstructs
the useful mathematics, and distinguishes exact identities, written
probability proofs, and finite computations.

The central target is the actual ordinary-integer implication

\[
x\in\mathcal E,\qquad x\bmod512\in\{129,257,385\}
\quad\Longrightarrow\quad (x+1)/2\in\mathcal E,
\]

where membership in `E` is witnessed by the finite exponential certificate
in [the density-one note](DENSITY_ONE.md). The witness set is exactly the
odd part of the basin of 1. PR146's [deep reverse reduction](https://github.com/GettysburgResearch/collatz/blob/e238c63a5d57f96bb063b7472498d1977df51951/research/upper-bit-mergers/DEEP_REVERSE_BASIN.md)
makes this full implication equivalent to Collatz; that reduction is a
source-pinned dependency, not newly proved or Lean-built here.

## What survives the review

| Result | What is established here | Boundary |
| --- | --- | --- |
| Certificate semantics and splicing | An increasing exponent tuple records exactly a finite odd-to-odd trajectory; on a coalescent class, the target certificate is obtained by replacing its prefix and subtracting one from the source suffix. | The source certificate is supplied; a bounded failed search for a merge returns UNRESOLVED. |
| Density-one transfer | A complete reconstruction of the PDF's excursion argument proves almost-sure type absorption, hence natural-density-one coalescent coverage in the three eligible classes. | Density is relative to all eligible integers, not conditional density among the convergent ones; an exceptional integer is not excluded. |
| Explicit excursion contraction | At successive zero-level excursions, `E sqrt(abs(delta')) <= ((3-sqrt(3))/2) sqrt(abs(delta)) + C`, with an explicit `C<54`. | This is a random-residue theorem. The repo already has a stronger quantitative absorption-tail argument for the same relation process. |
| Infinite certified exceptions | Every `x_s=(2^(54s+8)-175)/81`, `s>=1`, has a four-odd-step source certificate and is outside the PDF's coalescent set. | This is failure of affine coalescence, not failure of target convergence. PR163 separately excludes this rank as the globally least failure. |
| Two successive transfers | The updated ZIP's second application reaches a target in the ordinary component of `3^(27s-2)`. One application reaches the component of `3^(27s-1)`. | Both are consequences of the still-open transfer law; finitely checked powers are not an all-parameter proof. |
| Forward landing estimate | A distinct-prefix product calculation controls landing height after division by `3^a`. | An explicit two-odd-step family has `a=j-3` and a landing value exponentially larger than the target. Repeated values need separate handling. |

Read [DENSITY_ONE.md](DENSITY_ONE.md),
[EXCEPTIONAL_FAMILY.md](EXCEPTIONAL_FAMILY.md), and
[LANDING_AND_PHASE.md](LANDING_AND_PHASE.md) for statements and proofs.

## What is actually new relative to the reviewed repo

The supplied PDF is a useful alternate, explicit excursion proof, rather
than a new all-integer theorem. PR146 already treats the same canonical
process, up to arm orientation, and supplies a tail of order `h^(-1/2)`.
Its phase and bounded-rank notes already identify failures of whole-class
affine merging. This packet's useful synthesis is to connect the PDF's
exceptional set to the exact rank-four milestone, preserve the explicit
certificate splice and the second-transfer power progression, and correct
the interpretation of the experiments.

In particular, `17` and `33` both converge and meet although the forward
relation chain never absorbs. Likewise `129` and `65` meet despite being
an exceptional reverse pair. The PDF's statements that exceptional orbits
are "unrelated" or that no identity can link them are too broad. What is
absent is a merger of the two prescribed affine families on a binary
neighborhood of that parameter. See the [claim-by-claim review](../../reports/2026-11-20-certificate-transfer-intake/README.md).

## Current direction and handoff

The remaining useful task is a certificate transformation that also works
outside the coalescent set and has a well-founded justification. The
globally least-failure argument in newer PR163 narrows its possible
fourth valuations and excludes some whole families from being that
minimum. It does not convert the residual unbounded witness domain into
a finite problem. That is a more relevant frontier than increasing the
Monte Carlo depth of an already almost-surely absorbing process.

[HANDOFF.md](HANDOFF.md) updates the earlier ranking and explains the
logical payoff of the six standalone [question files](questions/).
Give an independent agent only the selected question file; the payoff key
and source links are intentionally outside that directory. Omitting the
project name does not make an open assertion easier or guarantee that a
specialist will not recognize it.

## Evidence and provenance

- [Original uploads and extracted code](../../archive/certificate-transfer-intake-20261120/README.md).
- [Source hashes, review findings, and finite replay](../../reports/2026-11-20-certificate-transfer-intake/README.md).
- [Independent finite checker](check_certificates.py), using explicit failures that remain active under optimized Python.
- [Exact publication validation](../../reports/2026-11-20-certificate-transfer-intake/VALIDATION.md).

Internal mathematical reconstruction and finite replay are not external
referee acceptance or a proof-assistant build. No claim in the accepted
integrated baseline is promoted by this exploratory packet.
