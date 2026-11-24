import Mathlib.Algebra.Ring.Int.Parity
import Mathlib.Basic.Real.Basic
import Mathlib.Data.List.Count
import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic

namespace Collatz.RotationalDistance

/-- Cleared literal shortcut equation for a state of denominator d. -/
def Step (d : ℤ) (b : Bool) (n v : ℤ) : Prop :=
  2*v = if b then 3*n+d else n

/-- A finite walk includes its intermediate numerators. -/
inductive Walk (d : ℤ) : List Bool → ℤ → ℤ → Prop where
  | nil (n) : Walk d [] n n
  | cons {b w n y z} : Step d b n y → Walk d w y z → Walk d (b::w) n z

def amp : List Bool → ℤ
  | [] => 1
  | b::w => (if b then 3 else 1) * amp w

theorem amp_odd (w : List Bool) : Odd (amp w) := by
  induction w with
  | nil => simp [amp]
  | cons b w ih =>
    cases b
    · simpa [amp] using ih
    · simpa [amp] using (show Odd (3:ℤ) by decide).mul ih

theorem same_word_difference {d n m u v : ℤ} {w : List Bool}
    (hn : Walk d w n u) (hm : Walk d w m v) :
    (2:ℤ)^w.length * (u-v) = amp w * (n-m) := by
  induction hn generalizing m v with
  | nil n =>
    cases hm
    simp [amp]
  | @cons b w n y z hb _ ih =>
    cases hm with
    | @cons _ _ _ y' _ hb' hw' =>
      have h := ih hw'
      cases b <;> simp only [Step, Bool.false_eq_true, ↓reduceIte] at hb hb' <;>
        simp [amp, pow_succ] <;> linear_combination 2*h + amp w*(hb-hb')

/-- Two integer numerators with matching literal bits are equal modulo the
full dyadic word modulus, even at nontrivial odd common denominator. -/
theorem common_run_dvd {d n m u v : ℤ} {w : List Bool}
    (hn : Walk d w n u) (hm : Walk d w m v) : (2:ℤ)^w.length ∣ n-m := by
  have h := same_word_difference hn hm
  have hcop : IsCoprime (2:ℤ) (amp w) := by
    obtain ⟨k,hk⟩ := amp_odd w
    exact ⟨-k,1,by rw [hk]; ring⟩
  exact (hcop.pow_left).dvd_of_dvd_mul_left ⟨u-v,h.symm⟩

/-- Correcting the numerator by d makes an odd step exactly homogeneous
and an even step affine with nonnegative intercept. -/
theorem dominance_step {d n m n' m' K : ℤ} {b c : Bool}
    (hd : 0 ≤ d) (hn : 0 ≤ n) (hK : 1 ≤ K)
    (hn' : Step d b n n') (hm' : Step d c m m')
    (h : m+d ≤ K*(n+d)) :
    m'+d ≤ (if c && !b then 3 else 1)*K*(n'+d) := by
  have hKd : d ≤ K*d := by nlinarith [mul_nonneg (show 0 ≤ K-1 by omega) hd]
  have hKn : 0 ≤ K*n := mul_nonneg (by omega) hn
  cases b <;> cases c <;> simp [Step] at hn' hm' ⊢ <;> nlinarith [congrArg (fun z : ℤ => K*z) hn']

/-- Number of positions with an odd partner bit and an even base bit. -/
def losses : List (Bool × Bool) → ℕ
  | [] => 0
  | (b,c)::w => (if c && !b then 1 else 0) + losses w

theorem nonneg_walk_step {d n n' : ℤ} {b : Bool}
    (hd : 0 ≤ d) (hn : 0 ≤ n) (hs : Step d b n n') : 0 ≤ n' := by
  cases b <;> simp [Step] at hs <;> omega

/-- The paired walk charges only directed disagreements. -/
theorem dominance_walk {d : ℤ} (hd : 0 ≤ d) (w : List (Bool × Bool))
    {n m n' m' K : ℤ} (hn : 0 ≤ n) (hK : 1 ≤ K)
    (h : m+d ≤ K*(n+d))
    (hw : Walk d (w.map Prod.fst) n n') (hv : Walk d (w.map Prod.snd) m m') :
    m'+d ≤ 3^(losses w)*K*(n'+d) := by
  induction w generalizing n m K with
  | nil =>
    cases hw; cases hv
    simpa [losses] using h
  | cons head w ih =>
    obtain ⟨b,c⟩ := head
    cases hw with
    | cons hb hx =>
      cases hv with
      | cons hc hy =>
        have hi := dominance_step hd hn hK hb hc h
        have hk : (1:ℤ) ≤ (if c && !b then 3 else 1)*K := by
          split <;> omega
        have hh := ih (nonneg_walk_step hd hn hb) hk hi hx hy
        cases b <;> cases c <;> simp [losses, pow_add] at hh ⊢ <;> linarith

/-- The geometric budget for successive matching runs and intervening
mismatches. Each supplied update is the literal clock bound derived from
divisibility and one-step height growth. -/
theorem clock_budget {s h : ℝ} {j : ℕ → ℝ} (hs : 1 < s) (hj : j 0 = 0)
    (step : ∀ i, j (i+1) ≤ s*j i+h) (k : ℕ) :
    (s-1)*j k ≤ h*(s^k-1) := by
  induction k with
  | zero => simp [hj]
  | succ k ih =>
    have hh := mul_le_mul_of_nonneg_left (step k) (show 0 ≤ s-1 by linarith)
    have hi := mul_le_mul_of_nonneg_left ih (show 0 ≤ s by linarith)
    rw [pow_succ]
    nlinarith

/-- A modular inverse and a continued-fraction residual produce a short
physical return even when the original shift shares factors with its period. -/
theorem euclidean_return (A r g N s u k p q e : ℤ)
    (hA : A = g*N) (hr : r = g*s) (hu : s*u = 1+N*k)
    (he : e = q*u-N*p) :
    e*r-g*q = A*(q*k-s*p) := by
  rw [hA, hr, he]
  linear_combination g*q*hu

def wordGain : List Bool → ℚ
  | [] => 1
  | b::w => (if b then 3/2 else 1/2) * wordGain w

def wordDrift : List Bool → ℚ
  | [] => 0
  | b::w => (if b then (1/2)*wordGain w else 0) + wordDrift w

def suffixControl (K : ℚ) : List Bool → Prop
  | [] => True
  | _::w => wordGain w ≤ K ∧ suffixControl K w

theorem drift_from_suffixes (w : List Bool) (K : ℚ) (h : suffixControl K w) :
    2*wordDrift w ≤ (w.count true : ℚ)*K := by
  induction w with
  | nil => simp [wordDrift]
  | cons b w ih =>
    obtain ⟨hs, hw⟩ := h
    have hh := ih hw
    cases b <;> simp [wordDrift] <;> linarith

theorem walk_affine {d n m : ℤ} {w : List Bool} (hw : Walk d w n m) :
    (m : ℚ) = wordGain w*n + wordDrift w*d := by
  induction hw with
  | nil n => simp [wordGain, wordDrift]
  | @cons b w n y z hs _ ih =>
    cases b <;> simp [Step] at hs <;>
      have hb := congrArg (fun z : ℤ => (z:ℚ)) hs <;>
      push_cast at hb <;> simp [wordGain, wordDrift] <;>
      linear_combination ih + (wordGain w/2)*hb

/-- Complete-denominator height bound from all suffix slopes at one phase. -/
theorem closed_height_from_suffixes {d n : ℤ} {w : List Bool} {K : ℚ}
    (hd : 0 ≤ d) (h : suffixControl K w) (hw : Walk d w n n) :
    2*(1-wordGain w)*n ≤ (w.count true : ℚ)*K*d := by
  have ha := walk_affine hw
  have hh := mul_le_mul_of_nonneg_right (drift_from_suffixes w K h)
    (show (0:ℚ) ≤ d by exact_mod_cast hd)
  linarith

#print axioms same_word_difference
#print axioms common_run_dvd
#print axioms dominance_step
#print axioms dominance_walk
#print axioms clock_budget
#print axioms euclidean_return
#print axioms drift_from_suffixes
#print axioms walk_affine
#print axioms closed_height_from_suffixes

end Collatz.RotationalDistance
