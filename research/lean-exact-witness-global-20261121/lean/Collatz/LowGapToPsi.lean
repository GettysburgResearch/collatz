/-
The low-gap loop program needs no separate forward-tripling dispatcher.
One actual source step converts a forward-tripling query to the psi-forward
shape already mandatory in the common comparison kernel.
-/
import Collatz.GapComparison

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset

namespace CollatzLowGapToPsi

theorem basin_three : Basin 3 := by
  have cert : Certificate 3 [1,4] := ⟨by simp [PositiveGaps],by decide⟩
  exact witness_basin (certificate_witness cert)

/-- Consume the actual first source exponent. Its successor has initial even
run exactly a-1 and the identical complete source tail. For a >= 4 this supplies
the even-run threshold three used by the compiled reset rules. -/
theorem forward_gap_data (n a : Nat) (tail : List Nat)
    (cert : Certificate n (a::tail)) :
    PoweredCertificate (shortcut n) (a-1) tail ∧
      Less (grades (a-1) tail) (grades 0 (a::tail)) ∧
      3*n = 2*shortcut n-1 := by
  obtain ⟨ha,u,step,tailCert⟩ := (certificate_cons_iff n a tail).mp cert
  obtain ⟨e,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : a≠0)
  have equation : 3*n+1 = 2*(2^e*u) := by
    rw [Nat.pow_succ] at step
    grind
  have normal : shortcut n = 2^e*u := by
    unfold shortcut
    split <;> omega
  refine ⟨⟨u,?_,tailCert⟩,?_,?_⟩
  · simpa using normal
  · simpa using grades_odd_decrease e tail
  · rw [normal]
    omega

/-- Every odd forward-tripling query is a psi-forward query on a strictly
smaller complete source certificate. Source one is closed explicitly. -/
theorem forward_to_psi {active : CollatzGapComparison.Active} (n : Nat) (word : List Nat)
    (cert : Certificate n word)
    (activated : ∀ s, 0<s → active s (2*s-1))
    (ih : CollatzGapComparison.Hyp active (grades 0 word)) : Basin (3*n) := by
  by_cases one : n=1
  · simpa [one] using basin_three
  have odd : n%2=1 := witness_odd (certificate_witness cert)
  have powered : PoweredCertificate n 0 word := ⟨n,by simp,cert⟩
  obtain ⟨e,tail,child,decrease⟩ := ordinary_step powered one
  have equation : 2*shortcut n=3*n+1 := by
    unfold shortcut
    split <;> omega
  have positive : 0<shortcut n := by omega
  have target : 2*shortcut n-1=3*n := by omega
  have result := ih (shortcut n) (2*shortcut n-1) e tail
    (activated _ positive) child decrease
  rwa [target] at result

/-- The entire unbounded language (2^k,3,1^ell,4,tail) now calls only the
psi-forward comparison family. The low prefix and one further actual source
step are charged together to the same parent multiset; no output witness from
one query is reused as an unranked source for another query. -/
theorem low_loop_to_psi {active : CollatzGapComparison.Active}
    (n k ell : Nat) (tail : List Nat)
    (cert : Certificate (3*n) (CollatzLowGapLoops.source k ell ++ tail))
    (activated : ∀ s, 0<s → active s (2*s-1))
    (ih : CollatzGapComparison.Hyp active
      (grades 0 (CollatzLowGapLoops.source k ell ++ tail))) : Basin n := by
  obtain ⟨u,tailCert,drop,merge⟩ :=
    CollatzLowGapLoops.whole_witness_rewrite n k ell tail cert
  have lower : CollatzGapComparison.Hyp active (grades 0 tail) := by
    intro source target e gaps ha hc lt
    exact ih source target e gaps ha hc (less_trans lt drop)
  exact merge.mpr (forward_to_psi u tail tailCert activated lower)

end CollatzLowGapToPsi
