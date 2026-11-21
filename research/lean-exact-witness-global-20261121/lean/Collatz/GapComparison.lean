/-
One whole-certificate induction for arbitrary source/target basin comparisons.

Reverse-tripling and psi-forward resets have different source/target shapes.
This kernel includes both in one explicitly activated domain and one graded
multiset order. A complete sound dispatcher remains an explicit hypothesis.
-/
import Collatz.HighGapPump
import Collatz.UnboundedGapReset
import Collatz.LowGapLoops
import Collatz.LowGapPump

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset

namespace CollatzGapComparison

/-- The domain includes the entire ordinary source/target pair. -/
def Active := Nat → Nat → Prop

def Claim (source target : Nat) : Prop := Basin source → Basin target

/-- Every recursive child supplies its own actual complete source witness and
decreases the same parent word. No bound on the child value or length is imposed. -/
def Hyp (active : Active) (old : List Nat) : Prop :=
  ∀ source target e gaps, active source target →
    PoweredCertificate source e gaps → Less (grades e gaps) old → Basin target

def Complete (active : Active) : Prop :=
  ∀ source target e gaps, active source target → PoweredCertificate source e gaps →
    Hyp active (grades e gaps) → Basin target

/-- Every activated comparison follows once all of its recursive cases are
covered. Distinct comparison shapes may be mixed because their whole source
certificates all decrease one genuinely common well-founded order. -/
theorem close {active : Active} (complete : Complete active)
    {source target : Nat} (activated : active source target) : Claim source target := by
  have all : ∀ word source target e gaps, grades e gaps = word →
      active source target → PoweredCertificate source e gaps → Basin target := by
    intro word
    induction word using CollatzGapMultiset.induction_on with
    | step word ih =>
      intro source target e gaps eq ha cert
      apply complete source target e gaps ha cert
      intro childSource childTarget childE childGaps childActive childCert decrease
      exact ih (grades childE childGaps) (by simpa [eq] using decrease)
        childSource childTarget childE childGaps rfl childActive childCert
  intro sourceBasin
  obtain ⟨e,gaps,cert⟩ := basin_powered_certificate sourceBasin
  exact all (grades e gaps) source target e gaps rfl activated cert

/-- Mandatory psi-forward comparisons suffice for all positive ordinary inputs.
Additional active pair shapes are permitted, but must also be covered. -/
theorem collatz_of_complete_psi {active : Active} (complete : Complete active)
    (coverage : ∀ s, 0 < s → active s (2*s-1)) :
    ∀ n, 0 < n → Basin n := by
  apply collatz_iff_psi_forward.mpr
  intro s hs known
  exact close complete (coverage s hs) known

/-- The original sparse deep reverse-tripling domain is another sufficient set
of mandatory pair queries in the very same kernel. -/
theorem collatz_of_complete_deep {active : Active} (complete : Complete active)
    (coverage : ∀ n, n % 18 = 9 → active (3*n) n) :
    ∀ n, 0 < n → Basin n := by
  apply deep_reverse_generates ⟨basin_twice,basin_odd,?_⟩
    (show Basin 1 from ⟨0,rfl⟩)
  intro n hn known
  exact close complete (coverage n hn) known

/-- General one-query transfer. Both source-witness validity and target
transport are supplied explicitly, independently of the rank comparison. -/
theorem one_query {active : Active} {old gaps : List Nat}
    {childSource childTarget target e : Nat}
    (activated : active childSource childTarget)
    (cert : PoweredCertificate childSource e gaps)
    (decrease : Less (grades e gaps) old)
    (transport : Basin childTarget → Basin target) (ih : Hyp active old) :
    Basin target :=
  transport (ih childSource childTarget e gaps activated cert decrease)

/-- Consuming one ordinary source step is valid in this common program whenever
the resulting comparison pair is active. Reaching source one is a terminal case
for the dispatcher, not an unrestricted new convergence premise. -/
theorem ordinary_source {active : Active} {source target e : Nat} {gaps : List Nat}
    (cert : PoweredCertificate source e gaps) (nonterminal : source ≠ 1)
    (activated : active (shortcut source) target)
    (ih : Hyp active (grades e gaps)) : Basin target := by
  obtain ⟨childE,childGaps,childCert,decrease⟩ := ordinary_step cert nonterminal
  exact ih (shortcut source) target childE childGaps activated childCert decrease

/-- The unbounded high-gap family consumes the pair (27m,9m) and queries
(27p,9p). Its complete source splice and its target merger have already been
proved by the arithmetic compiler. -/
theorem high_gap_rule {active : Active} (j m p a : Nat) (tail : List Nat)
    (cert : Certificate (27*m) (a::tail)) (high : 5 ≤ a)
    (guard : CollatzHighGapPump.Guard j m p) (activated : active (27*p) (9*p))
    (ih : Hyp active (grades 0 (a::tail))) : Basin (9*m) := by
  obtain ⟨childCert,decrease,merge⟩ :=
    CollatzHighGapPump.whole_witness_rewrite j m p a tail cert high guard
  have powered : PoweredCertificate (27*p) 0
      ((CollatzHighGapPump.sourceFront j ++ [3+(a-5)]) ++ tail) :=
    ⟨27*p,by simp,childCert⟩
  exact one_query activated powered decrease merge.mpr ih

/-- The same affine guard also admits the low first-gap language (1,b,tail),
for every b at least four. This is a separate arithmetic source splice. -/
theorem low_gap_pump_rule {active : Active} (j m p b : Nat) (tail : List Nat)
    (cert : Certificate (27*m) (1::b::tail)) (large : 4 ≤ b)
    (guard : CollatzHighGapPump.Guard j m p) (activated : active (27*p) (9*p))
    (ih : Hyp active (grades 0 (1::b::tail))) : Basin (9*m) := by
  obtain ⟨childCert,decrease,merge⟩ :=
    CollatzLowGapPump.whole_witness_rewrite j m p b tail cert large guard
  have powered : PoweredCertificate (27*p) 0
      ((CollatzLowGapPump.sourceFront j ++ [2+(b-4)]) ++ tail) :=
    ⟨27*p,by simp,childCert⟩
  exact one_query activated powered decrease merge.mpr ih

/-- The arbitrary two-loop low-gap language consumes the pair (3n,n) and
queries the actual suffix pair (u,3u). This forward-tripling query is in the
same activated pair domain as the high-gap and psi-reset queries. -/
theorem low_gap_rule {active : Active} (n k ell : Nat) (tail : List Nat)
    (cert : Certificate (3*n) (CollatzLowGapLoops.source k ell ++ tail))
    (activated : ∀ u, Certificate u tail → active u (3*u))
    (ih : Hyp active (grades 0 (CollatzLowGapLoops.source k ell ++ tail))) : Basin n := by
  obtain ⟨u,tailCert,decrease,merge⟩ :=
    CollatzLowGapLoops.whole_witness_rewrite n k ell tail cert
  have powered : PoweredCertificate u 0 tail := ⟨u,by simp,tailCert⟩
  exact one_query (activated u tailCert) powered decrease merge.mpr ih

/-- The explicit even-source reset consumes (P/2,P-1) and queries
(m,2m-1), sharing exactly the order used by high-gap reverse-tripling rules. -/
theorem even_reset_rule {active : Active} {l P w m e : Nat} {tail : List Nat}
    (guard : CollatzUnboundedGapReset.Guard l P w m) (high : 5 ≤ e)
    (cert : PoweredCertificate (P/2) e tail) (activated : active m (2*m-1))
    (ih : Hyp active (grades e tail)) : Basin (P-1) := by
  obtain ⟨childCert,decrease⟩ := CollatzUnboundedGapReset.complete_certificate_reset
    guard high cert
  exact one_query activated childCert decrease
    (CollatzUnboundedGapReset.target_basin_transfer guard).mp ih

/-- Any exact paired entrance, with arbitrary finite length and loop depth,
is a sound recursive rule in the same comparison program. -/
theorem compiled_reset_rule {active : Active} {sourceWord targetWord : List Nat}
    {l P w m e : Nat} {tail : List Nat}
    (pair : CollatzUnboundedGapReset.PairedEntrance sourceWord targetWord)
    (high : 3 ≤ e) (bound : ∀ a ∈ sourceWord, a ≤ e) (hm : 0 < m) (hw : 0 < w)
    (four : P % 4 = 0) (last : 2*P = 9*(3^l*w)+1)
    (entry : 3^sourceWord.length*m+correction sourceWord =
      2^total sourceWord*(2*(2^l*w)-1))
    (cert : PoweredCertificate (P/2) e tail) (activated : active m (2*m-1))
    (ih : Hyp active (grades e tail)) : Basin (P-1) := by
  obtain ⟨childCert,decrease,merge⟩ := CollatzUnboundedGapReset.compiled_certificate_reset
    pair high bound hm hw four last entry cert
  exact one_query activated childCert decrease merge.mp ih

end CollatzGapComparison
