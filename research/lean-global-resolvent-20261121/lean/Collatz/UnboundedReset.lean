import Collatz.TerminalFive

/-!
An unbounded ordinary reset with a variable all-odd middle segment.
The arithmetic guard is explicit; no complete normalized-unit coverage is claimed.
-/

open CollatzReverseBasin CollatzClosure CollatzTerminalFive

set_option autoImplicit false
set_option maxHeartbeats 4000000
set_option linter.unusedSimpArgs false

namespace CollatzUnboundedReset

theorem shortcut_two_mul_pred {a : Nat} (ha : 0 < a) :
    shortcut (2*a-1) = 3*a-1 := by
  unfold shortcut
  split <;> omega

theorem pow_two_le_three (r : Nat) : 2^r ≤ 3^r := by
  induction r with
  | zero => decide
  | succ r ih => simp only [Nat.pow_succ]; omega

theorem odd_run (r v : Nat) (hv : 0 < v) :
    orbit (2^r*v-1) r = 3^r*v-1 := by
  induction r generalizing v with
  | zero => simp [orbit]
  | succ r ih =>
    have hp : 0 < 2^r*v := Nat.mul_pos (Nat.pow_pos (by omega)) hv
    have hstart : 2^(r+1)*v-1 = 2*(2^r*v)-1 := by simp [Nat.pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
    have hstep : shortcut (2^(r+1)*v-1) = 2^r*(3*v)-1 := by
      rw [hstart, shortcut_two_mul_pred hp]
      congr 1
      simp [Nat.pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
    rw [← orbit_step, hstep, ih (3*v) (by omega)]
    congr 1
    simp [Nat.pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]

theorem odd_run_bound (r v : Nat) (hv : 0 < v) (j : Nat) (hj : j ≤ r) :
    orbit (2^r*v-1) j ≤ 3^r*v-1 := by
  induction r generalizing v j with
  | zero =>
    have h : j = 0 := by omega
    subst j
    simp [orbit]
  | succ r ih =>
    cases j with
    | zero =>
      have h := Nat.mul_le_mul_right v (pow_two_le_three (r+1))
      simpa [orbit] using Nat.sub_le_sub_right h 1
    | succ j =>
      have hp : 0 < 2^r*v := Nat.mul_pos (Nat.pow_pos (by omega)) hv
      have hstart : 2^(r+1)*v-1 = 2*(2^r*v)-1 := by simp [Nat.pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
      have hstep : shortcut (2^(r+1)*v-1) = 2^r*(3*v)-1 := by
        rw [hstart, shortcut_two_mul_pred hp]
        congr 1
        simp [Nat.pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
      rw [← orbit_step, hstep]
      have h := ih (3*v) (by omega) j (by omega)
      have he : 3^r*(3*v)-1 = 3^(r+1)*v-1 := by simp [Nat.pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
      rwa [he] at h

theorem middle_preserves_offset (r w : Nat) (hw : 0 < w) :
    orbit (2^(r+1)*w-1) r = 2*3^r*w-1 ∧
    orbit (2^(r+3)*w-1) r = 8*3^r*w-1 := by
  have h1 := odd_run r (2*w) (by omega)
  have h2 := odd_run r (8*w) (by omega)
  have e1 : 2^r*(2*w) = 2^(r+1)*w := by simp [Nat.pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
  have e2 : 2^r*(8*w) = 2^(r+3)*w := by simp [Nat.pow_add, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
  constructor
  · rw [e1] at h1
    simpa [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using h1
  · rw [e2] at h2
    simpa [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using h2


theorem entry_parameter {m v : Nat} (h : 2187*m+11959 = 16384*v) :
    ∃ t : Nat, m = 16384*t+13307 ∧ v = 2187*t+1777 := by
  have hb : 16384*(1064*m+5819)+m = 16384*(7971*v)+13307 := by omega
  have hm : m % 16384 = 13307 := by
    have hh := congrArg (fun n : Nat => n % 16384) hb
    simpa [Nat.add_mod, Nat.mul_mod] using hh
  refine ⟨m / 16384, ?_, ?_⟩ <;> omega


theorem entry_source_profile (t : Nat) :
    orbit (16384*t+13307) 0 = 16384*t+13307 ∧
    orbit (16384*t+13307) 1 = 24576*t+19961 ∧
    orbit (16384*t+13307) 2 = 36864*t+29942 ∧
    orbit (16384*t+13307) 3 = 18432*t+14971 ∧
    orbit (16384*t+13307) 4 = 27648*t+22457 ∧
    orbit (16384*t+13307) 5 = 41472*t+33686 ∧
    orbit (16384*t+13307) 6 = 20736*t+16843 ∧
    orbit (16384*t+13307) 7 = 31104*t+25265 ∧
    orbit (16384*t+13307) 8 = 46656*t+37898 ∧
    orbit (16384*t+13307) 9 = 23328*t+18949 ∧
    orbit (16384*t+13307) 10 = 34992*t+28424 ∧
    orbit (16384*t+13307) 11 = 17496*t+14212 ∧
    orbit (16384*t+13307) 12 = 8748*t+7106 ∧
    orbit (16384*t+13307) 13 = 4374*t+3553 := by
  have h0 : shortcut (16384*t+13307) = 24576*t+19961 := by unfold shortcut; split <;> omega
  have h1 : shortcut (24576*t+19961) = 36864*t+29942 := by unfold shortcut; split <;> omega
  have h2 : shortcut (36864*t+29942) = 18432*t+14971 := by unfold shortcut; split <;> omega
  have h3 : shortcut (18432*t+14971) = 27648*t+22457 := by unfold shortcut; split <;> omega
  have h4 : shortcut (27648*t+22457) = 41472*t+33686 := by unfold shortcut; split <;> omega
  have h5 : shortcut (41472*t+33686) = 20736*t+16843 := by unfold shortcut; split <;> omega
  have h6 : shortcut (20736*t+16843) = 31104*t+25265 := by unfold shortcut; split <;> omega
  have h7 : shortcut (31104*t+25265) = 46656*t+37898 := by unfold shortcut; split <;> omega
  have h8 : shortcut (46656*t+37898) = 23328*t+18949 := by unfold shortcut; split <;> omega
  have h9 : shortcut (23328*t+18949) = 34992*t+28424 := by unfold shortcut; split <;> omega
  have h10 : shortcut (34992*t+28424) = 17496*t+14212 := by unfold shortcut; split <;> omega
  have h11 : shortcut (17496*t+14212) = 8748*t+7106 := by unfold shortcut; split <;> omega
  have h12 : shortcut (8748*t+7106) = 4374*t+3553 := by unfold shortcut; split <;> omega
  simp only [orbit, h0, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12,
    and_self]

theorem entry_source {m v : Nat} (h : 2187*m+11959 = 16384*v) :
    orbit m 13 = 2*v-1 := by
  obtain ⟨t, hm, hv⟩ := entry_parameter h
  rw [hm, hv]
  obtain ⟨_, _, _, _, _, _, _, _, _, _, _, _, _, he⟩ := entry_source_profile t
  omega

theorem entry_source_bound {m v : Nat} (h : 2187*m+11959 = 16384*v)
    (j : Nat) (hj : j < 13) : 3*orbit m j+34 ≤ 64*v := by
  obtain ⟨t, hm, hv⟩ := entry_parameter h
  rw [hm, hv]
  obtain ⟨h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,_⟩ := entry_source_profile t
  have hc : j=0 ∨ j=1 ∨ j=2 ∨ j=3 ∨ j=4 ∨ j=5 ∨ j=6 ∨
      j=7 ∨ j=8 ∨ j=9 ∨ j=10 ∨ j=11 ∨ j=12 := by omega
  rcases hc with h | h | h | h | h | h | h | h | h | h | h | h | h <;>
    subst j <;> omega

theorem entry_target {m v : Nat} (h : 2187*m+11959 = 16384*v) :
    orbit (2*m-1) 12 = 8*v-1 := by
  obtain ⟨t, hm, hv⟩ := entry_parameter h
  rw [hm, hv]
  have hstart : 2*(16384*t+13307)-1 = 32768*t+26613 := by omega
  have h0 : shortcut (32768*t+26613) = 49152*t+39920 := by unfold shortcut; split <;> omega
  have h1 : shortcut (49152*t+39920) = 24576*t+19960 := by unfold shortcut; split <;> omega
  have h2 : shortcut (24576*t+19960) = 12288*t+9980 := by unfold shortcut; split <;> omega
  have h3 : shortcut (12288*t+9980) = 6144*t+4990 := by unfold shortcut; split <;> omega
  have h4 : shortcut (6144*t+4990) = 3072*t+2495 := by unfold shortcut; split <;> omega
  have h5 : shortcut (3072*t+2495) = 4608*t+3743 := by unfold shortcut; split <;> omega
  have h6 : shortcut (4608*t+3743) = 6912*t+5615 := by unfold shortcut; split <;> omega
  have h7 : shortcut (6912*t+5615) = 10368*t+8423 := by unfold shortcut; split <;> omega
  have h8 : shortcut (10368*t+8423) = 15552*t+12635 := by unfold shortcut; split <;> omega
  have h9 : shortcut (15552*t+12635) = 23328*t+18953 := by unfold shortcut; split <;> omega
  have h10 : shortcut (23328*t+18953) = 34992*t+28430 := by unfold shortcut; split <;> omega
  have h11 : shortcut (34992*t+28430) = 17496*t+14215 := by unfold shortcut; split <;> omega
  rw [hstart]
  simp only [orbit, h0, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11]
  omega


theorem tail_parameter {A P : Nat} (h : 2*P = 27*A+1) (hp : P % 4 = 0) :
    ∃ b : Nat, A = 8*b+5 ∧ P = 108*b+68 := by
  refine ⟨A / 8, ?_, ?_⟩ <;> omega

theorem source_tail_profile (b : Nat) :
    orbit (16*b+9) 0 = 16*b+9 ∧
    orbit (16*b+9) 1 = 24*b+14 ∧
    orbit (16*b+9) 2 = 12*b+7 ∧
    orbit (16*b+9) 3 = 18*b+11 ∧
    orbit (16*b+9) 4 = 27*b+17 := by
  have h0 : shortcut (16*b+9) = 24*b+14 := by unfold shortcut; split <;> omega
  have h1 : shortcut (24*b+14) = 12*b+7 := by unfold shortcut; split <;> omega
  have h2 : shortcut (12*b+7) = 18*b+11 := by unfold shortcut; split <;> omega
  have h3 : shortcut (18*b+11) = 27*b+17 := by unfold shortcut; split <;> omega
  simp only [orbit, h0, h1, h2, h3, and_self]

theorem source_tail {A P : Nat} (h : 2*P = 27*A+1) (hp : P % 4 = 0) :
    orbit (2*A-1) 4 = P/4 := by
  obtain ⟨b, hA, hP⟩ := tail_parameter h hp
  rw [hA, hP, show 2*(8*b+5)-1=16*b+9 by omega]
  obtain ⟨_,_,_,_,he⟩ := source_tail_profile b
  omega

theorem source_tail_bound {A P : Nat} (h : 2*P = 27*A+1) (hp : P % 4 = 0)
    (j : Nat) (hj : j ≤ 4) : orbit (2*A-1) j < P/2 := by
  obtain ⟨b, hA, hP⟩ := tail_parameter h hp
  rw [hA, hP, show 2*(8*b+5)-1=16*b+9 by omega]
  obtain ⟨h0,h1,h2,h3,h4⟩ := source_tail_profile b
  have hc : j=0 ∨ j=1 ∨ j=2 ∨ j=3 ∨ j=4 := by omega
  rcases hc with h | h | h | h | h <;> subst j <;> omega

theorem target_tail {A P : Nat} (h : 2*P = 27*A+1) (hp : P % 4 = 0) :
    orbit (8*A-1) 4 = P-1 := by
  obtain ⟨b, hA, hP⟩ := tail_parameter h hp
  rw [hA, hP, show 8*(8*b+5)-1=64*b+39 by omega]
  have h0 : shortcut (64*b+39) = 96*b+59 := by unfold shortcut; split <;> omega
  have h1 : shortcut (96*b+59) = 144*b+89 := by unfold shortcut; split <;> omega
  have h2 : shortcut (144*b+89) = 216*b+134 := by unfold shortcut; split <;> omega
  have h3 : shortcut (216*b+134) = 108*b+67 := by unfold shortcut; split <;> omega
  simp only [orbit, h0, h1, h2, h3]
  omega

theorem entry_power_bound (l : Nat) (hl : 3 ≤ l) :
    256*2^l ≤ 81*3^l := by
  have aux : ∀ r : Nat, 256*2^(3+r) ≤ 81*3^(3+r) := by
    intro r
    induction r with
    | zero => decide
    | succ r ih =>
      rw [show 3+(r+1)=(3+r)+1 by omega]
      simp only [Nat.pow_succ]
      omega
  obtain ⟨r, hr⟩ := Nat.exists_eq_add_of_le hl
  rw [hr]
  exact aux r


/-- All arithmetic guards for the unbounded grammar are ordinary equations. -/
structure Guard (l P w m : Nat) : Prop where
  depth : 3 ≤ l
  source_scale : 0 < w
  endpoint_pos : 0 < P
  endpoint_four : P % 4 = 0
  endpoint_eq : 2*P-1 = 3^(l+3)*w
  entry_eq : 2187*m+11959 = 2^(l+14)*w

theorem guard_equations {l P w m : Nat} (h : Guard l P w m) :
    2187*m+11959 = 16384*(2^l*w) ∧
    2*P = 27*(3^l*w)+1 := by
  have he : 2^(l+14)*w = 16384*(2^l*w) := by
    simp [Nat.pow_add]
    simp [Nat.pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
  have hp : 3^(l+3)*w = 27*(3^l*w) := by
    simp [Nat.pow_add]
    simp [Nat.pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
  constructor
  · have hh := h.entry_eq
    rwa [he] at hh
  · have hh := h.endpoint_eq
    rw [hp] at hh
    have hpos := h.endpoint_pos
    omega


theorem source_path {l P w m : Nat} (h : Guard l P w m) :
    orbit m (l+17) = P/4 := by
  obtain ⟨he, hp⟩ := guard_equations h
  have hin := entry_source he
  have hmid := odd_run l (2*w) (by have hw := h.source_scale; omega)
  have ee : 2*(2^l*w)-1 = 2^l*(2*w)-1 := by simp [Nat.pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
  have eo : 3^l*(2*w)-1 = 2*(3^l*w)-1 := by simp [Nat.pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
  have ht := source_tail hp h.endpoint_four
  rw [show l+17 = 13+(l+4) by omega, orbit_add, hin, ee,
    orbit_add, hmid, eo, ht]


theorem target_path {l P w m : Nat} (h : Guard l P w m) :
    orbit (2*m-1) (l+16) = P-1 := by
  obtain ⟨he, hp⟩ := guard_equations h
  have hin := entry_target he
  have hmid := odd_run l (8*w) (by have hw := h.source_scale; omega)
  have ee : 8*(2^l*w)-1 = 2^l*(8*w)-1 := by simp [Nat.pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
  have eo : 3^l*(8*w)-1 = 8*(3^l*w)-1 := by simp [Nat.pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
  have ht := target_tail hp h.endpoint_four
  rw [show l+16 = 12+(l+4) by omega, orbit_add, hin, ee,
    orbit_add, hmid, eo, ht]


/-- Every inserted source state, including the endpoint if desired, is below
    the removed parent state P/2.  This is uniform in the unbounded l. -/
theorem source_prefix_below {l P w m : Nat} (h : Guard l P w m)
    (j : Nat) (hj : j ≤ l+17) : orbit m j < P/2 := by
  obtain ⟨he, hp⟩ := guard_equations h
  have hin := entry_source he
  have hw := h.source_scale
  have hdom : 256*(2^l*w) ≤ 81*(3^l*w) := by
    simpa [Nat.mul_assoc] using Nat.mul_le_mul_right w (entry_power_bound l h.depth)
  by_cases hentry : j < 13
  · have hb := entry_source_bound he j hentry
    have hp4 := h.endpoint_four
    omega
  · have hfirst : 13+(j-13)=j := by omega
    rw [← hfirst, orbit_add, hin]
    have ee : 2*(2^l*w)-1 = 2^l*(2*w)-1 := by simp [Nat.pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
    rw [ee]
    by_cases hloop : j-13 ≤ l
    · have hb := odd_run_bound l (2*w) (by omega) (j-13) hloop
      have eo : 3^l*(2*w)-1 = 2*(3^l*w)-1 := by simp [Nat.pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
      rw [eo] at hb
      have hp4 := h.endpoint_four
      omega
    · have hsplit : j-13 = l+(j-13-l) := by omega
      rw [hsplit, orbit_add, odd_run l (2*w) (by omega)]
      have eo : 3^l*(2*w)-1 = 2*(3^l*w)-1 := by simp [Nat.pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
      rw [eo]
      exact source_tail_bound hp h.endpoint_four (j-13-l) (by omega)


theorem source_basin_transfer {l P w m : Nat} (h : Guard l P w m) :
    Basin m ↔ Basin (P/2) := by
  have he := source_path h
  have hhalf : shortcut (P/2) = P/4 := by
    have hp := h.endpoint_four
    unfold shortcut
    split <;> omega
  exact ((basin_orbit m (l+17)).symm.trans (by rw [he])).trans
    ((by rw [← hhalf]; exact basin_step (P/2)))

theorem target_basin_transfer {l P w m : Nat} (h : Guard l P w m) :
    Basin (2*m-1) ↔ Basin (P-1) := by
  have he := target_path h
  have hb := basin_orbit (2*m-1) (l+16)
  rw [he] at hb
  exact hb.symm

theorem source_positive {l P w m : Nat} (h : Guard l P w m) : 0 < m := by
  obtain ⟨he, _⟩ := guard_equations h
  obtain ⟨t, hm, _⟩ := entry_parameter he
  omega

/-- An arbitrary supplied suffix is preserved, without assuming its height. -/
theorem supplied_certificate_splice {l P w m d : Nat} (h : Guard l P w m)
    (hd : Hits (P/2) (d+1)) : Hits m (l+17+d) := by
  have hhalf : shortcut (P/2) = P/4 := by
    have hp := h.endpoint_four
    unfold shortcut
    split <;> omega
  change Hits (shortcut (P/2)) d at hd
  rw [hhalf] at hd
  apply (hits_iff_orbit _ _).mpr
  rw [orbit_add, source_path h]
  exact (hits_iff_orbit _ _).mp hd

/-- A failed parent comparison becomes a strictly smaller failed ψ comparison. -/
theorem failed_comparison_reset {l P w m : Nat} (h : Guard l P w m)
    (hc : Basin (P/2)) (hb : ¬ Basin (P-1)) :
    m < P/2 ∧ Basin m ∧ ¬ Basin (2*m-1) := by
  refine ⟨?_, (source_basin_transfer h).mpr hc, ?_⟩
  · simpa [orbit] using source_prefix_below h 0 (by omega)
  · exact fun hbad => hb ((target_basin_transfer h).mp hbad)

#print axioms odd_run
#print axioms entry_parameter
#print axioms source_path
#print axioms target_path
#print axioms source_prefix_below
#print axioms source_basin_transfer
#print axioms target_basin_transfer
#print axioms supplied_certificate_splice
#print axioms failed_comparison_reset

end CollatzUnboundedReset
