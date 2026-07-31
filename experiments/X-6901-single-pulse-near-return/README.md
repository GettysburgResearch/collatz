# X-6901 — exact single-pulse near-return certificate

**Associated claim:** `T-6907`  
**Status:** exact finite arithmetic and exact post-Matveev reduction; primary Matveev theorem remains external  
**Agent:** `gpt56-positive-tangent-01`

## Question

Can a one-pulse lift of any repetition or rotation of either known negative accelerated Collatz cycle map one positive odd integer to itself plus a nonnegative displacement?

The covered family is

```text
primitive baseline:
  (1,2) or (1,1,1,2,1,1,4);

repetition:
  arbitrary r>=1;

rotation:
  arbitrary primitive rotation;

pulse:
  one arbitrary positive increase delta;

endpoint:
  n -> n+d for arbitrary d>=0.
```

## Exact reduction

For negative fixed state `z`, put

```text
g=-(3z+1),
D=U^r*2^delta-Q^r.
```

Every positive near-return gives

```text
D | g*(2^delta-1)-3*d
```

and positivity forces

```text
0 < D <= g*(2^delta-1).
```

The checker reconstructs:

1. exact logarithm intervals for `log 2` and `log 3`;
2. the Matveev cutoff inequalities with enlarged constants `gmax=20,272`;
3. the Legendre thresholds;
4. every continued-fraction row through the first denominator beyond the cutoff;
5. uniform rejection of every upper-convergent family;
6. the complete small repetition ranges;
7. physical replay of every small exact hit.

## Result

The unique hit is

```text
(1,2) -> (2,2),
n=1,
d=0.
```

There are no nontrivial cycles and no positive near-returns with `d>0` in the declared infinite class.

## Replay

```bash
python3 -B experiments/X-6901-single-pulse-near-return/verify.py
```

The script uses only Python integers, `fractions.Fraction`, and the standard library.

## Proof boundary

- The script does not prove Matveev's theorem.
- The exact theorem normalization must be reconstructed from the primary source before `T-6907` is promoted.
- Agreement of one implementation with its assertions is not independent review.
- Multi-pulse and arbitrary first-crossing words remain outside the scope.
