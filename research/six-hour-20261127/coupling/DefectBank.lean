import GlobalReturnBudget

/-! An independently checkable relative-height refinement of PR197's
ordered-defect exchanges, with optional binary or ternary specialization. -/
set_option autoImplicit false
set_option warningAsError true
set_option maxHeartbeats 1000000
open private CollatzQuantitativeReturn.D CollatzQuantitativeReturn.f
  CollatzQuantitativeReturn.ev CollatzQuantitativeReturn.od
  CollatzQuantitativeReturn.oneD CollatzQuantitativeReturn.twoD
  CollatzQuantitativeReturn.asDef from QuantitativeReturn
namespace DefectBank
open CollatzReverseBasin CollatzTwoOdd
open CollatzQuantitativeReturn (D f ev od oneD twoD asDef)
abbrev Row := DirectedEleven.Row
abbrev V := DirectedEleven.value

def sub (r : Row) (m i : ℕ) : Row := (r.1*m,r.1*i+r.2)
def one (r : Row) : Row := (64*(r.1/48),64*(r.2/48)+1)
def two (k : ℕ) (r : Row) : Row := (k*(r.1/3),k*(r.2/3)+1)

inductive Plan where
  | split2 (a b : Plan)
  | split3 (a b c : Plan)
  | unit (a : Plan)
  | nonunit (a b : Plan)
  | use (i : ℕ) (word : String)

def checkedUse (K : ℕ) (orig : Row) (hs : List Row) (i : ℕ) (word : String) : Bool :=
  let s := hs[i]!
  decide (i<hs.length) &&
    if word="" then decide (s.1%48=0 ∧ s.2%48=17 ∧ s.1≤K*orig.1 ∧ s.2≤K*orig.2)
    else DirectedEleven.checked ⟨"",0,s,word⟩ &&
      (DirectedEleven.queries word.toList s).all
        (fun q => decide (3*q.1≤2*K*orig.1 ∧ 3*q.2+1≤2*K*orig.2))

def check (K : ℕ) : Plan → Row → Row → List Row → Bool
  | .split2 a b,o,r,hs =>
    check K a (sub o 2 0) (sub r 2 0) (hs.map (sub · 2 0)) &&
    check K b (sub o 2 1) (sub r 2 1) (hs.map (sub · 2 1))
  | .split3 a b c,o,r,hs =>
    check K a (sub o 3 0) (sub r 3 0) (hs.map (sub · 3 0)) &&
    check K b (sub o 3 1) (sub r 3 1) (hs.map (sub · 3 1)) &&
    check K c (sub o 3 2) (sub r 3 2) (hs.map (sub · 3 2))
  | .unit a,o,r,hs =>
    decide (r.1%48=0 ∧ r.2%48=1) && check K a o (one r) (r::hs)
  | .nonunit a b,o,r,hs =>
    decide (r.1%6=0 ∧ r.2%6=3) && check K a o (two 16 r) (r::hs) &&
      check K b o (two 32 r) (r::hs)
  | .use i word,o,r,hs => checkedUse K o (r::hs) i word

def Answer (K n : ℕ) := ∃ y, ReverseDefect y ∧ y≤K*n

private theorem subValue (r : Row) (m i t : ℕ) : V (sub r m i) t=V r (m*t+i) := by
  simp only [sub,V,DirectedEleven.value]; ring

private theorem direct {K : ℕ} {o r : Row} (t : ℕ) (bad : D (V r t))
    (ok : r.1%48=0 ∧ r.2%48=17 ∧ r.1≤K*o.1 ∧ r.2≤K*o.2) : Answer K (V o t) := by
  rcases ok with ⟨a,b,c,d⟩
  have modW : V r t%48=17 := by
    unfold V DirectedEleven.value
    rw [Nat.add_mod,Nat.mul_mod,a,b]; simp
  refine ⟨_,asDef bad modW,?_⟩
  have le:=Nat.add_le_add (Nat.mul_le_mul_right t c) d
  simpa only [V,DirectedEleven.value,Nat.mul_add,mul_assoc] using le

private theorem eleven {K : ℕ} {o r : Row} (t : ℕ)
    (modW : V r t%32=11) (bad : D (V r t))
    (a : 3*r.1≤2*K*o.1) (b : 3*r.2+1≤2*K*o.2) : Answer K (V o t) := by
  let q := V r t
  let u := q/32
  have eq : q=32*u+11 := by dsimp only [u]; change q%32=11 at modW; omega
  have h:=UnitResidueExchange.residue17_descends f ev od u
  change D q at bad
  rw [eq] at bad
  have canon : D (48*u+17) := by
    refine ⟨h.1.symm.trans bad.1,?_⟩
    simpa only [show 3*(48*u+17)=144*u+51 by omega,←h.2,
      show 96*u+33=3*(32*u+11) by omega] using bad.2
  have bound:=Nat.add_le_add (Nat.mul_le_mul_right t a) b
  have lim : 3*q+1≤2*(K*V o t) := by
    dsimp only [q,V,DirectedEleven.value]
    simpa only [Nat.mul_add,mul_assoc,add_assoc] using bound
  exact ⟨_,asDef canon (by omega),by omega⟩

private theorem use_sound {K : ℕ} {o : Row} {hs : List Row} {i : ℕ} {word : String}
    (ok : checkedUse K o hs i word=true) (t : ℕ) (hist : ∀ q∈hs,D (V q t)) :
    Answer K (V o t) := by
  simp only [checkedUse,Bool.and_eq_true,decide_eq_true_eq] at ok
  have member : hs[i]!∈hs := by rw [getElem!_pos hs i ok.1]; exact List.getElem_mem ..
  have bad := hist _ member
  by_cases empty : word=""
  · simp only [empty,ite_true] at ok
    exact direct t bad (of_decide_eq_true ok.2)
  · simp only [empty,ite_false] at ok
    have good:=ok.2
    simp only [Bool.and_eq_true] at good
    have fd : ¬f (3*V hs[i]! t)=false := by rw [bad.2]; decide
    obtain ⟨q,qm,qc,bl,bu⟩:=DirectedEleven.checkedSound good.1 (fun y => f y=false)
      (fun y => by simp [ev]) (fun y => by simp [od]) t bad.1 fd
    have budget:=of_decide_eq_true (List.all_eq_true.mp good.2 q qm)
    rcases budget with ⟨a,b⟩
    exact eleven t qc ⟨bl,by cases e : f (3*V q t) <;> simp_all⟩ a b

private def Meaning (K : ℕ) (o r : Row) (hs : List Row) := ∀ t,
  D (V r t) → (∀ q∈hs,D (V q t)) → Answer K (V o t)

private theorem split_sound {K m : ℕ} (positive : 0<m) {o r : Row} {hs : List Row}
    (child : ∀ i<m, Meaning K (sub o m i) (sub r m i) (hs.map (sub · m i))) : Meaning K o r hs := by
  intro t bad hist
  have eq : m*(t/m)+t%m=t := by rw [Nat.add_comm,Nat.mod_add_div]
  have h:=child (t%m) (Nat.mod_lt t positive) (t/m)
  rw [subValue,subValue,eq] at h
  apply h bad
  intro q has
  obtain ⟨y,ym,rfl⟩:=List.mem_map.mp has
  simpa only [subValue,eq] using hist y ym

theorem sound (K : ℕ) (plan : Plan) (o r : Row) (hs : List Row)
    (ok : check K plan o r hs=true) : ∀ t, D (V r t) → (∀ q∈hs,D (V q t)) → Answer K (V o t) := by
  change Meaning K o r hs
  induction plan generalizing o r hs with
  | split2 a b ia ib =>
    simp only [check,Bool.and_eq_true] at ok
    apply split_sound (m:=2) (by decide)
    intro i hi
    rcases (show i=0 ∨ i=1 by omega) with h|h <;> subst i
    · exact ia _ _ _ ok.1
    · exact ib _ _ _ ok.2
  | split3 a b c ia ib ic =>
    simp only [check,Bool.and_eq_true] at ok
    apply split_sound (m:=3) (by decide)
    intro i hi
    rcases (show i=0 ∨ i=1 ∨ i=2 by omega) with h|h|h <;> subst i
    · exact ia _ _ _ ok.1.1
    · exact ib _ _ _ ok.1.2
    · exact ic _ _ _ ok.2
  | unit more ih =>
    simp only [check,Bool.and_eq_true,decide_eq_true_eq] at ok
    intro t bad hist
    have a:=ok.1.1
    have b:=ok.1.2
    let u := r.1/48*t+r.2/48
    have original : V r t=48*u+1 := by
      have x : r.1=48*(r.1/48) := by omega
      have y : r.2=48*(r.2/48)+1 := by omega
      dsimp only [V,DirectedEleven.value,u]; rw [Nat.mul_add,←mul_assoc,←x]; omega
    have next : V (one r) t=64*u+1 := by simp only [V,DirectedEleven.value,one,u]; ring
    apply ih _ _ _ ok.2 t
    · rw [next]; exact oneD u (original ▸ bad)
    · simpa only [List.mem_cons,forall_eq_or_imp] using And.intro bad hist
  | nonunit a b ia ib =>
    simp only [check,Bool.and_eq_true,decide_eq_true_eq] at ok
    intro t bad hist
    have sa:=ok.1.1.1
    have sb:=ok.1.1.2
    let u:=r.1/3*t+r.2/3
    have orig : V r t=3*u := by
      have x : r.1=3*(r.1/3) := by omega
      have y : r.2=3*(r.2/3) := by omega
      dsimp only [V,DirectedEleven.value,u]; rw [Nat.mul_add,←mul_assoc,←x,←y]
    have odd : u%2=1 := by
      have x : r.1/3%2=0 := by omega
      have y : r.2/3%2=1 := by omega
      dsimp only [u]; rw [Nat.add_mod,Nat.mul_mod,x,y]; simp
    have form (k : ℕ) : V (two k r) t=k*u+1 := by simp only [V,DirectedEleven.value,two,u]; ring
    have keep : ∀ q∈r::hs,D (V q t) := by simpa only [List.mem_cons,forall_eq_or_imp] using And.intro bad hist
    rcases twoD u odd (orig ▸ bad) with l|u'
    · exact ia _ _ _ ok.1.2 t (form 16 ▸ l) keep
    · exact ib _ _ _ ok.2 t (form 32 ▸ u') keep
  | use i word =>
    intro t bad hist
    apply use_sound ok t
    simpa only [List.mem_cons,forall_eq_or_imp] using And.intro bad hist

theorem localize (K : ℕ) (plan : Plan) (ok : check K plan (16,1) (16,1) []=true)
    (x : ℕ) (res : x%16=1) (bad : ¬Basin x) (good : Basin (3*x)) : Answer K x := by
  have label : D x := by
    simp only [D,f,decide_eq_false_iff_not,decide_eq_true_eq]; exact ⟨bad,good⟩
  have eq : V (16,1) (x/16)=x := by dsimp [V,DirectedEleven.value]; omega
  have h:=sound K plan _ _ _ ok (x/16)
  rw [eq] at h
  exact h label (by simp)

#print axioms sound
#print axioms localize
end DefectBank
