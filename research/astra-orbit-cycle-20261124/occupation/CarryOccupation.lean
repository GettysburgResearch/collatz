import Std

namespace Collatz.CarryOccupation

/-- At any exceptional index the accumulated carry more than triples. -/
theorem exceptional_jump (K c : Nat) (h : 2 * K < c) : 3 * K < K + c := by omega

/-- Works even at an initial selected index of mass zero. Each selected update
is at most the mass present before the next selected update. -/
theorem exceptional_powers (mass carry : Nat → Nat) (s : Nat)
    (hjump : ∀ j < s, 2 * mass j < carry j)
    (hnext : ∀ j < s, mass j + carry j ≤ mass (j+1)) :
    3 ^ s ≤ 2 * mass s + 1 := by
  induction s with
  | zero => simp
  | succ s ih =>
    have hp := ih (fun j hj => hjump j (by omega)) (fun j hj => hnext j (by omega))
    have he := exceptional_jump (mass s) (carry s) (hjump s (by omega))
    have hn := hnext s (by omega)
    rw [Nat.pow_succ]
    omega

/-- Overlapping windows can be counted with multiplicity for an upper bound. -/
def affected (marks : List Nat) (m : Nat) : List Nat :=
  marks.flatMap (fun i => (List.range (m+1)).map (i + ·))

theorem mem_affected (marks : List Nat) (m i j : Nat)
    (hi : i ∈ marks) (hij : i ≤ j) (hji : j ≤ i+m) : j ∈ affected marks m := by
  apply List.mem_flatMap.mpr
  exact ⟨i, hi, List.mem_map.mpr ⟨j-i, List.mem_range.mpr (by omega), by omega⟩⟩

theorem affected_length (marks : List Nat) (m : Nat) :
    (affected marks m).length = marks.length * (m+1) := by
  induction marks with
  | nil => simp [affected]
  | cons i marks ih =>
    change (((List.range (m+1)).map (i + ·)) ++ affected marks m).length = _
    simp only [List.length_append, List.length_map, List.length_range, ih,
      List.length_cons, Nat.add_mul, Nat.one_mul, Nat.add_comm]

theorem positive_carry_count (cs : List Nat) :
    (cs.filter (fun x => decide (0 < x))).length ≤ cs.sum := by
  induction cs with
  | nil => simp
  | cons c cs ih =>
    by_cases h : 0 < c
    · simp [h] <;> omega
    · simp [h] <;> omega

/-- A duplicate-free set of identified dictionary words bounds all clean
endpoints. A mark at either end of the closed carry window is charged. -/
theorem dictionary_bound {β : Type} (N m : Nat) (marks good : List Nat)
    (words : List β) (w : Nat → β)
    (hcover : ∀ j < N, j < m ∨ (∃ i ∈ marks, i ≤ j ∧ j ≤ i+m) ∨ j ∈ good)
    (hmem : good.map w ⊆ words) (hinj : (good.map w).Nodup) :
    N ≤ m + marks.length * (m+1) + words.length := by
  have hg := hinj.length_le_of_subset hmem
  have hc : List.range N ⊆ List.range m ++ affected marks m ++ good := by
    intro j hj
    rcases hcover j (List.mem_range.mp hj) with h | ⟨i,hi,hij,hji⟩ | h
    · exact List.mem_append.mpr (Or.inl (List.mem_append.mpr (Or.inl (List.mem_range.mpr h))))
    · exact List.mem_append.mpr (Or.inl (List.mem_append.mpr (Or.inr
        (mem_affected marks m i j hi hij hji))))
    · exact List.mem_append.mpr (Or.inr h)
  have hh := List.nodup_range.length_le_of_subset hc
  simp only [List.length_range, List.length_map, List.length_append, affected_length] at hg hh
  omega

#print axioms exceptional_jump
#print axioms exceptional_powers
#print axioms mem_affected
#print axioms affected_length
#print axioms positive_carry_count
#print axioms dictionary_bound
end Collatz.CarryOccupation
