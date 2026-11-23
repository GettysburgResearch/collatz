# Independent reconstruction: cyclic phase and full-denominator carry

Reviewer: coordinating researcher, separate from the arithmetic author. Date: 2026-11-23.

Reviewed `HIGH_VARIANCE_ARITHMETIC.md`, SHA256 `9d9d2fa408c68e497c7497477befcc2ff5414ff1214d7d6381129e374db448c2`.

**VERIFIED for the displayed written deductions, with the literature boundary below.**

The cyclic-window argument averages over every starting point, so each offset permutes the same p-point measure even when q exceeds the period. The mean accumulated correction is exactly q*eta. This removes the window boundary term without asserting distinctness across repeated traversals. The continued-fraction choice and Rhin successor bound give exponent 1/8.616. The coordinator separately inspected Lagarias–Soundararajan equation (5.11); the original Rhin proof is not replayed. Leading-word counts, growing run thresholds and exponential-run moments follow with the stated sufficiently-large-minimum qualifications.

The narrow-cycle order argument produces the rank permutation j -> j+k modulo p, with gcd(k,p)=1 under primitivity. The unit u=2^r3^s modulo the whole D satisfies u^p=2 and u^A=3. The geometric sum has the explicit unit certificate u^(p-1)(u-1)P=1. The D=1 and all-gap-two exceptions are handled. No priority is claimed for this high/balanced-cycle exclusion, and no inaccessible literature proof is counted as reviewed.

For multiple height layers, the order inversion inequalities retain the positive odd displacement. Separation 2 gives only the identical odd-successor case, which is excluded by primitive-cycle distinctness. The varying weights 2^(-k_i) remain in the distinguished numerator. Their being units individually is not used to claim their sum is a unit.

For the carry recurrence, L modulo 2 is the identity, the bit of its rational solution equals the integer carry parity, and L^(-1)c_next=(L^(-1)c-bit)/2. The invariant box 1-2^a<=c<=2 follows separately for even and odd carries, including negative ones. Reaching zero is exactly nonnegative ordinary integrality of the whole rational cycle.

The M-matrix is B=L*P^(-1), so the firing vector is P*x. Its inverse positivity follows directly from H^p=(3^p/2^A)I. The pure dyadic control uses the correctly permuted vector (5,8,3), not (3,5,8). Its reduced vector (0,0,1) is z-superstable by the displayed inverse bound and proper-support boundary argument. The nine-state even-divisor control is expressly not a Collatz cycle: divisor 10 removes a factor 5. Both controls are separately checked by exact integer arithmetic in this report directory.

Guzman–Klivans is used only for its stated general representative theorem, inspected by the arithmetic author. The coordinator independently reconstructed the matrix arithmetic and both controls, not the complete external energy theorem proof. No all-word zero-class exclusion, global carry ranking or full Collatz proof is asserted.
