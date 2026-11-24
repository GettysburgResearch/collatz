module

public import Std

public section

namespace Collatz.PhaseRepulsion

-- The endpoint oddness is retained, including for an empty run.
private theorem twoPow_coprime_three (n : Nat) : Nat.Coprime (2^n) 3 := by
  exact Nat.Coprime.pow_left _ (by decide : Nat.Coprime 2 3)

structure OneRun (q c : Nat → Nat) (j L : Nat) : Prop where
  positive : ∀ i, j ≤ i → i ≤ j+L → 0 < q i
  odd : ∀ i, j ≤ i → i ≤ j+L → 2 ∣ q i+1
  floor : ∀ i, j ≤ i → i ≤ j+L → 2^(c i) ≤ q i
  step : ∀ i, j ≤ i → i < j+L → ∃ a : Nat, 1 ≤ a ∧
    2^a * q (i+1) = 3*q i+1 ∧ a+c (i+1) = 1+3*c i

theorem one_run (q c : Nat → Nat) (j L : Nat) (h : OneRun q c j L) :
    (c j = 0 → 2^(L+1) ∣ q j+1) ∧ 2^(c j+L) ≤ q j := by
  induction L generalizing j with
  | zero =>
    constructor
    · intro _
      exact h.odd j (by omega) (by omega)
    · simpa using h.floor j (by omega) (by omega)
  | succ L ih =>
    have tail : OneRun q c (j+1) L := {
      positive := fun i hlo hhi => h.positive i (by omega) (by omega)
      odd := fun i hlo hhi => h.odd i (by omega) (by omega)
      floor := fun i hlo hhi => h.floor i (by omega) (by omega)
      step := fun i hlo hhi => h.step i (by omega) (by omega) }
    obtain ⟨td, tl⟩ := ih (j+1) tail
    obtain ⟨a, ha, hq, hc⟩ := h.step j (by omega) (by omega)
    have hd : c j = 0 → 2^(L+1+1) ∣ q j+1 := by
      intro hz
      have h1 : a=1 := by omega
      have h0 : c (j+1)=0 := by omega
      simp [h1] at hq
      have eq : 2*(q (j+1)+1) = 3*(q j+1) := by omega
      have hd' := Nat.mul_dvd_mul_left 2 (td h0)
      rw [eq, Nat.mul_comm 2 (2^(L+1)), ←Nat.pow_succ] at hd'
      exact (twoPow_coprime_three _).dvd_of_dvd_mul_left hd'
    refine ⟨hd, ?_⟩
    by_cases hz : c j = 0
    · have hp : 2^(L+1+1) ≤ q j+1 := Nat.le_of_dvd (by omega) (hd hz)
      have hpos : 0 < 2^(L+1) := Nat.two_pow_pos _
      rw [Nat.pow_succ] at hp
      simp only [hz, Nat.zero_add]
      omega
    · have hj := h.positive j (by omega) (by omega)
      have ht := Nat.mul_le_mul_left (2^a) tl
      rw [← Nat.pow_add, ← Nat.add_assoc, hc, hq] at ht
      have he : c j+(L+1)+2 ≤ 1+3*c j+L := by omega
      have hp := Nat.pow_le_pow_right (by decide : 0 < 2) he
      rw [Nat.pow_add] at hp
      simp only [Nat.reducePow] at hp
      omega

theorem one_run_length (q c : Nat → Nat) (j L : Nat) (h : OneRun q c j L) :
    2^(L+1) ≤ q j+1 := by
  obtain ⟨hd, ht⟩ := one_run q c j L h
  by_cases hz : c j = 0
  · exact Nat.le_of_dvd (by omega) (hd hz)
  · have he : L+1 ≤ c j+L := by omega
    have hp := Nat.pow_le_pow_right (by decide : 0 < 2) he
    omega

#print axioms one_run
#print axioms one_run_length
end Collatz.PhaseRepulsion
