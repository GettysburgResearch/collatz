import Mathlib.Tactic

/-! Strict separation before a smooth multiplier's grade is overtaken.
    The statements concern actual integer endpoints and native clocks. -/

set_option autoImplicit false
set_option warningAsError true

namespace Collatz.Sprint.Descent

def bit (x : ℕ) : ℕ := x % 2

def T (x : ℕ) : ℕ := if bit x = 0 then x / 2 else (3*x+1)/2

def run : ℕ → ℕ → ℕ
  | 0, x => x
  | t+1, x => T (run t x)

def grade : ℕ → ℕ → ℕ
  | 0, _ => 0
  | t+1, x => grade t x + bit (run t x)

theorem double_step (x : ℕ) : 2*T x=3^(bit x)*x+bit x := by
  have h : x%2 = 0 ∨ x%2 = 1 := by omega
  rcases h with h | h <;> simp [T, bit, h] <;> omega

theorem strict_step (x y l j : ℕ) (separation : y<3^l*x)
    (aligned : j+bit x=l+bit y) : T y<3^j*T x := by
  have alignedPow : 3^j*3^(bit x)=(3:ℕ)^(bit y)*3^l := by
    rw [←pow_add, aligned, ←pow_add, Nat.add_comm]
  have e : bit y=0 ∨ bit y=1 := by unfold bit; omega
  have pos : bit y<3^(bit y) := by rcases e with e|e <;> simp [e]
  have lead := Nat.mul_le_mul_left (3^(bit y)) separation
  change 3^(bit y)*(y+1) ≤ 3^(bit y)*(3^l*x) at lead
  rw [Nat.mul_add, Nat.mul_one, ←Nat.mul_assoc, ←alignedPow,
    Nat.mul_assoc] at lead
  have scale : 2*(3^j*T x)=3^j*(3^(bit x)*x)+3^j*bit x := by
    calc
      2*(3^j*T x)=3^j*(2*T x) := by ring
      _ = _ := by rw [double_step, Nat.mul_add]
  have low := double_step y
  omega

theorem strict_corridor (x y s : ℕ) (start : y<3^s*x)
    (t : ℕ) (corridor : ∀ i≤t, grade i x ≤ s+grade i y) :
    run t y<3^(s+grade t y-grade t x)*run t x := by
  induction t with
  | zero => simpa [run, grade] using start
  | succ t ih =>
    have hin := corridor t (by omega)
    have hout := corridor (t+1) (by omega)
    apply strict_step (run t x) (run t y)
      (s+grade t y-grade t x) (s+grade (t+1) y-grade (t+1) x)
      (ih (fun i h => corridor i (by omega)))
    simp only [grade] at hout ⊢
    omega

theorem odd_launch (x s : ℕ) (odd : bit x=1) (positive : 0<s) :
    bit (3^s*x)=1 ∧ T (3^s*x)<3^s*T x := by
  have oddPow : (3^s) % 2=1 := by simp [Nat.pow_mod]
  have oddY : bit (3^s*x)=1 := by
    change (3^s*x)%2=1
    rw [Nat.mul_mod, oddPow, show x%2=1 from odd]
  refine ⟨oddY, ?_⟩
  have high := double_step x
  have low := double_step (3^s*x)
  rw [odd] at high
  rw [oddY] at low
  simp only [pow_one] at high low
  have gt : 1 < (3:ℕ)^s := one_lt_pow₀ (by decide) (by omega)
  have scaled : 2*(3^s*T x)=3*(3^s*x)+3^s := by
    calc
      _ = 3^s*(2*T x) := by ring
      _ = _ := by rw [high]; ring
  omega

theorem no_counted_meeting_before_overtake (x s h : ℕ) (odd : bit x=1)
    (positive : 0<s)
    (corridor : ∀ i≤h, grade i (T x)≤s+grade i (T (3^s*x)))
    (tie : grade h (T x)=s+grade h (T (3^s*x))) :
    run h (T (3^s*x)) < run h (T x) := by
  have strict := strict_corridor (T x) (T (3^s*x)) s
    (odd_launch x s odd positive).2 h corridor
  simpa [tie] using strict

#print axioms double_step
#print axioms strict_step
#print axioms strict_corridor
#print axioms odd_launch
#print axioms no_counted_meeting_before_overtake

end Collatz.Sprint.Descent
