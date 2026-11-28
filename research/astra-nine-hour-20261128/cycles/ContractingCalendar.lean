import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Algebra.Order.Field.Rat

/-! Arithmetic kernels for the two-slope shared-tail exclusion.
The finite Boolean certificate compares all pairs below 18 directly.
The analytic tail estimate and extraction of the genuine extremal
phases are the written parts of CONTRACTING_CALENDARS.md. -/

namespace Collatz.ContractingCalendar

/-- At two post-bit extremal phases, the shared tail gives the first
inequality. Strict lower and upper fixed-point bounds at their
respective predecessors then force the complete denominator inequality. -/
theorem contracting_span {A B d K m Wlo Whi : ℚ}
    (hB : 0<B) (loPos : 0<B-A) (hiPos : 0<B-3*A)
    (lower : d*K < (B-A)*Wlo) (upper : (B-3*A)*Whi < d*K)
    (span : 2*B*(m-1) ≤ 3*Whi-Wlo) :
    (m-1)*(B-A)*(B-3*A) < d*K := by
  have h₁ := mul_lt_mul_of_pos_right lower hiPos
  have h₂ := mul_lt_mul_of_pos_right upper (by linarith : 0 < 3*(B-A))
  have h₃ := mul_le_mul_of_nonneg_right span (le_of_lt (mul_pos loPos hiPos))
  have hu : 3*Whi*((B-A)*(B-3*A)) < 3*(B-A)*(d*K) := by
    convert h₂ using 1 <;> ring
  have hl : d*K*(B-3*A) < Wlo*((B-A)*(B-3*A)) := by
    convert h₁ using 1
    ring
  apply (mul_lt_mul_iff_right₀ (by positivity : 0 < 2*B)).mp
  calc
    2*B*((m-1)*(B-A)*(B-3*A)) = 2*B*(m-1)*((B-A)*(B-3*A)) := by ring
    _ ≤ (3*Whi-Wlo)*((B-A)*(B-3*A)) := h₃
    _ = 3*Whi*((B-A)*(B-3*A))-Wlo*((B-A)*(B-3*A)) := by ring
    _ < 3*(B-A)*(d*K)-d*K*(B-3*A) := sub_lt_sub hu hl
    _ = 2*B*(d*K) := by ring

/-- The homogeneous coordinate at a small branch. -/
theorem small_residual {R : Type*} [CommRing R] {A B D x y : R}
    (edge : B*y=A*x+D) :
    B*((B-A)*y-D)=A*((B-A)*x-D) := by
  linear_combination (B-A)*edge

/-- The residual at the end of a long true small-branch run contains
all the ternary divisibility, with its own source denominator retained. -/
theorem terminal_divisibility {s v L : ℕ} {x y : ℤ}
    (path : ((2:ℤ)^s)^L*y=((3:ℤ)^v)^L*x) :
    ((3:ℤ)^v)^L ∣ y := by
  have cop : IsCoprime (3:ℤ) 2 := ⟨1,-1,by decide⟩
  rw [← pow_mul, ← pow_mul] at path
  rw [← pow_mul]
  exact (cop.pow (m:=v*L) (n:=s*L)).dvd_of_dvd_mul_left ⟨x,path⟩

def testPair (s v : ℕ) : Bool :=
  let B := 2^s
  let A := 3^v
  decide (3*A ≥ B ∨ 2^(s-v+1)*A-A-B ≤ (B-A)*(B-3*A))

def checkRow (s : ℕ) : Bool :=
  (List.range s).all (testPair s)

def smallRange : Bool :=
  (List.range 18).all checkRow

set_option maxRecDepth 4000 in
set_option maxHeartbeats 1000000 in
theorem smallRange_true : smallRange = true := by decide +kernel

theorem finite_carry_comparison {s v : ℕ} (hs : s<18) (hv : v<s)
    (hc : 3*(3^v) < 2^s) :
    2^(s-v+1)*3^v-3^v-2^s ≤ (2^s-3^v)*(2^s-3*(3^v)) := by
  have rows : ∀ i ∈ List.range 18, checkRow i = true :=
    List.all_eq_true.mp smallRange_true
  have row := rows s (List.mem_range.mpr hs)
  have pairs : ∀ i ∈ List.range s, testPair s i = true := List.all_eq_true.mp row
  have p := pairs v (List.mem_range.mpr hv)
  simpa [testPair, not_le.mpr hc] using p

theorem farey_endpoints : (3:ℕ)^306 < 2^485 ∧ (2:ℕ)^84 < 3^53 := by
  decide +kernel

/-- Scaled rational form of the gap separating all intermediate denominators. -/
theorem intermediate_gap {s k : ℕ} (hs : s≤255) (hk : 84*k < 53*s) :
    485 + 200*485*k < 200*306*s := by omega

#print axioms farey_endpoints
#print axioms intermediate_gap
#print axioms contracting_span
#print axioms small_residual
#print axioms terminal_divisibility
#print axioms smallRange_true
#print axioms finite_carry_comparison

end Collatz.ContractingCalendar
