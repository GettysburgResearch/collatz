import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace Collatz.Diagonal.ThreeGradeCurvature

/-- Signed second difference of three consecutive rank labels. -/
def curv (x y z : ℤ) : ℤ := x - 2*y + z

/-- Equal slopes transport the signed curvature with the second difference of carries. -/
theorem commonSlope {d n x y z X Y Z a b c : ℤ}
    (hx : d*X=n*x+a) (hy : d*Y=n*y+b) (hz : d*Z=n*z+c) :
    d*curv X Y Z = n*curv x y z+curv a b c := by
  unfold curv
  linarith only [show d*X=n*x+a from hx, hy, hz,
    show d*(X-2*Y+Z)=d*X-2*(d*Y)+d*Z by ring,
    show n*(x-2*y+z)=n*x-2*(n*y)+n*z by ring]

/-- Lowbit transfer from three pruned-rank labels to the three low labels. -/
theorem phiPositive {x y z X Y Z a b c : ℤ}
    (hx : 2*X=3*x+a) (hy : 2*Y=3*y+b) (hz : 2*Z=3*z+c)
    (ha : 1≤a) (hb : b≤2) (hc : 1≤c) (hp : 0<curv x y z) :
    0<curv X Y Z := by
  have h := commonSlope hx hy hz
  unfold curv at h hp ⊢
  omega

/-- Lift the single-return column at a split to the upper high-rank octave. -/
theorem liftedSingle {x y z b c : ℤ}
    (hx : 4*y=3*x+b) (hy : 2*z=3*y+c) :
    8*z=9*x+(3*b+4*c) := by omega

/-- The two mixed columns have a common slope after their second return. -/
theorem twoMixed {x y z X Y Z b c B C : ℤ}
    (hx : 8*y=9*x+b) (hy : 4*z=3*y+c)
    (hX : 4*Y=3*X+B) (hY : 8*Z=9*Y+C) :
    32*z=27*x+(3*b+8*c) ∧ 32*Z=27*X+(9*B+4*C) := by omega

/-- Uniform scalar bounds for the single, double and paired transitions. -/
theorem scalarBound {H K e : ℤ} (h : 0≤H)
    (ht : (4*K=3*H+e ∧ -2≤e) ∨ (8*K=9*H+e ∧ -18≤e) ∨
          (32*K=27*H+e ∧ -102≤e)) :
    3*H-16≤4*K := by rcases ht with hr|hr|hr <;> omega

/-- A positive source which reaches a bad state of height at most four is at most ten. -/
theorem reverseCutoff {H K : ℤ} (h : 3*H-16≤4*K) (hK : K≤4) : H≤10 := by omega

/-- Lower bound through every stage of the longest six-transition block. -/
theorem largeBlock {a b c d e f g : ℤ} (ha : 128≤a)
    (hb : 3*a-16≤4*b) (hc : 3*b-16≤4*c) (hd : 3*c-16≤4*d)
    (he : 3*d-16≤4*e) (hf : 3*e-16≤4*f) (hg : 3*f-16≤4*g) :
    4<b ∧ 4<c ∧ 4<d ∧ 4<e ∧ 4<f ∧ 4<g := by omega

/-- Strict integer curvature implies an all-lag spacing bound. -/
theorem strictGap {g : ℕ → ℤ} (hg : ∀ r, 0 < g (r+1)-g r) (r t : ℕ) :
    (t : ℤ) ≤ g (r+t)-g r := by
  induction t with
  | zero => simp
  | succ t ih =>
    have hh := hg (r+t)
    change ((t+1 : ℕ) : ℤ) ≤ g ((r+t)+1)-g r
    rw [Nat.cast_add, Nat.cast_one]
    omega

/-- At a doubled octave the smallest physical gap is at least the period. -/
theorem octaveGap {g : ℕ → ℤ} (hg : ∀ r, 0 < g (r+1)-g r) (p : ℕ)
    (ho : g p=2*g 0) : (p : ℤ) ≤ g 0 := by
  have hh := strictGap hg 0 p
  simp only [Nat.zero_add, ho] at hh
  omega

end Collatz.Diagonal.ThreeGradeCurvature
