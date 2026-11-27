import PositiveAnchorProjection

/-! The finite forward positive-anchor query and its sharp true-extra-budget application. -/
namespace PositiveApplications
open MultiBlockCompensation ReflectedCycleMinimum SevenPhaseMinimum PositiveBudget PositiveAnchorProjection

/-- A cutoff decision at one actual positive target is exactly a positive
forward-visitor query at the smaller congruent anchor, with a reduced source pool. -/
theorem bounded_anchor_query {X a R z N : ℕ} (ha : 0<a) (hx : X=a+2*3^R*z) :
    (∃ y≤N, Ancestor R X y) ↔
    ∃ w d, 0<w ∧ w%2=1 ∧ X*w≤a*N ∧ shortcut^[d] w=a ∧ ordinaryCount w d≤R ∧
        w+2^d*(2*3^(R-ordinaryCount w d)*z)≤N := by
  constructor
  · rintro ⟨y,cutoff,_,yo,d,arr,budget⟩
    obtain ⟨w,wp,wo,cnt,last,sum,small⟩ := positive_projection ha hx arr budget yo
    refine ⟨w,d,wp,wo,small.trans (Nat.mul_le_mul_left _ cutoff),last,cnt.le.trans budget,?_⟩
    rwa [cnt,←sum]
  · rintro ⟨w,d,wp,wo,_,last,budget,cutoff⟩
    let y:=w+2^d*(2*3^(R-ordinaryCount w d)*z)
    obtain ⟨odd,cnt,arr⟩ := positive_lift (z:=z) last wo budget
    change y%2=1 at odd
    change ordinaryCount y d=ordinaryCount w d at cnt
    change shortcut^[d] y=a+2*3^R*z at arr
    exact ⟨y,cutoff,by omega,odd,d,arr.trans hx.symm,cnt.le.trans budget⟩

/-- Arbitrarily many actual extra departures at the marked seven-phase target,
with the input divisibility expressed by an explicit positive quotient k. -/
theorem seven_phase_sharp {t a h R z s k : ℕ} (row : (t,a,h)∈phases)
    (hr : 7≤R) (hz : 0<z) (hk : 0<k)
    (divisibility : displacement (11*((R-a)/7)+h) (7*((R-a)/7)+a) R z-17=2*3^s*k-1) :
    IsLeast {u : ℕ | Ancestor (R+s) (2*3^R*z-t) u} (2^(s+1)*k-1) := by
  have table : ∀ v∈phases,v.1≤91 ∧ v.1%2=1 := by decide
  obtain ⟨cap,odd⟩ := table _ row
  change t≤91 at cap
  change t%2=1 at odd
  have large : 91≤2*3^R*z := calc
    91≤2*(3:ℕ)^7*1 := by decide
    _≤2*3^R*z := Nat.mul_le_mul (Nat.mul_le_mul_left _ (Nat.pow_le_pow_right (by decide) hr)) hz
  have eq : 2*3^R*z=2*(3^R*z) := by ring
  have base := exact_minimum row hr hz
  dsimp only at base
  rw [divisibility] at base
  exact sharp_extension hk (by omega) base

end PositiveApplications
#print axioms PositiveApplications.bounded_anchor_query
#print axioms PositiveApplications.seven_phase_sharp
