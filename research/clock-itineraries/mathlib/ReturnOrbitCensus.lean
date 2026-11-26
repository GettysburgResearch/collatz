module
public import HourEscapePacking
import all HourEscapePacking
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.HourEscape
set_option autoImplicit false

private theorem words_choose (s b : ℕ) : (gapWords s b).length=s.choose b := by
  induction s generalizing b with
  | zero => cases b <;> simp [gapWords]
  | succ s ih =>
    cases b with
    | zero => simp [gapWords]
    | succ b => simp [gapWords,ih,Nat.choose_succ_succ,Nat.add_comm]

private theorem weighted_census (s b : ℕ) (fit : b≤s) :
    (gapWords s b).length*12^b*7^(s-b)≤19^s := by
  rw [words_choose]
  calc
    _ = 12^b*7^(s-b)*s.choose b := by ring
    _ ≤ ∑ k∈Finset.range (s+1),12^k*7^(s-k)*s.choose k :=
      Finset.single_le_sum (s:=Finset.range (s+1)) (f:=fun k => 12^k*7^(s-k)*s.choose k)
        (fun _ _ => Nat.zero_le _) (Finset.mem_range.mpr (show b<s+1 by omega))
    _ = _ := by simpa using (add_pow (12:ℕ) 7 s).symm

set_option exponentiation.threshold 1000 in
/-- For a block budget of 317 binary clocks per 200 odd gaps, the binomial
weights 12 and 7 certify a ternary word-count exponent of 19/20. -/
theorem sharp_census_power (r H : ℕ) :
    (gapWords (317*r+H) (200*r)).length^20≤(19^H)^20*(3^(200*r))^19 := by
  let W := (gapWords (317*r+H) (200*r)).length
  let Z := (12:ℕ)^(200*r)*7^(117*r)
  have budget := weighted_census (317*r+H) (200*r) (by omega)
  rw [show 317*r+H-200*r=117*r+H by omega,Nat.pow_add] at budget
  have wbound : W*Z≤19^(317*r+H) := by
    have lower := Nat.mul_le_mul_left ((gapWords (317*r+H) (200*r)).length*12^(200*r))
      (Nat.mul_le_mul_left (7^(117*r)) (Nat.one_le_pow H 7 (by decide)))
    simp only [Nat.mul_one] at lower
    simpa only [W,Z,Nat.mul_assoc] using lower.trans budget
  have powered := Nat.pow_le_pow_left wbound 20
  have base : ((19:ℕ)^317)^20≤(3^200)^19*(12^200*7^117)^20 := by decide
  have each : (19^(317*r):ℕ)^20≤(3^(200*r))^19*Z^20 := by
    have h := Nat.pow_le_pow_left base r
    simpa only [Z,mul_pow,←pow_mul,Nat.mul_assoc,Nat.mul_left_comm,Nat.mul_comm] using h
  rw [mul_pow W Z,pow_add,mul_pow (19^(317*r)) (19^H)] at powered
  apply Nat.le_of_mul_le_mul_right (b:=((19^H)^20*(3^(200*r))^19)) (c:=Z^20) _
    (by dsimp [Z]; positivity)
  calc
    _ ≤ (19^(317*r))^20*(19^H)^20 := powered
    _ ≤ ((3^(200*r))^19*Z^20)*(19^H)^20 := Nat.mul_le_mul_right _ each
    _ = _ := (Nat.mul_comm _ _).trans (Nat.mul_assoc _ _ _).symm

#print axioms sharp_census_power
end Collatz.Itinerary.HourEscape
