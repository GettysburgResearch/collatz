import RampShadow

namespace RampShadow

/-- On a physical positive path, an even input cannot increase x+1.
    Odd inputs multiply x+1 by exactly 3/2. -/
theorem shifted_growth {d p x y} (W : Walk d p x y) (hx : 0≤x) :
    (2:ℤ)^p*(y+1) ≤ 3^p*(x+1) := by
  induction W with
  | nil => simp
  | @even h p x y W IH =>
    have hx' : 0≤x := by omega
    have F := IH hx'
    nlinarith [mul_nonneg (show (0:ℤ)≤3^p by positivity) hx']
  | @odd h p x y z eq W IH =>
    have F := IH (show 0≤y by omega)
    have G := congrArg (fun r : ℤ => 3^p*r) eq
    simp only [pow_succ]
    nlinarith only [F,G]

/-- A fixed finite set of ordinary source prefixes controls all subsequent
    requested precisions. Zero is excluded since it has no odd departure. -/
def SmallPrefixBound (b L : ℕ) : Prop :=
  ∀ q : ℤ, 0<q → 2^b*q<4*3^b →
  ∀ d p : ℕ, ∀ z : ℤ, Walk d p q z → 2*p≤d+L

private theorem propagate_margin {K p b L : ℕ} (kp : K≤p)
    (initial : (3:ℤ)^K*2^(L+1)*3^b ≤ 4^K*2^b) :
    (3:ℤ)^p*2^(L+1)*3^b ≤ 4^p*2^b := by
  obtain ⟨a,rfl⟩ := Nat.exists_eq_add_of_le kp
  have grow : (3:ℤ)^a ≤4^a := pow_le_pow_left₀ (by norm_num) (by norm_num) _
  have X := mul_le_mul initial grow (by positivity) (by positivity)
  rw [pow_add (3:ℤ) K a,pow_add (4:ℤ) K a]
  nlinarith only [X]

/-- Any visitor costing at most K+j+b odds would provide a forbidden
    ordinary finite-source prefix, even with unbounded lower shortcut clock. -/
theorem prepaid_ramp {K b L j e k : ℕ} {s m n y : ℤ} (base : s=0 ∨ s=1)
    (hn : s<n) (hm : 0<m) (lt : m<n) (precision : (3:ℤ)^K ∣ n-s)
    (rise : (2:ℤ)^j*(y+1)=3^j*(n+1)) (W : Walk e k m y)
    (room : b≤K) (budget : SmallPrefixBound b L)
    (margin : (3:ℤ)^(K+1-b)*2^(L+1)*3^b ≤ 4^(K+1-b)*2^b) : K+j+b<k := by
  have lower := ramp_barrier base hn hm lt precision rise W
  by_contra! upper
  obtain ⟨d,ed⟩ := Nat.exists_eq_add_of_le (clocks_order W (by omega) lt rise)
  rw [show e=d+j by omega] at W
  obtain ⟨p,u,z,P,Q,ku⟩ := split W
  have uj := count_le Q
  have bp : b≤p := by omega
  obtain ⟨v,pv⟩ := Nat.exists_eq_add_of_le bp
  obtain ⟨d₀,r,z',dr,F,S⟩ := split_odds P b v pv
  have suffix := append S Q
  have kcap : v+u≤K+j := by omega
  obtain ⟨w,hw⟩ := precision
  obtain ⟨f,hf⟩ := Nat.exists_eq_add_of_le kcap
  let a : ℤ := 3^f*w
  have ha : 3^(v+u)*a=3^j*(n-s) := by
    dsimp [a]; rw [hw]
    rw [←mul_assoc,←pow_add,←hf,Nat.add_comm K j,pow_add]; ring
  obtain ⟨p',u',z₁,q,z₂,A,ku',u'j,ez',_,V,_,qnon,_,qsmall,_⟩ :=
    translated_origin suffix ha rise (by omega)
  have finite_shift : 2^b*z'<3^b*n := by
    have grow := shifted_growth F (by omega)
    have big := mul_le_mul_of_nonneg_left (show m+1≤n by omega)
      (show (0:ℤ)≤3^b by positivity)
    nlinarith only [grow,big,show (0:ℤ)<2^b by positivity]
  have bnd : (2:ℤ)^b*2^r*3^j < 2*3^b*3^(v+u) := by
    apply lt_of_mul_lt_mul_right _ (show (0:ℤ)≤n-s by omega)
    have X : (2:ℤ)^b*(2^r*a)≤2^b*z' := by
      apply mul_le_mul_of_nonneg_left _ (by positivity); omega
    have Y := mul_lt_mul_of_pos_right (lt_of_le_of_lt X finite_shift)
      (show (0:ℤ)<3^(v+u) by positivity)
    have Z := mul_le_mul_of_nonneg_left (show n≤2*(n-s) by omega)
      (show (0:ℤ)≤3^b*3^(v+u) by positivity)
    have rewriteL : (2:ℤ)^b*(2^r*a)*3^(v+u)=(2^b*2^r*3^j)*(n-s) := by
      linear_combination (2:ℤ)^b*2^r*ha
    rw [rewriteL] at Y
    nlinarith only [Y,Z]
  have qcap : (2:ℤ)^b*q<4*3^b := by
    apply lt_of_mul_lt_mul_right _ (show (0:ℤ)≤3^(v+u) by positivity)
    have first := mul_lt_mul_of_pos_left qsmall (show (0:ℤ)<2^b by positivity)
    have next := mul_le_mul_of_nonneg_left (show s+1≤2 by omega)
      (show (0:ℤ)≤2^b*2^r*3^j by positivity)
    nlinarith only [first,next,bnd]
  have pbig : K+1-b≤p' := by omega
  have qpos : 0<q := by
    by_contra! hq
    have eq := (zero_origin V (by omega)).1
    omega
  have lim := budget q qpos qcap r p' z₂ V
  have pay : (4:ℤ)^p'≤2^r*2^L := by
    rw [←pow_add,show (4:ℤ)=2^2 by norm_num,←pow_mul]
    exact pow_le_pow_right₀ (by norm_num) lim
  have sharp : (2:ℤ)^b*2^r < 2*3^b*3^p' := by
    have U : (3:ℤ)^u'≤3^j := pow_le_pow_right₀ (by norm_num) u'j
    rw [ku',pow_add] at bnd
    have Z := mul_le_mul_of_nonneg_left U (show (0:ℤ)≤2*3^b*3^p' by positivity)
    apply lt_of_mul_lt_mul_right _ (show (0:ℤ)≤3^j by positivity)
    nlinarith only [bnd,Z]
  have scale := mul_lt_mul_of_pos_right sharp (show (0:ℤ)<2^L by positivity)
  have rel := mul_le_mul_of_nonneg_right pay (show (0:ℤ)≤2^b by positivity)
  have floor := propagate_margin pbig margin
  rw [pow_succ] at floor
  nlinarith only [scale,rel,floor]

#print axioms prepaid_ramp
end RampShadow
