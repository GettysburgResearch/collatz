import RampShadow
import Mathlib.Data.Nat.ModEq

namespace RampShadow

private theorem row_exists (K : ℕ) : ∃ e, ∃ u : ℤ, Walk e K u 1 := by
  exact ⟨2*K,1,by simpa using lifted_twos K 0⟩

/-- Least native shortcut clock among all actual K-odd histories ending at 1. -/
noncomputable def price (K : ℕ) : ℕ := by
  classical
  exact Nat.find (row_exists K)

theorem price_row (K : ℕ) : ∃ u : ℤ, Walk (price K) K u 1 := by
  classical
  exact Nat.find_spec (row_exists K)

theorem price_min {f K : ℕ} {u : ℤ} (w : Walk f K u 1) : price K≤f := by
  classical
  exact Nat.find_min' (row_exists K) ⟨u,w⟩

theorem price_lower_budget {K b e : ℕ} {x n : ℤ} (near : (3:ℤ)^K ∣ n-1)
    (w : Walk e (b+K) x n) : price K+b≤e :=
  one_fibre_price (fun _ _ h => price_min h) near w

theorem price_increment (K : ℕ) :
    price K+1≤price (K+1) ∧ price (K+1)≤price K+2 := by
  obtain ⟨x,W⟩ := price_row (K+1)
  have lower := price_lower_budget (b:=1) (K:=K) (n:=1)
    (by simp) (by simpa [Nat.add_comm] using W : Walk (price (K+1)) (1+K) x 1)
  obtain ⟨u,U⟩ := price_row K
  have loop := lifted_twos 1 0
  norm_num at loop
  exact ⟨lower,price_min (append U loop)⟩

private theorem cycle_clock {h p : ℕ} {x y : ℤ} (w : Walk h p x y)
    (start : x=1 ∨ x=2) : (y=1 ∨ y=2) ∧ 2*(p:ℤ)+x=(h:ℤ)+y := by
  induction w <;> omega

private theorem power_margin (r : ℕ) : ((3:ℤ)+r)*3^r≤3*4^r := by
  induction r with
  | zero => norm_num
  | succ r ih =>
    simp only [Nat.cast_succ,pow_succ]
    nlinarith [mul_nonneg (Int.natCast_nonneg r) (show (0:ℤ)≤3^r by positivity)]

/-- At a *fixed* ordinary source, arbitrarily long visits to 1 must spend
    two shortcut clocks per additional odd input after their first arrival. -/
private theorem fixed_margin (u : ℤ) (B : ℕ) :
    ∃ K₀ : ℕ, ∀ K e : ℕ, K₀≤K → Walk e K u 1 → (B:ℤ)*3^K<2^e := by
  by_cases reach : ∃ h p, Walk h p u 1
  · obtain ⟨h,p,W⟩ := reach
    refine ⟨h+3*B*3^p+1,?_⟩
    intro K e late V
    have hK : h≤K := by omega
    have hE : h≤e := le_trans hK (count_le V)
    obtain ⟨d,hd⟩ := Nat.exists_eq_add_of_le hE
    rw [hd] at V
    obtain ⟨a,b,z,P,Q,Kab⟩ := split V
    have z1 : z=1 := (readout P).1.symm.trans (readout W).1
    have ap : a=p := (readout P).2.symm.trans (readout W).2
    subst z; subst a
    have D := (cycle_clock Q (Or.inl rfl)).2
    have deq : d=2*b := by omega
    have ph := count_le W
    have big : ((3*B*3^p:ℕ):ℤ)<b := by exact_mod_cast (show 3*B*3^p<b by omega)
    push_cast at big
    have bp := power_margin b
    have lb : (B:ℤ)*3^p*3^b < 4^b := by
      have mult := mul_lt_mul_of_pos_right big (show (0:ℤ)<3^b by positivity)
      nlinarith only [mult,bp,show (0:ℤ)<3^b by positivity]
    have keep := mul_le_mul_of_nonneg_right (one_le_pow₀ (by norm_num : (1:ℤ)≤2) (n:=h))
      (show (0:ℤ)≤4^b by positivity)
    rw [Kab,hd,deq,pow_add,pow_add,pow_mul]
    norm_num only [Int.reducePow] at *
    rw [one_mul] at keep
    nlinarith only [lb,keep]
  · exact ⟨0,fun K e _ W => False.elim (reach ⟨e,K,W⟩)⟩

private theorem finite_margin (B M : ℕ) :
    ∃ K₀ : ℕ, ∀ u : ℕ, u≤M → ∀ K e : ℕ, K₀≤K →
      Walk e K (u:ℤ) 1 → (B:ℤ)*3^K<2^e := by
  induction M with
  | zero =>
    obtain ⟨K₀,H⟩ := fixed_margin 0 B
    refine ⟨K₀,?_⟩
    intro u hu
    have eu : u=0 := Nat.le_zero.mp hu
    simpa [eu] using H
  | succ M ih =>
    obtain ⟨X,H⟩ := ih
    obtain ⟨Y,J⟩ := fixed_margin (M+1:ℕ) B
    refine ⟨max X Y,?_⟩
    intro u hu K e Kbig W
    by_cases low : u≤M
    · exact H u low K e (by omega) W
    · have eq : u=M+1 := by omega
      subst u
      exact J K e (by omega) W

/-- The least possible inverse multiplier at the single terminal 1 tends
    to infinity. Both the unit-cycle and every finite source are kept. -/
theorem price_multiplier_escapes (B : ℕ) :
    ∃ K₀ : ℕ, ∀ K : ℕ, K₀≤K → (B:ℤ)*3^K < 2^(price K) := by
  obtain ⟨K₀,H⟩ := finite_margin B B
  refine ⟨K₀,?_⟩
  intro K late
  obtain ⟨u,W⟩ := price_row K
  by_contra! bound
  obtain ⟨A,hA,_,eq⟩ := affine W
  have nonneg := nonneg_of_terminal W (by norm_num)
  have uB : u≤(B:ℤ) := by
    by_contra! hu
    have F := mul_lt_mul_of_pos_left hu (show (0:ℤ)<3^K by positivity)
    nlinarith only [bound,eq,hA,F]
  have id : (u.toNat:ℤ)=u := Int.toNat_of_nonneg nonneg
  have cap : u.toNat≤B := by omega
  exact (not_lt_of_ge bound) (H u.toNat cap K (price K) late (by simpa [id] using W))

/-- No fixed number of extra odd inputs can deliver a coefficient-contractive
    inverse path on any sufficiently deep fibre at 1. -/
theorem fixed_repayment_insufficient (b : ℕ) :
    ∃ K₀ : ℕ, ∀ K e : ℕ, ∀ x n : ℤ, K₀≤K →
      (3:ℤ)^K ∣ n-1 → Walk e (b+K) x n → (3:ℤ)^(b+K)<2^e := by
  obtain ⟨K₀,H⟩ := price_multiplier_escapes (3^b)
  refine ⟨K₀,?_⟩
  intro K e x n late near W
  have hp : price K≤e := by have := price_lower_budget near W; omega
  have cap := H K late
  push_cast at cap
  rw [pow_add]
  exact lt_of_lt_of_le cap (pow_le_pow_right₀ (by norm_num) hp)

#print axioms price_increment
#print axioms price_multiplier_escapes
#print axioms fixed_repayment_insufficient
end RampShadow
