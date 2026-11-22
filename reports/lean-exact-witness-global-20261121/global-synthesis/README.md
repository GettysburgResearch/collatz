# Checkpoint ten: canonical witnesses and actual binary-run forcing

Parent published PR177 head:
`9af9118a7e9af870a32a72a4efdcf77e886940ec`.

The scientific entrypoint is the
[research README](../../../research/lean-exact-witness-global-20261121/README.md).
Full Collatz and the original residue implication remain open.

## Mathematical scope

The new core-Lean packet proves an exact normal form for every complete
alphabet-four certificate, including its supplied terminal padding. The
remaining universal interval step is equivalent to the nonempty prefix-to-11
obligation `ElevenIntervalStep`; the fixed terminal tail cancels from the
original grade. All exceptional motifs and positive terminal padding close.
The conditional global theorem states its remaining premise explicitly.

The second route proves actual binary-pattern forcing through signed low
shadows. The signed trace exists for every requested finite odd-event length;
the magnitude, ordinary clock, positive endpoint, and low-block borrow bound
are exact. Uniform dyadic coset lifting supplies either of two alternating
high patterns within fewer than `4^S` odd events. `BinaryRunForcing` joins
these into one actual ordinary-path theorem.

Complete written arguments then prove binary-run compactness, bounded-run
eventual periodicity, quantitative occupation on every escaping orbit, and
divergent original-source run moments on the common shortcut clock. The
binary combinatorics and real asymptotic deductions are not claimed as Lean
theorems. Peer analytic comparisons retain their frozen source qualifications.

## Fresh formal execution

`checkpoint-ten.json` records the actual commands, durations, source hashes,
compiler identity, and proof boundary. A new build directory contained no
prior `.lake` outputs; all 38 Lean source files matched their recorded hashes.

- Fresh `lake build`: **38 jobs passed**.
- Each of the four new substantive modules passed a separate compile with
  warnings treated as errors.
- The combined `Audit.lean` checked **184 declarations**, including **43 new
  public theorems**.
- Every axiom set is empty or a subset of `propext`, `Classical.choice`, and
  `Quot.sound`. There is no `sorryAx`, custom conjectural axiom, or
  `native_decide` in the new proof modules.
- The new finite terminal base, forced by the seven terminal motifs, is
  kernel `decide` on targets at most 1105 with a proved 113-clock predicate.
  It is a base case of the unbounded normal-form theorem.

The raw logs are `checkpoint-ten-build.txt`, `checkpoint-ten-axioms.txt`, and
the four `checkpoint-ten-strict-*.txt` files. The empty strict logs indicate
successful, warning-free executions; their exit codes are in the JSON receipt.

## Exact structural replay

`binary-run-cases.json` contains forty selected signed/coset and large-gap
representatives, with exact integer certificates. The largest source has
3584 binary digits. Generation uses signed affine arithmetic; verification
independently follows the positive shortcut map and checks every odd gap,
clock, endpoint, signed borrow, forced residue, and binary-run exit.

All **40** certificates passed. All **16** deliberately damaged certificates
were rejected, including coordinated changes that preserve the initial affine
split or the total-clock bookkeeping. Normal and optimized Python verification
both passed in this coordinating replay. The agent's generation in both modes
was byte-identical; those exact committed inputs are retained by hash.

Reproduction from the repository root:

```bash
python -X utf8 -B research/lean-exact-witness-global-20261121/run-search/verify_binary_run_forcing.py --verify reports/lean-exact-witness-global-20261121/global-synthesis/binary-run-cases.json
python -O -X utf8 -B research/lean-exact-witness-global-20261121/run-search/verify_binary_run_forcing.py --verify reports/lean-exact-witness-global-20261121/global-synthesis/binary-run-cases.json
```

The finite cases test the implementation and sign conventions. They do not
enumerate the explicit binary-run cores or establish a new numerical Collatz
verification threshold.

## Source refresh and publication boundary

`SOURCE_REFRESH.json` records all 122 open PRs returned by two API pages and
24 selected frozen heads. This metadata inventory is distinct from the
selective mathematical reading and from new formal execution. The integrated
research map and scoped errata remain the baseline; no peer proof is relabeled
as freshly rebuilt here.

The lead reconstructed the signed separation, both binary joins, finite-core
count, occupation argument, and common-clock conversion. A strict versus
nonstrict endpoint in the single-leaf spike comparison was corrected before
publication. The reviewed written claims remain qualified exactly where they
use external source statements.

A complete clean-checkout integrity/regression gate is run on the final
committed tree before publication. PR177 records its actual checked commit,
tree, command and receipt digest, and the re-read remote head. The publication
tree must equal the checked tree. Repository integrity is distinct from the
kernel and mathematical evidence above.
