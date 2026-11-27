import Mathlib.Data.Finset.Card
import Mathlib.Tactic.Ring

/-! The labelled endpoint partition of a real interval depends only on its dyadic centre residue. -/

namespace Collatz.SixHour.ColorWords

def step (x : ℕ) : ℕ := if x % 2 = 0 then x / 2 else (3 * x + 1) / 2

def oddBit (x : ℕ) : ℕ := if x % 2 = 0 then 0 else 1

def endpoint : ℕ → ℕ → ℕ
  | 0, x => x
  | k + 1, x => endpoint k (step x)

def grade : ℕ → ℕ → ℕ
  | 0, _ => 0
  | k + 1, x => oddBit x + grade k (step x)

theorem bit_lift (x u : ℕ) : oddBit (x + 2 * u) = oddBit x := by
  simp [oddBit, Nat.add_mod]

theorem step_lift (x u : ℕ) : step (x + 2 * u) = step x + 3 ^ oddBit x * u := by
  have he : (x + 2 * u) % 2 = x % 2 := by omega
  unfold step oddBit
  rw [he]
  split <;> simp <;> omega

theorem endpoint_grade_lift (k x q : ℕ) :
    endpoint k (x + 2 ^ k * q) = endpoint k x + 3 ^ grade k x * q ∧
    grade k (x + 2 ^ k * q) = grade k x := by
  induction k generalizing x q with
  | zero => simp [endpoint, grade]
  | succ k ih =>
    rw [show 2 ^ (k + 1) * q = 2 * (2 ^ k * q) by rw [pow_succ]; ring]
    simp only [endpoint, grade, step_lift, bit_lift]
    rw [show 3 ^ oddBit x * (2 ^ k * q) = 2 ^ k * (3 ^ oddBit x * q) by ring]
    obtain ⟨he, hg⟩ := ih (step x) (3 ^ oddBit x * q)
    rw [he, hg, pow_add]
    constructor
    · ring
    · rfl

def labelled (k x : ℕ) : ℕ × ℕ := (grade k x, endpoint k x)

theorem labelled_lift_iff (k a b q : ℕ) :
    labelled k (a + 2 ^ k * q) = labelled k (b + 2 ^ k * q) ↔
      labelled k a = labelled k b := by
  obtain ⟨hea, hga⟩ := endpoint_grade_lift k a q
  obtain ⟨heb, hgb⟩ := endpoint_grade_lift k b q
  simp only [labelled, Prod.mk.injEq, hea, heb, hga, hgb]
  constructor
  · rintro ⟨hg, he⟩
    rw [hg] at he
    exact ⟨hg, Nat.add_right_cancel he⟩
  · rintro ⟨hg, he⟩
    rw [hg, he]
    exact ⟨rfl, rfl⟩

theorem color_endpoint {α : Type*} {f : ℕ → α} (hf : ∀ n, f (step n) = f n)
    (k x : ℕ) : f (endpoint k x) = f x := by
  induction k generalizing x with
  | zero => rfl
  | succ k ih => exact (ih (step x)).trans (hf x)

/-- A genuine shifted colour word factors through the original residue's single finite partition. -/
theorem block_factor {α : Type*} {f : ℕ → α} (hf : ∀ n, f (step n) = f n)
    (k a q : ℕ) :
    ∃ g : ℕ × ℕ → α, ∀ i : ℕ, f (a + 2 ^ k * q + i) = g (labelled k (a + i)) := by
  refine ⟨fun u => f (u.2 + 3 ^ u.1 * q), fun i => ?_⟩
  change f (a + 2 ^ k * q + i) = f (endpoint k (a + i) + 3 ^ grade k (a + i) * q)
  rw [← (endpoint_grade_lift k (a + i) q).1, color_endpoint hf]
  congr 1
  omega

end Collatz.SixHour.ColorWords
