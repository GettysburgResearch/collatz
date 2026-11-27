import HitClock

/-! The actual finite potential is monotone. Its universal reserve bound
cannot bootstrap verification past the supplied finite source cutoff. -/
set_option autoImplicit false
set_option warningAsError true

namespace PotentialBoundary
open CoreBranching PeakRigidity BinaryPrefixCriterion BinaryCylinder BirthReserve
open FiniteExtinction
open scoped BigOperators

def potential (N : ℕ) : ℚ := mass N+reserve N

theorem mass_tail_zero (N : ℕ) : mass N=tail 0 N := by
  rw [mass_active]
  unfold tail activeSum
  apply Finset.sum_congr rfl
  intro x _
  by_cases hx : x=0
  · simp [hx,tailWeight]
  · have hp : 1≤x := by omega
    simp [tailWeight,hp]

theorem potential_step (N : ℕ) : potential (N+1)≤potential N := by
  have birth := tail_drift 0 N
  have drift := reserve_drift N
  rw [←mass_tail_zero,←mass_tail_zero] at birth
  unfold potential
  linarith

theorem potential_antitone : Antitone potential :=
  antitone_nat_of_succ_le potential_step

theorem potential_initial : potential 0=5 := by
  rw [potential,mass_active]
  norm_num [reserve,activeSum,Gate,debt,grade]

theorem potential_bound (N : ℕ) : potential N≤5 := by
  simpa [potential_initial] using potential_antitone (Nat.zero_le N)

theorem ascent_grade (n b : ℕ) (positive : 0<b) : grade n (2^n*b-1)=n := by
  induction n generalizing b with
  | zero => rfl
  | succ n ih =>
    have p : 0<2^n*b := by positivity
    have form : 2^(n+1)*b-1=2*(2^n*b-1)+1 := by
      rw [pow_succ,show 2^n*2*b=2*(2^n*b) by ring]
      omega
    have st : step (2^(n+1)*b-1)=2^n*(3*b)-1 := by
      rw [form,step_odd,show 2^n*(3*b)=3*(2^n*b) by ring]
      omega
    have word : run 1 (2^(n+1)*b-1)=2^n*(3*b)-1 := by
      simpa [run] using st
    have first : grade 1 (2^(n+1)*b-1)=1 := by simp [grade,run,form]
    have whole := grade_add 1 n (2^(n+1)*b-1)
    rw [first,word,ih (3*b) (by omega)] at whole
    simpa only [Nat.add_comm 1 n] using whole

theorem mersenne_gate (N : ℕ) : Gate N (2^N-1) := by
  intro j hj
  have bound : j≤N := by have := Finset.mem_range.mp hj; omega
  have form : 2^j*2^(N-j)=(2:ℕ)^N := by rw [←pow_add,Nat.add_sub_of_le bound]
  have g := ascent_grade j (2^(N-j)) (by positivity)
  rw [form] at g
  simpa [g] using (show 5*j≤8*j by omega)

/-- The all-odd source below the cutoff gives a lower bound on the reserve. -/
theorem reserve_floor (N : ℕ) :
    (3*(N:ℚ)+5)/(2:ℚ)^N≤reserve N := by
  have p : 0<(2:ℕ)^N := by positivity
  have member : 2^N-1∈Finset.range (2^N) := Finset.mem_range.mpr (by omega)
  have g : grade N (2^N-1)=N := by
    simpa using ascent_grade N 1 (by decide)
  have debt_value : debt N (2^N-1)=3*N := by unfold debt; rw [g]; omega
  have sum_bound := Finset.single_le_sum
    (f:=fun x : ℕ => if Gate N x then (debt N x:ℚ)+5 else 0)
    (s:=Finset.range (2^N))
    (fun x _ => by split_ifs <;> positivity) member
  simp only [mersenne_gate,ite_true,debt_value,Nat.cast_mul,Nat.cast_ofNat] at sum_bound
  exact div_le_div_of_nonneg_right sum_bound (by positivity)

/-- A bound by reserve N alone is never small enough to certify the same
or a larger input range via the reciprocal-mass cutoff criterion. -/
theorem no_cutoff_bootstrap (N B : ℕ) (large : 2^N≤B) :
    1/(B:ℚ)≤reserve N := by
  have cast : (2:ℚ)^N≤(B:ℚ) := by exact_mod_cast large
  have inv := one_div_le_one_div_of_le (by positivity : (0:ℚ)<2^N) cast
  have num : (1:ℚ)/(2:ℚ)^N≤(3*(N:ℚ)+5)/(2:ℚ)^N := by
    apply div_le_div_of_nonneg_right
    · have h := Nat.cast_nonneg (α:=ℚ) N; linarith
    · positivity
  exact inv.trans (num.trans (reserve_floor N))

#print axioms potential_antitone
#print axioms potential_bound
#print axioms reserve_floor
#print axioms no_cutoff_bootstrap
end PotentialBoundary
