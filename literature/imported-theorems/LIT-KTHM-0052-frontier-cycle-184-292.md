# LIT-KTHM-0052 — The complete alternating `(k,A)=(184,292)` first-frontier family is empty

**Type:** exact native arithmetic theorem with a complete finite decoder and replay artifact.  
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

is necessary before the accelerated length can accommodate the first unexcluded case of `92` local minima.

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

The positive cycle denominator is

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

Every displayed factor is prime, their product is `(5)`, and the largest has only `48` bits.

## 4. The complete 92-local-minimum subfamily

At length `184`, a word with `92` local minima must alternate ascent and descent. After cyclic rotation it has the form

```text
w=(1,b_0,1,b_1,...,1,b_91),
b_i>=2,
sum_i b_i=200.                                          (7)
```

Its length is `184`, total valuation is `92+200=292`, and `(1)` proves that it has exactly `92` local minima.

Put

```text
c_i=b_i-2>=0,
sum_i c_i=16.                                           (8)
```

The family contains

```text
binom(107,16)=4335886749297756310                       (9)
```

ordered block words before cyclic and primitive normalization.

## 5. Two-step block recurrence

The pair of accelerated valuations `(1,2+c_i)` acts by

```text
boxed:
2^[3+c_i] x_(i+1)=9x_i+5.                               (10)
```

Let

```text
E_0=0,
E_j=sum_(i<j)(3+c_i)=3j+sum_(i<j)c_i.                   (11)
```

Composing all `92` blocks gives

```text
2^292 x_92=9^92 x_0+C(c),                               (12)
```

where

```text
C(c)=5S(c),
S(c)=sum_(j=0)^91 9^(91-j)2^(E_j).                      (13)
```

A cycle in this family requires

```text
D divides C(c).                                         (14)
```

It is enough to prove that `(14)` never occurs; no admissibility converse is needed for the exclusion.

## 6. Sixteen-jump telescoping reduction

Put

```text
u_j=sum_(i<j)c_i,
Q_j=9^(92-j)8^j,
0<=j<=92.                                               (15)
```

Since

```text
Q_j-Q_(j+1)=9^(91-j)8^j,                                (16)
```

summation by parts gives

```text
S(c)=J(c)-D,                                             (17)
```

where, after setting `u_92=16`,

```text
J(c)=sum_(j=1)^92 (2^[u_j]-2^[u_(j-1)])Q_j.             (18)
```

Resolve every jump into unit increments. There are unique nondecreasing positions

```text
1<=j_0<=j_1<=...<=j_15<=92                              (19)
```

such that

```text
boxed:
J(c)=sum_(r=0)^15 2^r Q_(j_r).                          (20)
```

Conversely every sequence `(19)` gives one weak composition `(8)`.

Because `D=5D'`, `(14)` and `(17)` are equivalent to

```text
boxed:
D' divides J(c),
D'=(2^292-3^184)/5.                                     (21)
```

Thus there is a positive integer `m` with

```text
sum_(r=0)^15 2^rQ_(j_r)=mD'.                            (22)
```

## 7. Exact finite multiplier interval

The sequence `Q_j` is strictly decreasing. Hence

```text
(2^16-1)Q_92 <= J(c) <= (2^16-1)Q_1.                   (23)
```

Dividing by `D'` gives the exact integer range

```text
boxed:
23<=m<=1005828.                                         (24)
```

No multiplier outside `(24)` can satisfy `(22)`.

## 8. Every multiplier has at most one jump sequence

### Decoder lemma

Fix `m` in `(24)` and put

```text
R_0=mD'.                                                 (25)
```

Suppose the first `r` jump terms have been removed, so

```text
R_r=sum_(s=r)^15 2^sQ_(j_s).                            (26)
```

The `s`th term has exact binary valuation

```text
v_2(2^sQ_(j_s))=s+3j_s.                                 (27)
```

Since the positions are nondecreasing, every term with `s>r` has valuation strictly larger than `r+3j_r`. Therefore the first remaining term is the unique term of least valuation and

```text
boxed:
j_r=(v_2(R_r)-r)/3.                                    (28)
```

The candidate position is valid only if the right side is an integer in `[1,92]`, is at least the previous position, and the term does not exceed `R_r`. Subtract it and repeat.

Thus `(28)` reconstructs the only possible sequence `(j_0,...,j_15)` from `m`. If the final remainder is nonzero, that multiplier is impossible. QED.

## 9. Complete exact scan

The proof artifact

```text
literature/experiments/LIT-X-0052-frontier-cycle/run.py
```

performs the finite scan `(24)` using only Python's standard library. It also verifies the complete factorization `(6)` with deterministic Miller--Rabin tests valid below `2^64`.

Replay:

```bash
python3 literature/experiments/LIT-X-0052-frontier-cycle/run.py \
  --check-results \
  literature/experiments/LIT-X-0052-frontier-cycle/results/canonical.json
```

The exact result is:

```text
multipliers in the interval:             1,005,806
surviving the initial v_2 filter:            71,843
valuation-mod-3 failures:                   71,788
term overshoots:                                51
full 16-position decodes with remainder:         4
solutions:                                        0
```

The transcript digest over all `71,843` decoded multipliers is

```text
c8449fe7c2d15679df8bb4d68ecd376c68b2995ef033e87fd2063447f5cde58d.   (29)
```

The four terminal decodes and their exact nonzero remainders are preserved in the canonical JSON.

## 10. Theorem

```text
boxed:
There is no positive accelerated Collatz cycle with
(k,A)=(184,292) whose valuation word has 92 local minima.             (30)
```

### Proof

Every such word has the alternating form `(7)`. If it were a cycle, `(14)` would hold and therefore `(22)` would have a solution with `m` in `(24)`. The decoder lemma proves that the finite scan checks the unique possible jump sequence for every such `m`. The scan finds none. QED.

## 11. What the failed family teaches

This was an unusually favorable packet:

```text
minimal accelerated length compatible with 92 local minima;
first local-minimum count beyond the published exclusion;
near-critical total valuation;
fully factored denominator with no factor above 48 bits;
constant two-step multiplier 9 and toll 5;
only sixteen excess valuation units.
```

Even this family is empty. The active cycle search should retain the sixteen-jump decoder as a general tool, but move to another total valuation, a longer accelerated word, or a nonminimal local-minimum count.

## 12. Status boundary

The theorem excludes one complete first-frontier family. It does not exclude other values of `A` at length `184`, longer cycles, divergent orbits, or the Collatz conjecture.