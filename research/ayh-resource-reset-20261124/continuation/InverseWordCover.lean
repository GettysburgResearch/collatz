import CriticalSection

/-! Twelve ternary cells supply ordinary inverse words of mean cost at most
three shortcut clocks per odd inverse. The root may be even. -/

namespace CollatzShell.CriticalCounting

def inverseWord (q : Nat) : List Nat :=
  if q%9 = 1 ∨ q%9 = 4 then [2]
  else if q%9 = 2 ∨ q%9 = 8 then [1]
  else if q%9 = 5 then [3]
  else if q%27 = 7 ∨ q%27 = 16 then [4,2]
  else if q%81 = 25 ∨ q%81 = 52 then [6,1,2]
  else if q%243 = 79 then [4,6,1,1]
  else [4,4,2,1]

/-- Every recorded preimage is odd, a ternary unit, and an exact positive
ordinary inverse; the root itself need only be a ternary unit. -/
def LegalWord (q : Nat) : List Nat → Prop
  | [] => 0 < q ∧ q%3 ≠ 0
  | a :: tail =>
    let y := (2^a*q-1)/3
    0<a ∧ y%2=1 ∧ y%3≠0 ∧ 3*y+1=2^a*q ∧ LegalWord y tail

set_option maxRecDepth 8192 in
private theorem last_classes :
    ∀ r : Fin 243, r.val%3≠0 →
      ¬(r.val%9=1 ∨ r.val%9=4) → ¬(r.val%9=2 ∨ r.val%9=8) → r.val%9≠5 →
      ¬(r.val%27=7 ∨ r.val%27=16) → ¬(r.val%81=25 ∨ r.val%81=52) →
      r.val≠79 → r.val=160 ∨ r.val=241 := by decide

/-- A legal exact word, with all intermediate outputs still admissible, starts
at every unit, uses at most four inverses, and costs at most three per inverse
on average. -/
theorem inverse_word_cover {q : Nat} (hu : q%3≠0) :
    LegalWord q (inverseWord q) ∧ 0<(inverseWord q).length ∧
    (inverseWord q).length≤4 ∧ (inverseWord q).sum≤3*(inverseWord q).length := by
  unfold inverseWord
  repeat' split
  all_goals try (norm_num [LegalWord]; omega)
  have cases' := last_classes ⟨q%243,Nat.mod_lt _ (by decide)⟩
  simp only [Nat.mod_mod_of_dvd q (by decide : 3 ∣ 243),
    Nat.mod_mod_of_dvd q (by decide : 9 ∣ 243),
    Nat.mod_mod_of_dvd q (by decide : 27 ∣ 243),
    Nat.mod_mod_of_dvd q (by decide : 81 ∣ 243)] at cases'
  have tail : q%243=160 ∨ q%243=241 := by apply cases' <;> assumption
  rcases tail with h | h
  all_goals have decomp := Nat.mod_add_div q 243
  all_goals rw [h] at decomp
  all_goals conv => enter [1]; rw [← decomp]
  all_goals norm_num [LegalWord]; omega

/-- At each prefix of a block a four-clock additive allowance suffices. -/
theorem inverse_word_prefix_cost (q i : Nat) (hi : i≤4) :
    ((inverseWord q).take i).sum≤3*i+4 := by
  unfold inverseWord
  repeat' split
  all_goals interval_cases i <;> decide

/-- An individual inverse link gives exactly the advertised physical clocks,
including when its root is even. -/
theorem inverse_link_clock {q y a : Nat} (ap : 0<a)
    (yo : y%2=1) (eq : 3*y+1=2^a*q) : orbit a y=q := by
  obtain ⟨j,rfl⟩ := Nat.exists_eq_succ_of_ne_zero ap.ne'
  have st : step y=2^j*q := by
    rw [show (2:Nat)^(j+1)*q=2*(2^j*q) by ring] at eq
    simp [step,yo,eq]
  simp only [orbit,st,orbit_pad]

#print axioms inverse_word_cover
#print axioms inverse_word_prefix_cost
#print axioms inverse_link_clock
end CollatzShell.CriticalCounting
