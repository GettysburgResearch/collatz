import MersenneReturnKernel
import MersenneParity
import TwoOddCertificate

namespace CollatzMersenneFirstBad
open CollatzReverseBasin CollatzTwoOdd

private theorem memStep (n : ℕ) : Basin (shortcut n) ↔ Basin n := by
  constructor
  · rintro ⟨k,h⟩; exact ⟨k+1,h⟩
  · rintro ⟨k,h⟩
    cases k with
    | zero => change n=1 at h; subst n; exact ⟨1,rfl⟩
    | succ k => exact ⟨k,h⟩

private theorem memEven (n : ℕ) : Basin (2*n) ↔ Basin n := by
  have e : shortcut (2*n)=n := by simp [shortcut]
  rw [←memStep (2*n),e]

private theorem memOdd (n : ℕ) : Basin (2*n+1) ↔ Basin (3*n+2) := by
  have e : shortcut (2*n+1)=3*n+2 := by unfold shortcut; split <;> omega
  rw [←memStep (2*n+1),e]

/-- At each exponent j≥3 the tripled Mersenne number joins the previous one
after exactly three versus two native steps. -/
theorem tripled_previous (j : ℕ) (hj : 3≤j) :
    Basin (3*(2^j-1)) ↔ Basin (2^(j-1)-1) := by
  let t := 2^(j-3)
  have hp : 0<t := Nat.pow_pos (by decide)
  have ej : 2^j=8*t := by
    calc 2^j=2^(3+(j-3)) := congrArg (fun b : ℕ => 2^b) (by omega)
         _ = _ := Nat.pow_add _ _ _
  have ek : 2^(j-1)=4*t := by
    calc 2^(j-1)=2^(2+(j-3)) := congrArg (fun b : ℕ => 2^b) (by omega)
         _ = _ := Nat.pow_add _ _ _
  rw [ej,ek]
  have a : shortcut (3*(8*t-1))=36*t-4 := by unfold shortcut; split <;> omega
  have b : shortcut (36*t-4)=18*t-2 := by unfold shortcut; split <;> omega
  have c : shortcut (18*t-2)=9*t-1 := by unfold shortcut; split <;> omega
  have d : shortcut (4*t-1)=6*t-1 := by unfold shortcut; split <;> omega
  have e : shortcut (6*t-1)=9*t-1 := by unfold shortcut; split <;> omega
  rw [←memStep (3*(8*t-1)),a,←memStep (36*t-4),b,←memStep (18*t-2),c,
      ←memStep (4*t-1),d,←memStep (6*t-1),e]

private theorem first_index (m z j : ℕ) (parent : 81*z+527=512*2^(98+162*m))
    (back : ∀ n : ℕ, 0<n → ¬Basin n → ∃ w, ReverseDefect w ∧ w≤2^40*n)
    (minimal : ∀ w, w%48=17 → w<z → Basin (3*w) → Basin w)
    (jp : 0<j) (ja : j≤98+162*m) (bad : ¬Basin (2^j-1))
    (first : ∀ k, 0<k → k<j → Basin (2^k-1)) : j=97+162*m := by
  let a := 98+162*m
  let r := a-j
  have pj : 2 ≤ 2^j := Nat.pow_le_pow_right (by decide : 0<2) (show 1≤j by omega)
  have near : r≤42 := by
    by_cases h : r≤42
    · exact h
    have high : j+43≤a := by dsimp [r] at h; omega
    obtain ⟨w,hw,bound⟩ := back (2^j-1) (by omega) bad
    have compare : 2^(j+43)≤2^a := Nat.pow_le_pow_right (by decide) high
    rw [Nat.pow_add] at compare
    change 81*z+527=512*2^a at parent
    have wz : w<z := by omega
    exact False.elim (hw.2.2 (minimal w hw.1 wz hw.2.1))
  have formula : 98-r+162*m=j := by dsimp [r,a] at *; omega
  have big : 50<j := by dsimp [r,a] at near; omega
  have power : (512*2^r)*2^j=512*2^a := by
    rw [Nat.mul_assoc,←Nat.pow_add]; apply congrArg (fun b : ℕ => 512*2^b)
    dsimp [r,a] at *; omega
  have few : r<3 := by
    by_cases lo : 3≤r
    · have safe : ∀ w : ℕ, w%48=17 → 81*w+527 < (512*2^r)*2^(98-r+162*m) →
          (¬Basin w) → (¬Basin (3*w)) := by
        intro w res lim hb ht
        rw [formula,power] at lim
        change 81*z+527=512*2^a at parent
        exact hb (minimal w res (by omega) ht)
      have p := MersenneReturnKernel.forty_returns m r lo near (fun n => ¬Basin n)
        (fun n => not_congr (memEven n)) (fun n => not_congr (memOdd n)) safe (formula ▸ bad)
      rw [formula] at p
      rcases p with upper | ⟨g,hg,lower⟩
      · exact False.elim (upper ((tripled_previous j (by omega)).mpr (first _ (by omega) (by omega))))
      · exact False.elim (lower (first (j-g) (by omega) (by omega)))
    · omega
  have odd : j%2=1 := by
    by_cases h : j%2=1
    · exact h
    let k := j/2-1
    have eq : j=2*k+2 := by dsimp [k]; omega
    have prior := first (2*k+1) (by omega) (by omega)
    have cur := (CollatzMersenneParity.even_mersenne_basin k).mpr prior
    exact False.elim (bad (eq ▸ cur))
  dsimp [r,a] at *
  omega

/-- At a parent from the rank-three family, if no smaller reverse defect
exists and the final Mersenne number is outside the basin, then the first
positive nonconvergent Mersenne exponent is exactly 97+162m. The bound on
the directed return is the explicit quantitative input. -/
theorem exact_first_bad (m z : ℕ) (parent : 81*z+527=512*2^(98+162*m))
    (back : ∀ n : ℕ, 0<n → ¬Basin n → ∃ w, ReverseDefect w ∧ w≤2^40*n)
    (minimal : ∀ w, w%48=17 → w<z → Basin (3*w) → Basin w)
    (bad : ¬Basin (2^(98+162*m)-1)) :
    ¬Basin (2^(97+162*m)-1) ∧ ∀ k, 0<k → k<97+162*m → Basin (2^k-1) := by
  classical
  have existsBad : ∃ k : ℕ, 0<k ∧ ¬Basin (2^k-1) := ⟨98+162*m,by omega,bad⟩
  let j := Nat.find existsBad
  obtain ⟨jp,hj⟩ := Nat.find_spec existsBad
  have ja : j≤98+162*m := Nat.find_min' existsBad ⟨by omega,bad⟩
  have first : ∀ k, 0<k → k<j → Basin (2^k-1) := by
    intro k hk less
    by_contra hb
    exact Nat.find_min existsBad less ⟨hk,hb⟩
  have id := first_index m z j parent back minimal jp ja hj first
  exact id ▸ And.intro hj first

#print axioms tripled_previous
#print axioms exact_first_bad
end CollatzMersenneFirstBad
