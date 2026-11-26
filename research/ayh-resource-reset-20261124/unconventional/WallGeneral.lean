import WallOrbit

namespace WallGeneral
open WallRational WallAffine WallRefinement WordRank

/-- After k repetitions of a word with L binary digits and integer value p. -/
def address (L p n : Nat) : Nat → Nat
  | 0 => n
  | k+1 => 2^L*address L p n k+p

theorem address_eq (L p n d k : Nat) (den : d+1=2^L) :
    d*address L p n k+p=2^(L*k)*(d*n+p) := by
  induction k with
  | zero => simp [address]
  | succ k ih =>
    rw [address,show L*(k+1)=L+L*k by ring,pow_add]
    calc
      _ = 2^L*(d*address L p n k)+(d+1)*p := by ring
      _ = _ := by rw [den,←Nat.mul_add,ih];ring

/-- The rational numerator orbit enters a cycle that contains an odd numerator. -/
structure PositiveCycle (d a : Int) where
  entry : Nat
  period : Nat
  returns : runD d period (runD d entry a)=runD d entry a
  positive : 0<grade d period (runD d entry a)

theorem phase_at (d a : Int) (c : PositiveCycle d a) (H : Nat) (later : c.entry≤H) :
    runD d c.period (runD d H a)=runD d H a ∧
    grade d c.period (runD d H a)=grade d c.period (runD d c.entry a) := by
  let j := H-c.entry
  let base := runD d c.entry a
  have start : runD d H a=runD d j base := by
    rw [←runD_add,show c.entry+j=H by dsimp [j];omega]
  rw [start]
  have ret : runD d c.period base=base := c.returns
  constructor
  · rw [←runD_add,Nat.add_comm j c.period,runD_add,ret]
  · have e : grade d (j+c.period) base=grade d (c.period+j) base := by rw [Nat.add_comm]
    rw [grade_add,grade_add,ret] at e
    change grade d c.period (runD d j base)=grade d c.period base
    omega

theorem chart_arm (d a q : Int) (L v K m other : Nat) (starts : Nat → Nat)
    (dodd : d%2=1) (source : ∀ k, d*(starts k:Int)=2^(L*k+v)*q+a)
    (c : PositiveCycle d a) (later : c.entry≤L*K+v)
    (count : grade d c.period (runD d c.entry a)=m) (i : Nat) :
    let k := K+c.period*2*other*i
    d*(run (L*k+v) (starts k):Int)=
      3^(grade d (L*K+v) a)*q*9^((m*other*L)*i)+runD d (L*K+v) a := by
  dsimp only
  let H := L*K+v
  let z := 2*other*L*i
  let phase := runD d H a
  have clk : L*(K+c.period*2*other*i)+v=H+c.period*z := by dsimp [H,z];ring
  obtain ⟨ret,gr⟩ := phase_at d a c H later
  obtain ⟨r,g⟩ := lap d phase c.period m z ret (gr.trans count)
  have aff := lift d a q _ _ dodd (source (K+c.period*2*other*i))
  rw [aff,clk,runD_add,grade_add]
  change 3^(grade d H a+grade d (c.period*z) phase)*q+runD d (c.period*z) phase=
    3^(grade d H a)*q*9^((m*other*L)*i)+phase
  rw [r,g,pow_add,show m*z=2*((m*other*L)*i) by dsimp [z];ring,pow_mul]
  ring

theorem signed_nat (h x : Nat) : runD 1 h (x:Int)=(run h x:Int) := by
  have one (t : Nat) : step 1 (t:Int)=(CollatzReverseBasin.shortcut t:Int) := by
    by_cases ev : t%2=0
    · obtain ⟨z,rfl⟩ : ∃ z,t=2*z := ⟨t/2,by omega⟩
      simp [step,CollatzReverseBasin.shortcut]
    · obtain ⟨z,rfl⟩ : ∃ z,t=2*z+1 := ⟨t/2,by omega⟩
      have h1 : CollatzReverseBasin.shortcut (2*z+1)=3*z+2 := by simp [CollatzReverseBasin.shortcut];omega
      rw [h1];push_cast;simp [step];omega
  induction h generalizing x with
  | zero => rfl
  | succ h ih => rw [runD,run,one,ih]

/-- Physical merger at (in general different) depths of an arbitrary word.
Both rational reference phases must enter cycles with positive odd counts. -/
theorem cross_clock (L p n d : Nat) (pos : 0<L) (pp : 0<p) (den : d+1=2^L)
    (l : PositiveCycle d (-(p:Int))) (r : PositiveCycle d ((d:Int)-p)) :
    ∃ k₁ k₂ h₁ h₂, run h₁ (address L p n k₁)=run h₂ (address L p n k₂+1) := by
  obtain ⟨v,q,odd,src⟩ := WallPeriodic.split_twos (d*n+p) (by omega)
  have dint : (d:Int)%2=1 := by
    obtain ⟨b,eq⟩ : ∃ b,L=b+1 := ⟨L-1,by omega⟩
    rw [eq,pow_succ] at den;omega
  have qint : (q:Int)%2=1 := by omega
  let K := l.entry+r.entry
  let H := L*K+v
  have kh : K≤H := by
    dsimp [H]
    have mul : K≤L*K := by simpa using Nat.mul_le_mul_right K pos
    omega
  have ltime : l.entry≤H := by dsimp [K] at kh;omega
  have rtime : r.entry≤H := by dsimp [K] at kh;omega
  let m := grade d l.period (runD d l.entry (-(p:Int)))
  let z := grade d r.period (runD d r.entry ((d:Int)-p))
  have mp : 0<m := l.positive
  have zp : 0<z := r.positive
  let kL := fun i => K+l.period*2*z*i
  let kR := fun i => K+r.period*2*m*i
  let X := fun i => run (L*kL i+v) (address L p n (kL i))
  let Y := fun i => run (L*kR i+v) (address L p n (kR i)+1)
  have num (k : Nat) : (d:Int)*address L p n k+p=2^(L*k+v)*q := by
    have e := address_eq L p n d k den
    rw [src,←Nat.mul_assoc,←pow_add] at e
    exact_mod_cast e
  have left (i : Nat) : (d:Int)*(X i:Int)=
      3^(grade d H (-(p:Int)))*(q:Int)*9^((m*z*L)*i)+runD d H (-(p:Int)) := by
    exact chart_arm d (-(p:Int)) q L v K m z (address L p n) dint
      (fun k => by have e := num k;omega) l ltime rfl i
  have right (i : Nat) : (d:Int)*(Y i:Int)=
      3^(grade d H ((d:Int)-p))*(q:Int)*9^((m*z*L)*i)+runD d H ((d:Int)-p) := by
    rw [show m*z=z*m by ring]
    apply chart_arm d ((d:Int)-p) q L v K z m (fun k => address L p n k+1) dint _ r rtime rfl i
    intro k
    push_cast
    rw [Int.mul_add,Int.mul_one]
    have e := num k
    omega
  obtain ⟨i,a,b,hit⟩ := WallOrbit.paired _ _ (m*z*L) (by positivity) d q _ _ dint qint
    (fun i => (X i:Int)) (fun i => (Y i:Int)) left right
  rw [signed_nat,signed_nat] at hit
  refine ⟨kL i,kR i,L*kL i+v+a,L*kR i+v+b,?_⟩
  rw [runAdd (L*kL i+v),runAdd (L*kR i+v)]
  exact_mod_cast hit

/-- No ordinary persistent mixed edge admits this eventually periodic trace:
start the theorem at any later mixed descendant to remove the transient. -/
theorem breaks (C : Coloring) {n : Nat} (cut : Mixed C n) (L p d : Nat)
    (pos : 0<L) (pp : 0<p) (den : d+1=2^L)
    (l : PositiveCycle d (-(p:Int))) (r : PositiveCycle d ((d:Int)-p)) :
    ∃ k, index C n (L*k)≠address L p n k := by
  by_contra! always
  obtain ⟨u,v,a,b,join⟩ := cross_clock L p n d pos pp den l r
  have left := (index_eq C cut (L*u)).1
  have right := (index_eq C cut (L*v)).2
  rw [always] at left right
  exact cut (left.symm.trans (((propagated_run C a _).symm.trans
    ((congrArg C.color join).trans (propagated_run C b _))).trans right))

end WallGeneral
