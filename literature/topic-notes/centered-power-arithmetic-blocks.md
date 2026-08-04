# Centered rational powers: the arithmetic-block target after real full-shift closure

## Exact native equivalence

PR #16 proves

```text
nontrivial ordinary 64->81 survivor
 <=
 exists xi>0 with ||xi(81/64)^n||<=1/81 for every n.
```

It also proves that every binary itinerary has one bounded real error path. Therefore interval propagation on the real errors alone cannot eliminate itineraries: the real scheduled language is a full two-shift.

The arithmetic content is in the nearest-integer cylinders. Appending one itinerary digit appends one base-64 block

```text
R_(K+1)=R_K+q_K 64^K,
```

and an ordinary integer exists exactly when `q_K=0` eventually.

## External sources to specialize

Dubickas's nearest-integer theorem supplies explicit large/small limit-point constants for

```text
||xi(p/q)^n||.
```

His two-interval theorem studies containment in unions of two intervals. Both are structurally relevant, but neither may be quoted before the constants and interval conventions are specialized to

```text
p=81,
q=64,
radius=1/81.
```

## Correct specialization task

1. Extract the exact large-limit constant from the full 2006 theorem.
2. Evaluate it rigorously at `(81,64)`.
3. Compare it with `1/81` using exact rational/algebraic inequalities.
4. Extract the extremal Thue–Morse sign word from the proof.
5. Translate that sign word into the native nearest-integer digits and appended blocks `q_K`.
6. Determine whether the extremal source construction is compatible with eventual block zero.

A constant strictly greater than `1/81` closes the ordinary section immediately. Equality would isolate the exact critical symbolic language. A smaller constant still gives the quantitative deficit a native block theorem must repair.

## Native fallback

Build the finite sign/carry graph from

```text
81u_n-64u_(n+1)=epsilon_n-epsilon_(n+1),
```

but attach the arithmetic state

```text
C_K mod 64
```

or the appended block `q_K`. A graph containing only real intervals is guaranteed to retain the full shift and cannot prove emptiness.

The most useful output is a finite or one-counter arithmetic graph whose long zero-block paths can be compared directly with the source's Thue–Morse extremals or with PR #20's repetition/height theorems.
