/-
Global proof development at the adjacent-pair boundary of the psi shadow.

These theorems do not prove OpenLemma.  They make one source-tail induction
step exact and show how the whole initial basin interval discharges its
even-exponent branch.  The odd-exponent branch remains an explicit residual.
-/
import Collatz.Shadow

open CollatzReverseBasin CollatzClosure

namespace CollatzPsiCompletion

def InitialBasin (n : Nat) : Prop :=
  ∀ j : Nat, 0 < j → j < n → Basin j

def LeastMissing (n : Nat) : Prop :=
  0 < n ∧ ¬ Basin n ∧ InitialBasin n

/-- One ordinary step of the odd member of an adjacent pair. -/
theorem basin_adjacent (u : Nat) : Basin (2*u+1) ↔ Basin (3*u+2) := by
  have hs : shortcut (2*u+1) = 3*u+2 := by
    unfold shortcut
    split <;> omega
  rw [← hs]
  exact (basin_step _).symm

/-- An even number of factors two in the adjacent source preserves the
adjacent type after replacing those factors by factors three. -/
theorem adjacent_source_four_power (d v : Nat) :
    Basin (2*(4^d*v)+1) ↔ Basin (2*(3^d*v)+1) := by
  have h := basin_pow_four_succ d (2*v)
  have he4 : 4^d*(2*v)+1 = 2*(4^d*v)+1 := by grind
  have he3 : 3^d*(2*v)+1 = 2*(3^d*v)+1 := by grind
  rwa [he4, he3] at h

/-- An odd number of factors two in the adjacent source removes the
adjacent type entirely. -/
theorem adjacent_source_twice_four_power (d v : Nat) (hv : v % 2 = 1) :
    Basin (2*(2*4^d*v)+1) ↔ Basin (3^d*v) := by
  have h1 := basin_pow_four_succ (d+1) v
  have he4 : 4^(d+1)*v+1 = 2*(2*4^d*v)+1 := by grind
  have he3 : 3^(d+1)*v+1 = 3*(3^d*v)+1 := by grind
  rw [he4, he3] at h1
  have hodd : (3^d*v) % 2 = 1 := by rw [Nat.mul_mod, three_pow_odd, hv]
  exact h1.trans (basin_odd _ hodd)

private theorem three_power_le_four_power (d : Nat) : 3^d ≤ 4^d := by
  induction d with
  | zero => decide
  | succ d ih =>
    rw [Nat.pow_succ, Nat.pow_succ]
    omega

private theorem odd_decomposition (u : Nat) (hu : 0 < u) :
    ∃ b v : Nat, v % 2 = 1 ∧ u = 2^b*v := by
  induction u using Nat.strong_induction_on with
  | h u ih =>
    rcases Nat.mod_two_eq_zero_or_one u with he | ho
    · have hp : 0 < u/2 := by omega
      obtain ⟨b, v, hv, huv⟩ := ih (u/2) (by omega) hp
      refine ⟨b+1, v, hv, ?_⟩
      have e : u = 2*(u/2) := by omega
      rw [e, huv, Nat.pow_succ]
      grind
    · exact ⟨0, u, ho, by simp⟩

/-- This covers every positive adjacent source, including even ones: if its
odd partner is missing while the initial interval is known, normalization
produces an odd known source no larger than the starting source. -/
theorem normalize_adjacent_below (n u : Nat) (hn : InitialBasin n)
    (hup : 0 < u) (hul : u < n) (hbad : ¬ Basin (2*u+1)) :
    ∃ w : Nat, w % 2 = 1 ∧ w ≤ u ∧ Basin w ∧ ¬ Basin (2*w+1) := by
  obtain ⟨b, v, hv, heq⟩ := odd_decomposition u hup
  have hvp : 0 < v := by omega
  rcases Nat.mod_two_eq_zero_or_one b with he | ho
  · let d := b/2
    have heb : b = 2*d := by dsimp [d]; omega
    have heu : u = 4^d*v := by
      rw [heq, heb, Nat.pow_mul]
    have hw : 3^d*v ≤ u := by
      rw [heu]
      exact Nat.mul_le_mul_right v (three_power_le_four_power d)
    have hwp : 0 < 3^d*v := Nat.mul_pos (Nat.pow_pos (by omega)) hvp
    have hwo : (3^d*v) % 2 = 1 := by rw [Nat.mul_mod, three_pow_odd, hv]
    refine ⟨3^d*v, hwo, hw, hn _ hwp (Nat.lt_of_le_of_lt hw hul), ?_⟩
    intro hb
    apply hbad
    rw [heu]
    exact (adjacent_source_four_power d v).mpr hb
  · let d := b/2
    have heb : b = 2*d+1 := by dsimp [d]; omega
    have heu : u = 2*4^d*v := by
      rw [heq, heb, Nat.pow_succ, Nat.pow_mul]
      grind
    have hw0 : 3^d*v ≤ 4^d*v :=
      Nat.mul_le_mul_right v (three_power_le_four_power d)
    have he2 : 2*4^d*v = 2*(4^d*v) := by grind
    have hw : 3^d*v ≤ u := by rw [heu, he2]; omega
    have hwp : 0 < 3^d*v := Nat.mul_pos (Nat.pow_pos (by omega)) hvp
    have hb := hn (3^d*v) hwp (Nat.lt_of_le_of_lt hw hul)
    apply False.elim
    apply hbad
    rw [heu]
    exact (adjacent_source_twice_four_power d v hv).mpr hb

/-- Even-exponent source-tail normal form.  Together with the odd form this
partitions positive accelerated exponents, after normalizing an even source. -/
theorem adjacent_even_tail (d u t : Nat) (ht : t % 2 = 1)
    (h : 3*u+1 = 4^(d+1)*t) :
    Basin (2*u+1) ↔ Basin (3^d*t) := by
  have h1 := basin_adjacent u
  have he : 3*u+2 = 4^(d+1)*t+1 := by omega
  rw [he] at h1
  have h2 := basin_pow_four_succ (d+1) t
  have he2 : 3^(d+1)*t+1 = 3*(3^d*t)+1 := by grind
  rw [he2] at h2
  have hodd : (3^d*t) % 2 = 1 := by
    rw [Nat.mul_mod, three_pow_odd, ht]
  exact (h1.trans h2).trans (basin_odd _ hodd)

/-- Odd-exponent source-tail normal form. -/
theorem adjacent_odd_tail (d u t : Nat)
    (h : 3*u+1 = 2*4^d*t) :
    Basin (2*u+1) ↔ Basin (2*(3^d*t)+1) := by
  have h1 := basin_adjacent u
  have he : 3*u+2 = 4^d*(2*t)+1 := by grind
  rw [he] at h1
  have h2 := basin_pow_four_succ d (2*t)
  have he2 : 3^d*(2*t)+1 = 2*(3^d*t)+1 := by grind
  rw [he2] at h2
  exact h1.trans h2

private theorem powers_gap (d : Nat) : 3*3^d+1 ≤ 4^(d+1) := by
  induction d with
  | zero => decide
  | succ d ih =>
    have e3 : 3^(d+1) = 3*3^d := by grind
    have e4 : 4^(d+1+1) = 4*4^(d+1) := by grind
    change 3*3^(d+1)+1 ≤ 4^(d+1+1)
    rw [e3, e4]
    omega

/-- The even-branch residual never exceeds its source. -/
theorem even_tail_le_source (d u t : Nat) (ht : 0 < t)
    (h : 3*u+1 = 4^(d+1)*t) : 3^d*t ≤ u := by
  have hb := Nat.mul_le_mul_right t (powers_gap d)
  have he : (3*3^d+1)*t = 3*(3^d*t)+t := by grind
  rw [he, ← h] at hb
  omega

/-- The whole initial basin interval closes every even source exponent. -/
theorem initial_basin_even_tail (n d u t : Nat) (hn : InitialBasin n)
    (hu : u < n) (ht : t % 2 = 1) (h : 3*u+1 = 4^(d+1)*t) :
    Basin (2*u+1) := by
  have htpos : 0 < t := by omega
  have hzpos : 0 < 3^d*t := Nat.mul_pos (Nat.pow_pos (by omega)) htpos
  have hzlt : 3^d*t < n := Nat.lt_of_le_of_lt (even_tail_le_source d u t htpos h) hu
  exact (adjacent_even_tail d u t ht h).mpr (hn _ hzpos hzlt)

/-- A least missing positive integer lies in the only unresolved parity branch. -/
theorem least_missing_mod_four (n : Nat) (hn : LeastMissing n) : n % 4 = 3 := by
  rcases hn with ⟨hnpos, hbad, hsmall⟩
  have hne1 : n ≠ 1 := by
    intro h
    subst n
    exact hbad ⟨0, rfl⟩
  have hodd : n % 2 = 1 := by
    rcases Nat.mod_two_eq_zero_or_one n with he | ho
    · have hb : Basin (n/2) := hsmall _ (by omega) (by omega)
      have heq : n = 2*(n/2) := by omega
      apply False.elim
      apply hbad
      rw [heq]
      exact (basin_twice _).mpr hb
    · exact ho
  have hne : n % 4 ≠ 1 := by
    intro hm
    have heq : n = 4*(n/4)+1 := by omega
    have hb : Basin (3*(n/4)+1) := hsmall _ (by omega) (by omega)
    exact hbad ((basin_exch n (3*(n/4)+1) (n/4) heq rfl).mpr hb)
  omega

/-- Minimality supplies a known source below the missing number, but its adjacent
odd partner is missing.  This is the zero-exponent boundary of Shadow. -/
theorem least_missing_adjacent (n : Nat) (hn : LeastMissing n) :
    ∃ u : Nat, 0 < u ∧ u < n ∧ 3*n = 4*u+1 ∧
      Basin u ∧ ¬ Basin (2*u+1) := by
  have hm := least_missing_mod_four n hn
  rcases hn with ⟨hnpos, hbad, hsmall⟩
  let q := n/4
  have heq : n = 4*q+3 := by dsimp [q]; omega
  let u := 3*q+2
  have hup : 0 < u := by dsimp [u]; omega
  have hul : u < n := by dsimp [u]; omega
  have hu : 3*n = 4*u+1 := by dsimp [u]; omega
  have hs : shortcut n = 2*u+1 := by
    unfold shortcut
    dsimp [u]
    split <;> omega
  refine ⟨u, hup, hul, hu, hsmall u hup hul, ?_⟩
  intro hb
  rw [← hs] at hb
  exact hbad ((basin_step n).mp hb)

/-- Hence a source below the first missing number cannot have an even
accelerated exponent when its adjacent odd partner is missing. -/
theorem missing_adjacent_no_even_tail (n u : Nat) (hn : InitialBasin n)
    (hu : u < n) (hbad : ¬ Basin (2*u+1)) :
    ∀ d t : Nat, t % 2 = 1 → 3*u+1 ≠ 4^(d+1)*t := by
  intro d t ht h
  exact hbad (initial_basin_even_tail n d u t hn hu ht h)

end CollatzPsiCompletion
