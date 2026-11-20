# Independent review of the single-multiplier reduction

Reviewer: `critical_boundary`, 20 November 2026. This review is separate
from the root agent's reconstruction and from the author of the theorem.

## Frozen scope

| File | SHA-256 of reviewed bytes |
|---|---|
| `../merger/SINGLE_MULTIPLIER.md`, current reviewed note | `a2d9106916591ebbb6d883151191617b385309e5698d3490bc79340e1465360f` |
| Same note, original mathematical-review pin | `d8377d133300a3f2027888667bc8d32a2fb45bd387c8a7fbd5c38ff3375752e1` |
| `../merger/check_single_multiplier.py` | `a068dce9b48e657b3bb512d4a4f78b1c0c2f0a28b9a439222d6721105ca1a8aa` |

**Verdict: VERIFIED at M5-001, M5-002 and M5-003 as conditional
mathematical statements at these bytes.** The physical merger hypothesis
M5 remains OPEN. The verdict does not extend to later changes or to the
unproved energy propagation in the neighboring critical packet.

## Independent reconstruction

1. The equivalence between `x ~ 5x` and `4x ~ 20x+1` uses exactly
   `T²(4x)=x`, `T²(20x+1)=15x+1=2T(5x)`. All numbers are positive.
2. Even M5 parameters reduce to their odd parts by actual halving.
   Restricting the least-counterexample argument to ternary units is
   essential: every quotient used in the descent remains a ternary unit,
   so no unproved multiplication-by-three invariance is needed.
3. For `n=3 mod4`, the two inputs at `5n` are odd and
   `T²(5n)=5(9n+1)/4`. Both M5 calls in C5 have legal ternary-unit
   parameters. For `n=7 mod8`, the output `p=(9n+1)/4` equals
   `3m+1` with positive odd unit `m=(3n-1)/4<n`.
4. In the three quinary cases after `n=3 mod8`, each displayed numerator
   has the required factor five, each division is exact, and each output
   is smaller and is a ternary unit.
5. The remaining class is `n=40k+27`, without an extra condition modulo
   three. The three ordinary steps give `v=45k+31`, hence `v=1 mod15`.
   The three parity cases of `v` give legal outputs; the largest slope
   is `27/32`, and its affine inequality is strict for the stated
   `n>=27`. Membership in the unit domain is preserved in each case.
6. The final extension from units to all positive integers uses the odd
   part and at most one odd step. The component of 1 is its basin because
   the shortcut cycle is `1 -> 2 -> 1`.
7. The quantitative bounds concern the abstract diagrams. They do not
   bound the unknown merger paths supplied by M5. The example
   `n=40k+11`, `p=90k+25>n` correctly shows why induction on M5 query
   size is unavailable for this selector.

## Executed verification

Both commands were run from the shared complete checkout:

```sh
python -X utf8 -B research/closure-attacks-20261120/merger/check_single_multiplier.py
python -OO -X utf8 -B research/closure-attacks-20261120/merger/check_single_multiplier.py
```

Both returned the same PASS JSON: 320 ternary-unit cells modulo 480,
at most three M5 calls per stage, query bound `3*n`, vertex bound
`15*n`, and `q <= (27*n+23)/32 < n`. The branch counts were
`160,32,8,4,2,2,8,64,32,8` in the checker's printed order. The checker
uses explicit runtime requirements, so `-OO` does not remove its tests.

The all-lift interpretation was checked separately: each state is an
integer affine expression in the unrestricted nonnegative cell parameter;
its residue coefficient is divisible by the modulus being tested.
Positivity and the displayed bounds are proved by nonnegative slopes and
the appropriate first parameter, with the cell containing 1 starting at
the next lift. The replay is therefore more than a bounded starting-value
census, while remaining evidence for the conditional algebra only.

## Provenance-only delta review

The original reconstruction and both executed runs above reviewed the
note at `d8377d133300a3f2027888667bc8d32a2fb45bd387c8a7fbd5c38ff3375752e1`.
The author then changed its opening status paragraph and source commentary
to acknowledge concurrent PR157
`64361ecca770092d6c8242dc6211e38818af2e50`, whose GCM-001--002 give the
stronger one-way forward-five basin criterion. The current note correctly
describes its symmetric M5 statement as an independent short corollary,
with no new criterion-strength claim relative to that source. Its source
commentary also records inspection of the later PR146 head
`1608bb607fadae62723a22156bc96f6ebb452e43` without importing its unproved
closing premises.

The current opening and source paragraphs were inspected against the
fetched PR157 theorem statement. No theorem, inequality, physical path,
selector branch or quantitative scope of M5-001--003 changed, and the
checker retains exactly its original SHA-256. The conditional mathematical
verdict therefore applies directly to the current full-note pin
`a2d9106916591ebbb6d883151191617b385309e5698d3490bc79340e1465360f`.
The executed checker runs are retained as the original receipt; they were
not redundantly rerun for a provenance-only edit. This delta review does
not certify all 464 cells of PR157 or the neighboring latest-PR146 claims.
