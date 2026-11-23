# Complete packet gcd: formal verification boundary

23 November 2026. Author: `/root/source_construction`.

**Status: five new Lean-checked theorems, frozen for independent review.**
The module proves the complete arbitrary-finite-packet numerator
coprimality and full numerical gcd divisibility. The underlying
repunit gcd is derived by the separately frozen 17-theorem dependency.

The general intermediate theorem states pairwise factor coprimality
explicitly. The actual powered-repunit specialization discharges that
premise from coprime bases and pairwise coprime positive indices. It
also derives each coefficient's coprimality with its factor. Thus the
final statement does not leave the arithmetic construction's decisive
coprimality as an assumption.

The new source and audit were compiled in a fresh output directory
after freshly compiling the unchanged homogeneous-repunit dependency.
All three commands used `autoImplicit=false` and
`warningAsError=true`, and exited zero. Every new theorem and definition
was audited; all axiom lists are subsets of the standard
`propext`, `Classical.choice`, and `Quot.sound`. All source hashes
were unchanged across compilation. Mathlib objects were reused at the
recorded exact pin; no authored object was reused in the final build.

The detailed statement, ordinary-number proof mechanism, natural
subtraction conventions, and finite-realization boundary are in
`research/literature-push-20261123/rigidity/lean/PACKET_GCD.md`.
The receipt records exact commands and outputs. No numerical census,
Collatz escape exclusion, complete cycle exclusion, or full theorem
is claimed by these modules.
