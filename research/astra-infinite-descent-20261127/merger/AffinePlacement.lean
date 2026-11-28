import AffineGeometry
import MarkedProgressions

/-! All-target, all-window ordinary realizations of finite positive
affine families whose slopes have a common prime-to-six part. Each arm
has its explicitly indexed first-visit clock and graded shift. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.AffinePlacement
open TwoGapRouting FirstArrival AffineGeometry

private theorem halves_lower (h n : ℕ) : n≤2^h*run h n := by
  have f:=MergerThreshold.forward_lower h n
  have p:=Nat.le_mul_of_pos_left n (by positivity : 0<(3:ℕ)^(odds h n))
  omega

private theorem before {n y t : ℕ} (u : 2^t*y<n) : run t n≠y := by
  intro equal
  have contrary:=halves_lower t n
  rw [equal] at contrary
  omega

/-- Transfer first arrivals through a coalesced prefix using only a
lower size bound on the reference input. -/
theorem first_of_prefix (f : Arm) (H U j D y : ℕ) (high : 2^H*y<U)
    (first : First D U y)
    (sync : run (H+f.delay) (input f (U+j))=run H U)
    (grade : f.debt+odds (H+f.delay) (input f (U+j))=odds H U) :
    First (D+f.delay) (input f (U+j)) y ∧
      f.debt+odds (D+f.delay) (input f (U+j))=odds D U := by
  have hd : H≤D := by
    by_contra! small
    have lo:=halves_lower D U
    rw [first.1] at lo
    have upper:=Nat.mul_le_mul_right y (Nat.pow_le_pow_right (by decide : 0<2) small.le)
    omega
  let L:=D-H
  have dl : H+L=D := by dsimp [L]; omega
  have fdl : H+f.delay+L=D+f.delay := by omega
  obtain ⟨tail,count⟩:=append H L U
  rw [dl] at tail count
  obtain ⟨hit,gr⟩:=append (H+f.delay) L (input f (U+j))
  rw [fdl,sync] at hit gr
  refine ⟨⟨hit.trans (tail.symm.trans first.1),?_⟩,by omega⟩
  intro i short seen
  by_cases early : i≤H+f.delay
  · have lev:=Nat.mul_le_mul_right y (Nat.pow_le_pow_right (by decide : 0<2) early)
    have lt:=Nat.mul_lt_mul_of_pos_left high (by positivity : 0<(2:ℕ)^f.delay)
    have deg:=Nat.le_mul_of_pos_left (U+j) (by positivity : 0<(3:ℕ)^f.debt)
    have md:=Nat.mul_le_mul_left (2^f.delay) deg
    have reach:=halves_lower i (input f (U+j))
    rw [seen] at reach
    rw [pow_add] at lev
    dsimp [input] at reach
    nlinarith only [lev,lt,md,reach,Nat.zero_le (2^f.delay*j),Nat.zero_le f.shift]
  · let v:=i-(H+f.delay)
    have iv : H+f.delay+v=i := by dsimp [v]; omega
    have ih : H+v<D := by omega
    have s:=(append (H+f.delay) v (input f (U+j))).1
    rw [iv,seen,sync] at s
    exact first.2 _ ih ((append H v U).1.trans s.symm)

private theorem shift_class (x c m : ℕ) (mp : 0<m) :
    ∃j, j<m ∧ x+j ≡ c [MOD m] := by
  let raw:=c+m*(x+1)-x
  have big:=Nat.le_mul_of_pos_left (x+1) mp
  have sum : x+raw=c+m*(x+1) := by dsimp [raw]; omega
  refine ⟨raw%m,Nat.mod_lt _ mp,((Nat.mod_modEq raw m).add_left x).trans ?_⟩
  rw [sum]
  simp [Nat.ModEq]

private theorem lift_parameter (U m W c : ℕ) (mp : 0<m) (wp : 0<W) :
    ∃j t, j<m*W ∧ U+j=m*t ∧ t ≡ c [MOD W] := by
  obtain ⟨j,small,congr⟩:=shift_class U (m*c) (m*W) (by positivity)
  have cc:=congr.of_dvd (dvd_mul_right m W)
  have div : m ∣ U+j := Nat.modEq_zero_iff_dvd.mp (cc.trans (by simp [Nat.ModEq]))
  obtain ⟨t,eq⟩:=div
  rw [eq] at congr
  exact ⟨j,t,small,eq,Nat.ModEq.mul_left_cancel' (by omega) congr⟩

/-- The parameter t lies in the actual interval. Clock residues and grade
residues apply to the common reference; the time and grade of every arm
are then exactly determined up to its fixed delay and debt. -/
def Placement (F : List Arm) (m W M Q : ℕ) (δ : ℝ) : Prop :=
  ∃ C K : ℝ, ∃G : ℕ, 0<C ∧ 0<K ∧ ∀y : ℕ, y%3≠0 → ∀X : ℝ, C*y≤X →
    ∀τ ρ : ℕ, ∃D g : ℕ, g≤G ∧ (2:ℝ)^D*y≤K*X ∧ D ≡ τ [MOD M] ∧ g ≡ ρ [MOD Q] ∧
      ∀c : ℕ, ∃t : ℕ, 0<t ∧ X≤t ∧ (t:ℝ)≤(1+δ)*X ∧ t ≡ c [MOD W] ∧
        ∀f∈F, First (D+f.delay) (input f (m*t)) y ∧
          f.debt+odds (D+f.delay) (input f (m*t))=g

theorem marked (F : List Arm) (m W M Q : ℕ) (mp : 0<m) (wp : 0<W)
    (time : 0<M) (count : 0<Q) (δ : ℝ) (positive : 0<δ) : Placement F m W M Q δ := by
  let J:=m*W
  obtain ⟨H,R,sync⟩:=rows F J
  obtain ⟨A,K,G,ap,kp,windows⟩:=MarkedProgressions.mixed_blocks [] H R 0 M Q time count
    (δ/2) (by positivity)
  let C:=A+(R:ℝ)+(2:ℝ)^H+2*(J+1)/δ+2
  have cp : 0<C := by dsimp [C]; positivity
  have mr : (1:ℝ)≤m := by exact_mod_cast mp
  have mrp : 0<(m:ℝ) := by positivity
  refine ⟨C,K*m,G,cp,by positivity,?_⟩
  intro y unit X high τ ρ
  have yr : (1:ℝ)≤y := by exact_mod_cast (show 1≤y by omega)
  have y0 : 0≤(y:ℝ) := by positivity
  have cx : C≤X := (le_mul_of_one_le_right cp.le yr).trans high
  have xp : 0<X := cp.trans_le cx
  have mx : X≤m*X := le_mul_of_one_le_left xp.le mr
  have mass : 0≤2*((J:ℝ)+1)/δ := by positivity
  have rp : 0≤(R:ℝ) := by positivity
  have hp : 0≤(2:ℝ)^H := by positivity
  have rest : A≤C := by dsimp [C]; linarith
  have rise : (2:ℝ)^H+1≤C := by dsimp [C]; linarith
  have minR : (R:ℝ)≤X := by dsimp [C] at cx; linarith
  have budget : (J:ℝ)≤δ/2*(m*X) := by
    have jx : 2*((J:ℝ)+1)/δ≤X := by dsimp [C] at cx; linarith
    have b:=(div_le_iff₀ positive).mp jx
    have e:=mul_le_mul_of_nonneg_left mx positive.le
    nlinarith only [b,e]
  have req : A*y≤m*X := ((mul_le_mul_of_nonneg_right rest y0).trans high).trans mx
  obtain ⟨U,D,g,_,binary,_,arms,bound,speed,tm,gm⟩:=windows y unit _ req 0 τ ρ
  obtain ⟨ul,uh,first,gr⟩:=arms 0 List.mem_cons_self
  simp only [Nat.cast_zero,add_zero] at ul uh first gr
  have RU : R≤U := by exact_mod_cast (minR.trans (mx.trans ul))
  obtain ⟨v,eq⟩:=(Nat.modEq_iff_exists_eq_add RU).mp binary.symm
  have up : 2^H*y<U := by
    have hh:=(mul_le_mul_of_nonneg_right rise y0).trans (high.trans (mx.trans ul))
    exact_mod_cast (show (2:ℝ)^H*y<U by nlinarith only [hh,yr])
  refine ⟨D,g,bound,by nlinarith only [speed],tm,gm,?_⟩
  intro c
  obtain ⟨j,t,jl,mt,tc⟩:=lift_parameter U m W c mp wp
  have idR : (U:ℝ)+j=m*t := by exact_mod_cast mt
  have jr : (j:ℝ)≤J := by exact_mod_cast jl.le
  have lo : X≤t := le_of_mul_le_mul_left (by linarith [show 0≤(j:ℝ) by positivity] :
      (m:ℝ)*X≤m*t) mrp
  have hi : (t:ℝ)≤(1+δ)*X := le_of_mul_le_mul_left (by nlinarith only [idR,jr,uh,budget] :
      (m:ℝ)*t≤m*((1+δ)*X)) mrp
  refine ⟨t,by exact_mod_cast xp.trans_le lo,lo,hi,tc,?_⟩
  intro f inside
  obtain ⟨p,q⟩:=sync v f inside j jl
  rw [←eq] at p q
  rw [←mt,←gr]
  exact first_of_prefix f H U j D y up first p q

#print axioms first_of_prefix
#print axioms marked
end Collatz.AffinePlacement
