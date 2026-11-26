import CheckpointUnitExit

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 12000
set_option maxHeartbeats 4000000

namespace CollatzFixedCofactorRescue
open CollatzReverseBasin CollatzMersenneParity CollatzCheckpointUnitExit

private def odds : ℕ → ℕ → ℕ
  | 0,_ => 0
  | k+1,x => x%2+odds k (shortcut x)

private theorem lift (t k x : ℕ) :
    atClock t (2^t*k+x)=3^(odds t x)*k+atClock t x := by
  induction t generalizing k x with
  | zero => simp [atClock,odds]
  | succ t ih =>
    rw [atClock, atClock, odds, pow_add (3:ℕ)]
    by_cases h : x%2=0
    · have a : shortcut (2^(t+1)*k+x)=2^t*k+shortcut x := by
        rw [show 2^(t+1)*k=2*(2^t*k) by ring]
        unfold shortcut
        split <;> omega
      rw [a,ih,h]
      simp
    · have o : x%2=1 := by omega
      have a : shortcut (2^(t+1)*k+x)=2^t*(3*k)+shortcut x := by
        rw [show 2^(t+1)*k=2*(2^t*k) by ring,
            show 2^t*(3*k)=3*(2^t*k) by ring]
        unfold shortcut
        split <;> omega
      rw [a,ih,o]
      ring

private theorem cat (a b x : ℕ) : atClock (a+b) x=atClock b (atClock a x) := by
  induction a generalizing x with
  | zero => simp [atClock]
  | succ a ih => simpa [Nat.succ_add,atClock] using ih (shortcut x)

private def sqMod (x M : ℕ) : ℕ → ℕ
  | 0 => x%M
  | k+1 => (sqMod x M k)^2%M

private theorem sqMod_correct (x M k : ℕ) : x^(2^k)%M = sqMod x M k := by
  induction k with
  | zero => simp [sqMod]
  | succ k ih =>
    rw [pow_succ,pow_mul,Nat.pow_mod,ih]
    rfl

private def R : ℕ := 357515049256705

private theorem sourceResidue (u : ℕ) :
    3^(42*(2^128*(1+2^49*u))) % (2^180) = 1+2^131*R := by
  have lo : (3^42)^(2^128) % (2^180) = 1+2^131*R := by
    rw [sqMod_correct]
    decide
  have hi : (3^42)^(2^177) % (2^180) = 1 := by
    rw [sqMod_correct]
    decide
  have decomp : 42*(2^128*(1+2^49*u)) = 42*2^128+(42*2^177)*u := by ring
  rw [decomp,pow_add,pow_mul,pow_mul (3:ℕ) (42*2^177) u,pow_mul,
      Nat.mul_mod,lo,Nat.pow_mod,hi,one_pow]
  decide

/-- Affine identity on the actual low-unit class, with explicitly unequal
exponents and with all odd/even choices forced by the ordinary map. -/
theorem shortMerger (k : ℕ) :
    let V:=2^49*k+R
    atClock 49 (4*3^84*V-5) =
      atClock 178 (3^21*(2^131*V+1)-1) := by
  dsimp only
  let X:=4*3^84*R-5
  let Y:=3^21*(2^131*R+1)-1
  have a : 4*3^84*(2^49*k+R)-5=2^49*((4*3^84)*k)+X := by
    dsimp [X,R]; omega
  have b : 3^21*(2^131*(2^49*k+R)+1)-1=2^178*((4*3^21)*k)+Y := by
    dsimp [Y,R]; omega
  rw [a,b,lift,lift]
  have c : odds 49 X=25 := by decide
  have d : odds 178 Y=88 := by decide
  have same : atClock 49 X=atClock 178 Y := by decide
  rw [c,d,same]
  omega

/-- Every supplied cofactor 1+2^49 u gives a physical rescue of the second raw
checkpoint by the earlier Mersenne exponent 42v+21. This includes cofactor 1. -/
theorem fixedCofactorFamily (u : ℕ) :
    let v:=2^128*(1+2^49*u)
    atClock 183 (32*3^(42*v-4)-17) =
      atClock ((42*v+21)+178) (2^(42*v+21)-1) := by
  let v:=2^128*(1+2^49*u)
  change atClock 183 (32*3^(42*v-4)-17) = atClock ((42*v+21)+178) (2^(42*v+21)-1)
  let k:=3^(42*v)/2^180
  let V:=2^49*k+R
  have res : 3^(42*v)%2^180=1+2^131*R := sourceResidue u
  have raw : 3^(42*v)=2^131*V+1 := by
    dsimp [V,k]
    have eqn:=Nat.mod_add_div (3^(42*v)) (2^180)
    rw [res] at eqn
    omega
  have big : 4≤42*v := by dsimp [v]; omega
  have reduce : 81*3^(42*v-4)=3^(42*v) := by
    rw [show (81:ℕ)=3^4 by decide,←pow_add,show 4+(42*v-4)=42*v by omega]
  have Vpos : 0<V := Nat.add_pos_right _ (by decide : 0<R)
  have first:=secondUnitExit 42 2 (3^(42*v-4)) V Vpos
    (by rw [reduce,raw]; omega)
  have start : atClock 134 (32*3^(42*v-4)-17)=4*3^84*V-5 := by
    change atClock 134 (32*3^(42*v-4)-17) = 9^42*(2^2*V)-5 at first
    rw [first]
    apply congrArg (·-5)
    rw [mul_left_comm,←mul_assoc]
    rfl
  have peak:=ascent (42*v+21) 1 (by decide)
  simp only [Nat.mul_one] at peak
  rw [show 183=134+49 by decide,cat,start,cat,peak,pow_add (3:ℕ) (42*v) 21,raw,Nat.mul_comm (2^131*V+1)]
  exact shortMerger k

#print axioms shortMerger
#print axioms fixedCofactorFamily

end CollatzFixedCofactorRescue
