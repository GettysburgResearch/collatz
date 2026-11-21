/-
Two unbounded low-gap loops and their exact whole-witness reduction.
The source suffix is preserved verbatim. The remaining F3 query is explicit;
this file does not assert a complete dispatcher.
-/
import Collatz.HighGapPump

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzHighGapPump CollatzDirected CollatzSourceWitness

namespace CollatzLowGapLoops

def repeatHead (a : Nat) : Nat → List Nat → List Nat
  | 0, tail => tail
  | k+1, tail => a :: repeatHead a k tail

theorem repeatHead_length (a k : Nat) (tail : List Nat) :
    (repeatHead a k tail).length = k + tail.length := by
  induction k with
  | zero => simp [repeatHead]
  | succ k ih => simp only [repeatHead,List.length_cons,ih]; omega

theorem repeatHead_total (a k : Nat) (tail : List Nat) :
    total (repeatHead a k tail) = a*k + total tail := by
  induction k with
  | zero => simp [repeatHead]
  | succ k ih => simp only [repeatHead,total,ih]; grind

theorem repeatHead_positive (a k : Nat) (tail : List Nat)
    (ha : 0<a) (ht : PositiveGaps tail) : PositiveGaps (repeatHead a k tail) := by
  induction k with
  | zero => exact ht
  | succ k ih =>
    intro b hb
    rcases List.mem_cons.mp hb with eq | mem
    · omega
    · exact ih b mem

theorem ones_correction (k b : Nat) :
    correction (repeatHead 1 k [b]) + 2^(k+1) = 3^(k+1) := by
  induction k with
  | zero => simp [repeatHead,correction]
  | succ k ih =>
    simp only [repeatHead,correction,repeatHead_length,List.length_cons,List.length_nil,
      Nat.zero_add]
    rw [show k+1+1 = (k+1)+1 by omega,Nat.pow_succ 2 (k+1),Nat.pow_succ 3 (k+1)]
    omega

def source (k ell : Nat) : List Nat :=
  repeatHead 2 k (3 :: repeatHead 1 ell [4])

def targetTail (k ell : Nat) : List Nat :=
  repeatHead 2 k (repeatHead 1 (ell+2) [2])

def target (k ell : Nat) : List Nat := 1 :: targetTail k ell

theorem source_positive (k ell : Nat) : PositiveGaps (source k ell) := by
  apply repeatHead_positive 2 k _ (by decide)
  intro b hb
  rcases List.mem_cons.mp hb with eq | mem
  · omega
  · exact repeatHead_positive 1 ell [4] (by decide)
      (by simp [PositiveGaps]) b mem

theorem target_positive (k ell : Nat) : PositiveGaps (target k ell) := by
  intro b hb
  rcases List.mem_cons.mp hb with eq | mem
  · omega
  · exact repeatHead_positive 2 k _ (by decide)
      (repeatHead_positive 1 (ell+2) [2] (by decide)
        (by simp [PositiveGaps])) b mem

theorem source_stats (k ell : Nat) :
    (source k ell).length = k+ell+2 ∧
      total (source k ell) = 2*k+ell+7 := by
  simp only [source,repeatHead_length,List.length_cons,List.length_nil,
    repeatHead_total,total]
  omega

theorem target_stats (k ell : Nat) :
    (target k ell).length = k+ell+4 ∧
      total (target k ell) = 2*k+ell+5 := by
  simp only [target,targetTail,repeatHead_length,List.length_cons,List.length_nil,
    repeatHead_total,total]
  omega

theorem correction_relation (k ell : Nat) :
    correction (target k ell) = 3*correction (source k ell) + 2^(2*k+ell+5) := by
  induction k with
  | zero =>
    have old := ones_correction ell 4
    have new := ones_correction (ell+3) 2
    have eq : target 0 ell = repeatHead 1 (ell+3) [2] := by
      simp only [target,targetTail,repeatHead]
    have sourceCor : correction (source 0 ell) =
        3^(ell+1)+8*correction (repeatHead 1 ell [4]) := by
      change correction (3 :: repeatHead 1 ell [4]) = _
      rw [correction,repeatHead_length]
      rfl
    rw [eq,sourceCor]
    have p3 : 3^(ell+3+1) = 27*3^(ell+1) := by
      rw [show ell+3+1 = (ell+1)+3 by omega,Nat.pow_add]
      grind
    have p2 : 2^(ell+3+1) = 8*2^(ell+1) := by
      rw [show ell+3+1 = (ell+1)+3 by omega,Nat.pow_add]
      grind
    have p2' : 2^(2*0+ell+5) = 16*2^(ell+1) := by
      rw [show 2*0+ell+5 = (ell+1)+4 by omega,Nat.pow_add]
      grind
    rw [p3,p2] at new
    rw [p2']
    omega
  | succ k ih =>
    have slen := (source_stats k ell).1
    have tlen : (targetTail k ell).length = (source k ell).length+1 := by
      have t := (target_stats k ell).1
      simp only [target,List.length_cons] at t
      omega
    have sourceStep : source (k+1) ell = 2 :: source k ell := rfl
    have targetStep : target (k+1) ell = 1 :: 2 :: targetTail k ell := rfl
    have exp : 3^(targetTail k ell).length = 3*3^(source k ell).length := by
      rw [tlen,Nat.pow_succ]
      grind
    have p2 : 2^(2*(k+1)+ell+5) = 4*2^(2*k+ell+5) := by
      rw [show 2*(k+1)+ell+5 = (2*k+ell+5)+2 by omega,Nat.pow_add]
      grind
    rw [sourceStep,targetStep,correction,correction,correction,List.length_cons,
      Nat.pow_succ 3 (targetTail k ell).length]
    simp only [show 2^1=2 by decide,show 2^2=4 by decide]
    change correction (1 :: targetTail k ell) = _ at ih
    simp only [correction] at ih
    rw [exp] at ih ⊢
    rw [p2]
    omega

/-- Exact prefix identity for any ordinary source divisible by three. Positivity
and every binary division follow from Prefix.prefix_cons_iff; no rational-only
path or unstated residue guard is used. -/
theorem target_prefix (n k ell u : Nat)
    (path : Prefix (3*n) (source k ell) u) :
    Prefix n (target k ell) (12*u+1) := by
  obtain ⟨sl,st⟩ := source_stats k ell
  obtain ⟨tl,tt⟩ := target_stats k ell
  have id := congrArg (fun z => 3*z) path.2
  rw [sl,st] at id
  have p3 : 3^(k+ell+4) = 9*3^(k+ell+2) := by
    rw [show k+ell+4 = (k+ell+2)+2 by omega,Nat.pow_add]
    grind
  have p2 : 2^(2*k+ell+7) = 4*2^(2*k+ell+5) := by
    rw [show 2*k+ell+7 = (2*k+ell+5)+2 by omega,Nat.pow_add]
    grind
  refine ⟨target_positive k ell,?_⟩
  rw [tl,tt,correction_relation,p3]
  rw [p2] at id
  grind

/-- Split an arbitrary supplied complete certificate at its stated word boundary. -/
theorem split_certificate (n : Nat) (front tail : List Nat)
    (cert : Certificate n (front ++ tail)) :
    ∃ u, Prefix n front u ∧ Certificate u tail := by
  induction front generalizing n with
  | nil =>
    refine ⟨n,?_,?_⟩
    · simp [Prefix,PositiveGaps,correction,total]
    · simpa using cert
  | cons a front ih =>
    obtain ⟨ha,m,step,rest⟩ := (certificate_cons_iff n a (front ++ tail)).mp cert
    obtain ⟨u,path,tailCert⟩ := ih m rest
    exact ⟨u,(prefix_cons_iff n a u front).mpr ⟨ha,m,step,path⟩,tailCert⟩

theorem source_nonempty (k ell : Nat) : source k ell ≠ [] := by
  intro eq
  have len := (source_stats k ell).1
  rw [eq] at len
  simp at len

theorem tail_rank (k ell : Nat) (tail : List Nat) :
    Less (grades 0 tail) (grades 0 (source k ell ++ tail)) := by
  have nonempty : (source k ell).map (2*·) ≠ [] := by
    intro empty
    have len := congrArg List.length empty
    simp only [List.length_map,List.length_nil] at len
    have slen := (source_stats k ell).1
    omega
  have lt : Less [] ((source k ell).map (2*·)) :=
    replace_many _ [] nonempty (by intro b hb; simp at hb)
  have full := (less_append_right_iff [] ((source k ell).map (2*·))
    (tail.map (2*·))).mpr lt
  simpa [grades,List.map_append] using full

/-- The two low-letter loops are unbounded. Their entire prefix is consumed,
and the inherited source witness is exactly the original suffix. -/
theorem whole_witness_rewrite (n k ell : Nat) (tail : List Nat)
    (cert : Certificate (3*n) (source k ell ++ tail)) :
    ∃ u, Certificate u tail ∧
      Less (grades 0 tail) (grades 0 (source k ell ++ tail)) ∧
      (Basin n ↔ Basin (3*u)) := by
  obtain ⟨u,path,tailCert⟩ := split_certificate (3*n) (source k ell) tail cert
  have targetPath := target_prefix n k ell u path
  have odd : u%2=1 := witness_odd (certificate_witness tailCert)
  have tripleOdd : (3*u)%2=1 := by omega
  have link : Basin (12*u+1) ↔ Basin (3*u) :=
    (basin_exch (12*u+1) (9*u+1) (3*u) (by omega) (by omega)).trans
      (by
        have h := basin_odd (3*u) tripleOdd
        have eq : 3*(3*u)+1=9*u+1 := by omega
        rwa [eq] at h)
  exact ⟨u,tailCert,tail_rank k ell tail,(prefix_basin targetPath).trans link⟩

/-- This is a concrete reverse-to-forward recursive rule in the common global
multiset induction. Activation of the F3 tail remains an explicit obligation. -/
theorem apply_reverse_rule {active : Active} (n k ell : Nat) (tail : List Nat)
    (cert : Certificate (3*n) (source k ell ++ tail))
    (activated : ∀ u, Certificate u tail → active (.forward 3) u)
    (ih : CollatzGapMultiset.Hyp active (grades 0 (source k ell ++ tail))) : Basin n := by
  obtain ⟨u,tailCert,decrease,merge⟩ := whole_witness_rewrite n k ell tail cert
  have odd : u%2=1 := witness_odd (certificate_witness tailCert)
  have ha : active (.forward 3) (oddCore u) := by
    rw [oddCore_of_odd u odd]
    exact activated u tailCert
  have powered : PoweredCertificate (known (.forward 3) u) 0 tail := by
    refine ⟨u,?_,tailCert⟩
    simp [known]
  have got := ih (.forward 3) u 0 tail (by omega) ha decrease powered
  exact merge.mpr got

end CollatzLowGapLoops
