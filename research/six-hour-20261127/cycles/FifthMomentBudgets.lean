import Std

/-! Exact arithmetic at the interfaces of the written moment arguments.
These theorems do not assert the analytic moment estimate, the computed
64-step maximum, the Subspace Theorem, or a Collatz conclusion. -/

namespace FifthMomentBudgets

def modularMaximum : Nat := 448804760794336774447153725940272863

theorem modular_maximum_power : modularMaximum ^ 5 < (3 : Nat) ^ 384 := by
  decide +kernel

theorem physical_band_inside_strip : (2 : Nat) ^ 79 < (3 : Nat) ^ 50 := by
  decide +kernel

theorem fifth_height_above_three :
    (3 : Rat) < 4 / (4 / 3 - 1 / 10000) := by
  decide +kernel

theorem third_layer_height_above_three :
    (3 : Rat) < 4 / (4 / 3 - 1 / 20000) := by
  decide +kernel

theorem fifth_log_margin : (11 / 10 : Rat) / 10000 < 1 / 7000 := by
  decide +kernel

theorem third_layer_log_margin :
    (1 / 7000 : Rat) - 8 / 100000 > 1 / 16000 := by
  decide +kernel

theorem third_layer_base_conversion : (11 / 10 : Rat) / 20000 < 1 / 16000 := by
  decide +kernel

theorem bridge_reset_cost :
    ((3 : Rat) * 3 ^ 5 / (9 / 100)) / 4 = 2025 := by
  decide +kernel

theorem sparse_retained_mass :
    (0 : Rat) < 1 - 6 / 100000000 - (3 / 100000000) / (1 / 2000000) := by
  decide +kernel

theorem sparse_separation_margin :
    (1 / 100000000 : Rat) * (4 + 1 / 1000000) < (1 / 1000000) / 2 := by
  decide +kernel

theorem sparse_consumer_margin :
    (3 + 1 / 100000000 : Rat) * (2666577000221 / 8000002000000) < 1 := by
  decide +kernel

end FifthMomentBudgets

#print axioms FifthMomentBudgets.modular_maximum_power
#print axioms FifthMomentBudgets.physical_band_inside_strip
#print axioms FifthMomentBudgets.fifth_height_above_three
#print axioms FifthMomentBudgets.third_layer_height_above_three
#print axioms FifthMomentBudgets.fifth_log_margin
#print axioms FifthMomentBudgets.third_layer_log_margin
#print axioms FifthMomentBudgets.third_layer_base_conversion
#print axioms FifthMomentBudgets.bridge_reset_cost
#print axioms FifthMomentBudgets.sparse_retained_mass
#print axioms FifthMomentBudgets.sparse_separation_margin
#print axioms FifthMomentBudgets.sparse_consumer_margin
