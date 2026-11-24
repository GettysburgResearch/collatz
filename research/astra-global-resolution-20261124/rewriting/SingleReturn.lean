import Std

namespace SingleReturn

def T (n : Nat) : Nat := if n % 2 = 0 then n/2 else (3*n+1)/2

private structure Rule where
  i : Nat
  j : Nat
  k : Nat
  l : Nat
deriving DecidableEq, Repr

private def rules : Char → Rule
  | 'h' => ⟨2,0,1,0⟩
  | 'D' => ⟨1,0,2,0⟩
  | 't' => ⟨2,1,3,2⟩
  | 'i' => ⟨3,2,2,1⟩
  | 'S' => ⟨8,7,9,8⟩
  | _   => ⟨1,0,1,0⟩

private theorem ruleSound (P : Nat → Prop) (inv : ∀ n, P n ↔ P (T n))
    (jump : ∀ n, P (9*n+8) → P (8*n+7)) (c : Char) (n : Nat) :
    P ((rules c).k*n+(rules c).l) → P ((rules c).i*n+(rules c).j) := by
  have even : P (2*n) ↔ P n := by
    have z : T (2*n) = n := by unfold T; split <;> omega
    simpa [z] using inv (2*n)
  have odd : P (2*n+1) ↔ P (3*n+2) := by
    have z : T (2*n+1) = 3*n+2 := by unfold T; split <;> omega
    simpa [z] using inv (2*n+1)
  unfold rules
  split <;> simp only [Nat.one_mul, Nat.add_zero] <;>
    first | exact even.mp | exact even.mpr | exact odd.mp | exact odd.mpr
          | exact jump n | exact id

private abbrev Row := Nat × Nat
private def eval (r : Row) (t : Nat) := r.1*t+r.2

private def applyRule (g : Rule) (r : Row) : Option Row :=
  let a := r.1/g.i
  let b := r.2/g.i
  if r.1 = g.i*a ∧ r.2 = g.i*b+g.j then
    some (g.k*a,g.k*b+g.l)
  else none

private theorem applySound (P : Nat → Prop) (inv : ∀ n, P n ↔ P (T n))
    (jump : ∀ n, P (9*n+8) → P (8*n+7)) (c : Char) (r q : Row)
    (ok : applyRule (rules c) r = some q) (t : Nat) :
    P (eval q t) → P (eval r t) := by
  generalize eq : rules c = g at ok
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
    have step := ruleSound P inv jump c ((r.1/g.i)*t+(r.2/g.i))
    rw [eq] at step
    simpa [eval, Nat.mul_add, Nat.mul_assoc, Nat.add_assoc] using step
  next => contradiction

private def word : List Char → Row → Option Row
  | [], r => some r
  | c::cs, r => (applyRule (rules c) r).bind (word cs)

private theorem wordSound (P : Nat → Prop) (inv : ∀ n, P n ↔ P (T n))
    (jump : ∀ n, P (9*n+8) → P (8*n+7)) (w : List Char) (r q : Row)
    (ok : word w r = some q) (t : Nat) : P (eval q t) → P (eval r t) := by
  induction w generalizing r with
  | nil =>
    exact Option.some.inj ok ▸ id
  | cons c cs ih =>
    cases e : applyRule (rules c) r with
    | none => simp [word,e] at ok
    | some v =>
      have wv : word cs v = some q := by simpa [word,e] using ok
      exact fun h => applySound P inv jump c r v e t (ih v wv h)

-- Each row (a,b) represents all a*t+b, t ≥ 0.
private def route : Nat → Nat → String
  | 32, b => match b with
    | 2 => "h"
    | 3 => "tthh"
    | 4 => "h"
    | 5 => "th"
    | 6 => "h"
    | 7 => "Sh"
    | 8 => "h"
    | 9 => "th"
    | 10 => "h"
    | 11 => "tthth"
    | 12 => "h"
    | 13 => "th"
    | 14 => "h"
    | 15 => "Si"
    | 16 => "h"
    | 17 => "th"
    | 18 => "h"
    | 19 => "tthh"
    | 20 => "h"
    | 21 => "th"
    | 22 => "h"
    | 23 => "Sh"
    | 24 => "h"
    | 25 => "th"
    | 26 => "h"
    | 28 => "h"
    | 29 => "th"
    | 30 => "h"
    | 31 => "Si"
    | 32 => "h"
    | 33 => "th"
    | _ => ""
  | 576, b => match b with
    | 27 => "tthSi"
    | 59 => "i"
    | 91 => "tthSi"
    | 155 => "i"
    | 219 => "tthSi"
    | 251 => "i"
    | 283 => "Dii"
    | 347 => "i"
    | 411 => "tthSi"
    | 443 => "i"
    | 475 => "tthSi"
    | 539 => "i"
    | 571 => "Dii"
    | _ => ""
  | 6912, b => match b with
    | 123 => "tthtthth"
    | 187 => "tthtthh"
    | 315 => "tthtthh"
    | 379 => "tthtthth"
    | 699 => "tthtthh"
    | 891 => "tthtthth"
    | 955 => "tthtthh"
    | 1083 => "tthtthh"
    | 1275 => "tthtDDiiiDiiiSh"
    | 1339 => "tthtthh"
    | 1467 => "tthtthh"
    | 1659 => "tthtthth"
    | 1851 => "tthtthh"
    | 1915 => "tthtthth"
    | 2107 => "tthtthh"
    | 2235 => "tthtthh"
    | 2427 => "tthtthth"
    | 2491 => "tthtthh"
    | 2619 => "tthtthh"
    | 2683 => "tthtthth"
    | 2811 => "tDDiDiiiShh"
    | 3003 => "tthtthh"
    | 3195 => "tthtthth"
    | 3259 => "tthtthh"
    | 3387 => "tthtthh"
    | 3643 => "tthtthh"
    | 3771 => "tthtthh"
    | 3835 => "tthtDDiiDDiDiiiShhh"
    | 3963 => "tthtthth"
    | 4155 => "tthtthh"
    | 4219 => "tthtthth"
    | 4411 => "tthtthh"
    | 4539 => "tthtthh"
    | 4731 => "tthtthth"
    | 4795 => "tthtthh"
    | 4923 => "tthtthh"
    | 4987 => "tthtthth"
    | 5307 => "tthtthh"
    | 5499 => "tthtthth"
    | 5563 => "tthtthh"
    | 5691 => "tthtthh"
    | 5947 => "tthtthh"
    | 6075 => "tthtthh"
    | 6139 => "ttDDDDiDiDiiiShhhhh"
    | 6267 => "tthtthth"
    | 6459 => "tthtthh"
    | 6523 => "tthtthth"
    | 6715 => "tthtthh"
    | 6843 => "tthtthh"
    | _ => ""
  | 82944, b => match b with
    | 507 => "tthtthtthh"
    | 763 => "tthtthSh"
    | 1531 => "tthtthtthh"
    | 2043 => "tthtthtDDiiDDiDiDiiiShhhh"
    | 3579 => "tthtthtthh"
    | 4347 => "tthtthSi"
    | 5115 => "tthtDDiiDDiiDiiiShh"
    | 5371 => "tthtthSi"
    | 5883 => "tthtthSh"
    | 6651 => "tthtthtthh"
    | 7419 => "tthtthSi"
    | 7675 => "tthtthtthh"
    | 8443 => "tthtthSi"
    | 8955 => "tthtthSh"
    | 9979 => "tthtthSh"
    | 10491 => "tthtthSi"
    | 11259 => "tthtthtDDiiDDiDiDiiiShhhh"
    | 12027 => "tthtthSh"
    | 12795 => "tthtthtthh"
    | 13563 => "tthtthSi"
    | 14587 => "tthtthSi"
    | 15355 => "tthtthtDDiDDDDiDiiiShhiDiiiShhh"
    | 15867 => "tthtthtthh"
    | 16891 => "tthtthtthh"
    | 17403 => "tthttDDDDiDiDiDiiiShhhhhh"
    | 18171 => "tthtthSh"
    | 18939 => "tthtthtthh"
    | 19195 => "tthtthSh"
    | 19707 => "tthtthSi"
    | 20475 => "tDDiDiDiiiShh"
    | 21243 => "tthtthSh"
    | 21499 => "tDDDDDDiDiDiiiShhhhhthh"
    | 22267 => "tthtthSh"
    | 22779 => "tthtthSi"
    | 23803 => "tthtthSi"
    | 24315 => "tthtthSh"
    | 25083 => "tthtthtthh"
    | 25851 => "tthtthSi"
    | 26107 => "tthtthtthh"
    | 26619 => "tthttDDDDiDiDiDiiiShhhhhh"
    | 27387 => "tthtthSh"
    | 28155 => "tthtthtthh"
    | 28411 => "tthtthSh"
    | 29179 => "tthtthtthh"
    | 29691 => "tthtDDiiiDiDiiiSh"
    | 30715 => "tthtDDiDDDDiDiiDiiiShhSiiiShh"
    | 31227 => "tthtthtthh"
    | 31995 => "tthtthSi"
    | 33019 => "tthtthSi"
    | 33531 => "tthtthSh"
    | 34299 => "tthtthtthh"
    | 35067 => "tthtthSi"
    | 35323 => "tthtthtthh"
    | 36091 => "tthtthSi"
    | 36603 => "tthtthSh"
    | 37627 => "tthtthSh"
    | 38139 => "tthtthSi"
    | 38907 => "tthtthtDDiiDDiDiDiiiShhhh"
    | 39675 => "tthtthSh"
    | 40443 => "tthtthtthh"
    | 41211 => "tthtthSi"
    | 41979 => "tthtDDiiiDDDiDiiiShhh"
    | 42235 => "tthtthSi"
    | 43003 => "tthtthtDDiDDDDiDiiiShhiDiiiShhh"
    | 43515 => "tthtthtthh"
    | 44539 => "tthtthtthh"
    | 45051 => "tthttDDDDiDiDiDiiiShhhhhh"
    | 45819 => "tthtthSh"
    | 46587 => "tthtthtthh"
    | 46843 => "tthtthSh"
    | 47355 => "tthtthSi"
    | 48123 => "tthtthtDDiiDDiDiDiiiShhhh"
    | 48891 => "tthtthSh"
    | 49147 => "ttDDDDiDDDiiDiiiShhiShhhh"
    | 49915 => "tthtthSh"
    | 50427 => "tthtthSi"
    | 51451 => "tthtthSi"
    | 51963 => "tthtthSh"
    | 52731 => "tthtthtthh"
    | 53499 => "tthtthSi"
    | 53755 => "tthtthtthh"
    | 54267 => "tthttDDDDiDiDiDiiiShhhhhh"
    | 55035 => "tthtthSh"
    | 55803 => "tthtthtthh"
    | 56059 => "tthtthSh"
    | 56827 => "tthtthtthh"
    | 57339 => "tthtthtDDiiDDiDiDiiiShhhh"
    | 58363 => "DDDiDiiiShh"
    | 58875 => "tthtthtthh"
    | 59643 => "tthtthSi"
    | 60411 => "tthtthtDDiiDDiDiDiiDiiiShhShh"
    | 60667 => "tthtthSi"
    | 61179 => "tthtthSh"
    | 61947 => "tthtthtthh"
    | 62715 => "tthtthSi"
    | 62971 => "tthtthtthh"
    | 63739 => "tthtthSi"
    | 64251 => "tthtthSh"
    | 65275 => "tthtthSh"
    | 65787 => "tthtthSi"
    | 66555 => "tthtthtDDiiDDiDiDiiiShhhh"
    | 67323 => "tthtthSh"
    | 67579 => "tDDiiDiiiSh"
    | 68091 => "tthtthtthh"
    | 68859 => "tthtthSi"
    | 69883 => "tthtthSi"
    | 70651 => "tthtthtDDiDDDDiDiiiShhiDiiiShhh"
    | 71163 => "tthtthtthh"
    | 72187 => "tthtthtthh"
    | 72699 => "tthttDDDDiDiDiDiiiShhhhhh"
    | 73467 => "tthtthSh"
    | 74235 => "tthtthtthh"
    | 74491 => "tthtthSh"
    | 75003 => "tthtthSi"
    | 75771 => "tthtthtDDiiDDiDiDiiiShhhh"
    | 76539 => "tthtthSh"
    | 76795 => "tthtthtDDiDDDDiDiiiiDiiiShhthhi"
    | 77563 => "tthtthSh"
    | 78075 => "tthtthSi"
    | 79099 => "tthtthSi"
    | 79611 => "tthtthSh"
    | 80379 => "tthtthtthh"
    | 81147 => "tthtthSi"
    | 81403 => "tthtthtthh"
    | 81915 => "tthttDDDDiDiDiDiiiShhhhhh"
    | 82683 => "tthtthSh"
    | _ => ""
  | 995328, b => match b with
    | 3067 => "DDDDDiDDDDiDiiiShhhtttthththhthhShhi"
    | 12283 => "tthtthtDDiDDDDiDiiiShhiDiiDiiiShh"
    | 14331 => "tthtthtthSii"
    | 32763 => "tDDiDiiDiiiShh"
    | 39931 => "tthtthtDDiDDDDiDiiiiDiDiiiShhhhi"
    | 69627 => "tthtDDiiDDiiDDDiDiiiShhhtthhi"
    | 86011 => "tthtthtDDDDDDDDiiDiiiShhiDiDiiiShhhhi"
    | 95227 => "tthtthtththh"
    | 97275 => "tthtthtDDiiDDiDDDiiDDiDiiiShhhthhiShh"
    | 115707 => "tthtthtththh"
    | 122875 => "tthtthttDDDDDDiDDiDiiDiiiShhSiiiShhhhh"
    | 152571 => "tthtthtththh"
    | 168955 => "tthtthtththh"
    | 178171 => "tthtthtthSii"
    | 180219 => "tthtDDiiDDiDDiiDiiiShhiSh"
    | 198651 => "tthtthtthSii"
    | 205819 => "tthtthtththh"
    | 235515 => "tthtthtthSii"
    | 251899 => "tthtthtthSii"
    | 261115 => "tthtthtDDiDDDDiDiiiShhiDiiDiiiShh"
    | 263163 => "tthtthtththh"
    | 281595 => "tDDiDiiDiiiShh"
    | 288763 => "tthtthtthSii"
    | 318459 => "tthtDDiiDDiiDDDiDiiiShhhtthhi"
    | 334843 => "tthtthtDDDDDDDDiiDiiiShhiDiDiiiShhhhi"
    | 344059 => "tthtDDiDDDDiDiiDiDiiiShhhhthh"
    | 346107 => "tthtthtthSii"
    | 364539 => "tDDDDiDDDDiDiiiShhhtttththtthhhthhiSii"
    | 371707 => "tthtthttDDDDDDiDDiDiiDiiiShhSiiiShhhhh"
    | 401403 => "tDDDDiDDDDiDiDiiiShhhhhthhh"
    | 417787 => "tDDiDDiiDiiiShhi"
    | 427003 => "tthtthtththh"
    | 429051 => "tthtDDiiDDiDDiiDiiiShhiSh"
    | 447483 => "tthtthtththh"
    | 454651 => "tDDiDDiDDDDiDiiiShhhtttthSiiShhhh"
    | 484347 => "tthtthtththh"
    | 500731 => "tthtthtththh"
    | 509947 => "tthtthtthSii"
    | 511995 => "tDDDDiiiDiiiShhi"
    | 530427 => "tthtthtthSii"
    | 537595 => "tthtthtththh"
    | 567291 => "tthtthtthSii"
    | 583675 => "tthtthtthSii"
    | 592891 => "tthtDDiDDDDiDiiDiDiiiShhhhthh"
    | 594939 => "tthtthtththh"
    | 613371 => "tDDDDiDDDDiDiiiShhhtttththtthhhthhSiii"
    | 620539 => "tthtthtthSii"
    | 650235 => "tDDDDiDDDDiDiDiiiShhhhhthhh"
    | 666619 => "tDDiDDiiDiiiShhi"
    | 675835 => "tDDDDDDiDiDiDiiiShhhhhhh"
    | 677883 => "tthtthtthSii"
    | 696315 => "tDDDDiDDDDiDiiiShhhtttththtthhhthhiSii"
    | 703483 => "tDDiDDiDDDDiDiiiShhhtttthSiiShhhh"
    | 733179 => "ttDDDDiDiDDiDiDiiiShhhhhtthhi"
    | 749563 => "DDDDDiDDDDiDiiiShhhtttthththhthhShhi"
    | 758779 => "tthtthtththh"
    | 760827 => "tDDDDiiiDiiiShhi"
    | 779259 => "tthtthtththh"
    | 786427 => "tthtthtDDiDDDDiDiiiiDiDiiiShhhhi"
    | 816123 => "tthtthtththh"
    | 832507 => "tthtthtththh"
    | 841723 => "tthtthtthSii"
    | 843771 => "tthtthtDDiiDDiDDDiiDDiDiiiShhhthhiShh"
    | 862203 => "tthtthtthSii"
    | 869371 => "tthtthtththh"
    | 899067 => "tthtthtthSii"
    | 915451 => "tthtthtthSii"
    | 924667 => "tDDDDDDiDiDiDiiiShhhhhhh"
    | 926715 => "tthtthtththh"
    | 945147 => "tDDDDiDDDDiDiiiShhhtttththtthhhthhSiii"
    | 952315 => "tthtthtthSii"
    | 982011 => "ttDDDDiDiDDiDiDiiiShhhhhtthhi"
    | _ => ""
  | _, _ => ""

private def dropRow (r : Row) : Bool :=
  match word (route r.1 r.2).toList r with
  | some q => decide (q.1 ≤ r.1 ∧ 0 < q.2 ∧ q.2 < r.2)
  | none => false

private def child (r : Row) (k i : Nat) : Row := (r.1*k,r.1*i+r.2)

private def covered : List Nat → Row → Bool
  | [], r => dropRow r
  | k::ks, r => dropRow r || (decide (0 < k) &&
      (List.range k).all (fun i => covered ks (child r k i)))

private theorem dropSound (P : Nat → Prop) (inv : ∀ n, P n ↔ P (T n))
    (jump : ∀ n, P (9*n+8) → P (8*n+7)) (r : Row)
    (done : dropRow r = true) (t : Nat) :
    ∃ z, 0 < z ∧ z < eval r t ∧ (P z → P (eval r t)) := by
  unfold dropRow at done
  cases ew : word (route r.1 r.2).toList r with
  | none => simp [ew] at done
  | some q =>
    simp [ew] at done
    obtain ⟨slope,pos,base⟩ := done
    refine ⟨eval q t, ?_, ?_, wordSound P inv jump _ _ _ ew t⟩
    · unfold eval; omega
    · have := Nat.mul_le_mul_right t slope
      unfold eval
      omega

private theorem coverSound (P : Nat → Prop) (inv : ∀ n, P n ↔ P (T n))
    (jump : ∀ n, P (9*n+8) → P (8*n+7)) (ks : List Nat) (r : Row)
    (ok : covered ks r = true) (t : Nat) :
    ∃ z, 0 < z ∧ z < eval r t ∧ (P z → P (eval r t)) := by
  induction ks generalizing r t with
  | nil => exact dropSound P inv jump r ok t
  | cons k ks ih =>
    by_cases done : dropRow r = true
    · exact dropSound P inv jump r done t
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

private theorem finiteCover : covered [32,18,12,12,12] (1,2) = true := by
  decide +kernel

/-- A one-sided implication across the three-step first return of 7(8u+7)
    to a multiple of seven suffices at every positive n. -/
theorem singleReturnCover (P : Nat → Prop) (one : P 1) (inv : ∀ n, P n ↔ P (T n))
    (jump : ∀ u, P (9*u+8) → P (8*u+7)) : ∀ n, 0 < n → P n := by
  intro n
  induction n using Nat.strongRecOn with
  | ind n ih =>
    intro pos
    by_cases eq : n = 1
    · simpa [eq] using one
    have h := coverSound P inv jump _ _ finiteCover (n-2)
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

theorem collatzIffSingleReturn : (∀ n, 0 < n → reachesOne n) ↔
    (∀ u, reachesOne (9*u+8) → reachesOne (8*u+7)) := by
  constructor
  · intro all u _
    exact all _ (by omega)
  · exact singleReturnCover reachesOne ⟨0,rfl⟩ reachesStep

end SingleReturn
namespace SingleReturn

private def childTest (P : Nat → Prop) (r : Nat) :=
  P (9*r-1) → P (18*r-1)

private theorem exchange (P : Nat → Prop) (inv : ∀ n, P n ↔ P (T n))
    (s : Nat) (hs : s > 0) : childTest P (2*s) ↔ childTest P (3*s) := by
  have a : T (9*(2*s)-1) = 9*(3*s)-1 := by unfold T; split <;> omega
  have b : T (18*(2*s)-1) = 18*(3*s)-1 := by unfold T; split <;> omega
  have h₁ := inv (9*(2*s)-1)
  have h₂ := inv (18*(2*s)-1)
  rw [a] at h₁
  rw [b] at h₂
  exact ⟨fun h x => h₂.mp (h (h₁.mpr x)), fun h x => h₂.mpr (h (h₁.mp x))⟩

private theorem oddCore (P : Nat → Prop) (inv : ∀ n, P n ↔ P (T n))
    (core : ∀ k, P (36*k+8) → P (72*k+17)) (r : Nat) (odd : r%2=1) :
    childTest P r := by
  let k := r/4
  by_cases h : r%4=1
  · have a : 9*r-1 = 36*k+8 := by dsimp [k]; omega
    have b : 18*r-1 = 72*k+17 := by dsimp [k]; omega
    simpa [childTest,a,b] using core k
  · have a : 9*r-1 = 36*k+26 := by dsimp [k]; omega
    have b : 18*r-1 = 72*k+53 := by dsimp [k]; omega
    have s₁ : T (36*k+26) = 18*k+13 := by unfold T; split <;> omega
    have s₂ : T (18*k+13) = 27*k+20 := by unfold T; split <;> omega
    have t₁ : T (72*k+53) = 108*k+80 := by unfold T; split <;> omega
    have t₂ : T (108*k+80) = 54*k+40 := by unfold T; split <;> omega
    have t₃ : T (54*k+40) = 27*k+20 := by unfold T; split <;> omega
    have left : P (36*k+26) ↔ P (27*k+20) :=
      (s₁ ▸ inv (36*k+26)).trans (s₂ ▸ inv (18*k+13))
    have right : P (72*k+53) ↔ P (27*k+20) :=
      (t₁ ▸ inv (72*k+53)).trans ((t₂ ▸ inv (108*k+80)).trans (t₃ ▸ inv (54*k+40)))
    unfold childTest
    rw [a,b]
    exact fun x => right.mpr (left.mp x)

private theorem allChildren (P : Nat → Prop) (inv : ∀ n, P n ↔ P (T n))
    (core : ∀ k, P (36*k+8) → P (72*k+17)) (a b : Nat)
    (ha : 0<a) (odd : b%2=1) : childTest P (a*b) := by
  induction a using Nat.strongRecOn generalizing b with
  | ind a ih =>
    by_cases h : a%2=0
    · let d := a/2
      have ad : a = 2*d := by dsimp [d]; omega
      have hd : 0<d := by dsimp [d]; omega
      have lt : d<a := by dsimp [d]; omega
      have odd' : (3*b)%2=1 := by omega
      have inner := ih d lt (3*b) hd odd'
      have rearr : d*(3*b) = 3*(d*b) := by ac_rfl
      rw [rearr] at inner
      rw [ad,Nat.mul_assoc]
      exact (exchange P inv (d*b) (Nat.mul_pos hd (by omega))).mpr inner
    · apply oddCore P inv core
      have aodd : a%2=1 := by omega
      simp [Nat.mul_mod,aodd,odd]

/-- Only the even antecedents 8 modulo 36 of the ordinary binary-child
    implication remain after following the all-odd prefix and its sibling. -/
theorem collatzIffEvenChild : (∀ n, 0 < n → reachesOne n) ↔
    (∀ k, reachesOne (36*k+8) → reachesOne (72*k+17)) := by
  constructor
  · intro all k _
    exact all _ (by omega)
  · intro core
    apply collatzIffSingleReturn.mpr
    intro u hu
    have child := allChildren reachesOne reachesStep core (u+1) 1 (by omega) (by decide)
    have a : 9*((u+1)*1)-1 = 9*u+8 := by omega
    have b : 18*((u+1)*1)-1 = 18*u+17 := by omega
    unfold childTest at child
    rw [a,b] at child
    have t₁ : T (8*u+7) = 12*u+11 := by unfold T; split <;> omega
    have t₂ : T (12*u+11) = 18*u+17 := by unfold T; split <;> omega
    exact ((t₁ ▸ reachesStep (8*u+7)).trans (t₂ ▸ reachesStep (12*u+11))).mpr (child hu)

end SingleReturn
