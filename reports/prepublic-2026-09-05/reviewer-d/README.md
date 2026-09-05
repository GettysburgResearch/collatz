# Reviewer D — independent audit of integrated main

**Repository:** GettysburgResearch/collatz. **Role:** Reviewer D, GPT-6 Astra Pro.
**Frozen main:** `cd1b3689e8d37fc4232945072e2faf6bd5ee47bd`.
**Head-capture cutoff:** 2026-09-05 19:43:16 UTC / 22:43:16 Asia/Jerusalem.
**Separate branch:** `reviewer-d/2026-09-05-integrated-main-audit`.

## Verdict

**The original resident mathematical spine survives at its stated scopes, with localized corrections required.** I found no failure of its core extraction, parity coding, coefficient-supercritical divergence, finite-safety, six-branch rigidity, or nonconstant factor-complexity arguments. That is not blanket approval of main, all source branches, all their artifacts, or any full Collatz proof.

The complete wording of the extraction and periodic packets is **VERIFIED WITH FIXES**: each contains a false ancillary statement. The three additional resident proposed claims receive clause-level verdicts. Two source-pinned dependency files contain overstated extensions, but the narrower clauses actually used by the resident factor-complexity repair survive. The proof review is independent reconstruction, not acceptance by the source model's identity or by its earlier review label.

This review adds reports and a bounded exact checker only. It does not edit proof bodies, promote canonical statuses, merge or close items, or change settings/workflows. Proposed replacement wording below remains pending review.

## Coverage

I read all seven original resident packets, covering the eight IC records, and reconstructed their main proofs. I also reviewed the three resident proposed files L-0041, L-0042 and T-0046, five PR16 dependency bodies at their exact source SHA, and the source finite-affine theorem for the six-branch packet. This is **16 proof-bearing files**, with clause-level exclusions in the matrix.

I additionally inspected the current front door, integrated index, four new mass/rank/orbit reference assemblies, conventions, errata, and both structural-validator implementations. That inspection does not constitute a second complete mathematical review of every newly imported PR87/88/90/91/92 body. The current main is the #95 integration commit, a child of the earlier `9704bcf1ff33cc9e2b729e0c40137a1e55b95397` baseline.

Read [the claim matrix](CLAIM_MATRIX.md), [independent proof audit](PROOF_AUDIT.md), and [exact sources, checks and exclusions](SOURCES_AND_VALIDATION.md).

## Findings requiring action

| Finding | Exact location | Assessment and action |
|---|---|---|
| FD-01 | `research/integrated/ordinary-extraction/README.md`, Adversarial examples, item 4 | **REJECTED as written.** A long zero-digit prefix followed by infinitely many nonzero digits can represent a negative ordinary integer. With binary moduli, `-2^J` has J initial zero appended digits followed entirely by maximal digits. Keep the signed stabilization theorems; correct this example. |
| FD-02 | `research/integrated/periodic-tails/README.md`, Consequences / The complete denominator is mandatory | **REJECTED as a characterization of positive ordinary realization.** The code block additionally requires a nontrivial cycle. The word `10` realizes the ordinary integer 1 but the cycle is trivial. Relabel the block as a counterexample-cycle certificate, or remove nontriviality from the general characterization. The displayed periodic/preperiod theorems survive. |
| FD-03 | `claims/lemmas/L-0041-six-branch-root-cap-recurrence.md`, equation (10) and the paragraph after (7) | **VERIFIED WITH FIXES.** At empty depth the positive survivor minimum is 1, not the empty canonical residue 0; restrict (10) to positive depth. A lifted source-value increment `P^n Q h` changes its high quotient by `P^n h`, not `P^n Q h`. The stated append and output recurrences are correct. |
| FD-04 | PR16 `T-9316-efficient-recurrence-thue-morse.md`, section 2, sentence beginning “Equivalently” | **REJECTED for unrestricted appended-block nonstabilization.** Constant words have arbitrarily efficient repetitions but completion 0 and zero appended blocks. Nontrivial ordinary-orbit exclusion and the recurrence cone survive; block nonstabilization needs the nonconstant exception already present in the resident repair. |
| FD-05 | PR16 `L-9313-centered-error-full-shift-cylinder.md`, section 2 | **REJECTED for the asserted strict strip at every nonconstant tail.** `1000...` gives error `1/N`; `0111...` gives `-1/N`. The weak strip, exact recurrence, uniqueness and cylinder stabilization survive. Strictness requires excluding eventual constant tails or using the separately established positive ordinary-orbit hypotheses. |
| FD-06 | `claims/lemmas/L-0042-syndetic-integral-algebraic-branches.md`, Consequence for extraction schemes | **GAP-BLOCKED as an unqualified transfer to complete-tree rigidity.** Syndetic integrality proves polynomiality, not restored full-tree/full-tail hypotheses or integer coefficients. Preserve the sound lemma; require the other rigidity hypotheses explicitly before drawing the section-machine consequence. |

An additional clarification is advisable in T-0046 section 5: cofinal emptiness must cover every possible overlap length for each candidate initial source, not merely one sequence of length ratios tending to the same limit. Its necessary overlap identities and limiting scale are verified; no emptiness theorem is supplied.

## What remains verified

The signed extraction criteria, the `-19/11` completion ghost, the full coefficient-divergence argument, the two-state terminal safety SCC theorem, and the exact six-branch rigidity statements withstand reconstruction. In the factor packet, the constant-word refutation remains valid and the **separate nonconstant repair remains valid**; it is not undermined by unused overstatements in its dependency files.

For the pending periodic packet, the full-denominator/sign, all-zero, finite-preperiod, trivial-cycle and fixed-block-controller mathematics has been checked. Its complete prose still needs FD-02 fixed and deterministic productive controller semantics made explicit. This review does not remove the repository's pending flag by editing it. SC*, FC*, the exact old FC-language bridge, ordinary extraction in a concrete unresolved architecture, and nontrivial cycle exclusion remain open or pending at their existing boundaries.

## Checks actually run

[The new checker](targeted_checks.py) and [its frozen report](checks.json) pass in normal and optimized Python, with eight genuinely altered, resealed reports rejected. Coverage includes 8,190 periodic words, 24,570 ordinary lifts, 7,938 preperiod pairs, 32,768 coefficient-identity positions, 11 independently minimized safety automata, all 36 six-branch ordered pairs, 1,554 complete finite type words, and 11,260 centered repeated-factor checks. Universal verdicts rely on the written arguments, not extrapolation from these tests.

**No authenticated full checkout was available. Neither full-repository validator was run against main.** Their code was inspected; the new standalone arithmetic audit is not a substitute or a claimed full-tree validation. No old heavy census, external Lean build, or large certificate was replayed.

## Recommended disposition

Accept this as a review record after checking its counterexamples and scope. Then prepare a separately reviewed erratum for FD-01–06, preserving the originals and historical verdict boundaries. Keep accepted core results, false auxiliary clauses, and proposed replacement wording separately identified. Do not discard the resident spine, and do not give an entire source file a blanket passing label merely because one dependency clause passed.
