# Incoming PR192 and the attribution correction in PR189

This is a root written reconstruction of the specified claims. It does not certify every file in either PR, and it does not count their reported Lean declarations as part of this packet's ten-module replay.

## Frozen bodies

PR192 head `be783656f0e889fe0d5318a2f7a9140099cb94b5`, directory `research/astra-phase-and-cycle-20261124/`:

| File | Git blob | Scope read |
|---|---|---|
| `README.md` | `9403293761380d988b33d2e09a68addcfef5e9b3` | Full overview and stated global boundary |
| `PHASE_SEPARATION.md` | `646f936d8abf50601e13a0ce31f2574b5051e93f` | PS1 through PS6, complete written proofs |
| `CYCLE_FACTORS.md` | `2e3845a9dfc830cf975581e195639c25f97e6e3d` | Sections 1–4, splitting proof and explicit norm controls |
| `FORMALIZATION.md` | `39af6a3a247b7167f75ce01e6c7b21aebf3a4149` | Claimed compiler/statement scope and visibility port |

[Pinned packet](https://github.com/GettysburgResearch/collatz/tree/be783656f0e889fe0d5318a2f7a9140099cb94b5/research/astra-phase-and-cycle-20261124).

## PS1–PS3: actual phase separation

**VERIFIED written, retaining the cited actual-scalar theorem.** For normalized height X=q/2^c, the exact identity is 2^(b+2c) X_next=3X+2^(-c), and X>=1. During a canonical-one run, zero carry forces physical gap one and zero next carry. This yields the exact divisibility of q+1 by 2^(L+1). Positive carry instead makes X contract by at least a factor two until the first zero; multiplying this loss by the remaining zero-carry lower bound gives the claimed source-height constraint. During a canonical-three run, subtracting the affine fixed point 1/5 gives contraction by 3/8. These arguments retain the actual source and do not assume rationality of its phase.

The two endpoint run bounds give the stated local real-power lower bounds. Applying them after n actual steps and using q_n+1<=(3/2)^n(q_0+1) gives the asymmetric fixed-source ternary approximation exponents. The centered phase is not the uncentered scalar in the triadic convergence criterion; excluding ternary-grid centered phases therefore does not exclude convergent sources. The sources 2^k-1 give the stated changing-source optimality of the local lower-side exponent. Aperiodic phases with uniformly short extreme runs are not excluded.

## PS4–PS6: complete finite canonical words and exact scalar fibers

**VERIFIED written.** The finite dyadic inverse congruence gives a literal ordinary gap prefix. A terminal run of unit gaps makes the discounted remainder small enough that canonical and actual digits agree on the desired initial word. This yields density of realized scalar phases, with a new source allowed for every word.

The stronger convergent construction fixes a two-step terminal scalar while varying the target residue. For its rational parameter map F(t), the displayed difference factors into (4^h-1) times a bracket of ternary valuation one, divided by nine. For 3|h, this gives exactly v3(F(t+h)-F(t))=v3(h); the three distinct base residues handle the other differences. Thus it permutes every ternary quotient. Undoing the prescribed gaps preserves positive odd integrality. The terminal value is above one, so a visit to the odd fixed point one cannot have occurred earlier. Backward scalar recurrence gives precisely the claimed carry sequence c_i=2*3^i and phase offset 7/18.

For the denominator-nine scalar fiber, odd first gap gives exactly the parameter range 0<=t<d with a=2t+1 and k=3d-1-3t; an even first gap cannot have reduced denominator nine. The same exact ternary distance identity gives discrepancy at most one in every residue quotient. This improves the physical-prefix flexibility in our ordinary gluing theorem by fixing a complete canonical prefix and a particular scalar, while still varying the source. It supports the same warning against replacing fixed-source asymptotics by finite-word realizability.

## Cycle factors

**VERIFIED written with the stated PR185 inputs.** For an integral monic factor of X^p-2^A, the common complex root modulus gives b dividing its degree. Comparing coefficients in the reciprocal-conjugate identity gives b dividing twice every nonzero exponent, so the factor is a polynomial in X^(b/gcd(b,2)). This supplies the root multiplicity in each projected cyclotomic fiber. The lcm-of-projected-orders conclusion still depends on the pinned PR185 primitivity argument.

Assigning each maximal prime power of g to one surviving order makes the product of the assigned totients divide that order's totient. Products of integers at least two dominate their sum; the sole possible totient one is accounted for separately. Hence the total totient cost is at most n. Counting prime bases and bounding each prime power by 2n gives log p<=3 sqrt(n) log(2n), and therefore residual degree divided by log p tends to infinity. The superpolynomial value bound additionally uses PR185's source-qualified logarithmic-form estimate. It does not imply any bound for the reduced denominator after integer evaluation.

The factor splitting criterion follows from the same fiber multiplicity. A proper factor for even b has exactly b/2 roots over each image, forcing 2^a eta to be a square in Q(eta). The cyclotomic-field test gives precisely v2(h)=2 as the exceptional split case. For a prime-power clock gcd, the resulting top surviving factor gives the stated exponential residual bound.

The rational saturation examples are a concrete obstruction to a proof using only nonzero component norms and polynomial survival. The root reconstructed their literal rational trajectories and complete evaluated denominators independently; this review does not repeat the entire component determinant census or PR185's analytic certificate. The independently replayed four rational controls had respective complete reduced denominators 55, 295, 1,078,415 and 82,955. The last has minimum cyclic state 88,181/82,955, exactly as reported. Positive rational cycles, including cycles above one, are compatible with Collatz. The missing step remains cancellation at the distinguished integer evaluation, plus a separate argument for divergent ordinary orbits.

## PR189 attribution-only change

The full compare from `a0be70b1ffa075cbc50755ac76036108c028d120` to `a390a1a4c75ee95db98b4b683d17c503f4e4a118` changes only eleven introductory lines in `research/stationary-carry-rigidity-20261124/README.md` (new blob `f31649f6387c2dbd80a57f3aef87f78fcfdd83d6`). It credits PR180 `7cfd911d35382d9d3bc988060ba88ade78a4267e`, `research/whole-source-20261123/COLLISION_CORE.md`, sections 3–4, equations (16)–(17), for the stationary collision-gap conclusion that S1 rederives. No proof or code changes. Our frozen old-head review remains a review of the same mathematics; attribution belongs to that earlier source.
