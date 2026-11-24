import Mathlib
import QuarterShift

namespace DyadicCompanion

open QuarterShift

/-- Natural-number numerator dynamics for a positive companion of denominator d. -/
def Coupled (d x u y v : ℕ) : Prop :=
  (2*y = x ∧ 2*v = 3*u) ∨
  (2*y = 3*x+1 ∧ 4*v = 3*u+d)

/-- The same integral height decreases strictly in both legal branches. -/
theorem heightDrop {d x u y v : ℕ} (hd : 0 < d) (hx : 20 ≤ x) (hu : 64*d ≤ u)
    (h : Coupled d x u y v) : y^2*v^3 < x^2*u^3 := by
  have hprod : 0 < x^2*u^3 := by
    have : 0 < u := by omega
    positivity
  rcases h with ⟨hy,hv⟩ | ⟨hy,hv⟩
  · have he : 32*(y^2*v^3) = 27*(x^2*u^3) := by
      calc 32*(y^2*v^3) = (2*y)^2*(2*v)^3 := by ring
           _ = 27*(x^2*u^3) := by rw [hy,hv]; ring
    omega
  · have h1 : 20*(2*y) ≤ 61*x := by omega
    have h2 : 64*(4*v) ≤ 193*u := by omega
    have hb := Nat.mul_le_mul (Nat.pow_le_pow_left h1 2) (Nat.pow_le_pow_left h2 3)
    have hc : 61^2*193^3 < 20^2*64^3*256 := by decide
    nlinarith only [hb, Nat.mul_lt_mul_of_pos_right hc hprod]

/-- Every all-time coupled path above the physical floor has a small companion numerator. -/
theorem visitsSmall (d : ℕ) (hd : 0 < d) (x u : ℕ → ℕ)
    (hx : ∀ i, 20 ≤ x i) (h : ∀ i, Coupled d (x i) (u i) (x (i+1)) (u (i+1))) :
    ∃ i, u i < 64*d := by
  classical
  by_contra! hall
  let R : ℕ → ℕ := fun i => (x i)^2*(u i)^3
  have hex : ∃ m, ∃ i, R i = m := ⟨R 0,0,rfl⟩
  obtain ⟨i,hi⟩ := Nat.find_spec hex
  have hl : R (i+1) < Nat.find hex := hi ▸ heightDrop hd (hx i) (hall i) (h i)
  exact (Nat.find_min hex hl) ⟨i+1,rfl⟩

def aux (u : ℕ) : ℕ := if u%2 = 0 then 3*u/2 else (3*u+1)/4

def auxAt : ℕ → ℕ → ℕ
  | 0, u => u
  | j+1, u => auxAt j (aux u)

/-- All integral companions 2 through 63 reach the forbidden class by clock 17. -/
theorem smallFails : ∀ u : Fin 64, 2 ≤ u.val →
    ∃ j : Fin 18, auxAt j.val u.val % 4 = 3 := by
  set_option maxRecDepth 10000 in decide

private theorem noAllOdd (x : ℕ → ℕ) (h : ∀ i, 2*(x (i+1))=3*x i+1) : False := by
  have he (k : ℕ) : 2^k*(x k+1)=3^k*(x 0+1) := by
    induction k with
    | zero => simp
    | succ k ih =>
      have hn : 2*(x (k+1)+1)=3*(x k+1) := by have := h k; omega
      calc 2^(k+1)*(x (k+1)+1) = 2^k*(2*(x (k+1)+1)) := by rw [pow_succ]; ring
           _ = 3*(2^k*(x k+1)) := by rw [hn]; ring
           _ = 3^(k+1)*(x 0+1) := by rw [ih,pow_succ]; ring
  let k := x 0+1
  have hc : Nat.Coprime (2^k) (3^k) := ((by decide : Nat.Coprime 2 3).pow_left k).pow_right k
  have hd : 2^k ∣ 3^k*(x 0+1) := ⟨x k+1,(he k).symm⟩
  have hle := Nat.le_of_dvd (by omega : 0<x 0+1) (hc.dvd_of_dvd_mul_left hd)
  have hlt : k < 2^k := Nat.lt_two_pow_self
  omega

private theorem deterministic {x u y v : ℕ} (h : Coupled 1 x u y v) :
    v=aux u ∧ u%4≠3 := by
  rcases h with ⟨_,hv⟩ | ⟨_,hv⟩
  · have he : u%2=0 := by omega
    simp [aux,he]
    omega
  · have ho : u%2≠0 := by omega
    simp [aux,ho]
    omega

/-- No positive ordinary path can stay above 20 with an all-time positive integral companion. -/
theorem integralCompanionImpossible (x u : ℕ → ℕ) (hx : ∀ i, 20 ≤ x i)
    (hu : ∀ i, 0 < u i)
    (h : ∀ i, Coupled 1 (x i) (u i) (x (i+1)) (u (i+1))) : False := by
  obtain ⟨i,hi⟩ := visitsSmall 1 (by decide) x u hx h
  have det (j : ℕ) : u (j+1)=aux (u j) ∧ u j%4 ≠ 3 := deterministic (h j)
  by_cases he : u i=1
  · have h1 (j : ℕ) : u (i+j)=1 := by
      induction j with
      | zero => simpa using he
      | succ j ih => rw [← Nat.add_assoc, (det (i+j)).1, ih]; decide
    apply noAllOdd (fun j => x (i+j))
    intro j
    rcases h (i+j) with ⟨_,hv⟩ | ⟨hy,_⟩
    · rw [h1 j] at hv
      omega
    · simpa [Nat.add_assoc] using hy
  · let a : Fin 64 := ⟨u i,by omega⟩
    obtain ⟨j,hj⟩ := smallFails a (by dsimp [a]; have := hu i; omega)
    have ha (j t : ℕ) : auxAt j (u t) = u (t+j) := by
      induction j generalizing t with
      | zero => simp [auxAt]
      | succ j ih => rw [auxAt,← (det t).1,ih]; congr 1; omega
    exact (det (i+j.val)).2 ((ha j.val i) ▸ hj)

#print axioms heightDrop
#print axioms visitsSmall
#print axioms smallFails
#print axioms integralCompanionImpossible
end DyadicCompanion
