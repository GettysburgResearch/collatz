/-!
The arithmetic budget of repeating one fixed inverse exponent block.
All variables are ordinary integers. No 3-adic completion or convergence
assumption enters the divisibility theorem.
-/

namespace CollatzDiscretePump

/-- The integer distance, after clearing its denominator, from the fixed
point of the inverse block with slope `2^A / 3^r` and correction `C`. -/
def defect (A r : Nat) (C q : Int) : Int :=
  ((2 : Int)^A - (3 : Int)^r)*q-C

/-- One inverse-block relation multiplies the defect by `2^A / 3^r`. -/
theorem defect_step (A r : Nat) (C x y : Int)
    (step : (3 : Int)^r*y+C=(2 : Int)^A*x) :
    (3 : Int)^r*defect A r C y=(2 : Int)^A*defect A r C x := by
  have scaled := congrArg (fun z => ((2 : Int)^A-(3 : Int)^r)*z) step
  dsimp [defect]
  grind only

/-- Exact defect identity for every finite ordinary inverse-block chain. -/
theorem defect_iter (A r k : Nat) (C : Int) (q : Nat → Int)
    (steps : ∀ j<k, (3 : Int)^r*q (j+1)+C=(2 : Int)^A*q j) :
    (3 : Int)^(r*k)*defect A r C (q k)=
      (2 : Int)^(A*k)*defect A r C (q 0) := by
  induction k with
  | zero => simp
  | succ k ih =>
    have prev := ih (fun j hj => steps j (by omega))
    have next := defect_step A r C (q k) (q (k+1)) (steps k (by omega))
    have lhs := congrArg (fun z => (3 : Int)^(r*k)*z) next
    have rhs := congrArg (fun z => (2 : Int)^A*z) prev
    clear steps ih
    simp only [Nat.mul_add, Nat.mul_one, Int.pow_add]
    grind only

/-- Repeating the fixed block `k` times spends `r*k` factors of three
from one fixed ordinary integer. This accepts any finite legal chain. -/
theorem loop_divisibility (A r k : Nat) (C : Int) (q : Nat → Int)
    (steps : ∀ j<k, (3 : Int)^r*q (j+1)+C=(2 : Int)^A*q j) :
    3^(r*k) ∣ (defect A r C (q 0)).natAbs := by
  have identity := defect_iter A r k C q steps
  have hdiv : (3 : Int)^(r*k) ∣
      (2 : Int)^(A*k)*defect A r C (q 0) := ⟨defect A r C (q k),identity.symm⟩
  have hnat : 3^(r*k) ∣ 2^(A*k)*(defect A r C (q 0)).natAbs := by
    simpa [Int.natAbs_mul,Int.natAbs_pow] using Int.natAbs_dvd_natAbs.mpr hdiv
  exact ((show Nat.Coprime 3 2 by decide).pow (r*k) (A*k)).dvd_of_dvd_mul_left hnat

/-- A nonzero defect gives an explicit finite ordinary pumping budget. -/
theorem loop_budget (A r k : Nat) (C : Int) (q : Nat → Int)
    (steps : ∀ j<k, (3 : Int)^r*q (j+1)+C=(2 : Int)^A*q j)
    (nonzero : defect A r C (q 0) ≠ 0) :
    3^(r*k) ≤ (defect A r C (q 0)).natAbs := by
  exact Nat.le_of_dvd (Int.natAbs_pos.mpr nonzero)
    (loop_divisibility A r k C q steps)

/-- A nonempty fixed block can be repeated indefinitely through ordinary
integers only when the fixed starting value is its exact fixed point. -/
theorem infinite_chain_fixed (A r : Nat) (C : Int) (q : Nat → Int)
    (nonempty : 0<r)
    (steps : ∀ j, (3 : Int)^r*q (j+1)+C=(2 : Int)^A*q j) :
    defect A r C (q 0)=0 := by
  apply Classical.byContradiction
  intro h
  let D := (defect A r C (q 0)).natAbs
  have bound := loop_budget A r D C q (fun j _ => steps j) h
  have exponent : D ≤ r*D := by
    simpa using Nat.mul_le_mul_right D (show 1≤r from nonempty)
  have growth : D < 3^(r*D) :=
    Nat.lt_of_lt_of_le (Nat.lt_pow_self (by decide : 1<3))
      (Nat.pow_le_pow_right (by decide : 0<3) exponent)
  exact (Nat.not_lt_of_ge bound) growth

/-- The fixed-point conclusion is in the original block equation. -/
theorem infinite_chain_fixed_equation (A r : Nat) (C : Int) (q : Nat → Int)
    (nonempty : 0<r)
    (steps : ∀ j, (3 : Int)^r*q (j+1)+C=(2 : Int)^A*q j) :
    (3 : Int)^r*q 0+C=(2 : Int)^A*q 0 := by
  have h := infinite_chain_fixed A r C q nonempty steps
  clear steps
  dsimp [defect] at h
  grind only

/-- Such an infinite ordinary chain is constant at every index. -/
theorem infinite_chain_constant (A r : Nat) (C : Int) (q : Nat → Int)
    (nonempty : 0<r)
    (steps : ∀ j, (3 : Int)^r*q (j+1)+C=(2 : Int)^A*q j) :
    ∀ j, q j=q 0 := by
  have fixed := infinite_chain_fixed_equation A r C q nonempty steps
  intro j
  induction j with
  | zero => rfl
  | succ j ih =>
    have step := steps j
    rw [ih] at step
    have equal : (3 : Int)^r*q (j+1)=(3 : Int)^r*q 0 := by omega
    exact Int.eq_of_mul_eq_mul_left
      (Int.pow_ne_zero (by decide : (3 : Int)≠0)) equal

def iterate (f : Nat → Nat) (n : Nat) : Nat → Nat
  | 0 => n
  | t+1 => iterate f (f n) t

/-- Actual first hit of one; padding by the terminal cycle is excluded. -/
def FirstHit (f : Nat → Nat) (source clock : Nat) : Prop :=
  iterate f source clock=1 ∧ ∀ t<clock, iterate f source t≠1

theorem first_hit_unique {f : Nat → Nat} {source s t : Nat}
    (hs : FirstHit f source s) (ht : FirstHit f source t) : s=t := by
  rcases hs with ⟨hits,firsts⟩
  rcases ht with ⟨hitt,firstt⟩
  by_cases h : s<t
  · exact False.elim (firstt s h hits)
  by_cases h' : t<s
  · exact False.elim (firsts t h' hitt)
  omega

/-- No ordinary canonical certificate family can contain a fixed nonempty
inverse-block pump. The prefix is any fixed affine ordinary prefix, and the
clock grows by the positive total of the pumped exponent block. -/
theorem no_canonical_affine_pump
    (f : Nat → Nat) (A r U Z b : Nat) (C P : Int)
    (sources : Nat → Nat) (q : Nat → Int)
    (nonempty : 0<r) (positiveClock : 0<A)
    (steps : ∀ j, (3 : Int)^r*q (j+1)+C=(2 : Int)^A*q j)
    (prefixEq : ∀ j, (3 : Int)^b*(sources j : Int)+P=(2 : Int)^U*q j)
    (canonical : ∀ j, FirstHit f (sources j) (U+j*A+Z)) : False := by
  have same := infinite_chain_constant A r C q nonempty steps 1
  have p0 := prefixEq 0
  have p1 := prefixEq 1
  rw [same] at p1
  have src : sources 1=sources 0 := by
    have cast : (sources 1 : Int)=(sources 0 : Int) := by
      have equal : (3 : Int)^b*(sources 1 : Int)=(3 : Int)^b*(sources 0 : Int) := by
        omega
      exact Int.eq_of_mul_eq_mul_left
        (Int.pow_ne_zero (by decide : (3 : Int)≠0)) equal
    exact Int.ofNat_inj.mp cast
  have c0 := canonical 0
  have c1 := canonical 1
  rw [src] at c1
  have clocks := first_hit_unique c0 c1
  omega

end CollatzDiscretePump
