import GapNumeratorFiber
import Mathlib.Data.Nat.ModEq
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Group.Finset.Sigma
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Linarith

/-! Finite arithmetic for stopped inverse cost, using positive actual integer paths. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.StoppedCorridor
open GapNumeratorFiber

/-- All cumulative gap costs satisfy q*S_j <= p*j+c. The list is reversed. -/
def Fits (p q c : ℕ) : List ℕ → Prop
  | [] => True
  | k :: w => Fits p q c w ∧ q * clock (k :: w) ≤ p * (w.length + 1) + c

def Survives (p q c n x : ℕ) : Prop :=
  ∃ w y, w.length = n ∧ Fits p q c w ∧ Follows w x y ∧ y % 3 ≠ 0

private theorem source_unit_of_edge {k z y : ℕ}
    (he : 2 ^ (k + 1) * z = 3 * y + 1) : z % 3 ≠ 0 := by
  intro hz
  have hm := congrArg (· % 3) he
  rw [Nat.mul_mod, hz] at hm
  simp only [Nat.mul_zero, Nat.zero_mod] at hm
  omega

theorem survives_prefix {p q c n x : ℕ} (h : Survives p q c (n + 1) x) :
    Survives p q c n x := by
  obtain ⟨w,y,hl,hfit,hw,_⟩ := h
  cases w with
  | nil => simp at hl
  | cons k w =>
    obtain ⟨z,hz,he⟩ := hw
    exact ⟨w,z,by simpa using hl,hfit.1,hz,source_unit_of_edge he⟩

/-- Changing a positive supplied lift preserves the word and r endpoint trits. -/
theorem follows_change_source {w : List ℕ} {x y x' r : ℕ} (hw : Follows w x y)
    (hx' : 0 < x') (hmod : x' ≡ x [MOD 3 ^ (w.length + r)]) :
    ∃ y' > 0, Follows w x' y' ∧ y' ≡ y [MOD 3 ^ r] := by
  induction w generalizing x y x' r with
  | nil =>
    change x = y at hw
    subst y
    exact ⟨x',hx',rfl,by simpa using hmod⟩
  | cons k w ih =>
    obtain ⟨z,hz,he⟩ := hw
    have h1 : x' ≡ x [MOD 3 ^ (w.length + (r + 1))] := by
      simpa only [List.length_cons, Nat.add_assoc, Nat.add_comm 1 r] using hmod
    obtain ⟨z',hzpos,hz',hm⟩ := ih hz hx' h1
    have hm1 : 2 ^ (k + 1) * z' ≡ 3 * y + 1 [MOD 3 * 3 ^ r] := by
      rw [← he]
      simpa only [pow_succ 3 r, Nat.mul_comm (3 ^ r) 3] using hm.mul_left (2 ^ (k+1))
    have h3 : 2 ^ (k + 1) * z' ≡ 3 * y + 1 [MOD 3] :=
      hm1.of_dvd (dvd_mul_right 3 (3 ^ r))
    change (2 ^ (k + 1) * z') % 3 = (3 * y + 1) % 3 at h3
    have htwo : 2 ≤ 2 ^ (k + 1) := by
      rw [pow_succ]; have := Nat.two_pow_pos k; omega
    have hpos : 2 ≤ 2 ^ (k + 1) * z' :=
      le_trans htwo (Nat.le_mul_of_pos_right _ hzpos)
    let y' := (2 ^ (k + 1) * z') / 3
    have ha : 2 ^ (k + 1) * z' = 3 * y' + 1 := by dsimp [y']; omega
    have hyp : 0 < y' := by omega
    rw [ha] at hm1
    exact ⟨y',hyp,⟨z',hz',ha⟩,Nat.ModEq.mul_left_cancel' (by decide : 3 ≠ 0)
      (Nat.ModEq.add_right_cancel' 1 hm1)⟩

/-- Every finite corridor test is constant on positive source cells of depth n+1. -/
theorem survives_congr {p q c n x x' : ℕ} (hx : 0 < x) (hx' : 0 < x')
    (hm : x' ≡ x [MOD 3 ^ (n + 1)]) : Survives p q c n x' ↔ Survives p q c n x := by
  suffices ht : ∀ {a b : ℕ}, 0 < b → b ≡ a [MOD 3 ^ (n + 1)] →
      Survives p q c n a → Survives p q c n b from ⟨ht hx hm.symm, ht hx' hm⟩
  intro a b hb hab h
  obtain ⟨w,y,hl,hfit,hw,hy⟩ := h
  obtain ⟨z,_,hz,hmz⟩ := follows_change_source (r := 1) hw hb (hl ▸ hab)
  have he : z % 3 = y % 3 := by simpa only [Nat.ModEq, pow_one] using hmz
  exact ⟨w,z,hl,hfit,hz,he ▸ hy⟩

private theorem repair_table : ∀ r : Fin 9, ∀ t : Fin 3, (r : ℕ) % 3 ≠ 0 →
    (t : ℕ) ≠ 0 → ∃ j : Fin 6, (2 ^ ((j : ℕ) + 1) * (r : ℕ)) % 9 = 3 * (t : ℕ) + 1 := by
  decide

/-- One positive legal gap, at most six, lands in the prescribed nonzero trit. -/
theorem actual_trit_repair (x t : ℕ) (hx : x % 3 ≠ 0) (ht : 0 < t) (ht3 : t < 3) :
    ∃ j < 6, ∃ y > 0, 2 ^ (j + 1) * x = 3 * y + 1 ∧ y % 3 = t ∧ y % 2 = 1 := by
  obtain ⟨j,hj⟩ := repair_table ⟨x % 9,Nat.mod_lt _ (by decide)⟩ ⟨t,ht3⟩
    (by change (x % 9) % 3 ≠ 0; rwa [Nat.mod_mod_of_dvd x (by decide : 3 ∣ 9)]) (by change t ≠ 0; omega)
  change (2 ^ ((j : ℕ) + 1) * (x % 9)) % 9 = 3*t+1 at hj
  have he : (2 ^ ((j : ℕ) + 1) * x) % 9 = 3*t+1 := by
    rw [Nat.mul_mod] at hj ⊢
    simpa only [Nat.mod_mod] using hj
  let y := 3 * ((2 ^ ((j : ℕ) + 1) * x) / 9) + t
  have ha : 2 ^ ((j : ℕ) + 1) * x = 3*y+1 := by dsimp [y]; omega
  have heven : 2 ^ ((j : ℕ) + 1) * x = 2 * (2 ^ (j : ℕ) * x) := by rw [pow_succ]; ring
  exact ⟨j,j.isLt,y,by dsimp [y]; omega,ha,by dsimp [y]; omega,by omega⟩

/-- Append the return-trit step to any actual stopping witness. -/
theorem append_repair {p q c n x t : ℕ} (h : Survives p q c n x) (ht : 0<t) (ht3 : t<3) :
    ∃ v y, v.length = n+1 ∧ Follows v x y ∧ y % 3 = t ∧ y % 2 = 1 ∧
      q * clock v ≤ p*n+c+6*q := by
  obtain ⟨w,z,hl,hfit,hw,hz⟩ := h
  obtain ⟨j,hj,y,_,he,hy,ho⟩ := actual_trit_repair z t hz ht ht3
  have hcost : q*clock w ≤ p*n+c := by
    cases w with
    | nil => simp [clock] at hl ⊢
    | cons k w => simpa only [← hl, List.length_cons] using hfit.2
  refine ⟨j::w,y,by simp [hl],⟨z,hw,he⟩,hy,ho,?_⟩
  have hemax : q*(j+1) ≤ 6*q := by simpa [Nat.mul_comm] using Nat.mul_le_mul_right q (show j+1≤6 by omega)
  change q*((j+1)+clock w) ≤ _
  rw [Nat.mul_add]
  omega

open Finset

/-- Exact finite tail sum, counted once per surviving depth on each source. -/
def survivalCount {ι : Type*} (s : Finset ι) (J : ι→ℕ) (N : ℕ) : ℕ :=
  ∑ j ∈ range (N+1), (s.filter fun x => j≤J x).card

theorem survivalCount_eq {ι : Type*} (s : Finset ι) (J : ι→ℕ) (N : ℕ)
    (hJ : ∀ x∈s, J x ≤ N) : survivalCount s J N = ∑ x∈s, (J x + 1) := by
  classical
  unfold survivalCount
  simp_rw [Finset.card_filter]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro x hx
  have hf : (range (N+1)).filter (fun j => j≤J x) = range (J x+1) := by
    ext j
    simp only [mem_filter, mem_range]
    have := hJ x hx
    omega
  simp only [← Finset.sum_filter, hf, Finset.sum_const, Finset.card_range, Nat.nsmul_eq_mul, Nat.mul_one]

/-- Finite regenerative ratio bound on arbitrary equally weighted stopping cells.
Refining to maximum precision makes the actual input cells equally weighted. -/
theorem stopped_reward {ι : Type*} (s : Finset ι) (J : ι→ℕ) (N : ℕ)
    (cost : ι→ℚ) (L a c : ℚ) (hJ : ∀ x∈s, J x ≤ N)
    (hcost : ∀ x∈s, cost x ≤ a * (J x : ℚ)+c+6)
    (hL : L * (∑ x∈s, ((J x : ℚ)+1)) ≤ ∑ x∈s, cost x) :
    (L-a)*(survivalCount s J N : ℚ) ≤ (c+6-a)*(s.card : ℚ) := by
  have hb : (∑ x∈s, cost x) ≤ a*(∑ x∈s, ((J x : ℚ)+1))+(c+6-a)*(s.card : ℚ) := by
    calc
      (∑ x∈s, cost x) ≤ ∑ x∈s, (a*((J x : ℚ)+1)+(c+6-a)) := by
        apply Finset.sum_le_sum
        intro x hx
        linarith [hcost x hx]
      _ = _ := by rw [Finset.sum_add_distrib, ← Finset.mul_sum]; simp [mul_comm]; ring
  rw [survivalCount_eq s J N hJ, Nat.cast_sum]
  simp only [Nat.cast_add, Nat.cast_one]
  linarith

end Collatz.StoppedCorridor
