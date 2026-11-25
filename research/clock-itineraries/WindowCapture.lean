module

public import FixedGate
public import MinimumDescent
import all TernaryItinerary
import all FixedGate
import all MinimumDescent

public section
namespace Collatz.Itinerary.WindowCapture

open FixedGate
set_option autoImplicit false

/-- Number of binary choices of length k with at most j expensive edges. -/
@[expose] def quota : Nat → Nat → Nat
  | 0, _ => 1
  | k+1, 0 => quota k 0
  | k+1, j+1 => quota k (j+1) + quota k j

private structure Landing (k budget q x : Nat) : Prop where
  odd : x % 2 = 1
  endpoint : after k x = q
  height : 3^k*x ≤ 2^budget*q
  clock : ∃ t, t ≤ budget ∧ run t x = q

private theorem two_children {q : Nat} {c : Bool} (odd : q%2=1) (col : q%3=digit c) :
    ∃ (u v e f : Nat) (a b : Bool), u≠v ∧ e≤4 ∧ f≤6 ∧
      Gap e u q ∧ u%3=digit a ∧ Gap f v q ∧ v%3=digit b := by
  obtain ⟨e,u,le,gu,cu⟩ := one odd col false
  obtain ⟨f,v,lf,gv,cv⟩ := one odd col true
  have ne : u≠v := by change u%3=1 at cu; change v%3=2 at cv; omega
  have diff : e≠f := by
    intro h
    subst f
    have eqn := gu.eqn.symm.trans gv.eqn
    omega
  have par := (gu.parity col).trans (gv.parity col).symm
  by_cases first : e<f
  · exact ⟨u,v,e,f,false,true,ne,by omega,lf,gu,cu,gv,cv⟩
  · exact ⟨v,u,f,e,true,false,Ne.symm ne,by omega,le,gv,cv,gu,cu⟩

private theorem extend {k B C q u x e : Nat} (p : Landing k B u x)
    (edge : Gap e u q) (clock : B+e≤C) : Landing (k+1) C q x := by
  refine ⟨p.odd,?_,?_,?_⟩
  · rw [after_add, p.endpoint]
    change (next u).2=q
    rw [gap_next edge]
  · calc
      3^(k+1)*x = 3*(3^k*x) := by rw [Nat.pow_succ]; ac_rfl
      _ ≤ 3*(2^B*u) := Nat.mul_le_mul_left _ p.height
      _ = 2^B*(3*u) := by ac_rfl
      _ ≤ 2^B*(2^e*q) := Nat.mul_le_mul_left _ (by have := edge.eqn; omega)
      _ = 2^(B+e)*q := by rw [Nat.pow_add]; ac_rfl
      _ ≤ 2^C*q := Nat.mul_le_mul_right _ (Nat.pow_le_pow_right (by decide) clock)
  · obtain ⟨s,hs,hit⟩ := p.clock
    exact ⟨s+e,by omega,by rw [run_add,hit,edge.follow]⟩

private theorem bank (k j q : Nat) {c : Bool} (odd : q%2=1) (col : q%3=digit c) :
    ∃ xs : List Nat, xs.Nodup ∧ xs.length=quota k j ∧
      ∀ x ∈ xs, Landing k (4*k+2*j) q x := by
  induction k generalizing j q c with
  | zero =>
    refine ⟨[q],by simp,by simp [quota],?_⟩
    intro x hx
    have eq : x=q := by simpa using hx
    subst x
    exact ⟨odd,rfl,by simpa using Nat.le_mul_of_pos_left q (Nat.pow_pos (by decide : 0<2)),0,by omega,rfl⟩
  | succ k ih =>
    obtain ⟨u,v,e,f,a,b,ne,he,hf,gu,cu,gv,cv⟩ := two_children odd col
    obtain ⟨xs,ndx,lx,hx⟩ := ih j u gu.oddSource cu
    cases j with
    | zero =>
      exact ⟨xs,ndx,lx,fun x mem => extend (hx x mem) gu (by omega)⟩
    | succ j =>
      obtain ⟨ys,ndy,ly,hy⟩ := ih j v gv.oddSource cv
      refine ⟨xs++ys,?_,by simp [quota,lx,ly],?_⟩
      · apply List.pairwise_append.mpr
        refine ⟨ndx,ndy,?_⟩
        intro x mx y my eq
        subst y
        exact ne ((hx x mx).endpoint.symm.trans (hy x my).endpoint)
      · intro x mem
        rcases List.mem_append.mp mem with inX | inY
        · exact extend (hx x inX) gu (by omega)
        · exact extend (hy x inY) gv (by omega)

private theorem octave_power {X x : Nat} (pos : 0<x) (small : x≤X) :
    ∃ d, X≤2^d*x ∧ 2^d*x<2*X := by
  classical
  have existsPower : ∃ d, X≤2^d*x := by
    refine ⟨X,?_⟩
    have h := Nat.lt_two_pow_self (n:=X)
    have g := Nat.le_mul_of_pos_right (2^X) pos
    omega
  obtain ⟨d,hd⟩ := existsPower
  induction d with
  | zero => exact ⟨0,hd,by simpa using (show x<2*X by omega)⟩
  | succ e ih =>
    by_cases early : X≤2^e*x
    · exact ih early
    · exact ⟨e+1,hd,by rw [Nat.pow_succ,Nat.mul_right_comm]; omega⟩

private theorem map_distinct {xs : List Nat} {f : Nat → Nat} (nd : xs.Nodup)
    (inj : ∀ x ∈ xs, ∀ y ∈ xs, f x=f y → x=y) : (xs.map f).Nodup := by
  induction xs with
  | nil => simp
  | cons x xs ih =>
    obtain ⟨absent,tail⟩ := List.nodup_cons.mp nd
    apply List.nodup_cons.mpr
    constructor
    · intro mem
      obtain ⟨y,my,equal⟩ := List.mem_map.mp mem
      have eq := inj y (by simp [my]) x (by simp) equal
      exact absent (eq ▸ my)
    · exact ih tail (fun i hi j hj => inj i (by simp [hi]) j (by simp [hj]))

/-- Distinct physical ancestors of the supplied target in the same octave.
The cardinality is a Pascal sum. The bound allows unequal shortcut clocks. -/
theorem octave_ancestors {k j q X : Nat} {c : Bool} (odd : q%2=1) (col : q%3=digit c)
    (room : 2^(4*k+2*j)*q ≤ 3^k*X) :
    ∃ zs : List Nat, zs.Nodup ∧ zs.length=quota k j ∧
      ∀ z ∈ zs, X≤z ∧ z<2*X ∧ ∃ t, run t z=q := by
  classical
  obtain ⟨xs,nd,len,lands⟩ := bank k j q odd col
  let d (x : Nat) := if h : ∃ e, X≤2^e*x ∧ 2^e*x<2*X then Classical.choose h else 0
  let lift (x : Nat) := 2^(d x)*x
  have octave (x : Nat) (hx : x∈xs) : X≤lift x ∧ lift x<2*X := by
    have h := lands x hx
    have small := Nat.le_of_mul_le_mul_left (Nat.le_trans h.height room) (Nat.pow_pos (by decide : 0<3))
    have ex := octave_power (x:=x) (by have := h.odd; omega) small
    simpa [lift,d,ex] using Classical.choose_spec ex
  refine ⟨xs.map lift,map_distinct nd ?_,by simp [len],?_⟩
  · intro x hx y hy eq
    have px := peel_unique (e:=d x) (k:=d x+d y) (lands x hx).odd (by omega)
    have py := peel_unique (e:=d y) (k:=d x+d y) (lands y hy).odd (by omega)
    change 2^(d x)*x=2^(d y)*y at eq
    rw [eq,py] at px
    exact (Prod.mk.inj px).2.symm
  · intro z hz
    obtain ⟨x,hx,rfl⟩ := List.mem_map.mp hz
    obtain ⟨s,_,hit⟩ := (lands x hx).clock
    exact ⟨(octave x hx).1,(octave x hx).2,d x+s,by rw [run_add]; exact (congrArg (run s) (halve (d x) x)).trans hit⟩

/-- Check one trajectory in chronological order, stopping at its first hit. -/
@[expose] def hitBy : Nat → Nat → Nat → Bool
  | 0, x, y => x==y
  | h+1, x, y => x==y || hitBy h (step x) y

private theorem hitBy_iff (H x y : Nat) : hitBy H x y=true ↔ ∃ t, t≤H ∧ run t x=y := by
  induction H generalizing x with
  | zero => simp [hitBy,run]
  | succ H ih =>
    rw [hitBy,Bool.or_eq_true,beq_iff_eq,ih]
    constructor
    · rintro (eq | ⟨t,ht,eq⟩)
      · exact ⟨0,by omega,eq⟩
      · exact ⟨t+1,by omega,eq⟩
    · rintro ⟨t,ht,eq⟩
      cases t with
      | zero => exact .inl eq
      | succ t => exact .inr ⟨t,by omega,eq⟩

/-- Executable list of octave sources missing the supplied gate by a deadline. -/
@[expose] def misses (X H y : Nat) : List Nat :=
  ((List.range X).map (fun i => X+i)).filter (fun z =>
    !(hitBy H z y))

private theorem hit_or_listed {X H y z : Nat} (low : X≤z) (high : z<2*X)
    (miss : ¬∃ t, t≤H ∧ run t z=y) : z∈misses X H y := by
  apply List.mem_filter.mpr
  constructor
  · exact List.mem_map.mpr ⟨z-X,List.mem_range.mpr (by omega),by omega⟩
  · cases h : hitBy H z y with
    | false => rfl
    | true => exact False.elim (miss ((hitBy_iff H z y).mp h))

private theorem shares_label {k j q X H y : Nat} {c : Bool} (odd : q%2=1)
    (col : q%3=digit c) (room : 2^(4*k+2*j)*q≤3^k*X)
    (few : (misses X H y).length<quota k j) : ReachesOne q ↔ ReachesOne y := by
  classical
  obtain ⟨zs,nd,len,lands⟩ := octave_ancestors odd col room
  have common : ∃ z ∈ zs, ∃ t, t≤H ∧ run t z=y := by
    apply Classical.byContradiction
    intro no
    have sub : zs ⊆ misses X H y := by
      intro z hz
      exact hit_or_listed (lands z hz).1 (lands z hz).2.1 (fun hit => no ⟨z,hz,hit⟩)
    have bound := nd.length_le_of_subset sub
    omega
  obtain ⟨z,hz,t,_,yt⟩ := common
  obtain ⟨s,qs⟩ := (lands z hz).2.2
  have hq := MinimumDescent.good_run s z
  have hy := MinimumDescent.good_run t z
  rw [qs] at hq
  rw [yt] at hy
  exact hq.trans hy.symm

/-- A sufficiently full octave at any single gate certifies convergence of
every eligible ordinary target fitting the height budget, including the gate. -/
theorem capture {k j q X H y : Nat} {c : Bool} (odd : q%2=1) (col : q%3=digit c)
    (room : 2^(4*k+2*j)*q≤3^k*X) (few : (misses X H y).length<quota k j) :
    ReachesOne q ∧ ReachesOne y := by
  have pos : 0<q := by omega
  have smaller := Nat.le_mul_of_pos_right (2^(4*k+2*j)) pos
  have oneRoom : 2^(4*k+2*j)*1≤3^k*X := by omega
  have gate := (shares_label (q:=1) (c:=false) (by decide) (by decide) oneRoom few).mp ⟨0,rfl⟩
  exact ⟨(shares_label odd col room few).mpr gate,gate⟩

private theorem quota_zero (k : Nat) : quota k 0=1 := by
  induction k with | zero => rfl | succ k ih => exact ih

private theorem quota_full (k j : Nat) (le : k≤j) : quota k j=2^k := by
  induction k generalizing j with
  | zero => rfl
  | succ k ih =>
    cases j with
    | zero => omega
    | succ j =>
      rw [quota,ih (j+1) (by omega),ih j (by omega),Nat.pow_succ]
      omega

private theorem except_last (k : Nat) : quota (k+1) k+1=2^(k+1) := by
  induction k with
  | zero => decide
  | succ k ih =>
    rw [quota,quota_full (k+1) (k+1) (by omega),Nat.pow_succ 2 (k+1)]
    omega

private theorem complementary (n : Nat) : ∀ i j, n=i+j+1 →
    quota n i+quota n j=2^n := by
  induction n with
  | zero => omega
  | succ n ih =>
    intro i j eq
    cases i with
    | zero =>
      have ej : j=n := by omega
      subst j
      rw [quota_zero]
      have := except_last n
      omega
    | succ i =>
      cases j with
      | zero =>
        have ei : i+1=n := by omega
        rw [ei,quota_zero,except_last]
      | succ j =>
        have left := ih i (j+1) (by omega)
        have right := ih (i+1) j (by omega)
        simp only [quota,Nat.pow_succ] at *
        omega

private theorem quota_mono (k j : Nat) : quota k j≤quota k (j+1) := by
  induction k generalizing j with
  | zero => simp [quota]
  | succ k ih =>
    cases j with
    | zero => simp [quota]
    | succ j =>
      exact Nat.add_le_add (ih (j+1)) (ih j)

/-- At least half the binary words fit the five-clock average budget. -/
theorem half_quota (k : Nat) : 2^k ≤ 2*quota k (k/2) := by
  by_cases z : k=0
  · subst k; decide
  have split : k=k/2+((k-1)/2)+1 := by omega
  have pair := complementary k (k/2) ((k-1)/2) split
  by_cases same : (k-1)/2=k/2
  · rw [same] at pair; omega
  · have le := quota_mono k ((k-1)/2)
    rw [show (k-1)/2+1=k/2 by omega] at le
    omega

/-- Lower end of the executable octave for target values through k+1. -/
@[expose] def window (k : Nat) : Nat := 2^(4*k+2*(k/2))*(k+1)/3^k+1

private theorem all_hit (all : Universal) (xs : List Nat) (pos : ∀ x∈xs, 0<x) :
    ∃ H, ∀ x∈xs, ∃ t, t≤H ∧ run t x=1 := by
  induction xs with
  | nil => exact ⟨0,by simp⟩
  | cons x xs ih =>
    obtain ⟨H,bound⟩ := ih (fun z hz => pos z (by simp [hz]))
    obtain ⟨s,hit⟩ := all x (pos x (by simp))
    refine ⟨H+s,?_⟩
    intro z hz
    rcases List.mem_cons.mp hz with rfl | tail
    · exact ⟨s,by omega,hit⟩
    · obtain ⟨t,ht,eq⟩ := bound z tail
      exact ⟨t,by omega,eq⟩

/-- Universal convergence is equivalent to almost all starts in these finite
octaves hitting one common, freely chosen gate by a finite deadline on an
unbounded sequence of stages. The gate and deadline may both vary by stage. -/
theorem universal_iff_window_capture : Universal ↔
    ∀ N, ∃ k H y, N≤k ∧ (misses (window k) H y).length<quota k (k/2) := by
  constructor
  · intro all N
    let X := window N
    let xs := (List.range X).map (fun i => X+i)
    have posX : 0<X := by simp [X,window]
    obtain ⟨H,hits⟩ := all_hit all xs (by
      intro z hz
      obtain ⟨i,_,rfl⟩ := List.mem_map.mp hz
      omega)
    have empty : misses X H 1=[] := by
      apply List.eq_nil_iff_forall_not_mem.mpr
      intro z hz
      obtain ⟨mem,absent⟩ := List.mem_filter.mp hz
      obtain ⟨t,ht,hit⟩ := hits z mem
      have found : hitBy H z 1=true := (hitBy_iff H z 1).mpr ⟨t,ht,hit⟩
      simp [found] at absent
    have positive := half_quota N
    have powpos := Nat.pow_pos (by decide : 0<2) (n:=N)
    exact ⟨N,H,1,Nat.le_refl _,by change (misses X H 1).length<_; rw [empty]; simp; omega⟩
  · intro windows
    apply Classical.byContradiction
    intro bad
    obtain ⟨q,c,odd,col,nonconvergent⟩ := odd_bad_unit bad
    obtain ⟨k,H,y,le,few⟩ := windows q
    have capacity := Nat.lt_mul_div_succ (2^(4*k+2*(k/2))*(k+1)) (Nat.pow_pos (by decide : 0<3) (n:=k))
    have room := Nat.le_trans (Nat.mul_le_mul_left (2^(4*k+2*(k/2))) (show q≤k+1 by omega)) (Nat.le_of_lt capacity)
    exact nonconvergent (capture odd col (X:=window k) room few).1

/-- Two ordinary starting values lie in the same forward component. -/
def Meet (x y : Nat) : Prop := ∃ i j, run i x=run j y

private theorem meet_trans {x y z : Nat} (h : Meet x y) (g : Meet y z) : Meet x z := by
  obtain ⟨i,j,eq⟩ := h
  obtain ⟨l,m,eq'⟩ := g
  exact ⟨i+l,m+j,by rw [run_add,eq,←run_add,Nat.add_comm j l,run_add l j,eq',←run_add]⟩

/-- Covering the octave by several arbitrary gates bounds the number of
distinct forward components among all targets that fit the height budget. -/
theorem component_packing {k j X : Nat} (roots gates holes : List Nat) (nd : roots.Nodup)
    (apart : ∀ x∈roots, ∀ z∈roots, x≠z → ¬Meet x z)
    (eligible : ∀ q∈roots, q%2=1 ∧ (∃ c, q%3=digit c) ∧ 2^(4*k+2*j)*q≤3^k*X)
    (few : holes.length<quota k j)
    (cover : ∀ z, X≤z → z<2*X → z∉holes → ∃ y∈gates, ∃ t, run t z=y) :
    roots.length≤gates.length := by
  classical
  have represented (q : Nat) (hq : q∈roots) : ∃ y∈gates, Meet q y := by
    obtain ⟨odd,⟨c,col⟩,room⟩ := eligible q hq
    obtain ⟨zs,distinct,size,land⟩ := octave_ancestors odd col room
    have available : ∃ z∈zs, z∉holes := by
      apply Classical.byContradiction
      intro no
      have sub : zs ⊆ holes := by
        intro z mem
        apply Classical.byContradiction
        exact fun absent => no ⟨z,mem,absent⟩
      have bound := distinct.length_le_of_subset sub
      omega
    obtain ⟨z,mem,usable⟩ := available
    obtain ⟨low,high,s,qs⟩ := land z mem
    obtain ⟨y,my,t,ys⟩ := cover z low high usable
    exact ⟨y,my,t,s,by rw [←qs,←ys,←run_add,←run_add,Nat.add_comm]⟩
  let dest (q : Nat) := if h : q∈roots then Classical.choose (represented q h) else 0
  have spec (q : Nat) (hq : q∈roots) : dest q∈gates ∧ Meet q (dest q) := by
    simpa [dest,hq] using Classical.choose_spec (represented q hq)
  have inj : (roots.map dest).Nodup := by
    apply map_distinct nd
    intro x hx z hz eq
    apply Classical.byContradiction
    intro ne
    obtain ⟨a,b,ez⟩ := (spec z hz).2
    rw [←eq] at ez
    exact apart x hx z hz ne (meet_trans (spec x hx).2 ⟨b,a,ez.symm⟩)
  have sub : roots.map dest ⊆ gates := by
    intro y mem
    obtain ⟨q,hq,rfl⟩ := List.mem_map.mp mem
    exact (spec q hq).1
  simpa using inj.length_le_of_subset sub

/-- One passing calculation handles ordinary even inputs and multiples of
three as well. The extra factor in the budget pays for entering the odd units. -/
theorem capture_positive_range {k j M X H y : Nat}
    (room : 2^(4*k+2*j)*((3*M+1)/2)≤3^k*X)
    (few : (misses X H y).length<quota k j) :
    ∀ n, 0<n → n≤M → ReachesOne n := by
  intro n pos hn
  obtain ⟨d,x,eq,odd⟩ := split_twos n pos
  obtain ⟨e,q,g⟩ := exists_gap odd
  obtain ⟨c,col⟩ := g.has_color
  have xsmall : x≤n := by rw [eq]; exact Nat.le_mul_of_pos_left x (Nat.pow_pos (by decide))
  have factor : 2≤2^e := Nat.pow_le_pow_right (by decide : 0<2) g.pos
  have bound := Nat.mul_le_mul_right q factor
  rw [g.eqn] at bound
  have small : q≤(3*M+1)/2 := by omega
  have fits := Nat.le_trans (Nat.mul_le_mul_left (2^(4*k+2*j)) small) room
  obtain ⟨t,hit⟩ := (capture g.oddTarget col fits few).1
  exact ⟨d+(e+t),by rw [eq,run_add,halve,run_add,g.follow,hit]⟩

/-- A finite example with one actual missed source and an unprescribed gate. -/
theorem one_hole_example : misses 107 75 4=[171] ∧ ReachesOne 5 := by
  have check : misses 107 75 4=[171] := by decide
  refine ⟨check,(capture (k:=1) (j:=1) (X:=107) (H:=75) (y:=4) (c:=true)
    (q:=5) (by decide) (by decide) (by decide) ?_).1⟩
  rw [check]; decide

#print axioms octave_ancestors
#print axioms capture
#print axioms half_quota
#print axioms universal_iff_window_capture
#print axioms component_packing
#print axioms capture_positive_range
#print axioms one_hole_example
end Collatz.Itinerary.WindowCapture
