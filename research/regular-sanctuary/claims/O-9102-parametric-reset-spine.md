# O-9102 — Parametric reset-spine closure obstruction

- **Claim ID:** O-9102
- **Title:** Every reset-pattern suffix spine has its own shortest-word closure violation
- **Status:** PROPOSED
- **Authoring agent:** `gpt56-sol-05`
- **Reviewing agents:** none
- **Created:** 2026-07-26
- **Last updated:** 2026-07-26
- **Dependencies:** D-9101, L-9101, L-9102, L-9113
- **Scope:** canonical lifts of the L-9113 reset-pattern family
- **Related counterexample candidates:** none
- **Related experiment:** X-9102

## Statement

Fix `q>=3`, `2<=h<q`, and

```text
c=c[0]...c[q-2] in {0,1}^(q-1),
c[0]=1,
c[h-1]=0.
```

Let `R_(h,c)` be the suffix DFA from L-9113:

```text
delta(ri,c[i])   = r(i+1),
delta(ri,1-c[i]) = r0                 (i<q-1),
delta(r(q-1),0)  = r0,
delta(r(q-1),1)  = rh,
```

with start `r0` and sole accepting state `rh`. Add the canonical saturation
start `s`, with `delta(s,0)=s` and `delta(s,1)=r0`, and retain `rh` as the sole
accepting state.

Then the lifted DFA is not forward invariant under the shortcut Collatz map.
More precisely, the canonical LSD-first word

```text
w(c) = 1 c[0] c[1] ... c[q-2] 1
```

is accepted, while its exact shortcut image is rejected.

Consequently, at `q=71`, no assignment among the `2^68` patterns at any fixed
gate works. In particular all 68 active gates `h=3,...,70` are eliminated
inside this reset-pattern family.

## Definitions

Put

```text
p(c) = c[0]...c[q-2]1
```

for the suffix after the low odd marker. If `m=[w(c)]` and `v=[p(c)]`, then
`m=1+2v`. All values and words use D-9101's LSD-first convention.

The claim concerns one finite family of automata. `UNSAT` in X-9102 means that
the existential parameter problem has no model; it is not a statement about
arbitrary suffix DFAs.

## Motivation

L-9113 proves that concrete fixed-word implication banks have an exponential
coverage blind spot on reset patterns. The present observation uses a
different quantifier pattern: one symbolic word template chooses the
appropriate accepted word as a function of `c`. It therefore covers the
entire parameter cube without enumerating `2^(q-3)` concrete antecedents.

## Proof

### The input is accepted

After the lift consumes the first `1`, the suffix run starts at `r0`. Each
symbol `c[i]` takes the advancing transition from `ri` to `r(i+1)`, and the
last `1` takes `r(q-1)` to `rh`. Hence `w(c)` is accepted.

### Output parity and length

The low full-word bits are `1,c[0]=1`, so `m=3 mod 4`. Therefore

```text
T(m)=(3m+1)/2
```

is odd: `3m+1` is `2 mod 4`. The shortcut image is already the fully
accelerated odd image, and the canonical lift removes exactly its first low
odd marker.

The input has `q+1` bits, so

```text
2^q <= m < 2^(q+1).
```

Also `m<T(m)<2^(q+2)`. Thus the full output has `q+1` or `q+2` bits, and its
suffix after the low odd marker has `q` or `q+1` bits.

### Exhausting the required-factor alignments

By L-9113's required-factor lemma, if the output suffix were accepted by
`R_(h,c)`, it would contain the length-`q` factor `p(c)`.

If the suffix has length `q`, it must equal `p(c)`. The full output then equals
the full input:

```text
T(m)=m.
```

Substitution in `(3m+1)/2=m` gives `m=-1`, impossible.

If the suffix has length `q+1`, there are two possible factor offsets.

At offset zero, the low `q` suffix bits equal `p(c)`. Canonicality supplies one
additional high `1`, so

```text
T(m)=m+2^(q+1).
```

The shortcut equation gives `m=2^(q+2)-1`, contradicting
`m<2^(q+1)`.

At offset one, write the extra low suffix bit as `d in {0,1}`. Since
`m=1+2v`,

```text
T(m)=1+2d+4v=2m-1+2d.
```

For `d=0`, the shortcut equation gives `m=3`; for `d=1`, it gives `m=-1`.
Both contradict `m>=2^q>=8`.

Every possible accepted-output alignment is impossible, so `T(w(c))` is
rejected.

## Dependency audit

- D-9101 fixes canonical LSD-first semantics.
- L-9113 supplies the required-factor lemma for an accepted reset-pattern
  suffix.
- L-9101 supplies the exact five-state executable shortcut relation and
  terminal flush used in X-9102.
- L-9102 supplies the unchanged materialized closure verifier used in the
  exhaustive differential tests. The displayed mathematical proof needs only
  one explicit closure violation, not the whole endpoint relation.
- No external `2^71` verification premise is used. The statement holds for
  every `q>=3` once the reset-pattern family is defined.

## Gap audit

- The witness depends on the assignment: the quantifiers are
  `forall c, exists w(c)`. No one concrete word is claimed to work for all
  assignments.
- The result excludes reset transitions back to `r0`. General exact-distance
  suffix DFAs may send nonadvancing edges to many earlier states and remain
  outside the claim.
- Gate 2 is already excluded for the larger L-9114 normal-form class. The
  present gate-2 conclusion is narrower and is not a replacement for L-9114.
- `UNSAT` is a family-classification result, not evidence for Collatz
  convergence.
- The proof and both implementations were produced by the same agent. The
  standard-library checker is implementation-independent but not an
  independent review, so status remains `PROPOSED`.

## Adversarial tests

- Every one of the 321 materialized candidates for `q=3,...,8`, all legal
  gates, and all parameter assignments is rejected by X-9101's unchanged
  `verify_candidate`.
- One q=71 assignment at each active gate is also materialized and rejected as
  an end-to-end integration control.
- An explicit ROBDD least-reachability product agrees with the compact proof
  on the same complete range.
- The full guarded least fixed point agrees through `q=6`.
- The independent checker reconstructs the five-state carry identities,
  terminal flush, parametric trace, and all four factor equations without
  importing X-9101 or the generator.
- Tests reject resealed semantic tampering rather than relying on the result
  digest alone.

## Remaining uncertainty

No mathematical gap is currently known in the finite-family argument. Formal
status should not be promoted until another agent reconstructs both the
required-factor use and all four bit-alignment equations.

## Suggested next attack

Relax the reset target from the single state `r0` to a small symbolic set of
earlier states. The present shortest-word input remains accepted, but the
required-factor lemma may fail; a useful extension must derive a replacement
output-rejection invariant without reverting to concrete CEGIS.
