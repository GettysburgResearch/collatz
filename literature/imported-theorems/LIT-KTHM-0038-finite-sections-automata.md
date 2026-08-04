# LIT-KTHM-0038 — Finite rooted-tree sections are exactly finite-state p-adic transductions

**Type:** standard automaton-group theorem, aligned with Anashin's analytic criterion.  
**Sources:** finite-state rooted-tree automorphisms; Anashin's van der Put finiteness criterion.  
**Maps to:** PR #3 padding/correction maps, Foundry operators, and PR #34 `L-9863`--`L-9867`.

## Definitions

Let `f:Z_2->Z_2` be a 2-adic isometry. For a least-significant-first binary prefix `p` of length `k`, define the section `f|_p` by

```text
f([p]+2^k z)=F_k(p)+2^k(f|_p)(z),                    (1)
```

where `F_k(p)` is the canonical output prefix modulo `2^k`.

Let

```text
Sec(f)={f|_p : p a finite binary word}.              (2)
```

## Theorem

The following are equivalent:

1. `f` is realized by a finite synchronous least-significant-first Mealy machine;
2. `Sec(f)` is finite.

When finite, the canonical machine with one state per distinct section is minimal.

## Proof

If `Sec(f)` is finite, use the current section as the machine state. On reading one input bit, equation `(1)` determines the next output bit and moves to the corresponding child section. This finite machine realizes `f`.

Conversely, after a deterministic synchronous machine reads a prefix `p`, its current state determines the output on every continuation. That continuation map is exactly `f|_p`. Hence a finite machine can reach only finitely many distinct sections.

Distinct sections disagree on some continuation and therefore cannot be merged in any deterministic exact machine. The section machine is minimal. ∎

## Analytic companion

Anashin characterizes finite-state p-adic automaton functions through their reduced van der Put coefficients. This supplies an alternative computational test and algorithms translating between coefficient automata and Mealy machines.

## Native use

For an exact p-adic correction or address map:

1. compute sections to increasing depth;
2. minimize the observed section machine;
3. prove closure of the section set, yielding a finite transducer; or
4. prove infinitely many sections, yielding an exact finite-state obstruction.

Triangularity or isometry alone is insufficient: an isometry may have infinitely many sections.