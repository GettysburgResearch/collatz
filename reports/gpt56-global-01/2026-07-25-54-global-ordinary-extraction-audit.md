# Global ordinary-extraction audit

**Agent:** `gpt56-global-01`  
**Reviewer/model identity:** OpenAI `GPT-5.6 Pro`  
**Issue:** #54  
**Branch:** `agent/gpt56-global-01/54-ordinary-extraction-audit`  
**Date:** 2026-07-25  
**Role:** global reconstruction and blocker audit; no bounded search or new encoding

## Frozen source heads

```text
main:                         b40e5c44959b20842e6c064084c668f5243b6ebd
cartography PR #38 pass 5:    f49501b7ec0f79b83890f1485180141c51cc8206
frozen corrected-stage PR #33:c9d62bce3e93f5785f72e4520bc576863d9379eb
H frontier PR #19:            e805dde4275daaef78ad74dbf1e469710481958e
fixed chart / cycle PR #45:   a7846473b10aa5caf8c9c57b0a612db0b8db402a
intrinsic refund PR #49:      cb0401d19e69f531d32ede58a158a80cc9872d7c
cycle height-gate PR #50:     1cba8c76a3b20eeafdfa6941c9847b77105e6ae4
run-core PR #51:              bf00552e5054fd8e5d1692648911b377c5624e56
fixed-pulse-cone PR #53:      cd6cf9ca76fb028966b4a638d9fb19fd8934849f
```

## Starting question

Is the repository making genuine progress toward a Collatz counterexample, or repeatedly relocating the full conjectural obstruction into new coordinates?

The pass deliberately refused to add:

- another finite-prefix search;
- another conditional growth theorem;
- another symbolic encoding of the same inverse limit;
- another proper-factor or near-integer cycle experiment.

The only accepted targets were:

1. ordinary-integer extraction from an infinite legal path;
2. universal elimination of a whole architecture;
3. full-denominator finite cycle closure.

## Main finding

The positive-orbit programs repeatedly reach the same exact logical boundary:

```text
every finite depth has positive ordinary representatives;
the residue classes are compatible;
one inverse-limit point exists;
any ordinary infinite survivor would grow or diverge;

missing:
one finite ordinary integer belongs to every depth.
```

The missing inference is not compactness. Compactness produces an inverse-limit point, usually in `Z_2`. Ordinary extraction is the assertion that its canonical representatives remain bounded.

## New theorem `T-7801`

For a nested chain

```text
R_N mod M_N,
M_N | M_(N+1),
M_N -> infinity,
0 <= R_N < M_N,
```

the following are equivalent:

```text
one nonnegative ordinary integer realizes every level;
R_N is eventually constant;
R_N is bounded;
liminf R_N is finite;
the appended mixed-radix digits are eventually zero.
```

For a whole deterministic architecture, let `S_N` be the positive integers surviving `N` exact blocks and let

```text
m_N=min S_N.
```

Then

```text
one ordinary infinite survivor exists
  <=> (m_N) is bounded
  <=> (m_N) is eventually constant.
```

Otherwise `m_N->infinity` and the architecture is empty in ordinary positive integers.

This gives a complete, architecture-specific decision criterion. It is genuinely weaker than Collatz because each architecture is a strict prescribed subsystem.

## New refutation `R-7801`

I then tested whether the common refund machinery could supply the missing bound abstractly.

It cannot.

For any nested dyadic residue chain selecting a nonordinary `2`-adic point and any prescribed expansion factors `Lambda_n`, `R-7801` constructs exact maps

```text
F_n(x)=(A_n*x+b_n)/q_n,
A_n odd,
q_n a power of two,
0 <= b_n < q_n,
A_n/q_n > Lambda_n,
```

such that:

```text
the first N steps are integral iff x_0=R_N mod M_N;
every finite prefix has infinitely many positive ordinary starts;
every legal step is positive and expands by more than Lambda_n;
the expansion factors may grow arbitrarily fast;
no ordinary integer follows every step.
```

The construction is exact congruence algebra. No computation or asymptotic heuristic is used.

This proves that there is no universal theorem of the form

```text
finite compatibility + exact affine replay + large refund/growth
  -> ordinary extraction.
```

Architecture-specific information beyond the common affine/cylinder/refund skeleton is mandatory.

## Architecture audit

### PR #45 fixed six-branch chart

The branch has an exact intrinsic state, exact physical blocks, and a conditional theorem that one forever-defined state is an unbounded Collatz orbit. It also excludes several low-description top boundaries.

It does not prove the least positive depth-`N` root is bounded or divergent. The requested existence lemma is exactly the architecture's whole survivor-existence problem.

**Assessment:** legitimate strict-subsystem reduction; no positive extraction progress yet.

### PR #51 negative-three run core

The run-core map, run-five criterion, block-average growth criterion, divisible-seven core, and several schedule exclusions are genuine. The affine schedule `r_n=64+n` was later closed negatively.

Every finite run prefix still has positive ordinary representatives without one common ordinary root. No theorem controls the least initial core for all depths.

**Assessment:** genuine family exclusions and useful exact dynamics; global ordinary existence unresolved.

### PR #49 intrinsic changing-height refund

The branch supplies the strongest local refund mechanism: exact intrinsic core, exact source blocks, common top modulus, conditional permanent refund, rapid growth, complexity, and prime-renewal constraints.

None of those statements bounds the least initial core. The source's plain generated-stack interpretation also received a transported-coordinate correction on review PR #48; regardless of representation, generated capacity does not establish legal content.

**Assessment:** substantial conditional structure, but the remaining entry/routing statement is still the full survivor-existence question for the subsystem.

### PR #19 H frontier

The branch itself states the correct direct target: prove the centered least root `nu_K` tends to infinity, or extract a stabilized positive root. Every finite itinerary is realizable, and extensive structure constrains any survivor.

**Assessment:** one of the clearest global reductions; current finite bounds and structured exclusions do not decide the asymptotic.

### PR #16 centered ordinary section

The nearest-integer cylinder and appended-block formulations isolate ordinary stabilization exactly. The depth-46 minimum is a strong exact finite datum, and broad symbolic classes are excluded.

The remaining theorem is still that the least-room minima tend to infinity or stabilize.

**Assessment:** genuine canonical Level-III reduction; no class decision.

### PR #33 corrected frozen stage class

The branch proves that every physically overlapping infinite directive in its frozen architecture has a nonordinary completion. This chain was independently reconstructed in the earlier review wave.

**Assessment:** genuine universal class elimination. This is not treading water.

### PR #53 fixed pulse cones

The proposed resultant theorem caps every coordinate in each fixed baseline/repetition pulse cone, reducing it to a finite decision.

It does not control changing repetitions or arbitrary baselines.

**Assessment:** genuine fixed-class narrowing, subject to independent reconstruction; not a global cycle result.

### PR #50 mixed-place cycle closure

This is the clearest global cycle reduction. If the real interval, dyadic replay depth, and odd-prime divisibility jointly exceed the exact height of a nonzero remainder, then the remainder vanishes and the full cycle equality follows.

The current critical construction is extremely far from the required height budget, and a former target was rejected at the first physical domain.

**Assessment:** genuine finite certificate mechanism; present near-hits are not close in the load-bearing metric.

## Blunt overall verdict

The answer is mixed.

### What is genuinely real

- complete infinite classes have been excluded;
- major theorem chains have survived independent reconstruction;
- false claims and invalid bridges have been found and repaired;
- exact finite certificate and mixed-height machinery has improved;
- several structured schedule, support, and pulse families have been closed.

### What has not happened

No positive architecture has yet proved one ordinary root survives forever. The sequence of intrinsic cores, quotients, carries, run schedules, and generated stacks has repeatedly changed the representation of the same missing ordinary-integer assertion.

Thus:

```text
negative/exclusion program:
  genuine progress;

positive-existence program:
  mostly improved reformulation and conditional infrastructure,
  not yet a reduction of the decisive ordinary-extraction theorem.
```

It would be misleading to call the whole project circular. It would also be misleading to claim that the positive construction program is now close merely because growth is automatic after existence.

## Why the least-root target is weaker than Collatz

For one architecture `A`, proving

```text
m_N(A) bounded
```

constructs a counterexample in that architecture. Proving

```text
m_N(A)->infinity
```

eliminates only that architecture.

Neither result decides arbitrary Collatz trajectories. The same applies to the finite union of the four current refund machines.

Therefore the target is exact, global, and materially weaker than Collatz while still decisive for the current program.

## Cycle-side exact inference

The cycle analogue is:

```text
many factors divide C
+ C/D near an integer
-/-> D divides C.
```

The missing exact inference is a height contradiction for

```text
R=C-ND.
```

A successful cycle result must either prove `R=0` directly or show that a nonzero `R` is divisible by more than its size permits. Proper-factor progress should be measured by its contribution to that exact budget.

## Recommended next actions

1. Stop opening new ordinary encodings unless they prove a statement about `m_N`.
2. Choose the smallest fixed chart and attack its least-root sequence directly.
3. Build an exact cross-architecture least-root ledger only if it is used to prove boundedness or divergence, not as another depth record.
4. On the cycle side, report every result in units of the mixed-place height deficit.
5. Preserve conditional growth, fresh-prime, entropy, and compiler results as infrastructure, but do not summarize them as ordinary existence progress.
6. Treat `Q-7801` as the common positive/negative decision atom.

## Candidate counterexamples

None.

## Files changed

```text
research/global-extraction/README.md
research/global-extraction/CLAIM_INVENTORY.md
research/global-extraction/GLOBAL_BLOCKER_MATRIX.md
research/global-extraction/claims/D-7801-survivor-towers.md
research/global-extraction/claims/T-7801-ordinary-extraction-dichotomy.md
research/global-extraction/claims/R-7801-expanding-affine-compactness-countermodel.md
research/global-extraction/claims/M-7801-global-progress-classification.md
research/global-extraction/claims/Q-7801-least-root-decision.md
reports/gpt56-global-01/2026-07-25-54-global-ordinary-extraction-audit.md
```

## Verification and limitations

- The two new mathematical proofs use elementary exact integer and congruence arguments.
- No repository code or finite experiment is load-bearing.
- The audit does not independently re-review every source theorem in every branch; it freezes their native and reviewed statuses.
- `R-7801` does not prove that a particular Collatz architecture is empty. It proves that their shared local skeleton cannot yield extraction.
- The actual least-root asymptotic remains open for the live positive architectures.
- No merge is performed by this agent.