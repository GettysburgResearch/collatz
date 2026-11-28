import AffineProfiles

/-! Ordinary Mersenne peaks on a complete refinement of any arithmetic
progression of exponents. The retained progression synchronizes any
prescribed finite list of exponent offsets, including their augmented grades. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.ExponentCylinders
open TwoGapRouting FixedGapClock AffineProfiles

/-- The normalized increment at every binary scale is odd. -/
private theorem increments {q e s : ℕ} (shape : q=1+2^(e+2)*(2*s+1)) (h : ℕ) :
    ∃c : ℕ, q^(2^h)=1+2^(e+2)*2^h*(2*c+1) := by
  induction h with
  | zero => exact ⟨s,by simpa using shape⟩
  | succ h ih =>
    obtain ⟨c,old⟩:=ih
    refine ⟨c+2^e*2^h*(2*c+1)^2,?_⟩
    rw [Nat.pow_succ 2 h,Nat.pow_mul,old]
    ring

private theorem grows {q e s : ℕ} (shape : q=1+2^(e+2)*(2*s+1)) (i : ℕ) :
    ∃w : ℕ, i≤w ∧ q^i=1+2^(e+2)*w := by
  induction i with
  | zero => exact ⟨0,by simp,by simp⟩
  | succ i ih =>
    obtain ⟨w,le,old⟩:=ih
    have positive : 0<(2*s+1)*(1+2^(e+2)*w) := by positivity
    refine ⟨w+(2*s+1)*(1+2^(e+2)*w),by omega,?_⟩
    rw [Nat.pow_succ,old,shape]; ring

private theorem attain {q e s A : ℕ} (shape : q=1+2^(e+2)*(2*s+1)) (odd : A%2=1)
    (h t : ℕ) : ∃i w : ℕ, A*q^i=A+2^(e+2)*(t+2^h*w) := by
  induction h with
  | zero =>
    obtain ⟨w,le,form⟩:=grows shape t
    have bound : t≤A*w := le.trans (Nat.le_mul_of_pos_left w (by omega))
    exact ⟨t,A*w-t,by rw [form,show t+2^0*(A*w-t)=A*w by simp; omega]; ring⟩
  | succ h ih =>
    obtain ⟨i,w,old⟩:=ih
    rcases Nat.mod_two_eq_zero_or_one w with even|isOdd
    · exact ⟨i,w/2,by rw [old,show 2^(h+1)*(w/2)=2^h*w by rw [Nat.pow_succ,Nat.mul_assoc]; congr 1; omega]⟩
    obtain ⟨c,inc⟩:=increments shape h
    have qo : q%2=1 := by
      rw [shape,show 2^(e+2)*(2*s+1)=2*(2^e*(2*(2*s+1))) by ring]
      omega
    have prod : (A*q^i*(2*c+1))%2=1 := by simp [Nat.mul_mod,Nat.pow_mod,odd,qo]
    let W:=w+A*q^i*(2*c+1)
    have we : 2*(W/2)=W := by dsimp [W]; omega
    refine ⟨i+2^h,W/2,?_⟩
    calc
      A*q^(i+2^h)=A*q^i+2^(e+2)*2^h*(A*q^i*(2*c+1)) := by rw [Nat.pow_add,inc]; ring
      _=A+2^(e+2)*(t+2^h*W) := by
        conv_lhs => lhs; rw [old]
        dsimp [W]; ring
      _=A+2^(e+2)*(t+2^(h+1)*(W/2)) := by rw [Nat.pow_succ 2 h,Nat.mul_assoc (2^h) 2,we]

/-- Every target class of the normalized powers has a whole arithmetic
progression of exponents as preimages, with ordinary nonnegative lifts. -/
private theorem attain_all {q e s A : ℕ} (shape : q=1+2^(e+2)*(2*s+1)) (odd : A%2=1)
    (h t : ℕ) : ∃i : ℕ, ∀u : ℕ, ∃v : ℕ,
    A*q^(i+2^h*u)=A+2^(e+2)*(t+2^h*v) := by
  obtain ⟨i,w,old⟩:=attain shape odd h t
  obtain ⟨c,inc⟩:=increments shape h
  refine ⟨i,?_⟩
  intro u
  induction u with
  | zero => exact ⟨w,by simpa using old⟩
  | succ u ih =>
    obtain ⟨v,now⟩:=ih
    let k:=i+2^h*u
    refine ⟨v+A*q^k*(2*c+1),?_⟩
    calc
      A*q^(i+2^h*(u+1))=A*q^k+2^(e+2)*2^h*(A*q^k*(2*c+1)) := by
        rw [show i+2^h*(u+1)=k+2^h by dsimp [k]; ring,Nat.pow_add,inc]; ring
      _=A+2^(e+2)*(t+2^h*(v+A*q^k*(2*c+1))) := by
        conv_lhs => lhs; rw [show A*q^k=_ from now]
        ring

private theorem nine_shape (b : ℕ) (bp : 0<b) :
    ∃e s : ℕ, 9^b=1+2^(e+2)*(2*s+1) := by
  have nine : 9≤9^b := by simpa only [Nat.pow_one] using Nat.pow_le_pow_right (by decide : 0<9) bp
  have mod4 : 9^b%4=1 := by simp [Nat.pow_mod]
  let w:=(9^b-1)/4
  have wp : w≠0 := by dsimp [w]; omega
  obtain ⟨e,c,co,eq⟩:=Nat.exists_eq_two_pow_mul_odd wp
  have cp:=Nat.odd_iff.mp co
  refine ⟨e,c/2,?_⟩
  rw [show 2*(c/2)+1=c by omega,show 2^(e+2)=2^e*4 from Nat.pow_add ..]
  have wf : 9^b=1+4*w := by dsimp [w]; omega
  rw [wf,eq]; ring

private def peakProfile (A d : ℕ) : Profile := ⟨d,3^d*A-1⟩

/-- Along any prescribed exponent progression there is an entire
subprogression where all requested peak powers have one actual endpoint
and one augmented grade after a single common number of postpeak steps. -/
theorem peak_progression (a b : ℕ) (bp : 0<b) (gaps : List ℕ) :
    ∃r P H : ℕ, 0<P ∧ ∀u d : ℕ, d∈gaps →
      let m:=a+b*(r+P*u)
      run H (3^(m+d)-1)=run H (3^m-1) ∧
      d+odds H (3^(m+d)-1)=odds H (3^m-1) := by
  obtain ⟨e,s,shape⟩:=nine_shape b bp
  let A:=3^a
  let q:=9^b
  let n:=e+2
  let f (d : ℕ):=peakProfile A d
  let post (d : ℕ):=advance n 0 (f d)
  obtain ⟨h,t,common⟩:=finite_coalesce (post 0) (gaps.map post)
  obtain ⟨i,classes⟩:=attain_all shape (show A%2=1 by dsimp [A]; simp [Nat.pow_mod]) h t
  refine ⟨2*i,2*2^h,n+h,by positivity,?_⟩
  intro u d hd
  let m:=a+b*(2*i+(2*2^h)*u)
  obtain ⟨v,power⟩:=classes u
  have expo : 3^m=A*q^(i+2^h*u) := by
    dsimp [m,A,q]
    rw [show a+b*(2*i+2*2^h*u)=a+2*(b*(i+2^h*u)) by ring,Nat.pow_add,Nat.pow_mul]
    change _*9^(b*(i+2^h*u))=_
    rw [Nat.pow_mul]
  have pos (l : ℕ) : 0<3^l*A := Nat.mul_pos (by positivity) (by dsimp [A]; positivity)
  have starts (l : ℕ) : 3^(m+l)-1=value (f l) (2^n*(t+2^h*v)) := by
    rw [Nat.add_comm m l,Nat.pow_add,expo,power]
    change 3^l*(A+2^n*(t+2^h*v))-1=3^l*(2^n*(t+2^h*v))+(3^l*A-1)
    rw [Nat.mul_add]; have := pos l; omega
  have ties := common (post d) (List.mem_map.mpr ⟨d,hd,rfl⟩)
  have representations (l : ℕ) :
      run (n+h) (3^(m+l)-1)=value (advance h t (post l)) v ∧
      l+odds (n+h) (3^(m+l)-1)=(advance h t (post l)).count := by
    have one:=cylinder n 0 (t+2^h*v) (f l)
    simp only [Nat.zero_add] at one
    obtain ⟨two,gr⟩:=cylinder h t v (post l)
    obtain ⟨hh,gg⟩:=append n h (3^(m+l)-1)
    rw [starts l] at hh gg ⊢
    rw [hh,gg,one.1]
    exact ⟨two,by rw [←Nat.add_assoc,show l+odds n _=(post l).count from one.2,gr]⟩
  have both:=representations d
  have ref:=representations 0
  rw [ties] at both
  simpa only [Nat.add_zero,Nat.zero_add] using And.intro (both.1.trans ref.1.symm) (both.2.trans ref.2.symm)

#print axioms peak_progression
end Collatz.ExponentCylinders
