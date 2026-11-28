import Mathlib.Tactic.IntervalCases
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-! Literal four-clock branching on the ordinary positive 3-unit graph.
This is a finite arithmetic foundation for the written electrical analysis;
it contains no assertion that every component is the component of 1. -/
namespace CoreBranching

def step (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else (3*n+1)/2

def run : ℕ → ℕ → ℕ
  | 0, n => n
  | k+1, n => run k (step n)

theorem step_double (n : ℕ) : step (2*n) = n := by
  simp [step]

theorem step_odd (n : ℕ) : step (2*n+1) = 3*n+2 := by
  simp [step, Nat.add_mod]
  omega

theorem run_add (a b n : ℕ) : run (a+b) n = run b (run a n) := by
  induction a generalizing n with
  | zero => simp [run]
  | succ a ih => simpa [Nat.succ_add, run] using ih (step n)

theorem four_double (n : ℕ) : run 4 (16*n) = n := by
  have he : 16*n = 2*(2*(2*(2*n))) := by omega
  rw [he]
  simp [run, step_double]

theorem six_rows (k : ℕ) :
    run 4 (48*k+4) = 9*k+1 ∧
    run 4 (48*k+8) = 9*k+2 ∧
    run 4 (48*k+20) = 9*k+4 ∧
    run 4 (48*k+26) = 9*k+5 ∧
    run 4 (48*k+37) = 9*k+7 ∧
    run 4 (48*k+40) = 9*k+8 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · have h0 : step (48*k+4) = 24*k+2 := by
      unfold step
      split <;> omega
    have h1 : step (24*k+2) = 12*k+1 := by
      unfold step
      split <;> omega
    have h2 : step (12*k+1) = 18*k+2 := by
      unfold step
      split <;> omega
    have h3 : step (18*k+2) = 9*k+1 := by
      unfold step
      split <;> omega
    simp only [run, h0, h1, h2, h3]
  · have h0 : step (48*k+8) = 24*k+4 := by
      unfold step
      split <;> omega
    have h1 : step (24*k+4) = 12*k+2 := by
      unfold step
      split <;> omega
    have h2 : step (12*k+2) = 6*k+1 := by
      unfold step
      split <;> omega
    have h3 : step (6*k+1) = 9*k+2 := by
      unfold step
      split <;> omega
    simp only [run, h0, h1, h2, h3]
  · have h0 : step (48*k+20) = 24*k+10 := by
      unfold step
      split <;> omega
    have h1 : step (24*k+10) = 12*k+5 := by
      unfold step
      split <;> omega
    have h2 : step (12*k+5) = 18*k+8 := by
      unfold step
      split <;> omega
    have h3 : step (18*k+8) = 9*k+4 := by
      unfold step
      split <;> omega
    simp only [run, h0, h1, h2, h3]
  · have h0 : step (48*k+26) = 24*k+13 := by
      unfold step
      split <;> omega
    have h1 : step (24*k+13) = 36*k+20 := by
      unfold step
      split <;> omega
    have h2 : step (36*k+20) = 18*k+10 := by
      unfold step
      split <;> omega
    have h3 : step (18*k+10) = 9*k+5 := by
      unfold step
      split <;> omega
    simp only [run, h0, h1, h2, h3]
  · have h0 : step (48*k+37) = 72*k+56 := by
      unfold step
      split <;> omega
    have h1 : step (72*k+56) = 36*k+28 := by
      unfold step
      split <;> omega
    have h2 : step (36*k+28) = 18*k+14 := by
      unfold step
      split <;> omega
    have h3 : step (18*k+14) = 9*k+7 := by
      unfold step
      split <;> omega
    simp only [run, h0, h1, h2, h3]
  · have h0 : step (48*k+40) = 24*k+20 := by
      unfold step
      split <;> omega
    have h1 : step (24*k+20) = 12*k+10 := by
      unfold step
      split <;> omega
    have h2 : step (12*k+10) = 6*k+5 := by
      unfold step
      split <;> omega
    have h3 : step (6*k+5) = 9*k+8 := by
      unfold step
      split <;> omega
    simp only [run, h0, h1, h2, h3]

def alternate (n : ℕ) : ℕ :=
  48*(n/9) + match n%9 with
    | 1 => 4
    | 2 => 8
    | 4 => 20
    | 5 => 26
    | 7 => 37
    | 8 => 40
    | _ => 0

theorem alternate_properties (n : ℕ) (hn : 0<n) (hu : n%3≠0) :
    0 < alternate n ∧ alternate n % 3 ≠ 0 ∧
      alternate n < 16*n ∧ run 4 (alternate n) = n := by
  have hm : n%9<9 := Nat.mod_lt n (by decide)
  have hrows := six_rows (n/9)
  have he : n = 9*(n/9)+n%9 := by omega
  interval_cases h : n%9 <;> simp [alternate, h] at * <;> omega

def child (b : Bool) (n : ℕ) : ℕ := if b then alternate n else 16*n

theorem child_properties (b : Bool) (n : ℕ) (hn : 0<n) (hu : n%3≠0) :
    0<child b n ∧ child b n%3≠0 ∧ child b n≤16*n ∧ run 4 (child b n)=n := by
  cases b
  · simp only [child, Bool.false_eq_true, ite_false]
    have hh := four_double n
    omega
  · simp only [child, ite_true]
    obtain ⟨ha, hu', hb, hc⟩ := alternate_properties n hn hu
    exact ⟨ha, hu', hb.le, hc⟩

theorem child_injective_bit (n : ℕ) (hn : 0<n) (hu : n%3≠0) :
    Function.Injective (fun b : Bool => child b n) := by
  have hlt := (alternate_properties n hn hu).2.2.1
  intro a b hab
  cases a <;> cases b <;> simp_all [child]

def ancestor (n : ℕ) : List Bool → ℕ
  | [] => n
  | b :: w => child b (ancestor n w)

theorem ancestor_unit (n : ℕ) (hn : 0<n) (hu : n%3≠0) (w : List Bool) :
    0<ancestor n w ∧ ancestor n w%3≠0 := by
  induction w with
  | nil => exact ⟨hn,hu⟩
  | cons b w ih =>
    have h := child_properties b (ancestor n w) ih.1 ih.2
    exact ⟨h.1,h.2.1⟩

theorem ancestor_clock (n : ℕ) (hn : 0<n) (hu : n%3≠0) (w : List Bool) :
    run (4*w.length) (ancestor n w) = n := by
  induction w with
  | nil => rfl
  | cons b w ih =>
    have hx := ancestor_unit n hn hu w
    have hh := (child_properties b (ancestor n w) hx.1 hx.2).2.2.2
    change run (4*(w.length+1)) (child b (ancestor n w)) = n
    rw [show 4*(w.length+1)=4+4*w.length by omega, run_add, hh]
    exact ih

theorem ancestor_height (n : ℕ) (hn : 0<n) (hu : n%3≠0) (w : List Bool) :
    ancestor n w ≤ 16^w.length*n := by
  induction w with
  | nil => simp [ancestor]
  | cons b w ih =>
    have hx := ancestor_unit n hn hu w
    have hh := (child_properties b (ancestor n w) hx.1 hx.2).2.2.1
    change child b (ancestor n w) ≤ 16^(w.length+1)*n
    calc
      _ ≤ 16*(ancestor n w) := hh
      _ ≤ 16*(16^w.length*n) := Nat.mul_le_mul_left 16 ih
      _ = _ := by rw [pow_succ]; ring

theorem ancestor_injective_at_depth (n : ℕ) (hn : 0<n) (hu : n%3≠0)
    (v w : List Bool) (hlen : v.length=w.length)
    (heq : ancestor n v=ancestor n w) : v=w := by
  induction v generalizing w with
  | nil => cases w <;> simp_all
  | cons b v ih =>
    cases w with
    | nil => simp at hlen
    | cons c w =>
      have hv := ancestor_unit n hn hu v
      have hw := ancestor_unit n hn hu w
      have hb := (child_properties b (ancestor n v) hv.1 hv.2).2.2.2
      have hc := (child_properties c (ancestor n w) hw.1 hw.2).2.2.2
      have ht : ancestor n v=ancestor n w := by
        have hh := congrArg (run 4) heq
        simpa only [ancestor, hb, hc] using hh
      have hwv : v=w := ih w (by simpa using hlen) ht
      subst w
      have hbc : b=c := child_injective_bit (ancestor n v) hv.1 hv.2 heq
      simp [hbc]

#print axioms step_double
#print axioms step_odd
#print axioms run_add
#print axioms four_double
#print axioms six_rows
#print axioms alternate_properties
#print axioms child_properties
#print axioms child_injective_bit
#print axioms ancestor_unit
#print axioms ancestor_clock
#print axioms ancestor_height
#print axioms ancestor_injective_at_depth

end CoreBranching
