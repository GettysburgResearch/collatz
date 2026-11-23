import Std

/-!
Finite arithmetic for complete Collatz prefix carries.

The statements below are implications from explicit integer affine/edge
equations. They do not assume or prove a divergent orbit, a stationary
law, a subexponential growth estimate, or universal Collatz convergence.
-/

namespace FixedSourcePrefixGcd

theorem affine_gcd_exact (u v p q c : Int)
    (hcoprime : Int.gcd u v = 1)
    (haffine : u * q = v * p + c) :
    Int.gcd c (u - v) = Int.gcd (q - p) (u - v) := by
  have hc : c = u * (q - p) + (u - v) * p := by
    simp only [Int.mul_sub, Int.sub_mul]
    omega
  have hunit : Int.gcd u (u - v) = 1 := by
    simpa only [Int.gcd_self_sub_right] using hcoprime
  calc
    Int.gcd c (u - v)
        = Int.gcd (u * (q - p) + (u - v) * p) (u - v) := by rw [hc]
    _ = Int.gcd (u * (q - p)) (u - v) :=
      Int.gcd_add_mul_left_left (u - v) (u * (q - p)) p
    _ = Int.gcd (q - p) (u - v) :=
      Int.gcd_mul_right_left_of_gcd_eq_one hunit

theorem affine_gcd_dvd_displacement (u v p q c : Int)
    (hcoprime : Int.gcd u v = 1)
    (haffine : u * q = v * p + c) :
    (Int.gcd c (u - v) : Int) ∣ q - p := by
  rw [affine_gcd_exact u v p q c hcoprime haffine]
  exact Int.gcd_dvd_left (q - p) (u - v)

theorem collatz_prefix_gcd_exact (a n : Nat) (p q c : Int)
    (haffine : (2 : Int)^a * q = (3 : Int)^n * p + c) :
    Int.gcd c ((2 : Int)^a - (3 : Int)^n) =
      Int.gcd (q - p) ((2 : Int)^a - (3 : Int)^n) := by
  apply affine_gcd_exact
  · exact Int.pow_gcd_pow_of_gcd_eq_one (by decide : Int.gcd 2 3 = 1)
  · exact haffine

theorem collatz_prefix_gcd_le_displacement (a n : Nat) (p q c : Int)
    (haffine : (2 : Int)^a * q = (3 : Int)^n * p + c)
    (hdistinct : q ≠ p) :
    Int.gcd c ((2 : Int)^a - (3 : Int)^n) ≤ (q - p).natAbs := by
  rw [collatz_prefix_gcd_exact a n p q c haffine]
  apply Nat.le_of_dvd
  · have hne : q - p ≠ 0 := by omega
    omega
  · exact Int.gcd_dvd_natAbs_left (q - p) ((2 : Int)^a - (3 : Int)^n)

def clock (g : Nat → Nat) : Nat → Nat
  | 0 => 0
  | n + 1 => clock g n + g n

def carry (g : Nat → Nat) : Nat → Int
  | 0 => 0
  | n + 1 => 3 * carry g n + (2 : Int) ^ clock g n

theorem prefix_affine_from_edges (g : Nat → Nat) (q : Nat → Int)
    (hedges : ∀ n, (2 : Int) ^ g n * q (n + 1) = 3 * q n + 1)
    (n : Nat) :
    (2 : Int) ^ clock g n * q n = (3 : Int) ^ n * q 0 + carry g n := by
  induction n with
  | zero => simp [clock, carry]
  | succ n ih =>
    calc
      (2 : Int) ^ clock g (n + 1) * q (n + 1)
          = (2 : Int) ^ clock g n * ((2 : Int) ^ g n * q (n + 1)) := by
              simp [clock, Int.pow_add, Int.mul_assoc]
      _ = (2 : Int) ^ clock g n * (3 * q n + 1) := by rw [hedges n]
      _ = 3 * ((2 : Int) ^ clock g n * q n) + (2 : Int) ^ clock g n := by
            simp [Int.mul_add, Int.mul_assoc, Int.mul_left_comm, Int.mul_comm]
      _ = 3 * ((3 : Int) ^ n * q 0 + carry g n) + (2 : Int) ^ clock g n := by
            rw [ih]
      _ = (3 : Int) ^ (n + 1) * q 0 + carry g (n + 1) := by
            simp [carry, Int.pow_succ, Int.mul_add, Int.add_assoc,
              Int.mul_assoc, Int.mul_comm]

theorem all_prefix_gcd_le_displacement (g : Nat → Nat) (q : Nat → Int)
    (hedges : ∀ n, (2 : Int) ^ g n * q (n + 1) = 3 * q n + 1)
    (n : Nat) (hdistinct : q n ≠ q 0) :
    Int.gcd (carry g n) ((2 : Int) ^ clock g n - (3 : Int) ^ n)
      ≤ (q n - q 0).natAbs := by
  exact collatz_prefix_gcd_le_displacement (clock g n) n (q 0) (q n)
    (carry g n) (prefix_affine_from_edges g q hedges n) hdistinct

#print axioms affine_gcd_exact
#print axioms affine_gcd_dvd_displacement
#print axioms collatz_prefix_gcd_exact
#print axioms collatz_prefix_gcd_le_displacement
#print axioms prefix_affine_from_edges
#print axioms all_prefix_gcd_le_displacement

end FixedSourcePrefixGcd
