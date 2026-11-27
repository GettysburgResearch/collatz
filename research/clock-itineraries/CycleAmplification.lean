module

public import CycleRows
public import FixedGate
import all FixedGate

public section
namespace Collatz.Itinerary.CycleAmplification

set_option autoImplicit false

private theorem compose {q y x v u : Nat} {tail pre : List Bool}
    (suf : Route q tail v y) (front : Route y pre u x) :
    Route q (tail++pre) (v+u) x := by
  induction suf with
  | nil => simpa using front
  | cons gap mark rest ih =>
    simpa [Nat.add_assoc] using Route.cons gap mark (ih front)

private theorem laps {q A : Nat} {marks : List Bool} (loop : Route q marks A q) (r : Nat) :
    ∃ ms, ms.length=r*marks.length ∧ Route q ms (r*A) q := by
  induction r with
  | zero => exact ⟨[],by simp,by simpa using Route.nil q⟩
  | succ r ih =>
    obtain ⟨ms,len,p⟩ := ih
    refine ⟨marks++ms,by simp [len,Nat.succ_mul,Nat.add_comm],?_⟩
    simpa [Nat.succ_mul,Nat.add_comm] using compose loop p

private theorem upper_scale {q x s : Nat} {marks : List Bool} (p : Route q marks s x) :
    2^s*q≤4^marks.length*x := by
  induction p with
  | nil => simp
  | @cons q y x e t mark ms g _ _ ih =>
    have edge := g.eqn
    have hy := g.oddSource
    have upper : 2^e*q≤4*y := by omega
    calc
      2^(e+t)*q=2^t*(2^e*q) := by rw [Nat.pow_add]; ac_rfl
      _ ≤ 2^t*(4*y) := Nat.mul_le_mul_left _ upper
      _ = 4*(2^t*y) := by ac_rfl
      _ ≤ 4*(4^ms.length*x) := Nat.mul_le_mul_left _ ih
      _ = 4^(mark::ms).length*x := by rw [List.length_cons,Nat.pow_succ]; ac_rfl

private theorem loop_rates {q A : Nat} {ms : List Bool} (h : Route q ms A q)
    (hq : 2<q) (hlen : 0<ms.length) :
    3^ms.length < 2^A ∧ A < 2*ms.length ∧ q%2=1 ∧ ∃ c : Bool, q%3=digit c := by
  cases h with
  | nil => simp at hlen
  | @cons _ y _ e t r rs edge _ rest =>
    have g := edge.eqn
    have pe := edge.pos
    have pp := Nat.two_pow_pos e
    have p2 : 2≤2^e := by
      simpa using Nat.pow_le_pow_right (by decide : 0<2) (show 1≤e by omega)
    have mult := Nat.mul_le_mul p2 (show 3≤q by omega)
    have lo : 3*y<2^e*q := by omega
    have hi : 2^e*q<4*y := by omega
    have past := rest.scale
    have other := upper_scale rest
    have rate1 : 3^(r::rs).length*q < 2^(e+t)*q := by
      calc
        _ = 3*(3^rs.length*q) := by rw [List.length_cons,Nat.pow_succ]; ac_rfl
        _ ≤ 3*(2^t*y) := Nat.mul_le_mul_left _ past
        _ = 2^t*(3*y) := by ac_rfl
        _ < 2^t*(2^e*q) := Nat.mul_lt_mul_of_pos_left lo (Nat.two_pow_pos _)
        _ = _ := by rw [Nat.pow_add]; ac_rfl
    have rate2 : 2^(e+t)*q < 4^(r::rs).length*q := by
      calc
        _ = 2^t*(2^e*q) := by rw [Nat.pow_add]; ac_rfl
        _ < 2^t*(4*y) := Nat.mul_lt_mul_of_pos_left hi (Nat.two_pow_pos _)
        _ = 4*(2^t*y) := by ac_rfl
        _ ≤ 4*(4^rs.length*q) := Nat.mul_le_mul_left _ other
        _ = _ := by rw [List.length_cons,Nat.pow_succ]; ac_rfl
    have lt := Nat.lt_of_mul_lt_mul_right rate2
    have pow : 4^(r::rs).length = 2^(2*(r::rs).length) := by rw [Nat.pow_mul]
    rw [pow] at lt
    have color : ∃ c : Bool, q%3=digit c := by
      have mod3 : 2^e*q%3=1 := by omega
      rw [Nat.mul_mod] at mod3
      by_cases h0 : q%3=0
      · simp [h0] at mod3
      · by_cases h1 : q%3=1
        · exact ⟨false,h1⟩
        · exact ⟨true, by change q%3=2; omega⟩
    exact ⟨Nat.lt_of_mul_lt_mul_right rate1,
      (Nat.pow_lt_pow_iff_right (by decide : 1<2)).1 lt,edge.oddTarget,color⟩

private theorem bernoulli (v r : Nat) :
    (v+r)*v^r ≤ v*(v+1)^r := by
  induction r with
  | zero => simp
  | succ r ih =>
    have shift : (v+(r+1))*v ≤ (v+r)*(v+1) := by grind
    calc
      _ = ((v+(r+1))*v)*v^r := by rw [Nat.pow_succ]; ac_rfl
      _ ≤ ((v+r)*(v+1))*v^r := Nat.mul_le_mul_right _ shift
      _ = ((v+r)*v^r)*(v+1) := by ac_rfl
      _ ≤ (v*(v+1)^r)*(v+1) := Nat.mul_le_mul_right _ ih
      _ = _ := by rw [Nat.pow_succ]; ac_rfl

/-- At r=v*t laps, Bernoulli's inequality gives dilation at least t+1. -/
private theorem stretch {v u p t m : Nat} (vp : 0<v) (gain : v<u)
    (tp : 0<t) (hp : v*p≤t) (hm : m≤t) :
    ((v*t)*p+m+1)*(v^(v*t))^6 < (u^(v*t))^6 := by
  let r := v*t
  have ber := bernoulli v r
  have up := Nat.mul_le_mul_left v (Nat.pow_le_pow_left (show v+1≤u by omega) r)
  have fact : (v+r)*v^r=v*((t+1)*v^r) := by dsimp [r]; grind
  rw [fact] at ber
  have ampl := Nat.le_of_mul_le_mul_left (Nat.le_trans ber up) vp
  have sq : r*p ≤ t*t := by
    have l : r*p=(v*p)*t := by dsimp [r]; ac_rfl
    rw [l]; exact Nat.mul_le_mul_right t hp
  have poly : r*p+m+1<(t+1)^2 := by
    have eq : (t+1)^2=t*t+2*t+1 := by grind
    omega
  have poly6 := Nat.lt_of_lt_of_le poly (Nat.pow_le_pow_right (by omega : 0<t+1) (by decide : 2≤6))
  have expand := Nat.mul_lt_mul_of_pos_right poly6 (Nat.pow_pos (Nat.pow_pos vp (n:=r)) (n:=6))
  have done := Nat.pow_le_pow_left ampl 6
  rw [Nat.mul_pow] at done
  exact Nat.lt_of_lt_of_le expand done

private theorem fill {q A r m : Nat} {marks : List Bool} {c : Bool}
    (loop : Route q marks A q) (hq : 2<q) (odd : q%2=1) (color : q%3=digit c)
    (short : A<2*marks.length) (hm : 2≤m) (large : 6*m+7≤r)
    (boost : (r*marks.length+m+1)*((3^marks.length)^r)^6 < ((2^A)^r)^6) :
    ∃ x ms, ms.length=r*marks.length+m ∧ Route q ms (2*(r*marks.length+m)) x ∧
      (r*marks.length+m+1)*(3^(r*marks.length+m)*x)^6 <
        (2^(2*(r*marks.length+m))*q)^6 := by
  let p := marks.length
  obtain ⟨k,clock⟩ := Nat.exists_eq_add_of_le (show A+1≤2*p from short)
  let b := r*p+m
  let u := r*(1+k)+2*m
  have prefixClock : 6*(m-2)+19≤u := by
    have le := Nat.mul_le_mul_left r (show 1≤1+k by omega)
    dsimp [u]; omega
  have balance : r*A+u=2*b := by
    calc
      _ = r*(A+1+k)+2*m := by dsimp [u]; grind
      _ = r*(2*p)+2*m := by rw [←clock]
      _ = _ := by dsimp [b]; grind
  let w := List.replicate (m-1) false
  have wl : w.length=m-1 := by simp [w]
  obtain ⟨r₀,x,front⟩ := free_marks odd color w (by omega) (s:=u) (by omega)
  have plen : (r₀::w).length=m := by simp only [List.length_cons]; omega
  obtain ⟨ms,len,tail⟩ := laps loop r
  have full := compose tail front
  rw [balance] at full
  have length : (ms++(r₀::w)).length=b := by rw [List.length_append,len,plen]
  have bound := front.scale
  rw [plen] at bound
  have P : 3^b*x=(3^p)^r*(3^m*x) := by
    dsimp [b]; rw [Nat.pow_add,Nat.mul_comm r p,Nat.pow_mul]; ac_rfl
  have Q : 2^(2*b)*q=(2^A)^r*(2^u*q) := by
    rw [←balance,Nat.pow_add,Nat.mul_comm r A,Nat.pow_mul]; ac_rfl
  refine ⟨x,ms++(r₀::w),length,full,?_⟩
  change (b+1)*(3^b*x)^6 < (2^(2*b)*q)^6
  rw [P,Q,Nat.mul_pow ((3^p)^r) (3^m*x) 6,Nat.mul_pow ((2^A)^r) (2^u*q) 6]
  have pos := Nat.pow_pos (Nat.mul_pos (Nat.two_pow_pos u) (by omega : 0<q)) (n:=6)
  have base := Nat.pow_le_pow_left bound 6
  calc
    _ = ((b+1)*((3^p)^r)^6)*(3^m*x)^6 := by rw [Nat.mul_assoc]
    _ ≤ ((b+1)*((3^p)^r)^6)*(2^u*q)^6 := Nat.mul_le_mul_left _ base
    _ < ((2^A)^r)^6*(2^u*q)^6 := Nat.mul_lt_mul_of_pos_right boost pos

/-- A single fixed endpoint of a nontrivial cycle supports distorted physical
rows at every sufficiently large b. No analytic floor is assumed. -/
theorem cycle_amplifies_eventually (cycle : CycleRows.NontrivialCycle) :
    ∃ q B, 2<q ∧ ∀ b, B≤b → ∃ x ms, ms.length=b ∧ Route q ms (2*b) x ∧
      (b+1)*(3^b*x)^6 < (2^(2*b)*q)^6 := by
  obtain ⟨q,A,marks,hq,hl,loop⟩ := cycle
  obtain ⟨gain,short,odd,c,color⟩ := loop_rates loop hq hl
  let p := marks.length
  let v := 3^p
  let d := v*p
  let T := 6*d+20
  have vp : 0<v := Nat.pow_pos (by decide : 0<3)
  have dp : 0<d := Nat.mul_pos vp hl
  refine ⟨q,d*T+2,hq,?_⟩
  intro b hb
  obtain ⟨a,eq⟩ := Nat.exists_eq_add_of_le hb
  let s := a%d
  let t := T+a/d
  let m := s+2
  let r := v*t
  have small : s<d := Nat.mod_lt _ dp
  have split : s+d*(a/d)=a := Nat.mod_add_div _ _
  have row : b=r*p+m := by
    calc
      b = d*T+2+a := eq
      _ = d*T+2+(s+d*(a/d)) := by rw [split]
      _ = r*p+m := by dsimp [r,t,m,d]; grind
  have lower : 6*d+20≤t := Nat.le_add_right _ _
  have cap : 6*m+7≤r := by
    have le : t≤r := by simpa [r] using Nat.mul_le_mul_right t (show 1≤v by omega)
    dsimp [m]; omega
  have lift := stretch (v:=v) (u:=2^A) (p:=p) (t:=t) (m:=m) vp gain
    (by omega) (by change d≤t; omega)
    (by dsimp [m]; omega)
  obtain ⟨x,ms,len,path,h⟩ := fill (r:=r) (m:=m) loop hq odd color short (by dsimp [m]; omega) cap lift
  rw [row]; exact ⟨x,ms,len,path,h⟩

theorem cycle_amplifies (cycle : CycleRows.NontrivialCycle) :
    ∀ B, ∃ b, B≤b ∧ CycleRows.Witness b := by
  obtain ⟨q,N,hq,allRows⟩ := cycle_amplifies_eventually cycle
  intro B
  obtain ⟨x,ms,len,path,h⟩ := allRows (B+N) (by omega)
  exact ⟨B+N,by omega,q,x,ms,hq,len,path,h⟩

/-- A positive shift at the endpoint can be transferred to the source.
Each reverse exponent e charges at most the factor 2^(e−1) to the shift. -/
theorem shifted_scale {q s x : Nat} {ms : List Bool} (p : Route q ms s x)
    (d : Nat) (hd : 0<d) :
    2^s*(q+d)≤3^ms.length*(x+2^(s-ms.length)*d) := by
  induction p generalizing d with
  | nil => simp
  | @cons q y x e t mark rs gap _ rest ih =>
    obtain ⟨f,hf⟩ := Nat.exists_eq_add_of_le (show 1≤e from gap.pos)
    have pow : 2^e=2*(2^f) := by rw [hf,Nat.pow_add]
    have pos := Nat.mul_pos (Nat.two_pow_pos f) hd
    have edge : 2^e*(q+d)≤3*(y+2^f*d) := by
      rw [Nat.mul_add,gap.eqn,pow]
      have assoc : 2*2^f*d=2*(2^f*d) := by ac_rfl
      rw [assoc]; omega
    have tail := ih (2^f*d) pos
    have depth := rest.depth_le_clock
    have ex : e+t-(mark::rs).length=(t-rs.length)+f := by
      simp only [List.length_cons]; omega
    calc
      2^(e+t)*(q+d) = 2^t*(2^e*(q+d)) := by rw [Nat.pow_add]; ac_rfl
      _ ≤ 2^t*(3*(y+2^f*d)) := Nat.mul_le_mul_left _ edge
      _ = 3*(2^t*(y+2^f*d)) := by ac_rfl
      _ ≤ 3*(3^rs.length*(x+2^(t-rs.length)*(2^f*d))) := Nat.mul_le_mul_left _ tail
      _ = _ := by
        rw [ex,Nat.pow_add,List.length_cons,Nat.pow_succ]
        rw [Nat.mul_assoc (2^(t-rs.length)) (2^f) d]; ac_rfl

/-- The search need only inspect fewer than 10*2^b positive sources. Each
source has a unique ordinary endpoint at its prescribed clock. -/
theorem finite_bounds {b q x : Nat} {ms : List Bool} (len : ms.length=b)
    (p : Route q ms (2*b) x) (test : (b+1)*(3^b*x)^6 < (2^(2*b)*q)^6) :
    x<10*2^b ∧ 2^b*(q+1)≤11*3^b := by
  have bp : 0<b := by
    by_cases z : b=0
    · have empty : ms=[] := by simpa [z] using len
      rw [z] at p test
      subst ms; cases p; simp at test
    · omega
  have budget := shifted_scale p 1 (by decide)
  rw [len,show 2*b-b=b by omega,Nat.mul_one] at budget
  have add : 2^(2*b)*q≤3^b*x+3^b*2^b := by
    rw [Nat.mul_add,Nat.mul_one,Nat.mul_add] at budget; exact Nat.le_trans (Nat.le_add_right _ _) budget
  have source : x<10*2^b := by
    apply Classical.byContradiction
    intro no
    have hi := Nat.mul_le_mul_left (3^b) (show 10*2^b≤x by omega)
    have regroup : 3^b*(10*2^b)=10*(3^b*2^b) := by ac_rfl
    rw [regroup] at hi
    have ratio : 10*(2^(2*b)*q) ≤ 11*(3^b*x) := by omega
    have raised := Nat.pow_le_pow_left ratio 6
    rw [Nat.mul_pow 10 _ 6,Nat.mul_pow 11 _ 6] at raised
    have min := Nat.mul_le_mul_right ((3^b*x)^6) (show 2≤b+1 by omega)
    omega
  have total := Nat.mul_le_mul_left (3^b) (show x+2^b≤11*2^b by omega)
  have dyad : 2^(2*b)*(q+1)=2^b*(2^b*(q+1)) := by
    rw [show 2*b=b+b by omega,Nat.pow_add]; ac_rfl
  have triad : 3^b*(11*2^b)=2^b*(11*3^b) := by ac_rfl
  have bound := Nat.le_trans budget total
  rw [dyad,triad] at bound
  exact ⟨source,Nat.le_of_mul_le_mul_left bound (Nat.two_pow_pos _)⟩

theorem bounded_witness_iff (b : Nat) :
    CycleRows.Witness b ↔ ∃ (q x : Nat) (ms : List Bool),
      2<q ∧ x<10*2^b ∧ 2^b*(q+1)≤11*3^b ∧ ms.length=b ∧ Route q ms (2*b) x ∧
      (b+1)*(3^b*x)^6 < (2^(2*b)*q)^6 := by
  constructor
  · rintro ⟨q,x,ms,hq,len,p,h⟩
    have bounds := finite_bounds len p h
    exact ⟨q,x,ms,hq,bounds.1,bounds.2,len,p,h⟩
  · rintro ⟨q,x,ms,hq,_,_,len,p,h⟩
    exact ⟨q,x,ms,hq,len,p,h⟩

private theorem source_unit {q s x : Nat} {rs : List Bool} (p : Route q rs s x)
    (nonempty : 0<rs.length) : x%2=1 ∧ ∃ c : Bool, x%3=digit c := by
  induction p with
  | nil => simp at nonempty
  | @cons q y x e t mark ms g hc rest ih =>
    by_cases h : 0<ms.length
    · exact ih h
    · have empty : ms=[] := by
        have zero : ms.length=0 := by omega
        simpa using zero
      subst ms; cases rest; exact ⟨g.oddSource,mark,hc⟩

/-- Decide a row by checking the deterministic forward orbit of each candidate
source below 10*2^b. Both the exact odd-step count and shortcut clock are fixed. -/
@[expose] def witnessTest (b : Nat) : Bool :=
  (List.range (10*2^b)).any fun x =>
    let q := FixedGate.after b x
    decide (x%2=1 ∧ x%3≠0 ∧ 2<q ∧ FixedGate.elapsed b x=2*b ∧
      (b+1)*(3^b*x)^6 < (2^(2*b)*q)^6)

theorem witnessTest_iff (b : Nat) : witnessTest b=true ↔ CycleRows.Witness b := by
  simp only [witnessTest,List.any_eq_true,List.mem_range,decide_eq_true_eq]
  constructor
  · rintro ⟨x,_,odd,modulo,hq,clock,test⟩
    have color : ∃ c : Bool, x%3=digit c := by
      by_cases h : x%3=1
      · exact ⟨false,h⟩
      · exact ⟨true,by change x%3=2; omega⟩
    obtain ⟨c,hc⟩ := color
    obtain ⟨ms,len,p,_,_⟩ := FixedGate.route_exists b x odd hc
    rw [clock] at p
    exact ⟨_,x,ms,hq,len,p,test⟩
  · rintro ⟨q,x,ms,hq,len,p,h⟩
    have bounds := finite_bounds len p h
    have positive : 0<ms.length := by
      cases ms with
      | nil =>
        have zero : b=0 := len.symm
        rw [zero] at h p; cases p; simp at h
      | cons => simp
    obtain ⟨odd,c,color⟩ := source_unit p positive
    have unit : x%3≠0 := by cases c <;> simp [digit,Bool.toNat] at color <;> omega
    obtain ⟨target,clock⟩ := FixedGate.route_read p
    rw [len] at target clock
    exact ⟨x,bounds.1,odd,unit,by rwa [target],clock,by rwa [target]⟩

#print axioms cycle_amplifies_eventually
#print axioms cycle_amplifies
#print axioms bounded_witness_iff
#print axioms witnessTest_iff

set_option maxRecDepth 3000 in
example : witnessTest 0=false ∧ witnessTest 1=false ∧ witnessTest 2=false := by decide

end Collatz.Itinerary.CycleAmplification
