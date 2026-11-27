import FloorCounting
import Mathlib.Data.Nat.ModEq

/-! One unconditional pair of actual paths at original hard parents.
The upper path of the supplied smaller canonical source reaches a site
less than 2^-40 times the original parent. -/
set_option autoImplicit false
set_option warningAsError true
namespace PaidCheckpoint
open CoreBranching FloorCounting PeakRigidity

private theorem step_pair (v : ℕ) : run 2 (4*v+1)=3*v+1 := by
  rw [show 4*v+1=2*(2*v)+1 by omega,run,step_odd,
      show 3*(2*v)+2=2*(3*v+1) by omega,run,step_double,run]

/-- All complete turns based at the signed positive center 1. -/
theorem positive_turns (n v : ℕ) : run (2*n) (4^n*v+1)=3^n*v+1 := by
  induction n generalizing v with
  | zero => simp [run]
  | succ n ih =>
    rw [show 2*(n+1)=2+2*n by omega,pow_succ,pow_succ,
        show 4^n*4*v+1=4*(4^n*v)+1 by ring,run_add,step_pair,
        show 3*(4^n*v)+1=4^n*(3*v)+1 by ring,ih]
    ring

private theorem small_after_turns (d : ℕ) :
    2^40*(3^(100+d)+1)<2^7*4^(100+d) := by
  induction d with
  | zero => decide +kernel
  | succ d ih =>
    rw [show 100+(d+1)=100+d+1 by omega,pow_succ,pow_succ]
    omega

/-- The two physical prefix identities use the same free parameter.
Here X=502+19683v is the particular residue of 2^(m-7). -/
theorem seed_paths (v : ℕ) :
    let w := 80225+3145728*v
    let X := 502+19683*v
    w%48=17 ∧ 6561*w+28927=2^20*X ∧
    run 13 w=128*X-1 ∧ grade 13 w=8 ∧
    run 20 (3*w)=X+1 ∧ grade 20 (3*w)=7 := by
  dsimp
  have lo := lift_prefix 13 0 80225 (384*v)
  have hi := lift_prefix 20 0 240675 (9*v)
  norm_num [show run 13 80225=64255 by decide,show grade 13 80225=8 by decide] at lo
  norm_num [show run 20 240675=503 by decide,show grade 20 240675=7 by decide] at hi
  have a : 8192*(384*v)=3145728*v := by ring
  have b : 3*(80225+3145728*v)=240675+1048576*(9*v) := by ring
  rw [a] at lo
  rw [b]
  omega

private theorem pow_residue (a b c d m t : ℕ)
    (h : a^b ≡ c [MOD m]) (p : a^d ≡ 1 [MOD m]) :
    a^(b+d*t) ≡ c [MOD m] := by
  rw [pow_add,pow_mul]
  simpa only [one_pow,mul_one] using h.mul (p.pow t)

theorem delayed_address (t : ℕ) :
    ∃ j, 12*2^(18*(64+81*t))-1=8111+13122*j := by
  have h := pow_residue 2 1152 676 1458 2187 t
    (by decide +kernel) (by decide +kernel)
  have e : 18*(64+81*t)=1152+1458*t := by ring
  change 2^(1152+1458*t)%2187=676%2187 at h
  rw [←e] at h
  exact ⟨2*(2^(18*(64+81*t))/2187),by omega⟩

/-- A literal smaller canonical source, both of its actual endpoints,
and the strict height payment. The source address j=50 mod81 is stated
as m=8111+13122t. -/
theorem paid_parent (t z : ℕ) (parent : 81*z+271=128*2^(8111+13122*t)) :
    ∃ w, 0<w ∧ w<z ∧ w%48=17 ∧
      run 13 w=2^(8111+13122*t)-1 ∧ grade 13 w=8 ∧
      run 20 (3*w)=2^(8104+13122*t)+1 ∧ grade 20 (3*w)=7 ∧
      run (20+(8104+13122*t)) (3*w)=3^(4052+6561*t)+1 ∧
      2^40*(3^(4052+6561*t)+1)<z := by
  let X := 2^(8104+13122*t)
  have res := pow_residue 2 8104 502 13122 19683 t
    (by decide +kernel) (by decide +kernel)
  change X%19683=502%19683 at res
  let v := X/19683
  have Xv : X=502+19683*v := by dsimp [v]; omega
  have power : 2^(8111+13122*t)=128*X := by
    change 2^(8111+13122*t)=128*2^(8104+13122*t)
    rw [show 8111+13122*t=7+(8104+13122*t) by omega,pow_add]
    rfl
  have tr := seed_paths v
  rw [←Xv] at tr
  obtain ⟨can,shape,lo,lg,hi,hg⟩:=tr
  let n := 4052+6561*t
  have clk : 8104+13122*t=2*n := by dsimp [n]; omega
  have powX : X=4^n := by
    dsimp [X]
    rw [clk,pow_mul]
    rfl
  have bound := small_after_turns (3952+6561*t)
  rw [show 100+(3952+6561*t)=n by dsimp [n]; omega,←powX] at bound
  rw [power] at parent ⊢
  refine ⟨80225+3145728*v,by omega,by omega,can,lo,lg,hi,hg,?_,by change 2^40*(3^n+1)<z; omega⟩
  rw [run_add,hi,clk,powX,←show 4^n*1=4^n by simp,positive_turns,mul_one]

#print axioms positive_turns
#print axioms seed_paths
#print axioms delayed_address
#print axioms paid_parent
end PaidCheckpoint
