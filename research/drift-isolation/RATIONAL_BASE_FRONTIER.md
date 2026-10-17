# Rational-base frontier for the exact `5x+1` control chart

Agent: `gpt56-drift-01`  
Issue: #26  
Status: research frontier; no counterexample claimed  
Primary claims: T-8806, T-8807, R-8801

## Exact reduction

The two physical shortcut branches

```text
T_5^2(4q-1)=5q-1,
T_5^2(4q-2)=5q-2
```

become, after the shift `X=A+1`,

```text
4X_(j+1)=5X_j+delta_j,
delta_j in {0,1}.
```

Define the rational-base `5/4` representation tree by

```text
x --r--> y  iff  4y=5x+r,  r in {0,1,2,3,4}.
```

The least admissible digit at a node is

```text
b(x)=(-x) mod 4 in {0,1,2,3},
```

and the least child is `ceil(5x/4)`. Therefore a positive chart survivor exists
exactly when some root `X>=2` has a bottom word using only digits `0,1` forever.

This formulation is self-contained. The surrounding rational-base literature
is a source of methods, not an imported proof.

## Why this is high-upside

The problem is no longer an informal connector search. It is one exact language
avoidance question:

```text
Does there exist X>=2 such that
b(tau^j(X)) in {0,1} for every j>=0,
where tau(x)=ceil(5x/4)?
```

A positive answer immediately gives a strictly increasing `5x+1` shortcut
orbit. A negative answer completely closes this exact amplifier as a positive
ordinary certificate.

The same object has three simultaneous descriptions:

1. **physical:** an orbit staying in residues `2,3 modulo 4` under `T_5^2`;
2. **rational-base:** a bottom word avoiding digits `2,3`;
3. **2-adic:** a shifted ordinary point in the dimension-`1/2` Cantor set of
   T-8807.

Methods that are weak in one description may be strong in another.

## External adjacency

Akiyama, Marsault, and Sakarovitch study subtrees, bottom words, top words, and
successor transducers in rational-base representation trees:

```text
Shigeki Akiyama, Victor Marsault, Jacques Sakarovitch,
"On subtrees of the representation tree in rational base numeration systems",
Discrete Mathematics & Theoretical Computer Science 20(1), 2018,
DOI: 10.23638/DMTCS-20-1-10.
```

The attribution and publication metadata were checked against the official
journal version. Their framework uses the same edge form `q m = p n + a`.
Before importing any theorem, the exact hypotheses and orientation must be
audited against `p=5`, `q=4`, the bottom choice, and the restricted alphabet
`{0,1}`.

The most relevant methodological possibilities are:

- finite transducers relating neighboring roots;
- subtree equivalence and ultimately periodic branch obstructions;
- language growth of bottom-word prefixes;
- arithmetic structure of nodes sharing long prefixes.

No literature result is treated here as proving existence or nonexistence of a
low-digit infinite path.

## First finite landscape

X-8802 checks every `1<=A<=10^6`, equivalently roots `2<=X<=1,000,001`.
The numbers surviving at least depths `0,1,2,...` begin

```text
1,000,000,
500,000,
250,000,
125,000,
62,500,
31,250,
15,630,
7,818,
3,910,
1,954,
976,
487,
242,
133,
73,
39,
22,
12,
5,
1,
0.
```

The unique depth-`19` record in this range is

```text
A=786766,
X=786767,
low-digit prefix=1101100001001100001,
first exit A=54592968.
```

This is exact finite evidence only. It neither predicts nor excludes an
infinite survivor.

## Live theorem targets

### Target A — finite-state eventual escape

Construct a residue abstraction and a ranking function proving that every
bottom orbit eventually reaches residue `1` or `2 modulo 4`, forcing digit `3`
or `2`. The abstraction must be inductive for the growing map
`tau(x)=ceil(5x/4)`.

### Target B — self-replicating low-digit subtree

Find finitely many affine node families closed under bottom children, all with
bottom digits in `{0,1}`. This would be a genuine constructive route, but it must
produce one ordinary root rather than only a compatible `2`-adic limit.

### Target C — Diophantine prefix bound

A depth-`k` low-digit prefix means that `X` lies in one of `2^k` exact residue
classes modulo `4^k`, while the physical orbit has grown by about `(5/4)^k`.
Exploit the simultaneous small alphabet and ordinary-height constraint to prove
an upper bound on `k` in terms of `log X`, ideally with a coefficient too small
to permit infinite survival.

### Target D — successor propagation

Use a rigorously verified rational-base successor transducer to relate bottom
words of `X` and `X+1`. Seek a finite forbidden-pattern theorem that propagates
across every sufficiently long interval of roots.

## Failure conditions

- Finite-prefix survival is not infinite existence.
- A `2`-adic completion is not automatically an ordinary integer.
- A transducer for full representations is not automatically a transducer for
  bottom words or the restricted alphabet.
- Measure zero or dimension `1/2` does not imply an empty integer section.
- Any transfer back to `3x+1` remains heuristic until separately proved.
