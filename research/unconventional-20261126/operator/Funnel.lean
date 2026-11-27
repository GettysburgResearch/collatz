module

public import Mathlib.Algebra.Ring.GeomSum
public import Mathlib.Logic.Function.Iterate
public import Mathlib.Data.Set.Disjoint
public import Mathlib.Tactic.Ring
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Positivity

/-! Arithmetic kernel for the ascending shortcut paths and their one-edge cones.
The Hilbert-space and Banach-space arguments are written in WEIGHTED_GAP.md. -/
@[expose] public section

namespace OrdinaryOperatorFunnel

def shortcut (x : ℕ) : ℕ :=
  if x % 2 = 0 then x / 2 else (3 * x + 1) / 2

def reaches (x a : ℕ) : Prop := ∃ t : ℕ, shortcut^[t] x = a

theorem reaches_step_iff_of_ne {x a : ℕ} (h : x ≠ a) :
    reaches x a ↔ reaches (shortcut x) a := by
  constructor
  · rintro ⟨t, ht⟩
    cases t with
    | zero => exact (h ht).elim
    | succ t => exact ⟨t, by simpa [Function.iterate_succ_apply] using ht⟩
  · rintro ⟨t, ht⟩
    exact ⟨t+1, by simpa [Function.iterate_succ_apply] using ht⟩

theorem shortcut_two_mul (x : ℕ) : shortcut (2*x) = x := by
  simp [shortcut]

theorem shortcut_odd_minus (u : ℕ) (hu : 0 < u) :
    shortcut (2*u-1) = 3*u-1 := by
  unfold shortcut
  have hodd : (2*u-1) % 2 ≠ 0 := by omega
  simp only [hodd, ↓reduceIte]
  omega

theorem climb (k y : ℕ) (hy : 0 < y) :
    shortcut^[k] (2^k*y-1) = 3^k*y-1 := by
  induction k generalizing y with
  | zero => simp
  | succ k ih =>
    rw [Function.iterate_succ_apply, pow_succ 2]
    have hpos : 0 < 2^k*y := Nat.mul_pos (by positivity) hy
    have heq : 2^k*2*y = 2*(2^k*y) := by ring
    rw [heq, shortcut_odd_minus _ hpos]
    have heq' : 3*(2^k*y) = 2^k*(3*y) := by ring
    rw [heq', ih _ (by omega), pow_succ]
    congr 1
    ring

theorem cube_lift (k : ℕ) (x : ℤ)
    (hx : (3:ℤ)^(k+1) ∣ x+1) :
    (3:ℤ)^(k+1+1) ∣ x^3+1 := by
  obtain ⟨u, hu⟩ := hx
  let v : ℤ := 3^k*u
  have h1 : x = 3*v-1 := by
    dsimp [v]
    rw [pow_succ] at hu
    linarith
  refine ⟨u*(3*v^2-3*v+1), ?_⟩
  calc
    x^3+1 = (x+1)*(x^2-x+1) := by ring
    _ = 3^(k+1)*u*(3*(3*v^2-3*v+1)) := by
      rw [hu]
      congr 1
      rw [h1]
      ring
    _ = 3^(k+1+1)*(u*(3*v^2-3*v+1)) := by
      rw [pow_succ 3 (k+1)]
      ring

theorem three_pow_dvd_fermat (k : ℕ) :
    3^(k+1) ∣ 2^(3^k)+1 := by
  have aux (j : ℕ) : (3:ℤ)^(j+1) ∣ (2:ℤ)^(3^j)+1 := by
    induction j with
    | zero => norm_num
    | succ j ih =>
      rw [pow_succ 3 j, pow_mul]
      exact cube_lift j _ ih
  exact_mod_cast aux k

theorem infinitely_many_funnel_exponents (k t : ℕ) :
    3^(k+1) ∣ 2^(3^k*(2*t+1))+1 := by
  have hodd : Odd (2*t+1) := ⟨t, rfl⟩
  have h : 2^(3^k)+1 ∣ (2^(3^k))^(2*t+1)+1 := by
    simpa using hodd.nat_add_dvd_pow_add_pow (x := 2^(3^k)) (y := 1)
  simpa [pow_mul] using dvd_trans (three_pow_dvd_fermat k) h

theorem climb_prefix (k j y : ℕ) (hj : j ≤ k) (hy : 0 < y) :
    shortcut^[j] (2^k*y-1) = 3^j*2^(k-j)*y-1 := by
  have h : 2^k*y = 2^j*(2^(k-j)*y) := by
    rw [← Nat.mul_assoc, ← pow_add, Nat.add_sub_of_le hj]
  rw [h, climb j _ (by positivity), Nat.mul_assoc]

theorem shortcut_power (e : ℕ) : ∃ d : ℕ, shortcut (2^e) = 2^d := by
  cases e with
  | zero => exact ⟨1, by decide⟩
  | succ e =>
    exact ⟨e, by rw [pow_succ', shortcut_two_mul]⟩

theorem iter_power (t e : ℕ) : ∃ d : ℕ, shortcut^[t] (2^e) = 2^d := by
  induction t generalizing e with
  | zero => exact ⟨e, rfl⟩
  | succ t ih =>
    obtain ⟨e', he'⟩ := shortcut_power e
    rw [Function.iterate_succ_apply, he']
    exact ih e'

theorem power_reaches_one (e : ℕ) : shortcut^[e] (2^e) = 1 := by
  induction e with
  | zero => rfl
  | succ e ih => rw [Function.iterate_succ_apply, pow_succ', shortcut_two_mul, ih]

theorem no_cross_of_distinct_odd_targets {a b L : ℕ}
    (hne : a ≠ b) (ha : shortcut a = 2^L) (hb : 1 < b) (hodd : b%2=1) :
    ¬ reaches a b := by
  rw [reaches_step_iff_of_ne hne, ha]
  rintro ⟨t, ht⟩
  obtain ⟨e, he⟩ := iter_power t L
  rw [ht] at he
  cases e with
  | zero => simp_all
  | succ e =>
    rw [pow_succ] at he
    omega

theorem odd_cone_doubling {a : ℕ} (ha : a%2=1) (x : ℕ) :
    reaches (2*x) a ↔ reaches x a := by
  have hn : 2*x ≠ a := by omega
  rw [reaches_step_iff_of_ne hn, shortcut_two_mul]

theorem disjoint_of_no_cross {a b : ℕ}
    (hab : ¬ reaches a b) (hba : ¬ reaches b a) :
    Disjoint {x | reaches x a} {x | reaches x b} := by
  rw [Set.disjoint_left]
  rintro x ⟨s, hs⟩ ⟨t, ht⟩
  rcases le_total s t with h | h
  · apply hab
    refine ⟨t-s, ?_⟩
    rw [← hs, ← Function.iterate_add_apply, Nat.sub_add_cancel h, ht]
  · apply hba
    refine ⟨s-t, ?_⟩
    rw [← ht, ← Function.iterate_add_apply, Nat.sub_add_cancel h, hs]

end OrdinaryOperatorFunnel
#print axioms OrdinaryOperatorFunnel.reaches_step_iff_of_ne
#print axioms OrdinaryOperatorFunnel.shortcut_two_mul
#print axioms OrdinaryOperatorFunnel.shortcut_odd_minus
#print axioms OrdinaryOperatorFunnel.climb
#print axioms OrdinaryOperatorFunnel.cube_lift
#print axioms OrdinaryOperatorFunnel.three_pow_dvd_fermat
#print axioms OrdinaryOperatorFunnel.infinitely_many_funnel_exponents
#print axioms OrdinaryOperatorFunnel.climb_prefix
#print axioms OrdinaryOperatorFunnel.shortcut_power
#print axioms OrdinaryOperatorFunnel.iter_power
#print axioms OrdinaryOperatorFunnel.power_reaches_one
#print axioms OrdinaryOperatorFunnel.no_cross_of_distinct_odd_targets
#print axioms OrdinaryOperatorFunnel.odd_cone_doubling
#print axioms OrdinaryOperatorFunnel.disjoint_of_no_cross
