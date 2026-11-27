import Std

namespace PrimeSwitch

def weight (v : Int) : List Nat → Int
  | [] => 0
  | e :: es => v^e + weight v es

theorem weight_append (v : Int) (a b : List Nat) :
    weight v (a ++ b) = weight v a + weight v b := by
  induction a with
  | nil => simp [weight]
  | cons e es ih => simp [weight, ih, Int.add_assoc]

theorem shifted_weight (v : Int) (t : Nat) (a : List Nat) :
    weight v (a.map (t + ·)) = v^t * weight v a := by
  induction a with
  | nil => simp [weight]
  | cons e es ih =>
    simp only [List.map_cons, weight, Int.pow_add, ih, Int.mul_add]

def alternatives : List Nat → List Nat × List Nat
  | [] => ([0], [])
  | t :: ts =>
    let (p, n) := alternatives ts
    (p.map (t + ·) ++ n, n.map (t + ·) ++ p)

def delta (v : Int) : List Nat → Int
  | [] => 1
  | t :: ts => (v^t - 1) * delta v ts

/-- The two choices implement exactly the signed polynomial product. -/
theorem switch_difference (v : Int) (ts : List Nat) :
    weight v (alternatives ts).1 - weight v (alternatives ts).2 = delta v ts := by
  induction ts with
  | nil => simp [alternatives, weight, delta]
  | cons t ts ih =>
    simp only [alternatives, weight_append, shifted_weight, delta]
    rw [← ih]
    grind

/-- Translating the entire copy multiplies its difference by one power. -/
theorem translated_switch (v : Int) (c : Nat) (ts : List Nat) :
    weight v ((alternatives ts).1.map (c + ·)) -
      weight v ((alternatives ts).2.map (c + ·)) = v^c * delta v ts := by
  rw [shifted_weight, shifted_weight, ← Int.mul_sub, switch_difference]

#print axioms switch_difference
#print axioms translated_switch

end PrimeSwitch
