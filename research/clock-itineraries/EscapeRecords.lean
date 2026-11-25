module

public import EscapeFrontier
public import DescentClocks
import all ClockRecurrence
import all SparseClock
import all FixedGate
import all TernaryItinerary

public section
namespace Collatz.Itinerary.EscapeRecords

open FixedGate ClockRecurrence EscapeFrontier Sparse
set_option autoImplicit false

private theorem high_by_time {a : Nat} (no : ¬Repeats a) (n : Nat) :
    ∃ k, k≤n ∧ n≤after k a := by
  apply Classical.byContradiction
  intro neg
  have distinct : (List.range (n+1) |>.map (fun j => after j a)).Nodup := by
    apply List.Pairwise.map _ _ List.nodup_range
    intro i j ne eqn
    have ordered {p q : Nat} (lt : p<q) (same : after p a=after q a) : False := by
      exact no ⟨p,q-p,by omega,by rw [show p+(q-p)=q by omega,same]⟩
    by_cases lt : i<j
    · exact ordered lt eqn
    · exact ordered (by omega : j<i) eqn.symm
  have sub : (List.range (n+1) |>.map (fun j => after j a))⊆List.range n := by
    intro x mem
    obtain ⟨k,hk,rfl⟩ := List.mem_map.1 mem
    have lt := List.mem_range.1 hk
    apply List.mem_range.2
    by_cases large : n≤after k a
    · exact False.elim (neg ⟨k,by omega,large⟩)
    · omega
  have count := distinct.length_le_of_subset sub
  simp at count
  omega

/-- The uncorrected ratio 3^k/2^s is unbounded on every
nonrepeating positive odd unit orbit. -/
theorem unbounded_deficit {a : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    (no : ¬Repeats a) (M : Nat) : ∃ k, M*2^(elapsed k a)<3^k := by
  let W := (M*a)^6
  let n := W+3
  obtain ⟨k,early,high⟩ := high_by_time no n
  obtain ⟨rs,len,path,_,_⟩ := route_exists k a odd color
  have cap : (2^(elapsed k a)*after k a)^6≤(k+1)*(3^k*a)^6 := by
    by_cases ok : (2^(elapsed k a)*after k a)^6≤(k+1)*(3^k*a)^6
    · exact ok
    · apply False.elim
      apply no
      apply repeats_of_arrival
      apply CycleRows.reached_cycle_of_distortion path (by dsimp [n] at high; omega)
      rw [len]
      omega
  refine ⟨k,?_⟩
  by_cases le : 3^k≤M*2^(elapsed k a)
  · have bound := Nat.mul_le_mul_left (k+1) (Nat.pow_le_pow_left (Nat.mul_le_mul_right a le) 6)
    have bound' := Nat.le_trans cap bound
    have normalize : (k+1)*(M*2^(elapsed k a)*a)^6 =
        (2^(elapsed k a))^6*((k+1)*W) := by simp only [W,Nat.mul_pow]; ac_rfl
    rw [normalize,Nat.mul_pow] at bound'
    have small := Nat.le_of_mul_le_mul_left bound' (Nat.pow_pos (Nat.two_pow_pos _))
    have window := Nat.mul_le_mul_right W (Nat.succ_le_succ early)
    change (k+1)*W≤(n+1)*W at window
    have square := Nat.pow_le_pow_right (by dsimp [n]; omega : 0<n) (by decide : 2≤6)
    have powers := Nat.pow_le_pow_left high 6
    have strict : (n+1)*W<n^2 := by dsimp [n]; grind
    omega
  · omega

/-- A terminal record for the uncorrected multiplicative clock. -/
def Critical (a k : Nat) : Prop :=
  ∀ i, i<k → 2^(elapsed k a)*3^i<3^k*2^(elapsed i a)

private theorem least {P : Nat → Prop} {n : Nat} (yes : P n) :
    ∃ k, P k ∧ ∀ j, P j → k≤j := by
  induction n using Nat.strongRecOn with
  | ind n ih =>
    by_cases prior : ∃ j, j<n ∧ P j
    · obtain ⟨j,lt,h⟩ := prior
      exact ih j lt h
    · refine ⟨n,yes,?_⟩
      intro j hj
      by_cases lt : j<n
      · exact False.elim (prior ⟨j,lt,hj⟩)
      · omega

private theorem cofinal_of_unbounded {a : Nat} (deficit : ∀ M, ∃ k, M*2^(elapsed k a)<3^k)
    (L : Nat) : ∃ k, L<k ∧ Critical a k := by
  let M := 3^L
  let above := fun k => M*2^(elapsed k a)<3^k
  obtain ⟨w,hw⟩ := deficit M
  obtain ⟨k,yes,first⟩ := least (P:=above) hw
  have gain : M*2^(elapsed k a)<3^k := yes
  have left := Nat.mul_le_mul_left M (Nat.two_pow_pos (elapsed k a))
  simp only [Nat.mul_one] at left
  have lt : 3^L<3^k := Nat.lt_of_le_of_lt left gain
  refine ⟨k,(Nat.pow_lt_pow_iff_right (by decide : 1<3)).mp lt,?_⟩
  intro i hi
  have earlier : 3^i≤M*2^(elapsed i a) := by
    by_cases small : M*2^(elapsed i a)<3^i
    · have := first i small; omega
    · omega
  have h₁ := Nat.mul_le_mul_left (2^(elapsed k a)) earlier
  have h₂ := Nat.mul_lt_mul_of_pos_right gain (Nat.two_pow_pos (elapsed i a))
  apply Nat.lt_of_le_of_lt h₁
  simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using h₂

theorem cofinal_critical {a : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    (no : ¬Repeats a) (L : Nat) : ∃ k, L<k ∧ Critical a k :=
  cofinal_of_unbounded (unbounded_deficit odd color no) L

private theorem path_segment {a : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    {i k b : Nat} (split : i+b=k) : ∃ es, Path es (after i a) (after k a) ∧
      es.length=b ∧ elapsed k a=elapsed i a+es.sum := by
  obtain ⟨_,_,_,oi,d,ci⟩ := route_exists i a odd color
  obtain ⟨marks,len,r,_,_⟩ := route_exists b (after i a) oi ci
  obtain ⟨es,path,time,el⟩ := path_of_route r
  rw [←after_add,split] at path
  exact ⟨es,path,el.trans len,by rw [←split,elapsed_add,time]⟩

private theorem critical_segment {a k i b s : Nat} (recorded : Critical a k)
    (split : i+b=k) (temporal : elapsed k a=elapsed i a+s) (nonempty : 0<b) : 2^s<3^b := by
  have raw := recorded i (by omega)
  rw [temporal,←split,Nat.pow_add,Nat.pow_add] at raw
  have norm : (2^(elapsed i a)*3^i)*2^s < (2^(elapsed i a)*3^i)*3^b := by
    simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using raw
  exact Nat.lt_of_mul_lt_mul_left norm

/-- A critical record is a strict ordinary height record. -/
theorem critical_height {a k : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    (recorded : Critical a k) {i : Nat} (prior : i<k) : after i a<after k a := by
  obtain ⟨es,path,len,tm⟩ := path_segment odd color (show i+(k-i)=k by omega)
  have grow := critical_segment recorded (show i+(k-i)=k by omega) tm (by omega)
  have affine := Shadow.affine path
  rw [len] at affine
  obtain ⟨_,_,_,oi,_⟩ := route_exists i a odd color
  have low := Nat.mul_lt_mul_of_pos_right grow (by omega : 0<after i a)
  by_cases rev : after k a≤after i a
  · have := Nat.mul_le_mul_left (2^es.sum) rev; omega
  · omega

/-- Arbitrarily late uncorrected records characterize nonrepetition of
this integer orbit. Each record compares with all earlier odd indices. -/
theorem escape_iff_critical {a : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c) :
    ¬Repeats a ↔ ∀ L, ∃ k, L<k ∧ Critical a k := by
  refine ⟨cofinal_critical odd color,?_⟩
  rintro records ⟨i,p,pos,eqn⟩
  obtain ⟨k,late,recd⟩ := records (i+p)
  let j := k-(i+p)
  have split : i+p+j=k := by dsimp [j]; omega
  have same : after k a=after (i+j) a := by rw [←split,after_add,eqn,←after_add]
  have := critical_height odd color recd (i:=i+j) (by omega)
  omega

/-- A repeating integer orbit is exactly one whose uncorrected
clock ratio 3^k/2^s admits one uniform upper bound. -/
theorem repeats_iff_bounded_deficit {a : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c) :
    Repeats a ↔ ∃ M, ∀ k, 3^k≤M*2^(elapsed k a) := by
  constructor
  · intro rep
    apply Classical.byContradiction
    intro no
    have unbounded : ∀ M, ∃ k, M*2^(elapsed k a)<3^k := by
      intro M
      apply Classical.byContradiction
      intro cap
      apply no
      refine ⟨M,fun k => ?_⟩
      by_cases larger : M*2^(elapsed k a)<3^k
      · exact False.elim (cap ⟨k,larger⟩)
      · omega
    exact (escape_iff_critical odd color).mpr (cofinal_of_unbounded unbounded) rep
  · rintro ⟨M,cap⟩
    apply Classical.byContradiction
    intro no
    obtain ⟨k,h⟩ := unbounded_deficit odd color no M
    have := cap k
    omega

private theorem path_read {es : List Nat} {x q : Nat} (p : Path es x q) :
    after es.length x=q ∧ elapsed es.length x=es.sum := by
  induction p with
  | nil => exact ⟨rfl,rfl⟩
  | cons edge _ ih =>
    have eqn := gap_next edge
    simpa only [List.length_cons,List.sum_cons,after,elapsed,eqn] using
      And.intro ih.1 (congrArg (_+·) ih.2)

private theorem path_drop {es : List Nat} {x q : Nat} (p : Path es x q)
    (j : Nat) (small : j≤es.length) : Path (es.drop j) (after j x) q := by
  induction p generalizing j with
  | nil =>
    have : j=0 := by simpa using small
    subst j
    exact .nil _
  | cons edge sub ih =>
    cases j with
    | zero => exact .cons edge sub
    | succ j =>
      rw [after,gap_next edge]
      exact ih j (by simpa using small)

private theorem odd_at {y : Nat} (odd : y%2=1) (j : Nat) : after j y%2=1 := by
  induction j generalizing y with
  | zero => exact odd
  | succ j ih => exact ih (next_gap odd).oddTarget

private theorem unit_at_succ {y : Nat} (odd : y%2=1) (j : Nat) : after (j+1) y%3≠0 := by
  obtain ⟨c,eqn⟩ := next_color (odd_at odd j)
  rw [after_add j 1]
  change (next (after j y)).2%3≠0
  cases c <;> simp [digit] at eqn <;> omega

private theorem bounded_predecessors {y z b : Nat} (odd : y%2=1) (zodd : z%2=1)
    (unit : z%3≠0) (endAt : after b y=z) (below : ∀ j, j<b → after j y<z) :
    3*(b-1)<z := by
  let key := fun j => after (j+1) y/3
  have inject {i j : Nat} (lt : i<j) (last : j+1<b) (same : key i=key j) : False := by
    have oi := odd_at odd (i+1)
    have oj := odd_at odd (j+1)
    have ui := unit_at_succ odd i
    have uj := unit_at_succ odd j
    change after (i+1) y/3=after (j+1) y/3 at same
    have eqn : after (i+1) y=after (j+1) y := by omega
    let t := b-(j+1)
    have first : i+1+t<b := by dsimp [t]; omega
    have finish : j+1+t=b := by dsimp [t]; omega
    have join : after (i+1+t) y=z := by rw [after_add,eqn,←after_add,finish,endAt]
    have := below _ first
    omega
  have distinct : ((List.range (b-1)).map key).Nodup := by
    apply List.pairwise_map.2
    apply List.pairwise_lt_range.imp_of_mem
    intro i j _ hj lt same
    have last := List.mem_range.1 hj
    exact inject lt (by omega) same
  have sub : (List.range (b-1)).map key ⊆ List.range (z/3) := by
    intro t mem
    obtain ⟨j,hj,rfl⟩ := List.mem_map.1 mem
    have small := List.mem_range.1 hj
    have low := below (j+1) (by omega)
    have oj := odd_at odd (j+1)
    have uj := unit_at_succ odd j
    apply List.mem_range.2
    dsimp [key]
    omega
  have size := distinct.length_le_of_subset sub
  simp only [List.length_map,List.length_range] at size
  omega

/-- At a critical record, every positive odd ternary unit representative
of the terminal class must be large enough for an entire translated
ordinary path. This holds simultaneously at every suffix depth. -/
theorem representative_bound {a k : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    (recorded : Critical a k) {b z d : Nat} (depth : b≤k) (zodd : z%2=1)
    (unit : z%3≠0) (lift : after k a=z+2*(3^b*d)) : 3*(b-1)<z := by
  let i := k-b
  have split : i+b=k := by dsimp [i]; omega
  obtain ⟨es,p,len,_⟩ := path_segment odd color split
  have rep : after k a=z+2*(3^es.length*d) := by rw [len,lift]
  obtain ⟨y,_,yo,small,_⟩ := DescentClocks.lower_lift p zodd rep
  apply bounded_predecessors yo zodd unit (by rw [←len]; exact (path_read small).1)
  intro j before
  have le : j≤es.length := by omega
  let word := es.drop j
  have upper := path_drop p j le
  have lower := path_drop small j le
  have l : word.length=b-j := by simp [word,len]
  have start : after j (after i a)=after (i+j) a := (after_add i j a).symm
  have time := (path_read upper).2
  change elapsed word.length (after j (after i a))=word.sum at time
  rw [start,l] at time
  have pieces : i+j+(b-j)=k := by omega
  have total : elapsed k a=elapsed (i+j) a+word.sum := by rw [←pieces,elapsed_add,time]
  have grow := critical_segment recorded pieces total (by omega)
  have affine := Shadow.affine lower
  change 2^word.sum*z=3^word.length*after j y+Shadow.carry word at affine
  rw [l] at affine
  have strict := Nat.mul_lt_mul_of_pos_right grow (by omega : 0<z)
  by_cases rev : z≤after j y
  · have := Nat.mul_le_mul_left (3^(b-j)) rev; omega
  · omega

theorem avoids_fixed_representative {a k z : Nat} {c : Bool} (odd : a%2=1)
    (color : a%3=digit c) (recorded : Critical a k) (zodd : z%2=1) (unit : z%3≠0)
    (late : z+2≤k) (d : Nat) : after k a≠z+2*(3^(z+2)*d) := by
  intro same
  have := representative_bound odd color recorded late zodd unit same
  omega

#print axioms unbounded_deficit
#print axioms cofinal_critical
#print axioms critical_height
#print axioms escape_iff_critical
#print axioms repeats_iff_bounded_deficit
#print axioms representative_bound
#print axioms avoids_fixed_representative
end Collatz.Itinerary.EscapeRecords
