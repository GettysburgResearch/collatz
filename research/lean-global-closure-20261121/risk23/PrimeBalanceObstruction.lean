import Std

/-!
An exact obstruction to an unrestricted cycle attack through completely additive
arithmetic potentials. This file does not prove Collatz convergence or exclude a
nontrivial cycle. It certifies two genuine, disjoint odd Collatz paths whose
endpoint products are equal:

  25 -> 19 -> 29 -> 11       and       55 -> 83 -> 125.

Their five distinct sources and five distinct images have equal products, but
the source and image sets differ. Thus product/prime-valuation balance, even
together with positivity and distinctness, does not supply cycle closure.

Only Lean core/Std is used. No native_decide or custom axiom is used.
-/

namespace Collatz.PrimeBalanceObstruction

/-- An actual accelerated odd edge, including its exact division exponent. -/
def OddEdge (x y a : Nat) : Prop :=
  0 < x ∧ x % 2 = 1 ∧ 0 < y ∧ y % 2 = 1 ∧
  0 < a ∧ 3 * x + 1 = 2 ^ a * y

theorem edge25 : OddEdge 25 19 2 := by unfold OddEdge; decide
theorem edge19 : OddEdge 19 29 1 := by unfold OddEdge; decide
theorem edge29 : OddEdge 29 11 3 := by unfold OddEdge; decide
theorem edge55 : OddEdge 55 83 1 := by unfold OddEdge; decide
theorem edge83 : OddEdge 83 125 1 := by unfold OddEdge; decide

theorem endpoint_product : (25 : Nat) * 55 = 11 * 125 := by decide

theorem full_product :
    (19 : Nat) * 25 * 29 * 55 * 83 = 29 * 19 * 11 * 83 * 125 := by
  decide

theorem exact_division_sum : (2 : Nat) + 1 + 3 + 1 + 1 = 8 := by decide

theorem full_denominator : (2 : Nat) ^ 8 - 3 ^ 5 = 13 := by decide

theorem word_numerator :
    (3 : Nat) ^ 4 + 3 ^ 3 * 2 ^ 2 + 3 ^ 2 * 2 ^ 3 +
      3 * 2 ^ 6 + 2 ^ 7 = 581 := by
  decide

theorem full_denominator_does_not_divide_word_numerator :
    ¬ (13 : Nat) ∣ 581 := by
  decide

theorem word_counts_coprime : Nat.gcd 8 5 = 1 := by decide

/-- The witness even passes the minimum inequality satisfied by all cycles. -/
theorem minimum_inequality :
    ((2 : Nat) ^ 8 - 3 ^ 5) * (3 * 19 + 1) ≤ 5 * 2 ^ 8 := by
  decide

theorem minimum_bound :
    (5 * (2 : Nat) ^ 8 - (2 ^ 8 - 3 ^ 5)) / (3 * (2 ^ 8 - 3 ^ 5)) = 32 := by
  decide

theorem distinct_sources : ([19, 25, 29, 55, 83] : List Nat).Nodup := by
  decide

theorem distinct_images : ([29, 19, 11, 83, 125] : List Nat).Nodup := by
  decide

theorem all_sources_gt_one_and_coprime_six :
    ∀ x ∈ ([19, 25, 29, 55, 83] : List Nat),
      1 < x ∧ x % 2 = 1 ∧ x % 3 ≠ 0 := by
  decide

theorem source_image_sets_differ :
    (25 : Nat) ∈ [19, 25, 29, 55, 83] ∧ 25 ∉ [29, 19, 11, 83, 125] := by
  decide

/--
No integer-valued, completely additive arithmetic potential can strictly
decrease on all genuine odd Collatz edges from inputs greater than one.

The multiplicativity-to-additivity hypothesis is restricted to positive
factors. Including zero would force the function to vanish identically and
would make the statement artificially trivial.
-/
theorem no_completely_additive_strict_descent
    (v : Nat → Int)
    (hadd : ∀ a b : Nat, 0 < a → 0 < b → v (a * b) = v a + v b) :
    ¬ (∀ x y a : Nat, 1 < x → OddEdge x y a → v y < v x) := by
  intro h
  have h25 : v 19 < v 25 := h 25 19 2 (by decide) edge25
  have h19 : v 29 < v 19 := h 19 29 1 (by decide) edge19
  have h29 : v 11 < v 29 := h 29 11 3 (by decide) edge29
  have h55 : v 83 < v 55 := h 55 83 1 (by decide) edge55
  have h83 : v 125 < v 83 := h 83 125 1 (by decide) edge83
  have hbal : v 25 + v 55 = v 11 + v 125 := by
    calc
      v 25 + v 55 = v (25 * 55) := (hadd 25 55 (by decide) (by decide)).symm
      _ = v (11 * 125) := congrArg v endpoint_product
      _ = v 11 + v 125 := hadd 11 125 (by decide) (by decide)
  omega

/-- The obstruction needs only the five explicit edges, not a global premise. -/
theorem no_simultaneous_decrease_on_witness
    (v : Nat → Int)
    (hbal : v 25 + v 55 = v 11 + v 125) :
    ¬ (v 19 < v 25 ∧ v 29 < v 19 ∧ v 11 < v 29 ∧
      v 83 < v 55 ∧ v 125 < v 83) := by
  omega

#print axioms edge25
#print axioms full_product
#print axioms full_denominator_does_not_divide_word_numerator
#print axioms minimum_inequality
#print axioms no_completely_additive_strict_descent
#print axioms no_simultaneous_decrease_on_witness

end Collatz.PrimeBalanceObstruction
