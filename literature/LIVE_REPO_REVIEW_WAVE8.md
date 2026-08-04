# Live repository review — wave 8

**Date:** 2026-07-23  
**Agent:** `gpt56-pro-03`  
**Scope:** newest constructive and critical-path work after wave 7  
**Status:** literature/strategy audit; no native status promotions

No positive-integer Collatz counterexample, nontrivial positive cycle, or unconditional resolution is claimed.

## Frozen heads inspected

```text
PR #45  a7846473b10aa5caf8c9c57b0a612db0b8db402a
PR #48  738b230c22d6475095945998ca89662714973d72
PR #50  1cba8c76a3b20eeafdfa6941c9847b77105e6ae4
PR #53  b9593b0c47bc893afaaaf31f1fc3519f52c20762
PR #16  87478352e65c7b816dfc8b3b30894b71fb50f662
```

PR #19 `ITERATION_10` and the latest PR #49/PR #51 interfaces were also inspected through their current changed files and review crosswalks.

# 1. Main eureka — the six-branch chart is one canonical rational-base orbit

PR #45/PR #50 use

```text
M=2^19,
N=3^12,
M h_(n+1)=N h_n+C_i,
i in {0,...,5}.
```

Every `h_n` is divisible by three. Put `x_n=h_n/3`. Then

```text
2^19 x_(n+1)=3^12 x_n+a_i,
a_i=C_i/3.
```

The six digits are

```text
229376
258048
290304
326592
367416
413343
```

and all lie below `2^19`. Therefore every legal native transition is exactly

```text
x_(n+1)=ceil(3^12 x_n / 2^19),
a_n=2^19 x_(n+1)-3^12 x_n,
a_n in A.
```

This is not a loose analogy. Reducing the same equation modulo `2^19` and `3^12` recovers the native source and output cells. The positive construction problem has the exact one-line form:

```text
Find x_0>0 whose minimal word in rational base 3^12/2^19
uses only the six digits A forever.
```

PR #45/PR #50's physical conjugacy would then turn `x_0` into an explicit positive unbounded shortcut-Collatz orbit.

## Immediate rigorous literature constraints

Dubickas's theorem applies verbatim to this exact ceiling map. The digit word must satisfy

```text
liminf p(L)/L >= log(2^19)/log(3^12/2^19)
                 = 971.866577472...
```

Therefore every periodic, Sturmian, Arnoux–Rauzy, or otherwise low-linear-complexity controller is excluded. Any proposed substitution, automaton, Farey grammar, or S-adic controller should report a proved factor-complexity upper bound and compare it to this number.

The rational-base tree literature further says that all integer-rooted futures are distinct and that the successor operation on minimal words is realized by an infinite sequential transducer retaining essentially the whole integer tree. This strongly supports the repository's finite-nucleus-plus-unbounded-root architecture.

The 2025/2026 normality conjecture predicts that every nonzero minimal word is normal over all `2^19` minimal digits. If true, it immediately forbids confinement to six digits. This is a precise conjectural finish line, not a theorem.

# 2. PR #48/PR #49 — transported stacks, not raw radix digits

The second-pass correction on PR #48 is conceptually correct and important. The current quotient's ordinary Euclidean digits are twisted by each intervening odd affine multiplier and carry. The genuine future stack is the pulled-back nested residue

```text
Theta_s=[-P_s^(-1) B_s] mod K_s,
```

from `L-8210`.

`LIT-KTHM-0054` records the stationary rational-base specialization:

```text
Q^s x_s=P^s x_0+C_s,
x_0=Theta_s mod Q^s.
```

An ordinary root exists exactly when the least representatives `Theta_s` eventually stabilize. This places the large generated-capacity theorem correctly: growth creates room for many transported levels, but legal content must still be generated through the inverse-affine cocycle.

The rational-base literature's infinite-tree phenomenon suggests that the unbounded quotient is not an implementation accident. It may be mathematically indispensable.

# 3. PR #50 critical Farey/mechanical grammar

The Farey/Christoffel compiler is now connected to two separate literatures:

1. **finite critical words:** Bugeaud–Reutenauer's integer-Ostrowski parametrization of Christoffel conjugates may compress rotations, borders, and sibling-swap choices more canonically than rotation-by-rotation enumeration;
2. **infinite chart paths:** Dubickas's rational-base complexity lower bound is a hard admissibility test on any limiting type word.

The crucial distinction is that the finite cycle grammar and the infinite minimal-word chart solve different ordinary equations. A Christoffel/Farey normal form can reduce a finite denominator circuit without implying that the corresponding infinite minimal word remains in the six-digit alphabet.

The mixed-place height theorem `L-8310` remains the right finite-cycle closure gate:

```text
real near-integer
+ physical dyadic replay
+ odd-prime quotient depth
=> exact C=ND.
```

The rational-base reduction does not replace that finite-cycle identity; it gives a cleaner divergence lane.

# 4. PR #53 pulse resultants — repetition length is now the sole infinite parameter

`L-8201` eliminates every pulse-height coordinate for one fixed negative-cycle word and proves explicit support-wise caps using a unique minimum `2`-adic valuation in the Sylvester resultant.

The next literature-supported ladder should be:

```text
native sparse resultants
 -> one fixed equation in the repetition parameter
 -> real and p-adic logarithmic bounds
 -> de Weger lattice reduction
 -> exact finite replay.
```

If the normalized repetition equation forces a large common divisor of multiplicatively independent exponential sequences, the Bugeaud–Corvaja–Zannier subexponential gcd theorem may give a contradiction. If coefficients vary with repetition, Corvaja–Zannier's variable-coefficient S-unit framework is a closer neighbor. Neither source applies until the native equation is written in their exact hypotheses.

Zero resultants or proper vanishing subsums should be treated as constructive resonant families and split into separate claims.

# 5. PR #16 centered powers

The exact ordinary-survivor equivalence

```text
||xi(81/64)^n|| <= 1/81 for every n
```

has now generated native recurrence and Thue–Morse exclusions. The remaining useful literature task is not another general Fourier theorem. It is full acquisition and exact specialization of Dubickas's nearest-integer limit-point and two-interval theorems:

```text
compute the explicit (81,64) constant;
compare it to 1/81;
extract the extremal sign/carry language;
translate that language to the appended blocks q_K.
```

The equality case is now meaningful because the branch has native tools excluding broad morphic and small-state encodings.

# 6. PR #19 H frontier

The latest H iteration supplies:

- a polynomial macro-growth barrier;
- explicit fresh-prime budget from the quantitative S-unit theorem;
- a sharper deficit-pressure identity.

For a finite macro grammar, the natural external framework is automaton-constrained switching:

```text
path-complete potential  -> exclusion/stability certificate;
occupation-measure dual  -> exact high-growth cycle or flow candidate.
```

For scalar multipliers, maximum cycle mean is the first exact layer. The affine intercepts then require one augmented ordinary state. A failed solver should output a rational cycle/occupation measure that can be replayed as an H renewal candidate, not merely report infeasibility.

# 7. Role of the supplied Väänänen–Wallisser paper

The full paper remains a powerful low-complexity firewall. Its Theorem 1 gives quantitative p-adic linear independence for Tschakaloff values in distinct multiplicative orbits, and its Padé determinant supplies explicit nonvanishing. It is well suited to periodic or finite-dimensional prescribed controllers.

The six-branch rational-base offense is different: its candidate digit word is the canonical minimal word of an ordinary integer root and is expected to require unbounded complexity. Väänänen–Wallisser should prune periodic reductions, not replace the restricted-minimal-word search.

# 8. Recommended next work

## Priority 1 — restricted minimal-word solver

Build one proof-producing program for

```text
P=3^12,
Q=2^19,
A={229376,258048,290304,326592,367416,413343},
x -> ceil(Px/Q).
```

It should:

1. retain the exact ordinary root/quotient;
2. generate the unique minimal digit;
3. reject immediately outside `A`;
4. use exact residue-cylinder pullback for long prefixes;
5. search for an inductive nonlinear arithmetic class, not a prescribed periodic word;
6. output a direct physical Collatz replay for any hit.

A positive infinite invariant here is a complete unconditional counterexample.

## Priority 2 — complexity/Ostrowski filters

- compute exact factor complexity of every proposed controller family;
- reject any family whose upper coefficient is below `971.866...`;
- encode critical Christoffel rotations through integer Ostrowski coordinates;
- preserve the ordinary root rather than only the word grammar.

## Priority 3 — repetition reduction on PR #53

Expose one repetition-only S-unit/exponential equation and feed it through explicit logarithmic bounds and LLL reduction.

## Priority 4 — full Dubickas specialization on PR #16

Obtain the exact source formulas and equality language at `(81,64)`.

## Priority 5 — H cycle/potential dual

Implement a proof-producing path-complete/occupation-measure pair on one frozen H macro grammar.

# Bottom line

The newest work is genuinely converging. PR #45/PR #50's six-branch construction is not merely another chart: it is an exact restricted minimal-word problem in one rational base. The repository now has a clean external theory for the tree, complexity, transducer, and conjectural normality of that word.

The full objective is therefore at a sharply named boundary:

```text
Does one positive integer have a minimal 3^12/2^19 word
confined forever to the six physical digits?
```

No such integer is presently supplied.
