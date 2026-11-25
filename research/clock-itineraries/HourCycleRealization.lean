module

public import HourEscapeCylinders
import all FixedGate
import all SynchronousShadow

public section
namespace Collatz.Itinerary.HourCycleRealization

open Sparse FixedGate
set_option autoImplicit false

/-- Coefficient of the common even translation at the indexed odd phase. -/
def coefficient (es : List Nat) (i : Nat) : Nat := 3^i*2^(es.drop i).sum

theorem phase_translation {es : List Nat} {x q : Nat} (p : Path es x q)
    (i d : Nat) (hi : i≤es.length) :
    after i (x+2*(2^es.sum*d))=after i x+2*(coefficient es i*d) := by
  induction p generalizing i d with
  | nil =>
    obtain rfl : i=0 := by simpa using hi
    simp [after,coefficient]
  | @cons x y q e es edge _ ih =>
    cases i with
    | zero => simp [after,coefficient]
    | succ i =>
      have b : i≤es.length := by simpa using hi
      have translated := Shadow.gap_translate edge (2^es.sum*d)
      have aligned : x+2*(2^(e::es).sum*d)=x+2*(2^e*(2^es.sum*d)) := by
        simp only [List.sum_cons,Nat.pow_add,Nat.mul_assoc]
      rw [aligned,after,gap_next translated,after,gap_next edge]
      have t := ih i (3*d) b
      simpa only [coefficient,List.drop_succ_cons,Nat.pow_succ,Nat.mul_comm,
        Nat.mul_left_comm,Nat.mul_assoc] using t

private theorem bound_prefix (f : Nat → Nat) (L : Nat) : ∃ M, ∀ i, i≤L → f i≤M := by
  induction L with
  | zero =>
    refine ⟨f 0,fun i hi => ?_⟩
    obtain rfl : i=0 := by omega
    omega
  | succ L ih =>
    obtain ⟨M,all⟩ := ih
    exact ⟨max M (f (L+1)),fun i hi => by
      by_cases small : i≤L
      · exact Nat.le_trans (all i small) (Nat.le_max_left ..)
      · obtain rfl : i=L+1 := by omega
        exact Nat.le_max_right ..⟩

/-- Every finite script whose homogeneous phases have a strict minimum
at k within one octave occurs at arbitrarily large ordinary height, still
with that minimum and octave, followed in one more odd step by t. -/
theorem octave_to_target (es : List Nat) (positive : ∀ e∈es, 0<e)
    (k : Nat) (inside : k≤es.length)
    (low : ∀ i, i≤es.length → i≠k → coefficient es k<coefficient es i)
    (high : ∀ i, i≤es.length → coefficient es i<2*coefficient es k)
    (t H : Nat) (odd : t%2=1) (unit : t%3≠0) :
    ∃ a q e, Path es a q ∧ Gap e q t ∧ H<after k a ∧
      (∀ i, i≤es.length → i≠k → after k a<after i a) ∧
      ∀ i, i≤es.length → after i a<2*after k a := by
  obtain ⟨x,q,_,qo,p⟩ := HourEscape.realize_positive_word es positive
  obtain ⟨M,cap⟩ := bound_prefix (fun i => after i x) es.length
  let u := H+M+1
  let z := q+2*(3^es.length*u)
  have zo : z%2=1 := by dsimp [z]; omega
  obtain ⟨e,v,_,_,edge⟩ := Shadow.one_gap_cylinder zo odd unit es.length
  let D := u+v
  let a := x+2*(2^es.sum*D)
  have endEq : z+2*(3^es.length*v)=q+2*(3^es.length*D) := by
    simp only [z,D,Nat.mul_add]; omega
  rw [endEq] at edge
  have witness := Shadow.translate p D
  have phase (i : Nat) (hi : i≤es.length) :
      after i a=after i x+2*(coefficient es i*D) := phase_translation p i D hi
  have large : H+M<D := by dsimp [D,u]; omega
  have cp : 0<coefficient es k := Nat.mul_pos (Nat.pow_pos (by decide)) (Nat.two_pow_pos _)
  have gain := Nat.mul_le_mul_right D (show 1≤coefficient es k from cp)
  simp only [Nat.one_mul] at gain
  refine ⟨a,_,e,witness,edge,?_,?_,?_⟩
  · rw [phase k inside]; omega
  · intro i hi diff
    rw [phase k inside,phase i hi]
    have margin := Nat.mul_le_mul_right D (low i hi diff)
    rw [Nat.succ_mul] at margin
    have bound := cap k inside
    omega
  · intro i hi
    rw [phase k inside,phase i hi]
    have margin := Nat.mul_le_mul_right D (high i hi)
    rw [Nat.succ_mul,Nat.mul_assoc] at margin
    have bound := cap i hi
    omega

private def down (n : Nat) : Nat := (3^n).log2
private def up (n : Nat) : Nat := if n=0 then 0 else down n+1

private theorem down_step (n : Nat) : down n+1≤down (n+1) ∧ down (n+1)≤down n+2 := by
  have p : 3^(n+1)≠0 := Nat.ne_of_gt (Nat.pow_pos (by decide))
  have lo := Nat.log2_self_le (Nat.ne_of_gt (Nat.pow_pos (n:=n) (by decide : 0<3)))
  have hi := Nat.lt_log2_self (n:=3^n)
  change 2^(down n)≤3^n at lo
  change 3^n<2^(down n+1) at hi
  constructor
  · apply (Nat.le_log2 p).2
    rw [Nat.pow_succ,Nat.pow_succ]
    omega
  · have bound : down (n+1)<down n+3 := by
      apply (Nat.log2_lt p).2
      rw [Nat.pow_succ 3,show down n+3=(down n+1)+2 by omega,Nat.pow_add]
      change 3^n*3<2^(down n+1)*4
      omega
    omega

private theorem up_step (n : Nat) : up n+1≤up (n+1) ∧ up (n+1)≤up n+2 := by
  cases n with
  | zero => decide
  | succ n => have h := down_step (n+1); simp only [up,Nat.add_one_ne_zero,ite_false]; omega

private theorem down_mono {i n : Nat} (h : i≤n) : down i≤down n := by
  induction n with
  | zero =>
    obtain rfl : i=0 := by omega
    exact Nat.le_refl _
  | succ n ih =>
    by_cases hi : i≤n
    · have a := ih hi; have b := down_step n; omega
    · obtain rfl : i=n+1 := by omega
      exact Nat.le_refl _

private theorem separated {n : Nat} (pos : 0<n) :
    2^(down n)<3^n ∧ 3^n<2^(up n) ∧ 2^(up n)<2*3^n := by
  have lo := Nat.log2_self_le (Nat.ne_of_gt (Nat.pow_pos (n:=n) (by decide : 0<3)))
  have hi := Nat.lt_log2_self (n:=3^n)
  change 2^(down n)≤3^n at lo
  change 3^n<2^(down n+1) at hi
  have neq : 2^(down n)≠3^n := by
    have unit (j : Nat) : 2^j%3≠0 := by
      induction j with
      | zero => decide
      | succ j ih => rw [Nat.pow_succ]; omega
    obtain ⟨j,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : n≠0)
    intro eqn
    have u := unit (down (j+1))
    rw [eqn,Nat.pow_succ] at u
    omega
  have strict := Nat.lt_of_le_of_ne lo neq
  simp only [up,ite_eq_right (by omega : n≠0)]
  refine ⟨strict,hi,?_⟩
  rw [Nat.pow_succ]; omega

/-- Remaining physical clock at each position of the symmetric mechanical window. -/
private def remaining (n j : Nat) : Nat :=
  if j<n then down n+up (n-j) else down n-down (j-n)

private theorem remaining_left {j n : Nat} (h : j≤n) :
    remaining n j=down n+up (n-j) := by
  by_cases lt : j<n
  · simp [remaining,lt]
  · obtain rfl : j=n := by omega
    simp [remaining,up,down,show Nat.log2 1=0 by decide]

private theorem remaining_right {j n : Nat} (h : n≤j) :
    remaining n j=down n-down (j-n) := by simp [remaining,show ¬j<n by omega]

private theorem remaining_step {j n : Nat} (h : j<2*n) :
    remaining n (j+1)+1≤remaining n j ∧ remaining n j≤remaining n (j+1)+2 := by
  by_cases before : j<n
  · rw [remaining_left (by omega),remaining_left (by omega : j≤n),
      show n-j=(n-(j+1))+1 by omega]
    have bound := up_step (n-(j+1))
    omega
  · rw [remaining_right (by omega),remaining_right (by omega : n≤j),
      show j+1-n=(j-n)+1 by omega]
    have bound := down_step (j-n)
    have fits := down_mono (show (j-n)+1≤n by omega)
    omega

private def differences (r : Nat → Nat) (a : Nat) : Nat → List Nat
  | 0 => []
  | l+1 => (r a-r (a+1))::differences r (a+1) l

private theorem differences_length (r : Nat → Nat) (l a : Nat) :
    (differences r a l).length=l := by
  induction l generalizing a with
  | zero => rfl
  | succ l ih => simp [differences,ih]

private theorem differences_gaps (r : Nat → Nat) (l a : Nat)
    (step : ∀ j, a≤j → j<a+l → r (j+1)+1≤r j ∧ r j≤r (j+1)+2) :
    ∀ e∈differences r a l, e=1 ∨ e=2 := by
  induction l generalizing a with
  | zero => simp [differences]
  | succ l ih =>
    simp only [differences,List.mem_cons]
    intro e member
    rcases member with eqn|tail
    · have h := step a (by omega) (by omega); omega
    · exact ih (a+1) (fun j hj h' => step j (by omega) (by omega)) e tail

private theorem differences_drop (r : Nat → Nat) (l a i : Nat) (size : i≤l)
    (mono : ∀ j, a≤j → j<a+l → r (j+1)≤r j) :
    ((differences r a l).drop i).sum+r (a+l)=r (a+i) := by
  induction l generalizing a i with
  | zero =>
    obtain rfl : i=0 := by omega
    simp [differences]
  | succ l ih =>
    have use (k : Nat) (hk : k≤l) := ih (a+1) k hk (fun j jl jh => mono j (by omega) (by omega))
    have fin : (a+1)+l=a+(l+1) := by omega
    cases i with
    | zero =>
      have rest := use 0 (by omega)
      simp only [Nat.add_zero,fin,List.drop_zero] at rest
      have start := mono a (by omega) (by omega)
      simp only [differences,List.drop_zero,List.sum_cons,Nat.add_zero]
      omega
    | succ i =>
      have rest := use i (by omega)
      simpa only [differences,List.drop_succ_cons,fin,show (a+1)+i=a+(i+1) by omega] using rest

def centeredWord (n : Nat) : List Nat := differences (remaining n) 0 (2*n)

private theorem centered_sum (n i : Nat) (hi : i≤2*n) :
    ((centeredWord n).drop i).sum=remaining n i := by
  have endR : remaining n (2*n)=0 := by
    rw [remaining_right (by omega),show 2*n-n=n by omega,Nat.sub_self]
  have h := differences_drop (remaining n) (2*n) 0 i hi (fun j _ hj => by
    have b := remaining_step (n:=n) (j:=j) (by omega); omega)
  simpa only [centeredWord,Nat.zero_add,endR,Nat.add_zero] using h

private theorem center_coefficient (n : Nat) :
    coefficient (centeredWord n) n=3^n*2^(down n) := by
  simp only [coefficient,centered_sum n n (by omega),remaining_right (Nat.le_refl n),Nat.sub_self]
  have zero : down 0=0 := by decide
  rw [zero,Nat.sub_zero]

private theorem center_bounds {n i : Nat} (hi : i≤2*n) (ne : i≠n) :
    coefficient (centeredWord n) n<coefficient (centeredWord n) i ∧
    coefficient (centeredWord n) i<2*coefficient (centeredWord n) n := by
  rw [center_coefficient,coefficient,centered_sum n i hi]
  by_cases left : i<n
  · let j := n-i
    have sep := separated (n:=j) (by dsimp [j]; omega)
    rw [remaining_left (by omega),Nat.pow_add]
    have N : 3^n=3^i*3^j := by rw [←Nat.pow_add,show i+j=n by dsimp [j]; omega]
    rw [N]
    change (3^i*3^j)*2^(down n)<3^i*(2^(down n)*2^(up j)) ∧
      3^i*(2^(down n)*2^(up j))<2*((3^i*3^j)*2^(down n))
    have pos := Nat.mul_pos (Nat.pow_pos (n:=i) (by decide : 0<3)) (Nat.two_pow_pos (down n))
    exact ⟨by simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using
      Nat.mul_lt_mul_of_pos_left sep.2.1 pos,by
      simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using
      Nat.mul_lt_mul_of_pos_left sep.2.2 pos⟩
  · let j := i-n
    have sep := separated (n:=j) (by dsimp [j]; omega)
    rw [remaining_right (by omega)]
    have F := down_mono (n:=n) (i:=j) (by dsimp [j]; omega)
    have pow2 : 2^(down n)=2^(down n-down j)*2^(down j) := by
      rw [←Nat.pow_add,show down n-down j+down j=down n by omega]
    have pow3 : 3^i=3^n*3^j := by rw [←Nat.pow_add,show n+j=i by dsimp [j]; omega]
    rw [pow2,pow3]
    have pos := Nat.mul_pos (Nat.pow_pos (n:=n) (by decide : 0<3)) (Nat.two_pow_pos (down n-down j))
    have hi' : 3^j<2*2^(down j) := by
      have h := sep.2.1
      rw [up,ite_eq_right (by dsimp [j]; omega),Nat.pow_succ] at h
      omega
    exact ⟨by simpa only [j,Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using
      Nat.mul_lt_mul_of_pos_left sep.1 pos,by
      simpa only [j,Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using
      Nat.mul_lt_mul_of_pos_left hi' pos⟩

/-- Every radius admits arbitrarily high ordinary one-octave windows
with a strict central minimum, all gaps one or two, and any chosen
ordinary unit as the very next odd value. -/
theorem centered_octave_to_target (n H t : Nat) (odd : t%2=1) (unit : t%3≠0) :
    let es := centeredWord n
    es.length=2*n ∧ (∀ e∈es, e=1 ∨ e=2) ∧
    ∃ a q e, Path es a q ∧ Gap e q t ∧ H<after n a ∧
      (∀ i, i≤2*n → i≠n → after n a<after i a) ∧
      ∀ i, i≤2*n → after i a<2*after n a := by
  have len := differences_length (remaining n) (2*n) 0
  change (centeredWord n).length=2*n at len
  have bin := differences_gaps (remaining n) (2*n) 0 (fun j _ hj => remaining_step (by omega))
  refine ⟨len,bin,?_⟩
  obtain ⟨a,q,e,path,edge,big,low,high⟩ := octave_to_target (centeredWord n)
    (fun e he => by have h := bin e he; omega) n (by omega)
    (fun i hi ne => (center_bounds (by omega) ne).1)
    (fun i hi => by
      by_cases eqn : i=n
      · subst i
        rw [center_coefficient]
        have p : 0<3^n*2^(down n) := Nat.mul_pos (Nat.pow_pos (by decide)) (Nat.two_pow_pos _)
        omega
      · exact (center_bounds (by omega) eqn).2) t H odd unit
  exact ⟨a,q,e,path,edge,big,fun i hi ne => low i (by omega) ne,fun i hi => high i (by omega)⟩

#print axioms phase_translation
#print axioms centered_octave_to_target
#print axioms octave_to_target
end Collatz.Itinerary.HourCycleRealization
