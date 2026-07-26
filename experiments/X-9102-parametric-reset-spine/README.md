# X-9102 — Exact Parametric Reset-Spine Closure

- **Experiment ID:** X-9102
- **Issue:** [#10](https://github.com/gfreund123/collatz/issues/10)
- **Agent:** `gpt56-sol-05`
- **Classification:** exact finite symbolic computation; mathematical claim
  remains `PROPOSED`
- **Candidate counterexamples:** none

## Research question

For `q=71`, fix a gate `h` in `3,...,70` and let

```text
c in {0,1}^70, c[0]=1, c[h-1]=0.
```

The suffix DFA has states `r0,...,r70`, start `r0`, and sole accepting state
`rh`. For `i<70`,

```text
delta(ri,c[i])   = r(i+1)
delta(ri,1-c[i]) = r0,
```

while `delta(r70,0)=r0` and `delta(r70,1)=rh`. Its canonical shortcut lift
adds state `s` with `delta(s,0)=s` and `delta(s,1)=r0`.

Does any of the `2^68` assignments at any active gate make the lifted
language forward invariant under the shortcut Collatz map?

## Result

No. All 68 gates are `UNSAT`, with no `UNKNOWN` records:

```text
68 gates * 2^68 assignments per gate
= 20,070,057,552,195,992,158,208 parameter assignments classified.
```

This is not a sampled or bounded-model result. Every gate has one compact
parametric closure-violation proof that covers its full parameter cube. The
result eliminates only the reset-pattern family from L-9113. It does not
eliminate arbitrary exact-floor suffix DFAs and says nothing about general
regular sanctuary existence.

The committed artifact is:

```text
results/parametric-reset-spine-q71-gates3-70.json
```

Its deterministic semantic-result SHA-256 is
`2116fb81d40b6de21c6df8306fa135d9d0ca5ec4a7583fa558a33930bfe9b680`;
the formatted-file SHA-256 is
`aad5b12ab1249d83adde64c0e9790b160a6d7ecd5212c818cc277bc138f9b876`.
No CNF was emitted, so `cnf_sha256` is explicitly `null`; a guarded
reachability proof was smaller and did not require a SAT dependency.

## Universal parametric witness

Put

```text
p = c[0] c[1] ... c[q-2] 1
w = 1 p.
```

Words are LSD-first. The first bit of `w` is the odd marker consumed by the
lift; the suffix `p` follows every advancing edge and its final `1` enters
`rh`. Thus `w` is accepted for every assignment.

Let `m=[w]` and `v=[p]`, so `m=1+2v`. Since `c[0]=1`, `m` is `3 mod 4`, and
the exact shortcut image

```text
y = T(m) = (3m+1)/2
```

is odd. The X-9101 five-state transducer, including its terminal carry flush,
is the executable arithmetic relation used by the guarded product.

The full input has `q+1` bits. Therefore `y` has `q+1` or `q+2` bits, and the
suffix after its low odd marker has `q` or `q+1` bits. L-9113's required-factor
argument says that an accepted suffix must contain `p`. There are only four
possible alignments:

1. A `q`-bit output suffix equals `p`, so `y=m`. The shortcut equation gives
   `m=-1`.
2. A `(q+1)`-bit suffix begins with `p`, so
   `y=m+2^(q+1)`. The equation gives `m=2^(q+2)-1`, above the input range.
3. A `(q+1)`-bit suffix ends with `p` and has extra low suffix bit `0`, so
   `y=2m-1`. The equation gives `m=3`, below the input range.
4. The same alignment with extra bit `1` gives `y=2m+1`, hence `m=-1`.

All contradict `2^q <= m < 2^(q+1)`. Consequently `T(w)` is rejected for
every assignment. Notice the quantifier order: the certificate proves
`forall c, exists w(c)` using one symbolic word template; it does not claim
one concrete word works for every `c`.

## Symbolic formulation and quantifier audit

`symbolic_closure.py` implements two exact guarded-product routes:

1. The q=71 classifier follows the acyclic parametric witness above. The
   parameter cube starts at the product start, every input edge has its
   explicit guard, and the exact factor-alignment terminal test covers the
   whole cube.
2. A general ROBDD least-fixed-point fallback starts with the full cube only
   at the product start and repeatedly unions guarded forward images. At a
   fixed point, a surviving assignment is materialized and passed to
   X-9101's unchanged `verify_candidate`; resource limits yield `UNKNOWN`.
   A negative fallback computation is also exported as `UNKNOWN` unless its
   complete derivation is serialized. The q=71 records do not use this
   fallback: each has the compact checkable proof.

The suggested existential inductive-set SAT encoding is sound only with all
three obligations:

```text
R(start)
R(v) and edge_guard(v,w,c)  => R(w)
R contains no bad terminal
```

With those clauses, arbitrary omission of a reachable state is impossible:
induction on path length forces every concretely reachable state into `R`.
Conversely, when no bad state is reachable, the least reachable set is a
witness for `R`. Thus this invariant encoding is existentially equivalent to
unreachability; requiring `R` itself to be least is unnecessary. Omitting the
start or guarded-closure clauses would be unsound.

X-9102 uses forward least reachability directly, so it does not depend on that
equivalence.

## Files

- `symbolic_closure.py` — generator/classifier, compact guarded proof,
  explicit ROBDD trace, complete least-fixed-point fallback, deterministic
  artifact writer, and strict in-process validator.
- `check_result.py` — separately implemented standard-library checker. It
  imports neither X-9101 nor the generator; it reconstructs the five-state
  carry table, terminal flush, guarded trace, algebraic obstruction, and any
  materialized SAT DFA.
- `test_symbolic_closure.py` — adversarial and differential tests.
- `results/parametric-reset-spine-q71-gates3-70.json` — q=71 classification.

## Validation

For every materialized assignment at every gate for `q=3,...,8`, the compact
proof and explicit ROBDD reachability agree with the existing X-9101
`verify_candidate`. This exhausts 321 `(q,h,c)` candidates. The tests also run
the full guarded least fixed point through `q=6`, materialize one q=71 member
at every active gate, check deterministic output, and reject digest, proof,
guarded-coverage, CNF-metadata, duplicate-key, and nonfinite-JSON tampering.

The frozen run used Python 3.12.3 on Linux 6.12.94+. The generator and checker
require only the Python standard library and the checked-in X-9101 source.
There is no randomness or solver seed.

Replay from this directory:

```text
python3 -B -m py_compile symbolic_closure.py check_result.py test_symbolic_closure.py
python3 -B -m unittest -v test_symbolic_closure.py
python3 -B symbolic_closure.py --detect-tools
python3 -B symbolic_closure.py \
  --q 71 --gate-min 3 --gate-max 70 \
  --output results/parametric-reset-spine-q71-gates3-70-replay.json
python3 -B check_result.py \
  results/parametric-reset-spine-q71-gates3-70-replay.json
```

At implementation time, no `kissat`, `cadical`, `minisat`, `glucose`,
`cryptominisat`, `z3`, `drat-trim`, `gratgen`, `lrat-check`, or `cake_lpr`
executable was present, and Python modules `z3`, `pysat`, and `pycosat` were
absent. No dependency was added because the direct guarded proof is exact and
independently replayable.

## Relationship to X-9101, L-9113, and L-9114

This is not another concrete-clause census. L-9113 proves that a concrete
antecedent bank needs exponentially many factors to cover this family.
X-9102 instead supplies one **parametric antecedent** `w(c)` and proves its
image rejected for the entire cube.

L-9114 excludes gate 2 for every exact-distance suffix DFA satisfying its
normal form. X-9102 excludes the much narrower reset-pattern family at every
gate (including gate 2 in small-q validation). It neither duplicates nor
strengthens L-9114 for non-reset transitions.

X-9101 remains the source of the five-state shortcut transducer and the
materialized verifier used for differential testing. X-9102 adds the
previously missing exact parametric classification and a checker that does not
import X-9101.

## Limitations

- The independent checker is a separate implementation by the same agent,
  not an independent human or agent review.
- The elementary proof relies on the required-factor property proved in
  L-9113; the checker also reconstructs the guarded trace directly.
- `UNSAT` concerns a finite automaton template, not Collatz convergence.
- No sanctuary candidate or ordinary counterexample integer is produced.
