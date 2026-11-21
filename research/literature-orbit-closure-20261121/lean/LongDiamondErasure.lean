module

public import HalfSourceMerge

@[expose] public section

/-!
# Long endpoint diamonds erase two or three initial odd steps

The eight-clock affine identity was found independently by the symbolic and
rewriting searches; its Lean proof is adapted from literature_rewriting/WildLift.lean.
The new source bounds follow by composing short--long--short endpoint diamonds
and applying the generic ordinary-source erasure theorem.
-/

namespace CollatzShell

theorem endpoint_diamond_eight_affine (v : Nat) :
    orbit 8 (256 * v + 184) = 27 * v + 20 ∧
    orbit 8 (3 * (256 * v + 184) + 2) = 27 * v + 20 := by
  have he (x : Nat) (h : x % 2 = 0) : step x = x / 2 := by simp [step, h]
  have ho (x : Nat) (h : x % 2 ≠ 0) : step x = (3*x+1)/2 := by simp [step, h]
  constructor
  · have e0 : step (256*v+184) = 128*v+92 := by rw [he _ (by omega)]; omega
    have e1 : step (128*v+92) = 64*v+46 := by rw [he _ (by omega)]; omega
    have e2 : step (64*v+46) = 32*v+23 := by rw [he _ (by omega)]; omega
    have e3 : step (32*v+23) = 48*v+35 := by rw [ho _ (by omega)]; omega
    have e4 : step (48*v+35) = 72*v+53 := by rw [ho _ (by omega)]; omega
    have e5 : step (72*v+53) = 108*v+80 := by rw [ho _ (by omega)]; omega
    have e6 : step (108*v+80) = 54*v+40 := by rw [he _ (by omega)]; omega
    have e7 : step (54*v+40) = 27*v+20 := by rw [he _ (by omega)]; omega
    simp only [orbit, e0, e1, e2, e3, e4, e5, e6, e7]
  · have h0 : 3 * (256*v+184)+2 = 768*v+554 := by omega
    have e0 : step (768*v+554) = 384*v+277 := by rw [he _ (by omega)]; omega
    have e1 : step (384*v+277) = 576*v+416 := by rw [ho _ (by omega)]; omega
    have e2 : step (576*v+416) = 288*v+208 := by rw [he _ (by omega)]; omega
    have e3 : step (288*v+208) = 144*v+104 := by rw [he _ (by omega)]; omega
    have e4 : step (144*v+104) = 72*v+52 := by rw [he _ (by omega)]; omega
    have e5 : step (72*v+52) = 36*v+26 := by rw [he _ (by omega)]; omega
    have e6 : step (36*v+26) = 18*v+13 := by rw [he _ (by omega)]; omega
    have e7 : step (18*v+13) = 27*v+20 := by rw [ho _ (by omega)]; omega
    simp only [h0, orbit, e0, e1, e2, e3, e4, e5, e6, e7]

theorem endpoint_diamond_eight (v : Nat) (phase : v%256=185) :
    orbit 8 (v-1)=orbit 8 (3*v-1) := by
  have decomp : v=256*(v/256)+185 := by omega
  have left : v-1=256*(v/256)+184 := by omega
  have right : 3*v-1=3*(256*(v/256)+184)+2 := by omega
  rw [left,right]
  exact (endpoint_diamond_eight_affine (v/256)).1.trans
    (endpoint_diamond_eight_affine (v/256)).2.symm

private theorem pad_short_diamond (v : Nat) (phase : v%4=3) :
    orbit 8 (v-1)=orbit 8 (3*v-1) := by
  have eq := half_source_two_clock_diamond v phase
  change orbit (2+6) (v-1)=orbit (2+6) (3*v-1)
  rw [orbit_add,orbit_add,eq]

/-- Four ordinary endpoints coalesce at clock eight. -/
theorem endpoint_diamond_chain (v : Nat) (phase : v%256=147) :
    orbit 8 (v-1)=orbit 8 (3*v-1) ∧
    orbit 8 (v-1)=orbit 8 (9*v-1) ∧
    orbit 8 (v-1)=orbit 8 (27*v-1) := by
  have short1 := pad_short_diamond v (by omega : v%4=3)
  have long := endpoint_diamond_eight (3*v) (by omega : (3*v)%256=185)
  have short2 := pad_short_diamond (9*v) (by omega : (9*v)%4=3)
  have eq9 : 3*(3*v)=9*v := by omega
  have eq27 : 3*(9*v)=27*v := by omega
  rw [eq9] at long
  rw [eq27] at short2
  exact ⟨short1,short1.trans long,(short1.trans long).trans short2⟩

/-- The long-diamond residue family has a quarter-source partner. -/
theorem rising_quarter_source_partner (k u : Nat) (hk : 3≤k) (hu : 0<u)
    (phase : (3^(k-2)*u)%256=147) :
    let n := 2^k*u-1
    let x := 2^(k-2)*u-1
    0<x ∧ 4*x+3=n ∧ x<n ∧ orbit (k+6) x=orbit (k+8) n := by
  have diamond := (endpoint_diamond_chain (3^(k-2)*u) phase).2.1
  have d : orbit 8 (3^(k-2)*u-1)=
      orbit 8 (3^2*(3^(k-2)*u)-1) := by norm_num only [Nat.reducePow]; exact diamond
  obtain ⟨xp,scale,lower,merge⟩ :=
    rising_erase_prefix k 2 8 u (by decide) (by omega) hu d
  dsimp only at *
  norm_num only [Nat.reducePow] at scale
  refine ⟨xp,by omega,lower,?_⟩
  simpa only [show k-2+8=k+6 by omega] using merge

/-- The short--long--short residue family has an eighth-source partner. -/
theorem rising_eighth_source_partner (k u : Nat) (hk : 4≤k) (hu : 0<u)
    (phase : (3^(k-3)*u)%256=147) :
    let n := 2^k*u-1
    let x := 2^(k-3)*u-1
    0<x ∧ 8*x+7=n ∧ x<n ∧ orbit (k+5) x=orbit (k+8) n := by
  have diamond := (endpoint_diamond_chain (3^(k-3)*u) phase).2.2
  have d : orbit 8 (3^(k-3)*u-1)=
      orbit 8 (3^3*(3^(k-3)*u)-1) := by norm_num only [Nat.reducePow]; exact diamond
  obtain ⟨xp,scale,lower,merge⟩ :=
    rising_erase_prefix k 3 8 u (by decide) (by omega) hu d
  dsimp only at *
  norm_num only [Nat.reducePow] at scale
  refine ⟨xp,by omega,lower,?_⟩
  simpa only [show k-3+8=k+5 by omega] using merge

#print axioms endpoint_diamond_eight_affine
#print axioms endpoint_diamond_eight
#print axioms endpoint_diamond_chain
#print axioms rising_quarter_source_partner
#print axioms rising_eighth_source_partner

end CollatzShell
