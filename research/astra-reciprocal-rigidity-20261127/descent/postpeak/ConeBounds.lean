import PostWords

namespace RampShadow.Postpeak

private theorem positive_envelope {e k x y} (W : Walk e k x y) (hx : 0<x) :
    (3/2:ℚ)^(e-k)*(y+1) ≤ (3/2:ℚ)^k*(x+1) := by
  induction W with
  | nil => simp
  | @even h p x y W IH =>
    have hp := count_le W
    have X : 0<x := by omega
    have prod := mul_le_mul_of_nonneg_left (IH X) (show (0:ℚ)≤3/2 by norm_num)
    have edge : (3/2:ℚ)*((x:ℚ)+1) ≤ (2*x:ℤ)+1 := by
      have a : (1:ℚ)≤x := by exact_mod_cast X
      push_cast
      linarith
    have edge' := mul_le_mul_of_nonneg_left edge (show (0:ℚ)≤(3/2:ℚ)^p by positivity)
    rw [show h+1-p=(h-p)+1 by omega,pow_succ]
    nlinarith only [prod,edge']
  | @odd h p x y z edge W IH =>
    have Y : 0<y := by omega
    have edge' : 3*(x:ℚ)+1=2*y := by exact_mod_cast edge
    have aux := congrArg (fun a : ℚ => (3/2:ℚ)^p*a) edge'
    try dsimp at aux
    rw [show h+1-(p+1)=h-p by omega,pow_succ]
    nlinarith only [IH Y,aux]

private theorem reverse_envelope {t f x y} (W : Walk t f x y) :
    (3:ℚ)^f*(x+1) ≤ (2:ℚ)^t*(y+1) := by
  induction W with
  | nil => simp
  | @even h p x y W IH =>
    have pos : (0:ℚ)≤3^p := by positivity
    push_cast
    rw [pow_succ]
    nlinarith only [IH,pos]
  | @odd h p x y z edge W IH =>
    have edge' : 3*(x:ℚ)+1=2*y := by exact_mod_cast edge
    have aux := congrArg (fun a : ℚ => (3:ℚ)^p*a) edge'
    try dsimp at aux
    rw [pow_succ,pow_succ]
    nlinarith only [IH,aux]

/-- Competing lower walks in the near-optimal sublevel have only a short
    even budget, regardless of their total clock. -/
theorem cheap_budget {H t f e k d : ℕ} {v m Y : ℤ}
    (pos : 0<v) (mp : 0<m) (lt : m<(2:ℤ)^H*v-1)
    (upper : Walk t f ((3:ℤ)^H*v-1) Y) (lower : Walk e k m Y)
    (grade : k+d=H+f) :
    (3/2:ℚ)^(e-k+d)*2^f < 2^t := by
  have P := positive_envelope lower mp
  have Q := reverse_envelope upper
  push_cast at Q
  ring_nf at Q
  have V : (0:ℚ)<v := by exact_mod_cast pos
  have M : (m:ℚ)+1<(2:ℚ)^H*v := by
    exact_mod_cast (show m+1<(2:ℤ)^H*v by omega)
  have poweq : (3:ℚ)^H*3^f=(3/2:ℚ)^k*(3/2:ℚ)^d*2^H*2^f := by
    rw [←pow_add (3:ℚ),←pow_add (3/2:ℚ)]
    rw [show (3/2:ℚ)^(k+d)*2^H*2^f=(3/2:ℚ)^(k+d)*2^(H+f) by rw [pow_add];ring]
    rw [grade,←mul_pow]; norm_num
  have lhs := mul_le_mul_of_nonneg_left Q (show 0≤(3/2:ℚ)^(e-k) by positivity)
  have rhs := mul_le_mul_of_nonneg_left P (show (0:ℚ)≤2^t by positivity)
  have strict := mul_lt_mul_of_pos_left M (show (0:ℚ)<2^t*(3/2:ℚ)^k by positivity)
  have direct : (3/2:ℚ)^(e-k)*((3:ℚ)^H*3^f)*v <
      2^t*(3/2:ℚ)^k*2^H*v := by nlinarith only [lhs,rhs,strict]
  rw [poweq] at direct
  apply lt_of_mul_lt_mul_right (a:=(3/2:ℚ)^k*2^H*v)
  · rw [pow_add]; nlinarith only [direct]
  · positivity

theorem budget_linear {l d f t : ℕ}
    (h : (3/2:ℚ)^(l+d)*2^f < 2^t) : l+d < 2*t := by
  have F : (1:ℚ)≤2^f := one_le_pow₀ (by norm_num)
  have L : (3/2:ℚ)^(l+d) < 2^t := by
    have Z := mul_le_mul_of_nonneg_left F (show 0≤(3/2:ℚ)^(l+d) by positivity)
    linarith
  by_contra! G
  have g := pow_le_pow_right₀ (show (1:ℚ)≤3/2 by norm_num) G
  have two := pow_le_pow_left₀ (by norm_num : (0:ℚ)≤2) (by norm_num : (2:ℚ)≤(3/2)^2) t
  rw [pow_mul] at g
  linarith

theorem actual_even_budget {l d f t : ℕ} (ft : f≤t)
    (h : (3/2:ℚ)^(l+d)*2^f < 2^t) : l+d<2*(t-f) := by
  have G : (3/2:ℚ)^(l+d)*2^0 < 2^(t-f) := by
    simp only [pow_zero,mul_one]
    apply lt_of_mul_lt_mul_right (a:=(2:ℚ)^f)
    · rw [←pow_add,show t-f+f=t by omega];exact h
    · positivity
  exact budget_linear G

/-- The number of even steps stays small even after the specified positive
    overspend in the lower odd budget. -/
theorem overflow_even_count {H t f e k b : ℕ} {v m Y : ℤ}
    (pos : 0<v) (mp : 0<m) (lt : m<(2:ℤ)^H*v-1)
    (upper : Walk t f ((3:ℤ)^H*v-1) Y) (lower : Walk e k m Y)
    (grade : k=H+f+b) : e-k≤2*(t-f)+b := by
  by_cases short : e-k≤b
  · omega
  obtain ⟨l,el⟩ := Nat.exists_eq_add_of_le (show b≤e-k by omega)
  have P := positive_envelope lower mp
  have Q := reverse_envelope upper
  push_cast at Q
  ring_nf at Q
  have V : (0:ℚ)<v := by exact_mod_cast pos
  have M : (m:ℚ)+1<(2:ℚ)^H*v := by
    exact_mod_cast (show m+1<(2:ℤ)^H*v by omega)
  have d3 : (3:ℚ)^H*3^f=(3/2:ℚ)^(H+f)*2^H*2^f := by
    rw [←pow_add (3:ℚ)]
    rw [show (3/2:ℚ)^(H+f)*2^H*2^f=(3/2:ℚ)^(H+f)*2^(H+f) by rw [pow_add (2:ℚ)];ring]
    rw [←mul_pow];norm_num
  have lhs := mul_le_mul_of_nonneg_left Q (show 0≤(3/2:ℚ)^(e-k) by positivity)
  have rhs := mul_le_mul_of_nonneg_left P (show (0:ℚ)≤2^t by positivity)
  have strict := mul_lt_mul_of_pos_left M (show (0:ℚ)<2^t*(3/2:ℚ)^k by positivity)
  have direct : (3/2:ℚ)^(e-k)*((3:ℚ)^H*3^f)*v <
      2^t*(3/2:ℚ)^k*2^H*v := by nlinarith only [lhs,rhs,strict]
  rw [d3,el,pow_add (3/2:ℚ) b l,grade,pow_add (3/2:ℚ) (H+f) b] at direct
  have cheap : (3/2:ℚ)^(l+0)*2^f < 2^t := by
    apply lt_of_mul_lt_mul_right (a:=(3/2:ℚ)^(H+f)*(3/2:ℚ)^b*2^H*v)
    · simp only [add_zero];nlinarith only [direct]
    · positivity
  have B := actual_even_budget (l:=l) (d:=0) (count_le upper) cheap
  omega

end RampShadow.Postpeak
