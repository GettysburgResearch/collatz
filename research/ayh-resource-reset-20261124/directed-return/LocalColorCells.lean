import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.Positivity

/-! Finite multiplicity and mixed-radix identities for the selected ordinary
trit cells. The predictable-test bound and the original-source census have
written proofs. -/

namespace Collatz.LocalColorCells

/-- A fixed source occupancy cap converts cell mass into distinct quotients. -/
theorem cell_mass_to_sites {ι : Type*} (s : Finset ι) (weight : ι → ℕ)
    (A K : ℕ) (hcap : ∀ i ∈ s, weight i ≤ A)
    (hmass : A*K < ∑ i ∈ s, weight i) : K < s.card := by
  have hsum : ∑ i ∈ s, weight i ≤ s.card*A := by
    calc
      _ ≤ ∑ _i ∈ s, A := Finset.sum_le_sum hcap
      _ = _ := by simp
  by_contra hn
  have h : s.card ≤ K := by omega
  have hprod := Nat.mul_le_mul_right A h
  rw [Nat.mul_comm A K] at hmass
  omega

/-- On a first deviation, the predictor's branch contains at least as much
ordinary mass as the realized complete reply word. -/
theorem modal_opposite_mass (word dissent mode : ℕ)
    (hw : word ≤ dissent) (hm : dissent ≤ mode) :
    word ≤ min dissent mode := by omega

/-- Equal ternary residues of the coarse coordinate and an equal binary
prefix give the increased ternary stride between the two physical sites. -/
theorem mixed_stride (u B e gap : ℕ) (h : 3^B ∣ 2^u * gap) :
    3^(e+B) ∣ 3^e * gap := by
  have hcop : Nat.Coprime (3^B) (2^u) :=
    Nat.Coprime.pow B u (by decide : Nat.Coprime 3 2)
  obtain ⟨j, hj⟩ := hcop.dvd_of_dvd_mul_left h
  refine ⟨j, ?_⟩
  rw [hj, pow_add, Nat.mul_assoc]

/-- Distinct coarse quotients are distinct ordinary trit sites and one
unseen binary cell bounds their physical spacing. -/
theorem column_gap (e q gap c K : ℕ) (hpos : 0 < gap) (hcell : gap < 2^K) :
    3^e*q+c < 3^e*(q+gap)+c ∧
    3^e*(q+gap)+c < 3^e*q+c + 3^e*2^K := by
  have hp : 0 < 3^e := by positivity
  have hlarge := Nat.mul_lt_mul_of_pos_left hcell hp
  have hgap : 0 < 3^e * gap := Nat.mul_pos hp hpos
  rw [Nat.mul_add]
  omega

end Collatz.LocalColorCells

#print axioms Collatz.LocalColorCells.cell_mass_to_sites
#print axioms Collatz.LocalColorCells.modal_opposite_mass
#print axioms Collatz.LocalColorCells.mixed_stride
#print axioms Collatz.LocalColorCells.column_gap
