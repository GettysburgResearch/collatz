import AnchorCertificate
import PrepaidRamp

/-! A finite kernel calculation forces an arbitrary-length merger barrier.
No universal convergence hypothesis appears in the theorem. -/
set_option autoImplicit false
set_option warningAsError true
namespace CertifiedRamp
open RampShadow

theorem finite_budget : SmallPrefixBound 12 22 := by
  intro q hp hq d p z w
  have cap : q≤648 := by norm_num at hq; omega
  exact_mod_cast AnchorCertificate.all_prefixes_648 hp cap d p z w

theorem margin (K : ℕ) (hK : 84≤K) :
    (3:ℤ)^(K+1-12)*2^(22+1)*3^12 ≤ 4^(K+1-12)*2^12 := by
  obtain ⟨h,rfl⟩ := Nat.exists_eq_add_of_le hK
  have initial : (3:ℤ)^73*2^23*3^12 ≤ 4^73*2^12 := by norm_num
  have grow : (3:ℤ)^h≤4^h := pow_le_pow_left₀ (by norm_num) (by norm_num) h
  have product := mul_le_mul initial grow (by positivity) (by positivity)
  rw [show 84+h+1-12=73+h by omega,pow_add (3:ℤ) 73 h,pow_add (4:ℤ) 73 h]
  convert product using 1 <;> ring

/-- For every precision at least 84 and every ramp length, any smaller
positive input reaching the ramp endpoint costs more than K+j+12 odd steps.
Its total clock e has no bound. -/
theorem twelve_extra_odds {K j e k : ℕ} {s m n y : ℤ}
    (hK : 84≤K) (base : s=0 ∨ s=1) (hn : s<n) (hm : 0<m) (lt : m<n)
    (precision : (3:ℤ)^K ∣ n-s)
    (rise : (2:ℤ)^j*(y+1)=3^j*(n+1)) (W : Walk e k m y) :
    K+j+12<k := by
  exact prepaid_ramp base hn hm lt precision rise W (by omega)
    finite_budget (margin K hK)

#print axioms finite_budget
#print axioms twelve_extra_odds
end CertifiedRamp
