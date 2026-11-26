import WallGate
import Mathlib.Data.Nat.ModEq

namespace WallShadow
open WallRefinement WordRank

/-- Lift a completely checked rational reference phase to any ordinary source
obeying its integer chart. Signs are encoded by the two offsets a and b. -/
private theorem chart (h r a b d p e : Nat) (hr : r < 2^h)
    (gcd : Nat.gcd (2^h) 15 = 1) (seed : 15*r+a = 2^h*d+b)
    (steps : odds h r=p) (out : 15*run h r = 3^p*d+e)
    (x q : Nat) (eq : 15*x+a = 2^h*q+b) : 15*run h x = 3^p*q+e := by
  have hmod : (15*x+a) ≡ (15*r+a) [MOD 2^h] := by
    rw [eq,seed]
    simp [Nat.ModEq]
  have hxr : x ≡ r [MOD 2^h] := Nat.ModEq.cancel_left_of_coprime gcd (Nat.ModEq.add_right_cancel' a hmod)
  have hx : x%(2^h)=r := Eq.trans hxr (Nat.mod_eq_of_lt hr)
  let z := x/(2^h)
  have rep : x=2^h*z+r := by dsimp [z]; rw [←hx, Nat.add_comm]; exact (Nat.mod_add_div x (2^h)).symm
  have root : q = 15*z+d := by
    have ee : 2^h*q+b=(2^h)*(15*z+d)+b := by
      calc
        _ = 15*x+a := eq.symm
        _ = (2^h)*(15*z)+(15*r+a) := by rw [rep]; ring
        _ = _ := by rw [seed]; ring
    exact Nat.eq_of_mul_eq_mul_left (by positivity : 0<2^h) (Nat.add_right_cancel ee)
  rw [rep,(liftPrefix h z r).1,steps,Nat.mul_add,out,root]
  ring

private theorem left_entry (x q : Nat) (e : 15*x+11=256*q) :
    15*run 8 x=243*q+12 :=
  chart 8 187 11 0 11 5 12 (by decide) (by decide) (by decide) (by decide) (by decide) x q e

private theorem right_entry (x q : Nat) (e : 15*x=256*q+4) :
    15*run 8 x=243*q+57 :=
  chart 8 188 0 4 11 5 57 (by decide) (by decide) (by decide) (by decide) (by decide) x q e

private theorem left_lap (x q : Nat) (e : 15*x=2^36*q+12) :
    15*run 36 x=3^12*q+12 :=
  chart 36 13743895348 0 12 3 12 12 (by decide) (by decide) (by decide)
    (by decide) (by decide) x q e

private theorem right_lap (x q : Nat) (e : 15*x=2^20*q+57) :
    15*run 20 x=3^12*q+57 :=
  chart 20 209719 0 57 3 12 57 (by decide) (by decide) (by decide)
    (by decide) (by decide) x q e

private theorem laps (k c : Nat)
    (one : ∀ x q, 15*x=2^k*q+c → 15*run k x=3^12*q+c)
    (i x q : Nat) (h : 15*x=2^(k*i)*q+c) :
    15*run (k*i) x=3^(12*i)*q+c := by
  induction i generalizing x q with
  | zero => simpa [run] using h
  | succ i ih =>
    have pk : k*(i+1)=k+k*i := by ring
    have qe : 15*x=2^k*(2^(k*i)*q)+c := by rw [h,pk,pow_add]; ring
    have h' := one x (2^(k*i)*q) qe
    have h'' : 15*run k x=2^(k*i)*(3^12*q)+c := by rw [h']; ring
    rw [pk,runAdd,ih _ _ h'',show 12*(i+1)=12*i+12 by ring,pow_add]
    ring

/-- The integer address after appending k copies of the four bits 1011. -/
def block (n : Nat) : Nat → Nat
 | 0 => n
 | k+1 => 16*(block n k)+11

theorem block_eq (n k : Nat) : 15*block n k+11 = 2^(4*k)*(15*n+11) := by
  induction k with
  | zero => simp [block]
  | succ k ih =>
    rw [show 4*(k+1)=4*k+4 by ring, pow_add, block]
    calc
      _ = 16*(15*block n k+11) := by ring
      _ = _ := by rw [ih]; ring

/-- The signed reference phases are 12 and 57 after eight clocks. -/
private theorem tracked (left : Bool) (i s v n q k : Nat)
    (source : 15*n+11=2^v*q)
    (length : 4*k+v=8+(if left then 36 else 20)*i+s) :
    let w := block n k + (if left then 0 else 1)
    let K := if left then 36 else 20
    let c := if left then 12 else 57
    15*run (8+K*i) w=2^s*(3^(5+12*i)*q)+c := by
  dsimp
  have a := block_eq n k
  rw [source, ←Nat.mul_assoc,←pow_add,length,show 8+(if left=true then 36 else 20)*i+s =
      8+((if left=true then 36 else 20)*i+s) by omega,pow_add] at a
  cases left with
  | false =>
    simp only [Bool.false_eq_true,ite_false] at a ⊢
    have ent : 15*(block n k+1) = 256*(2^(20*i+s)*q)+4 := by
      norm_num [Nat.mul_assoc] at a
      omega
    have z := right_entry _ _ ent
    have t : 15*run 8 (block n k+1)=2^(20*i)*(243*2^s*q)+57 := by
      rw [z,pow_add]; ring
    rw [runAdd,laps 20 57 right_lap i _ _ t,pow_add]
    ring
  | true =>
    simp only [ite_true,Nat.add_zero] at a ⊢
    have ent : 15*block n k+11 = 256*(2^(36*i+s)*q) := by
      norm_num [Nat.mul_assoc] at a
      omega
    have z := left_entry _ _ ent
    have t : 15*run 8 (block n k)=2^(36*i)*(243*2^s*q)+12 := by
      rw [z,pow_add]; ring
    rw [runAdd,laps 36 12 left_lap i _ _ t,pow_add]
    ring

open CollatzReverseBasin

private theorem even_phase (x q a : Nat) (h : 15*x=2*q+2*a) :
    15*shortcut x=q+a := by
  have p : x%2=0 := by omega
  simp only [shortcut,p,ite_true]
  omega

private theorem odd_phase (x q a : Nat) (h : 15*x=2*q+(2*a+1)) :
    15*shortcut x=3*q+3*a+9 := by
  have p : x%2≠0 := by omega
  simp only [shortcut,p,ite_false]
  omega

/-- Left endpoint charts, listed in order of the two-adic valuation modulo four. -/
def leftBias : Nat → Nat
  | 0 => 12 | 1 => 6 | 2 => 3 | _ => 12
def rightBias : Nat → Nat
  | 0 => 57 | 1 => 93 | 2 => 147 | _ => 228
def leftGrade (s : Nat) : Nat := if s=3 then 6 else 5

private theorem left_tail (s x q : Nat) (small : s<4) (e : 15*x=2^s*q+12) :
    15*run s x=3^(leftGrade s-5)*q+leftBias s := by
  have split : s=0 ∨ s=1 ∨ s=2 ∨ s=3 := by omega
  rcases split with rfl|rfl|rfl|rfl
  · simpa [run,leftGrade,leftBias] using e
  · simpa [run,leftGrade,leftBias] using even_phase x q 6 e
  · have a := even_phase x (2*q) 6 (by omega)
    simpa [run,leftGrade,leftBias] using even_phase (shortcut x) q 3 (by omega)
  · have a := even_phase x (4*q) 6 (by omega)
    have b := even_phase (shortcut x) (2*q) 3 (by omega)
    exact odd_phase (shortcut (shortcut x)) q 1 (by omega)

private theorem right_tail (s x q : Nat) (small : s<4) (e : 15*x=2^s*q+57) :
    15*run s x=3^s*q+rightBias s := by
  have split : s=0 ∨ s=1 ∨ s=2 ∨ s=3 := by omega
  rcases split with rfl|rfl|rfl|rfl
  · simpa [run,rightBias] using e
  · exact odd_phase x q 28 e
  · have a := odd_phase x (2*q) 28 (by omega)
    have b := odd_phase (shortcut x) (3*q) 46 (by omega)
    change 15*shortcut (shortcut x)=9*q+147
    omega
  · have a := odd_phase x (4*q) 28 (by omega)
    have b := odd_phase (shortcut x) (6*q) 46 (by omega)
    have d := odd_phase (shortcut (shortcut x)) (9*q) 73 (by omega)
    change 15*shortcut (shortcut (shortcut x))=27*q+228
    omega

/-- A common-clock comparison counts 12 odds in either a 36-step left lap
or a 20-step right lap. The two clocks can start at different wall depths. -/
theorem paired_charts (s v n q i kL kR : Nat) (small : s<4)
    (src : 15*n+11=2^v*q) (lenL : 4*kL+v=8+36*i+s) (lenR : 4*kR+v=8+20*i+s) :
    let X := run (8+36*i+s) (block n kL)
    let Y := run (8+20*i+s) (block n kR+1)
    15*X = 3^(leftGrade s+12*i)*q+leftBias s ∧
    15*Y = 3^(5+s+12*i)*q+rightBias s := by
  dsimp only
  have hL := tracked true i s v n q kL src lenL
  have hR := tracked false i s v n q kR src lenR
  simp only [ite_true,Nat.add_zero] at hL
  simp only [Bool.false_eq_true,ite_false] at hR
  rw [runAdd (8+36*i),runAdd (8+20*i)]
  rw [left_tail s _ _ small hL,right_tail s _ _ small hR]
  have ge : 5 ≤ leftGrade s := by unfold leftGrade; split <;> decide
  have el : leftGrade s+12*i=leftGrade s-5+(5+12*i) := by omega
  have er : 5+s+12*i=s+(5+12*i) := by omega
  rw [el,er,pow_add (3:Nat) (leftGrade s-5),pow_add (3:Nat) s]
  constructor <;> ring

end WallShadow
