import WallGate
import Mathlib.Data.Nat.ModEq
import Mathlib.Tactic.IntervalCases

namespace WallWheel
open WordRank

set_option exponentiation.threshold 1024 in
set_option maxRecDepth 8192 in
private theorem wheel_bit (i : Fin 10) :
    531441^(2^i.val) % (2^(5+i.val)) = 1+2^(4+i.val) := by
  have all : ∀ j : Fin 10, 531441^(2^j.val) % (2^(5+j.val)) = 1+2^(4+j.val) := by decide
  exact all i

private theorem two_lifts (k x t : Nat) (hk : k<10)
    (eq : x%(2^(4+k))=t%(2^(4+k))) :
    x%(2^(5+k))=t%(2^(5+k)) ∨ (x+2^(4+k))%(2^(5+k))=t%(2^(5+k)) := by
  interval_cases k <;> norm_num at * <;> omega

/-- The multiplier 3^12 moves through every lift of an odd residue modulo 16.
The exponent bound is the length of the orbit at precision 2^(4+k). -/
theorem wheel (k a t : Nat) (hk : k≤10) (odd : a%2=1) (same : a%16=t%16) :
    ∃ j<2^k, (531441^j*a)%(2^(4+k))=t%(2^(4+k)) := by
  induction k with
  | zero => exact ⟨0,by decide, by simpa using same⟩
  | succ k ih =>
    obtain ⟨j,hj,e⟩ := ih (by omega)
    let x := 531441^j*a
    let M := 2^(4+k)
    have xx : x%2=1 := by
      have powOdd : 531441^j ≡ 1 [MOD 2] := by simpa using (show 531441 ≡ 1 [MOD 2] by decide).pow j
      exact (show x ≡ 1*1 [MOD 2] from powOdd.mul odd)
    have bit := wheel_bit ⟨k,by omega⟩
    have mp : 2^(5+k)=2*M := by dsimp [M]; rw [show 5+k=(4+k)+1 by omega,pow_succ]; ring
    have add : (531441^(2^k)*x) ≡ (x+M) [MOD 2^(5+k)] := by
      have hbit : 531441^(2^k) ≡ (1+M) [MOD 2^(5+k)] := by
        change _ % _ = _ % _
        rw [bit]
        have hm : 1<M := by
          dsimp [M]
          rw [pow_add]; omega
        rw [Nat.mod_eq_of_lt (by omega : 1+M<2^(5+k))]
      refine (hbit.mul_right x).trans ?_
      have rep : x=2*(x/2)+1 := by omega
      have eq : (1+M)*x = (x+M)+(2*M)*(x/2) := by
        nth_rw 1 [rep]
        rw [show (1+M)*(2*(x/2)+1)=2*(x/2)+1+M+(2*M)*(x/2) by ring,←rep]
      rw [eq,mp]
      simp [Nat.ModEq]
    rcases two_lifts k x t (by omega) e with lhs|rhs
    · exact ⟨j,by rw [pow_succ]; omega,by simpa [show 4+(k+1)=5+k by omega] using lhs⟩
    · refine ⟨2^k+j,by rw [pow_succ]; omega,?_⟩
      rw [show 4+(k+1)=5+k by omega,pow_add,Nat.mul_assoc]
      exact Eq.trans add rhs

def multiplier (s : Nat) : Nat := if s=0 then 1 else if s=1 then 3 else 9
def offset (s : Nat) : Nat := if s=0 then 3 else if s=1 then 5 else 8

/-- Each row has one cylinder for every class modulo 16. -/
private def bank (s : Nat) : List Nat :=
  if s=0 then [736,369,98,99,388,21,406,1175,584,473,10,11,780,397,814,15]
  else if s=1 then [368,49,194,259,292,5,390,407,472,473,586,203,156,45,2990,271]
  else [7584,97,146,195,2148,293,3446,1495,184,393,13450,747,236,157,78,2607]

def residue (s : Nat) (t : Fin 16) : Nat := (bank s)[t.val]?.getD 0

private theorem bank_checked : ∀ (s : Fin 4) (t : Fin 16),
    let r := residue s.val t
    let A := multiplier s.val
    let B := offset s.val
    r<16384 ∧ r%16=t.val ∧ run 14 r = run 14 (A*r+B) ∧
      3^(odds 14 r)=A*3^(odds 14 (A*r+B)) := by decide

theorem bank_spec (s : Nat) (hs : s<4) (t : Fin 16) :
    residue s t<16384 ∧ residue s t%16=t.val := by
  have h := bank_checked ⟨s,hs⟩ t
  exact ⟨h.1,h.2.1⟩

/-- An ordinary x in the certified subclass physically merges with its affine mate. -/
theorem bank_merge (s x : Nat) (hs : s<4) (t : Fin 16) (hr : x%16384=residue s t) :
    run 14 x = run 14 (multiplier s*x+offset s) := by
  obtain ⟨_,_,v,o⟩ := bank_checked ⟨s,hs⟩ t
  let r := residue s t
  let A := multiplier s
  let B := offset s
  let z := x/16384
  have rep : x=2^14*z+r := by dsimp [z,r]; omega
  change run 14 x=run 14 (A*x+B)
  rw [rep,show A*(2^14*z+r)+B=2^14*(A*z)+(A*r+B) by ring,
    (liftPrefix 14 z r).1,(liftPrefix 14 (A*z) (A*r+B)).1]
  change run 14 r=run 14 (A*r+B) at v
  change 3^(odds 14 r)=A*3^(odds 14 (A*r+B)) at o
  rw [v,o]
  ring

end WallWheel
