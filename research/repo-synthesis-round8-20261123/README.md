# One actual scalar, finite recognition, and ordinary low-state returns

23 November 2026. Parent: `3954c775ba74e1f40776ff38cb4282698d4a334a`.

**Collatz remains OPEN.** This packet gives a smaller arithmetic
construction target, an explicit finite verifier, broad rational phase
exclusions, and an actual ordinary obstruction to a simple completion
attempt. It does not prove the universal arithmetic target.

The [repository synthesis](REPO_SYNTHESIS.md) records the whole-project
survey and why these three parallel attacks were selected. The
[source ledger](SOURCES.json) fixes upstream heads and proof boundaries.

## The central result: a real derivative already exists

For a positive odd ordinary q, let

\[
q_i=U^i(q),\quad g_i=v_2(3q_i+1),\quad
U(q_i)=(3q_i+1)/2^{g_i},\quad A_i=\sum_{j<i}g_j.
\]

The actual parity series and its real derivative at one satisfy

\[
B_q(z)=\sum_{i\ge0}\frac{z^{A_i}}{3^{i+1}},\qquad
\boxed{h(q)=2B'_q(1)=\sum_{i\ge0}\frac{g_i}{3^{i+1}}.}
\]

This real scalar exists unconditionally, has effective rational
enclosures, and obeys

\[
\frac12<h(q)\le1+\frac{\log_2q}{3},\qquad
h(Uq)=3h(q)-g(q).
\]

**R8-G2:** q reaches one if and only if `h(q)` belongs to `Z[1/3]`.
The same equivalence holds for every positive integer n with the
scalar `2B'_n(1)`; initial powers of two add an integer to h.

If `h(q)=a/3^r`, its denominator clears after r odd steps. Thereafter
the actual scalar is a positive integer, and the potential

\[
V(q,h)=\frac{q-1}{2^h-1}
\]

contracts by at most `3/4` per nonterminal odd step. Complete ordinary
gap equations are retained. [GERM_BRIDGE.md](GERM_BRIDGE.md) contains
the elementary construction and proof, including the sharp distinction
between the actual scalar and a freely chosen rational value.

## A supplied candidate can be decided in a bounded number of steps

**R8-G4:** Given a positive odd q, an integer a, and `r>=0`, the
equality `h(q)=a/3^r` has a total exact recognizer using at most

\[
\boxed{K(q,r)=4r+3\operatorname{bl}(q)}
\]

literal odd steps. It accepts at the standard endpoint or rejects an
incorrect candidate using exact rational bounds. It has no unresolved
output, but a rejected candidate does not refute convergence of q.

**R8-S1:** An incorrect candidate also satisfies

\[
\boxed{|h(q)-a/3^r|\ge3^{-(4r+3\operatorname{bl}(q)+1)}.}
\]

A certified approximation closer than this threshold proves equality.
[SCALAR_SEPARATION.md](SCALAR_SEPARATION.md) derives this from the
integer lattice at the verifier's rejection step. Producing a
successful candidate or sufficiently accurate approximation for every
q remains unproved.

## Which nontriadic rational phases are excluded

Write a putative rational scalar in lowest terms as `a/(3^r d)` with
`gcd(d,3)=1`. Its fractional parts after r steps follow multiplication
by three modulo d. The strict lower bound `h>1/2` supplies the smallest
admissible lift of each fraction. An exact finite phase sum then tests
contraction on the actual ordinary orbit.

[PRESSURE_CONSTRUCTION.md](PRESSURE_CONSTRUCTION.md) proves:

* All complete residual denominators `d>1` satisfying `3^k=-1 mod d`
  for some positive k are excluded, including the separately treated
  endpoint d=2.
* Among residual powers of two, only d=8 with numerator phase
  `{5,7}` survives this test. Its minimum scalar phases are `5/8,7/8`.
* For any prime `p>=5`, put `t=ord_p(3)` and `w=v_p(3^t-1)`.
  Every complete residual denominator `p^k` with `k>w` is excluded
  by a full residue-fiber argument.
* Literal convergence certificates for all odd sources through 31
  additionally exclude every numerator phase at each of
  `d=11,26,35,46,52,85,109`.

These are statements about complete residual denominators. They do
not exclude arbitrary composite denominators by testing their factors
separately. Irrational values are not excluded.

Under the earlier source-qualified escaping-component product, the
**same attained actual pressure maximum** m has

\[
\frac12<h(m)<H_*=
\frac23\sum_{j\ge1}\frac{\lfloor j\log_2 3\rfloor}{3^j}
<\frac{152}{243}.
\]

An exact forty-term enclosure puts `H*` below
`0.625344347433389`. This interval still contains `5/8`; clearing
a ternary denominator does not preserve the maximizing source.

## An actual obstruction to a tempting completion

One-step contraction of `q/h(q)` holds when `h(q)>=1`. It does not
pay for arbitrary low-state returns. [ORDINARY_SELECTOR.md](ORDINARY_SELECTOR.md)
constructs one positive ordinary source for every `m>=1` whose literal
prefix has gaps `(2,1)^m,(1,4)`. Its endpoint/source ratio is unbounded
as m grows, despite exactly one scalar state above one and all other
states below one. The source satisfies `q<2^(4m+11)`, so it uses at
most `4m+11` bits.

The actual initial scalar approaches `7/8` from below with explicit
error between `1/(4*9^(m+1))` and `3/(8*9^(m+1))`. The actual
scalar bounds use a finite prefix and the unconditional tail bound;
they do not assume convergence of the constructed terminal source.
This supplies changing finite ordinary sources, not one positive
ordinary infinite realization of the residual denominator-eight phase.

## Lean and exact execution

`GermBridge.lean` proves six finite arithmetic theorems for the
integer-stage contraction and candidate budget. `OrdinarySelector.lean`
proves eleven theorems for complete ordinary gap equalities, repeated
affine maps, scalar block intervals, the tail exponential estimate,
and affine expansion. Both modules are freshly compiled with Lean
4.34.1 and pinned Mathlib, with warnings treated as errors. An axiom
audit covers all seventeen theorems and three definitions.

The real series, its analytic interpretation, full modular source
construction, phase-family arguments, and their all-source attachment
remain written mathematics. The Lean scope is not advertised as a
formal proof of Collatz or of every result in this packet.

Run the bounded exact controls with:

```sh
python -X utf8 -B research/repo-synthesis-round8-20261123/exact_replay.py
python -O -X utf8 -B research/repo-synthesis-round8-20261123/exact_replay.py
```

The [execution and review report](../../reports/2026-11-23-repo-synthesis-round8/README.md)
records actual commands, source hashes, independent reconstruction,
finite coverage, and the complete-checkout gate. The
[literature boundary](LITERATURE_BOUNDARY.md) also records an exact
ordinary counterexample to an overlapping claimed uniform-descent
lemma, so that claim is not imported into this argument.
