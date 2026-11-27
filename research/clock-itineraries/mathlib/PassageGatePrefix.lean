module

public import PassageGatePacking
public import FixedGate
import all PassageGatePacking
import all HourTower
import all FixedGate
import all TernaryItinerary
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.PassageGate

open FixedGate HourTower Finset
set_option autoImplicit false

private theorem append_count (i j x : ℕ) : count (i+j) x=count i x+count j (run i x) := by
  induction i generalizing x with
  | zero => simp [run,count]
  | succ i ih => rw [Nat.succ_add,count,ih,count,run]; omega

private theorem no_odd_on_halvings (r y : ℕ) : count r (2^r*y)=0 := by
  induction r with
  | zero => rfl
  | succ r ih =>
    rw [pow_succ,Nat.mul_right_comm,show 2^r*y*2=2*(2^r*y) by omega,count]
    simpa [step] using ih

private theorem odd_on_partial_gap {e x y k : ℕ} (g : Gap e x y) (pos : 0<k) (le : k≤e) :
    count k x=1 := by
  obtain ⟨E,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt g.pos)
  obtain ⟨j,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt pos)
  have eqn := g.eqn
  rw [pow_succ,Nat.mul_right_comm] at eqn
  have move : step x=2^E*y := by simp [step,g.oddSource]; omega
  have sub : j+(E-j)=E := by omega
  have rest : count j (2^E*y)=0 := by
    rw [←sub,pow_add,mul_assoc]
    exact no_odd_on_halvings j _
  simp [count,move,rest,g.oddSource]

/-- By the first k native ticks, precisely count k x complete odd
departures have started. Their total exact clock is already at least k. -/
theorem closing_odd_date {x n k : ℕ} (odd : x%2=1) (within : k≤elapsed n x) :
    count k x≤n ∧ k≤elapsed (count k x) x := by
  induction n generalizing x k with
  | zero =>
    obtain rfl : k=0 := by simpa [elapsed] using within
    simp [count,elapsed]
  | succ n ih =>
    have g := next_gap odd
    let e := (next x).1
    by_cases stop : k≤e
    · by_cases zero : k=0
      · simp [zero,count,elapsed]
      · have c := odd_on_partial_gap g (by omega : 0<k) stop
        rwa [c,show elapsed 1 x=e by simp [elapsed,e],and_iff_right (by omega)]
    · have eqn : k=e+(k-e) := by omega
      have rest : k-e≤elapsed n (next x).2 := by
        change k ≤ e + elapsed n (next x).2 at within
        omega
      obtain ⟨size,lower⟩ := ih g.oddTarget rest
      have cs : count k x=count (k-e) (next x).2+1 := by
        conv => lhs; rw [eqn,append_count,g.follow,odd_on_partial_gap g g.pos le_rfl]
        omega
      rw [cs,elapsed]
      change _ ∧ k ≤ e + elapsed _ _
      omega

private theorem elapsed_add (i j x : ℕ) : elapsed (i+j) x=elapsed i x+elapsed j (after i x) := by
  induction i generalizing x with
  | zero => simp [elapsed,after]
  | succ i ih => rw [Nat.succ_add,elapsed,ih,elapsed,after]; omega

/-- Full prefix gate, including binary cutoffs in the middle of a long
single exponent. The final inequality tracks all remaining excess
after completing the gap at the cutoff. -/
theorem stopped_shell {x n k : ℕ} (odd : x%2=1) (within : k≤elapsed n x)
    (gate : ∀ j≤n, 4*elapsed j x≤7*j) :
    (∀ h≤k, 4*h≤7*count h x) ∧
    count k x≤n ∧
    elapsed (n-count k x) (after (count k x) x)+k ≤ elapsed n x := by
  obtain ⟨le,clock⟩ := closing_odd_date odd within
  refine ⟨fun h hk => ?_,le,?_⟩
  · obtain ⟨grade,ticks⟩ := closing_odd_date odd (le_trans hk within)
    have cap := gate (count h x) grade
    omega
  · have split := elapsed_add (count k x) (n-count k x) x
    rw [Nat.add_sub_of_le le] at split
    omega

/-- Start with a nonnegative bank. Each odd native tick deposits
three units; an even tick spends four and uses one of the allowed b. -/
def prefixOK : ℕ → ℕ → ℕ → ℕ → Bool
  | 0, _, _, _ => true
  | k+1, credit,b,x =>
    if x%2=1 then prefixOK k (credit+3) b (step x)
    else decide (4≤credit ∧ 0<b) && prefixOK k (credit-4) (b-1) (step x)

def ballotCount : ℕ → ℕ → ℕ → ℕ
  | 0, _, _ => 1
  | k+1, credit,b =>
    ballotCount k (credit+3) b +
      if 4≤credit ∧ 0<b then ballotCount k (credit-4) (b-1) else 0

theorem prefixOK_iff (k credit b x : ℕ) :
    prefixOK k credit b x=true ↔
      (∀ i≤k, 4*i≤credit+7*count i x) ∧ k≤b+count k x := by
  induction k generalizing credit b x with
  | zero => simp [prefixOK,count]
  | succ k ih =>
    have split (c : ℕ) :
        (∀ i≤k+1, 4*i≤c+7*count i x) ↔
        (∀ i≤k, 4*(i+1)≤c+7*(count i (step x)+x%2)) := by
      constructor
      · intro h i hi
        exact h (i+1) (by omega)
      · intro h i hi
        cases i with
        | zero => simp [count]
        | succ i => exact h i (by omega)
    rw [split]
    by_cases odd : x%2=1
    · simp only [prefixOK,odd,↓reduceIte,ih,count]
      constructor
      · rintro ⟨h,t⟩
        exact ⟨fun i hi => by have := h i hi; omega,by omega⟩
      · rintro ⟨h,t⟩
        exact ⟨fun i hi => by have := h i hi; omega,by omega⟩
    · have even : x%2=0 := by omega
      have branch : prefixOK (k+1) credit b x =
          (decide (4≤credit ∧ 0<b) && prefixOK k (credit-4) (b-1) (step x)) := by
        rw [prefixOK,ite_eq_right odd]
      rw [branch,Bool.and_eq_true,decide_eq_true_eq,ih]
      simp only [count,even,Nat.add_zero]
      have limited := count_le k (step x)
      constructor
      · rintro ⟨⟨bank,room⟩,h,t⟩
        exact ⟨fun i hi => by have := h i hi; omega,by omega⟩
      · rintro ⟨h,t⟩
        have first := h 0 (Nat.zero_le _)
        simp [count] at first
        refine ⟨⟨by omega,by omega⟩,fun i hi => ?_,by omega⟩
        have := h i hi
        omega

/-- Exact killed-binomial census for every translated native packet
with odd stride. This can be evaluated with the integer recurrence. -/
theorem prefix_census (k credit b a s : ℕ) (odd : s%2=1) :
    (∑ t ∈ range (2^k), if prefixOK k credit b (a+s*t) then 1 else 0)=
      ballotCount k credit b := by
  induction k generalizing credit b a s with
  | zero => simp [prefixOK,ballotCount]
  | succ k ih =>
    have arm (z : ℕ) :
        (∑ t ∈ range (2^k), if prefixOK (k+1) credit b (z+2*(s*t)) then 1 else 0)=
          if z%2=1 then ballotCount k (credit+3) b
          else if 4≤credit ∧ 0<b then ballotCount k (credit-4) (b-1) else 0 := by
      have phase (t : ℕ) : (z+2*(s*t))%2=z%2 := by omega
      by_cases zo : z%2=1
      · have three : (3*s)%2=1 := by simp [Nat.mul_mod,odd]
        simp only [prefixOK,phase,zo,↓reduceIte,affine_branch]
        exact ih (credit+3) b (step z) (3*s) three
      · have ze : z%2=0 := by omega
        by_cases room : 4≤credit ∧ 0<b
        · simp only [prefixOK,phase,↓reduceIte,room,
            affine_branch,ze]
          exact ih (credit-4) (b-1) (step z) s odd
        · simp [prefixOK,phase,zo,room]
    rw [pow_succ,Nat.mul_comm (2^k) 2,split_sum]
    have first (t : ℕ) : a+s*(2*t)=a+2*(s*t) := by ac_rfl
    have second (t : ℕ) : a+s*(2*t+1)=a+s+2*(s*t) := by
      rw [Nat.mul_add,Nat.mul_one]; ac_rfl
    simp only [first,second,arm,ballotCount]
    by_cases ao : a%2=1
    · simp [ao,show ¬(a+s)%2=1 by omega]
    · simp [ao,show (a+s)%2=1 by omega,Nat.add_comm]

#print axioms closing_odd_date
#print axioms stopped_shell
#print axioms prefixOK_iff
#print axioms prefix_census
end Collatz.Itinerary.PassageGate
