# Ordinary-integer gap audit

## What is proved

### Frozen direct dyadic-boundary class

For `D-9701`:

1. every finite type prefix has one exact initial residue cylinder;
2. the exact new residue block is computed by `L-9701`;
3. every infinite type directive has infinitely many nonzero blocks;
4. its unique `Z_2` completion is not any signed ordinary integer;
5. no positive high-tail initialization exists for the whole infinite class;
6. all statements quantify the full directive class, not sampled schedules.

### Corrected composed 256-transition class

Relative to the exact PR #3 `T-0027` interface, `T-9703` proves:

1. every finite complete stage has canonical data `0<=R_m<q_m` and
   `0<=S_m<N_m`;
2. `N_m/q_(m+1)<1/4` with an explicit exponentially decaying bound;
3. any ordinary nonnegative infinite stage trajectory eventually satisfies
   `z_m=R_m`, `Y_m=0`, and `S_m=R_(m+1)`;
4. the remaining ordinary tail is an exact cap-correction chain, not an
   arbitrary unbounded quotient zipper;
5. these conclusions quantify every infinite sequence of admissible stage
   words, not a sampled schedule family.

`T-9703` is a reduction, not yet a proof of nonexistence or a construction.

## Every ordinary-integer assumption exposed

### 1. Finite compatibility

A member of a finite cylinder proves only a finite exact replay. Neither theorem
uses finite compatibility as an infinite initialization.

### 2. Completion versus integer

Nested cylinders give one `Z_2` point. `T-9702` assumes that point is an
ordinary integer only for contradiction. `T-9703` begins with an explicit
ordinary nonnegative stage trajectory and derives a necessary tail form. Neither
identifies a completion with a finite word by compactness.

### 3. Least representatives

Eventual zero initial-cylinder blocks characterize nonnegative integer
completion. Negative integers have nonstabilizing least nonnegative residues.
`T-9702` excludes all signed integers in its frozen direct class.

For the composed stage, `Y_m=0` is a **physical stage quotient**, not directly
the cumulative initial residue block `a_k`. The bridge is: an ordinary initial
completion would generate an ordinary stage trajectory, and `T-9703` then forces
the cap-correction tail.

### 4. Positivity

The direct negative theorem does not assume future positivity; it excludes even
a signed infinite high-tail path.

The composed-stage theorem assumes nonnegative stage residuals because the
canonical cap bound is a nonnegative-tile statement. It does not infer
positivity from a 2-adic address.

### 5. Marked physical state

For the direct class, `X-9701` directly replays

```text
x=A_i(t)+2^(K_i(t))*h-34.
```

For the composed class, `T-9703` works at PR #3's exact residual-stage interface.
It does not independently reconstruct the 256 physical tower blocks and does
not supply one finite marked starting integer.

### 6. Logarithm digits

No digit of `-(7/4)log_2(3)` is initialized. PR #3 `T-0030` supplies the
ordinary forward bulk `V_m`, but `T-9703` does not assume `V_m` lies in the
physical residual cylinder.

### 7. Entropy and surplus

No branch count, entropy surplus, or bit-length estimate is treated as residue
membership. `T-9703` uses exact stage membership and compares the current odd
multiplier with the **next** complete binary radix.

### 8. Canonical cap positivity

The bound `0<=S_m<N_m` is not assumed from integrality. `L-9702` proves it by
composing local canonical tiles whose individual caps satisfy
`0<=psi_j<N_j`.

### 9. External theorem status

- `T-9702` uses elementary inequalities after freezing PR #3 tower formulas.
- `T-9703` uses the exact PR #3 `T-0027` interface and the self-contained
  `L-9702`; PR #3 remains `PROPOSED`.
- PR #32's independent verification of the ADEL carry chain is methodological
  support, not a proof dependency or silent promotion.
- PR #20's periodic-tail results and issue #29's unpublished comment are not
  imported as theorems.

## What remains open

### A. Infinite cap-correction chain

The primary full-stage question is now

```text
S_m(w_m)=R_(m+1)(w_(m+1))
```

for all sufficiently large `m`. A negative theorem must exclude every such
infinite directive. A positive theorem must construct one by a finite rule and
then meet every initialization, replay, positivity, and growth obligation.

### B. Tiny correction is not impossibility

`T-9703` gives

```text
0 <= R_(m+1) < 3^(A_m) << 2^(D_(m+1)).
```

An exponentially small target interval is a completion-height resource, not a
proof that the interval contains no admissible correction.

### C. Ordinary bulk generator

PR #3 `T-0030` supplies

```text
V_(m+1)=V_m+2^(m+1)V_m^2.
```

It remains auxiliary until an exact theorem expresses the cap-correction chain
as a finite affine or mixed-radix transform of `V_m`.

### D. Counter-prefix isometry

PR #3 `T-0028`/`T-0029` routes `O(m)` low prefix bits and `L-0029` peels them.
The complete stage correction has `Theta(2^m)` depth. Prefix routing alone does
not decide the cap-correction equality.

### E. Symbolic router

A Krieger/MacDonald router still needs a stationary legal graph, entropy and
periodic-point conditions, exact output decoding, and separate arithmetic
realization. `T-9703` reduces the arithmetic target but does not create that
stationary graph.

### F. Finite marked initialization

No eventually-zero cumulative initial directive is constructed. No finite
positive marked integer is proved to enter and follow a cap-correction chain.
Therefore no `K-####` identifier is created.
