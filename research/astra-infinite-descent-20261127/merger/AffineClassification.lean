import PrimeCore
import AffinePlacement

/-! Oracle-free characterization of positive affine families that admit
uniform common-target near-fast first-visit placements in every relative
parameter window with all physical and source congruence controls. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.AffineClassification
open PrimeCore AffineGeometry FirstArrival TwoGapRouting

def Windows (F : List Form) : Prop :=
  ∀W M Q : ℕ, 0<W → 0<M → 0<Q → ∀δ : ℝ, 0<δ →
  ∃ C K : ℝ, ∃G : ℕ, 0<C ∧ 0<K ∧ ∀y : ℕ, y%3≠0 → ∀X : ℝ, C*y≤X →
    ∀τ ρ : ℕ, ∃D g : ℕ, g≤G ∧ (2:ℝ)^D*y≤K*X ∧ D ≡ τ [MOD M] ∧ g ≡ ρ [MOD Q] ∧
      ∀c : ℕ, ∃t : ℕ, 0<t ∧ X≤t ∧ (t:ℝ)≤(1+δ)*X ∧ t ≡ c [MOD W] ∧
        ∀f∈F, First (D+(normalized f).delay) (f.slope*t+f.shift) y ∧
          (normalized f).debt+odds (D+(normalized f).delay) (f.slope*t+f.shift)=g

private theorem of_common (F : List Form) (m : ℕ) (mp : 0<m) (common : ∀f∈F,core f.slope=m) :
    Windows F := by
  intro W M Q wp time count δ positive
  obtain ⟨C,K,G,cp,kp,coreBank⟩:=
    AffinePlacement.marked (F.map normalized) m W M Q mp wp time count δ positive
  refine ⟨C,K,G,cp,kp,?_⟩
  intro y yu X large τ ρ
  obtain ⟨D,g,gb,speed,dt,gg,all⟩:=coreBank y yu X large τ ρ
  refine ⟨D,g,gb,speed,dt,gg,?_⟩
  intro c
  obtain ⟨t,tp,tl,tu,tc,arms⟩:=all c
  refine ⟨t,tp,tl,tu,tc,?_⟩
  intro f hf
  have h:=arms (normalized f) (List.mem_map.mpr ⟨f,hf,rfl⟩)
  have rebuild:=reconstruct f
  rw [common f hf] at rebuild
  have eq : input (normalized f) (m*t)=f.slope*t+f.shift := by
    change 2^(normalized f).delay*3^(normalized f).debt*(m*t)+f.shift=f.slope*t+f.shift
    rw [←rebuild]; ring
  rwa [eq] at h

private theorem bounded_of_windows (F : List Form) (full : Windows F) : BoundedMeet F := by
  obtain ⟨C,K,G,cp,_,full⟩:=full 1 1 1 (by decide) (by decide) (by decide) 1 (by norm_num)
  obtain ⟨H,hH⟩:=exists_nat_gt (K*C)
  let R:=delayBound F
  have delay {f : Form} (inside : f∈F) : (normalized f).delay≤R := delay_le inside
  refine ⟨H+R,?_⟩
  intro N
  obtain ⟨u,hu⟩:=exists_nat_gt ((N:ℝ)/C)
  let y:=3*u+1
  have yu : y%3≠0 := by dsimp [y]; omega
  have yp : 0<(y:ℝ) := by dsimp [y]; positivity
  have loc : (N:ℝ)≤C*y := by
    have u0 : 0≤(u:ℝ) := by positivity
    have unc:=(div_lt_iff₀ cp).mp hu
    dsimp [y]; push_cast
    nlinarith only [unc,mul_nonneg cp.le u0,cp]
  obtain ⟨D,g,_,speed,_,_,all⟩:=full y yu (C*y) (le_refl _) 0 0
  obtain ⟨t,_,low,_,_,arms⟩:=all 0
  have nt : N≤t := by exact_mod_cast loc.trans low
  have budget : (2:ℝ)^D≤K*C :=
    le_of_mul_le_mul_right (by simpa only [mul_assoc] using speed : (2:ℝ)^D*y≤K*C*y) yp
  have pow : (D:ℝ)≤(2:ℝ)^D := by exact_mod_cast (show D≤2^D from Nat.le_of_lt Nat.lt_two_pow_self)
  have dh : D≤H := by exact_mod_cast ((pow.trans budget).trans hH.le)
  refine ⟨t,y,nt,?_⟩
  intro f inside
  exact ⟨_,Nat.add_le_add dh (delay inside),(arms f inside).1.1⟩

/-- A prescribed finite family has the entire uniform window property
exactly when all its positive integer slopes have the same prime-to-six
part. The necessity even allows freely varying independent meeting clocks. -/
theorem iff_common (F : List Form) (positive : ∀f∈F,0<f.slope) :
    Windows F ↔ ∀f∈F,∀g∈F,core f.slope=core g.slope := by
  refine ⟨fun w => necessary F (bounded_of_windows F w),?_⟩
  intro common
  cases F with
  | nil => exact of_common [] 1 (by decide) (by simp)
  | cons f F =>
    have pos:=positive f List.mem_cons_self
    have nonzero : 0<core f.slope := Nat.ordCompl_pos 3 (Nat.ordCompl_pos 2 pos.ne').ne'
    exact of_common (f::F) (core f.slope) nonzero
      (fun g hg => common g hg f List.mem_cons_self)

#print axioms iff_common
end Collatz.AffineClassification
