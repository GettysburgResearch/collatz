import AffineOrbit

/-! Construct actual finite pairs of affine native calendars. At positive level
the upper arm has slope 3^j relative to the lower one; at level zero this is
an integer translation. All grade bounds below count both arms. -/

set_option autoImplicit false
namespace Collatz.SignedReturnRouter
open Collatz.PoweredAffine

structure Route (i : Nat) (a : Int) (j : Nat) (b : Int) where
  lower : List Bool
  upper : List Bool
  lengths : lower.length = upper.length
  grades : i + ones upper = j + ones lower
  graph (x : Rat) : evalWord upper (3^i*x-a) = 3^j*evalWord lower x-b

def Route.cost {i j : Nat} {a b : Int} (r : Route i a j b) : Nat :=
  ones r.lower + ones r.upper

private theorem ones_append (u v : List Bool) : ones (u++v)=ones u+ones v := by
  induction u with
  | nil => simp [ones]
  | cons b u ih => simp [ones, ih, Nat.add_assoc]

def Route.stay (i : Nat) (a : Int) : Route i a i a where
  lower := []
  upper := []
  lengths := rfl
  grades := rfl
  graph _ := rfl

@[simp] theorem Route.stay_cost (i : Nat) (a : Int) : (Route.stay i a).cost=0 := rfl

def Route.thenRoute {i j k : Nat} {a b c : Int} (r : Route i a j b) (s : Route j b k c) :
    Route i a k c where
  lower := r.lower++s.lower
  upper := r.upper++s.upper
  lengths := by simp [r.lengths,s.lengths]
  grades := by simp only [ones_append]; have := r.grades; have := s.grades; omega
  graph x := by rw [evalWord_append,evalWord_append,r.graph,s.graph]

@[simp] theorem Route.then_cost {i j k : Nat} {a b c : Int} (r : Route i a j b)
    (s : Route j b k c) : (r.thenRoute s).cost=r.cost+s.cost := by
  simp only [Route.cost,Route.thenRoute,ones_append]
  omega

def Route.evenBoth (j : Nat) (a b : Int) (h : 2*b=a) : Route j a j b where
  lower := [false]
  upper := [false]
  lengths := rfl
  grades := rfl
  graph x := by
    have h' : 2*(b:Rat)=a := by exact_mod_cast h
    simp only [evalWord,letter,Bool.false_eq_true, ↓reduceIte]
    linarith only [h']

def Route.up (j : Nat) (a b : Int) (h : 2*b=3*a-1) : Route j a (j+1) b where
  lower := [false]
  upper := [true]
  lengths := rfl
  grades := rfl
  graph x := by
    have h' : 2*(b:Rat)=3*a-1 := by exact_mod_cast h
    simp only [evalWord,letter,Bool.false_eq_true, ↓reduceIte,pow_succ]
    linarith only [h']

def Route.down (j : Nat) (a b : Int) (h : 2*b=a+(3:Int)^j) : Route (j+1) a j b where
  lower := [true]
  upper := [false]
  lengths := rfl
  grades := rfl
  graph x := by
    have h' : 2*(b:Rat)=a+(3:Rat)^j := by exact_mod_cast h
    simp only [evalWord,letter,Bool.false_eq_true, ↓reduceIte,pow_succ]
    linarith only [h']

def Route.swapZero {a b : Int} (r : Route 0 a 0 b) : Route 0 (-a) 0 (-b) where
  lower := r.upper
  upper := r.lower
  lengths := r.lengths.symm
  grades := r.grades.symm
  graph x := by
    have h := r.graph (x+a)
    simp only [pow_zero,one_mul,add_sub_cancel_right,Int.cast_neg,sub_neg_eq_add] at h ⊢
    linarith only [h]

@[simp] theorem Route.swap_cost {a b : Int} (r : Route 0 a 0 b) : r.swapZero.cost=r.cost := by
  simp [Route.cost,Route.swapZero,Nat.add_comm]

private theorem coast (M j : Nat) (a : Int) (lo : -(M:Int)≤a) (hi : a≤M) (nonzero : a≠0) :
    ∃ b : Int, -(M:Int)≤b ∧ b≤M ∧ b%2=1 ∧ (a%3≠0 → b%3≠0) ∧
      ∃ r : Route j a j b, r.cost=0 := by
  induction M generalizing a with
  | zero => omega
  | succ M ih =>
    by_cases odd : a%2=1
    · exact ⟨a,lo,hi,odd,id,Route.stay j a,rfl⟩
    · have halves : 2*(a/2)=a := by omega
      obtain ⟨b,bl,bh,bo,bu,r,rc⟩ := ih (a/2) (by omega) (by omega) (by omega)
      let e := Route.evenBoth j a (a/2) halves
      have ec : e.cost=0 := rfl
      exact ⟨b,by omega,by omega,bo,fun ha => bu (by omega),e.thenRoute r,by simp [ec,rc]⟩

private def avoidZero : Route 1 (-1) 0 1 :=
  (Route.up 1 (-1) (-2) (by decide)).thenRoute
    ((Route.evenBoth 2 (-2) (-1) (by decide)).thenRoute
      ((Route.down 1 (-1) 1 (by decide)).thenRoute (Route.down 0 1 1 (by decide))))

private theorem avoidZero_cost : avoidZero.cost=3 := by decide

private theorem odd_three_power (j : Nat) : (3:Int)^j%2=1 := by
  induction j with
  | zero => decide
  | succ j h => rw [pow_succ,Int.mul_emod,h]; decide

/-- At most one genuine odd letter per lost level, plus two for avoiding
the one possible last-step collapse. All common-even waits cost zero. -/
theorem descend_to_translation (j M : Nat) (a : Int) (hM : 2≤M)
    (powBound : (3:Int)^j ≤ M) (lo : -(M:Int)≤a) (hi : a≤M) (nonzero : a≠0)
    (unit : j=0 ∨ a%3≠0) :
    ∃ b : Int, -(M:Int)≤b ∧ b≤M ∧ b≠0 ∧ ∃ r : Route j a 0 b, r.cost≤j+2 := by
  induction j generalizing a with
  | zero => exact ⟨a,lo,hi,nonzero,Route.stay 0 a,by simp⟩
  | succ j ih =>
    obtain ⟨d,dl,dh,odd,du,r,rc⟩ := coast M (j+1) a lo hi nonzero
    have du' : d%3≠0 := du (by omega)
    by_cases exception : j=0 ∧ d= -1
    · obtain ⟨rfl,rfl⟩ := exception
      exact ⟨1,by omega,by omega,by decide,r.thenRoute avoidZero,by simp [rc,avoidZero_cost]⟩
    · let e := (d+(3:Int)^j)/2
      have oddPower := odd_three_power j
      have twice : 2*e=d+(3:Int)^j := by
        dsimp [e]
        omega
      have ppos : 0<(3:Int)^j := by positivity
      have pb : (3:Int)^j≤M := by rw [pow_succ] at powBound; omega
      have eu : j=0 ∨ e%3≠0 := by
        cases j with
        | zero => exact Or.inl rfl
        | succ k =>
          right
          rw [pow_succ] at twice
          omega
      have en : e≠0 := by
        intro eq
        rcases eu with h|h
        · subst j
          simp only [pow_zero,eq,mul_zero] at twice
          exact exception ⟨rfl,by omega⟩
        · omega
      obtain ⟨b,bl,bh,bnz,remain,hremain⟩ := ih e pb (by omega) (by omega) en eu
      let dec := Route.down j d e twice
      have cost : dec.cost=1 := rfl
      exact ⟨b,bl,bh,bnz,(r.thenRoute dec).thenRoute remain,by simp only [Route.then_cost,rc,cost]; omega⟩

private def plusCross (a b : Int) (h : 4*b=3*a+1) : Route 0 a 0 b where
  lower := [false,true]
  upper := [true,false]
  lengths := rfl
  grades := rfl
  graph x := by
    have h' : 4*(b:Rat)=3*a+1 := by exact_mod_cast h
    simp [evalWord,letter]
    linarith only [h']

private def minusCross (a b : Int) (h : 4*b=3*a-1) : Route 0 a 0 b where
  lower := [true,false]
  upper := [false,true]
  lengths := rfl
  grades := rfl
  graph x := by
    have h' : 4*(b:Rat)=3*a-1 := by exact_mod_cast h
    simp [evalWord,letter]
    linarith only [h']

private theorem shrink (a : Nat) (ha : 2≤a) :
    ∃ b : Nat, 1≤b ∧ 8*b≤7*a ∧ ∃ r : Route 0 (a:Int) 0 (b:Int), r.cost≤2 := by
  by_cases h : a%2=0
  · let b := a/2
    have hb : 2*(b:Int)=a := by dsimp [b]; omega
    exact ⟨b,by dsimp [b]; omega,by dsimp [b]; omega,Route.evenBoth 0 a b hb,by change 0≤2; decide⟩
  · by_cases plus : (3*a+1)%4=0
    · let b := (3*a+1)/4
      have hb : 4*(b:Int)=3*a+1 := by dsimp [b]; omega
      exact ⟨b,by dsimp [b]; omega,by dsimp [b]; omega,plusCross a b hb,by change 2≤2; decide⟩
    · let b := (3*a-1)/4
      have hb : 4*(b:Int)=3*a-1 := by dsimp [b]; omega
      exact ⟨b,by dsimp [b]; omega,by dsimp [b]; omega,minusCross a b hb,by change 2≤2; decide⟩

private theorem shrink_steps (n a : Nat) (ha : 0<a) :
    ∃ b : Nat, 0<b ∧ (b=1 ∨ 8^n*b≤7^n*a) ∧
      ∃ r : Route 0 (a:Int) 0 (b:Int), r.cost≤2*n := by
  induction n generalizing a with
  | zero => exact ⟨a,ha,Or.inr (by simp),Route.stay 0 a,by simp⟩
  | succ n ih =>
    by_cases h : a=1
    · exact ⟨a,ha,Or.inl h,Route.stay 0 a,by simp⟩
    · obtain ⟨b,bp,factor,stepRoute,cost⟩ := shrink a (by omega)
      obtain ⟨d,dp,done,rest,cc⟩ := ih b bp
      refine ⟨d,dp,?_,stepRoute.thenRoute rest,by simp only [Route.then_cost]; omega⟩
      rcases done with eq|small
      · exact Or.inl eq
      · right
        calc 8^(n+1)*d = 8*(8^n*d) := by ring
             _ ≤ 8*(7^n*b) := Nat.mul_le_mul_left _ small
             _ = 7^n*(8*b) := by ring
             _ ≤ 7^n*(7*a) := Nat.mul_le_mul_left _ factor
             _ = _ := by ring

/-- A nonzero positive translation of size at most 3^n contracts
to translation one in at most 18n combined odd departures. -/
theorem positive_to_one (n a : Nat) (ha : 0<a) (bound : a≤3^n) :
    ∃ r : Route 0 (a:Int) 0 1, r.cost≤18*n := by
  induction n generalizing a with
  | zero =>
    have eq : a=1 := by simp only [pow_zero] at bound; omega
    subst a
    exact ⟨Route.stay 0 1,by simp⟩
  | succ n ih =>
    obtain ⟨b,bp,done,r,cost⟩ := shrink_steps 9 a ha
    rcases done with eq|small
    · subst b
      exact ⟨r,by omega⟩
    · norm_num at small
      rw [pow_succ] at bound
      have bn : b≤3^n := by omega
      obtain ⟨rest,rc⟩ := ih b bp bn
      exact ⟨r.thenRoute rest,by simp only [Route.then_cost]; omega⟩

private def signFlip : Route 0 (-1) 0 1 where
  lower := [false,false,false,false,true,false,true,false,true]
  upper := [true,false,true,false,false,true,false,false,false]
  lengths := rfl
  grades := rfl
  graph x := by
    norm_num [evalWord,letter]
    ring

private theorem signFlip_cost : signFlip.cost=6 := by decide

/-- Allow both signs on the input translation, with a fixed six-grade
calendar to put the output in the original orientation. -/
theorem signed_to_one (n : Nat) (a : Int) (nonzero : a≠0)
    (bound : a.natAbs≤3^n) : ∃ r : Route 0 a 0 1, r.cost≤18*n+6 := by
  cases a with
  | ofNat a =>
    have ap : 0<a := Nat.pos_of_ne_zero (fun h => nonzero (by subst a; rfl))
    obtain ⟨r,hr⟩ := positive_to_one n a ap bound
    exact ⟨r,by omega⟩
  | negSucc a =>
    obtain ⟨r,hr⟩ := positive_to_one n (a+1) (by omega) bound
    let s := r.swapZero.thenRoute signFlip
    exact ⟨s,by simp only [s,Route.then_cost,Route.swap_cost,signFlip_cost]; omega⟩

/-- Reset an oriented line to adjacent translations by concrete paired
calendars, including the positive-level descent and both possible signs. -/
theorem reset_to_adjacent (j n : Nat) (a : Int) (nonzero : a≠0)
    (hn : 0<n) (hj : j≤n) (bound : a.natAbs≤3^n) (unit : j=0 ∨ a%3≠0) :
    ∃ r : Route j a 0 1, r.cost≤j+18*n+8 := by
  have power : (3:Nat)^j≤3^n := Nat.pow_le_pow_right (by decide) hj
  have pos : (2:Nat)≤3^n := by
    have w : (3:Nat)^1≤3^n := Nat.pow_le_pow_right (by decide) (by omega)
    omega
  have low : -((3^n:Nat):Int)≤a := by omega
  have high : a≤((3^n:Nat):Int) := by omega
  obtain ⟨b,bl,bh,bnz,r,hr⟩ := descend_to_translation j (3^n) a pos
    (by exact_mod_cast power) low high nonzero unit
  obtain ⟨s,hs⟩ := signed_to_one n b bnz (by omega)
  exact ⟨r.thenRoute s,by simp only [Route.then_cost]; omega⟩

/-- A six-grade return in the other orientation is needed when the longer
slope came from the first supplied arm. -/
theorem reset_to_reverse (j n : Nat) (a : Int) (nonzero : a≠0)
    (hn : 0<n) (hj : j≤n) (bound : a.natAbs≤3^n) (unit : j=0 ∨ a%3≠0) :
    ∃ r : Route j a 0 (-1), r.cost≤j+18*n+14 := by
  obtain ⟨r,hr⟩ := reset_to_adjacent j n a nonzero hn hj bound unit
  let s : Route 0 1 0 (-1) := signFlip.swapZero
  exact ⟨r.thenRoute s,by simp only [Route.then_cost,s,Route.swap_cost,signFlip_cost]; omega⟩

#print axioms descend_to_translation
#print axioms positive_to_one
#print axioms signed_to_one
#print axioms reset_to_adjacent
#print axioms reset_to_reverse
end Collatz.SignedReturnRouter
