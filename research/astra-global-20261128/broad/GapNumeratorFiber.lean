import Mathlib.Data.Finset.Card
import Mathlib.Tactic.Ring

/-! Native finite arithmetic behind the entropy and joint-dimension estimates.
A list is in reverse execution order. Each entry k encodes the positive gap k+1. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.GapNumeratorFiber

def clock : List ℕ → ℕ
  | [] => 0
  | k :: w => k + 1 + clock w

def numerator : List ℕ → ℕ
  | [] => 0
  | k :: w => 2 ^ (k + 1) * numerator w + 3 ^ w.length

/-- Integer endpoint relation for the inverse branches in the whole word. -/
def Follows : List ℕ → ℕ → ℕ → Prop
  | [], x, y => x = y
  | k :: w, x, y => ∃ z, Follows w x z ∧ 2 ^ (k + 1) * z = 3 * y + 1

theorem affine_of_follows {w : List ℕ} {x y : ℕ} (h : Follows w x y) :
    2 ^ clock w * x = 3 ^ w.length * y + numerator w := by
  induction w generalizing y with
  | nil => simpa [clock, numerator, Follows] using h
  | cons k w ih =>
    obtain ⟨z, hw, he⟩ := h
    calc
      2 ^ clock (k :: w) * x = 2 ^ (k + 1) * (2 ^ clock w * x) := by
        rw [clock, pow_add]
        ring
      _ = 3 ^ w.length * (2 ^ (k + 1) * z) + 2 ^ (k + 1) * numerator w := by
        rw [ih hw]
        ring
      _ = 3 ^ (k :: w).length * y + numerator (k :: w) := by
        rw [he, numerator, List.length_cons, pow_succ]
        ring

theorem residue_of_follows {w : List ℕ} {x y : ℕ} (h : Follows w x y) :
    (2 ^ clock w * x) % 3 ^ w.length = numerator w % 3 ^ w.length := by
  rw [affine_of_follows h, Nat.mul_add_mod_self_left]

private theorem three_pow_odd (n : ℕ) : 3 ^ n % 2 = 1 := by
  induction n with
  | zero => decide
  | succ n ih => rw [pow_succ, Nat.mul_mod, ih]

theorem numerator_odd (k : ℕ) (w : List ℕ) : numerator (k :: w) % 2 = 1 := by
  have he : 2 ^ (k + 1) * numerator w = 2 * (2 ^ k * numerator w) := by
    rw [pow_succ]
    ring
  rw [numerator, he, Nat.mul_add_mod_self_left, three_pow_odd]

private theorem odd_parts {a b u v : ℕ} (hu : u % 2 = 1) (hv : v % 2 = 1)
    (h : 2 ^ a * u = 2 ^ b * v) : a = b := by
  induction a generalizing b with
  | zero =>
    cases b with
    | zero => rfl
    | succ b =>
      have he : 2 ^ (b + 1) * v = 2 * (2 ^ b * v) := by rw [pow_succ]; ring
      rw [pow_zero, one_mul, he] at h
      omega
  | succ a ih =>
    have he : 2 ^ (a + 1) * u = 2 * (2 ^ a * u) := by rw [pow_succ]; ring
    cases b with
    | zero =>
      rw [pow_zero, one_mul, he] at h
      omega
    | succ b =>
      have hf : 2 ^ (b + 1) * v = 2 * (2 ^ b * v) := by rw [pow_succ]; ring
      rw [he, hf] at h
      exact congrArg Nat.succ (ih (by omega))

/-- Literal recovery at a fixed depth and total. -/
theorem word_eq_of_numerator {w v : List ℕ} (hl : w.length = v.length)
    (hc : clock w = clock v) (hn : numerator w = numerator v) : w = v := by
  induction w generalizing v with
  | nil => cases v <;> simp_all
  | cons k w ih =>
    cases v with
    | nil => simp at hl
    | cons j v =>
      have hlen : w.length = v.length := by simpa only [List.length_cons, Nat.add_left_inj] using hl
      cases w with
      | nil =>
        cases v with
        | nil =>
          have hkj : k = j := by simpa [clock] using hc
          rw [hkj]
        | cons i v => simp at hlen
      | cons i w =>
        cases v with
        | nil => simp at hlen
        | cons t v =>
          rw [numerator, numerator, hlen] at hn
          have hm := Nat.add_right_cancel hn
          have hk1 := odd_parts (numerator_odd i w) (numerator_odd t v) hm
          have hk : k = j := by omega
          subst j
          have ht : numerator (i :: w) = numerator (t :: v) :=
            Nat.eq_of_mul_eq_mul_left (pow_pos (by decide : 0 < (2 : ℕ)) _) hm
          have hclock : clock (i :: w) = clock (t :: v) := by
            simp only [clock] at hc ⊢
            omega
          rw [ih hlen hclock ht]

/-- A residue and one ordinary interval of width 3^n fix the exact word. -/
theorem word_eq_of_bin {w v : List ℕ} {n : ℕ} (hw : w.length = n)
    (hv : v.length = n) (hc : clock w = clock v)
    (hr : numerator w % 3 ^ n = numerator v % 3 ^ n)
    (hb : numerator w / 3 ^ n = numerator v / 3 ^ n) : w = v := by
  apply word_eq_of_numerator (hw.trans hv.symm) hc
  have h₁ := Nat.mod_add_div (numerator w) (3 ^ n)
  have h₂ := Nat.mod_add_div (numerator v) (3 ^ n)
  rw [hr, hb] at h₁
  omega

/-- K consecutive possible quotient indices permit at most K gap words.
The starting quotient and ternary residue are free parameters. -/
theorem fiber_card (s : Finset (List ℕ)) (n S r lo K : ℕ)
    (h : ∀ w ∈ s, w.length = n ∧ clock w = S ∧ numerator w % 3 ^ n = r ∧
       lo ≤ numerator w / 3 ^ n ∧ numerator w / 3 ^ n < lo + K) :
    s.card ≤ K := by
  have hc : s.card ≤ (Finset.range K).card := by
    apply Finset.card_le_card_of_injOn (fun w => numerator w / 3 ^ n - lo)
    · intro w hw
      have hh := h w hw
      apply Finset.mem_range.mpr
      change numerator w / 3 ^ n - lo < K
      omega
    · intro w hw v hv he
      obtain ⟨hwl, hwc, hwr, hwlo, _⟩ := h w hw
      obtain ⟨hvl, hvc, hvr, hvlo, _⟩ := h v hv
      apply word_eq_of_bin hwl hvl (hwc.trans hvc.symm) (hwr.trans hvr.symm)
      change numerator w / 3 ^ n - lo = numerator v / 3 ^ n - lo at he
      omega
  simpa using hc

end Collatz.GapNumeratorFiber
