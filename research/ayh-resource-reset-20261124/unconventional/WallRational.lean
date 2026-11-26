import WallGate

namespace WallRational
open WordRank CollatzReverseBasin WallRefinement

/-- Signed numerator dynamics for a fixed odd denominator d. -/
def step (d p : Int) : Int := if p%2=0 then p/2 else (3*p+d)/2
def runD (d : Int) : Nat → Int → Int
  | 0,p => p
  | h+1,p => runD d h (step d p)
def grade (d : Int) : Nat → Int → Nat
  | 0,_ => 0
  | h+1,p => grade d h (step d p)+(if p%2=0 then 0 else 1)

theorem runD_add (d p : Int) (a b : Nat) : runD d (a+b) p=runD d b (runD d a p) := by
  induction a generalizing p with
  | zero => simp [runD]
  | succ a ih => rw [Nat.succ_add,runD,runD,ih]

theorem grade_add (d p : Int) (a b : Nat) :
    grade d (a+b) p=grade d a p+grade d b (runD d a p) := by
  induction a generalizing p with
  | zero => simp [runD,grade]
  | succ a ih => rw [Nat.succ_add,grade,grade,runD,ih]; omega

private theorem step_lift (d p u : Int) (x : Nat) (hd : d%2=1)
    (eq : d*(x:Int)=2*u+p) :
    d*(shortcut x:Int)=(if p%2=0 then (1:Int) else 3)*u+step d p := by
  have par : (x:Int)%2=p%2 := by
    have h := congrArg (fun z : Int => z%2) eq
    rw [Int.mul_emod,hd] at h
    simpa using h
  by_cases hp : p%2=0
  · have x0 : x%2=0 := by omega
    obtain ⟨t,ht⟩ : ∃t:Nat,x=2*t := ⟨x/2,by omega⟩
    subst x
    have e : shortcut (2*t)=t := by simp [shortcut]
    simp only [e,step,hp,ite_true,one_mul]
    push_cast at eq
    have ep : p=2*(p/2) := by omega
    grind
  · have x1 : x%2=1 := by omega
    obtain ⟨t,ht⟩ : ∃t:Nat,x=2*t+1 := ⟨x/2,by omega⟩
    subst x
    have e : shortcut (2*t+1)=3*t+2 := by simp [shortcut]; omega
    simp only [e,step,hp,ite_false]
    push_cast at eq ⊢
    have ep : 2*((3*p+d)/2)=3*p+d := by omega
    grind

/-- Exact ordinary endpoint after exposing h prescribed low rational bits.
The signed p and free coefficient u may have either sign. -/
theorem lift (d p u : Int) (h x : Nat) (hd : d%2=1)
    (eq : d*(x:Int)=2^h*u+p) :
    d*(run h x:Int)=3^(grade d h p)*u+runD d h p := by
  induction h generalizing p u x with
  | zero => simpa [runD,grade,run] using eq
  | succ h ih =>
    let m : Int := if p%2=0 then 1 else 3
    have e : d*(x:Int)=2*(2^h*u)+p := by rw [eq,pow_succ]; ring
    have e' := step_lift d p (2^h*u) x hd e
    have nxt : d*(shortcut x:Int)=2^h*(m*u)+step d p := by rw [e']; dsimp [m]; ring
    rw [run,ih (step d p) (m*u) (shortcut x) nxt,runD,grade,pow_add]
    dsimp [m]
    split <;> ring

/-- If a signed reference phase returns after h steps, its iterated clock
gains the same grade on each lap. -/
theorem lap (d p : Int) (h g i : Nat) (ret : runD d h p=p) (cnt : grade d h p=g) :
    runD d (h*i) p=p ∧ grade d (h*i) p=g*i := by
  induction i with
  | zero => simp [runD,grade]
  | succ i ih =>
    rw [Nat.mul_succ,Nat.mul_succ,runD_add,grade_add,ih.1,ih.2,ret,cnt]
    exact ⟨rfl,rfl⟩

end WallRational
