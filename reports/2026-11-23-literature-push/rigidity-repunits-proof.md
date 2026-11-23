# Homogeneous repunit arithmetic core: proof and execution boundary

23 November 2026. Author: `/root/source_construction`.

**Status: Lean-checked algebraic core, frozen for independent review.**
This is a substantive cancellation lemma requested by the adjacent
unbounded-packet arithmetic lane, separate from the written analytic
rigidity packet.

## Exact statement

For `P,Q` natural and `Nat.Coprime P Q`, the new module proves

\[
\gcd(U_m(P,Q),U_n(P,Q))=U_{\gcd(m,n)}(P,Q),
\qquad U_n(P,Q)=\sum_{j<n}P^jQ^{n-1-j}.
\]

Both indices may be zero. Equality of the bases, or a zero base, is
permitted whenever the explicit base-coprimality hypothesis holds.
No quotient with a potentially zero denominator is used in this
general identity.

The recursive definition is linked to the displayed literal sum by a
proved theorem. Its addition formula and base coprimality give

\[
\gcd(U_m,U_{m+n})=\gcd(U_m,U_n).
\]

The proof then removes arbitrary multiples from the second index and
performs Euclidean gcd induction. Thus the repunit coprimality needed
by the packet construction is a conclusion, not an input.

The module separately proves the full numerical difference-of-powers
gcd for ordered bases and the quotient formula for strictly ordered
bases. It also specializes to `P=X^r,Q=Y^r` and proves coprimality with
the original `X*Y` when `r,n>0`. The last positivity conditions are
necessary and are not erased.

## Execution

The final build used a fresh external output directory. Both the source
and its axiom audit compiled with `autoImplicit=false` and
`warningAsError=true`, exiting zero. All 17 authored theorem
declarations and the recursive definition were audited. Every axiom
set is a subset of `propext`, `Classical.choice`, and `Quot.sound`.
No `sorryAx`, custom research axiom, or native-decision shortcut is
present.

The exact commands, runtime, mathlib pin, source hashes before and
after, and output hashes appear in `rigidity-repunits-lean-receipt.json`.
Mathlib dependency objects were reused; this authored module was
freshly compiled. Earlier development attempts are not represented as
the final successful receipt. No historical repository corpus was
rebuilt.

## Scope

The theorem applies to the actual complete integer repunits used by
the arithmetic construction. It proves no Collatz realization,
coefficient-stopping claim, or global cycle exclusion. The complete
packet numerator and full numerical gcd consumer are a further
formalization task; they are not silently included in this core's
17-theorem inventory.
