import AffineProfiles
import Threshold

/-! Uniformly bounded ordinary meeting clocks force an exact integer
relation between the slopes of two affine starts, except below an
explicit absolute parameter bound. Finite families of compatible slopes
admit a common moving endpoint on an ordinary dyadic cylinder. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.AffineGeometry
open TwoGapRouting AffineProfiles

private theorem odds_le (h n : ℕ) : odds h n≤h := by
  induction h generalizing n with
  | zero => simp [odds]
  | succ h ih =>
    have i:=ih (step n)
    simp only [odds]
    omega

private theorem carry_bound (h n : ℕ) :
    2^h*(run h n+1)≤3^(odds h n)*n+3^h := by
  induction h generalizing n with
  | zero => simp [run,odds]
  | succ h ih =>
    have prev:=Nat.mul_le_mul_left 2 (ih (step n))
    have num : 2*step n=3^(n%2)*n+n%2 := by
      unfold step
      split <;> rename_i p
      · rw [p]; simp; omega
      · rw [show n%2=1 by omega]; simp; omega
    have id:=congrArg (fun v : ℕ => 3^(odds h (step n))*v) num
    have bound : (3:ℕ)^(odds h (step n))≤3^h :=
      Nat.pow_le_pow_right (by decide) (odds_le _ _)
    have bit:=Nat.mul_le_mul_left (3^(odds h (step n))) (show n%2≤1 by omega)
    change 2^(h+1)*(run h (step n)+1)≤3^(n%2+odds h (step n))*n+3^(h+1)
    rw [pow_succ (2:ℕ),pow_succ (3:ℕ),pow_add]
    nlinarith only [prev,id,bound,bit]

private theorem ordered_bound {A B s t b d u v H : ℕ} (uh : u≤H) (vh : v≤H)
    (hit : run u (A*s+b)=run v (B*s+d))
    (less : 2^v*3^(odds u (A*s+b))*A<2^u*3^(odds v (B*s+d))*B)
    (size : b≤t) : s≤6^H*(t+1) := by
  let p:=3^(odds u (A*s+b))
  let q:=3^(odds v (B*s+d))
  have lower:=Nat.mul_le_mul_left (2^u) (MergerThreshold.forward_lower v (B*s+d))
  have upper:=Nat.mul_le_mul_left (2^v) (carry_bound u (A*s+b))
  rw [←hit] at lower
  have diff:=Nat.mul_le_mul_right s (Nat.succ_le_of_lt less)
  have loc : s≤2^v*(p*b+3^u) := by
    dsimp [p]
    nlinarith only [lower,upper,diff,Nat.zero_le (2^u*(3^(odds v (B*s+d))*d)),
      Nat.zero_le (2^u*odds v (B*s+d)),Nat.zero_le (2^v*2^u)]
  have powu : (3:ℕ)^u≤3^H:=Nat.pow_le_pow_right (by decide) uh
  have powv : (2:ℕ)^v≤2^H:=Nat.pow_le_pow_right (by decide) vh
  have powp : p≤3^H := Nat.pow_le_pow_right (by decide) ((odds_le _ _).trans uh)
  calc
    s ≤ 2^v*(p*b+3^u) := loc
    _ ≤ 2^H*(3^H*t+3^H) := Nat.mul_le_mul powv (Nat.add_le_add (Nat.mul_le_mul powp size) powu)
    _ = 6^H*(t+1) := by rw [show (6:ℕ)=2*3 by decide,mul_pow]; ring

/-- A direct guard for actual meets, even when the two clocks are
independent and no binary cylinder is assumed. -/
theorem slope_or_small (A b B d s u v H : ℕ) (uh : u≤H) (vh : v≤H)
    (hit : run u (A*s+b)=run v (B*s+d)) :
    2^v*3^(odds u (A*s+b))*A=2^u*3^(odds v (B*s+d))*B ∨
      s≤6^H*(max b d+1) := by
  rcases lt_trichotomy (2^v*3^(odds u (A*s+b))*A) (2^u*3^(odds v (B*s+d))*B) with l|e|g
  · exact Or.inr (ordered_bound uh vh hit l (le_max_left _ _))
  · exact Or.inl e
  · exact Or.inr (ordered_bound vh uh hit.symm g (le_max_right _ _))

/-- A graded slope has the form 2^delay times 3^debt, times a shared
ordinary scaling factor applied to the free parameter. -/
structure Arm where
  delay : ℕ
  debt : ℕ
  shift : ℕ
  deriving DecidableEq

def input (f : Arm) (u : ℕ) : ℕ := 2^f.delay*3^f.debt*u+f.shift

def post (f : Arm) (j : ℕ) : Profile :=
  let q:=f.debt+odds f.delay f.shift
  ⟨q,3^q*j+run f.delay f.shift⟩

private theorem prelude (f : Arm) (j u : ℕ) :
    run f.delay (input f (u+j))=value (post f j) u ∧
    f.debt+odds f.delay (input f (u+j))=(post f j).count := by
  have eq : input f (u+j)=f.shift+2^f.delay*(3^f.debt*(u+j)) := by unfold input; ring
  obtain ⟨r,g⟩:=lift f.delay f.shift (3^f.debt*(u+j))
  rw [eq,r,g]
  simp only [value,post,pow_add]
  exact ⟨by ring,True.intro⟩

/-- All listed slopes and all of their finite translates synchronize
with a distinguished ordinary reference on one complete binary cylinder.
Actual clock and grade differences exactly equal the chosen delay and debt. -/
theorem rows (F : List Arm) (J : ℕ) : ∃H R : ℕ, ∀v : ℕ, ∀f∈F, ∀j<J,
    run (H+f.delay) (input f (R+2^H*v+j))=run H (R+2^H*v) ∧
    f.debt+odds (H+f.delay) (input f (R+2^H*v+j))=odds H (R+2^H*v) := by
  let ref : Profile:=⟨0,0⟩
  let arms:=F.flatMap (fun f => (List.range J).map (post f))
  obtain ⟨H,R,core⟩:=finite_coalesce ref arms
  refine ⟨H,R,?_⟩
  intro v f inside j jl
  have mem : post f j∈arms := List.mem_flatMap.mpr
    ⟨f,inside,List.mem_map.mpr ⟨j,List.mem_range.mpr jl,rfl⟩⟩
  have prof:=cylinder H R v (post f j)
  rw [core _ mem] at prof
  have same:=cylinder H R v ref
  simp only [value,ref,pow_zero,one_mul,Nat.add_zero,Nat.zero_add] at same
  have pr:=prelude f j (R+2^H*v)
  obtain ⟨hit,gr⟩:=append f.delay H (input f (R+2^H*v+j))
  rw [Nat.add_comm f.delay H,pr.1] at hit gr
  refine ⟨hit.trans (prof.1.trans same.1.symm),?_⟩
  have pg:=prof.2
  have rg:=same.2
  rw [gr,←Nat.add_assoc,pr.2,pg,←rg]

#print axioms slope_or_small
#print axioms rows
end Collatz.AffineGeometry
