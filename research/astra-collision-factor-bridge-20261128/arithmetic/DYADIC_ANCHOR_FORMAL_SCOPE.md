# Exact rational anchor arithmetic: formal scope

[DyadicAnchor.lean](DyadicAnchor.lean) verifies the arithmetic used in Section 5 of the [critical damped-anchor obstruction](CRITICAL_DAMPED_ANCHOR_OBSTRUCTION.md). Its map is the rational affine branch

\[
                     F_e(x)=\frac{3x+1}{2^e}.
\]

All positive exponents are allowed. This is the anchor recursion; it is not a claim that every branch is the legal accelerated Collatz step at an integer.

The five public roots establish:

1. If \(r\) is odd and \(d\ge1\), then \(3r+2^d\) is odd.
2. The exact rational identity
   \[
   F_e(r/2^d)=\frac{3r+2^d}{2^{d+e}}.
   \]
3. Under the odd-numerator and positive-height hypotheses, the reduced denominator on the right is exactly \(2^{d+e}\).
4. Every exponent \(e\ge1\) strictly increases the reduced denominator of a nonintegral dyadic anchor.
5. Every integer anchor \(z\), positive or negative, has some positive exponent giving a nonintegral branch. The proof uses the explicit exponent \(|3z+1|\); this is an existence certificate, not an optimized exponent selection rule.

The five roots were freshly compiled, then imported into a separate complete root and axiom audit. The [receipt](../../../reports/astra-collision-factor-bridge-20261128/arithmetic/dyadic-anchor-lean.json) pins:

- Lean 4.34.1, commit `5045d0056413266e57c625dcd7c365b10e377c52`.
- Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`.
- Source SHA-256 `f8875dfd4edf6591c5758c210e46c16e5a570cdd213c81608e6fba0427876b52`.
- Runner SHA-256 `9ab5f807301b3a931d6200a7dc88419bec95fba373e7da33084584611c9c7b28`.

The source was unchanged during verification. The only reported axioms were `Classical.choice`, `Quot.sound`, and `propext`. There are no added axioms, admitted proofs, or native-decision shortcuts. Cached pinned dependencies were reused; no cold dependency rebuild or independent LeanChecker replay is claimed.

The [runner](check_dyadic_anchor.py) accepts explicit toolchain and Mathlib paths:

```bash
python -X utf8 -B research/astra-collision-factor-bridge-20261128/arithmetic/check_dyadic_anchor.py \
  --lean /path/to/lean-4.34.1/bin/lean \
  --mathlib /path/to/pinned/mathlib4 \
  --receipt reports/astra-collision-factor-bridge-20261128/arithmetic/dyadic-anchor-lean.json
```

The consequence that no finite nonzero positive atomic measure is stationary under the geometric affine pushforward remains a written measure argument. The singular-kernel estimates, ordinary-to-Haar interchange, signed-coefficient reduction, and full majorant obstruction also remain written. This finite kernel does not formalize Collatz convergence or the unresolved canonical ordinary trace bound.
