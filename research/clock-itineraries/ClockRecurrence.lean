module

public import ClosureProposal
import all ClosureProposal
import all CycleAmplification
import all FixedGate
import all TernaryItinerary

public section
namespace Collatz.Itinerary.ClockRecurrence

open FixedGate Proposal
set_option autoImplicit false

/-- Some positive number of odd gaps returns to a previously visited
odd value on this very ordinary orbit. -/
@[expose] def Repeats (a : Nat) : Prop :=
  ∃ i p, 0<p ∧ after (i+p) a=after i a

private theorem enter {a k : Nat} (h : Repeats (after k a)) : Repeats a := by
  obtain ⟨i,p,hp,eqn⟩ := h
  refine ⟨k+i,p,hp,?_⟩
  rw [Nat.add_assoc,after_add,after_add k i,eqn]

private theorem tail {a : Nat} (h : Repeats a) (k : Nat) : Repeats (after k a) := by
  obtain ⟨i,p,hp,eqn⟩ := h
  have swap (j : Nat) : after j (after k a)=after k (after j a) := by
    rw [←after_add,←after_add,Nat.add_comm k j]
  exact ⟨i,p,hp,by rw [swap,swap,eqn]⟩

/-- The exponential gain of whole laps eventually absorbs the
arbitrary incoming preperiod as well as the polynomial clock factor. -/
private theorem amplification (i p A L : Nat) (hp : 0<p) (gain : 3^p<2^A) :
    ∃ r, L≤r*p+i ∧ (r*p+i+1)*(3^(r*p+i))^6 < (2^(r*A))^6 := by
  let v := 3^p
  let B := (3^i)^6
  let t := v*(p*B)+(i+1)*B+L+1
  let r := v*t
  have big := CycleAmplification.stretch (v:=v) (u:=2^A) (p:=p*B) (m:=(i+1)*B) (t:=t)
    (Nat.pow_pos (by decide : 0<3)) gain (by dsimp [t]; omega) (by dsimp [t]; omega)
    (by dsimp [t]; omega)
  change (r*(p*B)+(i+1)*B+1)*(v^r)^6<((2^A)^r)^6 at big
  have cap : (r*p+i+1)*B≤r*(p*B)+(i+1)*B+1 := by grind
  have bound := Nat.lt_of_le_of_lt (Nat.mul_le_mul_right ((v^r)^6) cap) big
  have vr : 3^(r*p)=v^r := by dsimp [v]; rw [Nat.mul_comm r p,Nat.pow_mul]
  have ur : 2^(r*A)=(2^A)^r := by rw [Nat.mul_comm r A,Nat.pow_mul]
  have ht : t≤r := by
    simpa [r] using Nat.mul_le_mul_right t (Nat.pow_pos (n:=p) (by decide : 0<3))
  have hr : r≤r*p := by simpa using Nat.mul_le_mul_left r hp
  refine ⟨r,by dsimp [t] at ht; omega,?_⟩
  rw [Nat.pow_add,vr,Nat.mul_pow,ur]
  change (r*p+i+1)*((v^r)^6*B)<((2^A)^r)^6
  rwa [show (r*p+i+1)*((v^r)^6*B)=(r*p+i+1)*B*(v^r)^6 by ac_rfl]

/-- The clock boundary is exceeded at arbitrarily late depths, including
when the repeated component is reached through a long preperiod. -/
theorem cofinal_of_repeats {a : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    (rep : Repeats a) (L : Nat) : ∃ k, L≤k ∧ (k+1)*(3^k)^6 < (2^(elapsed k a))^6 := by
  obtain ⟨i,p,hp,eqn⟩ := rep
  let q := after i a
  have ret : after p q=q := by simpa [q,after_add] using eqn
  obtain ⟨pre,hlen,front,qo,d,qc⟩ := route_exists i a odd color
  obtain ⟨ms,ml,loop,_,_⟩ := route_exists p q qo qc
  rw [ret] at loop
  have gain : 3^p<2^(elapsed p q) := by
    by_cases one : q=1
    · rw [one,Proposal.clock_one,Nat.pow_mul]
      exact Nat.pow_lt_pow_left (by decide) (by omega)
    · have above : 2<q := by change q%2=1 at qo; omega
      simpa only [ml] using (CycleAmplification.loop_rates loop above (by omega)).1
  obtain ⟨r,late,growth⟩ := amplification i p (elapsed p q) L hp gain
  obtain ⟨laps,ll,repeated⟩ := CycleAmplification.laps loop r
  have w := CycleAmplification.compose repeated front
  have clocks := (route_read w).2
  rw [List.length_append,ll,ml,hlen] at clocks
  refine ⟨r*p+i,late,?_⟩
  rw [clocks]
  exact Nat.lt_of_lt_of_le growth (Nat.pow_le_pow_left
    (Nat.pow_le_pow_right (by decide) (show r*elapsed p q ≤ r*elapsed p q+elapsed i a by omega)) 6)

theorem crosses_of_repeats {a : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    (rep : Repeats a) : Crosses a := by
  obtain ⟨k,_,clock⟩ := cofinal_of_repeats odd color rep 0
  exact ⟨k,clock⟩

private theorem repeats_of_arrival {a : Nat} (arrived : CycleRows.ReachesNontrivialCycle a) :
    Repeats a := by
  obtain ⟨_,q,_,ms,⟨pre,front⟩,_,nonempty,loop⟩ := arrived
  exact ⟨pre.length,ms.length,nonempty,by rw [after_add,(route_read front).1,(route_read loop).1]⟩

private theorem repeats_of_tails {a : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    (h : ∀ i, Crosses (after i a)) : Repeats a := by
  induction a using Nat.strongRecOn generalizing c with
  | ind a ih =>
    by_cases one : a=1
    · subst a; exact ⟨0,1,by decide,rfl⟩
    obtain ⟨k,clock⟩ := h 0
    rcases crossing_descent_or_cycle (by omega : 2<a) odd color clock with lower | arrived
    · obtain ⟨_,_,_,qo,d,qc⟩ := route_exists k a odd color
      apply enter (k:=k)
      apply ih (after k a) lower qo qc
      intro j
      simpa [after_add] using h (k+j)
    · exact repeats_of_arrival arrived

/-- The crossing condition holds on all tails of a specified ordinary
unit if and only if its actual odd orbit eventually repeats. -/
theorem repeats_iff_every_tail_crosses {a : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c) :
    Repeats a ↔ ∀ i, Crosses (after i a) := by
  constructor
  · intro rep i
    obtain ⟨_,_,_,qo,d,qc⟩ := route_exists i a odd color
    exact crosses_of_repeats qo qc (tail rep i)
  · exact repeats_of_tails odd color

private theorem eventually_above {a : Nat} (no : ¬Repeats a) (A : Nat) :
    ∃ K, ∀ j, K≤j → A≤after j a := by
  induction A with
  | zero => exact ⟨0,by intros; omega⟩
  | succ A ih =>
    obtain ⟨K,prior⟩ := ih
    by_cases visit : ∃ i, after i a=A
    · obtain ⟨i,hi⟩ := visit
      refine ⟨K+i+1,?_⟩
      intro j hj
      have low := prior j (by omega)
      by_cases same : after j a=A
      · apply False.elim
        apply no
        exact ⟨i,j-i,by omega,by rw [show i+(j-i)=j by omega,same,hi]⟩
      · omega
    · refine ⟨K,?_⟩
      intro j hj
      have low := prior j hj
      have ne : after j a≠A := fun eqn => visit ⟨j,eqn⟩
      omega

/-- A single observer at the original gate suffices when the test
crosses its boundary at arbitrarily late depths. -/
theorem repeats_iff_cofinal {a : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c) :
    Repeats a ↔ ∀ L, ∃ k, L≤k ∧ (k+1)*(3^k)^6 < (2^(elapsed k a))^6 := by
  constructor
  · exact cofinal_of_repeats odd color
  · intro often
    apply Classical.byContradiction
    intro no
    by_cases one : a=1
    · subst a; exact no ⟨0,1,by decide,rfl⟩
    obtain ⟨K,high⟩ := eventually_above no a
    obtain ⟨k,late,clock⟩ := often K
    rcases crossing_descent_or_cycle (by omega : 2<a) odd color clock with smaller | arrived
    · have := high k late; omega
    · exact no (repeats_of_arrival arrived)

theorem no_repeat_iff_trapped_tail {a : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c) :
    ¬Repeats a ↔ ∃ i, ∀ k, (2^(elapsed k (after i a)))^6 ≤ (k+1)*(3^k)^6 := by
  rw [repeats_iff_every_tail_crosses odd color]
  simp only [Classical.not_forall, Crosses, not_exists, Nat.not_lt]

/-- Check a proposed finite list of crossing depths for one gate.
Repeated depths do not count towards the threshold. -/
@[expose] def certificate (a : Nat) (ks : List Nat) : Bool :=
  decide (ks.Nodup ∧ a/2<ks.length) &&
    ks.all (fun k => decide ((k+1)*(3^k)^6 < (2^(elapsed k a))^6))

private theorem certificate_iff (a : Nat) (ks : List Nat) : certificate a ks=true ↔
    ks.Nodup ∧ a/2<ks.length ∧ ∀ k ∈ ks, (k+1)*(3^k)^6 < (2^(elapsed k a))^6 := by
  simp [certificate,List.all_eq_true,and_assoc]

/-- More than floor(a/2) distinct crossing depths already certify that
the odd orbit repeats. Every repeating orbit has such a certificate. -/
theorem repeats_iff_certificate {a : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c) :
    Repeats a ↔ ∃ ks, certificate a ks=true := by
  constructor
  · intro rep
    have many (m : Nat) : ∃ (ks : List Nat) (L : Nat), ks.length=m ∧ ks.Nodup ∧
        ∀ k ∈ ks, k<L ∧ (k+1)*(3^k)^6 < (2^(elapsed k a))^6 := by
      induction m with
      | zero => exact ⟨[],0,rfl,by simp,by simp⟩
      | succ m ih =>
        obtain ⟨ks,L,len,nd,all⟩ := ih
        obtain ⟨k,late,win⟩ := cofinal_of_repeats odd color rep L
        have fresh : k∉ks := fun hk => (by have := (all k hk).1; omega)
        refine ⟨k::ks,k+1,by simp [len],List.nodup_cons.2 ⟨fresh,nd⟩,?_⟩
        intro j hj
        rcases List.mem_cons.1 hj with rfl | old
        · exact ⟨by omega,win⟩
        · exact ⟨by have := (all j old).1; omega,(all j old).2⟩
    obtain ⟨ks,_,len,nd,all⟩ := many (a/2+1)
    exact ⟨ks,(certificate_iff a ks).2 ⟨nd,by omega,fun k hk => (all k hk).2⟩⟩
  · rintro ⟨ks,cert⟩
    apply Classical.byContradiction
    intro no
    by_cases one : a=1
    · subst a; exact no ⟨0,1,by decide,rfl⟩
    obtain ⟨nd,large,clocks⟩ := (certificate_iff a ks).1 cert
    have atOdd (i : Nat) : after i a%2=1 := by
      obtain ⟨_,_,_,o,_⟩ := route_exists i a odd color
      exact o
    let index := fun i => after i a/2
    have ordered {i j : Nat} (lt : i<j) (eqn : index i=index j) : False := by
      have si := atOdd i
      have sj := atOdd j
      change after i a/2=after j a/2 at eqn
      exact no ⟨i,j-i,by omega,by rw [show i+(j-i)=j by omega]; omega⟩
    have mapped : (ks.map index).Nodup := List.Pairwise.map index (fun i j ne eqn => by
      by_cases lt : i<j
      · exact ordered lt eqn
      · exact ordered (by omega : j<i) eqn.symm) nd
    have sub : ks.map index ⊆ List.range (a/2) := by
      intro x mem
      obtain ⟨k,hk,rfl⟩ := List.mem_map.1 mem
      rcases crossing_descent_or_cycle (by omega : 2<a) odd color (clocks k hk) with smaller | arrived
      · apply List.mem_range.2
        change after k a/2<a/2
        have := atOdd k
        omega
      · exact False.elim (no (repeats_of_arrival arrived))
    have count := mapped.length_le_of_subset sub
    simp only [List.length_map,List.length_range] at count
    omega

#print axioms cofinal_of_repeats
#print axioms crosses_of_repeats
#print axioms repeats_iff_every_tail_crosses
#print axioms repeats_iff_cofinal
#print axioms no_repeat_iff_trapped_tail
#print axioms repeats_iff_certificate
end Collatz.Itinerary.ClockRecurrence
