# T-8403 — Six-state ordinary quotient criterion for a divergent Collatz orbit

Claim ID: `T-8403`  
Title: One forever-defined finite state of the six-branch quotient map is an unconditional divergent Collatz seed  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Dependencies: `L-8405`, `T-8402`, `L-8406`  
Scope: the `(L,b)=(6,1)` negative-three-cycle fixed-weight chart  
Related counterexample candidates: `Q-8402`; no `K-84xx` candidate

## Statement

Let

```text
(i_0,q_0),
i_0 in {0,...,5},
q_0 in Z_(>=0),
```

be one finite ordinary state of the deterministic partial quotient map in
`L-8406`.

Starting from `(i_r,q_r)`, compute

```text
r_r=[7153 q_r+e_(i_r)]_(524288).                      (1)
```

The next state exists exactly when `r_r` is one of the six domain digits. In
that case let `i_(r+1)` be the unique index with

```text
r_r=d_(i_(r+1)),                                       (2)
```

and put

```text
boxed:
q_(r+1)
 =q_r+(7153 q_r+e_(i_r)-d_(i_(r+1)))/524288.          (3)
```

Assume this recursion is defined for every `r>=0`. Define

```text
boxed:
h_0=524288 q_0+d_(i_0),
n_0=-5+2h_0.                                             (4)
```

If `h_0>3`, then `n_0` is a positive ordinary shortcut-Collatz counterexample.
Its exact orbit is unbounded.

## Proof

By `L-8406`, each transition `(1)`--`(3)` is equivalent to

```text
h_r=524288 q_r+d_(i_r),
h_(r+1)=531441 q_r+e_(i_r)
       =524288 q_(r+1)+d_(i_(r+1)).                    (5)
```

The branch word indexed by `i_r` is one of the six exact physical words of
`L-8405`, each containing six two-odd-step blocks over the negative three-cycle
coordinate. Hence `(5)` replays twelve accelerated odd Collatz steps exactly,
with no completion or interpolation.

Every legal quotient transition grows strictly by `L-8406/(14)`:

```text
q_(r+1)>q_r.                                           (6)
```

Independently, the physical macro chart is supercritical:

```text
531441>524288,
```

and every correction is nonnegative. Therefore

```text
h_(r+1)
 =(531441 h_r+C_(i_r))/524288
 >(h_r).                                                (7)
```

Thus all `h_r` and

```text
n_r=-5+2h_r
```

remain positive after a positive initialization and form a strictly increasing,
unbounded sequence of actual Collatz boundary states. The concatenated exact
blocks give an infinite positive shortcut-Collatz trajectory. It cannot enter
the trivial cycle, so `n_0` disproves the Collatz conjecture. **QED**

## Certificate size

A positive proof object would be unusually small:

```text
- one branch index i_0 in six states;
- one finite integer q_0;
- one finite inductive invariant proving (1)--(3) is defined forever.
```

No separate multiplier, positivity, or unboundedness proof would remain after
the invariant, because `(6)`--`(7)` are uniform.

## Why a residue lasso is insufficient

Modulo any fixed power of two, `(1)`--`(3)` has recurrent residue states. Such a
lasso only describes a compatible `2`-adic quotient unless it also proves that
the actual finite most-significant boundary is transported canonically.

The invariant must therefore state how newly exposed high quotient digits are
created by the odd factor `531441`, not merely that low residues recur.

## Finite evidence

`X-8404` exhausts the exact ordered-pair map and the least quotient cylinders
through seven transitions. The least compatible quotient grows from

```text
10,922
```

to

```text
1,039,272,265,886,964,930,051,342,828,874,282
```

(`110` bits). This is bounded evidence only and neither proves nor refutes the
forever-defined hypothesis.

## Gap audit

- No explicit `(i_0,q_0)` with all-time definedness is supplied.
- A long finite path is not an induction.
- A fixed-modulus SCC is not an ordinary top-boundary proof.
- The theorem is an exact implication, not a claimed counterexample.

## Next target

Construct a finite nucleus augmented by one genuine top/length counter whose
inductive transition implies that `(1)` always lands on one of the six domain
digits. Because quotient growth is automatic, this single top-boundary lemma
would produce the complete unconditional counterexample requested by issue #41.
