import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

set_option autoImplicit false

namespace PersistentDivisor

/-- The fee after one complete block divided by its persistent odd factor.
    The initial odd part is g*u, and the shifted landing is g*v. -/
theorem physical_fee (g u v z t b : ℕ) (hb : 0 < b)
    (landing : z+1 = g*v) (edge : 2^b*z+1 = 3^t*(g*u)) :
    ∃ fee : ℕ, 0 < fee ∧ g*fee+1 = 2^b ∧ 2^b*v = 3^t*u+fee := by
  have hp : 1 < 2^b := Nat.one_lt_pow (by omega) (by decide)
  have key : g*(2^b*v)+1 = g*(3^t*u)+2^b := by
    nlinarith only [edge, congrArg (fun a : ℕ => 2^b*a) landing]
  have grow : 3^t*u < 2^b*v := by
    by_contra! hn
    have := Nat.mul_le_mul_left g hn
    omega
  refine ⟨2^b*v-3^t*u, by omega, ?_, by omega⟩
  have diff : 3^t*u+(2^b*v-3^t*u) = 2^b*v := by omega
  nlinarith only [key, congrArg (fun n : ℕ => g*n) diff]

/-- The recurrence used after the first scaled block is likewise physical. -/
theorem physical_scaled_block (g u v z t b : ℕ) (hb : 0 < b)
    (landing : z+1 = g*v) (edge : 2^b*z+1 = 3^t*(g*u)) :
    ∃ fee : ℕ, 0 < fee ∧ g*fee+1=2^b ∧
      2^(t+b)*v = 3^t*(2^t*u)+2^t*fee := by
  obtain ⟨fee, hpos, hpay, hscaled⟩ := physical_fee g u v z t b hb landing edge
  refine ⟨fee, hpos, hpay, ?_⟩
  rw [pow_add]
  nlinarith only [congrArg (fun j : ℕ => 2^t*j) hscaled]

structure Coord where
  twos : ℕ
  threes : ℕ
  core : ℕ

def Coord.value (a : Coord) : ℕ := 2^a.twos * 3^a.threes * a.core

def Coord.raise (t : ℕ) (a : Coord) : Coord := ⟨a.twos, a.threes+t, a.core⟩

def total (xs : List Coord) : ℕ := (xs.map Coord.value).sum

def cores (xs : List Coord) : ℕ := (xs.map Coord.core).prod

theorem total_raise (xs : List Coord) (t : ℕ) :
    total (xs.map (Coord.raise t)) = 3^t * total xs := by
  induction xs with
  | nil => simp [total]
  | cons a xs ih =>
    change (Coord.raise t a).value + total (xs.map (Coord.raise t)) =
      3^t*(a.value+total xs)
    rw [ih]
    simp only [Coord.value, Coord.raise, pow_add]
    ring

theorem cores_raise (xs : List Coord) (t : ℕ) :
    cores (xs.map (Coord.raise t)) = cores xs := by
  induction xs with
  | nil => rfl
  | cons a xs ih =>
    change a.core * cores (xs.map (Coord.raise t)) = a.core * cores xs
    rw [ih]

/-- Exact scaled expansions after the first dyadic ascent power is removed.
    The four natural indices are shifted landing/g, total rises,
    remaining cumulative denominator exponent, and total reset excess. -/
inductive Chain (g u : ℕ) : List Coord → ℕ → ℕ → ℕ → ℕ → Prop
  | first (t b fee z : ℕ) (hfee : 0 < fee) (pay : g*fee+1=2^b)
      (edge : 2^b*z=3^t*u+fee) :
      Chain g u [⟨0,0,fee⟩] z t b b
  | more {xs : List Coord} {y T D B : ℕ} (p : Chain g u xs y T D B)
      (t b fee z : ℕ) (hfee : 0 < fee) (pay : g*fee+1=2^b)
      (edge : 2^(t+b)*z=3^t*y+2^t*fee) :
      Chain g u (⟨D+t,0,fee⟩ :: xs.map (Coord.raise t)) z
        (T+t) (D+(t+b)) (B+b)

/-- Exact positive Evertse coordinates, including every factor of g in their
    cores. This is integer algebra; the external analytic theorem is separate. -/
theorem chain_coordinates {g u : ℕ} {xs : List Coord} {z T D B : ℕ}
    (p : Chain g u xs z T D B) :
    2^D*z = 3^T*u+total xs ∧ g^xs.length*cores xs ≤ 2^B ∧
    (∀ a ∈ xs, 0 < a.core) := by
  induction p with
  | first t b fee z hfee pay edge =>
    refine ⟨?_, ?_, ?_⟩
    · simpa [total, Coord.value] using edge
    · simp [cores]
      omega
    · simpa using hfee
  | @more xs y T D B p t b fee z hfee pay edge ih =>
    obtain ⟨hsum, hbound, hpos⟩ := ih
    refine ⟨?_, ?_, ?_⟩
    · change 2^(D+(t+b))*z =
        3^(T+t)*u + ((⟨D+t,0,fee⟩ : Coord).value+total (xs.map (Coord.raise t)))
      rw [total_raise, pow_add (2 : ℕ) D, pow_add (3 : ℕ) T]
      simp only [Coord.value, pow_zero, mul_one, pow_add]
      rw [pow_add] at edge
      nlinarith only [congrArg (fun j : ℕ => 2^D*j) edge,
        congrArg (fun j : ℕ => 3^t*j) hsum]
    · change g^((xs.map (Coord.raise t)).length+1)*(fee*cores (xs.map (Coord.raise t))) ≤ _
      rw [List.length_map, cores_raise, pow_succ, pow_add]
      calc
        g^xs.length*g*(fee*cores xs) = (g*fee)*(g^xs.length*cores xs) := by ring
        _ ≤ 2^b*2^B := Nat.mul_le_mul (show g*fee ≤ 2^b by omega) hbound
        _ = _ := Nat.mul_comm _ _
    · intro a ha
      rcases List.mem_cons.mp ha with rfl | hin
      · exact hfee
      · rcases List.mem_map.mp hin with ⟨v, hv, rfl⟩
        exact hpos v hv

/-- Exact power of two on the coordinate sum, including the terminal shift.
    Since the retained g is odd, this is also the shift of the true landing. -/
theorem terminal_power {g u : ℕ} {xs : List Coord} {z T D B h w : ℕ}
    (p : Chain g u xs z T D B) (hz : z=2^h*w) (hw : Odd w) :
    2^(D+h) ∣ 3^T*u+total xs ∧ ¬ 2^(D+h+1) ∣ 3^T*u+total xs := by
  have sum := (chain_coordinates p).1
  have physical : 3^T*u+total xs = 2^(D+h)*w := by
    rw [← sum, hz, pow_add]
    ring
  rw [physical]
  refine ⟨⟨w, rfl⟩, ?_⟩
  rintro ⟨j, hj⟩
  have eq : 2^(D+h)*w=2^(D+h)*(2*j) := by
    simpa only [pow_succ, Nat.mul_assoc] using hj
  have bad := Nat.eq_of_mul_eq_mul_left (Nat.pow_pos (by decide : 0 < 2)) eq
  obtain ⟨k, hk⟩ := hw
  omega

#print axioms physical_fee
#print axioms physical_scaled_block
#print axioms total_raise
#print axioms cores_raise
#print axioms chain_coordinates
#print axioms terminal_power

end PersistentDivisor
