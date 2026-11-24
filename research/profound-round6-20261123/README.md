# The actual arithmetic germ detects every nonstandard positive cycle

23 November 2026. Round six, extending
`afe6f4d1a661b377c9daa4623bdd732ba478386b` on PR182.

**Full Collatz remains OPEN.** This packet gives an independently reviewed
written obstruction for every hypothetical nonstandard positive cycle,
with its finite polynomial and cycle arithmetic checked in Lean. Combined
with the exact, source-qualified arithmetic-germ theorem in PR178, it
strengthens that route from eventual periodicity to convergence to one.
The construction of the required germ for an arbitrary ordinary source
and existence of its limiting parity density remain unproved.

The main advance is to keep the whole Taylor expansion at the binary
interpolation point. A denominator prime may disappear from the known
value there and still be forced, to growing powers, into higher coefficients.
The separate collision lane proves a finite ordinary-source packing bound
and quantifies the missing rate needed to transfer it to a stationary law.

## 1. One actual source and its full translated series

Use the shortcut map `T(n)=n/2` for even `n`, and `(3n+1)/2` for odd `n`.
Fix one positive ordinary integer `n`, and put

\[
x_k=T^k(n),\qquad e_k=x_k\bmod2,\qquad p_k=\sum_{i<k}e_i,
\]
\[
B_n(z)=\sum_{k\ge0}e_k3^{-p_{k+1}}z^k,
\qquad J_n(t)=B_n(2+t)=\sum_{j\ge0}c_jt^j.
\]

The second series is the literal Taylor expansion of the binary analytic
function of this source. The complete affine identity gives `c_0=-n` in
`Q_2`. It does not give rationality of the other coefficients.

Suppose this actual source is eventually periodic. Let its cycle have
shortcut length `A` and odd count `p`, and set

\[
g=\gcd(A,p),\qquad u=A/g,\qquad v=p/g,
\qquad D_{\rm red}=2^u-3^v>0.
\]

The new quantitative statement is

\[
\boxed{
\text{for every prime }\ell\mid D_{\rm red},\quad
\limsup_{j\to\infty}
\frac{v_\ell(\operatorname{den}(c_j))}{j}
\ge\frac{v_\ell(D_{\rm red})}{u}>0.
}
\]

The proof applies to every cycle word and every actual finite prefix,
with no period bound. It first retains the complete repeated-block
denominator. The positive real pole cannot cancel because the complete
chronological numerator is positive there. The irreducible factor
`z^u-3^v` therefore remains in the reduced polynomial denominator, and
all its conjugate poles survive at every completion. Their translated
`ell`-adic distances give the displayed denominator-growth rate.

This rate retains the full valuation in `D_red`. It does not assert that
every factor of the larger number `2^A-3^p` survives. The choice of
`D_red` is justified by polynomial noncancellation before any evaluation,
not by replacing full-cycle integrality with a proper-factor test.

The complete proof is in [RATIONAL_SELECTION.md](RATIONAL_SELECTION.md),
claims R6-SEL-1--3. [CYCLE_ARITHMETIC.md](CYCLE_ARITHMETIC.md) independently
reconstructs the pole argument and proves the ordinary-cycle arithmetic.
The exact review is [JET_REVIEW.md](../../reports/2026-11-23-profound-round6/JET_REVIEW.md).

## 2. Why this excludes all other cycles under a ternary germ hypothesis

For the positive ordinary odd states `q_i` of a cycle, the actual equations
give

\[
3^p<2^A=\prod_{i=1}^p\left(3+\frac1{q_i}\right)\le4^p.
\]

If `D_red=1`, then `2^u=3^v+1`. A modulo-eight calculation forces
`(u,v)=(2,1)`, so `A=2p`. Equality in the product bound forces every odd
state to be one. Hence a nonstandard positive ordinary cycle has
`D_red>1` coprime to six, and supplies a denominator prime other than three.

Consequently, for a source already known to be eventually periodic,

\[
\boxed{J_n\in\mathbb Z[1/3][[t]]
\quad\Longleftrightarrow\quad n\text{ reaches }1.}
\]

This is an unrestricted conditional cycle theorem, not an unconditional
exclusion of hypothetical nonstandard cycles.

Define **J3** to require that the full actual germ has coefficients in
`Z[1/3]` and positive convergence radii at the complex and ternary places.
The frozen PR178 theorem, at
`398b3a04da071e96362005792417bd5cf8cc6497`, gives eventual periodicity from
such a germ when the actual parity density has a limit. Its external input
is Chambert-Loir--Noûs's multipoint rationality theorem, with its integral
model, local realizations, and strictly positive potential-game value.
The source hypotheses and its small-hole estimate were independently
reconstructed in the review; the general analytic theorem is not a Lean
result here.

The strengthened conclusion is therefore:

\[
\boxed{
\text{For a fixed positive ordinary source with limiting parity density,}
\qquad J3(n)\ \Longleftrightarrow\ n\text{ reaches }1.
}
\]

The converse has a stronger explicit denominator statement. If an actual
prefix `a` reaches one after `tau` steps and contains `s` odd inputs, then

\[
3^sJ_n(t)=C_a(2+t)-\frac{(2+t)^\tau}{1+4t+t^2}
\in\mathbb Z[[t]].
\]

One common denominator `3^s` clears the entire germ. Its complex radius
is at least `2-sqrt(3)`, its ternary radius at least one, and its limiting
parity density is `1/2`. The parameter `s` comes from known convergence;
this formula does not construct it for an arbitrary source.

## 3. An exact control against value-only cancellation

The positive odd-denominator rational cycle with word `110000` starts at
`1/11`. It is not an ordinary integer cycle. Its weighted series is

\[
B(z)=\frac{3+z}{9-z^6},\qquad D=55,\quad C(2)=5,
\quad D_{\rm red}=5.
\]

At the known interpolation value and the first derivative,

\[
B(2)=-\frac1{11},\qquad B'(2)=\frac{181}{605}.
\]

The factor five cancels from the value and reappears in the derivative.
In fact its denominator exponent is exactly `j` at every Taylor order
`j>=1`; [EXACT_CONTROLS.md](EXACT_CONTROLS.md) supplies the short recurrence
induction and distinguishes it from the 31 finite replay checks.

For a general ordinary source, even rationality of `d(n)=B_n'(2)` is
not established here. Its exact tail cocycle is

\[
2d(Tx)=3^{x\bmod2}d(x)+Tx.
\]

The actual convergent source `85` has `d(85)=0`, so positivity or
nonvanishing cannot be used as a universal derivative invariant.

## 4. The separate actual-source collision result

Let `pi_N` be the empirical law of `N` distinct ordinary states from one
orbit, with maximum `H_N`. Keeping every ordered pair and its complete
ordinary quotient gives, for every positive modulus `Q`,

\[
\frac1N\le\operatorname{Col}_Q(\pi_N)
\le\frac{\lfloor H_N/Q\rfloor+1}{N}.
\]

If `Q>H_N`, every collision is an ordinary diagonal and the lower bound
is an equality. For any comparison probability law `mu`, the full
collision and total-variation norms satisfy

\[
\|\pi_N\bmod Q-\mu\bmod Q\|_{\rm TV}
\ge\frac1{\sqrt2}
\left(\sqrt{\operatorname{Col}_Q(\mu)}
-\sqrt{\frac{\lfloor H_N/Q\rfloor+1}{N}}\right)_+.
\]

This yields an explicit obstruction to fast comparison at growing
modulus. If `H_N<=N^(beta+o(1))`, a proposed limiting law has collision
at least `c Q^(-d)`, and `Q=N^(kappa+o(1))`, then
`kappa*d<1` and `beta<1+kappa*(1-d)` force discrepancy at least
`(sqrt(c/2)-o(1))*Q^(-d/2)`.

The sharp critical iid model in the pinned PR180 has order-two exponent
about `0.705155598`, rather than its Shannon exponent about `0.949955527`.
This application retains its model hypothesis; no iid law is substituted
for an ordinary orbit. The new bound identifies the necessary missing
comparison rate and does not prove it. See
[COLLISION_CLOSURE.md](COLLISION_CLOSURE.md) and its
[independent review](../../reports/2026-11-23-profound-round6/COLLISION_REVIEW.md).

## 5. Formal and computational evidence

| Artifact | Checked scope |
|---|---|
| [RationalSelection.lean](RationalSelection.lean) | Seven all-word finite theorems: chronological carry-polynomial concatenation, positivity, and noncancellation at the positive root |
| [CycleArithmetic.lean](CycleArithmetic.lean) | Six arithmetic theorems: product derived from actual cycle equations, clock positivity, equality rigidity, and a reduced-clock prime away from two and three |
| [CollisionClosure.lean](CollisionClosure.lean) | Four finite-source theorems: recovery from residue/quotient, complete pair count, rational-probability normalization, and exact diagonal |
| [exact_replay.py](exact_replay.py) and [replay_jets.py](replay_jets.py) | Exact finite rational-cycle, ordinary-source Taylor, and full collision controls; explicit guards remain active under `python -O` |

All 17 new public statements passed a fresh local dependency build and
axiom audit with Lean 4.34.1 and the pinned Mathlib. Only `propext`,
`Classical.choice`, and `Quot.sound` appeared. The analytic radius theorem,
binomial irreducibility application, multipoint rationality, and stationary
limits remain written mathematics with the precise source boundary above.

Both normal and optimized exact replay passed with byte-identical output:
1,578 primitive positive rational words through length ten, 14,338 literal
rational steps, 4,192 independently constructed Taylor coefficients across
131 ordinary convergent sources, and 409,264 complete ordered collision
pairs across 2,071 actual source/modulus cases. These are bounded controls.

[SOURCES.json](SOURCES.json) pins the selected current repository and
primary literature inputs. The
[execution and review report](../../reports/2026-11-23-profound-round6/README.md)
records compiler commands, source hashes, exact counts, and checkout gates.
Prior scientific checkpoints, including the original dyadic-band work,
remain preserved. No historical-priority claim is made.

## 6. The next mathematical obligation

The main conditional route now asks for a construction of the **actual**
J3 germ, together with a limiting parity density, or a proved source
condition that replaces those assumptions. A fitted finite germ, the
constant value `-n`, and a finite filter do not supply it. The collision
route still needs an actual-source comparison at growing resolution or
a direct stationary collision upper. The full pressure lane likewise
retains its unproved lower comparison. None of these gaps is declared
closed by the finite Lean core or exact replay.
