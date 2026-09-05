# Synthesis: inverse mass, forward typicality, and a route to a complete proof

> **Status: PROPOSED CONNECTIONS, except for the elementary conditional reduction proved below.** The hypotheses needed to close Collatz are not currently established.

## The two results are complementary, not composable by inspection

| Axis | Predecessor paper | Natural-density/log-time paper |
|---|---|---|
| Direction | inverse | forward |
| Fixed object | target `a` | threshold function or finite floor `N_0` |
| Population | many sources reaching `a` | almost every source descends |
| Quantitative gain | lower count `C_a X^0.901` | fixed-floor upper count `C_d X (log N_0)^(-d)` |
| Time | unrestricted predecessor depth | explicit `O(log N)` forward clock |
| Exceptional issue | the complement may still be huge | one fixed exceptional source may remain |
| Full-Collatz gap | exponent below one and no pointwise conclusion | almost-boundedness is not convergence and fixed-floor decay is not a power of `X` |

The tempting slogan “many predecessors plus density one” is insufficient. A set of size `X^0.901` can have natural density zero, and a nonconvergent orbit can repeatedly visit small nonconvergent values while still satisfying every growing-threshold almost-bounded theorem.

The correct bridge must compare **counting exponents for one fixed floor** or establish a stronger structural statement about the exceptional set.

## A conditional exponent-race bridge

Let `T` denote the one-division Collatz map and `Syr` the odd-to-odd Syracuse map. For odd `N` and fixed `H`, define

\[
\mathcal B_H(X;C)=
\{N\le X:N\text{ odd and }\operatorname{Syr}^m(N)>H
\text{ for all }0\le m\le C\log N\}.
\]

### Hypothesis `INV(gamma)`

For every positive `b` with `3 ∤ b`, there are `c_b>0` and `X_b` such that

\[
\pi_b(X)\ge c_bX^\gamma
\qquad(X\ge X_b).
\]

The imported predecessor theorem supplies `INV(0.901)`.

### Hypothesis `FWD(beta)`

There is one `C>0` and one exponent `beta` such that for every fixed `H≥1`, some `K_H` satisfies

\[
\#\mathcal B_H(X;C)\le K_HX^\beta
\]

for all sufficiently large `X`.

### Bridge theorem

If `INV(gamma)` and `FWD(beta)` hold with `beta<gamma`, then every positive Collatz orbit reaches one.

### Proof

Assume otherwise and let `a` be the least positive starting value whose orbit does not reach one.

1. `a` is odd. If it were even, `a/2<a` would have the same nonconvergent tail.
2. Let `b=Syr(a)`. Then `b` is odd, lies on the same nonconvergent orbit, and `3 ∤ b`, because `3a+1` is congruent to one modulo three and division by a power of two preserves nonzero residue modulo three.
3. By `INV(gamma)`, at least `c_bX^gamma` positive sources `n≤X` reach `b` for large `X`.
4. Strip the maximal power of two from each such `n`, obtaining its odd core `m`. The odd core also reaches `b`. For each fixed odd `m≤X`, at most `1+floor(log_2 X)` sources `2^rm≤X` have that core. Hence the number of distinct odd cores reaching `b` is at least

   \[
   \frac{c_bX^\gamma}{1+\log_2X}.
   \]

5. Every such odd core is nonconvergent. Moreover, its Syracuse orbit can never visit a value at most `a-1`: that value would also reach `b`, hence would be a smaller counterexample than `a`.
6. Therefore every one of these cores lies in `mathcal B_{a-1}(X;C)`, regardless of the clock length.
7. `FWD(beta)` gives the upper bound `K_{a-1}X^beta`. Since

   \[
   \frac{X^{\gamma-\beta}}{1+\log_2X}\to\infty,
   \]

   the lower and upper bounds are incompatible.

This contradiction proves the theorem. `□`

### Immediate numerical target

With the imported inverse theorem, a forward estimate

\[
\#\mathcal B_H(X;C)=O_H(X^\beta)
\qquad\text{for any fixed }\beta<0.901
\]

would prove the full Collatz conjecture.

The current natural-density fixed-target theorem gives only

\[
\#\mathcal B_H(X;C_{\mathrm{Syr}})
\le C_dX(\log H)^{-d},
\]

which has counting exponent one when `H` is fixed. The exact gap is therefore a power saving of more than `0.099` in the counting endpoint, not a missing constant-factor optimization.

## Two-dimensional closure strategy

The bridge creates an exponent plane:

- inverse work raises `gamma` from `0.901` toward one;
- forward work lowers `beta` from one toward a power-saving exponent.

Collatz follows as soon as `gamma>beta`.

This suggests two realistic joint endpoints:

1. **Direct crossing:** keep `gamma=0.901` and prove `beta<0.901`.
2. **Asymptotic crossing:** prove inverse bounds `X^(1-epsilon)` for every `epsilon>0` and any fixed forward power saving `beta<1`; choose `epsilon<1-beta`.

The second endpoint may be structurally easier because it does not demand a very strong first forward exponent or an exactly linear predecessor theorem.

## Highest-value research programs

### Program A — fixed-height power saving

This is the shortest logical route from the two papers to a complete proof.

Target theorem:

```text
For every fixed H, the odd starts that do not enter [1,H]
within C log N Syracuse steps are O_H(X^beta), beta<1.
```

Subtasks:

1. Extract an explicit raw or Syracuse fixed-height count with all constants and thresholds.
2. Replace the one-shot natural/harmonic comparison by an iterated contraction that compounds with the counting endpoint rather than only with `log H`.
3. Prove a spectral gap or minorization estimate for the first-passage kernel after conditioning on survival above `H`.
4. Prevent concentration on a thin arithmetic family by using phase discrepancy at every scale, not only for one transport step.
5. Aim first for any `beta<1`; combine with higher inverse exponents if `beta` remains above `0.901`.

Main risk: a density theorem does not automatically contain endpoint power saving. A new contraction mechanism is required.

### Program B — uniform predecessor exponents

Target theorem:

```text
For every epsilon>0 and every fixed target b with 3∤b,
pi_b(X) >= c_(b,epsilon) X^(1-epsilon) eventually.
```

Subtasks:

1. Discover a level-recursive feasible-weight construction.
2. Replace the level-specific potential table by a uniform adaptive potential or structural termination theorem.
3. Prove a quantitative relation between level and feasible base approaching two.
4. Keep target reduction and coefficient transport uniform enough that the exponent can be chosen after the forward `beta` is known.

Main risk: finite LP feasibility may approach a ceiling below two, and termination potentials may become increasingly complex. Exact dual certificates should be computed in parallel to distinguish these cases.

### Program C — conditioned transport for `SC*`

The resident `SC*` problem fixes one source, so ambient density is the wrong measure. Condition the forward passage law on the residue cylinder determined by an all-supercritical prefix.

Target interface:

```text
uniform distortion/contraction inside every physically realizable
all-supercritical cylinder, with loss subexponential in depth.
```

A summable cylinder failure estimate or a deterministic consequence for canonical least representatives could prove fixed-source stopping. The predecessor paper's time-local choice machinery suggests how to preserve a functional minimum while using a coefficient-valid family of branches.

Main risk: conditioning on a depth-`k` cylinder can magnify errors by about the inverse cylinder mass. The proof must exploit the special supercritical geometry, not merely reweight the ambient theorem.

### Program D — one joint forward/inverse operator

Build an augmented finite-state prototype whose state records:

- residue modulo `3^k` for inverse branches;
- surplus or coefficient-stopping data;
- first-passage phase and survival above a fixed floor;
- the small history needed for dominance.

Search simultaneously for:

1. a positive inverse super-eigenvector;
2. a forward survivor contraction;
3. a bounded adaptive potential ensuring retarded termination;
4. a dual inequality proving the exponents cross.

The finite certificate target is a Collatz-specific Lasota–Yorke or Perron–Frobenius inequality. If successful at one finite level with `gamma>beta`, it would instantiate the bridge theorem directly.

Main risk: naïve product states are enormous. Use symmetry, sparse exceptional lifts, low-rank tensor structure, and proof-producing decomposition rather than a raw Cartesian product.

### Program E — exceptional-set rigidity

Instead of a global count, classify any family that could saturate the fixed-height bad set.

Potential theorem forms:

- every near-extremal bad family has bounded-state or eventually periodic valuation structure;
- every such structure enters the repository's periodic/full-denominator firewall;
- every aperiodic survivor has enough phase entropy to force a uniform passage contraction;
- every fixed-source survivor creates fresh rank or primes at a rate incompatible with small endpoint height.

This program connects the natural-density transport to the resident automata, factor-complexity, rank-escape, and periodic-tail results. It must preserve the repository's warning that method-class exclusions are not universal orbit theorems.

### Program F — retain `FC*` as an independent offense

The exponent-race bridge can eliminate both divergent orbits and cycles through a least-counterexample argument, but it is not yet established. The existing complete-denominator `FC*` route remains independently valuable and may close first-crossing realizations without any density theorem.

No import claim should conflate:

- predecessor lower bounds with complete-denominator divisibility;
- phase mixing with exact cycle replay;
- a sparse exceptional-set theorem with ordinary extraction.

## Concrete first experiments

1. **Adaptive-potential structure mining.** Obtain the level-18 potential and list the `484,801` nonzero-selector states in each of the D1 and D3 auxiliary families. Fit base-three suffix rules and compute minimal deterministic/counter automata reproducing the selector.
2. **Level sweep with duals.** Solve and certify levels 16, 17, 18, and one higher tractable level, recording primal feasible exponents and dual upper bounds.
3. **Parametric block ratio.** Generalize the natural-density source band from `1001/1000` to symbolic rational `alpha`; numerically map the admissible clock/error region before formal proof work.
4. **Fixed-floor survivor numerics.** For several fixed `H`, count odd starts surviving `C log N` up to large `X`, fit local power exponents, and stratify by residue and valuation words. This is only hypothesis generation; any exponent claim requires proof.
5. **Conditioned-kernel prototype.** Measure natural/harmonic passage discrepancy inside parity cylinders of increasing depth, especially all-supercritical cylinders from the resident SC packet.
6. **Normal-form extraction.** Materialize a sample of level-18 adaptive normal forms to estimate depth, reuse, and compressibility before attempting the entire state space.

## Recommended order of attack

By logical distance to a full proof:

1. fixed-height power-saving theorem with `beta<0.901`;
2. any fixed-height power saving plus inverse `1-epsilon` family;
3. cylinder-conditioned contraction strong enough for `SC*`;
4. complete `FC*` denominator synchronization;
5. joint operator certificate crossing `gamma` and `beta`.

By near-term tractability:

1. effective thresholds and parametric clock optimization;
2. adaptive-potential exception classification;
3. level-18 dual optimality and neighboring-level sweep;
4. materialized normal forms;
5. conditioned-kernel experiments;
6. structural fixed-height power saving.

## Status boundary

The bridge theorem is a conditional implication with a complete elementary proof. Neither `FWD(beta<0.901)` nor a uniform inverse `1-epsilon` theorem is presently established. The imported works materially narrow a possible full-solution route, but they do not themselves solve Collatz or the resident `SC*` and `FC*` obligations.
