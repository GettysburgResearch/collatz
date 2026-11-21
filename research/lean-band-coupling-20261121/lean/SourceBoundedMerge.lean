module

public import SectionDynamics

@[expose] public section

/-!
# The source bound needed to close a forced-section merger argument

The smaller partner must be below the original ordinary source `n`. A bound
below only the visited marked value does not supply the induction hypothesis
when that marked value exceeds `n`.
-/

namespace CollatzShell.ForwardSection

/-- A physical merger transfers convergence back through any actual forced
    endpoint. This does not require the endpoint itself to be marked. -/
theorem basin_of_merger_at_hit {n q x a b : Nat}
    (visit : Hits n q) (known : Basin x)
    (merge : orbit a x=orbit b q) : Basin n := by
  have bx : Basin (orbit a x) :=
    (basin_at_hit (show Hits x (orbit a x) from ⟨a,rfl⟩)).mp known
  have bq : Basin q :=
    (basin_at_hit (show Hits q (orbit b q) from ⟨b,rfl⟩)).mpr (merge ▸ bx)
  exact (basin_at_hit visit).mpr bq

/-- The induction transfer at a forced marked endpoint, stated more generally
    for any orbit endpoint: the witness is bounded by the source `n`, not by
    the endpoint `q`. -/
theorem basin_of_source_bounded_merger_at_hit {n q x a b : Nat}
    (visit : Hits n q) (positive : 0<x) (smaller : x<n)
    (merge : orbit a x=orbit b q)
    (previous : ∀ y, 0<y → y<n → Basin y) : Basin n :=
  basin_of_merger_at_hit visit (previous x positive smaller) merge

/-- Coverage at the forced first marked visit, retaining the original source
    in the strict size bound for the partner. -/
def SourceBoundedSectionMerge : Prop :=
  ∀ n, 1<n → ∃ x, 0<x ∧ x<n ∧
    ∃ a b, orbit a x=orbit b (orbit (firstVisit n) n)

/-- The corrected global closure criterion. This equivalence does not prove
    that the required source-bounded merger witnesses always exist. -/
theorem collatz_iff_source_bounded_section_merge :
    Universal ↔ SourceBoundedSectionMerge := by
  constructor
  · intro all n hn
    have mark := firstVisit_spec n (by omega : 0<n)
    have qp : 0<orbit (firstVisit n) n := by have := mark.1; omega
    obtain ⟨t,hit⟩ := all _ qp
    exact ⟨1,by omega,hn,0,t,hit.symm⟩
  · intro cover n hn
    induction n using Nat.strong_induction_on with
    | h n ih =>
      by_cases large : 1<n
      · obtain ⟨x,xp,xn,a,b,merge⟩ := cover n large
        exact basin_of_source_bounded_merger_at_hit
          (show Hits n (orbit (firstVisit n) n) from ⟨firstVisit n,rfl⟩)
          xp xn merge (fun y yp yn => ih y yn yp)
      · have one : n=1 := by omega
        exact ⟨0,one⟩

#print axioms basin_of_merger_at_hit
#print axioms basin_of_source_bounded_merger_at_hit
#print axioms collatz_iff_source_bounded_section_merge

end CollatzShell.ForwardSection
