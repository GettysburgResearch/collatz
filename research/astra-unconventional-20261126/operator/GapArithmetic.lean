import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Finite arithmetic kernels for the gap count. The list in 'offset' is
written with its last chronological departure at the head. -/

namespace Collatz.GapArithmetic

set_option autoImplicit false

def offset : List Bool → ℕ
  | [] => 0
  | false :: w => offset w
  | true :: w => 3 * offset w + 2 ^ w.length

private theorem two_pow_unit (n : ℕ) : ¬ (3 ∣ 2^n) := by
  intro h
  have hprime : Nat.Prime 3 := by decide
  have hh := hprime.dvd_of_dvd_pow h
  omega

/-- A word with positive affine offset has a ternary unit as its offset. -/
theorem offset_unit (w : List Bool) (h : 0 < offset w) : ¬ (3 ∣ offset w) := by
  induction w with
  | nil => simp [offset] at h
  | cons e w ih =>
    cases e with
    | false => exact ih h
    | true =>
      intro hd
      change 3 ∣ 3 * offset w + 2^w.length at hd
      exact two_pow_unit w.length (by omega)

/-- If a nonempty-active pair of word offsets cancels, the normalized rank
is zero. Here u and v are its two nonnegative rank exponents. -/
theorem zero_offset_rank {u v : ℕ} (x y : List Bool)
    (norm : min u v = 0) (act : 0 < offset x ∨ 0 < offset y)
    (h : 3^u * offset y = 3^v * offset x) : u = 0 ∧ v = 0 := by
  have hx : 0 < offset x := by
    by_contra! he
    have hzero : offset x = 0 := by omega
    have hy : offset y = 0 := by
      have hb : 3^u * offset y = 0 := by simpa only [hzero, Nat.mul_zero] using h
      exact (Nat.mul_eq_zero.mp hb).resolve_left (by positivity)
    omega
  have hy : 0 < offset y := by
    by_contra! he
    have hzero : offset y = 0 := by omega
    have hb : 0 = 3^v * offset x := by simpa only [hzero, Nat.mul_zero] using h
    have hpos : 0 < 3^v * offset x := by positivity
    omega
  rcases Nat.min_eq_zero_iff.mp norm with hu | hv
  · refine ⟨hu, ?_⟩
    by_contra hh
    obtain ⟨k, hk⟩ := Nat.exists_eq_succ_of_ne_zero hh
    rw [hu, pow_zero, one_mul, hk, pow_succ] at h
    exact offset_unit y hy ⟨3^k * offset x, by rw [h]; ring⟩
  · refine ⟨?_, hv⟩
    by_contra hh
    obtain ⟨k, hk⟩ := Nat.exists_eq_succ_of_ne_zero hh
    rw [hv, pow_zero, one_mul, hk, pow_succ] at h
    exact offset_unit x hx ⟨3^k * offset y, by rw [← h]; ring⟩

/-- Deep divisibility at both ends of a subword forces the same divisibility
of its additive term. This is the integer alternative to the logarithm bound. -/
theorem deep_ends {H L j : ℕ} {a b d : ℤ} (ha : (2 : ℤ)^L ∣ a)
    (hb : (2 : ℤ)^L ∣ b) (update : 2^H*b = 3^j*a+d) : (2 : ℤ)^L ∣ d := by
  obtain ⟨u, hu⟩ := ha
  obtain ⟨v, hv⟩ := hb
  refine ⟨2^H*v-3^j*u, ?_⟩
  rw [hu, hv] at update
  linear_combination -update

/-- A complementary stretch, recording only its actual magnitude inequalities
and the number of active clocks. Idle clocks may occur arbitrarily often. -/
inductive Stretch (R : ℕ) : ℕ → ℕ → ℕ → Prop
  | nil (x : ℕ) : Stretch R 0 x x
  | idle {k x y z : ℕ} : Stretch R k x y → z ≤ y → Stretch R k x z
  | active {k x y z : ℕ} : Stretch R k x y → z ≤ 2*y+3^R → Stretch R (k+1) x z

private theorem stretch_shift {R k x y : ℕ} (trace : Stretch R k x y) :
    y + 3^R ≤ 2^k * (x + 3^R) := by
  induction trace with
  | nil => simp
  | idle _ hz ih => omega
  | @active k x y z _ hz ih =>
    rw [pow_succ]
    calc
      z + 3^R ≤ 2 * (y + 3^R) := by omega
      _ ≤ 2 * (2^k * (x+3^R)) := by omega
      _ = _ := by ring

/-- If k active clocks start at rank zero or one, all their ranks have
magnitude at most k+1. The looser numerical base 24 suffices here. -/
theorem excursion_growth {k x y : ℕ} (hx : 1 ≤ x) (trace : Stretch (k+1) k x y) :
    y ≤ 24^k * x := by
  have hs := stretch_shift trace
  by_cases hk : k = 0
  · subst k
    simp only [zero_add, pow_one, pow_zero, one_mul] at hs ⊢
    omega
  have h4 : 4 ≤ 4^k := by
    simpa using (Nat.pow_le_pow_right (by decide : 0 < 4) (by omega : 1 ≤ k))
  have h3 : 1 ≤ 3^k := Nat.one_le_pow _ _ (by decide)
  have hb : 1+3^(k+1) ≤ 4^k * 3^k := by
    rw [pow_succ]
    nlinarith [Nat.mul_le_mul_right (3^k) h4]
  calc
    y ≤ 2^k * (x+3^(k+1)) := by omega
    _ ≤ 2^k * ((1+3^(k+1))*x) := by
      apply Nat.mul_le_mul_left
      nlinarith [Nat.mul_le_mul_left (3^(k+1)) hx]
    _ ≤ 2^k * (4^k * 3^k * x) :=
      Nat.mul_le_mul_left _ (Nat.mul_le_mul_right x hb)
    _ = 24^k * x := by rw [← Nat.mul_assoc, ← Nat.mul_assoc, ← mul_pow, ← mul_pow]; norm_num

/-- Concatenate complementary excursions with actual rank-zero common clocks.
The last three indices count common clocks, odd ones among them, and active
clocks in the complementary pieces. -/
inductive Pieces : ℕ → ℕ → ℕ → ℕ → ℕ → Prop
  | nil (x : ℕ) : Pieces x x 0 0 0
  | hold {x y z h e k b : ℕ} :
      Pieces x y h e k → 2*z=3^b*y → Pieces x z (h+1) (e+b) k
  | excursion {x y z h e k j : ℕ} :
      Pieces x y h e k → 1 ≤ y → Stretch (j+1) j y z → Pieces x z h e (k+j)

/-- The total time at rank zero is bounded even under arbitrarily many
reentries, with no bound on the lengths of intervening excursions. -/
theorem rank_zero_amortization {x y h e k : ℕ} (p : Pieces x y h e k) :
    2^h*y ≤ 3^e*24^k*x := by
  induction p with
  | nil => simp
  | @hold y z h e k b _ edge ih =>
    calc
      2^(h+1)*z = 3^b * (2^h*y) := by rw [pow_succ]; nlinarith [congrArg (fun n : ℕ => 2^h*n) edge]
      _ ≤ 3^b * (3^e*24^k*x) := Nat.mul_le_mul_left _ ih
      _ = _ := by rw [pow_add]; ring
  | @excursion y z h e k j _ hy trace ih =>
    calc
      2^h*z ≤ 2^h*(24^j*y) := Nat.mul_le_mul_left _ (excursion_growth hy trace)
      _ = 24^j*(2^h*y) := by ring
      _ ≤ 24^j*(3^e*24^k*x) := Nat.mul_le_mul_left _ ih
      _ = _ := by rw [pow_add]; ring

end Collatz.GapArithmetic

#print axioms Collatz.GapArithmetic.offset_unit
#print axioms Collatz.GapArithmetic.zero_offset_rank
#print axioms Collatz.GapArithmetic.deep_ends
#print axioms Collatz.GapArithmetic.excursion_growth
#print axioms Collatz.GapArithmetic.rank_zero_amortization
