import Lean.Elab.Tactic.Omega

namespace CollatzResearch.WidthCarry

/-- The head is the latest odd date. The tail contributes a multiple of three. -/
def signedNumerator : List (Int × Int) → Int
  | [] => 0
  | (w,d) :: tail => w * d + 3 * signedNumerator tail

/-- A four-copy signed bit difference at the latest date is forced to vanish. -/
theorem lastDigit {w d t : Int} (hw : w % 3 ≠ 0) (hl : -2 ≤ d) (hu : d ≤ 2)
    (hz : w * d + 3 * t = 0) : d = 0 := by
  have hcases : d = -2 ∨ d = -1 ∨ d = 0 ∨ d = 1 ∨ d = 2 := by omega
  rcases hcases with h | h | h | h | h <;> subst d <;> omega

/-- Exact local numerator equality decodes every pair-sum digit. -/
theorem noCarry (xs : List (Int × Int))
    (legal : ∀ x ∈ xs, x.1 % 3 ≠ 0 ∧ -2 ≤ x.2 ∧ x.2 ≤ 2)
    (hz : signedNumerator xs = 0) : ∀ x ∈ xs, x.2 = 0 := by
  induction xs with
  | nil => simp
  | cons x xs ih =>
    obtain ⟨w,d⟩ := x
    obtain ⟨hw,hl,hu⟩ := legal (w,d) (by simp)
    change w * d + 3 * signedNumerator xs = 0 at hz
    have hd := lastDigit hw hl hu hz
    change d = 0 at hd
    subst d
    have ht : signedNumerator xs = 0 := by omega
    have hs := ih (fun y hy => legal y (by simp [hy])) ht
    intro y hy
    rcases List.mem_cons.mp hy with h | h
    · subst y
      rfl
    · exact hs y h

abbrev GradePair := Nat × Nat

def energy (alphabet : List GradePair) : Nat :=
  (alphabet.flatMap fun a => alphabet.flatMap fun b =>
    alphabet.flatMap fun c => alphabet.filter fun d =>
      a.1+b.1 == c.1+d.1 && a.2+b.2 == c.2+d.2).length

theorem singletonEnergy : energy [(0,0),(1,0)] = 6 := by decide

theorem matchingEnergy : energy [(0,0),(1,0),(1,1)] = 15 := by decide

/-- Six copies need not decode from exact numerator equality. -/
theorem sixCopyCarry :
    signedNumerator [(16,-3),(8,-1),(2,1),(1,2)] = 0 := by decide

end CollatzResearch.WidthCarry
