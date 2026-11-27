import ScaledRamp
import CertifiedRamp

/-! The same finite ordinary prefix budget pays for a scaled virtual ramp.
The scale cancels from the finite-source bound and strengthens the final margin.
No additional convergence hypothesis or numerical certificate is required. -/
set_option autoImplicit false
set_option warningAsError true

namespace RampShadow.Postpeak

private theorem propagate_scaled_margin {K p b L : ℕ} (kp : K ≤ p)
    (initial : (3:ℤ)^K*2^(L+1)*3^b ≤ 4^K*2^b) :
    (3:ℤ)^p*2^(L+1)*3^b ≤ 4^p*2^b := by
  obtain ⟨a,rfl⟩ := Nat.exists_eq_add_of_le kp
  have grow : (3:ℤ)^a ≤ 4^a := pow_le_pow_left₀ (by norm_num) (by norm_num) _
  have X := mul_le_mul initial grow (by positivity) (by positivity)
  rw [pow_add (3:ℤ) K a,pow_add (4:ℤ) K a]
  nlinarith only [X]

/-- Any positive integer scale of a virtual ramp preserves the finite-budget
bonus against every smaller positive source and every lower physical clock. -/
theorem scaled_prepaid_ramp {K b L j e k : ℕ} {s m n c y : ℤ}
    (base : s=0 ∨ s=1) (hn : s<n) (hm : 0<m) (lt : m<n) (cp : 1≤c)
    (precision : (3:ℤ)^K ∣ n-s)
    (rise : (2:ℤ)^j*(y+1)=3^j*c*(n+1)) (W : Walk e k m y)
    (room : b≤K) (budget : SmallPrefixBound b L)
    (margin : (3:ℤ)^(K+1-b)*2^(L+1)*3^b ≤ 4^(K+1-b)*2^b) :
    K+j+b<k := by
  have lower := scaled_ramp base hn hm lt cp precision rise W
  by_contra! upper
  let N : ℤ := c*(n+1)-1
  let S : ℤ := c*(s+1)-1
  have cpos : 0<c := by omega
  have spos : 0≤s := by rcases base with G|G <;> omega
  have nN : n≤N := by
    have P := mul_le_mul_of_nonneg_right cp (show 0≤n+1 by omega)
    dsimp [N]; linarith only [P]
  have Spos : 0≤S := by
    have P := mul_le_mul_of_nonneg_right cp (show 0≤s+1 by omega)
    dsimp [S]; linarith only [P,spos]
  have Splus : S+1=c*(s+1) := by dsimp [S]; ring
  have vrise : (2:ℤ)^j*(y+1)=3^j*(N+1) := by
    dsimp [N]; linear_combination rise
  obtain ⟨d,ed⟩ := Nat.exists_eq_add_of_le
    (clocks_order W (by omega) (show m<N by omega) vrise)
  rw [show e=d+j by omega] at W
  obtain ⟨p,u,z,P,Q,ku⟩ := split W
  have uj := count_le Q
  have bp : b≤p := by omega
  obtain ⟨v,pv⟩ := Nat.exists_eq_add_of_le bp
  obtain ⟨d₀,r,z',dr,F,Suf⟩ := split_odds P b v pv
  have suffix := append Suf Q
  have kcap : v+u≤K+j := by omega
  obtain ⟨w,hw⟩ := precision
  obtain ⟨f,hf⟩ := Nat.exists_eq_add_of_le kcap
  let a : ℤ := 3^f*c*w
  have ha : 3^(v+u)*a=3^j*c*(n-s) := by
    dsimp [a]; rw [hw]
    have eq : (3:ℤ)^(v+u)*3^f=3^j*3^K := by
      rw [←pow_add,←pow_add,show v+u+f=j+K by omega]
    linear_combination c*w*eq
  have haN : 3^(v+u)*a=3^j*(N-S) := by
    dsimp [N,S]; linear_combination ha
  obtain ⟨p',u',z₁,q,z₂,A,ku',u'j,ez',_,V,_,qnon,_,qsmall,_⟩ :=
    translated_origin suffix haN vrise Spos
  rw [Splus] at qsmall
  have finite_shift : 2^b*z'<3^b*n := by
    have grow := shifted_growth F (by omega)
    have big := mul_le_mul_of_nonneg_left (show m+1≤n by omega)
      (show (0:ℤ)≤3^b by positivity)
    nlinarith only [grow,big,show (0:ℤ)<2^b by positivity]
  have bnd : (2:ℤ)^b*2^r*3^j*c < 2*3^b*3^(v+u) := by
    apply lt_of_mul_lt_mul_right _ (show (0:ℤ)≤n-s by omega)
    have X : (2:ℤ)^b*(2^r*a)≤2^b*z' := by
      apply mul_le_mul_of_nonneg_left _ (by positivity); omega
    have Y := mul_lt_mul_of_pos_right (lt_of_le_of_lt X finite_shift)
      (show (0:ℤ)<3^(v+u) by positivity)
    have Z := mul_le_mul_of_nonneg_left (show n≤2*(n-s) by omega)
      (show (0:ℤ)≤3^b*3^(v+u) by positivity)
    have rewriteL : (2:ℤ)^b*(2^r*a)*3^(v+u)=
        (2^b*2^r*3^j*c)*(n-s) := by
      linear_combination (2:ℤ)^b*2^r*ha
    rw [rewriteL] at Y
    nlinarith only [Y,Z]
  have qcap : (2:ℤ)^b*q<4*3^b := by
    apply lt_of_mul_lt_mul_right _ (show (0:ℤ)≤3^(v+u) by positivity)
    have first := mul_lt_mul_of_pos_left qsmall (show (0:ℤ)<2^b by positivity)
    have next := mul_le_mul_of_nonneg_left (show s+1≤2 by omega)
      (show (0:ℤ)≤2^b*2^r*3^j*c by positivity)
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
  have sharpC : (2:ℤ)^b*2^r*c < 2*3^b*3^p' := by
    have U : (3:ℤ)^u'≤3^j := pow_le_pow_right₀ (by norm_num) u'j
    rw [ku',pow_add] at bnd
    have Z := mul_le_mul_of_nonneg_left U
      (show (0:ℤ)≤2*3^b*3^p' by positivity)
    apply lt_of_mul_lt_mul_right _ (show (0:ℤ)≤3^j by positivity)
    nlinarith only [bnd,Z]
  have sharp : (2:ℤ)^b*2^r < 2*3^b*3^p' := by
    have C := mul_le_mul_of_nonneg_left cp
      (show (0:ℤ)≤2^b*2^r by positivity)
    nlinarith only [C,sharpC]
  have scale := mul_lt_mul_of_pos_right sharp (show (0:ℤ)<2^L by positivity)
  have rel := mul_le_mul_of_nonneg_right pay (show (0:ℤ)≤2^b by positivity)
  have floor := propagate_scaled_margin pbig margin
  rw [pow_succ] at floor
  nlinarith only [scale,rel,floor]

#print axioms scaled_prepaid_ramp
end RampShadow.Postpeak

namespace CertifiedRamp
open RampShadow RampShadow.Postpeak

/-- The existing 648-source kernel certificate also controls every positive
integer scale of the virtual ramp endpoint. -/
theorem twelve_extra_scaled_odds {K j e k : ℕ} {s m n c y : ℤ}
    (hK : 84≤K) (base : s=0 ∨ s=1) (hn : s<n) (hm : 0<m) (lt : m<n)
    (cp : 1≤c) (precision : (3:ℤ)^K ∣ n-s)
    (rise : (2:ℤ)^j*(y+1)=3^j*c*(n+1)) (W : Walk e k m y) :
    K+j+12<k := by
  exact scaled_prepaid_ramp base hn hm lt cp precision rise W (by omega)
    finite_budget (margin K hK)

#print axioms twelve_extra_scaled_odds
end CertifiedRamp
