# Independent reconstruction of the adaptive merger rules

Reviewer: the arithmetic research agent, separate from the merger-rule
author. The written arguments, affine identities, imported narrow
dependencies, and the actual checker output were reconstructed. This is
not external peer review or formal proof-assistant verification.

## Exact reviewed bytes

This prepublication review uses SHA-256 byte pins; the enclosing
publication record supplies the Git commit containing them. No verdict
is assigned to later bytes or the entirety of the imported source PR.

| Path | SHA-256 |
|---|---|
| `research/fixed-integer-descent/mergers.md` | `9e2aed5f50a66f22667443c5fc339d9001585f6e4f16ca38e883a770c880dc6a` |
| `experiments/fixed_integer_mergers.py` | `a3a38ff5212975150791362e78cc340ffdc0915d85f4183692a7845a17ede019` |
| `reports/2026-11-20-fixed-integer-descent/merger-report.json` | `a5296303c2b1ddd541bcfe8be0ee900c5e3073ce38281b359e70b9900c60cda4` |

The imported file was fetched directly at
`(PR #146, 7d04c4dd756cfe495eb3eee78eba35a99085cd2a,
research/upper-bit-mergers/THREE_RAY_SMALLER.md)`;
Git blob `d61f955798254eeab3b76e44841133bfade10703`.
Only the explicitly identified seven-residue-class certificate and
finite `81h` implication are used below. No verdict is supplied for its
separate unbounded-clock argument or any other file in PR #146.

## Claim reconstruction

**FM-001: VERIFIED.** For `x=2^k t-1`, reconstructed both paths to
`W-1,3W-1`, where `W=3^(k-1)t`. The guard makes `W=3 mod4`, so the next
two steps meet at `(3^k t-1)/4`, each with exactly `k` odd inputs.
All values are positive; `x>1` excludes the zero lower neighbor. The
clock is a displayed meeting time, not a claim of first meeting.

**FM-002: VERIFIED under exactly the printed guards.** Each rule has one
positive, strictly smaller demand. Reconstructed the F chain
`n -> 2a -> a`, the H word `OOEE` ending at `T(a)`, the opposite arm in
each case, and the factor `3*2^(L-3)t` in `x+1`. Reducing its odd part
modulo 4 gives the advertised guard `t=3^L mod4`. Valuations are allowed
to be arbitrarily large. The proof does not give coverage when the guard
fails, nor can the smaller comparison be used before its hypothesis is
available.

**FM-003: VERIFIED in its local and least-failure scopes.** An independent
coefficient-pair replay checked all eight new rows and all 114 displayed
graph edges. It checked divisibility, parity, positivity, the sole `M`
demand, and strict decrease, including the shifted `n=1 mod64` base
exception. The union calculation gave exactly 83 of 192 odd classes
modulo 384, comprising 35 additional classes beyond the inherited 48.

For the inherited exclusion, a separate exact replay checked all seven
source rows, 95 edges and 11 smaller demands, and confirmed that their
classes cover all 36 residues `7 mod8` modulo 288. This reconstructs
that narrow source dependency; it does not promote the entire source.
The resulting count concerns possible *least* failures of `P`, not all
integers in a hypothetical nonconvergent basin.

**FM-004: VERIFIED as a conditional neighborhood theorem with the stated
finite-convergence input.** The finite `81h` implication in the pinned
source was read and reconstructed: `g(2s)=g(3s)`, the comparison at
`8s-1`, the eight choices of `j`, the three four-step adjacent profiles,
the even-`h` reduction, and the final strong induction. A separate exact
check replayed the six adjacent profiles and eight odd residue choices.

For the new neighborhood, `K>=bitlength(r)` ensures that every positive
integer in the cylinder is `r+2^K u`, `u>=0`. The two lifted endpoint
slopes are integral, and their coefficient ratios are at most
`(3/4)^11/r`. For `u>=1`, the comparison budget is strictly smaller than
`n`, with exact common upper coefficient

`15676011/16777216 < 1`.

An earlier draft mistyped this numerator; it was corrected before this
frozen review. The written proof handles `Y=1,2` separately, and the base
representative `n=r` is supplied by the assumed seed certificates.
The theorem does not prove convergence of unproved seeds or a complete
cover by their neighborhoods.

## Checker execution actually completed

```bash
python -X utf8 -B experiments/fixed_integer_mergers.py --compare reports/2026-11-20-fixed-integer-descent/merger-report.json
```

This completed successfully and matched the frozen JSON. It included
25,002 adjacent-pair cases, 16,145 bounded adaptive cases, 705 deep-
valuation stress cases, 284,560 adaptive graph-edge replays, 5,120
ordinary neighborhood replays, and nine rejected negative controls.
The large stress inputs had up to 263 bits; this is not an all-source
coverage test. The independently reconstructed coefficientwise rows
establish their infinite ordinary progressions through their algebra.

The strongest remaining gap is universal coverage by a successful
well-founded rule. None of these local implications closes that gap.
