# Coordinator reconstruction and verification boundary

**Verdict:** VERIFIED at the written claim boundaries below, with the stated external prerequisites. This is not a verification of a complete Collatz proof. The source hashes in `MANIFEST.json` delimit this review; later heads are not covered. The four current Lean modules were independently rebuilt by the coordinator, rather than inferred from agent logs.

## Deterministic synchronization and selected source rows

I checked the common-center update `(U+v)/2`, error update `(3^epsilon e+epsilon)/2`, marginal parity contraction and integer packing by grade. Deleting duplicate affine profiles is legitimate. The compression constants can be chosen in the stated order, giving only O(log M) survivors at clock O(log M). Different arm parities need no independence.

For the signed pair relation `Y=3^s X+d`, I checked the valuation cases `d=0`, `v2(d)<=v2(3^s-1)`, and strict inequality. The both-odd preparation in the last case gives exactly valuation L-1. Summing setup costs over the grade drops is at most 4s. At equal grade the exact identity `2^v(4d'+2)=3d+1` gives the logarithmic contraction paying for all nonfinal macros; the final zero-disparity case is separately bounded. Bounds on canonical representatives give a multiplicative clock recurrence. There is no unsupported assertion that small discrepancy alone implies equality.

For actual rows, `L_i` attains every integer by bounded upward increments and its explicit linear lower bound. The single ternary congruence in a full power-of-two period assigns each pre-pad word to one original source cell. I checked backward integrality, positivity and exact forward parity decoding. The square-root carry estimate uses the hypergeometric subset bound, not independent fixed-count bits. The ordinary lattice cap is exponentially larger than one uniformly in `h+J<=k/10`, justifying the successful-phase proportion. The row can depend on the prescribed cell. All synchronized block members remain in the same source band because their complete carries are positive.

The convergent-control family has m shortcut odd inputs but only m-1 accelerated gaps of length one; its final accelerated gap has length d+1. The final text treats this distinction correctly. I reconstructed the finite reciprocal-mass estimate and the same-scale separation of distinct unit-gate bands. Neither supplies an upper deficit at a fixed exceptional gate. Cycle's independent trace review covers the main proof; the late additions received coordinator reconstruction.

## Actual parent mergers and the obstruction

I checked each original-to-peak clock, the rational-center grade table, the 947-clock positive representatives, the `L+1` full laps, and the shared immediate successor. The last shared successor is already included in the 1379-clock bank: no extra step is added. The full parent clocks differ as claimed. The congruence `v2(3^(162m)-1)=3+v2(m)` gives one nonempty progression at each L. Positivity follows from the least-residue representative and the large valuation of m. The two- and three-parent banks are disjoint under their exact seed conditions.

The finite-family construction retains one common free binary parameter, fixes its initial congruence before steering, and uses the full order of `3^162` modulo `2^H` to recover an actual exponent subprogression. It does not replace a specified m by a different m without saying so. The quantitative interval corollary follows by taking J proportional to log log N, so its modulus is N^(o(1)).

For finite augmented classes I reconstructed the shifted product, bounded even-gate argument and same-visit-time injection on a nonperiodic orbit. In the periodic case the first visit to a chosen phase has a simple departed prefix. The integer invariant `ell(j_m+p)-q h` is constant across the class, and its coefficient of `j_m+p` is positive. This proves finite classes without an unproved global convergence assumption. The resulting missing indices are not asserted to diverge.

The separate density-one note is only a consequence of the pinned PR146 absorption tail. I checked its conditioning cost and adjacent-offset union bound, but did not certify the full probabilistic source proof. Trace and cycle agents independently reconstructed the finite-family result; trace also verified the explicit three-parent construction from its frozen sources.

## Cycle arithmetic

I checked that reflection reverses an edge with the same mechanical increment, hence reverses its allowed coefficient monotonicity. In the cyclic convolution, only at most 2m ranks can cross either cut boundary; the positive constant coefficient makes the unchanged convolution force the corresponding physical edge to be constant. The sine multiplier has nonnegative coefficients, including the endpoint case in which n theta equals pi. Taking the reciprocal gcd removes matched pairs as well as reciprocal irreducibles.

For a root of the positive polynomial, the finite geometric mean bounds its radial displacement by its angle. Applying the reciprocal polynomial when necessary gives `|1-alpha|<=25 theta`. Evaluation of the primitive irreducible at one then bounds the inverse angle exponentially in its degree. Smyth's published lower bound controls the number of unmatched irreducible occurrences. This produces the logarithmic degree lower bound; it does not identify an absorbing factor.

I checked the exact-mask geometry at sufficiently large near-critical period pairs, including the rank-zero anchor, actual valuations and the 11/12 threshold in the ceiling argument. For the distribution theorem, greedy paths to zero honor the time-dependent mask; two legal 26-edge fillings permit the desired one-site switch for every feasible boundary. Nonunit characters are included. Small centered frequency residues would force a nonzero integer divisible by an impossibly large power of three. For large divisors the complete local carry has small range and uniquely recovers every internal valuation, with the last recovered from the boundary clock. The prime-power expansion and divisor union account for the full determinant and multiplicities. The arithmetic agent independently reconstructed these arguments and flagged a carriage-return typesetting error, which was corrected without changing the formula.

The p=41 witness lies in the rational numerator lattice at its specified denominator. The replay exhausts every inverse exponent within each cost budget. No denominator-one or full-basin conclusion is inferred from its 1,681 window tests.

## Critical records and heavy machinery

I reconstructed the PR210 signed finite-shadow mechanism, its rational classification, finite rational locking statement and periodic-approximation calculation. The forms at infinity, 2 and 3 have fixed algebraic coefficients under the algebraicity hypothesis. Primitive normalization removes only a power of two, preserving the product and leaving height at least 3^p. Taking a ternary limit of one rational linear relation forces rationality. The overlap repetition argument covers both short and long occurrence separations. Evertse's primary exposition permits three forms in three variables; the PDF's greater-than-or-equal signs are misread in plain extraction.

The mechanical script has irrational mean, bounded deficit and at most n+1 length-n factors. The repeated-switch family has strict criticality and logarithmic deficit; its repeated blocks meet S2 for every selection. Ternary coding is injective on the two-letter alphabet, and counting newly exposed switch bits proves the stated compact-set dimension. For the general switched family the finite ordinary realization chooses q larger than its actual beta_n, rather than reusing the singleton's linear beta bound. No fixed ordinary orbit is obtained by this compact construction.

The original upstream Lean file is preserved byte for byte. Adaptation changed imports and proof tactics, not theorem statements. The kernel checks parity and divisibility consumers; the signed count, compactness and Subspace Theorem are written mathematics. The final `RecordLock` and `CycleExclusion` assumptions remain open. The cycle agent independently checked the PR210 arguments and the explicit critical constructions.

## Actual execution

The root replay used Lean 4.34.1, compiler `5045d0056413266e57c625dcd7c365b10e377c52`, Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. Fourteen project modules were rebuilt from source in a fresh empty project cache with `-j1 -DwarningAsError=true -DautoImplicit=false`; 119 selected transitive inventories passed, 36 in the four current modules. Only the three allowed standard axioms occurred. The compiler and dependency libraries were reused.

All four mathematical control programs have zero Python AST assertion nodes and passed normally and under optimization with identical output. The root receipt binds each script and output hash. One report suffix was corrected from JSON to text for the arithmetic program, then the entire four-program control run was repeated under the corrected runner. No universal theorem is inferred from these finite controls.

Repository integrity is checked separately on clean complete commit checkouts. Its receipt records the actual five prescribed commands, checkout identity and status. It is not a mathematical proof checker.

## Final boundary

The baseline universal consumer is retained with explicit `FrontierMerger`; the compiled critical alternative retains explicit `RecordLock` and `CycleExclusion`. No custom axiom, placeholder proof or unproved source lemma was inserted to discharge them. The all-source ordinary merger, full cycle-denominator exclusion and fixed-gate source upper estimate remain open. Late PR200/201 material is reviewed separately in the intake reports, not silently assumed by these proofs.
