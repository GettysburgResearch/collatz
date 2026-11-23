# Complete carries, sharp random-model regularity, and the actual resolvent

Date: 2026-11-23. Continuation of PR180 from
`7d4ad9f11d3d7a54c67b0c6cff4f13a2ab967161`.

**Collatz remains OPEN.** Four parallel attacks pursued the original-law
collision estimate, pointwise Fourier control, complete positive-cycle
closure, and a global construction of the actual parity series. This
checkpoint supplies written proofs, a new Lean collision core, and exact
controls. The strongest new result is a complete integrability threshold
and Renyi spectrum for the explicitly specified geometric-2 affine model.
Its pointwise connection to an arbitrary ordinary orbit is not proved.

The four newly advanced peer heads inspected were PR176 `4171e1fe...`,
PR177 `f47a5ec5...`, PR178 `c91b80a3...`, and PR182 `cb1ae1bb...`.
Full source identities and uses are in [SOURCES.json](SOURCES.json) and
the [refresh record](../../reports/2026-11-23-closing-step/SOURCE_REFRESH.json).
The previous whole-repository survey is retained. Historical Lean modules
were not rebuilt for this pass.

## 1. The new mathematical results

| Attack | Established at the stated scope | Remaining ordinary closing step |
|---|---|---|
| Complete-carry decoding | For every stationary integrable gap law, the entropy lost in passing from words to ternary endpoints is bounded by its positive conditional drift budget. If each component has mean gap at most `log_2 3`, endpoint coding preserves the full entropy rate. The exact weighted collision inequality retains all carry-channel cross terms. | Bound the complete-carry moment under the squared **actual** word law, or otherwise use fixed-source arithmetic to exclude the critical limiting branch. |
| Random affine law and Fourier bridge | For iid geometric gaps of mean two, the ternary density belongs exactly to `L^p`, `1<=p<2`. Its full Renyi spectrum is explicit; its depth-`m` squared density norm is between `c m` and `C m^4` eventually. Bremont's theorem gives real Fourier decay, retained uniformly under ordinary residue conditioning when depth is `o(log frequency)`. | Identify the actual component's trace boundary with controlled finite model conditionals at the frequencies required by its original scales. Generic disintegration does not specify ordinary point fibres. |
| All positive cycles together | Conditional on the inherited uniform predecessor-density input (P), the sum of the complete logarithmic defects over **all** positive cycles is finite. This gives a simultaneous basin budget and a convergent product cancelling the actual resolvent's interior cycle poles. Repeated inverse laps have an exact ordinary integrality lattice. | Exclude even one nontrivial positive cycle with a small defect. Summability and pole cancellation do not do that. |
| Actual global parity series | Constructed meromorphically on `|z|<2` in the linear-growth source norm. Its operator poles are precisely actual positive-cycle roots, all simple. The actual forcing has no continuation through any point of `|z|=2` in that norm; all polynomial reweightings have essential spectral radius at least `1/2`. | Construct a stronger **fixed-source scalar** arithmetic continuation or recurrence. The uniform family already fails at the boundary on the known sources `2^k`. |

### Complete carries preserve more than a quotient-only calculation

For a chronological gap word, let `A` be its total division count, `C`
its full integer affine carry, `K=floor(C/3^m)`, and `r` its endpoint
modulo `3^m`. The triple `(A,K,r)` determines the word. Thus

\[
 H(\text{word})-H(r)=H(A,K\mid r).
\]

For a stationary gap process with conditional mean
`bar_g=E[G|invariant sigma-algebra]`, the complete logarithmic carry has
the exact asymptotic budget

\[
 \lim_m\frac{\mathbb E\log(K_m+1)}m
 =\mathbb E[(\bar g\log2-\log3)_+].
\]

Collision requires a different probability measure. With actual word
mass `P_m(w)`, put `Z_m=sum_w P_m(w)^2` and
`Ptilde_m(w)=P_m(w)^2/Z_m`. For any positive penalty with summable
reciprocal,

\[
 Z_m\le\operatorname{Col}_m
 \le Z_m\left(\sum_{a,k}L_{a,k}^{-1}\right)
                 \mathbb E_{\widetilde P_m}L_{A_m,K_m}.
\]

The [collision note](COLLISION_CLOSURE.md) evaluates this tilt exactly in
the geometric iid branch. For mean `1<b<2`,

\[
 (2b-1)^{-m}\le\operatorname{Col}_m
       \le C_b\sqrt m\,(2b-1)^{-m}.
\]

At the actual maximum-Shannon equality value `b=log_2 3`, this identifies
the endpoint Renyi-2 dimension as
`log(2 log_2 3-1)/log 3`, approximately `0.7051555`, while the Shannon
dimension is approximately `0.9499555`. A collision upper bound at the
larger exponent therefore cannot hold on this branch unless additional
ordinary-source information excludes it.

The separate [stationary counterexample](TILTED_MOMENT_OBSTRUCTION.md)
shows the moment distinction is essential: an explicit bounded ergodic
gap process of mean `3/2` has a sublinear original logarithmic carry,
but every positive carry moment under its squared-word tilt grows
exponentially. No ordinary-orbit realization is claimed for this control.

### The geometric-2 model now has an exact regularity threshold

For iid `P(G=e)=2^-e`, let

\[
 Y=\sum_{j\ge1}3^{j-1}2^{-(G_1+\cdots+G_j)}\in\mathbb Z_3^\times.
\]

Relative to Haar probability on all of `Z_3`, its law has density `F`, and

\[
 F\in L^p\ \Longleftrightarrow\ 1\le p<2,
 \qquad
 D_q=\begin{cases}
 1,&1<q\le2,\\
 \dfrac{\log(2^q-1)}{(q-1)\log3},&q>2.
 \end{cases}
\]

Tao's Proposition 1.14 supplies uniform `L^1` convergence of finite
ternary densities. Interpolating it with the new polynomial `L^2` bound
gives every `p<2`. At the endpoint, the transfer operator's diagonal
square-norm contributions already sum to the entire norm. Its infinitely
many positive-mass image supports necessarily overlap, forcing a positive
cross term and contradicting finite `L^2`. The same argument gives linear
growth of the finite squared norms. The generalized word tilt gives the
matching higher-order exponential rates.

[FOURIER_BRIDGE.md](FOURIER_BRIDGE.md) contains the proofs, primary
literature inputs, and a finite-depth real Fourier conditioning bound.
This is an iid model theorem. The actual component boundary and original
integer residues remain separate objects with an explicit unresolved
comparison step.

### Cycles and the resolvent meet in one qualified product

For an actual positive cycle with shortcut period `A` and odd count `p`,
its complete defect is

\[
 \delta_C=A\log2-p\log3>0.
\]

[POSITIVE_CYCLE.md](POSITIVE_CYCLE.md) proves, assuming the inherited
uniform input (P), `sum_C delta_C <=22/(3c0)` over all distinct positive
cycles. [GLOBAL_CONSTRUCTION.md](GLOBAL_CONSTRUCTION.md) independently
constructs the actual weighted parity resolvent and classifies its
interior poles by `z^A=3^p`. The
[cross-lane bridge](CYCLE_RESOLVENT_BRIDGE.md) then cancels these poles
by a nonzero bounded analytic Blaschke product in `w=z/2`.

The result is holomorphic inside the same disc. It supplies no boundary
growth estimate, no extension through `|z|=2`, and no proof that a cycle
factor is absent. The scalar continuation problem at a fixed ordinary
source remains the intended analytic target.

## 2. Formal scope and checks

The new [Lean module](lean/WeightedCollision.lean) contains exactly three
public theorems:

- `weighted_sum_cauchy`: finite weighted Cauchy without square roots.
- `labelled_collision_bound`: the full residue collision bound when a
  label and residue jointly determine each object.
- `complete_carry_recovery`: retained quotient and endpoint remainder
  recover the complete natural-number carry.

The joint injection is an explicit hypothesis of the finite collision
theorem. Recursive decoding of every gap word, the countable limit,
stationary entropy arguments, analytic moment estimates, Fourier results,
operator results, and cycle packing are **written proofs**, not new Lean
declarations. [THEOREMS.json](THEOREMS.json) fixes the complete formal
inventory. Fresh compilation with warnings treated as errors passed in
Lean 4.34.1 and the pinned Mathlib checkout; declaration audits report
only `propext`, `Classical.choice`, and `Quot.sound`.

The [finite cycle checker](check_cycle_return.py) verifies ordinary
inverse-return lattices and rational paired-product controls. Its 48 legal
return cases, 144 inverse-lattice cases, and 10 false-lap rejections replay
identically under normal Python and `-O`. These controls do not search for
unknown cycles or validate analytic input (P).

All principal notes and the new formal core have independent hash-bound
reviews in [REVIEW_BINDINGS.json](REVIEW_BINDINGS.json). The Fourier review
identified and repaired a zero-mass conditioning-domain omission: the
normalized conditional law is defined only for positive odd unit roots.
The terminal inverse endpoint may still be divisible by three.

Run the lightweight identity check after fetching the pinned source
commits:

```bash
python -X utf8 -B research/closing-step-20261123/check_packet.py --check-sources
python -X utf8 -B research/closing-step-20261123/check_cycle_return.py
python -X utf8 -B tools/validate.py
```

`check_packet.py` checks identities and recorded proof scope; it does not
reprove written mathematics or run the Lean compiler. Use `check_lean.py`
with explicit `--lean`, `--mathlib`, and `--report-dir` for a fresh compile.
Post-commit validation receipts are written outside the tested checkout.

## 3. The retained next closing obligation

The central missing estimate is now explicit: control the actual
collision-weighted carry, or identify the actual ordinary-root boundary
with the Fourier-controlled model at sufficient quantitative resolution.
For positive cycles the missing step is a contradiction for one complete
ordinary closing fibre, including its full denominator. Neither a generic
probability statement, a changing finite source, nor an analytic product
that cancels existing poles substitutes for either obligation.
