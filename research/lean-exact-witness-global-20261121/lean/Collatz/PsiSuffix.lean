/-
Complete supplied-certificate descent for arbitrary leading gap-two runs,
followed by (1, two^k, a), a >= 3. The result is a direct reverse-power-of-three
comparison on the literal suffix, with one common source rank.

The asymmetric psi reset composes with this theorem to a reverse-nine query
and an explicit smaller ordinary component partner. No full cover is asserted.
-/
import Collatz.AsymmetricPsiReset

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzHighGapPump CollatzLowGapLoops

set_option autoImplicit false
set_option maxHeartbeats 4000000

namespace CollatzPsiSuffix

def program (j k a : Nat) : List Nat :=
  repeatHead 2 j (1 :: repeatHead 2 k [a])

theorem repeatHead_append (a k : Nat) (front tail : List Nat) :
    repeatHead a k front ++ tail = repeatHead a k (front ++ tail) := by
  induction k with
  | zero => rfl
  | succ k ih => simp [repeatHead,ih]

theorem repeatHead_member (a k b : Nat) (tail : List Nat) (mem : b ∈ tail) :
    b ∈ repeatHead a k tail := by
  induction k with
  | zero => exact mem
  | succ k ih => exact List.mem_cons_of_mem a ih

theorem program_append (j k a : Nat) (tail : List Nat) :
    program j k a ++ tail = repeatHead 2 j (1 :: repeatHead 2 k (a::tail)) := by
  simp only [program,repeatHead_append,List.cons_append,List.nil_append]

theorem program_rank (j k a : Nat) (tail : List Nat) (high : 3 ≤ a) :
    Less (grades 0 ((a-2)::tail)) (grades 0 (program j k a ++ tail)) := by
  have member : a ∈ program j k a :=
    repeatHead_member 2 j a _ (List.mem_cons_of_mem 1
      (repeatHead_member 2 k a [a] (by simp)))
  have mapped : 2*a ∈ (program j k a).map (2*·) := List.mem_map.mpr ⟨a,member,rfl⟩
  have nonempty : (program j k a).map (2*·) ≠ [] := by
    intro eq
    rw [eq] at mapped
    simp at mapped
  have short : Less [2*(a-2)] ((program j k a).map (2*·)) := by
    apply replace_many _ _ nonempty
    intro b hb
    have eq : b = 2*(a-2) := by simpa using hb
    exact ⟨2*a,mapped,by omega⟩
  have drop := (less_append_right_iff [2*(a-2)] ((program j k a).map (2*·))
    (tail.map (2*·))).mpr short
  simpa [grades,List.map_append] using drop

/-- A supplied gap-two run commutes with psi. The exact shifted affine
identity is retained so subsequent target and source splices can be composed. -/
theorem twos_data (j n : Nat) (tail : List Nat)
    (cert : Certificate n (repeatHead 2 j tail)) :
    ∃ u, Certificate u tail ∧
      3^j*(n-1) = 4^j*(u-1) ∧
      (Basin (2*n-1) ↔ Basin (2*u-1)) := by
  induction j generalizing n with
  | zero => exact ⟨n,cert,by simp,Iff.rfl⟩
  | succ j ih =>
    obtain ⟨_,v,step,rest⟩ := (certificate_cons_iff n 2 (repeatHead 2 j tail)).mp cert
    obtain ⟨u,child,shift,merge⟩ := ih v rest
    have nodd := witness_odd (certificate_witness cert)
    have vodd := witness_odd (certificate_witness rest)
    have small : 3*(n-1) = 4*(v-1) := by omega
    have scaled := congrArg (fun x : Nat => 3^j*x) small
    have equation : 3^(j+1)*(n-1) = 4^(j+1)*(u-1) := by
      rw [Nat.pow_succ,Nat.pow_succ]
      grind
    have target : 3*n-1 = 2*(2*v-1) := by omega
    have link : Basin (2*n-1) ↔ Basin (2*v-1) := by
      have h := basin_psi n (by omega)
      rw [target] at h
      exact h.trans (basin_twice _)
    exact ⟨u,child,equation,link.trans merge⟩

/-- The entire unbounded gap-two run forces the power-of-three divisibility;
it is not an extra guard on the supplied certificate. -/
theorem twos_before_high (k a n : Nat) (tail : List Nat)
    (cert : Certificate n (repeatHead 2 k (a::tail))) (high : 3 ≤ a) :
    ∃ t, n = 4^(k+1)*t+1 ∧ Certificate (3^k*t) ((a-2)::tail) := by
  induction k generalizing n with
  | zero =>
    obtain ⟨_,q,step,tailCert⟩ := (certificate_cons_iff n a tail).mp cert
    have power : 2^a = 4*2^(a-2) := by
      calc
        2^a = 2^(2+(a-2)) := by congr 1; omega
        _ = 2^2*2^(a-2) := Nat.pow_add 2 2 (a-2)
        _ = _ := rfl
    have form : 3*n+1 = 4*(2^(a-2)*q) := by rw [power] at step; grind
    let t := n/4
    have parent : n = 4*t+1 := by dsimp [t]; omega
    have childEq : 3*t+1 = 2^(a-2)*q := by rw [parent] at form; omega
    have child : Certificate t ((a-2)::tail) :=
      (certificate_cons_iff t (a-2) tail).mpr ⟨by omega,q,childEq,tailCert⟩
    exact ⟨t,by simpa using parent,by simpa using child⟩
  | succ k ih =>
    obtain ⟨_,u,first,rest⟩ :=
      (certificate_cons_iff n 2 (repeatHead 2 k (a::tail))).mp cert
    obtain ⟨t,parent,child⟩ := ih u rest
    rw [parent] at first
    have modular := congrArg (fun x : Nat => x % 3) first
    have residue : t % 3 = 0 := by
      simp [Nat.add_mod,Nat.mul_mod,four_pow_mod_three] at modular
      omega
    obtain ⟨s,ts⟩ := Nat.dvd_of_mod_eq_zero residue
    rw [ts] at first child
    have source : n = 4^((k+1)+1)*s+1 := by
      rw [Nat.pow_succ 4 (k+1)]
      grind
    have equation : 3^k*(3*s) = 3^(k+1)*s := by rw [Nat.pow_succ]; grind
    rw [equation] at child
    exact ⟨s,source,child⟩

/-- The known source's literal suffix supplies the reverse-3^k child.
Both leading runs are arbitrary; there is no congruence or clock cutoff. -/
theorem whole_witness_handoff (n j k a : Nat) (tail : List Nat)
    (cert : Certificate n (program j k a ++ tail)) (high : 3 ≤ a) :
    ∃ t, 0<t ∧ Certificate (3^k*t) ((a-2)::tail) ∧
      Less (grades 0 ((a-2)::tail)) (grades 0 (program j k a ++ tail)) ∧
      (Basin (2*n-1) ↔ Basin t) ∧
      3^(j+1)*n + 2*4^j = 3^(j+1) + 2*4^(j+k+1)*t := by
  have normalized := cert
  rw [program_append] at normalized
  obtain ⟨u,core,shift,leading⟩ := twos_data j n _ normalized
  obtain ⟨_,v,first,rest⟩ :=
    (certificate_cons_iff u 1 (repeatHead 2 k (a::tail))).mp core
  obtain ⟨t,veq,child⟩ := twos_before_high k a v tail rest high
  have childodd := witness_odd (certificate_witness child)
  have tpos : 0<t := by
    by_cases zero : t=0
    · simp [zero] at childodd
    · omega
  have nodd := witness_odd (certificate_witness cert)
  have uodd := witness_odd (certificate_witness core)
  have equation : 3*u-1 = 2*(4^(k+1)*t) := by rw [veq] at first; omega
  have target : Basin (2*u-1) ↔ Basin t := by
    have link := basin_psi u (by omega)
    rw [equation] at link
    have four : Basin (4^(k+1)*t) ↔ Basin t := by
      simpa [Nat.pow_mul] using basin_pow_two (2*(k+1)) t
    exact link.trans ((basin_twice _).trans four)
  refine ⟨t,tpos,child,program_rank j k a tail high,leading.trans target,?_⟩
  have nshift : 3^j*n = 3^j*(n-1)+3^j := by
    have h : n=(n-1)+1 := by omega
    simpa [Nat.mul_add] using congrArg (fun x : Nat => 3^j*x) h
  have ushift : 4^j*u = 4^j*(u-1)+4^j := by
    have h : u=(u-1)+1 := by omega
    simpa [Nat.mul_add] using congrArg (fun x : Nat => 4^j*x) h
  have linear : 3^j*n + 4^j = 4^j*u + 3^j := by omega
  have scale := congrArg (fun x : Nat => 3*x) linear
  have endpoint : 3*u = 2*4^(k+1)*t+1 := by rw [veq] at first; grind
  have p4 : 4^(j+k+1) = 4^j*4^(k+1) := by
    rw [show j+k+1=j+(k+1) by omega,Nat.pow_add]
  rw [Nat.pow_succ,p4]
  grind

/-- The k=0 sublanguage closes outright on the complete supplied certificate. -/
theorem closes_without_twos (n j a : Nat) (tail : List Nat)
    (cert : Certificate n (program j 0 a ++ tail)) (high : 3 ≤ a) :
    Basin (2*n-1) := by
  obtain ⟨t,_,child,_,merge,_⟩ := whole_witness_handoff n j 0 a tail cert high
  have known : Basin t := by
    simpa using witness_basin (certificate_witness child)
  exact merge.mpr known

def asymmetricTail (e : Nat) : List Nat := [1,3,2,1,2,3,2,3,e-1]

theorem asymmetric_source (e j : Nat) :
    CollatzAsymmetricPsiReset.source e j = program j 2 3 ++ asymmetricTail e := by
  induction j with
  | zero => rfl
  | succ j ih =>
    simpa [CollatzAsymmetricPsiReset.source,program,repeatHead] using
      congrArg (List.cons 2) ih

/-- Compose the previously proved arbitrary-length reset with the full suffix
handoff. Its only recursive demand is reverse nine, with a literal inherited
tail and a strict decrease from the ORIGINAL parent certificate. In addition,
the wanted child is an explicit smaller ordinary component representative. -/
theorem asymmetric_to_reverse_nine (e j S m : Nat) (tail : List Nat)
    (cert : PoweredCertificate S e tail) (high : 3 ≤ e)
    (guard : CollatzAsymmetricPsiReset.Guard j S m) :
    ∃ t, 0<t ∧ 531441*t+578545 = 131072*S ∧ t<S ∧
      Certificate (9*t) ((1::asymmetricTail e) ++ tail) ∧
      Less (grades 0 ((1::asymmetricTail e) ++ tail)) (grades e tail) ∧
      (Basin (2*S-1) ↔ Basin t) := by
  obtain ⟨child,drop,merge⟩ :=
    CollatzAsymmetricPsiReset.whole_witness_reset e j S m tail cert high guard
  obtain ⟨q,mq,childCert⟩ := child
  have eq : m=q := by simpa using mq
  rw [← eq] at childCert
  rw [asymmetric_source,List.append_assoc] at childCert drop
  obtain ⟨t,tpos,lower,lowerDrop,target,polynomial⟩ :=
    whole_witness_handoff m j 2 3 (asymmetricTail e ++ tail) childCert (by decide)
  have power3 : 3^(j+13) = 531441*3^(j+1) := by
    rw [show j+13=(j+1)+12 by omega,Nat.pow_add]
    grind
  have power4 : 4^(j+2+1) = 64*4^j := by
    rw [show j+2+1=j+3 by omega,Nat.pow_add]
    grind
  unfold CollatzAsymmetricPsiReset.Guard at guard
  rw [power3] at guard
  rw [power4] at polynomial
  simp only [Nat.mul_assoc] at polynomial guard
  have linear : 531441*(4^j*t)+578545*4^j = 131072*(4^j*S) := by omega
  have factor : 4^j*(531441*t+578545) = 4^j*(131072*S) := by
    calc
      4^j*(531441*t+578545) = 531441*(4^j*t)+578545*4^j := by
        simp [Nat.mul_add,Nat.mul_left_comm,Nat.mul_comm,Nat.mul_assoc]
      _ = 131072*(4^j*S) := linear
      _ = 4^j*(131072*S) := by rw [Nat.mul_left_comm]
  have equation : 531441*t+578545 = 131072*S :=
    Nat.eq_of_mul_eq_mul_left (Nat.pow_pos (by decide)) factor
  refine ⟨t,tpos,equation,by omega,?_,?_,merge.symm.trans target⟩
  · simpa using lower
  · simpa using less_trans lowerDrop drop

def asymmetricExit : List Nat := repeatHead 1 10 [2,2,3]

/-- This merger identity also stands independently of a convergence witness.
The exact linear equation is a ternary progression, not a universal selector. -/
theorem asymmetric_small_partner (S t : Nat) (positive : 0<t)
    (equation : 531441*t+578545 = 131072*S) :
    t<S ∧ t<2*S-1 ∧ Prefix t asymmetricExit (3*S-1) ∧
      (Basin (2*S-1) ↔ Basin t) := by
  have small : t<S := by omega
  have path : Prefix t asymmetricExit (3*S-1) := by
    constructor
    · simp [asymmetricExit,repeatHead,PositiveGaps]
    · simp only [asymmetricExit,repeatHead,correction,total,List.length_cons,
        List.length_nil]
      omega
  exact ⟨small,by omega,path,
    (basin_psi S (by omega)).trans (prefix_basin path).symm⟩

end CollatzPsiSuffix
