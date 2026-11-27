module

public import TowerFrontierAffine
import all TowerFrontierAffine

public section

namespace Collatz.Itinerary.TowerFrontier

set_option autoImplicit false
set_option maxRecDepth 8192
set_option maxHeartbeats 2000000
set_option exponentiation.threshold 2048

/-- The odd representative used for the common descent cylinder. -/
@[expose] def residue : Nat := 133502105534397197179223251332334886243204321438662346759814009092742871678744120907946073259538408800798224770203862342877210489142017968717475320808294669157462980384239439137262182530448362064335867815876677937419656898439276610599029951801427860099905379309466493735118259135223196714721224843654466592205

private def check (r : Nat) : Bool :=
  let z := stride 1024 (3^r*residue) r
  z.1 < residue && z.2 ≤ 643

private theorem certificate_0 : segment check 24 0 = true := by decide +kernel
private theorem certificate_24 : segment check 24 24 = true := by decide +kernel
private theorem certificate_48 : segment check 24 48 = true := by decide +kernel
private theorem certificate_72 : segment check 24 72 = true := by decide +kernel
private theorem certificate_96 : segment check 24 96 = true := by decide +kernel
private theorem certificate_120 : segment check 24 120 = true := by decide +kernel
private theorem certificate_144 : segment check 24 144 = true := by decide +kernel
private theorem certificate_168 : segment check 24 168 = true := by decide +kernel
private theorem certificate_192 : segment check 24 192 = true := by decide +kernel
private theorem certificate_216 : segment check 24 216 = true := by decide +kernel
private theorem certificate_240 : segment check 24 240 = true := by decide +kernel
private theorem certificate_264 : segment check 24 264 = true := by decide +kernel
private theorem certificate_288 : segment check 24 288 = true := by decide +kernel
private theorem certificate_312 : segment check 24 312 = true := by decide +kernel
private theorem certificate_336 : segment check 24 336 = true := by decide +kernel
private theorem certificate_360 : segment check 24 360 = true := by decide +kernel
private theorem certificate_384 : segment check 24 384 = true := by decide +kernel
private theorem certificate_408 : segment check 24 408 = true := by decide +kernel
private theorem certificate_432 : segment check 24 432 = true := by decide +kernel
private theorem certificate_456 : segment check 24 456 = true := by decide +kernel
private theorem certificate_480 : segment check 24 480 = true := by decide +kernel
private theorem certificate_504 : segment check 24 504 = true := by decide +kernel
private theorem certificate_528 : segment check 9 528 = true := by decide +kernel

private theorem certificate : segment check 537 0 = true :=
  (@segment_join check 264 273 0
    (@segment_join check 120 144 0
      (@segment_join check 48 72 0
        (@segment_join check 24 24 0 certificate_0 certificate_24)
        (@segment_join check 24 48 48
          certificate_48
          (@segment_join check 24 24 72 certificate_72 certificate_96)))
      (@segment_join check 72 72 120
        (@segment_join check 24 48 120
          certificate_120
          (@segment_join check 24 24 144 certificate_144 certificate_168))
        (@segment_join check 24 48 192
          certificate_192
          (@segment_join check 24 24 216 certificate_216 certificate_240))))
    (@segment_join check 144 129 264
      (@segment_join check 72 72 264
        (@segment_join check 24 48 264
          certificate_264
          (@segment_join check 24 24 288 certificate_288 certificate_312))
        (@segment_join check 24 48 336
          certificate_336
          (@segment_join check 24 24 360 certificate_360 certificate_384)))
      (@segment_join check 72 57 408
        (@segment_join check 24 48 408
          certificate_408
          (@segment_join check 24 24 432 certificate_432 certificate_456))
        (@segment_join check 24 33 480
          certificate_480
          (@segment_join check 24 9 504 certificate_504 certificate_528)))))

private theorem descent_of_track (h r w t e : Nat)
    (p : (track h (3^r*w) r).1 < w)
    (q : (track h (3^r*w) r).2 ≤ e) (size : 3^e ≤ 2^h) :
    run h (3^r*(w+2^h*t)) < w+2^h*t := by
  have bound := Nat.le_trans (Nat.pow_le_pow_right (by decide : 0<3) q) size
  have hx : 3^r*(w+2^h*t) = 3^r*w+2^h*3^r*t := by rw [Nat.mul_add]; ac_rfl
  rw [hx, affine]
  exact Nat.add_lt_add_of_lt_of_le p (Nat.mul_le_mul_right t bound)

private theorem rank_checked {r : Nat} (h : check r=true) :
    (track 1024 (3^r*residue) r).1<residue ∧ (track 1024 (3^r*residue) r).2≤643 := by
  simpa [check, stride_eq] using h

/-- Every one of 537 consecutive powers descends below the same unscaled base
    after exactly 1024 shortcut steps, throughout this odd residue class. -/
theorem tower_descent (t r : Nat) (hr : r ≤ 536) :
    run 1024 (3^r*(residue+2^1024*t)) < residue+2^1024*t := by
  have h := rank_checked (segment_sound (r:=r) certificate (by omega) (by omega))
  exact descent_of_track 1024 r residue t 643 h.1 h.2 (by decide)

#print axioms tower_descent

private theorem next_lift {m b : Nat} (hm : 0<m) (hb : b<m) (a : Nat) :
    ∃ q, a ≤ b+m*q ∧ b+m*q < a+m := by
  have split := Nat.mod_add_div a m
  have rem := Nat.mod_lt a hm
  by_cases h : a ≤ b+m*(a/m)
  · exact ⟨a/m,h,by omega⟩
  · refine ⟨a/m+1,?_⟩
    rw [Nat.mul_succ]
    omega

/-- Each eligible step-six progression contains a common 537-rank witness
    in every full period of its binary residues. -/
theorem eligible_progression (a : Nat) (ha : a%6=1 ∨ a%6=5) :
    ∃ i < 2^1023, ∀ r ≤ 536, run 1024 (3^r*(a+6*i)) < a+6*i := by
  let m := 2^1024
  obtain ⟨q,low,high⟩ := next_lift (m:=m) (b:=residue) (by decide) (by decide) a
  let x := residue+m*q
  have lo : a≤x := low
  have hi : x<a+m := high
  have par : x%2=1 := by simp [x,Nat.add_mod,Nat.mul_mod,show m%2=0 by decide,show residue%2=1 by decide]
  have mm : m%6=4 := by decide
  obtain ⟨j,hj,match6⟩ : ∃ j ≤ 2, (x+m*j)%6=a%6 := by
    by_cases h : x%6=a%6
    · exact ⟨0,by decide,by simpa using h⟩
    by_cases h' : (x%6+4)%6=a%6
    · exact ⟨1,by decide,by simpa [Nat.add_mod,mm] using h'⟩
    refine ⟨2,by decide,?_⟩
    rw [Nat.add_mod,Nat.mul_mod,mm]
    omega
  let y := x+m*j
  let i := (y-a)/6
  have ly : a≤y := Nat.le_trans lo (Nat.le_add_right _ _)
  have shape : a+6*i=y := by dsimp [i]; change y%6=a%6 at match6; omega
  have mj : m*j≤m*2 := Nat.mul_le_mul_left _ hj
  have hhalf : m=2*2^1023 := by decide
  refine ⟨i,by dsimp [y] at shape; omega,?_⟩
  have rep : y=residue+2^1024*(q+j) := by dsimp [y,x,m]; rw [Nat.mul_add,Nat.add_assoc]
  intro r hr
  rw [shape,rep]
  exact tower_descent (q+j) r hr

#print axioms eligible_progression

end Collatz.Itinerary.TowerFrontier
