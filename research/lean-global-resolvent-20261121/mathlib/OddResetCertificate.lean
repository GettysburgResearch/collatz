import OddCertificateMeasure

/-!
Generated explicit Mathlib port, with kernel-checked end-to-end composition.

The source bodies below are extracted verbatim by build_odd_reset_certificate.py
from the following frozen core modules; the reset's outer namespace is renamed.
TerminalFive.lean: 369a2189d9a65b3cbe7be8dae1010b34bd53cb0107c7de3f256a0933fbdeddb4
UnboundedReset.lean: 66ec761aaffff2509e6cc2d48ce384a6ea05ca56c221c283c069807c7318dd6a
OddReset.lean: 46556cdabf11a88928cafcb1eab2bf328e8f477ce23767e93337c07eb359fa75

The separate core import is incompatible with Mathlib's induction declarations.
No theorem is postulated to cross that boundary: all copied proofs are rechecked.
The small interface below uses the odd-certificate module's exact shortcut map,
and orbit_eq proves equality of the two finite-iteration conventions.
The final theorem applies to EVERY complete supplied source certificate.
-/

set_option autoImplicit false
set_option maxHeartbeats 4000000
set_option linter.unusedSimpArgs false

namespace CollatzResetPortBase

def shortcut (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else (3*n+1) / 2

def Hits (n : Nat) : Nat → Prop
  | 0 => n = 1
  | k+1 => Hits (shortcut n) k

def Basin (n : Nat) : Prop := ∃ k, Hits n k

theorem basin_step (n : Nat) : Basin (shortcut n) ↔ Basin n := by
  constructor
  · rintro ⟨k,h⟩
    exact ⟨k+1,h⟩
  · rintro ⟨k,h⟩
    cases k with
    | zero => change n = 1 at h; subst n; exact ⟨1,rfl⟩
    | succ k => exact ⟨k,h⟩

def orbit (n : Nat) : Nat → Nat
  | 0 => n
  | t + 1 => shortcut (orbit n t)

theorem orbit_add (n s t : Nat) :
    orbit n (s + t) = orbit (orbit n s) t := by
  induction t with
  | zero => rfl
  | succ t ih => simpa [orbit, Nat.add_assoc] using congrArg shortcut ih

theorem orbit_step (n t : Nat) : orbit (shortcut n) t = orbit n (t + 1) := by
  have h := orbit_add n 1 t
  simpa [orbit, Nat.add_comm] using h.symm

theorem hits_iff_orbit (n d : Nat) : Hits n d ↔ orbit n d = 1 := by
  induction d generalizing n with
  | zero => rfl
  | succ d ih =>
    change Hits (shortcut n) d ↔ orbit n (d + 1) = 1
    rw [ih, orbit_step]

theorem basin_orbit (n t : Nat) : Basin (orbit n t) ↔ Basin n := by
  induction t with
  | zero => rfl
  | succ t ih => exact (basin_step _).trans ih

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


theorem shortcut_eq (n : Nat) : shortcut n = CollatzOddCertificate.step n := rfl

theorem orbit_eq (n k : Nat) : orbit n k = CollatzOddCertificate.orbit k n := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih =>
    rw [← orbit_step, ih]
    rfl

theorem basin_iff_certificate (n : Nat) :
    Basin n ↔ Nonempty (CollatzOddCertificate.HitCertificate n) := by
  constructor
  · rintro ⟨k,hk⟩
    refine ⟨⟨k, ?_⟩⟩
    rw [← orbit_eq]
    exact (hits_iff_orbit n k).mp hk
  · rintro ⟨⟨k,hk⟩⟩
    refine ⟨k, (hits_iff_orbit n k).mpr ?_⟩
    rwa [orbit_eq]

end CollatzResetPortBase

open CollatzResetPortBase

namespace CollatzOddResetPort


theorem entry_parameter {m v : Nat} (h : 27*m+279 = 512*v) :
    ∃ t : Nat, m = 512*t+331 ∧ v = 27*t+18 := by
  have hb : 512*(m+11)+m = 512*(19*v)+331 := by omega
  have hm : m % 512 = 331 := by
    have hh := congrArg (fun n : Nat => n % 512) hb
    simpa [Nat.add_mod, Nat.mul_mod] using hh
  refine ⟨m/512, ?_, ?_⟩ <;> omega

theorem entry_source_profile (t : Nat) :
    orbit (512*t+331) 0 = 512*t+331 ∧
    orbit (512*t+331) 1 = 768*t+497 ∧
    orbit (512*t+331) 2 = 1152*t+746 ∧
    orbit (512*t+331) 3 = 576*t+373 ∧
    orbit (512*t+331) 4 = 864*t+560 ∧
    orbit (512*t+331) 5 = 432*t+280 ∧
    orbit (512*t+331) 6 = 216*t+140 ∧
    orbit (512*t+331) 7 = 108*t+70 ∧
    orbit (512*t+331) 8 = 54*t+35 := by
  have h0 : shortcut (512*t+331) = 768*t+497 := by unfold shortcut; split <;> omega
  have h1 : shortcut (768*t+497) = 1152*t+746 := by unfold shortcut; split <;> omega
  have h2 : shortcut (1152*t+746) = 576*t+373 := by unfold shortcut; split <;> omega
  have h3 : shortcut (576*t+373) = 864*t+560 := by unfold shortcut; split <;> omega
  have h4 : shortcut (864*t+560) = 432*t+280 := by unfold shortcut; split <;> omega
  have h5 : shortcut (432*t+280) = 216*t+140 := by unfold shortcut; split <;> omega
  have h6 : shortcut (216*t+140) = 108*t+70 := by unfold shortcut; split <;> omega
  have h7 : shortcut (108*t+70) = 54*t+35 := by unfold shortcut; split <;> omega
  simp only [orbit, h0, h1, h2, h3, h4, h5, h6, h7, and_self]

theorem entry_source {m v : Nat} (h : 27*m+279 = 512*v) :
    orbit m 8 = 2*v-1 := by
  obtain ⟨t, hm, hv⟩ := entry_parameter h
  rw [hm, hv]
  obtain ⟨_,_,_,_,_,_,_,_,he⟩ := entry_source_profile t
  omega

theorem entry_odd_bound {m v : Nat} (h : 27*m+279 = 512*v)
    (j : Nat) (hj : j < 8) (ho : orbit m j % 2 = 1) :
    9*orbit m j+135 ≤ 256*v := by
  obtain ⟨t, hm, hv⟩ := entry_parameter h
  rw [hm] at ho ⊢
  rw [hv]
  obtain ⟨h0,h1,h2,h3,h4,h5,h6,h7,_⟩ := entry_source_profile t
  have hc : j=0 ∨ j=1 ∨ j=2 ∨ j=3 ∨ j=4 ∨ j=5 ∨ j=6 ∨ j=7 := by omega
  rcases hc with h | h | h | h | h | h | h | h <;> subst j <;> omega

theorem entry_target {m v : Nat} (h : 27*m+279 = 512*v) :
    orbit (2*m-1) 8 = 4*v-1 := by
  obtain ⟨t, hm, hv⟩ := entry_parameter h
  rw [hm, hv]
  have hstart : 2*(512*t+331)-1 = 1024*t+661 := by omega
  have h0 : shortcut (1024*t+661) = 1536*t+992 := by unfold shortcut; split <;> omega
  have h1 : shortcut (1536*t+992) = 768*t+496 := by unfold shortcut; split <;> omega
  have h2 : shortcut (768*t+496) = 384*t+248 := by unfold shortcut; split <;> omega
  have h3 : shortcut (384*t+248) = 192*t+124 := by unfold shortcut; split <;> omega
  have h4 : shortcut (192*t+124) = 96*t+62 := by unfold shortcut; split <;> omega
  have h5 : shortcut (96*t+62) = 48*t+31 := by unfold shortcut; split <;> omega
  have h6 : shortcut (48*t+31) = 72*t+47 := by unfold shortcut; split <;> omega
  have h7 : shortcut (72*t+47) = 108*t+71 := by unfold shortcut; split <;> omega
  rw [hstart]
  simp only [orbit, h0, h1, h2, h3, h4, h5, h6, h7]
  omega

theorem tail_parameter {A P : Nat} (h : 2*P=9*A+1) (hp : P%4=0) :
    ∃ b : Nat, A=8*b+7 ∧ P=36*b+32 := by
  refine ⟨A/8, ?_, ?_⟩ <;> omega

theorem source_tail_profile (b : Nat) :
    orbit (16*b+13) 0 = 16*b+13 ∧
    orbit (16*b+13) 1 = 24*b+20 ∧
    orbit (16*b+13) 2 = 12*b+10 ∧
    orbit (16*b+13) 3 = 6*b+5 ∧
    orbit (16*b+13) 4 = 9*b+8 := by
  have h0 : shortcut (16*b+13) = 24*b+20 := by unfold shortcut; split <;> omega
  have h1 : shortcut (24*b+20) = 12*b+10 := by unfold shortcut; split <;> omega
  have h2 : shortcut (12*b+10) = 6*b+5 := by unfold shortcut; split <;> omega
  have h3 : shortcut (6*b+5) = 9*b+8 := by unfold shortcut; split <;> omega
  simp only [orbit, h0, h1, h2, h3, and_self]

theorem source_tail {A P : Nat} (h : 2*P=9*A+1) (hp : P%4=0) :
    orbit (2*A-1) 4 = P/4 := by
  obtain ⟨b, hA, hP⟩ := tail_parameter h hp
  rw [hA, hP, show 2*(8*b+7)-1=16*b+13 by omega]
  obtain ⟨_,_,_,_,he⟩ := source_tail_profile b
  omega

theorem source_tail_odd_bound {A P : Nat} (h : 2*P=9*A+1) (hp : P%4=0)
    (j : Nat) (hj : j ≤ 4) (ho : orbit (2*A-1) j % 2 = 1) :
    orbit (2*A-1) j < P/2 := by
  obtain ⟨b, hA, hP⟩ := tail_parameter h hp
  rw [hA, show 2*(8*b+7)-1=16*b+13 by omega] at ho ⊢
  rw [hP]
  obtain ⟨h0,h1,h2,h3,h4⟩ := source_tail_profile b
  have hc : j=0 ∨ j=1 ∨ j=2 ∨ j=3 ∨ j=4 := by omega
  rcases hc with h | h | h | h | h <;> subst j <;> omega

theorem target_tail {A P : Nat} (h : 2*P=9*A+1) (hp : P%4=0) :
    orbit (4*A-1) 3 = P-1 := by
  obtain ⟨b, hA, hP⟩ := tail_parameter h hp
  rw [hA, hP, show 4*(8*b+7)-1=32*b+27 by omega]
  have h0 : shortcut (32*b+27) = 48*b+41 := by unfold shortcut; split <;> omega
  have h1 : shortcut (48*b+41) = 72*b+62 := by unfold shortcut; split <;> omega
  have h2 : shortcut (72*b+62) = 36*b+31 := by unfold shortcut; split <;> omega
  simp only [orbit, h0, h1, h2]
  omega

theorem entry_power_bound (l : Nat) (hl : 7 ≤ l) : 1024*2^l ≤ 81*3^l := by
  have aux : ∀ r : Nat, 1024*2^(7+r) ≤ 81*3^(7+r) := by
    intro r
    induction r with
    | zero => decide
    | succ r ih =>
      rw [show 7+(r+1)=(7+r)+1 by omega]
      simp only [Nat.pow_succ]
      omega
  obtain ⟨r, hr⟩ := Nat.exists_eq_add_of_le hl
  rw [hr]
  exact aux r

structure Guard (l P w m : Nat) : Prop where
  depth : 7 ≤ l
  source_scale : 0 < w
  endpoint_pos : 0 < P
  endpoint_four : P%4=0
  endpoint_eq : 2*P-1=3^(l+2)*w
  entry_eq : 27*m+279=2^(l+9)*w

theorem guard_equations {l P w m : Nat} (h : Guard l P w m) :
    27*m+279=512*(2^l*w) ∧ 2*P=9*(3^l*w)+1 := by
  have he : 2^(l+9)*w=512*(2^l*w) := by
    simp [Nat.pow_add, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
  have hp : 3^(l+2)*w=9*(3^l*w) := by
    simp [Nat.pow_add, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
  constructor
  · have hh := h.entry_eq
    rwa [he] at hh
  · have hh := h.endpoint_eq
    rw [hp] at hh
    have hpos := h.endpoint_pos
    omega

theorem source_path {l P w m : Nat} (h : Guard l P w m) :
    orbit m (l+12)=P/4 := by
  obtain ⟨he,hp⟩ := guard_equations h
  have hin := entry_source he
  have hm := odd_run l (2*w) (by have hw := h.source_scale; omega)
  have ee : 2*(2^l*w)-1=2^l*(2*w)-1 := by
    simp [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
  have eo : 3^l*(2*w)-1=2*(3^l*w)-1 := by
    simp [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
  rw [show l+12=8+(l+4) by omega, orbit_add, hin, ee,
    orbit_add, hm, eo, source_tail hp h.endpoint_four]

theorem target_path {l P w m : Nat} (h : Guard l P w m) :
    orbit (2*m-1) (l+11)=P-1 := by
  obtain ⟨he,hp⟩ := guard_equations h
  have hin := entry_target he
  have hm := odd_run l (4*w) (by have hw := h.source_scale; omega)
  have ee : 4*(2^l*w)-1=2^l*(4*w)-1 := by
    simp [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
  have eo : 3^l*(4*w)-1=4*(3^l*w)-1 := by
    simp [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
  rw [show l+11=8+(l+3) by omega, orbit_add, hin, ee,
    orbit_add, hm, eo, target_tail hp h.endpoint_four]

/-- Only odd source states are charged.  No bound on every even state is used. -/
theorem source_odd_prefix_below {l P w m : Nat} (h : Guard l P w m)
    (j : Nat) (hj : j ≤ l+12) (ho : orbit m j % 2 = 1) :
    orbit m j < P/2 := by
  obtain ⟨he,hp⟩ := guard_equations h
  have hin := entry_source he
  have hw := h.source_scale
  have hdom : 1024*(2^l*w) ≤ 81*(3^l*w) := by
    simpa [Nat.mul_assoc] using Nat.mul_le_mul_right w (entry_power_bound l h.depth)
  by_cases hentry : j < 8
  · have hb := entry_odd_bound he j hentry ho
    have hp4 := h.endpoint_four
    omega
  · have hf : 8+(j-8)=j := by omega
    rw [← hf, orbit_add, hin] at ho ⊢
    have ee : 2*(2^l*w)-1=2^l*(2*w)-1 := by
      simp [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
    rw [ee] at ho ⊢
    by_cases hloop : j-8 ≤ l
    · have hb := odd_run_bound l (2*w) (by omega) (j-8) hloop
      have eo : 3^l*(2*w)-1=2*(3^l*w)-1 := by
        simp [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
      rw [eo] at hb
      have hp4 := h.endpoint_four
      omega
    · have hsplit : j-8=l+(j-8-l) := by omega
      rw [hsplit, orbit_add, odd_run l (2*w) (by omega)] at ho ⊢
      have eo : 3^l*(2*w)-1=2*(3^l*w)-1 := by
        simp [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
      rw [eo] at ho ⊢
      exact source_tail_odd_bound hp h.endpoint_four (j-8-l) (by omega) ho

theorem source_positive_odd {l P w m : Nat} (h : Guard l P w m) :
    0 < m ∧ m%2=1 := by
  obtain ⟨he,_⟩ := guard_equations h
  obtain ⟨t,hm,_⟩ := entry_parameter he
  omega

theorem parent_even_nonterminal {l P w m : Nat} (h : Guard l P w m) :
    P/2%2=0 ∧ 1<P/2 ∧ shortcut (P/2)=P/4 := by
  have hp := h.endpoint_four
  have hpos := h.endpoint_pos
  refine ⟨by omega, by omega, ?_⟩
  unfold shortcut
  split <;> omega

theorem source_basin_transfer {l P w m : Nat} (h : Guard l P w m) :
    Basin m ↔ Basin (P/2) := by
  have he := source_path h
  have hhalf := (parent_even_nonterminal h).2.2
  exact ((basin_orbit m (l+12)).symm.trans (by rw [he])).trans
    ((by rw [← hhalf]; exact basin_step (P/2)))

theorem target_basin_transfer {l P w m : Nat} (h : Guard l P w m) :
    Basin (2*m-1) ↔ Basin (P-1) := by
  have he := target_path h
  have hb := basin_orbit (2*m-1) (l+11)
  rw [he] at hb
  exact hb.symm

theorem supplied_certificate_splice {l P w m d : Nat} (h : Guard l P w m)
    (hd : Hits (P/2) (d+1)) : Hits m (l+12+d) := by
  have hhalf := (parent_even_nonterminal h).2.2
  change Hits (shortcut (P/2)) d at hd
  rw [hhalf] at hd
  apply (hits_iff_orbit _ _).mpr
  rw [orbit_add, source_path h]
  exact (hits_iff_orbit _ _).mp hd

theorem failed_comparison_reset {l P w m : Nat} (h : Guard l P w m)
    (hc : Basin (P/2)) (hb : ¬ Basin (P-1)) :
    m<P/2 ∧ Basin m ∧ ¬ Basin (2*m-1) := by
  refine ⟨?_, (source_basin_transfer h).mpr hc, ?_⟩
  · have ho := (source_positive_odd h).2
    simpa [orbit] using source_odd_prefix_below h 0 (by omega) (by simpa [orbit] using ho)
  · exact fun ht => hb ((target_basin_transfer h).mp ht)

#print axioms source_path
#print axioms target_path
#print axioms source_odd_prefix_below
#print axioms source_positive_odd
#print axioms parent_even_nonterminal
#print axioms supplied_certificate_splice
#print axioms failed_comparison_reset



/-- Every supplied parent certificate has a strictly smaller complete child
certificate.  The statement preserves its arbitrary common suffix. -/
theorem complete_certificate_descent {l P w m : Nat} (h : Guard l P w m)
    (c : CollatzOddCertificate.HitCertificate (P/2)) :
    ∃ c' : CollatzOddCertificate.HitCertificate m,
      CollatzOddCertificate.Below (CollatzOddCertificate.measure c')
        (CollatzOddCertificate.measure c) := by
  have hp := parent_even_nonterminal h
  apply CollatzOddCertificate.splice_one_halving
    (b := l+12) hp.2.1 hp.1 ?_ ?_ ?_ c
  · have he := source_path h
    rw [orbit_eq] at he
    have hd : (P/2)/2 = P/4 := by omega
    rwa [hd]
  · intro he
    have ho := (source_positive_odd h).2
    omega
  · intro j hj ho
    have hodd : orbit m j % 2 = 1 := by rwa [orbit_eq]
    have hb := source_odd_prefix_below h j (by omega) hodd
    rwa [orbit_eq] at hb

/-- The same complete-certificate descent preserves a failed target comparison.
No closure or normalized-unit coverage is assumed. -/
theorem complete_failed_reset {l P w m : Nat} (h : Guard l P w m)
    (c : CollatzOddCertificate.HitCertificate (P/2))
    (hbad : ¬ Nonempty (CollatzOddCertificate.HitCertificate (P-1))) :
    ∃ c' : CollatzOddCertificate.HitCertificate m,
      CollatzOddCertificate.Below (CollatzOddCertificate.measure c')
        (CollatzOddCertificate.measure c) ∧
      ¬ Nonempty (CollatzOddCertificate.HitCertificate (2*m-1)) := by
  obtain ⟨c',hc'⟩ := complete_certificate_descent h c
  refine ⟨c',hc',?_⟩
  intro hc
  apply hbad
  apply (basin_iff_certificate (P-1)).mp
  exact (target_basin_transfer h).mp ((basin_iff_certificate (2*m-1)).mpr hc)

#print axioms complete_certificate_descent
#print axioms complete_failed_reset

end CollatzOddResetPort
