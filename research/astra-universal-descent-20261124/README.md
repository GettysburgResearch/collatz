# Unbounded smaller partners, uniform synchronization, and complete cycle denominators

**Collatz remains OPEN.** This is a full-proof attempt with three new research
lanes, developed by three parallel Astra 6.2 agents and synthesized by the root
agent on 24 November 2026. The positive partner theorem has been compiled in
Lean 4.34.1. The global counting and denominator theorems are written proofs,
with separately delimited finite Lean cores. See [verification](VERIFICATION.md)
for the exact source hashes, commands, axioms, and execution status.

The base is main at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
We inspected the live interfaces through PR191, used only the relevant source
statements, and did not re-audit the historical repository. Every new main
result below concerns actual ordinary sources or the complete reduced
denominator of an actual rational cycle. No GRH assumption is used.

## 1. A physical smaller partner at every ternary height

Use the ordinary shortcut map

```
T(n) = n/2                  if n is even
T(n) = (3n+1)/2             if n is odd.
```

For every h≥0 and positive odd u, let n=3^h u. If

```
3^(h+4) divides 1 + 2·4^h u,
z = (1 + 2·4^h u)/3^(h+4),
m = 2^(h+5) z − 1,
```

then

```
0 < m < n,                 T^(3h+7)(m) = T(n).
```

This whole statement, including the actual iteration and the existential
positive witness, is the Lean theorem `ShadowCore.guarded_certificate`.
It holds for unbounded h. The relative affine coefficient is
`(64/81)(8/9)^h`, and the intercept is negative.
For example, n=121 has the smaller partner m=95:

```
95 → 143 → 215 → 323 → 485 → 728 → 364 → 182 = T(121).
```

The congruence selects an infinite progression at every h. Independently,
the Chinese remainder theorem permits an arbitrarily long initial odd run
on n, so this construction enters every prescribed finite-clock obstruction
class. It does not cover every source at that h.

The all-height scope concerns arbitrary initial inputs. After an odd step,
an ordinary trajectory is not divisible by 3; on a recurrent or escaping
odd tail, only the h=0 portion of this certificate applies. The growing-h
family does not itself create a recurrent descent mechanism.

The same investigation proves unrestricted competing-word constraints,
an exact first eligible tier, and a complete inversion of smaller partners
at the immediate endpoint. These supporting statements remain written
mathematics. See [shadow.md](shadow.md) and [ShadowCore.lean](ShadowCore.lean).

**What still prevents strong induction:** every source outside the guarded
families still needs an actual smaller partner, or a separate convergence
argument. Passing to a different integer that satisfies the guard does not
solve that source's problem.

## 2. Uniform synchronized merging in every interval

Write u(n) for the odd part of n, and U(q)=u(3q+1) for the odd map. Put

```
theta = H_2(log(2)/log(3)) = 0.949955527188... .
```

There are absolute constants C,K such that for every integer interval I of
length L≥1, at any starting height, the number of distinct values

```
U^R(u(n)),     n in I and n>0,
R = ceil(K (log_2(2L))^2),
```

is at most

```
C L^theta / sqrt(log(2L)).
```

For every d>theta, the relaxed bound `C_d L^d` already holds after
`O_d(log L)` common odd steps. These are odd-step clocks; the number of
ordinary halving steps depends on the actual valuations.

This is an unconditional statement about every interval of ordinary
integers, including intervals very far above zero. Select the least source
in each terminal fiber. Every other source in the interval has a strictly
smaller ordinary partner in that same interval. The bound counts precisely
how many fiber minima this construction can leave unresolved.

The proof groups a common shortcut prefix by its number of odd steps.
Each group maps into a shorter interval whose width is independent of
the original interval's height. Keeping the widths separate preserves
the square-root logarithmic gain. A finite remaining-clock induction
gives the uniform synchronization time.

The related packing estimate applies uniformly to arbitrary transversals
of the exact moving inverse fibers in PR185. For their original mixture
zeta over N fibers, every modulus Q≥2 and every integer y satisfy

```
sum_{x != y, x == y (mod Q)} zeta(x)/|x-y|
    <= C log(2Q)/(N Q).
```

Combined with the pinned same-law collision lower bound, this forces a
large conditional harmonic mean separation between colliding ordinary
states. It does not bound the corresponding unweighted collision
probability from above. The precise missing separation estimate and all
orders of limits are in [escape.md](escape.md).

[EscapeCore.lean](EscapeCore.lean) formalizes the affine interval bound, the concrete odd-core transport,
and the deterministic finite-clock and inverse-fiber injectivity steps.
The binomial-tail, strong-induction counting, and infinite weighted-sum
arguments are written proofs, not claimed as fully Lean formalized.

## 3. A lower bound on the actual reduced cycle denominator

Take any primitive shortcut word with period A and a positive rational
cycle. Let d be the common reduced denominator after **all** numerical
cancellation, m its minimum, e=d m, and P(k) the number of distinct cyclic
length-k parity blocks. For every nonnegative s,t with s+t=P(k)<A,

```
2^(k+t) <= max(
    2^t (2^s-1)e,
    (3^t-2^t)(e+d)
).
```

This is an exact integer test. Setting d=1 gives a necessary condition
for an ordinary cycle, with no rounding or selected denominator factors.
Balancing the two sides yields

```
d(m+1) > 2^(k-P(k)/gamma)/2,
gamma = 1 + log(2)/log(3/2) = 2.709511291... .
```

The proof uses one window of cycle states around its minimum, in both
time directions. More starts than distinct parity blocks force two
different integer-scaled states into the same residue modulo 2^k.
This supplies a real lower bound on the reduced denominator rather
than on the formal polynomial denominator before evaluation.

The complete cycle product identity gives
`m <= p/[3(A log 2-p log 3)]`, with p the odd count. Thus the inequality
can be made entirely word-dependent. It excludes sufficiently low
complexity at a qualifying scale. Arbitrary high-complexity words remain
unresolved.

The cycle lane also constructs exact rational controls that are integral
at every member of any prescribed finite set of primes while their true
denominators tend to infinity. Those controls prevent an invalid passage
from finitely many local integrality checks to full integrality.

See [cycles.md](cycles.md) for the proofs and [CycleCore.lean](CycleCore.lean)
for the finite arithmetic scope.

## 4. How this attempt addresses the full theorem

The three lanes target different actual closing obligations:

| Lane | New result | Exact remaining universal step |
|---|---|---|
| Smaller partners | An unbounded, physically realized decreasing certificate, inside every fixed-clock obstruction class | Cover the remaining fixed sources |
| Escape and synchronization | Height-independent compression of every interval and weighted collisions on the unchanged inverse law | Control the residual fiber minima or the required unweighted separation |
| Cycles | A complete numerical denominator lower bound using two-sided factor complexity | Force a suitable complexity scale or supply a different obstruction for the high-complexity case |

These are not three proofs of Collatz. The universal coverage, unweighted
separation, and unrestricted cycle statements have not been proved.
The checkpoint records the positive results and the exact failure of the
attempt to close those last steps.

## 5. Second checkpoint: test the actual closing steps

The proof search continued after the first checkpoint, with the following
explicit outcomes. These are written results with an independently checked
proof; the numerical constant in the first has an exact rational certificate.

**The first endpoint does not give a uniformly inexpensive completion.**
For each fixed h>=1, more than 17/500 of the odd ternary units u, in relative
lower natural density, have no smaller partner at T(3^h u) within the
stated logarithmic excess budget. For a competing path with k odd steps,
the budget is (9/2)^(k-h-1) <= n/(2·3^(2h)). All competing words and clocks
are included; later source endpoints and larger budgets remain available.
The proof controls the rounding error in counting ordinary integers,
not merely the measure of residue classes in a completion.
[Exact statement and proof](SHADOW_COVERAGE_LIMIT.md).

**Positive rational cycles can have maximal factor complexity.**
For every fixed finite list of primes and every fixed positive minimum
floor, there are arbitrarily long positive rational cycles integral at
all those primes, with all cyclic blocks of length C log A distinct and
with true reduced denominator at least c·2^(A/2). Thus the low-complexity
scale required by the denominator screen does not follow from those
inputs. A proof using full ordinary integrality remains possible.
[Construction and proof](HIGH_COMPLEXITY_CONTROLS.md).

The concrete transport identity used in the synchronization proof is now
also formalized in Lean:

```
oddCore (T^k(n)) = U^(number of odd steps in the prefix)(oddCore n).
```

Together with the original finite cores, this gives 26 audited public
Lean declarations across the three modules. The complete analytic
synchronization proof and the two new limit results remain written
mathematics. The checker keeps the original checkpoint receipts and
separately records the changed module.

## 6. Inputs and scope

Only the comparison with PR185's collision lower bound imports its
source-qualified harmonic-flow construction. The partner construction,
uniform synchronization theorem, and cycle denominator bound above are
self-contained arguments.

The source snapshot is [SOURCES.json](SOURCES.json). Significant comparisons:

- PR182, head `cbec52dde5bed390a693310dd04e911033ba0cc9`:
  `research/phase-packing-round12-20261124/README.md`.
  Its origin-centered total-orbit bound already has the critical exponent
  and logarithmic gain. The new result here is uniform in translations,
  admissible inverse transversals, and a finite common synchronization clock.
- PR185, head `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`:
  `research/central-closure-20261123/COLLISION_LOGARITHMIC_GAIN.md`.
  Its critical same-law lower bound is retained with its original
  `1 <= m <= M`, `m^2 <= T M`, and source qualifications.
- PR187, head `099058f3f2602a48e109c964899f0a9a2a223338`:
  fixed-source repetition and complexity were already part of the program.
- PR191, head `37b3916633cd32a0c173b20bb18ec3a7ec290a63`:
  `research/two-sided-cycle-packing-20261124/README.md`.
  Its guarded return shadows and denominator packings are context, not
  assumed premises of the new arguments.

No claim of historical priority is made. Agent cross-inspection and Lean
execution are separately documented in [VERIFICATION.md](VERIFICATION.md).

