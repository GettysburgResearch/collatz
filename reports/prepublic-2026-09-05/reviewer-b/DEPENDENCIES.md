# Cross-PR dependency and conflict map

Baseline `9704bcf1ff33cc9e2b729e0c40137a1e55b95397`; #91 `b8c88843726ee7ac11cf91323c69bf911ca50706`; #92 `7bb6d36d3bc37dd09b52aa9a23c8e33973032359`.
All proposed combined exposition below remains pending its own integrated-wording review.

## Normalizations: do not combine these by their letter names

| Object | Domain / definition | What can transfer |
|---|---|---|
| Shortcut T | Positive integers; even n/2, odd (3n+1)/2 | Common elementary base of #87/#88/#90/#91/#92 |
| Syracuse S | Odd-to-odd, divide 3n+1 by its entire power of 2 | Clock is not shortcut clock or packet clock |
| #90/#92 early whole-run F | One maximal odd run followed by maximal even run | Same elementary physical map; distinct from later A |
| #91 section return R_sec | First positive return to n=1 mod3 or 1 | Finite fan and section arrival; 1 absorbing |
| #91/#90 rank P | (2n+1)^2/3^v3(2n+1); #90 later extends to h=0 | Not #92's moving minimum; do not import numerical rank comparisons |
| #92 acceleration A | Maximal number of repetitions of the active word 1^a0; a=0 for even inputs | Computable finite clock per module; A(1)=1, later killed operators exclude 1 |
| #92 moving rank R_* | min_a z_a(n)^2/3^v3(z_a(n)); z_a=3^a(n+1)-2^a(2n+1) | Exactly computable from 0,1,2 and possibly h=v3(2n+1); proper, unique zero at 1 |
| Spectrum refinement Phi | R_*^2+R_*+1-n | Orients equal-rank edges in the nonincreasing safe set; not a global decreasing rank |

### Three safe regions and their operator assumptions

- **91:** G = nonresonant section endpoints, Q=1. Arrival halves P. K_GG has weighted-supremum bound 1/2 against V=1/P. Unsafe-return tail is pointwise, for f<=CV, with Q(y) still present.
- **92 quarter:** G_q={n>1:4R_*(A(n))<=R_*(n)}. Distribution-free contraction in a *finite* R_*^p source moment. Unsafe entry does not automatically preserve that moment; its failure is proved.
- **92 spectrum:** G_le={n>1:R_*(A(n))<=R_*(n)}. Phi orients flat steps. The square-root spectrum gives a finite safe clock and polynomial source-mass tails. G_q is a proper subset: 3->4 is flat in R_*, hence safe only in G_le.

Rows of inverse/transfer kernels are endpoints and columns are sources. They are deterministic forward mass pushforwards evaluated by summing inverse fibers—not independently resampled random transitions. Explicit killed source/end restrictions and zero extension must appear whenever kernel blocks are exported.

## Dependency graph and exact external boundaries

```text
baseline IC-SC (fixed-source classification) ----+--> #92 orbitwise SC-tail crosswalk
#92 pass2 orbit counting/correction bound ------+
                                               +--> SC* iff eventual periodicity
                                               X    no nontrivial-cycle exclusion

#87 predecessor P(0.901) --> #87/#88 exponent race <-- #90 critical little-o bridge
                               ^
#92 exceptional critical residue identity ------+ (conditional comparison only)
#92 count of one injective orbit ---------------X not the whole exceptional basin

#91 section + P + inverse fan --> charged safe contraction --> resonance return
                              --> guarded P-repayment       X universal budget/cover

#92 finite-feature obstructions --> exact infinite moving minimum + A
                                   |--> inverse fan / finite rank fibers
                                   |--> rank spectrum (two alternative proofs)
                                   |--> G_q moment resolvent --X unsafe boundedness
                                   |--> G_le + Phi safe tail --X unsafe contraction
                                   +--> guarded switch blocks-X total successful selector

#90 P-based merging/clock constraints <---- comparison only ----> #92 R_*-based peak constraints
```

#87 is pinned at `e9adc409031a61f3801c4ee1e1e6deeb34188eb7`. The external predecessor declaration requires a fixed positive target not divisible by 3 and supplies a target-dependent eventual constant at exponent 901/1000. Its native computation assertions and large payload have NOT been replayed here. The natural-density theorem reaches a growing threshold, not one fixed endpoint with a power saving.

#88 is pinned at `c28922fb6d1c070bf86a76192f40bc9ea3edd67c`. Its actual file is `research/external/mazur-2026/fixed-height-forward-power-saving.md`; the PR description advertises other T-FHP paths. One-horizon no-descent sparsity and its entropy wall do not give exceptional-basin sparsity. Its all-subset fiber-saving obstruction concerns mass conservation; survivor-specific bias remains open.

#90's observed current head is `78ac7c8489f1df81230402808b1f4b77b18fae73`, including `CLOCK_DEFECT.md`, `BOUNDARY_FAN.md` and `INVERSE_SHADOW_FRONTIER.md`. Its description still labels a4b9... as current. These later files are inventoried/interface-qualified here, **not independently fully reviewed**. #91 originally cited #90 at aeb69...; #92 cited specified later snapshots. Old source pins remain historical evidence, not invalid links merely because later work exists.

The #92 source pin for #81 `T-6812-support-corrected-cofinal-envelope.md` at `09d6f9086d4ead63a5102f05458441939c29f4f5` was fetched successfully. Do not mark it missing just because the SHA also identifies a review-bearing branch. This review does not thereby verify the entire old #81 dependency cone.

The six carry rules are a value-preserving administrative subsystem of the Yolcu–Aaronson–Heule representation. The published paper/abstract is context; this review does not claim a full formal port or termination of the complete rewrite system. Assani's source was not accessible in full; no uninspected theorem from it is admitted.

## Genuine differences among the missing obligations

| Obligation | Domain and quantifiers | Not supplied by |
|---|---|---|
| Fixed-height exponent race | All exceptional *sources* up to X, fixed certified H, sufficient power/little-o | Sparse forward orbit/minima; natural/log density at growing H |
| #92 Mellin bias / signed root charge | Actual time-k survivor population at a fixed H | Ambient residue balance, finite horizons, H growing with 2^k |
| #91 Q-budget | Every required prefix of one actual no-descent source | Necessary lower charge pressure; safe-only contraction |
| Unsafe-return transport | Actual induced unsafe distribution, right norm/envelope | Safe resolvent; summable initial weight alone |
| Complete merging cover | Every candidate component minimum, a finite actual lower-rank meeting | Finite endpoint candidate list or finite-radius successful tiles |
| Total repayment selector | Every input receives a successful finite physically legal decrease | Computability of guards that may return UNRESOLVED |
| SC* / positive cycles | Fixed-source coefficient stopping / complete all-word cycle obstruction | SC-tail location / proper denominator factors / finite cycle samples |

## Conflicts and overlaps to resolve deliberately

1. #91/#92 share `research/astra-three-routes/README.md`. Preserve both source entries, build a neutral active subject index, and route the two programs separately.
2. In #92, `pass5/` and `pass5-spectrum-switch/` duplicate T-A3-1001/1002/1051/1052/1101/1102 and X-ASTRA3-005. Full path is mandatory even after PR qualification. Assign distinct integrated IDs without renaming frozen originals.
3. Rank counting is proved twice. Retain both proof provenances; 55/6 and 18 are compatible upper bounds, not disagreeing constants. A combined theorem/exposition is a proposed synthesis pending narrow review.
4. Earlier scalar finite-valuation obstructions do not contradict the moving minimum: its index depends on n and ranges over an infinite family. The separate whole-run obstruction cannot be applied to a different acceleration by name alone.
5. SC* implies eventual periodicity only after the new orbitwise argument is included; it does not resolve cycles. `IC-PERIODIC-001` and `RD-BRIDGE-001` remain at their previous pending boundaries.
