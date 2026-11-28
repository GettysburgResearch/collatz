import Mathlib.Data.Nat.Basic
import Lean.Elab.Tactic.Omega

/-! The recursive shortcut, odd count, and fourth-power estimate are those of
PR213 NativeGate and NativeTightness. This file uses the same recurrences in a
fresh namespace to check the centered count without the rational-mass imports.
The stochastic and fixed-basin limit theorems are separate written arguments. -/

set_option autoImplicit false
set_option warningAsError true

namespace Collatz.CriticalCount

def step (x : Nat) : Nat := if x % 2 = 0 then x / 2 else (3*x+1)/2

def orbit (x : Nat) : Nat → Nat
  | 0 => x
  | k+1 => step (orbit x k)

def odds (x : Nat) : Nat → Nat
  | 0 => 0
  | k+1 => odds x k + orbit x k % 2

def ReachesOne (x : Nat) : Prop := ∃ k, orbit x k = 1

theorem orbit_positive {x : Nat} (hx : 0 < x) (k : Nat) : 0 < orbit x k := by
  induction k with
  | zero => exact hx
  | succ k ih =>
    change 0 < step (orbit x k)
    unfold step
    split <;> omega

theorem orbit_add (x k j : Nat) : orbit x (k+j) = orbit (orbit x k) j := by
  induction j with
  | zero => rfl
  | succ j ih => exact congrArg step ih

theorem odds_add (x k j : Nat) : odds x (k+j) = odds x k + odds (orbit x k) j := by
  induction j with
  | zero => rfl
  | succ j ih =>
    change odds x (k+j) + orbit x (k+j) % 2 =
      odds x k + (odds (orbit x k) j + orbit (orbit x k) j % 2)
    rw [ih, orbit_add, Nat.add_assoc]

theorem one_even_clock (j : Nat) : orbit 1 (2*j) = 1 ∧ odds 1 (2*j) = j := by
  induction j with
  | zero => exact ⟨rfl, rfl⟩
  | succ j ih =>
    rw [show 2*(j+1) = 2*j+2 by omega, orbit_add, odds_add, ih.1, ih.2]
    exact ⟨rfl, rfl⟩

def twiceCentered (x k : Nat) : Int := 2*(odds x k : Int) - (k : Int)

theorem twiceCentered_add (x k r : Nat) :
    twiceCentered x (k+r) = twiceCentered x k + twiceCentered (orbit x k) r := by
  unfold twiceCentered
  rw [odds_add]
  omega

theorem one_score (r : Nat) : twiceCentered 1 r = (r % 2 : Nat) := by
  obtain ⟨j, hj | hj⟩ : ∃ j : Nat, r = 2*j ∨ r = 2*j+1 := ⟨r/2, by omega⟩
  · rw [hj]
    simp only [twiceCentered, (one_even_clock j).2]
    omega
  · rw [hj]
    simp only [twiceCentered, odds, (one_even_clock j).1, (one_even_clock j).2]
    omega

theorem centered_after_one (x k r : Nat) (hit : orbit x k = 1) :
    twiceCentered x (k+r) - twiceCentered x k = (r % 2 : Nat) := by
  rw [twiceCentered_add, hit, one_score]
  omega

theorem fourth_margin (x : Nat) (hx : 3 ≤ x) : (3*x+1)^4 ≤ 2^7*x^4 := by
  have base : 3*(3*x+1) ≤ 10*x := by omega
  have raised := Nat.pow_le_pow_left base 4
  rw [Nat.mul_pow, Nat.mul_pow] at raised
  have bound : 10^4*x^4 ≤ 3^4*(2^7*x^4) := by
    rw [← Nat.mul_assoc]
    exact Nat.mul_le_mul_right _ (by decide : 10^4 ≤ 3^4*2^7)
  exact Nat.le_of_mul_le_mul_left (Nat.le_trans raised bound) (by decide)

theorem protected_bound (x k : Nat) (floor : ∀ j < k, 3 ≤ orbit x j) :
    2^(4*k) * (orbit x k)^4 ≤ 2^(7*odds x k) * x^4 := by
  induction k with
  | zero => simp [orbit, odds]
  | succ k ih =>
    have hi := ih (fun j hj => floor j (by omega))
    let y := orbit x k
    have hf : 3 ≤ y := floor k (by omega)
    have oneStep : 2^4*(step y)^4 ≤ 2^(7*(y%2))*y^4 := by
      rw [← Nat.mul_pow]
      by_cases he : y%2=0
      · have eq : 2*step y = y := by simp only [step, he, ite_true]; omega
        rw [eq, he]
        simp
      · have odd : y%2=1 := by omega
        have eq : 2*step y = 3*y+1 := by simp only [step, he, ite_false]; omega
        rw [eq, odd]
        exact fourth_margin y hf
    change 2^(4*(k+1))*(step y)^4 ≤ 2^(7*(odds x k+y%2))*x^4
    rw [show 4*(k+1) = 4*k+4 by omega, Nat.mul_add, Nat.pow_add, Nat.pow_add]
    calc
      2^(4*k)*2^4*(step y)^4 = 2^(4*k)*(2^4*(step y)^4) := Nat.mul_assoc ..
      _ ≤ 2^(4*k)*(2^(7*(y%2))*y^4) := Nat.mul_le_mul_left _ oneStep
      _ = 2^(7*(y%2))*(2^(4*k)*y^4) := Nat.mul_left_comm ..
      _ ≤ 2^(7*(y%2))*(2^(7*odds x k)*x^4) := Nat.mul_le_mul_left _ hi
      _ = 2^(7*odds x k)*2^(7*(y%2))*x^4 := by rw [Nat.mul_assoc, Nat.mul_left_comm]

theorem protected_fixed_start (a r m : Nat) (ha : 0 < a) (small : a ≤ 2^m)
    (floor : ∀ i < r, 3 ≤ orbit a i) :
    (r : Int) ≤ 7*twiceCentered a r+8*(m : Int) := by
  have hb := protected_bound a r floor
  have ho := orbit_positive ha r
  have hp : 0 < (orbit a r)^4 := Nat.pow_pos ho
  have hs := Nat.pow_le_pow_left small 4
  have hpow : (2 : Nat)^(4*r) ≤ 2^(7*odds a r+m*4) := by
    calc
      (2 : Nat)^(4*r) = 2^(4*r)*1 := (Nat.mul_one _).symm
      _ ≤ 2^(4*r)*(orbit a r)^4 := Nat.mul_le_mul_left _ hp
      _ ≤ 2^(7*odds a r)*a^4 := hb
      _ ≤ 2^(7*odds a r)*(2^m)^4 := Nat.mul_le_mul_left _ hs
      _ = 2^(7*odds a r+m*4) := by rw [Nat.pow_add, Nat.pow_mul 2 m 4]
  have he := (Nat.pow_le_pow_iff_right (by decide : 1 < (2 : Nat))).mp hpow
  unfold twiceCentered
  omega

theorem nonconvergent_floor (a : Nat) (ha : 0 < a) (bad : ¬ ReachesOne a) (i : Nat) :
    3 ≤ orbit a i := by
  have hi := orbit_positive ha i
  have hone : orbit a i ≠ 1 := fun h => bad ⟨i, h⟩
  have htwo : orbit a i ≠ 2 := by
    intro h
    apply bad
    refine ⟨i+1, ?_⟩
    rw [orbit_add, h]
    decide
  omega

theorem centered_after_nonconvergent (x k a r m : Nat) (hit : orbit x k = a)
    (ha : 0 < a) (bad : ¬ ReachesOne a) (small : a ≤ 2^m) :
    (r : Int) ≤ 7*(twiceCentered x (k+r)-twiceCentered x k)+8*(m : Int) := by
  have h := protected_fixed_start a r m ha small (fun i _ => nonconvergent_floor a ha bad i)
  rw [twiceCentered_add, hit]
  omega

end Collatz.CriticalCount
