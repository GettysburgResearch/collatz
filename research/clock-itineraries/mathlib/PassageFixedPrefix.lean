module

public import PassageAligned
import all PassageAligned
import all PassageRouting
import all FiberTransport
import all TowerFrontierAffine
import all TernaryItinerary
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.PassageFixedPrefix

open TowerFrontier PassageRouting PassageAligned
set_option autoImplicit false

private theorem balance {j x a h L Q : ℕ} (hitA : track L a 0=(1,Q))
    (same : track (j+h) x 0=track h a 0) :
    ∃ H, FirstLow H x 1 ∧ H+2*Q=j+L+2*odds H x := by
  have aref : run L a=1 := by rw [←FiberTransport.track_value L a 0,hitA]
  have aq : odds L a=Q := congrArg Prod.snd hitA
  have through : track (j+(L+2*h)) x 0=track (L+2*h) a 0 := by
    conv => lhs; rw [show j+(L+2*h)=(j+h)+(L+h) by omega,TowerFrontier.track_add,same]
    conv => rhs; rw [show L+2*h=h+(L+h) by omega,TowerFrontier.track_add]
  have endHit : run (j+(L+2*h)) x=1 := by
    have eq := congrArg Prod.fst through
    simp only [FiberTransport.track_value] at eq
    rw [eq,run_add,aref,(PassageAligned.laps h).1]
  have endCount : odds (j+(L+2*h)) x=Q+h := by
    have eq : odds (j+(L+2*h)) x=odds (L+2*h) a := congrArg Prod.snd through
    rw [eq,PassageAligned.extend L,aref,aq,(PassageAligned.laps h).2]
  classical
  have existsHit : ∃ t, run t x=1 := ⟨_,endHit⟩
  let H := Nat.find existsHit
  have first : run H x=1 := Nat.find_spec existsHit
  have earlier (k : ℕ) (less : k<H) : 1<run k x := by
    have ne : run k x≠1 := Nat.find_min existsHit less
    have zrun (n : ℕ) : run n 0=0 := by
      induction n with
      | zero => rfl
      | succ n ih => simpa [run,step] using ih
    have nz : run k x≠0 := by
      intro z
      rw [show H=k+(H-k) by omega,run_add,z,zrun] at first
      contradiction
    omega
  let d := j+(L+2*h)-H
  have le : H≤j+(L+2*h) := Nat.find_min' existsHit endHit
  have total : H+d=j+(L+2*h) := by dsimp only [d]; omega
  rw [←total,run_add,first] at endHit
  rw [←total,PassageAligned.extend,first] at endCount
  have ret := PassageAligned.return_count d endHit
  exact ⟨H,⟨first,earlier⟩,by omega⟩

private theorem bernoulli (q : ℕ) : (q+5)*10^q≤5*12^q := by
  induction q with
  | zero => decide
  | succ q ih =>
    have step := Nat.mul_le_mul_right (10^q) (show 10*(q+1+5)≤12*(q+5) by omega)
    have mul := Nat.mul_le_mul_left 12 ih
    rw [pow_succ,pow_succ]
    nlinarith only [step,mul]

/-- A fixed ordinary reference hitting one controls the first arrival and
    odd grade of every scale-aligned profile, independently of binary depth. -/
theorem fixed_prefix_barrier {a L Q j x : ℕ} (hitA : track L a 0=(1,Q))
    (upper : x<2^j*(a+1)) (aligned : ∃ h, track (j+h) x 0=track h a 0) :
    ∃ H, FirstLow H x 1 ∧ H+2*Q=j+L+2*odds H x ∧
      2^L*12^(odds H x)<(a+1)*4^Q*10^(odds H x) ∧
      odds H x+5<5*(a+1)*4^Q := by
  obtain ⟨h,same⟩ := aligned
  obtain ⟨H,first,clock⟩ := balance hitA same
  let q := odds H x
  have pos10 : 0<10^q := Nat.pow_pos (by decide)
  have count := PassageAligned.odd_cost (m:=3) first (fun i hi odd => by have := first.2 i hi; omega)
  change 2^H*3^q≤x*10^q at count
  have price := Nat.mul_lt_mul_of_pos_right (count.trans_lt (Nat.mul_lt_mul_of_pos_right upper pos10))
    (Nat.pow_pos (by decide : 0<4) (n:=Q))
  have costEq : 2^H*3^q*4^Q=2^j*(2^L*12^q) := by
    have exp := congrArg (fun t : ℕ => 2^t) clock
    change 2^(H+2*Q)=2^(j+L+2*q) at exp
    rw [pow_add,pow_mul,pow_add,pow_add,pow_mul] at exp
    have mul := congrArg (fun v : ℕ => v*3^q) exp
    rw [show (12:ℕ)=4*3 by decide,mul_pow]
    change (2^H*4^Q)*3^q=(2^j*2^L*4^q)*3^q at mul
    nlinarith only [mul]
  rw [costEq] at price
  have reordered : (2^j*(a+1)*10^q)*4^Q=2^j*((a+1)*4^Q*10^q) := by ring
  rw [reordered] at price
  have sharp := Nat.lt_of_mul_lt_mul_left price
  have lower : 12^q≤2^L*12^q := Nat.le_mul_of_pos_left _ (Nat.two_pow_pos _)
  have lin := Nat.mul_lt_mul_of_pos_left (lower.trans_lt sharp) (by decide : 0<5)
  have B := bernoulli q
  have costQ : (q+5)*10^q<(5*(a+1)*4^Q)*10^q := by nlinarith only [lin,B]
  exact ⟨H,first,clock,sharp,Nat.lt_of_mul_lt_mul_right costQ⟩

#print axioms fixed_prefix_barrier

end Collatz.Itinerary.PassageFixedPrefix
