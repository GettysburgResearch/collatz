import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! Round 11 finite arithmetic candidate. Compiler replay is pending.
    No assertion of arbitrary-source realization or Collatz convergence. -/
namespace Collatz.FixedSourceRepetition
set_option autoImplicit false

def denom (b : Bool) : ℕ := if b then 32 else 8
def carry (b : Bool) : ℕ := if b then 5 else 7
def Edge (b : Bool) (q r : ℕ) : Prop := denom b * r = 9 * q + carry b

def extra (s : ℕ → Bool) : ℕ → ℕ
  | 0 => 1
  | n + 1 => extra s n * (if s n then 4 else 1)

def wordDen (s : ℕ → Bool) (m : ℕ) : ℕ := 8 ^ m * extra s m

theorem wordDen_succ (s : ℕ → Bool) (m : ℕ) :
    wordDen s (m + 1) = wordDen s m * denom (s m) := by
  cases hs : s m <;> simp [wordDen, extra, denom, hs, pow_succ] <;> ring

/-- The complete additive carry cancels, without identifying the source states. -/
theorem aligned (q r : ℕ → ℕ) (s : ℕ → Bool) (m : ℕ)
    (hq : ∀ i < m, Edge (s i) (q i) (q (i + 1)))
    (hr : ∀ i < m, Edge (s i) (r i) (r (i + 1))) :
    wordDen s m * r m + 9 ^ m * q 0 =
      wordDen s m * q m + 9 ^ m * r 0 := by
  induction m with
  | zero => simp [wordDen, extra, Nat.add_comm]
  | succ m ih =>
    have h := ih (fun i hi => hq i (by omega)) (fun i hi => hr i (by omega))
    have hq' : denom (s m) * q (m + 1) = 9 * q m + carry (s m) := hq m (by omega)
    have hr' : denom (s m) * r (m + 1) = 9 * r m + carry (s m) := hr m (by omega)
    calc
      wordDen s (m + 1) * r (m + 1) + 9 ^ (m + 1) * q 0 =
          wordDen s m * (denom (s m) * r (m + 1)) + 9 * (9 ^ m * q 0) := by
            rw [wordDen_succ, pow_succ]; ring
      _ = wordDen s m * (9 * r m + carry (s m)) + 9 * (9 ^ m * q 0) := by rw [hr']
      _ = 9 * (wordDen s m * r m + 9 ^ m * q 0) + wordDen s m * carry (s m) := by ring
      _ = 9 * (wordDen s m * q m + 9 ^ m * r 0) + wordDen s m * carry (s m) := by rw [h]
      _ = wordDen s m * (9 * q m + carry (s m)) + 9 * (9 ^ m * r 0) := by ring
      _ = wordDen s m * (denom (s m) * q (m + 1)) + 9 * (9 ^ m * r 0) := by rw [hq']
      _ = wordDen s (m + 1) * q (m + 1) + 9 ^ (m + 1) * r 0 := by
            rw [wordDen_succ, pow_succ]; ring

theorem difference_dvd (q r : ℕ → ℕ) (s : ℕ → Bool) (m : ℕ)
    (hq : ∀ i < m, Edge (s i) (q i) (q (i + 1)))
    (hr : ∀ i < m, Edge (s i) (r i) (r (i + 1))) :
    8 ^ m ∣ r 0 - q 0 := by
  have he := aligned q r s m hq hr
  have hd : 9 ^ m * (r 0 - q 0) = wordDen s m * (r m - q m) := by
    simp only [Nat.mul_sub_left_distrib]
    omega
  have hc : Nat.Coprime (8 ^ m) (9 ^ m) :=
    ((show Nat.Coprime 8 9 by decide).pow_left _).pow_right _
  apply hc.dvd_mul_left.mp
  refine ⟨extra s m * (r m - q m), ?_⟩
  rw [hd, wordDen]
  ring

theorem small_shared_word (q r : ℕ → ℕ) (s : ℕ → Bool) (m : ℕ)
    (hq : ∀ i < m, Edge (s i) (q i) (q (i + 1)))
    (hr : ∀ i < m, Edge (s i) (r i) (r (i + 1)))
    (hqs : q 0 < 8 ^ m) (hrs : r 0 < 8 ^ m) : q 0 = r 0 := by
  by_contra hn
  rcases lt_or_gt_of_ne hn with h | h
  · have hd := difference_dvd q r s m hq hr
    have hl := Nat.le_of_dvd (show 0 < r 0 - q 0 by omega) hd
    omega
  · have hd := difference_dvd r q s m hr hq
    have hl := Nat.le_of_dvd (show 0 < q 0 - r 0 by omega) hd
    omega

theorem edge_height (b : Bool) (q r : ℕ) (h : Edge b q r) :
    8 * (r + 7) ≤ 9 * (q + 7) := by
  cases b <;> simp [Edge, denom, carry] at h <;> omega

theorem prefix_height (q : ℕ → ℕ) (s : ℕ → Bool) (j : ℕ)
    (h : ∀ i < j, Edge (s i) (q i) (q (i + 1))) :
    8 ^ j * (q j + 7) ≤ 9 ^ j * (q 0 + 7) := by
  induction j with
  | zero => simp
  | succ j ih =>
    have hp := ih (fun i hi => h i (by omega))
    have hs := edge_height (s j) (q j) (q (j + 1)) (h j (by omega))
    calc
      8 ^ (j + 1) * (q (j + 1) + 7) = 8 ^ j * (8 * (q (j + 1) + 7)) := by ring
      _ ≤ 8 ^ j * (9 * (q j + 7)) := Nat.mul_le_mul_left _ hs
      _ = 9 * (8 ^ j * (q j + 7)) := by ring
      _ ≤ 9 * (9 ^ j * (q 0 + 7)) := Nat.mul_le_mul_left _ hp
      _ = 9 ^ (j + 1) * (q 0 + 7) := by ring

theorem two_start_bounds (q : ℕ → ℕ) (s : ℕ → Bool) (H : ℕ)
    (he : ∀ i < 2 * H, Edge (s i) (q i) (q (i + 1)))
    (hs : q 0 + 7 < 4 ^ H) : q H < 8 ^ H ∧ q (2 * H) < 8 ^ H := by
  have h1 := prefix_height q s H (fun i hi => he i (by omega))
  have h2 := prefix_height q s (2 * H) he
  have hp1 : (9 : ℕ) ^ H * 4 ^ H ≤ 8 ^ H * 8 ^ H := by
    simp only [← mul_pow]
    exact Nat.pow_le_pow_left (by norm_num) H
  have hp2 : (9 : ℕ) ^ (2 * H) * 4 ^ H ≤ 8 ^ (2 * H) * 8 ^ H := by
    calc
      (9 : ℕ) ^ (2 * H) * 4 ^ H = (9 ^ 2 * 4) ^ H := by rw [pow_mul, mul_pow]
      _ ≤ (8 ^ 2 * 8) ^ H := Nat.pow_le_pow_left (by norm_num) H
      _ = 8 ^ (2 * H) * 8 ^ H := by rw [mul_pow, ← pow_mul]
  have hl1 := lt_of_le_of_lt h1 (lt_of_lt_of_le (Nat.mul_lt_mul_of_pos_left hs (by positivity : 0 < 9 ^ H)) hp1)
  have hl2 := lt_of_le_of_lt h2 (lt_of_lt_of_le (Nat.mul_lt_mul_of_pos_left hs (by positivity : 0 < 9 ^ (2 * H))) hp2)
  constructor
  · by_contra! hn
    have hh := Nat.mul_le_mul_left (8 ^ H) (show 8 ^ H ≤ q H + 7 by omega)
    omega
  · by_contra! hn
    have hh := Nat.mul_le_mul_left (8 ^ (2 * H)) (show 8 ^ H ≤ q (2 * H) + 7 by omega)
    omega

/-- Matching shifted windows force equality of the actual states at their starts. -/
theorem early_repeat (q : ℕ → ℕ) (s : ℕ → Bool) (H : ℕ)
    (he : ∀ i < 3 * H, Edge (s i) (q i) (q (i + 1)))
    (hs : q 0 + 7 < 4 ^ H)
    (hm : ∀ i < H, s (H + i) = s (2 * H + i)) : q H = q (2 * H) := by
  have hb := two_start_bounds q s H (fun i hi => he i (by omega)) hs
  have hl : ∀ i < H, Edge (s (H + i)) (q (H + i)) (q (H + (i + 1))) := by
    intro i hi
    simpa [Nat.add_assoc] using he (H + i) (by omega)
  have hr : ∀ i < H, Edge (s (H + i)) (q (2 * H + i)) (q (2 * H + (i + 1))) := by
    intro i hi
    rw [hm i hi]
    simpa [Nat.add_assoc] using he (2 * H + i) (by omega)
  have h := small_shared_word (fun i => q (H + i)) (fun i => q (2 * H + i))
    (fun i => s (H + i)) H hl hr (by simpa using hb.1) (by simpa using hb.2)
  simpa using h

/-- The two literal affine branches have disjoint integer source domains. -/
theorem edge_deterministic (s t : Bool) (q r u : ℕ)
    (hs : Edge s q r) (ht : Edge t q u) : s = t ∧ r = u := by
  cases s <;> cases t <;> simp [Edge, denom, carry] at hs ht ⊢ <;> omega

theorem equal_start_future (q : ℕ → ℕ) (s : ℕ → Bool) (a b t : ℕ)
    (hab : a ≤ b) (he : ∀ i < b + t + 1, Edge (s i) (q i) (q (i + 1)))
    (h0 : q a = q b) : q (a + t) = q (b + t) ∧ s (a + t) = s (b + t) := by
  induction t with
  | zero =>
    have hl := he a (by omega)
    have hr := he b (by omega)
    rw [h0] at hl
    exact ⟨by simpa using h0, by simpa using (edge_deterministic _ _ _ _ _ hl hr).1⟩
  | succ t ih =>
    have hprev := ih (fun i hi => he i (by omega))
    have hl := he (a + t) (by omega)
    have hr := he (b + t) (by omega)
    rw [hprev.1] at hl
    have hnext : q (a + (t + 1)) = q (b + (t + 1)) := by
      simpa [Nat.add_assoc] using (edge_deterministic _ _ _ _ _ hl hr).2
    have hnl := he (a + (t + 1)) (by omega)
    have hnr := he (b + (t + 1)) (by omega)
    rw [hnext] at hnl
    exact ⟨hnext, (edge_deterministic _ _ _ _ _ hnl hnr).1⟩

/-- The finite repeat/mismatch interface for all bit-cap scripts. -/
theorem four_window_reject (q : ℕ → ℕ) (s : ℕ → Bool) (H t : ℕ)
    (he : ∀ i < 4 * H, Edge (s i) (q i) (q (i + 1)))
    (hs : q 0 + 7 < 4 ^ H)
    (hm : ∀ i < H, s (H + i) = s (2 * H + i))
    (ht : t < 2 * H) (hd : s (H + t) ≠ s (2 * H + t)) : False := by
  have h0 := early_repeat q s H (fun i hi => he i (by omega)) hs hm
  have hf := equal_start_future q s H (2 * H) t (by omega)
    (fun i hi => he i (by omega)) h0
  exact hd hf.2

end Collatz.FixedSourceRepetition

#print axioms Collatz.FixedSourceRepetition.wordDen_succ
#print axioms Collatz.FixedSourceRepetition.aligned
#print axioms Collatz.FixedSourceRepetition.difference_dvd
#print axioms Collatz.FixedSourceRepetition.small_shared_word
#print axioms Collatz.FixedSourceRepetition.edge_height
#print axioms Collatz.FixedSourceRepetition.prefix_height
#print axioms Collatz.FixedSourceRepetition.two_start_bounds
#print axioms Collatz.FixedSourceRepetition.early_repeat
#print axioms Collatz.FixedSourceRepetition.edge_deterministic
#print axioms Collatz.FixedSourceRepetition.equal_start_future
#print axioms Collatz.FixedSourceRepetition.four_window_reject
