import Std

/-! Integral affine bounds for every ordinary shortcut trajectory.
    No analytic or asymptotic counting claim is assumed. -/
namespace EscapeCore

def step (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else (3*n+1)/2

def state (n : Nat) : Nat → Nat
  | 0 => n
  | k+1 => step (state n k)

def ones (n : Nat) : Nat → Nat
  | 0 => 0
  | k+1 => if state n k % 2 = 0 then ones n k else ones n k + 1

theorem affine (n k : Nat) :
    ∃ b : Nat, 2^k * state n k = 3^(ones n k)*n + b ∧ b + 2^k ≤ 3^k := by
  induction k with
  | zero => exact ⟨0, by simp [state, ones], by decide⟩
  | succ k ih =>
    obtain ⟨b, hb, hbound⟩ := ih
    by_cases h : state n k % 2 = 0
    · have hs : 2 * step (state n k) = state n k := by simp [step,h]; omega
      refine ⟨b, ?_, ?_⟩
      · simp only [state, ones, h, ite_true, Nat.pow_succ]
        rw [Nat.mul_assoc, hs, hb]
      · simp only [Nat.pow_succ]
        omega
    · have hs : 2 * step (state n k) = 3 * state n k + 1 := by simp [step,h]; omega
      refine ⟨3*b+2^k, ?_, ?_⟩
      · simp only [state, ones, h, ite_false, Nat.pow_succ]
        rw [Nat.mul_assoc, hs, Nat.mul_add, Nat.mul_one]
        rw [Nat.mul_left_comm (2^k) 3 (state n k), hb, Nat.mul_add]
        rw [Nat.mul_comm (3^ones n k) 3, Nat.mul_assoc]
        omega
      · simp only [Nat.pow_succ]
        omega

/-- One common interval for all sources of the same Hamming weight,
    regardless of their order of odd steps. Endpoints are scaled to integers. -/
theorem translated_interval (n k M L : Nat) (hl : M ≤ n) (hu : n ≤ M+L) :
    3^(ones n k)*M ≤ 2^k * state n k ∧
    2^k * state n k + 2^k ≤ 3^(ones n k)*M + 3^(ones n k)*L + 3^k := by
  obtain ⟨b, hb, hbound⟩ := affine n k
  have ht := Nat.mul_le_mul_left (3^(ones n k)) hu
  have hs := Nat.mul_le_mul_left (3^(ones n k)) hl
  rw [Nat.mul_add] at ht
  rw [hb]
  omega

def forward {α : Type} (f : α → α) : Nat → α → α
  | 0, x => x
  | t+1, x => f (forward f t x)

theorem forward_add {α : Type} (f : α → α) (s t : Nat) (x : α) :
    forward f (s+t) x = forward f t (forward f s x) := by
  induction t with
  | zero => rfl
  | succ t ih => exact congrArg f ih

/-- A shortcut class spends exactly p of a terminal odd clock R.
    Equal residual images would already give equal original terminal images. -/
theorem residual_distinct {α β ι : Type} (f : α → α) (core : β → α)
    (x y : ι → β) (p R : Nat) (hp : p ≤ R)
    (transport : ∀ i, core (y i) = forward f p (core (x i)))
    (terminal : ∀ i j, forward f R (core (x i)) = forward f R (core (x j)) → i = j)
    (i j : ι) (h : forward f (R-p) (core (y i)) = forward f (R-p) (core (y j))) :
    i = j := by
  apply terminal
  have hR : p+(R-p) = R := by omega
  simpa only [transport, ← forward_add, hR] using h

/-- Any one choice per inverse fiber is synchronously distinct at every time. -/
theorem inverse_transversal {α ι : Type} (f : α → α) (r : Nat)
    (source target : ι → α) (retrace : ∀ i, forward f r (source i) = target i)
    (distinct : ∀ t i j, forward f t (target i) = forward f t (target j) → i = j)
    (t : Nat) (i j : ι) (h : forward f t (source i) = forward f t (source j)) :
    i = j := by
  by_cases ht : t ≤ r
  · apply distinct 0
    change target i = target j
    rw [← retrace i, ← retrace j]
    have hr : t+(r-t) = r := by omega
    simpa only [← forward_add, hr] using congrArg (forward f (r-t)) h
  · apply distinct (t-r)
    rw [← retrace i, ← retrace j, ← forward_add, ← forward_add]
    have ht' : r+(t-r) = t := by omega
    simpa only [ht'] using h

#print axioms affine
#print axioms translated_interval
#print axioms residual_distinct
#print axioms inverse_transversal
end EscapeCore
