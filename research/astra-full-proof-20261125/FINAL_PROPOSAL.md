# Final Lean proposal and the unclosed universal step

**Outcome: no complete proof of Collatz was obtained in this pass.** There is no new theorem asserting unconditional universal convergence. There is no admitted proof or custom axiom replacing the missing step. The proposal below is a concrete assessment of the new kernels and the remaining mathematics, rather than a conditional theorem renamed as the conjecture.

## 1. The target is an ordinary finite hit

With `step` and `run` from the existing `Collatz.SourceDeletion` module, the target proposition is

```lean
∀ n : Nat, 0 < n → ∃ h : Nat, run h n = 1
```

For an individual positive input, determinism gives the exact dichotomy needed in a proof: either some value repeats, giving an eventual positive cycle, or every value is distinct and the ordinary heights tend to infinity. Excluding only an escaping trajectory would leave the cycle obligation. Excluding a prescribed set of parity scripts would leave all other trajectories.

The existing least-disagreement and least-reverse-defect reductions remain available, with their different definitions preserved. In particular, unrestricted odd `¬Good z ∧ Good (3*z)` must not be silently identified with the canonical reverse defect `z ≡ 17 (mod 48)`. The new transport kernels apply to ordinary values with specified identities; using a leastness principle requires the appropriate predicate and size comparison as additional hypotheses.

## 2. What now works at arbitrary upper rank

Let `q` be a nonnegative integer. A signed reference numerator `a` is evolved with the odd branch `(3*a + 3^q)/2`. It is auxiliary data, not the ordinary source. If

\[
3^q z=a+2^{j+r}t,
\]

then the exact ordinary lift is

\[
3^q T^j(z)
 = A_j+2^r3^{o_j}t,
\]

where `A_j` and `o_j` are the signed reference endpoint and its odd count. `lift_signed` proves this endpoint identity and equality of the total odd counts. Agreement of each prefix parity follows from its one-step argument, or by applying the count identity at consecutive prefixes.

If the reference reaches an integral phase `b` with `o_j=q+m`, the denominator cancels and

\[
T^j(z)=b+2^r3^m t.
\]

This is useful in two different ways.

**An explicit replacement.** Two sources with possibly different upper ranks and different clocks meet when their integral signed phases and remaining monomials agree. `common_phase` proves equality of actual ordinary iterates and equivalence of basin membership for the `t=1` charts used in the replacement. `upper_certificate` separately constructs the replacement's upper hit, including its odd count. `replace_without_query` combines them: it does not infer a rank bound from an uncosted statement that the replacement's triple is good.

**Uniform contraction.** If the integral signed phase is a nonnegative periodic center with period `p` and odd count `o`, and `3^o < 2^p`, then `periodic_drop_eventual` supplies a finite explicit depth beyond which every positive terminal cofactor on that row contracts by any prescribed factor `B`. This applies at arbitrary prefix rank, subject to the seed identity, reference phase and odd count, and enough binary precision for the stated depth. It is not a theorem saying every upper certificate enters such a center.

On the specified canonical slice `27*z+5=2^(5+2*(k+1))*u` with odd `u>2`, `canonical_suffix` retains the same actual suffix of **every supplied** upper hit and saves exactly two odd inputs. Its output has good base `u` and bad multiple `3^k*u`; it does not claim that the orientation is still a reverse defect. `canonical_height` supplies the separate sufficient contraction for `k≥91`. The remaining smaller `k` need another justified move.

The missing transport claim is now concrete: for **each actual surviving least defect with its actual finite upper hit**, construct an ordinary smaller allowed defect, or an actual lower endpoint small enough for the proved return bound, with all certificate costs and source restrictions retained. The kernels can verify supplied data. They do not select such data universally. Negative signed centers and the coupled height/congruence conditions remain unresolved.

### Why the upper hit's clock cannot be the universal lower deadline

The new family

\[
z_m=\frac{2^{21+18m}-35}{27},\qquad H=21+18m,
\]

has a literal first hit `T^H(3*z_m)=1` using exactly two odd inputs. Nevertheless

\[
T^i(z_m)>z_m\quad(1\le i\le H),\qquad
T^4(z_m)=2^{H-4}-1,\qquad
T^H(z_m)=3^{H-4}-1.
\]

`NoEarlyDrop.no_early_drop` proves the infinite statement. Thus the supplied upper hit alone cannot imply a lower-drop deadline at the same clock for all ordinary sources. No member is known here to be bad or least, so the family does not refute a deadline theorem requiring additional badness or leastness hypotheses. These sources are `7 mod 16`, outside the canonical `17 mod 48` class.

## 3. An escape theorem with a genuine Lean topological core

The strongest new structural result concerns the entire unchanged ordinary trajectory. Suppose its heights are the values of a rational observable along a finite-dimensional rational dynamical system, all defined on that orbit. Then the heights eventually repeat.

The critical Lean theorem is `noetherian_finite_heights`. It states that a continuous update on a Noetherian space, with a clopen set of even heights and an actual natural-number Collatz height at each state, has finite height range. The theorem uses ordinary parity cancellation: equality of all future parities forces two natural-number heights to agree.

Here is why that theorem applies to a rational model. Give the actual hidden orbit its induced Zariski topology. It is Noetherian. On it, the rational expression

\[
\frac{2g(f(s))-g(s)}{2g(s)+1}
\]

is the parity bit. Its denominator is nonzero on every ordinary positive height, so the even fiber is clopen. Each irreducible component has one future parity sequence and hence one ordinary height. There are finitely many components. Poles away from the actual orbit and intersections between components do not invalidate this argument.

This also handles arbitrary-order rational recurrences with an explicit clock. A bounded degree and order that can fit *every finite prefix*, even with different coefficients at each horizon, already give one global rational recurrence: the finite-dimensional kernels of the fitting equations stabilize, and a generic vector over a rational function field avoids every denominator zero. With no clock variable and a fixed number of previous heights, an escaping orbit would require fitting degree growing at least linearly with the observation horizon. These are written consequences, not additional kernel-checked claims about algebraic geometry.

**Unproved universal input:** no rational model has been constructed for every ordinary Collatz trajectory. The actual implicit quadratic relation between successive heights is a two-valued algebraic correspondence. At each finite delay an escaping orbit would still have a recurrent parity word with two recurrent continuations. Neither finite-dimensionality of each delayed variety nor minimality of an integer counterexample turns that correspondence into a single rational map.

## 4. A second escape test: one scalar Mahler equation

For the actual trajectory, let `e_n` be its parity and let `E_n` count the earlier even inputs. Define

\[
F_x(z)=\sum_{n\ge0}e_n3^{E_n}z^n.
\]

The written theorem proves that eventual periodicity of the ordinary trajectory is equivalent to rationality of `F_x`, and also to the existence of any scalar `k`-Mahler equation for `F_x`, for some `k≥2` and arbitrary finite order.

The finite identity checked in Lean is

\[
3x+\sum_{j<n}e_j3^{E_j}(2/3)^j
=3\frac{2^n}{3^{Q_n}}x_n.
\]

At the dyadic place the right side tends to zero, giving `F_x(2/3)=-3x`. If the trajectory escapes, its distinct positive heights bound the real partial sums by `O_x(n^(1/3))`, so the real radius is at least `2/3` and the interior values are nonnegative. A Mahler lifting argument at a sufficiently late regular point, including a finite jet to remove possible singularities at the original point, would force the real meromorphic continuation there to have the same negative value. This is the contradiction. The real and dyadic raw sums are not equated without the lifting argument.

The external theorem is Adamczewski–Bell–Smertnig, Section 4, Theorem 4.3. The finite-jet argument, the infinite analytic conclusions and the automatic-block application are written mathematics, independently reviewed here; the external theorem has not been formalized in this packet. [Proof and exact hypotheses](global/README.md) · [Primary source](https://adamczewski.perso.math.cnrs.fr/HeightMahler.pdf).

**Unproved universal input:** the source identities `F_(2a)=3z F_a` and `F_(2a+1)=1+z F_(3a+2)` change the source index. They do not give a finite dilation equation for one fixed series. No argument here forces such an equation for an arbitrary ordinary counterexample. Every hypothetical positive cycle passes the Mahler test.

## 5. The cycle argument now allows arbitrary excursions

Write a primitive positive odd cycle as

\[
2^{a_i}x_{i+1}=3x_i+1,
\]

with odd period `p`, minimum `s`, and full reduced common denominator `d`. For the ordinary case `d=1`. A window whose endpoints lie at or below `K*s` may now contain arbitrarily high intermediate phases. `ExcursionBudget.lean` proves the clock charge for all high endpoints using clipped heights, and proves that a valuation word determines its terminal numerator modulo the full power `3^k`.

The written probability code assigns costs to the high-position mask, the entering valuations of high runs, and the possible low cumulative clocks. Together with the published Wu–Wang logarithm estimate this proves, for sufficiently large periods, that a cycle with at most `p/300` odd phases above `12s/5` has `d>p^(1/10)`. Hence an ordinary cycle must spend a positive proportion of its odd phases above `12s/5`, with no upper height cap. Larger thresholds and a two-gap refinement are explicitly source-qualified on the newer Chudnovsky preprint.

This is not all-cycle exclusion. High-occupation words still survive, and their full denominator is not proved greater than one. Iterating at a higher valley does not preserve the closed-lap identity. A separate exact construction shows that both actual size orders and the existing geometric tests permit more than `ln(3)/3` word entropy below the least-disagreement height ceiling. The constructed cycles have large denominators. Any next entropy argument must use ordinary numerator or least-basin arithmetic inside the windows, beyond those geometric tests. [Cycle proof](cycle/README.md) · [Quantified test of the entropy route](cycle/ORDER_ENTROPY.md).

## 6. What would complete the proof

There are two concrete possible completion routes after this pass.

1. **Finish the actual-certificate route.** Prove the universal selector described in Section 2 for the unchanged least defect, preserving its allowed source class and a genuinely well-founded cost. This can settle both escape and cycles without first classifying them.
2. **Finish both parts of the dynamical route.** Establish a universal boundedness bridge strong enough to invoke Section 3 or 4, and separately exclude every nontrivial ordinary positive cycle. The new cycle occupation estimate is only a necessary condition in the latter task.

Neither completion is supplied. Adding either unproved bridge as a Lean hypothesis would produce a valid conditional theorem, but would not meet the requested complete-proof target. The current proposal therefore ends with its actual verified components and exact open obligations.
