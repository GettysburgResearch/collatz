# Actual contact contraction, rational shadows, and a strict Green resolvent

This continuation develops three mathematical attacks in parallel from
PR185 at `7889fc680f5ee22237732eccc172b1699ef565da`, after reading the
new research in PR175, PR176, PR177, PR178, PR180, PR182, and PR183.
The source cutoff and exact file identities are in
[`SOURCE_SNAPSHOT.json`](SOURCE_SNAPSHOT.json) and
[`sources/latest-deltas.json`](sources/latest-deltas.json).

The strongest analytic result is a finite reference with geometric
collision contraction for the **actual next-contact transport**. A
second result completely controls the strict immigration correction on
one weighted Banach space, including an entire inverse and finite-clock
norm approximation below its endpoint weight. The arithmetic attack
turns a rational shadow into a certified descent of the original
ordinary target, retaining the full repeated-block denominator.

**Status:** the new finite arithmetic and algebraic cores are Lean
theorems. The countable and operator arguments are written deductions
from explicitly pinned source-qualified inputs. Universal Collatz
convergence, the last escaping excursion, and unrestricted positive
cycle exclusion remain open.

## 1. Contact returns have a finite contracting reference

Work on positive odd ternary units that are not themselves periodic,
killing forward transport on entry into a periodic state. Let `nu` be
the source-qualified ordinary harmonic flow, with

\[
L\nu=\nu,\qquad \frac\gamma q\le\nu(q)
\le\frac{V(q)}{\delta q},\qquad \delta,\gamma>0.
\]

For the contact section `C_M={V<=M}`, `M>=1`, set

\[
\rho=1-\frac{3\delta\gamma}{64M},\qquad
\sigma(q)=\nu(q)^2\mathbf1_{C_M}(q).
\]

Every contact target has two distinct actual unit parents with binary
exponents at most six. Each parent receives a uniformly positive
fraction of the target's harmonic mass. A proper ancestor uses only one
of these branches, so its mass is at most `rho` times the target mass.

If `J` moves each original contact source to its next actual forward
contact, the resulting theorem is

\[
\boxed{\sum_q\sigma(q)\le2(M/\delta)^2,\qquad
J\sigma\le\rho\sigma,\qquad
\mathcal E_\sigma(J^k a)\le\rho^k\mathcal E_\sigma(a),}
\]

where `E_sigma(a)=sum a(q)^2/nu(q)^2`. Exact source collisions remain
inside the square; each source is charged to its unique next target.
Consequently surviving source mass decays geometrically in contact
time. Forward contact heights satisfy

\[
q_k\le\frac M{\delta\gamma}\rho^kq_0.
\]

The number of visits is logarithmically bounded in the original source
height. In the inverse direction, contact heights grow exponentially,
so the costs `log(2+q)^(-A)` are summable for every `A>1` along every
realized inverse contact-return chain.

The clock here counts contacts. A source with no next contact is killed
by `J`, including a possible escaping source after its last contact.
Ordinary excursion durations and that final exit retain their own terms.

Full proof: [`CONTACT_RETURN_FINITE_REFERENCE.md`](CONTACT_RETURN_FINITE_REFERENCE.md).
Finite formal core: [`lean/ContactReturnContraction.lean`](lean/ContactReturnContraction.lean).

## 2. The strict Green correction has an entire inverse

On the same killed domain put

\[
S=\sum_{j\ge0}L^j,\qquad
Da(n)=\frac{a(n)}{3n+1},\qquad K=SLD.
\]

This operator transports the actual immigration correction at each
strictly later physical endpoint. For
`X_s=ell^1(N,n^(-s))`, `39/40<s<=1`, the pinned actual-path occupation
bound gives

\[
\boxed{\|K^j\|\le A_s\frac{C^{j-1}}{(j-1)!},\qquad
A_s=\frac{5s}{3(s-39/40)},\quad C=200/3.}
\]

The reason for the factorial is concrete: an application of `K^j`
chooses `j-1` strictly ordered intermediate states on one actual path.
The elementary symmetric sum of their weights is bounded by a power
of the full path-weight sum divided by `(j-1)!`.

Thus `K` is compact and quasinilpotent on that one space, and

\[
\boxed{R(z)=(I+zK)^{-1}
=I+\sum_{j\ge1}(-z)^jK^j\quad(z\in\mathbb C).}
\]

The written proof also provides the exact product kernel, explicit
finite input/output errors, and operator-norm convergence of physical
clock truncations for `39/40<s<1`. At `s=1`, an explicit convergent
inverse ladder proves a uniform odd-clock truncation error at least
`1/15`. Every witness in that ladder reaches 5 and then 1; no unproved
escaping orbit is used for the endpoint obstruction.

Full proof: [`STRICT_GREEN_VOLTERRA.md`](STRICT_GREEN_VOLTERRA.md).
Formal cores: [`lean/StrictGreenKernel.lean`](lean/StrictGreenKernel.lean)
and [`lean/OddDepthLadder.lean`](lean/OddDepthLadder.lean).

## 3. Rational shadows compile successful ordinary descent

A repeated contracting source block has rational fixed point `C/D`.
Its exact physical divisibility pins the original source in the form

\[
Dr-C=2^H t.
\]

For an affine target `n=Ar+B`, set `h=AC+DB`. The finite rational
numerator trajectory with denominator `D` uses the update

\[
h\longmapsto
\begin{cases}
h/2,&h\text{ even},\\
(3h+D)/2,&h\text{ odd}.
\end{cases}
\]

If its first `J<=H` steps have `o` odd steps and endpoint `h_J`, the
**actual ordinary target** obeys

\[
D T^J(n)=3^o A2^{H-J}t+h_J.
\]

Therefore a multiplier saving large enough to pay `h_J-h` proves
`T^J(n)<n`. This converts a finite rational-prefix certificate into a
successful ordinary descent, without resampling a source or assuming
eventual periodicity of rational trajectories.

For target `9r+2`, certified source prefixes include three consecutive
gaps 2, two consecutive gaps 3, and forty-eight consecutive gaps 4.
The conclusions hold for every positive source carrying that physical
prefix, with an arbitrary remaining source tail. The source fixed-point
exception is treated explicitly. The broader arbitrary changing source
language still needs a successful certificate or another proved exit.

The composed Lean theorem takes the actual repeated source trace, a
unit-displacement payment inequality, and the explicit fixed-point case,
and concludes descent for every supplied source. The full compiler proof
and its exact formal scope are recorded in
[`RATIONAL_SHADOW_DISPATCH.md`](RATIONAL_SHADOW_DISPATCH.md) and the
accompanying Lean modules.

## 4. The combined route retains its last-contact boundary

The two analytic attacks have an exact common interface. For a finite
nonnegative original source `eta`, define
`T_lambda a=L((1-1/(3n+1))*a)` and `S_lambda=sum T_lambda^j`. Then

\[
\boxed{\delta S\eta\le R(1)S\eta=S_\lambda\eta\le S\eta.}
\]

The stronger domain theorem is

\[
I-T_z=(I-L)(I+zK),\qquad
\ker(I-T_z)=R(z)\ker(I-L),
\]

on the same maximal transport domain, with equality of the actual ranges
of `I-T_z` and `I-L`. At `z=1`, this gives an order isomorphism of all
positive harmonic solutions, with `delta*nu<=R(1)nu<=nu` and the sharper
operator bound `||R(1)||<=1+A_s`. See
[`HARMONIC_KERNEL_FACTORIZATION.md`](HARMONIC_KERNEL_FACTORIZATION.md).
This is a right factorization, not an assertion about the whole transport
spectrum.

The finite-source identity follows by telescoping the multiplicative
correction along each physical path. It shows that the resolvent preserves positivity on the
finite-source Green cone containing PR176's last-contact measure. A
positive escaping component capacity remains positive under this
correction. The operator identity and contact contraction therefore
cannot by themselves remove the final ordinary excursion.

[`EXCURSION_RESOLVENT_INTERFACE.md`](EXCURSION_RESOLVENT_INTERFACE.md)
gives the detailed source-preserving calculation. The exact terminal-flux identity and capacity bound are in
[`CONTACT_EXIT_ACCOUNTING.md`](CONTACT_EXIT_ACCOUNTING.md). An actual-law bounded optional-stopping comparison replaces the old
full-prefix factor by a normalized contact error plus an explicit
entrance-time tail. Its proof, the Haar maximal estimate, and the still
open stopped correlation are in
[`STOPPED_MIXING_INTERFACE.md`](STOPPED_MIXING_INTERFACE.md).
The cycle attack is recorded separately in [`CYCLE_ATTEMPT_LEDGER.md`](CYCLE_ATTEMPT_LEDGER.md):
it derives a finite inverse certificate for every actual positive cycle,
but its depth remains a physical cost. Results already present in the
latest repo are identified as prior work.

## 5. Evidence and replay

The pinned runtime is Lean 4.34.1 at
`5045d0056413266e57c625dcd7c365b10e377c52` and Mathlib at
`d13f23b723b8a846827a245b89c10fc7d3f11612`.
[`check.py`](check.py) compiles only the new modules and their required
source dependencies in a fresh external build directory. It treats
warnings as errors, audits every new public theorem, rejects nonstandard
proof axioms, and runs the required complete-checkout repository gate.
The three rational-shadow certificates are also checked in normal and
optimized Python, with seven damaged controls rejected in each mode.
Earlier research packets and their receipts are preserved unchanged.

```bash
python -X utf8 -B research/multiple-attacks-20261122/check.py \
  --lean /absolute/path/to/lean \
  --mathlib /absolute/path/to/pinned/mathlib \
  --build-dir /absolute/path/to/empty/external/build
```

Run from a clean complete checkout. The driver writes its receipt,
compiler logs, source-port diff, and compiled artifacts outside the
repository. Actual publication and replay results belong in
`reports/multiple-attacks-20261122/`, separate from the scientific notes.

The finite Lean cores establish their stated identities and inequalities.
They do not formalize the construction of the canonical potential, the
ordinary harmonic flow, the countable operator arguments, or universal
Collatz convergence. The cited analytic dependencies retain their
source-qualified status.
