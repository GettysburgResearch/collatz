# Independent review: the complete complementary denominator budget

Reviewer: root agent. Date: 2026-11-23.

**Verdict: VERIFIED as written mathematics.** The all-period denominator
restriction is valid at its stated primitive positive-cycle scope. It is
not a complete cycle exclusion.

## Frozen targets

| File | SHA-256 |
|---|---|
| `research/profound-step-20261123/ARITHMETIC_CLOSURE.md` | `972e16e87bbef21867fd3e7d7ede31575596cdb69807e776d3b29c76428414ed` |
| `research/profound-step-20261123/check_companion_control.py` | `8ef1ffeff25b6f6fc937dc4a1b8c4c9f2817983b52f82d009bb2cff328f23abf` |
| `research/profound-step-20261123/reports/companion-control.json` | `87f70ec46f595c9d33e5c58267cd16e11f3f3c9957dfc2544b291b8514af5e81` |

## Reconstructed proof

For a nontrivial positive integer cycle all states exceed one, so the exact
ordinary product yields \(2^A<4^p\). Thus its complementary word has
\(q=A-p<A/2\), a positive full denominator \(2^A-3^q\), and a positive
rational fixed point. The finite affine word is legal over odd-denominator
rationals. Its reduced denominator \(b\) is coprime to six and is preserved
by every step.

A shorter primitive companion period would give a shorter period of the
original parity word. Equality of complete parity itineraries forces equality
of the corresponding rational 2-adic states by divisibility by all powers
of two. Hence the companion numerators are distinct. Without primitivity
the small-numerator budget could count one state repeatedly; the reviewed
statement explicitly excludes that mistake.

Multiplication around the companion gives exactly
\[
 \sum_{\text{odd companion }w}
 \log((3w+b)/(4w))=(A-2q)\log2.
\]
Only odd numerators \(0<w<b\) contribute positively. Distinctness and
coprimality justify charging each at most once in the finite product.
The derivative formulas make the summand decreasing and strictly convex.
The odd integers below the odd \(b\) are the midpoints of the disjoint
length-two intervals covering \([0,b-1]\). Their midpoint sum is at most
half the integral there. The omitted interval \((b-1,b)\) has positive
integral, including the case \(b=1\), so the final inequality is strict.
Direct integration yields \(b\log2/3\). This proves
\(b>3(2p-A)\), with the full coprimality-sensitive product refinement.

The minimum-dependent corollary follows with the correct direction from
\(2^A\le(3+1/m)^p\). Its constants agree with the exact logarithmic
expressions; it has no finite period cutoff.

## Escape companion and the sign control

The qualitative arbitrary-denominator companion argument was completed
before freezing. Infinitely many companion odd steps remove its finite
3-part. If they were eventually absent, the original positive integer
would be eventually all-odd, forcing \(2^L\mid x+1\) for every \(L\).
Outside the finite numerator box each original even step does not increase
\(x|w|\), and each original odd step contracts by at least \(5/6\).
Infinitely many original odd steps then contradict a positive integer
product. This recovers a known rational-companion mechanism; it does not
construct the companion for a general input.

Root reran the exact control checker. It reproduced the full negative
cycle through \(-17\), its complete carries and denominators, the legal
primitive positive companion, and product \(8\). In particular
\(\gcd(5296,1967)=1\). The note uses this only against a sign-independent
cancellation claim: the original denominator is negative. It does not
misrepresent this as a counterexample to a positive-source statement.

The primary Monks–Yazinski and Halbeisen–Hungerbühler papers were opened.
Their rationality/periodicity and full-word formulas are credited; the new
packet makes no priority claim for the numerator-budget bound.

## Verification limit

The exact control is a check of the displayed example and its algebra,
not a computation proving the universal integral inequality. No Lean
formalization is claimed for that integral argument. The first missing
full-cycle implication remains an effective restriction on
\(\gcd(2^A-3^{A-p},C_c)\) using positive original integer closure, or a
different all-period obstruction. The proved lower bound on \(b\) supplies
no opposite bound.
