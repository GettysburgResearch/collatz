# Independent scope review: CyclotomicBlockExclusion.lean

Reviewer: cycle_zero_atom. Date: 2026-11-22.
Reviewed source SHA-256: `d3ffda404a77fed64d13f2a4743388f051aecefe401dff778f80cf36e30ccb34`.

I read all ten theorem statements and proofs in the root-authored file.
This review is independent of the root's Lean compilation; I did not
rerun the compiler. It is a review of mathematical statement scope and
correspondence with N12–N17. The ten reviewed declarations are:
`complete_denominator_factorization`, `integer_bezout_805`,
`residual_coprime`, `reduced_divisibility`, `residual_lower_bound`,
`residual_exceeds_805`, `residual_nondivisibility`, `common_factor_pos`,
`complete_nondivisibility`, and `twelve_block_power_nondivisibility`.

- `integer_bezout_805` has the correct negative sign on U*D and homogeneous degree 14.
- `residual_coprime` correctly generalizes the power-of-two specialization to any coprime integers s,t.
- `reduced_divisibility` uses that coprimality to remove s^14 and obtain D' | 805*(t-u).
- The integer ordering t<s gives s>=t+1, and the displayed lower bound 12*t^7 is valid for t>=0. For t>=3 it strictly exceeds 805*t.
- `complete_nondivisibility` cancels the nonzero positive commonG only after the exact whole-denominator factorization. No cyclotomic denominator factor is discarded.
- `twelve_block_power_nondivisibility` instantiates s=2^a,t=3^b,u=2^b with b>0 and 3^b<2^a. Coprimality and the strict inequality 2^b<3^b are supplied inside the proof.

The formal result is the all-parameter integer divisibility exclusion for
the displayed polynomials. The parity-word construction, conditions
b>=1 and a-b>=2 ensuring legality, numerator correspondence, and
primitivity are separate written arguments. The Lean file states this
boundary explicitly. It does not state or assume unrestricted Collatz,
a universal cycle-word classification, or a bound on the number of
arbitrary positive cycles.

No statement-level flaw was found. The source contains no `sorry` or
custom cycle-exclusion axiom; the root owns the actual compiler and
`#print axioms` report.
