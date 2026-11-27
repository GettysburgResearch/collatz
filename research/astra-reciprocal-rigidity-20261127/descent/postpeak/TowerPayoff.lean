import PostWords

namespace RampShadow.Postpeak

/-- A compensated merger of two ordinary peaks gives an explicitly smaller
    start, with the chosen number of saved odd departures. No postpeak
    clock limit or protected-source assumption is required. -/
theorem tower_payoff {H a d p g f : ℕ} {v Y : ℤ}
    (height : p+a+d=H) (free : 1≤p) (vp : 0<v)
    (gain : (3:ℤ)^d<2^(a+d))
    (upper : Walk g f (3^H*v-1) Y)
    (earlier : Walk g (f+a) (3^(H-a)*v-1) Y) :
    let n := (2:ℤ)^H*v-1
    let m := (2:ℤ)^p*3^d*v-1
    0<m ∧ m<n ∧ Walk (p+g) (H+f-d) m Y ∧ Walk (H+g) (H+f) n Y := by
  dsimp
  have A : (1:ℤ)≤3^d*v := by
    have P := mul_le_mul (one_le_pow₀ (show (1:ℤ)≤3 by norm_num) (n:=d))
      (show 1≤v by omega) (by norm_num) (by positivity)
    simpa using P
  have PP : (2:ℤ)^1≤2^p := pow_le_pow_right₀ (by norm_num) free
  have MM := mul_le_mul PP A (by norm_num) (by positivity)
  have pace := mul_lt_mul_of_pos_left gain (show (0:ℤ)<2^p*v by positivity)
  have powH : (2:ℤ)^H=2^p*2^(a+d) := by rw [←pow_add,show p+(a+d)=H by omega]
  have ea : Walk g (f+a) (3^p*(3^d*v)-1) Y := by
    have eq : (3:ℤ)^(H-a)=3^p*3^d := by rw [←pow_add,show H-a=p+d by omega]
    simpa only [eq,mul_assoc] using earlier
  have joined := append (ramp_walk p (3^d*v)) ea
  have top := append (ramp_walk H v) upper
  refine ⟨?_,?_,?_,top⟩
  · norm_num at MM;nlinarith only [MM]
  · rw [powH];nlinarith only [pace]
  · rw [show H+f-d=p+(f+a) by omega]
    simpa only [mul_assoc] using joined

end RampShadow.Postpeak

#print axioms RampShadow.Postpeak.tower_payoff
