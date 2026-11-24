import Mathlib.Data.Nat.ModEq
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Data.Nat.GCD.Basic

namespace Collatz.PaidRenewal

def step (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else (3*n+1)/2

def run : ℕ → ℕ → ℕ
  | 0, n => n
  | k+1, n => run k (step n)

def odds : ℕ → ℕ → ℕ
  | 0, _ => 0
  | k+1, n => n%2 + odds k (step n)

theorem run_add (a b n : ℕ) : run (a+b) n = run b (run a n) := by
  induction a generalizing n with
  | zero => simp [run]
  | succ a ih => simpa [Nat.succ_add, run] using ih (step n)

private theorem step_lift (t b : ℕ) :
    step (2*t+b) = 3^(b%2)*t + step b := by
  by_cases h : b%2=0
  · simp [step, h, Nat.add_mod]; omega
  · have h' : b%2=1 := by omega
    simp [step, h', Nat.add_mod]; omega

theorem cylinder (k t b : ℕ) :
    run k (2^k*t+b) = 3^(odds k b)*t + run k b := by
  induction k generalizing t b with
  | zero => simp [odds, run]
  | succ k ih =>
    rw [run, show 2^(k+1)*t+b = 2*(2^k*t)+b by ring, step_lift]
    rw [show 3^(b%2)*(2^k*t)=2^k*(3^(b%2)*t) by ring, ih]
    simp only [odds, run, pow_add]
    ring

inductive Letter where | L | P deriving DecidableEq, Repr
open Letter
def width : Letter → ℕ | L => 3 | P => 5
def injection : Letter → ℕ | L => 0 | P => 83

/-- x = (q+7)/2, where q is the original positive odd boundary. -/
inductive Path : List Letter → ℕ → ℕ → Prop
  | nil (x) : Path [] x x
  | cons {a w x y z} (edge : 2^(width a)*y = 9*x+injection a)
      (tail : Path w y z) : Path (a::w) x z

def clock : List Letter → ℕ
  | [] => 0
  | a::w => width a + clock w

def carry : List Letter → ℕ
  | [] => 0
  | a::w => 9^w.length*injection a + 2^(width a)*carry w

theorem affine {w x z} (hp : Path w x z) :
    2^(clock w)*z = 9^w.length*x + carry w := by
  induction hp with
  | nil => simp [clock, carry]
  | @cons a w x y z edge _ ih =>
    simp only [clock, carry, List.length_cons, pow_add, pow_succ]
    calc
      2^(width a)*2^(clock w)*z = 2^(width a)*(2^(clock w)*z) := by ring
      _ = 2^(width a)*(9^w.length*y+carry w) := by rw [ih]
      _ = 9^w.length*(2^(width a)*y)+2^(width a)*carry w := by ring
      _ = _ := by rw [edge]; ring

/-- Both residue equations below are decidable integer identities on one
canonical cylinder representative. The parameter t for all lifts is derived. -/
structure Certificate (w : List Letter) (a b : ℕ) where
  base : ℕ
  endpoint : ℕ
  base_lt : base < 2^(clock w)
  source : 2^(clock w)*endpoint = 9^w.length*base + carry w
  source_ge : a ≤ base
  target_ge : b ≤ endpoint
  weight : 3^(odds (clock w) (base-a)) = 9^w.length
  returns : run (clock w) (base-a)+b = endpoint

theorem certified {w a b x z} (c : Certificate w a b) (hp : Path w x z) :
    run (clock w) (x-a)+b = z := by
  have h := affine hp
  let M := 2^(clock w)
  let S := 9^w.length
  have co : Nat.Coprime M S := by
    dsimp [M,S]
    exact ((show Nat.Coprime 2 9 by decide).pow_left _).pow_right _
  have hm : 0 < M := by dsimp [M]; positivity
  have ebase : M*c.endpoint = S*c.base + carry w := c.source
  have he : M*z = S*x + carry w := h
  have modEq : x ≡ c.base [MOD M] := by
    apply Nat.ModEq.cancel_left_of_coprime co
    show (S*x)%M=(S*c.base)%M
    have a1 : (S*x+carry w)%M=(S*c.base+carry w)%M := by
      rw [← he, ← ebase]; simp
    exact Nat.ModEq.add_right_cancel' (carry w) a1
  have residue : x % M = c.base := Eq.trans (show x%M=c.base%M from modEq) (Nat.mod_eq_of_lt c.base_lt)
  let t := x/M
  have hx : x = M*t+c.base := by
    dsimp [t]; have hd := Nat.mod_add_div x M; omega
  have hz : z=S*t+c.endpoint := by
    apply Nat.eq_of_mul_eq_mul_left hm
    calc
      M*z = S*x+carry w := he
      _ = S*(M*t+c.base)+carry w := by rw [← hx]
      _ = M*(S*t)+(S*c.base+carry w) := by ring
      _ = M*(S*t+c.endpoint) := by rw [← ebase]; ring
  have hs := c.source_ge
  rw [show x-a=2^(clock w)*t+(c.base-a) by change x-a=M*t+(c.base-a); omega,
    cylinder, c.weight, hz]
  change S*t+run (clock w) (c.base-a)+b=S*t+c.endpoint
  rw [Nat.add_assoc, c.returns]


inductive Mode where | A | B deriving DecidableEq, Repr
def anchor : Mode → ℕ | .A => 10 | .B => 7

inductive Move where
  | light (s : Mode)
  | ab | abShort | ba | bb | aa
  deriving DecidableEq, Repr

def entry : Move → Mode
  | .light s => s
  | .ab | .abShort | .aa => .A
  | .ba | .bb => .B

def exitMode : Move → Mode
  | .light s => s
  | .ab | .abShort | .bb => .B
  | .ba | .aa => .A

def word : Move → List Letter
  | .light _ => [L]
  | .ab => [P,P,L,L,L,P] ++ List.replicate 5 L
  | .abShort => [P,P,L,L,L,L,P] ++ List.replicate 4 L
  | .ba => [P,L,L,P,P,L,P,P] ++ List.replicate 9 L
  | .bb => [P,L,L,P,L,P,P] ++ List.replicate 6 L
  | .aa => [P,L,L,P,L,L,P,L,L,P,P] ++ List.replicate 9 L

private def cert_ab : Certificate (word .ab) 10 7 where
  base := 540692887333
  endpoint := 30863731320
  base_lt := by decide
  source := by decide
  source_ge := by decide
  target_ge := by decide
  weight := by decide
  returns := by decide

private def cert_abShort : Certificate (word .abShort) 10 7 where
  base := 269461403429
  endpoint := 15381345960
  base_lt := by decide
  source := by decide
  source_ge := by decide
  target_ge := by decide
  weight := by decide
  returns := by decide

private def cert_ba : Certificate (word .ba) 7 10 where
  base := 1095898912808651653
  endpoint := 7926170697808848
  base_lt := by decide
  source := by decide
  source_ge := by decide
  target_ge := by decide
  weight := by decide
  returns := by decide

private def cert_bb : Certificate (word .bb) 7 7 where
  base := 127322497043333
  endpoint := 2299577093460
  base_lt := by decide
  source := by decide
  source_ge := by decide
  target_ge := by decide
  weight := by decide
  returns := by decide

private def cert_aa : Certificate (word .aa) 10 10 where
  base := 869810517964567169925
  endpoint := 8957259313560260127
  base_lt := by decide
  source := by decide
  source_ge := by decide
  target_ge := by decide
  weight := by decide
  returns := by decide

private theorem light_return {x z : ℕ} (s : Mode) (hx : 13≤x)
    (eqn : 8*z=9*x) : run 3 (x-anchor s)+anchor s=z := by
  have dvd : 8 ∣ x := (show Nat.Coprime 8 9 by decide).dvd_of_dvd_mul_left ⟨z,eqn.symm⟩
  obtain ⟨t, ht⟩ := dvd
  have hy : 2≤t := by omega
  have h (a : ℕ) (ha : a=7 ∨ a=10) :
      x-a=2^3*(t-2)+(16-a) := by rcases ha with rfl|rfl <;> omega
  cases s
  · rw [show anchor .A=10 by rfl, h 10 (Or.inr rfl), cylinder]
    change 9*(t-2)+8+10=z
    omega
  · rw [show anchor .B=7 by rfl, h 7 (Or.inl rfl), cylinder]
    change 9*(t-2)+11+7=z
    omega

theorem transition {x z : ℕ} (e : Move) (hx : 13≤x) (hp : Path (word e) x z) :
    run (clock (word e)) (x-anchor (entry e))+anchor (exitMode e)=z := by
  cases e with
  | light s =>
    have h := affine hp
    change 8*z=9*x+0 at h
    exact light_return s hx (by omega)
  | ab => exact certified cert_ab hp
  | abShort => exact certified cert_abShort hp
  | ba => exact certified cert_ba hp
  | bb => exact certified cert_bb hp
  | aa => exact certified cert_aa hp

theorem path_append {w v x y z} (h₁ : Path w x y) (h₂ : Path v y z) :
    Path (w++v) x z := by
  induction h₁ with
  | nil => exact h₂
  | cons h _ ih => exact Path.cons h (ih h₂)

private theorem two_large {w x z} (h : Path w x z) (hl : 2≤w.length) (pos : 0<x) :
    13≤x := by
  cases h with
  | nil => simp at hl
  | @cons a w x y z h rest =>
    cases rest with
    | nil => simp at hl
    | @cons b v y u z g _ =>
      cases a <;> cases b <;> norm_num [width, injection] at h g <;> omega

def elapsed (e : ℕ → Move) : ℕ → ℕ
  | 0 => 0
  | i+1 => elapsed e i + clock (word (e i))

private theorem cost_pos (e : Move) : 0 < clock (word e) := by cases e <;> simp [word, clock, width]
private theorem len_pos (e : Move) : 0 < (word e).length := by cases e <;> simp [word]

def Bad (x : ℕ) : Prop := ∀ j, run j x ≠ 1

private theorem trivial_cycle (k : ℕ) (x : ℕ) (hx : x=1 ∨ x=2) :
    run k x=1 ∨ run k x=2 := by
  induction k generalizing x with
  | zero => exact hx
  | succ k ih =>
    apply ih
    rcases hx with rfl|rfl <;> decide

private theorem odd_below {x : ℕ} (h : 0<x) (hb : Bad x) :
    ∃ y, y%2=1 ∧ 0<y ∧ y≤x ∧ Bad y := by
  induction x using Nat.strong_induction_on with
  | h x ih =>
    by_cases he : x%2=0
    · have hs : step x = x/2 := by simp [step,he]
      have h' : Bad (x/2) := by
        intro j hit
        apply hb (j+1)
        simpa [run,hs] using hit
      obtain ⟨y,hy,hp,hle,hb'⟩ := ih (x/2) (by omega) (by omega) h'
      exact ⟨y,hy,hp,by omega,hb'⟩
    · exact ⟨x,by omega,h,by omega,hb⟩

/-- A single initial source shadows every checkpoint of any infinite graph
walk. Positivity of the ordinary coordinates and the raw L/P clock laws
suffice; no certificate or lower bound on target iterates is assumed. -/
theorem persistent_descent (e : ℕ → Move) (x : ℕ → ℕ)
    (chain : ∀ i, exitMode (e i) = entry (e (i+1)))
    (pos : ∀ i, 0<x i)
    (paths : ∀ i, Path (word (e i)) (x i) (x (i+1))) :
    let m := x 0-anchor (entry (e 0))
    (∀ i, run (elapsed e i) m=x i-anchor (entry (e i))) ∧
      Bad m ∧ ∃ y, y%2=1 ∧ 0<y ∧ y<2*x 0-7 ∧
        y<(3*(2*x 0-7)+1)/4 ∧ Bad y := by
  dsimp only
  have big (i) : 13≤x i := by
    apply two_large (path_append (paths i) (paths (i+1))) _ (pos i)
    rw [List.length_append]
    have := len_pos (e i)
    have := len_pos (e (i+1))
    omega
  have small (i) : anchor (entry (e i))=7 ∨ anchor (entry (e i))=10 := by
    cases entry (e i) <;> decide
  have shadow (i) : run (elapsed e i) (x 0-anchor (entry (e 0))) =
      x i-anchor (entry (e i)) := by
    induction i with
    | zero => rfl
    | succ i ih =>
      rw [elapsed, run_add, ih]
      have tr := transition (e i) (big i) (paths i)
      rw [chain i] at tr
      omega
  have growing (i) : i≤elapsed e i := by
    induction i with
    | zero => simp [elapsed]
    | succ i ih =>
      rw [elapsed]
      have := cost_pos (e i)
      omega
  have bad : Bad (x 0-anchor (entry (e 0))) := by
    intro j hit
    have hg := growing j
    have hh := trivial_cycle (elapsed e j-j) 1 (Or.inl rfl)
    have t := shadow j
    rw [show elapsed e j = j+(elapsed e j-j) by omega,run_add, hit] at t
    have := big j
    rcases small j with ha|ha <;> omega
  refine ⟨shadow,bad,?_⟩
  have b := big 0
  obtain ⟨y,hy,hp,hle,hby⟩ := odd_below (x:=x 0-anchor (entry (e 0)))
    (by rcases small 0 with ha|ha <;> omega) bad
  exact ⟨y,hy,hp,by rcases small 0 with ha|ha <;> omega,
    by rcases small 0 with ha|ha <;> omega,hby⟩

#print axioms cylinder
#print axioms certified
#print axioms transition
#print axioms persistent_descent
end Collatz.PaidRenewal
