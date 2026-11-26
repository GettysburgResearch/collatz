import ReverseBasin

namespace MersenneBarrier
open CollatzReverseBasin

def run : Nat → Nat → Nat
  | 0, x => x
  | i+1, x => run i (shortcut x)

private theorem run_add (i j x : Nat) :
    run (i+j) x = run j (run i x) := by
  induction i generalizing x with
  | zero => simp [run]
  | succ i ih => simpa [Nat.succ_add,run] using ih (shortcut x)

private theorem odd_run_nondecreasing (j x a : Nat) (eq : x+1=2^j*a) :
    x ≤ run j x := by
  induction j generalizing x a with
  | zero => exact Nat.le_refl _
  | succ j ih =>
    have h : x+1=2*(2^j*a) := by rw [eq,Nat.pow_succ]; ring
    have par : x%2≠0 := by omega
    have step : shortcut x=(3*x+1)/2 := by simp [shortcut,par]
    have next : shortcut x+1=2^j*(3*a) := by
      rw [step,show 2^j*(3*a)=3*(2^j*a) by ring]
      omega
    have inc : x≤shortcut x := by rw [step]; omega
    exact inc.trans (ih (shortcut x) (3*a) next)

private theorem first_seven (r : Nat) :
    run 7 (128*r+33)=81*r+22 ∧
    ∀ j ≤ 7, 9*(128*r+33) ≤ 16*run j (128*r+33) := by
  have h0 : shortcut (128*r+33)=192*r+50 := by unfold shortcut; split <;> omega
  have h1 : shortcut (192*r+50)=96*r+25 := by unfold shortcut; split <;> omega
  have h2 : shortcut (96*r+25)=144*r+38 := by unfold shortcut; split <;> omega
  have h3 : shortcut (144*r+38)=72*r+19 := by unfold shortcut; split <;> omega
  have h4 : shortcut (72*r+19)=108*r+29 := by unfold shortcut; split <;> omega
  have h5 : shortcut (108*r+29)=162*r+44 := by unfold shortcut; split <;> omega
  have h6 : shortcut (162*r+44)=81*r+22 := by unfold shortcut; split <;> omega
  constructor
  · simp only [run,h0,h1,h2,h3,h4,h5,h6]
  · intro j hj
    rcases (show j=0 ∨ j=1 ∨ j=2 ∨ j=3 ∨ j=4 ∨ j=5 ∨ j=6 ∨ j=7 by omega) with h|h|h|h|h|h|h|h <;>
      subst j <;> simp only [run,h0,h1,h2,h3,h4,h5,h6] <;> omega

/-- The finite lower-orbit obstruction holds simultaneously up to a clock
growing with the power, with an exact seventh ordinary state. -/
theorem mersenne_prefix (z L : Nat) (eq : 81*z+271=128*2^L) :
    run 7 z+1=2^L ∧ ∀ j ≤ 7+L, 9*z ≤ 16*run j z := by
  let r := z/128
  have hr : z=128*r+33 := by dsimp [r]; omega
  obtain ⟨ep,early⟩ := first_seven r
  rw [←hr] at ep early
  have eqpow : run 7 z+1=2^L := by omega
  refine ⟨eqpow,?_⟩
  intro j hj
  by_cases hsmall : j≤7
  · exact early j hsmall
  · let t := j-7
    have ht : t≤L := by dsimp [t]; omega
    have hsum : j=7+t := by dsimp [t]; omega
    have p : run 7 z+1=2^t*(2^(L-t)) := by
      rw [←Nat.pow_add, show t+(L-t)=L by omega,eqpow]
    have rise := odd_run_nondecreasing t (run 7 z) (2^(L-t)) p
    rw [hsum,run_add]
    have h7 := early 7 (by decide)
    omega

private theorem family_source (m : Nat) :
    ∃ z : Nat, z%48=17 ∧ 81*z+271=128*2^(162*m+11) := by
  induction m with
  | zero => exact ⟨3233,by decide,by decide⟩
  | succ m ih =>
    obtain ⟨z,hz,he⟩ := ih
    let a : Nat := 2^162
    let b : Nat := 271*(a-1)/81
    have id : 81*b+271=271*a := by decide
    have modA : a%48=16 := by decide
    have modB : b%48=33 := by decide
    refine ⟨a*z+b,?_,?_⟩
    · rw [Nat.add_mod,Nat.mul_mod,hz,modA,modB]
    · calc
        81*(a*z+b)+271 = a*(81*z)+ (81*b+271) := by ring
        _ = a*(81*z+271) := by rw [id]; ring
        _ = 128*2^(162*(m+1)+11) := by
          rw [he,show 162*(m+1)+11=162+(162*m+11) by omega,Nat.pow_add]
          dsimp [a]
          ring

/-- Arbitrarily long genuine ordinary prefixes obey this lower bound in
the residue of the reverse implication, for the displayed exponent family. -/
theorem mersenne_family (m : Nat) : ∃ z : Nat, z%48=17 ∧
    81*z+271=128*2^(162*m+11) ∧ run 7 z+1=2^(162*m+11) ∧
    ∀ j ≤ 162*m+18, 9*z ≤ 16*run j z := by
  obtain ⟨z,hz,eq⟩ := family_source m
  obtain ⟨ep,bound⟩ := mersenne_prefix z (162*m+11) eq
  exact ⟨z,hz,eq,ep,fun j hj => bound j (by omega)⟩

def oddCount : Nat → Nat → Nat
  | 0, _ => 0
  | i+1, x => x%2 + oddCount i (shortcut x)

private theorem count_add (i j x : Nat) :
    oddCount (i+j) x=oddCount i x+oddCount j (run i x) := by
  induction i generalizing x with
  | zero => simp [run,oddCount]
  | succ i ih => simp [Nat.succ_add,run,oddCount,ih,Nat.add_assoc]

private theorem halvings (k a : Nat) :
    run k (2^k*a)=a ∧ oddCount k (2^k*a)=0 := by
  induction k with
  | zero => simp [run,oddCount]
  | succ k ih =>
    have eq : 2^(k+1)*a=2*(2^k*a) := by rw [Nat.pow_succ]; ring
    simpa [eq,run,oddCount,shortcut] using ih

theorem three_odd_upper (b z : Nat) (eq : 81*z+271=128*2^(b+2)) :
    run (9+b) (3*z)=1 ∧ oddCount (9+b) (3*z)=3 := by
  let r := z/128
  have hr : z=128*r+33 := by dsimp [r]; omega
  let A := 864*r+224
  have Aeq : 3*A+64=128*2^b := by
    dsimp [A]
    rw [Nat.pow_add] at eq
    omega
  let w := A/64
  have Aw : A=64*w := by dsimp [w]; omega
  have weq : 3*w+1=2*2^b := by omega
  have wo : w%2=1 := by omega
  have sw : shortcut w=2^b := by
    unfold shortcut
    split <;> omega
  have h0 : shortcut (3*z)=576*r+149 := by unfold shortcut; split <;> omega
  have h1 : shortcut (576*r+149)=A := by dsimp [A]; unfold shortcut; split <;> omega
  have u2 : run 2 (3*z)=A ∧ oddCount 2 (3*z)=2 := by
    have o0 : (3*z)%2=1 := by rw [hr]; omega
    have o1 : (576*r+149)%2=1 := by omega
    simp [run,oddCount,h0,h1,o0,o1]
  have hw := halvings 6 w
  have ht := halvings b 1
  simp only [Nat.mul_one] at ht
  have r8 : run 8 (3*z)=w := by
    rw [show 8=2+6 by decide,run_add,u2.1,Aw]
    exact hw.1
  have o8 : oddCount 8 (3*z)=2 := by
    rw [show 8=2+6 by decide,count_add,u2.1,u2.2,Aw]
    exact (congrArg (2+·) hw.2)
  have r9 : run 9 (3*z)=2^b := by
    rw [show 9=8+1 by decide,run_add,r8]
    exact sw
  have o9 : oddCount 9 (3*z)=3 := by
    rw [show 9=8+1 by decide,count_add,r8,o8]
    simp [oddCount,wo]
  rw [run_add,count_add,r9,o9,ht.1,ht.2]
  decide

/-- One exact rank-three upper certificate coexists with every stated lower
prefix bound. The terminal lower source is an ordinary Mersenne integer. -/
theorem three_odd_family (m : Nat) : ∃ z : Nat, z%48=17 ∧
    run (162*m+18) (3*z)=1 ∧ oddCount (162*m+18) (3*z)=3 ∧
    run 7 z+1=2^(162*m+11) ∧ ∀ j≤162*m+18, 9*z≤16*run j z := by
  obtain ⟨z,hz,eq,ep,bound⟩ := mersenne_family m
  have top := three_odd_upper (162*m+9) z eq
  rw [show 9+(162*m+9)=162*m+18 by omega] at top
  exact ⟨z,hz,top.1,top.2,ep,bound⟩

#print axioms mersenne_prefix
#print axioms mersenne_family
#print axioms three_odd_upper
#print axioms three_odd_family
end MersenneBarrier
