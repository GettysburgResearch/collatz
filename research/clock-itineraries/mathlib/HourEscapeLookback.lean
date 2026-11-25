module

public import HourEscapeSigned
import all HourEscapeSigned
import all HourEscapeDrawdown
import all HourEscapeLimits
import all EscapeRecords
import all FixedGate
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.HourEscape

open EscapeRecords FixedGate Collatz.HourCycleShadow
set_option autoImplicit false

/-- The record k has spent its last n odd steps within a factor H of its
terminal coefficient. Every ratio compares actual indices from this source. -/
def RecordPlateau (a H n k : ℕ) : Prop :=
  n≤k ∧ Critical a k ∧ ∀ j,j≤n → RatioLE a H k (k-j)

/-- Arbitrarily long bounded-gain terminal windows suffice for an irrational
critical endpoint. Other portions of the ray may have unrestricted declines. -/
theorem irrational_of_local_plateaus {a H : ℕ} {c : Bool} (odd : a%2=1)
    (color : a%3=digit c) (plateaus : ∀ n, ∃ k, RecordPlateau a H n k) :
    ∃ e, RecordScript a e ∧ ∀ (d : ℕ) (A : ℤ), 0<d → ¬RationalTrace d A e := by
  let k := fun n => Classical.choose (plateaus n)
  have data (n : ℕ) : RecordPlateau a H n (k n) := Classical.choose_spec (plateaus n)
  let w := fun n j => if j<n then incoming a (k n) j else 0
  have budgets (n j : ℕ) (small : j≤n) :
      2^(prefixSum (incoming a (k n)) j)≤3^j ∧
      3^j≤H*2^(prefixSum (incoming a (k n)) j) := by
    obtain ⟨late,record,range⟩ := data n
    have inside := Nat.le_trans small late
    constructor
    · cases j with
      | zero => simp [prefixSum]
      | succ t =>
        exact (critical_segment record (show k n-(t+1)+(t+1)=k n by omega)
          (reverse_clock a (k n) (t+1) inside) (by omega)).le
    · exact (segment_ratio inside).mp (range j small)
  have bound (n j : ℕ) : w n j<3*H+1 := by
    by_cases small : j<n
    · have upper := (budgets n (j+1) (by omega)).1
      have lower := (budgets n j (by omega)).2
      rw [prefixSum,Nat.pow_add,Nat.pow_succ] at upper
      have combined := Nat.le_trans upper (Nat.mul_le_mul_right 3 lower)
      have reduce : 2^(incoming a (k n) j)≤3*H := by
        apply Nat.le_of_mul_le_mul_left (c:=2^(prefixSum (incoming a (k n)) j)) _ (Nat.two_pow_pos _)
        simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using combined
      have lowerGap := Nat.lt_two_pow_self (n:=incoming a (k n) j)
      simp only [w,small,↓reduceIte]
      omega
    · simp [w,small]
  obtain ⟨e,limit⟩ := trace_compact w bound
  have common (n R : ℕ) : ∃ t, n+R≤t ∧ ∀ j,j<n → incoming a (k t) j=e j := by
    obtain ⟨t,late,same⟩ := limit n (n+R)
    refine ⟨t,late,fun j hj => ?_⟩
    have inside : j<t := by omega
    simpa [w,inside] using same j hj
  have script : RecordScript a e := by
    intro n R
    obtain ⟨t,late,agree⟩ := common n R
    exact ⟨k t,Nat.le_trans late (data t).1,(data t).2.1,agree⟩
  have strip (n : ℕ) : 2^(prefixSum e n)≤3^n ∧ 3^n≤H*2^(prefixSum e n) := by
    obtain ⟨t,late,agree⟩ := common n 0
    rw [←sum_congr agree]
    exact budgets t n (by omega)
  have pos (j : ℕ) : 0<e j := by
    obtain ⟨i,_,_,agree⟩ := script (j+1) 0
    rw [←agree j (by omega)]
    obtain ⟨_,_,_,o,_⟩ := route_exists (i-(j+1)) a odd color
    exact (next_gap o).pos
  refine ⟨e,script,fun d A dp trace => ?_⟩
  obtain ⟨y,shadow⟩ := shadow_of_trace trace
  exact no_rational_balanced_shadow dp pos shadow (strip_is_bounded strip)

/-- If all actual critical endpoint scripts on the fixed ray have rational
coordinates, each requested gain is achieved within one fixed backward depth
uniformly at every sufficiently late critical record. -/
theorem uniform_lookback_of_rational_limits {a : ℕ} {c : Bool} (odd : a%2=1)
    (color : a%3=digit c)
    (rational : ∀ e, RecordScript a e → ∃ (d : ℕ) (A : ℤ), 0<d ∧ RationalTrace d A e)
    (H : ℕ) : ∃ n, ∀ k, n≤k → Critical a k →
      ∃ j, j≤n ∧ ¬ RatioLE a H k (k-j) := by
  by_contra! neg
  have plateaus (n : ℕ) : ∃ k, RecordPlateau a H n k := by
    obtain ⟨k,late,mark,cap⟩ := neg n
    exact ⟨k,late,mark,cap⟩
  obtain ⟨e,script,no⟩ := irrational_of_local_plateaus odd color plateaus
  obtain ⟨d,A,pos,trace⟩ := rational e script
  exact no d A pos trace

#print axioms irrational_of_local_plateaus
#print axioms uniform_lookback_of_rational_limits
end Collatz.Itinerary.HourEscape
