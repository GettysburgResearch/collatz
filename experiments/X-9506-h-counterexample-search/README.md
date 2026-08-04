# X-9506 — exact counterexample-first search

**Status:** `INTERNAL EXACT COMPUTATION`; finite search only.

This experiment attacks the requested direction directly: look for a positive
ordinary infinite orbit or a positive periodic orbit of the exact H block map.
It does **not** infer the infinite theorem from a finite bound.

## Ordinary-state sweep

For precision `K`, the complete ghost residue set modulo `2^K` is enumerated
without storing the attractor. Every residue is the boundary value of one
finite visible word. The branch separation makes this enumeration duplicate
free and gives exactly

```text
N(K)=N(K-2)+N(K-3).
```

For each residue `g mod 2^K`, the program forms the unique ordinary candidate

```text
P in [0,3*2^K),
P = g mod 2^K,
P = 1 mod 3,
```

and replays the exact block map with arbitrary-precision fallback. Therefore
an infinite exact state `P<3*2^K` would necessarily be tested.

At `K=65` the sweep covers all

```text
62,608,681
```

ghost residues and every positive H A-state with

```text
p=3n+4 < 3*2^65,
n <= 2^65-2 = 36,893,488,147,419,103,230.
```

Result:

```text
cycles found:             0
orbits surviving 300 blocks: 0
maximum exact block life: 34
```

The maximizing tested start is

```text
p = 73,620,272,205,778,649,092
n = 24,540,090,735,259,549,696
```

with exact block letters

```text
0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0
```

before leaving the exact domain.

## Periodic-word sweep

A second exact meet-in-the-middle search exhausts every periodic block word of
length at most `14`.

For a word `w`, write

```text
F_w(p)=(V_w p+C_w)/U_w.
```

A positive periodic orbit must have `U_w>V_w` and

```text
p=C_w/(U_w-V_w) in Z,
p=1 mod 3,
p>=16.
```

The fixed point is the unique periodic 2-adic ghost of `w^infinity`, so these
conditions are sufficient for exact intermediate legality. All contracting
total exponent pairs and all word orders were searched. No positive cycle was
found through period `14`.

## Reproduction

```bash
g++ -O3 -std=c++17 scan_ordinary.cpp -o scan_ordinary
./scan_ordinary 65

g++ -O3 -std=c++17 scan_periodic.cpp -o scan_periodic
./scan_periodic --max-length 14
```

The programs use Boost.Multiprecision headers for exact overflow fallback and
large modular products. No external library linking is required.

Canonical summary:

```text
results/canonical.json
```

Semantic digest:

```text
0d85b778a21b8a76bcad4323b7992e64c7fc5e759c1a69c794f0d843dc15cd8a
```

## Scope boundary

This is a strong finite negative search result, not an unconditional proof of
termination and not a counterexample. A genuine counterexample, if one exists,
must begin above the stated bound and cannot be periodic with block period at
most fourteen.
