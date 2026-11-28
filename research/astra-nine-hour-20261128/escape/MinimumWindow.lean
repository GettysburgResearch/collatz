import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! Finite occupation windows on the ordinary shortcut map. -/

namespace Collatz.MinimumWindow

def step (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def orbit : ℕ → ℕ → ℕ
  | 0, n => n
  | k + 1, n => orbit k (step n)

def count (mark : ℕ → Bool) : ℕ → ℕ → ℕ
  | 0, _ => 0
  | k + 1, n => (if mark n then 1 else 0) + count mark k (step n)

def oddMark (n : ℕ) : Bool := n % 2 == 1

theorem orbit_add (a b n : ℕ) : orbit (a+b) n = orbit b (orbit a n) := by
  induction a generalizing n with
  | zero => simp [orbit]
  | succ a ih => simpa only [Nat.succ_add, orbit] using ih (step n)

theorem count_add (f : ℕ → Bool) (a b n : ℕ) :
    count f (a+b) n = count f a n + count f b (orbit a n) := by
  induction a generalizing n with
  | zero => simp [count, orbit]
  | succ a ih => simp only [Nat.succ_add, count, orbit, ih, Nat.add_assoc]

theorem count_le (f : ℕ → Bool) (k n : ℕ) : count f k n ≤ k := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih =>
    have h := ih (step n)
    simp only [count]
    split <;> omega

/-- Delaying a window by d loses or adds at most d marked states. -/
theorem slide (f : ℕ → Bool) (h d n : ℕ) :
    count f h n ≤ count f h (orbit d n) + d ∧
    count f h (orbit d n) ≤ count f h n + d := by
  have h₁ := count_add f d h n
  have h₂ := count_add f h d n
  have h₃ := count_le f d n
  have h₄ := count_le f d (orbit h n)
  rw [Nat.add_comm d h] at h₁
  omega

/-- Compare the sampled window with the h-step window from the very site
actually reached at time b. The two time origins may be in either order. -/
theorem hit_window (f : ℕ → Bool) (h a b n m : ℕ) (hit : orbit b n = m) :
    count f h (orbit a n) ≤ count f h m + (a-b) + (b-a) ∧
    count f h m ≤ count f h (orbit a n) + (a-b) + (b-a) := by
  subst m
  by_cases hab : a ≤ b
  · obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le hab
    rw [orbit_add]
    have hc := slide f h d (orbit a n)
    omega
  · obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le (Nat.le_of_not_ge hab)
    rw [orbit_add]
    have hc := slide f h d (orbit b n)
    omega

private theorem local_power (n : ℕ) (hn : 3 ≤ n) :
    16 * (step n)^4 ≤ 2^(7 * (if oddMark n then 1 else 0)) * n^4 := by
  by_cases he : n % 2 = 0
  · have h : 2 * (n/2) = n := by omega
    simp [step, he, oddMark]
    calc
      16 * (n/2)^4 = (2*(n/2))^4 := by ring
      _ = n^4 := by rw [h]
      _ ≤ _ := by simp
  · have ho : n % 2 = 1 := by omega
    have h : 2 * ((3*n+1)/2) = 3*n+1 := by omega
    have hscale : 3 * (3*n+1) ≤ 10*n := by omega
    have hp := Nat.pow_le_pow_left hscale 4
    have hc : (3*n+1)^4 ≤ 128*n^4 := by
      rw [mul_pow, mul_pow] at hp
      norm_num at hp ⊢
      omega
    simp [step, oddMark, ho]
    calc
      16 * ((3*n+1)/2)^4 = (2*((3*n+1)/2))^4 := by ring
      _ = (3*n+1)^4 := by rw [h]
      _ ≤ _ := by simpa using hc

/-- The gate used in PR213, here in a standalone finite-window proof. -/
theorem path_power (k n : ℕ) (above : ∀ i < k, 3 ≤ orbit i n) :
    2^(4*k) * (orbit k n)^4 ≤ 2^(7 * count oddMark k n) * n^4 := by
  induction k generalizing n with
  | zero => simp [orbit, count]
  | succ k ih =>
    have hn : 3 ≤ n := above 0 (by omega)
    have hstep := local_power n hn
    have htail := ih (step n) (fun i hi => above (i+1) (by omega))
    simp only [count, orbit, Nat.mul_add, pow_add, Nat.mul_succ]
    calc
      2^(4*k) * 2^4 * (orbit k (step n))^4 =
          16 * (2^(4*k) * (orbit k (step n))^4) := by ring
      _ ≤ 16 * (2^(7 * count oddMark k (step n)) * (step n)^4) :=
        Nat.mul_le_mul_left _ htail
      _ = 2^(7 * count oddMark k (step n)) * (16 * (step n)^4) := by ring
      _ ≤ 2^(7 * count oddMark k (step n)) *
          (2^(7 * (if oddMark n then 1 else 0)) * n^4) := Nat.mul_le_mul_left _ hstep
      _ = _ := by ring

theorem minimum_prefix (m k : ℕ) (hm : 3 ≤ m) (least : ∀ i, m ≤ orbit i m) :
    4*k ≤ 7 * count oddMark k m := by
  have h := path_power k m (fun i _ => hm.trans (least i))
  have hlo := Nat.mul_le_mul_left (2^(4*k)) (Nat.pow_le_pow_left (least k) 4)
  have hpos : 0 < m^4 := by positivity
  have hpow := Nat.le_of_mul_le_mul_right (hlo.trans h) hpos
  exact (Nat.pow_le_pow_iff_right (by decide : 1 < 2)).mp hpow

theorem minimum_window (h a b n m : ℕ) (hit : orbit b n = m) (hm : 3 ≤ m)
    (least : ∀ i, m ≤ orbit i m) :
    4*h ≤ 7 * count oddMark h (orbit a n) + 7*((a-b)+(b-a)) := by
  have hp := minimum_prefix m h hm least
  have hw := (hit_window oddMark h a b n m hit).2
  omega

#print axioms hit_window
#print axioms path_power
#print axioms minimum_window

end Collatz.MinimumWindow
