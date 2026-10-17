# Linear-height quotient-refund program

## Exact seed theorem

For the phase-34 local recurrence, the 256-transition linear grid

```text
t_j=B+16j
```

has

```text
A(B)=1792B+3657472,
E(B)=2816B+5792512.
```

At every multiple of 16 with `B>=477424`,

```text
3^[A(B)]>2^[E(B+4096)].
```

See `LIT-KTHM-0050`.

## Why it is constructive

The frozen doubling schedule kills the free quotient before the next full cylinder. The linear schedule instead carries at least one complete next-stage quotient. Every finite current/next word pair has infinitely many positive ordinary quotient transitions.

This is a genuine architectural escape from the proposed cap/co-cap Evertse proof, not a denial of that proof's frozen scope.

## First theorem packet

1. Freeze one stage-word subalphabet small enough for exact replay.
2. Derive the quotient transition
   ```text
   Y_next=(3^[A(B)]Y+C_(w,v))/2^[E(B+4096)].
   ```
3. Retain the unique residue condition for integrality.
4. Construct a state family `K_B` with a forward lift chosen from the current state.
5. Prove `Y_next>Y` and physical positivity.
6. Supply one explicit finite `Y_0`.

## Suggested invariant state

```text
(B,
word-prefix state,
Y mod 2^r,
Y/2^r lower bound,
endpoint outside-prime content,
physical tower type).
```

The residue depth `r` should grow only when the ordinary quotient growth pays for it. A fixed bounded projection is not expected to close.

## Dual outcomes

```text
positive:
  an exact integer-first invariant gives a divergent Collatz orbit;

negative:
  prove every linear-height path still decomposes into bounded essential
  Evertse leaves or selects a nonordinary rational-base branch.
```

Either outcome sharply extends the current finite-type boundary.