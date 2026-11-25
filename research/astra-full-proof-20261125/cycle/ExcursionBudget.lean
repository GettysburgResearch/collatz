import Std

namespace Collatz.ExcursionBudget

/-- Number of endpoints above a fixed threshold in the first n steps. -/
def highVisits (x : Nat → Nat) (H : Nat) : Nat → Nat
  | 0 => 0
  | n + 1 => highVisits x H n + if H < x (n + 1) then 1 else 0

/-- Charge the odd-step valuation precisely when its endpoint is high. -/
def highClock (x a : Nat → Nat) (H : Nat) : Nat → Nat
  | 0 => 0
  | n + 1 => highClock x a H n + if H < x (n + 1) then a n else 0

private theorem high_step {x y a m H d : Nat}
    (floor : m ≤ x) (high : H < y) (edge : 2^a * y = 3*x + d) :
    m * 2^a * max H y ≤ (3*m + d) * max H x := by
  rw [Nat.max_eq_right (by omega : H ≤ y), Nat.mul_assoc, edge]
  calc
    m * (3*x + d) = 3*m*x + m*d := by simp [Nat.mul_add, Nat.mul_comm, Nat.mul_left_comm]
    _ ≤ 3*m*x + d*x := Nat.add_le_add_left (by simpa [Nat.mul_comm] using Nat.mul_le_mul_left d floor) _
    _ = (3*m + d) * x := by rw [Nat.add_mul]
    _ ≤ (3*m + d) * max H x := Nat.mul_le_mul_left _ (Nat.le_max_right _ _)

/-- Multiplicative budget for all high visits, including incomplete excursions. -/
theorem clipped_product (x a : Nat → Nat) (d m H n : Nat)
    (floor : ∀ i < n, m ≤ x i)
    (edge : ∀ i < n, 2^(a i) * x (i+1) = 3*x i + d) :
    m^(highVisits x H n) * 2^(highClock x a H n) * max H (x n)
       ≤ (3*m+d)^(highVisits x H n) * max H (x 0) := by
  induction n with
  | zero => simp [highVisits, highClock]
  | succ n ih =>
    have prev := ih (fun i hi => floor i (by omega)) (fun i hi => edge i (by omega))
    by_cases high : H < x (n+1)
    · have step := high_step (floor n (by omega)) high (edge n (by omega))
      simp only [highVisits, highClock, high, ite_true, Nat.pow_succ, Nat.pow_add]
      calc
        _ = (m^(highVisits x H n) * 2^(highClock x a H n)) *
              (m * 2^(a n) * max H (x (n+1))) := by ac_rfl
        _ ≤ (m^(highVisits x H n) * 2^(highClock x a H n)) *
              ((3*m+d) * max H (x n)) := Nat.mul_le_mul_left _ step
        _ = (3*m+d) * (m^(highVisits x H n) * 2^(highClock x a H n) * max H (x n)) := by ac_rfl
        _ ≤ (3*m+d) * ((3*m+d)^(highVisits x H n) * max H (x 0)) := Nat.mul_le_mul_left _ prev
        _ = _ := by ac_rfl
    · have next : max H (x (n+1)) ≤ max H (x n) := by
        rw [Nat.max_eq_left (by omega : x (n+1) ≤ H)]
        exact Nat.le_max_left _ _
      simp only [highVisits, highClock, high, ite_false, Nat.add_zero]
      exact Nat.le_trans (Nat.mul_le_mul_left _ next) prev

/-- An initially low window pays at most log₂(3 + d/m) clock per high visit,
written with integer powers. -/
theorem initially_low_budget (x a : Nat → Nat) {d m H n : Nat}
    (pos : 0 < H) (low : x 0 ≤ H)
    (floor : ∀ i < n, m ≤ x i)
    (edge : ∀ i < n, 2^(a i) * x (i+1) = 3*x i + d) :
    m^(highVisits x H n) * 2^(highClock x a H n) ≤ (3*m+d)^(highVisits x H n) := by
  have prod := clipped_product x a d m H n floor edge
  rw [Nat.max_eq_left low] at prod
  have small := Nat.mul_le_mul_left (m^(highVisits x H n) * 2^(highClock x a H n))
    (Nat.le_max_left H (x n))
  exact Nat.le_of_mul_le_mul_right (Nat.le_trans small prod) pos

/-- In a fixed rational lattice, a common valuation word determines the
terminal numerator modulo the full power of three. Natural subtraction
records one orientation, and exchanging x and y records the other. -/
theorem common_word_dvd (x y a : Nat → Nat) (d n : Nat)
    (ex : ∀ i < n, 2^(a i) * x (i+1) = 3*x i + d)
    (ey : ∀ i < n, 2^(a i) * y (i+1) = 3*y i + d) :
    3^n ∣ x n - y n := by
  induction n with
  | zero => simp
  | succ n ih =>
    have prev := ih (fun i hi => ex i (by omega)) (fun i hi => ey i (by omega))
    have step : 2^(a n) * (x (n+1) - y (n+1)) = 3 * (x n - y n) := by
      rw [Nat.mul_sub, ex n (by omega), ey n (by omega), Nat.add_sub_add_right, Nat.mul_sub]
    apply ((by decide : Nat.Coprime 3 2).pow (n+1) (a n)).dvd_of_dvd_mul_left
    rw [step, Nat.pow_succ, Nat.mul_comm (3^n) 3]
    exact Nat.mul_dvd_mul_left 3 prev

/-- Equal valuation words have at most one terminal in a common interval
[u,v] of length less than 3^n. -/
theorem common_word_terminal (x y a : Nat → Nat) {d n u v : Nat}
    (ex : ∀ i < n, 2^(a i) * x (i+1) = 3*x i + d)
    (ey : ∀ i < n, 2^(a i) * y (i+1) = 3*y i + d)
    (hx : u ≤ x n ∧ x n ≤ v) (hy : u ≤ y n ∧ y n ≤ v)
    (width : v-u < 3^n) : x n = y n := by
  rcases Nat.lt_trichotomy (x n) (y n) with lt | eq | gt
  · have bound := Nat.le_of_dvd (by omega : 0 < y n - x n) (common_word_dvd y x a d n ey ex)
    omega
  · exact eq
  · have bound := Nat.le_of_dvd (by omega : 0 < x n - y n) (common_word_dvd x y a d n ex ey)
    omega

#print axioms common_word_dvd
#print axioms common_word_terminal
#print axioms clipped_product
#print axioms initially_low_budget

end Collatz.ExcursionBudget
