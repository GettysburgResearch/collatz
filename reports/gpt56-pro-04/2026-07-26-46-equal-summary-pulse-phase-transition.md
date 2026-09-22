# Breakthrough report — minimum-edge full-denominator sieve and the negative-three pulse phase transition

**Agent:** `gpt56-pro-04` (`GPT-5.6 Pro`)
**Date:** 2026-07-26
**Host branch:** `agent/gpt56-pro-04/46-integer-first-counterexample-offense`
**Issue:** #46
**Status:** published on draft PR #47; no counterexample or `K-####` object

## 1. Objective discipline

This pass did not extend a finite prefix, add a prescribed schedule, or prove another theorem conditional on an ordinary infinite path.

The first target was the fixed six-branch least-root decision. The newest PR #64 already proves that direct quotient descent, every finite affine/rational nucleus, and every semilinear sanctuary fail. I found no valid bounded-root or root-escape theorem beyond that frontier.

I therefore switched to the other accepted global blocker: eliminate an exhaustive positive-cycle family by a full-denominator theorem, with no bounded repetition scan.

## 2. New general theorem `L-9608`

For a finite alphabet

```text
Q*x' = P*x + C_i,
0<P<Q,
```

put `W=max C_i-min C_i`. If `W<Q`, then every integral block-boundary cycle has zero carry at every edge:

```text
x_t=n for every t,
C_(i_t)=(Q-P)n for every t.
```

The proof iterates around the cycle, writes `(Q-P)n` as a positive weighted average of the selected constants, and then observes that

```text
Q*(x_1-n)=C_(i_0)-(Q-P)n
```

is a multiple of `Q` with absolute value below `Q`. It must vanish. Induction removes the complete repetition axis.

This extends the existing two-constant geometric-factor sieve to arbitrary finite alphabets and needs no factorization or coprimality.

## 3. New general theorem `L-9609`

For the same common-summary alphabet, let `D=Q-P` and choose a minimum `m` on a positive integer cycle. The outgoing edge must satisfy

```text
E_i=D*m+Q*k,
k>=0.
```

Thus every arbitrary-length grammar reduces to one finite first-edge target set.

If every `E_i` is divisible by `g`, `g|P`, and `gcd(g,Q)=1`, then

```text
m+k=0 mod g,
E_i>=gD.
```

Therefore

```text
E_max<gD
```

is an exact all-repetition cycle exclusion. When that height gate narrowly fails, only finitely many targets remain, and one congruence can eliminate the complete alphabet.

## 4. Exact physical application `T-9608`

In the negative-three coordinate

```text
n=-5+2h,
y=h-3,
```

the exact letters are

```text
A: 8*y'  = 9*y+3,
B: 16*y' = 9*y.
```

A macro with `a` letters `A` and `b` letters `B` has

```text
Q=8^a 16^b,
P=9^(a+b),
Q*y'=P*y+E_w.
```

The exact centered constant interval is

```text
E_min=3*9^b *(9^a-8^a),
E_max=3*16^b*(9^a-8^a).
```

Every `E_w` is divisible by three. The generic minimum-edge gate becomes

```text
9^a(16^b+9^b) < 2*8^a*16^b.
```

It excludes:

```text
a<=2, any b>=1;
a=3, b>=2;
a=4, b>=3;
a=5, b>=4.
```

The remaining contracting packets are closed exactly:

- `(3,1)` and `(4,1)` by the narrow-alphabet theorem and complete primitive denominators;
- `(4,2)` by its sole target `3D`, separated from every block constant modulo `7`;
- `(5,2)` by two targets congruent to `6 mod9`, while every block constant is `0` or `3 mod9`;
- `(5,3)` by two targets congruent to `5` or `6 mod8`, while every block constant is `0` or `3 mod8`.

The remaining packet `(5,1)` is supercritical:

```text
P=531441,
Q=524288,
P-Q=7153.
```

Positive cycles are impossible by sign, while one all-time ordinary path would be divergent.

Hence:

```text
for every b>=1 and every 0<=a<=5,
for arbitrary macro choice and arbitrary repetition length,
there is no nontrivial positive cycle.
```

The only fixed point is the all-`B` state `h=3`, physical `n=1`.

## 5. Why this is a genuine infinite-class result

The result is unbounded in all of the following simultaneously:

```text
pulse count b;
macro length a+b;
branch count binomial(a+b,b);
repetition length;
chronological switching among macro branches;
centered support aR after R macros.
```

It is therefore not another fixed-support or finite-period census.

It is genuinely weaker than Collatz: packets with at least six `A` letters, scale-varying summaries, nonaligned repairs, and unrestricted valuation words remain outside the theorem.

## 6. Exact phase transition

Within the one-pulse family:

```text
lengths 1--5:
    contracting;
    every arbitrary aligned cycle grammar is excluded;

length 6:
    first supercritical packet;
    cycles excluded by growth;
    ordinary extraction becomes the only positive issue.
```

Thus the six-branch least-root system is the exact first divergent packet beyond a complete all-repetition cycle-free regime, rather than an arbitrarily selected laboratory.

## 7. Verification

Independent standard-library checker:

```bash
python3 -B experiments/X-9612-equal-summary-pulse-phase/verify.py
```

Result:

```text
all independent L-9608/L-9609/T-9608 checks passed
```

Checker SHA-256:

```text
25b072c09b63179d39cb35f1165b90e7bd71062b557327874566bccbf65edb33
```

The checker independently reconstructs:

- chronological macro constants and centered tolls;
- all extrema and threshold inequalities;
- the complete exceptional target sets and residue separations;
- target disjointness for every subcritical packet with `a<=5`, `b<=12` as corroboration;
- direct multi-macro composition in selected packets;
- small generic instances of both abstract lemmas.

Finite replay is not used to extrapolate the theorem.

## 8. Remaining blocker

No six-branch ordinary root was extracted and no least-root divergence theorem was proved.

The exact next positive task remains

```text
six-branch m_N bounded
    -> explicit root and K-candidate replay;

or

m_N -> infinity
    -> complete six-branch architecture eliminated.
```

On the cycle side, the first aligned fixed-weight family not covered by this packet has `a>=6`.
