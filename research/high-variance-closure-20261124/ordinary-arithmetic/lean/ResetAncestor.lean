import Mathlib
import QuarterShift

/-! Exact ordinary ancestor minimization and the equal-cost edge at 8 modulo 18.
The marking rate is any natural function bounded by one. -/

namespace ResetAncestor

open QuarterShift

private theorem endpointLast (k m : ℕ) : endpoint (k+1) m = step (endpoint k m) := by
  induction k generalizing m with
  | zero => rfl
  | succ k ih => exact ih (step m)

/-- Traversal cost, excluding the terminal vertex. -/
def cost (rate : ℕ → ℕ) (m : ℕ) : ℕ → ℕ
  | 0 => 0
  | k+1 => cost rate m k + rate (endpoint k m)

private def bills (rate : ℕ → ℕ) (n : ℕ) : Set ℕ :=
  {v | ∃ m k, 0 < m ∧ endpoint k m = n ∧ m + cost rate m k = v}

/-- Least positive ancestor price plus its traversal cost. -/
noncomputable def toll (rate : ℕ → ℕ) (n : ℕ) : ℕ := sInf (bills rate n)

private theorem attained (rate : ℕ → ℕ) (n : ℕ) (hn : 0 < n) :
    toll rate n ∈ bills rate n := by
  apply Nat.sInf_mem
  exact ⟨n, n, 0, hn, rfl, by simp [cost]⟩

private theorem leBill (rate : ℕ → ℕ) {m k n : ℕ} (hm : 0 < m) (h : endpoint k m = n) :
    toll rate n ≤ m + cost rate m k := Nat.sInf_le ⟨m,k,hm,h,rfl⟩

private theorem extend (rate : ℕ → ℕ) {n : ℕ} (hn : 0 < n) :
    toll rate (step n) ≤ toll rate n + rate n := by
  obtain ⟨m,k,hm,hend,hbill⟩ := attained rate n hn
  have he : endpoint (k+1) m = step n := by rw [endpointLast, hend]
  have hl := leBill rate hm he
  simpa [cost, hend, ←hbill, Nat.add_assoc] using hl

/-- At a target with one incoming edge this is the exact dynamic-programming law. -/
theorem uniqueParent (rate : ℕ → ℕ) {n z : ℕ} (hn : 0 < n) (hz : 0 < z)
    (he : step n = z) (hu : ∀ m, step m = z → m = n) :
    toll rate z = min z (toll rate n + rate n) := by
  apply le_antisymm
  · apply le_min
    · simpa [cost, endpoint] using (leBill (k := 0) rate hz (n := z) rfl)
    · simpa [he] using extend rate hn
  · obtain ⟨m,k,hm,hend,hbill⟩ := attained rate z hz
    cases k with
    | zero =>
      simp [endpoint] at hend
      simp [cost] at hbill
      omega
    | succ k =>
      have hp := hu (endpoint k m) ((endpointLast k m).symm.trans hend)
      have hl := leBill rate hm hp
      simp only [cost, hp] at hbill
      omega

/-- Every marked source 8 mod 18 above the small cutoff has zero ancestor debit. -/
theorem equalToll (rate : ℕ → ℕ) (hr : ∀ m, rate m ≤ 1) {n : ℕ}
    (hlarge : 26 ≤ n) (hres : n % 18 = 8) (hmark : rate n = 0) :
    toll rate n = toll rate (step n) := by
  let m := (4*n-5)/9
  have hn : 0 < n := by omega
  have hn2 : n % 2 = 0 := by omega
  have hz : step n = n/2 := by simp [step, hn2]
  have hu : ∀ u, step u = step n → u = n := by
    intro u h
    rw [hz] at h
    unfold step at h
    split at h <;> omega
  have hm : 0 < m := by dsimp [m]; omega
  have hm2 : m % 2 = 1 := by dsimp [m]; omega
  have hstep : step m = (2*n-1)/3 := by simp [step, hm2, m]; omega
  have hs2 : ((2*n-1)/3) % 2 = 1 := by omega
  have hend : endpoint 2 m = n := by
    change step (step m) = n
    rw [hstep]
    simp [step, hs2]
    omega
  have hcost : cost rate m 2 ≤ 2 := by
    have h1 := hr m
    have h2 := hr (step m)
    simpa [cost,endpoint] using show rate m + rate (step m) ≤ 2 by omega
  have hl := leBill rate hm hend
  have hcheap : m + 2 ≤ n/2 := by dsimp [m]; omega
  have hb : toll rate n ≤ step n := by rw [hz]; omega
  rw [uniqueParent rate hn (by rw [hz]; omega) rfl hu, hmark, Nat.add_zero, min_eq_right hb]

/-- A delayed collision at ordinary sources whose first d inputs are even. -/
theorem delayedMerge (d u : ℕ) (hu : u % 2 = 1) :
    endpoint d (2^d * u) = u ∧
    endpoint d (2^d * (3*u+1)) = 3*u+1 ∧
    endpoint (d+1) (2^d * u) = endpoint (d+1) (2^d * (3*u+1)) := by
  have a := (even_run d u).1
  have b := (even_run d (3*u+1)).1
  refine ⟨a,b,?_⟩
  rw [endpointLast, endpointLast, a,b]
  have hh : (3*u+1) % 2 = 0 := by omega
  simp [step, hu, hh]

/-- One of the distinct last vertices in the delayed collision is nonperiodic. -/
theorem nonperiodicBranch (u : ℕ) (hu : u % 2 = 1) :
    u ∉ Function.periodicPts step ∨ 3*u+1 ∉ Function.periodicPts step := by
  by_contra! h
  obtain ⟨a,ha,hp⟩ := Function.mem_periodicPts.mp h.1
  obtain ⟨b,hb,hq⟩ := Function.mem_periodicPts.mp h.2
  have hstep : step u = step (3*u+1) := by
    have hh : (3*u+1) % 2 = 0 := by omega
    simp [step, hu, hh]
  have hsame := hp.eq_of_apply_eq hq ha hb hstep
  omega

#print axioms uniqueParent
#print axioms equalToll
#print axioms delayedMerge
#print axioms nonperiodicBranch

end ResetAncestor
