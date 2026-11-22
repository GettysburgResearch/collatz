module

public import ShellCover

@[expose] public section

/-!
# The finite bit budget for independent repeated blocks

This file checks the discrete closing argument in
`BOUNDED_POWER_LANGUAGES.md`. It does not postulate or formalize Matveev's
theorem. The required logarithmic source-height estimate is an explicit
hypothesis of `bounded_power_length_cap`.

`LocalBudget H spans` says that each block duration is bounded by the
initial budget plus the durations already consumed. This is the exact
recurrence obtained from nonzero repeated-block divisibility and the
ordinary shortcut-step bound on binary height.
-/

namespace CollatzBoundedPower

def LocalBudget (height : Nat) : List Nat → Prop
  | [] => True
  | span :: rest => span ≤ height ∧ LocalBudget (height + span) rest

/-- A nonzero integer divisible by the block's dyadic denominator pays
for that block's complete duration. Here `delta` represents `|D*x-C|`. -/
theorem dyadic_duration_bound (span delta coeff x d h : Nat)
    (hdelta : 0 < delta) (hdiv : 2^span ∣ delta)
    (hsize : delta ≤ coeff * (x+1)) (hcoeff : coeff ≤ 2^d)
    (hheight : x+1 < 2^h) : span < d+h := by
  have lower : 2^span ≤ delta := Nat.le_of_dvd hdelta hdiv
  have upper : delta < 2^(d+h) := by
    calc
      delta ≤ coeff * (x+1) := hsize
      _ ≤ 2^d * (x+1) := Nat.mul_le_mul_right (x+1) hcoeff
      _ < 2^d * 2^h :=
        Nat.mul_lt_mul_of_pos_left hheight (by positivity)
      _ = 2^(d+h) := by rw [pow_add]
  by_contra hbad
  have hexp : d+h ≤ span := by omega
  have hp := Nat.pow_le_pow_right (by decide : 0 < 2) hexp
  omega

/-- A list of independent block durations consumes at most a doubling
budget per block. The extra `height` avoids natural subtraction here. -/
theorem local_budget_sum_add (spans : List Nat) (height : Nat)
    (hbudget : LocalBudget height spans) :
    spans.sum + height ≤ 2^spans.length * height := by
  induction spans generalizing height with
  | nil => simp
  | cons span rest ih =>
    obtain ⟨hspan, hrest⟩ := hbudget
    have tail := ih (height+span) hrest
    have growth : height+span ≤ 2*height := by omega
    calc
      (span :: rest).sum + height = rest.sum + (height+span) := by
        simp only [List.sum_cons]
        omega
      _ ≤ 2^rest.length * (height+span) := tail
      _ ≤ 2^rest.length * (2*height) :=
        Nat.mul_le_mul_left _ growth
      _ = 2^(span :: rest).length * height := by
        simp only [List.length_cons, pow_succ]
        ring

theorem local_budget_sum (spans : List Nat) (height : Nat)
    (hbudget : LocalBudget height spans) :
    spans.sum ≤ (2^spans.length-1)*height := by
  have h := local_budget_sum_add spans height hbudget
  have pos : 0 < 2^spans.length := by positivity
  have split : 2^spans.length = (2^spans.length-1)+1 := by omega
  have rhs : 2^spans.length * height =
      (2^spans.length-1)*height + height := by
    conv_lhs => rw [split]
    ring
  omega

/-- One exact exponential-versus-linear comparison certifies its entire
infinite tail. -/
theorem threshold_add (J q t : Nat) (hq : J*(q+2) ≤ 2^q) :
    J*(q+t+2) ≤ 2^(q+t) := by
  induction t with
  | zero => simpa using hq
  | succ t ih =>
    calc
      J*(q+(t+1)+2) ≤ 2*(J*(q+t+2)) := by nlinarith
      _ ≤ 2*2^(q+t) := Nat.mul_le_mul_left 2 ih
      _ = 2^(q+(t+1)) := by
        rw [show q+(t+1) = (q+t)+1 by omega, pow_succ]
        ring

theorem threshold_of_le (J q p : Nat) (hq : J*(q+2) ≤ 2^q)
    (hqp : q ≤ p) : J*(p+2) ≤ 2^p := by
  have h := threshold_add J q (p-q) hq
  simpa only [Nat.add_sub_of_le hqp] using h

/-- The bit index of a positive length cannot enter the certified tail. -/
theorem dyadic_length_cap (J N p q : Nat) (hJ : 0 < J)
    (hlow : 2^p ≤ N) (hupp : N < 2^(p+1))
    (hlinear : N ≤ J*(p+1)) (hq : J*(q+2) ≤ 2^q) :
    N < 2^q := by
  have hpq : p < q := by
    by_contra hbad
    have hqp : q ≤ p := by omega
    have ht := threshold_of_le J q p hq hqp
    have strict : J*(p+1) < J*(p+2) :=
      Nat.mul_lt_mul_of_pos_left (by omega) hJ
    omega
  have hpow := Nat.pow_le_pow_right (by decide : 0 < 2)
    (show p+1 ≤ q by omega)
  omega

/-- Complete discrete closure. The source-height hypothesis comes from
the separately stated published logarithm bound in the written proof.
No uniform bound on the number of blocks is asserted here. -/
theorem bounded_power_length_cap (spans : List Nat) (height b d K p q : Nat)
    (hK : 0 < K)
    (hbudget : LocalBudget (height+d) spans)
    (hheight : height ≤ b+3*K+1+K*p)
    (hlow : 2^p ≤ spans.sum) (hupp : spans.sum < 2^(p+1))
    (hq : ((2^spans.length-1)*(b+3*K+1+d))*(q+2) ≤ 2^q) :
    spans.sum < 2^q := by
  let A := 2^spans.length-1
  let C := b+3*K+1+d
  have hlen : 0 < spans.length := by
    cases spans with
    | nil =>
      simp only [List.sum_nil] at hlow
      have hp : 0 < 2^p := by positivity
      omega
    | cons span rest => simp
  have hp := Nat.pow_le_pow_right (by decide : 0 < 2) hlen
  have hA : 0 < A := by
    dsimp [A]
    norm_num at hp
    omega
  have hC : 0 < C := by dsimp [C]; omega
  have hJ : 0 < A*C := Nat.mul_pos hA hC
  have hbase := local_budget_sum spans (height+d) hbudget
  have hlinear : spans.sum ≤ (A*C)*(p+1) := by
    have hsmall : height+d ≤ C+K*p := by dsimp [C]; omega
    have hKle : K ≤ C := by dsimp [C]; omega
    have hprod := Nat.mul_le_mul_right p hKle
    calc
      spans.sum ≤ A*(height+d) := hbase
      _ ≤ A*(C+K*p) := Nat.mul_le_mul_left A hsmall
      _ ≤ A*(C+C*p) := Nat.mul_le_mul_left A (by omega)
      _ = (A*C)*(p+1) := by ring
  exact dyadic_length_cap (A*C) spans.sum p q hJ hlow hupp hlinear hq

/-- The exact general-language threshold for the repository's P,Q pair.
This checks the arithmetic bound; it does not itself exclude the family. -/
theorem mixed_pin_threshold :
    (77309411391 : Nat)*(42+2) ≤ 2^42 := by norm_num

#print axioms dyadic_duration_bound
#print axioms local_budget_sum_add
#print axioms local_budget_sum
#print axioms threshold_add
#print axioms threshold_of_le
#print axioms dyadic_length_cap
#print axioms bounded_power_length_cap
#print axioms mixed_pin_threshold

end CollatzBoundedPower
