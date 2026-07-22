# LIT-KTHM-0052 — A fully factored first-frontier cycle family at `(k,A)=(184,292)`

**Type:** exact native arithmetic reduction and search-family certificate; no cycle is claimed.  
**Maps to:** issue #9, issue #41, `SYN/L-9904`, and the first parameter range not excluded by the published local-minimum bound.

## 1. Why `k=184` is the first possible accelerated length

For a positive odd state `x>1`, one accelerated step with valuation `a=v_2(3x+1)` satisfies

```text
a=1   -> (3x+1)/2 > x,
a>=2  -> (3x+1)/2^a < x.                                (1)
```

Along a cyclic sequence, local minima and local maxima alternate. Hence an accelerated word of length `k` has at most `floor(k/2)` local minima.

Hercher's theorem excludes every nontrivial positive cycle with at most `91` local minima. Therefore

```text
k>=184                                                   (2)
```

is necessary before the accelerated length can even accommodate the first unexcluded case of `92` local minima.

## 2. Frozen critical parameter

Set

```text
k=184,
A=292.                                                   (3)
```

Then

```text
A/k=73/46=1.586956521739...,
A-k*log_2(3)=0.3668998673...,
2^A/3^k=1.2895787421... .                                (4)
```

Thus the denominator is positive and close to the critical line:

```text
D=2^292-3^184
 =1786806590841408495003648024979272939822889499163552544403296804949023827414857928941215.
                                                                    (5)
```

## 3. Complete prime factorization

One has the exact squarefree factorization

```text
D =
5 * 11 * 13 * 17 * 83 * 89 * 179 * 1097 * 1301
  * 2963 * 4547 * 5113 * 13457 * 28697 * 1626211
  * 192491569 * 177790780231 * 314328249709
  * 167385996821689.                                    (6)
```

Every displayed factor is prime, their product is `(5)`, and the largest has only `48` bits. Therefore this is a fully smooth proof-carrying denominator, unusually well suited to prime-by-prime dynamic programming and CRT joins.

## 4. Exact 92-local-minimum subfamily

Take an alternating valuation word

```text
w=(1,b_0,1,b_1,...,1,b_91),
b_i>=2,
sum_i b_i=200.                                          (7)
```

Its length is `184` and its total valuation is

```text
92+200=292.                                              (8)
```

By `(1)`, every state preceding a valuation-one step is lower than both cyclic neighbours, so the word has exactly `92` local minima. It lies exactly at the first local-minimum count not excluded by Hercher.

Put

```text
c_i=b_i-2>=0,
sum_i c_i=16.                                           (9)
```

The family contains

```text
binom(107,16)=4335886749297756310                       (10)
```

ordered block words before cyclic and primitive normalization.

## 5. Two-step block recurrence

The pair of accelerated valuations `(1,2+c_i)` acts by

```text
boxed:
2^[3+c_i] x_(i+1)=9x_i+5.                               (11)
```

Let

```text
E_0=0,
E_j=sum_(i<j)(3+c_i)=3j+sum_(i<j)c_i.                   (12)
```

Composing all `92` blocks gives

```text
2^292 x_92=9^92 x_0+C(c),                               (13)
```

where

```text
boxed:
C(c)=5*sum_(j=0)^91 9^(91-j)2^(E_j).                   (14)
```

Since `9^92=3^184`, a positive cycle in this family exists exactly when

```text
boxed:
D divides C(c),
then x_0=C(c)/D is a positive odd integer and every
valuation in `(7)` replays exactly.                     (15)
```

The final replay implication should use the repository's primitive-cycle lemma; a periodic `c`-word is first reduced to its primitive root.

## 6. Search architecture

The exact factorization `(6)` makes the following proof-producing search natural:

1. choose a prime-power factor packet `M | D`;
2. dynamic-program the states
   ```text
   (block index, extra mass used, C mod M);
   ```
3. discard a packet as soon as residue zero is absent;
4. retain predecessor certificates for zero states;
5. join surviving packets by CRT;
6. quotient by cyclic rotation and reject nonprimitive `c`-words;
7. reconstruct `x_0=C/D` and replay all 184 valuations.

A smaller first grammar is `c_i in {0,1}` with exactly sixteen ones, i.e. descending valuations in `{2,3}`. It has

```text
binom(92,16)=315297189498738447                           (16)
```

ordered words and retains exactly `92` local minima.

## 7. Why this is a stronger target than a generic smooth scan

This packet simultaneously has:

```text
- the minimal accelerated length compatible with 92 local minima;
- the first local-minimum count beyond the published exclusion;
- a near-critical total valuation;
- a complete factorization into at most 48-bit primes;
- a 92-block affine recurrence with constant multiplier 9 and constant toll 5;
- only sixteen units of excess valuation beyond the alternating baseline.
```

It is therefore an unusually structured candidate family for issues #9 and #41.

## 8. Status boundary

No word satisfying `(15)` has been found here. Smoothness and criticality are search advantages, not evidence that a positive cycle exists. The packet is a rigorously frozen frontier family, not a `K-####` candidate.