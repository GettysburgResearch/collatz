import Mathlib.Tactic.Ring

/-! Whole-progression substitution and positive ordinary Collatz descent.
The affine rule/cover soundness construction adapts the proof pattern of PR193,
67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e, SingleReturn.lean. All rule
restrictions, certificates and theorems below are compiled in this namespace. -/
namespace UnitTripling

def T (n : Nat) : Nat := if n % 2 = 0 then n / 2 else (3*n+1)/2

inductive Mode | up | down | both deriving DecidableEq

def Forward (P : Nat → Prop) := ∀ u, u%3 ≠ 0 → P u → P (3*u)
def Reverse (P : Nat → Prop) := ∀ u, u%3 ≠ 0 → P (3*u) → P u
private def Law (m : Mode) (P : Nat → Prop) :=
  match m with | .up => Forward P | .down => Reverse P | .both => Forward P ∧ Reverse P

private structure Rule where
  i : Nat
  j : Nat
  k : Nat
  l : Nat

private def idle : Rule := ⟨1,0,1,0⟩
private def rules (m : Mode) : Char → Rule
  | 'h' => ⟨2,0,1,0⟩
  | 'D' => ⟨1,0,2,0⟩
  | 't' => ⟨2,1,3,2⟩
  | 'i' => ⟨3,2,2,1⟩
  | 'a' => if m = .down then idle else ⟨9,3,3,1⟩
  | 'b' => if m = .down then idle else ⟨9,6,3,2⟩
  | 'A' => if m = .up then idle else ⟨3,1,9,3⟩
  | 'B' => if m = .up then idle else ⟨3,2,9,6⟩
  | _ => idle

private theorem ruleSound (m : Mode) (P : Nat → Prop) (inv : ∀ n, P n ↔ P (T n))
    (jump : Law m P) (c : Char) (n : Nat) :
    P ((rules m c).k*n+(rules m c).l) → P ((rules m c).i*n+(rules m c).j) := by
  have even : P (2*n) ↔ P n := by
    have z : T (2*n) = n := by unfold T; split <;> omega
    simpa [z] using inv (2*n)
  have odd : P (2*n+1) ↔ P (3*n+2) := by
    have z : T (2*n+1) = 3*n+2 := by unfold T; split <;> omega
    simpa [z] using inv (2*n+1)
  have a : Forward P → (P (3*n+1) → P (9*n+3)) := by
    intro h; rw [show 9*n+3 = 3*(3*n+1) by omega]; exact h _ (by omega)
  have b : Forward P → (P (3*n+2) → P (9*n+6)) := by
    intro h; rw [show 9*n+6 = 3*(3*n+2) by omega]; exact h _ (by omega)
  have a' : Reverse P → (P (9*n+3) → P (3*n+1)) := by
    intro h; rw [show 9*n+3 = 3*(3*n+1) by omega]; exact h _ (by omega)
  have b' : Reverse P → (P (9*n+6) → P (3*n+2)) := by
    intro h; rw [show 9*n+6 = 3*(3*n+2) by omega]; exact h _ (by omega)
  cases m <;> unfold rules <;> split <;> simp [idle] <;>
    first | exact even.mp | exact even.mpr | exact odd.mp | exact odd.mpr
          | exact a jump | exact b jump | exact a' jump | exact b' jump
          | exact a jump.1 | exact b jump.1 | exact a' jump.2 | exact b' jump.2

private abbrev Row := Nat × Nat
private def eval (r : Row) (t : Nat) := r.1*t+r.2

private def applyRule (g : Rule) (r : Row) : Option Row :=
  let a := r.1/g.i
  let b := r.2/g.i
  if r.1 = g.i*a ∧ r.2 = g.i*b+g.j then
    some (g.k*a,g.k*b+g.l)
  else none

private theorem applySound (m : Mode) (P : Nat → Prop) (inv : ∀ n, P n ↔ P (T n))
    (jump : Law m P) (c : Char) (r q : Row)
    (ok : applyRule (rules m c) r = some q) (t : Nat) :
    P (eval q t) → P (eval r t) := by
  generalize eq : rules m c = g at ok
  simp only [applyRule] at ok
  split at ok
  next h =>
    have qeq := Option.some.inj ok
    subst q
    have src : eval r t = g.i*((r.1/g.i)*t+(r.2/g.i))+g.j := by
      unfold eval
      rw [Nat.mul_add, ← Nat.mul_assoc, ← h.1]
      omega
    rw [src]
    have step := ruleSound m P inv jump c ((r.1/g.i)*t+(r.2/g.i))
    rw [eq] at step
    simpa [eval, Nat.mul_add, Nat.mul_assoc, Nat.add_assoc] using step
  next => contradiction

private def word (m : Mode) : List Char → Row → Option Row
  | [], r => some r
  | c::cs, r => (applyRule (rules m c) r).bind (word m cs)

private theorem wordSound (m : Mode) (P : Nat → Prop) (inv : ∀ n, P n ↔ P (T n))
    (jump : Law m P) (w : List Char) (r q : Row)
    (ok : word m w r = some q) (t : Nat) : P (eval q t) → P (eval r t) := by
  induction w generalizing r with
  | nil =>
    exact Option.some.inj ok ▸ id
  | cons c cs ih =>
    cases e : applyRule (rules m c) r with
    | none => simp [word,e] at ok
    | some v =>
      have wv : word m cs v = some q := by simpa [word,e] using ok
      exact fun h => applySound m P inv jump c r v e t (ih v wv h)

-- Entries certify complete affine progressions at nonnegative integer parameters.
private def route : Mode → Nat → Nat → String
  | .up, 16, b => match b with
    | 2 => "h"
    | 3 => "tthh"
    | 4 => "h"
    | 5 => "th"
    | 6 => "h"
    | 8 => "h"
    | 9 => "th"
    | 10 => "h"
    | 12 => "h"
    | 13 => "th"
    | 14 => "h"
    | 16 => "h"
    | 17 => "th"
    | _ => ""
  | .up, 144, b => match b with
    | 7 => "tttDDibib"
    | 11 => "i"
    | 15 => "b"
    | 23 => "i"
    | 27 => "tthtDDDDibiathh"
    | 31 => "Dii"
    | 39 => "a"
    | 43 => "tthtDDiiib"
    | 47 => "i"
    | 55 => "tttDDibia"
    | 59 => "i"
    | 63 => "ttttDDibtDDibiathh"
    | 71 => "i"
    | 75 => "a"
    | 79 => "tttDDibib"
    | 87 => "b"
    | 91 => "tthtDDiiia"
    | 95 => "i"
    | 103 => "Dii"
    | 107 => "i"
    | 111 => "a"
    | 119 => "i"
    | 123 => "b"
    | 127 => "tttDDibia"
    | 135 => "tttDDibttDDibiathh"
    | 139 => "Dii"
    | 143 => "i"
    | _ => ""
  | .down, 16, b => match b with
    | 2 => "h"
    | 3 => "tthh"
    | 4 => "h"
    | 5 => "th"
    | 6 => "h"
    | 8 => "h"
    | 9 => "th"
    | 10 => "h"
    | 12 => "h"
    | 13 => "th"
    | 14 => "h"
    | 15 => "tBthhii"
    | 16 => "h"
    | 17 => "th"
    | _ => ""
  | .down, 144, b => match b with
    | 7 => "Athhh"
    | 11 => "i"
    | 23 => "i"
    | 55 => "Athhh"
    | 59 => "i"
    | 71 => "i"
    | 87 => "tDDiAttthhiDiiDiDiBtthhhhhhh"
    | 103 => "Dii"
    | 107 => "i"
    | 119 => "i"
    | 135 => "tDDiDiAtthhiDiDiAtthhhhhhh"
    | 139 => "Dii"
    | _ => ""
  | .down, 864, b => match b with
    | 27 => "tDDiDiAtthhthhhh"
    | 43 => "tthth"
    | 75 => "tthth"
    | 91 => "Aththh"
    | 171 => "tthth"
    | 183 => "ttthh"
    | 187 => "Aththh"
    | 219 => "tDDiDiBtthhthhhh"
    | 235 => "tthth"
    | 267 => "tthth"
    | 315 => "tDDiDiAtthhthhhh"
    | 331 => "tthth"
    | 363 => "tthth"
    | 379 => "Aththh"
    | 459 => "tthth"
    | 471 => "ttthh"
    | 475 => "Aththh"
    | 507 => "tDDiDiBtthhthhhh"
    | 523 => "tthth"
    | 555 => "tthth"
    | 603 => "tDDiDiAtthhthhhh"
    | 619 => "tthth"
    | 651 => "tthth"
    | 667 => "Aththh"
    | 747 => "tthth"
    | 759 => "ttthh"
    | 763 => "Aththh"
    | 795 => "tDDiDiBtthhthhhh"
    | 811 => "tthth"
    | 843 => "tthth"
    | _ => ""
  | .down, 5184, b => match b with
    | 39 => "tBththhi"
    | 123 => "tthttDDDDiDiDiDiiiiBthhthhhhhh"
    | 327 => "tDDiDiiiAthhhh"
    | 411 => "tthAthhi"
    | 615 => "tBththhi"
    | 699 => "tthtDDiiiDiiDiAtththtthhhh"
    | 987 => "tthAthhi"
    | 1191 => "tBththhi"
    | 1275 => "tthtDDiiiDiiii"
    | 1563 => "tthAthhi"
    | 1767 => "tBththhi"
    | 1851 => "tthttDDDDiDiDiDiiiiAthhthhhhhh"
    | 2055 => "tDDiDiiiBthhhh"
    | 2139 => "tthAthhi"
    | 2343 => "tBththhi"
    | 2427 => "tthtDDiiiDiiDiBtththtthhhh"
    | 2631 => "tDDiDiiDiBtthththhhhh"
    | 2715 => "tthAthhi"
    | 2919 => "tBththhi"
    | 3003 => "tthtDDiiiDiiiAthhh"
    | 3291 => "tthAthhi"
    | 3495 => "tBththhi"
    | 3783 => "tDDiDiiDDiAttthhhthhhhh"
    | 3867 => "tthAthhi"
    | 4071 => "tBththhi"
    | 4359 => "tDDiDiiDiAtthththhhhh"
    | 4443 => "tthAthhi"
    | 4647 => "tBththhi"
    | 4731 => "tthtDDiiiDiiDDiAttthhhtthhhh"
    | 5019 => "tthAthhi"
    | _ => ""
  | .down, 31104, b => match b with
    | 903 => "ttththh"
    | 1479 => "ttththAtDDDDiiiiiiDiiiAthhhhi"
    | 3207 => "ttththh"
    | 4155 => "tthtthh"
    | 4935 => "ttththAtDDDDiiiiiiDiiiBthhhhi"
    | 6663 => "ttththh"
    | 8763 => "tthtthh"
    | 10119 => "ttththh"
    | 11271 => "ttththh"
    | 11847 => "ttthtDDiiiiDDDiDiiiAthhhhh"
    | 13575 => "ttththh"
    | 14523 => "tthtthh"
    | 15303 => "ttththAtDDDDiiiiiiDiiiBthhhhi"
    | 16455 => "ttthtDDiiiDDiiDiiiBthhhh"
    | 17031 => "ttththh"
    | 19131 => "tthtthh"
    | 20487 => "ttththh"
    | 21639 => "ttththh"
    | 22215 => "ttthtDDiiiiDDDiDiiiBthhhhh"
    | 23943 => "ttththh"
    | 24891 => "tthtthh"
    | 25671 => "ttththAtDDDDiiiiiiDiiiBthhhhi"
    | 26823 => "ttthtDDiiiDDiiDiiiAthhhh"
    | 27399 => "ttththh"
    | 29499 => "tthtthh"
    | 30855 => "ttththh"
    | _ => ""
  | .down, 186624, b => match b with
    | 3579 => "tthAththh"
    | 6087 => "ttththth"
    | 8391 => "ttththth"
    | 9339 => "tthtthth"
    | 13947 => "tthtthth"
    | 18759 => "ttBtthhhh"
    | 19707 => "tthAththh"
    | 24315 => "tthAththh"
    | 29127 => "ttththth"
    | 30075 => "tthtthth"
    | 34683 => "tthtthth"
    | 37191 => "ttBtthhhh"
    | 39495 => "ttBtthhhh"
    | 40443 => "tthAththh"
    | 45051 => "tthAththh"
    | 49863 => "ttththth"
    | 50811 => "tthtthth"
    | 55419 => "tthtthth"
    | 60231 => "ttBtthhhh"
    | 61179 => "tthAththh"
    | 65787 => "tthAththh"
    | 68295 => "ttththth"
    | 70599 => "ttththth"
    | 71547 => "tthtthth"
    | 76155 => "tthtthth"
    | 80967 => "ttBtthhhh"
    | 81915 => "tthAththh"
    | 86523 => "tthAththh"
    | 91335 => "ttththth"
    | 92283 => "tthtthth"
    | 96891 => "tthtthth"
    | 99399 => "ttBtthhhh"
    | 101703 => "ttBtthhhh"
    | 102651 => "tthAththh"
    | 107259 => "tthAththh"
    | 112071 => "ttththth"
    | 113019 => "tthtthth"
    | 117627 => "tthtthth"
    | 122439 => "ttBtthhhh"
    | 123387 => "tthAththh"
    | 127995 => "tthAththh"
    | 130503 => "ttththth"
    | 132807 => "ttththth"
    | 133755 => "tthtthth"
    | 138363 => "tthtthth"
    | 143175 => "ttBtthhhh"
    | 144123 => "tthAththh"
    | 148731 => "tthAththh"
    | 153543 => "ttththth"
    | 154491 => "tthtthth"
    | 159099 => "tthtthth"
    | 161607 => "ttBtthhhh"
    | 163911 => "ttBtthhhh"
    | 164859 => "tthAththh"
    | 169467 => "tthAththh"
    | 174279 => "ttththth"
    | 175227 => "tthtthth"
    | 179835 => "tthtthth"
    | 184647 => "ttBtthhhh"
    | 185595 => "tthAththh"
    | _ => ""
  | .both, 18, b => match b with
    | 1 => "A"
    | 5 => "B"
    | 7 => "A"
    | 9 => "tDDiDiAtthhiDiDiAtthhhhi"
    | 11 => "B"
    | 13 => "A"
    | 17 => "B"
    | _ => ""
  | .both, 144, b => match b with
    | 3 => "tDDiAtBththhibiDi"
    | 15 => "tBthhiDDi"
    | 21 => "tDDiDiBtthhBthhiii"
    | 33 => "tDDiAtBthhiiiAthhii"
    | 51 => "tDDiAtBththhibiDi"
    | 57 => "tDDiAtBthhhhiDii"
    | 69 => "thhiBttDDiatttDDibi"
    | 75 => "tDDiDiBtthhthhiDi"
    | 87 => "tDDiAttthhiDiiDiDiBtthhhhi"
    | 93 => "tDDiDiBtthhBthhiii"
    | 105 => "tDDiAtBthhhhiDii"
    | 111 => "tBthhiDDi"
    | 129 => "tDDiDiBtthhiAthhii"
    | 141 => "tDDiAtBthhiiBthhiii"
    | _ => ""
  | .both, 864, b => match b with
    | 39 => "aDiBtthhtDDi"
    | 123 => "bthAthhiBtDDiDi"
    | 183 => "ttthhiDDDi"
    | 267 => "tBtthhiDiDi"
    | 327 => "aDiAtthhtDDi"
    | 411 => "bthAthhiBtDDiDi"
    | 471 => "ttthhiDDDi"
    | 555 => "tBtthhiDiDi"
    | 615 => "aDDDiAtBthhhAthhiibtDDi"
    | 699 => "bthAthhiBtDDiDi"
    | 759 => "ttthhiDDDi"
    | 843 => "tBtthhiDiDi"
    | _ => ""
  | _, _, _ => ""

private def dropRow (m : Mode) (r : Row) : Bool :=
  match word m (route m r.1 r.2).toList r with
  | some q => decide (q.1 ≤ r.1 ∧ 0 < q.2 ∧ q.2 < r.2)
  | none => false

private def child (r : Row) (k i : Nat) : Row := (r.1*k,r.1*i+r.2)

private def covered (m : Mode) : List Nat → Row → Bool
  | [], r => dropRow m r
  | k::ks, r => dropRow m r || (decide (0 < k) &&
      (List.range k).all (fun i => covered m ks (child r k i)))

private theorem dropSound (m : Mode) (P : Nat → Prop) (inv : ∀ n, P n ↔ P (T n))
    (jump : Law m P) (r : Row)
    (done : dropRow m r = true) (t : Nat) :
    ∃ z, 0 < z ∧ z < eval r t ∧ (P z → P (eval r t)) := by
  unfold dropRow at done
  cases ew : word m (route m r.1 r.2).toList r with
  | none => simp [ew] at done
  | some q =>
    simp [ew] at done
    obtain ⟨slope,pos,base⟩ := done
    refine ⟨eval q t, ?_, ?_, wordSound m P inv jump _ _ _ ew t⟩
    · unfold eval; omega
    · have := Nat.mul_le_mul_right t slope
      unfold eval
      omega

private theorem coverSound (m : Mode) (P : Nat → Prop) (inv : ∀ n, P n ↔ P (T n))
    (jump : Law m P) (ks : List Nat) (r : Row)
    (ok : covered m ks r = true) (t : Nat) :
    ∃ z, 0 < z ∧ z < eval r t ∧ (P z → P (eval r t)) := by
  induction ks generalizing r t with
  | nil => exact dropSound m P inv jump r ok t
  | cons k ks ih =>
    by_cases done : dropRow m r = true
    · exact dropSound m P inv jump r done t
    simp [covered,done] at ok
    obtain ⟨pos,splitOk⟩ := ok
    let i := t % k
    have hi : i < k := Nat.mod_lt t pos
    have key : i + k*(t/k) = t := Nat.mod_add_div t k
    have congr : eval (child r k i) (t/k) = eval r t := by
      unfold eval child
      simp only
      rw [Nat.mul_assoc, ← Nat.add_assoc, ← Nat.mul_add, Nat.add_comm (k*(t/k)) i, key]
    rw [← congr]
    exact ih _ (splitOk i hi) _

theorem upCover : covered .up [16,9] (1,2) = true := by decide +kernel
theorem downCover : covered .down [16,9,6,6,6,6] (1,2) = true := by decide +kernel

private theorem consumer (m : Mode) (ks : List Nat) (cert : covered m ks (1,2) = true)
    (P : Nat → Prop) (one : P 1) (inv : ∀ n, P n ↔ P (T n))
    (jump : Law m P) : ∀ n, 0<n → P n := by
  intro n
  induction n using Nat.strongRecOn with
  | ind n ih =>
    intro pos
    by_cases eq : n = 1
    · simpa [eq] using one
    have h := coverSound m P inv jump _ _ cert (n-2)
    have base : eval (1,2) (n-2) = n := by simp [eval]; omega
    rw [base] at h
    obtain ⟨z,hz,lt,pz⟩ := h
    exact pz (ih z lt hz)

def orbit (n : Nat) : Nat → Nat
  | 0 => n
  | k+1 => orbit (T n) k

def reachesOne (n : Nat) : Prop := ∃ k, orbit n k = 1

private theorem reachesStep (n : Nat) : reachesOne n ↔ reachesOne (T n) := by
  constructor
  · rintro ⟨k,h⟩
    cases k with
    | zero =>
      have hn : n = 1 := h
      subst n
      exact ⟨1, by decide⟩
    | succ k => exact ⟨k,h⟩
  · rintro ⟨k,h⟩
    exact ⟨k+1,h⟩

theorem basinIffUnitForward : (∀ n, 0 < n → reachesOne n) ↔ Forward reachesOne := by
  refine ⟨fun all u hu _ => all _ (by omega), ?_⟩
  exact consumer .up _ upCover reachesOne ⟨0,rfl⟩ reachesStep

theorem basinIffUnitReverse : (∀ n, 0 < n → reachesOne n) ↔ Reverse reachesOne := by
  refine ⟨fun all u hu _ => all _ (by omega), ?_⟩
  exact consumer .down _ downCover reachesOne ⟨0,rfl⟩ reachesStep

private def pairRow (r : Row) : Bool :=
  word .both (route .both r.1 r.2).toList r == some (3*r.1,3*r.2)

private def paired : List Nat → Row → Bool
  | [], r => pairRow r
  | k::ks, r => pairRow r || (decide (0<k) &&
      (List.range k).all (fun i => paired ks (child r k i)))

theorem pairedCover : paired [9,8,6] (2,1) = true := by decide +kernel

private theorem pairRowSound (P : Nat → Prop) (inv : ∀ n, P n ↔ P (T n))
    (jump : Law .both P) (r : Row) (d : pairRow r = true) (t : Nat) :
    P (3*eval r t) → P (eval r t) := by
  have w : word .both (route .both r.1 r.2).toList r = some (3*r.1,3*r.2) := by
    simpa [pairRow] using d
  have e : eval (3*r.1,3*r.2) t = 3*eval r t := by simp [eval]; ring
  simpa only [e] using wordSound .both P inv jump _ _ _ w t

private theorem pairedSound (P : Nat → Prop) (inv : ∀ n, P n ↔ P (T n))
    (jump : Law .both P) (ks : List Nat) (r : Row) (ok : paired ks r = true) (t : Nat) :
    P (3*eval r t) → P (eval r t) := by
  induction ks generalizing r t with
  | nil => exact pairRowSound P inv jump r ok t
  | cons k ks ih =>
    by_cases done : pairRow r = true
    · exact pairRowSound P inv jump r done t
    simp [paired,done] at ok
    obtain ⟨pos,splitOk⟩ := ok
    let i := t % k
    have hi : i < k := Nat.mod_lt t pos
    have key : i + k*(t/k) = t := Nat.mod_add_div t k
    have cong : eval (child r k i) (t/k) = eval r t := by
      unfold eval child
      simp only
      rw [Nat.mul_assoc, ← Nat.add_assoc, ← Nat.mul_add, Nat.add_comm (k*(t/k)) i, key]
    rw [← cong]
    exact ih _ (splitOk i hi) _

theorem allOddPairs {α : Type} (f : Nat → α) (inv : ∀ n, f n = f (T n))
    (units : ∀ u, u%3 ≠ 0 → f u = f (3*u)) (t : Nat) : f (2*t+1) = f (3*(2*t+1)) := by
  let P := fun n => f n = f (3*(2*t+1))
  have ip (n : Nat) : P n ↔ P (T n) := by dsimp [P]; rw [inv n]
  have laws : Law .both P := by
    constructor
    · intro u hu; dsimp [P]; rw [units u hu]; exact id
    · intro u hu; dsimp [P]; rw [units u hu]; exact id
  have v := pairedSound P ip laws _ _ pairedCover t
  exact v rfl

private theorem dyadic (k u : Nat) : reachesOne (2^k*u) ↔ reachesOne u := by
  induction k with
  | zero => simp
  | succ k ih =>
    have h : T (2^(k+1)*u) = 2^k*u := by
      rw [show 2^(k+1)*u = 2*(2^k*u) by ring]
      unfold T; split <;> omega
    exact ((h ▸ reachesStep (2^(k+1)*u))).trans ih

private theorem fromOddUnits (P : Nat → Prop) (even : ∀ n, P (2*n) ↔ P n)
    (odd : ∀ u, u%2=1 → u%3≠0 → P u) (u : Nat) (hu : u%3≠0) : P u := by
  induction u using Nat.strong_induction_on with
  | h u ih =>
    by_cases h : u%2=1
    · exact odd u h hu
    · have e : u=2*(u/2) := by omega
      have lower := ih (u/2) (by omega) (by omega)
      have z : P (2*(u/2)) := (even (u/2)).mpr lower
      rw [← e] at z
      exact z

private theorem twice (n : Nat) : reachesOne (2*n) ↔ reachesOne n := by
  simpa using dyadic 1 n

theorem basinIffOddUnitForward : (∀ n, 0<n → reachesOne n) ↔
    (∀ u, u%2=1 → u%3≠0 → reachesOne u → reachesOne (3*u)) := by
  refine ⟨fun all u _ hu => basinIffUnitForward.mp all u hu, ?_⟩
  intro H
  apply basinIffUnitForward.mpr
  apply fromOddUnits _ _ H
  intro n
  rw [show 3*(2*n)=2*(3*n) by ring,twice,twice]

theorem basinIffOddUnitReverse : (∀ n, 0<n → reachesOne n) ↔
    (∀ u, u%2=1 → u%3≠0 → reachesOne (3*u) → reachesOne u) := by
  refine ⟨fun all u _ hu => basinIffUnitReverse.mp all u hu, ?_⟩
  intro H
  apply basinIffUnitReverse.mpr
  apply fromOddUnits _ _ H
  intro n
  rw [show 3*(2*n)=2*(3*n) by ring,twice,twice]

theorem exactHead57 (u k v : Nat) (hv : 27*v=2^k*u+1) :
    (reachesOne (8*v-1) ↔ reachesOne u) ∧
    (reachesOne (81*(8*v-1)+57) ↔ reachesOne (3*u)) := by
  have pos : 0<v := by omega
  have s₁ : T (8*v-1) = 12*v-1 := by unfold T; split <;> omega
  have s₂ : T (12*v-1) = 18*v-1 := by unfold T; split <;> omega
  have s₃ : T (18*v-1) = 2^k*u := by unfold T; split <;> omega
  have childEq : 81*(8*v-1)+57 = 2^(k+3)*(3*u) := by
    rw [show 2^(k+3)*(3*u) = 24*(2^k*u) by ring]; omega
  exact ⟨(s₁ ▸ reachesStep _).trans ((s₂ ▸ reachesStep _).trans
      ((s₃ ▸ reachesStep _).trans (dyadic k u))), childEq ▸ dyadic (k+3) (3*u)⟩

set_option format.width 220
#print axioms upCover
#print axioms downCover
#print axioms pairedCover
#print axioms basinIffUnitForward
#print axioms basinIffUnitReverse
#print axioms basinIffOddUnitForward
#print axioms basinIffOddUnitReverse
#print axioms allOddPairs
#print axioms exactHead57

end UnitTripling
