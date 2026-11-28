import Init.Omega

/-! The first time of a target relative to an independently stopped orbit.
The two alternatives include both temporal orders and require no transience. -/

namespace Collatz.FirstHitClockCentres

def FirstAt (orbit : Nat → Nat → Nat) (P : Nat → Prop) (n t : Nat) : Prop :=
  P (orbit t n) ∧ ∀ j, j < t → ¬P (orbit j n)

variable {orbit : Nat → Nat → Nat}
variable (compose : ∀ i j x, orbit (i+j) x = orbit j (orbit i x))

include compose

theorem shift {P : Nat → Prop} {n a t : Nat}
    (first : FirstAt orbit P n t) (before : a ≤ t) :
    FirstAt orbit P (orbit a n) (t-a) := by
  constructor
  · have h : a+(t-a) = t := by omega
    rw [← compose, h]
    exact first.1
  · intro j hj
    rw [← compose]
    exact first.2 _ (by omega)

omit compose in
theorem unique {P : Nat → Prop} {n s t : Nat}
    (first : FirstAt orbit P n s) (other : FirstAt orbit P n t) : s = t := by
  by_cases h : s < t
  · exact False.elim (other.2 _ h first.1)
  · by_cases h' : t < s
    · exact False.elim (first.2 _ h' other.1)
    · omega

theorem two_orders {floor : Nat → Prop} {n y s t : Nat}
    (target : FirstAt orbit (fun v => v = y) n s)
    (land : FirstAt orbit floor n t) :
    (∃ v d, floor v ∧ FirstAt orbit (fun z => z=y) v d ∧ s=t+d)
      ∨ (∃ d, FirstAt orbit floor y d ∧ t=s+d) := by
  by_cases ht : t ≤ s
  · exact Or.inl ⟨orbit t n,s-t,land.1,shift compose target ht,by omega⟩
  · have h := shift compose land (a := s) (by omega)
    rw [target.1] at h
    exact Or.inr ⟨t-s,h,by omega⟩

theorem signed_clock_centres {floor : Nat → Prop} {n y s t : Nat}
    (target : FirstAt orbit (fun v => v=y) n s)
    (land : FirstAt orbit floor n t)
    (toTarget toFloor : Nat → Nat)
    (tSpec : ∀ v d, FirstAt orbit (fun z => z=y) v d → toTarget v = d)
    (fSpec : ∀ v d, FirstAt orbit floor v d → toFloor v = d) :
    (∃ v, floor v ∧ (s:Int)-t = toTarget v) ∨ (s:Int)-t = -(toFloor y:Int) := by
  rcases two_orders compose target land with ⟨v,d,hv,hd,hs⟩ | ⟨d,hd,ht⟩
  · exact Or.inl ⟨v,hv,by rw [tSpec _ _ hd]; omega⟩
  · exact Or.inr (by rw [fSpec _ _ hd]; omega)

#print axioms signed_clock_centres

end Collatz.FirstHitClockCentres
