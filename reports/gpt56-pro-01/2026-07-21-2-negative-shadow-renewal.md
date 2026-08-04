# Session report — negative shadows, rational-base returns, and renewal codes

Agent: `gpt56-pro-01`  
Issue: `#2`  
Branch: `agent/gpt56-pro-01/2-collision-rewrite-bootstrap`  
Date: 2026-07-21  
Starting hypothesis: The complete-dyadic-projection result was still phrased as local digit correction. The next advance should identify the invariant global object on which collision charts, negative cycles, real boundary growth, and finite rewrite grammars are different views of one mechanism.

## Approaches attempted

### 1. Reparameterizing the induced map

The session rewrote a chart boundary in the quotient coordinate hidden inside `T-0002`. This removed the nonnegative digit gauge and the separate lifting congruence.

### 2. Evaluating the chart at quotient `-1`

The affine collision identity remains valid on the entire residue class modulo `2^L`, including negative integers. Substituting one negative quotient showed that every branch is an affine shadow of a negative integer template.

### 3. Variable-length return systems

Instead of requiring one fixed chart, the session allowed any finite negative orbit segment returning to one target. This produced a renewal-code formulation with variable lengths and odd counts.

### 4. Topological audit of finite complete return tables

A finite union of dyadic cylinders covering all sufficiently large ordinary integers is clopen and dense, hence covers the entire 2-adic space. The target quotient itself then forces an all-even contracting return. This gave a precise reason a finite one-target all-supercritical return table cannot work.

### 5. Real-window audit

The signed rational-base recurrence was summed in the real topology. This exposed the intrinsic normalized aspect ratio

```text
diameter(alphabet) / (output radix - input radix).
```

A long common odd tail was then found to impose an exact exponential tax on this ratio.

## New results

### T-0008 — Negative-shadow/rational-base conjugacy

Every chart

```text
T^L(2^L Q + r_i) = 3^a Q + s
```

is equivalent to negative coalescence

```text
T^L(-u_i) = -v,
u_i = 2^L-r_i,
v = 3^a-s.
```

At positive chart boundaries `n(q)=3^a q-v`, the quotient return equation is

```text
3^a q_t = 2^L q_(t+1) + a_t,
a_t in {v-u_i}.
```

The former lifting congruence is absorbed into this integral signed rational-base equation.

### T-0009 — Renewal-code criterion and obstruction

A negative return template gives an exact variable-length map

```text
F_i(q) = 3^(a_i) * (q-v+u_i) / 2^(L_i).
```

A forward-invariant set on which selected return maps are defined and strictly increasing gives a positive Collatz counterexample.

However, a finite one-target return family covering every sufficiently large quotient must contain an all-even branch

```text
u_i = 2^(L_i) v,
a_i = 0,
```

which is subcritical. Therefore an all-expanding construction must use an infinite but finitely generated renewal language, a proper invariant survivor set, several targets/charts, or compensated subcritical branches.

### T-0010 — Fractional-window/aspect-ratio theorem

For every infinite signed return chain,

```text
q_t = C (N/M)^t + x_t,
x_t = (1/N) sum_{j>=0} a_(t+j) (M/N)^j.
```

The error `x_t` lies in the convex hull of the normalized signed alphabet `A/(N-M)`. Hence

```text
fractional_part(C (N/M)^t)
```

is trapped forever in a fixed circle arc of length at most

```text
delta = diameter(A)/(N-M) = diameter(D)/(N-M).
```

This defines the chart's normalized aspect ratio.

### L-0011 — Odd-tail aspect-ratio tax

For a core of length `L`, residue span `W`, and a common odd tail of length `k`,

```text
delta_k
 = (W / 2^L) / (2^k * (lambda_k-1)).
```

If the final expansion margin is at least `epsilon`, then

```text
delta_k < 2^(-k) / epsilon.
```

Thus branching and tail drift are algebraically separable but not geometrically independent for vertical closure.

### O-0006 — Aspect audit

Exact aspect ratios of the principal charts are:

```text
O-0001  1/17                         ~= 5.882e-2
O-0002  2/217                        ~= 9.217e-3
O-0003  5/46075                      ~= 1.085e-4
O-0004  94/588665                    ~= 1.597e-4
O-0005  17207/5284606410545          ~= 3.256e-9
```

The 339-branch chart is symbolically rich but has a microscopic stationary real window.

The complete-dyadic-projection family collapses still faster, reaching aspect ratio about `4.72e-264` already at `b=5`.

### X-0006 — Exact checks

The standard-library script verifies:

- negative shadowing for every branch of `O-0001` through `O-0005`;
- all 339 committed `O-0005` offsets;
- one exact three-block signed rational-base address;
- the finite address-polynomial identity;
- the elementary `-1` return table and its forced contracting branch;
- the tail aspect identity for the `T-0007` examples with `1 <= b <= 5`.

Local execution reproduced all committed summary lines.

## Candidate counterexamples

None.

The session supplies a new candidate **format**: a regular infinite negative-template renewal code, or a finite multi-target return graph, together with a positive invariant quotient set and a complete growth proof.

## Failed or blocked approaches

1. **Treating complete dyadic projection as nearly sufficient.** The real-window audit shows that the long correction and drift tails can make the stationary chart extraordinarily narrow after normalization.
2. **A finite all-supercritical complete return table around one target.** `T-0009` proves this is impossible: the 2-adic all-even boundary point forces a contracting branch.
3. **Optimizing branch count alone.** The new aspect ratio is independent information and can move in the opposite direction.
4. **Assuming the negative template itself is a counterexample.** Negative templates are finite return devices; the positive quotient chain remains the required infinite object.

## Potential errors audited

- The affine identity was extended to negative quotients only after checking that the first `L` parities depend solely on the residue modulo `2^L`.
- Strict negativity is preserved by the shortcut map, proving `v=3^a-s>0` rather than assuming it.
- The rational-base digit alphabet differs by one radix-gap translation from the earlier `D-h` gauge; the two formulations were reconciled explicitly.
- The finite-code obstruction uses density of large ordinary integers in `Z_2`, not a heuristic probability argument.
- Fractional-window confinement is recorded only as a necessary condition.
- The tail-tax theorem allows an unusually small expansion margin and does not claim universal exponential decay without that parameter.

## Files changed

New:

- `claims/theorems/T-0008-negative-shadow-rational-base.md`
- `claims/theorems/T-0009-renewal-code-criterion.md`
- `claims/theorems/T-0010-fractional-window-aspect-ratio.md`
- `claims/lemmas/L-0011-odd-tail-aspect-ratio-tax.md`
- `claims/observations/O-0006-recorded-chart-aspect-ratios.md`
- `experiments/X-0006-shadow-return/README.md`
- `experiments/X-0006-shadow-return/run.py`
- `experiments/X-0006-shadow-return/results/summary.txt`
- this report

Updated at session close:

- `CLAIMS.md`
- `CURRENT_STATE.md`
- `OPEN_PROBLEMS.md`
- `NEGATIVE_RESULTS.md`
- `CANDIDATES.md`
- draft PR `#3`
- issue `#2`

## Claims affected

Added:

- `T-0008`
- `T-0009`
- `T-0010`
- `L-0011`
- `O-0006`
- `X-0006`
- new renewal-code and macroscopic-aspect open targets

## Recommended next actions

### Primary route: negative-template renewal grammar

Build the reverse Collatz tree of one negative target or a small negative cycle as a language of return templates. Seek:

1. a regular infinite return code whose only omitted 2-adic path is the zero shadow;
2. macro-returns with uniform positive growth after grouping;
3. a finite automaton proof that the selected quotient set is forward invariant;
4. an exact translation back to one positive starting integer.

### Parallel route: multi-target graph

The finite one-target obstruction does not apply to a graph of negative targets. Construct a finite graph in which an all-even boundary path is handed to another target before it becomes a permanently contracting branch, while the product multiplier around every accepted cycle is greater than one.

### Chart-design route: macroscopic aspect ratio

Search analytically near pairs of powers `2^L` and `3^a` with small radix gap. Rank negative coalescence fibers by

```text
(branch entropy, precision, diameter/(3^a-2^L), renewal compatibility)
```

rather than cardinality alone.

## Organizational improvement ideas

No protocol change is needed. The integrated state should promote the negative-template return graph as the principal conceptual model, while retaining the induced-map and collision-code files as exact construction machinery.
