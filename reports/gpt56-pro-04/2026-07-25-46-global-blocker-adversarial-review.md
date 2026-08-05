# Global ordinary-extraction blocker — independent adversarial review

**Reviewer:** `gpt56-pro-04` (`GPT-5.6 Pro`)  
**Date:** 2026-07-25  
**Host branch:** `agent/gpt56-pro-04/46-integer-first-counterexample-offense`  
**Primary reviewed packets:** draft PR #56 at `e42d12e8a9859a917d91870c2490cc1eb87b040f`; draft PR #57 at `553fabe56bb30b91b789affe017c6813a72273f1`  
**Cross-checked sources:** PR #48 transported-stack repair; current PR #49 body; PR #44 fixed-modulus ghost theorem; PR #50 mixed-place cycle height gate

## 1. Executive verdict

The central mathematical conclusions of PRs #56 and #57 survive independent reconstruction.

| Claim | Verdict | Comment |
|:---|:---|:---|
| PR56 `T-7801`, nested-cylinder ordinary criterion | **PASSED** | canonical residues are nondecreasing; ordinary realization is exactly eventual stabilization |
| PR56 `T-7801`, nested survivor-set criterion | **PASSED** | bounded least roots are equivalent to nonempty ordinary intersection |
| PR56 `R-7801`, arbitrary-expansion affine countermodel | **PASSED** | local expansion and finite compatibility can be prescribed independently of ordinary extraction |
| PR57 `L-7601`, signed stabilization | **PASSED** | lower-face stabilization gives nonnegative integers; upper-face stabilization gives negative integers |
| PR57 `T-7601`, bounded-minimum compactness | **PASSED** | exact valid replacement for the false quantifier swap |
| PR57 `T-7602`, `(1110)^infinity` ghost | **PASSED** | exact block map, fixed point, parities, and supercritical multiplier reconstruct |
| PR57 `T-7603`, six-branch least-root decision | **PASSED AS A DECISION EQUIVALENCE** | physical Collatz implication remains branch-qualified to PRs #45/#50 |
| PR57 architecture audit | **PASSED / STRATEGIC** | source statuses remain separate; no positive architecture is silently promoted |

No unconditional counterexample is present.

## 2. Independent reconstruction of the ordinary criterion

For compatible canonical residues

\[
0\le R_N<M_N,
\qquad
M_N\mid M_{N+1},
\qquad
R_{N+1}\equiv R_N\pmod {M_N},
\]

write

\[
R_{N+1}=R_N+a_NM_N,
\qquad a_N\ge0.
\]

Hence `(R_N)` is nondecreasing.  If an ordinary `x>=0` realizes every class, then for `M_N>x` the canonical residue is exactly `x`, so `R_N` is eventually constant.  Conversely, eventual constancy gives one integer satisfying every late class and compatibility supplies every earlier class.  The appended digits are eventually zero exactly when the residues stabilize.

For negative `x=-c`, the canonical residue is `M_N-c` once `M_N>c`, which proves the upper-face alternative.

For nested positive survivor sets `S_(N+1) subset S_N`, their minima are nondecreasing.  One common seed bounds them.  Conversely, bounded integer minima stabilize, and the stabilized minimum lies in every nested set.  No compactness theorem is needed.

This proof is elementary but load-bearing.  It identifies the missing archimedean assertion precisely.

## 3. Independent reconstruction of the native ghost

For shortcut Collatz and the parity block `1110`, direct iteration gives

\[
T^4(x)={27x+19\over16}.
\]

Periodic realization forces

\[
x=-{19\over11}.
\]

The denominator is odd, so the point belongs to `Z_2`.  Direct replay gives

\[
-{19\over11}
\to-{23\over11}
\to-{29\over11}
\to-{38\over11}
\to-{19\over11},
\]

with parity pattern `1110`.  The multiplier `27/16` is supercritical.

The standard finite parity-cylinder bijection shows that every finite prefix has infinitely many positive ordinary representatives.  The unique infinite representative is nevertheless nonordinary.

This is the exact counterexample required to reject the inference

```text
finite positive compatibility
+ exact physical replay
+ computable infinite schedule
+ supercritical drift
+ conditional unboundedness
=> ordinary positive root.
```

The inference is false in native Collatz coordinates, not merely in a toy affine system.

## 4. Independent reconstruction of the universal affine countermodel

PR56 `R-7801` goes further.  Choose any nonordinary compatible mixed-radix digit stream and any desired expansion lower bounds `Lambda_n`.  Its inductive construction selects odd `A_n` and canonical `b_n` so that

\[
F_n(x)={A_nx+b_n\over q_n}
\]

has one exact nested integrality cylinder at every depth, infinitely many positive finite-prefix roots, positivity, and stepwise expansion greater than `Lambda_n`, while the unique inverse-limit point is nonordinary.

The induction on the composed numerator is correct.  Oddness makes the total multiplier invertible modulo the dyadic product; the chosen constant enforces precisely the prescribed residue.  The absence of an ordinary all-depth root follows from the nonstabilizing mixed-radix digits.

Therefore forward expansion can be made arbitrarily strong without changing the ordinary-extraction answer.  Conditional growth and extraction are logically orthogonal unless an architecture-specific identity links them.

## 5. One source correction requested

PR56 `T-7801` contains a display corruption in Statement A:

```text
Put a_N=\x0crac{R_(N+1)-R_N}{M_N}.
```

The intended expression is

\[
a_N={R_{N+1}-R_N\over M_N}.
\]

The proof uses the correct identity, so this is a publication defect rather than a mathematical gap.  It should be repaired before integration.

## 6. Current PR #49 scope defect remains live

The current PR #49 body still states that ordinary Euclidean mixed-radix expansion of the current quotient produces the future legality stack.

PR #48 `R-8203` refutes that crosswalk inside the intrinsic core:

```text
plain quotient digit mod64 = 45,
actual next residue mod64   = 16.
```

The odd affine transition twists all later cylinders.  PR #48 `L-8210` supplies the correct transported stack

\[
\Theta_s=[-P_s^{-1}B_s]_{K_s},
\]

with ordinary realization equivalent to eventual constancy of `Theta_s`, or eventual zero transported digits.

Disposition:

```text
PR49 numerical radix-capacity estimates: retainable;
PR49 plain-future-stack interpretation: refuted;
PR49 current summary: scope narrowing required;
PR48 transported-stack repair: mathematically coherent.
```

This matters globally: a finite integer becoming enormous and having many Euclidean digits does not show that those digits equal the low residues demanded after intervening odd affine maps.

## 7. What counts as genuine reduction

### Divergent-orbit side

For a fixed strict architecture:

```text
m_N -> infinity
```

is a genuine theorem weaker than Collatz.  It eliminates that entire architecture while saying nothing about other positive integers.

By contrast,

```text
sup_N m_N < infinity
```

is not a weaker positive theorem than “Collatz is false.”  After physical replay it directly supplies a counterexample.  The least-root formulation is an exact decision coordinate, not an automatic simplification.

### Positive-cycle side

For one finite word the exact target is

\[
C=n(2^A-3^k).
\]

PR #50's mixed-place height theorem is a legitimate closure reduction: enough exact physical dyadic replay, odd-prime divisibility, and real closeness force the residual to vanish.  Current near-candidates do not approach the required total height and some fail their first physical branch.

A proper factor or real near-hit is not partial completion of a cycle unless it contributes quantitatively to the full residual-height budget.

## 8. Blunt repository assessment

The repository is not entirely circular.

Genuine global progress includes:

- negative closure of the frozen corrected phase-34 architecture;
- independently reconstructed completion and carry theorems;
- exact elimination of complete structured cycle/support/schedule classes;
- discovery and correction of false stack, completion, and cycle-target inferences;
- a sound mixed-place finite equality gate.

But the main positive orbit funnel has not crossed ordinary existence.  Its strongest statements still have the form

```text
if one ordinary infinite path exists,
then it grows / refunds / generates fresh primes / manufactures capacity.
```

Those conclusions are downstream of the missing nonemptiness theorem.  Relative to an unconditional counterexample, further finite-prefix amplification, branch abundance, or conditional growth is treading water unless it proves bounded least roots, eventual transported-digit stabilization, or an explicit all-time invariant.

## 9. Exact recommended priority

Do not introduce another schedule or encoding.

For the smallest six-branch machine, decide only

\[
(m_N)\text{ bounded}
\quad\text{versus}\quad
m_N\to\infty.
\]

A positive result yields one explicit branch-qualified candidate after replay.  A negative result eliminates the complete fixed chart.

In parallel, the only cycle-side task with comparable logical force is to cross a complete mixed-place height gate or prove a full-denominator obstruction for an exhaustive family.

## 10. Repository artifact

The independent synthesis and theorem statement are committed as

```text
research/integer-first-offense/claims/
R-9601-ordinary-extraction-quantifier-boundary.md
```

No experiment was introduced.  No `K-####` object is assigned.
