import SignedEscape

namespace RampShadow.Postpeak.MirrorEnergy

def family (q x : ℤ) : Prop := ∃ j : ℕ, x = -(2^j*q)

noncomputable def energy (x : ℤ) : ℤ := by
  classical
  exact if family 3 x then 400*x^2 else if family 5 x then 441*x^2 else 450*x^2

private theorem family_dvd {q x : ℤ} (h : family q x) : q ∣ x := by
  obtain ⟨j,rfl⟩ := h
  exact ⟨-(2^j),by ring⟩

private theorem family_double (q x : ℤ) (odd : q%2=1) :
    family q (2*x) ↔ family q x := by
  constructor
  · rintro ⟨j,h⟩
    cases j with
    | zero => simp only [pow_zero,one_mul] at h;omega
    | succ j =>
      refine ⟨j,?_⟩
      rw [pow_succ] at h
      nlinarith only [h]
  · rintro ⟨j,h⟩
    refine ⟨j+1,?_⟩
    rw [pow_succ,h]
    ring

theorem energy_double (x : ℤ) : energy (2*x)=4*energy x := by
  classical
  simp only [energy,family_double 3 x (by norm_num),family_double 5 x (by norm_num)]
  split_ifs <;> ring

theorem energy_bounds (x : ℤ) : 400*x^2≤energy x ∧ energy x≤450*x^2 := by
  classical
  unfold energy
  split_ifs <;> constructor <;> nlinarith [sq_nonneg x]

private theorem energy_not_three {x : ℤ} (h : ¬3∣x) : 441*x^2≤energy x := by
  classical
  have F : ¬family 3 x := fun H => h (family_dvd H)
  simp only [energy,F,↓reduceIte]
  split_ifs <;> nlinarith [sq_nonneg x]

private theorem energy_coprime {x : ℤ} (h3 : ¬3∣x) (h5 : ¬5∣x) :
    energy x=450*x^2 := by
  classical
  have F3 : ¬family 3 x := fun H => h3 (family_dvd H)
  have F5 : ¬family 5 x := fun H => h5 (family_dvd H)
  simp [energy,F3,F5]

private theorem family_negative {q x : ℤ} (hq : 0<q) (h : family q x) : x<0 := by
  obtain ⟨j,rfl⟩ := h
  have P : (0:ℤ)<2^j*q := by positivity
  omega

private theorem energy_nonneg {x : ℤ} (hx : 0≤x) : energy x=450*x^2 := by
  classical
  have F3 : ¬family 3 x := fun H => by have := family_negative (by norm_num : (0:ℤ)<3) H;omega
  have F5 : ¬family 5 x := fun H => by have := family_negative (by norm_num : (0:ℤ)<5) H;omega
  simp [energy,F3,F5]

/-- A dyadically homogeneous correction at the two small negative rays
    makes every signed odd departure cost at least a factor two in energy. -/
theorem odd_energy {x y : ℤ} (edge : 3*x+1=2*y) (neq : x≠-1) :
    2*energy x≤energy y := by
  have squares := congrArg (fun z : ℤ => z^2) edge
  by_cases pos : 0≤x
  · have yp : 0≤y := by omega
    rw [energy_nonneg pos,energy_nonneg yp]
    nlinarith [sq_nonneg x]
  · by_cases three : x=-3
    · have yy : y=-4 := by omega
      have F : family 3 (-3) := ⟨0,by norm_num⟩
      rw [three,yy,energy_coprime (by norm_num : ¬(3:ℤ)∣-4) (by norm_num : ¬(5:ℤ)∣-4)]
      norm_num [energy,F]
    · by_cases five : x=-5
      · have yy : y=-7 := by omega
        have F : family 5 (-5) := ⟨0,by norm_num⟩
        have N : ¬family 3 (-5) := fun H => by
          have := family_dvd H
          norm_num at this
        rw [five,yy,energy_coprime (by norm_num : ¬(3:ℤ)∣-7) (by norm_num : ¬(5:ℤ)∣-7)]
        norm_num [energy,F,N]
      · have low : x≤-7 := by omega
        have nt : ¬3∣y := by rintro ⟨z,hz⟩;omega
        have lower := energy_not_three nt
        have upper := (energy_bounds x).2
        have P : 0≤(-x-7)*(-41*x-7) := mul_nonneg (by omega) (by omega)
        nlinarith only [lower,upper,P,squares]

theorem energy_growth {h p : ℕ} {x z : ℤ} (W : Walk h p x z) (neq : z≠-1) :
    (2:ℤ)^p*energy x≤4^(h-p)*energy z := by
  induction W with
  | nil => simp
  | @even h p x y W IH =>
    have hp := count_le W
    rw [energy_double,show h+1-p=(h-p)+1 by omega,pow_succ]
    nlinarith only [IH neq]
  | @odd h p x y z edge W IH =>
    have NX : x≠-1 := by
      intro X
      exact neq (minus_one_end W (by omega))
    have G := mul_le_mul_of_nonneg_left (odd_energy edge NX)
      (show (0:ℤ)≤2^p by positivity)
    rw [show h+1-(p+1)=h-p by omega,pow_succ]
    nlinarith only [G,IH neq]

/-- Uniform squared-magnitude bound, sharp in the odd/even exponent ratio
    on the signed cycle -5,-7,-10. -/
theorem squared_growth {h p : ℕ} {x z : ℤ} (W : Walk h p x z) (neq : z≠-1) :
    400*(2:ℤ)^p*x^2≤450*4^(h-p)*z^2 := by
  have A := energy_growth W neq
  have B := mul_le_mul_of_nonneg_left (energy_bounds x).1
    (show (0:ℤ)≤2^p by positivity)
  have C := mul_le_mul_of_nonneg_left (energy_bounds z).2
    (show (0:ℤ)≤4^(h-p) by positivity)
  nlinarith only [A,B,C]

/-- The even count of the prefix and the even count governing the terminal
    size are retained separately. The rational inequality 81 < 128 pays
    for the coefficient seven without a real logarithm. -/
theorem sharp_trap {h p r : ℕ} {x z : ℤ} (W : Walk h p x z)
    (high : 4*(h-p)+7*r+5≤2*p) (small : |z|≤2*(3:ℤ)^r) : z=-1 := by
  by_contra neq
  have xp : x≠0 := by
    intro eq
    have Q := (zero_origin W eq).1
    omega
  have xs : (1:ℤ)≤x^2 := by
    rcases lt_or_gt_of_ne xp with h|h <;> nlinarith
  have sqz : z^2≤4*(9:ℤ)^r := by
    have P := mul_self_le_mul_self (abs_nonneg z) small
    rw [←pow_two,←pow_two,sq_abs] at P
    have E : (2*(3:ℤ)^r)^2=4*9^r := by
      rw [mul_pow,←pow_mul,show r*2=2*r by omega,pow_mul]
      norm_num
    nlinarith only [P,E]
  have G := squared_growth W neq
  have X := mul_le_mul_of_nonneg_left xs (show (0:ℤ)≤400*2^p by positivity)
  have Z := mul_le_mul_of_nonneg_left sqz (show (0:ℤ)≤450*4^(h-p) by positivity)
  have R : (2:ℤ)^(p+1)≤9*4^(h-p)*9^r := by
    rw [pow_succ]
    nlinarith only [G,X,Z]
  have RR := mul_self_le_mul_self (show (0:ℤ)≤2^(p+1) by positivity) R
  have right : (9*(4:ℤ)^(h-p)*9^r)^2=81*16^(h-p)*81^r := by
    rw [mul_pow,mul_pow,←pow_mul (4:ℤ),show (h-p)*2=2*(h-p) by omega,pow_mul,
      ←pow_mul (9:ℤ),show r*2=2*r by omega,pow_mul]
    norm_num
  have left : ((2:ℤ)^(p+1))^2=2^(2*p+2) := by
    rw [←pow_mul]
    congr 1
    omega
  rw [←pow_two,←pow_two] at RR
  rw [left,right] at RR
  have powlow := pow_le_pow_right₀ (show (1:ℤ)≤2 by norm_num)
    (show 4*(h-p)+7*r+7≤2*p+2 by omega)
  have expand : (2:ℤ)^(4*(h-p)+7*r+7)=128*16^(h-p)*128^r := by
    rw [pow_add,pow_add,pow_mul,pow_mul]
    norm_num
    ring
  rw [expand] at powlow
  have base := pow_le_pow_left₀ (by norm_num : (0:ℤ)≤81)
    (by norm_num : (81:ℤ)≤128) r
  have compare := mul_le_mul_of_nonneg_left base
    (show (0:ℤ)≤81*16^(h-p) by positivity)
  have positive : (0:ℤ)<16^(h-p)*128^r := by positivity
  nlinarith only [RR,powlow,compare,positive]

#print axioms odd_energy
#print axioms energy_growth
#print axioms squared_growth
#print axioms sharp_trap

end RampShadow.Postpeak.MirrorEnergy
