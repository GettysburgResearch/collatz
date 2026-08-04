# Live repository review — wave 10

**Date:** 2026-07-31  
**Agent:** `gpt56-pro-03`  
**Scope:** complete inspection of the six newly supplied PDFs and direct attack on the centered and pulse blockers  
**Status:** source audit, exact corollaries, and one new branch-qualified finite-reduction theorem

No positive ordinary Collatz counterexample, nontrivial positive cycle, or unconditional resolution is claimed.

# 1. The centered source question is now settled sharply

The exact Dubickas 2006 constant at `(81,64)` is

\[
\frac{E(64/81)}{81}
=0.007747163838833358349\ldots<1/81.
\]

Using `81/64=(3/2)^4` and applying the same source theorem to `8xi` improves the necessary lower limit to

\[
\boxed{
\limsup|u_n|
\ge
\frac{3-T(2/3)}{324}
=0.008819168830315322822\ldots .}
\]

This is a genuine new corollary, but it remains below `1/81`.

Dubickas 2009 proves that neither sign half can persist: any hypothetical centered orbit has positive and negative errors infinitely often. The 2008 two-interval theorem does not match the native two-sided union.

**Conclusion:** the centered blocker is arithmetic stabilization, not a missing scalar real estimate. PR #16 should remove the conditional source language and PR #67 should use the outer-band requirement only as a renewal constraint.

# 2. The Matveev boundary in PR #53/PR #70 is closed

The complete English PDF confirms that Corollary 2.3 applies with

\[
\alpha_1=2,\quad\alpha_2=3,\quad D=1,
\quad A_1=\log2,\quad A_2=\log3.
\]

The first source constant at `n=2` is below `748,000,000`, so the branch's use of `2^32` was safe but coarse. Exact interval arithmetic now gives the strengthened cutoffs:

```text
T-8255 P3:   14.6 billion
T-8255 P11:   3.8 billion
T-8260 P3:   23.8 billion
T-8260 P11:   5.8 billion
```

The Matveev step may now be labeled `SOURCE-AUDITED`. Native theorem statuses remain separate.

# 3. Fixed support is finite-decision far beyond three pulses

For exactly `s` pulses, rotate after the largest gap. The last support then lies before fraction `(s-1)/s` of the repeated word. The same pulse-correction positivity used by PR #70 gives

\[
0<\Lambda
<2c_*\exp\left[-r\left(A\log2-\frac{s-1}{s}k\log3\right)\right].
\]

Matveev supplies a contradictory polylogarithmic lower bound whenever the exponential rate is positive. Combining this with PR #53 `L-8201` yields:

```text
P3=(1,2):
  every fixed support s<=18 is a finite exact decision;

P11=(1,1,1,2,1,1,4):
  every fixed support s<=117 is a finite exact decision.
```

This is not yet an exclusion. It identifies the exact next computation—support four—and the first genuine density barrier, support `19/118`.

# 4. The p-adic papers sharpen the next bridge, not the final conclusion

Bugeaud 2002 gives simultaneous `m`-adic estimates for a genuine two-term residual under explicit principal-unit hypotheses. Chim 2025 gives a single-prime estimate with optimal logarithmic exponent-height dependence.

For every fixed prime `ell>=5`, Chim implies

\[
v_\ell(2^a-3^b)=O_\ell(\log(a+b)).
\]

Hence the part of a growing denominator supported on any fixed finite prime set is only polynomial. Denominator families must continually acquire fresh primes.

The missing contradiction is now precise:

\[
\boxed{
\text{find a fresh denominator prime that cannot divide the pulse correction/resultants}.}
\]

Without this bridge, fresh primes are structural information rather than a full-denominator obstruction.

# 5. Files supplied to future agents

Wave 10 commits source-faithful capsules rather than the PDFs themselves:

```text
LIT-KTHM-0058  centered limit points and four-phase lift
LIT-KTHM-0059  small-interval/Sturmian boundary and nonapplications
LIT-KTHM-0060  exact Matveev log2/log3 specialization
LIT-KTHM-0061  fixed-support finite reduction
LIT-KTHM-0062  Bugeaud simultaneous m-adic theorem
LIT-KTHM-0063  Chim p-adic two-log theorem and finite-prime escape
```

Every note records theorem/page locations, hypotheses, native substitutions, gap audits, and what the source does not prove. Two exact replay artifacts freeze all numerical constants.

# 6. Highest-value next work

## A. Support four

Generalize the PR #70 continued-fraction layer symbolically in support `s`, then enumerate only the surviving small packets with `L-8201`. Do not start with a blind cap-box scan.

## B. Centered renewal composition

Compose two consecutive PR #67 height charts while retaining the transported ordinary quotient. Add the source constraints:

```text
both signs recur;
outer error band |u|>=0.008819... recurs infinitely often.
```

A successful ranking theorem must force an empty chart interval for the same seed, not choose a new quotient at each height.

## C. Fresh-prime/resultant incompatibility

For a fixed pulse support, choose a prime divisor of `D=2^a-3^b` outside the finite coefficient set and compare the orders of `2` and `3` in the one-variable resultants. The target is a proof that one such prime cannot divide all `E_i`.

## D. Six-branch zero digit

None of the six PDFs touches the exact zero-digit hitting theorem. It remains the cleanest negative ordinary-orbit target.

# Bottom line

The supplied papers produce real progress, but not a hidden Collatz resolution:

1. the centered source ambiguity is closed and the remaining gap is proven arithmetic;
2. the pulse Matveev step is validated and strengthened;
3. fixed-support pulse search is reduced to finite computation through support `18/117`;
4. the p-adic literature isolates the next missing prime-divisibility bridge.
