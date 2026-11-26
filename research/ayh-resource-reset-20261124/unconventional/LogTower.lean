import LogTowerCore
set_option maxRecDepth 40000
set_option maxHeartbeats 4000000
set_option exponentiation.threshold 10000
namespace LogTower
open CollatzReverseBasin WordRank LogTowerData
attribute [local irreducible] WordRank.run WordRank.odds

private theorem high_index (m : Nat) (p : 0<m) : 11+162*m=63+(162*m-52) := by omega

private theorem high_power (m : Nat) (p : 0<m) : 3^(11+162*m)=3^63*3^(162*m-52) :=
  (congrArg (fun t : Nat => 3^t) (high_index m p)).trans (pow_add _ _ _)

/-- Exact ordinary two-arm coordinates after the valuation-length cycle.
The remaining variable is unrestricted. This form also covers odd
two-adic valuations by permitting v to be twice an odd number. -/
theorem ordinary_gate (r v u : Nat) (large : 58≤r) (vp : 0<v)
    (ru : 3^(162*(4^r*v))=1+2^(2*r+3)*u) :
    let m:=4^r*v
    let U:=3^(r-58)*u
    run (2*r+3) (3^(11+162*m)-1)=1+3^71*U ∧
    run (2*r+3) (3^(162*m-52)-1)=1+U := by
  let m:=4^r*v
  let ell:=r-58
  have er : ell+58=r := by dsimp [ell]; omega
  change 3^(162*m)=1+2^(2*r+3)*u at ru
  have mp : 1≤m := Nat.mul_pos (Nat.pow_pos (by decide : 0<(4:Nat))) vp
  have jdef : 52+(162*m-52)=162*m := by omega
  let y:=3^(162*m-52)
  have y_id : 3^52*y=3^(162*m) := by
    change 3^52*3^(162*m-52)=_; rw [←pow_add,jdef]
  have phase : 2*r+3=119+2*ell := by omega
  have qeq : 3^52*y=1+2^119*(4^ell*u) := by
    rw [y_id,ru,phase,pow_add,pow_mul]; ring
  obtain ⟨lower,upper⟩:=anchor_lift y (4^ell*u) qeq
  have top : 3^(11+162*m)=3^63*y := high_power m mp
  have upl : run 119 (3^63*y-1)=1+4^ell*(3^71*u) := upper.trans (by ring)
  change run (2*r+3) (3^(11+162*m)-1)=1+3^71*(3^ell*u) ∧
    run (2*r+3) (y-1)=1+3^ell*u
  rw [phase,runAdd,runAdd,top,upl,lower,laps,laps]
  constructor <;> ring

/-- A full band of e6 exponents, with the same finite terminal trace for
every member. The grade invariant is 3^r v at the original exponent
m=4^r v. A dyadic residue suffices even when v varies. -/
theorem band_peaks (r v : Nat) (large : 2955≤2*r) (vp : 0<v)
    (locked : 3^r*v ≡ 1 [MOD 2^K]) :
    let m:=4^r*v
    run (2*r+3+K) (3^(11+162*m)-1)=run (2*r+3+K) (3^(162*m-52)-1) := by
  let m:=4^r*v
  let ell:=r-58
  have er : ell+58=r := by dsimp [ell]; omega
  obtain ⟨u,ru,cu⟩:=normalized r v large
  change 3^(162*m)=1+2^(2*r+3)*u at ru
  have seed : 3^58*seedU ≡ seedB [MOD 2^K] := by
    change _%_=seedB%2^K
    rw [finite_unit.2.1]
    exact (Nat.mod_eq_of_lt (by rw [←finite_unit.2.1]; exact Nat.mod_lt _ (by positivity))).symm
  have inc : 3^58*(3^ell*u) ≡ 3^58*seedU [MOD 2^K] := by
    calc
      3^58*(3^ell*u) = 3^r*u := by rw [←er,pow_add]; ring
      _ ≡ 3^r*(v*seedB) [MOD 2^K] := cu.mul_left _
      _ = (3^r*v)*seedB := by ring
      _ ≡ 1*seedB [MOD 2^K] := locked.mul_right _
      _ ≡ 3^58*seedU [MOD 2^K] := by simpa using seed.symm
  have endU : 3^ell*u ≡ seedU [MOD 2^K] := Nat.ModEq.cancel_left_of_coprime (by decide) inc
  obtain ⟨upper,lower⟩:=ordinary_gate r v u (by omega) vp ru
  change run (2*r+3+K) (3^(11+162*m)-1)=run (2*r+3+K) (3^(162*m-52)-1)
  rw [runAdd (2*r+3) K,runAdd (2*r+3) K,upper,lower]
  exact (terminal_lift _ endU).symm

private theorem six_form (r : Nat) : 4^r*3^(2*r)=6^(2*r) := calc
  _ = 2^(2*r)*3^(2*r) := by rw [pow_mul (2:Nat) 2 r]; rfl
  _ = _ := (mul_pow (2:Nat) 3 (2*r)).symm

private theorem six_general (s r : Nat) (form : s=2*r) (large : 2955≤2*r)
    (locked : 3^r*3^s ≡ 1 [MOD 2^K]) :
    run (s+2960) (3^(11+162*6^s)-1)=run (s+2960) (3^(162*6^s-52)-1) := by
  subst s
  have main:=band_peaks r (3^(2*r)) large (Nat.pow_pos (by decide)) locked
  change run (2*r+3+K) (3^(11+162*(4^r*3^(2*r)))-1)=run (2*r+3+K) (3^(162*(4^r*3^(2*r))-52)-1) at main
  simpa only [six_form,show 2*r+3+K=2*r+2960 by change 2*r+3+2957=2*r+2960; omega] using main

/-- The original, preassigned parameters are m=6^s for EVERY positive
multiple s of 2^2956. They approach both zero addresses. -/
theorem six_peaks (k : Nat) :
    let s:=2*(2^2955*(k+1))
    let m:=6^s
    run (s+2960) (3^(11+162*m)-1)=run (s+2960) (3^(162*m-52)-1) := by
  let r:=2^2955*(k+1)
  let s:=2*r
  have lr : 2955≤2*r := by dsimp [r]; omega
  have re : 3^r ≡ 1 [MOD 2^K] := rotation_multiple 2954 _
  have lock : 3^r*3^s ≡ 1 [MOD 2^K] := by
    have es : 3^s=(3^r)^2 := by dsimp [s]; rw [show 2*r=r*2 by ring,pow_mul]
    rw [es]; simpa using re.mul (re.pow 2)
  exact six_general s r rfl lr lock

#print axioms ordinary_gate
#print axioms normalized
#print axioms band_peaks
#print axioms six_peaks
end LogTower
