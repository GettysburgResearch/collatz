# T-8307 — Every eventually periodic six-branch type tail is nonpositive

Claim ID: `T-8307`  
Status: `PROPOSED / EXACT ORDINARY-SECTION EXCLUSION`  
Authoring agent: `gpt56-cycle-02`  
Created: 2026-07-23  
Dependencies: `T-8305`, `L-8309`  
Scope: ordinary positive intrinsic-core paths whose six-branch type tail is eventually periodic  
Related counterexample candidates: none

## 1. Period block

Assume an exact ordinary six-branch trajectory exists and that, after a finite prefix, its type sequence has period `p>=1`:

\[
i_{n+p}=i_n.
\tag{1}
\]

Move the starting index far enough that both endpoint type pairs repeat. Composing the exact intrinsic-core recurrence over one period cancels every type coboundary and gives

\[
\boxed{
2^{19p}x_{m+1}=3^{12p}x_m+B,}
\tag{2}
\]

where `x_m` is the core at successive period boundaries and

\[
B>0
\tag{3}
\]

is the positive affine toll of the period word.

Put

\[
Q=2^{19p},
\qquad
P=3^{12p}.
\tag{4}
\]

Then

\[
P>Q,
\qquad
\gcd(P,Q)=1.
\tag{5}
\]

## 2. Unique all-time integral point

The affine period map

\[
Qx'=Px+B
\tag{6}
\]

has the rational fixed point

\[
\boxed{
x_*={B\over Q-P}.}
\tag{7}
\]

Its denominator `Q-P` is odd, so

\[
x_*\in\mathbf Z_2.
\tag{8}
\]

For every finite iterate,

\[
\boxed{
x_m-x_*
=\left({P\over Q}\right)^m(x_0-x_*).}
\tag{9}
\]

If every `x_m` is an ordinary integer, then `x_m-x_*` belongs to `Z_2`, so

\[
\nu_2(x_m-x_*)\ge0.
\tag{10}
\]

But `(9)` gives

\[
\nu_2(x_m-x_*)
=\nu_2(x_0-x_*)-19pm.
\tag{11}
\]

Unless `x_0=x_*`, the right side is negative for all sufficiently large `m`, contradicting `(10)`. Therefore the sole all-time integral completion is

\[
\boxed{x_0=x_*.}
\tag{12}
\]

## 3. Sign obstruction

Because `B>0` and `Q-P<0`, the fixed point `(7)` is strictly negative in the real embedding:

\[
\boxed{x_*<0.}
\tag{13}
\]

Consequently no positive ordinary six-branch intrinsic-core path can have an eventually periodic type tail.

### Corollary — autonomous finite-state type generators fail

Every autonomous deterministic finite-state type generator emits an eventually periodic sequence. Hence no such generator can produce the type tail of a positive ordinary infinite six-branch path.

This does not exclude a controller that reads the unbounded core, changing top boundary, nonlinear quotient, stack, or another genuinely unbounded arithmetic state.

## 4. Relation to the constant-slope gauge

In the gauge of `L-8309`, one period has constant slope

\[
\lambda^p={P\over Q}>1
\]

and positive digit toll. Equation `(7)` is exactly the negative real fixed point of that expanding period map. The `2`-adic valuation argument proves that the periodic symbolic completion cannot secretly select a different positive ordinary point.

## 5. Gap audit

- The theorem excludes eventually periodic type tails, not arbitrary aperiodic tails.
- It does not exclude controllers with unbounded arithmetic state.
- It uses exact all-time integrality; finite periodic prefixes remain realizable.
- No positive infinite path, cycle, or Collatz conclusion beyond this type class is claimed.

## 6. Suggested next attack

The type schedule of a genuine witness must be aperiodic and generated from the changing ordinary core/top boundary. Use the constant-slope gauge to seek a nonlinear digit-selection invariant whose state grows with the actual quotient, not an autonomous symbolic schedule.
