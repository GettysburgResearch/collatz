# A finite-state inverse-conversion order, and an information barrier

**Status: PROPOSED computer-assisted universal certificate and analytic counting argument.** This order normalizes an inverse mixed-base conversion problem. It is not an order decreasing on every forward Collatz step.

## C1. The symbolic cone problem

Given t≥1 and 0<c<3^t with 3∤c, construct k,r such that, for **every positive integer x**,

    T^k(2^k x+r)=3^t x+c,

with exactly t odd steps and 0<r<2^k. The predecessor pass supplied k≤4t−2. Its inverse construction repeatedly replaces a symbolic value Y by `(2^a Y−1)/3`, choosing a so that the new constant is integral and, until the last inversion, not divisible by 3. Each such block gives one odd step and a−1 subsequent halvings in the forward direction.

The positive prefix is retained exactly. The choice of a below depends on the **symbolic affine constant**, not on a hypothetical parity of x. Until the last inversion the coefficient retains at least one factor 3, so the required divisibilities hold for every x. Each inverse source is odd. No intermediate positive trajectory has reached 1 because all endpoints dominate the positive prefix and the explicit inverse blocks stay positive.

## C2. Explicit finite credit and a natural-number rank

The supplied certificate is a function

    V : (Z/6561Z)^×_3 → {0,…,18},

where the domain means residues not divisible by 3 (both parities are included). For every positive unit constant c, the verifier selects an a∈{1,…,6} such that d=(2^a c−1)/3 is a positive unit and

    3a + V(d mod 6561) ≤ 7 + V(c mod 6561).                 (C2)

The certificate contains 4,374 values, encoded in increasing unit-residue order. Its potential-string SHA-256 is

    79a5a259e1773228093d43f5a09ec2acd8e5e26b2050f430a0ce88cb758e8d88.

### Why a finite check proves the quantified inequality

Write c=r+6561q. For a fixed action a,

    d=(2^a r−1)/3 + 2^a·2187q.

Modulo 6561, this depends only on q mod 3. Therefore checking the three lifts q=0,1,2 for each of the 4,374 unit residues checks **every** positive ordinary c. The chosen a must work for all three lifts, not just for a sampled representative. Integrality and being a unit are checked as well. Positivity follows already at the smallest positive representative. The verifier does not trust the synthesis recurrence or a floating-point solver.

For a symbolic state with t remaining ternary factors and unit constant c define

    R(t,c)=7t+V(c mod 6561)−1  if t≥1;
    R(0,anything)=0.

For t≥2 use a from C2. The rank drops by at least 3a. For the final inversion choose a=1 when c≡2 mod 3 and a=2 when c≡1 mod 3; its cost is at most 2, while R(1,c)≥6. Thus this last block is paid too. This is an explicit natural-number, well-founded rank for the entire conversion procedure, not a termination inference from a finite sample.

Summing yields the universal bound

    k ≤ floor((7t+V(c mod 6561)−1)/3)
      ≤ floor((7t+17)/3).                                  (C3)

The constant produced by inversion lies strictly between 0 and 2^k. One elementary induction proves the upper bound: if 0<c_j<3^s·2^b, then `(2^a c_j−1)/3 < 3^(s−1)·2^(a+b)`. After t inversions the upper bound is 2^k. Hence the output is a valid binary suffix, not merely a rational preimage.

### Evidence boundary

The finite inequality certificate and the lifting argument are the proof route. Literal traces of selected x values are only implementation regressions. Synthesis converged in 34 integer iterations; verification checks 13,122 modular lifts and rejects the all-zero-potential mutation. No SMT trust, external formal build, or original-Collatz termination follows from this.

## C3. A separate four-digit cover gives k≤3t

A small complete enumeration supplies a unit-preserving inverse block of four odd events and at most twelve shortcut steps for every unit residue modulo 3^5 (162 states). The terminal problems with 1,2,3,4 remaining odd events have worst-case minimum costs 2,6,9,11. The enumerator starts with the earlier 4t budget, not the desired 3t bound.

For arbitrary t, repeatedly use four-event preserving blocks while t>4, then use the appropriate terminal block. This proves k≤3t. The prefix-lifting argument is the same as C2: four divisions by 3 consume four low ternary digits; the extra digit enforces the final unit condition. `short_plan` independently enumerates these states and replayable exponent compositions.

Choosing among the predecessor construction and the two new constructions gives

    k ≤ min{4t−2, 3t, floor((7t+17)/3)}.

This improves the asymptotic worst-case slope from 4 to 7/3. It does not imply a smaller numeric source: that would require roughly k<t log_2(3), a much more demanding inequality.

## C4. Counting lower bound for ANY same-prefix inverse compiler

There are exactly 2·3^(t−1) unit ternary tails of length t. A shortest binary preimage may be assumed to begin with an odd dynamic step: if the original source were even for every prefix, remove that first halving to obtain a shorter binary preimage with the same prefix.

A length-k parity word with t odd steps and an odd first step has at most `binom(k−1,t−1)` choices. Each parity word fixes at most one residue r modulo 2^k and therefore at most one ternary constant c in the cone identity. Summing over k=t,…,K gives the exact necessary inequality

    binom(K,t) ≥ 2·3^(t−1)                                (C4)

for ANY compiler that covers every unit tail with maximum length K. Collisions between parity words only make this obstruction stronger.

If K=ρt+o(t), the logarithm of the binomial coefficient divided by t tends to

    ρ log ρ − (ρ−1) log(ρ−1).

Thus ρ is at least the unique root of

    ρ log ρ − (ρ−1) log(ρ−1)=log 3,

namely approximately **1.6417941208**, strictly above log_2(3)≈1.5849625007. For example, at t=100 the elementary integer bound requires a universal maximum length at least 167; every coefficient-contracting preimage has k≤158.

There is a stronger coverage consequence. A same-prefix cone `2^k x+r → 3^t x+c` can give a smaller source for EVERY positive prefix x only if 2^k<3^t. Therefore at most

    binom(floor(t log_2 3), t)

unit ternary tails can admit such an all-prefix contracting binary preimage, regardless of dictionary size or search algorithm. Dividing by `2·3^(t−1)` gives an exponentially decaying upper bound, by the preceding entropy calculation. This is an upper bound; not every counted parity word gives a distinct tail or a uniform inequality at small x.

At t=10 the count is at most 3003 out of 39366; at t=20 at most 84672315 out of 2324522934. These are complete combinatorial upper bounds, not empirical success percentages.

## What this rules out—and what it does not

C4 blocks a uniform strategy that proves convergence solely by replacing every longer ternary suffix with a shorter numeric binary source at the SAME positive prefix. It does not exclude different prefixes, multiple forward excursions, source-dependent comparisons, two-arm mergers, non-numeric ranks, or finite exceptional handling. The proper-ancestor normalization theorem in the companion note separately explains why even a more efficient ancestor compiler cannot alone enlarge the old suffix-closed K proof language.

The finite-state potential is useful as a certified conversion primitive and a model of explicit credit synthesis. Applying a potential with analogous credit across the actual critical-return process remains an open obligation. Resetting V or a source floor between arbitrary returns would not establish that obligation.
