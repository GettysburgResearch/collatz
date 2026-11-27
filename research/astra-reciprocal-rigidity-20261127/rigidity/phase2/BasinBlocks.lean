import FiniteTrace
import TernarySteering

/-! Qualitative ordinary Collatz synchronization on a complete binary residue class.
The signed map is used only for affine identities. Ordinary positive inputs are
recovered in the final statements. -/
namespace Collatz.ReciprocalRigidity.BasinBlocks

private def step (x : ℤ) : ℤ := if x % 2 = 0 then x/2 else (3*x+1)/2
private def run : ℕ → ℤ → ℤ
  | 0, x => x
  | h+1, x => run h (step x)

private theorem run_add (h k : ℕ) (x : ℤ) : run (h+k) x = run k (run h x) := by
  induction h generalizing x with
  | zero => simp [run]
  | succ h ih => rw [Nat.succ_add]; exact ih (step x)

private theorem step_even (u : ℤ) : step (2*u)=u := by unfold step; omega
private theorem step_odd (u : ℤ) : step (2*u+1)=3*u+2 := by unfold step; omega

private def ray (p : ℕ) (z t : ℤ) : ℤ := 3^p*t+z

private theorem ray_odd_slope (p : ℕ) : ∃ q : ℤ, 3^p=2*q+1 := by
  induction p with
  | zero => exact ⟨0, by norm_num⟩
  | succ p ih => obtain ⟨q,hq⟩ := ih; exact ⟨3*q+1, by rw [pow_succ,hq]; ring⟩

/-- Restrict the integer parameter by one bit to impose either parity on the base. -/
private theorem choose_bit (p : ℕ) (z e : ℤ) :
    ∃ b q : ℤ, ∀ t, ray p z (2*t+b)=2*ray p q t+e := by
  obtain ⟨w, hw⟩ := ray_odd_slope p
  refine ⟨e-z, w*(e-z), ?_⟩
  intro t; simp only [ray,hw]; ring

private def Sync (f g : ℤ → ℤ) : Prop :=
  ∃ h : ℕ, ∃ r : ℤ, ∃ p : ℕ, ∃ z : ℤ, ∀ t : ℤ,
    run h (f (2^h*t+r))=ray p z t ∧ run h (g (2^h*t+r))=ray p z t

private theorem sync_symm {f g : ℤ → ℤ} (h : Sync f g) : Sync g f := by
  obtain ⟨k,r,p,z,he⟩ := h
  exact ⟨k,r,p,z,fun t => (he t).symm⟩

private theorem pull_bit {f g f' g' : ℤ → ℤ} {b : ℤ}
    (hf : ∀ t, step (f (2*t+b))=f' t)
    (hg : ∀ t, step (g (2*t+b))=g' t) (h : Sync f' g') : Sync f g := by
  obtain ⟨k,r,p,z,he⟩ := h
  refine ⟨k+1, 2*r+b, p,z, ?_⟩
  intro t
  rw [show (2 : ℤ)^(k+1)*t+(2*r+b)=2*(2^k*t+r)+b by rw [pow_succ]; ring]
  simp only [run, hf,hg]
  exact he t

private def CanTie (j : ℕ) (D : ℤ) :=
  ∀ p z, Sync (ray p z) (fun t => 3^j*ray p z t+D)

private theorem tie_zero : CanTie 0 0 := by
  intro p z
  exact ⟨0,0,p,z,fun t => by simp [run]⟩

private theorem halve_even {j : ℕ} {d : ℤ} (h : CanTie j d) : CanTie j (2*d) := by
  intro p z
  obtain ⟨b,q,he⟩ := choose_bit p z 0
  refine pull_bit (b:=b) (f':=ray p q) (g':=fun t=>3^j*ray p q t+d) ?_ ?_ (h p q)
  · intro t; rw [he]; simp [step_even]
  · intro t; simp only [he,add_zero]
    rw [show (3:ℤ)^j*(2*ray p q t)+2*d=2*(3^j*ray p q t+d) by ring,step_even]

private theorem zero_to_nonzero {j : ℕ} {w : ℤ} (hw : (3:ℤ)^j=2*w+1)
    (h : CanTie j (-w)) : CanTie j 0 := by
  intro p z
  obtain ⟨b,q,he⟩ := choose_bit p z 1
  let Q := 3*q+2
  have hr (t : ℤ) : 3*ray p q t+2=ray (p+1) Q t := by
    simp only [ray,Q,pow_succ]; ring
  refine pull_bit (b:=b) (f':=ray (p+1) Q)
    (g':=fun t=>3^j*ray (p+1) Q t+(-w)) ?_ ?_ (h (p+1) Q)
  · intro t; rw [he,step_odd,hr]
  · intro t; simp only [he,add_zero,hw]
    rw [show (2*w+1)*(2*ray p q t+1)=2*((2*w+1)*ray p q t+w)+1 by ring,
      step_odd,← hr]
    ring

private theorem lower_odd {j : ℕ} {w d : ℤ} (hw : (3:ℤ)^j=2*w+1)
    (h : CanTie j (d-w)) : CanTie (j+1) (2*d+1) := by
  intro p z
  obtain ⟨b,q,he⟩ := choose_bit p z 1
  let Q := 3*q+2
  have hr (t : ℤ) : 3*ray p q t+2=ray (p+1) Q t := by simp only [ray,Q,pow_succ]; ring
  refine pull_bit (b:=b) (f':=ray (p+1) Q)
    (g':=fun t=>3^j*ray (p+1) Q t+(d-w)) ?_ ?_ (h (p+1) Q)
  · intro t; rw [he,step_odd,hr]
  · intro t; simp only [he,pow_succ,hw]
    rw [show (2*w+1)*3*(2*ray p q t+1)+(2*d+1)=
      2*((2*w+1)*(3*ray p q t+2)+(d-w)) by ring, step_even,← hr]

private theorem raise_even_base {d : ℤ} (h : CanTie 1 (3*d+2)) :
    CanTie 0 (2*d+1) := by
  intro p z
  obtain ⟨b,q,he⟩ := choose_bit p z 0
  refine pull_bit (b:=b) (f':=ray p q) (g':=fun t=>3^1*ray p q t+(3*d+2))
    ?_ ?_ (h p q)
  · intro t; rw [he]; simp [step_even]
  · intro t; simp only [he,add_zero,pow_zero,one_mul,pow_one]
    rw [show 2*ray p q t+(2*d+1)=2*(ray p q t+d)+1 by ring,step_odd]; ring

private theorem raise_odd_base {d : ℤ} (h : CanTie 1 (-3*d-1)) :
    CanTie 0 (2*d+1) := by
  intro p z
  obtain ⟨b,q,he⟩ := choose_bit p z 1
  let Q := q+d+1
  have hr (t : ℤ) : ray p Q t=ray p q t+d+1 := by simp only [Q,ray]; ring
  apply sync_symm
  refine pull_bit (b:=b) (f':=ray p Q) (g':=fun t=>3^1*ray p Q t+(-3*d-1))
    ?_ ?_ (h p Q)
  · intro t; simp only [he,pow_zero,one_mul]
    rw [show 2*ray p q t+1+(2*d+1)=2*(ray p q t+d+1) by ring,step_even,hr]
  · intro t; rw [he,step_odd,hr]; simp only [pow_one]; ring


/-- At fixed level, a nonzero offset may have all its factors of 2 removed. -/
private theorem odd_part (j : ℕ) (D : ℤ) (hD : D≠0) :
    ∃ d : ℤ, (2*d+1).natAbs ≤ D.natAbs ∧
      (CanTie j (2*d+1) → CanTie j D) := by
  generalize hn : D.natAbs=n
  induction n using Nat.strong_induction_on generalizing D with
  | h n ih =>
    by_cases even : D%2=0
    · let u := D/2
      have hu : D=2*u := by dsimp [u]; omega
      have hu0 : u≠0 := by intro h; rw [hu,h] at hD; simp at hD
      have hab : D.natAbs=2*u.natAbs := by rw [hu,Int.natAbs_mul]; rfl
      obtain ⟨d,hb,ht⟩ := ih u.natAbs (by have := Int.natAbs_pos.mpr hu0; omega) u hu0 rfl
      exact ⟨d,by omega, fun h => hu ▸ halve_even (ht h)⟩
    · let d := D/2
      have he : D=2*d+1 := by dsimp [d]; omega
      exact ⟨d,by rw [← he,hn],fun h=>he ▸ h⟩

private theorem small_offset (D d u e : ℤ) (hD : D=2*d+1)
    (he : 2*u=3*d+2 ∨ 2*u= -3*d-1)
    (hbound : (2*e+1).natAbs≤u.natAbs) (hlarge : 1<D.natAbs) :
    e.natAbs<D.natAbs := by
  have de := Int.natAbs_eq D
  have eu := Int.natAbs_eq u
  have ee := Int.natAbs_eq e
  have es := Int.natAbs_eq (2*e+1)
  rcases he with he|he <;> omega

private theorem bottom_tie (D : ℤ) : CanTie 0 D := by
  generalize hn : D.natAbs=n
  induction n using Nat.strong_induction_on generalizing D with
  | h n ih =>
    by_cases hz : D=0
    · rw [hz]; exact tie_zero
    by_cases even : D%2=0
    · let d := D/2
      have he : D=2*d := by dsimp [d]; omega
      have hd : d≠0 := by intro h; rw [he,h] at hz; simp at hz
      have hdabs : D.natAbs=2*d.natAbs := by rw [he,Int.natAbs_mul]; rfl
      rw [he]
      exact halve_even (ih d.natAbs (by have := Int.natAbs_pos.mpr hd; omega) d rfl)
    let d := D/2
    have he : D=2*d+1 := by dsimp [d]; omega
    have h1 : CanTie 1 1 := by
      have h := lower_odd (j:=0) (d:=0) (w:=0) (by norm_num) (by simpa using tie_zero)
      simpa using h
    have h2 : CanTie 1 2 := by simpa using halve_even h1
    by_cases hsmall : D.natAbs≤1
    · have hs : D=1 ∨ D= -1 := by have := Int.natAbs_eq D; omega
      rcases hs with hs|hs
      · rw [hs]; simpa using raise_even_base (d:=0) (by simpa using h2)
      · rw [hs]; simpa using raise_odd_base (d:= -1) (by simpa using h2)
    have hreduce (E u : ℤ) (hE : E=2*u) (h0 : u≠0)
        (hchoice : E=3*d+2 ∨ E= -3*d-1) : CanTie 1 E := by
      obtain ⟨v,hb,ht⟩ := odd_part 1 u h0
      have hv := small_offset D d u v he (hE ▸ hchoice) hb (by omega)
      have hlow := lower_odd (j:=0) (w:=0) (d:=v) (by norm_num)
        (by simpa using ih v.natAbs (by omega) v rfl)
      exact hE ▸ halve_even (ht hlow)
    rw [he]
    by_cases hc : (3*d+2)%2=0
    · apply raise_even_base
      exact hreduce (3*d+2) ((3*d+2)/2) (by omega) (by omega) (Or.inl rfl)
    · apply raise_odd_base
      exact hreduce (-3*d-1) ((-3*d-1)/2) (by omega) (by omega) (Or.inr rfl)

private theorem all_levels_tie (j : ℕ) (D : ℤ) : CanTie j D := by
  induction j generalizing D with
  | zero => exact bottom_tie D
  | succ j ih =>
    obtain ⟨w,hw⟩ := ray_odd_slope j
    have h_nonzero (d : ℤ) (hd : d≠0) : CanTie (j+1) d := by
      obtain ⟨e,_,he⟩ := odd_part (j+1) d hd
      exact he (lower_odd hw (ih (e-w)))
    by_cases hD : D=0
    · rw [hD]
      obtain ⟨w',hw'⟩ := ray_odd_slope (j+1)
      have h3 : (3 : ℤ)^j>0 := by positivity
      have hw0 : -w'≠0 := by rw [pow_succ] at hw'; omega
      exact zero_to_nonzero hw' (h_nonzero (-w') hw0)
    · exact h_nonzero D hD


private theorem tie_rays_le {p q : ℕ} (hp : p≤q) (z y : ℤ) :
    Sync (ray p z) (ray q y) := by
  have he : ray q y = fun t => 3^(q-p)*ray p z t+(y-3^(q-p)*z) := by
    funext t; simp only [ray]
    nth_rw 1 [show q=q-p+p by omega]
    rw [pow_add];ring
  rw [he]
  exact all_levels_tie (q-p) (y-3^(q-p)*z) p z

private theorem tie_rays (p q : ℕ) (z y : ℤ) : Sync (ray p z) (ray q y) := by
  rcases le_total p q with h|h
  · exact tie_rays_le h z y
  · exact sync_symm (tie_rays_le h y z)

private theorem affine_form (h : ℕ) (r : ℤ) :
    ∃ p : ℕ, ∃ z : ℤ, ∀ t, run h (2^h*t+r) = ray p z t := by
  induction h generalizing r with
  | zero => exact ⟨0,r,fun t=>by simp [run,ray]⟩
  | succ h ih =>
    let d:=r/2
    by_cases hr : r%2=0
    · have he : r=2*d := by dsimp [d];omega
      obtain ⟨p,z,hf⟩ := ih d
      refine ⟨p,z,fun t=>?_⟩
      rw [show (2:ℤ)^(h+1)*t+r=2*(2^h*t+d) by rw [pow_succ,he];ring,
        run,step_even,hf]
    · have he : r=2*d+1 := by dsimp [d];omega
      obtain ⟨p,z,hf⟩ := ih (3*d+2)
      refine ⟨p+1,z,fun t=>?_⟩
      rw [show (2:ℤ)^(h+1)*t+r=2*(2^h*t+d)+1 by rw [pow_succ,he];ring,
        run,step_odd,show 3*(2^h*t+d)+2=2^h*(3*t)+(3*d+2) by ring,hf]
      simp only [ray,pow_succ];ring

private theorem synchronized_class (m : ℕ) :
    ∃ h : ℕ, ∃ r : ℤ, ∃ p : ℕ, ∃ z : ℤ, ∀ i : ℕ, i<m →
      ∀ t : ℤ, run h (2^h*t+r+i) = ray p z t := by
  induction m with
  | zero => exact ⟨0,0,0,0,fun i hi=>by omega⟩
  | succ m ih =>
    obtain ⟨h,r,p,z,hb⟩:=ih
    obtain ⟨q,y,he⟩:=affine_form h (r+(m:ℤ))
    obtain ⟨k,v,P,Z,hpair⟩:=tie_rays p q z y
    refine ⟨h+k,2^h*v+r,P,Z,?_⟩
    intro i hi t
    rw [show (2:ℤ)^(h+k)*t+(2^h*v+r)+i=2^h*(2^k*t+v)+r+i by rw [pow_add];ring,run_add]
    by_cases hlt : i<m
    · rw [hb i hlt];exact (hpair t).1
    · have hEq : i=m := by omega
      rw [hEq,add_assoc,he];exact (hpair t).2

private theorem signed_step_nat (n : ℕ) : step (n:ℤ)=(FiniteTrace.step n:ℤ) := by
  unfold step FiniteTrace.step
  split_ifs <;> omega

private theorem signed_run_nat (h n : ℕ) : run h (n:ℤ)=(FiniteTrace.orbit h n:ℤ) := by
  induction h generalizing n with
  | zero => rfl
  | succ h ih => rw [run,signed_step_nat,ih,FiniteTrace.orbit]

private theorem half_run (k : ℕ) (v : ℤ) : run k (2^k*v)=v := by
  induction k with
  | zero => simp [run]
  | succ k ih => rw [pow_succ',mul_assoc,run,step_even,ih]

private theorem terminal (k : ℕ) (y v : ℤ) (h : 3*y+1=2^(k+1)*v) :
    run (k+1) y=v := by
  have he : 3*y+1=2*(2^k*v) := by rw [h,pow_succ'];ring
  have hy : y%2≠0 := by omega
  have hs : step y=2^k*v := by simp [step,hy,he]
  rw [run,hs,half_run]


/-- For every width and arbitrarily high floor, there is a consecutive block of
ordinary positive integers simultaneously reaching any target prime to 3.
All entries reach it at the very same shortcut date. -/
theorem arbitrarily_high_common_target_blocks (m v floor : ℕ) (hv : v%3≠0) :
    ∃ n : ℕ, floor≤n ∧ 0<n ∧ ∃ k : ℕ, ∀ i : ℕ, i<m →
      FiniteTrace.orbit k (n+i)=v := by
  obtain ⟨h,r,p,z,hblock⟩ := synchronized_class m
  let K : ℤ := floor+r.natAbs+1
  let B : ℤ := 3*z+1+3^(p+1)*K
  obtain ⟨e,hle,c,hE⟩ := TernarySteering.power_steering p (B.natAbs+1) v z hv
  have hv' : (1:ℤ)≤v := by omega
  have hexp : ∀ i : ℕ, (i:ℤ)<(2:ℤ)^i := by
    intro i;induction i with
    | zero => norm_num
    | succ i ih => rw [pow_succ,Nat.cast_succ];omega
  have hBe : B<(2:ℤ)^e*v := by
    have hB : B≤(B.natAbs:ℤ) := by have := Int.natAbs_eq B; omega
    have hpow : (2:ℤ)^e≤2^e*v := by
      simpa only [mul_one] using mul_le_mul_of_nonneg_left hv' (by positivity : 0≤(2:ℤ)^e)
    have := hexp e;omega
  have hk : K<c := by
    by_contra! hn
    have hm := mul_le_mul_of_nonneg_left hn (by positivity : 0≤(3:ℤ)^(p+1))
    dsimp [B] at hBe;omega
  have hK : 0≤c := by dsimp [K] at hk;omega
  have hs : (1:ℤ)≤2^h := by
    have hh : (0:ℤ)<2^h := by positivity
    omega
  have hsc := mul_le_mul_of_nonneg_right hs hK
  simp only [one_mul] at hsc
  let x : ℤ := 2^h*c+r
  have hx : (floor:ℤ)<x := by
    have hr := Int.natAbs_eq r
    dsimp [K] at hk;dsimp [x];omega
  let n := x.toNat
  have hncast : (n:ℤ)=x := Int.toNat_of_nonneg (by omega)
  have hterminal : run e (ray p z c) = (v:ℤ) := by
    cases e with
    | zero => omega
    | succ j =>
      apply terminal
      rw [hE];simp only [ray,pow_succ];ring
  refine ⟨n,by omega,by omega,h+e,?_⟩
  intro i hi
  have he : (FiniteTrace.orbit (h+e) (n+i):ℤ)=(v:ℤ) := by
    rw [← signed_run_nat,Nat.cast_add,hncast,run_add]
    change run e (run h ((2:ℤ)^h*c+r+i))=(v:ℤ)
    rw [hblock i hi c,hterminal]
  exact_mod_cast he

#print axioms arbitrarily_high_common_target_blocks

end Collatz.ReciprocalRigidity.BasinBlocks
