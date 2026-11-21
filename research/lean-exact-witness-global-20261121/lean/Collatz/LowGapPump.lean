/-
The high-gap affine pump also acts on the distinct source language (1,b,tail),
for every b >= 4. One exponent b pays for an arbitrarily long word of smaller
exponents. The complete original suffix is retained, with the same affine guard.
-/
import Collatz.HighGapPump

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzHighGapPump CollatzDirected CollatzSourceWitness

namespace CollatzLowGapPump

def sourceBase : List Nat := [1,1,3,2,3,1,2,2,2]
def sourceFrontBase : List Nat := [1,1,3,2,3,1,2,2]

def source : Nat → List Nat
  | 0 => sourceBase
  | j+1 => 2 :: source j

def sourceFront : Nat → List Nat
  | 0 => sourceFrontBase
  | j+1 => 2 :: sourceFront j

def targetBase : List Nat := [3,1,1,1,1,2,2,1,4,1]

def target : Nat → List Nat
  | 0 => targetBase
  | j+1 => pump (target j)

theorem source_last (j : Nat) : source j = sourceFront j ++ [2] := by
  induction j with
  | zero => rfl
  | succ j ih => simp [source,sourceFront,ih]

theorem source_positive (j : Nat) : PositiveGaps (source j) := by
  induction j with
  | zero => simp [PositiveGaps,source,sourceBase]
  | succ j ih =>
    intro a ha
    rcases List.mem_cons.mp ha with eq | mem
    · omega
    · exact ih a mem

theorem source_front_bound (j : Nat) : ∀ a ∈ sourceFront j, a ≤ 3 := by
  induction j with
  | zero => decide
  | succ j ih =>
    intro a ha
    rcases List.mem_cons.mp ha with eq | mem
    · omega
    · exact ih a mem

theorem source_stats (j : Nat) :
    (source j).length = j+9 ∧ total (source j) = 2*j+17 ∧
      correction (source j) + 3^(j+9) = 155102*4^j := by
  induction j with
  | zero => decide
  | succ j ih =>
    obtain ⟨len,tot,cor⟩ := ih
    refine ⟨by simp [source,len],by simp [source,total,tot]; omega,?_⟩
    simp only [source,correction,len]
    rw [show j+1+9 = (j+9)+1 by omega,Nat.pow_succ 3 (j+9),Nat.pow_succ 4 j]
    omega

theorem target_nonempty (j : Nat) : target j ≠ [] := by
  induction j with
  | zero => decide
  | succ j ih =>
    cases eq : target j with
    | nil => exact False.elim (ih eq)
    | cons a tail => simp [target,eq,pump]

theorem target_positive (j : Nat) : PositiveGaps (target j) := by
  induction j with
  | zero => simp [PositiveGaps,target,targetBase]
  | succ j ih =>
    cases eq : target j with
    | nil => exact False.elim (target_nonempty j eq)
    | cons a tail =>
      have positive : PositiveGaps (a::tail) := eq ▸ ih
      intro b hb
      simp only [target,eq,pump,List.mem_cons] at hb
      rcases hb with one | next | mem
      · omega
      · omega
      · exact positive b (List.mem_cons_of_mem a mem)

theorem target_stats (j : Nat) :
    (target j).length = (source j).length+1 ∧
      total (target j) = total (source j) ∧
      correction (target j) = correction (source j) + 2^total (source j) := by
  induction j with
  | zero => decide
  | succ j ih =>
    cases eq : target j with
    | nil => exact False.elim (target_nonempty j eq)
    | cons a tail =>
      obtain ⟨len,tot,cor⟩ := ih
      rw [eq] at len tot cor
      have lenEq : tail.length = (source j).length := by
        simp only [List.length_cons] at len
        omega
      refine ⟨by simp [target,eq,pump,source,lenEq],
        by simp [target,eq,pump,source,total] at tot ⊢; omega,?_⟩
      simp only [target,eq,pump,source,correction,List.length_cons,total,
        Nat.pow_succ,Nat.pow_add] at cor ⊢
      rw [lenEq] at cor ⊢
      grind

/-- Exactly the same affine guard as HighGapPump. A second parent language
realizes the same transformation of the two ordinary source/target values. -/
theorem source_prefix (j m p t : Nat) (guard : Guard j m p)
    (frontier : 243*m+5 = 32*t) : Prefix (27*p) (source j) t := by
  obtain ⟨len,tot,cor⟩ := source_stats j
  have powTwo : 2^(2*j+17) = 131072*4^j := by
    rw [Nat.pow_add,Nat.pow_mul]
    grind
  have powThree : 3^(j+9) = 19683*3^j := by rw [Nat.pow_add]; grind
  have powGuard : 3^(j+7) = 2187*3^j := by rw [Nat.pow_add]; grind
  have scaledGuard := congrArg (fun x => 243*x) guard
  have scaledFrontier := congrArg (fun x => (4096*4^j)*x) frontier
  unfold Guard at guard scaledGuard
  rw [powGuard] at guard scaledGuard
  rw [powThree] at cor
  refine ⟨source_positive j,?_⟩
  rw [len,tot,powTwo,powThree]
  grind

theorem target_prefix (j p t : Nat) (path : Prefix (27*p) (source j) t) :
    Prefix (9*p) (target j) (t+1) := by
  obtain ⟨len,tot,cor⟩ := target_stats j
  have id := path.2
  refine ⟨target_positive j,?_⟩
  rw [len,tot,cor,Nat.pow_succ]
  grind

theorem parent_target_prefix (m t : Nat) (frontier : 243*m+5 = 32*t) :
    Prefix (9*m) [2,2,1] (t+1) := by
  refine ⟨by simp [PositiveGaps],?_⟩
  change 27*(9*m)+37 = 32*(t+1)
  omega

theorem rank_decrease (j b : Nat) (tail : List Nat) (large : 4 ≤ b) :
    Less (grades 0 ((sourceFront j ++ [2+(b-4)]) ++ tail))
      (grades 0 (1::b::tail)) := by
  let inserted := (sourceFront j ++ [2+(b-4)]).map (2*·)
  have below : ∀ x ∈ inserted, x < 2*b := by
    intro x hx
    obtain ⟨a,ha,eq⟩ := List.mem_map.mp hx
    rcases List.mem_append.mp ha with front | last
    · have := source_front_bound j a front
      omega
    · have value : a=2+(b-4) := by simpa using last
      omega
  have low : Less inserted [2,2*b] :=
    replace_many [2,2*b] inserted (by simp) (by
      intro x hx
      exact ⟨2*b,by simp,below x hx⟩)
  have full := (less_append_right_iff inserted [2,2*b] (tail.map (2*·))).mpr low
  simpa [grades,inserted,List.map_append] using full

/-- Parent words (1,b,tail), with arbitrary b >= 4, share one full rewrite
schema. The last child gap is adjusted by b-4, and remains strictly below b.
Neither pump length nor numerical expansion is bounded. -/
theorem whole_witness_rewrite (j m p b : Nat) (tail : List Nat)
    (cert : Certificate (27*m) (1::b::tail)) (large : 4 ≤ b)
    (guard : Guard j m p) :
    let rewritten := (sourceFront j ++ [2+(b-4)]) ++ tail
    Certificate (27*p) rewritten ∧
      Less (grades 0 rewritten) (grades 0 (1::b::tail)) ∧
      (Basin (9*m) ↔ Basin (9*p)) := by
  obtain ⟨_,middle,first,rest⟩ := (certificate_cons_iff (27*m) 1 (b::tail)).mp cert
  obtain ⟨_,odd,second,tailCert⟩ := (certificate_cons_iff middle b tail).mp rest
  let t := 2^(b-4)*odd
  have power : 2^b = 16*2^(b-4) := by
    calc
      2^b = 2^(4+(b-4)) := by congr 1; omega
      _ = 2^4*2^(b-4) := Nat.pow_add 2 4 (b-4)
      _ = _ := rfl
  have frontier : 243*m+5 = 32*t := by
    rw [power] at second
    dsimp [t]
    change 3*(27*m)+1=2*middle at first
    grind
  have sourcePath := source_prefix j m p t guard frontier
  have childTarget := target_prefix j p t sourcePath
  have parentTarget := parent_target_prefix m t frontier
  rw [source_last] at sourcePath
  have extended := extend_last sourcePath (show t=2^(b-4)*odd from rfl)
  exact ⟨append_certificate extended tailCert,rank_decrease j b tail large,
    (prefix_basin parentTarget).trans (prefix_basin childTarget).symm⟩

theorem rewritten_sizes (j b : Nat) (tail : List Nat) (large : 4 ≤ b) :
    ((sourceFront j ++ [2+(b-4)]) ++ tail).length =
      (1::b::tail).length+j+7 ∧
    total ((sourceFront j ++ [2+(b-4)]) ++ tail) =
      total (1::b::tail)+2*j+12 := by
  obtain ⟨len,tot,_⟩ := source_stats j
  rw [source_last] at len tot
  simp only [List.length_append,List.length_cons,List.length_nil,
    total_append,total] at len tot ⊢
  omega

/-- A low-gap parent now uses the same deep reverse query as the high-gap pump.
All certificate arithmetic and strict rank hypotheses are supplied by the schema. -/
theorem apply_reverse_rule {active : Active} (j m p b : Nat) (tail : List Nat)
    (cert : Certificate (27*m) (1::b::tail)) (large : 4 ≤ b)
    (guard : Guard j m p) (activated : active (.reverse 3) (9*p))
    (ih : CollatzGapMultiset.Hyp active (grades 0 (1::b::tail))) : Basin (9*m) := by
  obtain ⟨childCert,decrease,merge⟩ := whole_witness_rewrite j m p b tail cert large guard
  have sourceOdd := witness_odd (certificate_witness childCert)
  have childOdd : (9*p)%2=1 := by omega
  have activeCore : active (.reverse 3) (oddCore (9*p)) := by
    rw [oddCore_of_odd _ childOdd]
    exact activated
  have powered : PoweredCertificate (known (.reverse 3) (9*p)) 0
      ((sourceFront j ++ [2+(b-4)]) ++ tail) := by
    refine ⟨27*p,?_,childCert⟩
    simp [known]
    omega
  have result := ih (.reverse 3) (9*p) 0 _ (by omega) activeCore decrease powered
  exact merge.mpr result

end CollatzLowGapPump
