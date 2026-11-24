import Std

/-! Integer critical lifts, moving-clock anchors and synchronous splicing.
    Odd iteration is abstract in the last two results so that clocks and
    choices of compressed representatives are explicit. -/
namespace ForwardAnchors

private theorem powTwoResidue (t : Nat) :
    2^t % 3 = 1 ∨ 2^t % 3 = 2 := by
  induction t with
  | zero => decide
  | succ t ih =>
    rw [Nat.pow_succ, Nat.mul_mod]
    rcases ih with h | h <;> simp [h]

/-- The physical incoming equation and both critical inequalities.
The input interval excludes the endpoints, which are divisible by three.
The odd cofactor y makes e the exact valuation of 3*x+1. -/
theorem criticalLift {y k : Nat} (odd : y%2=1)
    (unit : y%3=1 ∨ y%3=2)
    (low : 3*2^k<y) (high : y<6*2^k) :
    ∃ e x : Nat, 0<e ∧ x%2=1 ∧ 3*x+1=2^e*y ∧
      2^(e+k)≤x ∧ x<2^(e+k+1) ∧
      e+k+1≤5*e ∧ 5*e≤e+k+8 := by
  let b := k/4+1
  have pick : ∃ e : Nat, (e=b ∨ e=b+1) ∧ (2^e*y)%3=1 := by
    have hu : (2^b*y)%3=1 ∨ (2^b*y)%3=2 := by
      rw [Nat.mul_mod]
      rcases powTwoResidue b with h|h <;> rcases unit with hy|hy <;> simp [h,hy]
    rcases hu with h|h
    · exact ⟨b,Or.inl rfl,h⟩
    · refine ⟨b+1,Or.inr rfl,?_⟩
      rw [Nat.pow_succ, Nat.mul_right_comm (2^b) 2 y, Nat.mul_mod,h]
  obtain ⟨e,choice,cong⟩ := pick
  have ep : 0<e := by dsimp [b] at choice; omega
  let x := (2^e*y)/3
  have eq : 3*x+1=2^e*y := by
    have := Nat.mod_add_div (2^e*y) 3
    dsimp [x]
    omega
  obtain ⟨f,hf⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : e≠0)
  have ev : 2^e*y=2*(2^f*y) := by rw [hf,Nat.pow_succ]; ac_rfl
  have ox : x%2=1 := by omega
  have lo := Nat.mul_le_mul_left (2^e) (show 3*2^k+1≤y by omega)
  have hi := Nat.mul_lt_mul_of_pos_left high (Nat.two_pow_pos e)
  rw [Nat.mul_add,Nat.mul_one,Nat.mul_left_comm (2^e) 3] at lo
  rw [Nat.mul_left_comm (2^e) 6] at hi
  refine ⟨e,x,ep,ox,eq,?_,?_,?_,?_⟩
  · rw [Nat.pow_add]
    have := Nat.two_pow_pos e
    omega
  · rw [Nat.pow_succ,Nat.pow_add]
    omega
  · dsimp [b] at choice; omega
  · dsimp [b] at choice; omega

/-- Exact preservation of the leading-bit mark at a lifted endpoint. -/
theorem liftMarked {P a E x y w : Nat}
    (eq : 3*x+1=E*y) (base : 3*P+a=y)
    (bound : w*a≤70*(3*P)) : w*(x-E*P)≤70*(E*P) := by
  have low : E*P≤x := by
    rw [← base, Nat.mul_add, Nat.mul_left_comm E 3] at eq
    omega
  let z := x-E*P
  have add : x=E*P+z := by dsimp [z]; omega
  have h : 3*z+1=E*a := by
    rw [add,Nat.mul_add,← base,Nat.mul_add,Nat.mul_left_comm E 3] at eq
    omega
  have small := Nat.mul_le_mul_left w (show 3*z≤E*a by omega)
  have big := Nat.mul_le_mul_left E bound
  rw [Nat.mul_left_comm w 3, Nat.mul_left_comm w E] at small
  rw [Nat.mul_left_comm E 70, Nat.mul_left_comm E 3] at big
  change w*z≤70*(E*P)
  omega

def iter {α : Type} (f : α → α) : Nat → α → α
  | 0,x => x
  | n+1,x => f (iter f n x)

theorem iterAdd {α : Type} (f : α → α) (s t : Nat) (x : α) :
    iter f (s+t) x=iter f t (iter f s x) := by
  induction t with
  | zero => rfl
  | succ t ih => exact congrArg f ih

/-- The new anchor advances the *same* original orbit, even when the new
representative was selected from another arm of the fiber. -/
theorem nextAnchor {α : Type} (f : α → α) (start chosen : α)
    (j R : Nat) (shared : iter f R chosen=iter f R (iter f j start)) :
    iter f R chosen=iter f (j+R) start := by
  rw [iterAdd,shared]

/-- One delayed, independently chosen arm per time of one injective orbit.
The delays need not agree and no common upper bound on them is required. -/
theorem splicedTransversal {α : Type} (f : α → α) (x : α) (s : Nat → α)
    (inj : ∀ i j, iter f i x=iter f j x → i=j)
    (merges : ∀ i, ∃ d, iter f d (s i)=iter f d (iter f i x)) :
    ∀ t i j, iter f t (s i)=iter f t (s j) → i=j := by
  intro t i j meet
  obtain ⟨a,ha⟩ := merges i
  obtain ⟨b,hb⟩ := merges j
  let M := t+a+b
  have prolong (v w : α) (r : Nat) (hr : r≤M) (h : iter f r v=iter f r w) :
      iter f M v=iter f M w := by
    have hm : r+(M-r)=M := by omega
    rw [← hm, iterAdd, iterAdd,h]
  have hi := prolong _ _ a (by dsimp [M]; omega) ha
  have hj := prolong _ _ b (by dsimp [M]; omega) hb
  have hm := prolong _ _ t (by dsimp [M]; omega) meet
  have h := hi.symm.trans (hm.trans hj)
  rw [← iterAdd, ← iterAdd] at h
  have := inj _ _ h
  omega

/-- Products of actual positive correction numerators and denominators. -/
def prodN (g : Nat → Nat) : Nat → Nat
  | 0 => 1
  | n+1 => prodN g n * g n

def sumN (g : Nat → Nat) : Nat → Nat
  | 0 => 0
  | n+1 => sumN g n + g n

/-- Integer multiplicative form of the odd logarithmic telescope, avoiding
real arithmetic entirely. -/
theorem physicalProduct (w e : Nat → Nat)
    (physical : ∀ i, 2^(e i)*w (i+1)=3*w i+1) (h : Nat) :
    2^(sumN e h)*w h*prodN (fun i => 3*w i) h =
      3^h*w 0*prodN (fun i => 3*w i+1) h := by
  induction h with
  | zero => simp [sumN,prodN]
  | succ h ih =>
    simp only [sumN,prodN,Nat.pow_add,Nat.pow_succ]
    let D := prodN (fun i => 3*w i) h
    let P := prodN (fun i => 3*w i+1) h
    calc
      _ = 3*(2^(sumN e h)*w h*D)*(2^(e h)*w (h+1)) := by dsimp [D]; ac_rfl
      _ = 3*(3^h*w 0*P)*(3*w h+1) := by rw [physical, ih]
      _ = _ := by dsimp [P]; ac_rfl

/-- Fully cleared two-arm identity underlying the log discrepancy and
eventual equality of binary clocks on a disjoint observable section. -/
theorem mergeProduct (u v a b : Nat → Nat)
    (pu : ∀ i, 2^(a i)*u (i+1)=3*u i+1)
    (pv : ∀ i, 2^(b i)*v (i+1)=3*v i+1) (h : Nat) (meet : u h=v h) :
    2^(sumN b h)*u 0*prodN (fun i => 3*u i+1) h*prodN (fun i => 3*v i) h =
    2^(sumN a h)*v 0*prodN (fun i => 3*v i+1) h*prodN (fun i => 3*u i) h := by
  have hu := physicalProduct u a pu h
  have hv := physicalProduct v b pv h
  let Pu := prodN (fun i => 3*u i+1) h
  let Pv := prodN (fun i => 3*v i+1) h
  let Du := prodN (fun i => 3*u i) h
  let Dv := prodN (fun i => 3*v i) h
  have pos : 0<3^h := Nat.pow_pos (by decide)
  apply Nat.eq_of_mul_eq_mul_left pos
  calc
    _ = (3^h*u 0*Pu)*(2^(sumN b h)*Dv) := by dsimp [Pu,Dv]; ac_rfl
    _ = (2^(sumN a h)*u h*Du)*(2^(sumN b h)*Dv) := by rw [← hu]
    _ = (3^h*v 0*Pv)*(2^(sumN a h)*Du) := by rw [← hv, meet]; dsimp [Dv]; ac_rfl
    _ = _ := by dsimp [Pv,Du]; ac_rfl

/-- Every positive odd ternary unit has a positive odd ternary-unit
predecessor of exponent at most four. -/
theorem smallUnitInverse {y : Nat} (odd : y%2=1) (unit : y%3≠0) :
    ∃ b p : Nat, 1≤b ∧ b≤4 ∧ p%2=1 ∧ p%3≠0 ∧ 3*p+1=2^b*y := by
  have cases : y%9=1 ∨ y%9=2 ∨ y%9=4 ∨ y%9=5 ∨ y%9=7 ∨ y%9=8 := by omega
  rcases cases with h|h|h|h|h|h
  all_goals first
    | (refine ⟨1,(2*y-1)/3,by decide,by decide,?_,?_,?_⟩ <;> omega)
    | (refine ⟨2,(4*y-1)/3,by decide,by decide,?_,?_,?_⟩ <;> omega)
    | (refine ⟨3,(8*y-1)/3,by decide,by decide,?_,?_,?_⟩ <;> omega)
    | (refine ⟨4,(16*y-1)/3,by decide,by decide,?_,?_,?_⟩ <;> omega)

/-- Simultaneous extremality of unit minima, at adjacent phase indices. -/
theorem extremalSandwich {x y u p e b : Nat}
    (forward : y≤u) (backward : x≤p)
    (next : 3*x+1=2^e*u) (previous : 3*p+1=2^b*y) :
    2^e*y≤3*x+1 ∧ 3*x+1≤2^b*y := by
  constructor
  · rw [next]
    exact Nat.mul_le_mul_left _ forward
  · omega

#print axioms smallUnitInverse
#print axioms extremalSandwich

#print axioms physicalProduct
#print axioms mergeProduct

#print axioms criticalLift
#print axioms liftMarked
#print axioms nextAnchor
#print axioms splicedTransversal
end ForwardAnchors
