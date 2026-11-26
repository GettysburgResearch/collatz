import WallDichotomy

namespace WallDensity
open WallGeneral WallRational WallAffine WallOrbit WallUniform WallRefinement WordRank

def lapGrade {d a : Int} (c : PositiveCycle d a) : Nat :=
  grade d c.period (runD d c.entry a)

theorem time_pos {d a : Int} (c : PositiveCycle d a) : 0<c.period := by
  have p := c.positive
  by_contra! zero
  rw [show c.period=0 by omega,grade] at p
  omega

private theorem phases (d a : Int) (c : PositiveCycle d a) (base other L t : Nat)
    (late : c.entry≤base) :
    let S := 2*L*c.period*other
    runD d (base+S*t) a=runD d base a ∧
    grade d (base+S*t) a=grade d base a+2*((lapGrade c*other*L)*t) := by
  dsimp only
  let turns := 2*L*other*t
  have e : 2*L*c.period*other*t=c.period*turns := by dsimp [turns];ring
  obtain ⟨ret,cnt⟩ := phase_at d a c base late
  obtain ⟨endpt,num⟩ := lap d (runD d base a) c.period (lapGrade c) turns ret cnt
  rw [e,runD_add,grade_add,endpt,num]
  constructor
  · rfl
  · dsimp [turns];ring

theorem chart_from_residue (d a q : Int) (L K w t i other : Nat) (starts : Nat → Nat)
    (odd : d%2=1) (c : PositiveCycle d a) (late : c.entry≤L*K+w)
    (source : ∀ k, d*(starts k:Int)=2^(L*k+(2*L*c.period*other*t+w))*q+a) :
    let v := 2*L*c.period*other*t+w
    let k := K+c.period*2*other*i
    let g := lapGrade c*other*L
    d*(run (L*k+v) (starts k):Int)=
      3^(grade d (L*K+w) a)*(9^(g*t)*q)*9^(g*i)+runD d (L*K+w) a := by
  dsimp only
  let v := 2*L*c.period*other*t+w
  have late' : c.entry≤L*K+v := by dsimp [v];omega
  have row := chart_arm d a q L v K (lapGrade c) other starts odd source c late' rfl i
  dsimp only at row
  have tm : L*K+v=L*K+w+2*L*c.period*other*t := by dsimp [v];ring
  obtain ⟨cycle,count⟩ := phases d a c (L*K+w) other L t late
  rw [tm,cycle,count,pow_add,pow_mul] at row
  exact row.trans (by ring)

private def SameBlock (L p n B : Nat) : Prop :=
  ∃ k≤B, ∃ a b, run a (address L p n k)=run b (address L p n k+1)

private theorem at_residue (L p d w : Nat) (pos : 0<L) (den : d+1=2^L)
    (l : PositiveCycle d (-(p:Int))) (r : PositiveCycle d ((d:Int)-p))
    (density : lapGrade l*r.period=lapGrade r*l.period) :
    ∃ B, ∀ n q t, q%2=1 →
      d*n+p=2^(2*L*l.period*r.period*t+w)*q → SameBlock L p n B := by
  have dint : (d:Int)%2=1 := by
    obtain ⟨b,eq⟩ : ∃ b,L=b+1 := ⟨L-1,by omega⟩
    rw [eq,pow_succ] at den;omega
  let K := l.entry+r.entry
  let H := L*K+w
  have lh : K≤H := by
    have a : K≤L*K := by simpa using Nat.mul_le_mul_right K pos
    dsimp [H];omega
  have lt : l.entry≤H := by dsimp [K] at lh;omega
  have rt : r.entry≤H := by dsimp [K] at lh;omega
  let g := lapGrade l*r.period*L
  have gp : 0<g := Nat.mul_pos (Nat.mul_pos l.positive (time_pos r)) pos
  obtain ⟨T,meet⟩ := paired_bound (grade d H (-(p:Int))) (grade d H ((d:Int)-p)) g gp
    d (runD d H (-(p:Int))) (runD d H ((d:Int)-p)) dint
  let k := fun i => K+l.period*2*r.period*i
  refine ⟨k T,?_⟩
  intro n q t qo src
  let v := 2*L*l.period*r.period*t+w
  let X := fun i => run (L*k i+v) (address L p n (k i))
  let Y := fun i => run (L*k i+v) (address L p n (k i)+1)
  let unit : Int := 9^(g*t)*q
  have uo : unit%2=1 := by
    dsimp [unit];rw [Int.mul_emod,odd_power 9 (by decide)]
    have cast : (q:Int)%2=1 := by omega
    rw [cast];decide
  have num (k : Nat) : (d:Int)*address L p n k+p=2^(L*k+v)*q := by
    have e := address_eq L p n d k den
    rw [src,←Nat.mul_assoc,←pow_add] at e
    exact_mod_cast e
  have left (i : Nat) : (d:Int)*(X i:Int)=
      3^(grade d H (-(p:Int)))*unit*9^(g*i)+runD d H (-(p:Int)) := by
    exact chart_from_residue d (-(p:Int)) q L K w t i r.period (address L p n) dint l lt
      (fun j => by have e := num j;change _=2^(L*j+v)*(q:Int)+_;omega)
  have right (i : Nat) : (d:Int)*(Y i:Int)=
      3^(grade d H ((d:Int)-p))*unit*9^(g*i)+runD d H ((d:Int)-p) := by
    have swapped : 2*L*r.period*l.period*t+w=v := by dsimp [v];ring
    have base (j : Nat) : (d:Int)*((address L p n j+1:Nat):Int)=
        2^(L*j+(2*L*r.period*l.period*t+w))*(q:Int)+((d:Int)-p) := by
      rw [swapped];push_cast;rw [Int.mul_add,Int.mul_one]
      have e := num j;omega
    have row := chart_from_residue d ((d:Int)-p) q L K w t i l.period
      (fun j => address L p n j+1) dint r rt base
    dsimp only at row
    rw [swapped,show K+r.period*2*l.period*i=k i by dsimp [k];ring,←density] at row
    exact row
  obtain ⟨i,sm,a,b,e⟩ := meet unit (fun i => (X i:Int)) (fun i => (Y i:Int)) uo left right
  rw [signed_nat,signed_nat] at e
  refine ⟨k i,by dsimp [k];exact Nat.add_le_add_left (Nat.mul_le_mul_left _ (by omega)) _,
          L*k i+v+a,L*k i+v+b,?_⟩
  rw [runAdd (L*k i+v),runAdd (L*k i+v)]
  exact_mod_cast e

/-- Equal odd-step densities give a uniform ban from the very first digit.
A single block depth already works on both arms, even when their signed
reference cycles are distinct. Only the physical meeting clocks may vary. -/
theorem same_rate (L p d : Nat) (pos : 0<L) (pp : 0<p) (den : d+1=2^L)
    (l : PositiveCycle d (-(p:Int))) (r : PositiveCycle d ((d:Int)-p))
    (density : lapGrade l*r.period=lapGrade r*l.period) :
    ∃ B, ∀ n, ∃ k≤B, ∃ a b, run a (address L p n k)=run b (address L p n k+1) := by
  let S := 2*L*l.period*r.period
  have sp : 0<S := by dsimp [S];exact Nat.mul_pos (Nat.mul_pos (Nat.mul_pos (by decide) pos) (time_pos l)) (time_pos r)
  let P := fun w B => ∀ n q t, q%2=1 → d*n+p=2^(S*t+w)*q → SameBlock L p n B
  have all : ∀ w<S, ∃B, P w B := fun w _ => at_residue L p d w pos den l r density
  obtain ⟨B,bank⟩ := finite_bound S P all
  refine ⟨B,?_⟩
  intro n
  obtain ⟨v,q,qo,src⟩ := WallPeriodic.split_twos (d*n+p) (by omega)
  obtain ⟨b,le,row⟩ := bank (v%S) (Nat.mod_lt _ sp)
  have rep : S*(v/S)+v%S=v := by rw [Nat.add_comm];exact Nat.mod_add_div _ _
  obtain ⟨k,bk,a,t,meet⟩ := row n q (v/S) qo (by rw [rep];exact src)
  exact ⟨k,by omega,a,t,meet⟩

/-- The same word cap works from every position, without a source-dependent onset. -/
theorem universal_cap (L p d : Nat) (pos : 0<L) (pp : 0<p) (den : d+1=2^L)
    (l : PositiveCycle d (-(p:Int))) (r : PositiveCycle d ((d:Int)-p))
    (density : lapGrade l*r.period=lapGrade r*l.period) :
    ∃ B, ∀ (C : Coloring) (n : Nat), Mixed C n → ∀ j, ¬WallWords.Copies C n j L p B := by
  obtain ⟨B,all⟩ := same_rate L p d pos pp den l r density
  refine ⟨B,?_⟩
  intro C n cut j copies
  obtain ⟨k,small,a,b,meet⟩ := all (index C n j)
  have hCopies : WallWords.Copies C n j L p k := fun i hi => copies i (by omega)
  have agree := WallWords.read_blocks C hCopies
  have live := index_mixed C cut (j+L*k)
  rw [agree] at live
  exact live (((propagated_run C a _).symm.trans (congrArg C.color meet)).trans
    (propagated_run C b _))

set_option maxRecDepth 16384 in
/-- The signed rational model realizes this period, but ordinary walls obey
a common finite bound even from their initial edges. -/
theorem period18_uniform :
    ∃ B, ∀ (C : Coloring) (n : Nat), Mixed C n → ∀ j,
      ¬WallWords.Copies C n j 18 87383 B := by
  let l : PositiveCycle 262143 (-87383) := ⟨9,72,by decide,by decide⟩
  let r : PositiveCycle 262143 ((262143:Int)-87383) := ⟨288,72,by decide,by decide⟩
  exact universal_cap 18 87383 262143 (by decide) (by decide) (by decide) l r
    (by decide +revert)

end WallDensity
