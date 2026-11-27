import Mathlib.Algebra.Field.Rat
import Mathlib.Data.Rat.Cast.Order
import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! Center variation for a closed physical trace cut into arbitrary arcs.
The coordinates are scaled by the common positive rational orbit denominator. -/
namespace Collatz.InfiniteDescent.ArcHeight

theorem dyadic_center_gap {l p : ℕ} {a b : ℤ}
    (step : 2^l*b = 3^p*a) (nonzero : a ≠ 0) : (2:ℤ)^l ≤ |a| := by
  have cop : IsCoprime (2:ℤ) 3 := ⟨-1,1,by decide⟩
  have hd : (2:ℤ)^l ∣ a :=
    (cop.pow (m:=l) (n:=p)).dvd_of_dvd_mul_left ⟨b,step.symm⟩
  obtain ⟨k,hk⟩ := hd
  have hn : k ≠ 0 := by rintro rfl; simp [hk] at nonzero
  have hab : 1 ≤ |k| := by have := abs_pos.mpr hn; omega
  rw [hk,abs_mul,abs_of_nonneg (by positivity : (0:ℤ) ≤ 2^l)]
  simpa using mul_le_mul_of_nonneg_left hab (by positivity : (0:ℤ) ≤ 2^l)

structure Arc where
  x : ℤ
  y : ℤ
  old : ℚ
  u : ℤ
  w : ℤ
  v : ℕ
  l : ℕ
  p : ℕ
  pos : 0 < v
  transport : (2:ℤ)^l * ((v:ℤ)*y-w) = 3^p*((v:ℤ)*x-u)
  separate : (v:ℤ)*x-u ≠ 0

def center (a : Arc) : ℚ := a.u / a.v
def finish (a : Arc) : ℚ := a.w / a.v
def err (a : Arc) : ℚ := (center a - a.old) / (a.x - center a)
def cost (a : Arc) : ℚ := a.v * |center a-a.old| / 2^a.l

theorem rational_gap (a : Arc) : (2:ℚ)^a.l ≤ a.v*|a.x-center a| := by
  have h := dyadic_center_gap a.transport a.separate
  have hq : (2:ℚ)^a.l ≤ |(a.v:ℚ)*a.x-a.u| := by exact_mod_cast h
  have hv : (0:ℚ)<a.v := by exact_mod_cast a.pos
  have he : (a.v:ℚ)*a.x-a.u = a.v*(a.x-center a) := by
    unfold center
    field_simp
  rwa [he,abs_mul,abs_of_pos hv] at hq

theorem nonzero_gap (a : Arc) : (a.x:ℚ)-center a ≠ 0 := by
  intro h
  have hh := rational_gap a
  rw [h,abs_zero,mul_zero] at hh
  exact (not_le_of_gt (by positivity)) hh

theorem error_bound (a : Arc) : |err a| ≤ cost a := by
  rw [err,cost,abs_div]
  have hx := abs_pos.mpr (nonzero_gap a)
  apply (div_le_div_iff₀ hx (by positivity)).mpr
  calc
    _ ≤ |center a-a.old| *(a.v*|a.x-center a|) :=
      mul_le_mul_of_nonneg_left (rational_gap a) (abs_nonneg _)
    _ = _ := by ring

theorem centered_step (a : Arc) :
    (2:ℚ)^a.l*((a.y:ℚ)-finish a)*(1+err a) =
      3^a.p*((a.x:ℚ)-a.old) := by
  have ht : (2:ℚ)^a.l*((a.v:ℚ)*a.y-a.w) = 3^a.p*((a.v:ℚ)*a.x-a.u) := by
    exact_mod_cast a.transport
  have hv : (a.v:ℚ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt a.pos)
  have base : (2:ℚ)^a.l*(a.y-finish a) = 3^a.p*(a.x-center a) := by
    unfold center finish
    field_simp [hv]
    nlinarith only [ht]
  rw [base,err]
  field_simp [nonzero_gap]
  ring

inductive Trace : ℚ → ℚ → List Arc → ℚ → ℚ → Prop where
  | nil (x old : ℚ) : Trace x old [] x old
  | step {a : Arc} {as : List Arc} {z t : ℚ}
      (rest : Trace a.y (finish a) as z t) : Trace a.x a.old (a::as) z t

theorem telescoping {x s z t : ℚ} {as : List Arc} (tr : Trace x s as z t) :
    (2:ℚ)^(as.map Arc.l).sum * (z-t) * (as.map (fun a => 1+err a)).prod =
      3^(as.map Arc.p).sum*(x-s) := by
  induction tr with
  | nil => simp
  | @step a as z t rest ih =>
    simp only [List.map_cons,List.sum_cons,List.prod_cons,pow_add]
    calc
      _ = (2^a.l * (1+err a)) *
        (2^(as.map Arc.l).sum*(z-t)*(as.map (fun b => 1+err b)).prod) := by ring
      _ = _ := by rw [ih]; linear_combination (3:ℚ)^(as.map Arc.p).sum * centered_step a

theorem accumulated {es : List ℚ} (hs : (es.map abs).sum < 1) :
    1-(es.map abs).sum ≤ (es.map (fun e => 1+e)).prod := by
  induction es with
  | nil => simp
  | cons e es ih =>
    simp only [List.map_cons,List.sum_cons,List.prod_cons] at hs ⊢
    have ht := ih (by linarith [abs_nonneg e])
    have hn : (0:ℚ) ≤ (es.map abs).sum :=
      List.sum_nonneg (fun a ha => by obtain ⟨b,_,rfl⟩ := List.mem_map.mp ha; exact abs_nonneg _)
    calc
      _ ≤ (1-|e|)*(1-(es.map abs).sum) := by nlinarith [mul_nonneg (abs_nonneg e) hn]
      _ ≤ (1+e)*(es.map (fun x => 1+x)).prod :=
        mul_le_mul (by linarith [neg_abs_le e]) ht
          (by linarith [abs_nonneg e]) (by linarith [neg_abs_le e])

theorem sum_error_le_cost (as : List Arc) :
    (as.map (fun a => |err a|)).sum ≤ (as.map cost).sum := by
  induction as with
  | nil => simp
  | cons a as ih => simp only [List.map_cons,List.sum_cons]; exact add_le_add (error_bound a) ih

/-- Every closed nonreturning arc partition has enough weighted adjacent-center variation. -/
theorem weighted_variation {x s : ℚ} {as : List Arc} (tr : Trace x s as x s)
    (endgap : x-s ≠ 0) :
    1 - (3:ℚ)^(as.map Arc.p).sum / 2^(as.map Arc.l).sum ≤ (as.map cost).sum := by
  let rho : ℚ := 3^(as.map Arc.p).sum / 2^(as.map Arc.l).sum
  have hp : (as.map (fun a => 1+err a)).prod = rho := by
    apply (eq_div_iff (by positivity)).mpr
    apply mul_right_cancel₀ endgap
    convert telescoping tr using 1
    ring
  have he := sum_error_le_cost as
  change 1-rho ≤ _
  by_cases hsum : (as.map (fun a => |err a|)).sum < 1
  · have ha := accumulated (es:=as.map err) (by simpa [List.map_map,Function.comp_def] using hsum)
    simp only [List.map_map,Function.comp_def] at ha
    linarith
  · have hpos : (0:ℚ) ≤ rho := by dsimp [rho]; positivity
    linarith

#print axioms dyadic_center_gap
#print axioms centered_step
#print axioms telescoping
#print axioms weighted_variation

end Collatz.InfiniteDescent.ArcHeight
