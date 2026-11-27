import FairGrid

/-! Finite geometric summation of a power-saving occupation bound. -/
set_option autoImplicit false
set_option warningAsError true

namespace ReciprocalPacking
open Finset

noncomputable def ratio : ℝ := 6561/8192

private def band (I : Finset ℕ) (v : ℕ → ℕ) (K N : ℕ) : Finset ℕ :=
  I.filter (fun i => 8192^K≤v i ∧ v i<8192^(K+N))

private theorem band_one (I : Finset ℕ) (v : ℕ → ℕ)
    (packing : ∀ k : ℕ, (I.filter (fun i => v i<8192^k)).card≤4*6561^k)
    (K : ℕ) : ∑ i∈band I v K 1, (1/(v i:ℝ)) ≤ 26244*ratio^K := by
  let A := band I v K 1
  have sub : A⊆I.filter (fun i => v i<8192^(K+1)) := by
    intro i hi
    exact mem_filter.mpr ⟨(mem_filter.mp hi).1,(mem_filter.mp hi).2.2⟩
  have count := (card_le_card sub).trans (packing (K+1))
  have cast : (A.card:ℝ)≤4*(6561:ℝ)^(K+1) := by exact_mod_cast count
  calc
    _ ≤ ∑ _i∈A, (1:ℝ)/8192^K := by
      apply sum_le_sum
      intro i hi
      have low : 8192^K≤v i := (mem_filter.mp hi).2.1
      exact one_div_le_one_div_of_le (by positivity) (by exact_mod_cast low)
    _ = (A.card:ℝ)*(1/8192^K) := by simp
    _ ≤ (4*6561^(K+1))*(1/8192^K) := mul_le_mul_of_nonneg_right cast (by positivity)
    _ = _ := by rw [ratio,div_pow,pow_succ]; ring

private theorem finite_band (I : Finset ℕ) (v : ℕ → ℕ)
    (packing : ∀ k : ℕ, (I.filter (fun i => v i<8192^k)).card≤4*6561^k)
    (N K : ℕ) : ∑ i∈band I v K N, (1/(v i:ℝ)) ≤ 262144*ratio^K := by
  induction N generalizing K with
  | zero =>
    have empty : band I v K 0=∅ := by
      ext i
      simp [band]
    rw [empty,sum_empty]
    unfold ratio
    positivity
  | succ N ih =>
    have next := Nat.pow_le_pow_right (by decide : 0<8192) (show K≤K+1 by omega)
    have top := Nat.pow_le_pow_right (by decide : 0<8192) (show K+1≤K+1+N by omega)
    have split : band I v K (N+1) = band I v K 1 ∪ band I v (K+1) N := by
      ext i
      simp only [band,mem_filter,mem_union,show K+(N+1)=K+1+N by omega]
      constructor
      · rintro ⟨hi,low,upper⟩
        by_cases mid : v i<8192^(K+1)
        · exact Or.inl ⟨hi,low,mid⟩
        · exact Or.inr ⟨hi,Nat.le_of_not_gt mid,upper⟩
      · rintro (⟨hi,low,mid⟩|⟨hi,mid,upper⟩)
        · exact ⟨hi,low,lt_of_lt_of_le mid top⟩
        · exact ⟨hi,next.trans mid,upper⟩
    have disjoint : Disjoint (band I v K 1) (band I v (K+1) N) := by
      apply Finset.disjoint_left.mpr
      intro i hi hj
      exact (Nat.not_le_of_gt (mem_filter.mp hi).2.2) (mem_filter.mp hj).2.1
    rw [split,sum_union disjoint]
    calc
      _ ≤ 26244*ratio^K+262144*ratio^(K+1) :=
        add_le_add (band_one I v packing K) (ih (K+1))
      _ = (26244+262144*ratio)*ratio^K := by rw [pow_succ]; ring
      _ ≤ 262144*ratio^K := mul_le_mul_of_nonneg_right (by norm_num [ratio]) (by unfold ratio; positivity)

/-- The estimate holds for every finite index menu. Neither positivity of the
function below the cutoff nor a bound for the largest value is required. -/
theorem finite_tail (I : Finset ℕ) (v : ℕ → ℕ)
    (packing : ∀ k : ℕ, (I.filter (fun i => v i<8192^k)).card≤4*6561^k)
    (K : ℕ) : ∑ i∈I.filter (fun i => 8192^K≤v i), (1/(v i:ℝ)) ≤ 262144*ratio^K := by
  let N := (∑i∈I, v i)+1
  have full : I.filter (fun i => 8192^K≤v i)=band I v K N := by
    ext i
    simp only [band,mem_filter]
    constructor
    · rintro ⟨hi,lo⟩
      have sumL : v i≤∑j∈I, v j := single_le_sum (fun _ _ => Nat.zero_le _) hi
      have ltN : v i<N := by dsimp [N]; omega
      have p := Nat.lt_pow_self (a:=8192) (n:=K+N) (by decide)
      exact ⟨hi,lo,by omega⟩
    · rintro ⟨hi,lo,_⟩
      exact ⟨hi,lo⟩
  rw [full]
  exact finite_band I v packing N K

#print axioms finite_tail
end ReciprocalPacking

