import Collatz.GapMultiset

/-!
An unbounded even-source reset in the graded exponent multiset order.

The path arithmetic is adapted from PR176, commit
ad9a0611d22b48c0fd0c1da31091179654ba31a9,
research/lean-global-resolvent-20261121/lean/Collatz/OddReset.lean.
That source requires loop depth at least seven for its ordinary-height bound.
Here the exact paths hold at every natural depth, including zero. The new
multiset proof instead requires an initial even valuation at least five.
All finite inherited certificate tails are preserved literally.
No universal guard coverage or Collatz convergence is asserted.
-/

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset

set_option autoImplicit false
set_option maxHeartbeats 4000000

namespace CollatzUnboundedGapReset

def orbit (n : Nat) : Nat → Nat
  | 0 => n
  | k+1 => orbit (shortcut n) k

theorem orbit_add (n a b : Nat) : orbit n (a+b) = orbit (orbit n a) b := by
  induction a generalizing n with
  | zero => simp [orbit]
  | succ a ih => simpa only [Nat.succ_add,orbit] using ih (shortcut n)

theorem orbit_basin (n k : Nat) : Basin (orbit n k) ↔ Basin n := by
  induction k generalizing n with
  | zero => exact Iff.rfl
  | succ k ih => exact (ih (shortcut n)).trans (basin_step n)

theorem odd_run (l u : Nat) (hu : 0<u) :
    orbit (2^l*u-1) l = 3^l*u-1 := by
  induction l generalizing u with
  | zero => simp [orbit]
  | succ l ih =>
    have pos : 0<2^l*u := Nat.mul_pos (Nat.pow_pos (by decide)) hu
    have step : shortcut (2^(l+1)*u-1)=2^l*(3*u)-1 := by
      have left : 2^(l+1)*u=2*(2^l*u) := by simp [Nat.pow_succ]; grind
      have right : 2^l*(3*u)=3*(2^l*u) := by grind
      rw [left,right]
      unfold shortcut
      split <;> omega
    rw [orbit,step,ih (3*u) (by omega),Nat.pow_succ]
    congr 1
    grind

theorem entry_parameter {m v : Nat} (h : 27*m+279=512*v) :
    ∃ t : Nat, m=512*t+331 ∧ v=27*t+18 := by
  have hb : 512*(m+11)+m=512*(19*v)+331 := by omega
  have hm : m%512=331 := by
    have hh := congrArg (fun n : Nat => n%512) hb
    simpa [Nat.add_mod,Nat.mul_mod] using hh
  refine ⟨m/512,?_,?_⟩ <;> omega

theorem entry_target {m v : Nat} (h : 27*m+279=512*v) :
    orbit (2*m-1) 8=4*v-1 := by
  obtain ⟨t,hm,hv⟩ := entry_parameter h
  rw [hm,hv]
  have hstart : 2*(512*t+331)-1=1024*t+661 := by omega
  have h0 : shortcut (1024*t+661)=1536*t+992 := by unfold shortcut; split <;> omega
  have h1 : shortcut (1536*t+992)=768*t+496 := by unfold shortcut; split <;> omega
  have h2 : shortcut (768*t+496)=384*t+248 := by unfold shortcut; split <;> omega
  have h3 : shortcut (384*t+248)=192*t+124 := by unfold shortcut; split <;> omega
  have h4 : shortcut (192*t+124)=96*t+62 := by unfold shortcut; split <;> omega
  have h5 : shortcut (96*t+62)=48*t+31 := by unfold shortcut; split <;> omega
  have h6 : shortcut (48*t+31)=72*t+47 := by unfold shortcut; split <;> omega
  have h7 : shortcut (72*t+47)=108*t+71 := by unfold shortcut; split <;> omega
  rw [hstart]
  simp only [orbit,h0,h1,h2,h3,h4,h5,h6,h7]
  omega

theorem tail_parameter {A P : Nat} (h : 2*P=9*A+1) (hp : P%4=0) :
    ∃ b : Nat, A=8*b+7 ∧ P=36*b+32 := by
  refine ⟨A/8,?_,?_⟩ <;> omega

theorem target_tail {A P : Nat} (h : 2*P=9*A+1) (hp : P%4=0) :
    orbit (4*A-1) 3=P-1 := by
  obtain ⟨b,hA,hP⟩ := tail_parameter h hp
  rw [hA,hP,show 4*(8*b+7)-1=32*b+27 by omega]
  have h0 : shortcut (32*b+27)=48*b+41 := by unfold shortcut; split <;> omega
  have h1 : shortcut (48*b+41)=72*b+62 := by unfold shortcut; split <;> omega
  have h2 : shortcut (72*b+62)=36*b+31 := by unfold shortcut; split <;> omega
  simp only [orbit,h0,h1,h2]
  omega

/-- Exact path guards, with no lower bound on the loop depth. -/
structure Guard (l P w m : Nat) : Prop where
  source_scale : 0<w
  endpoint_pos : 0<P
  endpoint_four : P%4=0
  endpoint_eq : 2*P-1=3^(l+2)*w
  entry_eq : 27*m+279=2^(l+9)*w

theorem guard_equations {l P w m : Nat} (h : Guard l P w m) :
    27*m+279=512*(2^l*w) ∧ 2*P=9*(3^l*w)+1 := by
  have he : 2^(l+9)*w=512*(2^l*w) := by
    simp [Nat.pow_add,Nat.mul_assoc,Nat.mul_comm]
  have hp : 3^(l+2)*w=9*(3^l*w) := by
    simp [Nat.pow_add,Nat.mul_assoc,Nat.mul_comm]
  constructor
  · have hh := h.entry_eq
    rwa [he] at hh
  · have hh := h.endpoint_eq
    rw [hp] at hh
    have hpos := h.endpoint_pos
    omega

theorem target_path {l P w m : Nat} (h : Guard l P w m) :
    orbit (2*m-1) (l+11)=P-1 := by
  obtain ⟨he,hp⟩ := guard_equations h
  have hin := entry_target he
  have hm := odd_run l (4*w) (by have hw := h.source_scale; omega)
  have ee : 4*(2^l*w)-1=2^l*(4*w)-1 := by
    simp [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm]
  have eo : 3^l*(4*w)-1=4*(3^l*w)-1 := by
    simp [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm]
  rw [show l+11=8+(l+3) by omega,orbit_add,hin,ee,
    orbit_add,hm,eo,target_tail hp h.endpoint_four]

theorem target_basin_transfer {l P w m : Nat} (h : Guard l P w m) :
    Basin (2*m-1) ↔ Basin (P-1) := by
  have hb := orbit_basin (2*m-1) (l+11)
  rw [target_path h] at hb
  exact hb.symm

theorem source_positive_odd {l P w m : Nat} (h : Guard l P w m) :
    0<m ∧ m%2=1 := by
  obtain ⟨he,_⟩ := guard_equations h
  obtain ⟨t,hm,_⟩ := entry_parameter he
  omega

/-- Prepend the literal source entrance (1,2,5), retaining the supplied tail. -/
theorem entry_certificate {m v : Nat} {tail : List Nat}
    (h : 27*m+279=512*v) (cert : Certificate (2*v-1) tail) :
    Certificate m ([1,2,5]++tail) := by
  obtain ⟨t,hm,hv⟩ := entry_parameter h
  rw [hm]
  rw [hv,show 2*(27*t+18)-1=54*t+35 by omega] at cert
  apply (certificate_cons_iff _ _ _).mpr
  refine ⟨by decide,768*t+497,by omega,?_⟩
  apply (certificate_cons_iff _ _ _).mpr
  refine ⟨by decide,576*t+373,by omega,?_⟩
  apply (certificate_cons_iff _ _ _).mpr
  exact ⟨by decide,54*t+35,by omega,cert⟩

/-- Any number of exact exponent-one source steps. -/
theorem ones_certificate (l u : Nat) (hu : 0<u) (tail : List Nat)
    (cert : Certificate (3^l*u-1) tail) :
    Certificate (2^l*u-1) (List.replicate l 1++tail) := by
  induction l generalizing u with
  | zero => simpa using cert
  | succ l ih =>
    have pos : 0<2^l*u := Nat.mul_pos (Nat.pow_pos (by decide)) hu
    have left : 2^(l+1)*u=2*(2^l*u) := by simp [Nat.pow_succ]; grind
    have right : 2^l*(3*u)=3*(2^l*u) := by grind
    have he : 3*(2^(l+1)*u-1)+1=2^1*(2^l*(3*u)-1) := by
      rw [left,right]
      omega
    have endEq : 3^l*(3*u)-1=3^(l+1)*u-1 := by
      rw [Nat.pow_succ]
      congr 1
      grind
    have ht := ih (3*u) (by omega) (endEq ▸ cert)
    simpa only [List.replicate_succ,List.cons_append] using (certificate_cons_iff (2^(l+1)*u-1) 1 _).mpr
      ⟨by decide,2^l*(3*u)-1,he,ht⟩

/-- The last source gap absorbs the entire former initial even run. -/
theorem tail_certificate {A P e q : Nat} {tail : List Nat}
    (h : 2*P=9*A+1) (hp : P%4=0) (he : 0<e)
    (parent : P/2=2^e*q) (cert : Certificate q tail) :
    Certificate (2*A-1) ([3,e]++tail) := by
  obtain ⟨b,hA,hP⟩ := tail_parameter h hp
  rw [hA,show 2*(8*b+7)-1=16*b+13 by omega]
  have equation : 3*(6*b+5)+1=2^e*q := by rw [hP] at parent; omega
  apply (certificate_cons_iff _ _ _).mpr
  refine ⟨by decide,6*b+5,by omega,?_⟩
  exact (certificate_cons_iff _ _ _).mpr ⟨he,q,equation,cert⟩

def gapPrefix (l e : Nat) : List Nat := [1,2,5]++List.replicate l 1++[3,e]

theorem prefix_bounded (l e : Nat) (he : 5≤e) :
    ∀ a ∈ gapPrefix l e, a≤e := by
  intro a ha
  change a ∈ ([1,2,5]++List.replicate l 1)++[3,e] at ha
  rcases List.mem_append.mp ha with h | h
  · rcases List.mem_append.mp h with h | h
    · simp only [List.mem_cons,List.not_mem_nil,or_false] at h
      omega
    · have eq : a=1 := List.eq_of_mem_replicate h
      omega
  · simp only [List.mem_cons,List.not_mem_nil,or_false] at h
    omega

/-- Convert any complete supplied parent certificate, including arbitrary
terminal padding, and strictly decrease one common well-founded order. -/
theorem complete_certificate_reset {l P w m e : Nat} {tail : List Nat}
    (h : Guard l P w m) (he : 5≤e)
    (cert : PoweredCertificate (P/2) e tail) :
    PoweredCertificate m 0 (gapPrefix l e++tail) ∧
    Less (grades 0 (gapPrefix l e++tail)) (grades e tail) := by
  obtain ⟨q,parent,tailCert⟩ := cert
  obtain ⟨entry,last⟩ := guard_equations h
  have endCert := tail_certificate last h.endpoint_four (by omega) parent tailCert
  have endEq : 3^l*(2*w)-1=2*(3^l*w)-1 := by grind
  have loopCert := ones_certificate l (2*w) (by have hw := h.source_scale; omega)
    ([3,e]++tail) (endEq ▸ endCert)
  have startEq : 2^l*(2*w)-1=2*(2^l*w)-1 := by grind
  rw [startEq] at loopCert
  have fullCert := entry_certificate entry loopCert
  refine ⟨⟨m,by simp,?_⟩,even_to_odd_replacement e (gapPrefix l e) tail (by omega)
    (prefix_bounded l e he)⟩
  simpa [gapPrefix,List.append_assoc] using fullCert

theorem complete_failed_reset {l P w m e : Nat} {tail : List Nat}
    (h : Guard l P w m) (he : 5≤e)
    (cert : PoweredCertificate (P/2) e tail) (bad : ¬ Basin (P-1)) :
    PoweredCertificate m 0 (gapPrefix l e++tail) ∧
    Less (grades 0 (gapPrefix l e++tail)) (grades e tail) ∧
    ¬ Basin (2*m-1) := by
  obtain ⟨new,drop⟩ := complete_certificate_reset h he cert
  exact ⟨new,drop,fun hit => bad ((target_basin_transfer h).mp hit)⟩

/-- A depth-zero instance absent from the old height-decreasing reset. -/
theorem depth_zero_guard : Guard 0 13568 3015 57163 := by constructor <;> decide

theorem depth_zero_expands : 13568/2 < 57163 := by decide

/-! ## Arbitrary finite paired entrances -/

/-- A positive-gap word interpreted as exact ordinary odd steps. The endpoint
need not already be known to converge. -/
def WordPath (n endpoint : Nat) : List Nat → Prop
  | [] => n=endpoint
  | a::as => 0<a ∧ ∃ u, 3*n+1=2^a*u ∧ WordPath u endpoint as

/-- The complete affine identity supplies every intermediate integer guard.
This theorem does not assume convergence of either endpoint. -/
theorem word_path_of_identity {n endpoint : Nat} {word : List Nat}
    (positive : PositiveGaps word)
    (identity : 3^word.length*n+correction word=2^total word*endpoint) :
    WordPath n endpoint word := by
  induction word generalizing n with
  | nil => simpa [WordPath,correction,total] using identity
  | cons a as ih =>
    have ha : 0<a := positive a (by simp)
    have ht : PositiveGaps as := fun b hb => positive b (by simp [hb])
    have eq : 3^as.length*(3*n+1)+2^a*correction as=
        2^a*(2^total as*endpoint) := by
      simp only [List.length_cons,correction,total,Nat.pow_succ,Nat.pow_add] at identity
      grind
    have divides : 2^a ∣ 3^as.length*(3*n+1) := by
      have hs : 2^a ∣ 3^as.length*(3*n+1)+2^a*correction as :=
        ⟨2^total as*endpoint,eq⟩
      have hr : 2^a ∣ 2^a*correction as := ⟨correction as,rfl⟩
      exact (Nat.dvd_add_iff_left hr).mpr hs
    have coprime : Nat.Coprime (2^a) (3^as.length) :=
      Nat.gcd_pow_right_of_gcd_eq_one (Nat.gcd_pow_left_of_gcd_eq_one
        (by decide : Nat.gcd 2 3=1))
    obtain ⟨u,step⟩ := coprime.dvd_of_dvd_mul_left divides
    have tailEq : 3^as.length*u+correction as=2^total as*endpoint := by
      rw [step] at eq
      have product : 2^a*(3^as.length*u+correction as)=
          2^a*(2^total as*endpoint) := by grind
      exact Nat.eq_of_mul_eq_mul_left (Nat.pow_pos (by decide)) product
    exact ⟨ha,u,step,ih ht tailEq⟩

theorem word_path_basin {n endpoint : Nat} {word : List Nat}
    (path : WordPath n endpoint word) : Basin n ↔ Basin endpoint := by
  induction word generalizing n with
  | nil => change n=endpoint at path; subst n; exact Iff.rfl
  | cons a as ih =>
    obtain ⟨ha,u,step,tail⟩ := path
    have odd : n%2=1 := by
      obtain ⟨b,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : a≠0)
      rw [Nat.pow_succ] at step
      have even : 3*n+1=2*(2^b*u) := by grind
      omega
    have move := (basin_odd n odd).symm
    rw [step] at move
    exact move.trans ((basin_pow_two a u).trans (ih tail))

theorem word_path_prepend_certificate {n endpoint : Nat} {word tail : List Nat}
    (path : WordPath n endpoint word) (cert : Certificate endpoint tail) :
    Certificate n (word++tail) := by
  induction word generalizing n with
  | nil => change n=endpoint at path; subst n; simpa using cert
  | cons a as ih =>
    obtain ⟨ha,u,step,rest⟩ := path
    exact (certificate_cons_iff _ _ _).mpr ⟨ha,u,step,ih rest⟩

/-- The entire arbitrary-word grammar for entrances from (m,2m-1) to
(x,2x+1), with equal odd counts and equal shortcut clocks on the two arms. -/
structure PairedEntrance (source target : List Nat) : Prop where
  source_positive : PositiveGaps source
  target_positive : PositiveGaps target
  same_length : source.length=target.length
  same_total : total source=total target
  correction_eq : correction target=
    2*correction source+3^source.length+2^total source

theorem paired_entrance_paths {source target : List Nat} {m v : Nat}
    (h : PairedEntrance source target) (hm : 0<m) (hv : 0<v)
    (entry : 3^source.length*m+correction source=2^total source*(2*v-1)) :
    WordPath m (2*v-1) source ∧ WordPath (2*m-1) (4*v-1) target := by
  refine ⟨word_path_of_identity h.source_positive entry,?_⟩
  apply word_path_of_identity h.target_positive
  rw [←h.same_length,←h.same_total,h.correction_eq]
  have mulEq : 3^source.length*(2*m-1)+3^source.length=2*(3^source.length*m) := by
    have main : 3^source.length*(2*m)=2*(3^source.length*m) := by grind
    have sub : 3^source.length*(2*m-1)+3^source.length=3^source.length*(2*m) := by
      have restore : (2*m-1)+1=2*m := by omega
      simpa only [Nat.mul_add,Nat.mul_one] using
        congrArg (fun z : Nat => 3^source.length*z) restore
    exact sub.trans main
  have mid : 4*v-1=2*(2*v-1)+1 := by omega
  have product : 2^total source*(4*v-1)=
      2*(2^total source*(2*v-1))+2^total source := by rw [mid]; grind
  rw [product,←entry]
  omega

def compiledPrefix (source : List Nat) (l e : Nat) : List Nat :=
  source++List.replicate l 1++[3,e]

theorem compiled_prefix_bounded {source : List Nat} (l e : Nat)
    (he : 3≤e) (bound : ∀ a ∈ source, a≤e) :
    ∀ a ∈ compiledPrefix source l e, a≤e := by
  intro a ha
  change a ∈ (source++List.replicate l 1)++[3,e] at ha
  rcases List.mem_append.mp ha with h | h
  · rcases List.mem_append.mp h with h | h
    · exact bound a h
    · have eq : a=1 := List.eq_of_mem_replicate h
      omega
  · simp only [List.mem_cons,List.not_mem_nil,or_false] at h
    omega

/-- Compile any legal paired entrance and any loop depth into a complete
supplied-certificate rewrite. The source-word length and loop depth have no
upper bound, and the old tail is not shortened, replaced, or re-selected. -/
theorem compiled_certificate_reset {source target : List Nat}
    {l P w m e : Nat} {tail : List Nat}
    (pair : PairedEntrance source target) (he : 3≤e)
    (bound : ∀ a ∈ source, a≤e) (hm : 0<m) (hw : 0<w)
    (four : P%4=0) (last : 2*P=9*(3^l*w)+1)
    (entry : 3^source.length*m+correction source=
      2^total source*(2*(2^l*w)-1))
    (cert : PoweredCertificate (P/2) e tail) :
    PoweredCertificate m 0 (compiledPrefix source l e++tail) ∧
    Less (grades 0 (compiledPrefix source l e++tail)) (grades e tail) ∧
    (Basin (2*m-1) ↔ Basin (P-1)) := by
  obtain ⟨q,parent,tailCert⟩ := cert
  obtain ⟨sourcePath,targetPath⟩ := paired_entrance_paths pair hm
    (Nat.mul_pos (Nat.pow_pos (by decide)) hw) entry
  have endCert := tail_certificate last four (by omega) parent tailCert
  have endEq : 3^l*(2*w)-1=2*(3^l*w)-1 := by grind
  have loopCert := ones_certificate l (2*w) (by omega) ([3,e]++tail) (endEq ▸ endCert)
  have startEq : 2^l*(2*w)-1=2*(2^l*w)-1 := by grind
  rw [startEq] at loopCert
  have fullCert := word_path_prepend_certificate sourcePath loopCert
  refine ⟨⟨m,by simp,?_⟩,even_to_odd_replacement e (compiledPrefix source l e) tail
    (by omega) (compiled_prefix_bounded l e he bound),?_⟩
  · simpa [compiledPrefix,List.append_assoc] using fullCert
  · have front := word_path_basin targetPath
    have loop := basin_pow_two_pred l (4*w) (by omega)
    have left : 2^l*(4*w)-1=4*(2^l*w)-1 := by grind
    have right : 3^l*(4*w)-1=4*(3^l*w)-1 := by grind
    rw [left,right] at loop
    have finish := orbit_basin (4*(3^l*w)-1) 3
    rw [target_tail last four] at finish
    exact front.trans (loop.trans finish.symm)

/-- An entrance whose source uses only exponents one, two, and three. -/
def lowSource : List Nat := [1,2,1,2,1,2,3,3]
def lowTarget : List Nat := [5,1,1,1,1,1,2,3]

theorem low_entrance : PairedEntrance lowSource lowTarget := by
  constructor
  · intro a ha
    simp [lowSource] at ha
    omega
  · intro a ha
    simp [lowTarget] at ha
    omega
  · decide
  · decide
  · decide

theorem low_source_bounded : ∀ a ∈ lowSource, a≤3 := by
  intro a ha
  simp [lowSource] at ha
  omega

/-- A new depth-zero reset with initial even valuation exactly three.
The child source expands, while its complete exponent multiset decreases. -/
theorem low_depth_zero_reset {tail : List Nat}
    (cert : PoweredCertificate 358216 3 tail) :
    PoweredCertificate 1590267 0 (compiledPrefix lowSource 0 3++tail) ∧
    Less (grades 0 (compiledPrefix lowSource 0 3++tail)) (grades 3 tail) ∧
    (Basin (2*1590267-1) ↔ Basin 716431) := by
  exact compiled_certificate_reset (P:=716432) (w:=159207) (l:=0)
    low_entrance (by decide) low_source_bounded (by decide) (by decide)
    (by decide) (by decide) (by decide) cert

#print axioms target_path
#print axioms complete_certificate_reset
#print axioms complete_failed_reset
#print axioms depth_zero_guard
#print axioms word_path_of_identity
#print axioms compiled_certificate_reset
#print axioms low_entrance
#print axioms low_depth_zero_reset

end CollatzUnboundedGapReset
