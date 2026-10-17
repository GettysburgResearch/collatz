# T-9401 — Repetition rigidity for an ordinary survivor code

Claim ID: T-9401
Title: Early repeated-factor obstruction for ordinary `64 -> 81` survivors
Status: PROPOSED
Authoring agent: `gpt56-complexity-01`
Reviewing agents: none
Created: 2026-07-21
Last updated: 2026-07-21
Dependencies: D-9401, L-9401, L-9402
Scope: every positive ordinary integer represented by `Phi`
Related counterexample candidates: issue #4 M1; no `K-####` candidate

## Statement

Let `eps in {0,1}^N`, and suppose

```text
A = Phi(eps)
```

is an ordinary positive integer.  Let `r,t,ell` be integers with

```text
0 <= r < t,
ell >= 1,
eps[r:r+ell] = eps[t:t+ell].
```

Put

```text
delta = log_64(81) - 1 > 0.
```

Then either `A = 1` and `eps = 111...`, or

```text
64^(t+ell) < A * 81^t,
```

and therefore

```text
ell < delta*t + log_64(A).
```

Equivalently, a nontrivial ordinary survivor code cannot contain a
length-`ell` factor whose second occurrence starts too early relative to
`ell`.

## Construction of the periodic approximant

Set

```text
s = t-r.
```

Define `eta` by retaining the first `r` digits of `eps` and then repeating
the block `eps[r:t]` forever:

```text
eta = eps[0:r] (eps[r:t])^infinity.
```

Let

```text
Y = Phi(eta).
```

## Proof

### Step 1: the repeated factors give a long common prefix

The factor equality says

```text
eps_(r+j) = eps_(r+s+j)  for 0 <= j < ell.
```

Thus the finite interval

```text
eps[r : r+s+ell]
```

is `s`-periodic.  Repeatedly subtracting `s` from an index shows that the
periodic continuation `eta` agrees with `eps` at every position below

```text
r+s+ell = t+ell.
```

This remains valid when `ell > s`, so overlapping repetitions are included.

### Step 2: `2`-adic closeness

By L-9402,

```text
A - Y belongs to 64^(t+ell) * Z_2.
```

By L-9401, write `Y = p/q` in lowest terms with

```text
q odd,
0 <= Y <= 1,
q < 81^t,
```

because the preperiod has length `r` and the period has length `s=t-r`.
Therefore

```text
z = qA - p = q(A-Y)
```

is an ordinary integer divisible by `64^(t+ell)`.

### Step 3: the archimedean height squeeze

If `z != 0`, then

```text
64^(t+ell) <= |z|.
```

Since `A >= 1` and `0 <= Y <= 1`, we have `0 <= A-Y <= A`, so

```text
|z| = q|A-Y| <= qA < A*81^t.
```

Combining the inequalities gives

```text
64^(t+ell) < A*81^t.
```

Taking logarithms base `64` yields the claimed repetition bound.

### Step 4: classify the zero-numerator case

If `z = 0`, then `A = Y`.  But `Y` lies in the real interval `[0,1]`, and
`A` is a positive integer, so `A=Y=1`.  The all-one code has

```text
Phi(111...) = (17/81)/(1-64/81) = 1.
```

Injectivity from L-9402 therefore forces `eps = 111...`.

This is the trivial survivor.  **QED**

## Dependency audit

- D-9401 supplies the coding and indexing.
- L-9401 supplies rationality, odd denominator, real range, and the strict
  height `q < 81^t`.
- L-9402 supplies `64^(t+ell)` divisibility and injectivity.

No empirical or branch-external theorem is used.

## Gap audit

- The second start position is `t`, and the common-prefix length is exactly
  `t+ell`, not `r+ell`.
- The proof explicitly includes overlapping factors (`ell > t-r`).
- The strict final inequality comes from the strict denominator bound.
- The arbitrary nonperiodic code is never evaluated as the same real number
  as its `2`-adic value.  Only the eventually periodic approximant `eta` is
  identified with one rational in both completions.
- The theorem is conditional on `Phi(eps)` being an ordinary integer; a
  generic `2`-adic survivor is not constrained this way.
- `A=1` must be separated because the product-formula numerator may vanish.

## Adversarial tests

`X-9401` exhaustively checks the combinatorial common-prefix step for all
binary words through a frozen finite length, including overlapping copies,
and independently checks every algebraic ingredient of the approximant.
Finite tests are not the proof.

## Remaining uncertainty

The proof is complete-looking but has not been independently reconstructed.
No claim is made that a nontrivial ordinary survivor exists.

## Suggested next attack

1. Use chart congruences to reduce the denominator height.
2. Classify equality-near-extremizers where a recurrence nearly saturates
   the bound.
3. Translate stack or skeleton regeneration into forced repeated factors,
   making this theorem an obstruction to low-information S-adic grammars.
