import Mathlib.Tactic

namespace PeriodicBoundary

/-- A canonical pair is a lower-grade anchor u and an arm 3^s*u+d.
The bit is the parity of the current anchor. -/
def next (z : ℕ × ℤ) (b : Bool) : ℕ × ℤ :=
  let (s, d) := z
  if d % 2 = 0 then
    if b then (s, (3*d+1-3^s)/2) else (s, d/2)
  else
    match s with
    | 0 => if b then (1, (1-3*d)/2) else (1, (3*d+1)/2)
    | t+1 => if b then (t, (d-3^t)/2) else (t+2, (3*d+1)/2)

/-- Reachability by a finite anchor-parity word. -/
inductive Merges : ℕ × ℤ → Prop where
  | done : Merges (0, 0)
  | prepend {z : ℕ × ℤ} (b : Bool) : Merges (next z b) → Merges z

private theorem reduceThree (d : ℤ) (h : d % 4 = 3) :
    next (next (0,d) false) true=(0,(3*d-1)/4) := by
  have ho : d % 2 ≠ 0 := by omega
  have ho' : ((3*d+1)/2) % 2 ≠ 0 := by omega
  simp [next, ho, ho']
  omega

private theorem reduceOne (d : ℤ) (h : d % 4 = 1) :
    next (next (0,d) true) true=(0,-((3*d+1)/4)) := by
  have ho : d % 2 ≠ 0 := by omega
  have ho' : ((1-3*d)/2) % 2 ≠ 0 := by omega
  simp [next, ho, ho']
  omega

private theorem absSmaller {x y : ℤ} (h : |x| < |y|) : x.natAbs < y.natAbs := by
  exact_mod_cast (show (x.natAbs:ℤ)<(y.natAbs:ℤ) by simpa using h)

private theorem mergesZero (d : ℤ) : Merges (0,d) := by
  by_cases h0 : d = 0
  · subst d; exact .done
  by_cases hp : d = 1
  · subst d
    apply Merges.prepend false
    apply Merges.prepend false
    apply Merges.prepend true
    exact .done
  by_cases hm : d = -1
  · subst d
    apply Merges.prepend true
    apply Merges.prepend false
    apply Merges.prepend true
    exact .done
  by_cases he : d % 2 = 0
  · apply Merges.prepend false
    simp only [next, he, ite_true, Bool.false_eq_true, ite_false]
    exact mergesZero (d/2)
  by_cases ht : d % 4 = 3
  · apply Merges.prepend false
    apply Merges.prepend true
    rw [reduceThree d ht]
    exact mergesZero ((3*d-1)/4)
  · have hu : d % 4 = 1 := by omega
    apply Merges.prepend true
    apply Merges.prepend true
    rw [reduceOne d hu]
    exact mergesZero (-((3*d+1)/4))
termination_by d.natAbs
decreasing_by
  all_goals
    apply absSmaller
    rw [abs_lt]
    by_cases hd : 0 ≤ d
    · rw [abs_of_nonneg hd]; omega
    · rw [abs_of_neg (lt_of_not_ge hd)]; omega

private theorem mergesPositiveNonzero (s : ℕ) (d : ℤ) (hd : d ≠ 0)
    (lower : ∀ a : ℤ, Merges (s,a)) : Merges (s+1,d) := by
  by_cases he : d % 2 = 0
  · apply Merges.prepend false
    simp only [next, he, ite_true, Bool.false_eq_true, ite_false]
    exact mergesPositiveNonzero s (d/2) (by omega) lower
  · apply Merges.prepend true
    simpa [next, he] using lower ((d-3^s)/2)
termination_by d.natAbs
decreasing_by
  apply absSmaller
  rw [abs_lt]
  by_cases hp : 0 ≤ d
  · rw [abs_of_nonneg hp]; omega
  · rw [abs_of_neg (lt_of_not_ge hp)]; omega

/-- Every canonical pair state has a finite absorbing continuation. -/
theorem everyStateMerges (s : ℕ) (d : ℤ) : Merges (s,d) := by
  induction s generalizing d with
  | zero => exact mergesZero d
  | succ s ih =>
    by_cases hd : d=0
    · subst d
      apply Merges.prepend true
      have hp : (0 : ℤ) < 3^s := by positivity
      have hn : ((1-(3:ℤ)^(s+1))/2) ≠ 0 := by rw [pow_succ]; omega
      simpa [next] using mergesPositiveNonzero s _ hn ih
    · exact mergesPositiveNonzero s d hd ih

def numeratorStep (D a : ℤ) : ℤ :=
  if a % 2 = 0 then a / 2 else (3*a+D)/2

def walk (D : ℤ) : ℕ → ℤ → ℤ
  | 0, a => a
  | k+1, a => walk D k (numeratorStep D a)

def count (D : ℤ) : ℕ → ℤ → ℕ
  | 0, _ => 0
  | k+1, a => (if a % 2=0 then 0 else 1) + count D k (numeratorStep D a)

private theorem walkAdd (D : ℤ) (i j : ℕ) (a : ℤ) :
    walk D (i+j) a=walk D j (walk D i a) := by
  induction i generalizing a with
  | zero => simp [walk]
  | succ i ih => simpa [Nat.succ_add,walk] using ih (numeratorStep D a)

private theorem countAdd (D : ℤ) (i j : ℕ) (a : ℤ) :
    count D (i+j) a=count D i a + count D j (walk D i a) := by
  induction i generalizing a with
  | zero => simp [count,walk]
  | succ i ih => simp [Nat.succ_add, count, walk, ih, Nat.add_assoc]

/-- The exact integer-numerator form of the signed seed lift at its native clock. -/
theorem liftedWalk (D : ℤ) (k : ℕ) (z a : ℤ) :
    walk D k (2^k*z+a) = 3^(count D k a)*z+walk D k a := by
  induction k generalizing z a with
  | zero => simp [walk,count]
  | succ k ih =>
    rw [walk,walk,count]
    have hr : (2:ℤ)^(k+1)*z=2*(2^k*z) := by ring
    rw [hr]
    by_cases he : a%2=0
    · have q : numeratorStep D (2*(2^k*z)+a)=2^k*z+numeratorStep D a := by
        unfold numeratorStep; split <;> omega
      rw [q,ih]; simp [he]
    · have q : numeratorStep D (2*(2^k*z)+a)=2^k*(3*z)+numeratorStep D a := by
        unfold numeratorStep
        rw [show 2^k*(3*z)=3*(2^k*z) by ring]
        split <;> omega
      rw [q,ih]; simp [he,pow_add]; ring

private theorem repeatPeriod {D start tail : ℤ} {b stride p jump : ℕ}
    (hb : walk D b start=tail ∧ count D b start=p)
    (hs : walk D stride tail=tail ∧ count D stride tail=jump)
    (h : ℕ) : walk D (b+stride*h) start=tail ∧ count D (b+stride*h) start=p+jump*h := by
  induction h with
  | zero => simpa using hb
  | succ h ih =>
    rw [show b+stride*(h+1)=(b+stride*h)+stride by ring,
        walkAdd,countAdd,ih.1,ih.2,hs.1,hs.2,Nat.mul_succ]
    omega

/-- The two ordinary lifts have aligned native endpoint numerators on different
dyadic levels; they differ by 45, or three after dividing by 15. -/
theorem alignedNumerators (n : ℤ) (h : ℕ) :
    walk 15 (8+36*h) (2^(8+36*h)*(15*n+11)-11)
      = 3^(5+12*h)*(15*n+11)+12 ∧
    walk 15 (8+20*h) (2^(8+20*h)*(15*n+11)+4)
      = 3^(5+12*h)*(15*n+11)+57 := by
  have L := repeatPeriod (D:=15) (start:=-11) (tail:=12)
    (b:=8) (stride:=36) (p:=5) (jump:=12) (by decide) (by decide) h
  have R := repeatPeriod (D:=15) (start:=4) (tail:=57)
    (b:=8) (stride:=20) (p:=5) (jump:=12) (by decide) (by decide) h
  constructor
  · rw [sub_eq_add_neg,liftedWalk,L.1,L.2]
  · rw [liftedWalk,R.1,R.2]

#print axioms everyStateMerges
#print axioms liftedWalk
#print axioms alignedNumerators

end PeriodicBoundary
