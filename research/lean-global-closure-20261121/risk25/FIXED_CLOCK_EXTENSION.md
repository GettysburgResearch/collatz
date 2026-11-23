# The actual fixed-clock extension and the remaining carry energy

Date: 2026-11-23. Author: `/root/risk25_endpoint`.

**Status: a written consequence of the refreshed actual-law joining
theorem.** This follow-up is separate from the frozen critical carry
packet. It proves an exact product extension of the actual stationary
endpoint law in the critical iid branch. It gives no upper bound for
that endpoint law's collision, repeated-word density, or omitted mass.

## 1. Narrow refresh and exact pins

Only the following two new files were inspected. Their controls were
not replayed and their older corpus was not re-audited.

| Source | Exact object |
|---|---|
| PR180 | Head `7d4ad9f11d3d7a54c67b0c6cff4f13a2ab967161`; `research/profound-step-20261123/ENTROPY_ARITHMETIC.md`; blob `4530ed36c4f3ff6c9cf21149989e97cb94eb1714`; SHA-256 `b2906cada26d3bfbc3412423fb2b4ce4f0398c8d23518dcfd894f72ec58ff2f6` |
| PR182 | Head `cb1ae1bb4af0c8d082e9ff466b9fe0c84932301c`; `research/literature-round4-20261123/ACTUAL_LAW_RIGIDITY.md`; blob `2b875987b32ce8ee515c714fa330da77cc6cddde`; SHA-256 `a57e7aef865315ef3471a25e0fee18de4d6db75cf40455a0d658912666783e08` |

The original frozen contribution remains
`CRITICAL_CARRY_TRANSFER.md`, SHA-256
`cc45bcd43a450405b7b7cd12dd67fab45d43ac32caac3d875f5fdc5dca04b03d`.
The refreshed files do not require a correction to its statements.

## 2. Source-preserving density, with its exact limitation

PR180 proves the following under its pinned, source-qualified common
boundary construction. For the unchanged escaping source, let
`chi_j=3^j 2^(-A_j)` be its actual scales, `Z` its common real boundary,
and `mu_j` the conditional law after the common path has joined the
root `q_j`. Then almost every original boundary point has

`{iota(-chi_j Z):j>=N}` dense in `X_6` for every `N`.

Moreover, for every nonempty open `V`, the original conditional fibre
laws satisfy `sum_j p_j kappa_j(V)=infinity`. These conclusions use
upper local dimension one and bounded upward scale jumps. They do not
need a thickened measure with a vanishing retained coefficient.

This is a genuine improvement for the actual compact fibres. It gives
no positive time-frequency estimate. In the real fundamental domain,
the ternary coordinate still contains `-floor(-chi_j Z)` rather than
the original integer endpoint `q_j`. Thus the result does not bound
the original repeated-word density `J_m` or the omitted mass `tau_m`.
In particular, infinite occupation of every open compact cylinder
does not imply an exponentially small upper bound for endpoint
collisions at growing precision.

## 3. Exact product law for the endpoint and the profinite global clock

The following deduction uses PR180 Proposition 5, rather than its
source-qualified real-boundary theorem.

Fix one ordinary escaping source and a selected stationary time-limit
subsequence in the critical iid branch. Put

\[
 \ell=\log_2 3,\qquad
 \vartheta_j=\{j\ell\},\qquad
 K_j=\lfloor j\ell\rfloor-A_j.
\]

Let `eta` be the limiting two-sided gap process. In this branch it is
the positive geometric product law with mean `ell`. Proposition 5
states that, for every fixed positive integer `h`, every compatible
joint limit of the gap process, `vartheta_j`, and `K_j mod h` is

\[
 \eta\otimes\operatorname{Haar}_{\mathbb R/\mathbb Z}
      \otimes\operatorname{Unif}(\mathbb Z/h\mathbb Z).
 \tag{FC1}
\]

This fixed-modulus conclusion does not assert a rate as `h` grows.

**Consequence.** In the same joint limit, the full ternary endpoint
variable is independent of the phase and of the profinite global
clock. If `rho` denotes its actual stationary law, then the joint law is

\[
 \boxed{\rho\otimes\operatorname{Haar}_{\mathbb R/\mathbb Z}
              \otimes\operatorname{Haar}_{\widehat{\mathbb Z}}.}
 \tag{FC2}
\]

**Proof.** For any fixed endpoint precision `m`, the actual preceding
`m` gaps, in chronological order, determine its residue by

`q_j = 2^(-A(w)) C_w mod 3^m`, for all `j>=m`.

The initial exceptions have vanishing empirical proportion. This is
an exact identity, with the complete carry retained. Therefore the
endpoint residue is a measurable function of the two-sided gap
coordinate in every joint limit. Pushing (FC1) forward gives

\[
 \rho_m\otimes\operatorname{Haar}_{\mathbb R/\mathbb Z}
       \otimes\operatorname{Unif}(\mathbb Z/h\mathbb Z).
 \tag{FC3}
\]

The endpoint residues are consistent as `m` increases. Any finitely
many clock moduli are all factors of their least common multiple, so
(FC1) supplies their simultaneous product distribution as well.
Taking the inverse limits of the endpoint and clock cylinders proves
(FC2). This passage uses compact cylinder consistency, not a
growing-modulus convergence rate. `square`

This is an actual stationary-law extension. The profinite variable is
the **global scale clock**, not the source quotient or the complete
integer carry of a selected word.

## 4. What the product extension does to collision and to the transfer

At fixed endpoint precision `m` and fixed clock modulus `h`, (FC3)
gives the exact equality

\[
 \boxed{\operatorname{Col}(\rho_m,K\bmod h)
       =\frac1h\operatorname{Col}(\rho_m).}
 \tag{FC4}
\]

Conditioning on any clock residue recovers the unchanged endpoint
law. In particular, any collision gain obtained solely by observing
this extra finite label disappears when the label is forgotten.

The same statement is exact at the word level. Use a retained word
set `G_m`, its cardinality `L_m`, and original word masses `p_w`
as in the frozen carry packet. Write

\[
 J_m=L_m\sum_{w\in G_m}p_w^2,
 \qquad \tau_m=1-\sum_{w\in G_m}p_w.
\]

By (FC1), in the extension the mass of `(w,c)` is `p_w/h`. Against
the uniform reference on `G_m x Z/hZ`, the density energy is

\[
 \boxed{
  (L_mh)\sum_{w\in G_m}\sum_{c\bmod h}(p_w/h)^2=J_m,
  \qquad \tau_m^{\mathrm{extended}}=\tau_m.}
 \tag{FC5}
\]

Both quantities are also unchanged after conditioning on one clock
residue. Thus the strongest fixed-clock product joining supplied by
this refresh does not improve either term in the original transfer

\[
 \operatorname{Col}(\rho_m)
 \le\left(\sqrt{(R_m/L_m)J_m}+\tau_m\right)^2.
 \tag{FC6}
\]

There is no conflict between clock uniformity and the previously
proved actual strict collision gap. They concern different factors.
The map `K -> 2^K Z` is not a continuous function of the profinite
clock, so (FC2) supplies no distributional identity for the unbounded
real-scale carry.

## 5. What the refreshed finite ordinary construction contributes

PR182 constructs actual positive ordinary segments following a
periodic de Bruijn gap script. All sampled states are distinct, the
weights are the original uniform weights, and every block through a
prescribed finite depth has exactly a chosen rational Bernoulli law.
Every window has a period-dependent linear normalized-carry bound.
Nevertheless, the ternary endpoints lie in at most `d` script-phase
residues at every requested precision, giving collision at least `1/d`
even when the ordinary diagonal `1/N` is arbitrarily small.

For a script with `Delta=3^d-2^(A_v)>0` and phase carry `b_j`, the
exact original-source identity is

`2^(a_j)(Delta*q_j+b_j)=3^j(Delta*p+b_0)`.

Its binary divisibility forces

`2^(a_T)<=Delta*p+b_0`.

Consequently the source must grow with the requested horizon. The
construction is a finite ordinary witness to cross-source-box
aggregation; it is not a fixed escaping source, a stationary law of
one such source, or its canonical harmonic inverse law.

The quantified source payment is the reusable arithmetic part: a
single positive integer cannot follow one such expanding periodic
script indefinitely. A closing argument would still have to derive
sufficiently long same-source periodic structure from the actual
large `J_m`, or directly control the unbounded source quotients. Large
word energy alone is not a statement of periodicity, and neither
refreshed paper proves that implication.

## 6. Remaining target

No same-law bound `J_m=exp(o(m))` together with
`tau_m<=exp(-Phi(ell)m/2+o(m))` is obtained in this refresh. The
actual distortion-or-remainder alternative of the frozen packet
therefore remains the precise proved consequence. Its hypotheses
and its high-profile remainder have not been weakened or replaced by
a reference law.

This note uses the two cited files only at the stated written scopes.
It does not claim to independently verify their Lean companions or
the older qualified common-boundary construction. Collatz and the
original collision upper estimate remain open.
