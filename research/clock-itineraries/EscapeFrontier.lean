module

public import ClockRecurrence
public import SynchronousShadow
import all ClockRecurrence
import all FixedGate
import all TernaryItinerary
import all SynchronousShadow

public section
namespace Collatz.Itinerary.EscapeFrontier

open FixedGate ClockRecurrence
set_option autoImplicit false

/-- The exact clock on a segment beginning at an arbitrary odd index. -/
theorem elapsed_add (i j a : Nat) :
    elapsed (i+j) a=elapsed i a+elapsed j (after i a) := by
  induction i generalizing a with
  | zero => simp [elapsed,after]
  | succ i ih =>
    simp only [Nat.succ_add,elapsed,after,ih,Nat.add_assoc]

private theorem floor_bound {a M : Nat} (n : Nat) (odd : a%2=1)
    (floor : ∀ i, i<n → M≤after i a) :
    (M^n*2^(elapsed n a))*after n a ≤ (3*M+1)^n*a := by
  induction n generalizing a with
  | zero => simp [elapsed,after]
  | succ n ih =>
    let y := (next a).2
    let e := (next a).1
    have g : Gap e a y := next_gap odd
    have low : M≤a := floor 0 (by omega)
    have localBound : M*(2^e*y)≤(3*M+1)*a := by
      rw [g.eqn]
      have eq₁ : M*(3*a+1)=3*M*a+M := by grind
      have eq₂ : (3*M+1)*a=3*M*a+a := by grind
      omega
    have rest := ih g.oddTarget (fun i hi => floor (i+1) (by omega))
    have yp : 0<y := by have := g.oddTarget; omega
    apply Nat.le_of_mul_le_mul_left (c:=y) _ yp
    have estimate := Nat.mul_le_mul localBound rest
    simp only [Nat.pow_succ,elapsed,after,Nat.pow_add]
    change y*((M^n*M*(2^e*2^(elapsed n y)))*after n y) ≤ y*((3*M+1)^n*(3*M+1)*a)
    refine Nat.le_trans (Nat.le_of_eq ?_) (Nat.le_trans estimate (Nat.le_of_eq ?_)) <;> ac_rfl

/-- An orbit segment starting no higher than its endpoint has an
explicit upper clock frequency when all its odd inputs exceed a floor. -/
theorem clock_from_floor {a M n P Q : Nat} (odd : a%2=1) (pos : 0<M)
    (floor : ∀ i, i<n → M≤after i a) (ends : a≤after n a)
    (calibration : (3*M+1)^Q ≤ M^Q*2^P) :
    Q*elapsed n a≤P*n := by
  have big := floor_bound n odd floor
  have first := Nat.le_trans (Nat.mul_le_mul_left (M^n*2^(elapsed n a)) ends) big
  have linear := Nat.le_of_mul_le_mul_right first (by omega : 0<a)
  have powers := Nat.le_trans (Nat.pow_le_pow_left linear Q)
    (by rw [←Nat.pow_mul,Nat.mul_comm n Q,Nat.pow_mul]; exact Nat.pow_le_pow_left calibration n)
  rw [Nat.mul_pow,Nat.mul_pow,←Nat.pow_mul,←Nat.pow_mul,←Nat.pow_mul,←Nat.pow_mul] at powers
  rw [Nat.mul_comm n Q] at powers
  have cmp := Nat.le_of_mul_le_mul_left powers (Nat.pow_pos pos)
  have exps := (Nat.pow_le_pow_iff_right (by decide : 1<2)).mp cmp
  simpa only [Nat.mul_comm Q (elapsed n a)] using exps

/-- Credit earned by the odd clock relative to the slope u/v. -/
private def credit (u v a k : Nat) := u*k-v*elapsed k a

private def peak (u v a : Nat) : Nat → Nat
  | 0 => 0
  | k+1 => max (peak u v a k) (credit u v a (k+1))

/-- Increasing the running maximum strictly produces one physical
terminal index whose every nonempty incoming suffix beats the slope. -/
def records (u v a : Nat) : Nat → List Nat
  | 0 => []
  | k+1 =>
    if peak u v a k<credit u v a (k+1) then
      (k+1)::records u v a k
    else records u v a k

private theorem peak_dominates {u v a i n : Nat} (hi : i≤n) :
    credit u v a i≤peak u v a n := by
  induction n with
  | zero => have := Nat.le_zero.mp hi; subst i; simp [credit,peak,elapsed]
  | succ n ih =>
    by_cases h : i≤n
    · exact Nat.le_trans (ih h) (Nat.le_max_left ..)
    · have : i=n+1 := by omega
      subst i
      exact Nat.le_max_right ..

theorem record_suffixes {u v a n : Nat} :
    (records u v a n).Nodup ∧ ∀ k∈records u v a n,
      0<k ∧ k≤n ∧ ∀ i, i<k → v*elapsed k a+u*i<u*k+v*elapsed i a := by
  induction n with
  | zero => simp [records]
  | succ n ih =>
    obtain ⟨nodup,all⟩ := ih
    by_cases fresh : peak u v a n<credit u v a (n+1)
    · rw [records,if_pos fresh]
      refine ⟨List.nodup_cons.2 ⟨fun mem => by have := (all _ mem).2.1; omega,nodup⟩,?_⟩
      intro k hk
      rcases List.mem_cons.1 hk with rfl | old
      · refine ⟨by omega,by omega,?_⟩
        intro i hi
        have h := Nat.lt_of_le_of_lt (peak_dominates (u:=u) (v:=v) (a:=a) (by omega : i≤n)) fresh
        unfold credit at h
        omega
      · obtain ⟨pos,le,h⟩ := all k old
        exact ⟨pos,by omega,h⟩
    · rw [records,if_neg fresh]
      exact ⟨nodup,fun k hk => by obtain ⟨p,l,h⟩ := all k hk; exact ⟨p,by omega,h⟩⟩

private theorem peak_budget {u v a : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    (slope : v≤u) (n : Nat) : peak u v a n≤(u-v)*(records u v a n).length := by
  induction n with
  | zero => simp [peak,records]
  | succ n ih =>
    have ⟨_,_,_,o,_⟩ := route_exists n a odd color
    have gap := (next_gap o).pos
    have inc := snoc_clock n a
    have least : v≤v*(next (after n a)).1 := by
      simpa using Nat.mul_le_mul_left v gap
    have old := peak_dominates (u:=u) (v:=v) (a:=a) (i:=n) (n:=n) (by omega)
    have step : credit u v a (n+1) ≤ peak u v a n+(u-v) := by
      unfold credit at old ⊢
      rw [inc,Nat.mul_succ,Nat.mul_add]
      omega
    by_cases fresh : peak u v a n<credit u v a (n+1)
    · rw [records,if_pos fresh,peak,Nat.max_eq_right (Nat.le_of_lt fresh),List.length_cons,Nat.mul_succ]
      omega
    · rw [records,if_neg fresh,peak,Nat.max_eq_left (by omega)]
      exact ih

/-- A finite, deterministic count for the supplied orbit. It holds
without assuming divergence, convergence or a probability distribution. -/
theorem record_budget {u v a : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    (slope : v≤u) (n : Nat) :
    u*n≤v*elapsed n a+(u-v)*(records u v a n).length := by
  have h := Nat.le_trans (peak_dominates (u:=u) (v:=v) (a:=a) (i:=n) (n:=n) (by omega))
    (peak_budget odd color slope n)
  unfold credit at h
  omega

private theorem escaping_clock {a : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    (escapes : ¬Repeats a) :
    ∃ C K, ∀ n, K≤n → 41*elapsed n a≤65*n+C := by
  obtain ⟨i,high⟩ := eventually_above escapes 2048
  obtain ⟨K,ends⟩ := eventually_above escapes (after i a)
  obtain ⟨_,_,_,oi,_⟩ := route_exists i a odd color
  refine ⟨41*elapsed i a,K+i,?_⟩
  intro n late
  let j := n-i
  have split : i+j=n := by dsimp [j]; omega
  have h := clock_from_floor (M:=2048) (n:=j) (P:=65) (Q:=41) oi (by decide)
    (fun l _ => by rw [←after_add]; exact high _ (by omega))
    (by rw [←after_add,split]; exact ends n (by omega)) (by decide)
  have time := elapsed_add i j a
  rw [split] at time
  omega

/-- Three simultaneous lower frequencies of all-suffix records on the
supplied ordinary orbit. The additive constant covers its initial segment. -/
theorem escaping_records {a : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    (escapes : ¬Repeats a) :
    ∃ C K, ∀ n, K≤n →
      n ≤ 41*(records 8 5 a n).length+C ∧
      23*n ≤ 287*(records 18 11 a n).length+C ∧
      17*n ≤ 41*(records 2 1 a n).length+C := by
  obtain ⟨C,K,late⟩ := escaping_clock odd color escapes
  refine ⟨11*C,K,?_⟩
  intro n hn
  have time := late n hn
  have b₁ := record_budget (u:=8) (v:=5) odd color (by decide) n
  have b₂ := record_budget (u:=18) (v:=11) odd color (by decide) n
  have b₃ := record_budget (u:=2) (v:=1) odd color (by decide) n
  simp only [show 8-5=3 by decide] at b₁
  simp only [show 18-11=7 by decide] at b₂
  simp only [show 2-1=1 by decide,Nat.one_mul] at b₃
  omega

/-- Enumerate the chronological gap words for which every backwards
suffix has strict slope below u/v. -/
def words (u v : Nat) : Nat → List (List Nat)
  | 0 => [[]]
  | b+1 => (words u v b).flatMap fun es =>
      ((List.range (u*(b+1))).filter fun d => v*(d+1+es.sum)<u*(b+1)).map
        (fun d => (d+1)::es)

private theorem word_at_record {a u v k n : Nat} {c : Bool} (odd : a%2=1)
    (color : a%3=digit c) (recorded : k∈records u v a n) (vp : 0<v)
    (b i : Nat) (split : i+b=k) : ∃ es∈words u v b,
      Sparse.Path es (after i a) (after k a) ∧ es.length=b ∧
      elapsed k a=elapsed i a+es.sum := by
  induction b generalizing i with
  | zero =>
    have : i=k := by omega
    subst i
    exact ⟨[],by simp [words],.nil _,rfl,by simp⟩
  | succ b ih =>
    obtain ⟨es,mem,path,len,eqn⟩ := ih (i+1) (by omega)
    obtain ⟨_,_,_,oi,_⟩ := route_exists i a odd color
    let e := (next (after i a)).1
    have g : Gap e (after i a) (after (i+1) a) := by
      rw [after_add i 1]
      exact next_gap oi
    have inc : elapsed (i+1) a=elapsed i a+e := snoc_clock i a
    have clock : elapsed k a=elapsed i a+(e+es.sum) := by omega
    have upper := ((record_suffixes (u:=u) (v:=v) (a:=a) (n:=n)).2 k recorded).2.2 i (by omega)
    rw [clock,←split,Nat.mul_add,Nat.mul_add u] at upper
    have bound : v*(e+es.sum)<u*(b+1) := by omega
    have grow := Nat.mul_le_mul_right (e+es.sum) vp
    simp only [Nat.one_mul] at grow
    have ep := g.pos
    refine ⟨e::es,?_,.cons g path,by simp [len],by simpa using clock⟩
    apply List.mem_flatMap.2 ⟨es,mem,?_⟩
    apply List.mem_map.2 ⟨e-1,?_,congrArg (fun t => t::es) (show e-1+1=e by omega)⟩
    apply List.mem_filter.2
    refine ⟨List.mem_range.2 (by omega),?_⟩
    simp [show e-1+1=e by omega,bound]

private theorem mul_mod_eq {x y m : Nat} (h : x%m=y%m) (t : Nat) :
    (x*t)%m=(y*t)%m := by
  rw [Nat.mul_mod,Nat.mul_mod y,h]

private theorem pow_mod_eq {x y m : Nat} (h : x%m=y%m) (t : Nat) :
    x^t%m=y^t%m := by
  induction t with
  | zero => simp
  | succ t ih => rw [Nat.pow_succ,Nat.pow_succ,Nat.mul_mod,Nat.mul_mod (y^t),ih,h]

/-- The terminal residue determined by one ordinary gap word. -/
def residue (es : List Nat) : Nat :=
  let m := 3^es.length
  ((((m+1)/2)^es.sum)*Shadow.carry es)%m

private theorem path_residue {es : List Nat} {x q : Nat} (p : Sparse.Path es x q) :
    q%3^es.length=residue es := by
  let m := 3^es.length
  let inv := (m+1)/2
  have oddPower (t : Nat) : 3^t%2=1 := by
    induction t with
    | zero => decide
    | succ t ih => rw [Nat.pow_succ,Nat.mul_mod,ih]
  have odd : m%2=1 := oddPower es.length
  have factor : inv*2=m+1 := by dsimp [inv]; omega
  have congr : (inv*2)%m=1%m := by rw [factor,Nat.add_comm,Nat.add_mod_right]
  have cancel := mul_mod_eq (pow_mod_eq congr es.sum) q
  simp only [Nat.one_pow,Nat.one_mul,Nat.mul_pow] at cancel
  have aff := Shadow.affine p
  have scaled : (2^es.sum*q)%m=Shadow.carry es%m := by
    rw [aff]
    change (m*x+Shadow.carry es)%m=_
    rw [Nat.add_comm,Nat.add_mul_mod_self_left]
  have idn := mul_mod_eq scaled (inv^es.sum)
  unfold residue
  change q%m=(inv^es.sum*Shadow.carry es)%m
  rw [←cancel]
  simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using idn

/-- The finite list of ternary residues for one depth. -/
def residues (u v b : Nat) := ((words u v b).map residue).eraseDups

theorem record_residue {a u v k n : Nat} {c : Bool} (odd : a%2=1)
    (color : a%3=digit c) (recorded : k∈records u v a n) (vp : 0<v)
    {b : Nat} (depth : b≤k) : after k a%3^b∈residues u v b := by
  obtain ⟨es,mem,path,len,_⟩ := word_at_record odd color recorded vp b (k-b) (by omega)
  have value := path_residue path
  rw [len] at value
  simp only [residues,List.mem_eraseDups,List.mem_map]
  exact ⟨es,mem,value.symm⟩

private theorem elapsed_lower {a : Nat} (odd : a%2=1) (t : Nat) : t≤elapsed t a := by
  induction t generalizing a with
  | zero => omega
  | succ t ih =>
    have g := next_gap odd
    have := ih g.oddTarget
    have := g.pos
    rw [elapsed]
    omega

/-- Looking back t odd steps from a record adds at most (u-v)t to
every incoming suffix budget at the earlier ordinary endpoint. -/
theorem shifted_record {a u v k n : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    (recorded : k∈records u v a n) (slope : v≤u) {i h t : Nat} (prior : i<h)
    (split : h+t=k) : v*elapsed h a+u*i ≤ u*h+v*elapsed i a+(u-v)*t := by
  obtain ⟨_,_,_,oh,_⟩ := route_exists h a odd color
  have lower := Nat.mul_le_mul_left v (elapsed_lower oh t)
  have earlier := ((record_suffixes (u:=u) (v:=v) (a:=a) (n:=n)).2 k recorded).2.2 i (by omega)
  rw [←split,elapsed_add,Nat.mul_add v,Nat.mul_add u] at earlier
  have balance : u*t=(u-v)*t+v*t := by rw [←Nat.add_mul,Nat.sub_add_cancel slope]
  omega

set_option maxRecDepth 12000 in
set_option maxHeartbeats 5000000 in
theorem depth_eight : (residues 8 5 8).length=104 ∧
    (residues 18 11 8).length=143 ∧ (residues 2 1 8).length=403 := by decide

#print axioms elapsed_add
#print axioms clock_from_floor
#print axioms record_suffixes
#print axioms record_budget
#print axioms escaping_records
#print axioms record_residue
#print axioms shifted_record
#print axioms depth_eight
end Collatz.Itinerary.EscapeFrontier
