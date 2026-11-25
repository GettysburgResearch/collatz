import GateVisits
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

/-! Ordinary ancestor costs at an all-odd prefix of a ternarily divisible source.
The rival has arbitrary length and can start at any smaller ordinary integer. -/
namespace MersenneAncestors
open EscapeCore

private theorem grade_le (n t : ℕ) : ones n t ≤ t := by
  induction t with
  | zero => rfl
  | succ t ih => unfold ones; split <;> omega

private theorem shifted_lower (n t : ℕ) :
    3^(ones n t)*(n+1) ≤ 2^t*(state n t+1) := by
  induction t with
  | zero => simp [state, ones]
  | succ t ih =>
    by_cases e : state n t % 2 = 0
    · have hs : 2*(step (state n t)+1) = state n t+2 := by simp [step,e]; omega
      simp only [ones, e, ite_true, state, pow_succ]
      rw [Nat.mul_assoc, hs]
      exact ih.trans (Nat.mul_le_mul_left _ (by omega))
    · have hs : 2*(step (state n t)+1) = 3*(state n t+1) := by simp [step,e]; omega
      simp only [ones, e, ite_false, state, pow_succ]
      rw [Nat.mul_assoc (2^t), hs]
      simpa only [Nat.mul_comm,Nat.mul_assoc,Nat.mul_left_comm] using Nat.mul_le_mul_left 3 ih

private theorem shifted_upper (n t : ℕ) :
    2^t*(state n t+1) ≤ 3^t*(n+1) := by
  obtain ⟨b,hb,bc⟩ := affine n t
  have hg := Nat.mul_le_mul_right n (Nat.pow_le_pow_right (by decide : 0<3) (grade_le n t))
  rw [Nat.mul_add, Nat.mul_one, Nat.mul_add, Nat.mul_one]
  omega

/-- A strict binary source bound is transported using the actual odd grade.
It lets us recover a lower source bound from an exactly ternary-aligned threshold. -/
theorem threshold {n t D : ℕ} (h : n < 2^t*D) :
    state n t < 3^(ones n t)*D := by
  induction t generalizing D with
  | zero => simpa [state, ones] using h
  | succ t ih =>
    rw [pow_succ, Nat.mul_assoc] at h
    have prev := ih (D:=2*D) h
    by_cases e : state n t%2=0
    · simp only [state,ones,e,ite_true,step]
      rw [show 3^ones n t*(2*D) = 2*(3^ones n t*D) by ring] at prev
      omega
    · simp only [state,ones,e,ite_false,step,pow_succ]
      rw [show 3^ones n t*(2*D) = 2*(3^ones n t*D) by ring] at prev
      rw [show 3^ones n t*3*D=3*(3^ones n t*D) by ring]
      omega

/-- The unreduced initial all-odd word and its endpoint, including its last clock. -/
theorem staircase {x i a : ℕ} (start : x+1=2^i*a) :
    state x i+1=3^i*a ∧ ones x i=i := by
  induction i generalizing x a with
  | zero => simpa [state, ones] using start
  | succ i ih =>
    have odd : x%2≠0 := by rw [pow_succ,Nat.mul_right_comm] at start; omega
    have first : 2*(step x+1)=3*(x+1) := by simp [step,odd]; omega
    have next : step x+1=2^i*(3*a) := by
      rw [start,pow_succ] at first
      nlinarith only [first]
    obtain ⟨endpoint,grade⟩ := ih next
    rw [show i+1=1+i by omega, GateVisits.state_add, GateVisits.ones_add]
    change state (step x) i+1=3^(1+i)*a ∧ ones x 1+ones (step x) i=1+i
    have g : ones x 1 = 1 := by simp [ones,state,odd]
    rw [endpoint,grade,g,pow_add]; simp [Nat.mul_assoc,Nat.mul_comm]

private theorem before {x i y j : ℕ} (less : y<x) (early : j≤i)
    (top : 2^i*(state x i+1)=3^i*(x+1)) : state y j ≠ state x i := by
  intro hit
  obtain ⟨d,rfl⟩ := Nat.exists_eq_add_of_le early
  have up := shifted_upper y j
  rw [hit] at up
  have lower := Nat.mul_le_mul_right (state x (j+d)+1)
    (Nat.mul_le_mul_left (2^j) (Nat.pow_le_pow_left (by decide : 2≤3) d))
  have h := Nat.le_trans lower (show (2^j*3^d)*(state x (j+d)+1) ≤ 3^(j+d)*(y+1) by
    rw [pow_add]
    simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using Nat.mul_le_mul_left (3^d) up)
  rw [← pow_add,top] at h
  have := Nat.le_of_mul_le_mul_left h (by positivity)
  omega

private theorem after {x i y t h : ℕ} (divides : 3^h ∣ x)
    (budget : ones y (t+i) ≤ i+h)
    (top : 2^i*(state x i+1)=3^i*(x+1))
    (hit : state y (t+i)=state x i) : x ≤ y := by
  let z := state y t
  let p := ones y t
  let v := ones z i
  have grades : ones y (t+i)=p+v := GateVisits.ones_add y t i
  have suffix : state z i=state x i := (GateVisits.state_add y t i).symm.trans hit
  obtain ⟨w,hw⟩ := divides
  obtain ⟨d,hd⟩ := Nat.exists_eq_add_of_le (grades ▸ budget : p+v≤i+h)
  let D := 3^d*w
  have factor : 3^i*x=3^v*(3^p*D) := by
    dsimp [D]
    rw [hw,← Nat.mul_assoc,← pow_add,hd,pow_add,pow_add]
    ring
  obtain ⟨b,aff,carry⟩ := affine z i
  rw [suffix] at aff
  have lo : 3^v*(3^p*D) ≤ 3^v*z := by
    change 2^i*state x i=3^v*z+b at aff
    rw [Nat.mul_add,Nat.mul_one,Nat.mul_add,Nat.mul_one,factor] at top
    omega
  have zlo := Nat.le_of_mul_le_mul_left lo (by positivity)
  have ylo : 2^t*D ≤ y := by
    by_contra! small
    exact (Nat.not_lt_of_ge zlo) (threshold small)
  let P := 3^(p+v)
  let S := 2^t*3^i
  have aligned : S*x=P*(2^t*D) := by
    dsimp [S,P]
    rw [Nat.mul_assoc,factor,pow_add]; ring
  have lhs : S*x≤P*y := aligned ▸ Nat.mul_le_mul_left P ylo
  have rhs : P*(y+1)≤S*(x+1) := by
    have hlow := shifted_lower y (t+i)
    rw [hit, grades, pow_add 2, Nat.mul_assoc,top] at hlow
    simpa only [P,S,Nat.mul_assoc] using hlow
  have ps : P≤S := by rw [Nat.mul_add,Nat.mul_one,Nat.mul_add,Nat.mul_one] at rhs; omega
  have lower := (Nat.mul_le_mul_right x ps).trans lhs
  exact Nat.le_of_mul_le_mul_left lower (by dsimp [P]; positivity)

/-- Without a deadline on the rival shortcut clock, an actual merger with any
smaller natural source needs more than i+h odd steps during this entire arm. -/
theorem excess_grade {x i y j h : ℕ} (block : 2^i ∣ x+1) (depth : 3^h ∣ x)
    (smaller : y<x) (meet : state y j=state x i) : i+h < ones y j := by
  obtain ⟨a,ha⟩ := block
  have top : 2^i*(state x i+1)=3^i*(x+1) := by rw [(staircase ha).1,ha]; ring
  by_cases early : j≤i
  · exact False.elim (before smaller early top meet)
  · obtain ⟨t,ht⟩ := Nat.exists_eq_add_of_le (by omega : i≤j)
    rw [show j=t+i by omega] at meet ⊢
    by_contra! budget
    exact (Nat.not_le_of_gt smaller) (after depth budget top meet)

private theorem binary_lift (L b a : ℕ) :
    state (b+2^L*a) L=state b L+3^(ones b L)*a ∧
    ones (b+2^L*a) L=ones b L := by
  induction L generalizing b a with
  | zero => simp [state,ones]
  | succ L ih =>
    let e := b%2
    have hp : (b+2^(L+1)*a)%2=b%2 := by rw [pow_succ,Nat.mul_right_comm]; omega
    have hs : step (b+2^(L+1)*a)=step b+2^L*(3^e*a) := by
      rw [pow_succ,Nat.mul_right_comm] at hp ⊢
      rcases (show b%2=0 ∨ b%2=1 by omega) with h|h
      · simp [step,hp,e,h]; omega
      · simp [step,hp,e,h]
        rw [show 2^L*(3*a)=3*(2^L*a) by ring]; omega
    have one (n : ℕ) : ones n 1=n%2 := by simp [ones,state]; split <;> omega
    have split (n : ℕ) : state n (L+1)=state (step n) L ∧
        ones n (L+1)=n%2+ones (step n) L := by
      rw [show L+1=1+L by omega,GateVisits.state_add,GateVisits.ones_add,one]
      exact ⟨rfl,rfl⟩
    obtain ⟨a1,a2⟩ := split (b+2^(L+1)*a)
    obtain ⟨b1,b2⟩ := split b
    obtain ⟨r1,r2⟩ := ih (step b) (3^e*a)
    rw [a1,a2,b1,b2,hp,hs,r1,r2,pow_add]
    dsimp [e]
    constructor
    · ring
    · rfl

private theorem light_carry (n k : ℕ) :
    2^k*state n k ≤ 3^(ones n k)*n+2^k*3^(ones n k) := by
  induction k with
  | zero => simp [state,ones]
  | succ k ih =>
    by_cases e : state n k%2=0
    · have hs : 2*step (state n k)=state n k := by simp [step,e]; omega
      simp only [state,ones,e,ite_true,pow_succ]
      rw [Nat.mul_assoc (2^k),hs]
      nlinarith only [ih,show 0≤2^k*3^(ones n k) by omega]
    · have hs : 2*step (state n k)=3*state n k+1 := by simp [step,e]; omega
      have pos := Nat.mul_le_mul_left (2^k) (Nat.one_le_pow (ones n k) 3 (by decide))
      simp only [state,ones,e,ite_false,pow_succ]
      rw [Nat.mul_assoc (2^k),hs]
      have q := Nat.add_le_add (Nat.mul_le_mul_left 3 ih) pos
      have nonneg : 0≤2^k*3^(ones n k) := Nat.zero_le _
      nlinarith only [q,nonneg]

/-- The surplus beyond the ternary valuation gives an ordinary shadow from a
small seed to a small endpoint, carrying at least h native odd departures. -/
theorem bounded_shadow {x a y i k L h d : ℕ} (source : x=3^h*a)
    (large : 2*3^d≤a) (smaller : y<x) (block : 2^i ∣ x+1)
    (hit : state y ((k+L)+i)=state x i)
    (total : ones y ((k+L)+i)=i+h+d) (cut : ones y k=d) :
    ∃ b, b<3^d ∧ state b L<3^i ∧ h≤ones b L ∧ 2^L≤(2*3^d)*3^(ones b L) := by
  obtain ⟨a0,ha0⟩ := block
  have top : 2^i*(state x i+1)=3^i*(x+1) := by rw [(staircase ha0).1,ha0]; ring
  let Y := state y k
  let z := state y (k+L)
  let r := ones Y L
  let v := ones z i
  have g : r+v=i+h := by
    rw [GateVisits.ones_add y (k+L) i,GateVisits.ones_add y k L,cut] at total
    change d+r+v=i+h+d at total
    omega
  have rv : h≤r := by have hv := grade_le z i; change v≤i at hv; omega
  have factor : 3^i*x=3^v*(3^r*a) := by
    rw [source,← Nat.mul_assoc,← pow_add,← g,pow_add]; ring
  have z_eq : state Y L=z := (GateVisits.state_add y k L).symm
  obtain ⟨bc,aff,budget⟩ := affine z i
  have tgt : state z i=state x i := (GateVisits.state_add y (k+L) i).symm.trans hit
  rw [tgt] at aff
  change 2^i*state x i=3^v*z+bc at aff
  have full : 3^v*(3^r*a)≤3^v*z := by
    rw [Nat.mul_add,Nat.mul_one,Nat.mul_add,Nat.mul_one,factor] at top; omega
  have zl := Nat.le_of_mul_le_mul_left full (by positivity)
  have yl : 2^L*a≤Y := by
    by_contra! small
    have := threshold small
    rw [z_eq] at this; exact (Nat.not_lt_of_ge zl) this
  obtain ⟨b,hY⟩ := Nat.exists_eq_add_of_le yl
  have Yeq : Y=b+2^L*a := by omega
  obtain ⟨sl,gr⟩ := binary_lift L b a
  rw [← Yeq,z_eq] at sl
  rw [← Yeq] at gr
  change r=ones b L at gr
  let P := 3^(h+d)
  let S := 2^(k+L)
  have lower := shifted_lower y ((k+L)+i)
  rw [hit,total,show i+h+d=i+(h+d) by omega,pow_add 3,pow_add 2] at lower
  rw [Nat.mul_assoc (2^(k+L)),top] at lower
  have bound : P*(y+1) ≤ S*(x+1) := by
    apply Nat.le_of_mul_le_mul_left (c:=3^i) _ (by positivity)
    simpa only [P,S,Nat.mul_comm,Nat.mul_assoc,Nat.mul_left_comm] using lower
  have small : 3^d*y<S*a := by
    by_contra! neg
    have scaled : S*x≤P*y := by
      simpa only [S,P,source,pow_add,Nat.mul_assoc,Nat.mul_left_comm,Nat.mul_comm] using
        Nat.mul_le_mul_left (3^h) neg
    have ps : P≤S := by rw [Nat.mul_add,Nat.mul_one,Nat.mul_add,Nat.mul_one] at bound; omega
    have := Nat.le_of_mul_le_mul_left ((Nat.mul_le_mul_right x ps).trans scaled)
      (by dsimp [P]; positivity)
    omega
  have cap := light_carry y k
  rw [cut] at cap
  change 2^k*Y ≤ 3^d*y+2^k*3^d at cap
  have sa : S*a=2^k*(2^L*a) := by dsimp [S]; rw [pow_add, Nat.mul_assoc]
  have hb : b<3^d := by
    rw [Yeq,Nat.mul_add] at cap
    rw [sa] at small
    exact Nat.lt_of_mul_lt_mul_left (a:=2^k) (by omega : 2^k*b<2^k*3^d)
  have end_small : state b L<3^i := by
    have A : 2^i*state x i+2^i=3^v*(3^r*a)+3^i := by
      simpa only [Nat.mul_add,Nat.mul_one,factor] using top
    rw [← gr] at sl
    have exactZ : 3^v*z=3^v*(3^r*a)+3^v*state b L := by rw [sl]; ring
    have scaled : 3^v*state b L<3^i := by
      have positive : 0<2^i := by positivity
      omega
    exact (Nat.le_mul_of_pos_left _ (by positivity : 0<3^v)).trans_lt scaled
  have ratio : S≤2*P := by
    have q : S*a≤3^d*y+S*3^d := by
      have dk : 2^k≤S := by dsimp [S]; exact Nat.pow_le_pow_right (by decide) (by omega)
      have left : S*a≤2^k*Y := sa ▸ Nat.mul_le_mul_left _ yl
      exact left.trans (cap.trans (Nat.add_le_add_left (Nat.mul_le_mul_right _ dk) _))
    have q2 : S*a≤3^d*x+S*3^d := q.trans (Nat.add_le_add_right
      (Nat.mul_le_mul_left _ (Nat.le_of_lt smaller)) _)
    have wx : 3^d*x=P*a := by dsimp [P]; rw [source,pow_add]; ring
    rw [wx] at q2
    have Slarge := Nat.mul_le_mul_left S large
    apply Nat.le_of_mul_le_mul_right (c:=a) _ (Nat.lt_of_lt_of_le (Nat.mul_pos (by decide) (by positivity)) large)
    nlinarith only [Slarge,q2]
  refine ⟨b,hb,end_small,gr ▸ rv,?_⟩
  have dL : 2^L≤S := by dsimp [S]; exact Nat.pow_le_pow_right (by decide) (by omega)
  have rbound := Nat.mul_le_mul_left (2*3^d) (Nat.pow_le_pow_right (by decide : 0<3) rv)
  rw [← gr]
  exact (dL.trans ratio).trans (by simpa only [P,pow_add,Nat.mul_assoc,Nat.mul_left_comm,
    Nat.mul_comm] using rbound)

#print axioms threshold
#print axioms staircase
#print axioms excess_grade
#print axioms bounded_shadow
end MersenneAncestors
