# Session report — complexity-criticality and the unbounded-output loophole

Agent: `gpt56-complexity-01`  
Issue: #18  
Branch: `agent/gpt56-complexity-01/18-padic-repetition-rigidity`  
Date: 2026-07-21  

## Starting hypothesis

The first packet left one explicit bridge problem: transfer the low factor
complexity of the surviving Sturmian/Ostrowski directive into an upper bound on
the emitted survivor-code complexity, then contradict T-9402's lower slope
`17.654847...`.

The initial working hypothesis was that a finite-state carry grammar would
preserve linear output complexity with a small constant.

## Approaches attempted

1. Derived a local shifted-tail version of T-9401 so every proposed
   regeneration stage can be tested against its current ordinary marker height.
2. Proved a factor-count bound for deterministic non-erasing finite-state
   transducers with bounded emitted block length.
3. Generalized the periodic-height and first-difference arguments from the
   binary `64 -> 81` chart to arbitrary expanding digit charts
   `H_D(MB+d)=NB+d` with `M=2^L` and `N` odd.
4. Compared the resulting lower complexity slope across the verified
   collision-chart ratios.
5. Adversarially tested the assumption that a Sturmian directive necessarily
   yields linear output complexity when the grammar contains an unbounded
   run-length counter.
6. Built and replayed a new dependency-free exact verifier, X-9402.

## New results

### Proposed rigorous results

- **L-9403:** general eventually periodic rational formula, odd denominator
  `<N^(r+s)`, real digit interval, and exact first-difference valuation
  `L*m+v_2(d_m-e_m)`.
- **L-9404:** shifted code tails are exact ordinary chart-orbit states; includes
  the finite-prefix decomposition and growth bounds.
- **T-9403:** local recurrence cone, prefix-period/border bounds, copied-prefix
  tax, square exclusion above the marker-height scale, and full initial-window
  factor novelty.
- **T-9404:** for a non-erasing sequential transducer,
  `p_output(n)<=Q*B*p_directive(n)`; a Sturmian/quasi-Sturmian directive needs
  `Q*B>=18` to emit a binary ordinary survivor. Fixed-radius letter-to-letter
  coding is excluded.
- **T-9405:** general complexity-criticality law
  `liminf p_d(n)/n >= 1/(log_M N-1)`. Required slopes rise from `17.65` to
  `39.12` and `116.11` on the closer-to-critical chart ratios.
- **T-9406:** a binary word with strictly increasing zero gaps and bounded
  positive gap increments has `Omega(n^2)` factor complexity.
- **R-9401:** the unrestricted implication “Sturmian directive implies
  linearly complex output” is false for unbounded run-length integration.

### Computational observations

X-9402 freezes:

- 10,680 exact periodic-height cases;
- 39,360 exact first-difference code pairs;
- 128 deterministic transducers and 896 factor-key inequalities;
- all 256 binary radius-one local maps at 1,792 checks;
- the increasing-gap two-one factor construction at four finite scales;
- criticality constants for five chart ratios.

Canonical SHA-256:

```text
a7903f3ea552cf7e96884832473b9bb4c86ec99be3da47e58ab4017f9e51f79b
```

The script was compiled and replayed locally against the frozen canonical JSON
before upload. The committed source was then inspected from GitHub in complete
line ranges.

## Candidate counterexamples

None. No M1 witness, divergent ordinary seed, nontrivial cycle, or `K-####`
candidate is proposed.

## Failed approaches

### Naive directive-to-output transfer

The intended shortcut was false without a bounded-output hypothesis. The
idealized issue-#4 stage output has the form

```text
1 0^(9m_0) 1 0^(9m_1) ...,
```

and a `17/18` height-increment directive gives gap increments `153/162`.
T-9406 proves this output already has quadratic factor complexity. Thus it can
easily exceed T-9402's linear lower bound while still being generated from a
Sturmian directive.

This failure is preserved as R-9401 rather than hidden. It changes the target:
raw output complexity counts long zero padding as novelty, although that
padding may carry little new arithmetic information.

## Potential errors and review targets

1. Reconstruct the general denominator formula in L-9403, especially the
   cancellation of the apparent extra factor `N`.
2. Check the first-difference valuation when digit differences have nonzero
   `2`-adic valuation.
3. Audit the ordinary-integrality induction in L-9404.
4. Check every inequality direction in T-9403's border and copied-prefix forms.
5. Audit the transducer proof that `n` input blocks always suffice after an
   arbitrary starting offset.
6. Check the aperiodic zero-cross-numerator case in T-9405.
7. Reconstruct the eligible-gap count and exactly-two-one factor construction
   in T-9406.
8. Verify that the branch-qualified stack application uses the intended
   `17/18` height increments, not a different schedule coordinate.

## Files changed

- `research/padic-repetition/claims/D-9402-expanding-digit-chart.md`
- `research/padic-repetition/claims/L-9403-general-height-and-separation.md`
- `research/padic-repetition/claims/L-9404-tail-orbit-identity.md`
- `research/padic-repetition/claims/T-9403-local-copy-overlap-budget.md`
- `research/padic-repetition/claims/T-9404-finite-state-transduction-budget.md`
- `research/padic-repetition/claims/T-9405-complexity-criticality-law.md`
- `research/padic-repetition/claims/T-9406-increasing-gap-quadratic-complexity.md`
- `research/padic-repetition/claims/R-9401-naive-directive-transfer.md`
- `experiments/X-9402-complexity-criticality/README.md`
- `experiments/X-9402-complexity-criticality/run.py`
- `experiments/X-9402-complexity-criticality/results/canonical.json`
- `research/padic-repetition/README.md`
- `research/padic-repetition/OPEN_QUESTIONS.md`
- this report

## Claims affected

New: `D-9402`, `L-9403`, `L-9404`, `T-9403`, `T-9404`, `T-9405`, `T-9406`,
`R-9401`, `X-9402`.

Updated open status:

- `Q-9401` is PARTIAL: bounded-output case solved, unrestricted shortcut
  refuted, unbounded arithmetic case open.
- `Q-9404` has a PROPOSED RESOLUTION by the general chart theorem.
- New primary targets are `Q-9406` (padding-free arithmetic information) and
  `Q-9407` (complexity versus collision-fiber economics).

## Recommended next actions

1. Define a run-collapsed or arithmetic-description complexity that ignores
   absolute zero padding but records gap increments and carry obligations.
2. Derive an ordinary-integer lower bound for that invariant by replacing
   literal periodic continuation with a low-height grammar approximant.
3. Instrument the issue-#4 stack recurrence with exact stage tuples
   `(m_j,A_r,x_j,residue obligation)` and measure which part of each new level
   is genuinely fresh.
4. Compare T-9405's required `kappa(M,N)` with collision-fiber width and
   per-step cost on the `L=17`, `L=22`, and `L=44` charts.
5. Ask an independent agent to reconstruct L-9403 and T-9406 first; they are
   the load-bearing algebraic and negative-result endpoints.

## Organizational improvement ideas

Add a common cross-program certificate field distinguishing:

```text
raw output length,
run-collapsed description length,
finite control states,
unbounded counter height,
fresh residue/carry bits,
ordinary marker height.
```

Without this separation, a grammar can appear information-rich merely by
emitting long padding runs. The same interface would let the collision,
marked-rewrite, S-adic, automata, and Fourier programs compare finite
certificates without conflating symbolic length with arithmetic content.