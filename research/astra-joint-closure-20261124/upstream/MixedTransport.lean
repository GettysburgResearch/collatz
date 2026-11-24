import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Finite disjointness and phase transport for fixed-target inverse depth banks.
    Finite core from PR203, compiled in the joint-closure audit with narrow imports.
    The external mixing floor and all asymptotic estimates are absent. -/

namespace MixedTransport

def run (F : ℕ → ℕ) : ℕ → ℕ → ℕ
  | 0, x => x
  | j+1, x => run F j (F x)

theorem run_add (F : ℕ → ℕ) (i j x : ℕ) :
    run F (i+j) x = run F j (run F i x) := by
  induction i generalizing x with
  | zero => simp [run]
  | succ i ih =>
    rw [Nat.succ_add]
    change run F (i+j) (F x) = run F j (run F i (F x))
    exact ih (F x)

def Nonperiodic (F : ℕ → ℕ) (q : ℕ) : Prop :=
  ∀ d : ℕ, 0 < d → run F d q ≠ q

theorem distinct_depths (F : ℕ → ℕ) (y q b c : ℕ)
    (hn : Nonperiodic F q) (hb : run F b y = q)
    (hc : run F c y = q) : b = c := by
  have aux : ∀ i j : ℕ, run F i y = q → run F j y = q → i ≤ j := by
    intro i j hi hj
    by_contra h
    have hjlt : j < i := by omega
    have hs : j + (i-j) = i := by omega
    apply hn (i-j) (by omega)
    calc
      run F (i-j) q = run F (i-j) (run F j y) := congrArg (run F (i-j)) hj.symm
      _ = run F (j+(i-j)) y := (run_add F j (i-j) y).symm
      _ = q := by rw [hs, hi]
  exact le_antisymm (aux b c hb hc) (aux c b hc hb)

theorem cannot_hit_target_earlier (F : ℕ → ℕ) (x q a i j t : ℕ)
    (hn : Nonperiodic F q) (h : run F i x = q)
    (hq : run F j q = a) (ht : t < i) : run F t x ≠ a := by
  intro he
  have hs : t+(i-t) = i := by omega
  have ha : run F (i-t) a = q := by
    calc
      run F (i-t) a = run F (i-t) (run F t x) := congrArg (run F (i-t)) he.symm
      _ = run F (t+(i-t)) x := (run_add F t (i-t) x).symm
      _ = q := by rw [hs, h]
  apply hn (j+(i-t)) (by omega)
  rw [run_add, hq, ha]

theorem common_clock (F : ℕ → ℕ) (n M H s y q : ℕ)
    (hh : ∀ i < M, run F H (n+i) = y)
    (hs : run F s y = q) :
    ∀ i < M, run F (H+s) (n+i) = q := by
  intro i hi
  rw [run_add, hh i hi, hs]

theorem lift_transport (r z n y t q B E P R C : ℤ)
    (hn : n = r + R*t)
    (hy : y = z + P*t)
    (hword : B*y = E*q-C) :
    B*P*(n-r) = R*(E*q-C-B*z) := by
  rw [hn]
  have h1 : B*(z+P*t) = E*q-C := by rw [←hy, hword]
  linear_combination R*h1

theorem word_carry_step (q y y' E C B A : ℤ)
    (h : B*y = E*q-C) (h' : 3*y' = A*y-1) :
    (3*B)*y' = (A*E)*q-(A*C+B) := by
  linear_combination A*h + B*h'

end MixedTransport
#print axioms MixedTransport.run_add
#print axioms MixedTransport.distinct_depths
#print axioms MixedTransport.cannot_hit_target_earlier
#print axioms MixedTransport.common_clock
#print axioms MixedTransport.lift_transport
#print axioms MixedTransport.word_carry_step
