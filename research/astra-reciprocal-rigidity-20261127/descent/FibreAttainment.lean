import InversePrice

namespace RampShadow

private theorem bezout23 (m n : ℕ) :
    ∃ i j : ℤ, 2^m*i+3^n*j=1 := by
  have H := Nat.gcd_eq_gcd_ab (2^m) (3^n)
  have C := Nat.Coprime.pow m n (by decide : Nat.Coprime 2 3)
  rw [C.gcd_eq_one] at H
  push_cast at H
  exact ⟨_,_,H.symm⟩

/-- Two linear congruences and an arbitrary ordinary lower bound. -/
private theorem two_congruences {A B P Q : ℤ} (u N : ℤ) (Ppos : 1≤P) (Qpos : 1≤Q)
    (first : ∃ i j : ℤ, B*i+Q*j=1)
    (second : ∃ g h : ℤ, A*Q*g+P*h=1) :
    ∃ v t c : ℤ, N≤v ∧ u+A*v+1=P*t ∧ 2+B*v=Q*c := by
  obtain ⟨i,j,one⟩ := first
  obtain ⟨g,h,two⟩ := second
  let d := 2*A*i-u-1
  let v₀ := -2*i+Q*g*d
  let r := |N-v₀|+1
  refine ⟨v₀+P*Q*r,-h*d+A*Q*r,2*j+B*g*d+B*P*r,?_,?_,?_⟩
  · have R : 0≤r := by dsimp [r]; positivity
    have big : 1≤P*Q := by nlinarith [mul_nonneg (show 0≤P-1 by omega) (show 0≤Q-1 by omega)]
    have H := mul_le_mul_of_nonneg_right big R
    have G := le_abs_self (N-v₀)
    dsimp [r] at H ⊢; nlinarith only [H,G]
  · dsimp [v₀,d]; linear_combination (2*A*i-u-1)*two
  · dsimp [v₀,d]; linear_combination -2*one

/-- Arbitrarily high actual sources in every prescribed opening ramp,
    constructed from a physical history ending at 1 and a winning cost. -/
theorem arbitrary_attainment {K E b : ℕ} {u : ℤ}
    (row : Walk E K u 1) (winning : (2:ℤ)^(E+b)<3^(K+b)) (H : ℕ) (N : ℤ) :
    ∃ n m : ℤ, N≤n ∧ 0<m ∧ m<n ∧ (3:ℤ)^K ∣ n-1 ∧ (2:ℤ)^H ∣ n+1 ∧
      Walk (b+E) (b+K) m n := by
  obtain ⟨i,j,eq⟩ := bezout23 H K
  obtain ⟨g,h,eq₂⟩ := bezout23 (E+H) b
  rw [pow_add] at eq₂
  have first : ∃ i j : ℤ, 3^K*i+2^H*j=1 := ⟨j,i,by linarith⟩
  let V := max (max N (2*3^b)) (2^b*(u+1)+1)
  obtain ⟨v,t,c,vhigh,bridge,ramp⟩ := two_congruences (A:=(2:ℤ)^E) u V
    (one_le_pow₀ (by norm_num)) (one_le_pow₀ (by norm_num)) first ⟨g,h,eq₂⟩
  have capN : N≤v := le_trans (le_trans (le_max_left _ _) (le_max_left _ _)) vhigh
  have capT : (2:ℤ)*3^b≤v := le_trans (le_trans (le_max_right _ _) (le_max_left _ _)) vhigh
  have capU : (2:ℤ)^b*(u+1)+1≤v := le_trans (le_max_right _ _) vhigh
  have M : Walk (b+E) (b+K) (2^b*t-1) (1+3^K*v) := decode_one_fibre row bridge
  have u0 : 0≤u := nonneg_of_terminal row (by norm_num)
  have v0 : 0≤v := by linarith [show (0:ℤ)<3^b by positivity]
  have e1 : (1:ℤ)≤2^E := one_le_pow₀ (by norm_num)
  have B1 : (1:ℤ)≤2^b := one_le_pow₀ (by norm_num)
  have K1 : (1:ℤ)≤3^K := one_le_pow₀ (by norm_num)
  have tpos : 1<t := by
    by_contra! ht
    have X := mul_le_mul_of_nonneg_left ht (show (0:ℤ)≤3^b by positivity)
    have Y := mul_le_mul_of_nonneg_right e1 v0
    nlinarith [show (0:ℤ)<3^b by positivity]
  have mpos : 0<2^b*t-1 := by
    have := mul_le_mul_of_nonneg_right B1 (show 0≤t by omega)
    nlinarith only [this,tpos]
  rw [pow_add,pow_add] at winning
  have cost : (2:ℤ)^E*2^b+1≤3^K*3^b := by omega
  have paid := mul_le_mul_of_nonneg_right cost v0
  have small : 2^b*t-1<1+3^K*v := by
    apply lt_of_mul_lt_mul_right _ (show (0:ℤ)≤3^b by positivity)
    have twice := congrArg (fun x : ℤ => 2^b*x) bridge
    nlinarith only [paid,capU,twice,show (0:ℤ)<3^b by positivity]
  refine ⟨1+3^K*v,2^b*t-1,?_,mpos,small,⟨v,by ring⟩,⟨c,by linarith⟩,M⟩
  have := mul_le_mul_of_nonneg_right K1 v0
  nlinarith only [capN,this]

/-- Exact test for attainable contraction. All upper precision and lower
    height choices are made before selecting the two ordinary sources. -/
theorem contracting_rows_iff (K b : ℕ) :
    (2:ℤ)^(price K+b)<3^(K+b) ↔
    ∀ (H : ℕ) (N : ℤ), ∃ (n m : ℤ) (e : ℕ),
      N≤n ∧ 0<m ∧ m<n ∧ (3:ℤ)^K ∣ n-1 ∧ (2:ℤ)^H ∣ n+1 ∧
      Walk e (b+K) m n ∧ (2:ℤ)^e<3^(K+b) := by
  constructor
  · intro win H N
    obtain ⟨u,W⟩ := price_row K
    obtain ⟨n,m,large,pos,lt,tern,dyad,hit⟩ := arbitrary_attainment W win H N
    exact ⟨n,m,b+price K,large,pos,lt,tern,dyad,hit,by simpa [Nat.add_comm] using win⟩
  · intro all
    obtain ⟨n,m,e,_,_,_,tern,_,W,win⟩ := all 0 0
    have low := price_lower_budget tern W
    exact lt_of_le_of_lt (pow_le_pow_right₀ (by norm_num) low) win

#print axioms arbitrary_attainment
#print axioms contracting_rows_iff
end RampShadow
