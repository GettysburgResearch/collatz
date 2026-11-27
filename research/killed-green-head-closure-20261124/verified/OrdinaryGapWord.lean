import Mathlib.Logic.Function.Iterate
import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
Finite ordinary inverse legality for the chronological gap convention of PR201.
A letter `e` records a gap of `e+1` shortcut steps. The use of integers permits
a divisibility witness to be signed initially. Positivity and oddness of every
state are derived from the prescribed positive odd terminal.
-/
namespace Collatz.OrdinaryGapWord

inductive Word where
  | nil
  | snoc (front : Word) (extra : ℕ)
  deriving DecidableEq

def Word.depth : Word → ℕ
  | .nil => 0
  | .snoc u _ => u.depth + 1

def Word.clock : Word → ℕ
  | .nil => 0
  | .snoc u e => u.clock + (e+1)

def Word.carry : Word → ℤ
  | .nil => 0
  | .snoc u _ => 3*u.carry + 2^u.clock

def PositiveOdd (x : ℤ) : Prop := 0 < x ∧ x % 2 = 1

/-- A literal path through positive odd integers. Oddness of each next
integer makes the exponent in its gap equation the exact valuation. -/
inductive Path : Word → ℤ → ℤ → Prop where
  | nil {x} (hx : PositiveOdd x) : Path .nil x x
  | snoc {u x y q e} (h : Path u x y) (hq : PositiveOdd q)
      (step : 3*y + 1 = 2^(e+1)*q) : Path (.snoc u e) x q

theorem Path.endpoints {u x q} (h : Path u x q) : PositiveOdd x ∧ PositiveOdd q := by
  induction h with
  | nil hx => exact ⟨hx, hx⟩
  | snoc _ hq _ ih => exact ⟨ih.1, hq⟩

theorem Path.affine {u x q} (h : Path u x q) :
    (2:ℤ)^u.clock*q = 3^u.depth*x + u.carry := by
  induction h with
  | nil => simp [Word.clock, Word.depth, Word.carry]
  | @snoc u x y q e _ _ hs ih =>
    simp only [Word.clock, Word.depth, Word.carry, pow_add, pow_one]
    linear_combination (2:ℤ)^u.clock * (-hs) + 3*ih

/-- Full affine integrality already determines all intermediate ordinary
states, even when the signed source has no positivity or parity hypothesis. -/
theorem path_of_affine (u : Word) {x q : ℤ} (hq : PositiveOdd q)
    (h : (2:ℤ)^u.clock*q = 3^u.depth*x + u.carry) : Path u x q := by
  induction u generalizing x q with
  | nil =>
    simp [Word.clock, Word.depth, Word.carry] at h
    subst q
    exact .nil hq
  | snoc u e ih =>
    simp only [Word.clock, Word.depth, Word.carry, pow_add, pow_one] at h
    have hd : (3:ℤ) ∣ 2^u.clock * (2^(e+1)*q-1) := by
      refine ⟨3^u.depth*x + u.carry, ?_⟩
      linear_combination h
    have hcop : IsCoprime (3:ℤ) 2 := ⟨1, -1, by decide⟩
    obtain ⟨y, hy⟩ := (hcop.pow_right (n := u.clock)).dvd_of_dvd_mul_left hd
    have hs : 3*y+1 = 2^(e+1)*q := by linarith
    have hypos : 0 < (2:ℤ)^(e+1)*q := mul_pos (by positivity) hq.1
    have htwo : (2:ℤ)^(e+1)*q = 2*(2^e*q) := by rw [pow_succ]; ring
    have hyo : PositiveOdd y := by
      constructor <;> omega
    have haf : (2:ℤ)^u.clock*y = 3^u.depth*x + u.carry := by
      apply (mul_left_cancel₀ (by norm_num : (3:ℤ) ≠ 0))
      linear_combination h + (2:ℤ)^u.clock * (-hy)
    exact .snoc (ih hyo haf) hq hs

def shortcut (x : ℤ) : ℤ := if x%2 = 0 then x/2 else (3*x+1)/2

theorem even_run (n : ℕ) (x : ℤ) : shortcut^[n] (2^n*x) = x := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hs : shortcut (2^(n+1)*x) = 2^n*x := by
      have hm : (2:ℤ)^(n+1)*x = 2*(2^n*x) := by rw [pow_succ]; ring
      rw [hm]
      simp [shortcut]
    rw [Function.iterate_succ_apply, hs, ih]

/-- Each path maps to an actual shortcut orbit at exactly the stated clock. -/
theorem Path.shortcut_iterate {u x q} (h : Path u x q) : shortcut^[u.clock] x = q := by
  induction h with
  | nil => rfl
  | @snoc u x y q e hp _ hs ih =>
    have hy : y % 2 ≠ 0 := by have hh := hp.endpoints.2.2; omega
    have h1 : shortcut y = 2^e*q := by
      simp only [shortcut, hy, ↓reduceIte, hs, pow_succ]
      have hm : (2:ℤ)^e*2*q = 2*(2^e*q) := by ring
      rw [hm]
      simp
    rw [Word.clock, Nat.add_comm, Function.iterate_add_apply, ih,
      Function.iterate_succ_apply, h1, even_run]

/-- Uniqueness of a power of two times an odd integer. -/
theorem odd_part_unique {q r : ℤ} (hq : q%2=1) (hr : r%2=1) (a b : ℕ)
    (h : (2:ℤ)^a*q=2^b*r) : a=b ∧ q=r := by
  induction a generalizing b with
  | zero =>
    cases b with
    | zero => simpa using h
    | succ b =>
      have he : (2:ℤ)^(b+1)*r = 2*(2^b*r) := by rw [pow_succ]; ring
      rw [pow_zero, one_mul, he] at h
      omega
  | succ a ih =>
    cases b with
    | zero =>
      have he : (2:ℤ)^(a+1)*q = 2*(2^a*q) := by rw [pow_succ]; ring
      rw [pow_zero, one_mul, he] at h
      omega
    | succ b =>
      simp only [pow_succ] at h
      have hh : (2:ℤ)^a*q=2^b*r := by linarith only [h]
      obtain ⟨he, ho⟩ := ih b hh
      exact ⟨congrArg Nat.succ he, ho⟩

/-- Reading forwards from a source determines the entire gap word and
terminal at a fixed odd depth, even when the terminal was not specified. -/
theorem Path.unique_at_depth {u v x q r} (hu : Path u x q) (hv : Path v x r)
    (hd : u.depth = v.depth) : u=v ∧ q=r := by
  induction hu generalizing v r with
  | nil hx =>
    cases hv with
    | nil => exact ⟨rfl, rfl⟩
    | snoc => simp [Word.depth] at hd
  | @snoc u x y q e hp hq hs ih =>
    cases hv with
    | nil => simp [Word.depth] at hd
    | @snoc v _ z r f hv hr ht =>
      have hlen : u.depth=v.depth := Nat.add_right_cancel hd
      obtain ⟨rfl, rfl⟩ := ih hv hlen
      obtain ⟨hef, hqr⟩ := odd_part_unique hq.2 hr.2 (e+1) (f+1) (hs.symm.trans ht)
      have heq : e=f := Nat.add_right_cancel hef
      exact ⟨congrArg (Word.snoc u) heq, hqr⟩

/-- Precisely the full extra-depth bridge congruence. For every fixed word,
positive odd terminal, source class and extra ternary depth, it is equivalent
to a literal legal path from an ordinary source in that class. -/
theorem source_class_iff (u : Word) {q : ℤ} (hq : PositiveOdd q) (r : ℤ) (K : ℕ) :
    (3:ℤ)^(u.depth+K) ∣ 2^u.clock*q-u.carry-3^u.depth*r ↔
    ∃ x : ℤ, (3:ℤ)^K ∣ x-r ∧ Path u x q := by
  constructor
  · rintro ⟨k, hk⟩
    refine ⟨r+3^K*k, ⟨k, by ring⟩, path_of_affine u hq ?_⟩
    rw [pow_add] at hk
    linear_combination hk
  · rintro ⟨x, ⟨k, hk⟩, hp⟩
    refine ⟨k, ?_⟩
    rw [pow_add]
    linear_combination hp.affine + (3:ℤ)^u.depth*hk

/-- A fixed word at a fixed terminal has at most one signed source. -/
theorem Path.unique_source {u x z q} (hx : Path u x q) (hz : Path u z q) : x=z := by
  apply mul_left_cancel₀ (by positivity : (3:ℤ)^u.depth ≠ 0)
  linear_combination hz.affine - hx.affine

/-- Every noninitial odd vertex in a legal path is automatically prime to three. -/
theorem unit_after_gap {e : ℕ} {y q : ℤ} (hs : 3*y+1=2^(e+1)*q) : ¬ (3:ℤ) ∣ q := by
  rintro ⟨k, rfl⟩
  have h : 1 = 3 * (2^(e+1)*k-y) := by linear_combination hs
  omega

/-- At positive extra depth and a unit source class, the full bridge
congruence gives a unique unit source, at the literal shortcut clock. -/
theorem unit_source_class_iff (u : Word) {q : ℤ} (hq : PositiveOdd q)
    (r : ℤ) (hr : ¬ (3:ℤ) ∣ r) (K : ℕ) :
    (3:ℤ)^(u.depth+(K+1)) ∣ 2^u.clock*q-u.carry-3^u.depth*r ↔
    ∃! x : ℤ, ¬ (3:ℤ) ∣ x ∧ (3:ℤ)^(K+1) ∣ x-r ∧ Path u x q ∧ shortcut^[u.clock] x=q := by
  rw [source_class_iff u hq r (K+1)]
  constructor
  · rintro ⟨x, hc, hp⟩
    have hu : ¬ (3:ℤ) ∣ x := by
      rintro ⟨z, hz⟩
      obtain ⟨k, hk⟩ := hc
      apply hr
      refine ⟨z-3^K*k, ?_⟩
      rw [pow_succ] at hk
      linear_combination hz - hk
    exact ⟨x, ⟨hu, hc, hp, hp.shortcut_iterate⟩, fun _ h => h.2.2.1.unique_source hp⟩
  · rintro ⟨x, hx, _⟩
    exact ⟨x, hx.2.1, hx.2.2.1⟩

#print axioms Path.endpoints
#print axioms Path.affine
#print axioms path_of_affine
#print axioms even_run
#print axioms Path.shortcut_iterate
#print axioms odd_part_unique
#print axioms Path.unique_at_depth
#print axioms source_class_iff
#print axioms Path.unique_source
#print axioms unit_after_gap
#print axioms unit_source_class_iff

end Collatz.OrdinaryGapWord
