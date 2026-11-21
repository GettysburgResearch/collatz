/-
An asymmetric, arbitrary-length psi reset on the source residue two modulo three.
The child target takes one more odd step than its paired source prefix and
merges with one forward step of the parent target. All complete source tails
are retained. The affine guard remains an explicit coverage restriction.
-/
import Collatz.GapComparison

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzHighGapPump

set_option autoImplicit false
set_option maxHeartbeats 4000000

namespace CollatzAsymmetricPsiReset

/-- The final actual source gap is e-1; it is never a zero-gap ordinary step. -/
def sourceBase (e : Nat) : List Nat := [1,2,2,3,1,3,2,1,2,3,2,3,e-1]

def source (e : Nat) : Nat → List Nat
  | 0 => sourceBase e
  | j+1 => 2 :: source e j

def targetBase : List Nat := [8,1,1,1,1,1,1,1,1,1,1,2,2,3]

def target : Nat → List Nat
  | 0 => targetBase
  | j+1 => 2 :: target j

theorem source_positive (e j : Nat) (high : 3 ≤ e) : PositiveGaps (source e j) := by
  induction j with
  | zero => simp [PositiveGaps,source,sourceBase]; omega
  | succ j ih =>
    intro a ha
    rcases List.mem_cons.mp ha with eq | mem
    · omega
    · exact ih a mem

theorem source_bound (e j : Nat) (high : 3 ≤ e) : ∀ a ∈ source e j, a ≤ e := by
  induction j with
  | zero =>
    intro a ha
    simp only [source,sourceBase,List.mem_cons,List.not_mem_nil,or_false] at ha
    omega
  | succ j ih =>
    intro a ha
    rcases List.mem_cons.mp ha with eq | mem
    · omega
    · exact ih a mem

theorem source_stats (e j : Nat) :
    (source e j).length = j+13 ∧ total (source e j) = 2*j+25+(e-1) ∧
      correction (source e j) + 3^(j+13) = 75116642*4^j := by
  induction j with
  | zero => simp [source,sourceBase,total,correction]; omega
  | succ j ih =>
    obtain ⟨len,tot,cor⟩ := ih
    refine ⟨by simp [source,len],by simp [source,total,tot]; omega,?_⟩
    simp only [source,correction,len]
    rw [show j+1+13 = (j+13)+1 by omega,Nat.pow_succ 3 (j+13),Nat.pow_succ 4 j]
    omega

theorem target_positive (j : Nat) : PositiveGaps (target j) := by
  induction j with
  | zero => simp [PositiveGaps,target,targetBase]
  | succ j ih =>
    intro a ha
    rcases List.mem_cons.mp ha with eq | mem
    · omega
    · exact ih a mem

theorem target_stats (e j : Nat) :
    (target j).length = j+14 ∧ total (target j) = 2*j+25 ∧
      correction (target j) + 2^(2*j+25) =
        6*correction (source e j) + 3^(j+14) := by
  induction j with
  | zero => simp [source,sourceBase,target,targetBase,correction,total]
  | succ j ih =>
    obtain ⟨len,tot,cor⟩ := ih
    obtain ⟨slen,_,_⟩ := source_stats e j
    refine ⟨by simp [target,len],by simp [target,total,tot]; omega,?_⟩
    simp only [target,source,correction,len,slen]
    rw [show 2*(j+1)+25 = (2*j+25)+2 by omega,Nat.pow_add 2 (2*j+25) 2,
      show j+1+14 = (j+14)+1 by omega,Nat.pow_succ 3 (j+14)]
    have adjacent : 3^(j+14) = 3*3^(j+13) := by
      rw [show j+14=(j+13)+1 by omega,Nat.pow_succ]
      omega
    omega

/-- Pump depth is unrestricted, but integrality is a genuine ternary guard. -/
def Guard (j S m : Nat) : Prop :=
  3^(j+13)*m + 75116642*4^j = 16777216*4^j*S + 3^(j+13)

/-- This is precisely the residue reached by one ordinary odd source step.
The older symmetric reset instead forces the parent residue one. -/
theorem parent_residue (j S m : Nat) (guard : Guard j S m) : S % 3 = 2 := by
  have power : 3^(j+13) % 3 = 0 := by
    rw [Nat.pow_add]
    simp [Nat.mul_mod]
  have modular := congrArg (fun n : Nat => n % 3) guard
  simp [Nat.add_mod,Nat.mul_mod,power,four_pow_mod_three] at modular
  omega

theorem parent_lower_bound (S e : Nat) (tail : List Nat)
    (cert : PoweredCertificate S e tail) (high : 3 ≤ e) : 8 ≤ S := by
  obtain ⟨q,parent,tailCert⟩ := cert
  have odd := witness_odd (certificate_witness tailCert)
  have p : 2^3 ≤ 2^e := Nat.pow_le_pow_right (by decide) high
  have qpos : 1 ≤ q := by omega
  have lower := Nat.mul_le_mul_left (2^e) qpos
  rw [parent]
  omega

theorem source_prefix (e j S m q : Nat) (high : 3 ≤ e)
    (parent : S = 2^e*q) (guard : Guard j S m) : Prefix m (source e j) q := by
  obtain ⟨len,tot,cor⟩ := source_stats e j
  have power : 2^(2*j+25+(e-1)) = 16777216*4^j*2^e := by
    rw [show 2*j+25+(e-1) = (2*j+24)+e by omega,Nat.pow_add,
      Nat.pow_add,Nat.pow_mul]
    grind
  refine ⟨source_positive e j high,?_⟩
  rw [len,tot,power]
  unfold Guard at guard
  rw [parent] at guard
  grind

theorem target_prefix (e j S m : Nat) (guard : Guard j S m)
    (positive : 0 < m) (parent_positive : 0 < S) :
    Prefix (2*m-1) (target j) (3*S-1) := by
  obtain ⟨_,_,cor⟩ := source_stats e j
  obtain ⟨len,tot,tcor⟩ := target_stats e j
  have power : 2^(2*j+25) = 33554432*4^j := by
    rw [Nat.pow_add,Nat.pow_mul]
    grind
  have adjacent : 3^(j+14) = 3*3^(j+13) := by
    rw [show j+14=(j+13)+1 by omega,Nat.pow_succ]
    omega
  have pm : (2*m-1)+1=2*m := by omega
  have pS : (3*S-1)+1=3*S := by omega
  have scale_m := congrArg (fun x => 3^(j+14)*x) pm
  have scale_S := congrArg (fun x => 2^(2*j+25)*x) pS
  unfold Guard at guard
  rw [power] at tcor scale_S
  rw [adjacent] at tcor scale_m
  refine ⟨target_positive j,?_⟩
  rw [len,tot,power,adjacent]
  grind

/-- One even-run grade pays for arbitrarily many source gaps, all at most e.
The source and target prefixes each retain literal, exact ordinary legality. -/
theorem whole_witness_reset (e j S m : Nat) (tail : List Nat)
    (cert : PoweredCertificate S e tail) (high : 3 ≤ e) (guard : Guard j S m) :
    PoweredCertificate m 0 (source e j ++ tail) ∧
      Less (grades 0 (source e j ++ tail)) (grades e tail) ∧
      (Basin (2*m-1) ↔ Basin (2*S-1)) := by
  obtain ⟨q,parent,tailCert⟩ := cert
  have path := source_prefix e j S m q high parent guard
  have childCert := append_certificate path tailCert
  have odd := witness_odd (certificate_witness childCert)
  have qodd := witness_odd (certificate_witness tailCert)
  have parentPositive : 0 < S := by
    rw [parent]
    exact Nat.mul_pos (Nat.pow_pos (by decide)) (by omega)
  have targetPath := target_prefix e j S m guard (by omega) parentPositive
  refine ⟨⟨m,by simp,childCert⟩,
    even_to_odd_replacement e (source e j) tail (by omega) (source_bound e j high),?_⟩
  exact (prefix_basin targetPath).trans (basin_psi S parentPositive).symm

/-- The reset calls the same psi-forward family in the common complete-witness
induction; it does not need a separately activated auxiliary comparison shape. -/
theorem apply_psi_rule {active : CollatzGapComparison.Active}
    (e j S m : Nat) (tail : List Nat)
    (cert : PoweredCertificate S e tail) (high : 3 ≤ e) (guard : Guard j S m)
    (activated : active m (2*m-1))
    (ih : CollatzGapComparison.Hyp active (grades e tail)) : Basin (2*S-1) := by
  obtain ⟨child,drop,merge⟩ := whole_witness_reset e j S m tail cert high guard
  exact CollatzGapComparison.one_query activated child drop merge.mp ih

/-- The strict multiset decrease tolerates arbitrarily large ordinary expansion
whenever the displayed guard is met; no numerical-size bound replaces it. -/
theorem scaled_expansion (j S m k : Nat) (guard : Guard j S m) (large : 8 ≤ S)
    (ratio : k*3^j ≤ 4^j) : k*S < m := by
  by_cases gt : k*S < m
  · exact gt
  have le : m ≤ k*S := by omega
  have pp : 0 < 4^j := Nat.pow_pos (by decide)
  have power : 3^(j+13) = 1594323*3^j := by rw [Nat.pow_add]; grind
  have bound := Nat.mul_le_mul_left (3^(j+13)) le
  have ratio' := Nat.mul_le_mul_right (1594323*S) ratio
  have spos := Nat.mul_le_mul_left (4^j) large
  unfold Guard at guard
  rw [power] at guard bound
  grind

theorem exponential_expansion (c S m : Nat) (guard : Guard (3*c) S m)
    (large : 8 ≤ S) : 2^c*S < m := by
  apply scaled_expansion (3*c) S m (2^c) guard large
  have powers : 2^c*3^(3*c) = 54^c := by
    rw [Nat.pow_mul,← Nat.mul_pow]
  rw [powers,Nat.pow_mul]
  exact Nat.pow_le_pow_left (by decide) c

theorem depth_zero_guard : Guard 0 20136632 211899691 := by unfold Guard; decide

end CollatzAsymmetricPsiReset
