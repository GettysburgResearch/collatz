# Literature audit — waves 1 through 6

**Agent:** `gpt56-pro-03`  
**Issue:** `#7 — P1 literature audit and imported theorem suite`  
**Status:** citation and applicability audit; no native theorem is promoted by this package

This is the repository's durable external-results layer. It remains namespaced because active branches still use colliding native claim identifiers.

- `CLAUDE/...` refers to the issue-#4 symbolic-rewrite branch.
- `PR3/...` refers to draft PR #3.
- `TERM/...` refers to draft PR #6.
- `PING/...` refers to draft PR #11.
- `REG/...` refers to draft PR #12.
- `ADEL/...` refers to draft PR #16.
- `H/...` refers to draft PR #19.
- `PADIC/...` refers to draft PR #20.
- `FOUNDRY/...` refers to issue #21's diagonal-foundry branch.
- `DRIFT/...` refers to draft PR #35.
- `LIT-KTHM-####` identifies an imported theorem and never replaces a native claim ID.

## Wave 1 — foundational audit

Wave 1 located and audited the classical substrate: Terras/Everett parity cylinders, Lagarias surveys, Tao's almost-all theorem, automaticity and Gelfond–Schneider, Skolem–Mahler–Lech, Fatou–Pólya recurrence rigidity, Mahler/FLP, Fourier-decay and measure-rigidity neighbors, backward trees, and generalized undecidability.

It added `LIT-KTHM-0001` through `0014`, a verified source ledger, claim maps, applicability audits, and an explicit `UNVERIFIED` register.

Key discipline established:

```text
located theorem
 != native hypothesis reduction
 != analogy
 != novelty proof.
```

## Wave 2 — live portfolio audit

The common frontier was an **infinite ordinary-integer realization theorem**. Large finite objects, compact completion points, compatible residue prefixes, and decidable fixed-certificate checks were not enough.

Wave 2 added `LIT-KTHM-0015` through `0027`, covering affine monoids, rational-base addresses, graph potentials, clopen obstructions, regular transductions, safety kernels, cycle equations, transfer bounds, and graph-directed attractors.

### Blocking correctness finding

`PING/T-0104` and `PING/T-0105` are false as stated. For

```text
D0 = {0, 2^L - 1},
E  = {0, 1},
D1 = D0 + 2^L E,
```

one has `R(D0)=0`, while `D1-D1` contains `±1`. `LIT-KTHM-0024` supplies the corrected sufficient condition

```text
diam(D0) + R(D0) + 1 < 2^L,
```

which must hold at every iterated stage.

## Wave 3 — completion height and ordinary-marker convergence

The active programs converged on

```text
infinite directive
 -> one unique completion point in Z_2
 -> an ordinary integer exactly when least representatives
    or new digit blocks stabilize.
```

Wave 3 added `LIT-KTHM-0028` through `0033`:

- Foundry fixed points as strict `2`-adic contractions;
- p-adic automata and van der Put criteria;
- PR #3's explicit `-(7/4)log_2(3)` bulk;
- H ghosts as a separated countable `2`-adic IFS;
- the critical-particle size-biased spine;
- Krieger/MacDonald symbolic embedding as a conditional router theorem.

PR #16 and PR #20 independently produced the same completion-height constant

```text
1/(log_64 81 - 1)=17.654847...
```

through carry-run and repeated-factor arguments.

## Wave 4 — q-series, centered powers, and finite-state normalization

Wave 4 added `LIT-KTHM-0034` through `0041`.

1. Every periodic stack value is a finite vector of p-adic Tschakaloff values.
2. PR #16's ordinary section is exactly a centered rational-power orbit.
3. Finite synchronous transducibility of a `2`-adic isometry is section finiteness; Anashin supplies the van der Put criterion.
4. PR #3's ordinary quadratic bulk is formal multiplicative-group doubling.
5. Standard one-counter Foundry feedback has ultimately periodic autonomous output.
6. Static fractional Hall allocation can be purified under atomlessness, without producing temporal or integer coherence.
7. State-dependent finite traps and path-complete potentials extend common contraction.
8. q-Lucas/Cartier and min-plus section machines were identified as exact next objects.

PR #32 independently reconstructed the complete all-depth weighted-EQ chain; formal promotion belongs to the native ledger.

## Wave 5 — period-nine closure and Diophantine interfaces

The full Väänänen–Wallisser paper was supplied and inspected. Wave 5 added `LIT-KTHM-0042` and `0043`.

### Periodic stack tails through period nine

The source theorem applies to the exact PR #20 phase vector through dimension nine and fails its sufficient numerical condition at dimension ten. Consequently:

```text
minimal eventual periods 1,...,9:
  irrational selected 2-adic context;

minimal eventual period 10:
  first fixed period outside that source condition;

balanced nonperiodic 17/18:
  requires period-uniform estimates and S-adic passage.
```

### S-unit interface

`LIT-KTHM-0043` imports Evertse–Schlickewei–Schmidt finiteness for nondegenerate finite-rank multiplicative equations and supplies a strict native checklist: one fixed equation, finite rank, injective parameters, a proper-subsum audit, a finite-alphabet recurrence argument, and an explicit ordinary-realization contradiction.

This interfaces with PR #3/PR #33 cap stitches and PR #19/PR #34 successive H cores.

## Wave 6 — completion firewall and block q-Gaussian factorization

Wave 6 re-read the newest PR #3, PR #16, PR #19, PR #20, PR #32, PR #34, and PR #35 states and added `LIT-KTHM-0044` through `0047`.

### 1. PR #20 all-directive withdrawal

PR #20 correctly withdrew:

```text
T-9418  unbounded gaps imply irrationality;
T-9419  every positive stack directive is irrational;
T-9420  rational code iff eventually periodic;
T-9421  ordinary section triviality.
```

The same rational partial sums may converge to different values in `R` and `Q_2`. `LIT-KTHM-0044` supplies an elementary counterexample and the correct completion-safe Padé pattern:

```text
one rational Padé pair
 + finite-place error for the target
 + Archimedean bounds for the same rational coefficients
 + product formula
 -> contradiction.
```

The exact denominator-descent lemmas remain valid; the withdrawn statements remain open rather than refuted.

### 2. Exact decimated q-Gaussian moment lift

For PR #34's combined period-`r` moments, `LIT-KTHM-0045` proves

```text
nu_N=sum_(h=0)^(r-1)D_hm_(rN+h),
m_k=q_0^[k(k-1)/2]b^k,
```

or equivalently

```text
nu_N=L(D_W(x)x^(rN)).
```

The fine base Hankel determinant is an explicit Vandermonde product. Thus the periodic object is one fixed polynomial deformation of a quadratic-exponential moment functional followed by `r`-fold decimation.

### 3. Christoffel factorization and its exact nonapplication

Krattenthaler's theorem factors an ordinary fixed-degree polynomial moment deformation into the base Hankel determinant times one fixed-size orthogonal-polynomial determinant. `LIT-KTHM-0046` imports the result and shows why the scalar version does not retain the stack residue classes modulo `r`.

The correct target is the block functional

```text
L_h(y^N)=L(x^(rN+h)),
0<=h<r,
```

within biorthogonal Stieltjes–Wigert and mixed multiple-orthogonal theory.

### 4. Bulk cancellation in Hankel ratios

`LIT-KTHM-0047` proves the standard determinant identities

```text
h_n=Delta_(n+1)/Delta_n,
beta_n=Delta_(n+1)Delta_(n-1)/Delta_n^2.
```

These are the natural objects in which a universal cubic Hankel bulk can cancel. This explains why PR #34's cubic raw Schur quotient is a method boundary, not a no-go for Cramer ratios.

### 5. All-fixed-period proof program

PR #34 `T-9821` already supplies nonzero combined Hankel minors and the exact quadratic `2`-adic error. The remaining theorem is:

```text
base/bordered minor
 = universal fine q-Gaussian bulk
   x fixed-rank r-component boundary determinant,
```

followed by

```text
log_2 H(A_n:B_n)
 <=(81Sr-eta_r)n^2+o(n^2)
```

for some `eta_r>0`. The product formula would then prove irrationality for every fixed positive period.

Period-uniform control of the boundary factor is still needed to pass to the balanced S-adic directive.

### 6. PR #3's moving two-block frontier

The fixed corrected-stage architecture now has at most 64 eventual rooms; every possible room is transcendental and determines one tail. Existence requires one adjacent twelve-bit pattern—zero input cell plus allowed Hensel output lift—at every sufficiently late scale. The filter is empty in a finite audited range, but cofinal emptiness remains open.

### 7. PR #35's control frontier

The exact `5/4` completion and depth-50 minimum reinforce the same lesson: finite thinness, exact deep cylinders, and density zero do not replace an asymptotic minimum-divergence theorem.

## Verdict vocabulary

- **KNOWN — EXACT:** the located source proves essentially the same statement after notation changes.
- **KNOWN — COROLLARY:** the native statement follows by a short supplied derivation.
- **PARTIAL OVERLAP:** a load-bearing component is known, but the full native statement is not imported.
- **FOLKLORE / STANDARD:** elementary or standard; a proof is supplied where useful.
- **POSSIBLY NOVEL FORMULATION:** no exact antecedent was located after a documented search; not a novelty proof.
- **UNVERIFIED:** source attribution or exact theorem match was not confirmed.
- **MISAPPLIED / HYPOTHESES FAIL:** the cited theorem does not justify the native inference as written.
- **INTERNAL EXACT COMPUTATION:** a repository computation, not a literature theorem.

## Package map

- `literature/LIVE_REPO_REVIEW_WAVE2.md` through `LIVE_REPO_REVIEW_WAVE6.md` — live cross-program reviews.
- `literature/SOURCE_LEDGER.md` and wave supplements — only located sources, with inspection level.
- `literature/CLAIM_CROSSWALK.md` and `literature/claim-maps/` — branch-qualified mappings.
- `literature/APPLICABILITY_AUDITS.md` — theorem-hypothesis checks and nonapplications.
- `literature/UNVERIFIED.md` and wave supplements — honest source and applicability gaps.
- `literature/imported-theorems/` — 47 atomic statements/proofs/black-box boundaries.
- `literature/topic-notes/` — reusable research maps.
- `literature/references*.bib` — bibliographic records.
- `literature/check_literature*.py` — mechanical integrity checks.

## Process recommendation pending owner approval

Add a short README section establishing imported-theorem IDs, inspection levels, separation of source theorem/native reduction/analogy, and mandatory narrowing, withdrawal, or `REFUTED` status after a concrete review finding. Keep the fast-changing program dashboard in a separate `RESEARCH_INDEX.md`, not the stable README.

No statement in this suite resolves or refutes the Collatz conjecture.
