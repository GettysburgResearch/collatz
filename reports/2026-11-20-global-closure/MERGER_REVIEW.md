# Independent review of the forward-five descent

**Verdict: VERIFIED at the stated conditional scope by independent agent
reconstruction.** This is not external mathematical acceptance or formal
proof-assistant verification. The physical forward-five premise remains
unproved.

## Frozen objects

| Object | SHA-256 |
|---|---|
| `research/global-closure-20261120/merger.md` | `148bd92aa2c3d09e72bbc9521de8521a38f10691e53c5f6e0f780cb13bae065a` |
| `experiments/global_closure_merger.py` | `01f093ee6dd01820757bb23ae224f5d3df7b9130137980dfa96e123f1ab86c8b` |
| `merger-certificate.json` | `751523dd92445610a26302947a2f689aecc56a27eaf6fa1f9954eb2e59f5c7c1` |
| `merger-report.json` | `2a1099beb71531fa8f447c0356fa9789b2d5e8f9f75509022ef7e4215bea9306` |

## Mathematical reconstruction

The four assumptions of GCM-001 suffice for every arrow's stated reverse
membership implication. The extension of forward multiplication by five
from odd ternary units to even ternary units uses only doubling equivalence.
No step silently assigns tripling invariance to the ordinary basin.

For `B`, the positive odd input and its image `3x+1` meet after one
shortcut step from each. For `Ij`, its positive odd unit output `y`
satisfies `3y+1=2^j x`, so its actual `j`-step shortcut orbit reaches `x`,
even when `x` itself is even. Division by two is an ordinary equivalence.
Division by five is precisely the assumed implication in reverse proof
order. It is never justified as an ordinary Collatz transition.

All coefficients stay integral on their entire infinite cell. Positivity
at the minimum parameter and positive slope imply positivity at every
admitted lift. The explicit congruences ensure the odd-input restrictions
and preserve exclusion of multiples of three. The endpoint is at most
`19n/20`; the unbounded parameter is not replaced by a numerical sample.

The residue partition is complete on the integers coprime to thirty. Even
ternary units descend by halving; odd units divisible by five descend using
the assumed five rule. These cases and the base input 1 complete strong
induction. Intermediate values may exceed the candidate: their membership
comes from reading the certified implications backward, not from using
strong induction at a larger integer.

Taking `S=C intersect U` therefore establishes GCM-002's equivalence.
An arbitrary odd multiple of three enters the ternary units after its first
actual shortcut step. For the restricted five-ray form, the identity
`T^3(20x+1)=T(5x)` is legal for every positive odd `x`; together with
`4x` and `x` having the same fate, this identifies exactly the valuation-two
layer. Neither direction assumes convergence of an unproved source.

## Separate computation

The independent program
[`check_merger_independent.py`](check_merger_independent.py) does not import
the production checker. It composes rational linear polynomials, separately
checks their full-cell integrality and congruences, and proves coverage by
**107,416 pairwise CRT incompatibility checks** plus the exact density sum
`4/15`. This is different from the producer's final-modulus bitmap.

The actual completed execution verified all **464 cells**, **3,455 primitive
operations**, **219 conditional five uses**, and the exact largest endpoint
ratio **13403/14119**. Four altered certificates were rejected. See
[`merger-independent-report.json`](merger-independent-report.json).

The independent audit also records why no numerical descent may be silently
assigned to every intermediate premise: a five-closure argument can be as
large as `3669265/2239` times its phase's original input in this certificate.
The final endpoint descends; the intermediate ordinary values need not.

Reproduction:

```sh
python -X utf8 -B reports/2026-11-20-global-closure/check_merger_independent.py --compare reports/2026-11-20-global-closure/merger-independent-report.json
```

## Exact review boundary

No error requiring a change to the frozen merger proof, certificate, or
production checker was found. The 19-move and 73-edge bounds are costs of
the conditional augmented proof graph. They are not ordinary stopping-time
bounds, and the complete residue cover does not prove the five-closure
premise itself. That premise is the remaining global obligation.
