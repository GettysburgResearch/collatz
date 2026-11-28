import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Nat.ModEq
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
An end-to-end finite rational gate for the actual shortcut Collatz map.
The extinction condition at the end is an OPEN premise.  No instance of
that premise, no custom axiom, and no proof of Collatz is supplied.

The source-mass idea and the 7/4 odd-clock gate are prior work in PR201,
GLOBAL_PREFIX_TRACE.md.  This module uses the native binary clock, carries
the actual dynamics through the minimum argument, and defines its finite
observable directly on ordinary integers.
-/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.NativeGate

def step (x : ℕ) : ℕ := if x % 2 = 0 then x / 2 else (3 * x + 1) / 2

def orbit (x : ℕ) : ℕ → ℕ
  | 0 => x
  | k + 1 => step (orbit x k)

def odds (x : ℕ) : ℕ → ℕ
  | 0 => 0
  | k + 1 => odds x k + orbit x k % 2

def ReachesOne (x : ℕ) : Prop := ∃ k, orbit x k = 1
def Universal : Prop := ∀ x, 0 < x → ReachesOne x

def Gate (k x : ℕ) : Prop := ∀ j ≤ k, 4 * j ≤ 7 * odds x j

instance (k x : ℕ) : Decidable (Gate k x) :=
  inferInstanceAs (Decidable (∀ j ≤ k, 4 * j ≤ 7 * odds x j))

def candidates (k : ℕ) : Finset ℕ :=
  (Finset.range (2 ^ k + 1)).filter (fun x => 0 < x ∧ Gate k x)

def mass (k : ℕ) : ℚ := ∑ x ∈ candidates k, (x : ℚ)⁻¹

theorem step_positive {x : ℕ} (hx : 0 < x) : 0 < step x := by
  unfold step
  split_ifs with he
  · omega
  · omega

theorem orbit_positive {x : ℕ} (hx : 0 < x) (k : ℕ) : 0 < orbit x k := by
  induction k with
  | zero => exact hx
  | succ k ih => exact step_positive ih

theorem orbit_add (x k j : ℕ) : orbit x (k + j) = orbit (orbit x k) j := by
  induction j with
  | zero => simp [orbit]
  | succ j ih => simp [orbit, ih]

theorem reaches_of_orbit {x k : ℕ} (h : ReachesOne (orbit x k)) : ReachesOne x := by
  obtain ⟨j, hj⟩ := h
  exact ⟨k + j, by rw [orbit_add]; exact hj⟩

theorem even_step {x : ℕ} (hx : x % 2 = 0) : 2 * step x = x := by
  simp only [step, hx, ite_true]
  omega

theorem odd_step {x : ℕ} (hx : x % 2 = 1) : 2 * step x = 3 * x + 1 := by
  simp only [step, hx, show ¬ (1 : ℕ) = 0 by decide, ite_false]
  omega

theorem fourth_margin (x : ℕ) (hx : 3 ≤ x) : (3 * x + 1)^4 ≤ 2^7 * x^4 := by
  obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le hx
  have hp : 0 ≤ 47*t^4 + 456*t^3 + 1512*t^2 + 1788*t + 368 := Nat.zero_le _
  nlinarith [hp]

/-- The actual orbit's fourth-power homogeneous bound at a protected floor. -/
theorem protected_bound (x k : ℕ) (floor : ∀ j < k, 3 ≤ orbit x j) :
    2^(4*k) * (orbit x k)^4 ≤ 2^(7*odds x k) * x^4 := by
  induction k with
  | zero => simp [orbit, odds]
  | succ k ih =>
    have hi := ih (fun j hj => floor j (by omega))
    have hf := floor k (by omega)
    have he : orbit x k % 2 = 0 ∨ orbit x k % 2 = 1 := by omega
    rcases he with he | he
    · have hs := even_step he
      have hp : 2^4 * (step (orbit x k))^4 = (orbit x k)^4 := by
        nlinarith [congrArg (fun z : ℕ => z^4) hs]
      simp only [odds, he, Nat.add_zero, orbit]
      rw [show 4*(k+1) = 4*k+4 by omega, pow_add]
      calc
        2^(4*k) * 2^4 * (step (orbit x k))^4 = 2^(4*k) * (orbit x k)^4 := by
          rw [Nat.mul_assoc, hp]
        _ ≤ _ := hi
    · have hs := odd_step he
      have hp : 2^4 * (step (orbit x k))^4 ≤ 2^7 * (orbit x k)^4 := by
        have hf4 := fourth_margin (orbit x k) hf
        nlinarith [congrArg (fun z : ℕ => z^4) hs]
      simp only [odds, he, orbit]
      rw [show 4*(k+1) = 4*k+4 by omega, show 7*(odds x k+1) = 7*odds x k+7 by omega,
        pow_add, pow_add]
      calc
        2^(4*k) * 2^4 * (step (orbit x k))^4 ≤ 2^(4*k) * (2^7 * (orbit x k)^4) := by
          nlinarith [Nat.mul_le_mul_left (2^(4*k)) hp]
        _ = 2^7 * (2^(4*k) * (orbit x k)^4) := by ring
        _ ≤ 2^7 * (2^(7*odds x k) * x^4) := Nat.mul_le_mul_left _ hi
        _ = _ := by ring

/-- A positive least source at floor three passes every native prefix gate. -/
theorem least_source_gate {x : ℕ} (hx : 3 ≤ x)
    (least : ∀ k, x ≤ orbit x k) (k : ℕ) : Gate k x := by
  intro j hj
  have hb := protected_bound x j (fun i _ => hx.trans (least i))
  have hx4 : 0 < x^4 := by positivity
  have hle : x^4 ≤ (orbit x j)^4 := Nat.pow_le_pow_left (least j) 4
  have hpow : 2^(4*j) ≤ 2^(7*odds x j) := by
    have hmul : 2^(4*j) * x^4 ≤ 2^(7*odds x j) * x^4 :=
      (Nat.mul_le_mul_left _ hle).trans hb
    exact Nat.le_of_mul_le_mul_right hmul hx4
  exact (Nat.pow_le_pow_iff_right (by decide : 1 < (2 : ℕ))).mp hpow

theorem atom_le_mass {x k : ℕ} (hx : 0 < x) (hk : x ≤ 2^k) (hg : Gate k x) :
    (x : ℚ)⁻¹ ≤ mass k := by
  unfold mass
  apply Finset.single_le_sum (f := fun i : ℕ => (i : ℚ)⁻¹)
    (fun i _ => inv_nonneg.mpr (Nat.cast_nonneg i))
  simp only [candidates, Finset.mem_filter, Finset.mem_range]
  exact ⟨by omega, hx, hg⟩

/-- This is a finite observable condition; its universal truth is OPEN. -/
def Extinction : Prop := ∀ L : ℕ, 0 < L →
  ∃ k : ℕ, L ≤ 2^k ∧ mass k < (L : ℚ)⁻¹

/-- Every substantive premise is displayed: no generic map or oracle is hidden. -/
theorem extinction_implies_collatz (extinction : Extinction) : Universal := by
  intro x
  induction x using Nat.strong_induction_on with
  | h x ih =>
    intro hx
    by_contra hbad
    have hthree : 3 ≤ x := by
      have hone : x ≠ 1 := by
        intro h
        exact hbad ⟨0, by simpa [orbit] using h⟩
      have htwo : x ≠ 2 := by
        intro h
        subst x
        exact hbad ⟨1, by decide⟩
      omega
    have least (k : ℕ) : x ≤ orbit x k := by
      by_contra hlt
      have hgood := ih (orbit x k) (by omega) (orbit_positive hx k)
      exact hbad (reaches_of_orbit hgood)
    obtain ⟨k, hk, hmass⟩ := extinction x hx
    have ha := atom_le_mass hx hk (least_source_gate hthree least k)
    exact (not_lt_of_ge ha) hmass

/-- A single strictly small finite sum certifies every start through L.
This does not assert that such a certificate exists at every L. -/
theorem finite_certificate (L k : ℕ) (hL : 0 < L) (hcut : L ≤ 2^k)
    (hsmall : mass k < (L : ℚ)⁻¹) :
    ∀ x : ℕ, 0 < x → x ≤ L → ReachesOne x := by
  intro x
  induction x using Nat.strong_induction_on with
  | h x ih =>
    intro hx hxL
    by_contra hbad
    have hthree : 3 ≤ x := by
      have hone : x ≠ 1 := by
        intro h
        exact hbad ⟨0, by simpa [orbit] using h⟩
      have htwo : x ≠ 2 := by
        intro h
        subst x
        exact hbad ⟨1, by decide⟩
      omega
    have least (j : ℕ) : x ≤ orbit x j := by
      by_contra hlt
      have hgood := ih (orbit x j) (by omega) (orbit_positive hx j) (by omega)
      exact hbad (reaches_of_orbit hgood)
    have ha := atom_le_mass hx (hxL.trans hcut) (least_source_gate hthree least k)
    have horder : (L : ℚ)⁻¹ ≤ (x : ℚ)⁻¹ := by
      exact (inv_le_inv₀ (by exact_mod_cast hL) (by exact_mod_cast hx)).2
        (by exact_mod_cast hxL)
    exact (not_lt_of_ge (horder.trans ha)) hsmall

/-- Pure loss bookkeeping.  The debt reserve makes the actual global
loss budget finite; a genuinely nonsummable lower loss would contradict
any fixed positive ordinary atom.  This lemma supplies no loss estimate. -/
theorem loss_budget_excludes_atom (J D hazard : ℕ → ℚ) (atom budget : ℚ)
    (hpos : 0 < atom) (hJ : ∀ n, atom ≤ J n)
    (hh : ∀ n, 0 ≤ hazard n)
    (hD : ∀ n, hazard n * J n ≤ D n)
    (hbudget : ∀ N, ∑ n ∈ Finset.range N, D n ≤ budget)
    (hunbounded : ∀ B : ℚ, ∃ N, B < ∑ n ∈ Finset.range N, hazard n) : False := by
  obtain ⟨N, hN⟩ := hunbounded (budget / atom)
  have hlower : atom * (∑ n ∈ Finset.range N, hazard n) ≤
      ∑ n ∈ Finset.range N, D n := by
    rw [Finset.mul_sum]
    apply Finset.sum_le_sum
    intro n _
    have h := mul_le_mul_of_nonneg_left (hJ n) (hh n)
    nlinarith [hD n]
  have hupper := hbudget N
  have hstrict : budget < atom * (∑ n ∈ Finset.range N, hazard n) := by
    have h := (div_lt_iff₀ hpos).mp hN
    nlinarith
  linarith

/-- Binary-clock debt reserve: both children survive at debt at least four. -/
theorem reserve_high (d : ℚ) :
    1 + ((2*(d+3)+8) + (2*(d-4)+8))/2 = 2*d+8 := by ring

/-- At low debt the even child is killed and the unused reserve is nonnegative. -/
theorem reserve_low (d : ℚ) (hd : 0 ≤ d) :
    1 + (2*(d+3)+8)/2 ≤ 2*d+8 := by linarith

#print axioms protected_bound
#print axioms least_source_gate
#print axioms atom_le_mass
#print axioms extinction_implies_collatz
#print axioms finite_certificate
#print axioms loss_budget_excludes_atom
#print axioms reserve_high
#print axioms reserve_low

end Collatz.NativeGate
