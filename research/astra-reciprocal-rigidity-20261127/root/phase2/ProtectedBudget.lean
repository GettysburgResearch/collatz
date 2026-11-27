import ProtectedCone
import ScaledPrepaid

/-! A finite prefix certificate survives every maximal postpeak word in
the upper-even-count cone, with no bound on either native clock. -/
set_option autoImplicit false
set_option warningAsError true

namespace RampShadow.Postpeak

theorem protected_prepaid_barrier {w : Word} {H K b L e k : ℕ} {v m Y s : ℤ}
    (U : PeakWord w H v Y) (maximal : Maximal w)
    (tall : 21*(w.length-weight w)+9*(K+b)+3≤H)
    (vp : 0<v) (seed : s=0 ∨ s=1)
    (prec : (3:ℤ)^K ∣ (2:ℤ)^H*v-1-s)
    (mp : 0<m) (lt : m<(2:ℤ)^H*v-1) (W : Walk e k m Y)
    (room : b≤K) (budget : SmallPrefixBound b L)
    (margin : (3:ℤ)^(K+1-b)*2^(L+1)*3^b ≤ 4^(K+1-b)*2^b) :
    H+weight w+K+b < k := by
  by_contra! low
  by_cases discount : k≤H+weight w
  · obtain ⟨d,D⟩ := Nat.exists_eq_add_of_le discount
    obtain ⟨β,bl,bc,gain⟩ := collision_necessary U (by omega) vp mp lt W D.symm
    have more := (gain_width gain).1
    have less := maximal β bl bc
    omega
  · let surplus := k-(H+weight w)
    have grade : k=H+weight w+surplus := by dsimp [surplus]; omega
    have cap : surplus≤K+b := by omega
    obtain ⟨β,a,bl,bc,V⟩ := paid_peak U (by omega) vp mp lt W grade
    let δ := weight w-weight β
    have free := maximal β bl bc
    have fd : H+weight w-weight β=H+δ := by dsimp [δ]; omega
    rw [fd] at V
    have spos : s<(2:ℤ)^H*v-1 := by rcases seed with S|S <;> omega
    have rise : (2:ℤ)^(H+δ)*(3^(H+δ)*v-1+1) =
        3^(H+δ)*2^δ*(2^H*v-1+1) := by
      rw [pow_add (2:ℤ)]; ring
    have pay := scaled_prepaid_ramp seed spos mp lt
      (one_le_pow₀ (by norm_num : (1:ℤ)≤2) (n:=δ)) prec rise V
      room budget margin
    omega

#print axioms protected_prepaid_barrier
end RampShadow.Postpeak

namespace CertifiedRamp
open RampShadow RampShadow.Postpeak

/-- A fully instantiated all-time postpeak barrier from the original finite
648-source certificate. Upper odd stretches may have arbitrary length. -/
theorem twelve_extra_postpeak_odds {w : Word} {H K e k : ℕ} {v m Y s : ℤ}
    (hK : 84≤K) (U : PeakWord w H v Y) (maximal : Maximal w)
    (tall : 21*(w.length-weight w)+9*(K+12)+3≤H)
    (vp : 0<v) (seed : s=0 ∨ s=1)
    (prec : (3:ℤ)^K ∣ (2:ℤ)^H*v-1-s)
    (mp : 0<m) (lt : m<(2:ℤ)^H*v-1) (W : Walk e k m Y) :
    H+weight w+K+12 < k := by
  exact protected_prepaid_barrier U maximal tall vp seed prec mp lt W
    (by omega) finite_budget (margin K hK)

#print axioms twelve_extra_postpeak_odds
end CertifiedRamp
