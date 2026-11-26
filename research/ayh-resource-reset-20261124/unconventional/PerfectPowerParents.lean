import LogTower
import MersenneParity
import MersenneBarrier
import SignedCycleDilation
import FinalProofProposal


/-! A pointwise least-parent exclusion at every perfect 2^2956-th power
of an arbitrary ordinary base. -/
set_option maxRecDepth 40000
set_option maxHeartbeats 4000000
set_option exponentiation.threshold 10000
namespace PerfectPowerParents
open CollatzReverseBasin WordRank LogTowerData


private theorem split_base (b : Nat) (bp : 0<b) :
    ∃ a c : Nat, c%2=1 ∧ b=2^a*c := by
  induction b using Nat.strong_induction_on with
  | h b ih =>
    by_cases oc : b%2=1
    · exact ⟨0,b,oc,by simp⟩
    · obtain ⟨a,c,co,form⟩:=ih (b/2) (by omega) (by omega)
      refine ⟨a+1,c,co,?_⟩
      calc
        b=2*(b/2) := by omega
        _=2^(a+1)*c := by rw [form,pow_succ]; ring

private theorem odd_rotation (h b : Nat) (odd : b%2=1) :
    ∃ c : Nat, b^(2^(h+1))=1+2^(h+3)*c := by
  induction h with
  | zero =>
    have rem : b^2%8=1 := by
      rw [Nat.pow_mod]
      rcases (show b%8=1 ∨ b%8=3 ∨ b%8=5 ∨ b%8=7 by omega) with t|t|t|t <;> rw [t]
    exact ⟨b^2/8,by change b^2=1+8*(b^2/8); omega⟩
  | succ h ih =>
    obtain ⟨c,ec⟩:=ih
    refine ⟨c+2^(h+2)*c^2,?_⟩
    rw [pow_succ (2:Nat) (h+1),pow_mul,ec,show h+1+3=h+3+1 by omega,
        pow_succ (2:Nat) (h+3),show h+3=h+2+1 by omega,pow_succ (2:Nat) (h+2)]; ring

private theorem odd_mod (h b v : Nat) (odd : b%2=1) :
    b^(2^(h+1)*v) ≡ 1 [MOD 2^(h+3)] := by
  obtain ⟨c,hc⟩:=odd_rotation h b odd
  rw [pow_mul,hc]
  have eq : 1+2^(h+3)*c ≡ 1 [MOD 2^(h+3)] := by simp [Nat.ModEq]
  simpa only [one_pow] using eq.pow v

set_option maxHeartbeats 0 in
private theorem odd_anchor : run 1143 (3^173-1)=1 ∧ odds 1143 (3^173-1)=548 ∧
    run 1143 (3^131-1)=1 ∧ odds 1143 (3^131-1)=590 := by decide +kernel

private theorem shifted (A B Q : Nat) (large : 0<A) (eq : B=1+2^1143*Q) :
    A*B-1=2^1143*(A*Q)+(A-1) := by
  have h : 2^1143*(A*Q)+(A-1)=2^1143*(A*Q)+A-1 := by omega
  rw [h,eq]; apply congrArg (fun n : Nat => n-1); ring

section
attribute [local irreducible] WordRank.run WordRank.odds
/-- On the odd-base branch the original positive anchor has a grade-
compensated merger with exponent 42 lower. -/
private theorem odd_peaks (m : Nat) (phase : m ≡ 1 [MOD 2^1141]) :
    run 1143 (3^(11+162*m)-1)=run 1143 (3^(11+162*m-42)-1) := by
  let v:=m/2^1141
  have rem : m%2^1141=1 := phase
  have me : m=1+2^1141*v := by
    calc m = m%2^1141+2^1141*v := (Nat.mod_add_div _ _).symm
         _ = _ := by rw [rem]
  let R:=3^(2^1141*(162*v))
  have cR : R ≡ 1 [MOD 2^1143] := odd_mod 1140 3 (162*v) (by decide)
  let Q:=R/2^1143
  have re : R=1+2^1143*Q := by
    calc R = R%2^1143+2^1143*Q := (Nat.mod_add_div _ _).symm
         _ = _ := by rw [show R%2^1143=1 from cR]
  have e1 : 3^(11+162*m)=3^173*R := by
    apply (congrArg (fun x : Nat => 3^x) _).trans (pow_add 3 173 (2^1141*(162*v)))
    rw [me]; ring
  have e2 : 3^(11+162*m-42)=3^131*R := by
    apply (congrArg (fun x : Nat => 3^x) _).trans (pow_add 3 131 (2^1141*(162*v)))
    rw [me]; omega
  obtain ⟨l1,_⟩:=liftPrefix 1143 (3^173*Q) (3^173-1)
  obtain ⟨l2,_⟩:=liftPrefix 1143 (3^131*Q) (3^131-1)
  obtain ⟨t1,c1,t2,c2⟩:=odd_anchor
  rw [e1,e2,shifted _ _ _ (by positivity) re,shifted _ _ _ (by positivity) re,
      l1,l2,t1,t2,c1,c2]
  ring

end

private theorem reaches_peak (n : Nat) : run n (2^n-1)=3^n-1 := by
  have same (k x : Nat) : run k x=CollatzMersenneParity.atClock k x := by
    induction k generalizing x with
    | zero => rfl
    | succ k ih => exact ih (shortcut x)
  rw [same]
  simpa only [Nat.mul_one] using CollatzMersenneParity.ascent n 1 (by decide)

private theorem run_basin (h x : Nat) : Basin (run h x) ↔ Basin x := by
  induction h generalizing x with
  | zero => rfl
  | succ h ih => exact (ih (shortcut x)).trans (SignedCycleDilation.basin_value 1 x)

/-- The earlier ordinary source is within the already-established
quantitative leastness range; its triple's label is immaterial. -/
private theorem consume (m z n H : Nat) (np : 0<n) (lower : 40+n≤11+162*m)
    (eq : 81*z+271=128*2^(11+162*m))
    (hit : run H (3^(11+162*m)-1)=run H (3^n-1))
    (least : ∀ y, CollatzTwoOdd.ReverseDefect y → z≤y) : Basin z := by
  let j:=11+162*m
  have orig := (MersenneBarrier.mersenne_prefix z j eq).1
  change run 7 z+1=2^j at orig
  have join : run 7 z=2^j-1 := by omega
  have p1 : 1<(2:Nat)^n := Nat.one_lt_two_pow (by omega)
  have p2 : 2048≤(2:Nat)^j := Nat.pow_le_pow_right (by decide : 0<(2:Nat)) (show 11≤j by dsimp [j]; omega)
  have small : 2^40*(2^n-1)<2^j := calc
    _ < (2:Nat)^40*2^n := Nat.mul_lt_mul_of_pos_left (by omega) (by positivity)
    _ = (2:Nat)^(40+n) := (pow_add _ _ _).symm
    _ ≤ _ := Nat.pow_le_pow_right (by decide) lower
  change 81*z+271=128*2^j at eq
  by_contra fail
  have bad : ¬Basin (2^n-1) := by
    intro good
    have t:= (run_basin n (2^n-1)).mpr good
    rw [reaches_peak] at t
    have reached:= (run_basin H (3^n-1)).mpr t
    rw [←hit] at reached
    have b:= (run_basin H (3^j-1)).mp reached
    rw [←reaches_peak j] at b
    have c:= (run_basin j (2^j-1)).mp b
    exact fail ((run_basin 7 z).mp (join ▸ c))
  obtain ⟨y,d,cap⟩:=FinalProofProposal.quantitative_return (2^n-1) (by omega) bad
  have le:=least y d; omega

private theorem at_power (b z D G : Nat) (bounds : 2955≤2*G) (dp : 0<D)
    (de : D=2*G) (cp : ∀ c : Nat, c%2=1 → c^D ≡ 1 [MOD 2^K])
    (rotation : ∀ a : Nat, 3^(G*a) ≡ 1 [MOD 2^K])
    (eq : 81*z+271=128*2^(11+162*b^D))
    (least : ∀ y, CollatzTwoOdd.ReverseDefect y → z≤y) : Basin z := by
  by_cases zero : b=0
  · subst b
    have base : (0:Nat)^D=0 := zero_pow (by omega)
    rw [base] at eq
    have zz : z=3233 := by omega
    rw [zz]; exact ⟨107, rfl⟩
  obtain ⟨a,c,co,bc⟩:=split_base b (by omega)
  let m:=b^D
  have nonzero : 0<m := Nat.pow_pos (by omega)
  have cu:=cp c co
  by_cases az : a=0
  · subst a
    have mb : m=c^D := by dsimp [m]; simp only [bc,pow_zero,one_mul]
    have ph : m ≡ 1 [MOD 2^1141] := by rw [mb]; exact cu.of_dvd (pow_dvd_pow 2 (by decide : 1141≤K))
    have meet:=odd_peaks m ph
    exact consume m z (11+162*m-42) 1143 (by omega) (by omega) eq meet least
  · let r:=G*a
    have large : 2955≤2*r := by
      have le:=Nat.mul_le_mul_left (2*G) (show 1≤a by omega)
      dsimp [r]; nlinarith only [bounds,le]
    have rb : 3^r ≡ 1 [MOD 2^K] := rotation a
    have locked : 3^r*c^D ≡ 1 [MOD 2^K] := by simpa only [Nat.one_mul] using rb.mul cu
    have me : m=4^r*c^D := by
      dsimp [m,r]; rw [bc,mul_pow,←pow_mul,show (4:Nat)=2^2 by decide,←pow_mul]
      rw [show a*D=2*(G*a) by rw [de]; ring]
    have meet:=LogTower.band_peaks r (c^D) large (Nat.pow_pos (by omega)) locked
    change run _ (3^(11+162*(4^r*c^D))-1)=run _ (3^(162*(4^r*c^D)-52)-1) at meet
    rw [←me] at meet
    exact consume m z (162*m-52) _ (by omega) (by omega) eq meet least

/-- Every ordinary perfect power with this fixed exponent has a
convergent original e6 parent under leastness, regardless of base. -/
theorem excluded (b z : Nat)
    (eq : 81*z+271=128*2^(11+162*b^(2^2956)))
    (least : ∀ y, CollatzTwoOdd.ReverseDefect y → z≤y) : Basin z := by
  apply at_power b z (2^2956) (2^2955) (by decide) (by positivity) (by decide) _ _ eq least
  · intro c odd
    have cc:=odd_mod 2955 c 1 odd
    simp only [Nat.mul_one] at cc
    exact cc.of_dvd (pow_dvd_pow 2 (by decide : K≤2955+3))
  · intro a
    exact odd_mod 2954 3 a (by decide)

#print axioms odd_peaks
#print axioms excluded
end PerfectPowerParents
