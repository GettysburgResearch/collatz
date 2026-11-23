# Independent review of FastForward.lean

The review covers the six theorem declarations through `lower_marked_partner`, as read from the root's scratch source. Compilation of those declarations remains owned by the root. The mathematical review found no gap in the phase estimates, ordinary-clock accounting, height ceiling, or physical merger equation.

## Constants and quantifiers

- `grid_drop_or_mark`: `q > 0` suffices. The floor is `q*q`. From `j < q`, the rational-rotation error is at most one after multiplying by `q`, and `q*e <= 1`. The rational grid lies between one and two, so the resulting actual phase lies above its displayed integer and has `q*Delta <= 4`.
- The same actual endpoint has `x < 2^(2*q)`, since `n < 2^(q+1)` and `j+q+1 <= 2*q`. Thus `d(x)+1 <= 2*q`, and its phase product is at most eight, comfortably inside the existing threshold 35.
- The proof correctly invokes `section_of_phase` without asserting that the displayed integer is the floor of the logarithm. That lemma works with any integer below the logarithmic height. Consequently the finite theorem needs no additional `q >= 16`; that bound enters only through the pre-existing `GoodScale` definition.
- `bounded_visit_of_grid` handles even inputs by stripping their initial twos and accounts for those halvings inside `t`. The exact bound `2^t <= 4^j*n` gives `t <= 2*j+d(n)`, even when the selected endpoint is smaller than the source.
- In the floor-crossing branch `sqrt(x) <= q` and `d(x) < 2*q`; the older entrance theorem therefore adds fewer than `6*q` clocks. Together with `j < q`, this proves the stated strict bound `< 8*q+d(n)`. The proof does not use the unavailable assumption that the endpoint exceeds the source.
- `uniform_visit_at_good_scale` has `d(n) <= q` from the full source range `n <= 2^q`, hence the strict `< 9*q` clock.
- `orbit_growth` is valid including zero, because the shortcut map obeys `T(v) <= 2*v` for every natural `v`.
- `uniform_visit_with_height` correctly gets `T^t(n) <= 2^(t+q) < 2^(10*q)`. The strict exponent comparison follows from `t < 9*q`.

## The smaller marked partner

Given `T^a(u)=T^b(n)`, `u <= 2^q`, and `2^(10*q) <= n`, the forced visit `y=T^t(u)` is marked and strictly below `n`. The displayed clock identity is correct:

`T^a(y) = T^a(T^t(u)) = T^t(T^a(u)) = T^t(T^b(n)) = T^(b+t)(n)`.

The conclusion is a smaller marked component partner. It does not assert that `y` occurs on the forward orbit of `n`. The supplied merger is the actual hypothesis needed for the component-induction interface. No partner-existence hypothesis is discharged by the argument.

## Exact denominator 306 certificate

One exact Python integer computation verified `gcd(485,306)=1`, `485*306=148410`, `306^2=93636`, and

`2^148409 <= 3^93636 <= 2^148411`.

The ternary power has bit length 148410. No floating point was used.

`Integer306.lean` subsequently proves the entire bracket in Lean using only `Init`. The enormous-power comparisons are not used as `decide` inputs. Instead, three smaller integer certificates are checked with `decide`:

1. `899 * 2^485 <= 900 * 3^306`;
2. `3^306 <= 2^485`;
3. `900^306 <= 2 * 899^306`.

Raise the first inequality to the 306th power, use the third, cancel `899^306`, and remove one factor of two. Raise the second inequality to the 306th power for the upper side. All three numerical lemmas report no axioms; the assembled bracket reports only `propext`, `Classical.choice`, and `Quot.sound`. The module passed Lean with warnings treated as errors.

`Good306.lean` contains a short logarithmic bridge using only the three smaller inequalities above. Applying the increasing function `log_2` and the product/power identities gives three linear inequalities; the terms `log_2(899)` and `log_2(900)` cancel. The conclusion is `|306 log_2 3-485| <= 1/306`. The root can package this as `GoodScale 306` using the decidable coprimality fact. Its independent Mathlib compilation was still pending when this note was written; the root must retain the ordinary compilation gate for this bridge.


## Publication update

The final `FastForward.lean` uses the generic theorem
`approximation_of_power_bracket` with the verified `integer_bracket_306`,
rather than the optional `Good306.lean` draft. That generic logarithmic
bridge, `good_scale_306`, and the complete range certificate subsequently
passed Lean with warnings treated as errors. The main finite theorems and
the new explicit denominator-separation interface also passed. The final
combined replay receipt pins the published source; the earlier review pin
records the source examined during the independent mathematical review.
