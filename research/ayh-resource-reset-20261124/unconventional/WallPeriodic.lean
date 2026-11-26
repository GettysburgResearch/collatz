import WallShadow
import WallWheel

/-! Finite positive-source exclusion for a period-four wall that persists
forever in an exact signed rational model. -/
namespace WallPeriodic
open WordRank WallRefinement WallShadow WallWheel

private def depthL (v i : Nat) := (8+36*i+v%4-v)/4
private def depthR (v i : Nat) := (8+20*i+v%4-v)/4
private def X (n v i : Nat) := run (8+36*i+v%4) (block n (depthL v i))
private def Y (n v i : Nat) := run (8+20*i+v%4) (block n (depthR v i)+1)

private theorem charts (n v q i : Nat) (hv : 15*n+11=2^v*q) (large : v≤i) :
    15*X n v i=3^(leftGrade (v%4)+12*i)*q+leftBias (v%4) ∧
    Y n v i=multiplier (v%4)*X n v i+offset (v%4) := by
  let s := v%4
  have sm : s<4 := Nat.mod_lt _ (by decide)
  have dl : 4*depthL v i+v=8+36*i+s := by dsimp [depthL,s]; omega
  have dr : 4*depthR v i+v=8+20*i+s := by dsimp [depthR,s]; omega
  obtain ⟨hl,hr⟩ := paired_charts s v n q i _ _ sm hv dl dr
  change 15*X n v i=3^(leftGrade s+12*i)*q+leftBias s at hl
  change 15*Y n v i=3^(5+s+12*i)*q+rightBias s at hr
  refine ⟨hl,?_⟩
  change Y n v i=multiplier s*X n v i+offset s
  interval_cases s <;> norm_num [leftGrade,leftBias,rightBias,multiplier,offset,pow_add,Nat.mul_assoc] at hl hr ⊢ <;> omega

/-- Starting from any source valuation, two bounded, possibly different,
block depths have a left endpoint and a right endpoint that physically merge. -/
theorem cross_clock_merge (n v q : Nat) (src : 15*n+11=2^v*q) (qodd : q%2=1) :
    ∃ kL≤9*(v+1024)+3, ∃ kR≤9*(v+1024)+3,
    ∃ hL hR, run hL (block n kL)=run hR (block n kR+1) := by
  let s := v%4
  let i0 := v+1
  let a := 3^(leftGrade s+12*i0)*q
  let c := leftBias s
  have hs : s<4 := Nat.mod_lt _ (by decide)
  have hc : c<16384 := by
    change leftBias s<16384
    interval_cases s <;> decide
  have base : 15*X n v i0=a+c := (charts n v q i0 src (by dsimp [i0]; omega)).1
  let t : Fin 16 := ⟨X n v i0%16,Nat.mod_lt _ (by decide)⟩
  let r := residue s t
  obtain ⟨range,kind⟩ := bank_spec s hs t
  change r%16=X n v i0%16 at kind
  change r<16384 at range
  let target := 15*r+16384-c
  have ct : target+c=15*r+16384 := by dsimp [target]; omega
  have amod : a%16=target%16 := by omega
  have odd : a%2=1 := by
    have pp : 3^(leftGrade s+12*i0) ≡ 1 [MOD 2] := by
      simpa using (show 3 ≡ 1 [MOD 2] by decide).pow (leftGrade s+12*i0)
    exact (show a ≡ 1*1 [MOD 2] from pp.mul qodd)
  obtain ⟨j,limit,w⟩ := wheel 10 a target (by decide) odd amod
  change j<1024 at limit
  change 531441^j*a%16384=target%16384 at w
  let i := i0+j
  have sizing : v≤i ∧ i≤v+1024 := by dsimp [i,i0]; omega
  obtain ⟨hx,hy⟩ := charts n v q i src sizing.1
  have grade : 3^(leftGrade s+12*i)*q = 531441^j*a := by
    dsimp [i,a]
    rw [show leftGrade s+12*(i0+j)=12*j+(leftGrade s+12*i0) by ring,pow_add,pow_mul]
    ring
  change 15*X n v i=3^(leftGrade s+12*i)*q+c at hx
  rw [grade] at hx
  have e : X n v i % 16384=r := by omega
  have joint := bank_merge s (X n v i) hs t e
  change Y n v i=multiplier s*X n v i+offset s at hy
  rw [←hy] at joint
  refine ⟨depthL v i,by dsimp [depthL]; omega,depthR v i,by dsimp [depthR]; omega,
    8+36*i+s+14,8+20*i+s+14,?_⟩
  rw [runAdd (8+36*i+s) 14,runAdd (8+20*i+s) 14]
  exact joint

/-- A persistent oriented ordinary wall departs from the digits (1011)^infinity.
The bound measures blocks of four digits and depends only on the source valuation. -/
theorem breaks_by (C : Coloring) {n : Nat} (cut : Mixed C n)
    (v q : Nat) (src : 15*n+11=2^v*q) (qodd : q%2=1) :
    ∃ k≤9*(v+1024)+3, index C n (4*k) ≠ block n k := by
  obtain ⟨l,bl,r,br,hL,hR,merge⟩ := cross_clock_merge n v q src qodd
  by_contra! all
  have a := (index_eq C cut (4*l)).1
  have b := (index_eq C cut (4*r)).2
  rw [all l bl] at a
  rw [all r br] at b
  exact cut (a.symm.trans (((propagated_run C hL _).symm.trans
    ((congrArg C.color merge).trans (propagated_run C hR _))).trans b))

theorem split_twos (m : Nat) (pos : 0<m) : ∃ v q, q%2=1 ∧ m=2^v*q := by
  induction m using Nat.strong_induction_on with
  | h m ih =>
    by_cases odd : m%2=1
    · exact ⟨0,m,odd,by simp⟩
    · obtain ⟨v,q,z,e⟩ := ih (m/2) (by omega) (by omega)
      refine ⟨v+1,q,z,?_⟩
      calc
        m = 2*(m/2) := by omega
        _ = 2^(v+1)*q := by rw [e,pow_succ]; ring

theorem no_infinite_period (C : Coloring) {n : Nat} (cut : Mixed C n) :
    ∃ k, index C n (4*k) ≠ block n k := by
  obtain ⟨v,q,hq,src⟩ := split_twos (15*n+11) (by omega)
  obtain ⟨k,_,h⟩ := breaks_by C cut v q src hq
  exact ⟨k,h⟩

end WallPeriodic
