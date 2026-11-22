module

public import BandArithmetic

@[expose] public section

/-!
# Ordinary power-block compression

A finite actual Collatz itinerary is divided into powers of finite parity
blocks.  Every block and its repetition count may be chosen independently.
Either a block already witnesses an actual short cycle, or ordinary parity
separation bounds the total clock in terms of the original source and the
number of blocks.  No compressed description of an arbitrary infinite
itinerary is assumed here.

The companion written argument combines this exact arithmetic with a stated
published logarithmic-form estimate to classify bounded-power-block cycle
families.  That transcendence-theory step is not imported as a Lean axiom.
-/

namespace CollatzShell.BlockCompression

open BandArithmetic

/-- One atom of length `period`, repeated `copies` times. -/
structure Block where
  period : Nat
  copies : Nat
  deriving DecidableEq

def Block.duration (b : Block) : Nat := b.copies * b.period

/-- Equality of the actual parity digits at distance `period` throughout
the repeated part. This is precisely the finite periodic-prefix condition. -/
def Repeats (x : Nat) (b : Block) : Prop :=
  ∀ t < (b.copies - 1) * b.period,
    orbit t x % 2 = orbit (t + b.period) x % 2

/-- The source is transported by every complete preceding block. -/
def Trace : Nat → List Block → Prop
  | _, [] => True
  | x, b :: bs =>
      0 < b.period ∧ 0 < b.copies ∧ Repeats x b ∧
        Trace (orbit b.duration x) bs

def duration : List Block → Nat
  | [] => 0
  | b :: bs => b.duration + duration bs

/-- An actual later state is periodic, with the displayed bounded period. -/
def HasShortCycle (x B : Nat) : Prop :=
  ∃ t p : Nat, 0 < p ∧ p ≤ B ∧ orbit p (orbit t x) = orbit t x

private theorem step_upper (x : Nat) : step x ≤ 2 * x := by
  unfold step
  split <;> omega

theorem orbit_upper_dyadic (t x : Nat) : orbit t x ≤ 2 ^ t * x := by
  induction t generalizing x with
  | zero => simp [orbit]
  | succ t ih =>
    calc
      orbit (t+1) x = orbit t (step x) := rfl
      _ ≤ 2 ^ t * step x := ih _
      _ ≤ 2 ^ t * (2 * x) := Nat.mul_le_mul_left _ (step_upper x)
      _ = 2 ^ (t+1) * x := by rw [pow_succ]; ring

/-- A genuine repeated block whose first copy does not close a cycle must
pay for all its repeated parity digits with an ordinary source displacement. -/
theorem repeat_displacement {x : Nat} {b : Block} (repeated : Repeats x b)
    (nonfixed : orbit b.period x ≠ x) :
    2 ^ ((b.copies - 1) * b.period) ≤
      (x - orbit b.period x) + (orbit b.period x - x) := by
  apply repeated_parity_requires_displacement nonfixed.symm
  intro t ht
  have h := repeated t ht
  rw [Nat.add_comm t b.period, orbit_add] at h
  exact h

/-- Each repeated block has a source-height budget, with no restriction on
its independently chosen repetition count. -/
theorem repeat_power_bound {x : Nat} {b : Block} (copies : 0 < b.copies)
    (repeated : Repeats x b) (nonfixed : orbit b.period x ≠ x) :
    2 ^ b.duration ≤ 2 ^ (2 * b.period) * x := by
  have disp := repeat_displacement repeated nonfixed
  have up := orbit_upper_dyadic b.period x
  have base : x ≤ 2 ^ b.period * x := by
    have hp : 1 ≤ 2 ^ b.period := Nat.one_le_pow b.period 2 (by decide)
    nlinarith
  have small :
      (x - orbit b.period x) + (orbit b.period x - x) ≤
        2 ^ b.period * x := by omega
  have paid := disp.trans small
  have exp : (b.copies - 1) * b.period + b.period = b.duration := by
    unfold Block.duration
    have hk : b.copies - 1 + 1 = b.copies := by omega
    nlinarith
  calc
    2 ^ b.duration = 2 ^ ((b.copies - 1) * b.period) * 2 ^ b.period := by
      rw [← pow_add, exp]
    _ ≤ (2 ^ b.period * x) * 2 ^ b.period := Nat.mul_le_mul_right _ paid
    _ = 2 ^ (2 * b.period) * x := by
      rw [show 2 * b.period = b.period + b.period by omega, pow_add]
      ring

/-- The endpoint of a repeated atom is controlled by the same source budget. -/
theorem repeat_exit_bound {x : Nat} {b : Block} (copies : 0 < b.copies)
    (repeated : Repeats x b) (nonfixed : orbit b.period x ≠ x) :
    orbit b.duration x ≤ 2 ^ (2 * b.period) * x ^ 2 := by
  calc
    orbit b.duration x ≤ 2 ^ b.duration * x := orbit_upper_dyadic _ _
    _ ≤ (2 ^ (2 * b.period) * x) * x :=
      Nat.mul_le_mul_right _ (repeat_power_bound copies repeated nonfixed)
    _ = 2 ^ (2 * b.period) * x ^ 2 := by ring

theorem short_cycle_pullback {x y B : Nat} (t : Nat)
    (hit : orbit t x = y) (cycle : HasShortCycle y B) : HasShortCycle x B := by
  obtain ⟨s, p, pos, small, eq⟩ := cycle
  refine ⟨t+s, p, pos, small, ?_⟩
  simpa [orbit_add, hit] using eq

private theorem doubling_exponent (r : Nat) :
    1 + 2 * (2 ^ r - 1) = 2 ^ (r+1) - 1 := by
  have hp : 1 ≤ 2 ^ r := Nat.one_le_pow r 2 (by decide)
  rw [pow_succ]
  omega

/-- All actual finite power-block traces obey a dichotomy: a genuine small
cycle is already reached, or the complete clock obeys one source budget.
No bound is imposed on any repetition count and no source is resampled. -/
theorem short_cycle_or_trace_power_bound {x B : Nat} {bs : List Block}
    (trace : Trace x bs) (bounded : ∀ b ∈ bs, b.period ≤ B) :
    HasShortCycle x B ∨
      2 ^ duration bs ≤ (2 ^ (2 * B) * x) ^ (2 ^ bs.length - 1) := by
  induction bs generalizing x with
  | nil => simp [duration]
  | cons b bs ih =>
    obtain ⟨period, copies, repeated, tail⟩ := trace
    have bound : b.period ≤ B := bounded b (by simp)
    have tailbound : ∀ c ∈ bs, c.period ≤ B := by
      intro c hc
      exact bounded c (by simp [hc])
    by_cases fixed : orbit b.period x = x
    · exact Or.inl ⟨0, b.period, period, bound, by simpa [orbit] using fixed⟩
    · rcases ih tail tailbound with short | paid
      · exact Or.inl (short_cycle_pullback b.duration rfl short)
      · right
        let C := 2 ^ (2 * B)
        let e := 2 ^ bs.length - 1
        have atom : 2 ^ (2 * b.period) ≤ C :=
          Nat.pow_le_pow_right (by decide) (by omega)
        have front : 2 ^ b.duration ≤ C * x :=
          (repeat_power_bound copies repeated fixed).trans
            (Nat.mul_le_mul_right _ atom)
        have exit : orbit b.duration x ≤ C * x ^ 2 :=
          (repeat_exit_bound copies repeated fixed).trans
            (Nat.mul_le_mul_right _ atom)
        have next : C * orbit b.duration x ≤ (C * x) ^ 2 := by
          calc
            C * orbit b.duration x ≤ C * (C * x ^ 2) :=
              Nat.mul_le_mul_left _ exit
            _ = (C * x) ^ 2 := by ring
        have rest : 2 ^ duration bs ≤ (C * x) ^ (2 * e) := by
          calc
            2 ^ duration bs ≤ (C * orbit b.duration x) ^ e := paid
            _ ≤ ((C * x) ^ 2) ^ e := Nat.pow_le_pow_left next e
            _ = (C * x) ^ (2 * e) := by rw [pow_mul]
        calc
          2 ^ duration (b :: bs) = 2 ^ b.duration * 2 ^ duration bs := by
            simp [duration, pow_add]
          _ ≤ (C * x) * (C * x) ^ (2 * e) := Nat.mul_le_mul front rest
          _ = (C * x) ^ (1 + 2 * e) := by rw [pow_add, pow_one]
          _ = (2 ^ (2 * B) * x) ^ (2 ^ (b :: bs).length - 1) := by
            rw [List.length_cons]
            congr 1
            exact doubling_exponent bs.length

/-- An explicit integer clock budget following from the source-preserving
power bound. `Nat.log2` is the binary depth of the original ordinary source. -/
theorem trace_clock_bound_of_power_bound (x B : Nat) (bs : List Block)
    (paid : 2 ^ duration bs ≤ (2 ^ (2 * B) * x) ^ (2 ^ bs.length - 1)) :
    duration bs ≤ (2 ^ bs.length - 1) * (2 * B + x.log2 + 1) := by
  have base : 2 ^ (2 * B) * x ≤ 2 ^ (2 * B + x.log2 + 1) := by
    calc
      2 ^ (2 * B) * x ≤ 2 ^ (2 * B) * 2 ^ (x.log2 + 1) :=
        Nat.mul_le_mul_left _ Nat.lt_log2_self.le
      _ = 2 ^ (2 * B + x.log2 + 1) := by simp [pow_add, Nat.add_assoc]
  have power :
      2 ^ duration bs ≤ 2 ^ ((2 ^ bs.length - 1) * (2 * B + x.log2 + 1)) := by
    calc
      2 ^ duration bs ≤ (2 ^ (2 * B) * x) ^ (2 ^ bs.length - 1) := paid
      _ ≤ (2 ^ (2 * B + x.log2 + 1)) ^ (2 ^ bs.length - 1) :=
        Nat.pow_le_pow_left base _
      _ = 2 ^ ((2 ^ bs.length - 1) * (2 * B + x.log2 + 1)) := by
        rw [← pow_mul, Nat.mul_comm]
  exact (Nat.pow_le_pow_iff_right (by decide : 1 < 2)).mp power

/-- Universal finite trace alternative, including all exact fixed-block
cycles rather than discarding them in a denominator estimate. -/
theorem short_cycle_or_trace_clock_bound {x B : Nat} {bs : List Block}
    (trace : Trace x bs) (bounded : ∀ b ∈ bs, b.period ≤ B) :
    HasShortCycle x B ∨
      duration bs ≤ (2 ^ bs.length - 1) * (2 * B + x.log2 + 1) := by
  rcases short_cycle_or_trace_power_bound trace bounded with cycle | bound
  · exact Or.inl cycle
  · exact Or.inr (trace_clock_bound_of_power_bound x B bs bound)

/-- A compressed actual prefix exceeding the explicit budget supplies a
genuine finite cycle certificate; this implication is valid for every source. -/
theorem short_cycle_of_long_compressed_trace {x B : Nat} {bs : List Block}
    (trace : Trace x bs) (bounded : ∀ b ∈ bs, b.period ≤ B)
    (long : (2 ^ bs.length - 1) * (2 * B + x.log2 + 1) < duration bs) :
    HasShortCycle x B := by
  rcases short_cycle_or_trace_clock_bound trace bounded with cycle | bound
  · exact cycle
  · omega

/-- A period can be repeated any finite number of times. -/
theorem orbit_period_mul {x N : Nat} (cycle : orbit N x = x) (k : Nat) :
    orbit (N*k) x = x := by
  induction k with
  | zero => simp [orbit]
  | succ k ih =>
    rw [Nat.mul_succ, orbit_add, ih, cycle]

private theorem orbit_commute (a b x : Nat) :
    orbit a (orbit b x) = orbit b (orbit a x) := by
  rw [← orbit_add, ← orbit_add, Nat.add_comm]

/-- On a purely periodic ordinary orbit, a return at any later state pulls
back to the original source with exactly the same period. -/
theorem later_period_pullback {x N t p : Nat} (positive : 0 < N)
    (cycle : orbit N x = x) (later : orbit p (orbit t x) = orbit t x) :
    orbit p x = x := by
  have cover : t ≤ N*t := by nlinarith
  have close : orbit (N*t-t) (orbit t x) = x := by
    rw [← orbit_add, Nat.add_sub_of_le cover]
    exact orbit_period_mul cycle t
  have lifted := congrArg (orbit (N*t-t)) later
  rw [orbit_commute (N*t-t) p (orbit t x), close] at lifted
  exact lifted

/-- The short-cycle branch is impossible on a primitive cycle whose period
exceeds the atom-length bound. -/
theorem no_short_cycle_of_primitive {x N B : Nat} (positive : 0 < N)
    (cycle : orbit N x = x)
    (least : ∀ p, 0 < p → p < N → orbit p x ≠ x) (small : B < N) :
    ¬ HasShortCycle x B := by
  rintro ⟨t, p, pp, pb, later⟩
  exact least p pp (by omega) (later_period_pullback positive cycle later)

/-- The finite compression bound applies to a complete primitive positive
cycle, retaining its full clock and allowing independent block exponents. -/
theorem primitive_cycle_compression_bound {x N B : Nat} {bs : List Block}
    (positive : 0 < N) (cycle : orbit N x = x)
    (least : ∀ p, 0 < p → p < N → orbit p x ≠ x)
    (small : B < N) (trace : Trace x bs)
    (bounded : ∀ b ∈ bs, b.period ≤ B) (complete : duration bs = N) :
    N ≤ (2 ^ bs.length - 1) * (2 * B + x.log2 + 1) := by
  rcases short_cycle_or_trace_clock_bound trace bounded with short | bound
  · exact (no_short_cycle_of_primitive positive cycle least small short).elim
  · simpa [complete] using bound

end CollatzShell.BlockCompression
