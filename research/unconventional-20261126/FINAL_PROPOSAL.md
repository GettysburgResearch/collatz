# Final Lean proposal and the exact remaining mathematical work

**Collatz remains open in this packet.** The three-hour continuation supplies
new written restrictions, counterexamples to proposed shortcuts, and checked
finite interfaces. It does not contain a complete proof of either universal
obligation below. All maps and clocks in this document refer to the actual
positive-integer shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]

## 1. The checked endpoint

[FinalProposal.lean](FinalProposal.lean) defines `Collatz`, `NoEscape`, and
`CycleUnique` on the natural-number map and proves

```lean
theorem exact_final_obligations : Collatz ↔ NoEscape ∧ CycleUnique
```

Here `NoEscape` means that every positive source has two equal states at
distinct native times. `CycleUnique` means that every actual positive
periodic point eventually reaches 1. Repetition first reaches a positive
periodic point; the second obligation then reaches 1. Conversely convergence
gives both obligations. The proof is elementary and explicit. The two
propositions are definitions, not axioms and not theorem declarations.

[FiniteExit.lean](FiniteExit.lean) makes the first obligation a concrete
finite certificate. Given `X` and `n`, the Boolean `trap X n` evaluates the
first `X+1` actual states and checks that every one is below `X`. Pigeonhole
gives repetition. A repeated state bounds the entire future, so some such
certificate exists. The checked conclusion is

```lean
theorem exact_finite_proposal : Collatz ↔ FiniteTrapping ∧ CycleUnique
```

`FiniteTrapping` is exactly `∀ n > 0, ∃ X, trap X n = true` in mathematical
notation. Every supplied test terminates. No proof here establishes that
a successful test exists for every positive `n`, and no finite experiment
is substituted for that quantifier.

The complete finite packet has 64 audited declarations in twelve files.
See [the replay report](../../reports/unconventional-20261126/README.md)
for the exact source bytes, compiler, dependencies, commands and axiom
output. The infinite analytic arguments below are not formalized there.

## 2. A precise analytic target for `FiniteTrapping`

Fix `s=2`. At cutoff `X`, follow each ordinary source `x<X` until either
it exits at a state `y≥X` or a state repeats. At a genuine exit, attach
the weight `(C/y)^2`, where `C` is the principal multiplier `3^p/2^k` of
that exact prefix. Aggregate the weights at each exit as `J₂,X(y)`.
This is a finite terminating computation: a source staying below `X`
must repeat within `X+1` states.

[EXIT_GATES.md](operator/EXIT_GATES.md) proves in written mathematics
that the decreasing rearrangement of these gate weights converges in
`ℓ¹` to one strictly positive number per escaping ordinary component.
Consequently

\[
\sum_y J_{2,X}(y)\longrightarrow0
\quad\Longleftrightarrow\quad\text{NoEscape}.
\]

Every periodic component is invisible in this limit, which is why cycle
uniqueness remains a separate obligation. The augmented total
`∑ᵧ J₂,X(y)+∑ₓ≥X x⁻²` is nonincreasing; monotonicity does not determine
its limit.

[GATE_PROXIMITY.md](renewal/GATE_PROXIMITY.md) sharpens the target. It
constructs an explicit subset `E′X` of the actual exit gates with

\[
|E'_X|\ll \frac{X^\theta}{(\log X)^{3/2}},\qquad
\sum_{y\notin E'_X}J_{2,X}(y)\asymp\frac{\log X}{X},
\quad\theta=0.949955527\ldots.
\]

Thus a sufficient closing estimate, still **unproved**, is

\[
\boxed{\displaystyle\sum_{y\in E'_X}J_{2,X}(y)\longrightarrow0.}
\]

The number of gates alone cannot give this: their weights can concentrate.
The actual prime-cofactor and log-height theorems restrict that
concentration, but still allow diffuse critical records, signed-cycle
limits with arithmetically rough integer representatives, and slow peak
growth. Excluding all these alternatives requires a further argument on
one ordinary integer orbit for its entire future.

## 3. A precise arithmetic target for `CycleUnique`

For a nonempty native parity word `w` of length `N`, odd count `p`, and
integer carry `A_w`, its rational fixed point is

\[
x_w=\frac{A_w}{2^N-3^p}.
\]

When the denominator is positive and `A_w>0`, an ordinary cycle requires
the **whole** integer `2^N-3^p` to divide `A_w`. The needed conclusion is
that such a genuine positive integer fixed point belongs to the usual
cycle `{1,2}`. The new rational constructions preserve a nontrivial
reduced denominator deliberately. Cancelling many prime powers or making
that denominator subexponential in the period does not make it equal to one.

[DYADIC_CYCLE_ORDER.md](adelic/DYADIC_CYCLE_ORDER.md) adds an actual
integer restriction for a **primitive cycle**, with `N` its least native
period and `p` its distinct odd departures: the inversion count among
dyadic lifts of its odd phases has lower bound `gcd(N,p)−1` and the same
parity. The binary interval
geometry forbids low-depth inversions for integer phases. These are useful
filters, but they leave the coprime period/grade sector open. Neither a
global order-preservation assertion nor the same assertion restricted to
contracting words is available: the latter already fails at starts 859
and 860 after 46 steps, as checked in Lean.

The complete-denominator exclusion outside the known positive cycle is
the second missing universal theorem.
No claim in this packet substitutes bounded prime tests, local topology,
pressure, or an auxiliary real trajectory for that integer assertion.

## 4. What the unconventional pass changed

The actual shifted-cofactor theorem gives a lower native fraction
`log₃ 2` of simultaneous nearly full logarithmic cofactors against any
one adaptive bounded prime pool. The elementary polynomial theorem gives
a density-one conclusion for polynomials with no rational roots, uniformly
on finite simple segments. Mandatory log-height occupation then moves
these arithmetic tests to a clock that cannot lose all its mass on an
escape. The regular sector is conservative and its atoms are classified.

These are restrictions on possible ordinary counterexamples, with precise
quantifiers and reviewed written proofs. The rational and symbolic controls
show where several candidate closing arguments fail. The principal next
step is now visible: control the *weighted* mass on the thin critical
ordinary gates, and separately eliminate nontrivial solutions to the full
denominator-one cycle equation. The present results do not yet provide
either step.

The final [closing audit](CLOSING_AUDIT.md) computes the moving witness
attached to each true record and the positive residual in the direct
two-coordinate Subspace attempt. It also tests the combined nonlinear
arithmetic and interval geometry on genuine rational cycles, retaining
the distinction between exponential and subexponential denominators.

Independent review here means reconstruction by another GPT-6.2 Astra
agent and, for the principal later results, by the coordinator. It is not
an external expert endorsement, a priority determination, or a formal
verification of the full written mathematics.
