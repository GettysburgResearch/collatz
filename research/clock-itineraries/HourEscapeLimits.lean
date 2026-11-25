module

public import HourEscapeBranching
import all HourEscapeBranching
import all EscapeRecords
import all FixedGate

public section
namespace Collatz.Itinerary.HourEscape

open FixedGate EscapeRecords EscapeFrontier ClockRecurrence
set_option autoImplicit false

private def Cofinal (S : Nat → Prop) := ∀ T, ∃ i, T≤i ∧ S i

private theorem finite_choice {S : Nat → Prop} {f : Nat → Nat} {G : Nat}
    (cof : Cofinal S) (bounded : ∀ i, S i → f i<G) :
    ∃ g, Cofinal (fun i => S i ∧ f i=g) := by
  induction G generalizing S with
  | zero =>
    obtain ⟨i,_,hi⟩ := cof 0
    have := bounded i hi
    omega
  | succ G ih =>
    by_cases top : Cofinal (fun i => S i ∧ f i=G)
    · exact ⟨G,top⟩
    have below : Cofinal (fun i => S i ∧ f i<G) := by
      intro T
      apply Classical.byContradiction
      intro none
      apply top
      intro B
      obtain ⟨i,late,si⟩ := cof (max B T)
      have bound := bounded i si
      have lB : B≤i := Nat.le_trans (Nat.le_max_left ..) late
      have lT : T≤i := Nat.le_trans (Nat.le_max_right ..) late
      refine ⟨i,lB,si,?_⟩
      by_cases lt : f i<G
      · exact False.elim (none ⟨i,lT,si,lt⟩)
      · omega
    obtain ⟨g,cg⟩ := ih below (fun _ hi => hi.2)
    refine ⟨g,fun T => ?_⟩
    obtain ⟨i,late,⟨si,_⟩,eqn⟩ := cg T
    exact ⟨i,late,si,eqn⟩

private structure Cell where
  members : Nat → Prop
  cofinal : Cofinal members

private noncomputable def label (c : Cell) (f : Nat → Nat) {G : Nat}
    (bound : ∀ i, f i<G) : Nat :=
  Classical.choose (finite_choice c.cofinal (fun i _ => bound i))

private noncomputable def refineCell (c : Cell) (f : Nat → Nat) {G : Nat}
    (bound : ∀ i, f i<G) : Cell :=
  ⟨fun i => c.members i ∧ f i=label c f bound,
    Classical.choose_spec (finite_choice c.cofinal (fun i _ => bound i))⟩

private noncomputable def stage (w : Nat → Nat → Nat) {G : Nat}
    (bound : ∀ i j, w i j<G) : Nat → Cell
  | 0 => ⟨fun _ => True,fun T => ⟨T,Nat.le_refl _,trivial⟩⟩
  | n+1 => refineCell (stage w bound n) (w · n) (fun i => bound i n)

/-- A bounded-alphabet sequence of finite observations has a limit for which
each prescribed finite prefix occurs arbitrarily late. -/
private theorem trace_compact {G : Nat} (w : Nat → Nat → Nat)
    (bound : ∀ i j, w i j<G) :
    ∃ u : Nat → Nat, ∀ n T, ∃ i, T≤i ∧ ∀ j, j<n → w i j=u j := by
  let u := fun n => label (stage w bound n) (w · n) (fun i => bound i n)
  have agree (n i : Nat) (mem : (stage w bound n).members i) :
      ∀ j, j<n → w i j=u j := by
    induction n with
    | zero => omega
    | succ n ih =>
      change (stage w bound n).members i ∧ w i n=u n at mem
      intro j lt
      by_cases small : j<n
      · exact ih mem.1 j small
      · obtain rfl : j=n := by omega
        exact mem.2
  refine ⟨u,fun n T => ?_⟩
  obtain ⟨i,late,mem⟩ := (stage w bound n).cofinal T
  exact ⟨i,late,agree n i mem⟩

private theorem pair_compact {G : Nat} (l r : Nat → Nat → Nat)
    (lb : ∀ i j, l i j<G) (rb : ∀ i j, r i j<G) :
    ∃ u v : Nat → Nat, ∀ n T, ∃ i, T≤i ∧
      (∀ j, j<n → l i j=u j) ∧ (∀ j, j<n → r i j=v j) := by
  let w := fun i j => if j%2=0 then l i (j/2) else r i (j/2)
  have bound (i j : Nat) : w i j<G := by dsimp [w]; split <;> first | apply lb | apply rb
  obtain ⟨U,hU⟩ := trace_compact w bound
  refine ⟨fun j => U (2*j),fun j => U (2*j+1),fun n T => ?_⟩
  obtain ⟨i,late,agree⟩ := hU (2*n) T
  refine ⟨i,late,fun j hj => ?_,fun j hj => ?_⟩
  · simpa [w] using agree (2*j) (by omega)
  · have par : (2*j+1)%2≠0 := by omega
    have half : (2*j+1)/2=j := by omega
    simpa [w,par,half] using agree (2*j+1) (by omega)

/-- Every interval of J+1 odd-index sites contains an exact record. -/
def BoundedRecordGaps (a J : Nat) : Prop :=
  ∀ i, ∃ k, i≤k ∧ k≤i+J ∧ Critical a k

/-- Reverse exact gap words of arbitrarily late records from a single source
converge to this infinite script in the finite-prefix topology. -/
def RecordScript (a : Nat) (u : Nat → Nat) : Prop :=
  ∀ n R, ∃ k, n+R≤k ∧ Critical a k ∧ ∀ j, j<n → gapAt a (k-(j+1))=u j

def PeriodicAfter (D : Nat) (u : Nat → Nat) : Prop :=
  ∃ p, 0<p ∧ ∀ n, D≤n → u (n+p)=u n

private theorem bounded_alphabet {a J : Nat} (marks : BoundedRecordGaps a J) (i : Nat) :
    gapAt a i<3^(J+1) := by
  obtain ⟨k,lo,hi,mark⟩ := marks (i+1)
  let t := k-(i+1)
  have eqn : i+1+t=k := by dsimp [t]; omega
  have tm := elapsed_add (i+1) t a
  rw [eqn,snoc_clock] at tm
  have clocks : elapsed k a=elapsed i a+(gapAt a i+elapsed t (after (i+1) a)) := by
    simpa only [gapAt,Nat.add_assoc] using tm
  have localGain := critical_segment mark (show i+(t+1)=k by omega) clocks (by omega)
  have left := Nat.lt_two_pow_self (n:=gapAt a i+elapsed t (after (i+1) a))
  have right := Nat.pow_le_pow_right (by decide : 0<3) (show t+1≤J+1 by dsimp [t]; omega)
  omega

private theorem period_laps {u : Nat → Nat} {p D n : Nat}
    (period : ∀ n, D≤n → u (n+p)=u n) (start : D≤n) (t : Nat) :
    u (n+p*t)=u n := by
  induction t with
  | zero => simp
  | succ t ih => rw [Nat.mul_succ,←Nat.add_assoc,period _ (by omega),ih]

private theorem incompatible_periods {u v : Nat → Nat} {D l r : Nat} (hl : D<l) (hr : D<r)
    (past : ∀ n, u (l+n)=v (r+n)) (fork : u (l-1)≠v (r-1)) :
    ¬(PeriodicAfter D u ∧ PeriodicAfter D v) := by
  rintro ⟨⟨p,pp,pu⟩,⟨q,qp,pv⟩⟩
  have pos := Nat.mul_pos pp qp
  have lu := period_laps pu (n:=l-1) (by omega) q
  have rv := period_laps pv (n:=r-1) (by omega) p
  apply fork
  rw [←lu,←rv,Nat.mul_comm q p,show l-1+p*q=l+(p*q-1) by omega,
    show r-1+p*q=r+(p*q-1) by omega]
  exact past _

private theorem window_agree {f : Nat → Nat} {b i j h : Nat}
    (eqn : window f b i=window f b j) (lt : h<b) : f (i+h)=f (j+h) := by
  induction b generalizing i j h with
  | zero => omega
  | succ b ih =>
    change f i :: window f b (i+1)=f j :: window f b (j+1) at eqn
    obtain ⟨head,tail⟩ := List.cons.inj eqn
    cases h with
    | zero => simpa using head
    | succ h =>
      have hh := ih tail (show h<b by omega)
      simpa only [Nat.add_assoc,Nat.add_comm 1 h] using hh

private structure Fork (a b D J : Nat) where
  i : Nat
  j : Nat
  l : Nat
  r : Nat
  leftRange : D<l ∧ l≤D+1+J
  rightRange : D<r ∧ r≤D+1+J
  leftRecord : Critical a (i+b+l)
  rightRecord : Critical a (j+b+r)
  history : window (gapAt a) b i=window (gapAt a) b j
  branch : gapAt a (i+b)≠gapAt a (j+b)

private theorem fork_exists {a J : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    (escape : ¬Repeats a) (marks : BoundedRecordGaps a J) (b D : Nat) :
    Nonempty (Fork a b D J) := by
  obtain ⟨i,j,_,_,history,branch⟩ := right_special_windows odd color escape (I:=0)
    (fun n _ => bounded_alphabet marks n) b b
  obtain ⟨k,kl,kr,km⟩ := marks (i+b+(D+1))
  obtain ⟨s,sl,sr,sm⟩ := marks (j+b+(D+1))
  refine ⟨⟨i,j,k-(i+b),s-(j+b),⟨by omega,by omega⟩,⟨by omega,by omega⟩,
    ?_,?_,history,branch⟩⟩
  · rwa [show i+b+(k-(i+b))=k by omega]
  · rwa [show j+b+(s-(j+b))=s by omega]

private def observation (a k offset : Nat) : Nat → Nat
  | 0 => offset
  | n+1 => gapAt a (k-(n+1))

/-- On a fixed nonrepeating positive odd-unit ray with bounded exact-record
gaps, every proposed uniform preperiod bound fails for some limiting critical
script. Both sides of the branching comparison are genuine record subsequences
of this one ray; the theorem uses no rational classification or asymptotics. -/
theorem record_limit_unbounded_preperiod {a J : Nat} {c : Bool} (odd : a%2=1)
    (color : a%3=digit c) (escape : ¬Repeats a) (marks : BoundedRecordGaps a J)
    (D : Nat) : ∃ u, RecordScript a u ∧ ¬PeriodicAfter D u := by
  let z (b : Nat) := Classical.choice (fork_exists odd color escape marks b D)
  let left (b : Nat) := observation a ((z b).i+b+(z b).l) (z b).l
  let right (b : Nat) := observation a ((z b).j+b+(z b).r) (z b).r
  let G := 3^(J+1)+D+J+3
  have basePos := Nat.pow_pos (n:=J) (by decide : 0<3)
  have lb (b n : Nat) : left b n<G := by
    cases n with
    | zero =>
      apply Nat.lt_of_le_of_lt (z b).leftRange.2
      change D+1+J<3^(J+1)+D+J+3
      omega
    | succ n =>
      have hh := bounded_alphabet marks ((z b).i+b+(z b).l-(n+1))
      change gapAt a _<G
      dsimp [G]; omega
  have rb (b n : Nat) : right b n<G := by
    cases n with
    | zero =>
      apply Nat.lt_of_le_of_lt (z b).rightRange.2
      change D+1+J<3^(J+1)+D+J+3
      omega
    | succ n =>
      have hh := bounded_alphabet marks ((z b).j+b+(z b).r-(n+1))
      change gapAt a _<G
      dsimp [G]; omega
  obtain ⟨U,V,limit⟩ := pair_compact left right lb rb
  let u := fun n => U (n+1)
  let v := fun n => V (n+1)
  let l := U 0
  let r := V 0
  obtain ⟨b,_,headL,headR⟩ := limit 1 0
  have el : (z b).l=l := headL 0 (by decide)
  have er : (z b).r=r := headR 0 (by decide)
  have dl : D<l := el ▸ (z b).leftRange.1
  have dr : D<r := er ▸ (z b).rightRange.1
  have ru : RecordScript a u := by
    intro n R
    obtain ⟨t,late,A,_⟩ := limit (n+1) (n+R)
    exact ⟨(z t).i+t+(z t).l,by omega,(z t).leftRecord,fun j hj => A (j+1) (by omega)⟩
  have rv : RecordScript a v := by
    intro n R
    obtain ⟨t,late,_,B⟩ := limit (n+1) (n+R)
    exact ⟨(z t).j+t+(z t).r,by omega,(z t).rightRecord,fun j hj => B (j+1) (by omega)⟩
  have past (n : Nat) : u (l+n)=v (r+n) := by
    obtain ⟨t,late,A,B⟩ := limit (l+r+n+3) (n+1)
    have leq : (z t).l=l := A 0 (by omega)
    have req : (z t).r=r := B 0 (by omega)
    have L : gapAt a ((z t).i+t+(z t).l-(l+n+1))=u (l+n) := A (l+n+1) (by omega)
    have R : gapAt a ((z t).j+t+(z t).r-(r+n+1))=v (r+n) := B (r+n+1) (by omega)
    rw [←L,←R,show (z t).i+t+(z t).l-(l+n+1)=(z t).i+(t-(n+1)) by omega,
      show (z t).j+t+(z t).r-(r+n+1)=(z t).j+(t-(n+1)) by omega]
    exact window_agree (z t).history (by omega)
  have fork : u (l-1)≠v (r-1) := by
    obtain ⟨t,_,A,B⟩ := limit (l+r+3) 0
    have leq : (z t).l=l := A 0 (by omega)
    have req : (z t).r=r := B 0 (by omega)
    have L : gapAt a ((z t).i+t+(z t).l-(l-1+1))=u (l-1) := A (l-1+1) (by omega)
    have R : gapAt a ((z t).j+t+(z t).r-(r-1+1))=v (r-1) := B (r-1+1) (by omega)
    rw [←L,←R,show (z t).i+t+(z t).l-(l-1+1)=(z t).i+t by omega,
      show (z t).j+t+(z t).r-(r-1+1)=(z t).j+t by omega]
    exact (z t).branch
  have incompatible := incompatible_periods dl dr past fork
  by_cases h : PeriodicAfter D u
  · exact ⟨v,rv,fun hv => incompatible ⟨h,hv⟩⟩
  · exact ⟨u,ru,h⟩

#print axioms record_limit_unbounded_preperiod

end Collatz.Itinerary.HourEscape
