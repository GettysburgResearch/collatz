import Mathlib.Data.Int.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! Ternary comparisons for two simultaneous, ordinary shortcut trajectories. -/
namespace Collatz.InfiniteDescent.NativeInversion

def slope : Bool → ℤ | false => 1 | true => 3
def addend : Bool → ℤ | false => 0 | true => 1
def native (b : Bool) (x z : ℤ) := 2*z = slope b*x+addend b

def reverses (d e : ℤ) := (d<0 ∧ 0<e) ∨ (0<d ∧ e<0)

theorem aligned {a b : Bool} {x y z w : ℤ} (p : ℤ)
    (ax : native a x z) (ay : native b y w) :
    2*(slope a*w-slope b*p*z) =
      slope a*slope b*(y-p*x)+slope a*addend b-slope b*p*addend a := by
  unfold native at ax ay
  linear_combination slope a*ay-slope b*p*ax

private theorem reversal_algebra {a b : Bool} {p d e : ℤ} (hp : 0<p)
    (ha : 2*e=slope a*slope b*d + slope a*addend b-slope b*p*addend a)
    (change : reverses d e) : a=true ∧ 0<d ∧ 3*d<p := by
  unfold reverses at change
  cases a <;> cases b <;> simp [slope,addend] at ha ⊢ <;> omega

/-- The smaller lane is odd. Its larger partner lies just above a ternary multiple. -/
theorem crossing_source {a b : Bool} {x y z w : ℤ} (k : ℕ)
    (ax : native a x z) (ay : native b y w)
    (change : reverses (y-3^k*x) (slope a*w-slope b*3^k*z)) :
    a=true ∧ 2≤k ∧ 0<y-3^k*x ∧ 3*(y-3^k*x)<3^k := by
  have h := reversal_algebra (by positivity : (0:ℤ)<3^k) (aligned _ ax ay) change
  refine ⟨h.1, ?_, h.2⟩
  by_contra! hn
  have hk : k=0 ∨ k=1 := by omega
  rcases hk with rfl|rfl <;> norm_num at h <;> omega

/-- The even larger partner has an odd predecessor more than nine times
the odd smaller partner, also when the ternary power is exactly nine. -/
theorem even_partner_predecessor {x y z : ℤ} {k a : ℕ}
    (hx : 0<x) (xo : x%2=1) (ye : y%2=0) (hk : 2≤k)
    (hp : 0<y-3^k*x) (hs : 3*(y-3^k*x)<3^k)
    (apos : 0<a) (prev : 2^a*y=3*z+1) : 9*x<z := by
  have ha : (2:ℤ)≤2^a := by
    simpa using (pow_le_pow_right₀ (by decide : (1:ℤ)≤2) (show 1≤a by omega))
  by_cases h : k=2
  · subst k
    norm_num at hp hs
    have hy : y=9*x+1 := by omega
    have hune : a≠1 := by rintro rfl; simp [hy] at prev; omega
    have four : (4:ℤ)≤2^a := by
      exact_mod_cast (show (2:ℤ)^2≤2^a from pow_le_pow_right₀ (by decide) (by omega))
    have hy0 : 0≤y := by omega
    have := mul_le_mul_of_nonneg_right four hy0
    omega
  · have pow3 : (27:ℤ)≤3^k :=
      pow_le_pow_right₀ (by decide : (1:ℤ)≤3) (show 3≤k by omega)
    have low := mul_le_mul_of_nonneg_right pow3 hx.le
    have hy0 : 0≤y := by omega
    have := mul_le_mul_of_nonneg_right ha hy0
    omega

theorem odd_partner_bound {x y : ℤ} {k : ℕ} (hx : 0<x) (hk : 2≤k)
    (hp : 0<y-3^k*x) : 9*x<y := by
  have hpow : (9:ℤ)≤3^k := pow_le_pow_right₀ (by decide : (1:ℤ)≤3) hk
  have := mul_le_mul_of_nonneg_right hpow hx.le
  omega

/-- Once a list of nonzero integer comparisons changes sign, a neighboring
pair of its actual time slices reverses. -/
theorem first_reversal (d : ℕ → ℤ) (n : ℕ) (start : 0<d 0)
    (finish : d n<0) (sep : ∀ k, d k ≠ 0) : ∃ k<n, 0<d k ∧ d (k+1)<0 := by
  induction n with
  | zero => omega
  | succ n ih =>
    by_cases hn : d n<0
    · obtain ⟨k,hk,hd⟩ := ih hn
      exact ⟨k,by omega,hd⟩
    · exact ⟨n,by omega,by have := sep n; omega,finish⟩

/-- Native parity along a complete integer shortcut word. -/
inductive Path : List Bool → ℤ → ℤ → Prop
  | nil (x : ℤ) : Path [] x x
  | cons {a : Bool} {bits : List Bool} {x z y : ℤ} :
      native a x z → Path bits z y → Path (a::bits) x y

def scale : List Bool → ℤ
  | [] => 1
  | a :: bits => slope a * scale bits

theorem cylinder_bound {bits : List Bool} {x y : ℤ} (path : Path bits x y)
    (m : ℤ) (upper : x < 2^bits.length*m) : y < scale bits*m := by
  induction path generalizing m with
  | nil => simpa [scale] using upper
  | @cons a bits x z y step tail ih =>
    have nextBound : z < 2^bits.length*(slope a*m) := by
      cases a <;> simp [native,slope,addend] at step ⊢ <;>
        simp [pow_succ] at upper <;> nlinarith
    simpa [scale,mul_assoc,mul_left_comm,mul_comm] using ih (slope a*m) nextBound

theorem positive_source {bits : List Bool} {x y : ℤ} (path : Path bits x y)
    (positive : 0<y) : 0<x := by
  induction path with
  | nil => exact positive
  | @cons a bits x z y step tail ih =>
    have hz : 0<z := ih positive
    cases a <;> simp [native,slope,addend] at step <;> omega

/-- Two integer starts displaced by a full dyadic cylinder differ at the
endpoint by the exact ternary multiplier on the same prescribed word. -/
theorem cylinder_translate {bits : List Bool} {x y : ℤ} (path : Path bits x y)
    (m : ℤ) : Path bits (2^bits.length*m+x) (scale bits*m+y) := by
  induction path generalizing m with
  | nil z => simpa [scale] using Path.nil (m+z)
  | @cons a bits x z y step tail ih =>
    have first : native a (2^(a::bits).length*m+x)
        (2^bits.length*(slope a*m)+z) := by
      unfold native at step ⊢
      simp only [List.length_cons,pow_succ]
      linear_combination step
    have rest := ih (slope a*m)
    rw [show scale (a::bits)*m=scale bits*(slope a*m) by simp [scale]; ring]
    exact Path.cons first rest

#print axioms cylinder_bound
#print axioms positive_source
#print axioms cylinder_translate

#print axioms aligned
#print axioms crossing_source
#print axioms even_partner_predecessor
#print axioms first_reversal

end Collatz.InfiniteDescent.NativeInversion
