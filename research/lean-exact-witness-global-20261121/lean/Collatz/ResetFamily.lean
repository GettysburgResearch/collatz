/-
An unbounded family of exact adjacent-source resets.

The source always has the complete two-letter certificate [3,b].  The
ordinary reset of its adjacent target is larger than 2^j times that target.
Thus this particular source-tail reset has no uniform linear size bound.
This does not assert that a target fails to converge, nor that a different
witness transformation or a later ordinary descendant cannot contract.
-/
import Collatz.Witness
import Collatz.PsiCompletion

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzPsiCompletion

namespace CollatzResetFamily

def exponent (j : Nat) : Nat := 12*j+10
def source (j : Nat) : Nat := (2^(exponent j+3)-11)/9
def target (j : Nat) : Nat := 2*source j+1
def mersenne (j : Nat) : Nat := 2^exponent j-1
def resetCore (j : Nat) : Nat := (3^exponent j-1)/8
def reset (j : Nat) : Nat := 3*resetCore j

private theorem two_mod_nine (j : Nat) : 2^(exponent j+3) % 9 = 2 := by
  have he : exponent j+3 = 12*j+13 := by simp [exponent]
  rw [he, Nat.pow_add, Nat.pow_mul]
  simp [Nat.mul_mod, Nat.pow_mod]

private theorem three_mod_sixteen (j : Nat) : 3^exponent j % 16 = 9 := by
  unfold exponent
  rw [Nat.pow_add, Nat.pow_mul]
  simp [Nat.mul_mod, Nat.pow_mod]

private theorem two_lower (j : Nat) : 1024 ≤ 2^exponent j := by
  have h := Nat.pow_le_pow_of_le (by decide : 1 < 2)
    (by simp [exponent] : 10 ≤ exponent j)
  exact h

theorem source_identity (j : Nat) : 9*source j+11 = 2^(exponent j+3) := by
  have hm := two_mod_nine j
  have hl := two_lower j
  have he : 2^(exponent j+3) = 8*2^exponent j := by
    rw [Nat.pow_add]
    grind
  unfold source
  rw [he] at hm ⊢
  omega

theorem reset_identity (j : Nat) : 8*resetCore j+1 = 3^exponent j := by
  have hm := three_mod_sixteen j
  have hp : 0 < 3^exponent j := Nat.pow_pos (by decide)
  have hq := Nat.mod_add_div (3^exponent j) 16
  rw [hm] at hq
  unfold resetCore
  omega

theorem reset_odd (j : Nat) : reset j % 2 = 1 := by
  have hm := three_mod_sixteen j
  have he := reset_identity j
  unfold reset
  omega

/-- The supplied source certificate is complete for every parameter j. -/
theorem source_certificate (j : Nat) : Certificate (source j) [3, exponent j] := by
  have he := source_identity j
  constructor
  · intro a ha
    simp only [List.mem_cons, List.not_mem_nil, or_false] at ha
    rcases ha with rfl | rfl
    · decide
    · simp [exponent]
  · simpa [correction, total, Nat.add_comm] using he

theorem source_basin (j : Nat) : Basin (source j) :=
  witness_basin (certificate_witness (source_certificate j))

theorem source_mersenne_target (j : Nat) :
    source j < mersenne j ∧ mersenne j < target j := by
  have he := source_identity j
  have hl := two_lower j
  have hp : 2^(exponent j+3) = 8*2^exponent j := by
    rw [Nat.pow_add]
    grind
  rw [hp] at he
  unfold mersenne target
  omega

theorem target_lt_twice_power (j : Nat) : target j < 2*2^exponent j := by
  have he := source_identity j
  have hp : 2^(exponent j+3) = 8*2^exponent j := by
    rw [Nat.pow_add]
    grind
  rw [hp] at he
  unfold target
  omega

/-- The exact ordinary reset passes first through the next Mersenne number. -/
theorem target_mersenne_component (j : Nat) :
    Basin (target j) ↔ Basin (2*mersenne j+1) := by
  have hu := witness_odd (certificate_witness (source_certificate j))
  have he := source_identity j
  have hl := two_lower j
  have hp : 2^(exponent j+3) = 8*2^exponent j := by
    rw [Nat.pow_add]
    grind
  rw [hp] at he
  have h1 := basin_adjacent (source j)
  have h2 := basin_odd (3*source j+2) (by omega)
  have he2 : 3*(3*source j+2)+1 = 2*(2*(2*mersenne j+1)) := by
    unfold mersenne
    omega
  rw [he2] at h2
  change Basin (2*source j+1) ↔ Basin (2*mersenne j+1)
  exact (h1.trans h2.symm).trans ((basin_twice _).trans (basin_twice _))

/-- Every source word [3,b] in the family has the stated exact reset target. -/
theorem target_reset_component (j : Nat) :
    Basin (target j) ↔ Basin (reset j) := by
  have hm := two_lower j
  have heM : 2*mersenne j+1 = 2^(exponent j+1)-1 := by
    unfold mersenne
    rw [Nat.pow_succ]
    omega
  have hpow := basin_pow_two_pred (exponent j+1) 1 (by decide)
  simp only [Nat.mul_one] at hpow
  have hs := reset_identity j
  have heR : 3^(exponent j+1)-1 = 2*(4*reset j+1) := by
    rw [Nat.pow_succ]
    unfold reset
    omega
  have h1 := target_mersenne_component j
  rw [heM] at h1
  rw [heR] at hpow
  exact (((h1.trans hpow).trans (basin_twice _)).trans
    (basin_exch (4*reset j+1) (3*reset j+1) (reset j) rfl rfl)).trans
    (basin_odd _ (reset_odd j))

private theorem exponential_gap (j : Nat) :
    8*2^(13*j+10) < 3^(12*j+10) := by
  induction j with
  | zero => decide
  | succ j ih =>
    have e2 : 13*(j+1)+10 = (13*j+10)+13 := by omega
    have e3 : 12*(j+1)+10 = (12*j+10)+12 := by omega
    rw [e2, e3, Nat.pow_add 2 (13*j+10) 13, Nat.pow_add 3 (12*j+10) 12]
    have p2 : 2^13 = 8192 := by decide
    have p3 : 3^12 = 531441 := by decide
    rw [p2, p3]
    omega

/-- The reset amplification is unbounded, even though the original source
word has exactly two letters. -/
theorem reset_amplification (j : Nat) : 2^j*target j < reset j := by
  have hg := exponential_gap j
  have hs := reset_identity j
  have hn := target_lt_twice_power j
  have he : 2^(13*j+10) = 2^j*2^exponent j := by
    have ee : 13*j+10 = j+exponent j := by simp [exponent]; omega
    rw [ee, Nat.pow_add]
  change 8*2^(13*j+10) < 3^exponent j at hg
  rw [he, ← hs] at hg
  have hsmall : 2^j*2^exponent j ≤ resetCore j := by omega
  have hmul := Nat.mul_lt_mul_of_pos_left hn (Nat.pow_pos (by decide : 0 < 2) : 0 < 2^j)
  have he2 : 2^j*(2*2^exponent j) = 2*(2^j*2^exponent j) := by grind
  rw [he2] at hmul
  unfold reset
  omega

/-- Unbounded exact-certificate family, with no finite search premise. -/
theorem reset_family (j : Nat) :
    Certificate (source j) [3, exponent j] ∧
    source j < mersenne j ∧ mersenne j < target j ∧
    (Basin (target j) ↔ Basin (reset j)) ∧
    2^j*target j < reset j :=
  ⟨source_certificate j, (source_mersenne_target j).1,
    (source_mersenne_target j).2, target_reset_component j,
    reset_amplification j⟩

end CollatzResetFamily
