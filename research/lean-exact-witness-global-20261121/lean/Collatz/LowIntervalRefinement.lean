/-
Actual low-alphabet interval coverage by compensated source prefixes and
synchronized source-target steps. Literal source tails are retained and all
recursive calls strictly decrease the common graded multiset order.
-/
import Collatz.BoundedGapCofinal

open CollatzReverseBasin CollatzWitness CollatzGapMultiset
open CollatzHighGapPump CollatzLowGapLoops CollatzBoundedGapCofinal

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzLowIntervalRefinement

/-- Delete a nonempty literal odd prefix while keeping the same even run. -/
theorem prefix_rank (e : Nat) (front tail : List Nat) (nonempty : front ≠ []) :
    Less (grades e tail) (grades e (front ++ tail)) := by
  have mapped : front.map (2*·) ≠ [] := by
    intro eq
    have len := congrArg List.length eq
    simp only [List.length_map,List.length_nil] at len
    have nil := List.length_eq_zero_iff.mp len
    exact nonempty nil
  have short : Less [] (front.map (2*·)) :=
    replace_many _ [] mapped (by intro b hb; simp at hb)
  have suffix := (less_append_right_iff [] (front.map (2*·)) (tail.map (2*·))).mpr short
  have full := (less_append_left_iff
    (if e=0 then [] else [2*e+1]) (tail.map (2*·))
    (front.map (2*·) ++ tail.map (2*·))).mpr (by simpa using suffix)
  simpa [grades,List.map_append,List.append_assoc] using full

/-- A noncontracting coefficient and the positive affine correction force
strict growth of the actual supplied odd source. -/
theorem prefix_expands (q u : Nat) (front : List Nat)
    (path : Prefix q front u) (nonempty : front ≠ [])
    (coefficient : 2^total front ≤ 3^front.length) : q<u := by
  have correctionPositive : 0<correction front := by
    cases front with
    | nil => exact False.elim (nonempty rfl)
    | cons a tail =>
      have power : 0<3^tail.length := Nat.pow_pos (by decide)
      simp only [correction]
      omega
  have compared := Nat.mul_le_mul_right q coefficient
  by_cases result : q<u
  · exact result
  have reverse : u≤q := by omega
  have bound := Nat.mul_le_mul_left (2^total front) reverse
  have identity := path.2
  omega

/-- An arbitrarily long compensated prefix supplies an explicitly larger
known source with the same even run, while its complete source rank drops. -/
theorem scaled_prefix_rewrite (source e : Nat) (front tail : List Nat)
    (cert : PoweredCertificate source e (front ++ tail)) (nonempty : front ≠ [])
    (coefficient : 2^total front ≤ 3^front.length) :
    ∃ u, source<2^e*u ∧ Certificate u tail ∧
      Less (grades e tail) (grades e (front ++ tail)) := by
  obtain ⟨q,parent,sourceCert⟩ := cert
  obtain ⟨u,path,tailCert⟩ := split_certificate q front tail sourceCert
  have grows := prefix_expands q u front path nonempty coefficient
  have scaled := Nat.mul_lt_mul_of_pos_left grows (Nat.pow_pos (by decide) : 0<2^e)
  exact ⟨u,by simpa [parent] using scaled,tailCert,prefix_rank e front tail nonempty⟩

/-- This is a successful interval rule: the wanted integer remains unchanged
and is still below the new source's interval ceiling. -/
theorem coefficient_interval_rule (source target e : Nat) (front tail : List Nat)
    (active : Interval source target)
    (cert : PoweredCertificate source e (front ++ tail)) (nonempty : front ≠ [])
    (coefficient : 2^total front ≤ 3^front.length)
    (ih : CollatzGapComparison.Hyp Interval (grades e (front ++ tail))) : Basin target := by
  obtain ⟨u,grows,tailCert,drop⟩ :=
    scaled_prefix_rewrite source e front tail cert nonempty coefficient
  exact ih (2^e*u) target e tail ⟨active.1,by have h:=active.2; omega⟩
    ⟨u,rfl,tailCert⟩ drop

/-- Every first gap one closes, at every initial even valuation. -/
theorem first_gap_one_rule (source target e : Nat) (tail : List Nat)
    (active : Interval source target) (cert : PoweredCertificate source e (1::tail))
    (ih : CollatzGapComparison.Hyp Interval (grades e (1::tail))) : Basin target := by
  exact coefficient_interval_rule source target e [1] tail active cert (by decide)
    (by decide) ih

/-- The two runs are unbounded. They have coefficient (9/8)^k. -/
def balancedRuns (k : Nat) : List Nat := repeatHead 2 k (repeatHead 1 k [])

theorem balanced_runs_rule (source target e k : Nat) (tail : List Nat)
    (positive : 0<k) (active : Interval source target)
    (cert : PoweredCertificate source e (balancedRuns k ++ tail))
    (ih : CollatzGapComparison.Hyp Interval (grades e (balancedRuns k ++ tail))) :
    Basin target := by
  have length : (balancedRuns k).length = 2*k := by
    simp [balancedRuns,repeatHead_length]
    omega
  have sum : total (balancedRuns k) = 3*k := by
    simp [balancedRuns,repeatHead_total,total]
    omega
  have nonempty : balancedRuns k ≠ [] := by
    intro nil
    rw [nil] at length
    simp only [List.length_nil] at length
    omega
  have coefficient : 2^total (balancedRuns k) ≤ 3^(balancedRuns k).length := by
    rw [length,sum]
    simpa [Nat.pow_mul] using Nat.pow_le_pow_left (by decide : 8≤9) k
  exact coefficient_interval_rule source target e _ tail active cert nonempty coefficient ih

/-- For a>=2, a gap a followed by 2a-3 ones has coefficient (9/8)^(a-1).
For the remaining alphabet this includes (2,1), (3,1,1,1), and (4,1^5). -/
def compensatedGap (a : Nat) : List Nat := a :: repeatHead 1 (2*a-3) []

theorem compensated_gap_rule (source target e a : Nat) (tail : List Nat)
    (large : 2≤a) (active : Interval source target)
    (cert : PoweredCertificate source e (compensatedGap a ++ tail))
    (ih : CollatzGapComparison.Hyp Interval (grades e (compensatedGap a ++ tail))) :
    Basin target := by
  have length : (compensatedGap a).length = 2*(a-1) := by
    simp only [compensatedGap,List.length_cons,repeatHead_length,List.length_nil]
    omega
  have sum : total (compensatedGap a) = 3*(a-1) := by
    simp only [compensatedGap,total,repeatHead_total]
    omega
  have coefficient : 2^total (compensatedGap a) ≤ 3^(compensatedGap a).length := by
    rw [length,sum]
    simpa [Nat.pow_mul] using Nat.pow_le_pow_left (by decide : 8≤9) (a-1)
  exact coefficient_interval_rule source target e _ tail active cert (by simp [compensatedGap])
    coefficient ih

/-- Clearing one supplied source gap gives the exact slack which pays for
the target's upper interval boundary. -/
theorem scaled_gap_identity (source e q a u : Nat)
    (parent : source=2^e*q) (step : 3*q+1=2^a*u) :
    2^a*(2*(2^e*u))=6*source+2^(e+1) := by
  calc
    2^a*(2*(2^e*u)) = (2^e*2)*(2^a*u) := by ac_rfl
    _ = (2^e*2)*(3*q+1) := by rw [step]
    _ = 6*source+2^(e+1) := by
      simp only [parent,Nat.pow_succ,Nat.mul_add,Nat.mul_one]
      congr 1
      calc
        (2^e*2)*(3*q) = (2*3)*(2^e*q) := by ac_rfl
        _ = 6*(2^e*q) := rfl

private theorem paid_interval (source target e b child v : Nat) (even : 1≤e)
    (active : Interval source target)
    (slack : 2^b*(2*child)=6*source+2^(e+1))
    (step : 3*target+1=2^b*v) : Interval child v := by
  have positive : 0<v := by
    by_cases zero : v=0
    · simp [zero] at step
    · omega
  have payment : 4≤2^(e+1) := by
    exact Nat.pow_le_pow_right (by decide : 1≤2) (by omega : 2≤e+1)
  have scaled : 2^b*v≤2^b*(2*child) := by
    have upper := active.2
    omega
  have bound : v≤2*child := Nat.le_of_mul_le_mul_left scaled (Nat.pow_pos (by decide))
  exact ⟨positive,by omega⟩

private theorem one_gap_prefix (target b v : Nat) (positive : 0<b)
    (step : 3*target+1=2^b*v) : Prefix target [b] v := by
  refine ⟨?_,?_⟩
  · intro c mem
    have eq := List.mem_singleton.mp mem
    simpa [eq] using positive
  · simpa [correction,total] using step

/-- Source and target consume the same positive gap. The initial even run
is retained, and the literal remaining source word pays for the child query. -/
theorem matched_gap_rule (source target e a v : Nat) (tail : List Nat)
    (even : 1≤e) (active : Interval source target)
    (cert : PoweredCertificate source e (a::tail))
    (targetStep : 3*target+1=2^a*v)
    (ih : CollatzGapComparison.Hyp Interval (grades e (a::tail))) : Basin target := by
  obtain ⟨q,parent,sourceCert⟩ := cert
  obtain ⟨positive,u,step,tailCert⟩ := (certificate_cons_iff q a tail).mp sourceCert
  have childActive := paid_interval source target e a (2^e*u) v even active
    (scaled_gap_identity source e q a u parent step) targetStep
  have drop : Less (grades e tail) (grades e (a::tail)) :=
    prefix_rank e [a] tail (by simp)
  have child := ih (2^e*u) v e tail childActive ⟨u,rfl,tailCert⟩ drop
  exact (prefix_basin (one_gap_prefix target a v positive targetStep)).mpr child

/-- A larger source gap pays for a new initial even run below its own grade.
This compares the full source ranks in the original, common multiset order. -/
theorem shortened_gap_rank (e a : Nat) (tail : List Nat) (even : 1≤e)
    (large : e+1<a) : Less (grades (a-1) tail) (grades e (a::tail)) := by
  have base : Less [2*(a-1)+1] [2*e+1,2*a] := by
    apply replace_many _ _ (by simp)
    intro b mem
    have eq := List.mem_singleton.mp mem
    refine ⟨2*a,by simp,?_⟩
    omega
  have full := (less_append_right_iff [2*(a-1)+1] [2*e+1,2*a]
    (tail.map (2*·))).mpr base
  have eNe : e≠0 := by omega
  have aNe : a-1≠0 := by omega
  simpa [grades,eNe,aNe] using full

/-- The target needs only e+1 halvings when the supplied source gap is larger.
The remaining source gap becomes the new even run a-1, strictly below the
removed odd-gap grade. Both the supplied tail and the target endpoint survive. -/
theorem shortened_gap_rule (source target e a v : Nat) (tail : List Nat)
    (even : 1≤e) (large : e+1<a) (active : Interval source target)
    (cert : PoweredCertificate source e (a::tail))
    (targetStep : 3*target+1=2^(e+1)*v)
    (ih : CollatzGapComparison.Hyp Interval (grades e (a::tail))) : Basin target := by
  obtain ⟨q,parent,sourceCert⟩ := cert
  obtain ⟨_,u,step,tailCert⟩ := (certificate_cons_iff q a tail).mp sourceCert
  have shift : 2^(e+1)*2^(a-1)=2^e*2^a := by
    rw [←Nat.pow_add,←Nat.pow_add]
    congr 1
    omega
  have slack : 2^(e+1)*(2*(2^(a-1)*u))=6*source+2^(e+1) := by
    calc
      2^(e+1)*(2*(2^(a-1)*u)) = 2*(2^(e+1)*2^(a-1))*u := by ac_rfl
      _ = 2*(2^e*2^a)*u := by rw [shift]
      _ = 2^a*(2*(2^e*u)) := by ac_rfl
      _ = _ := scaled_gap_identity source e q a u parent step
  have childActive := paid_interval source target e (e+1) (2^(a-1)*u) v
    even active slack targetStep
  have child := ih (2^(a-1)*u) v (a-1) tail childActive ⟨u,rfl,tailCert⟩
    (shortened_gap_rank e a tail even large)
  exact (prefix_basin (one_gap_prefix target (e+1) v (by omega) targetStep)).mpr child

/-- Uniform coverage requires only min(a,e+1) target halvings. -/
theorem synchronized_gap_rule (source target e a v : Nat) (tail : List Nat)
    (even : 1≤e) (active : Interval source target)
    (cert : PoweredCertificate source e (a::tail))
    (targetStep : 3*target+1=2^(min a (e+1))*v)
    (ih : CollatzGapComparison.Hyp Interval (grades e (a::tail))) : Basin target := by
  by_cases small : a≤e+1
  · exact matched_gap_rule source target e a v tail even active cert
      (by simpa [Nat.min_eq_left small] using targetStep) ih
  · exact shortened_gap_rule source target e a v tail even (by omega) active cert
      (by simpa [Nat.min_eq_right (by omega : e+1≤a)] using targetStep) ih


private def hitDecision (x : Nat) : (k : Nat) → Decidable (Hits x k)
  | 0 => inferInstanceAs (Decidable (x=1))
  | k+1 => hitDecision (shortcut x) k

/-- The exact finite terminal range left by e<=3, checked by the Lean kernel.
This is a base case, not an increasing numerical verification threshold. -/
theorem terminal_range (n : Nat) (positive : 0<n) (small : n≤17) : Basin n := by
  letI (x k : Nat) : Decidable (Hits x k) := hitDecision x k
  have finite : ∀ n : Fin 18, n.val≠0 → ∃ k : Fin 14, Hits n.val k.val := by decide
  let v : Fin 18 := ⟨n,by omega⟩
  have nonzero : v.val≠0 := by dsimp [v]; omega
  obtain ⟨k,hit⟩ := finite v nonzero
  exact ⟨k.val,by simpa [v] using hit⟩

theorem terminal_even_rule (source target e : Nat) (small : e≤3)
    (active : Interval source target) (cert : PoweredCertificate source e []) :
    Basin target := by
  obtain ⟨q,parent,tailCert⟩ := cert
  have one : q=1 := by simpa [CollatzWitness.Certificate,total,correction] using tailCert.2
  have bound : 2^e≤8 := Nat.pow_le_pow_right (by decide : 1≤2) small
  have sourceBound : source≤8 := by rw [parent,one]; simpa using bound
  exact terminal_range target active.1 (by have h:=active.2; omega)

end CollatzLowIntervalRefinement
