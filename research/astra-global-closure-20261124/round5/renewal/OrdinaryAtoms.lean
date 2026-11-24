import Mathlib.Algebra.Ring.Parity
import Mathlib.Data.Finset.Max
import Mathlib.Data.Finset.Card
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-! Exact arithmetic for inverse words ending at a fixed ordinary shortcut target. -/
set_option autoImplicit false
namespace Collatz.OrdinaryAtoms

/-- Source parities in chronological order. -/
def oddCount : List Bool → ℕ
  | [] => 0
  | b :: w => (if b then 1 else 0) + oddCount w

def carry : List Bool → ℤ
  | [] => 0
  | b :: w => (if b then (3 : ℤ) ^ oddCount w else 0) + 2 * carry w

def step (x : ℤ) : ℤ := if x % 2 = 0 then x / 2 else (3*x+1) / 2

def bits : ℕ → ℤ → List Bool
  | 0, _ => []
  | n+1, x => decide (x%2 = 1) :: bits n (step x)

def endpoint : ℕ → ℤ → ℤ
  | 0, x => x
  | n+1, x => endpoint n (step x)

private theorem carry_nonneg (w : List Bool) : 0 ≤ carry w := by
  induction w with
  | nil => rfl
  | cons b w ih => cases b <;> simp only [carry, Bool.false_eq_true, ite_false,
      ite_true, zero_add] <;> positivity

private theorem scale_odd (w : List Bool) : (3 : ℤ) ^ oddCount w % 2 = 1 := by
  exact Int.odd_iff.mp ((show Odd (3:ℤ) from ⟨1,rfl⟩).pow)

private theorem even_inner {a u z : ℤ} (ha : a % 2 = 1) (eqn : a*u=2*z) :
    u%2=0 := by
  have h := congrArg (· % 2) eqn
  simpa [Int.mul_emod, ha] using h

/-- A whole-word signed affine equality forces all intermediate parities and
correct positive preimages, even when positivity of the computed source was unknown. -/
theorem decode (w : List Bool) (x q : ℤ) (hq : 0 < q)
    (row : (2:ℤ)^w.length*q = (3:ℤ)^oddCount w*x+carry w) :
    0 < x ∧ bits w.length x = w ∧ endpoint w.length x = q := by
  induction w generalizing x with
  | nil => simp [oddCount, carry] at row; simpa [bits, endpoint, ← row] using hq
  | cons b w ih =>
    have ha := scale_odd w
    cases b with
    | false =>
      simp only [List.length_cons, oddCount, carry, Bool.false_eq_true, ite_false,
        zero_add, pow_succ] at row
      have even := even_inner ha (show (3:ℤ)^oddCount w*x =
          2*((2:ℤ)^w.length*q-carry w) by linarith [row])
      have edge : 2*step x=x := by simp [step, even]; omega
      have tail : (2:ℤ)^w.length*q = (3:ℤ)^oddCount w*step x+carry w := by
        have scaled := congrArg (fun t : ℤ => (3:ℤ)^oddCount w*t) edge
        nlinarith only [row, scaled]
      obtain ⟨pos, itinerary, finish⟩ := ih (step x) tail
      have ne : ¬ x%2=1 := by omega
      exact ⟨by omega, by simp [bits, ne, itinerary], finish⟩
    | true =>
      simp only [List.length_cons, oddCount, carry, ite_true,
        pow_succ, pow_add] at row
      have even := even_inner ha (show (3:ℤ)^oddCount w*(3*x+1) =
          2*((2:ℤ)^w.length*q-carry w) by nlinarith only [row])
      have odd : x%2=1 := by omega
      have ne : ¬ x%2=0 := by omega
      have edge : 2*step x=3*x+1 := by simp [step, ne]; omega
      have tail : (2:ℤ)^w.length*q = (3:ℤ)^oddCount w*step x+carry w := by
        have scaled := congrArg (fun t : ℤ => (3:ℤ)^oddCount w*t) edge
        nlinarith only [row, scaled]
      obtain ⟨pos, itinerary, finish⟩ := ih (step x) tail
      exact ⟨by omega, by simp [bits, odd, itinerary], finish⟩

/-- Full ternary integrality alone supplies a positive physical source,
including all prescribed parities. -/
theorem integral_preimage (w : List Bool) (q : ℤ) (hq : 0 < q)
    (h : (3:ℤ)^oddCount w ∣ (2:ℤ)^w.length*q-carry w) :
    ∃ x : ℤ, 0 < x ∧ bits w.length x = w ∧ endpoint w.length x = q ∧
      (2:ℤ)^w.length*q = (3:ℤ)^oddCount w*x+carry w := by
  obtain ⟨x, hx⟩ := h
  have row : (2:ℤ)^w.length*q = (3:ℤ)^oddCount w*x+carry w := by omega
  obtain ⟨pos, itinerary, finish⟩ := decode w x q hq row
  exact ⟨x, pos, itinerary, finish, row⟩

/-- Fixed physical clock and odd count. An atom has at most the indicated
number of genuinely different binary words; the full ternary modulus is retained. -/
theorem fixed_clock_count (W : Finset (List Bool)) (e k q : ℕ) (hq : 0 < q)
    (len : ∀ w ∈ W, w.length=e) (cnt : ∀ w ∈ W, oddCount w=k)
    (legal : ∀ w ∈ W, (3:ℤ)^k ∣ (2:ℤ)^e*q-carry w) :
    W.card ≤ 2^e*q/3^k := by
  classical
  have get (w) (hw : w ∈ W) := integral_preimage w q (by exact_mod_cast hq)
      (by simpa [len w hw, cnt w hw] using legal w hw)
  choose x pos itinerary _finish row using get
  let source (w : List Bool) : ℕ := if h : w ∈ W then (x w h).toNat else 0
  have src (w) (hw : w ∈ W) : (source w : ℤ) = x w hw := by
    simp [source, hw, Int.toNat_of_nonneg (pos w hw).le]
  calc W.card ≤ (Finset.Icc 1 (2^e*q/3^k)).card := by
         apply Finset.card_le_card_of_injOn source
         · intro w hw
           apply Finset.mem_Icc.mpr
           constructor
           · have h := pos w hw; rw [← src w hw] at h; exact_mod_cast h
           · apply (Nat.le_div_iff_mul_le (by positivity : 0 < 3^k)).mpr
             have r := row w hw
             rw [len w hw, cnt w hw, ← src w hw] at r
             have nonneg := carry_nonneg w
             exact_mod_cast (show (source w:ℤ)*3^k ≤ 2^e*(q:ℤ) by nlinarith only [r,nonneg])
         · intro w hw v hv eqs
           have ix : x w hw = x v hv := by rw [← src w hw, ← src v hv, eqs]
           have a := itinerary w hw
           have b := itinerary v hv
           rw [len w hw, ix] at a
           rw [len v hv] at b
           exact a.symm.trans b
       _ = _ := by simp

/-- A localized real carry confines every integral inverse to one translated
interval. The bound is independent of the integer lift of the ternary target. -/
theorem localized_fixed_clock_count (W : Finset (List Bool)) (e k q B : ℕ) (hq : 0 < q)
    (len : ∀ w ∈ W, w.length=e) (cnt : ∀ w ∈ W, oddCount w=k)
    (legal : ∀ w ∈ W, (3:ℤ)^k ∣ (2:ℤ)^e*q-carry w)
    (cap : ∀ w ∈ W, carry w ≤ (2:ℤ)^e*B) :
    W.card ≤ 2^e*B/3^k+1 := by
  classical
  by_cases nonempty : W.Nonempty
  · have get (w) (hw : w ∈ W) := integral_preimage w q (by exact_mod_cast hq)
        (by simpa [len w hw, cnt w hw] using legal w hw)
    choose x _pos itinerary _finish row using get
    let source (w : List Bool) : ℤ := if h : w ∈ W then x w h else 0
    have src (w) (hw : w ∈ W) : source w = x w hw := by simp [source, hw]
    have eqn (w) (hw : w ∈ W) : (2:ℤ)^e*q = (3:ℤ)^k*source w+carry w := by
      simpa only [len w hw, cnt w hw, src w hw] using row w hw
    obtain ⟨a, ha, minimum⟩ := Finset.exists_min_image W source nonempty
    let shift (w : List Bool) := (source w - source a).toNat
    have diff (w) (hw : w ∈ W) : (shift w : ℤ) = source w - source a :=
      Int.toNat_of_nonneg (sub_nonneg.mpr (minimum w hw))
    calc W.card ≤ (Finset.range (2^e*B/3^k+1)).card := by
           apply Finset.card_le_card_of_injOn shift
           · intro w hw
             apply Finset.mem_range.mpr
             apply Nat.lt_succ_of_le
             apply (Nat.le_div_iff_mul_le (by positivity : 0 < 3^k)).mpr
             have bound : (shift w:ℤ)*3^k ≤ 2^e*(B:ℤ) := by
               rw [diff w hw]
               nlinarith only [eqn w hw,eqn a ha,cap a ha,carry_nonneg w]
             exact_mod_cast bound
           · intro w hw v hv same
             have h := congrArg (fun n : ℕ => (n:ℤ)) same
             change (shift w:ℤ) = (shift v:ℤ) at h
             rw [diff w hw, diff v hv] at h
             have ix : x w hw = x v hv := by rw [← src w hw, ← src v hv]; omega
             have a₁ := itinerary w hw
             have a₂ := itinerary v hv
             rw [len w hw, ix] at a₁
             rw [len v hv] at a₂
             exact a₁.symm.trans a₂
         _ = _ := by simp
  · simp [Finset.not_nonempty_iff_eq_empty.mp nonempty]

/-- The earliest chronological odd bit bounds the real carry below. -/
theorem first_odd_carry (w : List Bool) : (3:ℤ)^oddCount w ≤ carry (true::w) := by
  simp [carry, carry_nonneg w]

/-- Deterministic truncation behind the weak square-root renewal bound. -/
theorem truncated_clock (H : ℕ) (gaps : List ℕ) :
    min H gaps.sum ≤ (gaps.map (min H)).sum := by
  induction gaps with
  | nil => simp
  | cons g gs ih =>
    simp only [List.sum_cons,List.map_cons]
    omega

/-- Deterministic floor bound used before transferring the heavy-tail clock law. -/
theorem clock_floor (h : ℕ) (x : ℤ) (pos : 0 ≤ x) : x ≤ (2:ℤ)^h*endpoint h x := by
  induction h generalizing x with
  | zero => simp [endpoint]
  | succ h ih =>
    have edge : x ≤ 2*step x := by
      by_cases he : x%2=0 <;> simp [step, he] <;> omega
    have bound := ih (step x) (by omega)
    simp [endpoint,pow_succ]; linarith

#print axioms decode
#print axioms integral_preimage
#print axioms fixed_clock_count
#print axioms localized_fixed_clock_count
#print axioms first_odd_carry
#print axioms truncated_clock
#print axioms clock_floor
end Collatz.OrdinaryAtoms
