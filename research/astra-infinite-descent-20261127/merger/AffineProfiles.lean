import FixedGapClock
import SharpClock
import Mathlib.Data.Nat.Factorization.Basic

/-! Deterministic coalescence on a refined ordinary binary cylinder for
any finite collection of affine Collatz profiles. A profile records its
already-used odd count, including its contribution to the free slope. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.AffineProfiles
open TwoGapRouting FixedGapClock

structure Profile where
  count : ℕ
  base : ℕ
  deriving DecidableEq

def value (a : Profile) (t : ℕ) : ℕ := 3^a.count*t+a.base

def advance (h t : ℕ) (a : Profile) : Profile :=
  ⟨a.count+odds h (value a t),run h (value a t)⟩

theorem lift (h n u : ℕ) :
    run h (n+2^h*u)=run h n+3^(odds h n)*u ∧
    odds h (n+2^h*u)=odds h n := by
  induction h generalizing n u with
  | zero => simp [run,odds]
  | succ h ih =>
    let z:=2^h*u
    have form : n+2^(h+1)*u=n+2*z := by dsimp [z]; ring
    have parity : (n+2*z)%2=n%2 := by omega
    have st : step (n+2*z)=step n+2^h*(3^(n%2)*u) := by
      by_cases ev : n%2=0
      · have ev' : (n+2*z)%2=0 := parity.trans ev
        rw [step,ite_eq_left ev',step,ite_eq_left ev,ev,pow_zero,Nat.one_mul]
        dsimp [z]; omega
      · have od : n%2=1 := by omega
        have od' : (n+2*z)%2≠0 := by omega
        have eq : 2^h*(3*u)=3*z := by dsimp [z]; ring
        rw [step,ite_eq_right od',step,ite_eq_right ev,od,pow_one,eq]
        omega
    obtain ⟨r,g⟩:=ih (step n) (3^(n%2)*u)
    rw [form]
    simp only [run,odds,st,parity,r,g,pow_add]
    constructor <;> first | rfl | trivial | ring

theorem cylinder (h t u : ℕ) (a : Profile) :
    run h (value a (t+2^h*u))=value (advance h t a) u ∧
    a.count+odds h (value a (t+2^h*u))=(advance h t a).count := by
  have shape : value a (t+2^h*u)=value a t+2^h*(3^a.count*u) := by unfold value; ring
  obtain ⟨r,g⟩:=lift h (value a t) (3^a.count*u)
  rw [shape,r,g]
  simp only [value,advance,pow_add]
  constructor <;> first | rfl | trivial | ring

theorem advance_comp (h t H u : ℕ) (a : Profile) :
    advance H u (advance h t a)=advance (h+H) (t+2^h*u) a := by
  obtain ⟨v,g⟩:=cylinder h t u a
  obtain ⟨r,o⟩:=append h H (value a (t+2^h*u))
  rw [v] at r o
  change Profile.mk ((advance h t a).count+odds H (value (advance h t a) u))
    (run H (value (advance h t a) u)) = Profile.mk
    (a.count+odds (h+H) (value a (t+2^h*u))) (run (h+H) (value a (t+2^h*u)))
  rw [←g,r,o,Nat.add_assoc]

private theorem split_lt {a b : ℕ} (lt : a<b) :
    ∃ j, odds j a=odds j b ∧ run j a%2≠run j b%2 := by
  obtain ⟨j,v,vo,eq⟩:=Nat.exists_eq_two_pow_mul_odd (show b-a≠0 by omega)
  have form : b=a+2^j*v := by omega
  obtain ⟨r,g⟩:=lift j a v
  rw [←form] at r g
  have vParity : v%2=1 := Nat.odd_iff.mp vo
  have odd : 3^(odds j a)%2=1 := by simp [Nat.pow_mod]
  refine ⟨j,g.symm,?_⟩
  rw [r,Nat.add_mod,Nat.mul_mod,odd,vParity]
  omega

private theorem split_at {a b : ℕ} (ne : a≠b) :
    ∃ j, odds j a=odds j b ∧ run j a%2≠run j b%2 := by
  rcases lt_or_gt_of_ne ne with l|g
  · exact split_lt l
  · obtain ⟨j,eq,neq⟩:=split_lt g
    exact ⟨j,eq.symm,Ne.symm neq⟩

private theorem flip (h t : ℕ) (a : Profile) :
    odds h (value a (t+2^h))=odds h (value a t) ∧
    run h (value a (t+2^h))%2+run h (value a t)%2=1 := by
  obtain ⟨r,g⟩:=cylinder h t 1 a
  simp only [Nat.mul_one] at r g
  have odd : 3^((advance h t a).count)%2=1 := by simp [Nat.pow_mod]
  constructor
  · change a.count+_=a.count+_ at g
    omega
  · rw [r]
    change (3^(advance h t a).count*1+(advance h t a).base)%2+_ = 1
    rw [Nat.mul_one,Nat.add_mod,odd]
    change (1+(run h (value a t))%2)%2+_ = 1
    omega

/-- A deterministic finite refinement gives precisely one extra odd
departure to the lower-grade arm. The absolute grade gap drops by one. -/
theorem drop_one (a b : Profile) (lower : a.count<b.count) :
    ∃ h t, (advance h t a).count+(b.count-a.count-1)=(advance h t b).count := by
  have diff : ∃t, value a t≠value b t := by
    by_cases atZero : a.base=b.base
    · refine ⟨1,?_⟩
      have sep : 3^a.count<3^b.count := Nat.pow_lt_pow_right (by norm_num) lower
      simp only [value,Nat.mul_one,atZero]
      omega
    · exact ⟨0,by simpa [value] using atZero⟩
  obtain ⟨t,ne⟩:=diff
  obtain ⟨j,counts,differ⟩:=split_at ne
  have chooseBits : ∃ u, odds j (value a u)=odds j (value b u) ∧
      run j (value a u)%2=1 ∧ run j (value b u)%2=0 := by
    by_cases ok : run j (value a t)%2=1
    · exact ⟨t,counts,ok,by omega⟩
    · obtain ⟨ga,fa⟩:=flip j t a
      obtain ⟨gb,fb⟩:=flip j t b
      exact ⟨t+2^j,ga.trans (counts.trans gb.symm),by omega,by omega⟩
  obtain ⟨u,equal,od,ev⟩:=chooseBits
  have oa : odds (j+1) (value a u)=odds j (value a u)+run j (value a u)%2 := by
    simpa [odds] using (append j 1 (value a u)).2
  have ob : odds (j+1) (value b u)=odds j (value b u)+run j (value b u)%2 := by
    simpa [odds] using (append j 1 (value b u)).2
  rw [od] at oa
  rw [ev] at ob
  refine ⟨j+1,u,?_⟩
  change a.count+odds (j+1) (value a u)+(b.count-a.count-1)=b.count+odds (j+1) (value b u)
  omega

private theorem equal_order (a b : Profile) (eq : a.count=b.count) (ab : a.base≤b.base) :
    ∃h t, advance h t a=advance h t b := by
  let d:=b.base-a.base
  obtain ⟨H,g,core⟩:=cover d a.count
  let y:=3*(4^g*(a.base+1))+1
  have yu : y%3≠0 := by dsimp [y]; omega
  obtain ⟨x,_,congr,l,r,lg,rg⟩:=core H (le_refl H) y yu a.base
  have height:=SharpClock.physical_height H x
  rw [l,lg] at height
  have liftHeight : y≤2^H*y := Nat.le_mul_of_pos_left _ (by positivity)
  have start : a.base≤x := by
    by_contra! no
    have m:=Nat.mul_le_mul_left (4^g) no.le
    have p : 0<(4:ℕ)^g := by positivity
    dsimp [y] at liftHeight height
    nlinarith only [liftHeight,height,m,p,Nat.zero_le (4^g*a.base)]
  obtain ⟨t,div⟩:=(Nat.modEq_iff_dvd' start).mp congr.symm
  have xa : value a t=x := by unfold value; omega
  have xb : value b t=x+d := by unfold value at xa ⊢; rw [←eq]; dsimp [d]; omega
  exact ⟨H,t,by simp [advance,xa,xb,l,r,lg,rg,eq]⟩

private theorem equal_coalesce (a b : Profile) (eq : a.count=b.count) :
    ∃h t, advance h t a=advance h t b := by
  rcases le_total a.base b.base with le|ge
  · exact equal_order a b eq le
  · obtain ⟨h,t,e⟩:=equal_order b a eq.symm ge
    exact ⟨h,t,e.symm⟩

private theorem ascend (n : ℕ) : ∀a b : Profile, a.count+n=b.count →
    ∃h t, advance h t a=advance h t b := by
  induction n with
  | zero => exact fun a b eq => equal_coalesce a b (by omega)
  | succ n ih =>
    intro a b eq
    obtain ⟨h,t,drop⟩:=drop_one a b (by omega)
    obtain ⟨H,u,merged⟩:=ih (advance h t a) (advance h t b) (by omega)
    exact ⟨h+H,t+2^h*u,by simpa only [advance_comp] using merged⟩

/-- Every pair of ordinary affine profiles can be synchronized exactly on
a refined binary cylinder, even when the initial odd grades differ. -/
theorem coalesce (a b : Profile) : ∃h t, advance h t a=advance h t b := by
  rcases le_total a.count b.count with le|ge
  · exact ascend (b.count-a.count) a b (by omega)
  · obtain ⟨h,t,e⟩:=ascend (a.count-b.count) b a (by omega)
    exact ⟨h,t,e.symm⟩

/-- One common ordinary binary refinement synchronizes every member of
any prescribed finite list, simultaneously in position and odd count. -/
theorem finite_coalesce (a : Profile) (F : List Profile) :
    ∃h t, ∀b∈F, advance h t b=advance h t a := by
  induction F with
  | nil => exact ⟨0,0,by simp⟩
  | cons b F ih =>
    obtain ⟨h,t,old⟩:=ih
    obtain ⟨H,u,tie⟩:=coalesce (advance h t b) (advance h t a)
    refine ⟨h+H,t+2^h*u,?_⟩
    intro v hv
    rw [←advance_comp,←advance_comp]
    rcases List.mem_cons.mp hv with eq|mem
    · simpa only [eq] using tie
    · rw [old v mem]

private theorem positive_run (h n : ℕ) (np : 0<n) : 0<run h n := by
  induction h generalizing n with
  | zero => exact np
  | succ h ih =>
    apply ih
    unfold step
    split <;> omega

/-- Every supplied positive n has a natural translate which never shares
its endpoint at the same clock. A dyadic fusion limit synchronizing all
translates therefore cannot specialize to an ordinary positive integer. -/
theorem no_positive_double_sync (h n : ℕ) (np : 0<n) : run h n≠run h (2*n) := by
  cases h with
  | zero => change n≠2*n; omega
  | succ h =>
    have rhs : run (h+1) (2*n)=run h n := by simp [run,step]
    have lhs : run (h+1) n=step (run h n) := by simpa [run] using (append h 1 n).1
    rw [lhs,rhs]
    have p:=positive_run h n np
    unfold step
    split <;> omega

#print axioms no_positive_double_sync
#print axioms drop_one
#print axioms coalesce
#print axioms finite_coalesce
end Collatz.AffineProfiles
