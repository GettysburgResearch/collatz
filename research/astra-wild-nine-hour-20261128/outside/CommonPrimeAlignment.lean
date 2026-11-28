import Std

/- The finite two-date algebra used by the short-predecessor estimate. -/
namespace AstraWild.CommonPrimeAlignment

/-- If two differences have a common integral modulus, so does the affine
discrepancy between their proposed centers on the same physical segment. -/
theorem centerDefectDvd (q a b x y u v c : Int)
    (hxy : b * y = a * x + c)
    (hx : q ∣ x - u) (hy : q ∣ y - v) :
    q ∣ b * v - a * u - c := by
  obtain ⟨i, hi⟩ := hx
  obtain ⟨j, hj⟩ := hy
  refine ⟨a * i - b * j, ?_⟩
  grind

/-- The strict size comparison converts shared prime-power agreement into
an exact affine equality on the centers. -/
theorem centerAlignment (q a b x y u v c : Int)
    (hxy : b * y = a * x + c)
    (hx : q ∣ x - u) (hy : q ∣ y - v)
    (hq : ((b * v - a * u - c).natAbs : Int) < q) :
    b * v = a * u + c := by
  have hdiv := centerDefectDvd q a b x y u v c hxy hx hy
  by_cases hzero : b * v - a * u - c = 0
  · omega
  · have hpos := Int.natAbs_pos.mpr hzero
    have habs := Int.dvd_natAbs.mpr hdiv
    have hpos' : (0 : Int) < ((b * v - a * u - c).natAbs : Int) := by omega
    have := Int.le_of_dvd hpos' habs
    omega

end AstraWild.CommonPrimeAlignment
