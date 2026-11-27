module

public import Mathlib.Algebra.BigOperators.Group.Finset.Basic
public import Mathlib.Data.ZMod.Basic
public import Mathlib.Data.Nat.Choose.Sum
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring

/-! Two finite backbones of the weighted Syracuse pressure proof.
The window identity is algebraic and requires no monotonicity of g.
The carry decoding uses positive exponent letters, stored minus one. -/
@[expose] public section

namespace OrdinaryPressureWindows
open Finset

variable {α : Type*} [Field α] [LinearOrder α] [IsStrictOrderedRing α]

theorem window_sum_boundary (g : ℕ → α) (L m : ℕ) :
    ∑ i ∈ range L, (g (i+m) - g i)
      = ∑ j ∈ range m, (g (L+j) - g j) := by
  have h₁ := sum_range_add g L m
  have h₂ := sum_range_add g m L
  rw [Nat.add_comm m L] at h₂
  simp_rw [sum_sub_distrib, Nat.add_comm _ m]
  linarith

/-- The sum of overlaps of fixed-size information increments costs at most m
times a bound on total information, regardless of the number of windows. -/
theorem window_cost (g : ℕ → α) (L m : ℕ) (cap : α)
    (hpos : ∀ j, 0 ≤ g j) (hcap : ∀ j, g j ≤ cap) :
    ∑ i ∈ range L, (g (i+m) - g i) ≤ m*cap := by
  rw [window_sum_boundary]
  calc
    _ ≤ ∑ _j ∈ range m, cap := by
      apply sum_le_sum
      intro j _
      linarith [hpos j, hcap (L+j)]
    _ = _ := by simp

/-- A positive total local entropy gain conflicts with small boundary gains.
Its hypotheses are finite inequalities; this does not encode mutual information. -/
theorem exclude_linear_window_gain (g : ℕ → α) (L m : ℕ) (c lo hi : α)
    (hloc : c ≤ ∑ i ∈ range L, (g (i+m) - g i))
    (hlow : ∀ j < m, lo ≤ g j) (hhigh : ∀ j < m, g (L+j) ≤ hi) :
    c ≤ m*(hi-lo) := by
  rw [window_sum_boundary] at hloc
  calc
    c ≤ _ := hloc
    _ ≤ ∑ _j ∈ range m, (hi-lo) := by
      apply sum_le_sum
      intro j hj
      exact sub_le_sub (hhigh j (mem_range.mp hj)) (hlow j (mem_range.mp hj))
    _ = _ := by simp [mul_sub]

/-- In the cyclic entropy gap, invariance under a difference that is a unit
forces the base probability table to be constant. -/
theorem unit_translation_constant {m : ℕ} [NeZero m] {γ : Type*}
    (f : ZMod m → γ) (d : (ZMod m)ˣ)
    (hinv : ∀ x, f (x + (d : ZMod m)) = f x) (y : ZMod m) : f y = f 0 := by
  have iter (k : ℕ) : f ((k : ZMod m) * (d : ZMod m)) = f 0 := by
    induction k with
    | zero => simp
    | succ k ih =>
      rw [Nat.cast_succ, add_mul, one_mul, hinv, ih]
  have t := iter (y * (↑d⁻¹ : ZMod m)).val
  simpa [ZMod.natCast_zmod_val, mul_assoc] using t

/-- Equality of two translates whose difference is an additive generator. -/
theorem equal_translates_unit_difference {m : ℕ} [NeZero m] {γ : Type*}
    (f : ZMod m → γ) (a b : ZMod m) (hunit : IsUnit (a-b))
    (hsame : ∀ x, f (x+a) = f (x+b)) (y : ZMod m) : f y = f 0 := by
  rcases hunit with ⟨d, hd⟩
  apply unit_translation_constant f d _ y
  intro x
  rw [hd]
  simpa [sub_eq_add_neg, add_comm, add_left_comm, add_assoc] using hsame (x-b)

def clock : List ℕ → ℕ
  | [] => 0
  | a::w => (a+1) + clock w

def carry : List ℕ → ℕ
  | [] => 0
  | a::w => 3^w.length + 2^(a+1) * carry w

theorem nonempty_carry_odd (a : ℕ) (w : List ℕ) : carry (a::w) % 2 = 1 := by
  have ht : 3^w.length % 2 = 1 := by simp [Nat.pow_mod]
  rw [carry, pow_succ, Nat.mul_right_comm (2^a) 2 (carry w)]
  omega

theorem odd_factor_exponent (a b u v : ℕ) (hu : u%2=1) (hv : v%2=1)
    (h : 2^a * u = 2^b * v) : a=b := by
  induction a generalizing b with
  | zero =>
    cases b with
    | zero => rfl
    | succ b =>
      simp only [pow_zero, one_mul, pow_succ, Nat.mul_right_comm (2^b) 2 v] at h
      omega
  | succ a ih =>
    cases b with
    | zero =>
      simp only [pow_zero, one_mul, pow_succ, Nat.mul_right_comm (2^a) 2 u] at h
      omega
    | succ b =>
      simp only [pow_succ, Nat.mul_right_comm (2^a) 2 u,
        Nat.mul_right_comm (2^b) 2 v] at h
      exact congrArg Nat.succ (ih b (by omega))

theorem fixed_clock_decode (u v : List ℕ) (hlen : u.length=v.length)
    (hclock : clock u=clock v) (heq : carry u=carry v) : u=v := by
  induction u generalizing v with
  | nil => simpa using hlen.symm
  | cons a w ih =>
    cases v with
    | nil => simp at hlen
    | cons b t =>
      have hlen' : w.length=t.length := by simpa using hlen
      have prod : 2^(a+1)*carry w=2^(b+1)*carry t := by
        simp only [carry, hlen'] at heq
        omega
      cases w with
      | nil =>
        cases t with
        | nil =>
          simp only [clock, Nat.add_zero] at hclock
          simp [show a=b by omega]
        | cons x xs => simp at hlen'
      | cons x xs =>
        cases t with
        | nil => simp at hlen'
        | cons y ys =>
          have hpow := odd_factor_exponent (a+1) (b+1) _ _
            (nonempty_carry_odd x xs) (nonempty_carry_odd y ys) prod
          have hab : a=b := by omega
          subst b
          have hy : carry (x::xs)=carry (y::ys) := Nat.eq_of_mul_eq_mul_left (by positivity) prod
          have hc : clock (x::xs)=clock (y::ys) := Nat.add_left_cancel hclock
          rw [ih (y::ys) hlen' hc hy]

theorem carry_height (w : List ℕ) : carry w < 2^(clock w)*3^(w.length) := by
  induction w with
  | nil => decide
  | cons a w ih =>
    simp only [carry, clock, List.length_cons]
    rw [pow_add (2 : ℕ) (a+1) (clock w), pow_succ 3 w.length]
    have hp : 0 < 2^(a+1) := by positivity
    have ht : 0 < 2^(clock w) := by positivity
    have hs : 0 < 3^w.length := by positivity
    have hmul := Nat.mul_lt_mul_of_pos_left ih hp
    have hbase : 3^w.length ≤ 2^(a+1) * (2^(clock w)*3^w.length) := by
      calc
        _ ≤ 2^(clock w) * 3^w.length := Nat.le_mul_of_pos_left _ ht
        _ ≤ _ := Nat.le_mul_of_pos_left _ hp
    nlinarith

theorem fixed_clock_residue_decode (u v : List ℕ) (modulus : ℕ)
    (hlen : u.length=v.length) (hc : clock u=clock v)
    (capacity : 2^(clock u)*3^(u.length) ≤ modulus)
    (hr : carry u%modulus=carry v%modulus) : u=v := by
  have hu := lt_of_lt_of_le (carry_height u) capacity
  have hv : carry v < modulus := by
    apply lt_of_lt_of_le (carry_height v)
    simpa [hlen, hc] using capacity
  rw [Nat.mod_eq_of_lt hu, Nat.mod_eq_of_lt hv] at hr
  exact fixed_clock_decode u v hlen hc hr

end OrdinaryPressureWindows

#print axioms OrdinaryPressureWindows.window_sum_boundary
#print axioms OrdinaryPressureWindows.window_cost
#print axioms OrdinaryPressureWindows.exclude_linear_window_gain
#print axioms OrdinaryPressureWindows.unit_translation_constant
#print axioms OrdinaryPressureWindows.equal_translates_unit_difference
#print axioms OrdinaryPressureWindows.nonempty_carry_odd
#print axioms OrdinaryPressureWindows.odd_factor_exponent
#print axioms OrdinaryPressureWindows.fixed_clock_decode
#print axioms OrdinaryPressureWindows.carry_height
#print axioms OrdinaryPressureWindows.fixed_clock_residue_decode
