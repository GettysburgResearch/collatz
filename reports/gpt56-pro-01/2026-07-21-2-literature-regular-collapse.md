# Session report — literature-informed regular-collapse boundary

Agent: `gpt56-pro-01`  
Issue: `#2`  
Branch: `agent/gpt56-pro-01/2-collision-rewrite-bootstrap`  
Date: 2026-07-21  
External branch inspected: `agent/gpt56-pro-03/4-literature-audit` / PR #13

## Starting task

Inspect the literature-review branch before continuing the marked interval and
ordered-particle route. Determine which external results and neighboring tools
materially change the research strategy, then make a theorem-level contribution
and push it.

## Literature and tool review

The review focused on:

- `LITERATURE.md`;
- `literature/LIVE_REPO_REVIEW_WAVE2.md`;
- `literature/claim-maps/PR3-WAVE2.md`;
- imported theorems `LIT-KTHM-0016`–`0018`, `0019`–`0022`,
  `0026`, and `0027`;
- topic notes on rational-base returns and regular sanctuaries;
- PR #12's exact regular-sanctuary semantics and verifier architecture.

### Most important findings

1. **Graph expansion is standard infrastructure.** Positive cycle-mean
   potentials and phase weights should no longer consume primary research
   effort. The arithmetic selector, forward-invariant survivor, ordinary
   quotient, and exact replay remain native.
2. **Compact graph-directed attractors do not solve the ordinary boundary.**
   They construct completion points, possibly all nonordinary.
3. **Regular images and fixed-language closure are exact and effective.**
   Subsequential/rational transductions preserve regularity; closure of one DFA
   is finite product reachability; fixed skeletons have greatest safe kernels.
4. **PR #12 is already the exact laboratory for regular sanctuaries.**
   Its canonical finite-word semantics, terminal carry flushes, short witnesses,
   and safety kernel are directly relevant to the marked-spine route.
5. **The common frontier is ordinary realization.** Every branch can build
   finite objects or compatible completion paths; none may substitute those for
   one finite positive integer.

## New conceptual result

The finite interval and particle constructions suggested a large class of
finite-state decorated grammars. The literature review exposed that this class
can be compiled away.

### L-0015 — regular interval and marker projection

A regular language of synchronous finite endpoint pairs has an effectively
regular language of physical differences \(q-v\). The proof uses the two-state
binary addition relation

\[
v_i+n_i+c_i=q_i+2c_{i+1},
\]

projection, right quotient by high zero padding, and canonical intersection.

Fixed and diagonal interval gauges preserve regularity. Regular finite
population/marker languages have regular marked-rank projections.

### T-0020 — finite-phase regular block collapse

For finitely many regular phase languages and finitely many fixed Collatz block
edges

\[
T^{b_e}(D_e)\subseteq L_{\tau(e)},
\]

the finite union of all intermediate images

\[
K=\bigcup_e\bigcup_{0\le k<b_e}T^k(D_e)
\]

is a one-step regular sanctuary whenever the phase system is nonempty and
avoids `1,2`.

Conversely every regular sanctuary is a one-phase instance.

The marked-configuration corollary states that a finite-phase regular marked
interval or particle grammar, with rational marker extraction and exact marker
replay, compiles to the same class.

## Strategic correction

The preceding session ended with a broad search target:

> construct a finite-state, substitutional, or pushdown marked-particle grammar.

The literature-informed theorem narrows it:

- a **regular finite-state** marked grammar is not a new route; it belongs to
  PR #12;
- a fixed finite phase graph and fixed macro-blocks also do not enlarge the
  existential class;
- the new route begins only with an unbounded counter/stack, variable block
  lengths, or a genuinely nonregular ordinary survivor.

This is a useful negative result because it prevents duplicate search under
interval, particle, carry, and phase notation.

## Exact experiment

`X-0011` implements a compact independent bridge:

- endpoint-pair DFAs;
- exact difference projection with one carry bit;
- high-zero removal by right quotient;
- canonical determinization;
- exact shortcut transducer;
- closure witnesses;
- maximal safe-state kernels.

It verifies random finite endpoint languages, multiple gauges, the infinite
fixed-gauge all-positive control, exact closure, safe-kernel emptiness in the
semantic sense, and fixed-block normalization.

Validation:

```bash
python3 -m py_compile experiments/X-0011-regular-marked-collapse/run.py
python3 experiments/X-0011-regular-marked-collapse/run.py
```

Expected final line:

```text
all regular-marked-collapse checks passed
```

## Candidate counterexamples

None.

No regular sanctuary, counter-stack sanctuary, divergent seed, nontrivial
positive cycle, or `K-####` candidate is claimed.

## Failed or superseded routes

1. **Treating finite endpoint decoration as extra computational power.**
   Superseded by `L-0015`: regular endpoint languages project to regular marker
   languages.
2. **Treating finite phase graphs of fixed macro-blocks as beyond one-step
   regular closure.** Superseded by `T-0020`.
3. **Using graph attractor existence as ordinary realization.** Explicitly
   rejected by `LIT-KTHM-0027`.
4. **Continuing to optimize graph potentials.** Standard infrastructure; the
   selector and ordinary witness are the native bottleneck.
5. **Duplicating PR #12's broad regular search.** The correct action is
   interoperability and reuse.

## Files added

- `claims/lemmas/L-0015-regular-interval-projection.md`
- `claims/theorems/T-0020-regular-marked-grammar-collapse.md`
- `experiments/X-0011-regular-marked-collapse/README.md`
- `experiments/X-0011-regular-marked-collapse/run.py`
- `experiments/X-0011-regular-marked-collapse/results/summary.txt`
- this report

## Integrated files updated

- `CLAIMS.md`
- `CURRENT_STATE.md`
- `OPEN_PROBLEMS.md`
- `NEGATIVE_RESULTS.md`
- `CANDIDATES.md`
- PR #3 description
- issue #2 handoff

## Recommended next attack

Use the negative eleven-cycle padding counter as the first genuinely unbounded
memory component.

The target certificate should have states

\[
(i,t,\rho,\text{marker}),
\]

where:

- \(i\) is a finite negative phase;
- \(t\ge0\) is a unary cycle-padding counter;
- \(\rho\) is a finite low-order residue obligation;
- the marker is one ordinary finite particle.

A transition must prove

\[
(i,t,\rho,n)
\longmapsto
(j,t+\Delta_e,\rho',T^{b_e(t)}(n))
\]

with:

1. exact cylinder selection;
2. counter nonnegativity;
3. closure of the residue obligation;
4. positive cycle growth above a proved threshold;
5. one explicit finite initial marked state.

This is not reducible to a regular sanctuary because the block length and
accepted low-order obligations depend on an unbounded counter.

## Organizational note

No README change is proposed. PR #13's imported-theorem namespace and
source/native/analogy separation are useful and should be preserved when that
branch is integrated.
