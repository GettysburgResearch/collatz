module

public import CycleRows

public section
namespace Collatz.Itinerary.CycleRows

set_option autoImplicit false

private theorem sorted_bound {us : List Nat} (increasing : us.Pairwise (·<·))
    (M : Nat) (lower : ∀ u ∈ us, M≤u) :
    M*(us.map (·+1)).prod ≤ (M+us.length)*us.prod := by
  induction us generalizing M with
  | nil => simp
  | cons u us ih =>
    obtain ⟨head,tail⟩ := List.pairwise_cons.mp increasing
    have hu := lower u (by simp)
    have recursiveBound := ih tail (u+1) (fun v hv => head v hv)
    have cmp := Nat.mul_le_mul_right (us.length+1) hu
    have cross : M*(u+1+us.length) ≤ (M+(us.length+1))*u := by
      rw [show M*(u+1+us.length)=M*u+M*(us.length+1) by grind,
        show (M+(us.length+1))*u=M*u+u*(us.length+1) by grind]
      omega
    simp only [List.map_cons,List.prod_cons,List.length_cons]
    calc
      M*((u+1)*(us.map (·+1)).prod) ≤ M*((u+1+us.length)*us.prod) := Nat.mul_le_mul_left _ recursiveBound
      _ = (M*(u+1+us.length))*us.prod := by ac_rfl
      _ ≤ ((M+(us.length+1))*u)*us.prod := Nat.mul_le_mul_right _ cross
      _ = _ := by ac_rfl

private theorem perm_prod {xs ys : List Nat} (p : xs.Perm ys) : xs.prod=ys.prod := by
  induction p with
  | nil => rfl
  | cons _ _ ih => simp only [List.prod_cons,ih]
  | swap => simp only [List.prod_cons]; ac_rfl
  | trans _ _ ih₁ ih₂ => exact ih₁.trans ih₂

private theorem distinct_bound {us : List Nat} (distinct : us.Nodup)
    (pos : ∀ u ∈ us, 0<u) : (us.map (·+1)).prod ≤ (us.length+1)*us.prod := by
  let cmp := fun (a b : Nat) => decide (a≤b)
  have perm := List.mergeSort_perm us cmp
  have sorted := List.pairwise_mergeSort (le:=cmp)
    (by simp [cmp]; omega) (by simp [cmp]; omega) us
  have weak : (us.mergeSort cmp).Pairwise (·≤·) := sorted.imp (by simp [cmp])
  have strict : (us.mergeSort cmp).Pairwise (·<·) :=
    weak.imp₂ (fun _ _ le ne => by omega) (perm.nodup_iff.mpr distinct)
  have h := sorted_bound strict 1 (fun a ha => pos a (perm.mem_iff.mp ha))
  simpa only [Nat.one_mul,Nat.add_comm 1,perm.length_eq,perm_prod perm,
    perm_prod (perm.map (fun u => u+1))] using h

/-- An ordinary route recording each positive half-index u=(x-1)/2 of its
odd inputs, in reverse order. The trivial cycle is excluded from these inputs. -/
private inductive Track : Nat → List Nat → Nat → Nat → Prop where
  | nil (q : Nat) : Track q [] 0 q
  | cons {q u e x s : Nat} {us : List Nat} {c : Bool} (hu : 0<u)
      (gap : Gap e (2*u+1) q) (mark : (2*u+1)%3=digit c)
      (rest : Track (2*u+1) us s x) : Track q (u::us) (e+s) x

private theorem collect {q s x : Nat} {rs : List Bool} (r : Route q rs s x)
    (above : 2<q) : ∃ us, Track q us s x ∧ us.length=rs.length := by
  induction r with
  | nil => exact ⟨[],.nil _,rfl⟩
  | @cons q y x e s c rs g mark _ ih =>
    have ho := g.oddSource
    have eq := g.eqn
    have big : 2≤2^e := Nat.pow_le_pow_right (by decide : 0<2) g.pos
    have h := Nat.mul_le_mul_right q big
    have hy : 2<y := by omega
    obtain ⟨us,trace,hlen⟩ := ih hy
    obtain ⟨u,hu,rfl⟩ : ∃ u, 0<u ∧ y=2*u+1 := ⟨y/2,by omega,by omega⟩
    exact ⟨u::us,.cons hu g mark trace,by simp [hlen]⟩

private theorem route_from_member {q s x u : Nat} {us : List Nat} (t : Track q us s x)
    (mem : u∈us) : ∃ (T : Nat) (rs : List Bool), 0<rs.length ∧ Route q rs T (2*u+1) := by
  induction t with
  | nil => simp at mem
  | @cons q v e x s vs c _ g mark _ ih =>
    rcases List.mem_cons.mp mem with rfl | later
    · exact ⟨_,[c],by simp,.cons g mark (.nil _)⟩
    · obtain ⟨T,rs,_,r⟩ := ih later
      exact ⟨_,c::rs,by simp,.cons g mark r⟩

private theorem Track.route {q s x : Nat} {us : List Nat} (t : Track q us s x) :
    ∃ marks, Route q marks s x := by
  induction t with
  | nil y => exact ⟨[],Route.nil y⟩
  | cons _ g mark _ ih =>
    obtain ⟨_,r⟩ := ih
    exact ⟨_,.cons g mark r⟩

/-- A lap is reached by the same input whose clocks are being tested. -/
@[expose] def ReachesNontrivialCycle (x : Nat) : Prop :=
  ∃ (t q s : Nat) (marks : List Bool),
    (∃ pre, Route q pre t x) ∧ 2<q ∧ 0<marks.length ∧ Route q marks s q

private theorem clean {q s x : Nat} {us : List Nat} (t : Track q us s x)
    (nocycle : ¬ReachesNontrivialCycle x) : us.Nodup ∧ ∀ u ∈ us, 0<u := by
  induction t with
  | nil => simp
  | @cons q v e x s us c hv g mark rest ih =>
    obtain ⟨nd,pos⟩ := ih nocycle
    have absent : v∉us := by
      intro mem
      obtain ⟨T,rs,hl,r⟩ := route_from_member rest mem
      exact nocycle ⟨s,2*v+1,T,rs,rest.route,by omega,hl,r⟩
    exact ⟨List.nodup_cons.mpr ⟨absent,nd⟩,by simpa using And.intro hv pos⟩

private theorem local_sixth {e u q : Nat} (g : Gap e (2*u+1) q) :
    u*(2^e*q)^6 ≤ (u+1)*(3*(2*u+1))^6 := by
  rw [g.eqn]
  have identity : (u+1)*(3*(2*u+1))^6 =
      u*(3*(2*u+1)+1)^6 + (3888*u^5+15120*u^4+22140*u^3+15624*u^2+5381*u+729) := by
    grind
  omega

private theorem distortion_core {q s x : Nat} {us : List Nat} (t : Track q us s x) :
    us.prod*(2^s*q)^6 ≤ (us.map (·+1)).prod*(3^us.length*x)^6 := by
  induction t with
  | nil => simp
  | @cons q u e x s us c hu g _ _ ih =>
    have stepBound := local_sixth g
    have mult := Nat.mul_le_mul stepBound ih
    have yPos : 0<(2*u+1)^6 := Nat.pow_pos (by omega)
    apply Nat.le_of_mul_le_mul_left (c:=(2*u+1)^6) _ yPos
    simp only [List.prod_cons,List.map_cons,List.length_cons,Nat.pow_add,Nat.pow_succ 3]
    simp only [Nat.mul_pow] at mult ⊢
    refine Nat.le_trans (Nat.le_of_eq ?_) (Nat.le_trans mult (Nat.le_of_eq ?_)) <;> ac_rfl

/-- On any route ending above two, a superlinear sixth-power distortion
certifies an actual nontrivial cycle somewhere on the recorded route. -/
theorem reached_cycle_of_distortion {q s x : Nat} {rs : List Bool} (r : Route q rs s x)
    (above : 2<q) (large : (rs.length+1)*(3^rs.length*x)^6 < (2^s*q)^6) :
    ReachesNontrivialCycle x := by
  apply Classical.byContradiction
  intro no
  obtain ⟨us,t,hl⟩ := collect r above
  obtain ⟨nd,pos⟩ := clean t no
  have cap := distinct_bound nd pos
  have core := distortion_core t
  have bound := Nat.le_trans core (Nat.mul_le_mul_right ((3^us.length*x)^6) cap)
  rw [show ((us.length+1)*us.prod)*(3^us.length*x)^6 =
      us.prod*((us.length+1)*(3^us.length*x)^6) by ac_rfl] at bound
  have final := Nat.le_of_mul_le_mul_left bound (List.prod_pos_iff_forall_pos_nat.mpr pos)
  rw [hl] at final
  omega

theorem cycle_of_distortion {q s x : Nat} {rs : List Bool} (r : Route q rs s x)
    (above : 2<q) (large : (rs.length+1)*(3^rs.length*x)^6 < (2^s*q)^6) : NontrivialCycle := by
  obtain ⟨_,y,T,marks,_,hy,hl,loop⟩ := reached_cycle_of_distortion r above large
  exact ⟨y,T,marks,hy,hl,loop⟩

theorem witness_implies_cycle {b : Nat} (h : Witness b) : NontrivialCycle := by
  obtain ⟨q,x,rs,above,hl,r,large⟩ := h
  exact cycle_of_distortion r above (by simpa only [hl] using large)

#print axioms cycle_of_distortion
#print axioms reached_cycle_of_distortion
#print axioms witness_implies_cycle
end Collatz.Itinerary.CycleRows
