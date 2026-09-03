# Research map and open frontiers

> **Collatz remains unsolved.** This page is the durable scientific synthesis. It distinguishes resident proofs, source-pinned reviewed work, external source-qualified advances, open obligations, and proposed connections.

## Central firewall

For the shortcut map

\[
T(n)=\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2,
\end{cases}
\]

three objects must remain distinct:

1. every finite prefix has positive ordinary representatives;
2. compatible prefixes determine one point of `Z_2`;
3. one fixed positive ordinary integer realizes every prefix and the physical dynamics forever.

The resident extraction theorem says that ordinary realization occurs exactly on an eventual boundary face of canonical representatives; for nested positive survivor sets, bounded least roots are exactly the missing compactness principle. The `(1110)^∞` packet gives an explicit high-drift completion ghost showing why compatibility plus conditional growth is insufficient.

## Status of the resident spine

| Record | Exact status | What is resident | What remains |
|---|---|---|---|
| `IC-EXTRACT-001` | `VERIFIED`, accepted with local proof | signed residue stabilization and bounded-minimum extraction | decide a concrete least-root sequence |
| `IC-GHOST-001` | `VERIFIED`, accepted with local proof | finite parity cylinders and the `-19/11` ghost | architecture-specific ordinary extraction |
| `IC-PERIODIC-001` | `SOURCE-QUALIFIED`; components verified at exact SHAs; synthesis pending narrow review | component proof packet for periodic fixed points, full denominator, and preperiod transfer | review the exact combined wording; then solve the nontrivial cycle problem |
| `IC-SC-001` | `VERIFIED`, accepted with local proof | all-supercritical divergence and SC\* equivalence | prove universal fixed-source stopping |
| `IC-AUT-001` | `VERIFIED`, accepted with local proof | fixed-depth cofinite-tail/SCC obstruction | build a sound ordinary-boundary abstraction |
| `IC-RIG-001` | `VERIFIED`, accepted with local proof | one exact six-branch chart under complete-tree, full-tail, finite-control, eventual-integrality hypotheses | decide its least roots or use genuinely unbounded nonlinear state |
| `IC-REF-001` | false source statement, exact refutation accepted with local proof | constant-word counterexamples | preserve the refutation |
| `IC-REP-001` | separate `VERIFIED` repair, accepted with local proof | local repair proof with exact PR #16 dependencies source-pinned | import or reprove the dependencies; apply to a natural language |

Read the packets at [`../research/integrated/`](../research/integrated/README.md). The first eight are a resident spine, not a complete account of the reviewed repository; see the [`results catalog`](../research/RESULTS_CATALOG.md).

## External source-qualified advances: Mazur 2026

The [`Mazur 2026 external packet`](../research/external/mazur-2026/README.md) imports exact PDF fingerprints, public source routes, and provenance for two outside, publicly Lean-checked theorem families. This repository performed a full-paper read, visual page audit, and small exact-arithmetic checks, but did not replay the full Lean closures or the 645.7 MB predecessor payloads. The results therefore remain **EXTERNAL SOURCE-QUALIFIED**, not resident.

### Inverse predecessor growth

For every fixed positive target `a` with `3 ∤ a`, the imported predecessor theorem gives

\[
\pi_a(X)\ge C_aX^{901/1000}
\]

eventually, hence the unit-coefficient lower bound `pi_a(X)≥X^(9/10)` eventually. Its key method is an adaptive level-18 Krasikov–Lagarias elimination: a bounded potential chooses a fallback lift only when every ordinary auxiliary lift is history-dominated, while time-local critical pruning separately follows actual functional minima.

This is a strong inverse-tree population theorem. It does not prove `SC*`, ordinary all-depth realization, positive density, or cycle exclusion.

### Forward natural-density descent

For every threshold `f(N)→∞`, the imported forward theorem gives natural-density-one raw Collatz descent below `f(N)` by `C_Coll log N`, with `C_Coll<436`; the odd Syracuse form has odd-relative natural density one and `C_Syr<145`. A fixed-target form bounds the odd timed bad fraction by `C_d(log N_0)^(-d)` for every `0<d<5/143`.

This improves the averaging mode and retains one explicit clock, but it permits a density-zero exceptional set, does not assert arrival at one, and gives no power saving in the counting endpoint for a fixed floor.

### Proposed exponent-race bridge

The packet proves the following conditional reduction, pending narrow review as a repository connection:

> If predecessor sets grow as `Omega(X^gamma)` for every eligible fixed target and, for every fixed height `H`, odd starts that stay above `H` for logarithmic time are `O_H(X^beta)` with `beta<gamma`, then Collatz follows by a least-counterexample argument.

The imported inverse result supplies `gamma=0.901`. Thus a new fixed-height forward bound with any `beta<0.901` would close the conjecture. The current natural-density estimate has effective endpoint exponent one, so no contradiction is yet available. See [`synthesis-and-roadmap.md`](../research/external/mazur-2026/synthesis-and-roadmap.md) for the proof and research programs.

## Program 1 — ordinary extraction and completion

For compatible residues `r_n mod K_n`, a nonnegative ordinary point occurs exactly when the least representatives eventually stabilize; a negative ordinary point occurs when the upper co-representatives stabilize. For nested positive sets `S_n` with minima `m_n`,

\[
\bigcap_n S_n\ne\varnothing
\iff \sup_n m_n<\infty
\iff m_n\text{ eventually stabilizes}.
\]

### Load-bearing gap

For one concrete aperiodic architecture, prove either boundedness/stabilization or escape `m_n→∞`. More finite witnesses, a compact inverse limit, entropy, refund capacity, or conditional growth do not decide this.

## Program 2 — periodic tails, cycles, and the complete denominator

For a parity block `w` of length `L`, weight `s`, and affine constant `C_w`, the reviewed component arguments yield the unique periodic 2-adic realizer

\[
x_w=\frac{C_w}{2^L-3^s}.
\]

Positive ordinary realization requires the **complete** denominator and exact replay. Proper factors, local residues, or near-integrality are insufficient. The all-zero endpoint, finite preperiod, trivial cycle, and controller-to-parity compilation are included in the source-qualified synthesis but still require one narrow integrated-wording review.

### Load-bearing gap

Produce and replay one nontrivial positive cycle, or prove a complete all-word obstruction. Large bounded censuses remain finite evidence.

## Program 3 — coefficient stopping / SC\*

Let

\[
C_k(n)=\frac{3^{q_k(n)}}{2^k},
\qquad
\tau_c(n)=\min\{k\ge1:C_k(n)<1\}.
\]

Let `m_N^sup` be the least source whose first `N` coefficient prefixes are all supercritical. The resident theorem proves

\[
m_N^{sup}\to\infty
\iff
\tau_c(n)<\infty\text{ for every fixed }n>0.
\]

An ordinary orbit with all prefixes supercritical tends to `+∞`; this classifies the hypothetical survivor but does not exclude it.

### Smallest missing lemma

For each fixed `n`, bound the length of every all-supercritical word realized from `n`. Equivalently, beyond a source-dependent threshold prove

\[
v_2(3^{q(w)}n+A_w)<|w|.
\]

## Program 4 — first crossing / FC\*

For a first coefficient crossing of length `j` and weight `q`, put

\[
D=2^j-3^q>0,
\qquad
A_w=Dr+2^j d=Ds+3^q d,
\qquad s=r+d.
\]

`FC*` asks to exclude every complete nontrivial canonical realization with `d≥0`, including `d=0` cycles and `d>0` near-returns, using one common displacement, every denominator factor, all proper-prefix inequalities, compatible source/end quotients, and exact replay.

### Smallest missing lemma

Prove that the large complete denominator blocks cannot return the same small ordinary displacement and quotient jets in every factor. A one-factor sieve, bounded support theorem, or polynomially small candidate family is not enough.

## Program 5 — automata, rigidity, and representation limits

The resident method boundaries show:

- a fixed-depth safe language is cofinite and its terminal SCC is a finite-horizon artifact;
- in the exact six-branch chart, the ordinary high quotient immediately leaves the same language;
- complete-tree finite affine control collapses to the expanding forward map;
- complete-tree finite rational sections collapse after eventual integrality;
- the all-depth survivor contains no infinite arithmetic progression or semilinear forward-invariant sanctuary;
- one unrestricted factor-complexity screen is false, while its nonconstant repair is valid in the induced `64→81` model.

These results do **not** rule out arbitrary regular sets, proper sublanguages, unbounded arithmetic state, pushdown mechanisms, or direct height arguments.

## Proposed bridge

`RD-BRIDGE-001` proposes that a least positive counterexample has exactly two coefficient lanes: no first crossing (SC\*) or a first crossing producing an FC\* witness. The reviewed ingredients include the no-descent framework, all-supercritical classification, and cycle absorption. The exact source/end normalization, repeated-state coverage, trivial-cycle treatment, and cross-PR notation still need one narrow review.

Use **“principal proposed roadmap bridge,”** not **“established exhaustive reduction.”**

The external `MZ-BRIDGE-001` exponent-race reduction is a second proposed route. It compares a lower exponent for the inverse basin of an orbit point with an upper exponent for fixed-height forward survivors. It is not part of the canonical registry and does not replace `RD-BRIDGE-001` unless its missing forward power-saving theorem is proved and reviewed.

## Proposed cross-program connections

The following are useful hypotheses, not accepted theorems:

- **PROPOSED:** any symbolic or automata construction should export canonical least representatives, so the extraction firewall becomes a mandatory interface rather than an after-the-fact warning.
- **PROPOSED:** a bounded-state schedule generator routes into the periodic/full-denominator packet; only seed-first unbounded state can evade that firewall.
- **PROPOSED:** support-loss and factor-synchronization estimates may combine only if they preserve one common ordinary displacement across the complete denominator.
- **PROPOSED:** Lane-A rank or fresh-prime escape matters only after a theorem transfers numerator complexity to ordinary source or endpoint height.
- **PROPOSED:** natural/harmonic passage transport should be conditioned on physically realizable all-supercritical cylinders; ambient density alone cannot prove fixed-source stopping.
- **PROPOSED:** sparse nonzero adaptive fallback states in the level-18 predecessor potential may admit a structural 3-adic description and a uniform higher-level potential family.

## Where to go next

- Resident proof bodies: [`../research/integrated/`](../research/integrated/README.md)
- Reviewed source-pinned families beyond the spine: [`../research/RESULTS_CATALOG.md`](../research/RESULTS_CATALOG.md)
- External source-qualified imports: [`../research/external/`](../research/external/README.md)
- Agent workflow: [`../AGENTS.md`](../AGENTS.md)
- Exact historical review and lifecycle evidence: [`../archive/README.md`](../archive/README.md)
