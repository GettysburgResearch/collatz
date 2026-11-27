import PermanentSafeOrdinary

/-! An explicit finite ordinary clock for a permanently safe suffix on every
positive odd orbit avoiding one. All bounds are inequalities of natural
numbers. The exponent loss at each group of twenty steps covers one bit. -/

namespace PermanentSafeBitClock

open PermanentSafeOrdinary

theorem weighted_step (x : Nat) (hx : 3 ≤ x) :
    81 * (3 * x + 1) ^ 4 ≤ 10000 * x ^ 4 := by
  have hbase : 3 * (3 * x + 1) ≤ 10 * x := by omega
  simpa only [mul_pow, show (3 : Nat) ^ 4 = 81 by decide,
    show (10 : Nat) ^ 4 = 10000 by decide] using Nat.pow_le_pow_left hbase 4

theorem weighted_trajectory (n : Nat) (hfloor : ∀ j, 3 ≤ state n j) (j : Nat) :
    81 ^ j * 2 ^ (4 * clock n j) * (state n j) ^ 4 ≤ 10000 ^ j * n ^ 4 := by
  induction j with
  | zero => simp [state, clock]
  | succ j ih =>
    calc
      81 ^ (j + 1) * 2 ^ (4 * clock n (j+1)) * (state n (j+1)) ^ 4 =
          (81 ^ j * 2 ^ (4 * clock n j)) *
            (81 * (2 ^ valuation (state n j) * oddMap (state n j)) ^ 4) := by
              simp only [clock, state, pow_succ 81, mul_add, pow_add, mul_pow, ← pow_mul]
              ring
      _ = (81 ^ j * 2 ^ (4 * clock n j)) * (81 * (3 * state n j + 1) ^ 4) := by
        rw [exact_step]
      _ ≤ (81 ^ j * 2 ^ (4 * clock n j)) * (10000 * (state n j) ^ 4) :=
        Nat.mul_le_mul_left _ (weighted_step _ (hfloor j))
      _ = 10000 * (81 ^ j * 2 ^ (4 * clock n j) * (state n j) ^ 4) := by ring
      _ ≤ 10000 * (10000 ^ j * n ^ 4) := Nat.mul_le_mul_left _ ih
      _ = 10000 ^ (j+1) * n ^ 4 := by rw [pow_succ]; ring

theorem twenty_step_gain : (10000 : Nat) ^ 20 * 2 ≤ 10368 ^ 20 := by decide +kernel

theorem group_gain (bits j : Nat) (hj : 20 * bits ≤ j) :
    10000 ^ j * 2 ^ bits ≤ 10368 ^ j := by
  obtain ⟨r, rfl⟩ := Nat.exists_eq_add_of_le hj
  calc
    10000 ^ (20 * bits + r) * 2 ^ bits =
        (10000 ^ 20 * 2) ^ bits * 10000 ^ r := by
          rw [pow_add, pow_mul, mul_pow]
          ring
    _ ≤ (10368 ^ 20) ^ bits * 10368 ^ r :=
      Nat.mul_le_mul (Nat.pow_le_pow_left twenty_step_gain bits)
        (Nat.pow_le_pow_left (by decide : 10000 ≤ 10368) r)
    _ = 10368 ^ (20 * bits + r) := by rw [pow_add, pow_mul]

theorem physical_tail (n bits j : Nat) (hn : n ≤ 2 ^ bits)
    (hfloor : ∀ k, 3 ≤ state n k) (hj : 80 * bits ≤ j) :
    4 * clock n j ≤ 7 * j := by
  have hs : 0 < (state n j) ^ 4 := Nat.pow_pos (by have := hfloor j; omega)
  have hg : 20 * (4 * bits) ≤ j := by omega
  have hpow : 81 ^ j * 2 ^ (4 * clock n j) ≤ 81 ^ j * 2 ^ (7 * j) := by
    calc
      81 ^ j * 2 ^ (4 * clock n j) ≤
          81 ^ j * 2 ^ (4 * clock n j) * (state n j) ^ 4 :=
        Nat.le_mul_of_pos_right _ hs
      _ ≤ 10000 ^ j * n ^ 4 := weighted_trajectory n hfloor j
      _ ≤ 10000 ^ j * (2 ^ bits) ^ 4 :=
        Nat.mul_le_mul_left _ (Nat.pow_le_pow_left hn 4)
      _ = 10000 ^ j * 2 ^ (4 * bits) := by rw [← pow_mul, Nat.mul_comm bits 4]
      _ ≤ 10368 ^ j := group_gain (4 * bits) j hg
      _ = 81 ^ j * 2 ^ (7 * j) := by
        rw [show (10368 : Nat) = 81 * 2 ^ 7 by decide, mul_pow, pow_mul]
  exact (Nat.pow_le_pow_iff_right (by decide : 1 < (2 : Nat))).mp
    (Nat.le_of_mul_le_mul_left hpow (Nat.pow_pos (by decide : 0 < (81 : Nat))))

theorem bounded_bad_suffix (n bits : Nat) (hn : n % 2 = 1) (hb : Bad n)
    (hsize : n ≤ 2 ^ bits) :
    ∃ t ≤ 80 * bits, PermanentlySafe (state n t) := by
  have htail : ∀ j, 80 * bits < j →
      0 ≤ PermanentSafeDebt.debt (fun k => (clock n k : Int)) j := by
    intro j hj
    have h := physical_tail n bits j hsize (bad_state_lower n hn hb) (by omega)
    dsimp [PermanentSafeDebt.debt]
    omega
  obtain ⟨t, ht, _, hsafe⟩ := PermanentSafeDebt.bounded_safe_suffix
    (fun k => (clock n k : Int)) (80 * bits) (by rfl) htail
  refine ⟨t, ht, ?_⟩
  intro j
  have h := hsafe j
  change 4 * ((clock n (t+j) : Int) - (clock n t : Int)) ≤ 7 * (j : Int) at h
  rw [clock_add, Nat.cast_add] at h
  omega

noncomputable def firstBadSuffix (n : Nat) (hn : n % 2 = 1) (hb : Bad n) : Nat := by
  classical
  exact Nat.find (bad_has_safe_suffix n hn hb)

theorem first_bad_suffix_safe (n : Nat) (hn : n % 2 = 1) (hb : Bad n) :
    PermanentlySafe (state n (firstBadSuffix n hn hb)) := by
  classical
  exact Nat.find_spec (bad_has_safe_suffix n hn hb)

theorem first_bad_suffix_minimal (n t : Nat) (hn : n % 2 = 1) (hb : Bad n)
    (ht : PermanentlySafe (state n t)) : firstBadSuffix n hn hb ≤ t := by
  classical
  exact Nat.find_min' (p := fun j => PermanentlySafe (state n j))
    (bad_has_safe_suffix n hn hb) ht

theorem first_bad_suffix_bits (n bits : Nat) (hn : n % 2 = 1) (hb : Bad n)
    (hsize : n ≤ 2 ^ bits) : firstBadSuffix n hn hb ≤ 80 * bits := by
  obtain ⟨t, ht, hsafe⟩ := bounded_bad_suffix n bits hn hb hsize
  exact (first_bad_suffix_minimal n t hn hb hsafe).trans ht

theorem bad_iff_bounded_safe_suffix (n : Nat) (hn : n % 2 = 1) :
    Bad n ↔ ∃ t ≤ 80 * (n.log2 + 1), PermanentlySafe (state n t) := by
  constructor
  · intro hb
    exact bounded_bad_suffix n (n.log2+1) hn hb (Nat.le_of_lt Nat.lt_log2_self)
  · rintro ⟨t, _, h⟩
    exact safe_suffix_implies_bad n t h

end PermanentSafeBitClock

#print axioms PermanentSafeBitClock.weighted_step
#print axioms PermanentSafeBitClock.weighted_trajectory
#print axioms PermanentSafeBitClock.twenty_step_gain
#print axioms PermanentSafeBitClock.group_gain
#print axioms PermanentSafeBitClock.physical_tail
#print axioms PermanentSafeBitClock.bounded_bad_suffix
#print axioms PermanentSafeBitClock.first_bad_suffix_safe
#print axioms PermanentSafeBitClock.first_bad_suffix_minimal
#print axioms PermanentSafeBitClock.first_bad_suffix_bits
#print axioms PermanentSafeBitClock.bad_iff_bounded_safe_suffix
