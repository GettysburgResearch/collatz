import AnchorDescent

namespace Collatz.AnchorControl
open Collatz.SourceDeletion Collatz.MinimumFailure Collatz.AnchorDescent

/-- The complete immediate lower cone for the specified source 3^6*5. -/
def Lower (y : Nat) : Prop :=
  ∃ i s b : Nat, 0<b ∧ (b<5 ∨ (b=5 ∧ s<6)) ∧ y=2^i*3^s*b

private theorem table (j : Fin 12) : run j.val 3645<8192 ∧
    ∀ i : Fin 13, ∀ s : Fin 9, ∀ b : Fin 6, 0<b.val →
      (b.val<5 ∨ b.val=5 ∧ s.val<6) →
      run j.val 3645≠2^i.val*3^s.val*b.val := by
  revert j
  decide +kernel

theorem short_miss (j : Nat) (hj : j<12) : ¬Lower (run j 3645) := by
  rintro ⟨i,s,b,hb,lt,eq⟩
  obtain ⟨cap,miss⟩ := table ⟨j,hj⟩
  have pi := Nat.one_le_pow i 2 (by decide)
  have ps := Nat.one_le_pow s 3 (by decide)
  have sizeI : 2^i≤2^i*3^s*b := by
    calc
      _ ≤ 2^i*3^s := by simpa using Nat.mul_le_mul_left (2^i) ps
      _ ≤ _ := by simpa using Nat.mul_le_mul_left (2^i*3^s) hb
  have sizeS : 3^s≤2^i*3^s*b := by
    calc
      _ ≤ 2^i*3^s := by simpa using Nat.mul_le_mul_right (3^s) pi
      _ ≤ _ := by simpa using Nat.mul_le_mul_left (2^i*3^s) hb
  change run j 3645<8192 at cap
  have smallI : i<13 := by
    by_contra no
    have := Nat.pow_le_pow_right (by decide : 0<2) (show 13≤i by omega)
    omega
  have smallS : s<9 := by
    by_contra no
    have := Nat.pow_le_pow_right (by decide : 0<3) (show 9≤s by omega)
    omega
  exact miss ⟨i,smallI⟩ ⟨s,smallS⟩ ⟨b,by omega⟩ hb lt eq

private theorem bound_clock {j : Nat} (cap : 2^j≤3781) : j<12 := by
  by_contra no
  have := Nat.pow_le_pow_right (by decide : 0<2) (show 12≤j by omega)
  omega

private theorem dyadic_zero {y i u : Nat} (odd : y%2=1) (eq : y=2^i*u) : y=u := by
  cases i with
  | zero => simpa using eq
  | succ i =>
    rw [show 2^(i+1)*u=2*(2^i*u) by ring] at eq
    omega

/-- Every phase-1 anchor, with any nonnegative number of displacement
    units and any positive number of laps, misses the full immediate cone. -/
theorem no_positive {a h d t y : Nat} (ha : 0<a) (hd : 0<d)
    (hit : run h a=1) (src : 3645=a+2^h*4^d*t) (dst : y=a+2^h*3^d*t) :
    ¬Lower y := by
  by_cases tz : t=0
  · subst t
    simp only [Nat.mul_zero,Nat.add_zero] at src dst
    have eq : y=3645 := by omega
    rw [eq]; exact short_miss 0 (by decide)
  have ht : 0<t := by omega
  cases h with
  | zero =>
    change a=1 at hit
    have meet := positive_meeting (a:=a) (h:=0) hit d t
    simp only [Nat.zero_add,run] at meet
    rw [←src,←dst] at meet
    have cap := Nat.mul_le_mul_left (4^d) (show 1≤t from ht)
    simp only [Nat.mul_one] at cap
    simp only [pow_zero,Nat.one_mul] at src
    have power : (2:Nat)^(2*d)=4^d := by rw [pow_mul]; rfl
    have hj : 2*d<12 := bound_clock (by rw [power]; omega)
    rw [←meet]; exact short_miss _ hj
  | succ k =>
    have so := src
    have de := dst
    rw [show 2^(k+1)*4^d*t=2*(2^k*4^d*t) by ring] at so
    rw [show 2^(k+1)*3^d*t=2*(2^k*3^d*t) by ring] at de
    have odd : y%2=1 := by omega
    rintro ⟨i,s,b,_,lt,eq⟩
    rw [Nat.mul_assoc] at eq
    have same := dyadic_zero odd eq
    have hsrc : 3^6*5=a+2^(k+1)*4^d*t := src
    have bound := positive_anchor_scale ha hd ht hit hsrc (same.symm.trans dst)
      (by decide : 0<5) (by omega)
    omega

/-- Every negative-integer preperiod and positive-length return to any
    phase of magnitude at most 136 misses the same full immediate cone. -/
theorem no_negative {m C h e t y : Nat} (hm : 0<m) (hc : 0<C) (capC : C≤136)
    (he : 0<e) (hit : negRun h m=C) (lap : negRun e C=C)
    (src : 3645+m=2^h*2^e*t) (dst : y+m=2^h*3^(negOdds e C)*t) :
    ¬Lower y := by
  have ht : 0<t := by
    by_contra no
    have z : t=0 := by omega
    simp [z] at src
  cases h with
  | zero =>
    change m=C at hit
    have meet := negative_meeting (m:=m) (h:=0) hit lap src dst
    simp only [Nat.zero_add,run] at meet
    simp only [pow_zero,Nat.one_mul] at src
    have cap := Nat.mul_le_mul_left (2^e) (show 1≤t from ht)
    simp only [Nat.mul_one] at cap
    rw [←meet]
    exact short_miss _ (bound_clock (by omega))
  | succ k =>
    have so := src
    have de := dst
    rw [show 2^(k+1)*2^e*t=2*(2^k*2^e*t) by ring] at so
    rw [show 2^(k+1)*3^(negOdds e C)*t=2*(2^k*3^(negOdds e C)*t) by ring] at de
    have odd : y%2=1 := by omega
    rintro ⟨i,s,b,_,lt,eq⟩
    rw [Nat.mul_assoc] at eq
    have same := dyadic_zero odd eq
    have hsrc : 3^6*5+m=2^(k+1)*2^e*t := src
    have hdst : 3^s*b+m=2^(k+1)*3^(negOdds e C)*t := by rwa [←same]
    have bound := negative_anchor_scale hm hc he ht hit lap hsrc hdst
      (by decide : 0<5) (by omega)
    omega

theorem control_good : Good 3645 := ⟨31, by decide⟩

#print axioms short_miss
#print axioms no_positive
#print axioms no_negative
#print axioms control_good
end Collatz.AnchorControl
