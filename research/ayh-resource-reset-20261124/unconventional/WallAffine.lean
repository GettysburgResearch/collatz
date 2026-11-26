import WallRational

/-! Fixed words in any dyadic class for affine pairs whose odd slopes differ
by a power of three. All calculations use signed integer shortcut orbits. -/
namespace WallAffine
open WallRational

def Meets (x y : Int) : Prop := ∃ a b : Nat, runD 1 a x=runD 1 b y

private theorem meets_refl (x : Int) : Meets x x := ⟨0,0,rfl⟩
private theorem meets_symm {x y : Int} : Meets x y → Meets y x := by
  rintro ⟨a,b,e⟩; exact ⟨b,a,e.symm⟩
private theorem back {x y : Int} : Meets (step 1 x) (step 1 y) → Meets x y := by
  rintro ⟨a,b,e⟩; exact ⟨a+1,b+1,e⟩

def Cell (P : Int → Prop) : Prop := ∃ h : Nat, ∃ r : Int, ∀ z : Int, P (2^h*z+r)

private theorem cell_imp {P Q : Int → Prop} (h : Cell P) (imp : ∀ x, P x → Q x) : Cell Q := by
  obtain ⟨k,r,v⟩ := h
  exact ⟨k,r,fun z => imp _ (v z)⟩

theorem solve_unit (a b y : Int) (odd : a%2=1) (h : Nat) :
    ∃ t k : Int, a*t+b=2^h*k+y := by
  induction h with
  | zero => exact ⟨0,b-y,by ring⟩
  | succ h ih =>
    obtain ⟨t,k,e⟩ := ih
    by_cases kp : k%2=0
    · refine ⟨t,k/2,?_⟩
      rw [e,pow_succ,show (2^h*2)*(k/2)=2^h*(2*(k/2)) by ring]
      rw [show 2*(k/2)=k by omega]
    · refine ⟨t+2^h,(k+a)/2,?_⟩
      calc
        _ = a*t+b+2^h*a := by ring
        _ = 2^h*(k+a)+y := by rw [e]; ring
        _ = _ := by rw [pow_succ,show (2^h*2)*((k+a)/2)=2^h*(2*((k+a)/2)) by ring,
                          show 2*((k+a)/2)=k+a by omega]

theorem cell_pull {P : Int → Prop} (hp : Cell P) (a b : Int) (odd : a%2=1) :
    Cell (fun t => P (a*t+b)) := by
  obtain ⟨h,r,v⟩ := hp
  obtain ⟨t,k,e⟩ := solve_unit a b r odd h
  refine ⟨h,t,fun z => ?_⟩
  have t' : a*(2^h*z+t)+b=2^h*(a*z+k)+r := by
    calc _ = 2^h*(a*z)+(a*t+b) := by ring
         _ = _ := by rw [e]; ring
  change P (a*(2^h*z+t)+b)
  rw [t']
  exact v (a*z+k)

private theorem append_bit (b : Int) {P : Int → Prop} (h : Cell (fun x => P (2*x+b))) :
    Cell P := by
  obtain ⟨k,r,e⟩ := h
  refine ⟨k+1,2*r+b,fun z => ?_⟩
  rw [show (2:Int)^(k+1)*z+(2*r+b)=2*(2^k*z+r)+b by rw [pow_succ];ring]
  exact e z

def Absorb (s : Nat) (D : Int) := Cell (fun x => Meets x (3^s*x+D))

private theorem es (x : Int) : step 1 (2*x)=x := by simp [step]
private theorem os (x : Int) : step 1 (2*x+1)=3*x+2 := by
  simp [step]; omega

private theorem even_zero (s : Nat) (E : Int) (h : Absorb s E) : Absorb s (2*E) := by
  apply append_bit 0
  apply cell_imp h
  intro x yes
  simp only [Int.add_zero]
  apply back
  rw [es,show 3^s*(2*x)+2*E=2*(3^s*x+E) by ring,es]
  exact yes

private theorem down (s : Nat) (E : Int) (h : Absorb s E) :
    Absorb (s+1) (2*E+3^s) := by
  apply append_bit 1
  apply cell_imp (cell_pull h 3 2 (by decide))
  intro x yes
  apply back
  rw [os,show 3^(s+1)*(2*x+1)+(2*E+3^s)=2*(3^s*(3*x+2)+E) by rw [pow_succ];ring,es]
  exact yes

private theorem up_zero (D E : Int) (eq : 3*D+1=2*E) (h : Absorb 1 E) : Absorb 0 D := by
  have odd : D%2=1 := by omega
  apply append_bit 0
  apply cell_imp h
  intro x yes
  apply back
  simp only [pow_zero,Int.one_mul,Int.add_zero,es]
  have wh : 2*x+D=2*(x+D/2)+1 := by omega
  rw [wh,os,show 3*(x+D/2)+2=3*x+E by omega]
  exact yes

private theorem up_one (D E : Int) (eq : 1-3*D=2*E) (h : Absorb 1 E) : Absorb 0 D := by
  have odd : D%2=1 := by omega
  apply append_bit 1
  apply cell_imp (cell_pull h 1 ((D+1)/2) (by decide))
  intro x yes
  apply back
  apply meets_symm
  simp only [pow_zero,Int.one_mul,os]
  rw [show 2*x+1+D=2*(x+(D+1)/2) by omega,es]
  have e : 3*x+2=3*(x+(D+1)/2)+E := by omega
  rw [e]
  simpa using yes

private theorem zero_from (s : Nat) (E : Int) (eq : 3^s+2*E=1) (h : Absorb s E) :
    Absorb s 0 := by
  apply append_bit 1
  apply cell_imp (cell_pull h 3 2 (by decide))
  intro x yes
  apply back
  simp only [Int.add_zero,os]
  have rep : 3^s*(2*x+1)=2*(3^s*x-E)+1 := by
    calc _ = 2*(3^s*x)+3^s := by ring
         _ = _ := by omega
  rw [rep,os,show 3*(3^s*x-E)+2=3^s*(3*x+2)+E by
      have e : 2*3^s+4*E=2 := by omega
      grind]
  exact yes

private theorem strip (s : Nat) (D : Int) (nz : D≠0)
    (each : ∀ o : Int, o%2=1 → o.natAbs ≤ D.natAbs → Absorb s o) : Absorb s D := by
  by_cases odd : D%2=1
  · exact each D odd (by omega)
  · let E := D/2
    have e : D=2*E := by dsimp [E]; omega
    have e0 : E≠0 := by omega
    have small : E.natAbs < D.natAbs := by omega
    have next := strip s E e0 (fun o p b => each o p (by omega))
    exact e ▸ even_zero s E next
termination_by D.natAbs

private theorem zero_level : Absorb 0 0 := by
  refine ⟨0,0,?_⟩
  intro x; simp only [pow_zero,Int.one_mul,Int.add_zero]
  exact meets_refl x

private theorem tiny (D : Int) (h : D.natAbs=1) : Absorb 0 D := by
  have level : Absorb 1 2 := even_zero 1 1 (down 0 0 zero_level)
  have cases : D=1 ∨ D= -1 := by omega
  rcases cases with rfl|rfl
  · exact up_zero 1 2 (by decide) level
  · exact up_one (-1) 2 (by decide) level

private theorem shrink_odd (D E : Int) (big : 1<D.natAbs) (even : E%2=0) (nz : E≠0)
    (size : 2*E.natAbs≤3*D.natAbs+1)
    (smaller : ∀ x : Int, x.natAbs<D.natAbs → Absorb 0 x) : Absorb 1 E := by
  have half : E=2*(E/2) := by omega
  have hz : E/2≠0 := by omega
  have stripped := strip 1 (E/2) hz (by
    intro o odd bound
    let r := (o-1)/2
    have form : o=2*r+3^0 := by dsimp [r]; omega
    have small : r.natAbs<D.natAbs := by dsimp [r]; omega
    exact form ▸ down 0 r (smaller r small))
  exact half ▸ even_zero 1 (E/2) stripped

private theorem equal_slopes (D : Int) : Absorb 0 D := by
  by_cases d0 : D=0
  · exact d0 ▸ zero_level
  by_cases small : D.natAbs=1
  · exact tiny D small
  have big : 1<D.natAbs := by omega
  by_cases even : D%2=0
  · have e : D=2*(D/2) := by omega
    have sm : (D/2).natAbs < D.natAbs := by omega
    exact e ▸ even_zero 0 (D/2) (equal_slopes (D/2))
  · by_cases choice : (3*D+1)%4=0
    · let E := (3*D+1)/2
      have e : 3*D+1=2*E := by dsimp [E]; omega
      exact up_zero D E e (shrink_odd D E big (by dsimp [E]; omega) (by omega) (by omega)
        (fun x hx => equal_slopes x))
    · let E := (1-3*D)/2
      have e : 1-3*D=2*E := by dsimp [E]; omega
      exact up_one D E e (shrink_odd D E big (by dsimp [E]; omega) (by omega) (by omega)
        (fun x hx => equal_slopes x))
termination_by D.natAbs

private theorem three_odd (s : Nat) : ((3:Int)^s)%2=1 := by
  induction s with
  | zero => decide
  | succ s ih => rw [pow_succ,Int.mul_emod,ih]; decide

/-- The two signed orbits meet on a complete dyadic cylinder for every integral
offset and every ratio of slopes that is a nonnegative power of three. -/
theorem absorb (s : Nat) (D : Int) : Absorb s D := by
  induction s generalizing D with
  | zero => exact equal_slopes D
  | succ s ih =>
    have allOdd : ∀ o : Int, o%2=1 → Absorb (s+1) o := by
      intro o h
      let E := (o-3^s)/2
      have p := three_odd s
      have eq : o=2*E+3^s := by dsimp [E]; omega
      exact eq ▸ down s E (ih E)
    have allNonzero : ∀ d : Int, d≠0 → Absorb (s+1) d :=
      fun d nz => strip (s+1) d nz (fun o p _ => allOdd o p)
    by_cases d0 : D=0
    · subst D
      let E : Int := (1-3^(s+1))/2
      have p := three_odd (s+1)
      have powBig : 1<(3:Int)^(s+1) := by
        have z : 0 < (3:Int)^s := by positivity
        rw [pow_succ]; omega
      have e : (3:Int)^(s+1)+2*E=1 := by dsimp [E]; omega
      exact zero_from (s+1) E e (allNonzero E (by omega))
    · exact allNonzero D d0

theorem signed_lift (h : Nat) (t r : Int) :
    runD 1 h (2^h*t+r)=3^(grade 1 h r)*t+runD 1 h r := by
  induction h generalizing t r with
  | zero => simp [runD,grade]
  | succ h ih =>
    by_cases par : r%2=0
    · have e : r=2*(r/2) := by omega
      have er : step 1 r=r/2 := by simp [step,par]
      have ex : 2^(h+1)*t+r=2*(2^h*t+r/2) := by
        calc _ = 2*(2^h*t)+r := by rw [pow_succ];ring
             _ = _ := by omega
      rw [runD,ex,es,ih,grade,runD,er]
      simp [par]
    · have e : r=2*(r/2)+1 := by omega
      have er : step 1 r=3*(r/2)+2 := by nth_rw 1 [e]; exact os _
      have ex : 2^(h+1)*t+r=2*(2^h*t+r/2)+1 := by
        calc _ = 2*(2^h*t)+r := by rw [pow_succ];ring
             _ = _ := by omega
      rw [runD,ex,os,show 3*(2^h*t+r/2)+2=2^h*(3*t)+(3*(r/2)+2) by ring,ih,grade,runD,er]
      simp only [par,ite_false,pow_succ]
      ring

private theorem grouped (p q : Nat) (a b : Int) (le : p≤q) :
    Cell (fun t => Meets (3^p*t+a) (3^q*t+b)) := by
  let d := q-p
  have pp : q=p+d := by dsimp [d]; omega
  have h := cell_pull (absorb d (b-3^d*a)) (3^p) a (three_odd p)
  apply cell_imp h
  intro t ht
  change Meets _ (3^d*(3^p*t+a)+(b-3^d*a)) at ht
  rw [pp,pow_add,show 3^d*(3^p*t+a)+(b-3^d*a)=(3^p*3^d)*t+b by ring] at *
  exact ht

theorem two_slopes (p q : Nat) (a b : Int) :
    Cell (fun t => Meets (3^p*t+a) (3^q*t+b)) := by
  by_cases le : p≤q
  · exact grouped p q a b le
  · exact cell_imp (grouped q p b a (by omega)) (fun _ v => meets_symm v)

/-- Every prescribed dyadic class of the base contains a binary subcylinder
on which the affine mates meet. This universal arithmetic lemma is sufficient
for the periodic-wall application even with negative signed offsets. -/
theorem in_class (s h : Nat) (D r : Int) :
    Cell (fun t => Meets (2^h*t+r) (3^s*(2^h*t+r)+D)) := by
  let r' := 3^s*r+D
  let p := grade 1 h r
  let q := grade 1 h r'
  have ready := two_slopes p (q+s) (runD 1 h r) (runD 1 h r')
  apply cell_imp ready
  intro t ht
  obtain ⟨a,b,e⟩ := ht
  refine ⟨h+a,h+b,?_⟩
  rw [runD_add,runD_add,signed_lift,show 3^s*(2^h*t+r)+D=2^h*(3^s*t)+r' by dsimp [r'];ring,
      signed_lift]
  change runD 1 a (3^p*t+runD 1 h r)=runD 1 b (3^q*(3^s*t)+runD 1 h r')
  simpa [pow_add,mul_assoc] using e

end WallAffine
