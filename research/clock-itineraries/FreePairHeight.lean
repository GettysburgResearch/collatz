module

public import FreePairClock
import all PairInverseRays
import all FreePairClock

public section
namespace Collatz.Itinerary.FreePairHeight

open FreePairClock PairInverseRays
set_option autoImplicit false
set_option maxRecDepth 12288
set_option maxHeartbeats 4000000

/-- With a shared t≥0, these two rays either never form a tripling pair,
or the first one stays at or above the proposed lower affine bound. -/
private def separated (a c floor : Ray) : Bool :=
  decide ((3*a.1<c.1 ∧ 3*a.2≤c.2) ∨
    (c.1<3*a.1 ∧ c.2≤3*a.2) ∨ (floor.1≤a.1 ∧ floor.2≤a.2))

private theorem use_separated {a c floor : Ray} {t : Nat}
    (yes : separated a c floor=true) (eq : 3*value a t=value c t) :
    value floor t≤value a t := by
  obtain cases := of_decide_eq_true yes
  unfold value at *
  rw [Nat.mul_add,←Nat.mul_assoc] at eq
  rcases cases with ⟨base,slope⟩ | ⟨base,slope⟩ | ⟨base,slope⟩
  · have le := Nat.mul_le_mul_right t slope
    omega
  · have le := Nat.mul_le_mul_right t slope
    omega
  · exact Nat.add_le_add base (Nat.mul_le_mul_right t slope)

private def dominates (h b : Nat) (floor : Ray) : Bool :=
  let xs := rays h b (3^14)
  xs.all (fun a => xs.all (fun c => separated a c floor))

private theorem lower {h b t x : Nat} {floor : Ray}
    (short : h≤14) (checked : dominates h b floor=true)
    (hit : PairAt h x (b+3^14*t)) : value floor t≤x := by
  have div : 3^h∣3^14 := ⟨3^(14-h),by rw [←Nat.pow_add,show h+(14-h)=14 by omega]⟩
  obtain ⟨a,ma,ha⟩ := ray_complete h b (3^14) t x div hit.1
  obtain ⟨c,mc,hc⟩ := ray_complete h b (3^14) t (3*x) div hit.2
  have ok := List.all_eq_true.mp (List.all_eq_true.mp checked a ma) c mc
  rw [ha] at hc ⊢
  exact use_separated ok hc

private theorem attained {b : Nat} {a : Ray} (t : Nat)
    (ma : a∈rays 14 b (3^14)) (mc : triple a∈rays 14 b (3^14)) :
    PairAt 14 (value a t) (b+3^14*t) := by
  exact ⟨ray_sound ma t,by rw [←value_triple]; exact ray_sound mc t⟩

private def fixed : Ray := (337344,2902376448)
private def flexible : Ray := (221079,967458816)

private theorem check_fixed : dominates 14 556 fixed=true := by decide +kernel
private theorem check_flexible : ∀ i : Fin 15, dominates i.val 1093 flexible=true := by decide +kernel

/-- Exact minimum of the first arm on an infinite class at the fixed clock.
The ratio tends to 16384/27, the universal fixed-clock upper constant. -/
theorem fixed_minimum (t : Nat) :
    PairAt 14 (337344+2902376448*t) (556+3^14*t) ∧
    ∀ x, PairAt 14 x (556+3^14*t) → 337344+2902376448*t≤x := by
  refine ⟨attained (a:=fixed) t (by decide +kernel) (by decide +kernel),?_⟩
  exact fun _ hit => lower (by decide) check_fixed hit

/-- Exact minimum even when all clocks through 14 compete. The ratio tends
to 16384/81, the universal flexible-clock upper constant. -/
theorem flexible_minimum (t : Nat) :
    PairAt 14 (221079+967458816*t) (1093+3^14*t) ∧
    ∀ h≤14, ∀ x, PairAt h x (1093+3^14*t) → 221079+967458816*t≤x := by
  refine ⟨attained (a:=flexible) t (by decide +kernel) (by decide +kernel),?_⟩
  intro h sh _ hit
  exact lower sh (check_flexible ⟨h,by omega⟩) hit

#print axioms fixed_minimum
#print axioms flexible_minimum
end Collatz.Itinerary.FreePairHeight
