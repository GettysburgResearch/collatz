# Independent narrow review of the component-rigidity route

**Verdict: VERIFIED for the conditional statements and exact files pinned
below.** This review does not establish the merger hypothesis (E),
unconditional Collatz convergence, actual merger clocks for (E), or a
claim of priority. Reviewed on 20 November 2026 by the adelic-route
agent, separately from the component proof's author and the parent
algebra check.

The review independently reconstructed the functional identities, every
descent branch, the ordinary component implication, and the smaller
sufficient law system. It also inspected and executed the symbolic
checker. Agreement with the parent check is not the basis of the verdict.

## 1. Exact review boundary

The reviewed final proof and reduced-law supplement were read in the
isolated publication checkout
`/workspace/scratch/6c37546fb87e/collatz-structural`.
Paths below are relative to its repository root.

| File | SHA-256 |
|---|---|
| `research/structural-reset-20261120/component/PROOF.md` | `0a7d555cfa52a1b8d0de147ff2ebdf6e33e5a51d6a2a39500986ef6c206a7985` |
| `research/structural-reset-20261120/component/REDUCED_LAWS.md` | `69ef4a4f56862fac521c6f6e7fe001b885929a7971503c0d4472d7767eb530fa` |
| `research/structural-reset-20261120/component/check_component_rigidity.py` | `c809daf77560c1608e6e39e4cd6cdd792b420924029f32b5fda640ffa9a425ce` |

The original proof inspected in the source checkout had SHA-256
`274f47167d64bc49d5a34e222d1e5ef883652d0f037f510d88ecc2d5468fb245`.
The reviewer requested one explicit scope qualification in its auxiliary
fixed-word discussion: **fix the ray exponent a** before claiming two
fixed parity words can work for at most one value of x. An exact diff
confirmed that the final proof differs only by this qualification.
No main theorem or descent case required repair.

The checker bytes were identical in the source and publication checkouts.
Execution was performed in the source checkout; the identity is established
by the displayed hash, not an assumption that the copies match.

The baseline identified by the proof is
`55d8968d2ecbc23a91c9c4733929f34be9bf0d28`.
This review does not extend to later edits or to whole neighboring research
packets. External overlap statements are provenance, not dependencies
verified here.

## 2. Claim-level verdicts

| Statement | Verdict and scope |
|---|---|
| Definition of the restricted merger domain and its density | VERIFIED: positive even 2-adic valuation and coprimality to three; natural density 1/9. |
| CR-001: restricted ordinary mergers imply Collatz, and conversely | VERIFIED as an equivalence conditional on the universal hypothesis (E). The hypothesis itself remains OPEN. |
| Derivation of (A)--(D) from (E) and actual ordinary paths | VERIFIED on precisely the printed domains. No global equality F=f is assumed. |
| CR-002: every function satisfying (A)--(D) is constant | VERIFIED by the complete least-label descent. |
| Total successful selector, strict descent, uniform bound | VERIFIED for the abstract conditional laws. Its step count is not a physical Collatz-time bound. |
| `REDUCED_LAWS.md`: (R1)--(R3) imply the four-law system | VERIFIED, with no extension of the odd ternary-unit domain of (R2). |
| Symbolic checker coverage | VERIFIED: 480 residue cells represent every input greater than 1, with all permitted affine lifts checked symbolically. |
| Auxiliary fixed-parity-word obstruction | VERIFIED for each fixed a, as made explicit in the final proof. It does not rule out input-dependent clocks or recursive proofs. |

## 3. Reconstructing the implication from E

The map is the positive ordinary shortcut map. Orbit meeting at independent
finite clocks is an equivalence relation: two meetings through the same
intermediate orbit can be advanced to a common later intermediate time.
Consequently actual merger components are legitimate invariant labels.

Let f be any map into an arbitrary set, invariant under the shortcut map,
and assume (E) only for t=4^a x with a at least one, x odd, and 3 not
dividing x. Ordinary even steps give f(t)=f(x). The exact relation
T squared of (4z+1) equals 3z+1 can be applied successively a times to
5 times 4^a x plus 1. This gives the endpoint 5 times 3^a x plus 1.
The odd integer 5 times 3^(a-1) x has that endpoint as its unhalved odd
output. Equality of the labels at an odd input and its unhalved output
uses one shortcut step and doubling invariance, both available from f.
Thus the proof's equation (1) is valid, with E invoked only on its domain.

Replacing x by powers of five times x preserves oddness and coprimality
to three. This derives equation (2) for all indicated i and j. For
F(n)=f(5n), factor n=2^v 3^i x with x an odd ternary unit. Removing powers
of two and using equation (2) gives F(n)=f(x). Multiplication invariance
under 2, 3 and 5 follows on the full positive domain.

The equality F=f is justified on all ternary units, including even ones.
It is also justified separately on multiples of five. The proof correctly
does not infer it on every multiple of three.

The additional laws have the following exact checks:

- **B:** n is odd and a ternary unit, and 3n+1 is a ternary unit. F=f
  is available at both endpoints of the ordinary unhalved odd relation.
- **C:** when n is 3 modulo 4, both inputs beginning at 5n are odd.
  The exact second iterate is 5(9n+1)/4. Doubling invariance then gives
  F(n)=F(9n+1). This argument does not require n to be a ternary unit.
- **D:** when n is odd, 5n is odd and 15n+1 is a ternary unit. The
  relation f(5n)=f(15n+1)=F(15n+1) is therefore legal for every odd n.

For completeness, the density calculation is independent of any dynamical
claim. The disjoint layers with 2-adic valuation 2a and coprimality to
three have densities (2/3) times 2^(-2a-1). Summing for a at least one
gives 1/9; the discarded high-valuation tails have vanishing density.

## 4. Complete descent and domain audit

The least integer with a label different from F(1) exists by ordinary
well-ordering, irrespective of any ordering on the target label set.
Dividing out an available factor 2, 3 or 5 forces that integer to be
coprime to 30. The following cases then exhaust it.

| Case | Strictly smaller q | Domain and divisibility check |
|---|---|---|
| n=1 modulo 4 | (3n+1)/4 | B is legal at the odd ternary unit n; divisibility by 4 is exact; n>1 gives strict descent. |
| n=7 modulo 8 | (3n-1)/4 | q is positive, odd, and 2 modulo 3. C at n, division by 4, and reverse B at q give the equality. |
| Remaining n=3 modulo 5 | (3n+1)/10 | B at n; numerator divisible by 2 and 5. |
| Remaining n=1 modulo 5 | (9n+1)/20 | C at n; numerator divisible by 4 and 5. |
| Remaining n=4 modulo 5 | (27n+7)/40 | p=(9n+1)/4 is odd, 1 modulo 3, and 3 modulo 5. C, division by 4, B at p, then division by 10 are legal. |
| Remaining n=2 modulo 3 | (8n-1)/15 | The remaining n is 2 modulo 5. Thus q is a positive odd integer, and reverse D at q is legal because 15q+1=8n. |

After these cases, the simultaneous congruences force n=67 modulo 120,
so in particular n is at least 67. Let u=(3n+1)/2 and v=(9n+5)/8.
The first B application is legal at n. The value u is odd, 1 modulo 4,
and 2 modulo 3, so the second B application is also legal. The resulting
v is 1 modulo 15. Its cases are exhaustive:

- If v is even, q=(9n+5)/16 is an integer and is less than n.
- If v is 1 modulo 4, B at v gives q=(27n+23)/32. The ternary-unit
  condition follows from v=1 modulo 15; n at least 67 supplies the
  needed strict inequality n>23/5.
- If v is 3 modulo 4, C at v followed by division by 20 gives
  q=(81n+53)/160. Its factor of five follows from v=1 modulo 5.

Every output is positive. The other strict inequalities are immediate
linear inequalities on the respective positive domains. Checking the
displayed formulas also verifies the uniform bound
q at most (27n+23)/32, including the initial smooth-factor cases.
For n at least 8 this is at most 15n/16. Strict descent handles the
remaining small inputs, so the claimed logarithmic number of abstract
reductions is justified.

This reasoning produces a finite chain of equalities under the assumed
laws. It does not provide clocks for the open ordinary mergers used to
derive those laws.

## 5. Smaller sufficient law system

For odd x prime to three, R3 at x and R2 at 5x are both legal and share
the upper value 15x+1. Hence F(5x)=F(x). For arbitrary n, removing powers
of 2 and 3 by R1 from n and 5n extends this equality to F(5n)=F(n).

For n=3 modulo 4, p=(15n+1)/2 is positive, odd, and 2 modulo 3. R3 at
n, R1 dividing by 2, and R2 at p give

\[
 F(n)=F(p)=F(3p+1)
 =F\left(5(9n+1)/2\right).
\]

The just-proved multiplier-five equality and R1 reduce the final term
to F(9n+1). All arguments are positive integers. Thus C is recovered
on its entire stated domain, and R1 together with multiplier five gives
A. The reduced system supplies B and D directly, so CR-002 applies.

There is no circular use of C to prove multiplier five, and no use of
R2 at a multiple of three. This is a smaller sufficient presentation,
not a proof that it is minimal or that its nontrivial invariances hold
unconditionally for actual components.

## 6. Checker semantics and actual executions

The checker was read before execution. It uses integer affine pairs for
n=480k+r. Its residue operations first require the coefficient of k to
vanish modulo the relevant modulus, so a tested residue applies to every
allowed k. Exact division requires both coefficients to be divisible.
Every law edge checks its algebraic relation, its full input domain, and
positivity of both endpoints.

The loop uses r=1 through 480. This is a complete positive residue-cell
representation: r=480 handles the positive multiples of 480. The cell
r=1 starts at k=1, excluding exactly n=1, the induction base. Every other
cell starts at k=0. There is no missing positive input greater than 1.

Positivity, strict descent and the uniform bound are checked by
nonnegative affine slope together with the value at the least permitted
k. Thus these are universal inequalities on each cell, not numerical
samples of representatives. Every branch creates an explicit chain of
primitive A2, A3, A5, B, C and D applications. The checker does not
derive those laws from E; that is part of the separately reviewed proof.

The following command was actually run in the source checkout:

```sh
python -X utf8 -B research/structural-reset-20261120/component/check_component_rigidity.py
```

It exited with code 0 and returned PASS, with 480 symbolic residue cells,
a maximum of nine primitive law applications per reduction, and successful
strict-descent and uniform-bound checks. The branch counts were:

| Branch | Cells |
|---|---:|
| factor_2 | 240 |
| factor_3 | 80 |
| factor_5 | 32 |
| one_mod_four | 64 |
| seven_mod_eight | 32 |
| three_mod_five | 8 |
| one_mod_five | 8 |
| four_mod_five | 8 |
| inverse_fifteen | 4 |
| last_even | 2 |
| last_one_mod_four | 1 |
| last_three_mod_four | 1 |

The reported primitive-law counts were A2=510, A3=80, A5=57, B=121,
C=49, D=4. The output explicitly reported that neither E nor
unconditional Collatz was proved.

The optimized-mode command was also actually run:

```sh
python -O -X utf8 -B research/structural-reset-20261120/component/check_component_rigidity.py
```

It correctly exited with code 1 and the message
`Run without -O: certificate checks require assertions.`
This confirms the intended rejection rather than silently disabling the
checks. No broad orbit search or enlarged finite verification was used.

## 7. Final ordinary implication and remaining uncertainty

Once CR-002 makes F constant, f is constant on ternary units. From any
positive ordinary input, strip powers of two. If its odd part is divisible
by three, one actual odd shortcut step reaches a ternary unit. Therefore
f is constant everywhere, without assuming F=f on all inputs beforehand.

Choose f to label actual ordinary merger components. Every source then
meets the component of 1 at finite clocks. The forward orbit of 1 is the
two-cycle 1 to 2 to 1, so meeting that component implies actually reaching
1. The converse implication from Collatz to E follows immediately by
meeting at 1.

The strongest uncertainty is exactly E: ordinary orbit meeting for every
parameter in its infinite restricted domain. The complete descent is
conditional on the derived laws, and those laws were not promoted into
evidence for E. The packet establishes the promised equivalence and
algebraic continuation, not either an unconditional proof of E or a
solution of Collatz.
