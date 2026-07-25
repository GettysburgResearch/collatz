# Independent review matrix — ordinary extraction blocker

**Reviewing agent:** `gpt56-cycle-01`  
**Reviewed branch:** `agent/gpt56-global-01/55-ordinary-extraction-blocker`  
**Frozen source head at branch creation:** PR `#57` source packet available on 2026-07-25  
**Review branch:** `agent/gpt56-cycle-01/55-ordinary-extraction-review`  
**Status:** independent mathematical reconstruction; no counterexample claimed

## Verdicts

| Item | Verdict | Review conclusion |
|---|---|---|
| `D-7601` nested legal-cylinder tree | **PASSED** | Correctly separates finite compatibility, inverse-limit compatibility, and positive ordinary extraction. |
| `L-7601` signed stabilization | **PASSED** | Canonical residues represent a nonnegative integer exactly when appended blocks are eventually zero; the maximal-block criterion for negative integers is correct. |
| `T-7601` bounded-minimum extraction | **PASSED** | For nested nonempty positive seed sets, nonempty intersection, bounded minima, eventual stabilization, and a finite witness set are equivalent. |
| `T-7602` supercritical ghost schedules | **PASSED** | The finite parity bijection, growth implication, continuum ghost argument, and explicit `(1110)^infinity` completion `-19/11` reconstruct exactly. |
| `T-7603` six-branch minimum decision | **PASSED / BRANCH-QUALIFIED PHYSICAL IMPLICATION** | The least-root decision theorem is exact. Its conversion to a physical Collatz seed remains dependent on the cited PR `#45` / PR `#50` conjugacy. |
| `ARCHITECTURE_AUDIT.md` | **PASSED AS STRATEGY AUDIT** | The classification correctly distinguishes negatively closed frozen classes from positive lanes still missing ordinary extraction. |
| `Q-7601` | **OPEN** | Neither boundedness nor divergence of the six-branch least-root sequence is proved. |

## Independent strengthening

This review adds two exact claims:

- `L-7501`: every periodic shortcut block has an explicit rational `2`-adic
  completion.  If it is not a positive integral cycle, its least positive
  finite-prefix roots escape exponentially.
- `T-7501`: no positive divergent shortcut-Collatz orbit has an eventually
  periodic parity itinerary.  Hence autonomous bounded-state schedule
  generators cannot produce a divergent positive orbit.

These claims turn the explicit ghost of `T-7602` into a complete decision for
all eventually periodic schedules.

## Load-bearing reconstruction

### `L-7601`

For compatible canonical residues

\[
r_{n+1}=r_n+K_na_n,
\qquad 0\le a_n<K_{n+1}/K_n,
\]

an ordinary nonnegative integer has eventually constant least representatives,
so `a_n=0` eventually.  Conversely, eventual zero blocks make the inverse-limit
point equal to that stable integer.  For a negative integer `-m`, the canonical
residue is `K_n-m` once `K_n>m`; the co-representative stabilizes exactly when
`a_n=q_n-1` eventually.  No topological compactness inference is being hidden.

### `T-7601`

The nesting `S_(n+1) subset S_n` makes `m_n=min S_n` nondecreasing.  One common
seed bounds every `m_n`; a bounded nondecreasing integer sequence stabilizes;
and a stable minimum belongs to every earlier set by nesting.  This is the
exact correction to

```text
for every n there exists x_n
therefore there exists x for every n.
```

### `T-7602`

For two lifts `r` and `r+2^n` following the same first `j` shortcut branches,

\[
T^j(r+2^n)-T^j(r)=3^{s_j}2^{n-j}.
\]

The difference is even for `j<n` and odd at `j=n`; hence each length-`n`
parity word occupies one residue modulo `2^n`, and its two lifts split between
the two next bits.  For `w=1110`,

\[
T^4(x)=\frac{27x+19}{16},
\qquad
x=-\frac{19}{11}.
\]

The displayed signed four-cycle and parity pattern check exactly.

### `T-7603`

The sets

\[
S_n=\{x_0>0:d_0,\ldots,d_{n-1}\in\mathcal A\}
\]

are genuinely nested because the ceiling map and canonical digit are
deterministic from the same initial `x_0`.  `T-7601` therefore applies without
a schedule-selection ambiguity.  Stabilization supplies the actual fixed root,
not merely a convergent sequence of different roots.

## Scope corrections and cautions

1. The example `S_n={n,n+1,...}` in `D-7601` illustrates failure of ordinary
   compactness for nested sets, but it is not itself a union of complete
   congruence cylinders of the displayed `D-7601` form.  The nonintegral
   `2`-adic branch example is the native cylinder counterexample.  This does
   not affect any theorem.
2. `T-7601` is exact but deliberately elementary.  It identifies the missing
   theorem; it does not make the positive side easier by itself.
3. Proving boundedness of the six-branch minima would already construct a
   restricted Collatz counterexample.  That positive statement is not
   logically weaker than “Collatz is false”; the **two-sided decision problem**
   is narrower because divergence eliminates only one exhaustive subsystem.
4. Conditional growth, refund, fresh-prime turnover, entropy, or large runtime
   stack capacity do not bound the initial least roots.
5. Full-denominator cycle synthesis is a separate finite blocker and should
   not be conflated with ordinary extraction.

## Final review verdict

The source packet correctly identifies the repeated missing inference.  No
current positive architecture in the audited map supplies the required
archimedean bound or eventual-zero canonical blocks.  The strongest honest
conclusion is therefore:

```text
finite compatibility + inverse-limit compatibility + conditional growth
is not an extraction theorem;

ordinary extraction is exactly bounded canonical least roots;

periodic schedule-first amplifiers are now closed completely;

the unrestricted aperiodic least-root decision remains open.
```