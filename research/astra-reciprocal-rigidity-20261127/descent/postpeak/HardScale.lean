import ScaledRamp
import SignedEscape

namespace RampShadow.Postpeak

/-- Right before the first of the remaining odd departures. In the
    zero-grade case the suffix is empty. -/
private theorem split_odd_start {e k x y} (W : Walk e k x y) (b j : ℕ) (E : k=b+j) :
    ∃ d l z, e=d+l ∧ Walk d b x z ∧ Walk l j z y ∧
      ((j=0 ∧ l=0) ∨ z%2=1) := by
  induction W generalizing b with
  | nil x =>
    have B : b=0 := by omega
    have J : j=0 := by omega
    subst b;subst j
    exact ⟨0,0,x,rfl,.nil x,.nil x,Or.inl ⟨rfl,rfl⟩⟩
  | @even h p x y W IH =>
    obtain ⟨d,l,z,E,P,Q,S⟩ := IH b E
    exact ⟨d+1,l,z,by omega,.even P,Q,S⟩
  | @odd h p x z y edge W IH =>
    cases b with
    | zero =>
      have J : j=p+1 := by omega
      subst j
      refine ⟨0,h+1,x,by omega,.nil x,.odd edge W,Or.inr ?_⟩
      omega
    | succ b =>
      obtain ⟨d,l,w,H,P,Q,S⟩ := IH b (by omega)
      exact ⟨d+1,l,w,by omega,.odd edge P,Q,S⟩

/-- Pulling a formal negative source backwards through any word multiplies
    its magnitude by at most 2 for each even inverse. -/
theorem weighted_intercept_ceiling (w : Word) :
    2^w.length+intercept w ≤ (3:ℤ)^weight w*2^(w.length-weight w) := by
  induction w with
  | nil => norm_num [weight,intercept]
  | cons o w IH =>
    have W := weight_le w
    cases o with
    | false =>
      simp only [List.length_cons,weight,intercept,show w.length+1-weight w=(w.length-weight w)+1 by omega,pow_succ]
      nlinarith only [IH]
    | true =>
      simp only [List.length_cons,weight,intercept,show w.length+1-(weight w+1)=w.length-weight w by omega,pow_succ]
      have X := mul_le_mul_of_nonneg_left (one_le_pow₀ (show (1:ℤ)≤2 by norm_num) (n:=w.length-weight w))
        (show (0:ℤ)≤3^weight w by positivity)
      nlinarith only [IH,X]

/-- Every competitor of grade j+b splits into its inverse prefix and a
    true signed suffix from a small odd magnitude, with an explicit
    linear equation for its source. -/
theorem scaled_descriptor {j b δ e : ℕ} {n m v : ℤ}
    (rise : (2:ℤ)^j*v=2^δ*(n+1)) (W : Walk e (b+j) m (3^j*v-1)) :
    ∃ (α : Word) (l : ℕ) (M : ℤ),
      weight α=b ∧ e=α.length+j+l ∧ 1≤M ∧ M≤(2:ℤ)^l ∧
      ((j=0 ∧ l=0 ∧ M=1) ∨ M%2=1) ∧
      Walk (j+l) j (-M) (-1) ∧
      3^b*m=2^(α.length+l+δ)*(n+1)-(2^α.length*M+intercept α) := by
  obtain ⟨d,f,z,ef,P,Q,start⟩ := split_odd_start W b j rfl
  have jf := count_le Q
  let l := f-j
  have fl : f=j+l := by dsimp [l];omega
  obtain ⟨β,bl,bw,eq⟩ := word_of_walk Q
  let M := (2:ℤ)^f*v-z
  have sig : Walk f j (-M) (-1) := by
    have tailEq : (2:ℤ)^β.length*(-1)=3^weight β*(-M)+intercept β := by
      rw [bl,bw]
      dsimp [M]
      nlinarith only [eq]
    simpa only [bl,bw] using walk_of_word β (-M) (-1) tailEq
  have MP : 1≤M := by
    by_contra! N
    have G := nonneg_end sig (show 0≤ -M by omega)
    omega
  have cap := origin_magnitude sig
  rw [abs_of_nonpos (show -M≤0 by omega)] at cap
  norm_num at cap
  have odd : (j=0 ∧ l=0 ∧ M=1) ∨ M%2=1 := by
    rcases start with ⟨J,F⟩|Z
    · have L : l=0 := by omega
      exact Or.inl ⟨J,L,by simpa only [F,J,Nat.sub_zero,pow_zero] using (show M=1 by
        rw [F,J] at cap;norm_num at cap;omega)⟩
    · by_cases F : f=0
      · have jj : j=0 := by omega
        have mm : M=1 := by rw [F,jj] at cap;norm_num at cap;omega
        exact Or.inl ⟨jj,by omega,mm⟩
      · obtain ⟨r,R⟩ := Nat.exists_eq_succ_of_ne_zero F
        have even : (2:ℤ)^f*v%2=0 := by rw [R,pow_succ];ring_nf;omega
        dsimp [M]
        omega
  obtain ⟨α,al,aw,ae⟩ := word_of_walk P
  have zm : z=(2:ℤ)^(l+δ)*(n+1)-M := by
    dsimp [M]
    have H := congrArg (fun a : ℤ => (2:ℤ)^l*a) rise
    rw [fl,pow_add,pow_add]
    nlinarith only [H]
  refine ⟨α,l,M,aw,by omega,MP,by simpa only [l] using cap,odd,fl ▸ sig,?_⟩
  rw [al,pow_add (2:ℤ) (d+l) δ,pow_add (2:ℤ) d l]
  rw [zm,pow_add (2:ℤ) l δ] at ae
  nlinarith only [ae]

end RampShadow.Postpeak

#print axioms RampShadow.Postpeak.scaled_descriptor
