import OctaveCriterion

/-! Actual intersections of two ordinary orbits through the exact residue mixing clock. -/

namespace CollatzShell.PeriodicWindow

/-- In coordinates `x+1`, odd steps contribute no additive term. -/
private theorem shifted_affine (l n : Nat) : ∃ a B : Nat, B≤3^l ∧
    2^l*(orbit l n+1)=3^a*(n+1)+B := by
  induction l with
  | zero => exact ⟨0,0,by decide,by simp [orbit]⟩
  | succ l ih =>
    obtain ⟨a,B,small,eq⟩ := ih
    let x := orbit l n
    have chain : orbit (l+1) n=step x := by rw [orbit_add]; rfl
    by_cases h : x%2=0
    · have one : 2*(step x+1)=x+1+1 := by simp [step,h]; omega
      refine ⟨a,B+2^l,?_,?_⟩
      · have bound : 2^l≤3^l := Nat.pow_le_pow_left (by decide) _
        rw [pow_succ]; omega
      · rw [chain,pow_succ, Nat.mul_assoc,one,Nat.mul_add,eq]; ring
    · have one : 2*(step x+1)=3*(x+1) := by simp [step,h]; omega
      refine ⟨a+1,3*B,by rw [pow_succ]; omega,?_⟩
      rw [chain,pow_succ 2, Nat.mul_assoc,one,show 2^l*(3*(x+1))=3*(2^l*(x+1)) by ring]
      change 3*(2^l*(orbit l n+1))=_
      rw [eq,pow_succ]; ring

private theorem rise_prefix (b i u : Nat) (hi : i≤b) (hu : 0<u) :
    orbit i (2^b*u-1)+1=3^i*(2^(b-i)*u) := by
  have pos : 0<2^(b-i)*u := by positivity
  have e := (odd_run i _ pos).1
  rw [← Nat.mul_assoc, ← pow_add, Nat.add_sub_of_le hi] at e
  rw [e,Nat.sub_add_cancel (show 0<3^i*(2^(b-i)*u) by positivity)]

private theorem profile (b L i u : Nat) (hu : 0<u) (hi : i≤b+L) :
    ∃ a R : Nat, min i b ≤ a ∧ R≤3^L ∧ (i≤b → R=0) ∧
      2^L*(orbit i (2^b*u-1)+1) = 2^(b+L-i)*3^a*u+R := by
  by_cases early : i≤b
  · refine ⟨i,0,min_le_left _ _,Nat.zero_le _,fun _ => rfl,?_⟩
    rw [rise_prefix _ _ _ early hu,show b+L-i=L+(b-i) by omega,pow_add]; ring
  · let l := i-b
    have il : i=b+l := by dsimp [l]; omega
    have ll : l≤L := by dsimp [l]; omega
    obtain ⟨a,B,small,eq⟩ := shifted_affine l (orbit b (2^b*u-1))
    rw [← orbit_add,← il,rise_prefix b b u le_rfl hu,Nat.sub_self,pow_zero,one_mul] at eq
    refine ⟨a+b,2^(L-l)*B,by omega,?_,by omega,?_⟩
    · have cmp : 2^(L-l)≤3^(L-l) := Nat.pow_le_pow_left (by decide) _
      simpa only [← pow_add,Nat.sub_add_cancel ll] using Nat.mul_le_mul cmp small
    · calc 2^L*(orbit i (2^b*u-1)+1) = 2^(L-l)*(2^l*(orbit i (2^b*u-1)+1)) := by
             rw [← Nat.mul_assoc,← pow_add,Nat.sub_add_cancel ll]
           _ = _ := by rw [eq,pow_add,show b+L-i=L-l by omega]; ring

private theorem distinct_cores {u v : Nat} (uo : u%2=1) (vo : v%2=1) (uv : u<v) (gap : v<3*u)
    (i j a d : Nat) : 2^i*3^a*u ≠ 2^j*3^d*v := by
  intro eq
  have odd3 (x : Nat) : 3^x%2=1 := by induction x with | zero => rfl | succ x ih => rw [pow_succ]; omega
  rw [Nat.mul_assoc,Nat.mul_assoc] at eq
  have same := odd_core (by rw [Nat.mul_mod,odd3,uo]) (by rw [Nat.mul_mod,odd3,vo]) i j eq
  by_cases ad : a≤d
  · have h₁ := Nat.mul_lt_mul_of_pos_left uv (by positivity : 0<3^a)
    have h₂ := Nat.mul_le_mul_right v (Nat.pow_le_pow_right (by decide : 0<3) ad)
    omega
  · have h₁ := Nat.mul_lt_mul_of_pos_left gap (by positivity : 0<3^d)
    have h₂ := Nat.mul_le_mul_right u (Nat.pow_le_pow_right (by decide : 0<3) (by omega : d+1≤a))
    rw [pow_succ,Nat.mul_assoc] at h₂
    omega

private theorem low_high {b L i j u v w z : Nat} (hw : w≤v) (hz : u≤z) (wu : 0<w) (zu : 0<z)
    (ui : 0<u) (gap : v≤2*u) (margin : 2^(b+1)*3^L<3^b) (lb : L<b)
    (low : i≤L) (late : b<j) (time : j≤b+L) :
    orbit i (2^b*w-1)<orbit j (2^b*z-1) := by
  obtain ⟨a,R,az,_,_,eq⟩ := profile b L j z zu time
  have za : b≤a := by simpa [Nat.min_eq_right late.le] using az
  have top : 2^(b+L-j)*3^a ≥ 3^b := by
    exact (Nat.pow_le_pow_right (by decide) za).trans
      (by simpa only [one_mul] using Nat.mul_le_mul_right (3^a) (Nat.one_le_pow (b+L-j) 2 (by decide)))
  have early : 2^L*(orbit i (2^b*w-1)+1) ≤ 2^b*3^L*v := by
    rw [rise_prefix _ _ _ (by omega) wu]
    have splitPow : 2^L*2^(b-i)=2^b*2^(L-i) := by rw [← pow_add,← pow_add]; congr 1; omega
    have cmp : 2^(L-i)*3^i ≤ 3^L := by
      simpa only [← pow_add,Nat.sub_add_cancel low] using
        Nat.mul_le_mul_right (3^i) (Nat.pow_le_pow_left (by decide : 2≤3) (L-i))
    calc _ = (2^L*2^(b-i))*3^i*w := by ring
         _ = 2^b*(2^(L-i)*3^i)*w := by rw [splitPow]; ring
         _ ≤ _ := Nat.mul_le_mul (Nat.mul_le_mul_left _ cmp) hw
  have upper := Nat.mul_le_mul_left (2^b*3^L) gap
  have middle := Nat.mul_lt_mul_of_pos_right margin ui
  rw [show 2^(b+1)*3^L*u=2^b*3^L*(2*u) by ring] at middle
  have h := early.trans_lt (upper.trans_lt (middle.trans_le (Nat.mul_le_mul top hz)))
  have hh := Nat.lt_of_mul_lt_mul_left (by omega : 2^L*(orbit i (2^b*w-1)+1)<2^L*(orbit j (2^b*z-1)+1))
  omega

private theorem strip_offset {b L a R i u : Nat} (high : L<a) (small : R≤3^L) :
    (2^(b+L-i)*3^a*u+R) % 3^(L+1)=R := by
  have dvd : 3^(L+1) ∣ 2^(b+L-i)*3^a*u := by
    have da : L+1+(a-(L+1))=a := by omega
    refine ⟨2^(b+L-i)*3^(a-(L+1))*u,?_⟩
    calc _ = 2^(b+L-i)*3^(L+1+(a-(L+1)))*u := by rw [da]
         _ = _ := by rw [pow_add]; ring
  have pos : 0<3^L := by positivity
  have bound : R<3^(L+1) := by rw [pow_succ]; omega
  rw [Nat.add_mod,Nat.mod_eq_zero_of_dvd dvd,zero_add,Nat.mod_eq_of_lt bound,Nat.mod_eq_of_lt bound]

/-- The two ordinary arms fail to intersect at *any* pair of clocks in the given horizon. -/
theorem disjoint_rises {b L u v : Nat} (lb : L<b) (margin : 2^(b+1)*3^L<3^b)
    (uo : u%2=1) (vo : v%2=1) (uv : u<v) (ratio : v≤2*u) :
    meetsBy (b+L) (2^b*u-1) (2^b*v-1)=false := by
  apply decide_eq_false
  rintro ⟨i,j,hit⟩
  have ui : 0<u := by omega
  have vi : 0<v := by omega
  have it : i.val≤b+L := by omega
  have jt : j.val≤b+L := by omega
  obtain ⟨a,R,az,rs,first,eq⟩ := profile b L i.val u ui it
  obtain ⟨d,S,dz,ss,second,eq'⟩ := profile b L j.val v vi jt
  have glue := eq.symm.trans ((congrArg (fun n => 2^L*(n+1)) hit).trans eq')
  have no := distinct_cores uo vo uv (by omega) (b+L-i.val) (b+L-j.val) a d
  by_cases both : i.val≤b ∧ j.val≤b
  · rw [first both.1,second both.2] at glue; omega
  by_cases si : i.val≤L
  · have lt := low_high (b:=b) (L:=L) (w:=u) (z:=v) (u:=u) (v:=v)
      uv.le uv.le ui vi ui ratio margin lb si (by omega) jt
    omega
  by_cases sj : j.val≤L
  · have lt := low_high (b:=b) (L:=L) (w:=v) (z:=u) (u:=u) (v:=v)
      le_rfl le_rfl vi ui ui ratio margin lb sj (by omega) it
    omega
  have ah : L<a := by omega
  have dh : L<d := by omega
  have same := congrArg (fun n => n%3^(L+1)) glue
  change (_+R)%3^(L+1)=(_+S)%3^(L+1) at same
  rw [strip_offset ah rs,strip_offset dh ss] at same
  omega

private theorem margin_at (s : Nat) (hs : 3≤s) : 2^(5*s+1)*3^(s+s/2)<3^(5*s) := by
  have pow : 3^(s/2) ≤ 2^s := by
    calc 3^(s/2) ≤ 4^(s/2) := Nat.pow_le_pow_left (by decide) _
         _ = 2^(2*(s/2)) := by rw [pow_mul]; rfl
         _ ≤ 2^s := Nat.pow_le_pow_right (by decide) (by omega)
  have strict : 2*192^s < 243^s := by
    obtain ⟨j,rfl⟩ := Nat.exists_eq_add_of_le hs
    rw [pow_add,pow_add]
    have positive : 0<192^j := by positivity
    have big := Nat.pow_le_pow_left (by decide : 192≤243) j
    calc 2*(192^3*192^j) = (2*192^3)*192^j := by ring
         _ < 243^3*192^j := Nat.mul_lt_mul_of_pos_right (by decide) positive
         _ ≤ _ := Nat.mul_le_mul_left _ big
  calc 2^(5*s+1)*3^(s+s/2) ≤ 2^(5*s+1)*(3^s*2^s) := by
         rw [pow_add (3:Nat) s]; exact Nat.mul_le_mul_left _ (Nat.mul_le_mul_left _ pow)
       _ = 2*192^s := by
         rw [pow_succ,pow_mul,show (192:Nat)=2^5*(3*2) by decide,mul_pow,mul_pow]; ring
       _ < 243^s := strict
       _ = 3^(5*s) := by rw [pow_mul]; rfl

/-- On every stage `s ≥ 3`, exponentially many genuine comparisons still miss after
    the exact mixing clock plus another `floor(s/2)` steps on each arm. -/
theorem octave_deadline (s : Nat) (hs : 3≤s) :
    2^(s-1) ≤ (unmatched (64^s) (6*s+s/2)).card := by
  let p := 64^s
  let d := 2^s
  let B := 2^(5*s)
  have dp : 0<d := by dsimp [d]; positivity
  have bp : 0<B := by dsimp [B]; positivity
  have prod : B*d=p := by dsimp [B,d,p]; rw [← pow_add,show 5*s+s=6*s by omega,pow_mul]; rfl
  have dv : d=2*2^(s-1) := by dsimp [d]; rw [← Nat.pow_succ']; congr 1; omega
  let u (w : Nat) := d+2*w+1
  let x (w : Nat) := B*(u w+d)-1
  have inj : Function.Injective x := by
    intro w z eq
    have e (h : Nat) : 0<B*(u h+d) := Nat.mul_pos bp (by dsimp [u]; omega)
    change B*(u w+d)-1=B*(u z+d)-1 at eq
    have m : B*(u w+d)=B*(u z+d) := by have := e w; have := e z; omega
    have := Nat.eq_of_mul_eq_mul_left bp m
    dsimp [u] at this; omega
  let W := Finset.range (2^(s-1))
  have subset : W.image x ⊆ unmatched p (6*s+s/2) := by
    intro y hy
    obtain ⟨w,hw,rfl⟩ := Finset.mem_image.mp hy
    have wlt := Finset.mem_range.mp hw
    have rangeU : d<u w ∧ u w<2*d := by dsimp [u]; omega
    let ref := B*u w-1
    have lo : p≤ref := by have := Nat.mul_le_mul_left B (show d+1≤u w by omega); rw [Nat.mul_add,prod] at this; dsimp [ref]; omega
    have hi : ref<2*p := by have := Nat.mul_lt_mul_of_pos_left rangeU.2 bp; rw [show B*(2*d)=2*p by rw [← prod]; ring] at this; dsimp [ref]; omega
    have add : x w=ref+p := by dsimp [x,ref]; rw [Nat.mul_add,prod]; have := Nat.mul_pos bp (show 0<u w by omega); omega
    have target : p+x w%p=ref := by
      have pp : 0<p := by dsimp [p]; positivity
      rw [add,Nat.add_mod_right,show ref=(ref-p)+p by omega,Nat.add_mod_right,Nat.mod_eq_of_lt (by omega)]
      omega
    have uo : u w%2=1 := by dsimp [u]; omega
    have vo : (u w+d)%2=1 := by dsimp [u]; omega
    have no := disjoint_rises (b:=5*s) (L:=s+s/2) (by omega) (margin_at s hs) uo vo (by omega) (by omega)
    refine Finset.mem_filter.mpr ⟨Finset.mem_Ico.mpr ⟨by omega,by omega⟩,?_⟩
    rw [target]; unfold meetsBy at *; apply decide_eq_false
    rintro ⟨i,j,e⟩
    rw [show 5*s+(s+s/2)=6*s+s/2 by omega] at no
    exact (decide_eq_false_iff_not.mp no) ⟨j,i,e.symm⟩
  have count := Finset.card_le_card subset
  rwa [Finset.card_image_of_injective _ inj,Finset.card_range] at count

#print axioms octave_deadline

end CollatzShell.PeriodicWindow
