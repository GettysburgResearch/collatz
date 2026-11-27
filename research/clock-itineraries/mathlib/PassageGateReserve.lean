module

public import PassageGatePrefix
public import Mathlib.Algebra.Order.BigOperators.Group.Finset
import all PassageGatePrefix
import all PassageGatePacking
import all TernaryItinerary
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.PassageGate

open HourTower Finset
set_option autoImplicit false

/-- The physical five-eighths gate from PR 212, at its fixed native date. -/
def binaryGate (N x : ℕ) : Prop := ∀ i≤N, 5*i≤8*count i x

private theorem periodic_count (h x v : ℕ) : count h (x+2^h*v)=count h x := by
  induction h generalizing x v with
  | zero => rfl
  | succ h ih =>
    have sz : 2^(h+1)*v=2*(2^h*v) := by rw [pow_succ]; ac_rfl
    rw [sz,count,show (x+2*(2^h*v))%2=x%2 by omega,count,affine_branch]
    by_cases even : x%2=0
    · simp [even,ih]
    · simp only [ite_eq_right even]
      rw [show 3*2^h*v=2^h*(3*v) by ac_rfl,ih]

/-- Every parity word whose current bank pays the entire prescribed
future horizon yields a genuine upper-half ordinary representative. -/
theorem upper_lift_passes {M N x : ℕ} (safe : binaryGate M x)
    (paid : 5*N≤8*count M x) : binaryGate N (x+2^M) := by
  have sameBits (i : ℕ) (hi : i≤M) : count i (x+2^M)=count i x := by
    have s : i+(M-i)=M := Nat.add_sub_of_le hi
    rw [←s,pow_add,periodic_count]
  intro i hi
  by_cases early : i≤M
  · rw [sameBits i early]
    exact safe i early
  · have add := append_count M (i-M) (x+2^M)
    rw [Nat.add_sub_of_le (by omega),sameBits M le_rfl] at add
    omega

noncomputable def highBank (M N : ℕ) : Finset ℕ := by
  classical exact (range (2^M)).filter (fun x => binaryGate M x ∧ 5*N≤8*count M x)

noncomputable def upperBirths (M N : ℕ) : Finset ℕ := by
  classical exact (Ico (2^M) (2^(M+1))).filter (binaryGate N)

noncomputable def laterMass (M N : ℕ) : ℚ := by
  classical exact ∑ x ∈ (Ico (2^M) (2^N)).filter (binaryGate N), 1/(x:ℚ)

/-- Distinct paid parents furnish distinct, actually born sources. -/
theorem parent_count_le_newborns (M N : ℕ) : (highBank M N).card≤(upperBirths M N).card := by
  classical
  apply card_le_card_of_injOn (fun x : ℕ => x+2^M)
  · intro x hx
    have ⟨old,accept,bank⟩ := mem_filter.mp hx
    have lt := mem_range.mp old
    change x+2^M ∈ upperBirths M N
    apply mem_filter.mpr
    refine ⟨mem_Ico.mpr ⟨by omega,?_⟩,upper_lift_passes accept bank⟩
    rw [pow_succ]
    omega
  · intro x _ y _ same
    change x+2^M=y+2^M at same
    omega

/-- A lower bound on the actual later-source reciprocal mass of PR 212,
valid even if the ancestors selected by the bank later fail. -/
theorem newborn_mass_lower {M N : ℕ} (late : M<N) :
    ((highBank M N).card:ℚ)/2^(M+1) ≤ laterMass M N := by
  classical
  let upper := upperBirths M N
  let all := (Ico (2^M) (2^N)).filter (binaryGate N)
  have sub : upper⊆all := by
    intro x hx
    obtain ⟨sub,pass⟩ := mem_filter.mp hx
    have ⟨low,high⟩ := mem_Ico.mp sub
    exact mem_filter.mpr ⟨mem_Ico.mpr ⟨low,lt_of_lt_of_le high
      (Nat.pow_le_pow_right (by decide) late)⟩,pass⟩
  have cmp := parent_count_le_newborns M N
  have realCmp : ((highBank M N).card:ℚ)≤(upper.card:ℚ) := by exact_mod_cast cmp
  change _≤∑ x ∈ all, 1/(x:ℚ)
  calc
    _ ≤ (upper.card:ℚ)/2^(M+1) := div_le_div_of_nonneg_right realCmp (by positivity)
    _ = ∑ _x ∈ upper, 1/(2:ℚ)^(M+1) := by simp [div_eq_mul_inv]
    _ ≤ ∑ x ∈ upper, 1/(x:ℚ) := by
      apply sum_le_sum
      intro x hx
      have ⟨lo,hi⟩ := mem_Ico.mp (mem_filter.mp hx).1
      have pos : 0<x := lt_of_lt_of_le (Nat.two_pow_pos _) lo
      exact one_div_le_one_div_of_le (by exact_mod_cast pos) (by exact_mod_cast hi.le)
    _ ≤ _ := sum_le_sum_of_subset_of_nonneg sub (fun _ _ _ => by positivity)

#print axioms upper_lift_passes
#print axioms parent_count_le_newborns
#print axioms newborn_mass_lower
end Collatz.Itinerary.PassageGate
