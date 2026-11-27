import FiniteTrace
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Data.Finset.Max

/-! Ordinary Collatz preimage fibers of a fixed even-input count. -/
namespace Collatz.ReciprocalRigidity.FiberInterval

open FiniteTrace

/-- Even and odd site counts are taken *before* each of the first k updates. -/
def evens : ℕ → ℕ → ℕ
  | 0, _ => 0
  | k+1, n => (if n%2=0 then 1 else 0) + evens k (step n)

def odds : ℕ → ℕ → ℕ
  | 0, _ => 0
  | k+1, n => (if n%2=0 then 0 else 1) + odds k (step n)

theorem counts_sum (k n : ℕ) : evens k n+odds k n=k := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih =>
    simp only [evens,odds];have := ih (step n); split <;> omega

/-- The two rational interval endpoints are cleared using a positive denominator. -/
theorem endpoint_band (k n : ℕ) :
    3^(odds k n)*(n+1) ≤ 2^k*(orbit k n+1) ∧
    2^k*(orbit k n+1) ≤ 3^(odds k n)*(n+2^(evens k n)) := by
  induction k generalizing n with
  | zero => simp [odds,evens,orbit]
  | succ k ih =>
    let u:=n/2
    by_cases h : n%2=0
    · have hn : n=2*u := by dsimp [u];omega
      have hs : step n=u := by simp [step,h,u]
      obtain ⟨hl,hr⟩ := ih u
      simp only [odds,evens,orbit,h,↓reduceIte,zero_add,hs]
      have hlow : n+1≤2*(u+1) := by omega
      constructor
      · calc
          3^(odds k u)*(n+1) ≤ 3^(odds k u)*(2*(u+1)) := Nat.mul_le_mul_left _ hlow
          _ = 2*(3^(odds k u)*(u+1)) := by ring
          _ ≤ 2*(2^k*(orbit k u+1)) := Nat.mul_le_mul_left 2 hl
          _ = _ := by rw [pow_succ];ring
      · calc
          2^(k+1)*(orbit k u+1)=2*(2^k*(orbit k u+1)) := by rw [pow_succ];ring
          _ ≤ 2*(3^(odds k u)*(u+2^(evens k u))) := Nat.mul_le_mul_left 2 hr
          _ = _ := by rw [hn, pow_add];ring
    · have hn : n=2*u+1 := by dsimp [u];omega
      have hs : step n=3*u+2 := by unfold step;simp [h];omega
      let v:=3*u+2
      obtain ⟨hl,hr⟩ := ih v
      simp only [odds,evens,orbit,h,↓reduceIte,zero_add,hs]
      change 3^(1+odds k v)*(n+1) ≤2^(k+1)*(orbit k v+1) ∧
        _ ≤3^(1+odds k v)*(n+2^(evens k v))
      have hupper : 2*(v+2^(evens k v))≤3*(n+2^(evens k v)) := by
        have hpos : 0<2^(evens k v) := by positivity
        dsimp [v] at hpos ⊢;omega
      constructor
      · calc
          3^(1+odds k v)*(n+1) = 2*(3^(odds k v)*(v+1)) := by
            rw [hn,pow_add];dsimp [v];ring
          _ ≤ 2*(2^k*(orbit k v+1)) := Nat.mul_le_mul_left 2 hl
          _ = _ := by rw [pow_succ];ring
      · calc
          2^(k+1)*(orbit k v+1)=2*(2^k*(orbit k v+1)) := by rw [pow_succ];ring
          _ ≤ 2*(3^(odds k v)*(v+2^(evens k v))) := Nat.mul_le_mul_left 2 hr
          _ = 3^(odds k v)*(2*(v+2^(evens k v))) := by ring
          _ ≤ 3^(odds k v)*(3*(n+2^(evens k v))) := Nat.mul_le_mul_left _ hupper
          _ = _ := by rw [pow_add];ring

theorem equal_fiber_diameter {n m k j : ℕ} (ho : orbit k n=orbit k m)
    (hn : evens k n=j) (hm : evens k m=j) : n+1≤m+2^j := by
  have hcm := counts_sum k m
  have hcn := counts_sum k n
  have he : odds k n=odds k m := by omega
  have h := (endpoint_band k n).1
  rw [ho,he] at h
  have hb := h.trans (endpoint_band k m).2
  rw [hm] at hb
  exact Nat.le_of_mul_le_mul_left hb (by positivity)

theorem finite_fiber_card {S : Finset ℕ} {k j y : ℕ}
    (hS : ∀ n∈S, orbit k n=y ∧ evens k n=j) : S.card≤2^j := by
  classical
  by_cases hn : S.Nonempty
  · let a:=S.min' hn
    have ha : a∈S := S.min'_mem hn
    have hh := hS a ha
    have hs : S⊆Finset.Ico a (a+2^j) := by
      intro n h
      have h' := hS n h
      exact Finset.mem_Ico.mpr ⟨S.min'_le n h,
        by have := equal_fiber_diameter (h'.1.trans hh.1.symm) h'.2 hh.2;omega⟩
    simpa using Finset.card_le_card hs
  · have he : S=∅ := Finset.not_nonempty_iff_eq_empty.mp hn
    simp [he]

/-- The bound covers the complete physical fiber; its defining finite cutoff
follows from the lower endpoint estimate and loses no positive starting value. -/
def fiber (k y j : ℕ) : Finset ℕ :=
  (Finset.Icc 1 (2^k*(y+1))).filter fun n => orbit k n=y ∧ evens k n=j

theorem mem_fiber {k y j n : ℕ} :
    n∈fiber k y j ↔ 0<n ∧ orbit k n=y ∧ evens k n=j := by
  simp only [fiber,Finset.mem_filter,Finset.mem_Icc]
  constructor
  · rintro ⟨⟨hl,_⟩,ho,he⟩;exact ⟨hl,ho,he⟩
  · rintro ⟨hl,ho,he⟩
    have h := (endpoint_band k n).1
    rw [ho] at h
    have h1 : 1≤3^(odds k n) := Nat.one_le_pow _ _ (by decide)
    have hb := Nat.mul_le_mul_right (n+1) h1
    simp only [one_mul] at hb
    exact ⟨⟨hl,by omega⟩,ho,he⟩

theorem fiber_card (k y j : ℕ) : (fiber k y j).card≤2^j :=
  finite_fiber_card fun _ h => (mem_fiber.mp h).2

#print axioms endpoint_band
#print axioms fiber_card
end Collatz.ReciprocalRigidity.FiberInterval
