module
public import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Positivity
public section

namespace TwoAnchor

/-- Exact guarded shortcut history on the integers, recording clock and odd count. -/
inductive Trace : ℤ → ℕ → ℕ → ℤ → Prop where
  | nil (x : ℤ) : Trace x 0 0 x
  | even {q : ℤ} {t a : ℕ} {y : ℤ} :
    Trace q t a y → Trace (2*q) (t+1) a y
  | odd {q : ℤ} {t a : ℕ} {y : ℤ} :
    Trace (3*q+2) t a y → Trace (2*q+1) (t+1) (a+1) y

theorem Trace.join {x y z : ℤ} {t a u b : ℕ}
    (p : Trace x t a y) (q : Trace y u b z) :
    Trace x (u+t) (b+a) z := by
  induction p with
  | nil => simpa using q
  | even p ih => exact Trace.even (ih q)
  | odd p ih => exact Trace.odd (ih q)

theorem initial_odds (h : ℕ) (m : ℤ) :
    Trace (2^h*m-1) h h (3^h*m-1) := by
  induction h generalizing m with
  | zero => simpa using Trace.nil (m-1)
  | succ h ih =>
    have p : Trace (3*(2^h*m-1)+2) h h (3^(h+1)*m-1) := by
      convert ih (3*m) using 1 <;> ring
    convert Trace.odd p using 1
    ring

/-- Both arms merge with exactly h+1 odd steps, from source n and (n-1)/2.
    Here H=h+1 and 3^h*m=4*j+3 is equivalent to 3^H*m=1 mod 4. -/
theorem half_source (h : ℕ) (m j : ℤ) (hm : 3^h*m=4*j+3) :
    Trace (2^(h+1)*m-1) (h+3) (h+1) (3*j+2) ∧
    Trace (2^h*m-1) (h+2) (h+1) (3*j+2) := by
  have endN : Trace (3^(h+1)*m-1) 2 0 (3*j+2) := by
    have e := Trace.even (Trace.even (Trace.nil (3*j+2)))
    convert e using 1
    rw [pow_succ]
    linear_combination 3*hm
  have endM : Trace (3^h*m-1) 2 1 (3*j+2) := by
    have e := Trace.even (Trace.odd (q := j) (Trace.nil (3*j+2)))
    convert e using 1
    linear_combination hm
  constructor
  · convert (initial_odds (h+1) m).join endN using 1 <;> omega
  · convert (initial_odds h m).join endM using 1 <;> omega

/-- Integral displacement of any guarded ordinary history. -/
theorem Trace.shift {x y : ℤ} {t a : ℕ} (p : Trace x t a y) (k : ℤ) :
    Trace (x+2^t*k) t a (y+3^a*k) := by
  induction p generalizing k with
  | nil => simpa using Trace.nil _
  | @even q t a y p ih =>
    convert Trace.even (ih k) using 1
    ring
  | @odd q t a y p ih =>
    have tail : Trace (3*(q+2^t*k)+2) t a (y+3^(a+1)*k) := by
      convert ih (3*k) using 1 <;> ring
    convert Trace.odd tail using 1
    ring

theorem Trace.pos_of_end_pos {x y : ℤ} {t a : ℕ} (p : Trace x t a y) (hy : 0<y) :
    0<x := by
  induction p with
  | nil => exact hy
  | even p ih => have := ih hy; omega
  | odd p ih => have := ih hy; omega

theorem Trace.affine_lower {x y : ℤ} {t a : ℕ} (p : Trace x t a y) :
    3^a*x ≤ 2^t*y := by
  induction p with
  | nil => simp
  | @even q t a y p ih =>
    rw [pow_succ]
    linear_combination 2*ih
  | @odd q t a y p ih =>
    rw [pow_succ, pow_succ]
    have nonneg : (0:ℤ) ≤ 3^a := by positivity
    linear_combination 2*ih + nonneg

/-- No smaller predecessor of a positive target 1 + 3^a k with a odd inputs. -/
theorem clock_zero_barrier (x k : ℤ) (t a : ℕ) (hk : 0≤k)
    (p : Trace x t a (1+3^a*k)) : 1+3^a*k ≤ x := by
  have anchored : Trace (x-2^t*k) t a 1 := by
    convert p.shift (-k) using 1 <;> ring
  have hb := anchored.pos_of_end_pos (by decide)
  have hs := anchored.affine_lower
  have hpow : (0:ℤ) ≤ 3^a := by positivity
  have hdom : (3:ℤ)^a ≤ 2^t := by
    calc
      (3:ℤ)^a = 3^a*1 := by ring
      _ ≤ 3^a*(x-2^t*k) := mul_le_mul_of_nonneg_left (by omega) hpow
      _ ≤ 2^t := by simpa using hs
  have hh := mul_le_mul_of_nonneg_right hdom hk
  omega

#print axioms Trace.join
#print axioms Trace.shift
#print axioms Trace.pos_of_end_pos
#print axioms Trace.affine_lower
#print axioms clock_zero_barrier
#print axioms initial_odds
#print axioms half_source
end TwoAnchor
