module

public import BergmanDistance
import all BergmanRelative
import all BergmanDistance
import all TernaryItinerary
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.BergmanRelative

set_option autoImplicit false

private theorem label_run (F : ℕ → Prop) (invariant : ∀ x, F (step x) ↔ F x) (s x : ℕ) :
    F (run s x) ↔ F x := by
  induction s generalizing x with
  | zero => rfl
  | succ s ih => exact (ih (step x)).trans (invariant x)

/-- The PR 146 descent, with an arbitrary invariant component label.
The ordinary-basin specialization is TowerRecurrence.universal_of_odd_tripling. -/
theorem label_descent (F : ℕ → Prop) (invariant : ∀ x, F (step x) ↔ F x)
    (start : F 1) (trip : ∀ n, n%2=1 → (F n ↔ F (3*n))) : ∀ n, 0<n → F n := by
  have runLabel := label_run F invariant
  have scaling (e x : ℕ) : F (2^e*x) ↔ F x := by
    have h := runLabel e (2^e*x)
    rwa [halve,iff_comm] at h
  have equal_labels {a b h j : ℕ} (eq : run h a=run j b) : F a ↔ F b := by
    exact (runLabel h a).symm.trans (eq.symm ▸ runLabel j b)
  have powers (k n : Nat) (odd : n%2=1) : F n ↔ F (3^k*n) := by
    induction k with
    | zero => simp
    | succ k ih =>
      have o : (3^k*n)%2=1 := by simp [Nat.mul_mod,Nat.pow_mod,odd]
      simpa only [Nat.pow_succ,Nat.mul_right_comm,Nat.mul_comm 3] using
        ih.trans (trip _ o)
  have exchange (k m : Nat) (pos : 0<m) : F (2^k*m-1) ↔ F (3^k*m-1) := by
    apply equal_labels (h:=k) (j:=0)
    simpa using BasinTransport.affine_rays k 0 0 m pos
  have double_shift (m : Nat) (pos : 0<m) : F (4*m-1) ↔ F (8*m-1) := by
    have ray := exchange 2 m pos
    change F (4*m-1) ↔ F (9*m-1) at ray
    have link : F (3*(8*m-1)) ↔ F (9*m-1) := by
      have actual : run 1 (3*(8*m-1))=4*(9*m-1) := by
        change step (3*(8*m-1))=4*(9*m-1)
        unfold step; split <;> omega
      have down := runLabel 1 (3*(8*m-1))
      rw [actual] at down
      exact down.symm.trans (scaling 2 (9*m-1))
    exact ray.trans ((trip (8*m-1) (by omega)).trans link).symm
  have extra (i h : Nat) (pos : 0<h) :
      F (4*h-1) ↔ F (4*(2^i*h)-1) := by
    induction i with
    | zero => simp
    | succ i ih =>
      have more := double_shift (2^i*h) (Nat.mul_pos (Nat.pow_pos (by decide)) pos)
      rw [show 4*(2^(i+1)*h)=8*(2^i*h) by rw [Nat.pow_succ]; grind]
      exact ih.trans more
  have cell (y : Nat) (tag : y%16=3 ∨ y%16=5) : F (y-1) ↔ F y := by
    rcases tag with h | h
    · apply equal_labels (h:=4) (j:=4)
      simp only [run]; unfold step; repeat' first | omega | split
    · apply equal_labels (h:=3) (j:=3)
      simp only [run]; unfold step; repeat' first | omega | split
  have table : ∀ z : Fin 16, z.val%2=1 → ∃ i : Fin 4,
      (3^i.val*z.val)%16=3 ∨ (3^i.val*z.val)%16=5 := by decide
  have descend (h : Nat) (pos : 0<h) : F (4*h-1) ↔ F h := by
    obtain ⟨v,u,eq,odd⟩ := split_twos h pos
    let z := 3^(v+2)*u
    have oz : z%2=1 := by simp [z,Nat.mul_mod,Nat.pow_mod,odd]
    obtain ⟨i,hit⟩ := table ⟨z%16,by omega⟩ (by change z%16%2=1; omega)
    let t := i.val+(v+2)
    have pair : 3^t*u=3^i.val*z := by simp [t,z,Nat.pow_add,Nat.mul_assoc]
    have md : (3^t*u)%16=(3^i.val*(z%16))%16 := by rw [pair,Nat.mul_mod]; simp [Nat.mul_mod]
    have tag : (3^t*u)%16=3 ∨ (3^t*u)%16=5 := by rw [md]; exact hit
    have align : 4*(2^i.val*h)=2^t*u := by rw [eq]; simp only [t,Nat.pow_add]; grind
    calc
      F (4*h-1) ↔ F (4*(2^i.val*h)-1) := extra i.val h pos
      _ ↔ F (3^t*u-1) := by rw [align]; exact exchange t u (by omega)
      _ ↔ F (3^t*u) := cell _ tag
      _ ↔ F u := (powers t u odd).symm
      _ ↔ F h := by rw [eq]; exact (scaling v u).symm
  intro n
  induction n using Nat.strongRecOn with
  | ind n ih =>
    intro pos
    by_cases one : n=1
    · subst n; exact start
    by_cases even : n%2=0
    · have eq : n=2*(n/2) := by omega
      have done : F (2*(n/2)) := (scaling 1 (n/2)).mpr
        (ih (n/2) (by omega) (by omega))
      rwa [←eq] at done
    by_cases rem : n%4=1
    · have hit : run 2 n=(3*n+1)/4 := by simp only [run]; unfold step; split <;> split <;> omega
      apply (runLabel 2 n).mp
      rw [hit]; exact ih _ (by omega) (by omega)
    · let h := (n+1)/4
      have eq : n=4*h-1 := by dsimp [h]; omega
      have small : h<n := by dsimp [h]; omega
      have posH : 0<h := by dsimp [h]; omega
      exact eq ▸ (descend h posH).mpr (ih h small posH)

private theorem label_tower (F : ℕ → Prop) (invariant : ∀ x, F (step x) ↔ F x)
    (start : F 1) (different : ¬∀ n, 0<n → F n) :
    ∃ u r, u%2=1 ∧ u%3≠0 ∧ ¬(F u ↔ F (3^(r+1)*u)) := by
  have split3 (n : ℕ) (pos : 0<n) : ∃ v u, n=3^v*u ∧ u%3≠0 := by
    obtain ⟨v,u,unit,eqn⟩ := Nat.exists_eq_pow_mul_and_not_dvd (by omega : n≠0) 3 (by decide)
    exact ⟨v,u,eqn,fun zero => unit (Nat.dvd_of_mod_eq_zero zero)⟩
  by_contra! all
  apply different
  apply label_descent F invariant start
  intro n no
  obtain ⟨v,u,rfl,uu⟩ := split3 n (by omega)
  have uo : u%2=1 := by
    simpa only [Nat.mul_mod,Nat.pow_mod,show 3%2=1 by decide,one_pow,Nat.one_mod,
      Nat.one_mul,Nat.mod_mod] using no
  have levels (j : ℕ) : F u ↔ F (3^j*u) := by
    cases j with
    | zero => simp
    | succ j => exact all u j uo uu
  rw [show 3*(3^v*u)=3^(v+1)*u by ring]
  exact (levels v).symm.trans (levels (v+1))



/-- Every nonconstant component projection detects the entire transfer
row supremum through its crossing rows, even after an arbitrary height cut. -/
theorem nonconstant_projection_full (P : ℕ → Prop) (invariant : ∀ x, P (step x) ↔ P x)
    (different : ∃ n, 0<n ∧ ¬(P n ↔ P 1)) (k H : ℕ) :
    squaredNorm k H (fun n => n%3≠0 ∧ ¬(P n ↔ P (target n)))=
      squaredNorm k 0 (fun _ => True) := by
  let F (n : ℕ) := P n ↔ P 1
  have iv (x : ℕ) : F (step x) ↔ F x := iff_congr (invariant x) Iff.rfl
  have diff : ¬∀ n, 0<n → F n := by
    obtain ⟨n,pos,bad⟩ := different
    exact fun all => bad (all n pos)
  obtain ⟨u,r,uo,uu,change⟩ := label_tower F iv Iff.rfl diff
  have scale (j x : ℕ) : P (2^j*x) ↔ P x := by
    have h := label_run P invariant j (2^j*x)
    rwa [halve,iff_comm] at h
  apply norm_eq_full
  intro a
  obtain ⟨j,_,large,tag,row⟩ := ray_row uo uu r k a (max H 3)
  have unit : (2^j*u)%3≠0 := by
    have cop : Nat.Coprime (2^j) 3 := (show Nat.Coprime 2 3 by decide).pow_left _
    intro zero
    have dvd : 3∣2^j*u := Nat.dvd_of_mod_eq_zero zero
    exact uu (Nat.mod_eq_zero_of_dvd (cop.symm.dvd_of_dvd_mul_left dvd))
  refine ⟨_,large,⟨unit,?_⟩,row⟩
  intro same
  rw [target,tag,show 3^(r+1)*(2^j*u)=2^j*(3^(r+1)*u) by ring] at same
  exact change (iff_congr ((scale j u).symm.trans (same.trans (scale j _))) Iff.rfl)

#print axioms label_descent
#print axioms nonconstant_projection_full
end Collatz.Itinerary.BergmanRelative
