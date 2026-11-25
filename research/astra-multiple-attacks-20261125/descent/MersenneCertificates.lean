import SurplusProperness
import UniversalProposal

namespace MersenneCertificates
open EscapeCore

/-- Exact ternary valuation, normalized unit, and a lower bound for that unit. -/
theorem mersenne_unit (r : ℕ) :
    ∃ A, 2^(2*3^r)=1+3^(r+1)*(3*A+1) ∧ 3^r≤3*A+1 := by
  induction r with
  | zero => exact ⟨0,by decide,by decide⟩
  | succ r ih =>
    obtain ⟨A,e,b⟩ := ih
    let K := 3^r
    let U := 3*A+1
    refine ⟨A+K*U^2+K^2*U^3,?_,?_⟩
    · rw [show 2*3^(r+1)=(2*3^r)*3 by rw [pow_succ]; ring,pow_mul,e]
      dsimp [K,U]
      rw [pow_succ 3 (r+1),pow_succ 3 r]; ring
    · have hu : 1≤U^2 := Nat.one_le_pow _ _ (by dsimp [U]; omega)
      have kc := Nat.mul_le_mul_left K hu
      dsimp [K] at kc ⊢
      rw [pow_succ]
      nlinarith only [kc, Nat.zero_le (3^(r*2)*U^3),Nat.zero_le ((3^r)^2*U^3)]

private theorem half_power (k : ℕ) : state (2^k) k=1 := by
  induction k with
  | zero => rfl
  | succ k ih =>
    have e : step (2^(k+1))=2^k := by rw [pow_succ]; simp [step]
    rw [show k+1=1+k by omega,GateVisits.state_add]
    change state (step (2^(1+k))) k=1
    rw [Nat.add_comm 1 k,e,ih]

theorem good_quotient {q m : ℕ} (hm : 0<m) (eq : 3*q+1=2^m) : state q m=1 := by
  obtain ⟨k,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : m≠0)
  rw [pow_succ] at eq
  have odd : q%2≠0 := by omega
  have first : step q=2^k := by simp [step,odd]; omega
  change state q (k+1)=1
  rw [show k+1=1+k by omega,GateVisits.state_add]
  change state (step q) k=1
  rw [first,half_power]

private theorem odd_power (r : ℕ) : ∃ v, 3^(2*r+1)=4*v+3 := by
  induction r with
  | zero => exact ⟨0,rfl⟩
  | succ r ih =>
    obtain ⟨v,eq⟩ := ih
    refine ⟨9*v+6,?_⟩
    rw [show 2*(r+1)+1=(2*r+1)+2 by omega,pow_add,eq]
    ring

/-- The full binary staircase and its adjacent smaller Mersenne staircase
join two physical steps after the longer staircase ends. -/
theorem neighbor {x s m r : ℕ} (mersenne : x+1=2^m) (adj : x=2*s+1)
    (even : m=2*r+2) :
    state x (m+2)=state s (m+1) ∧ ones x (m+2)=m ∧ ones s (m+1)=m := by
  let d := 2*r+1
  have md : m=d+1 := by dsimp [d]; omega
  have sm : s+1=2^d := by rw [adj,md,pow_succ] at mersenne; omega
  obtain ⟨v,eq⟩ := odd_power r
  change 3^d=4*v+3 at eq
  obtain ⟨ex,gx⟩ := MersenneAncestors.staircase (x:=x) (i:=m) (a:=1) (by simpa using mersenne)
  obtain ⟨es,gs⟩ := MersenneAncestors.staircase (x:=s) (i:=d) (a:=1) (by simpa using sm)
  have xe : state x m=12*v+8 := by
    have g : 3^m=12*v+9 := by rw [md,pow_succ,eq]; ring
    rw [g] at ex; omega
  have se : state s d=4*v+2 := by rw [eq] at es; omega
  have sx : state (12*v+8) 2=3*v+2 ∧ ones (12*v+8) 2=0 := by
    have e1 : (12*v+8)%2=0 := by omega
    have e2 : (6*v+4)%2=0 := by omega
    have f1 : step (12*v+8)=6*v+4 := by simp [step,e1]; omega
    have f2 : step (6*v+4)=3*v+2 := by simp [step,e2]; omega
    simp [state,ones,f1,f2,e1,e2]
  have ss : state (4*v+2) 2=3*v+2 ∧ ones (4*v+2) 2=1 := by
    have e1 : (4*v+2)%2=0 := by omega

    have f1 : step (4*v+2)=2*v+1 := by simp [step,e1]; omega
    have f2 : step (2*v+1)=3*v+2 := by simp [step]; omega
    simp [state,ones,f1,f2,e1]
  rw [show m+1=d+2 by omega,GateVisits.state_add x,GateVisits.state_add s,
    GateVisits.ones_add x,GateVisits.ones_add s,xe,se,sx.1,ss.1,sx.2,ss.2,gx,gs]
  omega

/-- A genuinely smaller positive *multiple of three*, its two clocks,
and exact odd counts at the later common endpoint. -/
theorem terminal_certificate {x h a m r w : ℕ} (src : x=3^h*a)
    (unit : 0<a) (scaled : w+1=2^h*a) (triple : 3∣w) (hpos : 0<h)
    (mword : x+1=2^m) (even : m=2*r+2) :
    ∃ v, w=3*v ∧ 0<v ∧ w<x ∧ state w ((h+1)+(m+1))=state x (m+2)
      ∧ ones w ((h+1)+(m+1))=h+m ∧ ones x (m+2)=m := by
  obtain ⟨v,hv⟩ := triple
  have hpow : 2≤2^h := by simpa using Nat.pow_le_pow_right (by decide : 0<2) hpos
  have wpos : 0<w := by have := Nat.mul_le_mul_right a hpow; omega
  have wx : w<x := by
    have q := Nat.mul_le_mul_right a (Nat.pow_le_pow_left (by decide : 2≤3) h)
    omega
  rcases Nat.exists_eq_succ_of_ne_zero (by omega : m≠0) with ⟨j,mj⟩
  have xodd : x%2=1 := by rw [mj,pow_succ] at mword; omega
  let s := x/2
  have adj : x=2*s+1 := by dsimp [s]; omega
  obtain ⟨merger,gx,gs⟩ := neighbor mword adj even
  obtain ⟨we,wg⟩ := MersenneAncestors.staircase scaled
  have landing : state w h=2*s := by omega
  have gate : state w (h+1)=s := by simp [state,landing,step]
  have work : ones w (h+1)=h := by simp [ones,landing,wg]
  exact ⟨v,hv,by omega,wx,by rw [GateVisits.state_add,gate,← merger],
    by rw [GateVisits.ones_add,gate,work,gs],gx⟩

private theorem even_pow_unit (k : ℕ) : ∃ v, 2^(2*k)=3*v+1 := by
  induction k with
  | zero => exact ⟨0,rfl⟩
  | succ k ih =>
    obtain ⟨v,e⟩ := ih
    refine ⟨4*v+1,?_⟩
    rw [show 2*(k+1)=2*k+2 by omega,pow_add,e]; ring

/-- The obstruction and later actual certificate coexist for one chosen
ordinary triple and its convergent lower arm, beyond any requested thresholds. -/
theorem cofinal_certificates (I D H0 : ℕ) : ∃ h m q w,
    H0≤h ∧ I≤m ∧ 3*q+1=2^m ∧ (∃ A, 3*q=3^h*(3*A+1)) ∧ 0<q ∧ state q m=1 ∧
    (∀ i y j, i≤I → y<3*q → state y j=state (3*q) i → i+h+D<ones y j) ∧
    (∃ v, w=3*v ∧ 0<v ∧ w<3*q ∧ state w ((h+1)+(m+1))=state (3*q) (m+2) ∧
       ones w ((h+1)+(m+1))=h+m ∧ ones (3*q) (m+2)=m) := by
  obtain ⟨H,bound⟩ := SurplusProperness.unbounded_extra I D
  let k := H+H0+I+D+2
  let r := 2*k+1
  let h := r+1
  let m := 2*3^r
  obtain ⟨A,exp,grow⟩ := mersenne_unit r
  let a := 3*A+1
  let q := 3^r*a
  have base : 3*q=3^h*a := by dsimp [q,h]; rw [pow_succ]; ring
  have meq : 3*q+1=2^m := by dsimp [m]; rw [exp,base]; dsimp [a,h]; omega
  have rh : 3^D*3≤3^r := by
    rw [← pow_succ]
    exact Nat.pow_le_pow_right (by decide) (by dsimp [r,k]; omega)
  have au : 2*3^D≤a := by change 2*3^D≤3*A+1; omega
  have high : H≤h ∧ H0≤h := by dsimp [h,r,k]; omega
  have mi : I≤m := by
    have rlow := Nat.lt_pow_self (by decide : 1<3) (n:=r)
    dsimp [m,r,k] at rlow ⊢; omega
  have mp : 0<m := by dsimp [m]; positivity
  have htwo : h=2*(k+1) := by dsimp [h,r]; omega
  obtain ⟨v,ve⟩ := even_pow_unit (k+1)
  let w := 3*(v*a+A)
  have weq : w+1=2^h*a := by rw [htwo,ve]; dsimp [w,a]; ring
  refine ⟨h,m,q,w,high.2,mi,meq,⟨A,base⟩,by dsimp [q,a]; positivity,good_quotient mp meq,?_,?_⟩
  · intro i y j hi small hit
    have power : 2^i ∣ 3*q+1 := meq ▸ Nat.pow_dvd_pow 2 (hi.trans mi)
    exact bound high.1 base au hi power small hit
  · have nonzero : 0<3^r := by positivity
    exact terminal_certificate base (by dsimp [a]; omega) weq ⟨_,rfl⟩ (by dsimp [h]; omega)
      meq (r:=3^r-1) (by dsimp [m]; omega)

private theorem run_eq (t x : ℕ) : UniversalProposal.run t x=state x t := by
  induction t generalizing x with
  | zero => rfl
  | succ t ih =>
    rw [UniversalProposal.run,ih,show t+1=1+t by omega,GateVisits.state_add]
    rfl

/-- An actual smaller-triple certificate for the resident checker. Only
physical adjacency-component membership is required, with unrestricted clocks.
The normalized unit condition includes ternary depths one and two. -/
theorem adjacent_checker {q h a s v : ℕ} (high : 3*q=3^h*a)
    (adj : 3*q=2*s+1) (scaled : 3*v+1=2^h*a) (positive : 0<v)
    (meets : UniversalProposal.Meets (3*q) s) :
    ∃ c : UniversalProposal.Certificate, UniversalProposal.check q c=true := by
  obtain ⟨i,j,eq⟩ := meets
  have hx := (MersenneAncestors.staircase scaled).1
  have hite : state (3*v) h=2*s := by omega
  have hit : state (3*v) (h+1)=s := by simp [state,hite,step]
  have lt : v<q := by
    have pw := Nat.mul_le_mul_right a (Nat.pow_le_pow_left (by decide : 2≤3) h)
    omega
  have merger : UniversalProposal.run i (3*q)=UniversalProposal.run ((h+1)+j) (3*v) := by
    rw [eq,run_eq,run_eq,GateVisits.state_add,hit]
  exact ⟨⟨v,i,(h+1)+j⟩,decide_eq_true ⟨positive,lt,merger⟩⟩

/-- A seven-shortcut path from a smaller triple to the adjacent half.
Both the cost and the source formula are independent of deeper ternary digits. -/
theorem four_odd_partner {x s : ℕ} (dep : 243∣x) (adj : x=2*s+1) :
    ∃ v, 0<v ∧ 3*v<x ∧ state (3*v) 7=s ∧ ones (3*v) 7=4 := by
  obtain ⟨u,hu⟩ := dep
  let t := u/2
  have ux : u=2*t+1 := by dsimp [t]; omega
  have sx : s=243*t+121 := by omega
  let v := 128*t+63
  have v0 : 3*v=384*t+189 := by dsimp [v]; omega
  let z := 384*t+189
  have l1 : step z=576*t+284 := by unfold z step; split <;> omega
  have l2 : step (576*t+284)=288*t+142 := by unfold step; split <;> omega
  have l3 : step (288*t+142)=144*t+71 := by unfold step; split <;> omega
  have l4 : step (144*t+71)=216*t+107 := by unfold step; split <;> omega
  have l5 : step (216*t+107)=324*t+161 := by unfold step; split <;> omega
  have l6 : step (324*t+161)=486*t+242 := by unfold step; split <;> omega
  have l7 : step (486*t+242)=243*t+121 := by unfold step; split <;> omega
  refine ⟨v,by dsimp [v]; omega,by omega,?_,?_⟩
  · rw [v0]; change state z 7=s
    simp only [state,l1,l2,l3,l4,l5,l6,l7,sx]
  · rw [v0]; change ones z 7=4
    simp only [state,ones,l1,l2,l3,l4,l5,l6]
    have ez : z%2≠0 := by dsimp [z]; omega
    simp only [ez,show (576*t+284)%2=0 by omega,show (288*t+142)%2=0 by omega,
      show (144*t+71)%2≠0 by omega,show (216*t+107)%2≠0 by omega,
      show (324*t+161)%2≠0 by omega,show (486*t+242)%2=0 by omega,ite_true,ite_false]

/-- Every actual adjacent-arm merger at a 243-divisible triple gives a
literal certificate for the resident checker, for either ternary unit. -/
theorem four_odd_checker {q s : ℕ} (dep : 243∣3*q) (adj : 3*q=2*s+1)
    (meets : UniversalProposal.Meets (3*q) s) :
    ∃ c : UniversalProposal.Certificate, UniversalProposal.check q c=true := by
  obtain ⟨v,hv,less,hit,_⟩ := four_odd_partner dep adj
  obtain ⟨i,j,eq⟩ := meets
  have merger : UniversalProposal.run i (3*q)=UniversalProposal.run (7+j) (3*v) := by
    rw [eq,run_eq,run_eq,GateVisits.state_add,hit]
  have smaller : v<q := Nat.lt_of_mul_lt_mul_left less
  exact ⟨⟨v,i,7+j⟩,decide_eq_true ⟨hv,smaller,merger⟩⟩

/-- At the later Mersenne gate the extra odd work required of a smaller
triple is at most four even when the ternary valuation tends to infinity. -/
theorem four_odd_exit {x m r : ℕ} (dep : 243∣x) (mers : x+1=2^m) (even : m=2*r+2) :
    ∃ v, 0<v ∧ 3*v<x ∧ state (3*v) (7+(m+1))=state x (m+2) ∧
      ones (3*v) (7+(m+1))=m+4 ∧ ones x (m+2)=m := by
  let s := x/2
  have xm : x%2=1 := by rw [even,show 2*r+2=(2*r+1)+1 by omega,pow_succ] at mers; omega
  have ax : x=2*s+1 := by dsimp [s]; omega
  obtain ⟨v,hv,lt,reach,work⟩ := four_odd_partner dep ax
  obtain ⟨eq,gx,gs⟩ := neighbor mers ax even
  exact ⟨v,hv,lt,by rw [GateVisits.state_add,reach,← eq],
    by rw [GateVisits.ones_add,reach,work,gs]; omega,gx⟩

/-- Every smaller arm reaching the next even site first crosses the preceding
Mersenne site. Its last step is forced to be even, preserving its odd grade. -/
theorem next_site {x m y j : ℕ} (mers : x+1=2^m) (long : 2≤m)
    (small : y<x) (meet : state y j=state x (m+1)) :
    ∃ k, j=k+1 ∧ state y k=state x m ∧ ones y j=ones y k := by
  obtain ⟨d,md⟩ := Nat.exists_eq_add_of_le long
  obtain ⟨endpt,_⟩ := MersenneAncestors.staircase (x:=x) (i:=m) (a:=1) (by simpa using mers)
  have p : ∃ n, 3^m=3*n := by
    refine ⟨3^(d+1),?_⟩
    rw [show m=(d+1)+1 by omega,pow_succ,Nat.mul_comm]
  obtain ⟨n,pn⟩ := p
  have odd3 (k : ℕ) : 3^k%2=1 := by
    induction k with
    | zero => decide
    | succ k ih => rw [pow_succ]; omega
  have even : state x m%2=0 := by have := odd3 m; omega
  have half : 2*state x (m+1)=state x m := by simp [state,step,even]; omega
  have larg : 2*2^m ≤ 3^m := by
    rw [md,pow_add,pow_add]
    have q := Nat.pow_le_pow_left (by decide : 2≤3) d
    omega
  cases j with
  | zero =>
    change y=state x (m+1) at meet
    omega
  | succ k =>
    have hail : 2*step (state y k)=2*state x (m+1) := congrArg (2*·) meet
    rw [half] at hail
    have eq0 : state y k%2=0 := by
      by_contra no
      have odd : 2*step (state y k)=3*state y k+1 := by simp [step,no]; omega
      omega
    have same : 2*step (state y k)=state y k := by simp [step,eq0]; omega
    exact ⟨k,rfl,by omega,by simp [ones,eq0]⟩

#print axioms mersenne_unit
#print axioms good_quotient
#print axioms neighbor
#print axioms terminal_certificate
#print axioms cofinal_certificates
#print axioms adjacent_checker
#print axioms four_odd_partner
#print axioms four_odd_checker
#print axioms four_odd_exit
#print axioms next_site
end MersenneCertificates
