import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Range

/-!
The complete source block, an actual target survivor, and exact splice legality.

The shortcut map below is the repository's ordinary map.  The source affine
identity and first-hit floor are explicit inputs; no completeness or universal
dispatcher is inferred from a real affine contraction alone.
-/

namespace CollatzDeep.WholeSourceBuffer

def step (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else (3*n+1)/2

def orbit (n : Nat) : Nat → Nat
  | 0 => n
  | k+1 => step (orbit n k)

def odds (n : Nat) : Nat → Nat
  | 0 => 0
  | k+1 => odds n k + if orbit n k % 2 = 0 then 0 else 1

private theorem orbit_add (n a b : Nat) :
    orbit n (a+b) = orbit (orbit n a) b := by
  induction b with
  | zero => simp [orbit]
  | succ b ih =>
    change step (orbit n (a+b)) = step (orbit (orbit n a) b)
    exact congrArg step ih

private theorem orbit_positive (q a : Nat) (positive : 0 < q) :
    0 < orbit q a := by
  induction a with
  | zero => exact positive
  | succ a ih =>
    change 0 < step (orbit q a)
    unfold step
    split_ifs with even <;> omega

private theorem first_hit_distinct (q a : Nat)
    (hit : orbit q a = 1) (first : ∀ j < a, orbit q j ≠ 1)
    {i j : Nat} (ib : i ≤ a) (jb : j ≤ a)
    (same : orbit q i = orbit q j) : i = j := by
  have noEarly : ∀ i j : Nat, i < j → j ≤ a →
      orbit q i ≠ orbit q j := by
    intro i j ordered bounded equality
    have shifted := congrArg (fun z => orbit z (a-j)) equality
    rw [← orbit_add, ← orbit_add] at shifted
    have endClock : j+(a-j) = a := Nat.add_sub_of_le bounded
    rw [endClock, hit] at shifted
    exact first (i+(a-j)) (by omega) shifted
  rcases Nat.lt_trichotomy i j with lt | eq | gt
  · exact False.elim (noEarly i j lt jb same)
  · exact eq
  · exact False.elim (noEarly j i gt ib same.symm)

/-- An actual first-hit source confined to the original floor has at most
L distinct positive states, including its terminal 1. -/
theorem first_hit_clock_bound (q a l : Nat) (positive : 0 < q)
    (hit : orbit q a = 1) (first : ∀ j < a, orbit q j ≠ 1)
    (ceiling : ∀ j ≤ a, orbit q j ≤ l) : a+1 ≤ l := by
  have injective : Set.InjOn (fun j => orbit q j-1) (Finset.range (a+1)) := by
    intro i hi j hj equal
    change i ∈ Finset.range (a+1) at hi
    change j ∈ Finset.range (a+1) at hj
    have ir := Finset.mem_range.mp hi
    have jr := Finset.mem_range.mp hj
    have ib : i ≤ a := by omega
    have jb : j ≤ a := by omega
    have ip := orbit_positive q i positive
    have jp := orbit_positive q j positive
    change orbit q i-1 = orbit q j-1 at equal
    exact first_hit_distinct q a hit first ib jb (by omega)
  have contained : (Finset.range (a+1)).image (fun j => orbit q j-1) ⊆
      Finset.range l := by
    intro value member
    rcases Finset.mem_image.mp member with ⟨j, bounded, rfl⟩
    have jr := Finset.mem_range.mp bounded
    have jb : j ≤ a := by omega
    have top := ceiling j jb
    have bottom := orbit_positive q j positive
    apply Finset.mem_range.mpr
    omega
  have count := Finset.card_le_card contained
  rw [Finset.card_image_of_injOn injective] at count
  simpa only [Finset.card_range] using count

private theorem step_balance (n : Nat) :
    2*step n = if n % 2 = 0 then n else 3*n+1 := by
  by_cases even : n % 2 = 0
  · simp only [step, ite_eq_left even]
    have division := Nat.mod_add_div n 2
    omega
  · simp only [step, ite_eq_right even]
    have modBound := Nat.mod_lt n (by decide : 0 < 2)
    have parity : n % 2 = 1 := by omega
    have zeroMod : (3*n+1) % 2 = 0 := by omega
    have division := Nat.mod_add_div (3*n+1) 2
    omega

private theorem scaled_step_even (n k : Nat)
    (even : orbit n k % 2 = 0) :
    2^(k+1)*orbit n (k+1) = 2^k*orbit n k := by
  have balance := step_balance (orbit n k)
  simp only [ite_eq_left even] at balance
  change 2^(k+1)*step (orbit n k) = _
  rw [pow_succ]
  calc
    2^k*2*step (orbit n k) = 2^k*(2*step (orbit n k)) := by ring
    _ = 2^k*orbit n k := by rw [balance]

private theorem scaled_step_odd (n k : Nat)
    (odd : orbit n k % 2 ≠ 0) :
    2^(k+1)*orbit n (k+1) = 3*(2^k*orbit n k)+2^k := by
  have balance := step_balance (orbit n k)
  simp only [ite_eq_right odd] at balance
  change 2^(k+1)*step (orbit n k) = _
  rw [pow_succ]
  calc
    2^k*2*step (orbit n k) = 2^k*(2*step (orbit n k)) := by ring
    _ = 3*(2^k*orbit n k)+2^k := by rw [balance]; ring

private theorem survivor_potential (t a : Nat)
    (survives : ∀ j ≤ a, t ≤ orbit t j) :
    (3*t+1)*3^(odds t a)*t + a*(2^a*orbit t a) ≥
      (3*t+1)*(2^a*orbit t a) := by
  induction a with
  | zero => simp [orbit, odds]
  | succ a ih =>
    have old := ih (fun j bound => survives j (by omega))
    have lower : t*2^a ≤ 2^a*orbit t a := by
      have h := Nat.mul_le_mul_left (2^a) (survives a (by omega))
      nlinarith [Nat.zero_le (2^a*orbit t a)]
    by_cases even : orbit t a % 2 = 0
    · have scaled := scaled_step_even t a even
      have count : odds t (a+1) = odds t a := by simp [odds, even]
      rw [count, scaled]
      nlinarith [Nat.zero_le (2^a*orbit t a)]
    · have scaled := scaled_step_odd t a even
      have count : odds t (a+1) = odds t a+1 := by simp [odds, even]
      rw [count, pow_succ, scaled]
      nlinarith [Nat.zero_le (a*2^a)]

/-- Every actual target prefix staying above its starting value has this
exact coefficient budget; the additive errors are charged to the original t. -/
theorem survivor_coefficient_budget (t a : Nat) (positive : 0 < t)
    (survives : ∀ j ≤ a, t ≤ orbit t j) (short : a ≤ 3*t+1) :
    (3*t+1-a)*2^a ≤ (3*t+1)*3^(odds t a) := by
  have potential := survivor_potential t a survives
  have split : 3*t+1-a+a = 3*t+1 := Nat.sub_add_cancel short
  have lower := Nat.mul_le_mul_left ((3*t+1-a)*2^a) (survives a le_rfl)
  have expanded : (3*t+1-a)*2^a*orbit t a + a*(2^a*orbit t a) =
      (3*t+1)*(2^a*orbit t a) := by
    calc
      _ = (3*t+1-a+a)*(2^a*orbit t a) := by ring
      _ = _ := by rw [split]
  have scaled : ((3*t+1-a)*2^a)*t ≤ ((3*t+1)*3^(odds t a))*t := by
    nlinarith
  exact Nat.le_of_mul_le_mul_right scaled positive

/-- In a clock shorter than half the original target, survival forces a
homogeneous multiplier strictly greater than 5/6. -/
theorem short_survivor_coefficient (t a : Nat) (positive : 0 < t)
    (survives : ∀ j ≤ a, t ≤ orbit t j) (short : 2*a < t) :
    5*2^a < 6*3^(odds t a) := by
  have clockBound : a ≤ 3*t+1 := by omega
  have budget := survivor_coefficient_budget t a positive survives clockBound
  have split : 3*t+1-a+a = 3*t+1 := Nat.sub_add_cancel clockBound
  have ppos : 0 < 2^a := Nat.pow_pos (by decide)
  have margin : 6*a < 3*t+1 := by omega
  by_contra contrary
  have reverse : 6*3^(odds t a) ≤ 5*2^a := by omega
  have weighted := Nat.mul_le_mul_left (3*t+1) reverse
  have gap := Nat.mul_lt_mul_of_pos_right margin ppos
  nlinarith

/-- A complete source identity and a short surviving actual target force a
logarithmic surplus of target odd events: 3^(o-r) > 5q/6.  This displayed
natural-number version does not use subtraction of exponents. -/
theorem complete_source_survivor_surplus (q t r a c : Nat)
    (targetPositive : 0 < t) (correctionPositive : 0 < c)
    (completeSource : 3^r*q+c = 2^a)
    (survives : ∀ j ≤ a, t ≤ orbit t j) (short : 2*a < t) :
    5*3^r*q < 6*3^(odds t a) := by
  have bound := short_survivor_coefficient t a targetPositive survives short
  nlinarith

/-- The joint witness's actual first-hit source and original-target floor
supply the short clock internally. Every target surviving the WHOLE source
word must then have the displayed strict odd-count surplus. -/
theorem joint_source_survivor_surplus (q t r a c : Nat)
    (sourcePositive : 0 < q) (targetPositive : 0 < t)
    (correctionPositive : 0 < c) (completeSource : 3^r*q+c = 2^a)
    (sourceHit : orbit q a = 1)
    (sourceFirst : ∀ j < a, orbit q j ≠ 1)
    (sourceFloor : ∀ j ≤ a, orbit q j ≤ (t-1)/2)
    (targetSurvives : ∀ j ≤ a, t ≤ orbit t j) :
    5*3^r*q < 6*3^(odds t a) := by
  have clock := first_hit_clock_bound q a ((t-1)/2)
    sourcePositive sourceHit sourceFirst sourceFloor
  have short : 2*a < t := by omega
  exact complete_source_survivor_surplus q t r a c targetPositive
    correctionPositive completeSource targetSurvives short

/-- Completing the whole source gives a strict real coefficient contraction
whose fixed point lies between zero and one.  For every captured target the
formal whole-block affine numerator is below 17 times its denominator.  This
does not identify that affine branch with the target's actual parity branch. -/
theorem complete_source_buffer (q t r a c : Nat)
    (sourceNontrivial : 1 < q) (correctionPositive : 0 < c)
    (completeSource : 3^r*q+c = 2^a) (capture : t ≤ 16*q+1) :
    3^r < 2^a ∧ c < 2^a-3^r ∧ 3^r*t+c < 17*2^a := by
  have qpos : 0 < 3^r := Nat.pow_pos (by decide)
  have strict : 3^r < 2^a := by nlinarith
  have split : 2^a-3^r+3^r = 2^a := Nat.sub_add_cancel (by omega)
  have captured := Nat.mul_le_mul_left (3^r) capture
  constructor
  · exact strict
  constructor <;> nlinarith

/-- For a fixed affine parity prefix, an endpoint below the actual target
endpoint cannot have a positive predecessor when the binary modulus exceeds
the target. This checks the full congruence obstruction, without assuming
that real affine pullback preserves the integer parity cylinder. -/
theorem positive_splice_impossible (t u n v a o c : Nat)
    (binaryBeyond : t < 2^a) (endpointBelow : v < n)
    (targetIdentity : 3^o*t+c = 2^a*n)
    (spliceIdentity : 3^o*u+c = 2^a*v) (sourcePositive : 0 < u) : False := by
  have ppos : 0 < 2^a := Nat.pow_pos (by decide)
  have qpos : 0 < 3^o := Nat.pow_pos (by decide)
  have endpointScaled := Nat.mul_lt_mul_of_pos_left endpointBelow ppos
  have startBelow : u < t := by nlinarith
  have tSplit : t-u+u = t := Nat.sub_add_cancel (by omega)
  have nSplit : n-v+v = n := Nat.sub_add_cancel (by omega)
  have difference : 3^o*(t-u) = 2^a*(n-v) := by nlinarith
  have productDivides : 2^a ∣ 3^o*(t-u) := ⟨n-v, difference⟩
  have coprime : Nat.Coprime (2^a) (3^o) :=
    (by decide : Nat.Coprime 2 3).pow a o
  have divides : 2^a ∣ t-u := coprime.dvd_of_dvd_mul_left productDivides
  have lower := Nat.le_of_dvd (by omega : 0 < t-u) divides
  omega

/-- The canonical complete source has at least five odd steps and captures
t≤16q+1. Its full target prefix cannot be spliced to any supplied source
endpoint below t while retaining a positive integer starting source. -/
theorem whole_source_splice_impossible (q t u n v r a o c d : Nat)
    (sourcePositive : 0 < q) (correctionPositive : 0 < c)
    (sourceDepth : 5 ≤ r) (capture : t ≤ 16*q+1)
    (completeSource : 3^r*q+c = 2^a)
    (survival : t ≤ n) (endpointBelow : v < t)
    (targetIdentity : 3^o*t+d = 2^a*n)
    (spliceIdentity : 3^o*u+d = 2^a*v) (splicePositive : 0 < u) : False := by
  have powerBound : 243 ≤ 3^r := by
    have h := Nat.pow_le_pow_right (by decide : 0 < 3) sourceDepth
    norm_num at h
    exact h
  have weighted := Nat.mul_le_mul_right q powerBound
  have binaryBeyond : t < 2^a := by nlinarith
  exact positive_splice_impossible t u n v a o d binaryBeyond
    (by omega) targetIdentity spliceIdentity splicePositive

#print axioms first_hit_clock_bound
#print axioms survivor_coefficient_budget
#print axioms short_survivor_coefficient
#print axioms complete_source_survivor_surplus
#print axioms joint_source_survivor_surplus
#print axioms complete_source_buffer
#print axioms positive_splice_impossible
#print axioms whole_source_splice_impossible

end CollatzDeep.WholeSourceBuffer
