import DirectedEleven
import NonunitExit
import UnitResidueExchange

namespace DirectedEleven

private def Source (f : Nat → Bool) (a b : Bool) :=
  { x : Nat // x%16=1 ∧ f x=a ∧ f (3*x)=b }

private theorem nextSource (f : Nat → Bool)
    (ev : ∀ n, f (2*n)=f n) (od : ∀ n, f (2*n+1)=f (3*n+2))
    (a b : Bool) (neq : a≠b)
    (none : ¬∃ y, y%32=11 ∧ f y=a ∧ f (3*y)=b)
    (s : Source f a b) :
    ∃ t : Source f a b, ∃ c : Char, Letter c ∧ relation c (s.val : ℤ) (t.val : ℤ) := by
  obtain ⟨x,hx,left,right⟩ := s
  rcases Nat.mod_lt x (by decide : 0<3) |> (fun h => show x%3=0 ∨ x%3=1 ∨ x%3=2 by omega) with hz|hz|hz
  · let u := x/3
    have xu : x=3*u := by dsimp [u]; omega
    have hu : u%2=1 := by omega
    have d : f (3*u)≠f (3*(3*u)) := by rw [←xu,left,right]; exact neq
    rcases NonunitExit.directed_successor f ev od u hu d with h|h
    · refine ⟨⟨16*u+1,by omega,?_,?_⟩,'4',Or.inr (Or.inl rfl),?_⟩
      · simpa [←xu,left] using h.1
      · simpa [←xu,right] using h.2.1
      · simp [relation]; omega
    · refine ⟨⟨32*u+1,by omega,?_,?_⟩,'5',Or.inr (Or.inr rfl),?_⟩
      · simpa [←xu,left] using h.1
      · simpa [←xu,right] using h.2.1
      · simp [relation]; omega
  · let u := x/48
    have xu : x=48*u+1 := by dsimp [u]; omega
    obtain ⟨lo,hi⟩ := UnitResidueExchange.unit_one_exchange f ev od u
    refine ⟨⟨64*u+1,by omega,?_,?_⟩,'2',Or.inl rfl,?_⟩
    · simpa [←xu,left] using lo
    · rw [show 3*(64*u+1)=192*u+3 by omega, hi, show 144*u+3=3*x by omega, right]
    · simp [relation]; omega
  · let u := x/48
    have xu : x=48*u+17 := by dsimp [u]; omega
    obtain ⟨lo,hi⟩ := UnitResidueExchange.residue17_descends f ev od u
    exfalso
    apply none
    refine ⟨32*u+11,by omega,?_,?_⟩
    · simpa [←xu,left] using lo
    · rw [show 3*(32*u+11)=96*u+33 by omega, hi, show 144*u+51=3*x by omega, right]

private def tape (d : Nat → Char) : Nat → Nat → List Char
  | 0,_ => []
  | n+1,i => d i :: tape d n (i+1)

private theorem tape_len (d : Nat → Char) (n i : Nat) : (tape d n i).length=n := by
  induction n generalizing i <;> simp_all [tape]

private theorem tape_legal (d : Nat → Char) (h : ∀ i, Letter (d i)) (n i : Nat) :
    ∀ c ∈ tape d n i, Letter c := by
  induction n generalizing i with
  | zero => simp [tape]
  | succ n ih => simpa [tape] using And.intro (h i) (ih (i+1))

private theorem tape_follows (d : Nat → Char) (z : Nat → ℤ)
    (h : ∀ i, relation (d i) (z i) (z (i+1))) (n i : Nat) :
    follows z (tape d n i) i := by
  induction n generalizing i <;> simp_all [follows,tape]

private theorem append_follows (z : Nat → ℤ) (l r : List Char) (i : Nat) :
    follows z (l++r) i ↔ follows z l i ∧ follows z r (i+l.length) := by
  induction l generalizing i with
  | nil => simp [follows]
  | cons c l ih => simp [follows,ih,and_assoc,Nat.add_comm,Nat.add_left_comm]

private theorem shift_follows (z : Nat → ℤ) (k i : Nat) (w : List Char) :
    follows (fun n => z (k+n)) w i ↔ follows z w (k+i) := by
  induction w generalizing i <;> simp_all [follows,Nat.add_assoc]

private theorem colorSelect {a b c : Bool} (ab : a≠b) (ca : c≠a) : c=b := by
  cases a <;> cases b <;> cases c <;> simp_all

/-- Every positive 1 mod 16 binary tripling disagreement has an ordinary
11 mod 32 representative carrying the same ordered pair of labels. -/
theorem localize (f : Nat → Bool)
    (ev : ∀ n, f (2*n)=f n) (od : ∀ n, f (2*n+1)=f (3*n+2))
    (x : Nat) (hx : x%16=1) (different : f x≠f (3*x)) :
    ∃ y, y%32=11 ∧ f y=f x ∧ f (3*y)=f (3*x) := by
  classical
  by_contra no
  let a := f x
  let b := f (3*x)
  let step := nextSource f ev od a b different no
  let ss : Nat → Source f a b := Nat.rec (motive := fun _ => Source f a b)
    ⟨x,hx,rfl,rfl⟩ (fun _ s => (step s).choose)
  let d (i : Nat) := (step (ss i)).choose_spec.choose
  let z (i : Nat) := ((ss i).val : ℤ)
  have leg (i : Nat) : Letter (d i) := (step (ss i)).choose_spec.choose_spec.1
  have phy (i : Nat) : relation (d i) (z i) (z (i+1)) :=
    (step (ss i)).choose_spec.choose_spec.2
  let w := tape d 10 0
  obtain ⟨m,hm,l,r,heq⟩ := hit_at_ten w (tape_len _ _ _) (tape_legal _ leg _ _)
  have full : follows z w 0 := tape_follows d z phy 10 0
  rw [heq,List.append_assoc,append_follows] at full
  have middle : follows z m.digits.toList l.length := by
    have p := (append_follows z m.digits.toList r (0+l.length)).mp full.2
    simpa using p.1
  have shifted := (shift_follows z l.length 0 m.digits.toList).mpr (by simpa using middle)
  have start16 := (ss l.length).property.1
  have base : z (l.length+0)=16*((ss l.length).val/16:Nat)+1 := by
    dsimp [z]; omega
  obtain ⟨v,hv⟩ := all_midpoints_located m hm (fun n => z (l.length+n)) _ base shifted
  have prop := (List.all_eq_true.mp proper_rows) m hm
  simp only [Bool.and_eq_true,decide_eq_true_eq] at prop
  have ha : (0:ℤ)<m.row.1 := by exact_mod_cast prop.1
  have hb : (m.row.2:ℤ)<m.row.1 := by exact_mod_cast prop.2
  have hn : 0 ≤ z (l.length+m.atIndex) := by dsimp [z]; positivity
  have hpos : 0 ≤ v := by
    by_contra! bad
    have zle := mul_nonpos_of_nonneg_of_nonpos ha.le (show v+1≤0 by omega)
    nlinarith
  have hv' : value m.row v.toNat = (ss (l.length+m.atIndex)).val := by
    apply Int.ofNat_inj.mp
    simp only [value,Nat.cast_add,Nat.cast_mul,Int.toNat_of_nonneg hpos]
    exact hv.symm
  have chk := (List.all_eq_true.mp all_routes_checked) m hm
  let P (n : Nat) := f n=a
  have lo : P (value m.row v.toNat) := by rw [hv']; exact (ss _).property.2.1
  have hi : ¬P (3*value m.row v.toNat) := by
    dsimp [P]; rw [hv',(ss _).property.2.2]; exact Ne.symm different
  obtain ⟨q,_,q11,qa,qb⟩ := checkedSound chk P (fun n => by simp [P,ev]) (fun n => by simp [P,od]) v.toNat lo hi
  apply no
  refine ⟨value q v.toNat,q11,qa,?_⟩
  change f (3*value q v.toNat)≠f x at qb
  exact colorSelect different qb

#print axioms localize
end DirectedEleven
