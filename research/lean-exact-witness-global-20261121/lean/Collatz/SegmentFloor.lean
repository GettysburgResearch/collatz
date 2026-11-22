/-
Finite integer estimates for the S-unit sparse-endpoint attack.

A supplied positive-gap segment stays on its actual ordinary orbit. If all
its odd inputs exceed a floor M, the full affine correction is O(1/M)
relative to its initial value, for each fixed number of odd events. No
S-unit theorem, asymptotic density assertion, or analytic assumption is imported.
-/
import Collatz.SignedShadow

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzHighGapPump
open CollatzUnboundedGapReset

set_option autoImplicit false
set_option maxHeartbeats 1000000

namespace CollatzSegmentFloor

/-- An actual integral positive-gap segment, with its floor imposed at each
odd input. The final endpoint need not itself be an odd input. -/
inductive FloorPrefix (floor : Nat) : Nat → List Nat → Nat → Prop
  | nil (n : Nat) : FloorPrefix floor n [] n
  | cons {n middle endpoint a : Nat} {tail : List Nat}
      (above : floor ≤ n) (positiveGap : 0 < a)
      (edge : 3*n+1=2^a*middle)
      (rest : FloorPrefix floor middle tail endpoint) :
      FloorPrefix floor n (a::tail) endpoint

theorem to_prefix {floor n endpoint : Nat} {word : List Nat}
    (path : FloorPrefix floor n word endpoint) : Prefix n word endpoint := by
  induction path with
  | nil n => simp [Prefix, PositiveGaps, correction, total]
  | @cons n middle endpoint a tail above positiveGap edge rest ih =>
    exact (prefix_cons_iff n a endpoint tail).mpr ⟨positiveGap,middle,edge,ih⟩

/-- Every segment in the floor certificate is an actual ordinary prefix. -/
theorem actual_orbit {floor n endpoint : Nat} {word : List Nat}
    (path : FloorPrefix floor n word endpoint) :
    orbit n (total word)=endpoint :=
  CollatzSignedShadow.prefix_orbit (to_prefix path)

/-- A floor on the specified finite ordinary clock supplies the same floor
on every literal odd input of the given positive-gap prefix. -/
theorem of_bounded_orbit_floor {floor n endpoint : Nat} {word : List Nat}
    (path : Prefix n word endpoint)
    (above : ∀ k, k<total word → floor ≤ orbit n k) :
    FloorPrefix floor n word endpoint := by
  induction word generalizing n with
  | nil =>
    have same : n=endpoint := by simpa [correction,total] using path.2
    subst endpoint
    exact .nil n
  | cons a tail ih =>
    obtain ⟨positiveGap,middle,edge,rest⟩ :=
      (prefix_cons_iff n a endpoint tail).mp path
    have first : Prefix n [a] middle :=
      (prefix_cons_iff n a middle []).mpr
        ⟨positiveGap,middle,edge,by simp [Prefix,PositiveGaps,correction,total]⟩
    have reached : orbit n a=middle := by
      simpa [total] using CollatzSignedShadow.prefix_orbit first
    have startBound := above 0 (by simp only [total]; omega)
    apply FloorPrefix.cons (by simpa [orbit] using startBound) positiveGap edge
    apply ih rest
    intro k before
    have later := above (a+k) (by simp only [total]; omega)
    simpa [orbit_add,reached] using later

theorem of_orbit_floor {floor n endpoint : Nat} {word : List Nat}
    (path : Prefix n word endpoint)
    (above : ∀ k, floor ≤ orbit n k) : FloorPrefix floor n word endpoint :=
  of_bounded_orbit_floor path (fun k _ => above k)

/-- Exact integer version of the multiplicative product estimate.
After cancelling the positive initial state and the relevant powers of M,
this is the usual product of the factors 1+1/(3*n_i). -/
theorem product_bound {floor n endpoint : Nat} {word : List Nat}
    (path : FloorPrefix floor n word endpoint) :
    floor^word.length * 2^total word * endpoint ≤
      (3*floor+1)^word.length * n := by
  induction path with
  | nil n => simp [total]
  | @cons n middle endpoint a tail above positiveGap edge rest ih =>
    have edgeBound : floor * 2^a * middle ≤ (3*floor+1)*n := by
      calc
        floor * 2^a * middle = floor*(3*n+1) := by rw [Nat.mul_assoc,←edge]
        _ ≤ (3*floor+1)*n := by grind
    simp only [List.length_cons,total,Nat.pow_succ,Nat.pow_add]
    calc
      floor^tail.length*floor*(2^a*2^total tail)*endpoint =
          (floor*2^a)*(floor^tail.length*2^total tail*endpoint) := by ac_rfl
      _ ≤ (floor*2^a)*((3*floor+1)^tail.length*middle) :=
          Nat.mul_le_mul_left _ ih
      _ = (3*floor+1)^tail.length*(floor*2^a*middle) := by ac_rfl
      _ ≤ (3*floor+1)^tail.length*((3*floor+1)*n) :=
          Nat.mul_le_mul_left _ edgeBound
      _ = _ := by ac_rfl

/-- The same estimate retains the full affine correction instead of
replacing the segment by its linear coefficient. -/
theorem correction_product_bound {floor n endpoint : Nat} {word : List Nat}
    (path : FloorPrefix floor n word endpoint) :
    (3*floor)^word.length*n + floor^word.length*correction word ≤
      (3*floor+1)^word.length*n := by
  have bound := product_bound path
  have identity := (to_prefix path).2
  calc
    (3*floor)^word.length*n + floor^word.length*correction word =
        floor^word.length*(3^word.length*n+correction word) := by
          rw [Nat.mul_pow]
          grind
    _ = floor^word.length*(2^total word*endpoint) := by rw [identity]
    _ ≤ _ := by simpa [Nat.mul_assoc] using bound

/-- A simple explicit O(1/M) bound, uniform over every legal valuation
word of the specified length, with no bound on its individual gaps. -/
theorem correction_bound {floor n endpoint : Nat} {word : List Nat}
    (path : FloorPrefix floor n word endpoint) (positiveFloor : 0<floor) :
    floor*correction word ≤ n*word.length*4^word.length := by
  induction path with
  | nil n => simp [correction]
  | @cons n middle endpoint a tail above positiveGap edge rest ih =>
    have npositive : 0<n := by omega
    have growth : 2^a*middle≤4*n := by omega
    have threeFour : 3^tail.length≤4^tail.length :=
      Nat.pow_le_pow_left (by decide) _
    have first : floor*3^tail.length≤n*4^tail.length :=
      Nat.mul_le_mul above threeFour
    have second : 2^a*(floor*correction tail)≤
        4*n*tail.length*4^tail.length := by
      calc
        2^a*(floor*correction tail) ≤ 2^a*(middle*tail.length*4^tail.length) :=
          Nat.mul_le_mul_left _ ih
        _ = (2^a*middle)*(tail.length*4^tail.length) := by ac_rfl
        _ ≤ (4*n)*(tail.length*4^tail.length) :=
          Nat.mul_le_mul_right _ growth
        _ = _ := by ac_rfl
    simp only [correction,List.length_cons,Nat.pow_succ]
    calc
      floor*(3^tail.length+2^a*correction tail) =
          floor*3^tail.length+2^a*(floor*correction tail) := by grind
      _ ≤ n*4^tail.length+4*n*tail.length*4^tail.length :=
          Nat.add_le_add first second
      _ ≤ n*(tail.length+1)*(4^tail.length*4) := by grind

/-- A sharper bound with the exact geometric difference retained. It is
sharp on repetitions of the positive fixed odd state one. -/
theorem correction_sharp_bound {floor n endpoint : Nat} {word : List Nat}
    (path : FloorPrefix floor n word endpoint) (positiveFloor : 0<floor) :
    floor*correction word + 3^word.length*n ≤ 4^word.length*n := by
  induction path with
  | nil n => simp [correction]
  | @cons n middle endpoint a tail above positiveGap edge rest ih =>
    have scaled := Nat.mul_le_mul_left (2^a) ih
    have transported : 2^a*(floor*correction tail) +
        3^tail.length*(3*n+1) ≤ 4^tail.length*(3*n+1) := by
      calc
        2^a*(floor*correction tail) + 3^tail.length*(3*n+1) =
            2^a*(floor*correction tail + 3^tail.length*middle) := by rw [edge]; grind
        _ ≤ 2^a*(4^tail.length*middle) := scaled
        _ = 4^tail.length*(3*n+1) := by rw [edge]; ac_rfl
    have threeFour : 3^tail.length≤4^tail.length :=
      Nat.pow_le_pow_left (by decide) _
    have extra := Nat.mul_le_mul_left (floor-1) threeFour
    have floorFactor : floor=(floor-1)+1 := by omega
    have last : (3*n+floor)*4^tail.length ≤ 4*n*4^tail.length :=
      Nat.mul_le_mul_right _ (by omega)
    simp only [correction,List.length_cons,Nat.pow_succ]
    calc
      floor*(3^tail.length+2^a*correction tail) + 3^tail.length*3*n =
          (2^a*(floor*correction tail) + 3^tail.length*(3*n+1)) +
            (floor-1)*3^tail.length := by grind
      _ ≤ 4^tail.length*(3*n+1)+(floor-1)*4^tail.length :=
        Nat.add_le_add transported extra
      _ = (3*n+floor)*4^tail.length := by grind
      _ ≤ 4*n*4^tail.length := last
      _ = _ := by ac_rfl

/-- Any supplied positive lower bound for the normalized correction forces
failure of an explicit all-input floor. This is the finite arithmetic step
used after a nondegenerate S-unit cluster has supplied that lower bound. -/
theorem correction_forces_floor_failure {floor n endpoint numerator denominator : Nat}
    {word : List Nat} (path : FloorPrefix floor n word endpoint)
    (positiveFloor : 0<floor) (positiveStart : 0<n)
    (correctionLarge : numerator*n ≤ denominator*correction word)
    (floorLarge : denominator*word.length*4^word.length < numerator*floor) : False := by
  have upper := Nat.mul_le_mul_left denominator (correction_bound path positiveFloor)
  have lower := Nat.mul_le_mul_left floor correctionLarge
  have strict := Nat.mul_lt_mul_of_pos_right floorLarge positiveStart
  have first : numerator*floor*n ≤ denominator*(floor*correction word) := by
    simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using lower
  have last : denominator*(n*word.length*4^word.length) < numerator*floor*n := by
    simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using strict
  omega

/-- The floor failure is on this same original orbit, without resetting the
source or replacing the actual path by a freely chosen residue word. -/
theorem actual_return_below_floor {floor n endpoint numerator denominator : Nat}
    {word : List Nat} (path : Prefix n word endpoint)
    (positiveFloor : 0<floor) (positiveStart : 0<n)
    (correctionLarge : numerator*n ≤ denominator*correction word)
    (floorLarge : denominator*word.length*4^word.length < numerator*floor) :
    ∃ k, k<total word ∧ orbit n k<floor := by
  classical
  apply Classical.byContradiction
  intro absent
  have above : ∀ k, k<total word → floor≤orbit n k := by
    intro k before
    apply Classical.byContradiction
    intro below
    exact absent ⟨k,before,by omega⟩
  exact correction_forces_floor_failure (of_bounded_orbit_floor path above)
    positiveFloor positiveStart correctionLarge floorLarge

/-- The explicit floor used by the written S-unit theorem. A positive
ratio at least 1/Q between the correction and the initial leading term
forces a visit below Q*2^h during this very supplied segment. -/
theorem ratio_forces_return {n endpoint denominator : Nat} {word : List Nat}
    (path : Prefix n word endpoint) (positiveStart : 0<n)
    (positiveDenominator : 0<denominator)
    (large : 3^word.length*n ≤ denominator*correction word) :
    ∃ k, k<total word ∧ orbit n k<denominator*2^word.length := by
  classical
  apply Classical.byContradiction
  intro absent
  have above : ∀ k, k<total word → denominator*2^word.length≤orbit n k := by
    intro k before
    apply Classical.byContradiction
    intro lower
    exact absent ⟨k,before,by omega⟩
  have floorPositive : 0<denominator*2^word.length :=
    Nat.mul_pos positiveDenominator (Nat.pow_pos (by decide))
  have budget := correction_sharp_bound (of_bounded_orbit_floor path above) floorPositive
  have scaled := Nat.mul_le_mul_left (2^word.length) large
  have fourSix : 4^word.length≤6^word.length :=
    Nat.pow_le_pow_left (by decide) _
  have compared : 4^word.length*n ≤ 2^word.length*(3^word.length*n) := by
    calc
      4^word.length*n ≤ 6^word.length*n := Nat.mul_le_mul_right _ fourSix
      _ = 2^word.length*(3^word.length*n) := by
        rw [←Nat.mul_assoc,←Nat.mul_pow]
  have lower : 4^word.length*n ≤
      (denominator*2^word.length)*correction word := by
    apply Nat.le_trans compared
    simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using scaled
  have positive : 0<3^word.length*n :=
    Nat.mul_pos (Nat.pow_pos (by decide)) positiveStart
  omega

end CollatzSegmentFloor
