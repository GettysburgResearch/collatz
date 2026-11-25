import ReverseBasin
import TernaryPowerLift

namespace WordRank
open CollatzReverseBasin

def run : Nat → Nat → Nat
  | 0,n => n
  | k+1,n => run k (shortcut n)

def odds : Nat → Nat → Nat
  | 0,_ => 0
  | k+1,n => n%2 + odds k (shortcut n)

def word : Nat → Nat → List Bool
  | 0,_ => []
  | k+1,n => (n%2==1) :: word k (shortcut n)

theorem runAdd (a b n : Nat) : run (a+b) n=run b (run a n) := by
  induction a generalizing n with
  | zero => simp [run]
  | succ a ih => simpa [Nat.succ_add,run] using ih (shortcut n)

theorem oddsAdd (a b n : Nat) : odds (a+b) n=odds a n+odds b (run a n) := by
  induction a generalizing n with
  | zero => simp [run,odds]
  | succ a ih => simp [Nat.succ_add,run,odds,ih,Nat.add_assoc]

theorem halves (h v : Nat) : run h (2^h*v)=v ∧ odds h (2^h*v)=0 := by
  induction h with
  | zero => simp [run,odds]
  | succ h ih =>
    have eq : 2^(h+1)*v=2*(2^h*v) := by ring
    simpa [eq,run,odds,shortcut] using ih

theorem powOdd (q : Nat) : 3^q%2=1 := by
  induction q with
  | zero => decide
  | succ q h => rw [Nat.pow_succ,Nat.mul_mod,h]

private theorem shiftStep (u b : Nat) : shortcut (2*u+b) =
    (if b%2=0 then u else 3*u)+shortcut b := by
  have parity : (2*u+b)%2=b%2 := by omega
  unfold shortcut; rw [parity]; split <;> omega

/-- Specifying a word on an odd-slope progression selects a complete binary
subprogression in its original parameter. -/
theorem wordRow (W : List Bool) (A a : Nat) (odd : A%2=1) :
    ∃ c : Nat, ∀ k : Nat, word W.length (A*(2^W.length*k+c)+a)=W := by
  induction W generalizing A a with
  | nil => exact ⟨0,fun _ => rfl⟩
  | cons f W ih =>
    let b := if f then 1 else 0
    let r := (b+a)%2
    let y := A*r+a
    have bsmall : b<2 := by cases f <;> decide
    have yp : y%2=b := by
      dsimp [y,r]; rw [Nat.add_mod,Nat.mul_mod,odd]
      cases f <;> dsimp [b] <;> omega
    let D := if f then 3 else 1
    have dodd : D%2=1 := by cases f <;> decide
    have next (v : Nat) : shortcut (A*(2*v+r)+a) = (D*A)*v+shortcut y := by
      have eq : A*(2*v+r)+a = 2*(A*v)+y := by dsimp [y]; ring
      rw [eq,shiftStep]
      cases f <;> dsimp [b,D] at yp ⊢ <;> rw [yp] <;> simp ; ring
    have ao : (D*A)%2=1 := by rw [Nat.mul_mod,dodd,odd]
    obtain ⟨c,hc⟩ := ih (D*A) (shortcut y) ao
    refine ⟨2*c+r,fun k => ?_⟩
    have eq : 2^(W.length+1)*k+(2*c+r) = 2*(2^W.length*k+c)+r := by ring
    change (_ :: _) = f::W
    simp only [List.length_cons] at *
    rw [eq,next,hc]
    congr 1
    have zz : A*(2*(2^W.length*k+c)+r)+a=2*(A*(2^W.length*k+c))+y := by dsimp [y]; ring
    rw [zz]
    cases f <;> dsimp [b] at yp ⊢ <;> simp_all

/-- A whole dyadic cylinder follows the base's first h parities, with the
exact terminal slope 3^s where s counts those odd inputs. -/
theorem liftPrefix (h u b : Nat) :
    run h (2^h*u+b)=3^(odds h b)*u+run h b ∧ odds h (2^h*u+b)=odds h b := by
  induction h generalizing u b with
  | zero => simp [run,odds]
  | succ h ih =>
    let c := if b%2=0 then 1 else 3
    have step : shortcut (2^(h+1)*u+b)=2^h*(c*u)+shortcut b := by
      rw [show 2^(h+1)*u+b=2*(2^h*u)+b by ring]
      rw [shiftStep]
      by_cases e : b%2=0 <;> simp [c,e] ; ring
    have bit : (2^(h+1)*u+b)%2=b%2 := by
      rw [show 2^(h+1)*u+b=2*(2^h*u)+b by ring]; omega
    obtain ⟨rv,oc⟩ := ih (c*u) (shortcut b)
    simp only [run,odds,step,bit,rv,oc]
    rw [Nat.pow_add]
    by_cases e : b%2=0
    · simp [e,c]
    · have o : b%2=1 := by omega
      simp [o,c]; ring

private theorem unitStep (x : Nat) (hx : x%3≠0) : (shortcut x)%3≠0 := by
  unfold shortcut; split <;> omega

theorem unitRun (h x : Nat) (hx : x%3≠0) : (run h x)%3≠0 := by
  induction h generalizing x with
  | zero => exact hx
  | succ h ih => exact ih _ (unitStep _ hx)

private theorem unitOdd (x : Nat) (hx : x%2=1) : (shortcut x)%3≠0 := by
  unfold shortcut; split <;> omega

/-- A ternary progression of unit intercept can append any requested number
of odd inputs, then reach a large power of two with no further odd inputs
before that power. -/
theorem finishRow (R j v L : Nat) (unit : v%3≠0) :
    ∃ k e : Nat, L≤k ∧ 2≤e ∧ run R (3^(j+1)*k+v)=2^e ∧
      odds R (3^(j+1)*k+v)=R := by
  induction R generalizing j v L with
  | zero =>
    obtain ⟨e,k,le,h⟩ := TernaryPowerLift.cofinal j v (2+v+3^(j+1)*L) unit
    have hp := Nat.lt_two_pow_self (n:=e)
    have hk : L≤k := by
      by_contra! hh
      have cmp := Nat.mul_le_mul_left (3^(j+1)) (Nat.le_of_lt hh)
      omega
    exact ⟨k,e,hk,by omega,by simpa [run,Nat.add_comm] using h.symm,rfl⟩
  | succ R ih =>
    let A := 3^(j+1)
    let r := (v+1)%2
    let y := A*r+v
    have odd : A%2=1 := powOdd _
    have yo : y%2=1 := by dsimp [y,r]; rw [Nat.add_mod,Nat.mul_mod,odd]; omega
    obtain ⟨k,e,hk,he,rv,oc⟩ := ih (j+1) (shortcut y) L (unitOdd _ yo)
    have id : A*(2*k+r)+v=2*(A*k)+y := by dsimp [y]; ring
    have step : shortcut (A*(2*k+r)+v)=3^(j+1+1)*k+shortcut y := by
      rw [id,Nat.pow_succ]
      change shortcut (2*(A*k)+y)=A*3*k+shortcut y
      rw [shiftStep,yo]; simp; ring
    have odd' : (A*(2*k+r)+v)%2=1 := by rw [id]; omega
    refine ⟨2*k+r,e,by omega,he,?_,?_⟩
    · change run R (shortcut (A*(2*k+r)+v))=2^e
      rw [step,rv]
    · change (A*(2*k+r)+v)%2+odds R (shortcut (A*(2*k+r)+v))=R+1
      rw [odd',step,oc]; omega

/-- Every odd binary cylinder in a fixed ternary unit class attains every
rank from its forced prefix count upward, with cofinal ordinary starts. -/
theorem exactRankRow (H b R L : Nat) (unit : b%3≠0) :
    ∃ k e : Nat, L≤k ∧ 2≤e ∧
      run (H+R) (2^H*(243*k)+b)=2^e ∧
      odds (H+R) (2^H*(243*k)+b)=odds H b+R := by
  let s := odds H b
  let v := run H b
  obtain ⟨k,e,hk,he,rv,oc⟩ := finishRow R (s+4) v L (unitRun H b unit)
  have ep := liftPrefix H (243*k) b
  have eq : 3^(odds H b)*(243*k)=3^(s+4+1)*k := by dsimp [s]; ring
  rw [eq] at ep
  refine ⟨k,e,hk,he,?_,?_⟩
  · rw [runAdd,ep.1]; exact rv
  · rw [oddsAdd,ep.1,ep.2]; change _ + odds R (3^(s+4+1)*k+v) = _; rw [oc]
end WordRank
