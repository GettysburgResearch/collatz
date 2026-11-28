import AffineOrbit

/-! Finite positive-integer suffix selection at the first odd entrance.
The limiting source laws and probabilistic transport are separate written inputs. -/

namespace Collatz.InverseSuffixTransport
open Collatz.PoweredAffine

private theorem orbit_sum (x t d : ℕ) : orbit x (t + d) = orbit (orbit x t) d := by
  induction t generalizing x with
  | zero => simp [orbit]
  | succ t ih =>
    rw [Nat.succ_add]
    exact ih (step x)

private theorem step_half_lower (x : ℕ) : x ≤ 2 * step x := by
  by_cases h : x % 2 = 0
  · exact (even_step h).ge
  · have ho : x % 2 = 1 := by omega
    rw [odd_step ho]
    omega

/-- A source arriving at the prescribed native date lies below its
endpoint times the largest possible inverse multiplier. -/
theorem source_le_dyadic_endpoint (x t : ℕ) : x ≤ 2 ^ t * orbit x t := by
  induction t generalizing x with
  | zero => simp [orbit]
  | succ t ih =>
    calc
      x ≤ 2 * step x := step_half_lower x
      _ ≤ 2 * (2 ^ t * orbit (step x) t) := Nat.mul_le_mul_left 2 (ih (step x))
      _ = 2 ^ (t+1) * orbit x (t+1) := by simp [pow_succ, orbit]; ring

def FirstOddBelow (x z t : ℕ) : Prop :=
  (orbit x t % 2 = 1 ∧ orbit x t ≤ z) ∧
    ∀ i < t, ¬(orbit x i % 2 = 1 ∧ orbit x i ≤ z)

private theorem even_coast {x z : ℕ} (hx : x ≤ z) (t : ℕ)
    (skip : ∀ i < t, ¬(orbit x i % 2 = 1 ∧ orbit x i ≤ z)) :
    2 ^ t * orbit x t = x := by
  induction t generalizing x with
  | zero => simp [orbit]
  | succ t ih =>
    have he : x % 2 = 0 := by
      by_contra! h
      exact skip 0 (by omega) ⟨(show x % 2 = 1 by omega), hx⟩
    have hs := even_step he
    have rest := ih (x := step x) (by omega) (fun i hi => skip (i+1) (by omega))
    change 2 ^ (t+1) * orbit (step x) t = x
    calc
      _ = 2 * (2 ^ t * orbit (step x) t) := by rw [pow_succ]; ring
      _ = x := by rw [rest, hs]

/-- A target reached below the threshold before the first odd entrance
belongs to the exact halving string ending at that entrance. -/
theorem prior_target_coast {x a z t d : ℕ} (target : orbit x t = a)
    (within : a ≤ z) (entrance : FirstOddBelow x z d) (order : t ≤ d) :
    2 ^ (d-t) * orbit x d = a := by
  obtain ⟨j, rfl⟩ := Nat.exists_eq_add_of_le order
  have skip : ∀ i < j, ¬(orbit a i % 2 = 1 ∧ orbit a i ≤ z) := by
    intro i hi
    have s := entrance.2 (t+i) (by omega)
    rwa [orbit_sum, target] at s
  rw [Nat.add_sub_cancel_left, orbit_sum, target]
  exact even_coast within j skip

def incoming (x t k : ℕ) : List ℕ :=
  (List.range (k+1)).map fun i => orbit x (t-i)

/-- Every incoming native list can be read from its earlier landing when
the complete tail fits; the equality preserves the actual ordered values. -/
theorem read_incoming_from {x t d k : ℕ} (room : d + k ≤ t) :
    incoming x t k = incoming (orbit x d) (t-d) k := by
  unfold incoming
  apply List.map_congr_left
  intro i hi
  have bound := List.mem_range.mp hi
  have dates : t-i = d + ((t-d)-i) := by omega
  rw [dates, orbit_sum]

/-- Outside the small-landing error set, a successful source supplies
its complete k-step suffix through the actual first odd entrance. -/
theorem large_entrance_reads_incoming {x a z t d k : ℕ} (target : orbit x t = a)
    (within : a ≤ z) (entrance : FirstOddBelow x z d) (large : 2 ^ k * a < orbit x d) :
    d + k ≤ t ∧ incoming x t k = incoming (orbit x d) (t-d) k := by
  have room : d + k ≤ t := by
    by_contra! small
    by_cases early : t ≤ d
    · have coast := prior_target_coast target within entrance early
      have factor : 0 < 2 ^ (d-t) := by positivity
      have down := Nat.le_mul_of_pos_left (orbit x d) factor
      have base := Nat.le_mul_of_pos_left a (show 0 < 2 ^ k by positivity)
      omega
    · have split : d + (t-d) = t := by omega
      have bound := source_le_dyadic_endpoint (orbit x d) (t-d)
      rw [← orbit_sum, split, target] at bound
      have ex := Nat.pow_le_pow_right (show 0 < 2 by decide) (show t-d ≤ k by omega)
      exact (not_lt_of_ge (bound.trans (Nat.mul_le_mul_right a ex))) large
  exact ⟨room, read_incoming_from room⟩

end Collatz.InverseSuffixTransport
