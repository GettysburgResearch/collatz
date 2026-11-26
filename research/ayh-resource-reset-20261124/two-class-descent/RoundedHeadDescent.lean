import OffsetDescent

/-! Four possible rounded bottom heads share an exact physical future on
one progression. The imported orbit and affine lift use the ordinary shortcut. -/
namespace CollatzShell.RoundedHeadDescent
open OffsetDescent

private theorem profile (q a c : Nat) (hm : 3^(oddCount 13 c)*a=729)
    (hv : orbit 13 c=200) : orbit 13 (a*(8192*q)+c)=729*q+200 := by
  rw [show a*(8192*q)+c=2^13*(a*q)+c by ring, affine_lift, hv, ← Nat.mul_assoc, hm]

/-- At W near one half, the four possible bottom roundings are exactly
X−1, 3X−2, 9X−5, 27X−14. -/
theorem simultaneous_bottom (q : Nat) (x : Nat) (hx : x=8192*q+2242) :
    orbit 13 x=729*q+200 ∧ orbit 13 (x-1)=729*q+200 ∧
    orbit 13 (3*x-2)=729*q+200 ∧ orbit 13 (9*x-5)=729*q+200 ∧
    orbit 13 (27*x-14)=729*q+200 := by
  subst x
  have h₀ := profile q 1 2242 (by decide) (by decide)
  have h₁ := profile q 1 2241 (by decide) (by decide)
  have h₂ := profile q 3 6724 (by decide) (by decide)
  have h₃ := profile q 9 20173 (by decide) (by decide)
  have h₄ := profile q 27 60520 (by decide) (by decide)
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · simpa using h₀
  · simpa [show 8192*q+2242-1=8192*q+2241 by omega] using h₁
  · rw [show 3*(8192*q+2242)-2=3*(8192*q)+6724 by omega]
    exact h₂
  · rw [show 9*(8192*q+2242)-5=9*(8192*q)+20173 by omega]
    exact h₃
  · rw [show 27*(8192*q+2242)-14=27*(8192*q)+60520 by omega]
    exact h₄

end CollatzShell.RoundedHeadDescent
