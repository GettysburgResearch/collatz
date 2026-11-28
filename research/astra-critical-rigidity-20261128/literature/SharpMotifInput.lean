import BlockClock

/-!
Specialize PR212's actual finite-family existence theorem to consecutive
positive sources, one common subcritical clock, one grade, and endpoint one.
BlockClock and its project-local imports are pinned in ROUTER_REPLAY.json.
-/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.SharpMotif
open TwoGapRouting

theorem consecutive_subcritical_motifs (K : ℕ) :
    ∃ ℓ g t : ℕ, 0 < t ∧ 3 ^ g < 2 ^ ℓ ∧
      ∀ i ≤ K, run ℓ (t + i) = 1 ∧ odds ℓ (t + i) = g := by
  obtain ⟨B, g, cover⟩ := BlockClock.cover (List.range (K + 1)) 0 0 0
  let ℓ := B + 3 ^ g + 1
  have hB : B ≤ ℓ := Nat.le_succ_of_le (Nat.le_add_right B (3 ^ g))
  obtain ⟨t, positive, _, _, hits⟩ := cover ℓ hB 1 (by decide) 0
  refine ⟨ℓ, g, t, positive, ?_, ?_⟩
  · have small : 3 ^ g < ℓ := Nat.lt_succ_of_le (Nat.le_add_left (3 ^ g) B)
    exact lt_trans small Nat.lt_two_pow_self
  · intro i hi
    exact hits i (List.mem_cons.mpr (Or.inr (List.mem_range.mpr (by omega))))

#print axioms consecutive_subcritical_motifs
end Collatz.SharpMotif
