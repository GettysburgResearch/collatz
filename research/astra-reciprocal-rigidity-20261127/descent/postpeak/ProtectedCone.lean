import CollisionCone
import ScaledRamp

namespace RampShadow.Postpeak

/-- A word attains the largest number of odd departures among equal-clock
    words with the same signed offset. -/
def Maximal (w : Word) : Prop :=
  ∀ b : Word, b.length=w.length → offset b=offset w → weight b≤weight w

/-- For positive overspend the residual source reaches an actual pure peak
    before its same-offset tail starts. The long part of the translated
    prefix ends at the signed fixed point. -/
theorem paid_peak {w H v m Y e k b} (U : PeakWord w H v Y)
    (tall : 21*(w.length-weight w)+9*b+3≤H) (vp : 0<v) (mp : 0<m)
    (lt : m<(2:ℤ)^H*v-1) (W : Walk e k m Y) (grade : k=H+weight w+b) :
    ∃ β : Word, ∃ a : ℕ, β.length=w.length ∧ offset β=offset w ∧
      Walk a (k-weight β) m (3^(H+weight w-weight β)*v-1) := by
  let t := w.length
  let f := weight w
  let q := t-f
  have ft : f≤t := weight_le w
  have bud := overflow_even_count vp mp lt (peak_word_walk U) W grade
  change e-k≤2*q+b at bud
  change 21*q+9*b+3≤H at tall
  change k=H+f+b at grade
  obtain ⟨a0,a1,m1,e01,F,G⟩ := split_odds W b (H+f) (by omega)
  have a0k := count_le F
  have a1k := count_le G
  have qe : t=q+f := by dsimp [q];omega
  let h := a1-t
  have splitTime : a1=h+t := by dsimp [h];omega
  have G' : Walk (h+t) (H+f) m1 Y := splitTime ▸ G
  obtain ⟨p,u,z,L,R,price⟩ := split G'
  have uh := count_le R
  have ph := count_le L
  let x₀ := m1-2^h*v
  let z₀ := z-3^p*v
  have S : Walk h p x₀ z₀ := by
    simpa only [x₀,z₀,sub_eq_add_neg,mul_neg] using lift L (-v)
  have upperEq : (2:ℤ)^t*Y=3^(H+f)*v+offset w := U
  rw [price,pow_add] at upperEq
  obtain ⟨β,bl,bw,beq⟩ := word_of_walk R
  have trans : 3^u*z₀+intercept β=offset w := by
    dsimp [z₀]
    nlinarith only [upperEq,beq]
  have OB := offset_bounds w
  have BB := intercept_bounds β
  rw [bl] at BB
  have two : (0:ℤ)≤2^t := by positivity
  have tiny := small_state_refined uh OB.1 OB.2 BB.1 (by linarith [BB.2]) trans
  have tailEven : t-u≤2*q+b := by omega
  have Z := pow_le_pow_right₀ (show (1:ℤ)≤3 by norm_num) tailEven
  have small : |z₀|≤2*(3:ℤ)^(2*q+b) := by linarith only [tiny,Z]
  have high : 9*(2*q+b)+3≤p := by omega
  have low : h-p≤2*(2*q+b) := by omega
  have hit := signed_trap S high low small
  have zz : z=3^p*v-1 := by dsimp [z₀] at hit;omega
  refine ⟨β,a0+h,bl,?_,?_⟩
  · change intercept β-3^weight β=offset w
    rw [bw]
    rw [hit] at trans
    linarith only [trans]
  · rw [bw,show k-u=b+p by omega]
    change Walk (a0+h) (b+p) m (3^(H+f-u)*v-1)
    rw [show H+f-u=p by omega,←zz]
    exact append F L

/-- Ternary protection on the original ordinary source survives every
    maximal postpeak word in the upper-even-count cone. -/
theorem protected_barrier {w H K v m Y e k s} (U : PeakWord w H v Y)
    (maximal : Maximal w) (tall : 21*(w.length-weight w)+9*K+3≤H)
    (vp : 0<v) (seed : s=0 ∨ s=1) (prec : (3:ℤ)^K ∣ (2:ℤ)^H*v-1-s)
    (mp : 0<m) (lt : m<(2:ℤ)^H*v-1) (W : Walk e k m Y) :
    H+weight w+K < k := by
  by_contra! low
  by_cases discount : k≤H+weight w
  · obtain ⟨d,D⟩ := Nat.exists_eq_add_of_le discount
    obtain ⟨β,bl,bc,gain⟩ := collision_necessary U (by omega) vp mp lt W D.symm
    have more := (gain_width gain).1
    have less := maximal β bl bc
    omega
  · let b := k-(H+weight w)
    have grade : k=H+weight w+b := by dsimp [b];omega
    have cap : b≤K := by omega
    obtain ⟨β,a,bl,bc,V⟩ := paid_peak U (by omega) vp mp lt W grade
    let δ := weight w-weight β
    have free := maximal β bl bc
    have fd : H+weight w-weight β=H+δ := by dsimp [δ];omega
    rw [fd] at V
    have spos : s<(2:ℤ)^H*v-1 := by rcases seed with S|S <;> omega
    have rise : (2:ℤ)^(H+δ)*(3^(H+δ)*v-1+1) =
        3^(H+δ)*2^δ*(2^H*v-1+1) := by rw [pow_add (2:ℤ)];ring
    have pay := scaled_ramp seed spos mp lt
      (one_le_pow₀ (by norm_num : (1:ℤ)≤2) (n:=δ)) prec rise V
    omega

end RampShadow.Postpeak

#print axioms RampShadow.Postpeak.paid_peak
#print axioms RampShadow.Postpeak.protected_barrier
