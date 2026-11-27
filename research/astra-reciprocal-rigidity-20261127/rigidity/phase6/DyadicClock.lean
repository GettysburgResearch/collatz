import FiniteTrace
import Mathlib.Tactic.Linarith

/-! Exact ordinary inverse words and their clocks after dyadic shell lifting. -/

namespace Collatz.ReciprocalRigidity.DyadicClock
open Collatz.ReciprocalRigidity.FiniteTrace

private theorem orbit_add (a b x : ℕ) : orbit (a+b) x = orbit b (orbit a x) := by
  induction a generalizing x with
  | zero => simp [orbit]
  | succ a ih => rw [Nat.succ_add,orbit,ih,orbit]

theorem dyadic_steps (a x : ℕ) : orbit a (2^a*x) = x := by
  induction a with
  | zero => simp [orbit]
  | succ a ih =>
    rw [pow_succ,show 2^a*2*x=2*(2^a*x) by ring,orbit]
    have he (v : ℕ) : step (2*v)=v := by simp [step]
    rw [he,ih]

theorem one_inverse {e x y : ℕ} (he : 1 ≤ e) (hx : 3*x+1=2^e*y) :
    orbit e x=y := by
  obtain ⟨a,ha⟩ : ∃ a, e=a+1 := ⟨e-1, by omega⟩
  rw [ha,pow_succ] at hx
  have hm : 3*x+1=2*(2^a*y) := by rw [hx]; ring
  have hs : step x=2^a*y := by unfold step; split <;> omega
  rw [ha,orbit,hs,dyadic_steps]

/-- Its indices are root, terminal predecessor, number of odd transitions, and their true time. -/
inductive InverseWord : ℕ → ℕ → ℕ → ℕ → Prop
  | nil (y : ℕ) : InverseWord y y 0 0
  | extend {y x j s e z : ℕ} (prior : InverseWord y x j s)
      (he : 2≤e) (hz : 3*z+1=2^e*x) : InverseWord y z (j+1) (s+e)

theorem physical {y z j s : ℕ} (hw : InverseWord y z j s) : orbit s z=y := by
  induction hw with
  | nil => rfl
  | @extend x j s e z h he hz ih =>
    rw [Nat.add_comm s e,orbit_add,one_inverse (by omega : 1≤e) hz,ih]

/-- Integral form of the bounded real defect, including its two endpoint inequalities. -/
theorem footprint {y z j s : ℕ} (hw : InverseWord y z j s) :
    3^j*z ≤ 2^s*y ∧ 2^s*y+3^j ≤ 3^j*z+2^s := by
  induction hw with
  | nil => simp
  | @extend x j s e z h he hz ih =>
    obtain ⟨hu,hl⟩ := ih
    have he4 : 4≤2^e := Nat.pow_le_pow_right (by decide : 0<2) he
    have h1 := Nat.mul_le_mul_right (2^e) hu
    have h2 := Nat.mul_le_mul_right (2^e) hl
    have h3 := Nat.mul_le_mul_left (3^j) he4
    have h4 := congrArg (fun a : ℕ => 3^j*a) hz
    simp only [pow_add (2 : ℕ) s e,pow_succ (3 : ℕ) j]
    constructor <;> ring_nf at h1 h2 h3 h4 ⊢ <;> omega

/-- A lifted source visits its physical root at the advertised clock. -/
theorem lift_hits {y z j s : ℕ} (hw : InverseWord y z j s) (a : ℕ) :
    orbit (a+s) (2^a*z)=y := by rw [orbit_add,dyadic_steps,physical hw]

private theorem shell_power_bounds {y z j s a X : ℕ} (hw : InverseWord y z j s)
    (hlo : X≤2^a*z) :
    3^j*X≤2^(s+a)*y ∧ 2^(s+a)*y≤3^j*(2^a*z)+2^(s+a) := by
  obtain ⟨hu,hl⟩ := footprint hw
  have h1 := Nat.mul_le_mul_right (2^a) hu
  have h2 := Nat.mul_le_mul_right (2^a) hl
  have h3 := Nat.mul_le_mul_left (3^j) hlo
  rw [pow_add]
  constructor <;> ring_nf at h1 h2 h3 ⊢ <;> omega

/-- Two words at the same odd depth, lifted to one dyadic shell, have clocks at most one apart. -/
private theorem clock_le {y j z w s t a b X : ℕ} (hy : 2≤y)
    (hz : InverseWord y z j s) (hw : InverseWord y w j t)
    (hza : X≤2^a*z) (hzb : 2^a*z<2*X)
    (hwa : X≤2^b*w) : s+a ≤ t+b+1 := by
  obtain ⟨_,hu⟩ := shell_power_bounds hz hza
  obtain ⟨hl,_⟩ := shell_power_bounds hw hwa
  have hs := Nat.mul_lt_mul_of_pos_left hzb (by positivity : 0<3^j)
  by_contra hn
  have hpow := Nat.pow_le_pow_right (by decide : 0<2) (by omega : t+b+2≤s+a)
  rw [pow_add (2 : ℕ) (t+b) 2] at hpow
  have hp : 4*2^(t+b)≤2^(s+a) := by nlinarith only [hpow]
  have hdown : 2*2^(t+b)≤2^(s+a) := by omega
  have hdiff := Nat.mul_le_mul_left (2^(s+a)-2*2^(t+b)) hy
  have hab : 2^(s+a)-2*2^(t+b)+2*2^(t+b)=2^(s+a) := by omega
  have heq := congrArg (fun k : ℕ => k*y) hab
  nlinarith only [hu,hl,hs,hp,hdiff,heq,hab]

/-- The two possible clocks are adjacent, even when the odd words have widely differing totals. -/
theorem clocks_within_one {y j z w s t a b X : ℕ} (hy : 2≤y)
    (hz : InverseWord y z j s) (hw : InverseWord y w j t)
    (hza : X≤2^a*z) (hzb : 2^a*z<2*X)
    (hwa : X≤2^b*w) (hwb : 2^b*w<2*X) :
    s+a ≤ t+b+1 ∧ t+b ≤ s+a+1 :=
  ⟨clock_le hy hz hw hza hzb hwa,clock_le hy hw hz hwa hwb hza⟩

#print axioms physical
#print axioms footprint
#print axioms lift_hits
#print axioms clocks_within_one
end Collatz.ReciprocalRigidity.DyadicClock
