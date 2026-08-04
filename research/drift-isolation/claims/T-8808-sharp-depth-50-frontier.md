# T-8808 — Sharp depth-50 frontier for the `4 -> 5` chart

Claim ID: T-8808  
Title: The least positive base-`5/4` root surviving fifty low digits is `4538335001132531`  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: L-8804, T-8806, X-8803  
Scope: the exact finite depth `50` frontier  
Related counterexample candidates: issue #26; no `K-####` candidate

## Statement

Let

```text
tau(x)=ceil(5x/4),
b(x)=(-x) mod 4 in {0,1,2,3}.
```

Define the survival depth of a positive integer `X` as the least `j>=0` for
which

```text
b(tau^j(X)) in {2,3},
```

or infinity if there is no such `j`.

The exact least positive integer with survival depth at least `50` is

```text
X_50 = 4538335001132531.                              (1)
```

It survives exactly `50` steps, with bottom-digit prefix

```text
10011110111001011100001001101001011101010100000010.   (2)
```

After those steps the state is

```text
1085242780136381205,
```

whose bottom digit is `3`, so the path exits immediately.

Consequently:

1. every positive `X<X_50` emits digit `2` or `3` before depth `50`;
2. the bound is sharp because `X_50` survives all first `50` digits;
3. under the physical translation `X=A+1` from T-8806, every positive chart seed

   ```text
   A <= 4538335001132529
   ```

   exits the exact `4 -> 5` chart before `50` macro-steps, while

   ```text
   A_50=4538335001132530
   ```

   survives exactly `50` macro-steps.

No statement is made about what the full `5x+1` orbit does after leaving this
partial chart.

## Exact certificate

L-8804 is applied with the split

```text
h=m=25.
```

Both exact frontiers contain

```text
2^25=33554432
```

states. The minimizing mixed-radix decomposition is

```text
X_50 = r + 4^25*t,
t=4,
r=34735373762035.                                    (3)
```

Since

```text
4^25=1125899906842624,
```

equation (3) evaluates exactly to (1).

## Motivation

X-8802 found a depth-`19` root below one million by scanning ordinary seeds.
The composition theorem permits a qualitatively larger exact statement: it
certifies the minimum over the entire interval below `4^50`, without scanning
that interval and without assuming random residue behavior.

The theorem supplies a serious finite lower bound for any hypothetical ordinary
survivor and a frozen benchmark for future PDR, Diophantine, and rational-base
arguments.

## Proof

L-8804 gives a bijection between the full depth-`50` survivor set and pairs from
the two depth-`25` frontiers. It also proves that the cyclic-successor algorithm
returns the true least positive residue, rather than a sampled candidate.

X-8803 generates both exact frontiers, applies the modular inverse

```text
5^(-25) mod 4^25,
```

sorts the transformed right frontier, and evaluates the exact minimum formula.
The resulting pair is (3). The program then independently replays the original
integer map from `X_50`; it verifies all `50` allowed residues and records the
first forbidden state and digit shown above.

Because L-8804 proves completeness of the pair enumeration, no smaller positive
root can survive depth `50`. **QED**, conditional only on independent replay of
the deterministic exact program X-8803.

## Dependency audit

- L-8804 proves completeness and exact minimization of the split frontier.
- T-8806 translates roots `X` to physical chart seeds `A=X-1`.
- X-8803 is the reproducible exact arithmetic certificate.

## Gap audit

- This is a finite theorem. It does not prove global termination of the bottom
  map or nonexistence of an infinite chart survivor.
- “Exits” means leaves the two-branch partial chart, not that the full `5x+1`
  orbit reaches a cycle or terminates.
- The strict physical range ends at `A=X_50-2`; `A=X_50-1` is the sharp witness.
- The displayed prefix has length exactly `50`; the next digit is forbidden.
- The proof does not extrapolate from the growth of finite minima.

## Adversarial tests

- Direct and meet-in-the-middle minima agree at every depth `1..20`.
- The depth-`25` least positive root is independently reported as `175205631`.
- The final witness is replayed through depth `51`, forcing the exact exit at
  depth `50` rather than merely checking its residue-class membership.
- X-8803 checks that the transformed right frontier has no duplicates and that
  the modular inverse is correct.

## Remaining uncertainty

The least roots at finite depths are nondecreasing. Proving that they are
unbounded would settle the chart negatively; proving eventual stabilization
would produce an infinite ordinary survivor. Neither asymptotic conclusion is
claimed here.

## Suggested next attack

Use the exact minima and minimizing pair decompositions as training data for a
proof-producing recursive lower bound, not as evidence for a guessed growth
law.
