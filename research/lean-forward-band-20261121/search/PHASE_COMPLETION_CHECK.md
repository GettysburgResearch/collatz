# Full saved-frontier check with the new unbounded phase rule

The targeted completion check did **not** close the saved PR 180 parity-rank
frontier. The enriched and baseline bounded searches have the same remaining
frontiers through all six binary refinement levels. The new rule closes no
additional cells in this matched comparison.

## Scope and matched rules

The input is the saved `pure-psi-parity-2-1.json` search: 1,290 successful
affine cells and 150 unresolved odd cells modulo 1,440. Its SHA-256 is
`be5125c0334a6f19a845b5803aed88c0fcd0f51524b9d5c8730d7f5c2cae23a3`.

Both searches use the unchanged common rank

\[
R(n)=2n\text{ for even }n,\qquad R(n)=n\text{ for odd }n.
\]

Each state is an entire affine cell `a*t+b`, for every natural `t`. Ordinary
forward and inverse edges must be valid on the entire cell. Inductive psi
queries must have strictly smaller rank throughout the cell. For a root
`M*t+r`, both runs use:

- coefficient bound `a ≤ 100M`;
- constant bound `b ≤ 100r`;
- 100,000 visited nodes per cell;
- six complete binary refinements of the entire remaining frontier.

The enriched run additionally permits the kernel-proved
`solved_phase_odd_psi` without a rank restriction wherever its hypothesis
holds throughout the queried affine cell. For a fixed trailing-one depth
`h ≥ 2`, this requires the coefficient to be divisible by `2^(h+2)` and

\[
3^{h-1}\frac{b+1}{2^h}\equiv3\pmod4.
\]

It also recursively applies the uniform even-psi macro when both required
queries are already justified by the unchanged rank or by the new terminal.
The baseline disables both additions. Thus the enriched graph contains the
baseline graph, rather than replacing its rules with a different rank.

## Complete frontier comparison

Both runs give these same counts:

| Refinement | Modulus | Cells tested | Cells resolved | Cells remaining |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 1,440 | 150 | 0 | 150 |
| 1 | 2,880 | 300 | 100 | 200 |
| 2 | 5,760 | 400 | 50 | 350 |
| 3 | 11,520 | 700 | 150 | 550 |
| 4 | 23,040 | 1,100 | 300 | 800 |
| 5 | 46,080 | 1,600 | 200 | 1,400 |
| 6 | 92,160 | 2,800 | 400 | 2,400 |

The largest enriched search used 653 nodes, so the node cutoff did not bind.
All 2,400 final unresolved searches exhausted their queues in the bounded
graph. Because the added edges are a monotone extension and the bounded
searches do not hit the node cutoff, the equal remaining counts imply equal
frontier sets inductively at each level. The final two sets were also
compared directly: they contain exactly the same 2,400 cells.

The resolutions produced by the binary refinements already occur in the
baseline. They are not new coverage attributable to the unbounded rule.
This check is search evidence, not a newly exported Lean cover.

## An explicit unbounded complementary family

The surviving query family

\[
n_k=5\,2^{2k+1}-1
\]

consists of parameters in the previous **global odd-psi comparison
frontier**, not claimed marked starting values. Their leading mantissa tends
to `1.25`, so sufficiently large members lie outside the shrinking constant-70
band. This completion check is testing the proposed global odd-psi closure
after adding the new band-derived theorem.

The family
has exact odd-core parameters `r=2k`, `u=5`. For every `k`,

\[
3^{2k}\cdot5\equiv1\pmod4.
\]

It therefore remains in the complementary phase at every trailing-one depth.
The solved-phase theorem cannot be applied to it by selecting another odd
core: the odd core is uniquely `5`.

For `k ≥ 5`, its residues modulo 92,160 repeat with period three:

\[
10{,}239,\quad40{,}959,\quad71{,}679.
\]

All three cells are in the unchanged final frontier. The periodicity is exact:

\[
n_{k+3}-n_k=315\,2^{2k+1},\qquad92{,}160=45\,2^{11}.
\]

The previous `BandParityBridge` theorem identifies the complementary transfer
with the original same-source odd-psi query. The higher trailing-one depth
does not turn this family into the solved phase.

This is a family of **remaining comparison queries**, not a family of
Collatz counterexamples. The queue exhaustion is limited to the stated
height bounds; it does not rule out larger excursions, another selector, or
a different global proof.

## Artifacts

| Artifact | Bytes | Role |
| --- | ---: | --- |
| `search_phase_completion.py` | 8,937 | Enriched search, matched baseline replay, and compact export |
| `phase_completion_check.json` | 30,785 | Compact comparison receipt, input frontier, and all final unresolved residues |
| `phase_completion_search.json` | 1,175,071 | Full enriched paths, summaries, and frontier details |
| `phase_completion_baseline.json` | 91,927 | Baseline summaries and full final frontier |

The compact receipt records the full-data hashes and source-input hash. For
publication, the script, this note, and compact receipt preserve the bounded
completion result without requiring the larger path dump.

The canonical final frontier hash is the same for the enriched and baseline
outputs:

`d8f20844dc857563d5141cc5f9ee55924588202bfe5452dc0b8d578eb2b6d566`.

The compact receipt includes the 150 initial unresolved residues, so replay
requires no staging-directory paths or unpublished input files. From the
directory containing the script and receipt:

```sh
python3 search_phase_completion.py \
  --input phase_completion_check.json \
  --output phase_completion_replay.json \
  --levels 6 --height 100 --cap 100000 \
  --compare-baseline --compact
```

The replay performs both matched searches and records explicit frontier hashes
at every level. The comparison above used the two already completed runs;
no additional search was run when adding this replay interface.
