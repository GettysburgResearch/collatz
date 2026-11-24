import Mathlib.Data.Nat.ModEq
import Mathlib.Data.Finset.Card
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Finite arithmetic for cyclic Pliss phases and ternary companion packing. -/
set_option autoImplicit false
namespace Collatz.CompanionPacking

/-- Newest bit first, so extending the list applies one more forward branch. -/
def exponent : List Bool → ℕ
  | [] => 0
  | b :: bs => exponent bs + (if b then 2 else 1)

def carry : List Bool → ℕ
  | [] => 0
  | b :: bs => 3 * carry bs + (if b then 2 ^ exponent bs else 0)

inductive Walk (q : ℕ) : List Bool → ℕ → ℕ → Prop
  | start (a : ℕ) : Walk q [] a a
  | even {bs a m t} : Walk q bs a m → 2*t = 3*m → Walk q (false :: bs) a t
  | odd {bs a m t} : Walk q bs a m → 4*t = 3*m+q → Walk q (true :: bs) a t

theorem affine {q a t : ℕ} {bs : List Bool} (w : Walk q bs a t) :
    2 ^ exponent bs * t = 3 ^ bs.length * a + q * carry bs := by
  induction w with
  | start => simp [exponent, carry]
  | @even bs a m t _ h ih =>
    simp only [exponent, carry, Bool.false_eq_true, ite_false, List.length_cons,
      pow_succ, add_zero]
    calc
      2 ^ exponent bs * 2 * t = 2 ^ exponent bs * (2*t) := by ring
      _ = 3*(2 ^ exponent bs*m) := by rw [h]; ring
      _ = _ := by rw [ih]; ring
  | @odd bs a m t _ h ih =>
    simp only [exponent, carry, ite_true, List.length_cons]
    rw [pow_add, pow_succ]; norm_num1
    calc
      2 ^ exponent bs * 4 * t = 2 ^ exponent bs * (4*t) := by ring
      _ = 3*(2 ^ exponent bs*m) + q*2 ^ exponent bs := by rw [h]; ring
      _ = _ := by rw [ih]; ring

/-- Two bounded numerators with the same past agree, even for unrelated starts. -/
theorem same_past {q a b u v : ℕ} {bs : List Bool}
    (hu : Walk q bs a u) (hv : Walk q bs b v)
    (u_small : u < 3 ^ bs.length) (v_small : v < 3 ^ bs.length) : u = v := by
  have hc : Nat.Coprime (3 ^ bs.length) (2 ^ exponent bs) :=
    ((by decide : Nat.Coprime 3 2).pow_left _).pow_right _
  have hmul : Nat.ModEq (3 ^ bs.length) (2 ^ exponent bs*u) (2 ^ exponent bs*v) := by
    rw [affine hu, affine hv]
    simp [Nat.ModEq, Nat.add_mod]
  exact (Nat.ModEq.cancel_left_of_coprime hc hmul).eq_of_lt_of_lt u_small v_small

/-- The marked phases inject into their actual catalogue of past words. -/
theorem packing {ι : Type*} (marked : Finset ι) (catalogue : Finset (List Bool))
    (past : ι → List Bool) (a x : ι → ℕ) (q : ℕ)
    (hc : ∀ i ∈ marked, past i ∈ catalogue)
    (hw : ∀ i ∈ marked, Walk q (past i) (a i) (x i))
    (hs : ∀ i ∈ marked, x i < 3 ^ (past i).length)
    (distinct : Set.InjOn x (marked : Set ι)) : marked.card ≤ catalogue.card := by
  apply Finset.card_le_card_of_injOn past hc
  intro i hi j hj he
  have wj := hw j hj
  have sj := hs j hj
  rw [← he] at wj sj
  exact distinct hi hj (same_past (hw i hi) wj (hs i hi) sj)

/-- Scan signed increments, counting precisely the new strict running maxima. -/
def records : List ℤ → ℤ → ℤ → ℤ × ℕ
  | [], _, m => (m, 0)
  | d :: ds, s, m =>
      let r := records ds (s+d) (max m (s+d))
      (r.1, r.2 + if m < s+d then 1 else 0)

theorem record_bounds (ds : List ℤ) (s m u : ℤ) (hsm : s ≤ m)
    (hd : ∀ d ∈ ds, d ≤ u) :
    s + ds.sum ≤ (records ds s m).1 ∧
    (records ds s m).1 ≤ m + ↑(records ds s m).2 * u := by
  induction ds generalizing s m with
  | nil => simpa [records] using hsm
  | cons d ds ih =>
    have hdu := hd d (by simp)
    have hh := ih (s+d) (max m (s+d)) (le_max_right ..)
      (fun e he => hd e (by simp [he]))
    by_cases hit : m < s+d
    · rw [max_eq_right hit.le] at hh
      simp [records, max_eq_right hit.le, hit, Nat.cast_add] at *
      constructor <;> linarith [hh.1, hh.2]
    · have below : s+d ≤ m := le_of_not_gt hit
      rw [max_eq_left below] at hh
      simp [records, max_eq_left below, hit] at *
      exact ⟨by linarith [hh.1], hh.2⟩

#print axioms affine
#print axioms same_past
#print axioms packing
#print axioms record_bounds
end Collatz.CompanionPacking
