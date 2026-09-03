# Research map and open frontiers

> **Collatz remains unsolved.** This page is the durable scientific synthesis. It distinguishes resident proofs, source-pinned reviewed work, open obligations, and proposed connections.

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

## Proposed cross-program connections

The following are useful hypotheses, not accepted theorems:

- **PROPOSED:** any symbolic or automata construction should export canonical least representatives, so the extraction firewall becomes a mandatory interface rather than an after-the-fact warning.
- **PROPOSED:** a bounded-state schedule generator routes into the periodic/full-denominator packet; only seed-first unbounded state can evade that firewall.
- **PROPOSED:** support-loss and factor-synchronization estimates may combine only if they preserve one common ordinary displacement across the complete denominator.
- **PROPOSED:** Lane-A rank or fresh-prime escape matters only after a theorem transfers numerator complexity to ordinary source or endpoint height.

## External formal results and density interfaces

Two 2026 preprints by Mazur, each with a Lean formalization at a frozen commit, are imported as literature packets: [natural-density almost-bounded orbits in logarithmic time](../literature/mazur-2026-natural-density-log-time/README.md) (for every `f→∞`, a natural-density-one set has an iterate below `f(N)` within `436 log N` raw steps; fixed-target bad sets have natural density `≪ (log N_0)^{-d}`, `d<5/143`) and [certified `x^{9/10}` predecessor-set lower bounds](../literature/mazur-2026-predecessor-x090/README.md) (`π_a(x) ≥ x^{9/10}` for every `a` with `3∤a`). Neither proves Collatz. Both are averaged or inverse-tree statements and sit on the far side of the central firewall from every program above; their formal proofs were **not replayed** here, their paper-exposed numerics were.

Their exact interfaces are developed in [`research/density-interfaces/`](../research/density-interfaces/README.md), all `PROPOSED`:

- `L-DI-001` / `T-DI-002`: a Lane-A source `n` whose surplus `D_k=q_k−αk` stays below `H` has an orbit of lower natural density `≥ 2·3^{-H}` inside the fixed-target bad set `B_{n−1}`; hence any fixed-target density bound below `2·3^{-H}` empties the bounded-surplus sub-lane of `SC*`. With the present ineffective constants this yields only `sup_k D_k ≥ d·log_3 log(n−1) − log_3 C_d`. The unbounded-surplus sub-lane, the generic case, is invisible to averaged theorems.
- `T-DI-003`: the basin of a least counterexample `n_*` satisfies `x^{9/10} ≤ #(M∩[1,x]) ≤ 2C_d x (log(n_*−1))^{-d}`; a constraint, not a contradiction.
- The [improvement map](../research/density-interfaces/IMPROVEMENT_MAP.md) ranks strengthenings of both papers (effective constants, clocks at the intrinsic `1/log(4/3)` rate, the exponent cap `5/143 → 1/20`, the limit `λ_k → 2` of the Krasikov–Lagarias program) and records that none of them creates a route to a full solution.

### Load-bearing gap

An **effective** fixed-target density bound. Without explicit constants the interface produces symbolic consequences only; with an explicit bound below `1/2` at a computationally verified target it would give the first positive-density lower bound for the basin of `1`.

## Where to go next

- Resident proof bodies: [`../research/integrated/`](../research/integrated/README.md)
- Reviewed source-pinned families beyond the spine: [`../research/RESULTS_CATALOG.md`](../research/RESULTS_CATALOG.md)
- External literature packets and their interfaces: [`../literature/`](../literature/README.md), [`../research/density-interfaces/`](../research/density-interfaces/README.md)
- Agent workflow: [`../AGENTS.md`](../AGENTS.md)
- Exact historical review and lifecycle evidence: [`../archive/README.md`](../archive/README.md)
