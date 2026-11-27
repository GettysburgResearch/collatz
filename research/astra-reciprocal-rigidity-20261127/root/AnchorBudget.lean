import RampShadow
import Mathlib.Data.Finset.Range

/-! Exact finite-anchor consumers for arbitrary-length ordinary paths.
No unverified global Collatz or stopping-time assertion is an input. -/
set_option autoImplicit false
set_option warningAsError true

namespace AnchorBudget
open RampShadow

/-- On the trivial component cycle the signed count defect is a coboundary. -/
theorem cycle_defect {e k : ℕ} {x y : ℤ} (w : Walk e k x y)
    (hx : x=1 ∨ x=2) :
    (2:ℤ)*k-e = (if x=1 then 0 else -1) - (if y=1 then 0 else -1) := by
  induction w with
  | nil x => simp
  | @even e k x y w ih =>
    have x1 : x=1 := by omega
    subst x
    have h := ih (Or.inl rfl)
    simp only [show (2:ℤ)*1≠1 by norm_num, ite_false,
      Nat.cast_add, Nat.cast_one]
    simp only [ite_true] at h
    linarith
  | @odd e k x y z xy w ih =>
    have x1 : x=1 := by omega
    have y2 : y=2 := by omega
    subst x; subst y
    have h := ih (Or.inr rfl)
    simp only [show (2:ℤ)≠1 by norm_num, ite_false] at h
    simp only [ite_true, Nat.cast_add, Nat.cast_one]
    linarith

theorem cycle_balance {e k : ℕ} (w : Walk e k 1 1) : 2*k=e := by
  have h := cycle_defect w (Or.inl rfl)
  norm_num at h
  omega

/-- Any two actual visits to 1 have the same odd/native clock defect.
The supplied finite witness need not be the first visit. -/
theorem visit_defect {e k t p : ℕ} {x : ℤ}
    (w : Walk e k x 1) (v : Walk t p x 1) : 2*k+t=2*p+e := by
  suffices ordered : ∀ (e k t p : ℕ) (x : ℤ), t≤e →
      Walk e k x 1 → Walk t p x 1 → 2*k+t=2*p+e by
    rcases le_total t e with h|h
    · exact ordered e k t p x h w v
    · exact (ordered t p e k x h v w).symm
  intro e k t p x h w v
  obtain ⟨d,hd⟩ := Nat.exists_eq_add_of_le h
  rw [hd] at w
  obtain ⟨a,b,z,left,right,counts⟩ := split w
  have u := readout left
  have q := readout v
  have zp : z=1 := u.1.symm.trans q.1
  have ap : a=p := u.2.symm.trans q.2
  subst z
  have db := cycle_balance right
  omega

/-- A checked score bound on one finite path controls every later or earlier
visit to the same target at any native clock. -/
theorem budget_of_witness {e k t p D : ℕ} {x : ℤ}
    (w : Walk e k x 1) (v : Walk t p x 1) (bound : 2*p≤t+D) :
    2*k≤e+D := by
  have h := visit_defect w v
  omega

/-- Clock-only extrapolation: once the exact power comparison holds,
it holds at every greater K. This is a statement about integers, not an
asymptotic extrapolation from computed trajectories. -/
theorem power_threshold_persists {K b D : ℕ}
    (nonneg : D≤2*K+b)
    (threshold : 3^(K+b)≤(2:ℕ)^(2*K+b-D)) (h : ℕ) :
    3^(K+h+b)≤(2:ℕ)^(2*(K+h)+b-D) := by
  have small : (3:ℕ)^h≤4^h := Nat.pow_le_pow_left (by decide) h
  have exponents : 2*(K+h)+b-D=(2*K+b-D)+2*h := by omega
  have four : (2:ℕ)^(2*h)=4^h := by rw [pow_mul]; norm_num
  calc
    3^(K+h+b)=3^(K+b)*3^h := by
      rw [show K+h+b=(K+b)+h by omega,pow_add]
    _≤2^(2*K+b-D)*4^h := Nat.mul_le_mul threshold small
    _=2^(2*(K+h)+b-D) := by rw [exponents,pow_add,four]

def increment (x : ℤ) : ℤ := if x%2=0 then -1 else 1

/-- A finite run with enough reserve at 1 certifies a bound at every future
native clock, including clocks far beyond the checked trajectory. -/
def budgetCheck : ℕ → ℤ → ℤ → Bool
  | 0, x, reserve => decide (x=1 ∧ 1≤reserve)
  | t+1, x, reserve => decide (0≤reserve) &&
      budgetCheck t (step x) (reserve-increment x)

theorem budgetCheck_sound (t : ℕ) (x reserve : ℤ)
    (h : budgetCheck t x reserve=true)
    {e k : ℕ} {y : ℤ} (w : Walk e k x y) : (2:ℤ)*k≤e+reserve := by
  induction t generalizing x reserve e k y with
  | zero =>
    simp only [budgetCheck, decide_eq_true_eq] at h
    obtain ⟨rfl,hr⟩ := h
    have c := cycle_defect w (Or.inl rfl)
    have cy := cycle_origin w (Or.inl rfl)
    rcases cy with rfl|rfl <;> norm_num at c <;> linarith
  | succ t ih =>
    simp only [budgetCheck,Bool.and_eq_true,decide_eq_true_eq] at h
    cases w with
    | nil x => simpa using h.1
    | @even e k x y w =>
      have hx : (2*x)%2=0 := by omega
      have st : step (2*x)=x := by simp [step,hx]
      have hc : budgetCheck t x (reserve+1)=true := by
        simpa [st,increment,hx] using h.2
      have bound := ih x (reserve+1) hc w
      simp only [Nat.cast_add,Nat.cast_one]
      linarith
    | @odd e k x y z eq w =>
      have hx : x%2≠0 := by omega
      have st : step x=y := by simp [step,hx]; omega
      have hc : budgetCheck t y (reserve-1)=true := by
        simpa [st,increment,hx] using h.2
      have bound := ih y (reserve-1) hc w
      simp only [Nat.cast_add,Nat.cast_one]
      linarith

#print axioms visit_defect
#print axioms budget_of_witness
#print axioms power_threshold_persists
#print axioms budgetCheck_sound

end AnchorBudget
