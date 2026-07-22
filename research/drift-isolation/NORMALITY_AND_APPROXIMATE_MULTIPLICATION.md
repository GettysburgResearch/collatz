# The exact global frontier: approximate multiplication and base-`5/4` normality

Agent: `gpt56-drift-01`  
Issue: #26  
Status: **OPEN FRONTIER, EXACTLY IDENTIFIED**

## One problem, four equivalent faces

For a positive integer `A`, set

```text
X=A+1,
tau(X)=ceil(5X/4),
b(X)=(-X) mod 4 in {0,1,2,3}.
```

The following are equivalent by T-8802 and T-8806:

1. `A` remains forever in the exact two-branch `5x+1` chart;
2. every state `tau^j(X)` is `0` or `3 modulo 4`;
3. the base-`5/4` bottom word from seed `X` uses only digits `0,1`;
4. the Dubickas–Mossinghoff approximate-multiplication map with
   `p=5,q=4,S={0,3}` never stops at `X`.

Any such orbit is strictly increasing. A positive solution is therefore already
a concrete divergent `5x+1` orbit, not merely a symbolic or `2`-adic object.

## What a complete negative result must prove

Let `m_n` be the least positive root surviving `n` bottom digits. The sets of
ordinary survivors are nested, so `m_n` is nondecreasing. Moreover:

```text
there is an infinite positive survivor
iff
(m_n) is bounded
iff
(m_n) eventually stabilizes.
```

Therefore global termination is equivalent to

```text
m_n -> infinity.                                      (1)
```

L-8804 gives an exact meet-in-the-middle formula for `m_(h+m)`. T-8808 computes

```text
m_50=4538335001132531.
```

The missing theorem is an asymptotic lower bound proving (1), not another finite
census.

## What the ordinary completion forces

A hypothetical physical seed gives an ordinary integer

```text
M=A+2=(1/5)*sum eps_j*(4/5)^j in Q_2.
```

Current unconditional constraints include:

- T-8803: factor-complexity slope at least
  `1/(log_4(5)-1)=6.212567...`;
- T-8807: the full completion Cantor set has Haar measure zero and dimension
  `1/2`; ordinary survivors have density zero;
- T-8809: both symbols occur in every multiplicative interval
  `(X,log_4(5)X+O_A(1)]`, giving at least `6.700134... log Y` occurrences of
  each symbol below position `Y`;
- T-8808: no positive root below `4538335001132531` survives fifty digits.

These conditions are mutually compatible. None silently implies emptiness.

## Why normality would finish it

The bottom word is a nonempty-seed minimal word in rational base `5/4`.
The current rational-base normality conjecture predicts that every such word is
normal over `{0,1,2,3}`. Normality would force digits `2` and `3` infinitely
often, so the partial chart would always be left.

Only a tiny fragment is needed here:

```text
Every nonempty-seed base-5/4 minimal word contains a 2 or a 3.              (2)
```

A proof of (2) completes the negative result. A counterexample to (2) completes
the positive result by producing a divergent physical seed.

## Productive theorem targets below normality

### A. Recursive minimum growth

Use the exact composition

```text
S_(h+m)
  <->
{(r,s) in S_h x S_m}
```

and prove that every cyclic successor distance in the transformed right
frontier is large enough to make `m_(h+m)>m_h` on an unbounded sequence of
splits.

### B. Forbidden-pair richness

Prove only that the union of digits `{2,3}` appears in every sufficiently long
prefix of every nonempty-seed minimal word. No frequencies or full normality are
needed.

### C. Two-color support versus physical grammar

T-8809 forces both `0` and `1` supports to be multiplicatively syndetic. Derive
an independent upper bound from the integer bottom-map grammar that violates
one of those local counts.

### D. Diophantine stopping bound

Every surviving root defines integers

```text
X_n=ceil(lambda*(5/4)^n)
```

for a fixed real `lambda`, with all `X_n mod4 in {0,3}`. A quantitative theorem
showing that such simultaneous rational approximations cannot persist would
settle (2).

### E. Proof-producing PDR

A finite residue invariant alone is unlikely to see an ordinary-section
obstruction, but a residue-plus-height abstraction might. Any PDR certificate
must be exported as a finite inductive invariant and checked independently.

## Non-result boundary

- Long finite survival is not infinite survival.
- Haar measure zero is not emptiness.
- Positive fair-parity drift is not a divergence proof.
- The normality conjecture is not imported as a theorem.
- The known complexity lower bound does not imply occurrence of all four digits.

The global result is now isolated at its true mathematical boundary. Wave 3
adds exact tools and sharp necessary conditions without relabeling that boundary
as solved.
