import WallLinear

namespace WallDelay
open WallRational WallGeneral WallDensity WordRank

/-- The two signed reference trajectories are disjoint even after reduction
modulo this fixed binary precision, at all pairs of chronological clocks. -/
def Separated (d a b : Int) (s : Nat) : Prop :=
  ∀ i j, (runD d i a)%(2^s)≠(runD d j b)%(2^s)

private theorem residue (d a q : Int) (M s h x : Nat) (odd : d%2=1) (room : h+s≤M)
    (src : d*(x:Int)=2^M*q+a) : (d*(run h x:Int))%2^s=(runD d h a)%2^s := by
  let R := M-(h+s)
  have exp : M=h+s+R := by dsimp [R];omega
  let u : Int := 2^s*(2^R*q)
  have eq : d*(x:Int)=2^h*u+a := by rw [src,exp,pow_add,pow_add];dsimp [u];ring
  rw [lift d a u h x odd eq]
  rw [show 3^(grade d h a)*u=2^s*(3^(grade d h a)*(2^R*q)) by dsimp [u];ring]
  simp

/-- If two distinct rational shadows are separated modulo 2^s, at least
one physical arm must run almost to its full valuation-plus-depth clock
before an ordinary merger can occur. This bound holds at any block depths. -/
theorem merger_needs_clock (L p d s : Nat) (pos : 0<L) (den : d+1=2^L)
    (sep : Separated d (-(p:Int)) ((d:Int)-p) s)
    (n v q i j h t : Nat) (src : d*n+p=2^v*q)
    (meet : run h (address L p n i)=run t (address L p n j+1)) :
    L*i+v<h+s ∨ L*j+v<t+s := by
  have odd : (d:Int)%2=1 := by
    obtain ⟨x,e⟩ : ∃ x,L=x+1 := ⟨L-1,by omega⟩
    rw [e,pow_succ] at den;omega
  have addr (k : Nat) : (d:Int)*address L p n k+p=2^(L*k+v)*(q:Int) := by
    have e := address_eq L p n d k den
    rw [src,←Nat.mul_assoc,←pow_add] at e
    exact_mod_cast e
  by_contra! no
  have left := residue d (-(p:Int)) q (L*i+v) s h (address L p n i) odd no.1
    (by rw [←addr];ring)
  have right := residue d ((d:Int)-p) q (L*j+v) s t (address L p n j+1) odd no.2
    (by rw [←addr,Nat.cast_add,Nat.cast_one];ring)
  rw [meet] at left
  exact sep h t (left.symm.trans right)

private def states (d : Int) : Nat → Int → List Int
  | 0,_ => []
  | k+1,a => a::states d k (step d a)

private theorem in_states (d a : Int) (N k : Nat) (lt : k<N) : runD d k a∈states d N a := by
  induction N generalizing a k with
  | zero => omega
  | succ N ih =>
    cases k with
    | zero => simp [runD,states]
    | succ k => exact List.mem_cons_of_mem _ (ih _ _ (by omega))

private theorem finite_state (d a : Int) (c : PositiveCycle d a) (k : Nat) :
    runD d k a∈states d (c.entry+c.period) a := by
  have pp := time_pos c
  by_cases small : k<c.entry
  · exact in_states d a _ k (by omega)
  let rem := (k-c.entry)%c.period
  let times := (k-c.entry)/c.period
  have sr : rem<c.period := Nat.mod_lt _ pp
  have rep : c.entry+c.period*times+rem=k := by
    have e := Nat.mod_add_div (k-c.entry) c.period
    dsimp [times,rem];omega
  have eq := (lap d (runD d c.entry a) c.period (lapGrade c) times c.returns rfl).1
  have unroll : runD d k a=runD d (c.entry+rem) a := by
    nth_rw 1 [←rep]
    rw [runD_add,runD_add,eq,runD_add]
  rw [unroll]
  exact in_states d a _ _ (by omega)

private def residues (d a : Int) (N s : Nat) : List Int :=
  (states d N a).map (fun x => x%(2^s))

private theorem certify (d a b : Int) (s : Nat) (l : PositiveCycle d a) (r : PositiveCycle d b)
    (test : (residues d a (l.entry+l.period) s).all
      (fun x => !(residues d b (r.entry+r.period) s).contains x)=true) : Separated d a b s := by
  intro i j eq
  have left : (runD d i a)%2^s∈residues d a (l.entry+l.period) s :=
    List.mem_map.mpr ⟨_,finite_state d a l i,rfl⟩
  have right : (runD d j b)%2^s∈residues d b (r.entry+r.period) s :=
    List.mem_map.mpr ⟨_,finite_state d b r j,rfl⟩
  have neg := List.all_eq_true.mp test _ left
  rw [eq] at neg
  simp [right] at neg

set_option maxRecDepth 16384 in
set_option maxHeartbeats 2000000 in
/-- The two disjoint period-18 reference orbits are separated modulo 65536
including every preperiodic state. -/
theorem period18_separated : Separated 262143 (-87383) (262143-87383) 16 := by
  let l : PositiveCycle 262143 (-87383) := ⟨9,72,by decide,by decide⟩
  let r : PositiveCycle 262143 (262143-87383) := ⟨288,72,by decide,by decide⟩
  exact certify _ _ _ 16 l r (by decide +revert)


set_option maxRecDepth 16384 in
theorem other_separations :
    Separated 15 (-11) (15-11) 6 ∧ Separated 255 (-95) (255-95) 7 ∧
    Separated 4095 (-2047) (4095-2047) 13 := by
  let l₄ : PositiveCycle 15 (-11) := ⟨4,3,by decide,by decide⟩
  let r₄ : PositiveCycle 15 (15-11) := ⟨8,5,by decide,by decide⟩
  let l₈ : PositiveCycle 255 (-95) := ⟨7,7,by decide,by decide⟩
  let r₈ : PositiveCycle 255 (255-95) := ⟨9,31,by decide,by decide⟩
  let l₁₂ : PositiveCycle 4095 (-2047) := ⟨41,48,by decide,by decide⟩
  let r₁₂ : PositiveCycle 4095 (4095-2047) := ⟨13,84,by decide,by decide⟩
  exact ⟨certify _ _ _ 6 l₄ r₄ (by decide +revert),
         certify _ _ _ 7 l₈ r₈ (by decide +revert),
         certify _ _ _ 13 l₁₂ r₁₂ (by decide +revert)⟩

/-- All four residue precisions are sharp by exhibited chronological pairs. -/
theorem missing_bit :
    ¬Separated 15 (-11) (15-11) 5 ∧ ¬Separated 255 (-95) (255-95) 6 ∧
    ¬Separated 4095 (-2047) (4095-2047) 12 ∧ ¬Separated 262143 (-87383) (262143-87383) 15 :=
  ⟨fun h => h 0 4 (by decide),fun h => h 6 0 (by decide),
   fun h => h 0 12 (by decide),fun h => h 5 5 (by decide)⟩

/-- Given any common physical horizon H, some positive source rules out
every merger before H at every pair of repeated-word block depths. -/
theorem period18_unbounded_clocks (H : Nat) :
    ∃ n, 0<n ∧ ∀ i j h t, h≤H → t≤H →
      run h (address 18 87383 n i)≠run t (address 18 87383 n j+1) := by
  let J := H+16
  let n := address 18 87383 0 J
  have eq := address_eq 18 87383 0 262143 J (by decide)
  simp only [Nat.mul_zero,Nat.zero_add] at eq
  have bigger : 1<2^(18*J) := by
    have mono : (2:Nat)^1≤2^(18*J) := Nat.pow_le_pow_right (by decide) (by dsimp [J];omega)
    omega
  have np : 0<n := by dsimp [n];omega
  refine ⟨n,np,?_⟩
  intro i j h t hl tl meet
  have bad := merger_needs_clock 18 87383 262143 16 (by decide) (by decide)
    period18_separated n (18*J) 87383 i j h t eq meet
  dsimp [J] at bad
  omega

end WallDelay
