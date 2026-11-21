/-
An arbitrary-length guarded high-gap source rewrite.
The arithmetic splices and the complete inherited tail are checked in Lean core.
The affine guard is a genuine restriction; this family is not a complete cover.
-/
import Collatz.GapMultiset

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset

namespace CollatzHighGapPump

theorem total_append (xs ys : List Nat) : total (xs ++ ys) = total xs + total ys := by
  induction xs with
  | nil => simp [total]
  | cons x xs ih => simp [total,ih,Nat.add_assoc]

theorem correction_append (xs ys : List Nat) :
    correction (xs ++ ys) = 3^ys.length*correction xs + 2^total xs*correction ys := by
  induction xs with
  | nil => simp [correction,total]
  | cons x xs ih =>
    simp only [List.cons_append,List.length_append,correction,total,ih,Nat.pow_add]
    grind

/-- An exact positive-gap prefix, with an arbitrary ordinary endpoint. -/
def Prefix (n : Nat) (word : List Nat) (endpoint : Nat) : Prop :=
  PositiveGaps word ∧ 3^word.length*n + correction word = 2^total word*endpoint

theorem prefix_cons_iff (n a endpoint : Nat) (tail : List Nat) :
    Prefix n (a::tail) endpoint ↔
      0 < a ∧ ∃ m, 3*n+1 = 2^a*m ∧ Prefix m tail endpoint := by
  constructor
  · rintro ⟨positive,identity⟩
    have ha : 0 < a := positive a (by simp)
    have ht : PositiveGaps tail := fun b hb => positive b (by simp [hb])
    have eq : 3^tail.length*(3*n+1) + 2^a*correction tail =
        2^a*(2^total tail*endpoint) := by
      simp only [List.length_cons,correction,total,Nat.pow_succ,Nat.pow_add] at identity
      grind
    have divides : 2^a ∣ 3^tail.length*(3*n+1) := by
      have sum : 2^a ∣ 3^tail.length*(3*n+1) + 2^a*correction tail :=
        ⟨2^total tail*endpoint,eq⟩
      have rest : 2^a ∣ 2^a*correction tail := ⟨correction tail,rfl⟩
      exact (Nat.dvd_add_iff_left rest).mpr sum
    have coprime : Nat.Coprime (2^a) (3^tail.length) :=
      Nat.gcd_pow_right_of_gcd_eq_one (Nat.gcd_pow_left_of_gcd_eq_one
        (by decide : Nat.gcd 2 3 = 1))
    obtain ⟨m,step⟩ := coprime.dvd_of_dvd_mul_left divides
    have step' : 3*n+1 = 2^a*m := step
    have tailEq : 3^tail.length*m + correction tail = 2^total tail*endpoint := by
      rw [step'] at eq
      have factored : 2^a*(3^tail.length*m + correction tail) =
          2^a*(2^total tail*endpoint) := by grind
      exact Nat.eq_of_mul_eq_mul_left (Nat.pow_pos (by decide)) factored
    exact ⟨ha,m,step',ht,tailEq⟩
  · rintro ⟨ha,m,step,positive,identity⟩
    refine ⟨?_,?_⟩
    · intro b hb
      rcases List.mem_cons.mp hb with eq | mem
      · simpa [eq] using ha
      · exact positive b mem
    · simp only [List.length_cons,correction,total,Nat.pow_succ,Nat.pow_add]
      calc
        3^tail.length*3*n + (3^tail.length + 2^a*correction tail) =
            3^tail.length*(3*n+1) + 2^a*correction tail := by grind
        _ = 2^a*(3^tail.length*m + correction tail) := by rw [step]; grind
        _ = _ := by rw [identity]; grind

/-- Polynomial legality entails actual integral odd steps; this is not merely a
rational affine identity. The endpoint itself need not be odd. -/
theorem prefix_basin {n endpoint : Nat} {word : List Nat} (h : Prefix n word endpoint) :
    Basin n ↔ Basin endpoint := by
  induction word generalizing n with
  | nil =>
    have eq : n = endpoint := by simpa [Prefix,correction,total] using h.2
    subst n; exact Iff.rfl
  | cons a tail ih =>
    obtain ⟨ha,m,eq,rest⟩ := (prefix_cons_iff n a endpoint tail).mp h
    have odd : n % 2 = 1 := by
      obtain ⟨b,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : a ≠ 0)
      rw [Nat.pow_succ] at eq
      have form : 3*n+1 = 2*(2^b*m) := by grind
      omega
    have ordinary : Basin n ↔ Basin m := by
      have link := (basin_odd n odd).symm
      rw [eq] at link
      exact link.trans (basin_pow_two a m)
    exact ordinary.trans (ih rest)

/-- Attach the same complete source tail to an exact prefix. -/
theorem append_certificate {n endpoint : Nat} {front tail : List Nat}
    (path : Prefix n front endpoint) (cert : Certificate endpoint tail) :
    Certificate n (front ++ tail) := by
  refine ⟨?_,?_⟩
  · intro a ha
    rcases List.mem_append.mp ha with hf | ht
    · exact path.1 a hf
    · exact cert.1 a ht
  · rw [List.length_append,correction_append,total_append,Nat.pow_add,Nat.pow_add]
    have hp := path.2
    have hc := cert.2
    calc
      3^front.length*3^tail.length*n +
          (3^tail.length*correction front + 2^total front*correction tail) =
          3^tail.length*(3^front.length*n+correction front)+
            2^total front*correction tail := by grind
      _ = 2^total front*(3^tail.length*endpoint+correction tail) := by rw [hp]; grind
      _ = _ := by rw [hc]

theorem correction_last (front : List Nat) (a b : Nat) :
    correction (front ++ [a]) = correction (front ++ [b]) := by
  simp [correction_append,correction]

theorem extend_last {n endpoint odd a h : Nat} {front : List Nat}
    (path : Prefix n (front ++ [a]) endpoint) (eq : endpoint = 2^h*odd) :
    Prefix n (front ++ [a+h]) odd := by
  refine ⟨?_,?_⟩
  · intro b hb
    rcases List.mem_append.mp hb with hf | hl
    · exact path.1 b (List.mem_append.mpr (Or.inl hf))
    · have ba : b = a+h := by simpa using hl
      have pos := path.1 a (by simp)
      omega
  · have id := path.2
    rw [eq] at id
    rw [correction_last front a (a+h)] at id
    simpa [List.length_append,total_append,total,Nat.pow_add,Nat.mul_assoc] using id

def sourceBase : List Nat := [1,1,3,2,3,1,3,3]
def sourceFrontBase : List Nat := [1,1,3,2,3,1,3]

def source : Nat → List Nat
  | 0 => sourceBase
  | j+1 => 2 :: source j

def sourceFront : Nat → List Nat
  | 0 => sourceFrontBase
  | j+1 => 2 :: sourceFront j

theorem source_last (j : Nat) : source j = sourceFront j ++ [3] := by
  induction j with
  | zero => rfl
  | succ j ih => simp [source,sourceFront,ih]

def targetBase : List Nat := [3,1,1,1,1,2,2,1,1,1,3]

def pump : List Nat → List Nat
  | [] => []
  | a::tail => 1 :: (a+1) :: tail

def target : Nat → List Nat
  | 0 => targetBase
  | j+1 => pump (target j)

theorem source_positive (j : Nat) : PositiveGaps (source j) := by
  induction j with
  | zero => simp [PositiveGaps,source,sourceBase]
  | succ j ih =>
    intro a ha
    rcases List.mem_cons.mp ha with eq | mem
    · omega
    · exact ih a mem

theorem source_front_bound (j : Nat) : ∀ a ∈ sourceFront j, a ≤ 4 := by
  induction j with
  | zero => decide
  | succ j ih =>
    intro a ha
    rcases List.mem_cons.mp ha with eq | mem
    · omega
    · exact ih a mem

theorem source_stats (j : Nat) :
    (source j).length = j+8 ∧ total (source j) = 2*j+17 ∧
      correction (source j) + 3^(j+8) = 48970*4^j := by
  induction j with
  | zero => decide
  | succ j ih =>
    obtain ⟨len,tot,cor⟩ := ih
    refine ⟨by simp [source,len],by simp [source,total,tot]; omega,?_⟩
    simp only [source,correction,len]
    rw [show j+1+8 = (j+8)+1 by omega,Nat.pow_succ 3 (j+8),Nat.pow_succ 4 j]
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
      have p : PositiveGaps (a::tail) := eq ▸ ih
      intro b hb
      simp only [target,eq,pump,List.mem_cons] at hb
      rcases hb with one | next | mem
      · omega
      · omega
      · exact p b (List.mem_cons_of_mem a mem)

theorem target_stats (j : Nat) :
    (target j).length = (source j).length+3 ∧
      total (target j) = total (source j) ∧
      correction (target j) = 2*2^total (source j) + 9*correction (source j) := by
  induction j with
  | zero => decide
  | succ j ih =>
    cases eq : target j with
    | nil => exact False.elim (target_nonempty j eq)
    | cons a tail =>
      obtain ⟨len,tot,cor⟩ := ih
      rw [eq] at len tot cor
      have lenEq : tail.length = (source j).length+2 := by simp only [List.length_cons] at len; omega
      refine ⟨by simp [target,eq,pump,source,lenEq],
        by simp [target,eq,pump,source,total] at tot ⊢; omega,?_⟩
      simp only [target,eq,pump,source,correction,List.length_cons,total,
        Nat.pow_succ,Nat.pow_add] at cor ⊢
      have exp : 3^tail.length = 9*3^(source j).length := by rw [lenEq,Nat.pow_add]; grind
      rw [exp] at cor ⊢
      grind

/-- This exact affine congruence is the guard of the pumped rewrite. -/
def Guard (j m p : Nat) : Prop :=
  3^(j+7)*p + 554*4^j = 4096*4^j*m + 81*3^j

theorem source_prefix (j m p t : Nat) (guard : Guard j m p)
    (frontier : 81*m+1 = 32*t) : Prefix (27*p) (source j) t := by
  obtain ⟨len,tot,cor⟩ := source_stats j
  have powTwo : 2^(2*j+17) = 131072*4^j := by
    rw [Nat.pow_add,Nat.pow_mul]
    grind
  have powThree : 3^(j+8) = 6561*3^j := by rw [Nat.pow_add]; grind
  have powGuard : 3^(j+7) = 2187*3^j := by rw [Nat.pow_add]; grind
  have scaledGuard := congrArg (fun x => 81*x) guard
  have scaledFrontier := congrArg (fun x => (4096*4^j)*x) frontier
  unfold Guard at guard scaledGuard
  rw [powGuard] at guard scaledGuard
  rw [powThree] at cor
  refine ⟨source_positive j,?_⟩
  rw [len,tot,powTwo,powThree]
  grind

theorem target_prefix (j p t : Nat) (path : Prefix (27*p) (source j) t) :
    Prefix (9*p) (target j) (9*t+2) := by
  obtain ⟨len,tot,cor⟩ := target_stats j
  have id := congrArg (fun x => 9*x) path.2
  refine ⟨target_positive j,?_⟩
  rw [len,tot,cor,Nat.pow_add]
  grind

theorem parent_target_prefix (m t : Nat) (frontier : 81*m+1 = 32*t) :
    Prefix (9*m) [1,1,2,1] (9*t+2) := by
  refine ⟨by simp [PositiveGaps],?_⟩
  change 81*(9*m)+73 = 32*(9*t+2)
  omega

/-- A whole supplied certificate is transformed for every pump length j.
The child may expand without bound; the complete arbitrary source tail remains
unchanged. Source integrality, target merging, and strict multiset descent are
proved together under the displayed guard. -/
theorem whole_witness_rewrite (j m p a : Nat) (tail : List Nat)
    (cert : Certificate (27*m) (a::tail)) (high : 5 ≤ a) (guard : Guard j m p) :
    let rewritten := (sourceFront j ++ [3+(a-5)]) ++ tail
    Certificate (27*p) rewritten ∧
      Less (grades 0 rewritten) (grades 0 (a::tail)) ∧
      (Basin (9*m) ↔ Basin (9*p)) := by
  obtain ⟨_,odd,first,tailCert⟩ := (certificate_cons_iff (27*m) a tail).mp cert
  let t := 2^(a-5)*odd
  have frontier : 81*m+1 = 32*t := by
    have power : 2^a = 32*2^(a-5) := by
      calc
        2^a = 2^(5+(a-5)) := by congr 1; omega
        _ = 2^5*2^(a-5) := Nat.pow_add 2 5 (a-5)
        _ = _ := rfl
    rw [power] at first
    dsimp [t]
    grind
  have sourcePath := source_prefix j m p t guard frontier
  have childTarget := target_prefix j p t sourcePath
  have parentTarget := parent_target_prefix m t frontier
  rw [source_last] at sourcePath
  have extended := extend_last sourcePath (show t = 2^(a-5)*odd from rfl)
  refine ⟨append_certificate extended tailCert,?_,?_⟩
  · exact unbounded_high_gap_replacement a 3 (sourceFront j) tail high
      (source_front_bound j) (by decide)
  · exact (prefix_basin parentTarget).trans (prefix_basin childTarget).symm

/-- Both the number of accelerated gaps and their sum increase. Thus the new
multiset proof genuinely admits witnesses beyond source-length descent. -/
theorem rewritten_sizes (j a : Nat) (tail : List Nat) (high : 5 ≤ a) :
    ((sourceFront j ++ [3+(a-5)]) ++ tail).length = (a::tail).length+j+7 ∧
      total ((sourceFront j ++ [3+(a-5)]) ++ tail) = total (a::tail)+2*j+12 := by
  obtain ⟨len,tot,_⟩ := source_stats j
  rw [source_last] at len tot
  simp only [List.length_append,List.length_cons,List.length_nil,total_append,total] at len tot ⊢
  omega

open CollatzDirected CollatzSourceWitness

/-- The pumped family is a concrete recursive reverse-tripling rule in the same
global multiset induction system, with no new query kind and no length cutoff. -/
theorem apply_reverse_rule {active : Active} (j m p a : Nat) (tail : List Nat)
    (cert : Certificate (27*m) (a::tail)) (high : 5 ≤ a) (guard : Guard j m p)
    (activated : active (.reverse 3) (9*p))
    (ih : CollatzGapMultiset.Hyp active (grades 0 (a::tail))) : Basin (9*m) := by
  obtain ⟨childCert,decrease,merge⟩ := whole_witness_rewrite j m p a tail cert high guard
  have sourceOdd := witness_odd (certificate_witness childCert)
  have childOdd : (9*p) % 2 = 1 := by omega
  have activeCore : active (.reverse 3) (oddCore (9*p)) := by
    rw [oddCore_of_odd _ childOdd]
    exact activated
  have powered : PoweredCertificate (known (.reverse 3) (9*p)) 0
      ((sourceFront j ++ [3+(a-5)]) ++ tail) := by
    refine ⟨27*p,?_,childCert⟩
    simp [known]
    omega
  have result := ih (.reverse 3) (9*p) 0 _ (by omega) activeCore decrease powered
  exact merge.mpr result

theorem scaled_expansion (j m p k : Nat) (guard : Guard j m p) (positive : 0 < m)
    (ratio : k*3^j ≤ 4^j) : k*m < p := by
  by_cases gt : k*m < p
  · exact gt
  have le : p ≤ k*m := by omega
  have pp : 0 < 4^j := Nat.pow_pos (by decide)
  have power : 3^(j+7) = 2187*3^j := by rw [Nat.pow_add]; grind
  have bound := Nat.mul_le_mul_left (3^(j+7)) le
  have ratio' := Nat.mul_le_mul_right (2187*m) ratio
  have mpos := Nat.mul_le_mul_left (4^j) positive
  unfold Guard at guard
  rw [power] at guard bound
  grind

theorem exponential_expansion (c m p : Nat) (guard : Guard (3*c) m p)
    (positive : 0 < m) : 2^c*m < p := by
  apply scaled_expansion (3*c) m p (2^c) guard positive
  have powers : 2^c*3^(3*c) = 54^c := by
    rw [Nat.pow_mul,← Nat.mul_pow]
  rw [powers,Nat.pow_mul]
  exact Nat.pow_le_pow_left (by decide) c

/-- A fixed numerical exponential energy cannot certify every pumped prefix:
there is an explicit pump depth at which its proposed decrease reverses. This
is a statement about the uniform rank inequality, not a Collatz counterexample. -/
theorem fixed_base_prefix_failure (c : Nat) (positive : 0 < c) :
    CollatzWitnessEnergy.prefixEnergy c [5] <
      CollatzWitnessEnergy.prefixEnergy c (source (c^3)) := by
  have energy (j : Nat) : CollatzWitnessEnergy.prefixEnergy c (source j) =
      j*c^2 + CollatzWitnessEnergy.prefixEnergy c sourceBase := by
    induction j with
    | zero => simp [source]
    | succ j ih =>
      simp only [source,CollatzWitnessEnergy.prefixEnergy,ih]
      grind
  have basePositive : 0 < CollatzWitnessEnergy.prefixEnergy c sourceBase := by
    simp only [sourceBase,CollatzWitnessEnergy.prefixEnergy]
    have cp : 0 < c^1 := Nat.pow_pos positive
    omega
  rw [energy]
  have powers : c^3*c^2 = c^5 := by rw [← Nat.pow_add]
  rw [powers]
  simp only [CollatzWitnessEnergy.prefixEnergy,Nat.add_zero]
  omega

end CollatzHighGapPump
