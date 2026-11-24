import MinimumFailure
import UpperRepresentative
import Mathlib.Data.Fintype.Pigeonhole

namespace Collatz.OneEvenEscape

open Collatz.MinimumFailure

/-- Exact run, including the unit condition that makes reversal unique. -/
structure Edge (x z : Nat) : Type where
  m : Nat
  a : Nat
  first : x+1 = 2^m*a
  last : 2*z+1 = 3^m*a
  unit : a%3 ≠ 0

private theorem grade_unique {i j a b : Nat} (ha : a%3≠0) (hb : b%3≠0)
    (eq : 3^i*a=3^j*b) : i=j ∧ a=b := by
  induction i generalizing j with
  | zero =>
    cases j with
    | zero => simpa using eq
    | succ j =>
      simp only [Nat.pow_zero, Nat.one_mul, Nat.pow_succ] at eq
      have e : a=3*(3^j*b) := by rw [eq]; ac_rfl
      omega
  | succ i ih =>
    cases j with
    | zero =>
      simp only [Nat.pow_zero, Nat.one_mul, Nat.pow_succ] at eq
      have e : b=3*(3^i*a) := by rw [←eq]; ac_rfl
      omega
    | succ j =>
      have e : 3*(3^i*a)=3*(3^j*b) := by
        simpa only [Nat.pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using eq
      obtain ⟨hh, hv⟩ := ih (j := j) (by omega)
      exact ⟨congrArg Nat.succ hh,hv⟩

theorem reverse_unique {x y z : Nat} (e : Edge x z) (f : Edge y z) : x=y := by
  obtain ⟨hm,ha⟩ := grade_unique e.unit f.unit (e.last.symm.trans f.last)
  have h := e.first
  rw [hm,ha,←f.first] at h
  omega

/-- The original multiple of three cannot be crossed a second time by rewinding. -/
theorem path_no_repeat (y : Nat → Nat) (N : Nat) (root : y 0%3=0)
    (edges : ∀ i, i<N → Edge (y i) (y (i+1)))
    (units : ∀ i, i<N → y (i+1)%3=1)
    (i j : Nat) (lt : i<j) (hj : j≤N) : y i≠y j := by
  induction i generalizing j with
  | zero =>
    cases j with
    | zero => omega
    | succ j =>
      have u := units j (by omega)
      intro eq
      rw [←eq] at u
      omega
  | succ i ih =>
    cases j with
    | zero => omega
    | succ j =>
      intro eq
      have ej := edges j (by omega)
      rw [←eq] at ej
      exact ih j (by omega) (by omega) (reverse_unique (edges i (by omega)) ej)

/-- A complete singleton chain from a multiple of three must cross any
given ordinary ceiling by the stated finite (linear) pigeonhole deadline. -/
theorem bounded_chain_escapes (y : Nat → Nat) (B : Nat) (root : y 0%3=0)
    (edges : ∀ i, i<B+1 → Edge (y i) (y (i+1)))
    (units : ∀ i, i<B+1 → y (i+1)%3=1) :
    ∃ i≤B+1, B<y i := by
  by_contra h
  have bound (i : Fin (B+2)) : y i.val<B+1 := by
    have hi := i.isLt
    by_contra neg
    exact h ⟨i.val,by omega,by omega⟩
  let f : Fin (B+2) → Fin (B+1) := fun i => ⟨y i.val,bound i⟩
  obtain ⟨i,j,diff,eq⟩ := Fintype.exists_ne_map_eq_of_card_lt f (by simp)
  have valEq : y i.val=y j.val := congrArg Fin.val eq
  have hne : i.val≠j.val := fun e => diff (Fin.ext e)
  have hi := i.isLt
  have hj := j.isLt
  by_cases lt : i.val<j.val
  · exact path_no_repeat y (B+1) root edges units i j lt (by omega) valEq
  · exact path_no_repeat y (B+1) root edges units j i (by omega) (by omega) valEq.symm

/-- For the recentered branch, a repeated vertex makes the *starting*
vertex periodic, even though it need not be a ternary root. -/
theorem rewind_repeat (y : Nat → Nat) (N : Nat)
    (edges : ∀ i, i<N → Edge (y i) (y (i+1)))
    (i d : Nat) (endle : i+d≤N) (again : y i=y (i+d)) : y 0=y d := by
  induction i with
  | zero => simpa using again
  | succ i ih =>
    have other := edges (i+d) (by omega)
    have eq : y (i+1) = y ((i+d)+1) := by simpa [Nat.succ_add] using again
    rw [←eq] at other
    exact ih (by omega) (reverse_unique (edges i (by omega)) other)

/-- At any visited interior site, a double even exit makes its own small
multiple of three merge with the originally bad arm. No bound on run length. -/
theorem interior_double_exit {q u e b : Nat} (least : LeastDiscordance q)
    (bad : ¬Good (6*u+1)) (pos : 0<u) (size : u<q)
    (hb : 0<b) (shape : 2^(e+1)*b=6*u+2) : (3^e*b)%4≠3 := by
  intro double
  have safe := smaller_multiples_good least (3*u) (by omega) (by omega) (by omega)
  have meet := UpperRepresentative.first_exit_labels label label_step e b hb double
  have h : 2^(e+1)*b=2*(2^e*b) := by rw [Nat.pow_succ]; ac_rfl
  rw [shape, show 2^e*b-1=3*u by omega] at meet
  exact bad ((label_eq_one _).mp ((by simpa using meet : label (6*u+1)=label (3*u)).trans
    ((label_eq_one _).mpr safe)))

/-- Success of the other exit certifies a bad multiple on the *upper* side. -/
theorem singleton_upper {x m a : Nat} (bad : ¬Good x) (ha : 0<a)
    (shape : 2^m*a=x+1) (single : (3^m*a)%4=3) : ¬Good (2*x+1) := by
  intro hg
  have meet := UpperRepresentative.first_exit_labels label label_step m a ha single
  have h : 2^(m+1)*a=2*(2^m*a) := by rw [Nat.pow_succ]; ac_rfl
  rw [h,shape] at meet
  have m' : label (2*x+1)=label x := by simpa [Nat.mul_add] using meet
  exact bad ((label_eq_one x).mp (m'.symm.trans ((label_eq_one _).mpr hg)))

/-- The least bad multiple bounds the height of every continuing odd site. -/
theorem singleton_floor {q x m a : Nat} (least : LeastDiscordance q)
    (bad : ¬Good x) (hx : x%3=1) (ha : 0<a) (shape : 2^m*a=x+1)
    (single : (3^m*a)%4=3) : 3*q≤2*x+1 := by
  by_contra small
  exact singleton_upper bad ha shape single (smaller_multiples_good least _ (by omega)
    (by omega) (by omega))

#print axioms reverse_unique
#print axioms path_no_repeat
#print axioms bounded_chain_escapes
#print axioms rewind_repeat
#print axioms interior_double_exit
#print axioms singleton_upper
#print axioms singleton_floor

end Collatz.OneEvenEscape
