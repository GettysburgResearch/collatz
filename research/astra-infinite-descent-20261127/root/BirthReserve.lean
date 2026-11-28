import BinaryCylinder
import Mathlib.Algebra.BigOperators.Field
import Mathlib.Algebra.Order.Ring.Pow

/-! A complete finite birth budget for reciprocal mass on actual binary
Collatz cylinders. The local debt inequality in PR201 is lifted here to
the entire ordinary-source population, at every depth. -/
set_option autoImplicit false
set_option warningAsError true

namespace BirthReserve
open CoreBranching PeakRigidity FloorCounting BinaryPrefixCriterion BinaryCylinder
open scoped BigOperators

def activeSum (N : ℕ) (f : ℕ → ℚ) : ℚ :=
  ∑ x ∈ Finset.range (2^N), if Gate N x then f x else 0

def debt (N x : ℕ) : ℕ := 8*grade N x-5*N
def contribution (N x : ℕ) : ℚ := if Gate N x then (debt N x:ℚ)+5 else 0
def probability (N : ℕ) : ℚ := activeSum N (fun _ => 1)/(2:ℚ)^N
def reserve (N : ℕ) : ℚ := activeSum N (fun x => (debt N x:ℚ)+5)/(2:ℚ)^N
def tailWeight (M x : ℕ) : ℚ := if 2^M≤x then 1/(x:ℚ) else 0
def tail (M N : ℕ) : ℚ := activeSum N (tailWeight M)

theorem range_pair (N : ℕ) (f : ℕ → ℚ) :
    (∑ x ∈ Finset.range (2^(N+1)), f x) =
      ∑ x ∈ Finset.range (2^N), (f x+f (x+2^N)) := by
  rw [pow_succ, Nat.mul_two, Finset.sum_range_add, ←Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intros
  simp [Nat.add_comm]

theorem activeSum_nonneg (N : ℕ) (f : ℕ → ℚ) (hf : ∀ x, 0≤f x) :
    0≤activeSum N f := by
  apply Finset.sum_nonneg
  intro x _
  split_ifs <;> simp_all

theorem reserve_nonneg (N : ℕ) : 0≤reserve N := by
  unfold reserve
  apply div_nonneg
  · apply activeSum_nonneg
    intro x
    positivity
  · positivity

theorem debt_shift (N x : ℕ) : debt N (x+2^N)=debt N x := by
  simp [debt,grade_shift]

theorem debt_exact (N x : ℕ) (hg : Gate N x) : debt N x+5*N=8*grade N x := by
  have h := hg N (Finset.mem_range.mpr (by omega))
  unfold debt
  omega

theorem contribution_child (N x : ℕ) (hg : Gate N x) :
    contribution (N+1) x =
      if run N x%2=1 then (debt N x:ℚ)+8
      else if 5≤debt N x then (debt N x:ℚ) else 0 := by
  have hdebt := debt_exact N x hg
  have hp := Nat.mod_lt (run N x) (by decide : 0<2)
  by_cases ho : run N x%2=1
  · have hn : Gate (N+1) x := (gate_succ N x).mpr ⟨hg,by simp [grade,ho]; omega⟩
    have hd : debt (N+1) x=debt N x+3 := by unfold debt; simp only [grade,ho]; omega
    simp [contribution,hn,ho,hd]
    ring
  · have he : run N x%2=0 := by omega
    by_cases h5 : 5≤debt N x
    · have hn : Gate (N+1) x := (gate_succ N x).mpr ⟨hg,by simp [grade,he]; omega⟩
      have hd : debt (N+1) x+5=debt N x := by unfold debt; simp only [grade,he]; omega
      have hdq : (debt (N+1) x:ℚ)+5=debt N x := by exact_mod_cast hd
      simp [contribution,hn,ho,h5,hdq]
    · have hn : ¬Gate (N+1) x := by
        intro h
        have hlast := (gate_succ N x).mp h |>.2
        simp only [grade,he] at hlast
        omega
      simp [contribution,hn,ho,h5]

theorem paired_reserve (N x : ℕ) :
    (if Gate N x then (1:ℚ) else 0) +
      (contribution (N+1) x+contribution (N+1) (x+2^N))/2 ≤ contribution N x := by
  by_cases hg : Gate N x
  · have hgs : Gate N (x+2^N) := (gate_shift N x).mpr hg
    rw [contribution_child N x hg,contribution_child N (x+2^N) hgs,debt_shift]
    have pp := paired_parity N x
    have small := debt_reserve_step (debt N x)
    unfold nextReserve at small
    have h0 := Nat.mod_lt (run N x) (by decide : 0<2)
    have h1 := Nat.mod_lt (run N (x+2^N)) (by decide : 0<2)
    rcases (show run N x%2=0 ∨ run N x%2=1 by omega) with h|h
    · have h' : run N (x+2^N)%2=1 := by omega
      simp only [h,h',show ¬(0:ℕ)=1 by decide,ite_false,ite_true,contribution,hg]
      split_ifs at small ⊢ <;> linarith
    · have h' : run N (x+2^N)%2=0 := by omega
      simp only [h,h',show ¬(0:ℕ)=1 by decide,ite_false,ite_true,contribution,hg]
      split_ifs at small ⊢ <;> linarith
  · have h0 : ¬Gate (N+1) x := fun h => hg ((gate_succ N x).mp h).1
    have h1 : ¬Gate (N+1) (x+2^N) := by
      intro h
      exact hg ((gate_shift N x).mp ((gate_succ N (x+2^N)).mp h).1)
    simp [contribution,hg,h0,h1]

/-- The reserve pays for every possible new ordinary representative. -/
theorem reserve_drift (N : ℕ) : probability N+reserve (N+1)≤reserve N := by
  have h := Finset.sum_le_sum (s:=Finset.range (2^N))
    (fun x _ => paired_reserve N x)
  have p : (0:ℚ)<2^N := by positivity
  have hb := div_le_div_of_nonneg_right h (le_of_lt p)
  have pair : (∑ x ∈ Finset.range (2^N),
      (contribution (N+1) x+contribution (N+1) (x+2^N))) =
      ∑ x ∈ Finset.range (2^(N+1)), contribution (N+1) x :=
    (range_pair N (contribution (N+1))).symm
  rw [Finset.sum_add_distrib, ←Finset.sum_div, pair] at hb
  change probability N+reserve (N+1)≤reserve N
  unfold probability reserve activeSum
  change _ ≤ (∑ x ∈ Finset.range (2^N), contribution N x)/(2:ℚ)^N
  simp only [contribution] at hb ⊢
  convert hb using 1
  simp only [pow_succ]
  ring

theorem tailWeight_nonneg (M x : ℕ) : 0≤tailWeight M x := by
  unfold tailWeight
  split_ifs
  · exact div_nonneg (by norm_num) (Nat.cast_nonneg x)
  · rfl

theorem new_weight (M N x : ℕ) : tailWeight M (x+2^N)≤1/(2:ℚ)^N := by
  unfold tailWeight
  split_ifs
  · have hx : (2:ℚ)^N≤(x+2^N:ℕ) := by norm_cast; omega
    exact one_div_le_one_div_of_le (by positivity) hx
  · positivity

theorem paired_birth (M N x : ℕ) :
    (if Gate (N+1) x then tailWeight M x else 0) +
    (if Gate (N+1) (x+2^N) then tailWeight M (x+2^N) else 0) ≤
    (if Gate N x then tailWeight M x else 0) +
    (if Gate N x then 1/(2:ℚ)^N else 0) := by
  by_cases hg : Gate N x
  · simp only [hg,ite_true]
    have hn := tailWeight_nonneg M x
    have hb := new_weight M N x
    have hp : (0:ℚ)≤1/2^N := by positivity
    split_ifs <;> linarith
  · have h0 : ¬Gate (N+1) x := fun h => hg ((gate_succ N x).mp h).1
    have h1 : ¬Gate (N+1) (x+2^N) := by
      intro h
      exact hg ((gate_shift N x).mp ((gate_succ N (x+2^N)).mp h).1)
    simp [hg,h0,h1]

theorem tail_drift (M N : ℕ) : tail M (N+1)≤tail M N+probability N := by
  unfold tail activeSum
  rw [range_pair]
  have h := Finset.sum_le_sum (s:=Finset.range (2^N))
    (fun x _ => paired_birth M N x)
  simp only [Finset.sum_add_distrib] at h ⊢
  apply le_trans h
  unfold probability activeSum
  rw [Finset.sum_div]
  apply add_le_add le_rfl
  apply Finset.sum_le_sum
  intro x _
  split_ifs <;> simp

theorem tail_initial (M : ℕ) : tail M M=0 := by
  unfold tail activeSum
  apply Finset.sum_eq_zero
  intro x hx
  have h : ¬2^M≤x := by have := Finset.mem_range.mp hx; omega
  simp [tailWeight,h]

/-- Every later population born above 2^M is bounded by the depth-M reserve,
irrespective of its lifetime and of the behavior of all other sources. -/
theorem tail_with_reserve (M k : ℕ) : tail M (M+k)+reserve (M+k)≤reserve M := by
  induction k with
  | zero => simp [tail_initial]
  | succ k ih =>
    have hd := tail_drift M (M+k)
    have hr := reserve_drift (M+k)
    simp only [Nat.add_assoc] at *
    linarith

theorem tail_bound (M N : ℕ) (hMN : M≤N) : tail M N≤reserve M := by
  have h := tail_with_reserve M (N-M)
  rw [Nat.add_sub_of_le hMN] at h
  have hr := reserve_nonneg N
  linarith

theorem activeSum_one (N : ℕ) : activeSum N (fun _ => 1)=(accepted N).card := by
  simp [activeSum, accepted, Finset.sum_boole]

theorem reserve_le_probability (N : ℕ) :
    reserve N≤((3*N+5:ℕ):ℚ)*probability N := by
  have hs : activeSum N (fun x => (debt N x:ℚ)+5)≤
      ((3*N+5:ℕ):ℚ)*activeSum N (fun _ => 1) := by
    unfold activeSum
    rw [Finset.mul_sum]
    apply Finset.sum_le_sum
    intro x _
    by_cases hg : Gate N x
    · simp only [hg,ite_true,mul_one]
      have d : debt N x+5≤3*N+5 := by
        have h := BinaryCylinder.grade_le N x
        unfold debt
        omega
      exact_mod_cast d
    · simp [hg]
  have h := div_le_div_of_nonneg_right hs (by positivity : (0:ℚ)≤2^N)
  simpa [reserve,probability,mul_div_assoc] using h

theorem probability_eighth (k : ℕ) :
    probability (8*k)≤(6561/8192:ℚ)^k := by
  have hn := accepted_card_eighth k
  have h : ((accepted (8*k)).card:ℚ)*(2:ℚ)^(5*k)≤(3:ℚ)^(8*k) := by
    exact_mod_cast hn
  simp only [pow_mul] at h
  norm_num at h
  unfold probability
  rw [activeSum_one,div_pow,pow_mul]
  norm_num
  apply (div_le_div_iff₀ (by positivity) (by positivity)).mpr
  have ht : (8192:ℚ)^k=(32:ℚ)^k*256^k := by rw [←mul_pow]; norm_num
  rw [ht,←mul_assoc]
  exact mul_le_mul_of_nonneg_right h (by positivity)

/-- Explicit decay of all future births, with no Collatz assumption. -/
theorem reserve_eighth (k : ℕ) :
    reserve (8*k)≤(24*(k:ℚ)+5)*(6561/8192:ℚ)^k := by
  have h := reserve_le_probability (8*k)
  have hh := mul_le_mul_of_nonneg_left (probability_eighth k)
    (by positivity : (0:ℚ)≤((3*(8*k)+5:ℕ):ℚ))
  have hs := h.trans hh
  norm_num at hs ⊢
  convert hs using 1
  ring

theorem reserve_geometric (k : ℕ) :
    reserve (8*k)≤128*(31/32:ℚ)^k := by
  have bern := one_add_mul_le_pow (a := (1375/6561:ℚ)) (by norm_num) k
  norm_num at bern
  have kp : (0:ℚ)≤k := Nat.cast_nonneg k
  have linear : 24*(k:ℚ)+5≤128*(1+(k:ℚ)*(1375/6561:ℚ)) := by linarith
  have b : 24*(k:ℚ)+5≤128*(7936/6561:ℚ)^k := by
    exact linear.trans (mul_le_mul_of_nonneg_left bern (by norm_num : (0:ℚ)≤128))
  calc
    reserve (8*k) ≤ (24*(k:ℚ)+5)*(6561/8192:ℚ)^k := reserve_eighth k
    _ ≤ (128*(7936/6561:ℚ)^k)*(6561/8192:ℚ)^k :=
      mul_le_mul_of_nonneg_right b (by positivity)
    _ = 128*(31/32:ℚ)^k := by rw [mul_assoc,←mul_pow]; norm_num

#print axioms reserve_drift
#print axioms tail_drift
#print axioms tail_bound
end BirthReserve
