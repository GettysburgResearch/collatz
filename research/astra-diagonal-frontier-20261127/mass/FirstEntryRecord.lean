import Std

/-! Reverse debt at an ancestor of one specified permanently passing
terminal. Weak maxima retain ties. First forward entry forbids every
further weak record, equivalently every earlier reverse sum is negative. -/

namespace FirstEntryRecord

def safeAt (debt : Nat → Int) (i : Nat) : Prop :=
  ∀ j, i ≤ j → debt i ≤ debt j

def reverseDebt (debt : Nat → Int) (h i : Nat) : Int :=
  debt h - debt (h - i)

def weakRecord (R : Nat → Int) (i : Nat) : Prop :=
  ∀ j ≤ i, R j ≤ R i

theorem safe_iff_record (debt : Nat → Int) (h i : Nat) (hi : i ≤ h)
    (hs : safeAt debt h) :
    safeAt debt (h-i) ↔ weakRecord (reverseDebt debt h) i := by
  constructor
  · intro hsafe j hj
    have hy := hsafe (h-j) (by omega)
    unfold reverseDebt
    omega
  · intro hrecord j hj
    by_cases hjh : j ≤ h
    · have hh := hrecord (h-j) (by omega)
      have heq : h-(h-j)=j := by omega
      unfold reverseDebt at hh
      rw [heq] at hh
      omega
    · have hh := hrecord 0 (by omega)
      simp only [reverseDebt, Nat.sub_zero, Int.sub_self] at hh
      have hlate := hs j (by omega)
      omega

theorem no_more_records_iff (R : Nat → Int) (h : Nat) (hz : R 0 = 0) :
    (∀ i, 0 < i → i ≤ h → ¬ weakRecord R i) ↔
    (∀ i, 0 < i → i ≤ h → R i < 0) := by
  constructor
  · intro hno i
    induction i using Nat.strongRecOn with
    | ind i ih =>
      intro hpos hlim
      apply Int.lt_of_not_ge
      intro hnon
      apply hno i hpos hlim
      intro j hj
      by_cases hji : j=i
      · simp [hji]
      by_cases hj0 : j=0
      · simpa [hj0, hz] using hnon
      have hneg := ih j (by omega) (by omega) (by omega)
      omega
  · intro hneg i hp hl hrec
    have hh := hrec 0 (by omega)
    rw [hz] at hh
    have := hneg i hp hl
    omega

theorem first_entry_iff (debt : Nat → Int) (h : Nat) (hs : safeAt debt h) :
    (∀ i, 0 < i → i ≤ h → ¬ safeAt debt (h-i)) ↔
    (∀ i, 0 < i → i ≤ h → reverseDebt debt h i < 0) := by
  rw [← no_more_records_iff (reverseDebt debt h) h (by simp [reverseDebt])]
  constructor <;> intro hyp i hp hl
  · exact fun hr => hyp i hp hl ((safe_iff_record debt h i hl hs).mpr hr)
  · exact fun hsa => hyp i hp hl ((safe_iff_record debt h i hl hs).mp hsa)

#print axioms safe_iff_record
#print axioms no_more_records_iff
#print axioms first_entry_iff

end FirstEntryRecord
