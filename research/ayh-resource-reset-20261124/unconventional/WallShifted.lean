import WallEscape

namespace WallShifted
open WallGeneral WallRational WallAffine WallOrbit WallUniform WallDensity WallRefinement WordRank

private theorem compatible (L W s₁ s₂ : Nat) (d a b : Int) (pos : 0<L) (odd : d%2=1)
    (l : PositiveCycle d a) (r : PositiveCycle d b)
    (density : lapGrade l*r.period=lapGrade r*l.period) :
    ∃ B, ∀ (t : Nat) (q : Int) (F G : Nat→Nat), q%2=1 →
      (∀ k, d*(F k:Int)=2^(L*k+(2*L*l.period*r.period*t+W)+s₁)*q+a) →
      (∀ k, d*(G k:Int)=2^(L*k+(2*L*l.period*r.period*t+W)+s₂)*q+b) →
      ∃ k≤B, ∃ i j, run i (F k)=run j (G k) := by
  let K := l.entry+r.entry
  let H := L*K+W
  have kh : K≤H := by
    have le : K≤L*K := by simpa using Nat.mul_le_mul_right K pos
    dsimp [H];omega
  have lt : l.entry≤L*K+(W+s₁) := by dsimp [H,K] at kh;dsimp [K];omega
  have rt : r.entry≤L*K+(W+s₂) := by dsimp [H,K] at kh;dsimp [K];omega
  let g := lapGrade l*r.period*L
  have gp : 0<g := Nat.mul_pos (Nat.mul_pos l.positive (time_pos r)) pos
  obtain ⟨T,meet⟩ := paired_bound (grade d (L*K+(W+s₁)) a) (grade d (L*K+(W+s₂)) b) g gp
    d (runD d (L*K+(W+s₁)) a) (runD d (L*K+(W+s₂)) b) odd
  let k := fun i => K+l.period*2*r.period*i
  refine ⟨k T,?_⟩
  intro t q F G qo fl gl
  let v := 2*L*l.period*r.period*t+W
  let X := fun i => run (L*k i+v+s₁) (F (k i))
  let Y := fun i => run (L*k i+v+s₂) (G (k i))
  let unit : Int := 9^(g*t)*q
  have uo : unit%2=1 := by dsimp [unit];rw [Int.mul_emod,odd_power 9 (by decide),qo];decide
  have left (i : Nat) : d*(X i:Int)=3^(grade d (L*K+(W+s₁)) a)*unit*9^(g*i)+runD d (L*K+(W+s₁)) a := by
    have eq (k : Nat) : L*k+(2*L*l.period*r.period*t+(W+s₁))=L*k+v+s₁ := by dsimp [v];ring
    have row := chart_from_residue d a q L K (W+s₁) t i r.period F odd l lt
      (fun k => by rw [eq];exact fl k)
    dsimp only at row
    rw [eq] at row
    exact row
  have right (i : Nat) : d*(Y i:Int)=3^(grade d (L*K+(W+s₂)) b)*unit*9^(g*i)+runD d (L*K+(W+s₂)) b := by
    have eq (k : Nat) : L*k+(2*L*r.period*l.period*t+(W+s₂))=L*k+v+s₂ := by dsimp [v];ring
    have row := chart_from_residue d b q L K (W+s₂) t i l.period G odd r rt
      (fun k => by rw [eq];exact gl k)
    dsimp only at row
    rw [eq,show K+r.period*2*l.period*i=k i by dsimp [k];ring,←density] at row
    exact row
  obtain ⟨i,bn,h₁,h₂,e⟩ := meet unit (fun i => (X i:Int)) (fun i => (Y i:Int)) uo left right
  rw [signed_nat,signed_nat] at e
  refine ⟨k i,by dsimp [k];exact Nat.add_le_add_left (Nat.mul_le_mul_left _ (by omega)) _,
          L*k i+v+s₁+h₁,L*k i+v+s₂+h₂,?_⟩
  rw [runAdd (L*k i+v+s₁),runAdd (L*k i+v+s₂)]
  exact_mod_cast e

/-- Equal cycle densities at two different within-word phases also synchronize
by a bounded block depth uniformly in the unbounded original valuation. -/
theorem sampled (L s₁ s₂ : Nat) (d a b : Int) (pos : 0<L) (odd : d%2=1)
    (l : PositiveCycle d a) (r : PositiveCycle d b)
    (density : lapGrade l*r.period=lapGrade r*l.period) :
    ∃ B, ∀ (v : Nat) (q : Int) (F G : Nat→Nat), q%2=1 →
      (∀ k, d*(F k:Int)=2^(L*k+v+s₁)*q+a) →
      (∀ k, d*(G k:Int)=2^(L*k+v+s₂)*q+b) →
      ∃ k≤B, ∃ i j, run i (F k)=run j (G k) := by
  let S := 2*L*l.period*r.period
  have sp : 0<S := by dsimp [S];exact Nat.mul_pos (Nat.mul_pos (Nat.mul_pos (by decide) pos) (time_pos l)) (time_pos r)
  let P := fun W B => ∀ (t : Nat) (q : Int) (F G : Nat→Nat), q%2=1 →
      (∀ k, d*(F k:Int)=2^(L*k+(S*t+W)+s₁)*q+a) →
      (∀ k, d*(G k:Int)=2^(L*k+(S*t+W)+s₂)*q+b) →
      ∃ k≤B, ∃ i j, run i (F k)=run j (G k)
  have all : ∀W<S, ∃B, P W B := fun W _ => compatible L W s₁ s₂ d a b pos odd l r density
  obtain ⟨B,bank⟩ := finite_bound S P all
  refine ⟨B,?_⟩
  intro v q F G qo fl gl
  obtain ⟨h,le,cert⟩ := bank (v%S) (Nat.mod_lt _ sp)
  have rep : S*(v/S)+v%S=v := by rw [Nat.add_comm];exact Nat.mod_add_div _ _
  obtain ⟨k,bn,i,j,e⟩ := cert (v/S) q F G qo
    (fun k => by rw [rep];exact fl k) (fun k => by rw [rep];exact gl k)
  exact ⟨k,by omega,i,j,e⟩


private def atPhase (n p d j : Nat) : Nat := 2^j*n+(2^j*p)/d

private theorem phase_eq (n p d L k s : Nat) (den : d+1=2^L) :
    d*atPhase n p d (L*k+s)+(2^s*p)%d=2^(L*k+s)*(d*n+p) := by
  have power : 2^L ≡ 1 [MOD d] := by rw [←den];simp [Nat.ModEq]
  have mod : (2^(L*k+s)*p)%d=(2^s*p)%d := by
    rw [pow_add,pow_mul]
    have pre := ((power.pow k).mul_right (2^s)).mul_right p
    simpa [Nat.ModEq] using pre
  have rep := Nat.mod_add_div (2^(L*k+s)*p) d
  rw [mod] at rep
  dsimp [atPhase]
  calc
    _ = 2^(L*k+s)*(d*n)+((2^s*p)%d+d*((2^(L*k+s)*p)/d)) := by ring
    _ = _ := by rw [rep];ring

/-- A left phase and any right phase of the same word with the same
positive cycle density give one global block cap from every initial edge. -/
theorem rotation_cap (L p d s₁ s₂ : Nat) (pos : 0<L) (pp : 0<p) (small : p<d)
    (den : d+1=2^L) (late₁ : s₁≤L) (late₂ : s₂≤L)
    (l : PositiveCycle d (-(((2^s₁*p)%d:Nat):Int)))
    (r : PositiveCycle d ((d:Int)-(((2^s₂*p)%d:Nat):Int)))
    (density : lapGrade l*r.period=lapGrade r*l.period) :
    ∃ B, 0<B ∧ ∀ (C : Coloring) (n : Nat), Mixed C n → ∀ j, ¬WallWords.Copies C n j L p B := by
  have odd : (d:Int)%2=1 := by
    obtain ⟨b,eq⟩ : ∃ b,L=b+1 := ⟨L-1,by omega⟩
    rw [eq,pow_succ] at den;omega
  obtain ⟨B,all⟩ := sampled L s₁ s₂ _ _ _ pos odd l r density
  refine ⟨B+1,by omega,?_⟩
  intro C n cut j copies
  let m := index C n j
  let N := L*(B+1)
  have cm : Mixed C m := index_mixed C cut j
  obtain ⟨v,q,qo,src⟩ := WallPeriodic.split_twos (d*m+p) (by omega)
  let F := fun k => atPhase m p d (L*k+s₁)
  let G := fun k => atPhase m p d (L*k+s₂)+1
  have lift (k s : Nat) : (d:Int)*(atPhase m p d (L*k+s):Int)+(((2^s*p)%d:Nat):Int)
      =2^(L*k+v+s)*(q:Int) := by
    have e := phase_eq m p d L k s den
    rw [src,←Nat.mul_assoc,←pow_add,show L*k+s+v=L*k+v+s by omega] at e
    exact_mod_cast e
  obtain ⟨k,bk,i,t,meet⟩ := all v q F G (by omega)
    (fun k => by change (d:Int)*(atPhase m p d (L*k+s₁):Int)=_;rw [←lift k s₁];ring)
    (fun k => by change (d:Int)*((atPhase m p d (L*k+s₂)+1:Nat):Int)=_;rw [Nat.cast_add,Nat.cast_one,←lift k s₂];ring)
  have endpt := WallWords.read_blocks C copies
  rw [WallPeriodic.index_add] at endpt
  have finalEq : d*index C m N+p=2^N*(d*m+p) := by
    change d*index C (index C n j) (L*(B+1))+p=_
    rw [endpt];exact address_eq L p _ d (B+1) den
  have sample (s : Nat) (hs : s≤L) : index C m (L*k+s)=atPhase m p d (L*k+s) := by
    apply WallTernary.finite_floor C m N d p _ _ small finalEq
    have le := Nat.mul_le_mul_left L bk
    dsimp [N];rw [Nat.mul_add,Nat.mul_one];omega
  obtain ⟨left,_⟩ := index_eq C cm (L*k+s₁)
  obtain ⟨_,right⟩ := index_eq C cm (L*k+s₂)
  rw [sample s₁ late₁] at left
  rw [sample s₂ late₂] at right
  exact cm (left.symm.trans (((propagated_run C i _).symm.trans
    ((congrArg C.color meet).trans (propagated_run C t _))).trans right))

end WallShifted
