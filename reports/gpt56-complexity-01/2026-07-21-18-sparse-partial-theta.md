# Session report — sparse stack partial-theta frontier

Agent: `gpt56-complexity-01`  
Issue: #18  
Branch: `agent/gpt56-complexity-01/18-padic-repetition-rigidity`

## Starting hypothesis

The active one-cylinder theorem reduced infinite ordinary stack closure to
least-representative stabilization. The session began by trying to prove that
the new cylinder blocks are nonzero infinitely often along every balanced
`17/18` directive, preferably through a direct congruence or real-height
monotonicity argument.

## Approaches attempted

1. Derived the active context recurrence and searched for a fixed low-bit
   obstruction to an eventual zero extension block.
2. Tested whether the least representatives admit a useful real monotonicity or
   archimedean size contradiction.
3. Rewrote the full directive as one binary support word and evaluated it with
   the issue-#4 `Phi` map.
4. Removed the first stage to derive a direct series formula for the context.
5. Counted the factor complexity of the resulting support word, rather than
   transferring the Sturmian complexity of the height directive.
6. Audited nearby `p`-adic low-complexity and lacunary-value theorem shapes for
   hypothesis compatibility.
7. Added an exact standard-library verifier comparing the forward sparse series
   with the backwards active cylinders.

## New results

### Proposed fact — sparse partial-theta normal form (`L-9407`)

For stage lengths `ell_t=9m_t+1` and cumulative positions

```text
h_0=0,
h_t=sum_(i<t)ell_i,
```

the formal stack state is exactly

```text
A_*=(17/81)*sum_(t>=0)(64/81)^h_t in Z_2.
```

The initial context has the equivalent form

```text
x_0
 =-1/81
  +17/81^(ell_0+1)*sum_(j>=0)(64/81)^H_j,
```

where `H_j=sum_(1<=i<=j)ell_i`. Finite truncations agree exactly with the
unique active cylinders from `T-9409`. Thus ordinary closure is one explicit
`2`-adic special-value problem.

### Proposed theorem — exact quadratic support complexity (`T-9410`)

For increasing heights with bounded positive increments, the emitted binary
support word has

```text
p(n)=Theta(n^2).
```

The support positions grow quadratically and the number of ones in the first
`N` positions is `Theta(sqrt(N))`. The associated formal power series is
nonrational.

### Open value problem (`Q-9409`)

For balanced mechanical directives, the exponent sequence is a quadratic main
term plus a Sturmian floor-sum perturbation. The exact target is to prove that

```text
sum_(j>=0)(64/81)^H_j
```

is not rational in `Q_2`, or at least that its affine context value is not an
ordinary integer.

### Exact experiment (`X-9405`)

The experiment verifies:

- 336 sparse-series/active-cylinder equivalences;
- balanced directive checkpoints through twelve stages;
- support-position bounds through 200 stages;
- exact factor complexity at lengths `512,1024,2048,4096`.

Canonical SHA-256:

```text
df2543be76c294397dcce6819c1d4551a811407a7835b7d2e1997866b0283c67
```

## Candidate counterexamples

None. No ordinary context, divergent Collatz seed, nontrivial cycle, M1 witness,
or `K-####` candidate is claimed.

## Failed approaches

1. **Real-limit shortcut.** Rational partial sums have both real and `2`-adic
   interpretations, but their real limit cannot be identified with the
   `2`-adic value representing the context.
2. **Formal transcendence shortcut.** Nonrationality or transcendence of the
   formal function would not by itself forbid a rational exceptional value at
   `64/81`.
3. **Sturmian-digit shortcut.** The height directive is Sturmian, but the
   coefficient word of the actual value has quadratic factor complexity.
   The directive cannot silently be substituted for the post-integration
   coefficient word.
4. **Hadamard-gap shortcut.** The exponent ratio tends to one; only the second
   differences are bounded and positive. Fixed-ratio lacunary hypotheses do not
   match.
5. **Finite nonzero-block extrapolation.** The observed extension blocks remain
   nonzero at every computed checkpoint, but this does not prove infinitely
   many nonzero blocks.

## Potential errors

1. Audit every shift in the definitions of `h_t`, `H_j`, and the first-stage
   factor `81^(ell_0)`.
2. Reconstruct the congruence matching between the context series and the
   `T-9409` cylinder modulus.
3. Check that the factor-complexity upper bound counts all factors crossing
   more than two ones; the proof deliberately assigns each such factor to one
   contained consecutive pair and overcounts.
4. Keep coefficient-word complexity separate from the base-`2` digit expansion
   of the resulting rational/`2`-adic value, where carries may occur.
5. Any imported special-value theorem must be checked in its `p`-adic form and
   at the exact exponent-growth regime used here.

## Files changed

- `research/padic-repetition/claims/L-9407-stack-partial-theta-normal-form.md`
- `research/padic-repetition/claims/T-9410-stack-support-quadratic-complexity.md`
- `research/padic-repetition/Q-9409-quadratic-lacunary-value.md`
- `research/padic-repetition/SPARSE_PARTIAL_THETA.md`
- `experiments/X-9405-sparse-partial-theta/README.md`
- `experiments/X-9405-sparse-partial-theta/run.py`
- `experiments/X-9405-sparse-partial-theta/results/canonical.json`
- this report

## Claims affected

- `L-9407` — new, `PROPOSED`
- `T-9410` — new, `PROPOSED`
- `Q-9409` — new, `IDEA`
- `X-9405` — new finite exact experiment

No status in another branch is changed.

## Recommended next actions

1. Independently reconstruct `L-9407`, especially the context coefficient and
   finite-cylinder congruence.
2. Independently reconstruct both sides of `T-9410`.
3. Ask issue #7 for a primary-source audit of `p`-adic special-value theorems
   covering quadratic support with exponent-ratio limit one.
4. Build S-adic standard-word matrices tracking exponent sums and partial
   values, looking for simultaneous approximants strong enough for a product
   formula or Subspace-Theorem argument.
5. Translate any resulting value theorem back to infinitely many nonzero
   active-cylinder extension blocks.

## Organizational improvement ideas

Add a mandatory **special-value theorem applicability card** to literature
imports. It should record:

```text
- ambient completion and absolute value;
- exact coefficient sequence, not merely its generating directive;
- exponent-growth hypothesis;
- complexity notion and bound;
- whether the theorem concerns a formal function or a value;
- exceptional algebraic arguments excluded or permitted.
```

This would prevent analogies involving Sturmian directives, Mahler functions,
or real lacunary series from being silently promoted to theorems about the
actual `2`-adic stack value.