import Collatz.Closure

/-!
# Exact positive correction normalization

No global convergence hypothesis is used here. The main result proves that a
single positive affine word identity determines an actual odd Collatz path;
the companion head theorem proves that changing proposed rank and clock budgets
does not create a choice of the next odd exponent.
-/

open CollatzReverseBasin CollatzClosure

namespace CollatzCorrection

def Equation (n q r A B : Nat) : Prop :=
  2 ^ A * q = 3 ^ r * n + B

def OddStep (n a q : Nat) : Prop :=
  0 < a ∧ n % 2 = 1 ∧ q % 2 = 1 ∧ 2 ^ a * q = 3 * n + 1

def clock : List Nat → Nat
  | [] => 0
  | a :: w => a + clock w

def correction : List Nat → Nat
  | [] => 0
  | a :: w => 3 ^ w.length + 2 ^ a * correction w

def Legal (w : List Nat) : Prop := ∀ a ∈ w, 0 < a

inductive Path : Nat → Nat → List Nat → Prop
  | nil (n : Nat) : Path n n []
  | cons {n q z a : Nat} {w : List Nat} :
      OddStep n a q → Path q z w → Path n z (a :: w)

theorem pow_two_even {a : Nat} (ha : 0 < a) : 2 ^ a % 2 = 0 := by
  obtain ⟨b, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt ha)
  simp [Nat.pow_succ]

theorem odd_quotient_unique {a b q r : Nat}
    (hq : q % 2 = 1) (hr : r % 2 = 1)
    (h : 2 ^ a * q = 2 ^ b * r) : a = b ∧ q = r := by
  induction a generalizing b with
  | zero =>
    cases b with
    | zero => simpa using h
    | succ b =>
      have hm := congrArg (fun n : Nat => n % 2) h
      simp [Nat.pow_succ, Nat.mul_mod, hq] at hm
  | succ a ih =>
    cases b with
    | zero =>
      have hm := congrArg (fun n : Nat => n % 2) h
      simp [Nat.pow_succ, Nat.mul_mod, hr] at hm
    | succ b =>
      have h' : 2 ^ a * q = 2 ^ b * r := by
        rw [Nat.pow_succ, Nat.pow_succ] at h
        have hh : 2 * (2 ^ a * q) = 2 * (2 ^ b * r) := by grind
        exact Nat.eq_of_mul_eq_mul_left (by omega) hh
      obtain ⟨hab, hqr⟩ := ih h'
      exact ⟨by omega, hqr⟩

theorem odd_step_unique {n a b q r : Nat}
    (h : OddStep n a q) (g : OddStep n b r) : a = b ∧ q = r :=
  odd_quotient_unique h.2.2.1 g.2.2.1 (h.2.2.2.trans g.2.2.2.symm)

/-- Peeling a valid head cancels every prospective target rank and clock budget. -/
theorem peel_exact (n q z r a d C : Nat)
    (step : 2 ^ a * q = 3 * n + 1) :
    Equation n z (r + 1) (a + d) (3 ^ r + 2 ^ a * C) ↔
      Equation q z r d C := by
  unfold Equation
  have e : 3 ^ (r + 1) * n + (3 ^ r + 2 ^ a * C) =
      2 ^ a * (3 ^ r * q + C) := by
    rw [Nat.pow_succ]
    grind
  rw [e, Nat.pow_add]
  rw [Nat.mul_assoc]
  exact Nat.mul_left_cancel_iff (Nat.pow_pos (by omega))

/-- A positive correction head forces the exact next ordinary odd step. -/
theorem head_forced {n z r a d C : Nat} (ha : 0 < a)
    (parity : (2 ^ d * z + C) % 2 = 1)
    (enc : Equation n z (r + 1) (a + d) (3 ^ r + 2 ^ a * C)) :
    ∃ q, OddStep n a q ∧ Equation q z r d C := by
  have e : 2 ^ a * (2 ^ d * z) =
      3 ^ r * (3 * n + 1) + 2 ^ a * C := by
    unfold Equation at enc
    rw [Nat.pow_add, Nat.pow_succ] at enc
    grind
  have hd : 2 ^ a ∣ 3 ^ r * (3 * n + 1) :=
    (Nat.dvd_add_iff_left (show 2 ^ a ∣ 2 ^ a * C from ⟨C, rfl⟩)).mpr
      ⟨2 ^ d * z, e.symm⟩
  have cop : (2 ^ a).Coprime (3 ^ r) :=
    ((show Nat.Coprime 2 3 by decide).pow_left a).pow_right r
  obtain ⟨q, hq⟩ := cop.dvd_of_dvd_mul_left hd
  have tail : Equation q z r d C := (peel_exact n q z r a d C hq.symm).mp enc
  have qo : q % 2 = 1 := by
    unfold Equation at tail
    have hm := congrArg (fun t : Nat => t % 2) tail
    have hp := three_pow_odd r
    rw [Nat.add_mod, Nat.mul_mod (3 ^ r) q 2, hp] at hm
    simp only [Nat.one_mul, Nat.mod_mod] at hm
    rw [Nat.add_mod] at parity
    omega
  have no : n % 2 = 1 := by
    have hm := congrArg (fun t : Nat => t % 2) hq
    have hp := pow_two_even ha
    rw [Nat.add_mod, Nat.mul_mod 3 n 2, Nat.mul_mod (2 ^ a) q 2, hp] at hm
    simp at hm
    omega
  exact ⟨q, ⟨ha, no, qo, hq.symm⟩, tail⟩

theorem legal_tail {a : Nat} {w : List Nat} (h : Legal (a :: w)) : Legal w := by
  intro x hx
  exact h x (by simp [hx])

theorem clock_positive {a : Nat} {w : List Nat} (h : Legal (a :: w)) :
    0 < clock (a :: w) := by
  have ha := h a (by simp)
  simp only [clock]
  omega

theorem correction_odd {a : Nat} {w : List Nat} (h : Legal (a :: w)) :
    correction (a :: w) % 2 = 1 := by
  have hp := pow_two_even (h a (by simp))
  have h3 := three_pow_odd w.length
  simp [correction, Nat.add_mod, Nat.mul_mod, hp, h3]

theorem tail_parity (q : Nat) (hq : q % 2 = 1) (w : List Nat) (h : Legal w) :
    (2 ^ clock w * q + correction w) % 2 = 1 := by
  cases w with
  | nil => simpa [clock, correction] using hq
  | cons a w =>
    have hp := pow_two_even (clock_positive h)
    have hc := correction_odd h
    simp [Nat.add_mod, Nat.mul_mod, hp, hc]

/-- One affine identity plus positive exponents supplies every ordinary inverse guard. -/
theorem equation_to_path (w : List Nat) (h : Legal w) (n q : Nat) (hq : q % 2 = 1)
    (enc : Equation n q w.length (clock w) (correction w)) : Path n q w := by
  induction w generalizing n with
  | nil =>
    simp [Equation, clock, correction] at enc
    subst n
    exact .nil q
  | cons a w ih =>
    have ha := h a (by simp)
    have hw := legal_tail h
    obtain ⟨z, step, tail⟩ := head_forced ha (tail_parity q hq w hw) enc
    exact .cons step (ih hw z tail)

theorem path_to_equation {n q : Nat} {w : List Nat} (h : Path n q w) :
    Equation n q w.length (clock w) (correction w) := by
  induction h with
  | nil n => simp [Equation, clock, correction]
  | @cons n z q a w step path ih =>
    exact (peel_exact n z q w.length a (clock w) (correction w) step.2.2.2).mpr ih

/-- An entire supplied physical prefix cancels for every remaining rank/clock budget. -/
theorem prefix_budget_cancel {n q : Nat} {w : List Nat} (path : Path n q w)
    (z r d C : Nat) :
    Equation n z (w.length + r) (clock w + d)
        (3 ^ r * correction w + 2 ^ clock w * C) ↔ Equation q z r d C := by
  induction path with
  | nil n => simp [clock, correction]
  | @cons n q y a w step path ih =>
    have er : (a :: w).length + r = (w.length + r) + 1 := by simp; omega
    have ec : clock (a :: w) + d = a + (clock w + d) := by simp [clock, Nat.add_assoc]
    have eb : 3 ^ r * correction (a :: w) + 2 ^ clock (a :: w) * C =
        3 ^ (w.length + r) + 2 ^ a * (3 ^ r * correction w + 2 ^ clock w * C) := by
      simp only [correction, clock, Nat.pow_add]
      grind
    rw [er, ec, eb]
    exact (peel_exact n q z (w.length + r) a (clock w + d)
      (3 ^ r * correction w + 2 ^ clock w * C) step.2.2.2).trans ih

theorem equation_iff_path (w : List Nat) (h : Legal w) (n q : Nat) (hq : q % 2 = 1) :
    Equation n q w.length (clock w) (correction w) ↔ Path n q w :=
  ⟨equation_to_path w h n q hq, path_to_equation⟩

/-- Changing any of the target budgets or endpoints cannot alter a legal decoded head. -/
theorem head_budget_independent
    {n z z' r r' a a' d d' C C' : Nat}
    (ha : 0 < a) (ha' : 0 < a')
    (parity : (2 ^ d * z + C) % 2 = 1)
    (parity' : (2 ^ d' * z' + C') % 2 = 1)
    (enc : Equation n z (r + 1) (a + d) (3 ^ r + 2 ^ a * C))
    (enc' : Equation n z' (r' + 1) (a' + d') (3 ^ r' + 2 ^ a' * C')) :
    a = a' := by
  obtain ⟨q, step, _⟩ := head_forced ha parity enc
  obtain ⟨q', step', _⟩ := head_forced ha' parity' enc'
  exact (odd_step_unique step step').1

/-- Exact unbalanced target equation, without subtraction or sign conventions. -/
theorem unbalanced_target_equation (n R A B s d C : Nat)
    (source : Equation n 1 R A B) :
    Equation (5 * n) 1 (R + s) (A + d) C ↔
      C + 5 * 3 ^ s * 2 ^ A = 2 ^ (A + d) + 5 * 3 ^ s * B := by
  unfold Equation at source ⊢
  rw [Nat.pow_add 3 R s]
  grind

/-- Both rank and clock may increase or decrease; this form covers every target budget. -/
theorem arbitrary_target_equation (n R A B P D C : Nat)
    (source : Equation n 1 R A B) :
    Equation (5 * n) 1 P D C ↔
      3 ^ R * C + 5 * 3 ^ P * 2 ^ A =
        3 ^ R * 2 ^ D + 5 * 3 ^ P * B := by
  unfold Equation at source ⊢
  have positive : 0 < 3 ^ R := Nat.pow_pos (by omega)
  constructor
  · intro target
    grind
  · intro identity
    have eq : 3 ^ R * 2 ^ D = 3 ^ R * (3 ^ P * (5 * n) + C) := by grind
    simpa using Nat.eq_of_mul_eq_mul_left positive eq

/-- Unlike `Path`, this relation disallows padding after the first arrival at one. -/
inductive FirstPath : Nat → List Nat → Prop
  | done : FirstPath 1 []
  | next {n q a : Nat} {w : List Nat} :
      n ≠ 1 → OddStep n a q → FirstPath q w → FirstPath n (a :: w)

/-- Successful first-hit correction normalization has no rank, clock, or word choice. -/
theorem first_path_unique {n : Nat} {w v : List Nat}
    (h : FirstPath n w) (g : FirstPath n v) : w = v := by
  induction h generalizing v with
  | done =>
    cases g with
    | done => rfl
    | next ne step path => exact False.elim (ne rfl)
  | @next n q a w ne step path ih =>
    cases g with
    | done => exact False.elim (ne rfl)
    | @next n q' a' v ne' step' path' =>
      obtain ⟨aa, qq⟩ := odd_step_unique step step'
      subst a'
      subst q'
      exact congrArg (List.cons a) (ih path')

/-- A previously known control: a fivefold target can have strictly smaller odd rank. -/
theorem first_hit_seventeen : FirstPath 17 [2, 3, 4] := by
  exact .next (q := 13) (by decide) (by unfold OddStep; decide)
    (.next (q := 5) (by decide) (by unfold OddStep; decide)
      (.next (q := 1) (by decide) (by unfold OddStep; decide) .done))

theorem first_hit_eighty_five : FirstPath 85 [8] := by
  exact .next (q := 1) (by decide) (by unfold OddStep; decide) .done

/-- Restricting to R+s, s>=0, misses this first-hit word. Non-first-hit padding is separate. -/
theorem nonnegative_rank_overhead_misses_known_pair (w : List Nat)
    (path : FirstPath 85 w) : ¬ 3 ≤ w.length := by
  have eq := first_path_unique path first_hit_eighty_five
  subst w
  decide

theorem basin_power_two (a q : Nat) : Basin (2 ^ a * q) ↔ Basin q := by
  induction a with
  | zero => simp
  | succ a ih =>
    have e : 2 ^ (a + 1) * q = 2 * (2 ^ a * q) := by grind
    rw [e]
    exact (basin_twice _).trans ih

def run : Nat → Nat → Nat
  | 0, n => n
  | k + 1, n => run k (shortcut n)

theorem run_add (a b n : Nat) : run (a + b) n = run b (run a n) := by
  induction a generalizing n with
  | zero => simp [run]
  | succ a ih => simpa [run, Nat.succ_add] using ih (shortcut n)

theorem run_power_two (a q : Nat) : run a (2 ^ a * q) = q := by
  induction a with
  | zero => simp [run]
  | succ a ih =>
    have e : 2 ^ (a + 1) * q = 2 * (2 ^ a * q) := by grind
    rw [e]
    simpa [run, shortcut] using ih

theorem odd_step_run {n a q : Nat} (h : OddStep n a q) : run a n = q := by
  obtain ⟨a, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt h.1)
  have e : shortcut n = 2 ^ a * q := by
    have eq : 3 * n + 1 = 2 * (2 ^ a * q) := by
      have hh := h.2.2.2
      rw [Nat.pow_succ] at hh
      grind
    have odd := h.2.1
    simp [shortcut, odd, eq]
  simpa [run, e] using run_power_two a q

theorem path_run {n q : Nat} {w : List Nat} (h : Path n q w) : run (clock w) n = q := by
  induction h with
  | nil n => rfl
  | @cons n q z a w step path ih =>
    rw [clock, run_add, odd_step_run step]
    exact ih

theorem equation_clock_replay (w : List Nat) (h : Legal w) (n q : Nat) (hq : q % 2 = 1)
    (enc : Equation n q w.length (clock w) (correction w)) : run (clock w) n = q :=
  path_run (equation_to_path w h n q hq enc)

theorem odd_step_basin {n a q : Nat} (h : OddStep n a q) : Basin n ↔ Basin q := by
  have hodd := basin_odd n h.2.1
  rw [← h.2.2.2] at hodd
  exact hodd.symm.trans (basin_power_two a q)

theorem path_basin {n q : Nat} {w : List Nat} (h : Path n q w) : Basin n ↔ Basin q := by
  induction h with
  | nil n => rfl
  | cons step path ih => exact (odd_step_basin step).trans ih

theorem certificate_sound (w : List Nat) (h : Legal w) (n : Nat)
    (enc : Equation n 1 w.length (clock w) (correction w)) : Basin n := by
  have path := equation_to_path w h n 1 (by decide) enc
  exact (path_basin path).mpr ⟨0, rfl⟩

end CollatzCorrection

#print axioms CollatzCorrection.head_forced
#print axioms CollatzCorrection.equation_iff_path
#print axioms CollatzCorrection.certificate_sound
#print axioms CollatzCorrection.head_budget_independent
#print axioms CollatzCorrection.arbitrary_target_equation
#print axioms CollatzCorrection.first_path_unique
#print axioms CollatzCorrection.prefix_budget_cancel
#print axioms CollatzCorrection.nonnegative_rank_overhead_misses_known_pair
#print axioms CollatzCorrection.equation_clock_replay
