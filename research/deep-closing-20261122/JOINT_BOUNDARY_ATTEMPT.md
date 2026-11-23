# Testing joint real and ternary boundary machinery

Status: **SOURCE-QUALIFIED applicability analysis; closing estimate OPEN.**
The aim was to obtain an entropy lower bound for the actual escaping time
law in `ACTUAL_ORBIT_ENTROPY.md`, using joint-completion geometry rather
than an independently sampled predecessor law. No result below is an
assumption of the new Lean proofs.

## Boundary theorem and the attempted import

[Brofferio, 2006](https://www.numdam.org/article/AIF_2006__56_2_499_0.pdf)
identifies the Poisson boundary of a nonabelian rational affine random
walk, under a logarithmic first-moment condition, through its contracting
completions. This is substantial machinery for a specified random-walk
law. It does not turn a deterministic positive orbit into a typical
sample of that law. We inspected the theorem and hypotheses, not its full
proof anew.

The first proposed route was to encode the actual gap process as a
stationary increment process, use its negative ternary drift, and apply
boundary rigidity. Our finite proof supplies an upper mean gap bound and
a deterministic ternary coding map. It does not supply independent
increments or a full-support transition policy. Replacing the actual
increments by a geometric law changes the measure whose entropy needs
to be bounded below. The Poisson-boundary theorem therefore leaves this
specific import unproved.

## Quantitative quotient mixing and the source label

The recent primary manuscript
[Paper 19, sections 10.6 and 11](https://rstation.ai/problems/collatz/papers/19)
works with the compact quotient
\((\mathbb R\times\mathbb Q_3)/\operatorname{diag}\mathbb Z[1/3]\).
For its projected stationary law it derives

\[
(D_2)_*\nu=\tfrac12(\nu+(D_3)_*\nu),\qquad
(D_{2^n})_*\nu=\sum_{j=0}^n2^{-n}\binom nj(D_{3^j})_*\nu,
\]

and quantitative finite-partition convergence to Haar. Every integer
diagonal \((a,a)\) projects to the same identity. The integer trace is
recovered on a cell of Haar volume \(2^{-n}\), introducing a factor
\(2^n\). These inspected statements are SOURCE-QUALIFIED; their full
proof and computational dependencies were not independently rebuilt.

Our attempted continuation was to apply quotient mixing at the scale of
the actual arithmetic trace. This fails at a precise estimate: an
unconditional additive error \(\varepsilon_n\) becomes as large as
\(2^n\varepsilon_n\) after normalization on that cell. Polynomial
\(\varepsilon_n\) does not yield a vanishing relative error. Moreover the
quotient has discarded which integer source was selected. Choosing a
fixed coarse partition avoids this loss only by giving up the specified
integer trace. Taking the limits in the opposite order does not repair
either issue.

## The needed strengthened statement

A useful theorem would keep an original ordinary source, the real floor
or stopping condition, and the complete relevant ternary residue together,
and give relative control on its arithmetic cells. It must apply to the
actual time law, or prove a transfer to it with a controlled cost. A
mixing bound after averaging away the source does not have this meaning.

The sibling calculation in `SIBLING_SMOOTHING_ATTEMPT.md` tests one such
transfer explicitly: ternary smoothing of sources can cost exponentially
many gap units, while their future laws collapse to one state. This is why
the missing estimate needs an escape-specific premise.

The main entropy theorem provides a concrete threshold for such work:
forcing upper entropy dimension strictly above
\(\Phi(\log_2 3)/\log3\) for every actual nonperiodic positive orbit would
contradict the new ceiling and exclude escape. No theorem inspected here
supplies that premise. Cycle exclusion would remain a separate obligation.
