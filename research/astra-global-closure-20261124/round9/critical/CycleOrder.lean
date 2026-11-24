import Std

namespace CriticalCycle

/-- The positive shortcut Collatz map, also defined at zero. -/
def T (n : Nat) : Nat := if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def run : Nat → Nat → Nat
  | 0, n => n
  | h + 1, n => run h (T n)

def odds : Nat → Nat → Nat
  | 0, _ => 0
  | h + 1, n => n % 2 + odds h (T n)

/-- Comparing the lifted mantissas after clearing the common denominator four. -/
theorem quarter_order {X Y c d : Nat} (h : X < Y) (hc : c ≤ 4) (hd : 1 ≤ d) :
    3 * X + c ≤ 3 * Y + d := by omega

/-- The top image lies below twice the bottom image at the minimum mantissa. -/
theorem no_wrap_overlap {s Y c : Nat} (hy : Y < 8 * s) (hc : c ≤ 4) :
    3 * Y + c < 2 * (3 * (4 * s) + 4) := by omega

private theorem ordered_ranks {p : Nat} (f : Nat → Nat)
    (bounded : ∀ i < p, f i < p)
    (ordered : ∀ i j, i < j → j < p → f i < f j) :
    ∀ i < p, f i = i := by
  have gap : ∀ i l, i + l < p → f i + l ≤ f (i + l) := by
    intro i l hl
    induction l with
    | zero => simp
    | succ l ih =>
      have prev := ih (by omega)
      have increase := ordered (i + l) (i + (l + 1)) (by omega) hl
      omega
  intro i hi
  have lo := gap 0 i (by omega)
  have hi' := gap i (p - 1 - i) (by omega)
  have bound := bounded (i + (p - 1 - i)) (by omega)
  simp only [Nat.zero_add] at lo
  omega

def unrotate (p r j : Nat) : Nat := if r ≤ j then j - r else p - r + j

/-- Cutting the cyclic order gives a strictly increasing enumeration of the
same finite ranks. Undoing the cut recovers the unique rotation. -/
theorem one_cut_rotation {p r : Nat} (hr : r ≤ p) (f : Nat → Nat)
    (bounded : ∀ i < p, f i < p)
    (ordered : ∀ i j, i < j → j < p →
      unrotate p r (f i) < unrotate p r (f j)) :
    ∀ i < p, f i = if i + r < p then i + r else i + r - p := by
  have br : ∀ i < p, unrotate p r (f i) < p := by
    intro i hi
    have := bounded i hi
    unfold unrotate
    split <;> omega
  intro i hi
  have eqn := ordered_ranks (fun j => unrotate p r (f j)) br ordered i hi
  have := bounded i hi
  dsimp [unrotate] at eqn
  split at eqn <;> split <;> omega

/-- A single rotation that visits the neighboring rank has primitive clock data. -/
theorem rotation_primitive {p r : Nat} (visits : ∃ j, j * r % p = 1) :
    Nat.Coprime (p + r) p := by
  obtain ⟨j, hj⟩ := visits
  have dh := Nat.dvd_trans (Nat.gcd_dvd_left r p) (Nat.dvd_mul_left r j)
  have dp := Nat.dvd_trans (Nat.gcd_dvd_right r p) (Nat.dvd_mul_right p (j * r / p))
  have eqn := Nat.mod_add_div (j * r) p
  rw [hj, Nat.add_comm] at eqn
  rw [← eqn] at dh
  exact (Nat.gcd_self_add_left p r).trans (Nat.eq_one_of_dvd_one ((Nat.dvd_add_right dp).mp dh))

def total (f : Nat → Nat) : Nat → Nat
  | 0 => 0
  | j + 1 => total f j + f j

/-- The changes of dyadic band telescope over a closed list of odd sites. -/
theorem clock_total (a b k : Nat → Nat) (p : Nat)
    (edge : ∀ i < p, b i + k i = a i + k (i + 1))
    (closed : k p = k 0) : total b p = total a p := by
  have tel : ∀ j ≤ p, total b j + k 0 = total a j + k j := by
    intro j hj
    induction j with
    | zero => rfl
    | succ j ih =>
      have prev := ih (by omega)
      have here := edge j (by omega)
      dsimp only [total]
      omega
  have eqn := tel p (by omega)
  omega

/-- An integer one-octave cycle cannot have closing denominator one at clock at least three. -/
theorem no_unit_gap (h p : Nat) (hh : 3 ≤ h) : 2 ^ h ≠ 3 ^ p + 1 := by
  have mod3 : ∀ j, 3 ^ j % 8 = 1 ∨ 3 ^ j % 8 = 3 := by
    intro j
    induction j with
    | zero => decide
    | succ j ih =>
      rw [Nat.pow_succ, Nat.mul_mod]
      rcases ih with left | right
      · rw [left]; decide
      · rw [right]; decide
  obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le hh
  have mod2 : 2 ^ (3 + d) % 8 = 0 := by
    rw [Nat.pow_add, show (2 : Nat) ^ 3 = 8 by decide]
    omega
  have hp := mod3 p
  omega

/-- At most five consecutive minimal inverse exponents of size two can begin at
an odd minimum at least 28 in the height range of the least-disagreement cycle. -/
theorem six_twos_exceed {s y : Nat} (hs : 28 ≤ s)
    (step : 729 * y + 3367 = 4096 * s) : 16 * s + 7 < 3 * y := by omega

/-- The first default inverse from the extra ancestor 4x+1 shadows 2y+1. -/
theorem first_detour_shadow {x y : Nat} (old : 3 * y + 1 = 4 * x) :
    3 * (2 * y + 1) + 1 = 2 * (4 * x + 1) := by omega

/-- Further default inverse steps keep the same shadow as long as their
reference exponents are one. -/
theorem continuing_detour_shadow {x y : Nat} (old : 3 * y + 1 = 2 * x) :
    3 * (2 * y + 1) + 1 = 2 * (2 * x + 1) := by omega

private theorem translated_step (n t : Nat) :
    T (n + 2 * t) = T n + 3 ^ (n % 2) * t := by
  have hp : (n + 2 * t) % 2 = n % 2 := by omega
  rcases (show n % 2 = 0 ∨ n % 2 = 1 by omega) with hn | hn <;>
    simp [T, hp, hn] <;> omega

/-- A binary displacement through an actual shortcut prefix. -/
theorem lift (h n t : Nat) :
    run h (n + 2 ^ h * t) = run h n + 3 ^ (odds h n) * t := by
  induction h generalizing n t with
  | zero => simp [run, odds]
  | succ h ih =>
    rw [run, run, odds, Nat.pow_succ]
    rw [show 2 ^ h * 2 * t = 2 * (2 ^ h * t) by
      simp [Nat.mul_comm, Nat.mul_left_comm]]
    rw [translated_step, show 3 ^ (n % 2) * (2 ^ h * t) =
      2 ^ h * (3 ^ (n % 2) * t) by
      simp [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm], ih, Nat.pow_add]
    simp [Nat.mul_comm, Nat.mul_left_comm]

/-- The two-sided test begins on ordinary sources whose original bad-multiple
candidate and recentered minimum candidate meet at fixed independent clocks. -/
theorem recentered_meeting (m : Nat) :
    run 4 (11 + 16 * m) = run 5 (23 + 32 * m) := by
  have left := lift 4 11 m
  have right := lift 5 23 m
  have a : run 4 11 = 20 := by decide
  have b : odds 4 11 = 3 := by decide
  have c : run 5 23 = 20 := by decide
  have d : odds 5 23 = 3 := by decide
  rw [a, b] at left
  rw [c, d] at right
  exact left.trans right.symm

/-- A whole ternary progression of actual targets has smaller positive
multiple-of-three ancestors at exactly 26 ordinary steps. -/
theorem small_multiple (t : Nat) :
    let s := 116582680 + 129140163 * t
    let z := 181749759 + 201326592 * t
    run 26 z = s ∧ 0 < z ∧ z % 3 = 0 ∧ z < 2 * s + 1 := by
  dsimp only
  have base : run 26 181749759 = 116582680 := by decide
  have grade : odds 26 181749759 = 16 := by decide
  have step := lift 26 181749759 (3 * t)
  rw [base, grade] at step
  change run 26 (181749759 + 67108864 * (3 * t)) =
    116582680 + 43046721 * (3 * t) at step
  constructor
  · rw [show 201326592 * t = 67108864 * (3 * t) by omega, step]
    omega
  · omega

/-- The unrestricted three-weight polynomial can vanish at an upper convergent. -/
theorem relaxed_polynomial_vanishes :
    (6 ^ 5) % 13 = 2 ∧ (6 ^ 8) % 13 = 3 ∧
    4 * 6 ^ 4 + 6 ^ 3 + 2 * 6 ^ 2 + 2 * 6 + 2 = 422 * 13 := by decide

#print axioms relaxed_polynomial_vanishes
#print axioms quarter_order
#print axioms no_wrap_overlap
#print axioms one_cut_rotation
#print axioms rotation_primitive
#print axioms clock_total
#print axioms no_unit_gap
#print axioms six_twos_exceed
#print axioms first_detour_shadow
#print axioms continuing_detour_shadow
#print axioms lift
#print axioms recentered_meeting
#print axioms small_multiple

end CriticalCycle
