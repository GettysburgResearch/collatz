import BandSteering

/-! Odd, injective inverse fans inside the actual shrinking dyadic section. -/

namespace CollatzShell.ForwardSection

open Real

/-- The last six-clock inverse carries only this many initial halvings. -/
def fanPadding (bit : Bool) (q : Nat) : Nat :=
  match q % 9 with
  | 1 => if bit then 2 else 4
  | 2 => if bit then 3 else 5
  | 4 => if bit then 0 else 4
  | 5 => if bit then 1 else 3
  | 7 => if bit then 0 else 2
  | _ => if bit then 1 else 5

def bareChild (bit : Bool) (q : Nat) : Nat := child bit q / 2^(fanPadding bit q)

theorem bareChild_spec (bit : Bool) (q : Nat) (hu : q%3 ≠ 0) :
    fanPadding bit q ≤ 5 ∧
    2^(fanPadding bit q)*bareChild bit q = child bit q ∧
    bareChild bit q % 2 = 1 ∧ bareChild bit q % 3 ≠ 0 := by
  have choices : q%9=1 ∨ q%9=2 ∨ q%9=4 ∨ q%9=5 ∨ q%9=7 ∨ q%9=8 := by omega
  rcases choices with e|e|e|e|e|e <;> cases bit <;>
    simp [bareChild,fanPadding,child,e] <;> omega

/-- Strip only the initial padding from the last member of the existing equal-clock fan. -/
def oddFan : (s : Nat) → (Fin s → Bool) → Nat → Nat
  | 0, _, z => z
  | s+1, w, z => bareChild (w (Fin.last s)) (fan s (fun i => w i.castSucc) z)

def oddFanPadding : (s : Nat) → (Fin s → Bool) → Nat → Nat
  | 0, _, _ => 0
  | s+1, w, z => fanPadding (w (Fin.last s)) (fan s (fun i => w i.castSucc) z)

theorem oddFan_spec (s : Nat) (hs : 0<s) (w : Fin s → Bool) (z : Nat)
    (hu : z%3≠0) :
    oddFanPadding s w z ≤ 5 ∧
    2^(oddFanPadding s w z)*oddFan s w z = fan s w z ∧
    oddFan s w z % 2 = 1 ∧ oddFan s w z % 3 ≠ 0 := by
  cases s with
  | zero => omega
  | succ s =>
    exact bareChild_spec _ _ (fan_spec s (fun i => w i.castSucc) z hu).2.1

theorem oddFan_clock (s : Nat) (hs : 0<s) (w : Fin s → Bool) (z : Nat)
    (hu : z%3≠0) : orbit (6*s-oddFanPadding s w z) (oddFan s w z)=z := by
  obtain ⟨pb,pad,_,_⟩ := oddFan_spec s hs w z hu
  have bound : oddFanPadding s w z ≤ 6*s := by omega
  have undo : orbit (oddFanPadding s w z) (fan s w z)=oddFan s w z := by
    rw [← pad,orbit_pad]
  have eq := orbit_add (oddFanPadding s w z) (6*s-oddFanPadding s w z) (fan s w z)
  rw [Nat.add_sub_of_le bound,(fan_spec s w z hu).1,undo] at eq
  exact eq.symm

theorem oddFan_hit (s : Nat) (hs : 0<s) (w : Fin s → Bool) (z : Nat)
    (hu : z%3≠0) : Hits (oddFan s w z) z :=
  ⟨6*s-oddFanPadding s w z,oddFan_clock s hs w z hu⟩

/-- The padded fan stays in a strict octave, independent of its branching depth. -/
theorem fan_strict_octave (s z : Nat) (hu : z%3≠0) (hz : 2≤z)
    (u v : Fin s → Bool) : fan s u z < 2*fan s v z := by
  have upper := (fan_spec s u z hu).2.2.2
  have lower := (fan_spec s v z hu).2.2.1
  have dd : 0<(3:Nat)^s := by positivity
  have zz := Nat.mul_le_mul_left (64^s) hz
  have cmp : 3^s*fan s u z < 3^s*(2*fan s v z) := by
    nlinarith only [upper,lower,zz,dd]
  exact (Nat.mul_lt_mul_left dd).mp cmp

/-- Oddification loses no fan members because dyadic multiples cannot share a strict octave. -/
theorem oddFan_injective (s z : Nat) (hs : 0<s) (hu : z%3≠0) (hz : 2≤z) :
    Function.Injective (fun w => oddFan s w z) := by
  intro a b eq
  change oddFan s a z=oddFan s b z at eq
  obtain ⟨_,pa,_,_⟩ := oddFan_spec s hs a z hu
  obtain ⟨_,pb,_,_⟩ := oddFan_spec s hs b z hu
  have pads : oddFanPadding s a z=oddFanPadding s b z := by
    by_contra ne
    rcases lt_or_gt_of_ne ne with h|h
    · have power : 2*2^(oddFanPadding s a z) ≤ 2^(oddFanPadding s b z) := by
        rw [mul_comm,← pow_succ]
        exact Nat.pow_le_pow_right (by decide) h
      have multiple := Nat.mul_le_mul_right (oddFan s a z) power
      rw [mul_assoc,pa,eq,pb] at multiple
      exact (Nat.not_le_of_lt (fan_strict_octave s z hu hz b a)) multiple
    · have power : 2*2^(oddFanPadding s b z) ≤ 2^(oddFanPadding s a z) := by
        rw [mul_comm,← pow_succ]
        exact Nat.pow_le_pow_right (by decide) h
      have multiple := Nat.mul_le_mul_right (oddFan s b z) power
      rw [mul_assoc,pb,← eq,pa] at multiple
      exact (Nat.not_le_of_lt (fan_strict_octave s z hu hz a b)) multiple
  apply fan_injective s z hu
  change fan s a z=fan s b z
  rw [← pa,← pb,pads,eq]

theorem oddFan_le_raw (s z : Nat) (hs : 0<s) (hu : z%3≠0) (w : Fin s → Bool) :
    oddFan s w z ≤ fan s w z := by
  have pad := (oddFan_spec s hs w z hu).2.1
  have power : 1≤2^(oddFanPadding s w z) := Nat.one_le_pow _ _ (by decide)
  have h := Nat.mul_le_mul_right (oddFan s w z) power
  simpa [pad] using h

theorem oddFan_upper (s z : Nat) (hs : 0<s) (hu : z%3≠0) (w : Fin s → Bool) :
    oddFan s w z < 32^s*z := by
  have upper := (fan_spec s w z hu).2.2.2
  have nz : 0<fan s w z := by have := (fan_spec s w z hu).2.1; omega
  have ps : (2:Nat)^s<3^s := Nat.pow_lt_pow_left (by decide) hs.ne'
  have lt := Nat.mul_lt_mul_of_pos_right ps nz
  have fact : (2:Nat)^s*32^s=64^s := by rw [← mul_pow]; rfl
  have bound : 2^s*fan s w z < 2^s*(32^s*z) := by
    rw [← mul_assoc,fact]
    exact lt.trans_le upper
  exact (oddFan_le_raw s z hs hu w).trans_lt ((Nat.mul_lt_mul_left (by positivity)).mp bound)

/-- Child growth is uniform once the root is at least two. -/
private theorem child_grows (b : Bool) (z : Nat) (hu : z%3≠0) (hz : 2≤z) :
    16*z ≤ child b z := by
  have choices : z%9=1 ∨ z%9=2 ∨ z%9=4 ∨ z%9=5 ∨ z%9=7 ∨ z%9=8 := by omega
  rcases choices with e|e|e|e|e|e <;> cases b <;> simp [child,e] <;> omega

theorem fan_lower (s z : Nat) (hu : z%3≠0) (hz : 2≤z) (w : Fin s → Bool) :
    16^s*z ≤ fan s w z := by
  induction s with
  | zero => simp [fan]
  | succ s ih =>
    let v := fan s (fun i => w i.castSucc) z
    have low : 16^s*z≤v := ih (fun i => w i.castSucc)
    have vz : 2≤v := by
      have one : 1≤16^s := Nat.one_le_pow _ _ (by decide)
      have mult := Nat.mul_le_mul_right z one
      omega
    have grow := child_grows (w (Fin.last s)) v (fan_spec s _ z hu).2.1 vz
    change 16^(s+1)*z ≤ child (w (Fin.last s)) v
    rw [pow_succ]
    nlinarith only [low,grow]

theorem oddFan_lower (s z : Nat) (hs : 2≤s) (hu : z%3≠0) (hz : 2≤z)
    (w : Fin s → Bool) : z≤oddFan s w z := by
  obtain ⟨pb,pad,_,_⟩ := oddFan_spec s (by omega) w z hu
  have high : 2^(oddFanPadding s w z)≤32 := by
    exact (Nat.pow_le_pow_right (by decide) pb)
  have lower := fan_lower s z hu hz w
  have min : 32≤16^s := (by decide : 32≤(16:Nat)^2).trans
    (Nat.pow_le_pow_right (by decide) hs)
  have left := Nat.mul_le_mul_right z min
  have right := Nat.mul_le_mul_right (oddFan s w z) high
  rw [pad] at right
  exact (Nat.mul_le_mul_left_iff (by decide : 0<32)).mp (left.trans (lower.trans right))

/-- The entire fan has a phase error depending on the root, not on its depth. -/
theorem oddFan_phase (s z : Nat) (hs : 0<s) (hu : z%3≠0) (hz : 2≤z)
    (w : Fin s → Bool) : ∃ e : ℝ, 0≤e ∧ e≤4/(z:ℝ) ∧
      height (oddFan s w z)=height z+((6*s-oddFanPadding s w z:Nat):ℝ)-(s:ℝ)*alpha-e := by
  let X := fan s w z
  let F : ℝ := (64:ℝ)^s*(z:ℝ)/(3:ℝ)^s
  have zp : (0:ℝ)<z := by exact_mod_cast (show 0<z by omega)
  have xp : (0:ℝ)<X := by
    have unit := (fan_spec s w z hu).2.1
    exact_mod_cast (show 0<X by dsimp [X]; omega)
  have fp : 0<F := by dsimp [F]; positivity
  have dp : (0:ℝ)<(3:ℝ)^s := by positivity
  have lower : (64:ℝ)^s*z+(3:ℝ)^s ≤ (3:ℝ)^s*X+(64:ℝ)^s := by
    exact_mod_cast (fan_spec s w z hu).2.2.1
  have upper : (3:ℝ)^s*X ≤ (64:ℝ)^s*z := by
    exact_mod_cast (fan_spec s w z hu).2.2.2
  have lo : F*(1-1/(z:ℝ))≤X := by
    have eq : F*(1-1/(z:ℝ))=((64:ℝ)^s*z-(64:ℝ)^s)/(3:ℝ)^s := by
      dsimp [F]; field_simp
    rw [eq]
    apply (div_le_iff₀ dp).mpr
    nlinarith only [lower,dp]
  have hi : (X:ℝ)≤F := (le_div_iff₀ dp).mpr (by simpa [mul_comm] using upper)
  obtain ⟨e,ep,eb,eq⟩ := Band.log_error fp (by exact_mod_cast hz) xp lo hi
  have log64 : logb 2 (64:ℝ)=6 := by
    rw [show (64:ℝ)=(2:ℝ)^6 by norm_num,logb_pow,logb_two]
    norm_num
  have lf : logb 2 F=height z+(6:ℝ)*s-(s:ℝ)*alpha := by
    dsimp [F,height,alpha]
    rw [logb_div (by positivity) (by positivity),logb_mul (by positivity) zp.ne',
      logb_pow,logb_pow,log64]
    ring
  obtain ⟨pb,pad,odd,_⟩ := oddFan_spec s hs w z hu
  have op : (0:ℝ)<oddFan s w z := by exact_mod_cast (show 0<oddFan s w z by omega)
  have realpad : (2:ℝ)^(oddFanPadding s w z)*(oddFan s w z:ℝ)=X := by exact_mod_cast pad
  have lp := congrArg (logb 2) realpad
  rw [logb_mul (by positivity) op.ne',logb_pow,logb_two,mul_one] at lp
  have ptime : oddFanPadding s w z≤6*s := by omega
  rw [lf] at eq
  refine ⟨e,ep,eb,?_⟩
  rw [Nat.cast_sub ptime,Nat.cast_mul,Nat.cast_ofNat]
  dsimp [height] at eq ⊢
  change (oddFanPadding s w z:ℝ)+logb 2 (oddFan s w z)=logb 2 (X:ℝ) at lp
  linarith

theorem sixteen_mul_le_pow_two (Q : Nat) (hQ : 8≤Q) : 16*Q≤2^Q := by
  induction Q, hQ using Nat.le_induction with
  | base => decide
  | succ Q hQ ih => rw [pow_succ]; omega

/-- A single phase-steered root produces exponentially many actual marked ancestors.
The output family retains all binary choices after removing its initial halvings. -/
theorem oddFan_marked_of_phase {Q z : Nat} (hQ : 8≤Q) (hu : z%3≠0)
    (hzlo : 2^Q≤z) (hzhi : z<2^(5*Q))
    (phase : ∃ Z : ℤ, 1/(4*(Q:ℝ))≤height z-(Q:ℝ)*alpha-Z ∧
      height z-(Q:ℝ)*alpha-Z≤7/(2*(Q:ℝ))) :
    ∀ w, Marked (oddFan Q w z) ∧ oddFan Q w z<2^(10*Q) ∧ Hits (oddFan Q w z) z := by
  have qp : 0<Q := by omega
  have qr : (0:ℝ)<Q := by exact_mod_cast qp
  have small : 16*Q≤z := (sixteen_mul_le_pow_two Q hQ).trans hzlo
  have hz : 2≤z := by omega
  have zp : (0:ℝ)<z := by exact_mod_cast (show 0<z by omega)
  have error_bound : (4:ℝ)/z≤1/(4*(Q:ℝ)) := by
    apply (div_le_div_iff₀ zp (by positivity)).mpr
    exact_mod_cast (show 4*(4*Q)≤1*z by omega)
  obtain ⟨Z,lo,hi⟩ := phase
  intro w
  have os := oddFan_spec Q qp w z hu
  have op : 0<oddFan Q w z := by have := os.2.2.1; omega
  have high : oddFan Q w z<2^(10*Q) := by
    calc _ < 32^Q*z := oddFan_upper Q z qp hu w
         _ < 32^Q*2^(5*Q) := Nat.mul_lt_mul_of_pos_left hzhi (by positivity)
         _ = 2^(10*Q) := by
           rw [show (32:Nat)=2^5 by decide,← pow_mul,← pow_add]
           congr 1
           omega
  have digits : (oddFan Q w z).log2+1≤10*Q := by
    have b := (Nat.log2_lt op.ne').mpr high
    omega
  obtain ⟨e,ep,eb,eq⟩ := oddFan_phase Q z qp hu hz w
  have ee : e≤1/(4*(Q:ℝ)) := eb.trans error_bound
  let W : ℤ := Z+(6*Q-oddFanPadding Q w z:Nat)
  have form : height (oddFan Q w z)-W=height z-Q*alpha-Z-e := by
    rw [eq]
    dsimp [W]
    push_cast
    ring
  have nonneg : 0≤height (oddFan Q w z)-W := by rw [form]; linarith
  have close : ((oddFan Q w z).log2+1:ℝ)*(height (oddFan Q w z)-W)≤35 := by
    have dl : ((oddFan Q w z).log2+1:ℝ)≤10*(Q:ℝ) := by exact_mod_cast digits
    have hi' : height (oddFan Q w z)-W≤7/(2*(Q:ℝ)) := by rw [form]; linarith
    calc _ ≤ (10*(Q:ℝ))*(height (oddFan Q w z)-W) := mul_le_mul_of_nonneg_right dl nonneg
         _ ≤ (10*(Q:ℝ))*(7/(2*(Q:ℝ))) := mul_le_mul_of_nonneg_left hi' (by positivity)
         _ = 35 := by field_simp; ring
  exact ⟨⟨os.2.2.1,section_of_phase op nonneg close⟩,high,oddFan_hit Q qp w z hu⟩

theorem marked_fan_of_phase {Q z : Nat} (hQ : 8≤Q) (hu : z%3≠0)
    (hzlo : 2^Q≤z) (hzhi : z<2^(5*Q))
    (phase : ∃ Z : ℤ, 1/(4*(Q:ℝ))≤height z-(Q:ℝ)*alpha-Z ∧
      height z-(Q:ℝ)*alpha-Z≤7/(2*(Q:ℝ))) :
    ∃ f : (Fin Q → Bool) → Nat, Function.Injective f ∧
      ∀ w, Marked (f w) ∧ f w<2^(10*Q) ∧ Hits (f w) z := by
  have hz : 2≤z := by have := (sixteen_mul_le_pow_two Q hQ).trans hzlo; omega
  exact ⟨fun w => oddFan Q w z,oddFan_injective Q z (by omega) hu hz,
    oddFan_marked_of_phase hQ hu hzlo hzhi phase⟩

#print axioms marked_fan_of_phase

end CollatzShell.ForwardSection
