import PostWords

namespace RampShadow.BandParents

open Postpeak

/-- A native odd-even-even factor in the sixfold band has an explicitly
    smaller odd predecessor of the actual last state. -/
theorem odd_even_even {X x y peak : ℤ} (xp : 0<x)
    (odd : 3*x+1=2*peak) (even₂ : peak=4*y) (top : peak≤6*X) :
    ∃ m : ℤ, 0<m ∧ m<X ∧ 4*m+1=x ∧ Walk 1 1 m y := by
  let m := (x-1)/4
  have E : 3*x+1=8*y := by omega
  have eq : 4*m+1=x := by dsimp [m];omega
  exact ⟨m,by omega,by omega,eq,.odd (by omega) (.nil y)⟩

def word29 : Word :=
  [true,true,false,true,true,false,true,true,false,true,true,false,true,false,true,
    false,true,true,false,true,false,true,true,true,false,true,false,true,true]

def prefix11 : Word :=
  [true,true,false,true,true,false,true,true,false,true,true]

def lower28 : Word :=
  [true,true,true,true,true,true,true,true,true,true,true,true,false,true,false,true,
    false,true,true,true,false,true,false,true,false,false,false,false]

private theorem word_constants :
    word29.length=29 ∧ weight word29=19 ∧ intercept word29=5895447367 ∧
    prefix11.length=11 ∧ weight prefix11=8 ∧ intercept prefix11=12325 ∧
    lower28.length=28 ∧ weight lower28=19 ∧ intercept lower28=1204331483 := by decide

/-- For a literal 29-letter word, the affordable partner is (x+3)/2.
    The only required local size comparison is at the eleventh state.
    No convergence assumption on either ordinary start is used. -/
theorem motif_twenty_nine {x X y : ℤ} (floor : 2≤X) (xp : 0<x)
    (native : (2:ℤ)^word29.length*y=3^weight word29*x+intercept word29)
    (band : 2*run 11 x≤9*X) :
    ∃ m : ℤ, 0<m ∧ m<X ∧ 2*m=x+3 ∧ Walk 28 19 m y ∧ Walk 29 19 x y := by
  obtain ⟨L,W,A,Lp,Wp,Ap,Lb,Wb,Ab⟩ := word_constants
  have upper := walk_of_word word29 x y native
  rw [L,W] at upper
  rw [L,W,A] at native
  norm_num at native
  let r := 526520403*y-1139853850*x-5781787119
  have origin : x=29253627+536870912*r := by dsimp [r];linarith only [native]
  let peak := 93717314+1719926784*r
  have peq : 2048*peak=6561*x+12325 := by dsimp only [peak];linear_combination -6561*origin
  have PW := walk_of_word prefix11 x peak (by rw [Lp,Wp,Ap];norm_num;exact peq)
  rw [Lp,Wp] at PW
  rw [(readout PW).1] at band
  let m := 14626815+268435456*r
  have eq : 2*m=x+3 := by dsimp only [m];linear_combination -origin
  have hit := walk_of_word lower28 m y (by rw [Lb,Wb,Ab];norm_num;linarith only [native,eq])
  rw [Lb,Wb] at hit
  exact ⟨m,by linarith only [eq,xp],by linarith only [eq,peq,band,floor],eq,hit,upper⟩

end RampShadow.BandParents

#print axioms RampShadow.BandParents.odd_even_even
#print axioms RampShadow.BandParents.motif_twenty_nine
