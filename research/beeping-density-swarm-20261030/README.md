# Positive density, beeping computation, and transported arithmetic ranks

**Collatz remains unresolved.** This exploratory packet supplies proved-scope
constructions, conditional reductions, exact obstructions and reproducible
checks. It supplies no complete convergence proof, nontrivial positive cycle,
or divergent positive trajectory. New claims remain **PROPOSED**; external
density and single-fold claims remain **SOURCE-QUALIFIED** where used.

The pass began from the user-supplied Mazur positive-density paper and the
17-state beeping machine. Four agents worked on density, rewriting/orders,
machine semantics and synthesis, with separate mathematical reconstruction of
the principal local arguments. We inspected current main at
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a` and relevant later source packets.
The [source and execution record](../../reports/beeping-density-swarm-20261030/README.md)
states that inspection's actual scope; it is not an exhaustive new review of
every historical PR.

## 1. A computable observable gives a precise analytic proof target

Let T be the shortcut map, let tau(n) be its first hitting time of 1, allowing
infinity, and let b(n) be the positive binary bit length. Define

\[
R(n)=\frac{b(n)}{b(n)+\tau(n)},\qquad R(n)=0\text{ when }\tau(n)=\infty.
\]

This rational-valued function is **uniformly computable as a real** without
assuming Collatz: simulate at most M b(n) steps and return zero if the input
has not yet reached one. The error is at most 1/(M+1). This is an approximation
algorithm; it does not decide whether the exact value is zero. An exponential
version has exponentially small truncation error.

The function satisfies the unconditional pointwise estimate

\[
|R(Tn)-R(n)|\le\frac1{b(n)-1}\quad(n\ge4).
\]

If R can be approximated in **logarithmic mean absolute error** by functions
of a fixed finite number of low binary digits, then the Collatz parity
conjugacy makes it equal in that norm to a constant. Mazur's fast positive
density result forces that constant positive; the positive-density
predecessor theorem would force it zero if any counterexample existed.
This proves a sufficient criterion for full Collatz, conditional on those
external density results.

The missing property is substantial: for this already asymptotically invariant
observable, that regularity is equivalent to concentration around a constant
in the stated norm. We have **not** established it. The order of limits fixes
the bit resolution before taking the averaging cutoff to infinity.

Read [REGULARITY_BRIDGE.md](REGULARITY_BRIDGE.md) for DREG-001--007, both
natural and logarithmic norms, the indicator equivalence, and the exact
conditional-variance test. The separate
[regularity review](REGULARITY_REVIEW.md) reconstructs these implications.

## 2. A least rank envelope repairs one-step moment loss

The actual-prefix rank Gamma is inherited from PR106; its finite evaluator
and arbitrary-period selection theorem are credited there. Define S to be
the shortcut map absorbed at one, and set

\[
\Phi(n)=\max_{j\ge0}\left\lceil\frac{\Gamma(S^j n)}{3^j}\right\rceil.
\]

This maximum is an exact finite computation using O(log n) forward positions.
It is the least integer majorant of Gamma satisfying
`Phi(Sn) <= 3 Phi(n)`. It retains the old critical summability exponent 1/2,
and every positive Phi moment stays finite after one killed forward step.

The simple height-squared weight already has bounded growth. The additional
value here is minimality relative to Gamma, a total contact interface, and
arithmetic savings: `Phi(6^h) <= 12^h`, while `(6^h)^2=36^h`. Thus the new
moment space is strictly larger than the corresponding height-moment space
for each fixed positive moment exponent p. It is also strictly smaller than
the Gamma-moment space that exhibited the
original unbounded one-step spikes. No old integrability assumption is silently
transferred to the stronger space.

The contact set is `C={n>=2:Phi(n)=Gamma(n)}`. Every source reaches C or one
in O(log n) shortcut steps. Every contact endpoint also has a **complete
finite inverse fan** for its positive-time contact return, with the exact
return-length bound `r <= ceil(log_3 Phi(endpoint))`. If P is the endpoint
rank, the entire fan can be enumerated using O(P^0.3046...) tested nodes,
where the exact exponent is `log(phi)/log(3 phi)` and phi is the golden ratio.
This counts search nodes, not bit operations or exceptional starting integers.
These statements provide an executable induced map and finite arithmetic
tests of its inverse rows.

They do not give descent. The first contact return `11 -> 17 -> 26` raises
Phi from 48 to 192; `19 -> 29 -> 44` raises it from 192 to 1728. The latter
also rules out a strict inverse supersolution based only on `Phi^(-s)`, for
every s>0, on the current contact operator killed only at one. Possible
escapes include additional arithmetic information, finite weight corrections,
a larger certified terminal set, or a different certified grouping of returns.

Read [RANK_ENVELOPE.md](RANK_ENVELOPE.md) for the proofs, the rational envelope
with growth factor 9/4, the complete fans and exact failed strengthenings.
See the separate [rank review](RANK_ENVELOPE_REVIEW.md).

## 3. The 17-state machine is an exact arithmetic interface

The literal machine from the post was checked against a complete tape invariant,
including retained capacity. Its three macros implement an even shortcut step,
an odd shortcut step, and a reset that increments the tested input and emits
that input's number of beeps. The blank run therefore beeps infinitely often
exactly when Collatz holds. If b is the least counterexample, the total number
of beeps is b(b-1)/2. This is an audit of the source's equivalence, not a new
solution criterion claimed as a proof.

The additional exact clock identity is

\[
A(n)=\frac23n^2+2n-\frac83+
\sum_{\substack{v\text{ on the preterminal shortcut orbit}\\v\text{ odd}}}
\frac{(v+1)(25v+23)}{12}.
\]

Here A(n) is literal machine time spent in arithmetic macros when the input
converges. A finite-prefix form holds without convergence on arithmetic
segments before the first visit to one. The gap to the
first beep for input n is A(n)+n+5. Thus a timing proof has to control an
explicit positive quadratic sum on actual odd trajectories.

The packet also excludes finite lexicographic nonnegative quasi-polynomial
ranks on **all** canonical machine configurations. Reachable-only invariants,
adaptive blocks and nonpolynomial orders are outside that obstruction.

The Diophantine connection needs a quantifier correction: the set of convergent
inputs is infinite whether Collatz is true or false. Conditional on the claimed
single-fold theorem, represent the set of **fully verified initial segments**
instead. Its polynomial has exactly b-1 complete solutions if b is the least
counterexample, and infinitely many if all inputs converge. This packet neither
constructs numerical coefficients for that polynomial nor verifies the full
external single-fold theorem.

Read [BEEPING_ENERGY_AND_RANKS.md](BEEPING_ENERGY_AND_RANKS.md).

## 4. Positive sources escape the worst reference spike

For the mean-one ternary inverse-reference density rho_q defined in
[NEGATIVE_SPIKE_BARRIER.md](NEGATIVE_SPIKE_BARRIER.md), we prove

\[
\rho_q(t)\le6qt+(64/81)^q
\quad\text{for every fixed positive odd integer }t\text{ and }q\ge1.
\]

At the negative fixed point, by contrast, `rho_q(-1) >= (3/2)^q`. The positive
bound groups inverse words by total valuation, uses positivity and fixed-depth
source injectivity to bound every layer, then controls the remaining geometric
tail. It assumes neither convergence nor nonperiodicity of the target.
The corresponding depth generating series has radius at least one at each
fixed positive odd target, whereas at -1 its radius is at most two thirds.
The separate [spike review](NEGATIVE_SPIKE_REVIEW.md) reconstructs the proof.

This is control of weighted inverse histories, not forward termination. Its
factor t matters when endpoints move under transport, and the bound still
grows with q. A uniform or summable transported estimate remains missing.

## 5. Two concrete barriers guide the next attempt

**Global inverse-law clipping has an arithmetic limit.** The all-one inverse
valuation word creates a spike at the negative fixed point -1. It forces a
tail exponent at most `log(2)/log(3/2)` and divergence of the critical strong
moment. The particular global clipping/source-charge census cannot reach a
target-loss exponent below `log_2(3)` by strengthening that tail bound alone.
This is a limitation of that census, not an upper bound on actual positive
predecessor density. At a fixed positive odd target t, the initial all-one run
has the exact finite budget `v_3(t+1)`. The open opportunity is to retain such
ordinary-source budgets through later transported branches. See
[NEGATIVE_SPIKE_BARRIER.md](NEGATIVE_SPIKE_BARRIER.md).

**Small invariance error does not imply concentration.** Majority functions
of k parity bits have mean one half and stay one half away from every constant,
while their one-step error is exactly
`binom(k-1,(k-1)/2)/2^k -> 0`. They can also match arbitrary fixed finite
anchor data at vanishing cost. A computable slow log-log oscillation has the
same pointwise O(1/log n) invariance rate as the soft observable and still
fails the needed regularity. See [NEAR_INVARIANTS.md](NEAR_INVARIANTS.md).

The [rewriting source note](YAH_AND_NASHIDA_SOURCES.md) records the exact
Yolcu--Aaronson--Heule system and newly located Nashida barrier preprints,
retaining their stated hypotheses and formalization limits. No general claim
that all matrix orders or all well-founded orders are impossible is made.

## 6. What would close a route, and what has actually been checked

There are three precise remaining proof tasks, not three established lemmas:

1. Prove logarithmic mean concentration/dyadic approximation for the actual
   soft stopping observable, using its hitting-time structure.
2. Find a strictly positive summable contact weight with a strict inequality
   on **every complete inverse fan**, or a total physical smaller-rank merger
   selector on that contact set. Pure powers of Phi have already failed with
   the current terminal set; finite corrections or an enlarged certified
   terminal set remain possible.
3. Prove a source-conditioned bound for accumulated near-negative inverse
   runs that survives actual transport, rather than resetting to a global
   reference supremum.

The principal computations include whole-tape checks of 1,068 machine macros;
10,000 arithmetic energy checks; rational soft-clock diagnostics through
100,000 inputs; exact parity-majority enumeration over 349,524 source residues;
finite rank/Bellman/contact checks; complete small contact fans; and exact
geometric-law residue sums. These are evidence for the implementations and
examples. The universal local theorems rest on their written proofs. None of
the finite runs proves an asymptotic regularity statement.

All code and bounded receipts are in
[the experiment directory](../../experiments/beeping-density-swarm-20261030/README.md).
The [execution report](../../reports/beeping-density-swarm-20261030/README.md)
separates independent reconstruction, self-checks, external source-reported
Lean evidence and complete-checkout validation. No external Lean build or
full mathematical acceptance is claimed.
