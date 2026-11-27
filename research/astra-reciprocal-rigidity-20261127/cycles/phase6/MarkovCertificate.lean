import Mathlib.Data.Nat.Choose.Basic

/-! Exact one-step certificates for two four-copy signed-numerator chains. -/

namespace CollatzResearch.MarkovCertificate

/-- Arguments are the counts in states 0 and 1; the third is 4-a-b. -/
def dimerWeight : ℕ → ℕ → ℕ
  | 0, 0 => 1000
  | 0, 1 => 300
  | 0, 2 => 396
  | 0, 3 => 303
  | 0, 4 => 539
  | 1, 0 => 404
  | 1, 1 => 128
  | 1, 2 => 126
  | 1, 3 => 187
  | 2, 0 => 434
  | 2, 1 => 130
  | 2, 2 => 319
  | 3, 0 => 255
  | 3, 1 => 297
  | 4, 0 => 734
  | _, _ => 0

/-- The number of active copies, from zero to four, is the sole state. -/
def twoGapWeight : ℕ → ℕ
  | 0 => 1000
  | 1 => 468
  | 2 => 469
  | 3 => 443
  | 4 => 558
  | _ => 0

/-- Integer numerator of one parity-constrained transfer, at denominator 100^b. -/
def row (b e yes no : ℕ) (nextWeight : ℕ → ℕ) : ℕ :=
  ((List.range (b+1)).map (fun j =>
    if j % 2 = e then b.choose j * yes^j * no^(b-j) * nextWeight j else 0)).sum

theorem dimer_certificate :
    ∀ a b : Fin 5, a.val + b.val ≤ 4 → ∀ e : Fin 2,
      50 * row b e 72 30 (fun j => dimerWeight (4-a.val-j) a) ≤
        37 * 100^b.val * dimerWeight a b := by decide +kernel

theorem dimer_range :
    ∀ a b : Fin 5, a.val + b.val ≤ 4 →
      126 ≤ dimerWeight a b ∧ dimerWeight a b ≤ 1000 := by decide +kernel

theorem two_gap_certificate :
    ∀ b : Fin 5, ∀ e : Fin 2,
      25 * row b e 59 42 (fun j => twoGapWeight (4-j)) ≤
        14 * 100^b.val * twoGapWeight b := by decide +kernel

theorem two_gap_range :
    ∀ b : Fin 5, 443 ≤ twoGapWeight b ∧ twoGapWeight b ≤ 1000 := by decide +kernel

#print axioms dimer_certificate
#print axioms dimer_range
#print axioms two_gap_certificate
#print axioms two_gap_range

end CollatzResearch.MarkovCertificate
