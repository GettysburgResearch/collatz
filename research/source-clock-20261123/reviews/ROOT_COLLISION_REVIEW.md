# Independent reconstruction: collision transfer test

Date: 2026-11-23. Reviewer: root agent.

Reviewed file: `research/source-clock-20261123/COLLISION_TRANSFER.md`.

SHA256: `4f6494baa8fd85e936e69367c45a27ab774a8a0aa6ee188919e49f44371b7fe9`.

**VERIFIED** for the explicit model in Section 1 and **VERIFIED conditional
on the retained source inputs** for Section 2. This review does not identify
the model with a Collatz boundary measure or establish a collision upper bound.

For `beta=theta/2>0`, substitution `x=exp(-u)` proves integrability and
strict positivity of the normalizing constant. At every interior point
the density is continuous and strictly positive, so the ordinary local
dimension is exactly one. There is no atom at the endpoint zero.

On `[epsilon/2,epsilon]`, both factors `x^(beta-1)` and
`(log(e/x))^(1/4)` are at least their values at `epsilon` because
`0<beta<1`. Integrating that half-interval gives the stated first-cell
lower bound. Squaring it gives the exact square-root logarithmic excess
with exponent `2 beta=theta`. This alone rules out an upper constant
times `3^(-theta m)` for this model.

The differential entropy integral is finite in absolute value: after the
same substitution, its integrand has an exponential factor `exp(-beta u)`
times at most a fixed power of `1+u`. Jensen on each equal-length cell
therefore bounds the partition entropy below by `m log 3 - integral f log f`.
The number of cells bounds it above by `m log 3`. Thus the model also has
Shannon information dimension one. Its high collision concentration is
compatible with both almost-everywhere dimension and mean information
dimension; neither gives uniform or Renyi-2 regularity.

For the actual retained law, retracing from `q_(r+j)` to `q_j` has
ordinary inverse probability `nu(q_j)/nu(q_(r+j)) >= v_0/C_E`.
Averaging these unchanged atoms gives (6) for every `r`. The pinned
trace comparisons give `F(q_j) >= eta delta v_0 q_j`. On an escaping
ordinary orbit the values are distinct positive integers, so only
finitely many are below any fixed bound. Therefore its empirical
low-profile mass tends to zero. Applying the retained-law lower bound
to the high-profile event proves (10), including the infimum over `r`.

No exchange of a moving-root limit with fixed-root inverse recurrence
occurs in this argument. The result identifies the actual positive mass
which a collision completion must still control; it does not rule that
mass out.
