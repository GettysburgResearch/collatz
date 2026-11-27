import Std

namespace Collatz.TraceClocks

def iter (f : Nat → Nat) : Nat → Nat → Nat
  | 0, n => n
  | t + 1, n => iter f t (f n)

private theorem iter_add (f : Nat → Nat) (s t n : Nat) :
    iter f (s + t) n = iter f t (iter f s n) := by
  induction s generalizing n with
  | zero => simp [iter]
  | succ s ih => rw [Nat.succ_add]; exact ih (f n)

/-- The partner's clock is completely unrestricted, including when its orbit
escapes. This applies at a realized stopping time by substituting its value. -/
theorem prefix_meets_trace_iff (f : Nat → Nat) (x y h : Nat) :
    (∃ i ≤ h, ∃ k, iter f i x = iter f k y) ↔
      ∃ l, iter f h x = iter f l y := by
  constructor
  · rintro ⟨i, hi, k, he⟩
    obtain ⟨d, hd⟩ := Nat.exists_eq_add_of_le hi
    exact ⟨k + d, by rw [hd, iter_add, he, iter_add]⟩
  · rintro ⟨l, he⟩
    exact ⟨h, Nat.le_refl h, l, he⟩

def fast (n : Nat) : Nat := if n % 2 = 0 then n / 2 else (3*n+1)/2

def slow (n : Nat) : Nat := if n % 2 = 0 then n / 2 else 3*n+1

def odds : Nat → Nat → Nat
  | 0, _ => 0
  | t+1, n => n % 2 + odds t (fast n)

private theorem one_step (n : Nat) : iter slow (1 + n % 2) n = fast n := by
  rcases (show n%2 = 0 ∨ n%2 = 1 by omega) with h|h
  · simp [h, iter, slow, fast]
  · have he : (3*n+1)%2 = 0 := by omega
    simp [h, iter, slow, fast, he]

/-- Exact conversion of a physical shortcut clock including every grouped odd
branch. Real-valued drift and stopping-time bounds are separate. -/
theorem slow_at_shortcut_clock (n t : Nat) :
    iter slow (t + odds t n) n = iter fast t n := by
  induction t generalizing n with
  | zero => simp [iter, odds]
  | succ t ih =>
    have ha : t + 1 + odds (t+1) n = (1 + n%2) + (t + odds t (fast n)) := by
      simp only [odds]; omega
    rw [ha, iter_add, one_step, ih, iter]

/-- Every ordinary hit at an odd target is a shortcut-clock endpoint, with
its exact ordinary time. No endpoint claim is needed for skipped even states. -/
theorem odd_hit_has_shortcut_clock (n s y : Nat) (hy : y % 2 = 1)
    (hit : iter slow s n = y) :
    ∃ t, t + odds t n = s ∧ iter fast t n = y := by
  induction s using Nat.strongRecOn generalizing n with
  | ind s ih =>
    cases s with
    | zero => exact ⟨0, rfl, hit⟩
    | succ s =>
      rcases (show n%2=0 ∨ n%2=1 by omega) with hn|hn
      · have eq : slow n = fast n := by simp [slow, fast, hn]
        obtain ⟨t, ht, he⟩ := ih s (by omega) (fast n) (by simpa [iter, eq] using hit)
        exact ⟨t+1, by simp only [odds, hn, Nat.zero_add]; omega, he⟩
      · cases s with
        | zero =>
          have e : 3*n+1=y := by simpa [iter, slow, hn] using hit
          omega
        | succ s =>
          have eq : iter slow 2 n = fast n := by simpa [hn] using one_step n
          have hl : iter slow s (fast n) = y := by
            rw [← eq, ← iter_add]
            rw [show 2+s = s+1+1 by omega]
            exact hit
          obtain ⟨t, ht, he⟩ := ih s (by omega) (fast n) hl
          exact ⟨t+1, by simp only [odds, hn]; omega, he⟩

#print axioms prefix_meets_trace_iff
#print axioms slow_at_shortcut_clock
#print axioms odd_hit_has_shortcut_clock

end Collatz.TraceClocks
