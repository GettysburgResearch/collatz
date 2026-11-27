import FirstPassage
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity

namespace Collatz.FirstPassage

private theorem shift_one (n k : ℕ) :
    step (n+2*k) = step n + 3^(n%2)*k := by
  have p : n%2=0 ∨ n%2=1 := by omega
  rcases p with p|p <;> simp [step,p] <;> omega

/-- A high binary translation of a control follows its entire physical word. -/
theorem run_binary_translate (c u h : ℕ) :
    run (c+2^h*u) h = run c h + 3^(odds c h)*u := by
  induction h generalizing c u with
  | zero => simp [run,odds]
  | succ h ih =>
    rw [show 2^(h+1)*u=2*(2^h*u) by ring,run,shift_one,run,odds,pow_add]
    rw [show 3^(c%2)*(2^h*u)=2^h*(3^(c%2)*u) by ring,ih]
    ring

private theorem physical_lower (c h : ℕ) :
    3^(odds c h)*c ≤ 2^h*run c h := by
  induction h generalizing c with
  | zero => simp [run,odds]
  | succ h ih =>
    have one : 3^(c%2)*c ≤ 2*step c := by
      have p : c%2=0 ∨ c%2=1 := by omega
      rcases p with p|p <;> simp [step,p] <;> omega
    calc
      3^(odds c (h+1))*c = 3^(odds (step c) h)*(3^(c%2)*c) := by rw [odds,pow_add]; ring
      _ ≤ 3^(odds (step c) h)*(2*step c) := Nat.mul_le_mul_left _ one
      _ = 2*(3^(odds (step c) h)*step c) := by ring
      _ ≤ 2*(2^h*run (step c) h) := Nat.mul_le_mul_left _ (ih (step c))
      _ = 2^(h+1)*run c (h+1) := by rw [run]; ring

/-- A control reaching a fixed physical upper target has a bounded initial
height if its binary lift stays above a prescribed lower floor. -/
theorem aligned_floor {c u h s v : ℕ}
    (target : run c h=v) (floorAt : s ≤ run (c+2^h*u) h) :
    c*s ≤ (c+2^h*u)*v := by
  have bound := Nat.mul_le_mul_right u (physical_lower c h)
  rw [run_binary_translate,target] at floorAt
  rw [target] at bound
  calc
    c*s ≤ c*(v+3^(odds c h)*u) := Nat.mul_le_mul_left _ floorAt
    _ ≤ (c+2^h*u)*v := by nlinarith

/-- Any positive first-hit path from outside 1,2 has two consecutive
even departures before its visit to one. The claim also allows later hits. -/
theorem four_before_one {c h : ℕ} (hc : 2<c) (hit : run c h=1) :
    ∃ i, i+2≤h ∧ 4 ∣ run c i := by
  induction h generalizing c with
  | zero => simp [run] at hit; omega
  | succ h ih =>
    by_cases high : 2<step c
    · obtain ⟨i,hi,hd⟩ := ih high hit
      exact ⟨i+1,by omega,hd⟩
    · have cc : c=4 := by
        unfold step at high
        split at high <;> omega
      subst c
      cases h with
      | zero => contradiction
      | succ h => exact ⟨0,by omega,by decide⟩

/-- On a lower orbit with no multiple of four, every completely aligned
ordinary certificate for one has initial control 1 or 2 (or zero a priori). -/
theorem restricted_alignment {x c u h : ℕ}
    (lift : x=c+2^h*u) (hit : run c h=1)
    (restricted : ∀ i, ¬ 4 ∣ run x i) : c≤2 := by
  by_contra! bad
  obtain ⟨i,hi,hd⟩ := four_before_one bad hit
  obtain ⟨j,hj⟩ := Nat.exists_eq_add_of_le hi
  have coeff : 2^h*u=2^i*(4*(2^j*u)) := by rw [hj]; ring
  apply restricted i
  rw [lift,coeff,run_binary_translate]
  exact Nat.dvd_add hd ⟨3^(odds c i)*(2^j*u),by ring⟩

#print axioms run_binary_translate
#print axioms aligned_floor
#print axioms four_before_one
#print axioms restricted_alignment

end Collatz.FirstPassage

namespace Collatz.FirstPassage

/-- A shared finite parity word on the positive input x and the negative
input -m. Record terminal magnitudes u,v and physical odd count p. -/
inductive OppositeMatch (cap : ℕ) : ℕ → ℕ → ℕ → ℕ → ℕ → Prop where
  | stop {x m : ℕ} (pos : 0<x) : OppositeMatch cap x m x m 0
  | half {x m u v p : ℕ} (tail : OppositeMatch cap x m u v p) :
      OppositeMatch cap (2*x) (2*m) u v p
  | odd {x m a b u v p : ℕ} (pos : 0<x) (bounded : x≤cap)
      (plus : 2*a=3*x+1) (minus : 2*b+1=3*m) (tail : OppositeMatch cap a b u v p) :
      OppositeMatch cap x m u v (p+1)

/-- Negative magnitudes spend a definite fraction of their ratio at each
common odd departure, even if the reflected negative orbit is unknown. -/
theorem opposite_budget {cap x m u v p : ℕ} (path : OppositeMatch cap x m u v p) :
    0<x ∧ (v:ℚ)/u + (p:ℚ)/(3*(cap:ℚ)+1) ≤ (m:ℚ)/x := by
  induction path with
  | stop pos => exact ⟨pos,by simp⟩
  | @half x m u v p _ ih =>
    refine ⟨by omega,?_⟩
    have hx : 0<(x:ℚ) := by exact_mod_cast ih.1
    push_cast
    have eq : (2*(m:ℚ))/(2*x)=(m:ℚ)/x := by field_simp
    rw [eq]
    exact ih.2
  | @odd x m a b u v p pos bounded plus minus _ ih =>
    refine ⟨pos,?_⟩
    have hx : 0<(x:ℚ) := by exact_mod_cast pos
    have hc : (x:ℚ)≤cap := by exact_mod_cast bounded
    have hcap : 0<3*(cap:ℚ)+1 := by positivity
    have hx' : 0<3*(x:ℚ)+1 := by positivity
    have hn : 0≤(m:ℚ) := by positivity
    have pa : 2*(a:ℚ)=3*x+1 := by exact_mod_cast plus
    have pb : 2*(b:ℚ)+1=3*m := by exact_mod_cast minus
    have identity : (m:ℚ)/x - (b:ℚ)/a = (m+x)/(x*(3*x+1)) := by
      rw [show (a:ℚ)=(3*x+1)/2 by linarith,show (b:ℚ)=(3*m-1)/2 by linarith]
      field_simp
      ring
    have small : 1/(3*(cap:ℚ)+1) ≤ 1/(3*(x:ℚ)+1) := by
      apply (div_le_div_iff₀ hcap hx').mpr
      linarith
    have large : 1/(3*(x:ℚ)+1) ≤ (m+x)/(x*(3*x+1)) := by
      apply (div_le_div_iff₀ hx' (mul_pos hx hx')).mpr
      nlinarith [mul_nonneg hn hx'.le]
    push_cast
    rw [add_div]
    linarith [ih.2]

#print axioms opposite_budget

end Collatz.FirstPassage

namespace Collatz.FirstPassage

/-- At a source congruent to one modulo four below five times its protected
floor, the only positive control that can lift its entire physical hit is one. -/
theorem canonical_aligned_one {x c u h s : ℕ} (lift : x=c+2^h*u)
    (row : x%4=1) (size : x<5*s) (hit : run c h=1) (floorAt : s≤run x h) :
    c=1 := by
  rw [lift] at floorAt
  have bound := aligned_floor hit floorAt
  rw [← lift,mul_one] at bound
  have cc : c<5 := by
    by_contra! big
    have contra := Nat.mul_le_mul_right s big
    omega
  cases h with
  | zero => exact hit
  | succ h =>
    cases h with
    | zero =>
      change step c=1 at hit
      unfold step at hit
      norm_num at lift
      split at hit <;> omega
    | succ h =>
      rw [show 2^(h+1+1)*u=4*(2^h*u) by ring] at lift
      omega

#print axioms canonical_aligned_one

end Collatz.FirstPassage
