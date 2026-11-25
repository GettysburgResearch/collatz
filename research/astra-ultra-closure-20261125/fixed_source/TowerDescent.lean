import PhysicalEcho
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Fintype.EquivFin
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Algebra.Order.BigOperators.Group.Finset

/-! Lower-base descent for a growing window of ternary exponents. -/

namespace TowerDescent
open PhysicalEcho
open scoped BigOperators

private theorem odds_succ_mod (h n : ℕ) :
    odds (h+1) n = n%2 + odds h (step n) := by
  change (if n%2=0 then 0 else 1) + _ = _
  split <;> omega

theorem odds_le (h n : ℕ) : odds h n ≤ h := by
  induction h generalizing n with
  | zero => simp [odds]
  | succ h ih =>
    rw [odds_succ_mod]
    have := ih (step n)
    omega

/-- The extra summand covers every arrangement of the odd inputs. -/
theorem endpoint_bound (h n : ℕ) :
    2^h * orbit h n ≤ 3^(odds h n) * (n + 2^h) := by
  induction h generalizing n with
  | zero => simp [orbit, odds]
  | succ h ih =>
    have first : 2 * (step n + 2^h) ≤ 3^(n%2) * (n + 2^(h+1)) := by
      by_cases even : n%2=0
      · simp [step, even, pow_succ]; omega
      · have odd : n%2=1 := by omega
        have ex : 2 * step n = 3*n+1 := by simp [step, odd]; omega
        have pos : 0 < (2:ℕ)^h := by positivity
        rw [odd, pow_one, Nat.mul_add, ex, pow_succ]; omega
    calc
      2^(h+1)*orbit (h+1) n = 2*(2^h*orbit h (step n)) := by rw [orbit, pow_succ]; ring
      _ ≤ 2*(3^(odds h (step n))*(step n+2^h)) := Nat.mul_le_mul_left _ (ih _)
      _ = 3^(odds h (step n))*(2*(step n+2^h)) := by ring
      _ ≤ 3^(odds h (step n))*(3^(n%2)*(n+2^(h+1))) := Nat.mul_le_mul_left _ first
      _ = _ := by rw [odds_succ_mod, pow_add]; ring

/-- Any observed parity count below the stated arithmetic budget certifies
a positive lower-base endpoint at precisely h clocks. -/
theorem below_base_of_budget {h w r R K : ℕ} (base : 2^h ≤ w)
    (rank : r≤R) (word : odds h (3^r*w) ≤ K) (budget : 3^K*(3^R+1) < 2^h) :
    orbit h (3^r*w) < w := by
  have three : ∀ {a b : ℕ}, a ≤ b → 3^a ≤ 3^b := fun h => Nat.pow_le_pow_right (by decide) h
  have wpos : 0<w := lt_of_lt_of_le (by positivity : 0 < (2:ℕ)^h) base
  apply Nat.lt_of_mul_lt_mul_left ((endpoint_bound h _).trans_lt ?_)
  calc
    _ ≤ 3^K*(3^R*w+w) := Nat.mul_le_mul (three word)
      (Nat.add_le_add (Nat.mul_le_mul_right w (three rank)) base)
    _ = (3^K*(3^R+1))*w := by ring
    _ < _ := Nat.mul_lt_mul_of_pos_right budget wpos

private theorem power_pair (a b t : ℕ) (ht : 0<t) : a^t+b^t ≤ (a+b)^t := by
  induction t with
  | zero => omega
  | succ t ih =>
    cases t with
    | zero => simp
    | succ k =>
      have prev := ih (by omega)
      calc
        _ ≤ (a^(k+1)+b^(k+1))*(a+b) := by
          rw [pow_succ a, pow_succ b, Nat.add_mul, Nat.mul_add, Nat.mul_add]; omega
        _ ≤ _ := by simpa only [pow_succ (a+b) (k+1)] using Nat.mul_le_mul_right (a+b) prev

private theorem budget_32 (t : ℕ) (ht : 0<t) : 3^(18*t)*(3^(2*t)+1) < 2^(32*t) := by
  have pair := power_pair (3^20) (3^18) t ht
  have strict := Nat.pow_lt_pow_left (show (3:ℕ)^20+3^18<2^32 by decide) (Nat.ne_of_gt ht)
  calc
    _ = (3^20)^t+(3^18)^t := by
      rw [Nat.mul_add, Nat.mul_one, ←pow_add, show 18*t+2*t=20*t by omega, pow_mul, pow_mul]
    _ ≤ _ := pair
    _ < _ := by simpa only [pow_mul] using strict

theorem below_base {t w r : ℕ} (ht : 0<t) (base : 2^(32*t) ≤ w)
    (rank : r≤2*t) (word : odds (32*t) (3^r*w) ≤ 18*t) :
    orbit (32*t) (3^r*w) < w :=
  below_base_of_budget base rank word (budget_32 t ht)

/-- Physical parity vectors for a whole consecutive block of candidate bases. -/
def parityCode (h offset r : ℕ) (i : Fin (2^h)) : Fin h → Fin 2 :=
  fun j => ⟨orbit j.val (3^r*(offset+i.val)) % 2, Nat.mod_lt _ (by decide)⟩

theorem code_bijective (h offset r : ℕ) : Function.Bijective (parityCode h offset r) := by
  apply (Fintype.bijective_iff_injective_and_card _).mpr
  constructor
  · intro i j eq
    have ag : agree h (3^r*(offset+i.val)) (3^r*(offset+j.val)) :=
      fun k hk => congrArg Fin.val (congrFun eq ⟨k,hk⟩)
    have hc : Nat.Coprime (2^h) (3^r) := ((show Nat.Coprime 2 3 by decide).pow_left _).pow_right _
    have small := Nat.ModEq.add_left_cancel' offset
      (Nat.ModEq.cancel_left_of_coprime hc (agree_congruent h _ _ ag))
    exact Fin.ext (small.eq_of_lt_of_lt i.isLt j.isLt)
  · simp

def bitWeight (A B : ℕ) (d : Fin 2) : ℕ := if d.val = 0 then B else A

private theorem word_weight (A B h n : ℕ) :
    (∏ i : Fin h, bitWeight A B ⟨orbit i.val n % 2, Nat.mod_lt _ (by decide)⟩) =
      A^(odds h n)*B^(h-odds h n) := by
  induction h generalizing n with
  | zero => simp [odds]
  | succ h ih =>
    rw [Fin.prod_univ_succ]
    change bitWeight A B ⟨n%2,_⟩ *
      (∏ i : Fin h, bitWeight A B ⟨orbit i.val (step n)%2, _⟩) = _
    rw [ih,odds_succ_mod]
    have bound := odds_le h (step n)
    by_cases even : n%2=0
    · simp only [bitWeight, even, ↓reduceIte, Nat.zero_add]
      rw [show h+1-odds h (step n)=h-odds h (step n)+1 by omega, pow_succ]; ring
    · have odd : n%2=1 := by omega
      simp only [bitWeight, odd, Nat.one_ne_zero, ite_false]
      rw [show h+1-(1+odds h (step n))=h-odds h (step n) by omega, pow_add]; ring

/-- Exact total weight for the actual words from any full block and any
fixed exponent. No independence between exponents is assumed. -/
theorem total_weight (A B h offset r : ℕ) :
    (∑ i : Fin (2^h), A^(odds h (3^r*(offset+i.val))) *
      B^(h-odds h (3^r*(offset+i.val)))) = (A+B)^h := by
  calc
    _ = ∑ w : Fin h → Fin 2, ∏ j, bitWeight A B (w j) :=
      Fintype.sum_bijective _ (code_bijective h offset r) _ _ (fun i => (word_weight _ _ _ _).symm)
    _ = (∑ d : Fin 2, bitWeight A B d)^h := (Fintype.sum_pow (bitWeight A B) _).symm
    _ = _ := by simp [Fin.sum_univ_succ, bitWeight, Nat.add_comm]

/-- Offsets in a full dyadic block for which the specified endpoint fails
the strict lower-base test. -/
def failures (h offset r : ℕ) : Finset (Fin (2^h)) :=
  Finset.univ.filter (fun i => offset+i.val ≤ orbit h (3^r*(offset+i.val)))

theorem failures_bound {h offset r R K A B : ℕ} (start : 2^h ≤ offset)
    (rank : r≤R) (cutoff : K≤h) (order : B≤A) (budget : 3^K*(3^R+1) < 2^h) :
    (failures h offset r).card * (A^K*B^(h-K)) ≤ (A+B)^h := by
  let weight (i : Fin (2^h)) := A^(odds h (3^r*(offset+i.val))) *
    B^(h-odds h (3^r*(offset+i.val)))
  have on_fail : ∀ i ∈ failures h offset r, A^K*B^(h-K) ≤ weight i := by
    intro i hi
    have fail := (Finset.mem_filter.mp hi).2
    let p := odds h (3^r*(offset+i.val))
    have low : K ≤ p := by
      by_contra! no
      exact (Nat.not_le_of_lt (below_base_of_budget (by omega : 2^h ≤ offset+i.val)
        rank no.le budget)) fail
    have high : p ≤ h := odds_le _ _
    obtain ⟨d,hd⟩ := Nat.exists_eq_add_of_le low
    have bridge : h-K=d+(h-p) := by omega
    change _ ≤ A^p*B^(h-p)
    rw [bridge, pow_add, hd, pow_add]
    exact Nat.mul_le_mul_left (A^K)
      (Nat.mul_le_mul_right (B^(h-(K+d))) (Nat.pow_le_pow_left order d)) |>.trans_eq (by ring)
  calc
    _ = ∑ _i ∈ failures h offset r, A^K*B^(h-K) := by simp
    _ ≤ ∑ i ∈ failures h offset r, weight i := Finset.sum_le_sum on_fail
    _ ≤ ∑ i, weight i := Finset.sum_le_sum_of_subset (Finset.subset_univ _)
    _ = _ := total_weight _ _ _ _ _

/-- The bad set for any exponent in the growing rank window. -/
def exceptional (h offset R : ℕ) : Finset (Fin (2^h)) :=
  (Finset.range (R+1)).biUnion (failures h offset)

theorem simultaneous_budget {h offset R K A B : ℕ} (start : 2^h ≤ offset)
    (cutoff : K≤h) (order : B≤A) (budget : 3^K*(3^R+1)<2^h) :
    (exceptional h offset R).card * (A^K*B^(h-K)) ≤ (R+1)*(A+B)^h := by
  calc
    _ ≤ (∑ r ∈ Finset.range (R+1), (failures h offset r).card) * _ :=
      Nat.mul_le_mul_right _ Finset.card_biUnion_le
    _ = ∑ r ∈ Finset.range (R+1), (failures h offset r).card * _ := by rw [Finset.sum_mul]
    _ ≤ ∑ _r ∈ Finset.range (R+1), (A+B)^h := by
      apply Finset.sum_le_sum
      intro r hr
      exact failures_bound start (by have := Finset.mem_range.mp hr; omega) cutoff order budget
    _ = _ := by simp

theorem simultaneous_bound (t offset : ℕ) (ht : 0<t) (start : 2^(32*t) ≤ offset) :
    (exceptional (32*t) offset (2*t)).card * (9^(18*t)*7^(14*t)) ≤ (2*t+1)*16^(32*t) := by
  simpa only [show 32*t-18*t=14*t by omega] using
    simultaneous_budget start (show 18*t≤32*t by omega) (show 7≤9 by decide) (budget_32 t ht)

theorem orbit_pos (h n : ℕ) (hn : 0<n) : 0<orbit h n := by
  induction h generalizing n with
  | zero => exact hn
  | succ h ih =>
    apply ih
    unfold step
    split <;> omega

/-- Every source outside the exceptional set has an actual positive ordinary
endpoint at exponent zero of a smaller base, for each requested exponent. -/
theorem good_block_merger {h offset R : ℕ} {i : Fin (2^h)} (start : 0<offset)
    (outside : i ∉ exceptional h offset R) (r : ℕ) (rank : r≤R) :
    ∃ b : ℕ, 0<b ∧ b<offset+i.val ∧ orbit h (3^r*(offset+i.val))=orbit 0 (3^0*b) := by
  refine ⟨orbit h (3^r*(offset+i.val)), orbit_pos _ _ (by positivity), ?_, by simp [orbit]⟩
  by_contra! large
  apply outside
  apply Finset.mem_biUnion.mpr
  exact ⟨r, Finset.mem_range.mpr (by omega), Finset.mem_filter.mpr ⟨Finset.mem_univ _, large⟩⟩

/-- A strict counting budget produces one common base in every full block
whose supplied-exponent trajectories all reach a strictly smaller base. -/
theorem exists_simultaneous_mergers {h offset R K A B : ℕ} (start : 2^h ≤ offset)
    (cutoff : K≤h) (order : B≤A) (budget : 3^K*(3^R+1)<2^h)
    (mass : (R+1)*(A+B)^h < 2^h*(A^K*B^(h-K))) :
    ∃ i : Fin (2^h), ∀ r ≤ R, ∃ b : ℕ, 0<b ∧ b<offset+i.val ∧
      orbit h (3^r*(offset+i.val))=orbit 0 (3^0*b) := by
  have card := (simultaneous_budget start cutoff order budget).trans_lt mass
  have outside : ∃ i : Fin (2^h), i ∉ exceptional h offset R := by
    by_contra! all
    have full := Finset.eq_univ_of_forall all
    rw [full, Finset.card_univ, Fintype.card_fin] at card
    exact Nat.lt_irrefl _ card
  obtain ⟨i,hi⟩ := outside
  exact ⟨i, good_block_merger (lt_of_lt_of_le (by positivity : 0 < 2^h) start) hi⟩

set_option maxRecDepth 5000 in
set_option exponentiation.threshold 2048 in
/-- The first 65 exponents at a common base, in every block of length
2^1024 starting at or beyond 2^1024. The two numerical inputs are checked
by the kernel; no enumeration of that block is performed. -/
theorem block_1024 (offset : ℕ) (start : 2^1024≤offset) :
    ∃ i : Fin (2^1024), ∀ r ≤ 64, ∃ b : ℕ, 0<b ∧ b<offset+i.val ∧
      orbit 1024 (3^r*(offset+i.val))=orbit 0 (3^0*b) :=
  exists_simultaneous_mergers start (show 576≤1024 by decide) (show 7≤9 by decide)
    (by decide) (by decide)

/-- Applies directly to a first bad tower. The smaller-base assumption is
needed only at exponent zero, where the ordinary descent lands. -/
theorem first_bad_requires_exception {h offset R r : ℕ} {i : Fin (2^h)}
    (start : 0<offset) (rank : r≤R)
    (smaller : ∀ b : ℕ, 0<b → b<offset+i.val → ∃ k, orbit k b=1)
    (bad : ¬∃ k, orbit k (3^r*(offset+i.val))=1) :
    i ∈ exceptional h offset R := by
  by_contra outside
  obtain ⟨b,hb,lt,hit⟩ := good_block_merger start outside r rank
  have meet : orbit h (3^r*(offset+i.val))=b := by simpa [orbit] using hit
  obtain ⟨k,hk⟩ := smaller b hb lt
  exact bad ⟨h+k, by rw [orbit_add,meet,hk]⟩

#print axioms exists_simultaneous_mergers
#print axioms block_1024
#print axioms first_bad_requires_exception
#print axioms endpoint_bound
#print axioms below_base_of_budget
#print axioms below_base
#print axioms code_bijective
#print axioms total_weight
#print axioms failures_bound
#print axioms simultaneous_budget
#print axioms simultaneous_bound
#print axioms good_block_merger

end TowerDescent
