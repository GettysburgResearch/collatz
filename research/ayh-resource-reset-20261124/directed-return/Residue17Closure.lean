import DirectedElevenLocal
import UnitResidueExchange
import ReverseBasin

/-! A conditional ordinary Collatz equivalence consuming the complete
directed residue localization and the pinned PR146 descent certificate. -/
namespace Residue17Closure

theorem localize_seventeen (f : ℕ → Bool)
    (he : ∀ n, f (2*n)=f n) (ho : ∀ n, f (2*n+1)=f (3*n+2))
    (x : ℕ) (hx : x%16=1) (hd : f x ≠ f (3*x)) :
    ∃ z, z%48=17 ∧ f z=f x ∧ f (3*z)=f (3*x) := by
  obtain ⟨y,hy,hl,hr⟩ := DirectedEleven.localize f he ho x hx hd
  let t := y/32
  have ey : y=32*t+11 := by dsimp [t]; omega
  obtain ⟨h1,h2⟩ := UnitResidueExchange.residue17_descends f he ho t
  refine ⟨48*t+17, by omega, ?_, ?_⟩
  · exact h1.symm.trans (ey ▸ hl)
  · have er : 3*y=96*t+33 := by omega
    have ez : 3*(48*t+17)=144*t+51 := by omega
    rw [ez]
    exact h2.symm.trans (er ▸ hr)

open CollatzReverseBasin

private theorem basin_step (n : ℕ) : Basin (shortcut n) ↔ Basin n := by
  constructor
  · rintro ⟨k,h⟩; exact ⟨k+1,h⟩
  · rintro ⟨k,h⟩
    cases k with
    | zero => change n=1 at h; subst n; exact ⟨1,rfl⟩
    | succ k => exact ⟨k,h⟩

private theorem basin_twice (n : ℕ) : Basin (2*n) ↔ Basin n := by
  have e : shortcut (2*n)=n := by simp [shortcut]
  simpa only [e] using (basin_step (2*n)).symm

private theorem basin_odd (n : ℕ) : Basin (2*n+1) ↔ Basin (3*n+2) := by
  have e : shortcut (2*n+1)=3*n+2 := by simp [shortcut]; omega
  simpa only [e] using (basin_step (2*n+1)).symm

noncomputable def basinLabel (n : ℕ) : Bool := by
  classical
  exact decide (Basin n)

private theorem label_even (n : ℕ) : basinLabel (2*n)=basinLabel n := by
  classical
  simp only [basinLabel, basin_twice]

private theorem label_odd (n : ℕ) : basinLabel (2*n+1)=basinLabel (3*n+2) := by
  classical
  simp only [basinLabel, basin_odd]

private theorem label_three_binary (k : ℕ) :
    basinLabel (3*(16*k+1)) = basinLabel (32*k+1) := by
  have od (a b : ℕ) :
      basinLabel ((2*a)*k+(2*b+1)) = basinLabel ((3*a)*k+(3*b+2)) := by
    convert label_odd (a*k+b) using 1 <;> congr 1 <;> ring
  have ev (a b : ℕ) :
      basinLabel ((2*a)*k+2*b) = basinLabel (a*k+b) := by
    convert label_even (a*k+b) using 1; congr 1; ring
  calc
    _ = basinLabel (48*k+3) := by congr 1; ring
    _ = basinLabel (72*k+5) := od 24 1
    _ = basinLabel (108*k+8) := od 36 2
    _ = basinLabel (54*k+4) := ev 54 4
    _ = basinLabel (27*k+2) := ev 27 2
    _ = basinLabel (18*k+1) := (od 9 0).symm
    _ = basinLabel (36*k+2) := (ev 18 1).symm
    _ = basinLabel (24*k+1) := (od 12 0).symm
    _ = basinLabel (48*k+2) := (ev 24 1).symm
    _ = basinLabel (32*k+1) := (od 16 0).symm

/-- This is a complete conditional equivalence for the ordinary shortcut map.
The restricted reverse basin implication is a hypothesis, not a proved fact. -/
theorem collatz_iff_reverse_seventeen :
    (∀ n : ℕ, 0<n → Basin n) ↔
    (∀ z : ℕ, z%48=17 → Basin (3*z) → Basin z) := by
  classical
  constructor
  · exact fun h z hz _ => h z (by omega)
  intro restricted
  apply collatz_iff_reverse_binary.mpr
  intro k hhigh
  by_contra hlow
  have lo : basinLabel (16*k+1)=false := by simp [basinLabel,hlow]
  have hi : basinLabel (3*(16*k+1))=true := by
    rw [label_three_binary]
    simp [basinLabel,hhigh]
  obtain ⟨z,hz,za,zb⟩ := localize_seventeen basinLabel label_even label_odd
      (16*k+1) (by omega) (by rw [lo,hi]; decide)
  have bad : ¬ Basin z := by simpa [basinLabel] using za.trans lo
  have good : Basin (3*z) := by simpa [basinLabel] using zb.trans hi
  exact bad (restricted z hz good)

#print axioms localize_seventeen
#print axioms collatz_iff_reverse_seventeen
end Residue17Closure
