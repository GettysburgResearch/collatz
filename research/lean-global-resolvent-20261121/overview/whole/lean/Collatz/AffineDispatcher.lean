import Collatz.SourceEnvelope
import Collatz.TerminalCarry

set_option autoImplicit false
set_option maxHeartbeats 2000000
set_option maxRecDepth 2000

namespace CollatzAffineDispatcher

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzHighGapPump CollatzLowIntervalRefinement CollatzBoundedGapCofinal
open CollatzSourceEnvelope
open CollatzTerminalCarry (SignedPath iterate signed_path_exists signed_path_transfer
  iterate_add iterate_basin iterate_positive)

/-- One actual source edge refreshes exactly the binary horizon that is
consumed on the target. The carry may be any signed integer. -/
theorem affine_gap_transport {r u a p k n : Nat} {d z : Int}
    (gap : 3*r+1=2^a*u)
    (source : (n:Int)=(3:Int)^(p+1)*r+d)
    (path : SignedPath (d-(3:Int)^p) a k z) :
    (iterate n a:Int)=(3:Int)^(p+k)*u+z := by
  have lifted := congrArg (fun x : Nat => (x:Int)) gap
  simp only [Int.natCast_add,Int.natCast_mul,Int.natCast_pow] at lifted
  have pin : (n:Int)=((3:Int)^p*u)*(2:Int)^a+(d-(3:Int)^p) := by
    rw [Int.pow_succ] at source
    grind
  have result := signed_path_transfer path (Nat.le_refl a) pin
  simp only [Nat.sub_self,Int.pow_zero,Int.mul_one] at result
  rw [Int.pow_add]
  grind

/-- The complete compositional affine language. A source letter consumes
its exact number of ordinary target steps; the next degree records the
actual odd steps of the signed carry. Degree zero is a stopping state. -/
inductive Dispatch : Nat → Int → List Nat → Nat → Int → Prop where
  | done (p : Nat) (d : Int) : Dispatch p d [] p d
  | step {p a k out : Nat} {d z final : Int} {tail : List Nat} :
      SignedPath (d-(3:Int)^p) a k z → Dispatch (p+k) z tail out final →
      Dispatch (p+1) d (a::tail) out final

/-- Every finite supplied source word has a dispatch: consume the whole word
or stop earlier at degree zero. No finite-state carry restriction is imposed. -/
theorem dispatch_exists (p : Nat) (d : Int) (word : List Nat) :
    ∃ front tail out final, word=front++tail ∧
      Dispatch p d front out final ∧ (out=0 ∨ tail=[]) := by
  induction word generalizing p d with
  | nil => exact ⟨[],[],p,d,rfl,Dispatch.done p d,Or.inr rfl⟩
  | cons a word ih =>
    cases p with
    | zero => exact ⟨[],a::word,0,d,rfl,Dispatch.done 0 d,Or.inl rfl⟩
    | succ p =>
      obtain ⟨k,z,path⟩ := signed_path_exists (d-(3:Int)^p) a
      obtain ⟨front,tail,out,final,split,program,stop⟩ := ih (p+k) z
      exact ⟨a::front,tail,out,final,by simp [split],Dispatch.step path program,stop⟩

/-- Every dispatch has an exact positive ordinary interpretation on the
actual supplied prefix and the unchanged integer target. -/
theorem dispatch_transport {p out q u n : Nat} {d final : Int} {word : List Nat}
    (program : Dispatch p d word out final) (path : Prefix q word u)
    (source : (n:Int)=(3:Int)^p*q+d) :
    (iterate n (CollatzWitness.total word):Int)=(3:Int)^out*u+final := by
  induction program generalizing q n with
  | done p d =>
    have eq : q=u := by simpa [Prefix,correction,total] using path.2
    simpa [iterate,total,eq] using source
  | @step p a k out d z final tail signed program ih =>
    obtain ⟨_,v,gap,rest⟩ := (prefix_cons_iff q a u tail).mp path
    have first := affine_gap_transport gap source signed
    have result := ih rest first
    simpa only [CollatzWitness.total,iterate_add] using result

theorem signed_path_negative {d z : Int} {clock odds : Nat}
    (path : SignedPath d clock odds z) (negative : d<0) : z<0 := by
  induction path with
  | done d => exact negative
  | even even path ih => exact ih (by omega)
  | odd odd path ih => exact ih (by omega)

/-- Negative affine offsets remain negative throughout the source-driven
program, including every escaped state of the smaller two-state language. -/
theorem dispatch_negative {p out : Nat} {d final : Int} {word : List Nat}
    (program : Dispatch p d word out final) (negative : d<0) : final<0 := by
  induction program with
  | done p d => exact negative
  | @step p a k out d z final tail signed program ih =>
    have power : 0≤(3:Int)^p := by
      have h : 0≤((3:Nat)^p:Int) := Int.natCast_nonneg _
      simpa using h
    exact ih (signed_path_negative signed (by omega))

/-- Total normalization on an actual complete source. The only terminal
alternative to degree zero is the literal source endpoint one, with its
explicit signed affine target debt. That debt is not assumed convergent. -/
theorem complete_dispatch_normal_form {p q n : Nat} {d : Int} {word : List Nat}
    (cert : Certificate q word) (source : (n:Int)=(3:Int)^p*q+d) (negative : d<0) :
    ∃ front tail u out final, word=front++tail ∧ Dispatch p d front out final ∧
      Prefix q front u ∧ Certificate u tail ∧
      (iterate n (CollatzWitness.total front):Int)=(3:Int)^out*u+final ∧
      final<0 ∧ (out=0 ∨ (tail=[] ∧ u=1)) := by
  obtain ⟨front,tail,out,final,split,program,stop⟩ := dispatch_exists p d word
  obtain ⟨u,path,rest⟩ := CollatzLowGapLoops.split_certificate q front tail
    (by simpa [split] using cert)
  refine ⟨front,tail,u,out,final,split,program,path,rest,
    dispatch_transport program path source,dispatch_negative program negative,?_⟩
  rcases stop with zero | empty
  · exact Or.inl zero
  · have one : u=1 := by simpa [empty,Certificate,correction,total] using rest.2
    exact Or.inr ⟨empty,one⟩

/-- Any nonempty prefix can be consumed while installing its maximal paid
initial run. This is the same complete multiset rank as PR177. -/
theorem boosted_prefix_rank (e : Nat) (front tail : List Nat)
    (positive : 1≤e) (nonempty : front≠[]) :
    Less (grades (boost e front) tail) (grades e (front++tail)) := by
  induction front generalizing e with
  | nil => exact False.elim (nonempty rfl)
  | cons a front ih =>
    have first := boosted_step_rank e a (front++tail) positive
    cases front with
    | nil => simpa [boost] using first
    | cons b front =>
      have next := ih (max e (a-1))
        (by have h:=Nat.le_max_left e (a-1); omega) (by simp)
      exact less_trans next first

/-- The exact rank-paid target capture rule for the entire dispatch language.
The target inequality is an explicit hypothesis; total transitions alone do
not establish it. No fresh complete certificate is substituted for the tail. -/
theorem dispatch_interval_rule {p out e q u n : Nat} {d final : Int}
    {front tail : List Nat}
    (positive : 1≤e) (nonempty : front≠[]) (targetPositive : 0<n)
    (program : Dispatch p d front out final) (path : Prefix q front u)
    (source : (n:Int)=(3:Int)^p*q+d) (cert : Certificate u tail)
    (capture : (3:Int)^out*u+final≤2*((2:Int)^(boost e front)*u)+1)
    (ih : CollatzGapComparison.Hyp Interval (grades e (front++tail))) : Basin n := by
  have endpoint := dispatch_transport program path source
  have height : iterate n (CollatzWitness.total front)≤2*(2^(boost e front)*u)+1 := by
    have cast : ((2*(2^(boost e front)*u)+1:Nat):Int)=
        2*((2:Int)^(boost e front)*u)+1 := by
      simp
    rw [← endpoint,← cast] at capture
    omega
  have endpointPositive := iterate_positive targetPositive (CollatzWitness.total front)
  have child := ih (2^(boost e front)*u) (iterate n (CollatzWitness.total front))
    (boost e front) tail ⟨endpointPositive,height⟩ ⟨u,rfl,cert⟩
    (boosted_prefix_rank e front tail positive nonempty)
  exact (iterate_basin n (CollatzWitness.total front)).mp child

/-- A purely coefficient-based sufficient capture criterion for every signed
state. The source-dependent full inequality can be weaker and remains
available in dispatch_interval_rule. -/
theorem coefficient_paid_interval_rule {p out e q u n : Nat} {d final : Int}
    {front tail : List Nat}
    (positive : 1≤e) (nonempty : front≠[]) (targetPositive : 0<n)
    (program : Dispatch p d front out final) (path : Prefix q front u)
    (source : (n:Int)=(3:Int)^p*q+d) (cert : Certificate u tail) (negative : d<0)
    (paid : (3:Nat)^out≤2*2^(boost e front))
    (ih : CollatzGapComparison.Hyp Interval (grades e (front++tail))) : Basin n := by
  apply dispatch_interval_rule positive nonempty targetPositive program path source cert _ ih
  have last := dispatch_negative program negative
  have lifted : (((3:Nat)^out:Nat):Int)≤((2*2^(boost e front):Nat):Int) := by omega
  have power : (3:Int)^out≤2*(2:Int)^(boost e front) := by simpa using lifted
  have scaled := Int.mul_le_mul_of_nonneg_right power (Int.natCast_nonneg u)
  have form : (2*(2:Int)^(boost e front))*(u:Int)=
      2*((2:Int)^(boost e front)*u) := by grind
  rw [form] at scaled
  omega

/-- Any dispatched affine state can continue at its own physical clock and
meet a paid partner at an independent clock. Only the source prefix is
charged to the complete certificate rank; no equality of the two clocks
or convergence of an arbitrary terminal debt is assumed. -/
theorem dispatch_merger_interval_rule {p out e q u n endpoint partner L R : Nat}
    {d final : Int} {front tail : List Nat}
    (positive : 1≤e) (nonempty : front≠[])
    (program : Dispatch p d front out final) (path : Prefix q front u)
    (source : (n:Int)=(3:Int)^p*q+d) (cert : Certificate u tail)
    (pin : (endpoint:Int)=(3:Int)^out*u+final)
    (partnerPositive : 0<partner) (paid : partner≤2*(2^(boost e front)*u)+1)
    (meeting : iterate partner L=iterate endpoint R)
    (ih : CollatzGapComparison.Hyp Interval (grades e (front++tail))) : Basin n := by
  have transport := dispatch_transport program path source
  have actual : iterate n (CollatzWitness.total front)=endpoint := by omega
  have child := ih (2^(boost e front)*u) partner (boost e front) tail
    ⟨partnerPositive,paid⟩ ⟨u,rfl,cert⟩
    (boosted_prefix_rank e front tail positive nonempty)
  have met := (iterate_basin partner L).mpr child
  rw [meeting] at met
  have known := (iterate_basin endpoint R).mp met
  rw [← actual] at known
  exact (iterate_basin n (CollatzWitness.total front)).mp known

/-- Degree-zero termination is always a successful interval handoff when the
offset began negative and a nonempty source prefix has been consumed. -/
theorem zero_degree_interval_rule {p e q u n : Nat} {d final : Int}
    {front tail : List Nat}
    (positive : 1≤e) (nonempty : front≠[]) (targetPositive : 0<n)
    (program : Dispatch p d front 0 final) (path : Prefix q front u)
    (source : (n:Int)=(3:Int)^p*q+d) (cert : Certificate u tail) (negative : d<0)
    (ih : CollatzGapComparison.Hyp Interval (grades e (front++tail))) : Basin n := by
  apply dispatch_interval_rule positive nonempty targetPositive program path source cert _ ih
  have last := dispatch_negative program negative
  have power : 1≤(2:Int)^(boost e front) := by
    have h : 1≤(2:Nat)^(boost e front) := Nat.one_le_pow _ _ (by decide)
    have lifted : (1:Int)≤((2:Nat)^(boost e front):Int) := by omega
    simpa using lifted
  have upos : 0≤(u:Int) := Int.natCast_nonneg _
  have scaled : (u:Int)≤(2:Int)^(boost e front)*u := by
    simpa using Int.mul_le_mul_of_nonneg_right power upos
  simp only [Int.pow_zero,Int.one_mul]
  omega

/-- Every low-interval target admits the same degree-three negative-offset
initialization. Source identity and offset are retained exactly. -/
theorem low_target_initialization {q n : Nat} (positive : 0<q) (bound : n≤16*q+1) :
    (n:Int)=(3:Int)^3*q+((n:Int)-27*q) ∧ (n:Int)-27*q<0 := by
  change (n:Int)=27*q+((n:Int)-27*q) ∧ (n:Int)-27*q<0
  omega

/-- The previously unsupported small-language edge D2 followed by gap one
has a regular state in the total dispatcher; this does not itself assert
that every later state eventually captures. -/
theorem debt_two_gap_one : Dispatch 2 (-1) [1] 1 (-2) := by
  have path : SignedPath ((-1:Int)-(3:Int)^1) 1 0 (-2) := by
    apply SignedPath.even (by decide)
    change SignedPath (-2) 0 0 (-2)
    exact SignedPath.done (-2)
  exact Dispatch.step path (Dispatch.done 1 (-2))

end CollatzAffineDispatcher
