# Actual clock dissipation under repeated contact resets

**Status: source-qualified written theorem, with a five-theorem Lean
arithmetic certificate. No exclusion of escaping Collatz orbits.**

The actual forward/contact family `Pi L^k` in
[ORDINARY_BOUNDARY.md](ORDINARY_BOUNDARY.md) has a strong finite-`Lp`
limit against one finite reference. Repeating the one-step reset gives
a different operator, `Q=Pi L`. On the last contacts of any hypothetical
escaping component, this repeated-reset chain has an integer clock that
tends to minus infinity almost surely. It has no nonzero finite
stationary measure. The distinction retains the actual inverse hitting
depth; the two compositions cannot be interchanged.

## 1. Inputs and the exact reset clock

Use the same retained nonperiodic odd-unit domain `N`, positive ordinary
harmonic flow `nu`, and contact set `C2={V<=2}` as in
`ORDINARY_BOUNDARY.md`. Its pinned PR185 and PR176 inputs supply
`Lnu=nu`, `nu(q)>=gamma/q>0`, and almost-sure inverse first contact at
every retained root. The actual integer coordinate on an escaping
component is the one from PR183's `WOLD_CHANNELS.md` and
`ASYNCHRONOUS_RESIDUE.md`, at
`68345f60a4f757acb42a69a4ac95910f8ce26163`:

\[
h_C(Ux)=h_C(x)+1.
\tag{Q1}
\]

Fix one escaping component `C` and its last-contact set
`Lambda=Lambda_0 intersect C`. If `x` is in `Lambda`, its forward
successor `q=Ux` is retained, is not a contact, and has no future
contacts. The inverse first-contact law `mu_q` is supported on
`Lambda`. Define the Markov kernel

\[
Q(x,y)=\mu_{Ux}(y).
\tag{Q2}
\]

For an actual first-contact path from `q=Ux` to `y`, let `tau>=1` be
its inverse depth, so `U^tau y=Ux`. Equations (Q1)--(Q2) give the exact
clock identity

\[
\boxed{h_C(y)-h_C(x)=1-\tau\le0.}
\tag{Q3}
\]

No expected hitting time is assumed finite. The path depth is retained
in (Q3), even though the reset operator itself records only its endpoint.

## 2. Every ordinary unit target has an actual noncontact parent

For every positive odd ternary unit `q`, choose `1<=e<=54` with

\[
2^e q\equiv52\pmod {81}.
\tag{Q4}
\]

Such an exponent exists. One elementary verification is that
`2^54=1 mod81`, `2^27=-1 mod81`, and `2^18=28 mod81`, so the order is
54 and its powers exhaust the 54 unit residues. The Lean module instead
checks the entire finite coverage statement directly by kernel reduction;
it does not assume that generator claim.

Because `2^e q` is even, (Q4) gives an integer `s>=0` such that

\[
2^e q=162s+52,
\qquad p=54s+17,
\qquad 3p+1=2^e q.
\tag{Q5}
\]

Thus `p` is a positive odd unit and `U(p)=q` with its exact valuation
`e`. It has two genuine gap-one unit predecessors:

\[
24s+7\ \longmapsto\ 36s+11\ \longmapsto\ 54s+17=p.
\tag{Q6}
\]

The canonical floor and its two critical excessive edge inequalities
therefore imply

\[
\boxed{V(p)\ge(3/2)^2 V(24s+7)\ge9/4>2.}
\tag{Q7}
\]

When `q` is retained, its parent `p` is also retained: a periodic parent
would have a periodic successor. Starting the inverse walk at `q`, the
first step to this noncontact `p` has positive probability
`nu(p)/nu(q)`. Almost-sure contact from `p` then requires at least one
more inverse step. In particular, for `q=Ux` from Section 1,

\[
\boxed{
Q\bigl(x,\{y:h_C(y)<h_C(x)\}\bigr)
\ge\frac{\nu(p)}{\nu(q)}
\ge\frac{3\gamma}{2^{54}q\nu(q)}>0.}
\tag{Q8}
\]

The last inequality uses `p<2^54 q/3` and `nu(p)>=gamma/p`.
This is a positive lower bound at each fixed root, not a uniform lower
bound along all possible reset trajectories.

## 3. Repeated resets are transient in the actual clock

Let

\[
\beta(q)=\Pr_q(\tau=1)
=\sum_{\substack{y\in\mathcal C_2\\Uy=q}}
                              \frac{\nu(y)}{\nu(q)}.
\tag{Q9}
\]

For the post-contact roots under consideration, `0<=beta(q)<1` by
(Q8). If one reset has depth exactly one, its endpoint `y` obeys
`Uy=q`. Therefore the **next** reset again uses the identical law
`mu_q`. While the integer clock stays unchanged, all reset endpoints
are contact parents of this same `q`, and the probability of another
unchanged-clock step remains exactly `beta(q)`.

The probability of `r` consecutive unchanged-clock resets is
`beta(q)^r`, which tends to zero. A strict decrease consequently occurs
after finitely many resets almost surely. Repeating this argument after
each strict decrease proves

\[
\boxed{h_C(X_k)\longrightarrow-\infty\quad\text{almost surely}}
\tag{Q10}
\]

for the `Q` chain starting at any last contact `X_0`. Only finitely many
successive waiting stages are needed to cross each prescribed integer
threshold, and a countable intersection gives (Q10). There is no claim
of a uniform rate or finite mean waiting time after averaging over the
successive roots.

Every finite set of last contacts has a finite minimum clock. Thus the
probability of each such finite set tends to zero. A nonzero finite
initial measure obeys the same conclusion by summing the individual
probability bounds. In particular the family `Q^k` applied to any
nonzero probability measure on these escaping last contacts is not
uniformly tight.

### No nonzero finite stationary measure

There is also a direct proof that does not use (Q10). Take any bounded
strictly increasing function of the integer clock, for example
`phi(t)=arctan(t)`. Equations (Q3) and (Q8) imply at every state `x`

\[
\sum_y Q(x,y)\phi(h_C(y))<\phi(h_C(x)).
\tag{Q11}
\]

If a nonzero finite positive measure `rho` were stationary, integrate
(Q11) against `rho`. The integrands are bounded, so both sums are
absolutely integrable and can be interchanged. Their strict difference
has positive integral, contradicting stationarity. No first moment of
`h_C` or of `tau` is needed. The argument also rules out a finite
stationary measure spread over multiple escaping components by
restricting it to one component of positive mass.

## 4. What the clock calculation resolves

When escaping mass is present, the limit `b_infinity` in (B39) of
`ORDINARY_BOUNDARY.md` is a nonzero finite measure on these last
contacts. It satisfies `Pi b_infinity=b_infinity`, because first contact
at a contact has depth zero. But (Q11) proves

\[
Qb_\infty\ne b_\infty.
\tag{Q12}
\]

Thus `Pi L^k a` has the established strong limit, while `(Pi L)^k`
discards a new inverse depth at every step and drifts to clock minus
infinity. Uniform domination for the first family cannot be imported
into the second family. This calculation identifies the exact loss in
an attempted iteration of the common-reference theorem. It does not
prove that the hypothetical escaping component is absent, and says
nothing about additional periodic components outside the killed domain.

## 5. Formal scope

[ContactClock.lean](lean/ContactClock.lean) checks five public theorems:
the finite unit-residue cover, its lift to arbitrary unit integers, the
actual parent with its exact odd valuation, the two unit gap-one
predecessors, and the scalar consequence `V(p)>=9/4`. All five compiled
with Lean 4.34.1 and warnings as errors; their axiom audits use only
`propext`, `Classical.choice`, and `Quot.sound`. The infinite
first-contact and Markov-chain arguments above retain their written,
source-qualified status. No such analytic premise is installed as a
Lean axiom.
