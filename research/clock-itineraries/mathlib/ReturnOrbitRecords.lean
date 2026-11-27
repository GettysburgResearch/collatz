module
public import ReturnOrbitTernaryWindows
public import HourEscapeLookback
import all ReturnOrbitBinary
import all HourEscapeDrawdown
import all HourEscapeLimits
import all HourEscapeBranching
import all FixedGate
import all EscapeRecords
import all HourCycleShadow
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.HourEscape
open FixedGate EscapeRecords EscapeFrontier ClockRecurrence Collatz.HourCycleShadow
set_option autoImplicit false

/-- At an actual strict record on an ordinary ray, a sufficiently accurate
ternary rational approximation forces a large recent gain in the uncorrected
clock. There is no height, nonrepetition or global drawdown assumption. -/
theorem actual_record_rational_gain {a k d H : ℕ} {A : ℤ} {c : Bool}
    (odd : a%2=1) (color : a%3=digit c) (dp : 0 < d) (hp : 0 < H)
    (record : Critical a k) (room : inverseRationalHorizon d H A ≤ k)
    (residue : (3:ℤ)^(inverseRationalHorizon d H A)∣(d:ℤ)*after k a-A) :
    ∃ j, 0 < j ∧ j ≤ inverseRationalHorizon d H A ∧ ¬RatioLE a H k (k-j) := by
  let L := inverseRationalHorizon d H A
  let e := incoming a k
  let x := fun i => after (k-i) a
  have pos (i : ℕ) : 0 < e i := by
    obtain ⟨_,_,_,oi,_⟩ := route_exists (k-(i+1)) a odd color
    exact (next_gap oi).pos
  have edge (i : ℕ) (hi : i < L) : 3*x (i+1)+1=2^(e i)*x i := by
    obtain ⟨_,_,_,oi,_⟩ := route_exists (k-(i+1)) a odd color
    have g := next_gap oi
    have nextState : after ((k-(i+1))+1) a=(next (after (k-(i+1)) a)).2 := by rw [after_add]; rfl
    rw [show k-(i+1)+1=k-i by change L ≤ k at room; omega] at nextState
    have eqn := g.eqn.symm
    rw [←nextState] at eqn
    exact eqn
  by_contra! flat
  apply ordinary_ternary_clock_exclusion (d:=d) (K:=H) (A:=A) (x:=x) dp hp pos edge _ (by
    simpa [x] using residue)
  intro j hj
  have inside := hj.trans room
  have bounds : 2^(prefixSum e j) ≤ 3^j ∧ 3^j ≤ H*2^(prefixSum e j) := by
    cases j with
    | zero => simpa [prefixSum] using (show 1≤H by omega)
    | succ j =>
      have left := critical_segment record (show k-(j+1)+(j+1)=k by omega)
        (reverse_clock a k (j+1) inside) (by omega)
      exact ⟨left.le,(segment_ratio inside).mp (flat (j+1) (by omega) hj)⟩
  have clock (i : ℕ) : total e i=prefixSum e i := by
    induction i with
    | zero => rfl
    | succ i ih => simp [total,prefixSum,ih]
  rw [weight_formula,clock]
  have pow : 0 < (2:ℝ)^(prefixSum e j) := by positivity
  have lower : (2:ℝ)^(prefixSum e j) ≤ 3^j := by exact_mod_cast bounds.1
  have upper : (3:ℝ)^j ≤ H*2^(prefixSum e j) := by exact_mod_cast bounds.2
  have hpos : 1 ≤ (H:ℝ) := by exact_mod_cast hp
  have one : (1:ℝ) ≤ 3^j/2^(prefixSum e j) := (le_div_iff₀ pow).mpr (by simpa using lower)
  exact ⟨by simpa using mul_le_mul hpos one (by norm_num : (0:ℝ) ≤ 1) (Nat.cast_nonneg H),
    (div_le_iff₀ pow).mpr upper⟩

/-- One fixed escaping ray with bounded drawdowns and unbounded record gaps
has arbitrarily late actual critical endpoints simultaneously excluding
every rational candidate whose explicit horizon fits the available depth. -/
theorem actual_drought_excludes_moving_rationals {a B : ℕ} {c : Bool}
    (odd : a%2=1) (color : a%3=digit c) (escape : ¬Repeats a)
    (drawdown : BoundedDrawdown a B) (droughts : ¬∃ J, BoundedRecordGaps a J)
    (n R : ℕ) : ∃ k, R ≤ k ∧ n ≤ k ∧ Critical a k ∧
      ∀ (d : ℕ) (A : ℤ), 0 < d → inverseRationalHorizon d (2*B) A ≤ n →
        ¬(3:ℤ)^n∣(d:ℤ)*after k a-A := by
  obtain ⟨w⟩ := drought_exists odd color escape drawdown droughts (max n R)
  have bn : 0 < B := by
    have h := drawdown 0 0 (by omega)
    have one : 1≤B := by simpa [RatioLE,elapsed] using h
    omega
  refine ⟨w.k,(Nat.le_max_right n R).trans w.late,(Nat.le_max_left n R).trans w.late,
    w.record,fun d A dp fit div => ?_⟩
  obtain ⟨j,_,small,high⟩ := actual_record_rational_gain (d:=d) (H:=2*B) (A:=A) odd color dp
    (by omega) w.record (fit.trans ((Nat.le_max_left n R).trans w.late))
    (dvd_trans (pow_dvd_pow (3:ℤ) fit) div)
  exact high (w.cap j (small.trans (fit.trans (Nat.le_max_left n R))))

#print axioms actual_record_rational_gain
#print axioms actual_drought_excludes_moving_rationals
end Collatz.Itinerary.HourEscape
