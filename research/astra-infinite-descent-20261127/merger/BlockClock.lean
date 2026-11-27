import AffineProfiles
import FirstArrival

/-! Arbitrary finite families of additive shifts, with one prescribed dyadic
source class and arbitrary ternary source class, endpoint and sufficiently
large first clock. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.BlockClock
open TwoGapRouting FixedGapClock AffineProfiles FirstArrival

def Cover (F : List ℕ) (v r s B g : ℕ) : Prop :=
  ∀ D, B≤D → ∀ y, y%3≠0 → ∀c, ∃x, 0<x ∧ x ≡ r [MOD 2^v] ∧
    x ≡ c [MOD 3^s] ∧ ∀i∈0::F, run D (x+i)=y ∧ odds D (x+i)=g

private theorem prepare (F : List ℕ) (v r : ℕ) :
    ∃H R p a, R ≡ r [MOD 2^v] ∧ v≤H ∧
      ∀u, ∀i∈0::F, run H (R+2^H*u+i)=3^p*u+a ∧ odds H (R+2^H*u+i)=p := by
  let arm (i : ℕ) : Profile:=⟨0,i⟩
  let atV (i : ℕ):=advance v r (arm i)
  obtain ⟨h,t,all⟩:=finite_coalesce (atV 0) (F.map atV)
  let H:=v+h
  let R:=r+2^v*t
  let A:=advance H R (arm 0)
  have selected (i : ℕ) (hi : i∈0::F) : advance H R (arm i)=A := by
    rcases List.mem_cons.mp hi with same|rest
    · rw [same]
    · have m:=all _ (List.mem_map.mpr ⟨i,rest,rfl⟩)
      simpa only [atV,advance_comp] using m
  refine ⟨H,R,A.count,A.base,?_,by dsimp [H]; omega,?_⟩
  · simp [R,Nat.ModEq]
  · intro u i hi
    have res:=cylinder H R u (arm i)
    rw [selected i hi] at res
    simpa [arm,value] using res

private theorem close {H R p a s C L y : ℕ} (yc : y%3≠0)
    (late : 6*3^(p+s)<L) (large : 16*(a+1)≤L) :
    ∃u, 0<u ∧ R+2^H*u ≡ C [MOD 3^s] ∧
      run L (3^p*u+a)=y ∧ odds L (3^p*u+a)=2 := by
  obtain ⟨t,be⟩:=dyadic_class s H R C
  obtain ⟨w,_,_,_,_,_,res,_,hit,count,_⟩:=route (p+s) L y (3^p*t+a) late yc
  have phys:=SharpClock.physical_height L w
  rw [hit,count] at phys
  have yy := Nat.le_mul_of_pos_right (2^L) (show 0<y by omega)
  have growth : L≤2^L := (show L<2^L from Nat.lt_two_pow_self).le
  have aw : a<w := by norm_num at phys; omega
  rw [pow_add] at res
  have md:=res.of_dvd (dvd_mul_right (3^p) (3^s))
  have wmod : w ≡ a [MOD 3^p] := md.trans (by simp [Nat.ModEq])
  obtain ⟨u,du⟩:=(Nat.modEq_iff_dvd' aw.le).mp wmod.symm
  have eq : w=3^p*u+a := by omega
  have res' : 3^p*u+a ≡ 3^p*t+a [MOD 3^p*3^s] := by rw [←eq]; exact res
  have win:=Nat.ModEq.mul_left_cancel' (by positivity : (3:ℕ)^p≠0) (res'.add_right_cancel' a)
  have cl:=((win.mul_left (2^H)).add_right R).trans be
  refine ⟨u,?_,by simpa only [Nat.add_comm R] using cl,by rwa [←eq],by rwa [←eq]⟩
  by_contra! none
  rw [show u=0 by omega] at eq
  simp at eq
  omega

/-- After a constant depending on the finite offsets and binary/ternary
precisions, every supplied common clock and ternary-unit target works.
The common odd grade is independent of all target and clock choices. -/
theorem cover (F : List ℕ) (v r s : ℕ) : ∃ B g, Cover F v r s B g := by
  obtain ⟨H,R,p,a,binary,vH,paths⟩:=prepare F v r
  let B:=H+(6*3^(p+s)+1)+16*(a+1)
  refine ⟨B,p+2,?_⟩
  intro D late y unit c
  let L:=D-H
  have dl : H+L=D := by dsimp [L,B] at *; omega
  obtain ⟨u,up,xc,endp,lastGrade⟩:=close (H:=H) (R:=R) (C:=c) unit
    (show 6*3^(p+s)<L by dsimp [L,B] at *; omega)
    (show 16*(a+1)≤L by dsimp [L,B] at *; omega)
  refine ⟨R+2^H*u,by positivity,?_,xc,?_⟩
  · have prefixCongr : R+2^H*u ≡ R [MOD 2^H] := by simp [Nat.ModEq]
    exact (prefixCongr.of_dvd (pow_dvd_pow (2:ℕ) vH)).trans binary
  · intro i hi
    obtain ⟨p1,p2⟩:=paths u i hi
    obtain ⟨w,g⟩:=append H L (R+2^H*u+i)
    rw [dl,p1,endp] at w
    rw [dl,p1,p2,lastGrade] at g
    exact ⟨w,g⟩

/-- The entire finite family first reaches even or odd unit target y at the
supplied clock, including when y belongs to a cycle. -/
theorem first_cover (F : List ℕ) (v r s : ℕ) : ∃B g, ∀D, B≤D → ∀y, y%3≠0 →
    ∀c, ∃x, 0<x ∧ x ≡ r [MOD 2^v] ∧ x ≡ c [MOD 3^s] ∧
      ∀i∈0::F, First D (x+i) y ∧ odds D (x+i)=g := by
  obtain ⟨B,g,base⟩:=cover F v r s
  refine ⟨B+10,g+1,?_⟩
  intro D late y unit c
  obtain ⟨b,e,_,bu,_,eb,away,leg,ec⟩:=branch y unit
  obtain ⟨x,xp,xb,xc,all⟩:=base (D-e) (by omega) b bu c
  have clock : D-e+e=D := by omega
  refine ⟨x,xp,xb,xc,?_⟩
  intro i hi
  obtain ⟨meet,grade⟩:=all i hi
  have eq:=(append (D-e) e (x+i)).2
  rw [clock,meet,grade,ec] at eq
  exact ⟨clock ▸ join meet away leg,eq⟩

#print axioms cover
#print axioms first_cover
end Collatz.BlockClock
