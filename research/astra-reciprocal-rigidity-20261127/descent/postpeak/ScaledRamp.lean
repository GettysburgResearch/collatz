import PostWords

namespace RampShadow.Postpeak

/-- Lower signed carry bound, valid for every parity word. -/
theorem intercept_floor (w : Word) : (3:ℤ)^weight w≤2^w.length+intercept w := by
  induction w with
  | nil => norm_num [weight,intercept]
  | cons b w ih =>
    have H : (0:ℤ)≤3^weight w := by positivity
    cases b <;> simp only [weight,List.length_cons,intercept,pow_succ] <;> linarith

/-- A multiplicative increase of the virtual ramp source's shifted height
    preserves ternary protection of the original source. -/
theorem scaled_ramp {K j e k : ℕ} {s m n c Y : ℤ}
    (seed : s=0 ∨ s=1) (hn : s<n) (mp : 0<m) (lt : m<n) (cp : 1≤c)
    (prec : (3:ℤ)^K∣n-s) (ramp : 2^j*(Y+1)=3^j*c*(n+1))
    (W : Walk e k m Y) : K+j<k := by
  by_contra! cap
  let N := c*(n+1)-1
  have spos : 0≤s := by rcases seed with G|G <;> omega
  have npos : 0≤n+1 := by omega
  have nN : n≤N := by
    have P := mul_le_mul_of_nonneg_right cp npos
    dsimp [N];linarith only [P]
  have vramp : 2^j*(Y+1)=3^j*(N+1) := by dsimp [N];linear_combination ramp
  obtain ⟨d,ed⟩ := Nat.exists_eq_add_of_le (clocks_order W (by omega) (show m<N by omega) vramp)
  have eqe : e=d+j := by omega
  have W' : Walk (d+j) k m Y := eqe ▸ W
  obtain ⟨v,V⟩ := prec
  obtain ⟨f,F⟩ := Nat.exists_eq_add_of_le cap
  let a := (3:ℤ)^f*c*v
  have A : 3^k*a=3^j*c*(n-s) := by
    dsimp [a];rw [V]
    have eq : (3:ℤ)^k*3^f=3^j*3^K := by
      rw [←pow_add,←pow_add,show k+f=j+K by omega]
    linear_combination c*v*eq
  obtain ⟨p,u,z,L,R,ku⟩ := split W'
  let m₀ := m-2^d*a
  let z₀ := z-3^p*a
  have S : Walk d p m₀ z₀ := by
    simpa only [m₀,z₀,sub_eq_add_neg,mul_neg] using lift L (-a)
  have PA : (3:ℤ)^u*3^p*a=3^j*c*(n-s) := by
    rw [←pow_add,show u+p=k by omega];exact A
  obtain ⟨B,B0,Bmax,Beq⟩ := affine R
  have Eq : 3^u*z₀+B=3^j*c*(s+1)-2^j := by
    dsimp [z₀];linear_combination Beq.symm + ramp - PA
  have lower : (3:ℤ)^j*(s+1)≤3^j*c*(s+1) := by
    have X := mul_le_mul_of_nonneg_right cp (show 0≤s+1 by omega)
    have Y := mul_le_mul_of_nonneg_left X (show (0:ℤ)≤3^j by positivity)
    linarith only [Y]
  have Z : 0≤z₀ := by
    by_contra! G
    have q := mul_neg_of_pos_of_neg (show (0:ℤ)<3^u by positivity) G
    have r := mul_nonneg (show (0:ℤ)≤3^j by positivity) spos
    nlinarith only [q,r,Eq,lower,Bmax]
  have mpos := nonneg_of_terminal S Z
  have sm : s≤m₀ := by
    rcases seed with ss|ss
    · omega
    · by_contra! neg
      have Z0 := (zero_origin S (by omega)).2
      rw [Z0,ss] at Eq
      rw [ss] at lower
      have pow : (0:ℤ)<3^j := by positivity
      nlinarith only [Eq,lower,Bmax,pow]
  obtain ⟨b,bl,bw,whole⟩ := word_of_walk W'
  have carry := intercept_floor b
  rw [bl,bw,pow_add] at carry
  rw [pow_add] at whole
  have slopeEq : 3^k*m₀+intercept b+2^d*2^j=2^d*3^j*c*(s+1) := by
    dsimp [m₀]
    linear_combination -whole + (2:ℤ)^d*ramp - (2:ℤ)^d*A
  have sm' := mul_le_mul_of_nonneg_left (show s+1≤m₀+1 by omega)
    (show (0:ℤ)≤3^k by positivity)
  have slope : (3:ℤ)^k≤2^d*3^j*c := by
    apply le_of_mul_le_mul_right (a:=s+1)
    · nlinarith only [carry,slopeEq,sm']
    · omega
  have prod := mul_le_mul_of_nonneg_right slope (show 0≤n-s by omega)
  have sub : n-s≤2^d*a := by
    apply le_of_mul_le_mul_left (a:=(3:ℤ)^k)
    · nlinarith only [prod,congrArg (fun q : ℤ => (2:ℤ)^d*q) A]
    · positivity
  dsimp [m₀] at sm
  omega

end RampShadow.Postpeak

#print axioms RampShadow.Postpeak.scaled_ramp
