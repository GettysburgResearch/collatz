module

public import BergmanRelative
public import Mathlib.Basic.Real.Basic
public import Mathlib.Algebra.Order.AbsoluteValue.Basic
public import Mathlib.Data.Rat.Floor
public import Mathlib.Order.ConditionallyCompleteLattice.Basic
import all BergmanRelative
import all TernaryItinerary
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.BergmanRelative

set_option autoImplicit false

def rowSet (k H : ℕ) (selected : ℕ → Prop) : Set ℝ :=
  insert 0 {v | ∃ n, 3≤n ∧ H<n ∧ selected n ∧ v=(mass k n:ℝ)}

noncomputable def squaredNorm (k H : ℕ) (selected : ℕ → Prop) : ℝ :=
  sSup (rowSet k H selected)

private theorem cap (k a : ℕ) : mass k a ≤ (3:ℚ)^k := by
  induction k generalizing a with
  | zero => simp [mass]
  | succ k ih =>
    have ev := ih (2*a)
    have od := ih ((2*a-1)/3)
    have coef : ((2*a+1:ℕ):ℚ)/((a+1:ℕ):ℚ)≤2 := by
      apply (div_le_iff₀ (by positivity)).mpr
      push_cast
      linarith
    have even := mul_le_mul coef ev (mass_nonneg ..) (by norm_num)
    simp only [mass,pow_succ]
    split <;> linarith only [even,od,show 0≤(3:ℚ)^k by positivity]

private theorem rowBdd (k H : ℕ) (P : ℕ → Prop) : BddAbove (rowSet k H P) := by
  refine ⟨(3:ℝ)^k,?_⟩
  intro z mem
  rcases mem with eq|⟨n,_,_,_,rfl⟩
  · rw [eq]; positivity
  · exact_mod_cast cap k n

private theorem rowNonempty (k H : ℕ) (P : ℕ → Prop) : (rowSet k H P).Nonempty := ⟨0,Or.inl rfl⟩

private theorem norm_nonneg (k H : ℕ) (P : ℕ → Prop) : 0≤squaredNorm k H P :=
  le_csSup (rowBdd k H P) (Or.inl rfl)

private theorem norm_le_full (k H : ℕ) (P : ℕ → Prop) :
    squaredNorm k H P≤squaredNorm k 0 (fun _ => True) := by
  apply csSup_le (rowNonempty ..)
  intro z inSet
  rcases inSet with rfl|⟨n,domain,_,_,rfl⟩
  · exact norm_nonneg ..
  · exact le_csSup (rowBdd ..) (Or.inr ⟨n,domain,by omega,trivial,rfl⟩)

private theorem norm_eq_full {k H : ℕ} {P : ℕ → Prop}
    (cofinal : ∀ a, ∃ n, max H 3<n ∧ P n ∧ mass k a≤mass k n) :
    squaredNorm k H P=squaredNorm k 0 (fun _ => True) := by
  apply le_antisymm (norm_le_full ..)
  apply csSup_le (rowNonempty ..)
  intro z inSet
  rcases inSet with rfl|⟨a,_,_,_,rfl⟩
  · exact norm_nonneg ..
  · obtain ⟨n,large,sel,dom⟩ := cofinal a
    exact le_trans (by exact_mod_cast dom : (mass k a:ℝ)≤mass k n)
      (le_csSup (rowBdd ..) (Or.inr ⟨n,by omega,by omega,sel,rfl⟩))

private theorem norm_zero {k H : ℕ} {P : ℕ → Prop}
    (absent : ∀ n, 3≤n → ¬P n) : squaredNorm k H P=0 := by
  apply le_antisymm _ (norm_nonneg ..)
  apply csSup_le (rowNonempty ..)
  rintro _ (rfl|⟨n,dom,_,sel,_⟩)
  · exact le_rfl
  · exact (absent n dom sel).elim

/-- The component-crossing part of the selected dilation has either zero
or the entire squared power norm, uniformly after every height cutoff. -/
theorem selected_norm_dichotomy (k H : ℕ) :
    (Universal → squaredNorm k H (fun n => n%3≠0 ∧ ¬Meet n (target n))=0) ∧
    (¬Universal → squaredNorm k H (fun n => n%3≠0 ∧ ¬Meet n (target n))=
      squaredNorm k 0 (fun _ => True)) := by
  constructor
  · intro all
    apply norm_zero
    rintro n dom ⟨_,never⟩
    obtain ⟨i,hi⟩ := all n (by omega)
    obtain ⟨j,hj⟩ := all (target n) (Nat.mul_pos (by positivity) (by omega))
    exact never ⟨i,j,hi.trans hj.symm⟩
  · intro fail
    apply norm_eq_full
    intro a
    obtain ⟨n,large,unit,never,dom⟩ := mismatch_dominates fail k a (max H 3)
    exact ⟨n,large,⟨unit,never⟩,dom⟩

private theorem meet_trans {x y z : ℕ} (xy : Meet x y) (yz : Meet y z) : Meet x z := by
  obtain ⟨a,b,ab⟩ := xy
  obtain ⟨c,d,cd⟩ := yz
  refine ⟨a+c,d+b,?_⟩
  calc
    run (a+c) x=run (b+c) y := by simp only [run_add,ab]
    _=run (c+b) y := by rw [Nat.add_comm b c]
    _=run (d+b) z := by simp only [run_add,cd]

private theorem meet_symm {x y : ℕ} (h : Meet x y) : Meet y x := by
  obtain ⟨a,b,eq⟩ := h; exact ⟨b,a,eq.symm⟩

private theorem dyadic_meet_iff (j x y : ℕ) :
    Meet (2^j*x) (2^j*y) ↔ Meet x y := by
  have dx : Meet (2^j*x) x := ⟨j,0,halve ..⟩
  have dy : Meet (2^j*y) y := ⟨j,0,halve ..⟩
  exact ⟨fun h => meet_trans (meet_symm dx) (meet_trans h dy),
    fun h => meet_trans dx (meet_trans h (meet_symm dy))⟩

def tripleDefect (n : ℕ) : Prop := ¬Meet n (3*n)

private theorem triple_double (j n : ℕ) : tripleDefect (2^j*n) ↔ tripleDefect n := by
  unfold tripleDefect
  rw [show 3*(2^j*n)=2^j*(3*n) by ring,dyadic_meet_iff]

theorem fixed_unit_full {q : ℕ} (qu : q%3≠0) (dq : tripleDefect q) (k H : ℕ) :
    squaredNorm k H tripleDefect=squaredNorm k 0 (fun _ => True) := by
  obtain ⟨e,u,eu,uo⟩ := split_twos q (by omega)
  rw [eu] at dq qu
  have du := (triple_double e u).mp dq
  have uu : u%3≠0 := by intro bad; simp [Nat.mul_mod,bad] at qu
  apply norm_eq_full
  intro a
  obtain ⟨j,_,large,_,row⟩ := ray_row uo uu 0 k a (max H 3)
  exact ⟨_,large,(triple_double j u).mpr du,row⟩

private theorem even_below (k n : ℕ) : (evenMass k n:ℝ)≤(2:ℝ)^k := by
  change ((((2^k*n+1:ℕ):ℚ)/((n+1:ℕ):ℚ):ℚ):ℝ)≤_
  push_cast
  apply (div_le_iff₀ (by positivity)).mpr
  nlinarith only [show 1≤(2:ℝ)^k from one_le_pow₀ (by norm_num)]

private theorem dyadic_norm {P : ℕ → Prop} {q : ℕ} (positive : 0<q)
    (ray : ∀ j, P (2^j*q)) (allNonunit : ∀ n, P n → n%3=0) (k H : ℕ) :
    squaredNorm k H P=(2:ℝ)^k := by
  apply csSup_eq_of_forall_le_of_forall_lt_exists_gt (rowNonempty ..)
  · rintro _ (rfl|⟨n,_,_,dn,rfl⟩)
    · positivity
    · rw [nonunit_mass k n (allNonunit n dn)]; exact even_below ..
  · intro w less
    have delta : 0<(2:ℝ)^k-w := by linarith
    obtain ⟨J,big⟩ := exists_nat_gt (((2:ℝ)^k+|w|+1)/((2:ℝ)^k-w))
    let j := J+H+3
    let n := 2^j*q
    have tall : j<n := lt_of_lt_of_le Nat.lt_two_pow_self
      (by simpa [n] using Nat.mul_le_mul_left (2^j) (show 1≤q from positive))
    have far : J<n ∧ H<n ∧ 3≤n := by dsimp [j] at tall; omega
    have bad : P n := ray j
    refine ⟨(mass k n:ℝ),Or.inr ⟨n,far.2.2,far.2.1,bad,rfl⟩,?_⟩
    rw [nonunit_mass k n (allNonunit _ bad)]
    change w<((((2^k*n+1:ℕ):ℚ)/((n+1:ℕ):ℚ):ℚ):ℝ)
    push_cast
    apply (lt_div_iff₀ (by positivity)).mpr
    have above : (((2:ℝ)^k+|w|+1)/((2:ℝ)^k-w))<(n:ℝ) :=
      big.trans (by exact_mod_cast far.1)
    have mul := (div_lt_iff₀ delta).mp above
    nlinarith only [mul,le_abs_self w,show 0≤(2:ℝ)^k by positivity]

/-- If every tripling defect starts at a multiple of three, its dyadic
descendants supply exactly the dyadic squared norm at every depth. -/
theorem fixed_nonunit_norm {q : ℕ} (positive : 0<q) (dq : tripleDefect q)
    (allNonunit : ∀ n, tripleDefect n → n%3=0) (k H : ℕ) :
    squaredNorm k H tripleDefect=(2:ℝ)^k :=
  dyadic_norm positive (fun j => (triple_double j q).mpr dq) allNonunit k H

theorem full_dyadic_lower (k : ℕ) : (2:ℝ)^k≤squaredNorm k 0 (fun _ => True) := by
  have eqn := dyadic_norm (P:=fun n => n%3=0) (q:=3) (by decide)
    (fun j => by simp) (fun _ h => h) k 0
  rw [←eqn]
  exact norm_le_full ..

theorem universal_iff_fixed_gap (k H : ℕ) :
    Universal ↔ squaredNorm k H tripleDefect<(2:ℝ)^k := by
  constructor
  · intro all
    rw [norm_zero (P:=tripleDefect) (fun n large dq => by
      obtain ⟨i,hi⟩ := all n (by omega)
      obtain ⟨j,hj⟩ := all (3*n) (by omega)
      exact dq ⟨i,j,hi.trans hj.symm⟩)]
    positivity
  · intro small
    by_contra failure
    have existsBad : ∃ q, 0<q ∧ tripleDefect q := by
      by_contra! none
      apply failure
      apply TowerRecurrence.universal_of_odd_tripling
      intro x odd
      exact meet_labels (Classical.byContradiction (none x (by omega)))
    obtain ⟨q,pos,dq⟩ := existsBad
    by_cases unitDefect : ∃ u, u%3≠0 ∧ tripleDefect u
    · obtain ⟨u,uu,du⟩ := unitDefect
      rw [fixed_unit_full uu du] at small
      exact (not_lt_of_ge (full_dyadic_lower k)) small
    · push Not at unitDefect
      have nonunit (n : ℕ) (bad : tripleDefect n) : n%3=0 := by
        by_contra no
        exact unitDefect n no bad
      rw [fixed_nonunit_norm pos dq nonunit] at small
      exact lt_irrefl _ small

#print axioms selected_norm_dichotomy
#print axioms fixed_unit_full
#print axioms fixed_nonunit_norm
#print axioms universal_iff_fixed_gap
end Collatz.Itinerary.BergmanRelative
