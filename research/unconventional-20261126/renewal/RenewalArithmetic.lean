import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Data.Int.Basic
import Mathlib.Tactic.Ring

/-! Two finite arithmetic steps used by the unbounded-record precision bound
    and by the character encoding in the improved cycle sieve. -/
namespace RenewalArithmetic

/-- The cleared difference of two prescribed rational coordinates, written
    in terms of how closely the actual endpoints match those coordinates. -/
theorem bridge_identity (M P C x y a d b e : ℤ)
    (step : P * y = M * x + C) :
    M * a * e + d * e * C - P * b * d =
      M * e * (a - d * x) + P * d * (e * y - b) := by
  have hc : C = P * y - M * x := by
    calc
      C = (M * x + C) - M * x := by ring
      _ = P * y - M * x := by rw [← step]
  rw [hc]
  ring

/-- Divisibility at the two opposite endpoints of the same finite path. -/
theorem joint_precision (M P C x y a d b e U V : ℤ)
    (step : P * y = M * x + C) (clock₂ : U ∣ P) (clock₃ : V ∣ M)
    (source : U ∣ a - d * x) (target : V ∣ e * y - b) :
    U * V ∣ M * a * e + d * e * C - P * b * d := by
  rw [bridge_identity M P C x y a d b e step]
  obtain ⟨p, hp⟩ := clock₂
  obtain ⟨m, hm⟩ := clock₃
  obtain ⟨i, hi⟩ := source
  obtain ⟨j, hj⟩ := target
  refine ⟨m * e * i + p * d * j, ?_⟩
  rw [hm, hp, hi, hj]
  ring

/-- Each entry records the ternary grade and the signed modular carry on
    one transition between successive centered Fourier representatives. -/
inductive CarryPath (modulus : ℤ) (width : ℕ) : List (ℕ × ℤ) → ℤ → ℤ → Prop where
  | nil (x : ℤ) : CarryPath modulus width [] x x
  | step {grade : ℕ} {carry : ℤ} {rest : List (ℕ × ℤ)} {x y z : ℤ}
      (edge : (3 : ℤ) ^ grade * y = 2 ^ width * x + modulus * carry)
      (tail : CarryPath modulus width rest y z) :
      CarryPath modulus width ((grade, carry) :: rest) x z

def carryOffset (modulus : ℤ) (width : ℕ) : List (ℕ × ℤ) → ℤ
  | [] => 0
  | (grade, carry) :: rest =>
      ((2 : ℤ) ^ width) ^ rest.length * modulus * carry +
        3 ^ grade * carryOffset modulus width rest

theorem carry_telescope {M : ℤ} {W : ℕ} {data : List (ℕ × ℤ)} {x z : ℤ}
    (path : CarryPath M W data x z) :
    (3 : ℤ) ^ (data.map Prod.fst).sum * z =
      ((2 : ℤ) ^ W) ^ data.length * x + carryOffset M W data := by
  induction path with
  | nil => simp [carryOffset]
  | @step grade carry rest x y z edge _ ih =>
      simp only [List.map_cons, List.sum_cons, List.length_cons, carryOffset, pow_add, pow_succ]
      calc
        _ = (3 : ℤ) ^ grade * (3 ^ (rest.map Prod.fst).sum * z) := by ring
        _ = (3 : ℤ) ^ grade * (((2 : ℤ) ^ W) ^ rest.length * y +
          carryOffset M W rest) := by rw [ih]
        _ = ((2 : ℤ) ^ W) ^ rest.length * (3 ^ grade * y) +
          3 ^ grade * carryOffset M W rest := by ring
        _ = _ := by rw [edge]; ring

/-- An identical transition-carry string forces a ternary power to divide
    the difference of its two possible initial representatives. -/
theorem carry_string_divisor {M : ℤ} {W : ℕ} {data : List (ℕ × ℤ)} {x z x' z' : ℤ}
    (first : CarryPath M W data x z) (second : CarryPath M W data x' z') :
    (3 : ℤ) ^ (data.map Prod.fst).sum ∣ x - x' := by
  have hthree : IsCoprime (3 : ℤ) 2 := ⟨1, -1, by decide⟩
  have cop : IsCoprime ((3 : ℤ) ^ (data.map Prod.fst).sum)
      (((2 : ℤ) ^ W) ^ data.length) := ((hthree.pow_left).pow_right).pow_right
  apply cop.dvd_of_dvd_mul_left
  refine ⟨z - z', ?_⟩
  calc
    _ = (((2 : ℤ) ^ W) ^ data.length * x + carryOffset M W data) -
        (((2 : ℤ) ^ W) ^ data.length * x' + carryOffset M W data) := by ring
    _ = _ := by rw [← carry_telescope first, ← carry_telescope second]; ring

/-- Two centered representatives closer than the encoded ternary power
    coincide when the signed transition carries agree. -/
theorem centered_carry_string_injective
    {M : ℤ} {W : ℕ} {data : List (ℕ × ℤ)} {x z x' z' : ℤ}
    (first : CarryPath M W data x z) (second : CarryPath M W data x' z')
    (size : (x - x').natAbs < ((3 : ℤ) ^ (data.map Prod.fst).sum).natAbs) :
    x = x' :=
  sub_eq_zero.mp (Int.eq_zero_of_dvd_of_natAbs_lt_natAbs
    (carry_string_divisor first second) size)

#print axioms bridge_identity
#print axioms joint_precision
#print axioms carry_telescope
#print axioms carry_string_divisor
#print axioms centered_carry_string_injective

end RenewalArithmetic
