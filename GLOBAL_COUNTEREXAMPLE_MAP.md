# Global Collatz counterexample map

**Agent:** `gpt56-cartographer-01`  
**Issue:** [#36 — Global counterexample-result dependency map and atomic blocker lemma synthesis](https://github.com/gfreund123/collatz/issues/36)  
**Repository analyzed:** `gfreund123/collatz` (the connected private repository corresponding to the project named in the request)  
**Analysis mode:** dependency cartography only; no independent proof verification was attempted  
**Snapshot:** see [`ANALYSIS_SNAPSHOT.md`](ANALYSIS_SNAPSHOT.md)  
**Atomic handoff problems:** see [`ATOMIC_COUNTEREXAMPLE_LEMMAS.md`](ATOMIC_COUNTEREXAMPLE_LEMMAS.md)  
**Machine-readable overview:** [`docs/global-counterexample-map.mmd`](docs/global-counterexample-map.mmd)

## 1. Scope and status policy

This document answers one question only:

> How does every active result family connect—or fail to connect—to a full disproof of the ordinary positive-integer Collatz conjecture?

For the shortcut map

\[
T(n)=
\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2,
\end{cases}
\]

a full disproof has three logically complete forms:

1. an explicit positive nontrivial cycle;
2. an explicit positive orbit that never reaches \(1\), including an unbounded orbit;
3. a rigorously equivalent existence witness, such as a third functional-graph component.

The map deliberately distinguishes **mathematical confidence** from **distance to a counterexample**. A proved obstruction can be green while closing a construction route. A proposed construction can be orange while sitting one implication from a counterexample.

### Color legend

| Color | Meaning |
|---|---|
| Green | `PROVED` or `INDEPENDENTLY_VERIFIED` in the source currently inspected |
| Blue | source-inspected external literature input, with native hypotheses audited |
| Orange | native `PROPOSED` theorem or lemma |
| Yellow | exact finite computation / `EMPIRICAL` observation |
| Red | `REFUTED`, `SUPERSEDED`, withdrawn, or dependency-quarantined claim/route |
| Grey | open question, `IDEA`, or implication not yet supplied |

When sources disagree, this map uses the stricter or newer status and records the conflict. In particular, no theorem is promoted merely because another branch cites it confidently.

## 2. Executive diagnosis

There is no positive-integer counterexample, nontrivial positive cycle, regular sanctuary, infinite cap-stitch grammar, or equivalent third-component witness in the repository snapshot.

The project has nevertheless converged on a much sharper global structure.

### 2.1 The universal bottleneck is ordinary realization

Most constructive programs have already solved their finite arithmetic:

- every finite parity word has a unique residue class;
- many finite expanding schedules are exactly realizable;
- collision fibers have large branch count and complete finite projections;
- H itineraries, stack schedules, connector words, and cap prefixes can be compiled to arbitrary finite depth;
- real bounded-error paths or \(2\)-adic inverse-limit points are frequently unique.

But an infinite symbolic object gives a point of \(\mathbb Z_2\), not automatically an element of \(\mathbb Z_{>0}\). The common missing implication is

\[
\text{nested compatible cylinders}
\Longrightarrow
\text{eventual stabilization of canonical representatives}
\Longrightarrow
\text{one positive integer}.
\]

This is explicit in the proved classical realization layer (`L-9904`) and in the cross-direction stabilization lemma (`L-9801`, proposed). It reappears as:

- eventual zero appended blocks in the \(64\to81\) centered program;
- cap-to-correction equality after quotient extinction in PR #3/#33;
- eventual zero carry or positive ordinary ghost in the H program;
- finite digit support in the foundry;
- stabilization of least positive representatives in the conditioned \(3\)-adic program;
- low-digit survival in the \(5x+1\) control chart.

### 2.2 The repository is rich in filters and poor in integer-first generators

The strongest native results exclude periodic, automatic, finite-state, fixed-substitution, finite cyclic exponential-polynomial, fixed-prime, bounded-memory, and several padded or return architectures. Those filters substantially constrain a hypothetical witness.

Far fewer results start from one ordinary integer and preserve it by construction. The principal integer-first routes are:

- a finite positive cycle certificate;
- a finite regular-sanctuary certificate;
- a direct coverage deficit;
- a third component/ray with exact coefficient support.

These routes bypass the inverse-limit stabilization problem and deserve more attention than their present staffing suggests.

### 2.3 The most developed corrected-stage class is now proposed closed

In the corrected phase-\(-34\) collision lane, quotient extinction leaves a cap or co-cap equality at every sufficiently late scale. PR #3 and PR #34 then expose one real room, exact boundary floors, 84 canonical seams, nonautonomous carry, tiny completion height, and forced fresh primes.

During the cutoff pass, PR #33 advanced to proposed `T-9705`: a uniform exclusion of **every signed ordinary completion** of the frozen corrected 256-transition class. Its closing chain turns any hypothetical cap or co-cap path into infinitely many distinct primitive 258-coordinate zero sums with:

- 256 internal \(\{2,3\}\)-unit coordinates;
- no proper nonempty vanishing subsum;
- endpoint outside-prime height exponent below \(1/50\);
- a primitive gcd bounded by \(216\);
- projective distinctness forced by a growing \(2\)-adic valuation.

Evertse's 1984 finiteness theorem is then invoked to obtain a contradiction.

Accordingly, the current source-level standing is:

> **If proposed `T-9705` survives review, the entire frozen corrected 256-stage architecture cannot contain a positive ordinary initialization, regardless of seam choice or room prefix.**

The constructive collision program must therefore either identify a genuine gap in that theorem or change the stage architecture so that at least one closing hypothesis fails. Continuing a free word/seam search inside the frozen class is no longer on a live path to a counterexample.

### 2.4 A hypothetical witness must satisfy a three-way tension

The active filters jointly force a prospective constructive witness to be:

- **high information:** large factor complexity and no bounded-state description;
- **arithmetically renewing:** infinitely many fresh primes or unbounded state;
- **very low height:** canonical representatives live in exponentially thin cusps.

PR #33 now packages this tension into an almost-\(S\)-unit contradiction for the frozen 256-stage collision class. The remaining high-leverage opportunity is to determine how far that template generalizes—to variable-width collision architectures and to H—or, constructively, how an architecture can escape it without losing physical growth.

## 3. Full-conjecture overview

```mermaid
flowchart LR
    FALSE([Collatz is false])

    CYCLE([Positive nontrivial cycle])
    DIV([Positive orbit avoids 1])
    EQUIV([Equivalent third component / exact deficit])

    CYCLE --> FALSE
    DIV --> FALSE
    EQUIV --> FALSE

    subgraph FINITE["Integer-first finite certificates"]
      CYCEQ["Cycle equation + exact replay<br/>#9, L-9905"]
      M8{"m=8, K=13<br/>792 compositions"}
      SAN["Regular sanctuary DFA<br/>#10 / PR #12"]
      CYCEQ --> M8 --> CYCLE
      SAN --> DIV
    end

    subgraph ADDRESS["Address-first expanding constructions"]
      COLL["Collision / phase -34 towers<br/>PR #3"]
      EXT["Free quotient extinction<br/>T-0031 / T-9703"]
      CAP{"Cap or co-cap tail"}
      ROOM["One real room / 84 seams / fresh primes"]
      EXCL["T-9705: Evertse exclusion of all<br/>signed ordinary completions"]
      DEAD["Frozen corrected 256-stage class<br/>proposed closed"]
      ESC{"New architecture breaking a<br/>T-9705 hypothesis"}
      INIT{"Positive marked initialization"}
      COLL --> EXT --> CAP
      ROOM --> CAP
      CAP --> EXCL --> DEAD
      ESC --> INIT --> DIV

      M1["64 -> 81 centered/M1 attractor"]
      ZBLOCK{"Appended blocks eventually zero"}
      M1 --> ZBLOCK --> DIV

      HLANE["Partial H subsystem<br/>PR #19"]
      HINT{"Ordinary H seed / stabilized cylinders"}
      HLANE --> HINT --> DIV
    end

    subgraph GLOBAL["Equivalent full-map witnesses"]
      CONE["Third fixed-cone extreme ray<br/>#24"]
      COVER["Coverage deficit C(x) < x<br/>#25"]
      SPEC["Certified point spectrum with support extraction<br/>#27"]
      CONE --> EQUIV
      COVER --> EQUIV
      SPEC --> EQUIV
    end

    subgraph FILTERS["Powerful filters, not witnesses"]
      COMP["Complexity / recurrence floors"]
      PADE["p-adic irrationality: periods 1..9"]
      FSTATE["Finite-state / foundry collapse"]
      HEIGHT["Completion-height and packing obstructions"]
    end

    COMP -. constrains .-> M1
    PADE -. constrains .-> M1
    FSTATE -. constrains .-> SAN
    HEIGHT -. constrains .-> CAP

    classDef proved fill:#c8f7c5,stroke:#267326,color:#111;
    classDef literature fill:#cfe8ff,stroke:#2563a8,color:#111;
    classDef proposed fill:#ffd6a5,stroke:#b45309,color:#111;
    classDef empirical fill:#fff2a8,stroke:#9a7b00,color:#111;
    classDef refuted fill:#ffc7c7,stroke:#a11,color:#111;
    classDef open fill:#e5e7eb,stroke:#666,color:#111;

    class CYCEQ proved;
    class COLL,EXT,ROOM,EXCL,DEAD,M1,HLANE,COMP,PADE,HEIGHT proposed;
    class M8,CAP,ESC,INIT,ZBLOCK,HINT,SAN,CONE,COVER,SPEC,EQUIV,CYCLE,DIV,FALSE open;
```

The graph source with more status annotations is kept separately so it can be rendered or edited without changing this report.

## Detailed map files

- [`cartography/CONSTRUCTIVE_LANES.md`](cartography/CONSTRUCTIVE_LANES.md) — ordinary-realization funnel; cycle, collision, centered/M1, H, sanctuary, resonance, and foundry lanes.
- [`cartography/EQUIVALENT_AND_INDIRECT.md`](cartography/EQUIVALENT_AND_INDIRECT.md) — full-map equivalent witnesses, diagnostic programs, and cross-direction connections.
- [`cartography/CROSSWALK_AND_PRIORITIES.md`](cartography/CROSSWALK_AND_PRIORITIES.md) — repository-wide issue/PR crosswalk, quarantines, priorities, and update protocol.
- [`ATOMIC_COUNTEREXAMPLE_LEMMAS.md`](ATOMIC_COUNTEREXAMPLE_LEMMAS.md) — index of standalone blocker and construction atoms.
- [`ANALYSIS_SNAPSHOT.md`](ANALYSIS_SNAPSHOT.md) — exact commit/time cutoff.
- [`docs/global-counterexample-map.mmd`](docs/global-counterexample-map.mmd) and [`docs/global-counterexample-map.dot`](docs/global-counterexample-map.dot) — editable diagram sources.

## Bottom line

The repository has not produced a counterexample. Its most general repeated bottleneck is the passage from arbitrarily deep finite compatibility to one ordinary positive integer. At the cutoff, PR #33 newly proposed a class-wide almost-\(S\)-unit exclusion for the frozen corrected 256-stage collision architecture, so that class is mapped as proposed closed. The shortest remaining full-disproof paths are a finite positive cycle, a finite regular sanctuary, a native centered/M1 survivor, a positive H survivor, an exact third component/ray, or a rigorous coverage deficit.
