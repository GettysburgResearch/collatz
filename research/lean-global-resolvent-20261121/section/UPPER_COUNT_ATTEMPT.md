# Attempt to close the actual-section survivor count

**Status: OPEN.** This note records a fresh attack on the upper estimate after
the new inverse population was proved. It does not introduce an axiom or a
claimed proof of convergence.

Use the ordinary shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]

The marked set is the original PR173 set: odd `x`, with `d=floor(log_2 x)`,
satisfying `(d+1)(x-2^d) <= 70*2^d`.

## 1. The precise upper estimate under attack

At an admissible scale `Q`, let `S_Q(t)` count marked `x<2^(10Q)` that have
not visited one at any shortcut clock from zero through `t`.
The new construction gives `2^Q` distinct marked ancestors of each supplied
positive ternary unit `a<=2^Q`. Their clocks to `a` lie in
`[7Q-5,11Q)`.

The attempted closing assertion is

\[
\forall K\ \exists Q\ge K,\ t:\quad Q\text{ admissible},
\qquad S_Q(t)<2^Q.
\]

The root composition proves that this assertion is equivalent to full
convergence. This attempt did not establish the displayed inequality.

## 2. Why the available finite parity count does not close it

An initial integer interval of length roughly `2^D` permits exact parity
counting for the first `D` shortcut decisions. The usual large-deviation
calculation concerns descent below the *starting value*. It does not count
visits to the fixed value one.

This distinction persists after restriction to the marked set. If `m` is a
least nonconvergent integer, its constructed marked ancestors can descend
all the way to `m`, while avoiding one forever. Those ancestors can therefore
pass a relative-descent test without leaving `S_Q(t)`.

The leading-bit restriction defining a mark fixes only about `log_2 D` bits
at binary length `D`. It does not provide new independent low bits after the
first `D` parity decisions. Applying a fresh binomial law at every subsequent
marked return would require a new ordinary-trajectory theorem. No such
theorem was proved in this attempt.

## 3. Population amplification remains a lower estimate

The pooled population theorem gives, for any finite set of bad unit sources
`A` below `2^Q`,

\[
2^Q |A|\le(4Q+5)S_Q(t)\qquad\text{for every }t.
\]

The inequality is compatible with the marked set's known size. Even if one
strengthens it to permit iteration at every successive scale, and ignores
polynomial losses, the idealized recurrence `B(10Q) >= 2^Q B(Q)` permits
exponent `1/9`: a population of order `X^(1/9)` fits inside a section of
size `O(X/log X)`. The actual admissible scales are only proved cofinal;
closure of those scales under multiplication by ten is not asserted. This calculation is a scope check on this particular
amplification inequality, not an impossibility theorem for stronger inverse
constructions.

The supplied power-weight and critical marked-weight arguments have the
same issue. At height `2^(10Q)`, a fan of `2^Q` leaves can contribute only
an exponentially small total to a decreasing summable weight. Thus these
lower populations do not contradict finiteness of the section's weighted
mass. A source-sensitive return or absorption estimate is still required.

## 4. Coupling to the newest logarithmic predecessor result

The written PR180 derivation at
`f87cb69b3dd86257731ddfbab58c87bf3b5f63d6`,
[LINEAR_BLOCK_ATOM_FLOOR.md](https://github.com/GettysburgResearch/collatz/blob/f87cb69b3dd86257731ddfbab58c87bf3b5f63d6/research/lean-ordinary-closure-20261121/LINEAR_BLOCK_ATOM_FLOOR.md),
asserts, using Tao's fine-scale mixing theorem, a constant `c>0` such that
every positive ternary unit `a` has lower logarithmic predecessor density
at least

\[
\frac{c}{44a\log(64/3)}.
\]

This is a **source-qualified analytic dependency**, not a new Lean theorem
or an independently completed review here. Its companion
`REPOSITORY_RIGIDITY_COROLLARY.md` keeps finite five energy as the open
hypothesis.

Even granting that lower bound, the new section construction supplies no
upper fixed-floor density. There is, however, a precise stronger analytic
target: if one could prove that the logarithmic density of starts whose
entire orbit avoids `{1,...,K}` is `o(1/K)`, with a uniform bound strong
enough to compare with the constant above, then all sufficiently large
least counterexamples would be excluded.

Indeed, let `m` be a least counterexample. It is odd. It is itself a ternary
unit, or its next shortcut value is a unit `a<=2m`. Every predecessor of
that `a` avoids `{1,...,m-1}`. The quoted lower bound would therefore force
the fixed-floor survivor density to be at least

\[
\frac{c}{88m\log(64/3)}.
\]

An `o(1/K)` upper bound at `K=m-1` contradicts this for large `m`; an actual
finite verification up to the resulting threshold would handle the rest.
Neither the required quantitative upper bound nor an effective threshold
was established. Ordinary almost-boundedness, whose floor is allowed to
grow with the input, is not substituted for this assertion.

## 5. A clock consequence useful for future experiments

The new section count cannot pass at a very early linear clock. Choose the
unit target `a=5`, available at every admissible scale. Each of its `2^Q`
constructed leaves reaches five only at a supplied clock at least `7Q-5`.
None can have visited one earlier: the forward orbit of one is `{1,2}` and
never reaches five. Thus the same leaves force

\[
S_Q(7Q-6)\ge2^Q.
\]

This is an elementary written consequence of the checked clock theorem;
it was not separately formalized here. It restricts observation-time
experiments and does not rule out a later passing clock.

## Outcome

No upper survivor estimate, complete ranked selector, or unconditional
multi-return descent was obtained. The remaining inference is still a
statement about **actual ordinary trajectories avoiding a fixed floor**.
The new band geometry and the new inverse multiplicity are both available
without supplying that statement.
