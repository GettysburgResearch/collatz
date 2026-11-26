import WallGeneral

/-! Four primitive exceptional rational walls among the cyclically
parity-admissible necklaces of least period at most 30. Each pair of
positive-cycle witnesses and its ordinary exclusion are kernel-checked. -/
set_option maxRecDepth 16384

namespace WallExamples
open WallGeneral WallRational WallRefinement

private def cycleAt (d a : Int) (e t : Nat)
    (ret : runD d t (runD d e a)=runD d e a)
    (pos : 0<grade d t (runD d e a)) : PositiveCycle d a :=
  ⟨e,t,ret,pos⟩

theorem period4 (C : Coloring) {n : Nat} (cut : Mixed C n) :
    ∃ k, index C n (4*k)≠address 4 7 n k :=
  breaks C cut 4 7 15 (by decide) (by decide) (by decide)
    (cycleAt _ _ 2 3 (by decide) (by decide))
    (cycleAt _ _ 9 5 (by decide) (by decide))

theorem period8 (C : Coloring) {n : Nat} (cut : Mixed C n) :
    ∃ k, index C n (8*k)≠address 8 95 n k :=
  breaks C cut 8 95 255 (by decide) (by decide) (by decide)
    (cycleAt _ _ 7 7 (by decide) (by decide))
    (cycleAt _ _ 9 31 (by decide) (by decide))

theorem period12 (C : Coloring) {n : Nat} (cut : Mixed C n) :
    ∃ k, index C n (12*k)≠address 12 2047 n k :=
  breaks C cut 12 2047 4095 (by decide) (by decide) (by decide)
    (cycleAt _ _ 41 48 (by decide) (by decide))
    (cycleAt _ _ 13 84 (by decide) (by decide))

theorem period18 (C : Coloring) {n : Nat} (cut : Mixed C n) :
    ∃ k, index C n (18*k)≠address 18 87383 n k :=
  breaks C cut 18 87383 262143 (by decide) (by decide) (by decide)
    (cycleAt _ _ 9 72 (by decide) (by decide))
    (cycleAt _ _ 288 72 (by decide) (by decide))

end WallExamples
