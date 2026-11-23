# Independent review: negative-numerator exact recognition

Date: 2026-11-23. Reviewer: `/root/ordinary_escape`.

**Verdict: VERIFIED within the explicitly separated written, formal and
finite-control scopes below.** No mathematical correction was required.
This is an internal independent reconstruction, not external referee
acceptance. It does not prove universal candidate existence or Collatz.

## Exact reviewed files

All paths are relative to the repository root.

| File | SHA256 |
|---|---|
| `research/lean-exact-witness-global-20261121/universal-step-20261123/candidate/NEGATIVE_NUMERATOR_RECOGNITION.md` | `ff00acf44c7b99eef45baec24a59c76c71777e610c8f103f1dbe997d1176d2eb` |
| `research/lean-exact-witness-global-20261121/universal-step-20261123/candidate/NegativeCandidate.lean` | `6f4739e252c100b501dc0a1fbaaf10644631f075e3ff82f497dee2dec7e3b8cd` |
| `research/lean-exact-witness-global-20261121/universal-step-20261123/candidate/negative_candidate.py` | `f1995c7e5552044c7e8a73aac48e8a5ad9a2aa9ec6f093d46fed10298a05556a` |

The author confirmed these three files were frozen during review.
The verdict does not extend to modified hashes or neighboring claims.

## 1. Sign and first-crossing reconstruction

For the shortcut map, a first hit of 1 from an input outside {1,2,4}
necessarily has the final segment 8 -> 4 -> 2 -> 1. The alternative odd
preimage of 2 is 1, which cannot occur before the first hit, while 4 has
no positive odd preimage. The complementary values pulled backward
from Omega(1)=2 are 1, 1/3, -1/9.

Both earlier complementary inverse branches, y -> 2y and
 y -> (2y-1)/3, preserve negativity. Thus the first crossing of the true
negative dual is exactly (8,-1/9) -> (4,1/3). These facts verify the
nonnegative exceptions and the accepted terminal state.

Reducedness is retained during the negative true trace: the backward
numerator updates are A -> 2A and A -> 2A+3^r, and r is at least two.
They preserve numerator coprimality to three. Hence the literal accepted
crossing is (x,w,r)=(4,1,1); it is not merely one unreduced presentation
among possible omitted terminal representations.

The implication from a triadic Omega equality to convergence uses the
manuscript's frozen finite-rigidity input. I did not replace that input
with a new formal theorem or independently re-audit the historical corpus.
Its scope is explicitly retained in the manuscript.

## 2. Binary numerator clock and sharp denominator bound

For a compatible negative-to-negative step at positive denominator
exponent, both updates satisfy 2|w'| <= |w|. In the original-even case,
2|w'|=|w|-3^(r-1); in the original-odd case there is equality. Thus a
negative state at clock K implies 2^K|w_K| <= A.

At the first original hit of 8, w_K=-1, so K < bl(A). The first positive
crossing takes K+1 transitions and the ordinary first hit takes K+3.
Consequently the stated bounds are respectively bl(A) and bl(A)+2.
The distinct K and K+1 clocks were checked for an off-by-one error.

For b original-even inputs before the first 8, r=b+2, and the full
complementary carry gives A=2^K+9D_K. Since the even positions obey
 d_j >= j, D_K >= 3^b-2^b. With K>=b this yields

A >= 3^r-2^(r+1).

Equality forces K=b and the all-even prefix, giving exactly
 n=2^(r+1), r>=2. The consequences 3^r<=9A and r<=bl(A)+1 follow as
stated. The backward-code Lean definitions correspond to these same
literal numerator updates, not an unrelated height abstraction.

## 3. Executable soundness, completeness and totality

The Python recognizer reduces the supplied fraction first, handles all
nonnegative possibilities without exponentiation, and rejects r<2 or
 r>bl(A)+1 before computing 3^r. A giant binary-encoded exponent is
therefore screened without constructing its power.

During the loop, q=3^exponent is maintained exactly. Complementary parity
makes both numerator divisions integral. The implementation immediately
rejects every wrong first crossing, including zero, and rejects a
negative integral endpoint. It never silently continues through a
positive sector. An accepted crossing appends the literal 4 -> 2 -> 1
suffix and the corresponding complementary values 1/3 -> 1 -> 2.
This establishes soundness for the complete complementary itinerary.

Completeness uses the frozen rigidity input only to identify a true
candidate's forced terminal segment. The newly reconstructed height
bounds show that none of its filters rejects that candidate and that its
crossing occurs within the supplied fuel. The exception at fuel exhaustion
is unreachable for valid inputs: otherwise a nonzero negative integer
numerator at clock E would have 2^E|w_E|<=A<2^E.

For accepted odd inputs, the implementation lists the actual odd-state
clocks, including the terminal 1, and checks the entire original integer
identity. The n=1 exception correctly emits the length-zero tuple [0].
For even inputs it promises an ordinary trajectory, not an E-tuple.
The accepted trajectory cannot have visited 1 earlier, since after doing
so the ordinary orbit would stay in {1,2} and could not later reach the
accepted crossing at 4.

## 4. Bit complexity and input size

The recognition claim is about native integer inputs with the usual bit
size, not about a polynomial bound for finding a candidate. Reduction
uses O(bl(|a|)) divisions by three, even if r is very large. A surviving
negative candidate has r=O(E), so 3^r has O(E) bits. The ordinary state
has O(bl(n)+E) bits throughout at most E transitions; the first positive
numerator is also of O(E) bits and is immediately processed.

The explicitly emitted path and tuple have polynomial total bit size.
Checking their complete integer identity also uses polynomial-size
integers and polynomially many operations. Thus the stated polynomial
bit-cost recognition claim is supported. O(E) refers to trajectory
transitions, not bit operations. No bound for a successful numerator
has been inferred from this verification bound.

## 5. Formal replay actually executed

The reviewer executed:

```
/workspace/scratch/c6766c1207a3/collatz_work/nov23_runtime/lean-4.34.1-linux/bin/lean -j 1 -DwarningAsError=true research/lean-exact-witness-global-20261121/universal-step-20261123/candidate/NegativeCandidate.lean
```

Exit code: 0. All thirteen printed transitive axiom sets were subsets of
`propext`, `Classical.choice`, and `Quot.sound`. No `sorryAx` or custom
research axiom appeared.

The formal scope was inspected rather than inferred from compilation:
`negativeSeek_sound` proves an ordinary hit within the fuel bound;
`negativePath_clock` and `negativeSeek_complete` fund and replay literal
first-crossing certificates. The module does not formally construct those
certificates from Omega equality, classify all infinite complementary
points, prove the Python implementation equivalent to Lean, or prove the
bit-complexity statement. The manuscript labels those boundaries correctly.

## 6. Independent finite implementation controls actually executed

Using an independent `Fraction` pullback of the actual finite ordinary
trajectory, I computed the exact complementary value for each n=1,...,64.
For each of these inputs I compared the recognizer with exact rational
equality on all a=-64,...,32 and r=0,...,5.

- 37,248 supplied candidate presentations checked.
- 31 accepted presentations; all agreed with exact rational equality.
- Every accepted ordinary clock equaled the independently computed first hit.
- A native exponent with 100,001 bits was rejected by the exponent-height
  filter without power construction.
- The unreduced presentation (-3^100)/3^102 for n=8 reduced to -1/9
  and was accepted with the expected reduced pair.

These are targeted finite controls of the new recognizer, not a new
Collatz census or an all-input proof. The mathematical proofs above,
and the explicitly scoped Lean declarations, supply the universal
recognition justification.

## Remaining theorem

The reviewed result verifies every *supplied* triadic candidate with a
much shorter exact first-crossing procedure. It still does not supply a
successful candidate for every positive n or transform an arbitrary
complete source witness for x into one for (x+1)/2. Those constructions
remain OPEN, and the verdict does not upgrade their status.
