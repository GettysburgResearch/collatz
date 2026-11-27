module
public import ReturnOrbitRecords
import all ReturnOrbitBinary
import all ReturnOrbitTernary
import all HourEscapeBranching
import all HourCycleShadow
import all FixedGate
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.HourEscape
open FixedGate EscapeRecords Collatz.HourCycleShadow
set_option autoImplicit false

/-- Absolute constants, kept factored so the integer inequalities are usable
without writing out the decimal expansions. -/
def censusConstant : ℕ := (76*10^10)^20*(3^200*4*10^2)^19
def recordGainConstant : ℕ := 31*(censusConstant+1)

set_option exponentiation.threshold 4096 in
/-- The inverse precision is polynomial jointly in the clock width and
denominator and linear in the absolute value of the rational coordinate. -/
theorem inverse_horizon_polynomial {d H : ℕ} (A : ℤ) (hp : 0<H) :
    inverseRationalHorizon d H A ≤
      recordGainConstant*H^718*(A.natAbs/d+1+d^19) := by
  let Y := A.natAbs/d+1
  have h₄ : 1≤H^4 := Nat.one_le_pow _ _ hp
  have h₇ : 1≤H^714 := Nat.one_le_pow _ _ hp
  have head : 30*H^4+1≤31*H^4 := by omega
  have coefficient : (76*(10*H^3)^10)^20*((3^200)*(4*(10*H^3)^2*d))^19=
      censusConstant*H^714*d^19 := by
    unfold censusConstant
    ring
  have scaled : Y≤(censusConstant+1)*H^714*Y := by
    have lo : 1≤(censusConstant+1)*H^714 := Nat.mul_pos (Nat.succ_pos _) h₇
    simpa only [Nat.one_mul] using Nat.mul_le_mul_right Y lo
  have cd : censusConstant*H^714*d^19≤(censusConstant+1)*H^714*d^19 :=
    Nat.mul_le_mul_right _ (Nat.mul_le_mul_right _ (Nat.le_succ _))
  have sample : rationalSample d (10*H^3) A≤(censusConstant+1)*H^714*(Y+d^19) := by
    unfold rationalSample
    rw [coefficient,Nat.mul_add]
    exact Nat.add_le_add scaled cd
  unfold inverseRationalHorizon
  calc
    _ ≤ 31*H^4*((censusConstant+1)*H^714*(Y+d^19)) := Nat.mul_le_mul head sample
    _ = _ := by change _=31*(censusConstant+1)*H^718*(Y+d^19); ring

/-- A fixed ordinary critical record agreeing through n ternary digits
with a moving rational must exhibit a polynomially large recent gain. -/
theorem polynomial_gain_at_ordinary_record {a k n d H : ℕ} {A : ℤ} {c : Bool}
    (odd : a%2=1) (color : a%3=digit c) (dp : 0<d) (hp : 0<H)
    (record : Critical a k) (enough : n≤k)
    (budget : recordGainConstant*H^718*(A.natAbs/d+1+d^19)≤n)
    (congruent : (3:ℤ)^n∣(d:ℤ)*after k a-A) :
    ∃ j, 0<j ∧ j≤n ∧ ¬RatioLE a H k (k-j) := by
  have room := (inverse_horizon_polynomial (d:=d) A hp).trans budget
  obtain ⟨j,pos,len,gain⟩ := actual_record_rational_gain odd color dp hp record (room.trans enough)
    (dvd_trans (pow_dvd_pow (3:ℤ) room) congruent)
  exact ⟨j,pos,len.trans room,gain⟩

#print axioms inverse_horizon_polynomial
#print axioms polynomial_gain_at_ordinary_record

/-- On every fixed ordinary odd unit orbit, its own integral starting state
forces an explicit two-sided clock excursion. This statement has no residue,
height, escape, or nonrepetition premise. -/
theorem fixed_ordinary_clock_excursion {a K : ℕ} {c : Bool} (odd : a%2=1)
    (color : a%3=digit c) (kp : 0<K) :
    ∃ j, j≤rationalHorizon 1 K (a:ℤ) ∧
      (K*3^j<2^(elapsed j a) ∨ K*2^(elapsed j a)<3^j) := by
  let e := gapAt a
  let y := fun i => (after i a:ℤ)
  have state (i : ℕ) : after i a%2=1 := (route_exists i a odd color).choose_spec.2.2.1
  have epos (i : ℕ) : 0<e i := (next_gap (state i)).pos
  have y0 : y 0=(a:ℤ) := rfl
  have step (i : ℕ) : (2:ℤ)^(e i)*y (i+1)=3*y i+1 := by
    have g := (next_gap (state i)).eqn
    have nxt : after (i+1) a=(next (after i a)).2 := by rw [after_add]; rfl
    rw [←nxt] at g
    change (2:ℤ)^((next (after i a)).1)*(after (i+1) a:ℤ)=3*(after i a:ℤ)+1
    exact_mod_cast g
  have clock (i : ℕ) : total e i=elapsed i a := by
    induction i with
    | zero => rfl
    | succ i ih => rw [total,ih,snoc_clock]; rfl
  by_contra! all
  apply finite_dyadic_rational_rigidity (d:=1) (K:=K) (e:=e) (y:=y) kp (by decide) epos
    (fun i _ => step i) (fun i _ => by change (after i a:ℤ)%2=1; exact_mod_cast state i)
  intro i hi
  rw [y0] at hi
  obtain ⟨low,high⟩ := all i hi
  rw [weight_formula,clock]
  have lo : (2:ℝ)^(elapsed i a)≤K*3^i := by exact_mod_cast low
  have up : (3:ℝ)^i≤K*2^(elapsed i a) := by exact_mod_cast high
  have pos : 0<(2:ℝ)^(elapsed i a) := by positivity
  constructor
  · rw [←mul_div_assoc]
    exact (le_div_iff₀ pos).mpr (by simpa using lo)
  · exact (div_le_iff₀ pos).mpr up

#print axioms fixed_ordinary_clock_excursion
end Collatz.Itinerary.HourEscape
