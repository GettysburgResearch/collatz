import AffineGeometry

/-! Exact classification of finite positive affine families which meet
at arbitrarily large parameters within a single bounded physical clock
budget. The common endpoint and the individual clocks may vary freely. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.PrimeCore
open TwoGapRouting AffineGeometry
open Nat

def core (a : ℕ) : ℕ := ordCompl[3] (ordCompl[2] a)

private theorem peel (p q a : ℕ) : core (2^p*3^q*a)=core a := by
  have clean3 : ordCompl[2] (3^q) = 3^q :=
    (Nat.ordCompl_eq_self_iff_zero_or_not_dvd (3^q) Nat.prime_two).mpr
      (Or.inr (fun bad => (by decide : ¬2 ∣ (3:ℕ)) (Nat.prime_two.dvd_of_dvd_pow bad)))
  unfold core
  rw [Nat.mul_assoc,Nat.ordCompl_self_pow_mul _ _ Nat.prime_two,
    Nat.ordCompl_mul,clean3,Nat.ordCompl_self_pow_mul _ _ Nat.prime_three]

structure Form where
  slope : ℕ
  shift : ℕ
  deriving DecidableEq

def normalized (f : Form) : Arm := ⟨f.slope.factorization 2,(ordCompl[2] f.slope).factorization 3,f.shift⟩

theorem reconstruct (f : Form) : core f.slope*2^(normalized f).delay*3^(normalized f).debt=f.slope := by
  have first:=Nat.ordProj_mul_ordCompl_eq_self f.slope 2
  have second:=Nat.ordProj_mul_ordCompl_eq_self (ordCompl[2] f.slope) 3
  change 2^f.slope.factorization 2*(ordCompl[2] f.slope)=f.slope at first
  change 3^(ordCompl[2] f.slope).factorization 3*core f.slope=ordCompl[2] f.slope at second
  change core f.slope*2^f.slope.factorization 2*3^(ordCompl[2] f.slope).factorization 3=f.slope
  rw [←second] at first
  simpa only [Nat.mul_assoc,Nat.mul_left_comm,Nat.mul_comm] using first

/-- A clock bound is fixed before the parameters are taken arbitrarily
large. A common endpoint is selected for the entire family at each
parameter; every arm may choose a different ordinary time up to the bound. -/
def BoundedMeet (F : List Form) : Prop :=
  ∃ H : ℕ, ∀ N : ℕ, ∃ t z : ℕ, N≤t ∧
    ∀f∈F, ∃i≤H, run i (f.slope*t+f.shift)=z

theorem necessary (F : List Form) (unbounded : BoundedMeet F) :
    ∀f∈F,∀g∈F,core f.slope=core g.slope := by
  obtain ⟨H,visits⟩:=unbounded
  intro f hf g hg
  obtain ⟨t,z,large,both⟩:=visits (6^H*(max f.shift g.shift+1)+1)
  obtain ⟨i,ic,fi⟩:=both f hf
  obtain ⟨j,jc,gj⟩:=both g hg
  rcases slope_or_small _ _ _ _ _ _ _ H ic jc (fi.trans gj.symm) with slope|small
  · have eq:=congrArg core slope
    simpa only [peel] using eq
  · omega

def delayBound (F : List Form) := (F.map (fun f => (normalized f).delay)).foldr max 0

theorem delay_le {f : Form} {F : List Form} (inside : f∈F) :
    (normalized f).delay≤delayBound F := by
  induction F with
  | nil => simp at inside
  | cons a F ih =>
    change (normalized f).delay≤max (normalized a).delay (delayBound F)
    rcases List.mem_cons.mp inside with eq|rest
    · exact eq ▸ le_max_left _ _
    · exact (ih rest).trans (le_max_right _ _)

theorem sufficient (F : List Form) (m : ℕ) (mp : 0<m) (common : ∀f∈F,core f.slope=m) :
    BoundedMeet F := by
  obtain ⟨H,R,sync⟩:=rows (F.map normalized) (m+1)
  refine ⟨H+delayBound F,?_⟩
  intro N
  let u:=m*N
  let U:=R+2^H*u
  let t:=U/m+1
  let j:=m-U%m
  have jm : j<m+1 := by dsimp [j]; omega
  have ud:=Nat.mod_add_div U m
  have rem:=Nat.mod_lt U mp
  have mt : m*t=U+j := by dsimp [t,j]; rw [Nat.mul_add,Nat.mul_one]; omega
  have um : m*N≤U := (Nat.le_mul_of_pos_left u (by positivity : 0<(2:ℕ)^H)).trans (by
    dsimp [U]; omega)
  have nt : N≤t := by
    have div : N≤U/m := (Nat.le_div_iff_mul_le mp).mpr (by simpa only [Nat.mul_comm] using um)
    dsimp [t]; omega
  refine ⟨t,run H U,nt,?_⟩
  intro f hf
  let a:=normalized f
  have inlist : a∈F.map normalized := List.mem_map.mpr ⟨f,hf,rfl⟩
  have p:=(sync u a inlist j jm).1
  change run (H+a.delay) (input a (U+j))=run H U at p
  have rebuild:=reconstruct f
  rw [common f hf] at rebuild
  have form : input a (m*t)=f.slope*t+f.shift := by
    change 2^a.delay*3^a.debt*(m*t)+f.shift=f.slope*t+f.shift
    rw [←rebuild]
    dsimp [a]; ring
  refine ⟨H+a.delay,Nat.add_le_add_left (delay_le hf) H,?_⟩
  rw [←form,mt]
  exact p

theorem characterization (F : List Form) (positive : ∀f∈F,0<f.slope) :
    BoundedMeet F ↔ ∀f∈F,∀g∈F,core f.slope=core g.slope := by
  refine ⟨necessary F,?_⟩
  intro common
  cases F with
  | nil => exact ⟨0,fun N => ⟨N,0,le_rfl,by simp⟩⟩
  | cons f F =>
    have pos:=positive f List.mem_cons_self
    have nonzero : 0<core f.slope := Nat.ordCompl_pos 3 (Nat.ordCompl_pos 2 pos.ne').ne'
    exact sufficient (f::F) (core f.slope) nonzero
      (fun g hg => common g hg f List.mem_cons_self)

#print axioms reconstruct
#print axioms necessary
#print axioms sufficient
#print axioms characterization
end Collatz.PrimeCore
