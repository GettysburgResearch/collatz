module

public import PairCapture
import all PairCapture
import all TowerCapture
import all WindowCapture
import all TernaryItinerary

public section
namespace Collatz.Itinerary.PairCapture

open TowerCapture WindowCapture
set_option autoImplicit false
attribute [local irreducible] run

private theorem quota_upper (k j : Nat) : quota k j≤2^k := by
  induction k generalizing j with
  | zero => simp [quota]
  | succ k ih =>
    cases j with
    | zero =>
      rw [quota,Nat.pow_succ]
      have h := ih 0
      omega
    | succ j =>
      rw [quota,Nat.pow_succ]
      have a := ih j
      have b := ih (j+1)
      omega

private theorem window_room (k : Nat) : quota k (k/2)≤9710*window k+1 := by
  have prod : 2^k*3^k≤2^(4*k+2*(k/2)) := calc
    2^k*3^k = 6^k := (Nat.mul_pow 2 3 k).symm
    _ ≤ 16^k := Nat.pow_le_pow_left (by decide : 6≤16) k
    _ = 2^(4*k) := (Nat.pow_mul 2 4 k).symm
    _ ≤ _ := Nat.pow_le_pow_right (by decide) (by omega)
  have num := Nat.le_mul_of_pos_right (2^(4*k+2*(k/2))) (Nat.succ_pos k)
  have div := (Nat.le_div_iff_mul_le (Nat.pow_pos (by decide : 0<3) (n:=k))).mpr (Nat.le_trans prod num)
  change 2^k≤2^(4*k+2*(k/2))*(k+1)/3^k at div
  have q := quota_upper k (k/2)
  unfold window
  omega

/-- Every passing window forces a large product of the gate and its dyadic
observation budget. The last quota-sized interval must contain a hit. -/
theorem gate_deadline_floor (k O g : Nat)
    (few : (pairMisses k O g).length<quota k (k/2)) :
    23+32*(9710*window k+1-quota k (k/2))≤2^O*g := by
  let Q := quota k (k/2)
  let N := 9710*window k+1
  let start (i : Nat) := N-Q+i
  let xs := (List.range Q).map start
  have nd : xs.Nodup := map_distinct List.nodup_range (by
    intro i _ j _ same
    exact Nat.add_left_cancel same)
  have witness : ∃ u∈xs, u∉pairMisses k O g := by
    apply Classical.byContradiction
    intro no
    have sub : xs ⊆ pairMisses k O g := by
      intro u hu
      exact Classical.byContradiction (fun miss => no ⟨u,hu,miss⟩)
    have count := nd.length_le_of_subset sub
    have len : xs.length=Q := by simp [xs]
    rw [len] at count
    exact (Nat.not_lt_of_ge count) few
  obtain ⟨u,hu,hits⟩ := witness
  obtain ⟨i,mem,hui⟩ := List.mem_map.mp hu
  change N-Q+i=u at hui
  have ilt := List.mem_range.mp mem
  have room' : Q≤N := window_room k
  have bounds : N-Q≤u ∧ u<N := by omega
  have within : u≤9710*window k := by have top : u<9710*window k+1 := bounds.2; omega
  obtain ⟨r,_,t,le,hit⟩ := covered within hits
  have h := input_bound t (arm u r)
  rw [hit] at h
  have floor : 23+32*u≤arm u r := by unfold arm; split <;> omega
  have chain := Nat.le_trans floor (Nat.le_trans h
    (Nat.mul_le_mul_right g (Nat.pow_le_pow_right (by decide : 0<2) le)))
  change 23+32*(N-Q)≤2^O*g
  omega

#print axioms gate_deadline_floor
end Collatz.Itinerary.PairCapture
