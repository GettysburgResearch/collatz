# Polynomial spectrum and certified cylinder energy

**PROPOSED research; self-audited only. No full Collatz proof.**

This continuation of PR142 attacks two bottlenecks rather than treating the
source-qualified positive-floor bridge as a convergence theorem. It also
compares with PR140 at `6bee3183ff7f29f2e20ca88ab94bc7745c1af602`.

## What is established in the proposed proofs

[Polynomial spectrum](POLYNOMIAL_SPECTRUM.md) gives the complete phase diagram
for the actual Jacobian inverse operator on `l^1(n^-s)`, after removing ANY
finite set of states. For every real `s<=1`, its spectrum and Fredholm
essential spectrum are the disk of radius `(3/2)^(1-s)`. For `s>1` it is
unbounded. All approximate-spectrum witnesses are supported on explicitly
constructed positive trajectories that reach 1. The same family rules out a
bounded spectral radius below one for every regularly varying weight.

This extends the inherited harmonic (`s=1`) result; it does not claim that
result anew. Its practical meaning is that polynomial reweighting and finite
verification cannot repair the current global contraction strategy. Failure
of that strategy is not evidence of a nonconvergent Collatz trajectory.

[The energy operator](ENERGY_OPERATOR.md) identifies the full Haar Gram
operator with a Poisson kernel of the affine odometer `x -> 4x+1`. It gives
sharp squared singular-value bounds `3/5` and `5/3`, and the explicit bound

    E_q >= log_4(4 + q log(4)/4).

This elementary lower growth needs no external trace floor, atom floor or
mixing theorem. It is weaker than linear lower bounds obtainable with
stronger positivity inputs. The density-special-case correlation identity
and previous quadratic upper bounds are explicitly credited, not relabeled
as discoveries of this pass.

## Executed evidence

The [exact checker](../../experiments/spectral-energy-20261031/check_exact.py)
compares two complete rational cylinder-law constructions through depth 5,
checks 40 signed Gram identities, and reconstructs 12 disjoint convergent
corridors (90 literal odd-map steps, up to a 531,434-bit source). It checks
91 whole-vector residuals and 12 critical terminal-cancellation pairs.

The [integer interval checker](../../experiments/spectral-energy-20261031/certify_energy.py)
encloses all 7,174,452 residues across depths 1 through 14, including the
entire infinite geometric exponent tail. No floating-point arithmetic or
sampling enters these bounds. In particular,

    7.742768288642 <= E_14 <= 7.742768288643,
    0.470254334094 <= E_14-E_13 <= 0.470254334095.

These are cylinder residues, NOT millions of ordinary trajectories. The
finite increments suggest linear growth but do not prove an asymptotic
upper bound. Both new suites passed in normal and optimized Python with
byte-identical outputs. Six recovered suites also passed in both modes.

See [replay instructions](../../experiments/spectral-energy-20261031/README.md),
[the self-audit](REVIEW.md) and [the receipt](../../reports/spectral-energy-20261031/README.md).

## What this does not establish

No uniform ordinary forward-survivor estimate, nontrivial-cycle exclusion,
full convergence proof, independent-agent review, proof-assistant build,
complete-checkout validation or remote CI success is claimed. The ordinary
weighted sequence operator and the Haar operator are kept distinct.

The positive next target on the energy side is a uniform bound on the
weighted odometer correlations in E1, not a deduction from a bounded single
step norm. On the convergence side, a successful replacement must distinguish
persistent survivors from the explicit, arbitrarily long convergent
corridors. Neither missing assertion is smuggled into the spectral proof.
